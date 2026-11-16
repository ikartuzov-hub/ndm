# -*- coding: utf-8 -*-
"""Собирает готовые к заливке страницы репозитория ndm из исходников.

Запуск из корня репозитория:  python3 _src/build.py
"""
import io, os, re, glob

SITE = "https://ajuda.seedwave.pt"
PAGES = []   # (url, приоритет) — наполняется по ходу сборки
LANG_ORDER = ["pt", "en", "ru", "es", "de"]

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
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
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
CF_ANALYTICS = "<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{\"token\": \"8a509477310442638b80e4b22319b89b\"}'></script><!-- End Cloudflare Web Analytics -->"
SW_ECO = '<script defer src="https://seedwave.pt/nav/sw.js"></script>'
FOOT = "\n" + CF_ANALYTICS + "\n" + SW_ECO + "\n</body>\n</html>\n"

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
    · <a data-mad href="https://seedwave.pt/madeira/?lang=pt&amp;utm_source=ndm&amp;utm_medium=footer">Madeira</a>
    · <a href="https://www.linkedin.com/in/igor-kartuzov" target="_blank" rel="noopener">Igor Kartuzov</a>
  </footer>"""


# ---------- мост «Хочу такого же» → Лис (l.seedwave.pt) ------------------
# Блок в конце гида, перед подвалом. Свои тексты на 5 языков, свои цвета (индиго Лиса),
# не зависит от движка страницы: язык берёт из <html lang> и следит за его сменой.
# Три строки «что делал секретарь» — только факты из Досье проекта, без приукрашивания.
# События PostHog: lis_bridge_view (блок попал на экран), lis_bridge_click (нажата кнопка).
LIS_BRIDGE = {   # готовая страница → ключ истории
    "subsidio/index.html": "voos",
    "cesd/index.html": "cesd",
    "cesd/lite/index.html": "cesd",
    "acidente/index.html": "acidente",
    "acidente/lite/index.html": "acidente",
}
LIS_T = r"""{
ru:{sub:"ИИ-секретарь · сделан на Мадейре",tail:"Лис — такой же секретарь, настроенный под тебя.",btn:"Хочу такого же",note:"Лис работает только с тем, к чему ты сам открыл доступ.",
 voos:{h:"Эту заявку подавали вдвоём: человек и его ИИ-секретарь",l:["разобрал счёт авиакомпании до строки","заполнил поля портала и сверил суммы","заметил, что портал занизил возврат на 170 €"],m:"Человек вошёл своим ключом и нажал «Отправить»."},
 cesd:{h:"Эту карту получали вдвоём: человек и его ИИ-секретарь",l:["провёл запасным путём, когда портал отказал","составил обращение на португальском","следил за ответом службы до самой поездки"],m:"Человек вошёл своим ключом и поставил подпись."},
 acidente:{h:"Этот гид вырос из настоящего ДТП. Рядом был ИИ-секретарь",l:["голосом подсказал порядок действий на месте","дал фразы по-португальски для звонка в полицию","собрал план: страховая, сроки, подменная машина"],m:"Решения принимал человек."}},
pt:{sub:"Secretário de IA · feito na Madeira",tail:"O Lis é um secretário assim, configurado à medida de cada pessoa.",btn:"Quero um igual",note:"O Lis só trabalha com aquilo a que a própria pessoa deu acesso.",
 voos:{h:"Este pedido foi feito a dois: uma pessoa e o seu secretário de IA",l:["leu a fatura da companhia aérea linha a linha","preencheu os campos do portal e conferiu os valores","reparou que o portal tinha reduzido o reembolso em 170 €"],m:"A pessoa entrou com a sua chave e carregou em «Submeter»."},
 cesd:{h:"Este cartão foi obtido a dois: uma pessoa e o seu secretário de IA",l:["indicou o caminho alternativo quando o portal recusou","redigiu o pedido em português","acompanhou a resposta dos serviços até à viagem"],m:"A pessoa entrou com a sua chave e assinou."},
 acidente:{h:"Este guia nasceu de um acidente real. Ao lado estava um secretário de IA",l:["indicou por voz, no local, o que fazer primeiro","deu as frases em português para ligar à polícia","preparou o plano: seguradora, prazos, viatura de substituição"],m:"As decisões foram da pessoa."}},
en:{sub:"AI secretary · made in Madeira",tail:"Lis is a secretary like that, set up for one person at a time.",btn:"I want one too",note:"Lis only works with what its owner has opened access to.",
 voos:{h:"This claim was filed by two: a person and their AI secretary",l:["read the airline invoice line by line","filled in the portal fields and checked the amounts","noticed the portal had cut the refund by €170"],m:"The person signed in with their own key and pressed Submit."},
 cesd:{h:"This card was obtained by two: a person and their AI secretary",l:["showed the fallback route when the portal refused","drafted the request in Portuguese","kept track of the reply right up to the trip"],m:"The person signed in with their own key and signed."},
 acidente:{h:"This guide grew out of a real accident. An AI secretary was alongside",l:["talked through what to do first, by voice, on the spot","gave the Portuguese phrases for calling the police","put together the plan: insurer, deadlines, replacement car"],m:"The decisions were the person's."}},
es:{sub:"Secretario de IA · hecho en Madeira",tail:"Lis es un secretario así, configurado a la medida de cada persona.",btn:"Quiero uno igual",note:"Lis solo trabaja con aquello a lo que la propia persona dio acceso.",
 voos:{h:"Esta solicitud se hizo entre dos: una persona y su secretario de IA",l:["leyó la factura de la aerolínea línea por línea","rellenó los campos del portal y comprobó los importes","detectó que el portal había reducido el reembolso en 170 €"],m:"La persona entró con su clave y pulsó «Submeter»."},
 cesd:{h:"Esta tarjeta se consiguió entre dos: una persona y su secretario de IA",l:["indicó la vía alternativa cuando el portal la rechazó","redactó la solicitud en portugués","siguió la respuesta del organismo hasta el viaje"],m:"La persona entró con su clave y firmó."},
 acidente:{h:"Esta guía nació de un accidente real. Al lado había un secretario de IA",l:["indicó por voz, en el lugar, qué hacer primero","dio las frases en portugués para llamar a la policía","preparó el plan: aseguradora, plazos, coche de sustitución"],m:"Las decisiones las tomó la persona."}},
de:{sub:"KI-Sekretär · gemacht auf Madeira",tail:"Lis ist so ein Sekretär, eingerichtet für genau einen Menschen.",btn:"So einen will ich",note:"Lis arbeitet nur mit dem, wofür sein Besitzer selbst den Zugang geöffnet hat.",
 voos:{h:"Diesen Antrag haben zwei gestellt: ein Mensch und sein KI-Sekretär",l:["hat die Rechnung der Airline Zeile für Zeile gelesen","hat die Felder im Portal ausgefüllt und die Beträge geprüft","hat bemerkt, dass das Portal die Erstattung um 170 € gekürzt hatte"],m:"Der Mensch hat sich mit seinem Schlüssel angemeldet und auf «Submeter» gedrückt."},
 cesd:{h:"Diese Karte haben zwei bekommen: ein Mensch und sein KI-Sekretär",l:["hat den Ausweichweg gezeigt, als das Portal ablehnte","hat die Anfrage auf Portugiesisch verfasst","hat die Antwort der Behörde bis zur Reise verfolgt"],m:"Der Mensch hat sich mit seinem Schlüssel angemeldet und unterschrieben."},
 acidente:{h:"Dieser Leitfaden entstand aus einem echten Unfall. Ein KI-Sekretär war dabei",l:["hat vor Ort per Stimme gesagt, was zuerst zu tun ist","hat die portugiesischen Sätze für den Anruf bei der Polizei geliefert","hat den Plan erstellt: Versicherung, Fristen, Ersatzwagen"],m:"Entschieden hat der Mensch."}}
}"""
LIS_HTML = """<style>
.lisb{--lb:#F6F5FF;--ll:#E4E1FB;--la:#6D5DFC;--lah:#5445E6;--li:#1B1A2E;--lm:#5C5B78;--lon:#fff;
 box-sizing:border-box;max-width:560px;margin:36px auto 8px;padding:18px 18px 16px;border:2px solid var(--la);border-radius:16px;
 background:var(--lb);color:var(--li);font:400 16px/1.45 "IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;text-align:left}
:root[data-theme="dark"] .lisb{--lb:#1A1A33;--ll:#2E2C55;--la:#8B7DFF;--lah:#A297FF;--li:#F1EFFF;--lm:#A9A6C9;--lon:#121226}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]):not([data-theme="dark"]) .lisb{--lb:#1A1A33;--ll:#2E2C55;--la:#8B7DFF;--lah:#A297FF;--li:#F1EFFF;--lm:#A9A6C9;--lon:#121226}}
.lisb *{box-sizing:border-box}
.lisb-top{display:flex;align-items:center;gap:10px;margin:0 0 10px}
.lisb-top svg{width:38px;height:38px;flex:none;border:1px solid var(--ll);border-radius:11px;padding:5px;background:transparent}
.lisb-top b{display:block;font-weight:600;font-size:16px;line-height:1.2}
.lisb-top small{display:block;font-size:13px;color:var(--lm)}
.lisb h3{margin:0 0 10px;font:600 18px/1.3 inherit;font-family:inherit;color:var(--li)}
.lisb ul{list-style:none;margin:0 0 10px;padding:0}
.lisb li{position:relative;padding:3px 0 3px 26px;font-size:15.5px;color:var(--li)}
.lisb li::before{content:"";position:absolute;left:4px;top:9px;width:11px;height:6px;border-left:2px solid var(--la);border-bottom:2px solid var(--la);transform:rotate(-45deg)}
.lisb p{margin:0 0 8px;font-size:15px;color:var(--lm)}
.lisb p.lisb-tail{color:var(--li);font-weight:500}
.lisb a.lisb-btn{display:block;margin:12px 0 10px;padding:13px 16px;border-radius:12px;background:var(--la);color:var(--lon);
 font-weight:600;font-size:16.5px;text-align:center;text-decoration:none;min-height:48px}
.lisb a.lisb-btn:hover,.lisb a.lisb-btn:focus-visible{background:var(--lah);outline:none}
.lisb p.lisb-note{font-size:12.5px;margin:0}
@media print{.lisb{display:none}}
</style>
<aside class="lisb" id="lisBridge" data-guide="%(g)s" aria-label="Lis">
  <div class="lisb-top"><svg viewBox="0 0 100 100" fill="none" stroke="var(--la)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M35 18 L35 66 L60 66"/><path d="M14 84 Q26 78 38 84 Q50 90 62 84 Q74 78 86 84"/></svg>
    <div><b>Lis</b><small data-lb="sub"></small></div></div>
  <h3 data-lb="h"></h3>
  <ul data-lb="l"></ul>
  <p data-lb="m"></p>
  <p class="lisb-tail" data-lb="tail"></p>
  <a class="lisb-btn" id="lisBridgeBtn" href="https://l.seedwave.pt/?utm_source=ndm&amp;utm_medium=bridge&amp;utm_campaign=%(g)s" rel="noopener"><span data-lb="btn"></span> →</a>
  <p class="lisb-note" data-lb="note"></p>
</aside>
<script>
(function(){
var T=%(t)s;
var box=document.getElementById('lisBridge');if(!box)return;
var g=box.getAttribute('data-guide'),btn=document.getElementById('lisBridgeBtn');
function L(){var h=(document.documentElement.getAttribute('lang')||'pt').slice(0,2).toLowerCase();return T[h]?h:'pt';}
function paint(){var k=L(),t=T[k],s=t[g];
  var v={sub:t.sub,h:s.h,m:s.m,tail:t.tail,btn:t.btn,note:t.note};
  box.querySelectorAll('[data-lb]').forEach(function(e){var n=e.getAttribute('data-lb');
    if(n==='l'){e.innerHTML=s.l.map(function(x){return '<li>'+x+'</li>';}).join('');}
    else if(e.textContent!==v[n])e.textContent=v[n];});
  btn.href='https://l.seedwave.pt/?lang='+k+'&utm_source=ndm&utm_medium=bridge&utm_campaign='+g;}
function tr(ev){try{window.swTrack&&window.swTrack(ev,{guide:g,lang:L(),page:location.pathname});}catch(e){}}
paint();
if(window.MutationObserver)new MutationObserver(paint).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
btn.addEventListener('click',function(){tr('lis_bridge_click');});
if(window.IntersectionObserver){var seen=false;var io=new IntersectionObserver(function(en){
  if(seen||!en[0].isIntersecting)return;seen=true;io.disconnect();
  var n=0;(function go(){if(window.swTrack)tr('lis_bridge_view');else if(n++<20)setTimeout(go,500);})();},{threshold:.5});io.observe(box);}
})();
</script>
"""


def lis_bridge(p, s):
    """Вставляет мост к Лису перед первым <footer> страниц из LIS_BRIDGE."""
    g = LIS_BRIDGE.get(p.replace(os.sep, "/"))
    if not g or 'id="lisBridge"' in s:
        return s
    i = s.find("<footer")
    if i < 0:
        return s
    return s[:i] + (LIS_HTML % {"g": g, "t": LIS_T}) + s[i:]


# ---------- сторож сроков: «Напомнить о следующем сроке» → @SeedWaveBot -----
# Стоит перед мостом к Лису. Ссылка t.me/SeedWaveBot?start=porta_<дверь>_<full|lite>_<язык>
# ведёт в ветку porta_ движка SeedWave Engine (6093348): приветствие → ✅ → строка в Notion
# «🌙 Portas — подписчики» → напоминания сценарием 8437652 в 09:00. Двери: voos, cesd, acidente.
# События PostHog: watch_view, watch_click. Один подписчик = один «пользователь» воронки.
WATCH_PAGES = {
    "subsidio/index.html": ("voos", "full"),
    "cesd/index.html": ("cesd", "full"),
    "cesd/lite/index.html": ("cesd", "lite"),
    "acidente/index.html": ("acidente", "full"),
    "acidente/lite/index.html": ("acidente", "lite"),
}
WATCH_T = r"""{
ru:{h:"🔔 Бесплатный сторож сроков",btn:"Напомнить мне в Telegram",free:"Первым ста — и расширенная версия бесплатно, навсегда.",
 voos:"Напомню в Telegram: после полёта — сохранить счёт, через два месяца — подать на возврат.",
 cesd:"Напомню в Telegram: пришла ли карта, а позже — проверить её срок.",
 acidente:"Напомню в Telegram: положить в машину бланк, жилет и знак, а через полгода — проверить полис."},
pt:{h:"🔔 Vigia de prazos gratuito",btn:"Lembrar-me no Telegram",free:"Para os primeiros cem, a versão alargada também será grátis — para sempre.",
 voos:"Lembro no Telegram: depois do voo — guardar a fatura; dois meses depois — pedir o reembolso.",
 cesd:"Lembro no Telegram: se o cartão já chegou e, mais tarde, a sua validade.",
 acidente:"Lembro no Telegram: pôr no carro a declaração, o colete e o triângulo e, daqui a seis meses, confirmar a apólice."},
en:{h:"🔔 Free deadline watcher",btn:"Remind me on Telegram",free:"For the first hundred, the extended version will be free too — forever.",
 voos:"I'll remind you on Telegram: after a flight — keep the invoice; two months later — claim the refund.",
 cesd:"I'll remind you on Telegram: whether the card has arrived and, later, its expiry date.",
 acidente:"I'll remind you on Telegram: put the form, vest and triangle in the car, and in six months — check the policy."},
es:{h:"🔔 Vigilante de plazos gratuito",btn:"Recordármelo en Telegram",free:"Para los primeros cien, la versión ampliada también será gratis, para siempre.",
 voos:"Se lo recuerdo en Telegram: tras el vuelo — guardar la factura; dos meses después — pedir el reembolso.",
 cesd:"Se lo recuerdo en Telegram: si ya llegó la tarjeta y, más tarde, su validez.",
 acidente:"Se lo recuerdo en Telegram: poner en el coche la declaración, el chaleco y el triángulo y, en seis meses, revisar la póliza."},
de:{h:"🔔 Kostenloser Fristenwächter",btn:"Per Telegram erinnern",free:"Für die ersten hundert bleibt auch die erweiterte Version kostenlos — für immer.",
 voos:"Ich erinnere Sie per Telegram: nach dem Flug — Rechnung aufheben; zwei Monate später — Erstattung beantragen.",
 cesd:"Ich erinnere Sie per Telegram: ob die Karte da ist und später an ihr Ablaufdatum.",
 acidente:"Ich erinnere Sie per Telegram: Unfallbericht, Weste und Dreieck ins Auto legen und in sechs Monaten die Police prüfen."}
}"""
WATCH_HTML = """<style>
.swatch{box-sizing:border-box;max-width:560px;margin:36px auto 0;padding:16px 18px;border:1.5px dashed var(--accent,#B23A0E);border-radius:16px;
 background:var(--card,var(--surface,#fff));color:var(--ink,#1A1512);font:400 16px/1.45 "IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;text-align:left}
.swatch *{box-sizing:border-box}
.swatch h3{margin:0 0 6px;font:600 18px/1.3 "IBM Plex Sans",system-ui,sans-serif;color:var(--ink,#1A1512)}
.swatch p{margin:0 0 10px;font-size:15.5px;color:var(--ink-soft,#6B5C51)}
.swatch a.swatch-btn{display:block;margin:4px 0 10px;padding:13px 16px;border-radius:12px;background:#229ED9;color:#fff;font-weight:600;font-size:16.5px;text-align:center;text-decoration:none;min-height:48px}
.swatch a.swatch-btn:hover,.swatch a.swatch-btn:focus-visible{background:#1A87BB;outline:none}
.swatch p.swatch-free{font-size:13px;margin:0;color:var(--ink,#1A1512);font-weight:500}
@media print{.swatch{display:none}}
</style>
<aside class="swatch" id="swWatch" data-door="%(door)s" data-zone="%(zone)s" aria-label="SeedWave">
  <h3 data-sw="h"></h3>
  <p data-sw="line"></p>
  <a class="swatch-btn" id="swWatchBtn" href="https://t.me/SeedWaveBot?start=porta_%(door)s_%(zone)s_pt" target="_blank" rel="noopener"><span data-sw="btn"></span> →</a>
  <p class="swatch-free" data-sw="free"></p>
</aside>
<script>
(function(){
var T=%(t)s;
var box=document.getElementById('swWatch');if(!box)return;
var door=box.getAttribute('data-door'),zone=box.getAttribute('data-zone'),btn=document.getElementById('swWatchBtn');
function L(){var h=(document.documentElement.getAttribute('lang')||'pt').slice(0,2).toLowerCase();return T[h]?h:'pt';}
function paint(){var k=L(),t=T[k],v={h:t.h,line:t[door],btn:t.btn,free:t.free};
  box.querySelectorAll('[data-sw]').forEach(function(e){var n=e.getAttribute('data-sw');if(e.textContent!==v[n])e.textContent=v[n];});
  btn.href='https://t.me/SeedWaveBot?start=porta_'+door+'_'+zone+'_'+k;}
function tr(ev){try{window.swTrack&&window.swTrack(ev,{guide:door,zone:zone,lang:L()});}catch(e){}}
paint();
if(window.MutationObserver)new MutationObserver(paint).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
btn.addEventListener('click',function(){tr('watch_click');});
if(window.IntersectionObserver){var seen=false;var io=new IntersectionObserver(function(en){
  if(seen||!en[0].isIntersecting)return;seen=true;io.disconnect();
  var n=0;(function go(){if(window.swTrack)tr('watch_view');else if(n++<20)setTimeout(go,500);})();},{threshold:.5});io.observe(box);}
})();
</script>
"""


def watch_block(p, s):
    """Сторож сроков — перед мостом к Лису (или перед подвалом, если моста нет)."""
    w = WATCH_PAGES.get(p.replace(os.sep, "/"))
    if not w or 'id="swWatch"' in s:
        return s
    i = s.find('<style>\n.lisb{')
    if i < 0:
        i = s.find("<footer")
    if i < 0:
        return s
    return s[:i] + (WATCH_HTML % {"door": w[0], "zone": w[1], "t": WATCH_T}) + s[i:]


def read(p):
    return io.open(p, encoding="utf-8").read()


def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    s = lis_bridge(p, s)
    s = watch_block(p, s)
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
OG2 = SITE + "/subsidio/og-image.png?v=490"
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
# \u0438\u043a\u043e\u043d\u043a\u0430 \u00ab\u043d\u0430 \u044d\u043a\u0440\u0430\u043d \u0414\u043e\u043c\u043e\u0439\u00bb \u2014 \u03a3 \u0441\u0435\u0440\u0438\u0438 SIMplifica \u0432 \u0441\u0438\u043d\u0435\u043c, \u043f\u043e\u0434\u043f\u0438\u0441\u044c \u00abCart\u00e3o\u00bb
__import__("subprocess").run([__import__("sys").executable, "_src/sigma_assets.py", "cartao",
                              "#1F5FA8", "#E8F0FA", "Cart\u00e3o", "/cartao/"], check=True)
write("cartao/index.html", wrap(FONTS + cartao, lang="pt",
      title="Cart\u00e3o de Residente na RAM: o pedido ecr\u00e3 a ecr\u00e3 \u2014 nDm",
      desc=DESC_CARTAO, app="Cart\u00e3o", root="../",
      ogtitle="Cart\u00e3o de Residente \u2014 Damos o Caminho",
      og=SITE + "/cartao/og-image.png", url=SITE + "/cartao/")
      .replace('href="../icon.svg?v=1"', 'href="/cartao/icon.svg?v=1"')
      .replace('href="../apple-touch-icon.png"', 'href="/cartao/icon-180.png"')
      .replace('href="../manifest.webmanifest"', 'href="/cartao/manifest.webmanifest"'))
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

# ---------- /trilhos/ — SIMplifica: бронь тропы (выпуск 4) ---------------
# Σ серии SIMplifica в зелёном, подпись «Trilhos». Движок и стили — внутри тела.
subprocess_run([__import__("sys").executable, "_src/sigma_assets.py", "trilhos",
                "#2E7D4F", "#EAF5EE", "Trilhos", "/trilhos/"], check=True)
subprocess_run([__import__("sys").executable, "_src/trilhos-og.py"], check=True)
tri = read("_src/trilhos-body.html")
tri = tri.replace("{{I18N}}", "\n".join(
    read("_src/i18n/trilhos.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/trilhos.%s.js" % L)))
DESC_TRI = ("Reservar um percurso pedestre na Madeira no SIMplifica: residentes a 0 € e visitantes "
            "no mesmo pedido, sem conta, passo a passo, com as armadilhas do formulário.")
html = wrap(FONTS + tri, lang="pt",
            title="Reservar um trilho na Madeira: residentes e visitantes num só pedido — nDm",
            desc=DESC_TRI, app="Trilhos", root="../",
            ogtitle="Reservar um trilho na Madeira — passo a passo",
            og=SITE + "/trilhos/og-image.png", url=SITE + "/trilhos/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/trilhos/icon.svg?v=1"')
            .replace('href="../apple-touch-icon.png"', 'href="/trilhos/icon-180.png"')
            .replace('href="../manifest.webmanifest"', 'href="/trilhos/manifest.webmanifest"'))
write("trilhos/index.html", html)
PAGES.append(SITE + "/trilhos/")
print("built: trilhos/index.html")

# ---------- /cesd/ — Cartão Europeu de Seguro de Doença (Segurança Social) -----
# Устроена как /trilhos/: движок и стили внутри тела, тексты в _src/i18n/cesd.*.js.
# Картинки (образцы GIT-53 и MG2 с вымышленными данными, сетка подписи CMD),
# обложка и Σ в синем ЕС — _src/cesd-assets.py.
subprocess_run([__import__("sys").executable, "_src/cesd-assets.py"], check=True)
ces = read("_src/cesd-body.html")
ces = ces.replace("{{I18N}}", "\n".join(
    read("_src/i18n/cesd.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/cesd.%s.js" % L)))
DESC_CES = ("O Cartão Europeu de Seguro de Doença é gratuito. Quando a Segurança Social Direta recusa: "
            "o pedido no e-Clic, os modelos GIT-53 e MG2 e a assinatura com a Chave Móvel Digital.")
html = wrap(FONTS + ces, lang="pt",
            title="Cartão Europeu de Seguro de Doença: quando o portal recusa — nDm",
            desc=DESC_CES, app="CESD", root="../",
            ogtitle="Cartão Europeu de Seguro de Doença — passo a passo",
            og=SITE + "/cesd/og-image.png", url=SITE + "/cesd/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/cesd/icon.svg?v=2"')
            .replace('href="../apple-touch-icon.png"', 'href="/cesd/icon-180.png?v=2"')
            .replace('href="../manifest.webmanifest"', 'href="/cesd/manifest.webmanifest"'))
write("cesd/index.html", html)
PAGES.append(SITE + "/cesd/")
print("built: cesd/index.html")

# ---------- /cesd/lite/ — «Лайт»: один экран, пояснения по тапу (06.11.2026) ----------
# Тот же знак и манифест, что у /cesd/; тексты в _src/i18n/cesdlite.*.js.
lit = read("_src/cesd-lite-body.html")
lit = lit.replace("{{I18N}}", "\n".join(
    read("_src/i18n/cesdlite.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/cesdlite.%s.js" % L)))
DESC_LIT = ("O Cartão Europeu de Seguro de Doença é gratuito para quem vive em Portugal: "
            "carrega na Segurança Social Direta — deixa ou não deixa. O que fazer em cada caso.")
html = wrap(FONTS + lit, lang="pt",
            title="Cartão Europeu de Seguro de Doença em duas perguntas — nDm",
            desc=DESC_LIT, app="CESD", root="../../",
            ogtitle="Cartão Europeu de Saúde — duas perguntas",
            og=SITE + "/cesd/og-image.png", url=SITE + "/cesd/lite/")
html = (html.replace('href="../../icon.svg?v=1"', 'href="/cesd/icon.svg?v=2"')
            .replace('href="../../apple-touch-icon.png"', 'href="/cesd/icon-180.png?v=2"')
            .replace('href="../../manifest.webmanifest"', 'href="/cesd/manifest.webmanifest"'))
write("cesd/lite/index.html", html)
PAGES.append(SITE + "/cesd/lite/")
print("built: cesd/lite/index.html")


# ---------- /aima/ — AIMA: трекер процесса (серия A, первая страница) ----------
# Устроена как /cesd/: движок и стили внутри тела, тексты в _src/i18n/aima.*.js.
# Скрины трекера — статика в aima/img (сняты с живого дела, данные замазаны);
# значок A в фиолетовом AIMA и обложка — _src/aima-assets.py.
subprocess_run([__import__("sys").executable, "_src/aima-assets.py"], check=True)
aim = read("_src/aima-body.html")
aim = aim.replace("{{I18N}}", "\n".join(
    read("_src/i18n/aima.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/aima.%s.js" % L)))
DESC_AIMA = ("A AIMA tem um rastreador de processos com oito etapas, da submissão ao cartão entregue. "
             "Chega-se lá pelo formulário de contacto, sem conta nem senha: o link, as etapas e o que fazer quando falha.")
html = wrap(FONTS + aim, lang="pt",
            title="Onde está o meu processo na AIMA? O rastreador oficial, passo a passo — nDm",
            desc=DESC_AIMA, app="AIMA", root="../",
            ogtitle="Onde está o meu processo na AIMA? — o rastreador oficial",
            og=SITE + "/aima/og-image.png", url=SITE + "/aima/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/aima/icon.svg?v=1"')
            .replace('href="../apple-touch-icon.png"', 'href="/aima/icon-180.png"')
            .replace('href="../manifest.webmanifest"', 'href="/aima/manifest.webmanifest"'))
write("aima/index.html", html)
PAGES.append(SITE + "/aima/")
print("built: aima/index.html")

# ---------- /cmd/ — Chave Móvel Digital: «número + PIN = a sua chave» (08.11.2026) ----------
# Устроена как /cesd/lite/: один экран, пояснения по тапу, памятка на печать.
# Значок-ключ в бирюзе и обложка — _src/cmd-assets.py; тексты — _src/i18n/cmd.*.js.
subprocess_run([__import__("sys").executable, "_src/cmd-assets.py"], check=True)
cmd = read("_src/cmd-body.html")
cmd = cmd.replace("{{I18N}}", "\n".join(
    read("_src/i18n/cmd.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/cmd.%s.js" % L)))
DESC_CMD = ("A Chave Móvel Digital não é um cartão nem uma app: é o seu número de telemóvel e o PIN que escolheu. "
            "Como entrar nas Finanças e na Segurança Social, e o que fazer se esqueceu o PIN.")
html = wrap(FONTS + cmd, lang="pt",
            title="Onde está a minha Chave Móvel Digital? Em três passos — nDm",
            desc=DESC_CMD, app="Chave", root="../",
            ogtitle="Onde está a minha Chave Móvel Digital? Número + PIN = a sua chave",
            og=SITE + "/cmd/og-image.png", url=SITE + "/cmd/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/cmd/icon.svg?v=1"')
            .replace('href="../apple-touch-icon.png"', 'href="/cmd/icon-180.png"')
            .replace('href="../manifest.webmanifest"', 'href="/cmd/manifest.webmanifest"'))
write("cmd/index.html", html)
PAGES.append(SITE + "/cmd/")
print("built: cmd/index.html")

# ---------- /renda/ — Renda até 2 300 €: IRS 10 % em vez de 25 % (08.11.2026) ----------
# Устроена как /cmd/: один экран, калькулятор-ползунок (без ввода текста), роли сдаю/снимаю,
# «золотая зона» 2 301–2 760 €, пояснения по тапу. Значок-домик в терракоте — _src/renda-assets.py.
subprocess_run([__import__("sys").executable, "_src/renda-assets.py"], check=True)
ren = read("_src/renda-body.html")
ren = ren.replace("{{I18N}}", "\n".join(
    read("_src/i18n/renda.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/renda.%s.js" % L)))
DESC_RENDA = ("Desde 2026, as rendas habitacionais até 2 300 € por mês pagam IRS a 10 % em vez de 25 %. "
              "Às vezes baixar a renda rende mais ao senhorio. Calculadora para senhorios e inquilinos.")
html = wrap(FONTS + ren, lang="pt",
            title="Renda até 2 300 €: IRS de 10 % em vez de 25 % — calculadora — nDm",
            desc=DESC_RENDA, app="Renda", root="../",
            ogtitle="Renda até 2 300 €: IRS de 10 % em vez de 25 %. Faça a conta",
            og=SITE + "/renda/og-image.png", url=SITE + "/renda/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/renda/icon.svg?v=1"')
            .replace('href="../apple-touch-icon.png"', 'href="/renda/icon-180.png"')
            .replace('href="../manifest.webmanifest"', 'href="/renda/manifest.webmanifest"'))
write("renda/index.html", html)
PAGES.append(SITE + "/renda/")
print("built: renda/index.html")

# ---------- /acidente/ — ДТП в Португалии: первые 5 минут, фразы, бланк DAAA (15.11.2026) ----------
# Устроена как /cmd/: один экран, движок и стили внутри тела, тексты в _src/i18n/acidente.*.js.
# Вау — «Показать португальцу»: фраза PT-PT на весь экран + голос; бланк DAAA схемой, три случая.
# Значок-треугольник в красно-оранжевом, обложка и офлайн-воркер sw.js — _src/acidente-assets.py.
subprocess_run([__import__("sys").executable, "_src/acidente-assets.py"], check=True)
acd = read("_src/acidente-body.html")
acd = acd.replace("{{I18N}}", "\n".join(
    read("_src/i18n/acidente.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/acidente.%s.js" % L)))
DESC_ACD = ("Acidente de carro em Portugal: os primeiros 5 minutos, frases em ecrã inteiro para mostrar, "
            "a declaração amigável campo a campo, quando chamar a polícia e os prazos do seguro.")
html = wrap(FONTS + acd, lang="pt",
            title="Acidente de carro em Portugal: o que fazer e como preencher a declaração amigável — nDm",
            desc=DESC_ACD, app="Acidente", root="../",
            ogtitle="Acidente em Portugal: um toque não é motivo para pânico",
            og=SITE + "/acidente/og-image.png", url=SITE + "/acidente/")
html = (html.replace('href="../icon.svg?v=1"', 'href="/acidente/icon.svg?v=1"')
            .replace('href="../apple-touch-icon.png"', 'href="/acidente/icon-180.png"')
            .replace('href="../manifest.webmanifest"', 'href="/acidente/manifest.webmanifest"'))
write("acidente/index.html", html)
PAGES.append(SITE + "/acidente/")
print("built: acidente/index.html")

# ---------- /acidente/lite/ — «Лайт»: 8 шагов на одном экране, кто въехал / в кого въехали (15.11.2026) ----------
# Иконка — инверсия полной версии (белый треугольник на красно-оранжевом), свой манифест.
# Образцы заполненного бланка A4 на 5 языках — _src/acidente-pdf.py (Chromium → PDF).
subprocess_run([__import__("sys").executable, "_src/acidente-pdf.py"], check=True)
acl = read("_src/acidente-lite-body.html")
acl = acl.replace("{{I18N}}", "\n".join(
    read("_src/i18n/acidentelite.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/acidentelite.%s.js" % L)))
html = wrap(FONTS + acl, lang="pt",
            title="Acidente de carro em Portugal — 8 passos, em curto (Lite) — nDm",
            desc=("Bateram-te ou bateste: quatro piscas, colete, triângulo, fotos, documentos, declaração amigável, "
                  "polícia, seguro. Marca os passos com o dedo; frases em ecrã inteiro e com voz."),
            app="Acidente Lite", root="../../",
            ogtitle="Acidente? Vai passo a passo — 8 passos no telemóvel",
            og=SITE + "/acidente/og-image.png", url=SITE + "/acidente/lite/")
html = (html.replace('href="../../icon.svg?v=1"', 'href="/acidente/lite/icon.svg?v=1"')
            .replace('href="../../apple-touch-icon.png"', 'href="/acidente/lite/icon-180.png"')
            .replace('href="../../manifest.webmanifest"', 'href="/acidente/lite/manifest.webmanifest"'))
write("acidente/lite/index.html", html)
PAGES.append(SITE + "/acidente/lite/")
print("built: acidente/lite/index.html")

# ---------- /participar/ — «Заявить о себе 😉»: воронка nDm → SeedWave -------------
# Форма → Make (webhook 3965164, сценарий 8141929) → Telegram Игорю + Notion «🙋 Заявить о себе».
subprocess_run([__import__("sys").executable, "_src/participar-assets.py"], check=True)
par = read("_src/participar-body.html")
par = par.replace("{{I18N}}", "\n".join(
    read("_src/i18n/participar.%s.js" % L).strip()
    for L in LANG_ORDER if os.path.exists("_src/i18n/participar.%s.js" % L)))
html = wrap(FONTS + par, lang="pt",
            title="Dê-se a conhecer: pergunta, ideia, trabalho, serviço ou setor — e receba mais na Madeira e em Portugal — nDm · SeedWave",
            desc=("Os guias dos serviços públicos da Madeira e de Portugal são gratuitos. Dê-se a conhecer e receba mais: "
                  "resposta de uma pessoa, ideias onde apostar, pessoas que precisam de si e os novos guias em primeira mão."),
            app="nDm", root="../",
            ogtitle="Dê-se a conhecer 😉 — nDm · SeedWave",
            og=SITE + "/participar/og-image.png", url=SITE + "/participar/")
write("participar/index.html", html)
PAGES.append(SITE + "/participar/")
print("built: participar/index.html")

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
write("llms.txt", read("_src/llms.txt"))
print("built: llms.txt")

# ---------- пререндер -----------------------------------------------------
# ОБЯЗАТЕЛЕН: без него на сайте лежат пустые оболочки, которые краулер не читает.
# Поэтому вызывается прямо здесь, а не отдельной командой — чтобы нельзя было забыть.
import subprocess, sys
print()
subprocess.run([sys.executable, "_src/prerender.py"], check=True)
