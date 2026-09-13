from PIL import Image, ImageDraw
import math

ACC = (194, 74, 24)
BGT = (255, 241, 230)

def draw(size, mode):
    """mode 'tile' — знак цветом на светлом фоне; 'app' — белый знак на акценте."""
    S = size * 4
    bg = BGT if mode == "tile" else ACC
    fg = ACC if mode == "tile" else (255, 255, 255)
    im = Image.new("RGBA", (S, S), bg + (255,))
    d = ImageDraw.Draw(im)
    k = S / 100.0
    w = max(2, int(7 * k))
    d.line([(33*k, 22*k), (33*k, 68*k)], fill=fg, width=w)
    bb = [(33-40)*k, (45-23)*k, (33+40)*k, (45+23)*k]
    d.arc(bb, -90, 90, fill=fg, width=w)
    pts = []
    for i in range(61):
        t = i / 60
        x = 22 + t * 54
        y = 82 - 5 * math.sin(t * 2 * math.pi)
        pts.append((x*k, y*k))
    d.line(pts, fill=fg, width=w, joint="curve")
    return im.resize((size, size), Image.LANCZOS)

draw(180, "app").convert("RGB").save("apple-touch-icon.png")
draw(192, "app").save("icon-192.png")
draw(512, "app").save("icon-512.png")
print("icons ok")
