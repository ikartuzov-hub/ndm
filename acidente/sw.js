/* nDm · /acidente/ — офлайн: страница и её значки остаются в телефоне после первого открытия.
   Сеть первой (свежий текст), без сети — из кэша. */
var C='acidente-v2';
self.addEventListener('install',function(e){self.skipWaiting();e.waitUntil(caches.open(C).then(function(c){
  return c.addAll(['/acidente/','/acidente/lite/','/acidente/icon.svg','/acidente/icon-192.png']).catch(function(){});}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x.indexOf('acidente-')===0&&x!==C;}).map(function(x){return caches.delete(x);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('fetch',function(e){var r=e.request;if(r.method!=='GET')return;var u=new URL(r.url);
  if(u.origin!==location.origin||u.pathname.indexOf('/acidente/')!==0)return;
  e.respondWith(fetch(r).then(function(res){if(res.ok){var cp=res.clone();caches.open(C).then(function(c){c.put(r,cp);});}return res;})
    .catch(function(){return caches.match(r,{ignoreSearch:true}).then(function(m){return m||caches.match('/acidente/');});}));});
