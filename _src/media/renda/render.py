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
for i in range(3): add(1.0+i*.5, tone(330,.25,10), .1)                      # crickets / waiting
add(4.0, tone(660,.3,8), .15); add(4.15, tone(880,.3,8), .12)                # Zé appears
add(5.0, tone(392,.2,10), .15); add(5.2, tone(311,.3,8), .15)                # Manuel shock
add(6.1, tone(250,.25,10), .15)                                             # strike
for i in range(8): add(8.2+i*.12, tone(400+i*30,.08,40), .08)               # bar 1 grows
for i in range(8): add(9.4+i*.12, tone(520+i*40,.08,40), .08)               # bar 2 grows
for i,f in enumerate([659,784,1046]): add(10.6+i*.09, tone(f,.6,4), .12)     # +2340
click(12.0)
for i in range(14): add(12.5+i*.14+.7, tone(1500+(i%3)*200,.12,30), .1)      # coins drop
add(15.7, tone(196,.4,6), .22); add(15.75, tone(147,.5,6), .18)              # alert buzz
add(16.3, tone(196,.3,6), .14)
for i,f in enumerate([523,659,784,1046]): add(18.1+i*.12, tone(f,.9,3), .14)   # finale
add(19.6, tone(1046,1.0,2), .1); add(19.6, tone(1568,1.0,2), .07)
a=np.tanh(a*1.4)*.8
import wave
wav=S/f'audio_{lang}.wav'
with wave.open(str(wav),'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype('<i2').tobytes())
out9=S/f'renda_ze_{lang}_9x16.mp4'; out1=S/f'renda_ze_{lang}_1x1.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',str(fr/'%04d.png'),'-i',str(wav),
  '-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(out9)],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(out9),'-vf','crop=1080:1080:0:420,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',str(out1)],check=True)
print(out9, out9.stat().st_size//1024,'KB;', out1, out1.stat().st_size//1024,'KB')
