# -*- coding: utf-8 -*-
"""Иконки и OG-обложка /aima/ — серия AIMA, буква A в фиолетовом AIMA.
Скриншоты трекера (aima/img/01–08.jpg) — статика: сняты с живого дела, личные
данные замазаны до попадания в репозиторий; исходники в репо не лежат.

Запуск из корня репозитория:  python3 _src/aima-assets.py"""
import io, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, "_src")
from sigma_assets import build as sigma, A_PATHS

ACC = (178, 58, 14); MK = (91, 42, 134)
BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (107, 92, 81)
D = "/usr/share/fonts/truetype/dejavu/"; G = "/usr/share/fonts/truetype/google-fonts/"
STAGES = ["Submetido", "Em análise", "Em decisão", "Decisão final – Deferido",
          "Cartão em produção", "Cartão emitido", "Cartão enviado", "Cartão entregue"]


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
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#5B2A86" '
           'stroke-width="7" stroke-linecap="round" stroke-linejoin="round">%s'
           '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>') % "".join('<path d="%s"/>' % x for x in A_PATHS)
    m = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=50, output_height=50))).convert("RGBA")
    im.paste(m, (X - 6, 44), m)
    d.text((X + 48, 52), "AIMA · nDm", font=lora(26), fill=INK)
    d.text((X, 140), "O  R A S T R E A D O R", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 19), fill=ACC)
    d.text((X, 176), "Onde está o meu", font=lora(60), fill=INK)
    d.text((X, 250), "processo na AIMA?", font=lora(60), fill=INK)
    pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 28)
    d.text((X, 356), "Oito etapas, da submissão ao cartão", font=pop, fill=SOFT)
    d.text((X, 396), "Sem conta · cinco minutos · o link por e-mail", font=pop, fill=SOFT)
    d.text((X, 520), "ajuda.seedwave.pt/aima", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=ACC)
    # справа: карточка трекера — восемь стадий, последняя горит
    cx, cy, cw, ch = 790, 150, 340, 330
    d.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=22, fill=(255, 255, 255), outline=(230, 217, 204), width=2)
    f = ImageFont.truetype(G + "Poppins-Regular.ttf", 17); fb = ImageFont.truetype(G + "Poppins-Bold.ttf", 17)
    d.line([cx + 34, cy + 34, cx + 34, cy + ch - 34], fill=(230, 217, 204), width=3)
    for i, s in enumerate(STAGES):
        y = cy + 30 + i * 38
        last = i == len(STAGES) - 1
        col = (31, 95, 168) if last else (46, 125, 79)
        d.ellipse([cx + 25, y, cx + 43, y + 18], fill=col)
        d.text((cx + 58, y - 2), s, font=fb if last else f, fill=INK if last else SOFT)
    im.save("aima/og-image.png")
    print("aima og ok")


if __name__ == "__main__":
    sigma("aima", "#5B2A86", "#F0E8F7", "AIMA", "/aima/", "a")
    og()
