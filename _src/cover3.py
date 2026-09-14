# -*- coding: utf-8 -*-
"""OG-обложка корня домена — «Damos o Caminho».
Запуск из корня: python3 _src/cover3.py  →  og-image.png"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
BG   = (250, 246, 241)
INK  = (26, 21, 18)
SOFT = (107, 92, 81)
ACC  = (178, 58, 14)
LINE = (230, 217, 204)
LIN2 = (214, 196, 179)
WATER= (94, 127, 147)

G = "/usr/share/fonts/truetype/google-fonts/"
D = "/usr/share/fonts/truetype/dejavu/"

def lora(sz, bold=False):
    f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
    try: f.set_variation_by_axes([700 if bold else 500])
    except Exception: pass
    return f
def popp(sz, w="Regular"): return ImageFont.truetype(G + "Poppins-%s.ttf" % w, sz)
def mono(sz, bold=True):
    return ImageFont.truetype(D + ("DejaVuSansMono-Bold.ttf" if bold else "DejaVuSansMono.ttf"), sz)

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)
X = 82

# ---------- brandmark ---------------------------------------------------
def mark(ox, oy, s, col):
    w = max(2, int(7 * s))
    d.line([(ox + 33*s, oy + 18*s), (ox + 33*s, oy + 70*s)], fill=col, width=w)
    bb = [ox + (33-45)*s, oy + (44-26)*s, ox + (33+45)*s, oy + (44+26)*s]
    d.arc(bb, -90, 90, fill=col, width=w)
    pts = [(ox + (20 + t/60*60)*s, oy + (86 - 6*math.sin(t/60*2*math.pi))*s) for t in range(61)]
    d.line(pts, fill=col, width=w, joint="curve")

mark(X - 4, 46, 0.46, ACC)
d.text((X + 44, 50), "nDm", font=lora(27, True), fill=INK)

# ---------- title -------------------------------------------------------
d.text((X, 132), "S U B S Í D I O   D E   M O B I L I D A D E", font=mono(19), fill=ACC)
d.text((X, 172), "Damos o Caminho", font=lora(74, True), fill=INK)
d.text((X, 288), "Tem direito? Três perguntas.", font=popp(28), fill=SOFT)
d.text((X, 328), "Depois, o guia — passo a passo, com imagens.", font=popp(28), fill=SOFT)

# ---------- flight: FNC → LIS ------------------------------------------
A  = (X + 26, 470)          # Funchal
B  = (X + 470, 430)         # Lisboa
C  = (X + 250, 392)         # control point of the arc

def bez(t):
    return ((1-t)**2*A[0] + 2*(1-t)*t*C[0] + t*t*B[0],
            (1-t)**2*A[1] + 2*(1-t)*t*C[1] + t*t*B[1])

# dashed trail
seg, gap, t = 0.028, 0.018, 0.0
while t < 1.0:
    p, q = bez(t), bez(min(1.0, t + seg))
    d.line([p, q], fill=ACC, width=3)
    t += seg + gap

for p, label, dy in ((A, "FNC", 22), (B, "LIS", -34)):
    d.ellipse([p[0]-8, p[1]-8, p[0]+8, p[1]+8], fill=ACC)
    tw = d.textlength(label, font=mono(17))
    d.text((p[0] - tw/2, p[1] + dy), label, font=mono(17), fill=SOFT)

# payout, right of the arc
d.text((X + 540, 404), "+ 365,15 €", font=lora(46, True), fill=ACC)
d.text((X + 542, 462), "devolvidos num pedido real", font=popp(19), fill=SOFT)

# ---------- footer line -------------------------------------------------
d.line([(X, 548), (W - X, 548)], fill=LINE, width=2)
d.text((X, 568), "Gratuito, sem registo   ·   PT EN RU DE ES", font=mono(18, False), fill=SOFT)
tw = d.textlength("SeedWave · Igor Kartuzov", font=popp(19))
d.text((W - X - tw, 566), "SeedWave · Igor Kartuzov", font=popp(19), fill=SOFT)

im.save("og-image.png")
print("ok", im.size)
