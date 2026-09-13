from PIL import Image, ImageDraw, ImageFont
import math, random

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

# ---------- mark ------------------------------------------------------
def mark(ox, oy, s, col):
    w = max(2, int(7 * s))
    d.line([(ox + 33*s, oy + 18*s), (ox + 33*s, oy + 70*s)], fill=col, width=w)
    bb = [ox + (33-45)*s, oy + (44-26)*s, ox + (33+45)*s, oy + (44+26)*s]
    d.arc(bb, -90, 90, fill=col, width=w)
    pts = []
    for i in range(61):
        t = i / 60
        x = 20 + t * 60
        y = 86 - 6 * math.sin(t * 2 * math.pi)
        pts.append((ox + x*s, oy + y*s))
    d.line(pts, fill=col, width=w, joint="curve")

mark(X - 4, 46, 0.46, ACC)
d.text((X + 44, 50), "nDm", font=lora(27, True), fill=INK)

# ---------- eyebrow / title / sub -------------------------------------
d.text((X, 128), "S U B S Í D I O   D E   M O B I L I D A D E", font=mono(19), fill=ACC)
d.text((X, 166), "Documentos TAP", font=lora(76, True), fill=INK)
d.text((X, 278), "Como pedir à companhia aérea a fatura", font=popp(28), fill=SOFT)
d.text((X, 318), "e o comprovativo — passo a passo", font=popp(28), fill=SOFT)
d.text((X, 374), "SeedWave · Igor Kartuzov · Madeira   ·   PT EN RU DE ES",
       font=popp(20), fill=SOFT)

# ---------- boarding-pass band ----------------------------------------
BX, BY, BR, BB = 82, 424, 1118, 606
d.rounded_rectangle([BX, BY, BR, BB], radius=8, fill=PAPER, outline=LIN2, width=2)

# barcode stripe (decorative, not a real code)
random.seed(7)
bx = BX + 26
by0, by1 = BY + 22, BB - 22
while bx < BX + 96:
    w = random.choice([2, 2, 3, 5])
    d.rectangle([bx, by0, bx + w, by1], fill=(34, 30, 27))
    bx += w + random.choice([3, 4, 6])

TX = BX + 124                      # text column inside the pass
d.text((TX, BY + 18), "BOARDING PASS", font=mono(15), fill=SOFT)
d.text((TX, BY + 42), "SILVA / MARIA MRS", font=mono(23), fill=INK)

d.text((TX, BY + 84), "TP 1694", font=mono(25), fill=INK)
d.text((TX + 124, BY + 90), "01ABR", font=mono(16), fill=SOFT)

d.text((TX, BY + 124), "FROM  FUNCHAL (FNC)", font=mono(16), fill=SOFT)
d.text((TX, BY + 148), "TO    LISBOA  (LIS)", font=mono(16), fill=SOFT)

# right-hand cells: exactly the two numbers the form asks for
def cell(x, y, w, label, value):
    d.rounded_rectangle([x, y, x + w, y + 58], radius=4, fill=ACCS, outline=ACC, width=2)
    d.text((x + 14, y + 8), label, font=mono(13), fill=ACC)
    d.text((x + 14, y + 28), value, font=mono(19), fill=INK)

cell(TX + 372, BY + 28, 296, "PNR", "ABC123")
cell(TX + 372, BY + 100, 296, "E-TICKET", "0471234567890")

d.text((TX + 692, BY + 40), "SEAT", font=mono(13), fill=SOFT)
d.text((TX + 692, BY + 58), "22A", font=mono(25), fill=INK)
d.text((TX + 692, BY + 106), "ECONOMY", font=mono(13), fill=SOFT)

im.save("og-image.png")
print("ok", im.size)
