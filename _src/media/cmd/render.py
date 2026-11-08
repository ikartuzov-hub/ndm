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
for i in range(5): add(.8+i*.6, tone(600+i*90,.15,25), .15)                  # things fly out of drawer
for i in range(3): add(1.2+i*.4, tone(420,.2,12), .1)                       # question marks
add(4.0, tone(660,.3,8), .15); add(4.15, tone(880,.3,8), .12)                # Zé appears
add(5.0, tone(196,.4,6), .22); add(5.05, tone(147,.5,6), .18)                # big X buzz
click(7.4); click(7.7)                                                      # chips fly
for i,f in enumerate([523,659,784,1046,1318]): add(9.1+i*.07, tone(f,.7,4), .12)  # key ta-da
add(11.4, tone(260,.6,4), .12)                                              # sad / folder
add(12.3, tone(1200,.25,14), .14); add(13.1, tone(900,.3,10), .14)           # sheet pops, PIN circled
add(14.7, tone(700,.2,14), .12); add(15.5, tone(1046,.4,5), .15); add(16.05, tone(1318,.5,4), .15)  # app, key, ok
for i,f in enumerate([523,659,784,1046]): add(17.8+i*.12, tone(f,.9,3), .14)   # finale
add(19.4, tone(1046,1.0,2), .1); add(19.4, tone(1568,1.0,2), .07)
a=np.tanh(a*1.4)*.8
import wave
wav=S/f'audio_{lang}.wav'
with wave.open(str(wav),'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((a*32767).astype('<i2').tobytes())
out9=S/f'cmd_ze_{lang}_9x16.mp4'; out1=S/f'cmd_ze_{lang}_1x1.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(FPS),'-i',str(fr/'%04d.png'),'-i',str(wav),
  '-vf','format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',str(out9)],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(out9),'-vf','crop=1080:1080:0:420,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','copy','-movflags','+faststart',str(out1)],check=True)
print(out9, out9.stat().st_size//1024,'KB;', out1, out1.stat().st_size//1024,'KB')
