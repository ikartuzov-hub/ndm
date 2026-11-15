# -*- coding: utf-8 -*-
"""Иконки, OG-обложка и офлайн-воркер /acidente/ — «ДТП в Португалии».
Значок — треугольник с «!» + волна, красно-оранжевый #B4410F (закон серии: знак + волна).

Запуск из корня репозитория:  python3 _src/acidente-assets.py"""
import io, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "_src")
from sigma_assets import build as sigma, TRI_PATHS

ACC = (180, 65, 15); ACCS = (251, 230, 218); GOLD = (227, 162, 26)
BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (94, 82, 72); WHITE = (255, 255, 255)
D = "/usr/share/fonts/truetype/dejavu/"; G = "/usr/share/fonts/truetype/google-fonts/"


def lora(sz):
    f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
    try:
        f.set_variation_by_axes([700])
    except Exception:
        pass
    return f


def og():
    import cairosvg
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im); X = 82
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#B4410F" '
           'stroke-width="7" stroke-linecap="round" stroke-linejoin="round">%s'
           '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>') % "".join('<path d="%s"/>' % x for x in TRI_PATHS)
    m = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=50, output_height=50))).convert("RGBA")
    im.paste(m, (X - 6, 44), m)
    d.text((X + 48, 52), "Acidente · nDm", font=lora(26), fill=INK)
    d.text((X, 140), "A C I D E N T E   E M   P O R T U G A L", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 19), fill=ACC)
    d.text((X, 176), "Um toque não é", font=lora(58), fill=INK)
    d.text((X, 248), "motivo para pânico", font=lora(58), fill=INK)
    pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 27)
    d.text((X, 350), "5 minutos · frases para mostrar ·", font=pop, fill=SOFT)
    d.text((X, 388), "a declaração amigável campo a campo", font=ImageFont.truetype(G + "Poppins-Bold.ttf", 27), fill=INK)
    d.text((X, 520), "ajuda.seedwave.pt/acidente", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=ACC)
    # справа: телефон с фразой на весь экран
    px, py, pw, ph = 860, 70, 270, 500
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=38, fill=INK)
    d.rounded_rectangle([px + 12, py + 14, px + pw - 12, py + ph - 14], radius=28, fill=ACC)
    big = lora(30)
    for i, ln in enumerate(["Tem a", "declaração", "amigável?"]):
        d.text((px + 34, py + 120 + i * 44), ln, font=big, fill=WHITE)
    d.text((px + 34, py + 270), "У вас есть бланк?", font=ImageFont.truetype(D + "DejaVuSans.ttf", 18), fill=ACCS)
    d.rounded_rectangle([px + 34, py + 400, px + pw - 34, py + 448], radius=16, fill=WHITE)
    d.text((px + 62, py + 410), "▶  Ouvir", font=ImageFont.truetype(G + "Poppins-Bold.ttf", 22), fill=INK)
    # треугольник-знак рядом с телефоном
    t = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="#FDF1D6" stroke="#E3A21A" stroke-width="7" '
        'stroke-linejoin="round" stroke-linecap="round"><path d="M50 12 L88 80 L12 80 Z"/><path d="M50 36 L50 56" fill="none"/>'
        '<path d="M50 67 L50 67"/></g></svg>').encode(), output_width=150, output_height=150))).convert("RGBA")
    im.paste(t, (720, 400), t)
    im.save("acidente/og-image.png")
    print("acidente og ok")


SW = """/* nDm · /acidente/ — офлайн: страница и её значки остаются в телефоне после первого открытия.
   Сеть первой (свежий текст), без сети — из кэша. */
var C='acidente-v2';
self.addEventListener('install',function(e){self.skipWaiting();e.waitUntil(caches.open(C).then(function(c){
  return c.addAll(['/acidente/','/acidente/lite/','/acidente/icon.svg','/acidente/icon-192.png']).catch(function(){});}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x.indexOf('acidente-')===0&&x!==C;}).map(function(x){return caches.delete(x);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('fetch',function(e){var r=e.request;if(r.method!=='GET')return;var u=new URL(r.url);
  if(u.origin!==location.origin||u.pathname.indexOf('/acidente/')!==0)return;
  e.respondWith(fetch(r).then(function(res){if(res.ok){var cp=res.clone();caches.open(C).then(function(c){c.put(r,cp);});}return res;})
    .catch(function(){return caches.match(r,{ignoreSearch:true}).then(function(m){return m||caches.match('/acidente/');});}));});
"""


if __name__ == "__main__":
    sigma("acidente", "#B4410F", "#FBE6DA", "Acidente", "/acidente/", "tri")
    sigma("acidente/lite", "#FFFFFF", "#B4410F", "Acidente Lite", "/acidente/lite/", "tri")
    og()
    io.open("acidente/sw.js", "w", encoding="utf-8").write(SW)
    print("acidente sw ok")
