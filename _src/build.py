# -*- coding: utf-8 -*-
"""Собирает готовые к заливке страницы репозитория ndm из исходников.

Запуск из корня репозитория:  python3 _src/build.py
"""
import io, os, re, glob

SITE = "https://ajuda.seedwave.pt"
PAGES = []   # (url, приоритет) — наполняется по ходу сборки
LANG_ORDER = ["pt", "en", "ru", "de", "es"]

HEAD = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{root}icon.svg?v=1" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}manifest.webmanifest">
<meta name="apple-mobile-web-app-title" content="{app}">
<meta name="theme-color" content="#FAF6F1">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
{alts}
<style>html{{color-scheme:light dark}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
FOOT = "\n</body>\n</html>\n"

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bitter:wght@500;600;700&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
"""

MARK = """<svg viewBox="0 0 100 100" fill="none" stroke="var(--accent)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M33 18 L33 70"/>
        <path d="M33 18 C68 18 78 30 78 44 C78 58 68 70 33 70"/>
        <path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/>
      </svg>"""

# шапка страниц выпуска 2: брендмарк ведёт на «Damos o Caminho» (корень домена)
BAR = """<div class="bar">
    <a class="brand" href="/" rel="noopener">
      %s
      <b>nDm</b>
    </a>
    <div class="ctrls">
      <div class="lang-wrap">
        <button class="rb" id="lang" type="button" aria-haspopup="true" aria-expanded="false" aria-label="Idioma">PT</button>
        <div class="menu" id="langmenu" hidden></div>
      </div>
      <button class="rb" id="theme" type="button" aria-label="Tema">☾</button>
    </div>
  </div>
  <p class="crumbs">{crumbs}</p>""" % MARK

FOOTER = """<footer>
    © <span id="yr"></span> <a id="hubLink" href="https://seedwave.pt/hub/" target="_blank" rel="noopener">SeedWave</a>
    · <a href="https://www.linkedin.com/in/igor-kartuzov" target="_blank" rel="noopener">Igor Kartuzov</a>
  </footer>"""


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    io.open(p, "w", encoding="utf-8").write(s)


def alts(url):
    """hreflang-альтернативы: та же страница с ?lang= для каждого языка."""
    rows = ['<link rel="alternate" hreflang="%s" href="%s?lang=%s">' % (
        'pt-PT' if L == 'pt' else L, url, L) for L in LANG_ORDER]
    rows.append('<link rel="alternate" hreflang="x-default" href="%s">' % url)
    return "\n".join(rows)


def wrap(body, **kw):
    kw.setdefault("alts", alts(kw["url"]))
    return HEAD.format(**kw) + body.strip() + FOOT


def i18n(name):
    """Склеивает _src/i18n/<name>.<lang>.js в порядке PT · EN · RU · DE · ES."""
    parts = []
    for L in LANG_ORDER:
        p = "_src/i18n/%s.%s.js" % (name, L)
        if os.path.exists(p):
            parts.append(read(p).strip())
    return "var T = {}; var P = NDM.P;\n" + "\n".join(parts)


def page(body_file, name, out, crumbs, **meta):
    body = read(body_file)
    body = body.replace("{{BAR}}", BAR.format(crumbs=crumbs)).replace("{{FOOTER}}", FOOTER)
    head = FONTS + "<style>\n" + read("_src/ndm.css").strip() + "\n</style>\n"
    scripts = ("<script>\n" + read("_src/ndm.js").strip() + "\n</script>\n" +
               "<script>\n" + i18n(name) + "\n</script>\n")
    # тело страницы: разметка, затем движок + тексты, затем её собственный <script>
    idx = body.rfind("<script>")
    body = body[:idx] + scripts + body[idx:]
    write(out, wrap(head + body, **meta))
    PAGES.append(meta["url"])
    print("built:", out)


# ---------- / — «Damos o Caminho» --------------------------------------
root = read("_src/root-body.html")
root = re.sub(r"^<title>.*?</title>\s*", "", root, count=1, flags=re.S)
DESC_ROOT = ("Subsídio de Mobilidade: tem direito? Três perguntas, o guia passo a passo e o que mudou "
             "na lei. Gratuito, em cinco línguas. nDm — Nova Dádiva da Madeira.")
write("index.html", wrap(root, lang="pt", title="Damos o Caminho — nDm", desc=DESC_ROOT,
      app="nDm", root="", ogtitle="Subsídio de Mobilidade — Damos o Caminho",
      og=SITE + "/og-image.png", url=SITE + "/"))
PAGES.append(SITE + "/")
print("built: index.html")

# ---------- /tap/ — выпуск 1 --------------------------------------------
tap = read("_src/tap-body.html")
tap = re.sub(r"^<title>.*?</title>\s*", "", tap, count=1, flags=re.S)
tap = tap.replace('<a class="brand" href="https://seedwave.pt/hub/">', '<a class="brand" href="../">')
DESC_TAP = ("Como pedir à TAP a fatura e o comprovativo de viagem para o subsídio de "
            "mobilidade — passo a passo, com imagens. PT · EN · RU · DE · ES.")
write("tap/index.html", wrap(tap, lang="pt", title="Documentos TAP — nDm", desc=DESC_TAP,
      app="Documentos TAP", root="../", ogtitle="Documentos TAP — Damos o caminho",
      og=SITE + "/tap/og-image.png", url=SITE + "/tap/"))
PAGES.append(SITE + "/tap/")
print("built: tap/index.html")

# ---------- /subsidio/ — выпуск 2: подача + три справочных -------------
OG2 = SITE + "/subsidio/og-image.png"
CR = '<a href="/">Damos o Caminho</a><span>›</span>'
page("_src/subsidio-body.html", "subsidio", "subsidio/index.html",
     CR + "Subsídio de Mobilidade",
     lang="pt", title="Subsídio de Mobilidade: o pedido em cinco passos — nDm",
     desc="Cada ecrã do portal ssm.gov.pt e cada campo, com imagens reais e a fatura da TAP ao lado. Onde as pessoas perdem dinheiro. PT · EN · RU · DE · ES.",
     app="Subsídio", root="../", ogtitle="O pedido em cinco passos — Damos o Caminho",
     og=OG2, url=SITE + "/subsidio/")

page("_src/ref-body.html", "dinheiro", "subsidio/dinheiro/index.html",
     CR + '<a href="../">Subsídio</a><span>›</span>Quanto e porquê',
     lang="pt", title="Quanto dinheiro e por quê — nDm",
     desc="O que o Subsídio de Mobilidade devolve e o que não devolve: tarifa, taxas, copagamento, desconto e o tecto que já não existe.",
     app="Subsídio", root="../../", ogtitle="Quanto dinheiro e por quê — Damos o Caminho",
     og=OG2, url=SITE + "/subsidio/dinheiro/")

page("_src/ref-body.html", "rejeitado", "subsidio/rejeitado/index.html",
     CR + '<a href="../">Subsídio</a><span>›</span>Rejeitado',
     lang="pt", title="Primeiro acesso: «Rejeitado» não é recusa — nDm",
     desc="Porque é que o portal ssm.gov.pt marca «Rejeitado» logo no registo, o que fazer, e o que existe na área pessoal.",
     app="Subsídio", root="../../", ogtitle="«Rejeitado» não é recusa — Damos o Caminho",
     og=OG2, url=SITE + "/subsidio/rejeitado/")

page("_src/ref-body.html", "familia", "subsidio/familia/index.html",
     CR + '<a href="../">Subsídio</a><span>›</span>Família',
     lang="pt", title="Família e ajudar outra pessoa — nDm",
     desc="Como acrescentar cônjuge e filhos ao Subsídio de Mobilidade — e a regra número um se está a tratar do pedido por outra pessoa.",
     app="Subsídio", root="../../", ogtitle="Família e ajudar outra pessoa — Damos o Caminho",
     og=OG2, url=SITE + "/subsidio/familia/")


# ---------- /cartao/ — выпуск 3: Cartão de Residente na RAM --------------
# У страницы свой движок и свои стили внутри тела; от общего контура ей нужны
# только шапка с метатегами и пререндер. Тексты — в _src/i18n/cartao.<язык>.js.
cartao = read("_src/cartao-body.html")
cartao = cartao.replace("{{I18N}}", "\n".join(
    read("_src/i18n/cartao.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/cartao.%s.js" % L)))
DESC_CARTAO = ("Como pedir o Cart\u00e3o de Residente na RAM no portal SIMplifica \u2014 ecr\u00e3 a ecr\u00e3, "
               "com imagens de um pedido real. Trilhos a 0 \u20ac e subs\u00eddio do Porto Santo. "
               "PT \u00b7 EN \u00b7 RU \u00b7 DE \u00b7 ES.")
write("cartao/index.html", wrap(FONTS + cartao, lang="pt",
      title="Cart\u00e3o de Residente na RAM: o pedido ecr\u00e3 a ecr\u00e3 \u2014 nDm",
      desc=DESC_CARTAO, app="Cart\u00e3o", root="../",
      ogtitle="Cart\u00e3o de Residente \u2014 Damos o Caminho",
      og=SITE + "/cartao/og-image.png", url=SITE + "/cartao/"))
PAGES.append(SITE + "/cartao/")
print("built: cartao/index.html")

# ---------- /magnolia/ — SIMplifica: бронь корта в Quinta Magnólia --------
# Устроена как /cartao/: свой движок внутри тела, тексты в _src/i18n/magnolia.*.js.
# Иконка «на экран Домой» своя — Σ серии SIMplifica в терракоте, подпись «Magnólia».
subprocess_run = __import__("subprocess").run
subprocess_run([__import__("sys").executable, "_src/magnolia-assets.py"], check=True)
mag = read("_src/magnolia-body.html")
mag = mag.replace("{{I18N}}", "\n".join(
    read("_src/i18n/magnolia.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/magnolia.%s.js" % L)))
DESC_MAG = ("Reservar padel, ténis ou squash na Quinta Magnólia, no Funchal, pelo portal SIMplifica: "
            "o caminho completo, os preços oficiais e a semana gratuita de 23 a 30 de setembro.")
html = wrap(FONTS + mag, lang="pt",
            title="Reservar um campo de padel na Quinta Magnólia — nDm",
            desc=DESC_MAG, app="Magnólia", root="../",
            ogtitle="Padel na Quinta Magnólia — reservar passo a passo",
            og=SITE + "/magnolia/og-image.png", url=SITE + "/magnolia/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/magnolia/icon.svg?v=1"')
            .replace('href="../apple-touch-icon.png"', 'href="/magnolia/icon-180.png"')
            .replace('href="../manifest.webmanifest"', 'href="/magnolia/manifest.webmanifest"'))
write("magnolia/index.html", html)
PAGES.append(SITE + "/magnolia/")
print("built: magnolia/index.html")

# ---------- /lei-23-2026/ — новость про отменённый потолок ---------------
page("_src/news-body.html", "news", "lei-23-2026/index.html",
     CR + "Lei 23/2026",
     lang="pt", title="O tecto de 400 € saiu da lei — nDm",
     desc="A Lei 23/2026 acabou com o limite máximo de reembolso das viagens entre a Madeira e o continente. A página oficial continua a dizer 400 €.",
     app="Subsídio", root="../", ogtitle="O tecto de 400 € saiu da lei — Damos o Caminho",
     og=SITE + "/og-image.png", url=SITE + "/lei-23-2026/")

# ---------- sitemap.xml + robots.txt -----------------------------------
import datetime
today = datetime.date.today().isoformat()
rows = []
for u in PAGES:
    rows.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>" % (u, today))
    for L in LANG_ORDER:
        rows.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s?lang=%s"/>' % (
            "pt-PT" if L == "pt" else L, u, L))
    rows.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % u)
    rows.append("  </url>")

write("sitemap.xml",
      '<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
      '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
      + "\n".join(rows) + "\n</urlset>\n")
print("built: sitemap.xml (%d страниц)" % len(PAGES))

write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
print("built: robots.txt")

# ---------- пререндер -----------------------------------------------------
# ОБЯЗАТЕЛЕН: без него на сайте лежат пустые оболочки, которые краулер не читает.
# Поэтому вызывается прямо здесь, а не отдельной командой — чтобы нельзя было забыть.
import subprocess, sys
print()
subprocess.run([sys.executable, "_src/prerender.py"], check=True)
