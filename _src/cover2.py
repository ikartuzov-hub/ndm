# -*- coding: utf-8 -*-
"""OG-обложка выпуска 2 «Subsídio de Mobilidade — O pedido em cinco passos».
Запуск из корня: python3 _src/cover2.py  →  subsidio/og-image.png"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
BG   = (250, 246, 241)
INK  = (26, 21, 18)
SOFT = (107, 92, 81)
ACC  = (178, 58, 14)
ACCS = (246, 227, 216)
LINE = (230, 217, 204)
LIN2 = (214, 196, 179)
PAPER= (255, 255, 255)

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

def mark(ox, oy, s, col):
    w = max(2, int(7 * s))
    d.line([(ox + 33*s, oy + 18*s), (ox + 33*s, oy + 70*s)], fill=col, width=w)
    bb = [ox + (33-45)*s, oy + (44-26)*s, ox + (33+45)*s, oy + (44+26)*s]
    d.arc(bb, -90, 90, fill=col, width=w)
    pts = [(ox + (20 + t/60*60)*s, oy + (86 - 6*math.sin(t/60*2*math.pi))*s) for t in range(61)]
    d.line(pts, fill=col, width=w, joint="curve")

mark(X - 4, 46, 0.46, ACC)
d.text((X + 44, 50), "nDm", font=lora(27, True), fill=INK)

d.text((X, 128), "S U B S Í D I O   D E   M O B I L I D A D E", font=mono(19), fill=ACC)
d.text((X, 166), "O pedido em cinco passos", font=lora(68, True), fill=INK)
d.text((X, 268), "Cada ecrã do portal, cada campo — e a fatura", font=popp(28), fill=SOFT)
d.text((X, 308), "da TAP ao lado, com os sete números que se copiam", font=popp(28), fill=SOFT)
d.text((X, 364), "SeedWave · Igor Kartuzov · Madeira   ·   PT EN RU DE ES",
       font=popp(20), fill=SOFT)

# ---------- portal band: five steps + reembolso -----------------------
BX, BY, BR, BB = 82, 414, 1118, 606
d.rounded_rectangle([BX, BY, BR, BB], radius=8, fill=PAPER, outline=LIN2, width=2)
# perforated accent stripe (as on the site's calc card)
y = BY + 12
while y < BB - 12:
    d.rectangle([BX + 3, y, BX + 8, min(y + 10, BB - 12)], fill=ACC)
    y += 18

steps = ["Beneficiário", "IBAN", "Viagem", "Passageiros", "Próximos passos"]
sx, sy = BX + 64, BY + 46
gap = 128
for i, s in enumerate(steps):
    cx = sx + i * gap
    lit = i < 4
    if i < len(steps) - 1:
        d.line([(cx + 16, sy), (cx + gap - 16, sy)], fill=LIN2 if i >= 3 else ACC, width=2)
    d.ellipse([cx - 16, sy - 16, cx + 16, sy + 16], outline=ACC, width=2, fill=ACCS if lit else PAPER)
    d.text((cx - 5, sy - 10), str(i + 1), font=mono(16), fill=ACC)
    tw = d.textlength(s, font=mono(12, False))
    d.text((cx - tw / 2, sy + 26), s, font=mono(12, False), fill=SOFT)

# right: the three portal totals
TX = BX + 700
def row(y, label, value, big=False, col=INK):
    d.text((TX, y), label, font=mono(13, False), fill=SOFT)
    f = mono(26) if big else mono(19)
    vw = d.textlength(value, font=f)
    d.text((BR - 34 - vw, y - (6 if big else 2)), value, font=f, fill=col)
row(BY + 30, "CUSTO", "444,15 €")
row(BY + 68, "COPAGAMENTO", "− 79,00 €")
d.line([(TX, BY + 106), (BR - 34, BY + 106)], fill=LINE, width=2)
row(BY + 124, "REEMBOLSO", "365,15 €", big=True, col=ACC)

d.text((BX + 40, BB - 44), "Pedido real · aprovado e pago · 15 dias", font=mono(13, False), fill=SOFT)

im.save("subsidio/og-image.png")
print("ok", im.size)
