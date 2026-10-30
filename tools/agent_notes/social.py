"""Collect candidate social-media posts about result families (Bluesky, Mathstodon, X via Grok).

    python3 tools/agent_notes/social.py --out social.json [--families 102 025 ...]
                                        [--sources bluesky,mastodon,x] [--max-x-posts 2000]
                                        [--x-since YYYY-MM-DD] [--x-focus TEXT ...] [--x-handles a,b]

Credentials come from the environment or ~/.config/oai-math-revised/secrets.env
(XAI_API_KEY, BLUESKY_HANDLE, BLUESKY_APP_PASSWORD, MASTODON_TOKEN); sources
without credentials are skipped. Output has the same shape as prepass.py
(folder -> list of {source, title, url, context}); every candidate is attached to
all papers of its family and still has to be checked by an agent.

X search is billed per post fetched (xAI: $5 per 1,000 posts plus tokens);
--max-x-posts stops the X part once that many posts have been fetched, and
--max-x-usd once that much has been spent, counting earlier runs with the same --out.
With --x-focus, each family gets one search per focus instead of one general search.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "site"))
from catalog import load  # noqa: E402

SECRETS = Path.home() / ".config" / "oai-math-revised" / "secrets.env"
SINCE = "2026-10-05"
XAI_MODEL = os.environ.get("XAI_MODEL", "grok-4.7")


def secrets() -> dict[str, str]:
    out = {}
    if SECRETS.exists():
        for line in SECRETS.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip()
    out.update({k: v for k, v in os.environ.items() if k in ("XAI_API_KEY", "BLUESKY_HANDLE", "BLUESKY_APP_PASSWORD", "MASTODON_TOKEN")})
    return {k: v for k, v in out.items() if v}


def http(url: str, data: dict | None = None, headers: dict | None = None, timeout: int = 120) -> dict:
    body = json.dumps(data).encode() if data is not None else None
    h = {"User-Agent": "oai-math-revised (github.com/mathcommunity/oai-math-revised)", **(headers or {})}
    if body is not None:
        h["Content-Type"] = "application/json"
    with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=h), timeout=timeout) as r:
        return json.loads(r.read())


def plain(text: str) -> str:
    text = re.sub(r"<[^>]+>|\$[^$]*\$", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# --- Bluesky ------------------------------------------------------------------

def bluesky_session(sec: dict) -> str:
    r = http("https://bsky.social/xrpc/com.atproto.server.createSession",
             {"identifier": sec["BLUESKY_HANDLE"], "password": sec["BLUESKY_APP_PASSWORD"]})
    return r["accessJwt"]


def bluesky(query: str, token: str) -> list[dict]:
    q = urllib.parse.urlencode({"q": query, "since": f"{SINCE}T00:00:00Z", "limit": 25, "sort": "top"})
    r = http(f"https://bsky.social/xrpc/app.bsky.feed.searchPosts?{q}", headers={"Authorization": f"Bearer {token}"})
    out = []
    for p in r.get("posts", []):
        rkey = p["uri"].rsplit("/", 1)[-1]
        handle = p["author"]["handle"]
        out.append({"source": "Bluesky", "title": f"@{handle}, {(p.get('record', {}).get('createdAt') or p.get('indexedAt', ''))[:10]}",
                    "url": f"https://bsky.app/profile/{handle}/post/{rkey}",
                    "context": post_text(p.get("record", {}).get("text", ""))[:500]})
    return out


# --- Mathstodon ----------------------------------------------------------------

def mastodon(query: str, token: str) -> list[dict]:
    q = urllib.parse.urlencode({"q": query, "type": "statuses", "limit": 20})
    r = http(f"https://mathstodon.xyz/api/v2/search?{q}", headers={"Authorization": f"Bearer {token}"})
    return [{"source": "Mathstodon", "title": f"@{s['account']['acct']}, {s['created_at'][:10]}",
             "url": s["url"], "context": post_text(s.get("content", ""))[:500]}
            for s in r.get("statuses", []) if s.get("created_at", "") >= SINCE]


# --- X via Grok -----------------------------------------------------------------

X_PROMPT = """Search X for posts since {since} that discuss this specific result from the OpenAI math release (github.com/openai/math, October 2026):

Result family {num}: {title}
Summary: {summary}
Papers: {papers}

{focus}Only include posts that are specifically about this result (not about the release in general), preferably by mathematicians or other people commenting with expertise. Return ONLY a JSON array (no prose), at most 10 entries, each
{{"url": "https://x.com/<handle>/status/<id>", "author": "<display name> (@handle)", "date": "YYYY-MM-DD", "summary": "<one neutral sentence on what the post says about the result>"}}
Return [] if there are none."""


def x_search(fam, papers, key: str, since: str = SINCE, focus: str = "", handles: list[str] | None = None) -> tuple[list[dict], dict]:
    prompt = X_PROMPT.format(since=since, num=fam.num, title=plain(fam.title), summary=plain(fam.summary)[:800],
                             papers="; ".join(plain(papers[s].title) for s in fam.papers),
                             focus=f"Look specifically for: {focus}\n\n" if focus else "")
    tool = {"type": "x_search", "from_date": since}
    if handles:
        tool["allowed_x_handles"] = handles
    r = http("https://api.x.ai/v1/responses",
             {"model": XAI_MODEL, "input": [{"role": "user", "content": prompt}],
              "tools": [tool]},
             headers={"Authorization": f"Bearer {key}"}, timeout=300)
    texts = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("type") == "output_text" and isinstance(o.get("text"), str):
                texts.append(o["text"])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(r.get("output", []))
    text = "\n".join(texts)
    m = re.search(r"\[.*\]", text, flags=re.S)
    items = []
    try:
        items = json.loads(m.group(0)) if m else []
    except json.JSONDecodeError:
        pass
    out = []
    for it in items if isinstance(items, list) else []:
        url = str(it.get("url", ""))
        if re.fullmatch(r"https://(x|twitter)\.com/[A-Za-z0-9_]+/status/\d+", url):
            out.append({"source": "X (via Grok search)", "title": f"{it.get('author', '')}, {it.get('date', '')}",
                        "url": url.replace("twitter.com", "x.com"), "context": str(it.get("summary", ""))[:400]})
    return out, r.get("usage", {})


def post_text(html_fragment: str) -> str:
    """Post text from HTML: drop tags, decode entities, keep $...$ math."""
    import html as _html
    text = re.sub(r"<br\s*/?>", " ", html_fragment)
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", "", text))).strip()


def oembed_text(url: str) -> str | None:
    """Text of a public X post via publish.twitter.com/oembed, or None if it does not exist."""
    try:
        r = http("https://publish.twitter.com/oembed?" + urllib.parse.urlencode({"url": url, "omit_script": 1}), timeout=30)
    except Exception:
        return None
    m = re.search(r"<p[^>]*>(.*?)</p>", r.get("html", ""), flags=re.S)
    return post_text(m.group(1)) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--families", nargs="*")
    ap.add_argument("--sources", default="bluesky,mastodon,x")
    ap.add_argument("--max-x-posts", type=int, default=2000)
    ap.add_argument("--max-x-usd", type=float, default=10.0, help="stop X searches once xAI reports this much spent")
    ap.add_argument("--x-since", default=SINCE, help="only posts from this date on (X is billed per post fetched)")
    ap.add_argument("--x-focus", nargs="*", default=[""], help="one X search per family for each of these angles")
    ap.add_argument("--x-handles", help="comma-separated: only posts by these accounts (at most 10)")
    args = ap.parse_args()
    sec = secrets()
    _, families, papers = load(ROOT)
    nums = [f.zfill(3) for f in args.families] if args.families else sorted(families)
    sources = set(args.sources.split(","))
    out_path = Path(args.out)
    result: dict[str, list] = json.loads(out_path.read_text()) if out_path.exists() else {}
    usage_log = out_path.with_suffix(".usage.jsonl")

    bsky_token = None
    if "bluesky" in sources and {"BLUESKY_HANDLE", "BLUESKY_APP_PASSWORD"} <= sec.keys():
        bsky_token = bluesky_session(sec)
    elif "bluesky" in sources:
        print("bluesky: no credentials, skipped", file=sys.stderr)
    if "mastodon" in sources and "MASTODON_TOKEN" not in sec:
        print("mastodon: no token, skipped", file=sys.stderr)
    if "x" in sources and "XAI_API_KEY" not in sec:
        print("x: no XAI_API_KEY, skipped", file=sys.stderr)

    x_posts, x_usd = 0, 0.0
    if usage_log.exists():
        for line in usage_log.read_text().splitlines():
            usage = json.loads(line)["usage"]
            x_posts += usage.get("server_side_tool_usage_details", {}).get("x_posts_fetched", 0)
            x_usd += usage.get("cost_in_usd_ticks", 0) / 1e10
    handles = args.x_handles.split(",") if args.x_handles else None
    for num in nums:
        fam = families[num]
        query = plain(fam.title)
        found: list[dict] = []
        try:
            if bsky_token:
                found += bluesky(query, bsky_token)
            if "mastodon" in sources and "MASTODON_TOKEN" in sec:
                found += mastodon(query, sec["MASTODON_TOKEN"])
            for focus in args.x_focus if "x" in sources and "XAI_API_KEY" in sec else []:
                if x_posts >= args.max_x_posts or x_usd >= args.max_x_usd:
                    break
                items, usage = x_search(fam, papers, sec["XAI_API_KEY"], args.x_since, focus, handles)
                fetched = usage.get("server_side_tool_usage_details", {}).get("x_posts_fetched", 0)
                x_posts += fetched
                x_usd += usage.get("cost_in_usd_ticks", 0) / 1e10  # xAI reports cost in 1e-10 USD ticks
                for c in items:  # verify existence and get the post's own text from X's oEmbed endpoint
                    text = oembed_text(c["url"])
                    if text is not None:
                        c["context"] = f"Post text: {text} | Grok's summary: {c['context']}"
                        found.append(c)
                with open(usage_log, "a") as f:
                    f.write(json.dumps({"family": num, "focus": focus, "x_items": len(items), "usage": usage}) + "\n")
        except Exception as e:  # keep going; report per family
            print(f"{num}: {type(e).__name__}: {e}", file=sys.stderr)
        for s in fam.papers:
            have = {c["url"] for c in result.get(s, [])}
            result.setdefault(s, []).extend(c for c in found if c["url"] not in have)
        out_path.write_text(json.dumps(result, indent=1, ensure_ascii=False))
        print(f"{num}: {len(found)} candidates ({', '.join(sorted({c['source'] for c in found})) or '-'})"
              f"; X so far: {x_posts} posts, ${x_usd:.2f}", file=sys.stderr)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
