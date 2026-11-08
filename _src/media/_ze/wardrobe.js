// Гардероб Зé: уровень образа по уровню проекта (принято 08.11.2026, паспорт Зé в Notion).
// Вставлять в scene.html ПОСЛЕ блока «hero Zé» (нужны переменные manRoot, legs, armL, armR) и вызвать zeLook(N).
// 1 — Простой Зé: рубашка #2F6F8F, без растительности (бюрократия для людей, гиды nDm).
// 2 — Зé-предприниматель: тёмно-синий блейзер, аккуратные усы, коричневые туфли (ИП, малый бизнес, Prazos).
// 3 — Зé-консультант / банкир: похудел и подкачался, белая рубашка, приталенный костюм, часы, кейс
//     (субсидии организаций: Painel de Apoios, Portugal 2030, Funcionamento).
function zeLook(level){
  if(level<2) return;
  if(level>=3) return zeBanker();
  const JK='#24384F';
  const jk=el('g',{},manRoot); manRoot.insertBefore(jk,armL);
  el('path',{d:'M140 470 q0 -40 40 -40 h22 l13 60 l13 -60 h22 q40 0 40 40 v150 h-150z',fill:JK},jk);
  el('path',{d:'M202 430 l13 60 l-26 -20z M228 430 l-13 60 l26 -20z',fill:'#1A2A3C'},jk);
  el('circle',{cx:215,cy:560,r:5,fill:'#C9A227'},jk);
  armL.querySelector('path').setAttribute('stroke',JK); armR.querySelector('path').setAttribute('stroke',JK);
  el('path',{d:'M190 372 q25 -14 50 0 q-12 8 -25 3 q-13 5 -25 -3z',fill:'#4A2E1E'},manRoot);   // усы
  legs.querySelectorAll('ellipse').forEach(e=>e.setAttribute('fill','#6B3B1F'));             // коричневые туфли
}
// 3 — Зé-консультант / банкир: похудел и подкачался (V-силуэт, без второго подбородка),
// белая рубашка, приталенный тёмно-синий костюм, галстук цвета акцента, платок в кармане,
// золотые часы, короткая ухоженная борода, чёрные лакированные туфли, тонкий кейс.
function zeBanker(){
  const SUIT='#1B2433', SUIT2='#121925';
  // убрать «второй подбородок» и старое туловище
  manRoot.querySelectorAll('path').forEach(p=>{if(p.getAttribute('opacity')==='0.35'||p.getAttribute('opacity')==='.35')p.remove()});
  manRoot.querySelectorAll('rect').forEach(r=>{if(r.getAttribute('fill')==='var(--teal)')r.remove()});
  // ноги стройнее, костюмные брюки, лакированные туфли
  legs.innerHTML='';
  el('rect',{x:170,y:600,width:36,height:150,rx:14,fill:SUIT},legs); el('rect',{x:224,y:600,width:36,height:150,rx:14,fill:SUIT},legs);
  el('path',{d:'M150 752 q2 -14 22 -14 h26 q10 0 10 14z M222 752 q0 -14 10 -14 h26 q20 0 22 14z',fill:'#0E0E12'},legs);
  el('path',{d:'M160 744 h18 M236 744 h18',stroke:'#fff','stroke-width':3,'stroke-linecap':'round',opacity:.5},legs);
  const body=el('g',{},manRoot); manRoot.insertBefore(body,armL);
  // белая рубашка, V-силуэт: широкие плечи, узкая талия
  el('path',{d:'M146 470 q0 -40 40 -42 h58 q40 2 40 42 l-20 150 h-98z',fill:'#FFFFFF',stroke:'#E3E6EA','stroke-width':2},body);
  // пиджак: две полы, открытая грудь
  el('path',{d:'M146 470 q0 -40 40 -42 h10 l12 66 l-10 126 h-44z',fill:SUIT},body);
  el('path',{d:'M284 470 q0 -40 -40 -42 h-10 l-12 66 l10 126 h44z',fill:SUIT},body);
  el('path',{d:'M196 428 l12 66 l-26 -32z M234 428 l-12 66 l26 -32z',fill:SUIT2},body);          // лацканы
  el('path',{d:'M215 540 v70',stroke:'#E3E6EA','stroke-width':2},body); el('circle',{cx:215,cy:556,r:2.5,fill:'#C9CDD3'},body); el('circle',{cx:215,cy:586,r:2.5,fill:'#C9CDD3'},body); // пуговицы рубашки
  el('path',{d:'M207 430 h16 l5 16 l-13 74 l-13 -74z',fill:'var(--acc)'},body);                  // галстук
  el('path',{d:'M203 430 l12 12 l12 -12',fill:'none',stroke:'#E3E6EA','stroke-width':3},body);  // воротник
  el('path',{d:'M244 512 l18 -4 l2 8 l-18 4z',fill:'#FFFFFF'},body);                             // платок в кармане
  // лицо стройнее: голова чуть уже, уши ближе
  manRoot.querySelectorAll('circle').forEach(c=>{const cx=+c.getAttribute('cx'),cy=+c.getAttribute('cy'),r=+c.getAttribute('r');
    if(cx===215&&cy===345&&r===78)c.setAttribute('transform','translate(215 345) scale(0.9 1) translate(-215 -345)');
    if(cy===350&&(cx===137||cx===293))c.setAttribute('cx',cx===137?145:285);});
  // руки в рукавах костюма, тоньше; золотые часы на левом запястье
  [armL,armR].forEach(a=>{const p=a.querySelector('path');p.setAttribute('stroke',SUIT);p.setAttribute('stroke-width',26);});
  el('rect',{x:80,y:548,width:22,height:12,rx:4,fill:'#D4AF37',transform:'rotate(-60 91 554)'},armL);
  // короткая ухоженная борода + усы
  el('path',{d:'M166 376 q6 44 49 48 q43 -4 49 -48 q-8 22 -49 24 q-41 -2 -49 -24z',fill:'#3E2617'},manRoot);
  el('path',{d:'M188 372 q27 -12 54 0 q-14 7 -27 3 q-13 4 -27 -3z',fill:'#3E2617'},manRoot);
  // тонкий кожаный кейс
  const bc=el('g',{transform:'translate(58 584)'},armL);
  el('rect',{x:-14,y:-6,width:30,height:12,rx:5,fill:'none',stroke:'#2A1C14','stroke-width':4},bc);
  el('rect',{x:-40,y:4,width:84,height:58,rx:7,fill:'#3A2416'},bc);
  el('rect',{x:-4,y:22,width:12,height:7,rx:2,fill:'#D4AF37'},bc);
}
