# -*- coding: utf-8 -*-
"""Картинка 1:1 «39 → 14 dias» для постов CESD-2 (PT/RU/EN). python3 card3914.py <outdir>"""
import sys, pathlib
from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/google-fonts/"; D="/usr/share/fonts/truetype/dejavu/"
BG=(250,246,241); INK=(26,21,18); SOFT=(107,92,81); ACC=(178,58,14); ACCS=(246,227,216); EU=(0,51,153); GOLD=(255,204,0); OK=(30,122,70); OKS=(221,243,229); LINE=(230,217,204)
def lora(sz,bold=True):
    f=ImageFont.truetype(G+"Lora-Variable.ttf",sz)
    try: f.set_variation_by_axes([700 if bold else 500])
    except Exception: pass
    return f
def popp(sz,w="Regular"): return ImageFont.truetype(G+"Poppins-%s.ttf"%w,sz)
def dj(sz,bold=False): return ImageFont.truetype(D+("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"),sz)
def mono(sz): return ImageFont.truetype(D+"DejaVuSansMono-Bold.ttf",sz)
T={
 "pt":dict(top="CARTÃO EUROPEU DE SEGURO DE DOENÇA · MADEIRA", h="Dois pedidos.\nDois prazos.", a="1.º pedido", b="2.º pedido", a2="formulários depois\nde a Segurança Social pedir", b2="formulários enviados\nlogo no 1.º contacto", unit="dias", why="A recusa online era o título antigo na base.\nMG2 + título novo — e o formulário abre.", url="ajuda.seedwave.pt/cesd/lite", ai="imagem criada com IA"),
 "ru":dict(top="ЕВРОПЕЙСКАЯ МЕДКАРТА · МАДЕЙРА", h="Две заявки.\nДва срока.", a="1-я заявка", b="2-я заявка", a2="бланки — после\nзапроса Segurança Social", b2="бланки — сразу\nс первым обращением", unit="дней", why="Онлайн-отказ был из-за старого ВНЖ в базе.\nMG2 + новый ВНЖ — и форма открылась.", url="ajuda.seedwave.pt/cesd/lite/ru", ai="картинка создана с ИИ"),
 "en":dict(top="EUROPEAN HEALTH INSURANCE CARD · MADEIRA", h="Two applications.\nTwo timelines.", a="1st application", b="2nd application", a2="forms only after\nSegurança Social asked", b2="forms attached\nto the first request", unit="days", why="The online refusal was an old permit on file.\nMG2 + new permit — and the form opens.", url="ajuda.seedwave.pt/cesd/lite/en", ai="image created with AI"),
}
out=pathlib.Path(sys.argv[1]); out.mkdir(parents=True,exist_ok=True)
for lang,t in T.items():
    im=Image.new("RGB",(1080,1080),BG); d=ImageDraw.Draw(im)
    f_h = lora(78) if lang!="ru" else dj(72,True)
    f_t = popp(22,"Medium") if lang!="ru" else dj(22,True)
    f_b = popp(26) if lang!="ru" else dj(24)
    f_s = popp(24,"Medium") if lang!="ru" else dj(23,True)
    d.text((70,60),t["top"],font=mono(22),fill=EU)
    d.multiline_text((70,110),t["h"],font=f_h,fill=INK,spacing=6)
    # two columns
    for i,(lab,sub,n,col,colS) in enumerate([(t["a"],t["a2"],"39",ACC,ACCS),(t["b"],t["b2"],"14",OK,OKS)]):
        x=70+i*490; y=340
        d.rounded_rectangle([x,y,x+450,y+420],radius=28,fill=colS)
        d.text((x+30,y+28),lab,font=f_s,fill=col)
        d.text((x+30,y+80),n,font=lora(190),fill=col)
        d.text((x+30,y+300),t["unit"],font=f_s,fill=col)
        d.multiline_text((x+30,y+340),sub,font=f_b,fill=SOFT,spacing=4)
    # arrow between
    d.text((505,470),"→",font=dj(70,True),fill=INK)
    d.multiline_text((70,810),t["why"],font=f_b,fill=INK,spacing=6)
    d.rounded_rectangle([70,930,1010,1000],radius=14,fill=ACCS)
    d.text((90,948),t["url"],font=mono(30),fill=ACC)
    d.text((70,1030),t["ai"],font=mono(20),fill=SOFT)
    im.save(out/f"cesd2_39_14_{lang}.png"); print("ok",lang)
