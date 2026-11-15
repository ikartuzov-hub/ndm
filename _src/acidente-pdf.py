# -*- coding: utf-8 -*-
"""Образец заполненного бланка Declaração Amigável на A4 — «положи в бардачок».
Бланк по-португальски (как настоящий), пояснения внизу — на языке читателя.
Случай: удар сзади на светофоре (наш, Лиссабон, ноябрь 2026); все данные вымышленные.

Кладёт acidente/daaa-exemplo-{pt,en,ru,es,de}.pdf.
Запуск из корня репозитория:  python3 _src/acidente-pdf.py"""
import io, os

NOTES = {
"pt": ("Exemplo de preenchimento — guarde no porta-luvas, junto à declaração em branco", [
 "O azul é o exemplo do que se escreve à mão. Os dados são fictícios.",
 "A e B não dizem nada sobre a culpa. Cada um preenche a sua coluna com os seus documentos; 1–5 e o croquis 13 — em conjunto.",
 "1 — data e <b>hora</b> (não deixe a hora em branco). 2 — rua e uma referência.",
 "6–9 — da apólice e da carta. Confira a matrícula com a chapa.",
 "12 — embate atrás no semáforo: quem estava parado — quadrado 1 (risque «estacionado»); quem bateu — quadrado 8. Em baixo, o número de quadrados.",
 "13 — croquis: rua, filas, setas, semáforo. 14 — as suas observações, antes de assinar.",
 "15 — assinar é concordar com os factos, não admitir culpa. Depois de assinar, nada se corrige; cada um fica com um exemplar.",
 "Depois: o verso (Participação) para a sua seguradora, em 8 dias. Feridos, desacordo ou sem declaração — 112."]),
"en": ("Sample of a filled-in form — keep it in the glovebox, next to a blank one", [
 "Blue shows what you write by hand. All data is made up.",
 "A and B say nothing about fault. Each driver fills in their own column from their own documents; 1–5 and sketch 13 — together.",
 "1 — date and <b>time</b> (don't leave the time blank). 2 — street and a landmark.",
 "6–9 — copy from the policy and the licence. Check the plate against the car.",
 "12 — hit from behind at a light: the stopped car — square 1 (cross out «estacionado»); the car that hit — square 8. At the bottom, the number of squares ticked.",
 "13 — sketch: street, lanes, arrows, traffic light. 14 — your remarks, before signing.",
 "15 — signing means agreeing on the facts, not admitting fault. Nothing is corrected after signing; each driver keeps one copy.",
 "Then: the back page (Participação) for your insurer, within 8 days. Injuries, disagreement or no form — 112."]),
"ru": ("Образец заполнения — положите в бардачок рядом с чистым бланком", [
 "Синим — то, что пишут от руки. Данные выдуманы.",
 "A и B — не про вину. Каждый заполняет свою колонку по своим документам; поля 1–5 и схему 13 — вместе.",
 "1 — дата и <b>время</b> (время не пропускать). 2 — улица и ориентир.",
 "6–9 — переписать с полиса и прав. Номер машины сверить со знаком.",
 "12 — удар сзади на светофоре: кто стоял — квадрат 1 (зачеркнуть «estacionado»), кто ударил — квадрат 8. Внизу — число отмеченных квадратов.",
 "13 — схема: улица, полосы, стрелки, светофор. 14 — свои замечания, до подписи.",
 "15 — подпись = согласие с фактами, а не признание вины. После подписи ничего не исправлять; каждому свой экземпляр.",
 "Потом: оборот (Participação) — для своей страховой, в течение 8 дней. Раненые, спор или нет бланка — 112."]),
"es": ("Ejemplo de parte rellenado — guárdalo en la guantera, junto a uno en blanco", [
 "En azul, lo que se escribe a mano. Los datos son ficticios.",
 "A y B no indican la culpa. Cada uno rellena su columna con sus documentos; 1–5 y el croquis 13, juntos.",
 "1 — fecha y <b>hora</b> (no dejes la hora en blanco). 2 — calle y una referencia.",
 "6–9 — de la póliza y del permiso. Comprueba la matrícula con la placa.",
 "12 — golpe por detrás en el semáforo: el que estaba parado — cuadro 1 (tacha «estacionado»); el que golpeó — cuadro 8. Abajo, el número de cuadros.",
 "13 — croquis: calle, carriles, flechas, semáforo. 14 — tus observaciones, antes de firmar.",
 "15 — firmar es estar de acuerdo con los hechos, no reconocer la culpa. Tras firmar no se corrige nada; cada uno se queda una copia.",
 "Después: el reverso (Participação) para tu aseguradora, en 8 días. Heridos, desacuerdo o sin parte — 112."]),
"de": ("Musterformular — ins Handschuhfach legen, neben ein leeres", [
 "Blau ist, was man von Hand schreibt. Alle Daten sind erfunden.",
 "A und B sagen nichts über die Schuld. Jeder füllt seine Spalte mit den eigenen Papieren aus; 1–5 und Skizze 13 — gemeinsam.",
 "1 — Datum und <b>Uhrzeit</b> (Uhrzeit nicht leer lassen). 2 — Straße und Bezugspunkt.",
 "6–9 — aus Police und Führerschein. Kennzeichen mit dem Schild vergleichen.",
 "12 — Auffahrunfall an der Ampel: wer stand — Kästchen 1 («estacionado» streichen); wer auffuhr — Kästchen 8. Unten die Zahl der Kreuze.",
 "13 — Skizze: Straße, Spuren, Pfeile, Ampel. 14 — eigene Bemerkungen, vor der Unterschrift.",
 "15 — Unterschrift heißt Einigkeit über Fakten, kein Schuldeingeständnis. Danach nichts mehr ändern; jeder behält ein Exemplar.",
 "Danach: Rückseite (Participação) für die eigene Versicherung, binnen 8 Tagen. Verletzte, Streit oder kein Formular — 112."]),
}

BLANK = {
"pt": ("Declaração em branco — reserva, se não houver a original", [
 "A declaração original é <b>gratuita na sua seguradora</b> — peça duas. É melhor: tem folha autocopiativa, escreve-se uma vez e fica a cópia.",
 "Esta folha é de reserva, para quando não há declaração no carro. Imprima <b>dois exemplares</b>.",
 "Preencham os dois iguais; os dois condutores assinam as duas folhas; cada um fica com uma.",
 "A seguradora aceita a participação por qualquer meio escrito (DL 291/2007, art. 35.º): o essencial são os factos iguais e as duas assinaturas.",
 "Como preencher — veja o exemplo preenchido em ajuda.seedwave.pt/acidente."]),
"en": ("Blank form — a backup if there is no original", [
 "The original form is <b>free from your insurer</b> — ask for two. It's better: it has a self-copying second sheet, you write once and get the copy.",
 "This sheet is a backup for when there's no form in the car. Print <b>two copies</b>.",
 "Fill both in identically; both drivers sign both sheets; each keeps one.",
 "Insurers accept a claim in any written form (DL 291/2007, art. 35): what matters is identical facts and both signatures.",
 "How to fill it in — see the filled-in sample at ajuda.seedwave.pt/acidente."]),
"ru": ("Чистый бланк — запасной вариант, если настоящего нет", [
 "Настоящий бланк <b>бесплатно выдаёт ваша страховая</b> — попросите два. Он удобнее: второй лист копирующий, пишете один раз — копия отпечатывается.",
 "Этот лист — запасной, на случай если бланка в машине нет. Распечатайте <b>два экземпляра</b>.",
 "Заполните оба одинаково; оба водителя подписывают оба листа; каждый забирает один.",
 "Страховая принимает заявление в любой письменной форме (DL 291/2007, ст. 35): главное — одинаковые факты и подписи обоих.",
 "Как заполнять — образец заполненного бланка на ajuda.seedwave.pt/acidente."]),
"es": ("Parte en blanco — reserva, si no hay el original", [
 "El parte original es <b>gratis en tu aseguradora</b> — pide dos. Es mejor: tiene hoja autocopiativa, escribes una vez y sale la copia.",
 "Esta hoja es de reserva, para cuando no hay parte en el coche. Imprime <b>dos ejemplares</b>.",
 "Rellenad los dos iguales; los dos conductores firman las dos hojas; cada uno se queda una.",
 "La aseguradora acepta el parte por cualquier medio escrito (DL 291/2007, art. 35): lo esencial son los mismos hechos y las dos firmas.",
 "Cómo rellenarlo — mira el ejemplo rellenado en ajuda.seedwave.pt/acidente."]),
"de": ("Leeres Formular — Reserve, falls kein Original da ist", [
 "Das Original bekommen Sie <b>kostenlos bei Ihrer Versicherung</b> — fragen Sie nach zwei. Es ist besser: Durchschreibeblatt, einmal schreiben, Kopie entsteht.",
 "Dieses Blatt ist eine Reserve, falls kein Formular im Auto liegt. <b>Zwei Exemplare</b> drucken.",
 "Beide gleich ausfüllen; beide Fahrer unterschreiben beide Blätter; jeder behält eins.",
 "Versicherer akzeptieren die Meldung in jeder schriftlichen Form (DL 291/2007, Art. 35): entscheidend sind gleiche Fakten und beide Unterschriften.",
 "Wie man es ausfüllt — siehe Musterformular auf ajuda.seedwave.pt/acidente."]),
}


CIRC = ["estava estacionado / parado", "saía de um estacionamento / abria uma porta", "ia estacionar",
 "saía de um parque, local privado ou caminho particular", "entrava num parque, local privado ou caminho particular",
 "entrava numa rotunda", "circulava numa rotunda", "embateu na traseira de outro veículo (mesmo sentido, mesma fila)",
 "circulava no mesmo sentido mas noutra fila", "mudava de fila", "ultrapassava", "virava à direita", "virava à esquerda",
 "recuava", "circulava na faixa reservada ao sentido contrário", "apresentava-se pela direita (cruzamento)",
 "não respeitou sinal de prioridade ou semáforo vermelho"]

CAR = ('<svg viewBox="0 0 60 100" width="34" height="56"><rect x="8" y="6" width="44" height="88" rx="12" fill="none" stroke="#444" stroke-width="2.5"/>'
       '<rect x="14" y="22" width="32" height="16" rx="3" fill="none" stroke="#444" stroke-width="1.5"/><rect x="14" y="64" width="32" height="12" rx="3" fill="none" stroke="#444" stroke-width="1.5"/>'
       '%s</svg>')
ARROW_REAR = '<path d="M30 140 L30 100" transform="translate(0,-38)" stroke="#1F4FB5" stroke-width="4" marker-end="url(#ah)"/><defs><marker id="ah" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="#1F4FB5"/></marker></defs>'


def col(side, d):
    hl = "#E3EEFA" if side == "A" else "#FFF5CC"
    st = "#2F6DB5" if side == "A" else "#C99A06"
    arrow = ('<path d="M30 4 L30 -18" stroke="#1F4FB5" stroke-width="4"/>' if False else "")
    # стрелка точки удара: A — сзади (низ картинки), B — спереди (верх)
    ar = ('<g stroke="#1F4FB5" stroke-width="4" fill="#1F4FB5"><path d="M30 99 L30 86"/><path d="M24 90 L30 82 L36 90 Z"/></g>' if side == "A"
          else '<g stroke="#1F4FB5" stroke-width="4" fill="#1F4FB5"><path d="M30 1 L30 14"/><path d="M24 10 L30 18 L36 10 Z"/></g>')
    ar = ar if d['ap'] else ''
    car = ('<svg viewBox="0 0 60 100" width="36" height="60"><rect x="8" y="6" width="44" height="88" rx="12" fill="none" stroke="#444" stroke-width="2.5"/>'
           '<rect x="14" y="20" width="32" height="15" rx="3" fill="none" stroke="#444" stroke-width="1.5"/><text x="30" y="58" text-anchor="middle" font-size="9" fill="#888">frente</text>%s</svg>') % ar
    return f'''<div class="col" style="--hl:{hl};--st:{st}">
<div class="cap">VEÍCULO {side}</div>
<div class="f"><b>6</b> Tomador do seguro / segurado<br>Apelido: <i>{d["ap"]}</i> · Nome: <i>{d["nm"]}</i><br>Morada: <i>{d["mo"]}</i><br>País: <i>{"Portugal" if d["ap"] else ""}</i> · Tel.: <i>{d["tel"]}</i> · NIF: <i>{d["nif"]}</i></div>
<div class="f"><b>7</b> Veículo a motor<br>Marca, modelo: <i>{d["car"]}</i><br>N.º de matrícula: <i>{d["mat"]}</i> · País: <i>{"PT" if d["ap"] else ""}</i></div>
<div class="f"><b>8</b> Companhia de seguros<br>Nome: <i>{d["seg"]}</i><br>Apólice n.º: <i>{d["ap_n"]}</i> · Carta Verde: <i>{"—" if d["ap"] else ""}</i><br>Válida de <i>{d["de"]}</i> a <i>{d["a"]}</i><br>Danos próprios cobertos? <span class="bx">{"✕" if d["dp"] is True else ""}</span> sim <span class="bx">{"✕" if d["dp"] is False else ""}</span> não</div>
<div class="f"><b>9</b> Condutor<br>Apelido: <i>{d["ap"]}</i> · Nome: <i>{d["nm"]}</i><br>Data de nasc.: <i>{d["nasc"]}</i><br>Carta de condução n.º: <i>{d["carta"]}</i> · Cat.: <i>{"B" if d["ap"] else ""}</i> · Válida até: <i>{d["val"]}</i></div>
<div class="f row"><div><b>10</b> Ponto de embate inicial</div>{car}</div>
<div class="f"><b>11</b> Danos visíveis<br><i>{d["dan"]}</i></div>
<div class="f"><b>14</b> As minhas observações<br><i>{d["obs"]}</i></div>
<div class="f sig"><b>15</b> Assinatura do condutor {side}<br><i class="s">{d["sig"]}</i></div>
</div>'''


A = dict(ap="SILVA", nm="ANA", mo="R. DO EXEMPLO 12, 1000-001 LISBOA", tel="91X XXX XXX", nif="2XXXXXXXX",
         car="MINI COOPER SE", mat="AA-00-AA", seg="SEGURADORA EXEMPLO", ap_n="0001234567", de="02/12/2025", a="21/12/2026", dp=False,
         nasc="01/01/1995", carta="L-0000001", val="2035", dan="PARA-CHOQUES TRASEIRO, CÂMARA TRASEIRA", obs="ESTAVA PARADO NO SEMÁFORO VERMELHO.", sig="Ana Silva")
B = dict(ap="SANTOS", nm="JOÃO", mo="AV. DO MODELO 3, 1100-002 LISBOA", tel="96X XXX XXX", nif="5XXXXXXXX",
         car="KIA E-NIRO", mat="BB-11-BB", seg="OUTRA SEGURADORA", ap_n="0007654321", de="23/03/2026", a="11/04/2027", dp=True,
         nasc="15/06/1988", carta="L-0000002", val="2031", dan="PARA-CHOQUES DA FRENTE", obs="—", sig="J. Santos")

SKETCH = '''<svg viewBox="0 0 220 120" width="100%" height="150">
<rect x="0" y="0" width="220" height="120" fill="#fff"/>
<rect x="0" y="30" width="220" height="60" fill="#EEE"/>
<line x1="0" y1="60" x2="220" y2="60" stroke="#999" stroke-dasharray="8 6" stroke-width="2"/>
<line x1="150" y1="62" x2="150" y2="90" stroke="#555" stroke-width="3"/>
<g transform="translate(156,2)"><rect x="0" y="0" width="12" height="26" rx="3" fill="#333"/><circle cx="6" cy="6" r="4" fill="#E53935"/><circle cx="6" cy="13" r="3" fill="#666"/><circle cx="6" cy="20" r="3" fill="#666"/></g>
<g><rect x="104" y="66" width="42" height="20" rx="5" fill="#E3EEFA" stroke="#2F6DB5" stroke-width="2"/><text x="125" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#2F6DB5">A</text></g>
<g><rect x="50" y="66" width="42" height="20" rx="5" fill="#FFF5CC" stroke="#C99A06" stroke-width="2"/><text x="71" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="#C99A06">B</text></g>
<path d="M14 76 L44 76" stroke="#1F4FB5" stroke-width="3"/><path d="M40 71 L48 76 L40 81 Z" fill="#1F4FB5"/>
<circle cx="97" cy="76" r="7" fill="none" stroke="#E53935" stroke-width="2"/>
<text x="6" y="22" font-size="10" fill="#1F4FB5" font-style="italic">AV. DAS FORÇAS ARMADAS →</text>
<text x="6" y="110" font-size="9" fill="#1F4FB5" font-style="italic">A parado no vermelho · B embate na traseira</text>
</svg>'''


def html(lang, blank=False):
    title, notes = (BLANK if blank else NOTES)[lang]
    E = {k: ('' if k != 'dp' else None) for k in A}
    SK = '<div style="height:150px"></div>' if blank else SKETCH
    def v(x):
        return '' if blank else x
    rows = "".join('<tr><td class="c"><span class="bx">%s</span></td><td class="n">%d</td><td class="t">%s</td><td class="c"><span class="bx">%s</span></td></tr>' % (
        "✕" if (i == 0 and not blank) else "", i + 1, t, "✕" if (i == 7 and not blank) else "") for i, t in enumerate(CIRC))
    nl = "".join("<li>%s</li>" % n for n in notes)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:8mm}}
*{{box-sizing:border-box}}
body{{margin:0;font:8.1pt/1.32 "DejaVu Sans",sans-serif;color:#222}}
i:empty{{display:inline-block;min-width:70px;border-bottom:1px dotted #999;height:9px}}
i{{font-style:normal;color:#1F4FB5;font-weight:700;font-family:"DejaVu Sans Mono",monospace}}
i.s{{font:italic 13pt "DejaVu Serif",serif;color:#1F4FB5}}
.hd{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #222;padding-bottom:3px;margin-bottom:4px}}
.hd h1{{font:700 11.5pt "DejaVu Sans",sans-serif;margin:0}}
.hd .st{{border:2px solid #C62828;color:#C62828;font-weight:700;padding:2px 8px;border-radius:4px;transform:rotate(-3deg);font-size:9pt}}
.sub{{font-size:8.5pt;font-weight:700;color:#B4410F;margin:0 0 4px}}
.top{{display:grid;grid-template-columns:1fr 2fr 1.2fr;gap:4px;margin-bottom:4px}}
.top2{{display:grid;grid-template-columns:1.6fr 1fr;gap:4px;margin-bottom:4px}}
.f{{border:1px solid #888;border-radius:3px;padding:4px 6px;margin-bottom:4px;background:#fff}}
.f b{{display:inline-block;background:#222;color:#fff;border-radius:2px;padding:0 4px;margin-right:3px;font-size:7pt}}
.bx{{display:inline-block;width:10px;height:10px;border:1px solid #333;text-align:center;line-height:9px;font-size:8pt;color:#1F4FB5;font-weight:700;vertical-align:middle}}
.grid{{display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:5px}}
.col{{background:var(--hl);border:1.5px solid var(--st);border-radius:5px;padding:4px}}
.cap{{font-weight:700;color:var(--st);text-align:center;margin-bottom:3px;font-size:8.5pt}}
.row{{display:flex;justify-content:space-between;align-items:center}}
.sig{{height:50px}}
table{{width:100%;border-collapse:collapse;font-size:7.4pt}}
td{{border-bottom:1px solid #ddd;padding:2.4px 2px;vertical-align:middle}}
td.c{{width:16px;text-align:center}} td.n{{width:12px;color:#777;text-align:right;padding-right:4px}}
.mid{{border:1.5px solid #555;border-radius:5px;padding:4px}}
.mid .cap{{color:#222}}
.cnt{{display:flex;justify-content:space-between;margin-top:4px;font-weight:700}}
.notes{{margin-top:5px;border:2px dashed #B4410F;border-radius:6px;padding:5px 8px 4px}}
.notes h2{{font:700 10pt "DejaVu Sans",sans-serif;margin:0 0 2px;color:#B4410F}}
.notes ol{{margin:0;padding-left:15px;font-size:8.5pt;columns:2;column-gap:14px}}
.notes li{{margin:0 0 2px;break-inside:avoid}}
.ft{{display:flex;justify-content:space-between;font-size:7pt;color:#666;margin-top:3px}}
</style></head><body>
<div class="hd"><h1>DECLARAÇÃO AMIGÁVEL DE ACIDENTE AUTOMÓVEL</h1><span class="st">{"EM BRANCO · reserva" if blank else "EXEMPLO · dados fictícios"}</span></div>
<p class="sub">{title}</p>
<div class="top">
 <div class="f"><b>1</b> Data do acidente / Hora<br><i>{v("13/11/2026 · 13:40")}</i></div>
 <div class="f"><b>2</b> Localização — País: <i>{v("PORTUGAL")}</i><br>Local: <i>{v("LISBOA, AV. DAS FORÇAS ARMADAS (SEMÁFORO)")}</i></div>
 <div class="f"><b>3</b> Feridos, mesmo ligeiros<br><span class="bx">{v("✕")}</span> não &nbsp; <span class="bx"></span> sim</div>
</div>
<div class="top2">
 <div class="f"><b>4</b> Danos materiais em veículos além de A e B: <span class="bx">{v("✕")}</span> não <span class="bx"></span> sim · em objetos: <span class="bx">{v("✕")}</span> não <span class="bx"></span> sim</div>
 <div class="f"><b>5</b> Testemunhas: <i>{v("—")}</i></div>
</div>
<div class="grid">
{col("A", E if blank else A)}
<div>
 <div class="mid"><div class="cap">12 · CIRCUNSTÂNCIAS</div>
 <table><tr><td class="c"><b style="color:#2F6DB5">A</b></td><td></td><td style="color:#777">assinale com uma cruz</td><td class="c"><b style="color:#C99A06">B</b></td></tr>{rows}</table>
 <div class="cnt"><span>A: n.º de quadrados <i>{v("1")}</i></span><span>B: <i>{v("1")}</i></span></div></div>
 <div class="f" style="margin-top:4px"><b>13</b> Croquis do acidente no momento do embate{SK}</div>
</div>
{col("B", E if blank else B)}
</div>
<div class="notes"><h2>{title}</h2><ol>{nl}</ol></div>
<div class="ft"><span>nDm · SeedWave — ajuda.seedwave.pt/acidente</span><span>112 · e-SEGURNET · ASF 217 983 983</span></div>
</body></html>'''


def main():
    from playwright.sync_api import sync_playwright
    os.makedirs("acidente", exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        for L in NOTES:
            pg.set_content(html(L), wait_until="load")
            pg.pdf(path="acidente/daaa-exemplo-%s.pdf" % L, format="A4", print_background=True,
                   margin={"top": "8mm", "bottom": "8mm", "left": "8mm", "right": "8mm"})
            pg.set_content(html(L, blank=True), wait_until="load")
            pg.pdf(path="acidente/daaa-branco-%s.pdf" % L, format="A4", print_background=True,
                   margin={"top": "8mm", "bottom": "8mm", "left": "8mm", "right": "8mm"})
            print("pdf:", L)
        br.close()


if __name__ == "__main__":
    main()
