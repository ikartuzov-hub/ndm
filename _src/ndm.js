/* nDm page engine: language, theme, share, common renderers. Expects a global T = {pt:{…}, …}. */
window.NDM = (function(){
  var ORDER = ["pt","en","ru","de","es"];
  var LNAMES = { pt:"Português", en:"English", ru:"Русский", de:"Deutsch", es:"Español" };
  var TAGS = { pt:"pt-PT", en:"en", ru:"ru", de:"de", es:"es" };
  var SSMURL = "https://www.ssm.gov.pt/";
  var LANGS = [], lang, pageRender;

  function pickLang(){
    if (window.NDM_LANG && LANGS.indexOf(window.NDM_LANG) >= 0) return window.NDM_LANG;
    var q = new URLSearchParams(location.search).get('lang');
    if (LANGS.indexOf(q) >= 0) return q;
    var st = null;
    try { st = localStorage.getItem('ndm-lang'); } catch(e){}
    if (LANGS.indexOf(st) >= 0) return st;
    var nav = (navigator.language || '').slice(0, 2).toLowerCase();
    if (LANGS.indexOf(nav) >= 0) return nav;
    return LANGS.indexOf('pt') >= 0 ? 'pt' : LANGS[0];
  }

  var P = function(s){ return '<span class="pt">' + s + '</span>'; };

  function warnBlock(w){
    if (!w) return '';
    var h = '<h4>' + w.h + '</h4><p>' + w.p + '</p>';
    if (w.p2) h += '<p>' + w.p2 + '</p>';
    return h;
  }
  /* текст подписи → безопасное значение атрибута alt */
  function attr(s){
    return String(s == null ? '' : s)
      .replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim()
      .replace(/&/g, '&amp;').replace(/"/g, '&quot;');
  }
  function figs(list){
    if (!list || !list.length) return '';
    return list.map(function(f){
      // подпись идёт и в alt: это экраны портала, а не украшение —
      // без описания их не понимают ни краулер, ни ИИ-сети, ни экранный диктор
      return '<figure><img src="' + f.src + '" alt="' + attr(f.cap) + '" loading="lazy"><figcaption>' + f.cap + '</figcaption></figure>';
    }).join('');
  }
  function marks(list){
    if (!list || !list.length) return '';
    return '<ul class="fields">' + list.map(function(f, j){
      return '<li><span class="mk">' + (j + 1) + '</span><span>' + f + '</span></li>';
    }).join('') + '</ul>';
  }
  function actBlock(t){
    return '<div class="act">' +
      '<p class="url">ssm.gov.pt</p>' +
      '<div class="row">' +
        '<a class="btn btn-go" id="openSsm" href="' + SSMURL + '" target="_blank" rel="noopener">' + t.openBtn + '</a>' +
        '<button class="btn btn-copy" id="copySsm" type="button"><span>' + t.copyBtn + '</span></button>' +
      '</div>' +
      '<p class="hint">' + t.openHint + '</p>' +
    '</div>';
  }
  function langPath(L){
    var parts = location.pathname.split('/').filter(Boolean);
    if (parts.length && ORDER.indexOf(parts[parts.length - 1]) >= 0) parts.pop();
    if (L !== 'pt') parts.push(L);
    return '/' + (parts.length ? parts.join('/') + '/' : '');
  }

  function withLang(href){
    try {
      var u = new URL(href, location.href);
      if (window.NDM_LANG){
        // языковые адреса: /subsidio/ru/ вместо /subsidio/?lang=ru
        var parts = u.pathname.split('/').filter(Boolean);
        if (parts.length && ORDER.indexOf(parts[parts.length - 1]) >= 0) parts.pop();
        if (lang !== 'pt') parts.push(lang);
        return '/' + (parts.length ? parts.join('/') + '/' : '') + u.hash;
      }
      u.searchParams.set('lang', lang);
      return u.pathname + u.search + u.hash;
    } catch(e){ return href; }
  }

  /* Заголовок вкладки и описание — на языке страницы.
     Пререндер снимает DOM ПОСЛЕ рендера, поэтому языковые адреса уезжают
     в поиск и в карточку мессенджера уже с переведёнными метатегами.
     До этого на всех 32 непортугальских адресах висел португальский title. */
  function strip(s){ return String(s == null ? '' : s).replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim(); }
  function clip(s, n){
    s = strip(s);
    if (s.length <= n) return s;
    var c = s.slice(0, n), i = c.lastIndexOf(' ');
    return (i > 60 ? c.slice(0, i) : c).replace(/[ ,;:.\u2013\u2014-]+$/, '') + '\u2026';
  }
  function meta(sel, val){
    var e = document.querySelector(sel);
    if (e && val) e.setAttribute('content', val);
  }
  function setMeta(t){
    var title = t.shareTitle || (t.h1 ? strip(t.h1).replace(/[.\s]+$/, '') + ' \u2014 nDm' : '');
    var desc = clip(t.lead || '', 165);
    if (title){ document.title = title; meta('meta[property="og:title"]', title); }
    if (desc){ meta('meta[name="description"]', desc); meta('meta[property="og:description"]', desc); }
  }

  function render(){
    var t = T[lang];
    document.documentElement.lang = TAGS[lang];

    var lb = document.getElementById('lang');
    if (lb){
      lb.textContent = lang.toUpperCase();
      lb.parentNode.style.display = LANGS.length > 1 ? '' : 'none';
      document.getElementById('langmenu').innerHTML = LANGS.map(function(L){
        return '<button type="button" data-l="' + L + '"' + (L === lang ? ' aria-current="true"' : '') + '>' +
               '<span>' + LNAMES[L] + '</span><span class="code">' + L.toUpperCase() + '</span></button>';
      }).join('');
    }

    var nodes = document.querySelectorAll('[data-t]');
    for (var i = 0; i < nodes.length; i++){
      var k = nodes[i].getAttribute('data-t');
      if (typeof t[k] === 'string') nodes[i].innerHTML = t[k];
    }
    setMeta(t);

    // страховка для картинок, размеченных прямо в теле страницы
    var figs2 = document.querySelectorAll('figure img');
    for (var q = 0; q < figs2.length; q++){
      if (figs2[q].getAttribute('alt')) continue;
      var cap = figs2[q].parentNode.querySelector('figcaption');
      if (cap && cap.textContent.trim()) figs2[q].setAttribute('alt', cap.textContent.trim());
    }

    var hub = document.getElementById('hubLink');
    if (hub) hub.href = 'https://seedwave.pt/hub/?lang=' + lang;

    if (pageRender) pageRender(t, lang);

    // every internal link carries the current language
    var links = document.querySelectorAll('a[data-ll]');
    for (var j = 0; j < links.length; j++) links[j].href = withLang(links[j].getAttribute('data-ll'));
    var inl = document.querySelectorAll('a[href^="/"], a[href^="../"], a[href^="./"], a[href^="#"]');
    for (var m = 0; m < inl.length; m++){
      var a = inl[m], h = a.getAttribute('href');
      if (h.charAt(0) === '#' || a.hasAttribute('data-ll') || /[?&]lang=/.test(h)) continue;
      a.href = withLang(h);
    }

    var go = document.getElementById('openSsm');
    if (go) go.addEventListener('click', function(e){
      if (window.innerWidth < 900) return;
      var w = Math.max(560, Math.round(screen.availWidth / 2));
      var f = 'noopener,noreferrer,width=' + w + ',height=' + screen.availHeight +
              ',left=' + (screen.availLeft + screen.availWidth - w) + ',top=' + screen.availTop;
      var win = window.open(SSMURL, 'ssmportal', f);
      if (win) e.preventDefault();
    });
    var cp = document.getElementById('copySsm');
    if (cp) cp.addEventListener('click', function(){
      var span = cp.querySelector('span'), old = span.textContent;
      var done = function(){ span.textContent = t.copiedLink; setTimeout(function(){ span.textContent = old; }, 2200); };
      if (navigator.clipboard) navigator.clipboard.writeText(SSMURL).then(done, done); else done();
    });
  }

  function init(fn){
    pageRender = fn;
    LANGS = ORDER.filter(function(l){ return window.T && T[l]; });
    lang = pickLang();
    var yr = document.getElementById('yr');
    if (yr) yr.textContent = new Date().getFullYear();
    render();

    var lbtn = document.getElementById('lang'), lmenu = document.getElementById('langmenu');
    if (lbtn){
      var closeMenu = function(){ lmenu.hidden = true; lbtn.setAttribute('aria-expanded', 'false'); };
      lbtn.addEventListener('click', function(e){
        e.stopPropagation();
        var open = lmenu.hidden;
        lmenu.hidden = !open;
        lbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      lmenu.addEventListener('click', function(e){
        var b = e.target.closest('button[data-l]');
        if (!b) return;
        lang = b.getAttribute('data-l');
        try { localStorage.setItem('ndm-lang', lang); } catch(err){}
        if (window.NDM_LANG){ location.href = langPath(lang); return; }
        closeMenu(); render();
        try { var u = new URL(location.href); u.searchParams.set('lang', lang); history.replaceState(null, '', u); } catch(err){}
      });
      document.addEventListener('click', closeMenu);
      document.addEventListener('keydown', function(e){ if (e.key === 'Escape') closeMenu(); });
    }

    var root = document.documentElement, tb = document.getElementById('theme');
    if (tb){
      var stored = null;
      try { stored = localStorage.getItem('ndm-theme'); } catch(e){}
      if (stored) root.setAttribute('data-theme', stored);
      var isDark = function(){
        var a = root.getAttribute('data-theme');
        if (a) return a === 'dark';
        return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      };
      var paint = function(){ tb.textContent = isDark() ? '☀' : '☾'; };
      paint();
      tb.addEventListener('click', function(){
        var next = isDark() ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try { localStorage.setItem('ndm-theme', next); } catch(e){}
        paint();
      });
    }

    var rows = Array.prototype.slice.call(document.querySelectorAll('#calc .cr'));
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (rows.length && !reduce){
      var k = 0;
      rows[0].classList.add('on');
      setInterval(function(){
        rows = Array.prototype.slice.call(document.querySelectorAll('#calc .cr'));
        if (!rows.length) return;
        rows.forEach(function(r){ r.classList.remove('on'); });
        k = (k + 1) % rows.length;
        rows[k].classList.add('on');
      }, 1500);
    }

    var sb = document.getElementById('share');
    if (sb) sb.addEventListener('click', function(){
      var t = T[lang], url = withLang(location.pathname);
      url = location.origin + url;
      if (navigator.share){ navigator.share({ title: t.shareTitle || document.title, text: t.shareText, url: url }).catch(function(){}); return; }
      var done = function(){
        var span = sb.querySelector('span'), old = span.textContent;
        span.textContent = t.copied;
        setTimeout(function(){ span.textContent = old; }, 2200);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(t.shareText + ' ' + url).then(done, done); else done();
    });
  }

  return { init: init, P: P, lang: function(){ return lang; }, warn: warnBlock, figs: figs, marks: marks, act: actBlock };
})();
