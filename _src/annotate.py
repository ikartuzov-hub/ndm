from PIL import Image, ImageDraw, ImageFont
import os

SRC_A = "/tmp/claude-chrome-screenshots-BWHMfU"
SRC_B = "/mnt/user-data/outputs/tap-docs"
OUT = "/home/claude/tapguide/img"

F = lambda s, b=False: ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if b else ""), s)

RED = (214, 40, 40)
MASK = (232, 232, 232)
MASKTXT = (130, 130, 130)

def redact(d, box, label=""):
    d.rectangle(box, fill=MASK)
    if label:
        f = F(15)
        d.text((box[0] + 6, box[1] + (box[3] - box[1]) / 2 - 9), label, font=f, fill=MASKTXT)

def frame(d, box, w=3):
    d.rectangle(box, outline=RED, width=w)

def badge(d, xy, n):
    r = 17
    x, y = xy
    d.ellipse([x - r, y - r, x + r, y + r], fill=RED)
    f = F(20, True)
    t = str(n)
    bb = d.textbbox((0, 0), t, font=f)
    d.text((x - (bb[2] - bb[0]) / 2, y - (bb[3] - bb[1]) / 2 - bb[1]), t, font=f, fill="white")

def arrow(d, a, b, w=4):
    import math
    d.line([a, b], fill=RED, width=w)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    L = 14
    for s in (0.5, -0.5):
        d.line([b, (b[0] - L * math.cos(ang - s), b[1] - L * math.sin(ang - s))], fill=RED, width=w)

def build(name, src, crop, fn):
    im = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(im)
    fn(d)
    im = im.crop(crop)
    # scale to max width 1000
    if im.width > 1000:
        h = int(im.height * 1000 / im.width)
        im = im.resize((1000, h), Image.LANCZOS)
    im.save(os.path.join(OUT, name), quality=88)
    print(name, im.size)

# --- 1. empty form
def a1(d):
    frame(d, (436, 150, 788, 190)); badge(d, (410, 170), 1)
    frame(d, (436, 236, 788, 276)); badge(d, (410, 256), 2)
    frame(d, (436, 322, 788, 362)); badge(d, (410, 342), 3)
    frame(d, (538, 370, 788, 422))
build("s1.jpg", f"{SRC_A}/screenshot-1789307183642-1.jpg", (380, 70, 860, 450), a1)

# --- 2. passengers + doc types
def a2(d):
    redact(d, (156, 244, 420, 274), "PASSAGEIRO 1")
    redact(d, (156, 282, 420, 312), "PASSAGEIRO 2")
    redact(d, (596, 244, 740, 274), "047........")
    redact(d, (596, 282, 740, 312), "047........")
    redact(d, (868, 244, 950, 274), "XXXXXX")
    redact(d, (868, 282, 950, 312), "XXXXXX")
    frame(d, (130, 230, 1090, 320))
    frame(d, (132, 428, 560, 462)); badge(d, (118, 445), 1)
    frame(d, (536, 458, 910, 492), 4); badge(d, (118, 475), 2)
    frame(d, (132, 488, 560, 520)); badge(d, (118, 504), 3)
    arrow(d, (700, 530), (760, 495))
build("s2.jpg", f"{SRC_B}/tap-2b-dados-fiscais-diferentes.jpg", (90, 150, 1130, 640), a2)

# --- 3. two NIF
def a3(d):
    redact(d, (143, 236, 400, 266), "PASSAGEIRO 1")
    redact(d, (143, 262, 400, 286), "047........")
    redact(d, (143, 430, 400, 460), "PASSAGEIRO 2")
    redact(d, (143, 456, 400, 480), "047........")
    frame(d, (468, 321, 756, 361)); badge(d, (442, 341), 1)
    frame(d, (468, 515, 756, 555)); badge(d, (442, 535), 2)
build("s3.jpg", f"{SRC_B}/tap-3b-dois-nifs.jpg", (100, 190, 1130, 670), a3)

# --- 4. two emails
def a4(d):
    redact(d, (143, 186, 400, 214), "PASSAGEIRO 1")
    redact(d, (143, 216, 400, 236), "047........")
    redact(d, (468, 272, 756, 310), "NIF")
    redact(d, (143, 358, 543, 396), "NOME (automatico)")
    redact(d, (143, 554, 400, 582), "PASSAGEIRO 2")
    redact(d, (143, 584, 400, 604), "047........")
    redact(d, (468, 640, 756, 678), "NIF")
    redact(d, (143, 726, 543, 764), "NOME (automatico)")
    frame(d, (468, 272, 756, 310)); badge(d, (442, 291), 1)
    frame(d, (143, 443, 543, 483)); badge(d, (130, 420), 2)
build("s4.jpg", f"{SRC_B}/tap-4b-dois-emails.jpg", (100, 150, 1130, 530), a4)

# --- 5. dados passageiros
def a5(d):
    redact(d, (143, 186, 400, 214), "PASSAGEIRO 1")
    redact(d, (143, 216, 400, 236), "047........")
    redact(d, (143, 554, 400, 582), "PASSAGEIRO 2")
    redact(d, (143, 584, 400, 604), "047........")
    frame(d, (468, 271, 756, 311), 4); badge(d, (442, 291), 1)
    frame(d, (143, 357, 543, 397)); badge(d, (130, 336), 2)
    frame(d, (143, 443, 265, 483)); badge(d, (130, 422), 3)
    frame(d, (305, 443, 592, 483))
build("s5.jpg", f"{SRC_B}/tap-5-dados-passageiros.jpg", (100, 150, 1130, 530), a5)

# --- 6. success + subsidy button
def a6(d):
    redact(d, (156, 410, 420, 434), "PASSAGEIRO 1")
    redact(d, (156, 436, 420, 460), "PASSAGEIRO 2")
    frame(d, (116, 155, 1108, 300))
    frame(d, (800, 505, 1110, 560), 5); badge(d, (778, 532), 1)
    arrow(d, (640, 600), (860, 566))
build("s6.jpg", f"{SRC_B}/tap-6-sucesso.jpg", (100, 130, 1130, 620), a6)

# --- 7. subsidy NIFs
def a7(d):
    redact(d, (144, 198, 420, 226), "PASSAGEIRO 1")
    redact(d, (144, 391, 420, 419), "PASSAGEIRO 2")
    frame(d, (144, 281, 429, 321)); badge(d, (128, 301), 1)
    frame(d, (144, 475, 429, 515)); badge(d, (128, 495), 2)
    frame(d, (849, 556, 1110, 607))
build("s7.jpg", f"{SRC_B}/tap-7-pedido-subsidio-nifs.jpg", (100, 90, 1130, 630), a7)

# --- 8. final success
def a8(d):
    redact(d, (156, 410, 420, 434), "PASSAGEIRO 1")
    redact(d, (156, 436, 420, 460), "PASSAGEIRO 2")
    frame(d, (116, 155, 1108, 300))
build("s8.jpg", f"{SRC_B}/tap-8-sucesso-subsidio.jpg", (100, 130, 1130, 500), a8)
