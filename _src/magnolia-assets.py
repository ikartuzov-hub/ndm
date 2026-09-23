# -*- coding: utf-8 -*-
"""Значок, иконки телефона, manifest и OG-обложка страницы /magnolia/.

Серия SIMplifica: Σ + волна, у каждой услуги свой цвет. Магнолия — терракота.
Запуск из корня репозитория: python3 _src/magnolia-assets.py"""
from PIL import Image, ImageDraw, ImageFont
import io, json, math, os

ACC = (180, 83, 42)      # #B4532A
TILE = (248, 236, 229)   # #F8ECE5
BG = (250, 246, 241)
INK = (26, 21, 18)
SOFT = (107, 92, 81)
COURT = (47, 110, 142)
OUT = "magnolia"
os.makedirs(OUT, exist_ok=True)

SIGMA = [(68, 20), (32, 20), (52, 45), (32, 70), (68, 70)]


def wave(k, ox=0, oy=0):
    return [(ox + (20 + t / 60 * 60) * k, oy + (86 - 6 * math.sin(t / 60 * 2 * math.pi)) * k)
            for t in range(61)]


def mark(d, k, col, ox=0, oy=0):
    w = max(2, int(7 * k))
    pts = [(ox + x * k, oy + y * k) for x, y in SIGMA]
    d.line(pts, fill=col, width=w, joint="curve")
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=col)
    for t in range(0, 601):
        x = ox + (20 + t / 600 * 60) * k
        y = oy + (86 - 6 * math.sin(t / 600 * 2 * math.pi)) * k
        d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=col)


def tile(size):
    S = size * 4
    im = Image.new("RGB", (S, S), TILE)
    mark(ImageDraw.Draw(im), S / 100.0, ACC)
    return im.resize((size, size), Image.LANCZOS)


tile(180).save(OUT + "/icon-180.png")
tile(192).save(OUT + "/icon-192.png")
tile(512).save(OUT + "/icon-512.png")

io.open(OUT + "/icon.svg", "w", encoding="utf-8").write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Magnólia">'
    '<rect width="100" height="100" rx="23" fill="#F8ECE5"/>'
    '<g fill="none" stroke="#B4532A" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M68 20 L32 20 L52 45 L32 70 L68 70"/>'
    '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>\n')

io.open(OUT + "/manifest.webmanifest", "w", encoding="utf-8").write(json.dumps({
    "name": "Magnólia — reservar padel",
    "short_name": "Magnólia",
    "start_url": "/magnolia/",
    "display": "standalone",
    "background_color": "#FAF6F1",
    "theme_color": "#FAF6F1",
    "icons": [{"src": "/magnolia/icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "/magnolia/icon-512.png", "sizes": "512x512", "type": "image/png"}],
}, ensure_ascii=False, indent=2) + "\n")

# ---------- OG 1200×630 ---------------------------------------------------
G = "/usr/share/fonts/truetype/google-fonts/"
D = "/usr/share/fonts/truetype/dejavu/"


def lora(sz):
    f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
    try:
        f.set_variation_by_axes([700])
    except Exception:
        pass
    return f


def popp(sz):
    return ImageFont.truetype(G + "Poppins-Regular.ttf", sz)


def mono(sz):
    return ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", sz)


W, H = 1200, 630
im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)
X = 82
mark(d, 0.5, ACC, X - 6, 44)
d.text((X + 48, 52), "SIMplifica · nDm", font=lora(26), fill=INK)
d.text((X, 140), "Q U I N T A   M A G N Ó L I A", font=mono(19), fill=ACC)
d.text((X, 176), "Reservar padel", font=lora(72), fill=INK)
d.text((X, 262), "no Funchal", font=lora(72), fill=INK)
d.text((X, 372), "Passo a passo no SIMplifica.", font=popp(28), fill=SOFT)
d.text((X, 412), "Preços oficiais. PT · EN · RU · DE · ES", font=popp(28), fill=SOFT)
d.text((X, 520), "ajuda.seedwave.pt/magnolia", font=mono(22), fill=ACC)

# корт сверху: справа
cx, cy, cw, ch = 860, 70, 260, 490
d.rounded_rectangle([cx - 10, cy - 10, cx + cw + 10, cy + ch + 10], 12, outline=(203, 220, 229), width=10)
d.rectangle([cx, cy, cx + cw, cy + ch], outline=COURT, width=4)
d.line([(cx, cy + ch / 2), (cx + cw, cy + ch / 2)], fill=COURT, width=7)
d.line([(cx, cy + ch * .29), (cx + cw, cy + ch * .29)], fill=COURT, width=4)
d.line([(cx, cy + ch * .71), (cx + cw, cy + ch * .71)], fill=COURT, width=4)
d.line([(cx + cw / 2, cy + ch * .29), (cx + cw / 2, cy + ch * .71)], fill=COURT, width=4)
# траектория мяча пунктиром и сам мяч
A, B, C = (cx + 70, cy + ch - 60), (cx + cw - 60, cy + 70), (cx + cw * .8, cy + ch * .55)
prev = None
for i in range(0, 41):
    t = i / 40
    p = ((1 - t) ** 2 * A[0] + 2 * (1 - t) * t * C[0] + t * t * B[0],
         (1 - t) ** 2 * A[1] + 2 * (1 - t) * t * C[1] + t * t * B[1])
    if prev and i % 2:
        d.line([prev, p], fill=ACC, width=4)
    prev = p
d.ellipse([B[0] - 16, B[1] - 16, B[0] + 16, B[1] + 16], fill=(214, 232, 58), outline=(157, 170, 31), width=3)
im.save(OUT + "/og-image.png")
print("magnolia assets ok")
