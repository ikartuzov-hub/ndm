# -*- coding: utf-8 -*-
"""Иконки и OG-обложка /renda/ — «Renda até 2 300 €: IRS 10 % em vez de 25 %».
Значок — домик + волна в терракоте #A8461F (закон серии: знак + волна).

Запуск из корня репозитория:  python3 _src/renda-assets.py"""
import io, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "_src")
from sigma_assets import build as sigma, HOUSE_PATHS

TER = (168, 70, 31); TERS = (251, 233, 223); GREEN = (14, 110, 99); GREENS = (224, 242, 238)
BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (94, 82, 72); GOLD = (227, 162, 26); GOLDS = (253, 241, 214)
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
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#A8461F" '
           'stroke-width="7" stroke-linecap="round" stroke-linejoin="round">%s'
           '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>') % "".join('<path d="%s"/>' % x for x in HOUSE_PATHS)
    m = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=50, output_height=50))).convert("RGBA")
    im.paste(m, (X - 6, 44), m)
    d.text((X + 48, 52), "Renda · nDm", font=lora(26), fill=INK)
    d.text((X, 140), "I R S   ·   A R R E N D A M E N T O", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 19), fill=TER)
    d.text((X, 176), "Renda até 2 300 €:", font=lora(56), fill=INK)
    d.text((X, 246), "IRS de 25 % para 10 %", font=lora(50), fill=INK)
    pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 28)
    d.text((X, 350), "Baixar a renda pode render mais", font=pop, fill=SOFT)
    d.text((X, 390), "ao senhorio. Faça a conta.", font=ImageFont.truetype(G + "Poppins-Bold.ttf", 28), fill=INK)
    d.text((X, 520), "ajuda.seedwave.pt/renda", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=TER)
    # справа: две полосы «на руках за год»
    fx = 760; mono = ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22); pb = ImageFont.truetype(G + "Poppins-Bold.ttf", 26)
    d.text((fx, 160), "2 500 € · 25 %", font=pb, fill=SOFT)
    d.rounded_rectangle([fx, 200, fx + int(360 * 22500 / 25000), 262], radius=16, fill=TER)
    d.text((fx + 18, 218), "22 500 €", font=mono, fill=(255, 255, 255))
    d.text((fx, 300), "2 300 € · 10 %", font=pb, fill=SOFT)
    d.rounded_rectangle([fx, 340, fx + int(360 * 24840 / 25000), 402], radius=16, fill=GREEN)
    d.text((fx + 18, 358), "24 840 €", font=mono, fill=(255, 255, 255))
    d.rounded_rectangle([fx, 440, fx + 360, 500], radius=16, fill=GOLDS, outline=GOLD, width=3)
    d.text((fx + 22, 452), "+2 340 € / ano", font=pb, fill=INK)
    im.save("renda/og-image.png")
    print("renda og ok")


if __name__ == "__main__":
    sigma("renda", "#A8461F", "#FBE9DF", "Renda", "/renda/", "house")
    og()
