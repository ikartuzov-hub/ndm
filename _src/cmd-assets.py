# -*- coding: utf-8 -*-
"""Иконки и OG-обложка /cmd/ — «Chave Móvel Digital: número + PIN = a sua chave».
Значок — ключ + волна в бирюзе #0E6E63 (закон серии: знак + волна).

Запуск из корня репозитория:  python3 _src/cmd-assets.py"""
import io, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "_src")
from sigma_assets import build as sigma, KEY_PATHS

TEAL = (14, 110, 99); GOLD = (227, 162, 26); GOLDS = (253, 241, 214); TEALS = (224, 242, 238)
BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (94, 82, 72)
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
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#0E6E63" '
           'stroke-width="7" stroke-linecap="round" stroke-linejoin="round">%s'
           '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>') % "".join('<path d="%s"/>' % x for x in KEY_PATHS)
    m = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=50, output_height=50))).convert("RGBA")
    im.paste(m, (X - 6, 44), m)
    d.text((X + 48, 52), "Chave · nDm", font=lora(26), fill=INK)
    d.text((X, 140), "C H A V E   M Ó V E L   D I G I T A L", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 19), fill=TEAL)
    d.text((X, 176), "Onde está a minha", font=lora(60), fill=INK)
    d.text((X, 250), "chave?", font=lora(60), fill=INK)
    pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 28)
    d.text((X, 350), "Não é um cartão nem uma app:", font=pop, fill=SOFT)
    d.text((X, 390), "é o seu número + o seu PIN", font=ImageFont.truetype(G + "Poppins-Bold.ttf", 28), fill=INK)
    d.text((X, 520), "ajuda.seedwave.pt/cmd", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=TEAL)
    # справа: формула телефон + PIN = ключ
    fx = 720
    big = ImageFont.truetype(G + "Poppins-Bold.ttf", 46)
    mono = ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 26)
    d.rounded_rectangle([fx, 150, fx + 400, 240], radius=24, fill=TEALS, outline=TEAL, width=3)
    d.rounded_rectangle([fx + 24, 166, fx + 56, 224], radius=8, outline=TEAL, width=4)
    d.text((fx + 76, 178), "9•• ••• •••", font=mono, fill=INK)
    d.text((fx + 182, 246), "+", font=big, fill=SOFT)
    d.rounded_rectangle([fx, 310, fx + 400, 400], radius=24, fill=TEALS, outline=TEAL, width=3)
    d.text((fx + 28, 336), "PIN", font=ImageFont.truetype(G + "Poppins-Bold.ttf", 26), fill=TEAL)
    d.text((fx + 110, 334), "• • • •", font=mono, fill=INK)
    d.text((fx + 182, 404), "=", font=big, fill=SOFT)
    # ключ
    k = Image.new("RGBA", (400, 120), (0, 0, 0, 0)); kd = ImageDraw.Draw(k)
    kd.ellipse([20, 20, 100, 100], fill=GOLDS, outline=GOLD, width=14)
    kd.rounded_rectangle([96, 53, 380, 67], radius=7, fill=GOLD)
    kd.rounded_rectangle([300, 53, 314, 104], radius=7, fill=GOLD)
    kd.rounded_rectangle([352, 53, 366, 94], radius=7, fill=GOLD)
    im.paste(k, (fx, 466), k)
    im.save("cmd/og-image.png")
    print("cmd og ok")


if __name__ == "__main__":
    sigma("cmd", "#0E6E63", "#E0F2EE", "Chave", "/cmd/", "key")
    og()
