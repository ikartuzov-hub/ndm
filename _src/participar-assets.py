# -*- coding: utf-8 -*-
"""Обложка /participar/ 1200×630: знак nDm, «Dê-se a conhecer 😉» и облако шести тем."""
import io, os
import cairosvg
from PIL import Image, ImageDraw, ImageFont
ACC = (178, 58, 14); BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (107, 92, 81); SW = (14, 143, 168)
D = "/usr/share/fonts/truetype/dejavu/"; G = "/usr/share/fonts/truetype/google-fonts/"
def lora(sz):
    f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
    try: f.set_variation_by_axes([700])
    except Exception: pass
    return f
os.makedirs("participar", exist_ok=True)
W, H = 1200, 630
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im); X = 82
mk = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#B23A0E" stroke-width="7" '
      'stroke-linecap="round"><path d="M30 18 L30 70"/><path d="M30 18 C62 18 74 34 72 48 C70 62 58 70 30 70"/>'
      '<path d="M18 88 Q30 82 40 88 Q50 94 60 88 Q70 82 82 88"/></g></svg>')
m = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=mk.encode(), output_width=52, output_height=52))).convert("RGBA")
im.paste(m, (X - 6, 44), m)
d.text((X + 54, 54), "nDm · SeedWave", font=lora(26), fill=INK)
d.text((X, 150), "Dê-se a conhecer", font=lora(76), fill=INK)
# подмигивающий смайлик — рисуем сами, эмодзи-шрифта в сборке может не быть
cx, cy, r = X + 700, 196, 40
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 200, 61))
d.ellipse([cx - 18, cy - 14, cx - 6, cy + 0], fill=INK)
d.arc([cx + 4, cy - 12, cx + 22, cy + 2], 200, 340, fill=INK, width=5)
d.arc([cx - 22, cy - 6, cx + 22, cy + 26], 20, 160, fill=INK, width=5)
pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 28)
d.text((X, 262), "Uma pergunta, a sua experiência, uma ideia,", font=pop, fill=SOFT)
d.text((X, 302), "procuro trabalho, posso oferecer…", font=pop, fill=SOFT)
chips = ["❓ Pergunta", "🧭 Experiência", "🎁 Apoio", "💡 Ideia", "🔎 Trabalho", "🛠 Ofereço"]
chips = [c.split(" ", 1)[1] for c in chips]
f = ImageFont.truetype(G + "Poppins-Regular.ttf", 26); x, y = X, 380
for i, c in enumerate(chips):
    w = d.textbbox((0, 0), c, font=f)[2] + 44
    if x + w > W - 70: x, y = X, y + 70
    on = i == 0
    d.rounded_rectangle([x, y, x + w, y + 54], radius=27, fill=ACC if on else (255, 255, 255), outline=ACC if on else (230, 217, 204), width=2)
    d.text((x + 22, y + 11), c, font=f, fill=(255, 255, 255) if on else INK); x += w + 12
d.text((X, 548), "ajuda.seedwave.pt/participar", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=ACC)
d.text((W - 300, 548), "gratuito", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=SW)
im.save("participar/og-image.png", optimize=True)
print("participar og")
