# -*- coding: utf-8 -*-
"""OG-обложка /trilhos/. Запуск из корня: python3 _src/trilhos-og.py"""
import math, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "_src")
from sigma_assets import mark

ACC = (46, 125, 79); BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (107, 92, 81)
G = "/usr/share/fonts/truetype/google-fonts/"; D = "/usr/share/fonts/truetype/dejavu/"


def lora(sz):
    f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
    try:
        f.set_variation_by_axes([700])
    except Exception:
        pass
    return f


W, H = 1200, 630
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im); X = 82
mark(d, 0.5, ACC, X - 6, 44)
d.text((X + 48, 52), "SIMplifica · nDm", font=lora(26), fill=INK)
d.text((X, 140), "P E R C U R S O S   P E D E S T R E S", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 19), fill=ACC)
d.text((X, 176), "Reservar um trilho", font=lora(66), fill=INK)
d.text((X, 256), "na Madeira", font=lora(66), fill=INK)
pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 28)
d.text((X, 364), "Residente 0 € · visitante 4,50 €", font=pop, fill=SOFT)
d.text((X, 404), "Passo a passo no SIMplifica. PT · EN · RU · DE · ES", font=pop, fill=SOFT)
d.text((X, 520), "ajuda.seedwave.pt/trilhos", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=ACC)
# горный профиль и тропа справа
d.polygon([(760, 560), (880, 300), (960, 400), (1060, 220), (1180, 560)], fill=(214, 232, 220))
pts = [(790 + i * 9, 540 - i * 7 + 18 * math.sin(i / 3)) for i in range(40)]
for i in range(0, len(pts) - 1, 2):
    d.line([pts[i], pts[i + 1]], fill=ACC, width=6)
d.ellipse([pts[-1][0] - 12, pts[-1][1] - 12, pts[-1][0] + 12, pts[-1][1] + 12], fill=ACC)
im.save("trilhos/og-image.png")
print("trilhos og ok")
