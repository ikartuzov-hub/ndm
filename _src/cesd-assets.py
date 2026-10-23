# -*- coding: utf-8 -*-
"""Картинки /cesd/: образцы GIT-53 и MG2 с вымышленными данными, схема подписи CMD,
OG-обложка и иконки. Картинки без слов — только цифры-метки, пояснения живут
в текстах страницы (_src/i18n/cesd.<язык>.js), поэтому набор один на все языки.

Запуск из корня репозитория:  python3 _src/cesd-assets.py
Нужны: pdftoppm (poppler), PIL, pypdf, reportlab. Пустые бланки — _src/cesd/*.pdf
(официальные формы Segurança Social: GIT 53/2025 и MG 2/2023)."""
import io, math, os, subprocess, sys, tempfile
import pypdf
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas

sys.path.insert(0, "_src")
from sigma_assets import mark, build as sigma

OUT = "cesd/img"
ACC = (178, 58, 14)            # фирменная терракота nDm
EU = (0, 51, 153)              # синий ЕС — карта и штамп
BG = (250, 246, 241); INK = (26, 21, 18); SOFT = (107, 92, 81)
D = "/usr/share/fonts/truetype/dejavu/"
G = "/usr/share/fonts/truetype/google-fonts/"
DPI = 150; K = DPI / 72.0
H = 841.89

# ---------- вымышленный заявитель --------------------------------------------
P = dict(name="MARIA EXEMPLO", niss="12345678901", y="1985", m="04", d="12",
         nat="Exemplo", addr="Rua do Exemplo 10, 2.º Esq.", loc="Funchal",
         cp1="9000", cp2="000", city="FUNCHAL", tel="910000000", mail="maria@exemplo.pt",
         dist="Região Autónoma da Madeira", conc="Funchal", freg="Sé",
         r1=("2026", "01", "15"), r2=("2028", "01", "15"), today=("2026", "10", "23"))


def font(sz, bold=True):
    return ImageFont.truetype(D + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), sz)


def fill_git(path):
    """Накладывает данные на GIT-53 (у бланка нет полей формы — пишем поверх)."""
    ops = {0: [], 2: []}
    y = lambda top: top + 10.3
    t = lambda pg, x, top, s: ops[pg].append(("t", x, top, s))
    def boxes(pg, xs, top, s):
        for x, ch in zip(xs, s):
            ops[pg].append(("t", x + 3.4, top, ch))
    xm = lambda pg, x, top, w, h: ops[pg].append(("x", x, top, w, h))
    t(0, 54, y(177.1), P["name"])
    boxes(0, [51.3, 65.5, 79.7, 94.0, 108.1, 122.3, 136.6, 150.8, 164.9, 179.1, 193.3], y(210), P["niss"])
    t(0, 271, y(209.9), P["y"]); t(0, 314, y(209.9), P["m"]); t(0, 338, y(209.9), P["d"])
    t(0, 407, y(209.9), P["nat"])
    t(0, 54, y(244.2), P["addr"]); t(0, 54, y(278), P["loc"])
    boxes(0, [281.2, 295.4, 309.6, 323.8], y(278), P["cp1"]); boxes(0, [341.0, 355.2, 369.4], y(278), P["cp2"])
    t(0, 391, y(278), P["city"])
    boxes(0, [50.8, 65.0, 79.2, 93.4, 107.6, 121.8, 136.0, 150.2, 164.4], y(313.3), P["tel"])
    t(0, 283, y(312.6), P["mail"])
    for x, v in zip((342, 385, 409), P["r1"]): t(0, x, y(352.1), v)
    for x, v in zip((442, 485, 509), P["r2"]): t(0, x, y(352.1), v)
    xm(0, 52.5, 429.7, 11.7, 12.5); xm(0, 141.7, 504.0, 13.2, 13.2)
    xm(0, 414.4, 504.0, 13.2, 13.2); xm(0, 52.5, 563.9, 11.7, 12.5)
    for x, v in zip((56, 99, 123), P["today"]): t(2, x, y(392.7), v)
    r = pypdf.PdfReader("_src/cesd/GIT-53.pdf"); w = pypdf.PdfWriter()
    for i, pg in enumerate(r.pages):
        if i in ops:
            b = io.BytesIO(); c = canvas.Canvas(b, pagesize=(595.276, H))
            for o in ops[i]:
                if o[0] == "t":
                    c.setFont("Helvetica", 9); c.drawString(o[1], H - o[2], o[3])
                else:
                    _, x, top, ww, hh = o; c.setLineWidth(1.3)
                    c.line(x + 2.5, H - top - hh + 2.5, x + ww - 2.5, H - top - 2.5)
                    c.line(x + 2.5, H - top - 2.5, x + ww - 2.5, H - top - hh + 2.5)
            c.save(); b.seek(0); pg.merge_page(pypdf.PdfReader(b).pages[0])
        w.add_page(pg)
    w.write(path)


def fill_mg2(path):
    r = pypdf.PdfReader("_src/cesd/MG2.pdf"); w = pypdf.PdfWriter(clone_from=r)
    w.update_page_form_field_values(w.pages[0], {
        "Nome Completo": P["name"], "NISS": P["niss"], "ano": P["y"], "mês": P["m"], "dia": P["d"],
        "Telemóvel 3": P["tel"], "Email 3": P["mail"], "Morada 2": P["addr"],
        "Localidade 2": P["loc"], "Cdigo Postal 2": P["cp1"], "Codigo postal 3  2": P["cp2"],
        "Localidade 3": P["city"], "Distrito 2": P["dist"], "Concelho 2": P["conc"],
        "Freguesia 2": P["freg"], "ano1": P["today"][0], "mês1": P["today"][1], "dia1": P["today"][2]},
        auto_regenerate=False)
    w.set_need_appearances_writer(True)
    w.write(path)


def render(pdf, page):
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-f", str(page), "-l", str(page),
                        "-singlefile", pdf, td + "/p"], check=True)
        return Image.open(td + "/p.png").convert("RGB")


def stamp(d, x0, top, w, h, k):
    """Похожий на штамп CMD блок: синий квадрат-логотип и пять строк. Данные вымышленные."""
    d.rectangle([x0, top, x0 + w, top + h], fill=(255, 255, 255))
    s = h * 0.92
    d.rounded_rectangle([x0 + 4 * k, top + (h - s) / 2, x0 + 4 * k + s * 1.5, top + (h + s) / 2],
                        radius=int(3 * k), fill=(84, 117, 166))
    cx, cy, rr = x0 + 4 * k + s * .75, top + h / 2, s * .28
    d.arc([cx - rr, cy - rr, cx + rr, cy + rr], 60, 300, fill=(255, 255, 255), width=max(2, int(3 * k)))
    f = ImageFont.truetype(D + "DejaVuSans.ttf", max(9, int(5.6 * k)))
    lines = ["Assinado por: " + P["name"].title(), "Identificação: PASRU-0000000",
             "Data: 2026-10-23 às 15:51:41", "Local: Funchal", "Motivo: Requerimento CESD"]
    tx = x0 + 4 * k + s * 1.5 + 6 * k
    for i, L in enumerate(lines):
        d.text((tx, top + 2 * k + i * h / 5.4), L, font=f, fill=INK)


def badge(d, x, y, n, r=24):
    d.ellipse([x - r, y - r, x + r, y + r], fill=ACC, outline=(255, 255, 255), width=4)
    f = font(int(r * 1.15))
    bb = d.textbbox((0, 0), str(n), font=f)
    d.text((x - (bb[2] - bb[0]) / 2 - bb[0], y - (bb[3] - bb[1]) / 2 - bb[1]), str(n), font=f, fill=(255, 255, 255))


def frame(d, box, w=5):
    d.rounded_rectangle(box, radius=10, outline=ACC, width=w)


def watermark(im):
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = font(int(im.width * 0.07))
    for yy in range(-200, im.height + 200, int(im.width * 0.38)):
        d.text((im.width * 0.12, yy), "EXEMPLO", font=f, fill=ACC + (34,))
    lay = lay.rotate(18, resample=Image.BICUBIC, center=(im.width / 2, im.height / 2))
    return Image.alpha_composite(im.convert("RGBA"), lay).convert("RGB")


def px(v):
    return v * K


def save(im, name, w=1240):
    if im.width != w:
        im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    im.save(OUT + "/" + name, quality=86)
    print("cesd img:", name, im.size)


def main():
    os.makedirs(OUT, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        g, m = td + "/g.pdf", td + "/m.pdf"
        fill_git(g); fill_mg2(m)
        g1, g3, m1 = render(g, 1), render(g, 3), render(m, 1)
    clean_g3, clean_m1 = g3.copy(), m1.copy()   # для схемы сетки — без меток

    # 01 — GIT-53, стр. 1: данные, титулярность, система
    im = g1; d = ImageDraw.Draw(im)
    frame(d, (px(48), px(172), px(564), px(195)))
    frame(d, (px(48), px(205), px(210), px(228)))
    frame(d, (px(48), px(240), px(564), px(296)))
    frame(d, (px(334), px(348), px(530), px(370)))
    frame(d, (px(48), px(424), px(160), px(446)))
    frame(d, (px(136), px(498), px(452), px(522)))
    frame(d, (px(48), px(558), px(320), px(580)))
    for n, (x, y) in enumerate([(30, 184), (30, 217), (30, 268), (316, 359), (30, 435),
                                (118, 510), (30, 569)], 1):
        badge(d, px(x), px(y), n)
    crop = im.crop((0, int(px(140)), im.width, int(px(600))))
    save(watermark(crop), "01.jpg")

    # 02 — GIT-53, стр. 3: дата и подпись (штамп в клетке 12)
    im = g3; d = ImageDraw.Draw(im)
    stamp(d, px(392), px(H - 421), px(180), px(61) * 0.98, K)
    frame(d, (px(46), px(388), px(160), px(412)))
    frame(d, (px(318), px(388), px(568), px(470)))
    # номера 8 и 9 — продолжение легенды GIT-53 со стр. 1
    badge(d, px(30), px(400), 8); badge(d, px(300), px(428), 9)
    crop = im.crop((0, int(px(270)), im.width, int(px(500))))
    save(watermark(crop), "02.jpg")

    # 03 — MG2, стр. 1 (штамп в клетке 15)
    im = m1; d = ImageDraw.Draw(im)
    stamp(d, px(392), px(H - 284), px(180), px(61) * 0.98, K)
    frame(d, (px(48), px(122), px(566), px(240)))
    frame(d, (px(48), px(250), px(566), px(320)))
    frame(d, (px(48), px(336), px(566), px(450)))
    frame(d, (px(46), px(500), px(570), px(620)))
    for n, (x, y) in enumerate([(30, 180), (30, 285), (30, 392), (30, 560)], 1):
        badge(d, px(x), px(y), n)
    crop = im.crop((0, int(px(100)), im.width, int(px(640))))
    save(watermark(crop), "03.jpg")

    # 04 — схема сетки CMD: где ляжет штамп
    save(grid_figure(clean_g3, clean_m1), "04.jpg")

    # иконки «на экран Домой» — Σ в синем ЕС, подпись CESD
    sigma("cesd", "#1D4FA0", "#EAF0FA", "CESD", "/cesd/", "s")
    og()


def grid_figure(g3, m1):
    """Две миниатюры страниц с наложенной сеткой 6×3 из сервиса подписи CMD.
    Геометрия снята с реальных подписей: клетка 9 → штамп на y 497–558 pt от низа,
    12 → 360–421, 15 → 223–284; шаг ряда 137 pt, штамп — в верхней части клетки."""
    W = 1240; pad = 40; th = (W - 3 * pad) // 2
    pages = [(g3.copy(), 12, "GIT-53 · 3"), (m1.copy(), 15, "MG2 · 1")]
    tiles = []
    for im, cell, cap in pages:
        d = ImageDraw.Draw(im, "RGBA")
        row, col = (cell - 1) // 3, (cell - 1) % 3
        for r in range(6):
            for c in range(3):
                x0, x1 = px(32 + 180 * c), px(32 + 180 * (c + 1))
                ytop = px(H - (832 - 137 * r)); ybot = ytop + px(137)
                on = (r == row and c == col)
                d.rectangle([x0, ytop, x1, ybot], outline=(29, 79, 160, 255), width=4,
                            fill=(29, 79, 160, 70) if on else (29, 79, 160, 10))
                f = font(46)
                n = str(r * 3 + c + 1)
                d.text((x0 + 16, ytop + 10), n, font=f, fill=(29, 79, 160, 255 if on else 150))
        stamp(d, px(392), px(H - (832 - 137 * row)), px(180), px(61) * 0.98, K)
        tiles.append((im.resize((th, int(im.height * th / im.width)), Image.LANCZOS), cap, cell))
    hh = max(t[0].height for t in tiles)
    out = Image.new("RGB", (W, hh + 120), BG); d = ImageDraw.Draw(out)
    for i, (t, cap, cell) in enumerate(tiles):
        x = pad + i * (th + pad)
        out.paste(t, (x, 100)); d.rectangle([x, 100, x + th, 100 + t.height], outline=(220, 210, 200), width=2)
        f = font(40)
        d.text((x, 30), cap, font=f, fill=INK)
        bx = x + th - 140
        d.rounded_rectangle([bx, 22, bx + 140, 82], radius=30, fill=ACC)
        bb = d.textbbox((0, 0), str(cell), font=f)
        d.text((bx + 70 - (bb[2] - bb[0]) / 2 - bb[0], 52 - (bb[3] - bb[1]) / 2 - bb[1]), str(cell), font=f, fill=(255, 255, 255))
    return out


def og():
    def lora(sz):
        f = ImageFont.truetype(G + "Lora-Variable.ttf", sz)
        try:
            f.set_variation_by_axes([700])
        except Exception:
            pass
        return f
    W, Hh = 1200, 630
    im = Image.new("RGB", (W, Hh), BG); d = ImageDraw.Draw(im); X = 82
    mark(d, 0.5, (29, 79, 160), X - 6, 44, glyph="s")
    d.text((X + 48, 52), "Segurança Social · nDm", font=lora(26), fill=INK)
    d.text((X, 140), "C A R T Ã O   E U R O P E U", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 19), fill=ACC)
    d.text((X, 176), "Cartão Europeu de", font=lora(60), fill=INK)
    d.text((X, 250), "Seguro de Doença", font=lora(60), fill=INK)
    pop = ImageFont.truetype(G + "Poppins-Regular.ttf", 28)
    d.text((X, 356), "Gratuito · 3 anos · quando o portal recusa", font=pop, fill=SOFT)
    d.text((X, 396), "e-Clic, GIT-53, MG2, assinatura CMD", font=pop, fill=SOFT)
    d.text((X, 520), "ajuda.seedwave.pt/cesd", font=ImageFont.truetype(D + "DejaVuSansMono-Bold.ttf", 22), fill=ACC)
    # карта справа: синий прямоугольник и круг из 12 звёзд
    cx0, cy0, cw, ch = 800, 200, 330, 208
    d.rounded_rectangle([cx0, cy0, cx0 + cw, cy0 + ch], radius=22, fill=EU)
    ox, oy, rad = cx0 + 92, cy0 + ch / 2, 58
    for i in range(12):
        a = i * math.pi / 6
        sx, sy = ox + rad * math.cos(a), oy + rad * math.sin(a)
        star(d, sx, sy, 11, (255, 204, 0))
    d.text((cx0 + 180, cy0 + 70), "CESD", font=ImageFont.truetype(D + "DejaVuSans-Bold.ttf", 44), fill=(255, 255, 255))
    d.rounded_rectangle([cx0 + 182, cy0 + 132, cx0 + 300, cy0 + 144], radius=6, fill=(90, 120, 190))
    d.rounded_rectangle([cx0 + 182, cy0 + 156, cx0 + 260, cy0 + 168], radius=6, fill=(90, 120, 190))
    im.save("cesd/og-image.png")
    print("cesd og ok")


def star(d, x, y, r, col):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    d.polygon(pts, fill=col)


if __name__ == "__main__":
    main()
