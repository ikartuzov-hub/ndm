# -*- coding: utf-8 -*-
"""Пререндер: запекает текст страниц в HTML и раскладывает по языковым адресам.

Зачем. Все страницы рисует JavaScript, и краулеру без JS достаётся пустая оболочка —
до пререндера это было 68 знаков текста на весь сайт. Google такое ещё вытягивает,
Bing хуже, а ИИ-краулеры (GPTBot, ClaudeBot, PerplexityBot) JS не выполняют вовсе.

Что делает. Поднимает локальный сервер на собранном сайте, открывает каждую страницу
на каждом из пяти языков в Chromium, ждёт отрисовки и сохраняет получившийся DOM:
португальский — на канонический адрес, остальные — в подпапку языка.

  /subsidio/            → португальский (канонический)
  /subsidio/en/ /ru/ …  → остальные четыре

В каждую страницу дописывается NDM_LANG — чтобы движок при загрузке в браузере
не перерисовал её в другой язык, — и правятся canonical, og:url, hreflang и <html lang>.

Запуск из корня репозитория, ПОСЛЕ build.py:  python3 _src/prerender.py
"""
import asyncio, io, os, re, http.server, socketserver, threading, functools, json

SITE = "https://ajuda.seedwave.pt"
LANGS = ["pt", "en", "ru", "de", "es"]
HTML_LANG = {"pt": "pt-PT", "en": "en", "ru": "ru", "de": "de", "es": "es"}
PORT = 0          # свободный порт выбирает система — сборку можно гонять подряд
import datetime
DATE = datetime.date.today().isoformat()

# страница → (её путь, нужен ли JSON-LD статьи)
PAGES = ["", "tap/", "cartao/", "subsidio/", "subsidio/dinheiro/", "subsidio/rejeitado/",
         "subsidio/familia/", "lei-23-2026/", "magnolia/", "trilhos/"]


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve():
    handler = functools.partial(Quiet, directory=os.getcwd())
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1]


def head_fix(html, path, lang):
    """Правит метатеги под конкретную языковую версию страницы."""
    url = SITE + "/" + path
    lurl = url if lang == "pt" else url + lang + "/"

    html = re.sub(r'<html lang="[^"]*"', '<html lang="%s"' % HTML_LANG[lang], html, count=1)
    html = re.sub(r'<link rel="canonical" href="[^"]*">',
                  '<link rel="canonical" href="%s">' % lurl, html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]*">',
                  '<meta property="og:url" content="%s">' % lurl, html, count=1)
    html = re.sub(r'<meta property="og:locale" content="[^"]*">',
                  '<meta property="og:locale" content="%s">' % (
                      "pt_PT" if lang == "pt" else HTML_LANG[lang]), html, count=1)

    alts = "\n".join(
        ['<link rel="alternate" hreflang="%s" href="%s">' % (
            HTML_LANG[L], url if L == "pt" else url + L + "/") for L in LANGS]
        + ['<link rel="alternate" hreflang="x-default" href="%s">' % url])
    html = re.sub(r'(<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*)+', alts + "\n",
                  html, count=1)
    return html


def jsonld(html, path, lang, ld):
    """Разметка для поиска и нейросетей. Вопросы и ответы берутся из отрисованного
    DOM — значит совпадают с видимым текстом посимвольно, как требует Google."""
    url = SITE + "/" + path
    lurl = url if lang == "pt" else url + lang + "/"
    blocks = []
    if not path:
        # корень домена: до 14.09 уходил в поиск вообще без разметки — пять адресов
        # из сорока, и самые важные. WebSite опознаёт сайт, ItemList отдаёт ИИ-сетям
        # оглавление с первой же страницы, без обхода ссылок.
        blocks.append({
            "@context": "https://schema.org", "@type": "WebSite",
            "name": "nDm — Nova Dádiva da Madeira",
            "alternateName": "Damos o Caminho",
            "url": lurl, "inLanguage": HTML_LANG[lang],
            "description": ld["desc"],
            "isAccessibleForFree": True,
            "publisher": {"@type": "Organization", "name": "SeedWave",
                          "url": "https://seedwave.pt/"},
            "author": {"@type": "Person", "name": "Igor Kartuzov",
                       "url": "https://www.linkedin.com/in/igor-kartuzov/"},
        })
        if ld.get("refs"):
            blocks.append({
                "@context": "https://schema.org", "@type": "ItemList",
                "name": ld["title"], "inLanguage": HTML_LANG[lang],
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1,
                     "name": name.strip(), "description": desc.strip(),
                     "url": SITE + href if href.startswith("/") else href}
                    for i, (href, name, desc) in enumerate(ld["refs"]) if name.strip()],
            })
    elif path == "lei-23-2026/":
        blocks.append({
            "@context": "https://schema.org", "@type": "NewsArticle",
            "headline": ld["h1"], "description": ld["desc"],
            "inLanguage": HTML_LANG[lang],
            "datePublished": "2026-09-13", "dateModified": DATE,
            "mainEntityOfPage": lurl, "url": lurl,
            "image": SITE + "/og-image.png",
            "author": {"@type": "Person", "name": "Igor Kartuzov",
                       "url": "https://www.linkedin.com/in/igor-kartuzov/"},
            "publisher": {"@type": "Organization", "name": "SeedWave",
                          "url": "https://seedwave.pt/"},
            "isAccessibleForFree": True,
        })
    elif path:
        blocks.append({
            "@context": "https://schema.org", "@type": "HowTo",
            "name": ld["h1"], "description": ld["desc"],
            "inLanguage": HTML_LANG[lang], "url": lurl,
            "dateModified": DATE, "totalTime": "PT20M",
            "author": {"@type": "Person", "name": "Igor Kartuzov"},
        })
    if ld["qa"]:
        blocks.append({
            "@context": "https://schema.org", "@type": "FAQPage",
            "inLanguage": HTML_LANG[lang],
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ld["qa"]],
        })
    if not blocks:
        return html
    tag = "\n".join('<script type="application/ld+json">%s</script>' %
                    json.dumps(b, ensure_ascii=False) for b in blocks)
    return html.replace("</head>", tag + "\n</head>", 1)


def depth_fix(html, path, lang):
    """Языковая подпапка на уровень глубже — чинит относительные ссылки на ресурсы."""
    if lang == "pt":
        return html
    html = html.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
    html = re.sub(r'(<img[^>]*\ssrc=")(?!\.\.?/|/|https?:|data:)', r'\1../', html)
    return html


async def main():
    from playwright.async_api import async_playwright
    httpd, port = serve()
    made, out_files = [], {}
    async with async_playwright() as p:
        br = await p.chromium.launch()
        # язык задаётся ДО отрисовки — тогда движок сам строит языковые ссылки
        for lang in LANGS:
            ctx = await br.new_context(viewport={"width": 1100, "height": 900})
            await ctx.add_init_script('window.NDM_LANG="%s";' % lang)
            pg = await ctx.new_page()
            for path in PAGES:
                await pg.goto("http://127.0.0.1:%d/%s" % (port, path), wait_until="networkidle")
                await pg.wait_for_timeout(350)
                html = await pg.evaluate("() => '<!doctype html>\\n' + document.documentElement.outerHTML")
                ld = await pg.evaluate("""() => {
                    const qa = [...document.querySelectorAll('.qa')].map(e => [
                        e.querySelector('h3').textContent, e.querySelector('p').textContent]);
                    // карточки разделов с корня — из отрисованного DOM, как и всё остальное
                    const refs = [...document.querySelectorAll('#refs a.ref')].map(a => [
                        a.getAttribute('href') || a.dataset.ll || '',
                        (a.children[1] || {}).textContent || '',
                        (a.children[2] || {}).textContent || '']);
                    return { qa: qa, refs: refs,
                             title: document.title || '',
                             h1: (document.querySelector('h1')||{}).textContent || '',
                             desc: (document.querySelector('meta[name=description]')||{}).content || '' };
                }""")
                html = html.replace("<head>", '<head>\n<script>window.NDM_LANG="%s";</script>' % lang, 1)
                html = jsonld(html, path, lang, ld)
                html = head_fix(html, path, lang)
                html = depth_fix(html, path, lang)
                out = (path or "") + ("" if lang == "pt" else lang + "/") + "index.html"
                out_files[out] = html
                made.append(SITE + "/" + path + ("" if lang == "pt" else lang + "/"))
            await ctx.close()
        await br.close()
    httpd.shutdown()

    # пишем всё разом: иначе пререндер затирает исходник до отрисовки прочих языков
    for out, html in out_files.items():
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        io.open(out, "w", encoding="utf-8").write(html)

    # sitemap со всеми языковыми адресами
    today = DATE
    rows = []
    for path in PAGES:
        url = SITE + "/" + path
        for lang in LANGS:
            lurl = url if lang == "pt" else url + lang + "/"
            rows.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>" % (lurl, today))
            for L in LANGS:
                rows.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (
                    HTML_LANG[L], url if L == "pt" else url + L + "/"))
            rows.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % url)
            rows.append("  </url>")
    io.open("sitemap.xml", "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")

    io.open("indexnow.json", "w", encoding="utf-8").write(json.dumps({
        "host": "ajuda.seedwave.pt",
        "key": io.open("_src/indexnow.key").read().strip(),
        "keyLocation": SITE + "/" + io.open("_src/indexnow.key").read().strip() + ".txt",
        "urlList": made,
    }, ensure_ascii=False, indent=2) + "\n")

    print("пререндер: %d адресов (%d страниц × %d языков)" % (len(made), len(PAGES), len(LANGS)))


asyncio.run(main())
