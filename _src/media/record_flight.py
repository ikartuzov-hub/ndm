#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Пересборка ролика «FNC → LIS» из живой страницы nDm.

Снимает анимацию карты с корня сайта (index.html), прячет лишнее, добавляет подпись,
пишет 12 секунд и кодирует в MP4 под ленту LinkedIn (1200×630, H.264, без звука).

Запуск из корня репозитория:  python3 _src/media/record_flight.py
Результат:                    media/flight-400.mp4
Требуется:                    playwright (chromium) + ffmpeg
"""
import http.server, threading, functools, os, pathlib, subprocess, glob, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT  = ROOT / "media" / "flight-400.mp4"
TMP  = pathlib.Path("/tmp/ndm_flight_rec")

TITLE = "The €400 cap is gone since June 2026"
SUB   = "No maximum on the eligible ticket cost — the official service page still shows the old number"
URL   = "ajuda.seedwave.pt"

CSS = """
  body>*:not(.wrap):not(#capline){display:none!important}
  .wrap>*:not(main){display:none!important}
  main>*:not(:first-child){display:none!important}
  .stage>*:not(.flightbox):not(.wordmark){display:none!important}
  .top{display:none!important}
  #flight .scale{display:none!important}
  .wrap{padding-top:0!important}
  .stage{padding-top:2px!important}
  .wordmark{font-size:1.9rem!important; margin:0!important}
  .flightbox{max-width:900px;margin:-20px auto 0}
  #capline{position:fixed; left:0; right:0; bottom:30px; text-align:center; z-index:99;
    font-family:"IBM Plex Sans",system-ui,sans-serif}
  #capline b{display:block; font-family:Bitter,Georgia,serif; font-size:32px; color:#1A1512; letter-spacing:-.015em}
  #capline i{display:block; font-style:normal; font-size:18px; color:#6B5C51; margin-top:10px}
  #capline s{display:block; text-decoration:none; font-family:"IBM Plex Mono",monospace;
    font-size:15px; color:#B23A0E; margin-top:14px; letter-spacing:.08em}
"""

def main():
    os.chdir(ROOT)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8931),
            functools.partial(http.server.SimpleHTTPRequestHandler))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    TMP.mkdir(exist_ok=True)
    for f in glob.glob(str(TMP / "*.webm")):
        os.remove(f)
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1200, "height": 630}, device_scale_factor=1,
                            record_video_dir=str(TMP), record_video_size={"width": 1200, "height": 630},
                            color_scheme="light")
        pg = ctx.new_page()
        pg.goto("http://127.0.0.1:8931/", wait_until="networkidle")
        pg.wait_for_timeout(1200)
        pg.evaluate("""([t,s,u]) => {
          const d=document.createElement('div'); d.id='capline';
          d.innerHTML='<b>'+t+'</b><i>'+s+'</i><s>'+u+'</s>';
          document.body.appendChild(d);
        }""", [TITLE, SUB, URL])
        pg.add_style_tag(content=CSS)
        pg.wait_for_timeout(13700)     # 3.2 с на применение стилей + 12 с полезной записи
        ctx.close(); b.close()
    srv.shutdown()
    webm = glob.glob(str(TMP / "*.webm"))[0]
    OUT.parent.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "3.2", "-i", webm, "-t", "12",
                    "-vf", "fps=25,scale=1200:630:flags=lanczos,format=yuv420p",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "20",
                    "-movflags", "+faststart", "-an", str(OUT)], check=True)
    print("готово:", OUT, OUT.stat().st_size // 1024, "КБ")

if __name__ == "__main__":
    sys.exit(main())
