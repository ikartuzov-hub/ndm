# -*- coding: utf-8 -*-
"""Обложка профиля Facebook, позиционирование «В» (29.10.2026).
Запуск: python3 _src/fb-cover-v.py → _src/media/fb_cover_v.png (1640×624)."""
from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 1640, 624
BG  = (22, 19, 17)
INK = (246, 238, 228)
SOFT= (176, 160, 146)
ACC = (226, 104, 52)
TEAL= (64, 156, 160)

G = "/usr/share/fonts/truetype/google-fonts/"
D = "/usr/share/fonts/truetype/dejavu/"
def lora(sz, w=700):
    f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def popp(sz, w="Regular"): return ImageFont.truetype(G + "Poppins-%s.ttf" % w, sz)
def mono(sz): return ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", sz)

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)

# волны внизу — фирменная линия SeedWave
for k, (col, amp, ph, y0, w) in enumerate([
        (ACC, 16, 0.0, 548, 4), (TEAL, 12, 1.3, 566, 3), ((90, 78, 70), 10, 2.4, 582, 2)]):
    pts = [(x, y0 + amp * math.sin(x / 120 + ph)) for x in range(0, W + 1, 4)]
    d.line(pts, fill=col, width=w, joint="curve")

# текстовый блок — в безопасной зоне (центр, без углов под аватар)
X = 420
d.text((X, 92), "S E E D W A V E   ·   M A D E I R A",
       font=mono(20), fill=ACC)
d.text((X, 140), "Subsídios e fundos europeus", font=lora(72), fill=INK)
d.text((X, 228), "para empresas", font=lora(72), fill=INK)
d.line([(X, 340), (X + 90, 340)], fill=ACC, width=4)
d.text((X, 366), "Sistemas com IA  ·  fundador SeedWave", font=popp(34, "Medium"), fill=INK)
d.text((X, 418), "Madeira  ·  Lisboa  ·  Portugal", font=popp(30), fill=SOFT)

f = popp(22, "Medium")
t = "seedwave.pt"
d.text((W - 70 - d.textlength(t, font=f), 476), t, font=f, fill=SOFT)
f2 = popp(15)
t2 = "imagem criada com IA"
d.text((W - 70 - d.textlength(t2, font=f2), 600), t2, font=f2, fill=(110, 98, 88))

os.makedirs("_src/media", exist_ok=True)
im.save("_src/media/fb_cover_v.png", optimize=True)
print("ok")
