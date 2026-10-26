import sys, os, subprocess, pathlib, math
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
def tone(f,d,dec=6,wave='sine'):
    t=np.linspace(0,d,int(sr*d),False); env=np.exp(-dec*t)
    s=np.sin(2*np.pi*f*t)+.3*np.sin(4*np.pi*f*t); return s*env
def noise(d,dec=4):
    t=np.linspace(0,d,int(sr*d),False); n=np.random.randn(len(t))
    k=np.ones(40)/40; n=np.convolve(n,k,'same'); return n*np.exp(-dec*t)*np.sin(np.pi*t/d)
for i in range(9): add(1.2+i*.17+1.0, tone(1500+i*60,.25,14), .18)      # coins out (soft)
add(2.95, tone(220,.8,3), .15)                                            # sigh (low)
add(5.4, noise(1.8,1.5), .25); add(7.4, noise(1.8,1.5), .25)              # plane whoosh
for i in range(7): add(11+i*.32, tone(900,.08,40), .12)                    # row ticks
add(13.4, tone(660,.3,8), .15); add(13.9, tone(520,.3,8), .15)
add(14.45, tone(880,.6,4), .2); add(14.45, tone(1320,.6,4), .12)           # result
for i,t in enumerate([15.6,16.1,16.6]): add(t, tone(700+i*100,.12,30), .14) # calendar flips
add(17.05, tone(1046,.5,5), .18)
for i in range(9): add(17.9+i*.17+1.0, tone(1800+i*80,.3,12), .22)       # coins back
for i,f in enumerate([523,659,784,1046]): add(18.9+i*.12, tone(f,.9,3), .14)  # ta-da arpeggio
add(22.3, tone(1046,1.2,2), .12); add(22.3, tone(1318,1.2,2), .08); add(22.3, tone(1568,1.2,2), .08)
a=np.tanh(a*1.4)*.8
import wave, struct
wav=S/f'audio_{lang}.wav'
with wave.open(str(wav),'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype('<i2').tobytes())
out9=S/f'voos490_{lang}_9x16.mp4'; out1=S/f'voos490_{lang}_1x1.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',str(fr/'%04d.png'),'-i',str(wav),
  '-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(out9)],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(out9),'-vf','crop=1080:1080:0:420,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',str(out1)],check=True)
print(out9, out9.stat().st_size//1024,'KB;', out1, out1.stat().st_size//1024,'KB')
