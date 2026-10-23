# -*- coding: utf-8 -*-
"""Иконки серий nDm: буква + волна, у каждой услуги свой цвет.
Σ — серия SIMplifica; S — серия Segurança Social (первая — CESD).

  python3 _src/sigma_assets.py <папка> <цвет знака #hex> <цвет тайла #hex> <короткое имя> <start_url> [sigma|s|cd]

Кладёт в папку icon.svg, icon-180/192/512.png и manifest.webmanifest."""
import io, json, math, os, sys
from PIL import Image, ImageDraw

SIGMA = [(68, 20), (32, 20), (52, 45), (32, 70), (68, 70)]
# S — четыре кубических сегмента в той же сетке 100×100, что Σ (концы на 20 и 70)
S_SEGS = [((68, 26), (63, 19), (55, 17), (48, 17)), ((48, 17), (37, 17), (31, 23), (32, 31)),
          ((32, 31), (33, 40), (43, 42), (50, 44)), ((50, 44), (60, 46), (68, 50), (68, 58)),
          ((68, 58), (68, 66), (60, 71), (50, 71)), ((50, 71), (42, 71), (35, 68), (31, 63))]
# Cd — Cartão (europeu de seguro) de Doença: две буквы, принято 23.10.2026 (S занята знаком SeedWave)
CD_PATHS = ['M44 29 A21 21 0 1 0 44 61', 'M76 20 L76 70', 'M76 57 A12 12 0 1 1 52 57 A12 12 0 1 1 76 57']
S_PATH = ("M68 26 C63 19 55 17 48 17 C37 17 31 23 32 31 C33 40 43 42 50 44 "
          "C60 46 68 50 68 58 C68 66 60 71 50 71 C42 71 35 68 31 63")


def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(u**3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t**3 * d
                 for a, b, c, d in zip(p0, p1, p2, p3))


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mark(d, k, col, ox=0, oy=0, glyph="sigma"):
    w = max(2, int(7 * k))
    if glyph == "s":
        for seg in S_SEGS:
            for t in range(0, 201):
                x, y = bez(*seg, t / 200)
                x, y = ox + x * k, oy + y * k
                d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=col)
    else:
        pts = [(ox + x * k, oy + y * k) for x, y in SIGMA]
        d.line(pts, fill=col, width=w, joint="curve")
        for p in (pts[0], pts[-1]):
            d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=col)
    # волна — плотной цепочкой кругов: толстая линия PIL даёт зазубрины на изгибах
    for t in range(0, 601):
        x = ox + (20 + t / 600 * 60) * k
        y = oy + (86 - 6 * math.sin(t / 600 * 2 * math.pi)) * k
        d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=col)


def build(out, acc, tile, short, start, glyph="sigma"):
    os.makedirs(out, exist_ok=True)
    A, T = rgb(acc), rgb(tile)
    paths = CD_PATHS if glyph == "cd" else [S_PATH if glyph == "s" else "M68 20 L32 20 L52 45 L32 70 L68 70"]
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="%s">'
           '<rect width="100" height="100" rx="23" fill="%s"/>'
           '<g fill="none" stroke="%s" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">%s'
           '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>\n') % (
        short, tile, acc, "".join('<path d="%s"/>' % x for x in paths))
    for size in ((180, 192, 512) if glyph == "cd" else ()):
        import cairosvg
        cairosvg.svg2png(bytestring=svg.encode(), write_to="%s/icon-%d.png" % (out, size),
                         output_width=size, output_height=size)
    for size in (() if glyph == "cd" else (180, 192, 512)):
        S = size * 4
        im = Image.new("RGB", (S, S), T)
        mark(ImageDraw.Draw(im), S / 100.0, A, glyph=glyph)
        im.resize((size, size), Image.LANCZOS).save("%s/icon-%d.png" % (out, size))
    io.open(out + "/icon.svg", "w", encoding="utf-8").write(svg)
    io.open(out + "/manifest.webmanifest", "w", encoding="utf-8").write(json.dumps({
        "name": short, "short_name": short, "start_url": start, "display": "standalone",
        "background_color": "#FAF6F1", "theme_color": "#FAF6F1",
        "icons": [{"src": start + "icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": start + "icon-512.png", "sizes": "512x512", "type": "image/png"}],
    }, ensure_ascii=False, indent=2) + "\n")
    print("sigma assets:", out, acc)


if __name__ == "__main__":
    build(*sys.argv[1:7])
