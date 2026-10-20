// Math rendering, copy buttons, and search/filters on the browse page.
(function () {
  function renderMath(el) {
    if (window.renderMathInElement) {
      renderMathInElement(el, {
        delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }],
        throwOnError: false,
        ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"],
      });
    }
  }

  function norm(s) {
    return s.normalize("NFKD").replace(/[̀-ͯ]/g, "").replace(/\\[a-zA-Z]+|[${}^_\\]/g, " ")
      .replace(/--/g, "-").toLowerCase();
  }

  function setupCopy() {
    document.querySelectorAll(".cite .copy").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var text = btn.parentElement.querySelector("code").textContent;
        navigator.clipboard.writeText(text).then(function () {
          btn.textContent = "Copied";
          setTimeout(function () { btn.textContent = "Copy BibTeX"; }, 2000);
        });
      });
    });
  }

  // Open the <details> containing the element named in the URL hash.
  function openHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    var el = id && document.getElementById(id);
    if (!el) return;
    for (var d = el; d; d = d.parentElement) if (d.tagName === "DETAILS") d.open = true;
    el.scrollIntoView();
  }

  function setupBrowse() {
    var q = document.getElementById("q");
    if (!q) return;
    var browse = document.getElementById("browse");
    var fd = document.getElementById("fd"), fn = document.getElementById("fn");
    var fl = document.getElementById("fl"), fo = document.getElementById("fo");
    var count = document.getElementById("count"), empty = document.getElementById("empty");
    var clearwrap = document.getElementById("clearwrap");
    var discs = Array.prototype.slice.call(browse.querySelectorAll(".disc"));
    var items = Array.prototype.slice.call(browse.querySelectorAll("li[data-slug]"));
    var defaultCount = count.textContent;
    var index = null, loading = null, wasActive = false;

    if (window.matchMedia("(max-width: 699px)").matches) document.getElementById("filters").open = false;

    function link(id, fn) {
      document.getElementById(id).addEventListener("click", function (e) { e.preventDefault(); fn(); });
    }
    link("expand", function () { discs.forEach(function (d) { if (!d.hidden) d.open = true; }); });
    link("collapse", function () { discs.forEach(function (d) { d.open = false; }); });
    link("clear", function () {
      q.value = ""; fd.value = ""; fn.checked = fl.checked = false; update();
    });

    function matches(p, terms) {
      if (fd.value && p.d !== fd.value) return false;
      if (fn.checked && !p.n) return false;
      if (fl.checked && !p.l) return false;
      return terms.every(function (t) {
        if (/^\d{1,3}$/.test(t) && p.f === ("00" + t).slice(-3)) return true;
        return p.hay.indexOf(t) >= 0;
      });
    }

    function update() {
      var terms = norm(q.value).split(/\s+/).filter(Boolean);
      var active = terms.length > 0 || !!fd.value || fn.checked || fl.checked;
      clearwrap.hidden = !active;
      if (active && !index) {
        count.textContent = "Loading…";
        if (!loading) {
          loading = fetch("assets/index.json").then(function (r) {
            if (!r.ok) throw new Error(r.status);
            return r.json();
          }).then(function (data) {
            index = {};
            data.forEach(function (p) { p.hay = [p.t, p.ft, p.s.toLowerCase(), p.f, p.x].join(" "); index[p.s] = p; });
            update();
          }).catch(function () {
            loading = null;
            count.textContent = "Search is unavailable right now. Reload the page to try again.";
          });
        }
        return;
      }
      var nPapers = 0, fams = {};
      items.forEach(function (li) {
        var p = index && index[li.dataset.slug];
        var earlier = li.classList.contains("earlier");
        var show = (!earlier || fo.checked) && (!active || (p && matches(p, terms)));
        li.hidden = !show;
        if (show) {
          if (!earlier) nPapers++;
          var fam = li.closest(".fam");
          if (fam) fams[fam.id] = true;
        }
      });
      browse.querySelectorAll(".fam").forEach(function (f) { f.hidden = !fams[f.id]; });
      discs.forEach(function (d) {
        var any = !!d.querySelector(".fam:not([hidden])");
        d.hidden = !any;
        if (active) d.open = any;
        else if (wasActive) d.open = false;
      });
      var wd = document.getElementById("withdrawn");
      wd.hidden = !wd.querySelector("li:not([hidden])");
      var nFams = Object.keys(fams).length;
      if (!active) {
        count.textContent = defaultCount;
      } else {
        count.textContent = nFams + (nFams === 1 ? " family, " : " families, ") + nPapers + (nPapers === 1 ? " manuscript matches" : " manuscripts match");
      }
      var none = active && !browse.querySelector("li[data-slug]:not([hidden])");
      empty.hidden = !none;
      if (none) {
        empty.textContent = terms.length ? 'Nothing matches "' + q.value.trim() + '". Try fewer or different words, or clear the filters.'
          : "Nothing matches these filters.";
      }
      wasActive = active;
    }

    var timer;
    q.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(update, 150); });
    [fd, fn, fl, fo].forEach(function (el) { el.addEventListener("change", update); });
    if (q.value || fd.value || fn.checked || fl.checked || fo.checked) update();  // restored form state
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderMath(document.body);
    setupCopy();
    setupBrowse();
    openHash();
    window.addEventListener("hashchange", openHash);
  });
})();
