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
for i in range(12): add(1.0+i*.09, tone(1400+i*50,.2,16), .12)         # stars
add(2.1, tone(880,.5,5), .15)                                          # card tag
click(4.6); add(5.4, tone(330,.5,6), .18); add(5.5, tone(262,.6,6), .18)  # click 1, refuse buzz
add(6.8, tone(220,.8,3), .12)                                          # sigh
for i in range(3): add(9.0+i*.9, tone(1000+i*120,.25,14), .14)          # docs whoosh
add(11.8, tone(500,.15,30), .25); add(11.85, tone(380,.2,20), .2)        # stamp
for i in range(14): add(13.1+i*.09, tone(1200,.05,60), .08)             # day dots
add(14.3, tone(784,.5,5), .16); add(14.3, tone(1046,.5,5), .1)           # 14 days
click(16.0); add(16.6, tone(1046,.5,4), .2); add(16.75, tone(1318,.6,4), .14)  # click 2, ok
for i,f in enumerate([523,659,784,1046]): add(17.5+i*.12, tone(f,.9,3), .14)   # ta-da
add(19.0, tone(1046,1.0,2), .1); add(19.0, tone(1568,1.0,2), .07)
a=np.tanh(a*1.4)*.8
import wave
wav=S/f'audio_{lang}.wav'
with wave.open(str(wav),'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype('<i2').tobytes())
out9=S/f'cesd2_{lang}_9x16.mp4'; out1=S/f'cesd2_{lang}_1x1.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',str(fr/'%04d.png'),'-i',str(wav),
  '-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(out9)],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(out9),'-vf','crop=1080:1080:0:420,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',str(out1)],check=True)
print(out9, out9.stat().st_size//1024,'KB;', out1, out1.stat().st_size//1024,'KB')
