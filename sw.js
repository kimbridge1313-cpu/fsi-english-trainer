/* FSI Lab PWA — versioned static lesson cache. No user records leave the device. */
const CACHE_NAME='fsi-lab-offline-v1';
const CACHE_PREFIX='fsi-lab-offline-';
const CORE=['/','/index.html','/curriculum/index.json','/manifest.webmanifest','/icon.svg','/icons/icon-192.png','/icons/icon-512.png','/icons/apple-touch-icon.png'];
const lessonPath = path => typeof path==='string' && /^curriculum\/lessons\/[a-z0-9-]+\.json$/.test(path) ? '/'+path : null;
async function seedCache(){
  const cache=await caches.open(CACHE_NAME);
  await cache.addAll(CORE);
  const cached=await cache.match('/curriculum/index.json');
  const manifest=await cached.json();
  const paths=(manifest.lessons||[]).map(lesson=>lessonPath(lesson.file)).filter(Boolean);
  await cache.addAll(paths);
}
async function cacheNewLessons(){
  const cache=await caches.open(CACHE_NAME);
  const response=await fetch('/curriculum/index.json',{cache:'no-store'});
  if(!response.ok)throw new Error('Unable to refresh offline course catalog');
  await cache.put('/curriculum/index.json',response.clone());
  const manifest=await response.json();
  const paths=(manifest.lessons||[]).map(lesson=>lessonPath(lesson.file)).filter(Boolean);
  await Promise.allSettled(paths.map(async path=>{
    if(await cache.match(path))return;
    const item=await fetch(path);
    if(!item.ok)throw new Error('Unable to cache '+path);
    await cache.put(path,item);
  }));
}
self.addEventListener('install',event=>{
  event.waitUntil((async()=>{await seedCache();await self.skipWaiting();})());
});
self.addEventListener('activate',event=>{
  event.waitUntil((async()=>{
    for(const key of await caches.keys()){
      if(key.startsWith(CACHE_PREFIX)&&key!==CACHE_NAME)await caches.delete(key);
    }
    await self.clients.claim();
  })());
});
self.addEventListener('message',event=>{
  if(event.data&&event.data.type==='CACHE_NEW_LESSONS')event.waitUntil(cacheNewLessons().catch(err=>console.warn('Offline lesson refresh failed',err)));
});
self.addEventListener('fetch',event=>{
  const request=event.request;
  if(request.method!=='GET')return;
  const url=new URL(request.url);
  if(url.origin!==self.location.origin || url.pathname==='/sw.js')return;
  const supported=request.mode==='navigate'||url.pathname==='/curriculum/index.json'||url.pathname.startsWith('/curriculum/lessons/')||url.pathname==='/manifest.webmanifest'||url.pathname==='/icon.svg'||url.pathname.startsWith('/icons/');
  if(!supported)return;
  event.respondWith((async()=>{
    const cache=await caches.open(CACHE_NAME);
    try{
      const response=await fetch(request);
      if(response.ok)await cache.put(request,response.clone());
      return response;
    }catch(err){
      const cached=await cache.match(request,{ignoreSearch:true});
      if(cached)return cached;
      if(request.mode==='navigate'){
        const home=await cache.match('/')||await cache.match('/index.html');
        if(home)return home;
      }
      return new Response('Offline content not available. Connect to the internet once to cache this lesson.',{status:503,headers:{'Content-Type':'text/plain; charset=utf-8'}});
    }
  })());
});
