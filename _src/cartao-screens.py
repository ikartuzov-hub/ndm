from annotate2 import *

T={
'ru':{
 'e1a':'Ваша почта. Сюда придёт карта',
 'e1b':'Обе галочки обязательны. Про Порту-Санту — это нормально',
 'e1c':'Потом нажмите Seguinte',
 'e2a':'Эти поля портал заполнил сам. Просто проверьте',
 'e2b':'Этот блок не для вас. Оставьте пустым',
 'e3a':'Портал ставит эту точку сам. Это для португальцев',
 'e3b':'У вас ВНЖ — нажмите сюда',
 'e4a':'Справка, что живёте тут больше 6 месяцев',
 'e4b':'Номер вашего ВНЖ',
 'e4c':'Скан ВНЖ, обе стороны',
 'e4d':'Справка о NIF с сайта налоговой',
 'e4e':'Выберите страну из списка',
 'e5a':'Так выглядит, когда всё загружено',
 'e5b':'Нажмите Seguinte',
 'e6a':'Заявка ушла. Ждите письма',
 'e6b':'Нажмите Terminar — это закрывает окно, не заявку',
},
'pt':{
 'e1a':'O seu email. É aqui que o cartão chega',
 'e1b':'As duas caixas são obrigatórias. A referência ao Porto Santo é normal',
 'e1c':'Depois carregue em Seguinte',
 'e2a':'Estes campos vêm do perfil. Basta conferir',
 'e2b':'Este bloco não é para si. Deixe em branco',
 'e3a':'O portal marca esta opção sozinho. É para portugueses',
 'e3b':'Tem título de residência — carregue aqui',
 'e4a':'Comprovativo de que vive cá há mais de 6 meses',
 'e4b':'Número do seu título de residência',
 'e4c':'Digitalização do título, frente e verso',
 'e4d':'Certidão do NIF, do Portal das Finanças',
 'e4e':'Escolha o país da lista',
 'e5a':'É assim que fica com tudo carregado',
 'e5b':'Carregue em Seguinte',
 'e6a':'O pedido foi submetido. Aguarde o email',
 'e6b':'Carregue em Terminar — fecha a janela, não o pedido',
},
}
TITLE='Emissão do Cartão de Residente na RAM'

def build(lang):
    t=T[lang]
    # 1 Solicitação
    im,d=load('Снимок_экрана___2026-09-08_в_11_29_13.png')
    mask(d,[(510,510,900,542),(510,578,760,610)]); retitle(d,(480,300,1420,420),TITLE,40)
    n,d,W=prep(im,(470,280,1460,940),520)
    frame(d,(28,228,935,268)); frame(d,(28,296,935,336))
    frame(d,(26,340,935,406)); frame(d,(26,420,935,486))
    callout(d,W+22,180,470,t['e1a'],945,248)
    callout(d,W+22,350,470,t['e1b'],945,412)
    callout(d,W+22,540,470,t['e1c'],930,596)
    save(n,'01.jpg',lang)
    # 2 Perfil
    im,d=load('Снимок_экрана___2026-09-08_в_11_30_10.png')
    mask(d,[(508,240,900,270),(508,308,760,338),(508,376,760,406),(508,444,1000,472),(508,552,700,582),(508,620,700,650),(508,688,760,718)])
    retitle(d,(480,40,1420,150),TITLE,40)
    n,d,W=prep(im,(470,180,1460,1010),520)
    frame(d,(26,30,940,540))
    frame(d,(26,562,940,780))
    callout(d,W+22,200,470,t['e2a'],948,285)
    callout(d,W+22,600,470,t['e2b'],948,660)
    save(n,'02.jpg',lang)
    # 3 Condição
    im,d=load('Снимок_экрана___2026-09-08_в_11_30_48.png')
    mask(d,[(150,10,560,34)]); retitle(d,(40,360,925,470),TITLE,34)
    n,d,W=prep(im,(40,480,940,800),540)
    frame(d,(306,80,510,112))
    callout(d,W+20,10,490,t['e3a'],400,62,fs=24)
    callout(d,W+20,150,490,t['e3b'],518,96,fs=24)
    save(n,'03.jpg',lang)
    # 4 Documentos пустые
    im,d=load('Снимок_экрана___2026-09-08_в_11_31_44.png')
    mask(d,[(150,18,560,44)]); retitle(d,(40,95,925,205),TITLE,34)
    n,d,W=prep(im,(330,230,940,810),600)
    frame(d,(8,28,575,85)); frame(d,(8,255,570,292)); frame(d,(8,320,575,377)); frame(d,(8,425,575,482)); frame(d,(8,522,570,562))
    callout(d,W+20,14,560,t['e4a'],578,56,fs=24)
    callout(d,W+20,140,560,t['e4b'],573,273,fs=24)
    callout(d,W+20,250,560,t['e4c'],578,348,fs=24)
    callout(d,W+20,380,560,t['e4d'],578,453,fs=24)
    callout(d,W+20,500,560,t['e4e'],573,542,fs=24)
    save(n,'04.jpg',lang)
    # 5 Documentos заполнено
    im,d=load('Снимок_экрана___2026-09-08_в_11_40_40.png')
    mask(d,[(506,546,1392,580),(505,352,1400,382),(505,682,1400,712),(505,718,1400,748),(505,856,1400,886)])
    retitle(d,(480,80,1420,190),TITLE,40)
    n,d,W=prep(im,(470,222,1460,1090),520)
    frame(d,(26,38,940,168))
    frame(d,(820,822,935,858))
    callout(d,W+22,70,470,t['e5a'],948,120)
    callout(d,W+22,790,470,t['e5b'],942,840)
    save(n,'05.jpg',lang)
    # 6 Submetido
    im,d=load('Снимок_экрана___2026-09-08_в_11_42_42.png')
    mask(d,[(150,10,560,34)]); retitle(d,(40,105,925,225),TITLE,34)
    n,d,W=prep(im,(40,380,940,820),540)
    frame(d,(452,172,712,204))
    callout(d,W+20,70,490,t['e6a'],718,188,fs=24)
    callout(d,W+20,230,490,t['e6b'],860,268,fs=24)
    save(n,'06.jpg',lang)

for lg in ('ru','pt'): build(lg)
