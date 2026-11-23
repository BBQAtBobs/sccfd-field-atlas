import re
p='index.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:90]); s=s.replace(a,b)
def span(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i); s=s[:i]+new+s[j:]

# ================= draw()
span("function draw(){","\n\n/* panel */",r'''function placeSVG(p,x,y,sel,dim,wrong){
 if(p.des)return`<g class="pl h${sel?' sel':''}${dim?' dim':''}${wrong?' wrong':''}" data-p="${p.id}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><circle class="hit" r="14"/>${sel?'<circle class="pulse" r="10"/>':''}<rect x="-7.5" y="-7.5" width="15" height="15" rx="3.5"/><text dy="3.7">H</text></g>`;
 return`<g class="pl l k-${p.kind}${sel?' sel':''}${dim?' dim':''}" data-p="${p.id}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><circle class="hit" r="12"/>${sel?'<circle class="pulse" r="8"/>':''}<circle class="d" r="${sel?6:4.5}"/></g>`}
function draw(){
 const {k,tx,ty,v}=T(),now=performance.now();
 world.setAttribute('transform',`translate(${tx.toFixed(2)} ${ty.toFixed(2)}) scale(${k})`);
 const S=s=>[s.x*k+tx,s.y*k+ty];
 const boxes=[],hit=b=>boxes.some(o=>b[0]<o[2]&&b[2]>o[0]&&b[1]<o[3]&&b[3]>o[1]);
 const onScreen=(x,y,m=0)=>x>-m&&y>-m&&x<v.w+m&&y<v.full+m;
 const g=state.game,gs=g&&g.phase!=='done'?g:null,c=gs&&gs.cur,rev=!!(gs&&gs.phase==='reveal');
 const pinG=gs&&(gs.id==='pin'||gs.id==='find'),hospG=gs&&gs.id==='hosp',showSt=!gs||(!pinG&&!hospG);
 let lk='',mk='',lb='';
 const showB=state.bat||(state.sel&&state.sel.battalion);
 if(showB&&!g){const b=BAT[showB],h=byNum[b.hq];const[hx,hy]=S(h);for(const n of b.stations){if(n===b.hq)continue;const[x,y]=S(byNum[n]);lk+=`<line class="link" stroke="${bc(showB)}" x1="${hx}" y1="${hy}" x2="${x}" y2="${y}"/>`}}
 linksG.innerHTML=lk;
 // places
 let places=[];
 if(!g){if(layers.hosp)places=places.concat(PL.hospitals);if(layers.lm)places=places.concat(PL.landmarks.filter(l=>layers.kinds[l.kind]!==false));if(state.place&&!places.includes(state.place))places.push(state.place)}
 else if(hospG)places=PL.hospitals;
 for(const p of places){const[x,y]=S(p);if(!onScreen(x,y,20))continue;
  const isT=hospG&&c.kind==='which'&&p===c.t,sel=state.place===p||(hospG&&rev&&isT),wrong=hospG&&rev&&c.pick===p&&!isT;
  const dim=(!g&&state.hf&&p.des&&!p.des.includes(state.hf))||(hospG&&rev&&!sel&&!wrong);
  mk+=placeSVG(p,x,y,sel,dim,wrong);boxes.push([x-8,y-8,x+8,y+8])}
 // stations
 for(const s of ST){const[x,y]=S(s);if(showSt)boxes.push([x-15,y-15,x+15,y+15])}
 if(showSt){const order=[...ST].sort((a,b)=>(a===state.sel)-(b===state.sel));
  for(const s of order){const[x,y]=S(s);if(!onScreen(x,y,30))continue;
   if(gs){const isT=s===c.t,picked=c.pick===s;if(!inBat(s)&&!isT)continue;
    const lit=isT&&(gs.id!=='rig'||rev),wrong=rev&&picked&&!isT,big=rev&&(isT||picked);
    mk+=`<g class="mk game${lit?' sel':''}${wrong?' wrong':''}" data-n="${s.num}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><circle class="hit" r="20"/>${lit?'<circle class="pulse" r="12"/><circle class="pulse p2" r="12"/>':''}<circle class="dot" r="${big?11.5:7.5}"/>${big?`<text dy="3.9">${s.num}</text>`:''}</g>`;continue}
   const sel=s===state.sel,lv=ufLevel(s),dim=!inBat(s)||lv===0,half=!dim&&lv===1;
   mk+=`<g class="mk${sel?' sel':''}${dim&&!sel?' dim':''}${half?' half':''}" data-n="${s.num}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})" role="button" aria-label="Station ${s.num} ${esc(s.name)}"><circle class="hit" r="20"/>${sel?'<circle class="pulse" r="12"/>':''}${isHQ(s)?`<circle class="ring" r="15.5" style="stroke:${bc(s.battalion)}"/>`:''}<circle class="dot" r="11.5" style="stroke:${sel?'var(--red)':bc(s.battalion)}"/><text dy="3.9">${s.num}</text></g>`}}
 // pin reveal: animated miss line, then the answer
 if(pinG&&rev&&c.guess){const t=c.t,[x2,y2]=S(t),gx=c.guess.x*k+tx,gy=c.guess.y*k+ty,pr=reduce?1:Math.min(1,(now-c.t0)/750),e=1-(1-pr)**3,ex=gx+(x2-gx)*e,ey=gy+(y2-gy)*e;
  mk+=`<line class="miss" x1="${gx}" y1="${gy}" x2="${ex.toFixed(1)}" y2="${ey.toFixed(1)}"/><g class="guess" transform="translate(${gx} ${gy})"><circle r="7"/><circle r="2"/></g>`;
  if(pr>.82)mk+=t.num?`<g class="mk game sel" transform="translate(${x2} ${y2})"><circle class="pulse" r="12"/><circle class="pulse p2" r="12"/><circle class="dot" r="11.5"/><text dy="3.9">${t.num}</text></g>`:placeSVG(t,x2,y2,true,false,false);
  if(pr<1)sched()}
 const hq=D.facilities.find(f=>f.id==='hq');if(hq&&!g){const[x,y]=S(hq);mk+=`<g class="fac" transform="translate(${x} ${y}) rotate(45)"><rect x="-4" y="-4" width="8" height="8"/></g>`;boxes.push([x-6,y-6,x+6,y+6])}
 marksG.innerHTML=mk;
 // labels
 if(!gs){const named=[...ST].filter(s=>shown(s)||s===state.sel).sort((a,b)=>(b===state.sel)-(a===state.sel)||isHQ(b)-isHQ(a));
  for(const s of named){const[x,y]=S(s);if(!onScreen(x,y))continue;const w=s.name.length*6.9+4;
   for(const [dx,anchor] of [[17,'start'],[-17,'end']]){const bx=anchor==='start'?[x+dx,y-9,x+dx+w,y+7]:[x+dx-w,y-9,x+dx,y+7];if(s!==state.sel&&hit(bx))continue;boxes.push(bx);lb+=`<text class="name"${ufLevel(s)===1&&s!==state.sel?' opacity=".55"':''} x="${x+dx}" y="${y+4.5}" text-anchor="${anchor}">${esc(s.name)}</text>`;break}}}
 else if(rev&&(!pinG||(now-c.t0)>600)){const t=hospG?(c.kind==='which'?c.t:null):c.t;if(t){const[x,y]=S(t),nm=t.num?t.name:(t.short||t.name),w=nm.length*7;boxes.push([x+15,y-9,x+15+w,y+7]);lb+=`<text class="name" x="${x+15}" y="${y+4.5}">${esc(nm)}</text>`}}
 if(!g)for(const p of places){if(!p.des&&p!==state.place&&view.k<fitK*2.2)continue;const[x,y]=S(p);if(!onScreen(x,y))continue;const nm=p.des?p.short:p.name,w=nm.length*6.1+4,b=[x+11,y-8,x+11+w,y+6];if(p!==state.place&&hit(b))continue;boxes.push(b);lb+=`<text class="plbl${p.des?' h':''}${state.hf&&p.des&&!p.des.includes(state.hf)?' dim':''}" x="${x+11}" y="${y+4}">${esc(nm)}</text>`}
 if(hq&&!g&&view.k>fitK*3){const[x,y]=S(hq);const b=[x+9,y-8,x+82,y+6];if(!hit(b)){boxes.push(b);lb+=`<text class="lbl sc" x="${x+10}" y="${y+4}">Headquarters</text>`}}
 for(const sh of shields){let n=0;for(const cc of sh.c){const x=cc[0]*k+tx,y=cc[1]*k+ty;if(!onScreen(x,y,-20))continue;const w=sh.ref.length*6+10,b=[x-w/2-30,y-9-30,x+w/2+30,y+9+30];if(hit(b))continue;boxes.push([x-w/2-60,y-40,x+w/2+60,y+40]);lb+=`<g class="sh" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><rect x="${-w/2}" y="-8" width="${w}" height="16" rx="3"/><text dy="3.8">${sh.ref}</text></g>`;if(++n>=2)break}}
 for(const cl of cityLabels){if(!cl.at)continue;const x=cl.at[0]*k+tx,y=cl.at[1]*k+ty;if(!onScreen(x,y,-10))continue;const fs=cl.big?14:12.5,w=cl.name.length*fs*.55,b=[x-w/2,y-fs,x+w/2,y+4];if(hit(b))continue;boxes.push(b);lb+=`<text class="lbl${cl.sc?' sc':''}${cl.big?' big':''}" x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="middle">${esc(cl.name)}</text>`}
 labelsG.innerHTML=lb;
 const mpp=MPU/k,opts=[.25,.5,1,2,5,10,20];let mi=opts[0];for(const o of opts){if(o*1609.34/mpp<=130)mi=o}
 $('#scale').innerHTML=`${mi} mi<i style="width:${(mi*1609.34/mpp).toFixed(0)}px"></i>`;
}''')

# ================= places panels (insert before /* state changes */)
rep("\n\n/* state changes */",r'''
/* hospitals & landmarks */
const DES_ORDER=['trauma','trauma-peds','burn','stroke-comp','stroke','stemi','peds-adv','peds','ld','vad','safe','helipad'];
const KIND1={school:'School',park:'Park',peak:'Peak',venue:'Landmark',tech:'Tech campus',ems:'Dispatch & EMS'};
const srcPL=ids=>'<p class="src">Source: '+ids.map(i=>PL.meta.sources[i]).filter(Boolean).map(x=>`<a href="${esc(x.url)}">${esc(x.title)}</a>`).join(' · ')+'.</p>';
const desChip=(k,p)=>{const d=PL.designations[k];return`<span class="dchip${d.info?' info':''}">${esc(d.label)}${k==='trauma'&&p&&p.trauma?' · '+esc(p.trauma):''}</span>`};
function renderPlace(p){const near=ST.map(o=>[o,miles(p,o)]).sort((a,b)=>a[1]-b[1]).slice(0,3),isH=!!p.des;
 const des=isH?DES_ORDER.filter(k=>p.des.includes(k)&&!(k==='stroke'&&p.des.includes('stroke-comp'))):[];
 enter(`<div class="crumbs"><button data-act="all">All</button><span>/</span>${isH?'<button data-act="hosps">Hospitals</button>':`<span>${esc(PL.kinds[p.kind].label)}</span>`}</div>
 <div class="hero">${isH?'<span class="hbig">H</span>':`<span class="lbig k-${p.kind}"><i></i></span>`}<div><h1>${esc(p.name)}</h1><p class="addr">${esc(isH?'Hospital':KIND1[p.kind])} · ${esc(p.city)}</p></div></div>
 ${isH?`<h3>Designations</h3><div class="dchips">${des.length?des.map(k=>desChip(k,p)).join(''):'<span class="area">Emergency department only</span>'}</div>`:(p.note?`<p class="area" style="margin-top:14px">${esc(p.note)}</p>`:'')}
 ${isH&&p.note?`<p class="note">${esc(p.note)}</p>`:''}
 <div class="acts"><a href="https://www.google.com/maps/search/?api=1&query=${p.lat},${p.lon}" target="_blank" rel="noopener">Google Maps ↗</a></div>
 <h3>Closest SCCFD stations</h3>${near.map(([o,d])=>stationRow(o,d.toFixed(1)+' mi straight-line')).join('')}
 ${isH&&des.some(k=>PL.designations[k].info)?`<p class="sub">${esc(PL.meta.infoNote)}</p>`:''}
 ${srcPL(isH?['policy602','osm']:['osm'])}`)}
function renderHospitals(){const H=PL.hospitals;
 const row=k=>{const d=PL.designations[k],hs=H.filter(h=>h.des.includes(k));return`<div class="drow${state.hf===k?' on':''}"><button class="dname" data-hf="${k}" aria-pressed="${state.hf===k}"><b>${esc(d.label)}</b><small>${hs.length}</small></button><div class="dh">${hs.map(h=>`<button data-place="${h.id}">${esc(h.short)}${k==='trauma'&&h.trauma?` <em>${esc(h.trauma)}</em>`:''}</button>`).join('')}</div></div>`};
 enter(`<div class="crumbs"><button data-act="all">← All stations</button></div><p class="dept">Santa Clara County EMS</p><h1>Hospitals</h1>
 <p class="area">${H.length} hospitals take 9-1-1 patients. Tap a designation to light those hospitals up on the map.</p>
 <h3>Specialty centers</h3>${DES_ORDER.filter(k=>!PL.designations[k].info).map(row).join('')}
 <h3>Also good to know</h3>${DES_ORDER.filter(k=>PL.designations[k].info).map(row).join('')}<p class="sub">${esc(PL.meta.infoNote)}</p>
 ${srcPL(['policy602','emsar'])}`)}
function syncLayers(){try{localStorage.setItem('fa-layers',JSON.stringify(layers))}catch(e){}for(const i of document.querySelectorAll('#lay input')){const l=i.dataset.l;i.checked=l==='hosp'?layers.hosp:l==='lm'?layers.lm:layers.kinds[l]!==false;if(l!=='hosp'&&l!=='lm')i.disabled=!layers.lm}sched()}
function leaveStudy(){if(state.mode==='study'){state.mode='map';state.game=null;document.body.dataset.mode='map';tabSync()}}
function selectPlace(id){const p=PI[id];if(!p)return;leaveStudy();state.sel=null;state.place=p;if(p.des)layers.hosp=true;else{layers.lm=true;layers.kinds[p.kind]=true}syncLayers();renderPlace(p);setHash('place-'+id);
 if(isMob()&&sheet.getBoundingClientRect().height<200)setSheet(snaps()[1]);
 flyTo({cx:p.x,cy:p.y,k:Math.min(Math.max(view.k,fitK*3.5),fitK*12)})}
function openHospitals(){leaveStudy();state.sel=null;state.place=null;layers.hosp=true;syncLayers();renderHospitals();setHash('hospitals');fitHosp()}
function fitHosp(){const hs=state.hf?PL.hospitals.filter(h=>h.des.includes(state.hf)):PL.hospitals,t=boundsView(hs.map(h=>[h.x,h.y]),isMob()?50:80);t.k=Math.min(t.k,fitK*5);flyTo(t)}
function setHF(k){state.hf=state.hf===k?null:k;renderHospitals();fitHosp();sched()}

/* state changes */''')

# select(): clear place & hf
rep("function select(n,fly=true){const s=byNum[n];if(!s)return;","function select(n,fly=true){const s=byNum[n];if(!s)return;state.place=null;state.hf=null;")
rep("function setBat(id,fly=true){if(state.mode==='study'){state.bat=id;state.game=null;segSync();renderStudy();fitShown();return}state.bat=id;",
    "function setBat(id,fly=true){if(state.mode==='study'){state.bat=id;segSync();if(!state.game){setup.id?renderSetup():renderStudy();fitShown()}return}state.place=null;state.hf=null;state.bat=id;")
rep("if(h==='study')return setMode('study');","if(h==='study')return setMode('study');if(h==='hospitals')return openHospitals();const pm=h.match(/^place-(.+)$/);if(pm){const id=Object.keys(PI).find(k=>k.toLowerCase()===pm[1]);if(id)return selectPlace(id)}")

# overview: promo + hospitals link
rep("  h+=`<p class=\"dept\">${esc(dep.name)}</p><h1>${dep.stations} fire stations</h1>",
    "  h+=`<button class=\"promo\" data-act=\"study\"><span class=\"pi\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 20 20\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.7\"><circle cx=\"10\" cy=\"10\" r=\"7.5\"/><circle cx=\"10\" cy=\"10\" r=\"3.5\"/><circle cx=\"10\" cy=\"10\" r=\".6\" fill=\"currentColor\"/></svg></span><span><b>Study mode</b><small>Drop the pin, name that station, hospitals and more.</small></span><span class=\"arr\">→</span></button><p class=\"dept\">${esc(dep.name)}</p><h1>${dep.stations} fire stations</h1>")
rep("<div><b>${esc(dep.serviceArea)}</b><span>service area</span></div></div>`}",
    "<div><b>${esc(dep.serviceArea)}</b><span>service area</span></div></div><button class=\"promo sec\" data-act=\"hosps\"><span class=\"pi h\">H</span><span><b>Hospitals & specialty centers</b><small>Trauma, burn, stroke, STEMI and pediatric centers</small></span><span class=\"arr\">→</span></button>`}")

# ================= study module
span("/* study */\nconst isMob","\n\n/* search */",r'''/* study */
const isMob=()=>innerWidth<=760;
const shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const near3=(s,pool)=>pool.filter(o=>o!==s).sort((a,b)=>miles(s,a)-miles(s,b)).slice(0,3);
const CATS={all:'Everything',hospital:'Hospitals',school:'Schools',park:'Parks & peaks',place:'Landmarks'};
const catOf=p=>p.des?'hospital':p.kind==='school'?'school':(p.kind==='park'||p.kind==='peak')?'park':'place';
const findPool=cat=>[...PL.hospitals,...PL.landmarks].filter(p=>cat==='all'||catOf(p)===cat);
const rigPool=()=>{const us=[];for(const s of ST.filter(inBat))for(const u of s.units){if(u.type==='antique'||u.status==='reserve'||u.type==='trailer')continue;if(u.type==='engine'&&u.num===String(s.num))continue;us.push({t:s,u})}return us};
const PLURAL={trauma:'adult trauma centers','stroke-comp':'comprehensive stroke centers',stemi:'STEMI centers',stroke:'stroke centers (primary or comprehensive)',burn:'burn centers','trauma-peds':'pediatric trauma centers'};
const art=l=>{const w=/^[A-Z]{2}/.test(l)?l:l[0].toLowerCase()+l.slice(1);return(/^[aeiou]/i.test(w)?'an ':'a ')+w};
function hospQs(){const H=PL.hospitals,qs=[];
 for(const k of ['trauma','trauma-peds','burn','stroke-comp','stemi','peds-adv','vad','safe']){const yes=H.filter(h=>h.des.includes(k)),no=H.filter(h=>!h.des.includes(k));if(!yes.length||no.length<3)continue;
  for(const t of shuffle([...yes]).slice(0,k==='burn'?1:2))qs.push({kind:'which',k,t,choices:shuffle([t,...shuffle([...no]).slice(0,3)])})}
 for(const k of ['trauma','trauma-peds','stroke-comp','stemi','stroke','burn']){const n=H.filter(h=>h.des.includes(k)).length,o=new Set([n]);for(const d of [1,-1,2,3,-2,4])if(o.size<4&&n+d>=1)o.add(n+d);qs.push({kind:'count',k,n,choices:shuffle([...o])})}
 return shuffle(qs)}
const GAMES=[
 {id:'pin',title:'Drop the pin',blurb:'A station comes up. Tap where it is on the map.',how:['We show a station number, plus its name if you want it.','Tap the map where you think the station is.','Scored like GeoGuessr: up to 5,000 a round. The closer you are, the more you get.'],pool:()=>ST.filter(inBat),opt:'names',pts:true,area:true},
 {id:'name',title:'Name that station',blurb:'A station lights up. Pick which one it is.',how:['One station pulses on the map.','Pick its number and name from four choices.','The wrong answers are its nearest neighbors, so look closely.'],pool:()=>ST.filter(inBat),area:true},
 {id:'numbers',title:'Numbers & names',blurb:'Station 72 is…? Seven Springs is Station…? Tie each number to its name.',how:['Half the questions give you a number, half give you a name.','Pick the match. The station lights up on the map as you go, so you build the picture while you drill.'],pool:()=>ST.filter(inBat),area:true},
 {id:'rig',title:"Where's the rig?",blurb:'We call out a unit. Tap the station it runs out of.',how:['We call a unit, like Truck 85, Haz Mat 72 or Engine 371.','Tap the station it runs out of.','Engines that share their station\'s number are left out, since those are freebies.'],pool:rigPool,area:true},
 {id:'find',title:'Find it on the map',blurb:'Hospitals, high schools, parks, peaks and landmarks.',how:['We name a place: a hospital, high school, park, peak or landmark.','Tap the map where it is. Scored the same way as Drop the pin.'],pool:()=>findPool(setup.cat),opt:'cat',pts:true},
 {id:'hosp',title:'Hospital designations',blurb:'Trauma, burn, stroke, STEMI and pediatric centers.',how:['Questions like "Which of these is a burn center?" or "How many STEMI centers are in the county?"','Answers come from Santa Clara County EMS Policy 602.'],pool:hospQs}];
const GI=Object.fromEntries(GAMES.map(g=>[g.id,g]));
const setup={id:null,count:10,cat:'all'};
let showNames=true;try{showNames=localStorage.getItem('fa-names')!=='0'}catch(e){}
const bestKey=()=>'fa-best2-'+setup.id+(setup.id==='find'?'-'+setup.cat:'');
const best=k=>{try{return +localStorage.getItem(k)||0}catch(e){return 0}};
const fmtMi=d=>d<0.19?Math.max(10,Math.round(d*5280/10)*10)+' ft':d.toFixed(1)+' mi';
const ptsFor=(d,D)=>d<0.05?5000:Math.round(5000*Math.exp(-10*d/D));
const tier=d=>d<0.05?'Perfect':d<0.25?'Bullseye':d<0.75?'Close':d<2?'In the area':d<5?'Wrong part of town':'Way off';
function tabSync(){for(const b of document.querySelectorAll('#tabs button'))b.setAttribute('aria-pressed',String(b.dataset.mode===state.mode))}
function setMode(m){state.mode=m;document.body.dataset.mode=m;tabSync();state.sel=null;state.place=null;state.hf=null;state.game=null;setup.id=null;
 if(m==='study'){state.uf=null;ufSync();renderStudy();setHash('study');fitShown();if(isMob())setSheet(snaps()[1])}else{renderOverview();setHash(state.bat?state.bat.toLowerCase():'');fitShown()}}
function renderStudy(){setup.id=null;
 enter(`<p class="dept">Study</p><h1>Learn the county</h1><p class="area">Short drills on the map. Pick a game, choose how many questions, and go.</p>
 <div class="cards">${GAMES.map(G=>{const b=best('fa-best2-'+G.id+(G.id==='find'?'-all':''));return`<button class="game" data-game="${G.id}"><strong>${esc(G.title)}</strong><span>${esc(G.blurb)}</span>${b?`<small>Best ${b}%</small>`:''}</button>`}).join('')}</div>`)}
function openSetup(id){setup.id=id;renderSetup();if(isMob())setSheet(snaps()[2])}
function renderSetup(){const G=GI[setup.id],n=G.pool().length,opts=[5,10].filter(c=>c<n),cnt=setup.count==='all'||setup.count>=n?'all':setup.count,b=best(bestKey());
 enter(`<div class="crumbs"><button data-act="studyhome">← Study</button></div><p class="dept">Study</p><h1>${esc(G.title)}</h1>
 <ol class="how">${G.how.map(x=>`<li>${esc(x)}</li>`).join('')}</ol>
 ${G.opt==='cat'?`<p class="lab">What to find</p><div class="pills">${Object.entries(CATS).map(([k,v])=>`<button data-cat="${k}" aria-pressed="${setup.cat===k}">${esc(v)}</button>`).join('')}</div>`:''}
 <p class="lab">How many questions?</p><div class="pills">${opts.map(c=>`<button data-count="${c}" aria-pressed="${cnt===c}">${c}</button>`).join('')}<button data-count="all" aria-pressed="${cnt==='all'}">All ${n}</button></div>
 ${G.opt==='names'?`<label class="tog"><input type="checkbox" id="names"${showNames?' checked':''}> Show the station name with the number</label>`:''}
 ${G.area?`<p class="sub" style="margin-top:14px">Area: ${state.bat?esc(BAT[state.bat].name):'all 19 stations'}. Change it with the battalion buttons at the top.</p>`:''}
 <button class="next" data-act="start">Start</button>${b?`<p class="sub" style="text-align:center;margin-top:10px">Your best here: ${b}%</p>`:''}`)}
function startGame(){const G=GI[setup.id],pool=G.pool(),n=setup.count==='all'?pool.length:Math.min(setup.count,pool.length);if(!n)return;
 const picked=shuffle([...pool]).slice(0,n);let rounds;
 if(G.id==='pin'||G.id==='find')rounds=picked.map(t=>({t}));
 else if(G.id==='name')rounds=picked.map(t=>({t,choices:shuffle([t,...near3(t,ST)])}));
 else if(G.id==='numbers')rounds=picked.map((t,i)=>({t,dir:i%2?'name':'num',choices:shuffle([t,...near3(t,ST)])}));
 else rounds=picked;
 let Dm=5;if(G.pts){const xs=pool.map(p=>p.lon),ys=pool.map(p=>p.lat);Dm=Math.max(5,miles({lat:Math.min(...ys),lon:Math.min(...xs)},{lat:Math.max(...ys),lon:Math.max(...xs)}))}
 state.sel=null;state.place=null;state.game={id:G.id,rounds,i:0,score:0,log:[],D:Dm};askRound()}
function askRound(){const g=state.game;g.cur=g.rounds[g.i];g.phase='ask';renderGame();if(isMob())setSheet(g.cur.choices?370:240);if(g.id==='hosp'){const t=boundsView(PL.hospitals.map(h=>[h.x,h.y]),isMob()?40:70);flyTo(t)}else if(g.id==='find')flyTo(boundsView(GI.find.pool().map(p=>[p.x,p.y]),isMob()?40:70));else fitShown()}
function gameTap(e){const g=state.game;if(!g||g.phase!=='ask')return;
 if(g.id==='pin'||g.id==='find'){const r=svg.getBoundingClientRect(),t=T(),wx=(e.clientX-r.left-t.tx)/t.k,wy=(e.clientY-r.top-t.ty)/t.k;g.cur.guess={x:wx,y:wy,lon:wx/CX+LON0,lat:LAT0-wy/1000};reveal()}
 else if(g.id==='rig'&&downMk){g.cur.pick=byNum[downMk.dataset.n];reveal()}}
function reveal(){const g=state.game,c=g.cur;g.phase='reveal';c.t0=performance.now();
 if(g.id==='pin'||g.id==='find'){c.d=miles(c.guess,c.t);c.p=ptsFor(c.d,g.D);g.score+=c.p;g.log.push({t:c.t,d:c.d,p:c.p});const tv=boundsView([[c.guess.x,c.guess.y],[c.t.x,c.t.y]],isMob()?60:120);tv.k=Math.min(tv.k,fitK*5);flyTo(tv)}
 else{c.ok=c.kind==='count'?c.pick===c.n:c.pick===c.t;if(c.ok)g.score++;g.log.push({c,ok:c.ok})}
 renderGame();if(isMob())setSheet(c.choices?440:330);sched()}
function nextRound(){const g=state.game;if(!g)return;g.i++;if(g.i<g.rounds.length)return askRound();
 g.phase='done';const n=g.rounds.length,G=GI[g.id];g.pct=Math.round(100*(G.pts?g.score/(5000*n):g.score/n));const b=best(bestKey());g.newBest=g.pct>b&&n>=5;if(g.newBest)try{localStorage.setItem(bestKey(),g.pct)}catch(e){}
 renderGame();fitShown();if(isMob())setSheet(snaps()[1]);sched()}
const isRight=(c,o)=>c.kind==='count'?o===c.n:o===c.t;
function choicesHTML(c,ask,f){return`<div class="choices">${c.choices.map((o,i)=>{const r=isRight(c,o),cls=ask?'':r?'ok':o===c.pick?'bad':'fade';return`<button data-ch="${i}"${ask?'':' disabled'} class="${cls}"><span class="k">${i+1}</span>${f(o)}${!ask&&r?'<i class="ck">✓</i>':''}</button>`}).join('')}</div>`}
function feedback(g,c){const t=c.t;
 if(g.id==='pin'||g.id==='find')return`<div class="fb pin"><div class="pts"><span class="count" data-to="${c.p}">0</span><small>points</small></div><div><b>${tier(c.d)}</b><span>${c.d<0.05?'Right on it':fmtMi(c.d)+' off'}. ${t.num?`Station ${t.num}, ${esc(t.name)}`:esc(t.name)+', '+esc(t.city)}.</span></div></div>`;
 let msg;
 if(g.id==='rig')msg=(c.ok?'':`That's Station ${c.pick.num}. `)+`${esc(uName(c.u))} runs out of Station ${t.num}, ${esc(t.name)}.`;
 else if(g.id==='hosp')msg=c.kind==='count'?`There ${c.n===1?'is':'are'} ${c.n}: ${PL.hospitals.filter(h=>h.des.includes(c.k)).map(h=>esc(h.short)).join(', ')}.`:`${esc(t.name)} is ${art(PL.designations[c.k].label)}${c.k==='trauma'&&t.trauma?' ('+esc(t.trauma)+')':''}.`;
 else msg=`Station ${t.num} is ${esc(t.name)}.`;
 return`<div class="fb ${c.ok?'ok':'bad'}"><span class="ic">${c.ok?'✓':'✕'}</span><div><b>${c.ok?['Correct','Yes','Got it'][g.i%3]:'Not quite'}</b><span>${msg}</span></div></div>`}
function renderGame(){const g=state.game,G=GI[g.id],c=g.cur,n=g.rounds.length,ask=g.phase==='ask';
 let h=`<div class="crumbs"><button data-act="studyhome">← Study</button><span class="nav prog">${g.phase==='done'?'':`${g.i+1} of ${n}`}</span></div>`;
 if(g.phase==='done'){
  const max=G.pts?5000*n:n;
  h+=`<p class="dept">${esc(G.title)}</p><div class="final"><b class="count" data-to="${g.score}">0</b><span>${G.pts?`of ${max.toLocaleString()} points`:`of ${n} right`} · ${g.pct}%${g.newBest?' · new best':''}</span></div>`;
  h+=`<div class="strip">${g.log.map(x=>G.pts?`<i style="height:${Math.max(6,x.p/50)}%" title="${x.p}"></i>`:`<i class="${x.ok?'ok':'bad'}"></i>`).join('')}</div>`;
  if(G.pts){const rows=[...g.log].sort((a,b)=>b.d-a.d).slice(0,5);h+=`<h3>Biggest misses</h3>`+rows.map(x=>x.t.num?stationRow(x.t,fmtMi(x.d)+' off'):`<button class="row" data-place="${x.t.id}"><span class="badge">${x.t.des?'H':'·'}</span><span><strong>${esc(x.t.name)}</strong><em>${fmtMi(x.d)} off</em></span><span></span></button>`).join('')}
  else{const miss=g.log.filter(x=>!x.ok);h+=miss.length?`<h3>Review these</h3>`+miss.map(({c:q})=>q.t&&q.t.num?stationRow(q.t,g.id==='rig'?uName(q.u)+' runs here':'Station '+q.t.num+' · '+q.t.name):q.kind==='count'?`<p class="rv">${esc(PLURAL[q.k][0].toUpperCase()+PLURAL[q.k].slice(1))}: <b>${q.n}</b></p>`:`<button class="row" data-place="${q.t.id}"><span class="badge">H</span><span><strong>${esc(q.t.name)}</strong><em>${esc(PL.designations[q.k].label)}</em></span><span></span></button>`).join(''):`<p class="area" style="margin-top:14px">Clean sweep.</p>`}
  h+=`<div class="acts"><button class="sv" data-act="again">Play again</button><button data-act="studyhome">Back to Study</button></div>`;
  enter(h);countUp();return}
 h+=`<div class="bar2"><i style="width:${((g.i+(ask?0:1))/n*100).toFixed(1)}%"></i></div><p class="dept">${esc(G.title)}</p>`;
 const t=c.t;
 if(g.id==='pin')h+=`<h1 class="prompt">Station ${t.num}${showNames||!ask?`<span>${esc(t.name)}</span>`:''}</h1>`;
 if(g.id==='find')h+=`<h1 class="prompt">${esc(t.name)}<span>${t.des?'Hospital':esc(KIND1[t.kind])}${ask?'':' · '+esc(t.city)}</span></h1>`;
 if(g.id==='rig')h+=`<h1 class="prompt">${esc(uName(c.u))}</h1>`;
 if(g.id==='name')h+=`<h1 class="prompt sm">Which station is lit up?</h1>`+choicesHTML(c,ask,o=>`<b>${o.num}</b>${esc(o.name)}`);
 if(g.id==='numbers')h+=(c.dir==='num'?`<h1 class="prompt sm">Station ${t.num} is…</h1>`:`<h1 class="prompt sm">${esc(t.name)} is Station…</h1>`)+choicesHTML(c,ask,o=>c.dir==='num'?`<b class="nm">${esc(o.name)}</b>`:`<b>${o.num}</b>`);
 if(g.id==='hosp')h+=(c.kind==='which'?`<h1 class="prompt sm">Which of these is ${esc(art(PL.designations[c.k].label))}?</h1>`+choicesHTML(c,ask,o=>`<b class="nm">${esc(o.name)}</b>`):`<h1 class="prompt sm">How many ${esc(PLURAL[c.k])} are in the county?</h1>`+choicesHTML(c,ask,o=>`<b>${o}</b>`));
 if(ask&&(g.id==='pin'||g.id==='find'))h+=`<p class="hint">Tap the map where it is.</p>`;
 if(ask&&g.id==='rig')h+=`<p class="hint">Tap the station it runs out of.</p>`;
 if(!ask)h+=feedback(g,c)+`<button class="next" data-act="next">${g.i+1<n?'Next':'See results'}</button>`;
 enter(h);countUp()}
function countUp(){for(const el of pbody.querySelectorAll('.count[data-to]')){const to=+el.dataset.to;if(reduce||!to){el.textContent=to.toLocaleString();continue}const t0=performance.now(),step=now=>{const p=Math.min(1,(now-t0)/800),e=1-(1-p)**3;el.textContent=Math.round(to*e).toLocaleString();if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)}}
pbody.addEventListener('change',e=>{if(e.target.id==='names'){showNames=e.target.checked;try{localStorage.setItem('fa-names',showNames?'1':'0')}catch(x){}}});
$('#tabs').addEventListener('click',e=>{const b=e.target.closest('button');if(b&&D&&b.dataset.mode!==state.mode)setMode(b.dataset.mode)});''')

# ================= search: add places
rep("hits.sort((a,b)=>b.sc-a.sc||a.s.num-b.s.num);hits=hits.slice(0,8);hi=0;",
    "if(q.length>=3)for(const p of [...PL.hospitals,...PL.landmarks]){const n=p.name.toLowerCase(),sh=(p.short||'').toLowerCase();const sc=n.startsWith(ql)||sh.startsWith(ql)||p.id.toLowerCase()===ql?45:n.includes(ql)?25:0;if(sc)hits.push({sc,p,label:p.name,hint:p.des?'Hospital':KIND1[p.kind]})}\n hits.sort((a,b)=>b.sc-a.sc||((a.s?a.s.num:999)-(b.s?b.s.num:999)));hits=hits.slice(0,8);hi=0;")
rep("<span class=\"badge\">${h.s.num}</span>","<span class=\"badge\">${h.s?h.s.num:h.p.des?'H':'·'}</span>")
rep("No station or unit matches that.","No station, unit or place matches that.")
rep("function pick(i){const h=hits[i];if(!h)return;qIn.value='';resBox.classList.remove('on');qIn.blur();select(h.s.num)}","function pick(i){const h=hits[i];if(!h)return;qIn.value='';resBox.classList.remove('on');qIn.blur();h.s?select(h.s.num):selectPlace(h.p.id)}")
rep('placeholder="Station, unit or town, e.g. T85"','placeholder="Station, unit, town or hospital"')

# ================= panel click handler
span("/* panel clicks */","\n\n/* map gestures */",r'''/* panel clicks */
pbody.addEventListener('click',async e=>{const t=e.target.closest('button');if(!t||t.disabled)return;const g=state.game,a=t.dataset.act;
 if(t.dataset.game)return openSetup(t.dataset.game);
 if(t.dataset.count){setup.count=t.dataset.count==='all'?'all':+t.dataset.count;return renderSetup()}
 if(t.dataset.cat){setup.cat=t.dataset.cat;return renderSetup()}
 if(t.dataset.ch!=null){if(g&&g.phase==='ask'){g.cur.pick=g.cur.choices[+t.dataset.ch];reveal()}return}
 if(t.dataset.place)return selectPlace(t.dataset.place);
 if(t.dataset.hf)return setHF(t.dataset.hf);
 if(t.dataset.n)return select(+t.dataset.n);
 if(t.dataset.bat)return setBat(t.dataset.bat);
 if(a==='start'||a==='again')return startGame();
 if(a==='studyhome'){state.game=null;renderStudy();fitShown();if(isMob())setSheet(snaps()[1]);return}
 if(a==='study')return setMode('study');
 if(a==='hosps'){state.hf=null;return openHospitals()}
 if(a==='all'){state.uf=null;state.place=null;state.hf=null;ufSync();return setBat(null)}
 if(a==='clearuf')return setUF(null);
 if(a==='next')return g?nextRound():step(1);
 if(a==='prev')return step(-1);
 if(t.dataset.copy){try{await navigator.clipboard.writeText(t.dataset.copy);t.textContent='Copied'}catch(err){t.textContent='Copy blocked here'}setTimeout(()=>t.textContent='Copy address',1800)}});''')

# gestures: places
rep("const ptrs=new Map();let moved=0,downMk=null,pinch=null;","const ptrs=new Map();let moved=0,downMk=null,downPl=null,pinch=null;")
rep("downMk=e.target.closest('.mk');","downMk=e.target.closest('.mk');downPl=e.target.closest('.pl');")
rep("if(downMk)select(+downMk.dataset.n);else if(state.sel){state.sel=null;state.bat?renderOverview():renderOverview();setHash(state.bat?state.bat.toLowerCase():'');sched()}",
    "if(downMk)select(+downMk.dataset.n);else if(downPl)selectPlace(downPl.dataset.p);else if(state.sel||state.place){state.sel=null;state.place=null;state.hf=null;renderOverview();setHash(state.bat?state.bat.toLowerCase():'');sched()}")
rep("if(state.game){if(state.game.phase==='reveal'&&(e.key==='Enter'||e.key===' ')){e.preventDefault();nextRound()}return}",
    "if(state.game){const g=state.game;if(g.phase==='reveal'&&(e.key==='Enter'||e.key===' ')){e.preventDefault();nextRound()}else if(g.phase==='ask'&&g.cur&&g.cur.choices&&/^[1-4]$/.test(e.key)){const o=g.cur.choices[+e.key-1];if(o!=null){g.cur.pick=o;reveal()}}return}")

# globals & loading
rep("let D,G,ST=[],","let PL={hospitals:[],landmarks:[],designations:{},kinds:{},meta:{sources:{}}},PI={},layers={hosp:true,lm:false,kinds:{}},D,G,ST=[],")
rep("const state={sel:null,bat:null,uf:null,mode:'map',game:null};","const state={sel:null,bat:null,uf:null,mode:'map',game:null,place:null,hf:null};try{Object.assign(layers,JSON.parse(localStorage.getItem('fa-layers')||'{}'))}catch(e){}")
rep("Promise.all(['data/stations.json','data/geo.json'].map(","Promise.all(['data/stations.json','data/geo.json','data/places.json'].map(")
rep(" .then(([d,g])=>{D=d;G=g;"," .then(([d,g,pl])=>{D=d;G=g;PL=pl;for(const p of [...PL.hospitals,...PL.landmarks]){[p.x,p.y]=P(p.lon,p.lat);PI[p.id]=p}")
rep(" lastW=innerWidth;fitK="," syncLayers();\n $('#laybtn').addEventListener('click',()=>{const l=$('#lay');l.hidden=!l.hidden;$('#laybtn').setAttribute('aria-expanded',String(!l.hidden))});\n $('#lay').addEventListener('change',e=>{const i=e.target,l=i.dataset.l;if(l==='hosp')layers.hosp=i.checked;else if(l==='lm')layers.lm=i.checked;else layers.kinds[l]=i.checked;if(!layers.hosp&&state.hf)state.hf=null;syncLayers()});\n lastW=innerWidth;fitK=")

# ================= HTML: tabs, layers
rep('<nav class="tabs" id="tabs" aria-label="Sections"><button data-mode="map" aria-pressed="true">Map</button><button data-mode="study" aria-pressed="false">Study</button></nav>',
    '<nav class="tabs" id="tabs" aria-label="Sections"><button data-mode="map" aria-pressed="true"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M1.5 3.5l4-1.5 5 2 4-1.5v10l-4 1.5-5-2-4 1.5z"/><path d="M5.5 2v10M10.5 4v10"/></svg>Map</button><button data-mode="study" aria-pressed="false"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8" cy="8" r="6.3"/><circle cx="8" cy="8" r="2.8"/></svg>Study</button></nav>')
rep('''   <button id="zfit" aria-label="Show all stations in view">''','''   <button id="laybtn" aria-label="Map layers" aria-expanded="false" aria-controls="lay"><svg width="17" height="17" viewBox="0 0 17 17" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M8.5 2l6.5 3.5-6.5 3.5L2 5.5z"/><path d="M2 8.5l6.5 3.5 6.5-3.5M2 11.5L8.5 15l6.5-3.5"/></svg></button>
   <button id="zfit" aria-label="Show all stations in view">''')
rep('  <nav class="uf" id="uf" aria-label="Filter by apparatus"></nav>','''  <nav class="uf" id="uf" aria-label="Filter by apparatus"></nav>
  <div class="lay" id="lay" hidden><p>Show on the map</p>
   <label><input type="checkbox" data-l="hosp"><span class="sw h">H</span>Hospitals</label>
   <label><input type="checkbox" data-l="lm"><span class="sw"></span>Landmarks</label>
   <div class="sub2"><label><input type="checkbox" data-l="school"><i class="k-school"></i>High schools & colleges</label><label><input type="checkbox" data-l="park"><i class="k-park"></i>Parks & open space</label><label><input type="checkbox" data-l="peak"><i class="k-peak"></i>Peaks</label><label><input type="checkbox" data-l="venue"><i class="k-venue"></i>Venues & landmarks</label><label><input type="checkbox" data-l="tech"><i class="k-tech"></i>Tech campuses</label><label><input type="checkbox" data-l="ems"><i class="k-ems"></i>Dispatch & EMS</label></div></div>''')

# ================= CSS
rep(".tabs button{height:32px;padding:0 13px;border-radius:6px;font:600 14px \"Barlow Semi Condensed\",sans-serif;color:var(--muted)}",
    ".tabs button{display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 15px;border-radius:7px;font:600 15px \"Barlow Semi Condensed\",sans-serif;color:var(--muted)}\n.tabs button:hover{color:var(--ink)}")
rep("/* study */\n.tabs{",r"""/* places */
:root{--hosp:#5aa2ff;--ok:#3dbb7a;--k-school:#d9a83a;--k-park:#53b37f;--k-peak:#b08d68;--k-venue:#a08cf5;--k-tech:#48b9d8;--k-ems:#ff8a65}
:root[data-theme=light]{--hosp:#1e62d0;--ok:#1d8a4e;--k-school:#a87a10;--k-park:#2f8a58;--k-peak:#86643f;--k-venue:#6f55d9;--k-tech:#1a85a6;--k-ems:#d9532c}
.k-school{--kc:var(--k-school)}.k-park{--kc:var(--k-park)}.k-peak{--kc:var(--k-peak)}.k-venue{--kc:var(--k-venue)}.k-tech{--kc:var(--k-tech)}.k-ems{--kc:var(--k-ems)}
.pl{cursor:pointer;transition:opacity .25s}.pl .hit{fill:transparent}
.pl.h rect{fill:var(--mk);stroke:var(--hosp);stroke-width:1.6}
.pl.h text{font:700 10px "Barlow Semi Condensed",sans-serif;fill:var(--hosp);text-anchor:middle;pointer-events:none}
.pl.h.sel rect{fill:var(--hosp)}.pl.h.sel text{fill:var(--mk)}
.pl.h.wrong rect{stroke:var(--red);stroke-dasharray:3 2}
.pl.dim{opacity:.22}
.pl.l .d{fill:var(--kc);stroke:var(--mk);stroke-width:1.5}
.pl.l.sel .d{stroke:var(--ink);stroke-width:2}
.pl .pulse{stroke:var(--hosp)}.pl.l .pulse{stroke:var(--kc)}
.plbl{font:600 11.5px "Barlow Semi Condensed",sans-serif;fill:var(--muted);paint-order:stroke;stroke:var(--home);stroke-width:3px;stroke-linejoin:round;pointer-events:none}
.plbl.h{fill:var(--hosp)}.plbl.dim{opacity:.25}
.pulse.p2{animation-delay:1.2s}
.lay{position:absolute;right:66px;top:12px;width:250px;padding:12px 14px;border-radius:12px;background:var(--panel);border:1px solid var(--rule2);box-shadow:var(--shadow);z-index:3}
.lay p{margin:0 0 6px;font-size:13px;color:var(--muted)}
.lay label{display:flex;align-items:center;gap:10px;min-height:36px;font-size:15px;cursor:pointer}
.lay input{width:18px;height:18px;accent-color:var(--hosp);margin:0}
.lay .sw{width:18px;height:18px;border-radius:50%;border:2px solid var(--muted)}.lay .sw.h{border-radius:4px;border-color:var(--hosp);color:var(--hosp);font:700 10px/14px "Barlow Semi Condensed";text-align:center}
.lay .sub2{padding-left:28px}.lay .sub2 label{font-size:14px;min-height:32px;color:var(--muted)}.lay .sub2 i{width:9px;height:9px;border-radius:50%;background:var(--kc)}
.lay input:disabled+i{opacity:.4}
.hbig{width:64px;height:64px;border-radius:13px;display:grid;place-items:center;font:700 36px "Barlow Semi Condensed",sans-serif;background:var(--hosp);color:var(--mk)}
.lbig{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;border:2px solid var(--kc)}.lbig i{width:18px;height:18px;border-radius:50%;background:var(--kc)}
.dchips{display:flex;flex-wrap:wrap;gap:6px}
.dchip{padding:7px 11px;border-radius:7px;background:var(--panel2);border:1px solid var(--rule2);font-size:14.5px;font-weight:500}
.dchip.info{color:var(--muted);border-style:dashed}
.drow{padding:10px 0;border-bottom:1px solid var(--rule)}
.dname{display:flex;width:100%;justify-content:space-between;align-items:baseline;min-height:34px;text-align:left}
.dname b{font-weight:600;font-size:15.5px}.dname small{color:var(--muted);font-size:13px}
.dname:hover b,.drow.on .dname b{color:var(--hosp)}
.dh{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
.dh button{min-height:34px;padding:0 11px;border-radius:7px;border:1px solid var(--rule2);background:var(--panel2);font-size:14px}
.dh button:hover{border-color:var(--hosp)}.dh em{font-style:normal;color:var(--muted);font-size:12.5px}
.promo{display:flex;align-items:center;gap:14px;width:100%;text-align:left;padding:13px 14px;margin:0 0 22px;border-radius:12px;border:1px solid var(--rule2);background:var(--panel2);transition:border-color .2s}
.promo:hover{border-color:var(--mkline)}
.promo.sec{margin:20px 0 4px}
.promo b{display:block;font:600 17px "Barlow Semi Condensed",sans-serif}
.promo small{display:block;color:var(--muted);font-size:13.5px;line-height:1.35;margin-top:1px}
.promo .pi{flex:none;width:40px;height:40px;border-radius:10px;display:grid;place-items:center;background:var(--chipbg);color:var(--chipink)}
.promo .pi.h{background:var(--hosp);color:var(--mk);font:700 20px "Barlow Semi Condensed",sans-serif}
.promo .arr{margin-left:auto;color:var(--muted);font-size:19px;transition:transform .2s}.promo:hover .arr{transform:translateX(3px)}
/* study */
.cards{display:grid;gap:10px;margin-top:18px}
.how{margin:14px 0 4px;padding-left:20px;font-size:15.5px;line-height:1.5}.how li{margin:5px 0}.how li::marker{color:var(--muted)}
.lab{font-size:13px;color:var(--muted);margin:22px 0 8px}
.pills{display:flex;flex-wrap:wrap;gap:6px}
.pills button{min-height:40px;padding:0 15px;border-radius:20px;border:1px solid var(--rule2);background:var(--panel2);font-size:15px;font-weight:500}
.pills button[aria-pressed=true]{background:var(--ink);color:var(--panel);border-color:var(--ink)}
.bar2{height:3px;background:var(--rule);border-radius:2px;margin:-6px 0 16px;overflow:hidden}.bar2 i{display:block;height:100%;background:var(--red);transition:width .45s cubic-bezier(.2,.8,.2,1)}
.prog{color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums;align-items:center}
.prompt.sm{font-size:28px;line-height:1.15}
.hint{color:var(--muted);margin:12px 0 0;display:flex;align-items:center;gap:9px;font-size:15px}
.hint::before{content:'';width:8px;height:8px;border-radius:50%;background:var(--red);animation:blink 1.6s ease-in-out infinite}
@keyframes blink{50%{opacity:.25}}
.choices button{position:relative}
.choices .k{position:absolute;right:9px;top:7px;font-size:11px;color:var(--faint)}
.choices b.nm{font:600 17px/1.2 "Barlow Semi Condensed",sans-serif;padding-right:12px}
.choices .ok{border-color:var(--ok)!important;background:transparent!important}.choices .bad{border-color:var(--red)!important;background:transparent!important}.choices .fade{opacity:.4}
.choices .ck{position:absolute;right:9px;bottom:7px;font-style:normal;font-weight:700;color:var(--ok)}
.choices .ok .k,.choices .bad .k{display:none}
.fb{display:flex;gap:14px;align-items:center;margin-top:18px;padding-top:16px;border-top:1px solid var(--rule);animation:enter .3s ease-out}
.fb .ic{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:15px;border:1.5px solid}
.fb.ok .ic{color:var(--ok);border-color:var(--ok)}.fb.bad .ic{color:var(--red);border-color:var(--red)}
.fb b{display:block;font:600 19px "Barlow Semi Condensed",sans-serif}.fb span{color:var(--muted);font-size:14.5px;line-height:1.4}
.fb .pts{flex:none;text-align:center;min-width:88px;padding-right:14px;border-right:1px solid var(--rule)}
.fb .pts .count{display:block;font:700 32px/1 "Barlow Semi Condensed",sans-serif;color:var(--ink);font-variant-numeric:tabular-nums}
.fb .pts small{font-size:12px;color:var(--muted)}
.final{margin:6px 0 2px}.final b{display:block;font:700 60px/1 "Barlow Semi Condensed",sans-serif;font-variant-numeric:tabular-nums}.final span{display:block;color:var(--muted);margin-top:6px}
.strip{display:flex;gap:4px;align-items:flex-end;height:44px;margin:18px 0 6px}.strip i{flex:1;background:var(--mkline);border-radius:2px;min-height:4px;height:100%}.strip i.ok{background:var(--ok)}.strip i.bad{background:var(--red);opacity:.75}
.rv{margin:8px 0;font-size:15px}
.tabs{""")
rep(" .prompt{font-size:34px}"," .prompt{font-size:34px}\n .lay{right:60px;top:10px}\n .tabs button{padding:0 11px;height:32px}.tabs svg{display:none}")
open(p,'w').write(s);print("patched")
