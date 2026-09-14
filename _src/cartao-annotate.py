from PIL import Image, ImageDraw, ImageFont
import os, math, sys
SRC='/mnt/user-data/uploads/'
ACC=(178,58,14); MASK=(230,217,204); BG=(250,246,241); INK=(26,21,18)
def F(sz,bold=True):
    p='/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if bold else '')+'.ttf'
    return ImageFont.truetype(p,sz)
def mask(d,boxes):
    for b in boxes: d.rounded_rectangle(b,radius=5,fill=MASK)
def retitle(d,box,text,size):
    d.rectangle(box,fill=(246,242,237)); f=F(size)
    bb=d.textbbox((0,0),text,font=f)
    d.text((box[0]+((box[2]-box[0])-(bb[2]-bb[0]))/2, box[1]+((box[3]-box[1])-(bb[3]-bb[1]))/2-bb[1]), text,font=f,fill=(60,50,44))
def load(name):
    im=Image.open(SRC+name).convert('RGB'); return im, ImageDraw.Draw(im)
def prep(im,crop,pad):
    im=im.crop(crop)
    n=Image.new('RGB',(im.width+pad,im.height),BG); n.paste(im,(0,0))
    d=ImageDraw.Draw(n)
    d.line([(im.width,0),(im.width,im.height)],fill=(235,226,216),width=2)
    return n,d,im.width
def wrap(d,text,f,maxw):
    out=[];line=''
    for w in text.split():
        t=(line+' '+w).strip()
        if d.textlength(t,font=f)<=maxw: line=t
        else: out.append(line); line=w
    if line: out.append(line)
    return out
def callout(d,x,y,w,text,ax,ay,n=None,fs=25):
    f=F(fs); lines=wrap(d,text,f,w-34)
    h=18+len(lines)*(fs+9)+10
    d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=(255,255,255),outline=ACC,width=3)
    ty=y+14
    for L in lines:
        d.text((x+17,ty),L,font=f,fill=INK); ty+=fs+9
    sx=x if ax<x else x+w
    sy=y+h/2
    d.line([(sx,sy),(ax,ay)],fill=ACC,width=6)
    a=math.atan2(ay-sy,ax-sx); Lh=24; s=.45
    d.polygon([(ax,ay),(ax-Lh*math.cos(a-s),ay-Lh*math.sin(a-s)),(ax-Lh*math.cos(a+s),ay-Lh*math.sin(a+s))],fill=ACC)
    if n is not None:
        r=21; d.ellipse([x-r,y+h/2-r,x+r,y+h/2+r],fill=ACC) if False else None
def frame(d,box,w=5):
    d.rounded_rectangle(box,radius=10,outline=ACC,width=w)
def save(n,name,lang,w=1240):
    out='ndm/cartao/img/%s/'%lang; os.makedirs(out,exist_ok=True)
    n=n.resize((w,int(n.height*w/n.width)),Image.LANCZOS)
    n.save(out+name,quality=88); print(lang,name,n.size)
