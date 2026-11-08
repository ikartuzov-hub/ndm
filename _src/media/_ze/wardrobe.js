// Гардероб Зé: уровень образа по уровню проекта (принято 08.11.2026, паспорт Зé в Notion).
// Вставлять в scene.html ПОСЛЕ блока «hero Zé» (нужны переменные manRoot, legs, armL, armR) и вызвать zeLook(N).
// 1 — Простой Зé: рубашка #2F6F8F, без растительности (бюрократия для людей, гиды nDm).
// 2 — Зé-предприниматель: тёмно-синий блейзер, аккуратные усы, коричневые туфли (ИП, малый бизнес, Prazos).
// 3 — Зé-консультант: графитовый костюм, галстук цвета акцента серии, бородка из барбершопа, золотая папка
//     (субсидии организаций: Painel de Apoios, Portugal 2030, Funcionamento).
function zeLook(level){
  if(level<2) return;
  const JK=level>=3?'#2E2F38':'#24384F';
  const jk=el('g',{},manRoot); manRoot.insertBefore(jk,armL);
  el('path',{d:'M140 470 q0 -40 40 -40 h22 l13 60 l13 -60 h22 q40 0 40 40 v150 h-150z',fill:JK},jk);
  el('path',{d:'M202 430 l13 60 l-26 -20z M228 430 l-13 60 l26 -20z',fill:'#1A2A3C'},jk);
  el('circle',{cx:215,cy:560,r:5,fill:'#C9A227'},jk);
  armL.querySelector('path').setAttribute('stroke',JK); armR.querySelector('path').setAttribute('stroke',JK);
  if(level===2){
    el('path',{d:'M190 372 q25 -14 50 0 q-12 8 -25 3 q-13 5 -25 -3z',fill:'#4A2E1E'},manRoot);   // усы
    legs.querySelectorAll('ellipse').forEach(e=>e.setAttribute('fill','#6B3B1F'));             // коричневые туфли
  } else {
    legs.querySelectorAll('rect').forEach(e=>e.setAttribute('fill',JK));                        // брюки костюма
    el('path',{d:'M209 440 h12 l4 14 l-10 60 l-10 -60z',fill:'var(--acc)'},manRoot);            // галстук
    el('path',{d:'M160 372 q8 58 55 62 q47 -4 55 -62 q-10 30 -55 32 q-45 -2 -55 -32z',fill:'#4A2E1E'},manRoot); // бородка
    const fol=el('g',{transform:'translate(66 560) rotate(-8)'},armL);                          // папка с документами
    el('rect',{x:-6,y:-10,width:62,height:80,rx:6,fill:'#C9A227'},fol); el('rect',{x:4,y:2,width:42,height:6,rx:3,fill:'#fff',opacity:.8},fol);
  }
}
