import sys, subprocess, pathlib
import numpy as np
from playwright.sync_api import sync_playwright
FPS=25; S=pathlib.Path(sys.argv[2]); S.mkdir(parents=True,exist_ok=True)
lang=sys.argv[1]; fr=S/f'frames_{lang}'; fr.mkdir(exist_ok=True)
here=pathlib.Path(__file__).resolve().parent
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto((here/'scene.html').as_uri()); pg.wait_for_timeout(600)
    pg.evaluate(f"setLang('{lang}')"); DUR=pg.evaluate("DUR")
    n=int(DUR*FPS)
    for i in range(n):
        pg.evaluate(f"render({i/FPS})"); pg.screenshot(path=str(fr/f'{i:04d}.png'))
    b.close()
# ---- audio ----
sr=44100; a=np.zeros(int(DUR*sr))
def add(t,sig,g=1):
    i=int(t*sr); j=min(len(a),i+len(sig)); a[i:j]+=sig[:j-i]*g
def tone(f,d,dec=6):
    t=np.linspace(0,d,int(sr*d),False); env=np.exp(-dec*t)
    return (np.sin(2*np.pi*f*t)+.3*np.sin(4*np.pi*f*t))*env
def click(t0): add(t0, tone(1800,.06,60), .25); add(t0+.02, tone(900,.08,40), .15)
add(0.2, tone(660,.3,8), .15); add(0.35, tone(880,.3,8), .12)               # Zé pops in
add(1.0, tone(523,.2,10), .1); add(1.25, tone(659,.25,10), .1)               # question
for i in range(10): add(5.0+i*.32, tone(300+(i%2)*40,.12,25), .09)          # 10 searches
add(8.3, tone(196,.4,6), .16); add(8.35, tone(147,.5,6), .13)                # forgot
add(9.0, tone(660,.3,8), .15); add(9.15, tone(880,.3,8), .12)                # Zé spring
add(9.7, tone(988,.4,6), .12)                                                # phone shows
for i in range(6): add(12.3+i*.13, tone(700+i*90,.08,40), .08)              # link flies
add(13.05, tone(1318,.5,5), .14); add(13.1, tone(1760,.4,6), .08)            # ding
for i in range(7): add(13.4+i*.3, tone(500+i*60,.12,25), .1)                # items land
for i,f in enumerate([659,784,1046]): add(16.1+i*.09, tone(f,.6,4), .12)    # plate
for i in range(12): add(16.4+(i%6)*.25+(i>5), tone(1500+(i%3)*200,.12,30), .07) # sparks
click(19.4); add(20.0, tone(784,.3,8), .12); add(20.4, tone(1046,.4,6), .12) # own shelf
for i,f in enumerate([523,659,784,1046]): add(22.1+i*.12, tone(f,.9,3), .14)   # finale
add(23.6, tone(1046,1.0,2), .1); add(23.6, tone(1568,1.0,2), .07)
a=np.tanh(a*1.4)*.8
import wave
wav=S/f'audio_{lang}.wav'
with wave.open(str(wav),'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype('<i2').tobytes())
out9=S/f'biblioteca_ze_{lang}_9x16.mp4'; out1=S/f'biblioteca_ze_{lang}_1x1.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',str(fr/'%04d.png'),'-i',str(wav),
  '-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(out9)],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(out9),'-vf','crop=1080:1080:0:420,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',str(out1)],check=True)
print(out9, out9.stat().st_size//1024,'KB;', out1, out1.stat().st_size//1024,'KB')
