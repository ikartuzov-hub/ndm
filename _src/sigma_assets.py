# -*- coding: utf-8 -*-
"""Иконки серии SIMplifica: одна Σ + волна, у каждой услуги свой цвет.

  python3 _src/sigma_assets.py <папка> <цвет знака #hex> <цвет тайла #hex> <короткое имя> <start_url>

Кладёт в папку icon.svg, icon-180/192/512.png и manifest.webmanifest."""
import io, json, math, os, sys
from PIL import Image, ImageDraw

SIGMA = [(68, 20), (32, 20), (52, 45), (32, 70), (68, 70)]


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mark(d, k, col, ox=0, oy=0):
    w = max(2, int(7 * k))
    pts = [(ox + x * k, oy + y * k) for x, y in SIGMA]
    d.line(pts, fill=col, width=w, joint="curve")
    for p in (pts[0], pts[-1]):
        d.ellipse([p[0] - w / 2, p[1] - w / 2, p[0] + w / 2, p[1] + w / 2], fill=col)
    # волна — плотной цепочкой кругов: толстая линия PIL даёт зазубрины на изгибах
    for t in range(0, 601):
        x = ox + (20 + t / 600 * 60) * k
        y = oy + (86 - 6 * math.sin(t / 600 * 2 * math.pi)) * k
        d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=col)


def build(out, acc, tile, short, start):
    os.makedirs(out, exist_ok=True)
    A, T = rgb(acc), rgb(tile)
    for size in (180, 192, 512):
        S = size * 4
        im = Image.new("RGB", (S, S), T)
        mark(ImageDraw.Draw(im), S / 100.0, A)
        im.resize((size, size), Image.LANCZOS).save("%s/icon-%d.png" % (out, size))
    io.open(out + "/icon.svg", "w", encoding="utf-8").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="%s">'
        '<rect width="100" height="100" rx="23" fill="%s"/>'
        '<g fill="none" stroke="%s" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M68 20 L32 20 L52 45 L32 70 L68 70"/>'
        '<path d="M20 86 Q30 80 40 86 Q50 92 60 86 Q70 80 80 86"/></g></svg>\n' % (short, tile, acc))
    io.open(out + "/manifest.webmanifest", "w", encoding="utf-8").write(json.dumps({
        "name": short, "short_name": short, "start_url": start, "display": "standalone",
        "background_color": "#FAF6F1", "theme_color": "#FAF6F1",
        "icons": [{"src": start + "icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": start + "icon-512.png", "sizes": "512x512", "type": "image/png"}],
    }, ensure_ascii=False, indent=2) + "\n")
    print("sigma assets:", out, acc)


if __name__ == "__main__":
    build(*sys.argv[1:6])
