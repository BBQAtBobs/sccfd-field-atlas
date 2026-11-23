p='index.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:100]); s=s.replace(a,b)
def span(start,end,new,keep_end=True):
    global s
    i=s.index(start); j=s.index(end,i); s=s[:i]+new+s[j:]
def cut_line(prefix):
    global s
    i=s.index(prefix); j=s.index("\n",i); s=s[:i]+s[j+1:]

# ---------------- HTML
i=s.index(' <nav class="seg" id="seg"'); j=s.index('</nav>',i)+len('</nav>\n'); s=s[:i]+s[j:]
i=s.index('   <button id="laybtn"'); j=s.index('</button>',i)+len('</button>\n'); s=s[:i]+s[j:]
i=s.index('  <nav class="uf" id="uf"'); j=s.index('  <div class="scale" id="scale"></div>'); s=s[:i]+'  <div class="fbar" id="fbar" role="toolbar" aria-label="Filters"></div>\n  <div class="fmenu" id="fmenu" hidden></div>\n'+s[j:]
rep('<svg id="svg"><g id="world">','''<svg id="svg"><defs>
<symbol id="g-school" viewBox="0 0 12 12"><path d="M.8 5L6 2.3 11.2 5 6 7.7z" fill="currentColor"/><path d="M3.1 6.3v2.5c1.6 1.2 4.2 1.2 5.8 0V6.3" fill="none" stroke="currentColor" stroke-width="1.3"/></symbol>
<symbol id="g-park" viewBox="0 0 12 12"><path d="M6 .6l3.7 5.1H7.7l2.7 3.7H1.6l2.7-3.7H2.3z" fill="currentColor"/><rect x="5.3" y="9.3" width="1.4" height="2.1" fill="currentColor"/></symbol>
<symbol id="g-peak" viewBox="0 0 12 12"><path d="M.5 10.9L4.4 3.2l2.5 4.1 1.3-1.9 3.3 5.5z" fill="currentColor"/></symbol>
<symbol id="g-venue" viewBox="0 0 12 12"><path d="M6 .8l1.6 3.3 3.6.5-2.6 2.5.6 3.6L6 9 2.8 10.7l.6-3.6L.8 4.6l3.6-.5z" fill="currentColor"/></symbol>
<symbol id="g-tech" viewBox="0 0 12 12"><rect x="2.6" y="2.6" width="6.8" height="6.8" rx="1.3" fill="currentColor"/><path d="M4.2.8v1.6M7.8.8v1.6M4.2 9.6v1.6M7.8 9.6v1.6M.8 4.2h1.6M.8 7.8h1.6M9.6 4.2h1.6M9.6 7.8h1.6" stroke="currentColor" stroke-width="1.1"/></symbol>
<symbol id="g-ems" viewBox="0 0 12 12"><circle cx="6" cy="6" r="1.7" fill="currentColor"/><path d="M3.5 3.5a3.6 3.6 0 0 0 0 5M8.5 3.5a3.6 3.6 0 0 1 0 5M1.7 1.7a6.1 6.1 0 0 0 0 8.6M10.3 1.7a6.1 6.1 0 0 1 0 8.6" fill="none" stroke="currentColor" stroke-width="1.15" stroke-linecap="round"/></symbol>
<symbol id="g-flame" viewBox="0 0 12 12"><path d="M6.3.6c.9 2.6 3.6 3.6 3.6 6.8a3.9 3.9 0 0 1-7.8 0c0-2.2 1.5-3 2.1-4.6.7 1.2 1.2 1.6 1.4 2.3.5-1.3.9-2.6.7-4.5z" fill="currentColor"/></symbol>
</defs><g id="world">''')

# ---------------- CSS
rep("grid-template-areas:'brand tools' 'search seg'","grid-template-areas:'brand tools' 'search search'")
rep(".pl.h rect{fill:var(--mk);stroke:var(--hosp);stroke-width:1.6}",".pl.h rect{fill:#f4f4f1;stroke:rgba(0,0,0,.28);stroke-width:1}.pl.h .hx{fill:none;stroke:#d8241b;stroke-width:2.5}")
rep(".pl.h text{font:700 10px \"Barlow Semi Condensed\",sans-serif;fill:var(--hosp);text-anchor:middle;pointer-events:none}","")
rep(".pl.h.sel rect{fill:var(--hosp)}.pl.h.sel text{fill:var(--mk)}",".pl.h.sel rect{fill:#d8241b;stroke:#d8241b}.pl.h.sel .hx{stroke:#fff}")
rep(".pl.h.wrong rect{stroke:var(--red);stroke-dasharray:3 2}",".pl.h.wrong rect{stroke:var(--red);stroke-width:2;stroke-dasharray:3 2}")
rep(".pl.l .d{fill:var(--kc);stroke:var(--mk);stroke-width:1.5}\n.pl.l.sel .d{stroke:var(--ink);stroke-width:2}",".pl.l{color:var(--kc)}.pl.l .bg{fill:var(--mk);stroke:var(--kc);stroke-width:1.4}.pl.l.sel .bg{fill:var(--kc)}.pl.l.sel use{color:var(--mk)}")
rep(".pl .pulse{stroke:var(--hosp)}",".pl .pulse{stroke:var(--red)}")
rep(".plbl.h{fill:var(--hosp)}",".plbl.h{fill:var(--ink)}")
rep(".hbig{width:64px;height:64px;border-radius:13px;display:grid;place-items:center;font:700 36px \"Barlow Semi Condensed\",sans-serif;background:var(--hosp);color:var(--mk)}",
    ".hbig{width:64px;height:64px;border-radius:13px;display:grid;place-items:center;background:#f4f4f1;box-shadow:inset 0 0 0 1px rgba(0,0,0,.15)}.hbig svg,.pi.h svg{display:block}")
rep(".lbig{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;border:2px solid var(--kc)}.lbig i{width:18px;height:18px;border-radius:50%;background:var(--kc)}",
    ".lbig{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;border:2px solid var(--kc);color:var(--kc)}")
rep(".promo .pi.h{background:var(--hosp);color:var(--mk);font:700 20px \"Barlow Semi Condensed\",sans-serif}",".promo .pi.h{background:#f4f4f1}")
rep(".chip{background:var(--panel2);color:var(--ink)}",".chip{background:none;border:0;border-left:3px solid var(--c);border-radius:0;text-align:left;padding:3px 0 3px 9px;font-size:14px;color:var(--ink)}")
rep("/* study */\n.cards{display:grid;gap:10px;margin-top:18px}",r"""/* filter bar */
.fbar{position:absolute;left:12px;top:12px;right:66px;display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding:2px;z-index:2}
.fbar::-webkit-scrollbar{display:none}
.fbtn{flex:none;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 11px 0 14px;border-radius:10px;background:var(--panel);border:1px solid var(--rule2);box-shadow:var(--shadow);font:600 15px "Barlow Semi Condensed",sans-serif;color:var(--ink);transition:border-color .2s}
.fbtn:hover{border-color:var(--mkline)}.fbtn.on{border-color:var(--ink)}
.fbtn .car{opacity:.55;transition:transform .2s}.fbtn.open .car{transform:rotate(180deg)}
.fbtn .dot,.fmenu .dot{width:9px;height:9px;border-radius:50%;flex:none}
.fbtn .ico{color:var(--muted);display:block}
.fbtn.on .cnt{font:600 12px "Barlow",sans-serif;color:var(--muted)}
.mini-h{width:17px;height:17px;border-radius:4px;background:#f4f4f1;box-shadow:inset 0 0 0 1px rgba(0,0,0,.2);display:grid;place-items:center;flex:none}
.fclear{flex:none;height:40px;padding:0 12px;border-radius:10px;color:var(--muted);font-size:14px;background:var(--panel);border:1px solid var(--rule2)}
.fclear:hover{color:var(--ink)}
.fmenu{position:absolute;z-index:6;width:250px;max-width:calc(100% - 20px);padding:6px;border-radius:12px;background:var(--panel);border:1px solid var(--rule2);box-shadow:var(--shadow);animation:enter .16s ease-out}
.fmenu button,.fmenu label{display:flex;align-items:center;gap:10px;width:100%;min-height:42px;padding:0 10px;border-radius:8px;text-align:left;font-size:15px;cursor:pointer}
.fmenu button:hover,.fmenu label:hover{background:var(--hover)}
.fmenu .sel{font-weight:600}.fmenu .sel::after{content:'';margin-left:auto;width:7px;height:7px;border-radius:50%;background:var(--red);flex:none}
.fmenu small{margin-left:auto;color:var(--muted);font-size:12.5px}.fmenu .sel small{margin-left:6px}
.fmenu .mt{justify-content:space-between;font-weight:600}
.fmenu input{accent-color:var(--red);width:18px;height:18px;margin:0;flex:none}
.fmenu .msep{height:1px;background:var(--rule);margin:5px 8px}
.fmenu .sq{width:10px;height:10px;border-radius:2px;flex:none}
.fmenu .kr svg{color:var(--kc);flex:none}.fmenu .kr input:disabled~*{opacity:.4}
.fmenu .go{color:var(--muted)}
.backbar{display:inline-flex;align-items:center;gap:8px;min-height:38px;margin:-8px 0 12px -6px;padding:0 10px 0 6px;border-radius:8px;color:var(--muted);font-size:14.5px;font-weight:500}
.backbar:hover{color:var(--ink);background:var(--hover)}.backbar svg{transition:transform .2s}.backbar:hover svg{transform:translateX(-2px)}
/* hospital info */
.hrows{display:grid;grid-template-columns:7.2em minmax(0,1fr);margin:6px 0 0}
.hrows dt,.hrows dd{padding:11px 0;border-top:1px solid var(--rule);margin:0}
.hrows dt{color:var(--muted);font-size:14px}.hrows dd{font-weight:600}.hrows dd.no{color:var(--faint);font-weight:400}
.htab{width:100%;border-collapse:collapse;margin-top:6px;font-size:14px}
.htab th{font:600 11.5px/1.15 "Barlow",sans-serif;color:var(--muted);text-align:center;padding:6px 2px;vertical-align:bottom}
.htab th:first-child{text-align:left}
.htab td{padding:0 2px;border-top:1px solid var(--rule);text-align:center;height:46px}
.htab td:first-child{text-align:left;padding:0}
.htab td button{width:100%;min-height:46px;text-align:left;font-weight:600;font-size:15px;display:flex;align-items:center;gap:9px}
.htab td button:hover{color:var(--red)}
.htab .v{font:700 14.5px "Barlow Semi Condensed",sans-serif}
.htab .yes{display:inline-block;width:9px;height:9px;border-radius:50%;background:var(--ink)}
.htab .hi{background:var(--hover)}.htab th.hi{color:var(--ink)}
.htab tr.dim td{opacity:.32}
.legend2{font-size:12.5px;color:var(--faint);margin:10px 0 0;line-height:1.5}
/* study */
.cards{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:10px;margin-top:18px}
.game{padding:0!important;margin:0!important;overflow:hidden;display:flex!important;flex-direction:column}
.game .ill{display:block;aspect-ratio:160/84;background:var(--panel)}.game .ill svg{width:100%;height:100%;display:block}
.game strong{padding:10px 12px 0;font-size:18px!important}.game .bl{padding:2px 12px 12px;font-size:13.5px!important;line-height:1.35}
.game small{padding:0 12px 12px;margin-top:-6px!important;color:var(--muted)!important}
.game:hover{border-color:var(--mkline)}
.hero-ill{margin:0 -22px 16px;aspect-ratio:160/72;overflow:hidden;background:var(--panel2)}.hero-ill svg{width:100%;height:100%;display:block}
.il-bg{fill:var(--home)}.il-road{stroke:var(--fwy);fill:none}.il-mut{fill:var(--mkline)}.il-ink{fill:var(--ink)}.il-red{fill:var(--red)}.il-card{fill:var(--panel2);stroke:var(--rule2)}
.il-ring{fill:none;stroke:var(--red);stroke-width:2;transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-out infinite}
.il-dash{fill:none;stroke:var(--ink);stroke-width:1.6;stroke-dasharray:3 4;opacity:.7}
.il-truck{fill:#f1f1ee;stroke:rgba(0,0,0,.25);stroke-width:1}.il-win{fill:#7d8a96}.il-wheel{fill:#1b1d20;stroke:#5c6066;stroke-width:2}
.il-arrow{fill:none;stroke:var(--muted);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.il-txt{font:700 22px "Barlow Semi Condensed",sans-serif;fill:var(--ink)}
.pinbob{transform-box:fill-box;transform-origin:bottom center}.game:hover .pinbob{animation:bob .7s ease}
@keyframes bob{0%{transform:translateY(0)}35%{transform:translateY(-8px)}70%{transform:translateY(0)}85%{transform:translateY(-2px)}100%{transform:none}}
.streak{display:inline-flex;align-items:center;gap:4px;margin-right:10px;color:var(--k-ems);font-weight:600;animation:enter .3s ease-out}
.fb .ic{position:relative}.fb.ok .ic::after{content:'';position:absolute;inset:-2px;border-radius:50%;border:2px solid var(--ok);animation:burst .7s ease-out forwards}
@keyframes burst{from{transform:scale(1);opacity:.9}to{transform:scale(2.3);opacity:0}}
.choices .ok{animation:pop .35s ease}
@keyframes pop{40%{transform:scale(1.03)}}
.gpin path{fill:var(--ink)}.gpin circle{fill:var(--home)}.gsh{fill:#000;opacity:.25}""")
rep(" .lay{right:60px;top:10px}\n"," .fbar{left:10px;top:10px;right:60px}.fbtn{height:38px;font-size:14.5px}\n .hero-ill{margin:0 -18px 14px}\n")

# ---------------- placeSVG
span("function placeSVG(","function draw(){",r'''const HX='<path class="hx" d="M-3.6-4.4v8.8M3.6-4.4v8.8M-3.6 0h7.2"/>';
function placeSVG(p,x,y,sel,dim,wrong){
 if(p.des)return`<g class="pl h${sel?' sel':''}${dim?' dim':''}${wrong?' wrong':''}" data-p="${p.id}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><circle class="hit" r="15"/>${sel?'<circle class="pulse" r="11"/>':''}<rect x="-8.5" y="-8.5" width="17" height="17" rx="4"/>${HX}</g>`;
 return`<g class="pl l k-${p.kind}${sel?' sel':''}${dim?' dim':''}" data-p="${p.id}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><circle class="hit" r="13"/>${sel?'<circle class="pulse" r="10"/>':''}<circle class="bg" r="${sel?10.5:9}"/><use href="#g-${p.kind}" x="-5.5" y="-5.5" width="11" height="11"/></g>`}
''')

# ---------------- pin reveal block (drop + line + answer)
span(" // pin reveal: animated miss line, then the answer\n"," const hq=D.facilities.find",r''' // pin reveal: the pin drops, the line draws, the answer pings
 if(pinG&&rev&&c.guess){const t=c.t,[x2,y2]=S(t),gx=c.guess.x*k+tx,gy=c.guess.y*k+ty,el=reduce?5000:now-c.t0;
  const p1=Math.min(1,el/340),dy=p1<1?-52*(1-p1)**2:0,sq=p1<1?1:Math.max(0,1-((el-340)/120)),pr=Math.max(0,Math.min(1,(el-380)/700)),e=1-(1-pr)**3,ex=gx+(x2-gx)*e,ey=gy+(y2-gy)*e;
  if(pr>0)mk+=`<line class="miss" x1="${gx}" y1="${gy}" x2="${ex.toFixed(1)}" y2="${ey.toFixed(1)}"/>`;
  mk+=`<ellipse class="gsh" cx="${gx}" cy="${gy}" rx="${(5+3*p1).toFixed(1)}" ry="2"/><g class="gpin" transform="translate(${gx} ${(gy+dy).toFixed(1)}) scale(${(1+.12*sq*(p1===1?1:0)).toFixed(3)},${(1-.12*sq*(p1===1?1:0)).toFixed(3)})"><path d="M0 0c-6-7-9.5-10.6-9.5-15.2a9.5 9.5 0 0 1 19 0C9.5-10.6 6-7 0 0z"/><circle cy="-15.2" r="3.4"/></g>`;
  if(pr>.85)mk+=t.num?`<g class="mk game sel" transform="translate(${x2} ${y2})"><circle class="pulse" r="12"/><circle class="pulse p2" r="12"/><circle class="dot" r="11.5"/><text dy="3.9">${t.num}</text></g>`:placeSVG(t,x2,y2,true,false,false);
  if(el<1200)sched()}
''')

# ---------------- hospital/place panels + filters + history
span("function renderPlace(p){","function leaveStudy(){",r'''const yes='<span class="yes" aria-label="yes"></span>';
function renderPlace(p){pushView({v:'place',id:p.id});const near=ST.map(o=>[o,miles(p,o)]).sort((a,b)=>a[1]-b[1]).slice(0,3),isH=!!p.des,has=k=>isH&&p.des.includes(k);
 const row=(l,v)=>`<dt>${l}</dt><dd${v?'':' class="no"'}>${v||'—'}</dd>`;
 const also=['ld','vad','safe','helipad'].filter(has).map(k=>PL.designations[k].short).join(', ');
 enter(`${isH?'<div class="crumbs"><button data-act="hosps">All hospitals</button></div>':''}
 <div class="hero">${isH?`<span class="hbig"><svg width="40" height="40" viewBox="-10 -10 20 20"><path d="M-3.6-4.4v8.8M3.6-4.4v8.8M-3.6 0h7.2" fill="none" stroke="#d8241b" stroke-width="2.6"/></svg></span>`:`<span class="lbig k-${p.kind}"><svg width="30" height="30"><use href="#g-${p.kind}"/></svg></span>`}<div><h1>${esc(p.name)}</h1><p class="addr">${esc(isH?'Hospital':KIND1[p.kind])} · ${esc(p.city)}</p></div></div>
 ${isH?`<dl class="hrows">${row('Trauma',has('trauma')?`${esc(p.trauma||'')} adult${has('trauma-peds')?' + pediatric':''}`:'')}${row('Burn',has('burn')?'Burn center':'')}${row('Stroke',has('stroke-comp')?'Comprehensive':has('stroke')?'Primary':'')}${row('STEMI',has('stemi')?'STEMI center':'')}${row('Pediatrics',has('peds-adv')?'Advanced':has('peds')?'General':'')}${row('Also',also)}</dl>`:(p.note?`<p class="area" style="margin-top:14px">${esc(p.note)}</p>`:'')}
 ${isH&&p.note?`<p class="note">${esc(p.note)}</p>`:''}
 <div class="acts"><a href="https://www.google.com/maps/search/?api=1&query=${p.lat},${p.lon}" target="_blank" rel="noopener">Google Maps ↗</a></div>
 <h3>Closest SCCFD stations</h3>${near.map(([o,d])=>stationRow(o,d.toFixed(1)+' mi straight-line')).join('')}
 ${isH&&also?`<p class="sub">${esc(PL.meta.infoNote)}</p>`:''}
 ${srcPL(isH?['policy602','osm']:['osm'])}`)}
const HCOLS=[{k:'trauma',h:'Adult<br>trauma',v:h=>h.des.includes('trauma')?`<span class="v">${h.trauma.replace('Level ','')}</span>`:''},{k:'trauma-peds',h:'Peds<br>trauma',v:h=>h.des.includes('trauma-peds')?yes:''},{k:'burn',h:'Burn',v:h=>h.des.includes('burn')?yes:''},{k:'stroke',h:'Stroke',v:h=>h.des.includes('stroke-comp')?'<span class="v">C</span>':h.des.includes('stroke')?'<span class="v">P</span>':''},{k:'stemi',h:'STEMI',v:h=>h.des.includes('stemi')?yes:''},{k:'peds',h:'Peds',v:h=>h.des.includes('peds-adv')?'<span class="v">A</span>':h.des.includes('peds')?'<span class="v">G</span>':''}];
const HF=[['trauma','Trauma centers'],['trauma-peds','Pediatric trauma'],['burn','Burn center'],['stroke-comp','Comprehensive stroke'],['stroke','All stroke centers'],['stemi','STEMI centers'],['peds-adv','Advanced pediatric']];
const HFL=Object.fromEntries(HF);
const colOf=k=>k==='stroke-comp'?'stroke':k==='peds-adv'?'peds':k;
function renderHospitals(){pushView({v:'hospitals',hf:state.hf});const H=[...PL.hospitals].sort((a,b)=>a.short.localeCompare(b.short)),hc=state.hf&&colOf(state.hf);
 enter(`<p class="dept">Santa Clara County EMS</p><h1>${state.hf?esc(HFL[state.hf]):'Hospitals'}</h1>
 <p class="area">${state.hf?`${PL.hospitals.filter(h=>h.des.includes(state.hf)).length} of ${H.length} hospitals. The rest are dimmed on the map.`:`${H.length} hospitals take 9-1-1 patients. Use the Hospitals filter on the map to light up one kind.`}</p>
 <table class="htab"><thead><tr><th>Hospital</th>${HCOLS.map(c=>`<th class="${c.k===hc?'hi':''}">${c.h}</th>`).join('')}</tr></thead><tbody>
 ${H.map(h=>`<tr class="${state.hf&&!h.des.includes(state.hf)?'dim':''}"><td><button data-place="${h.id}">${esc(h.short)}</button></td>${HCOLS.map(c=>`<td class="${c.k===hc?'hi':''}">${c.v(h)}</td>`).join('')}</tr>`).join('')}</tbody></table>
 <p class="legend2">Trauma: Level I or II. Stroke: C = comprehensive, P = primary. Peds: A = advanced, G = general pediatric center. Tap a hospital for details.</p>
 ${srcPL(['policy602','emsar'])}`)}
function syncLayers(){try{localStorage.setItem('fa-layers',JSON.stringify(layers))}catch(e){}renderFbar();sched()}
/* filter bar */
let openMenu=null;
const CAR='<svg class="car" width="11" height="11" viewBox="0 0 12 12"><path d="M2.5 4.5L6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const MINIH='<span class="mini-h"><svg width="11" height="11" viewBox="-6 -6 12 12"><path d="M-2.6-3.2v6.4M2.6-3.2v6.4M-2.6 0h5.2" fill="none" stroke="#d8241b" stroke-width="1.8"/></svg></span>';
function renderFbar(){const fb=$('#fbar');if(!fb||!D)return;const kOn=Object.keys(PL.kinds).filter(k=>layers.kinds[k]!==false).length;
 const btn=(id,on,inner,nb)=>`<button class="fbtn${on?' on':''}${openMenu===id?' open':''}${nb?' nb':''}" data-fb="${id}" aria-expanded="${openMenu===id}" aria-haspopup="true">${inner}${CAR}</button>`;
 fb.innerHTML=btn('bat',!!state.bat,state.bat?`<i class="dot" style="background:${bc(state.bat)}"></i><span>${esc(BAT[state.bat].name)}</span>`:'<span>Battalion</span>')
  +btn('units',!!state.uf,`<span>${state.uf?esc(UFI[state.uf].label):'Apparatus'}</span>`,1)
  +btn('hosp',layers.hosp,`${MINIH}<span>${state.hf?esc(HFL[state.hf]):'Hospitals'}</span>`,1)
  +btn('lm',layers.lm,`<svg class="ico" width="15" height="15"><use href="#g-peak"/></svg><span>Landmarks</span>${layers.lm&&kOn<6?`<span class="cnt">${kOn}/6</span>`:''}`,1)
  +(state.bat||state.uf||state.hf?'<button class="fclear nb" data-fb="clear">Clear</button>':'');
 renderMenu()}
function renderMenu(){const m=$('#fmenu');if(!openMenu||!D){m.hidden=true;return}let h='';
 if(openMenu==='bat')h=`<button data-mv="bat:" class="${state.bat?'':'sel'}">All battalions<small>19 stations</small></button>`+D.battalions.map(b=>`<button data-mv="bat:${b.id}" class="${state.bat===b.id?'sel':''}"><i class="dot" style="background:${bc(b.id)}"></i>${esc(b.name)}<small>${b.stations.length} stations</small></button>`).join('');
 if(openMenu==='units')h=`<button data-mv="uf:" class="${state.uf?'':'sel'}">All apparatus</button>`+UFS.map(f=>`<button data-mv="uf:${f.id}" class="${state.uf===f.id?'sel':''}"><i class="sq" style="background:var(--u-${f.c})"></i>${esc(f.label)}</button>`).join('');
 if(openMenu==='hosp')h=`<label class="mt">Show hospitals<input type="checkbox" data-mt="hosp"${layers.hosp?' checked':''}></label><div class="msep"></div><button data-mv="hf:" class="${layers.hosp&&!state.hf?'sel':''}">All hospitals<small>${PL.hospitals.length}</small></button>`+HF.map(([k,l])=>`<button data-mv="hf:${k}" class="${state.hf===k?'sel':''}">${esc(l)}<small>${PL.hospitals.filter(x=>x.des.includes(k)).length}</small></button>`).join('')+`<div class="msep"></div><button class="go" data-mv="table">Hospital table →</button>`;
 if(openMenu==='lm')h=`<label class="mt">Show landmarks<input type="checkbox" data-mt="lm"${layers.lm?' checked':''}></label><div class="msep"></div>`+Object.entries(PL.kinds).map(([k,v])=>`<label class="kr k-${k}"><input type="checkbox" data-mk="${k}"${layers.kinds[k]!==false?' checked':''}${layers.lm?'':' disabled'}><svg width="15" height="15"><use href="#g-${k}"/></svg><span>${esc(v.label)}</span></label>`).join('');
 m.innerHTML=h;m.hidden=false;const b=$(`#fbar [data-fb="${openMenu}"]`),mr=$('#map').getBoundingClientRect(),r=b.getBoundingClientRect();
 m.style.top=(r.bottom-mr.top+6)+'px';m.style.left=Math.max(10,Math.min(r.left-mr.left,mr.width-m.offsetWidth-10))+'px'}
function closeMenu(){if(openMenu){openMenu=null;renderFbar()}}
function initFbar(){
 $('#fbar').addEventListener('click',e=>{const b=e.target.closest('[data-fb]');if(!b)return;const id=b.dataset.fb;
  if(id==='clear'){openMenu=null;state.hf=null;state.uf=null;state.place=null;state.sel=null;return setBat(null)}
  openMenu=openMenu===id?null:id;renderFbar()});
 $('#fmenu').addEventListener('click',e=>{const b=e.target.closest('button[data-mv]');if(!b)return;const[kind,val]=b.dataset.mv.split(':');openMenu=null;
  if(kind==='bat')return setBat(val||null);
  if(kind==='uf')return setUF(val||null);
  if(kind==='hf'){layers.hosp=true;state.hf=val||null;syncLayers();return openHospitals()}
  if(kind==='table'){layers.hosp=true;syncLayers();return openHospitals()}});
 $('#fmenu').addEventListener('change',e=>{const i=e.target;if(i.dataset.mt==='hosp'){layers.hosp=i.checked;if(!i.checked)state.hf=null}else if(i.dataset.mt==='lm')layers.lm=i.checked;else if(i.dataset.mk)layers.kinds[i.dataset.mk]=i.checked;syncLayers()});
 document.addEventListener('pointerdown',e=>{if(openMenu&&!e.target.closest('#fmenu,#fbar'))closeMenu()},true);
 addEventListener('resize',()=>openMenu&&renderMenu())}
/* back navigation */
const hist=[];let restoring=false;
function pushView(v){if(restoring||state.mode!=='map')return;const last=hist[hist.length-1];if(last&&JSON.stringify(last)===JSON.stringify(v))return;hist.push(v);if(hist.length>40)hist.shift()}
const isRoot=v=>!v||(v.v==='overview'&&!v.bat&&!v.uf);
function viewLabel(v){if(!v||v.v==='overview')return v&&v.uf?UFI[v.uf].label:v&&v.bat?BAT[v.bat].name:'All stations';if(v.v==='station')return'Station '+v.n;if(v.v==='place')return PI[v.id]?(PI[v.id].short||PI[v.id].name):'Back';return v.hf?HFL[v.hf]:'Hospitals'}
function goBack(){hist.pop();const v=hist.pop()||{v:'overview'};restoreView(v)}
function restoreView(v){if(v.v==='station')return select(v.n);if(v.v==='place')return selectPlace(v.id);if(v.v==='hospitals'){state.hf=v.hf||null;return openHospitals()}
 state.sel=null;state.place=null;state.hf=null;state.bat=v.bat||null;state.uf=v.uf||null;renderFbar();renderOverview();setHash(state.uf?'units-'+state.uf:state.bat?state.bat.toLowerCase():'');fitShown()}
''')

# segSync/ufSync -> filter bar
rep("function ufSync(){for(const b of $('#uf').children)b.setAttribute('aria-pressed',String(b.dataset.uf===state.uf))}","function ufSync(){renderFbar()}")
rep("function segSync(){for(const b of $('#seg').children)b.setAttribute('aria-pressed',String((b.dataset.bat||null)===state.bat))}","function segSync(){renderFbar()}")
# openHospitals uses syncLayers already
# enter(): back bar
rep("function enter(html){pbody.innerHTML=html;","function enter(html){const cur=hist[hist.length-1],bb=state.mode==='map'&&cur&&!isRoot(cur)?`<button class=\"backbar\" data-act=\"back\"><svg width=\"14\" height=\"14\" viewBox=\"0 0 14 14\"><path d=\"M8.5 2.5L4 7l4.5 4.5\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/></svg>${esc(viewLabel(hist[hist.length-2]))}</button>`:'';pbody.innerHTML=bb+html;")
rep("function renderOverview(){\n if(state.uf)return renderUnits();","function renderOverview(){\n pushView({v:'overview',bat:state.bat,uf:state.uf});\n if(state.uf)return renderUnits();")
rep("function renderStation(s){\n const b=BAT[s.battalion]","function renderStation(s){\n pushView({v:'station',n:s.num});\n const b=BAT[s.battalion]")
rep('let h=`<div class="crumbs"><button data-act="clearuf">← All stations</button></div><p class="dept">','let h=`<p class="dept">')
rep('h+=`<div class="crumbs"><button data-act="all">← All stations</button></div><p class="dept">${b.kind','h+=`<p class="dept">${b.kind')
rep('enter(`<div class="crumbs"><button data-act="all">All</button><span>/</span><button data-bat=','enter(`<div class="crumbs"><button data-bat=')
# panel click: back
rep(" if(a==='start'||a==='again')return startGame();"," if(a==='back')return goBack();\n if(a==='start'||a==='again')return startGame();")
# keyboard Esc -> back
rep("else if(e.key==='Escape'&&state.sel){state.sel=null;renderOverview();setHash(state.bat?state.bat.toLowerCase():'');sched()}","else if(e.key==='Escape'){if(openMenu)closeMenu();else if(hist.length>1&&!isRoot(hist[hist.length-1]))goBack()}")
# promo hospitals icon
rep('<span class="pi h">H</span>','<span class="pi h"><svg width="22" height="22" viewBox="-10 -10 20 20"><path d="M-3.6-4.4v8.8M3.6-4.4v8.8M-3.6 0h7.2" fill="none" stroke="#d8241b" stroke-width="2.6"/></svg></span>')
# init: replace old seg/uf/layers wiring
i=s.index(" $('#seg').innerHTML="); j=s.index(" lastW=innerWidth;fitK=",i); s=s[:i]+" initFbar();syncLayers();\n"+s[j:]

# ---------------- games: illustrations, copy, streaks
ILL={
'pin':'<rect class="il-bg" width="160" height="84"/><path class="il-road" stroke-width="3" d="M-5 64C40 50 72 72 165 30"/><path class="il-road" stroke-width="2" d="M28-5L62 90M120-5l-18 95"/><circle class="il-mut" cx="108" cy="58" r="3.2"/><path class="il-dash" d="M108 58Q95 40 80 44"/><g class="pinbob"><path class="il-red" d="M80 46c-6.5-7.5-9.8-11.3-9.8-16a9.8 9.8 0 0 1 19.6 0c0 4.7-3.3 8.5-9.8 16z"/><circle cx="80" cy="30" r="3.6" fill="var(--home)"/></g>',
'name':'<rect class="il-bg" width="160" height="84"/><path class="il-road" stroke-width="2.5" d="M-5 30C50 40 90 20 165 52"/><circle class="il-mut" cx="30" cy="54" r="5"/><circle class="il-mut" cx="56" cy="24" r="5"/><circle class="il-mut" cx="120" cy="22" r="5"/><circle class="il-mut" cx="132" cy="62" r="5"/><circle class="il-mut" cx="62" cy="64" r="5"/><circle class="il-ring" cx="94" cy="46" r="8"/><circle class="il-red" cx="94" cy="46" r="8"/><text x="94" y="50.5" text-anchor="middle" style="font:700 11px Barlow Semi Condensed;fill:#fff">?</text>',
'numbers':'<rect class="il-bg" width="160" height="84"/><rect class="il-card" x="18" y="20" width="46" height="44" rx="8"/><text class="il-txt" x="41" y="50" text-anchor="middle">72</text><path class="il-arrow" d="M72 36h18m-5-5 5 5-5 5M90 50H72m5-5-5 5 5 5"/><rect class="il-card" x="98" y="20" width="46" height="44" rx="8"/><rect class="il-mut" x="106" y="32" width="30" height="5" rx="2.5"/><rect class="il-mut" x="106" y="42" width="22" height="5" rx="2.5" opacity=".6"/>',
'rig':'<rect class="il-bg" width="160" height="84"/><path class="il-road" stroke-width="2" d="M0 71h160"/><rect class="il-truck" x="20" y="36" width="98" height="27" rx="3"/><path class="il-truck" d="M118 63V40h13l11 11v12z"/><path class="il-win" d="M121 43h9l8 8h-17z"/><rect class="il-red" x="20" y="51" width="122" height="4"/><path d="M24 33h86M24 29h86M30 29v4M42 29v4M54 29v4M66 29v4M78 29v4M90 29v4M102 29v4" stroke="var(--mkline)" stroke-width="1.6"/><rect class="il-red" x="121" y="37" width="10" height="3" rx="1"/><circle class="il-wheel" cx="42" cy="64" r="7"/><circle class="il-wheel" cx="100" cy="64" r="7"/><circle class="il-wheel" cx="128" cy="64" r="7"/>',
'find':'<rect class="il-bg" width="160" height="84"/><path class="il-mut" d="M8 72L48 22l24 30 14-18 40 38z"/><path d="M48 22l-8 10 5-1 3 4 3-4 5 1z" fill="var(--panel2)"/><g color="var(--k-venue)"><use href="#g-venue" x="116" y="12" width="22" height="22"/></g><g transform="translate(136 56)"><rect x="-9" y="-9" width="18" height="18" rx="4" fill="#f4f4f1"/><path d="M-3.6-4.4v8.8M3.6-4.4v8.8M-3.6 0h7.2" fill="none" stroke="#d8241b" stroke-width="2.4"/></g><g color="var(--k-school)"><use href="#g-school" x="96" y="50" width="18" height="18"/></g>',
'hosp':'<rect class="il-bg" width="160" height="84"/><g transform="translate(80 42)"><circle class="il-ring" r="24"/><rect x="-22" y="-22" width="44" height="44" rx="10" fill="#f4f4f1"/><path d="M-8-10v20M8-10v20M-8 0h16" fill="none" stroke="#d8241b" stroke-width="5"/></g><g style="font:700 12px Barlow Semi Condensed"><circle cx="128" cy="26" r="11" class="il-card"/><text x="128" y="30" text-anchor="middle" fill="var(--ink)">I</text><circle cx="32" cy="58" r="11" class="il-card"/><text x="32" y="62" text-anchor="middle" fill="var(--ink)">C</text></g>'}
import json
rep("const GI=Object.fromEntries(GAMES.map(g=>[g.id,g]));","const GI=Object.fromEntries(GAMES.map(g=>[g.id,g]));\nconst ILL="+json.dumps(ILL)+";\nconst illus=id=>`<svg viewBox=\"0 0 160 84\" preserveAspectRatio=\"xMidYMid slice\" aria-hidden=\"true\">${ILL[id]}</svg>`;")
for a,b in [("blurb:'A station comes up. Tap where it is on the map.'","blurb:'We call a station. You drop the pin. Closer is better.'"),
            ("blurb:'A station lights up. Pick which one it is.'","blurb:'One station is pinging. Which one is it?'"),
            ("blurb:'Station 72 is…? Seven Springs is Station…? Tie each number to its name.'","blurb:'72 is…? Seven Springs is…? Lock in the numbers.'"),
            ("blurb:'We call out a unit. Tap the station it runs out of.'","blurb:'We call a rig. You find its house.'"),
            ("blurb:'Hospitals, high schools, parks, peaks and landmarks.'","blurb:'Hospitals, schools, parks and peaks. Pin it.'"),
            ("blurb:'Trauma, burn, stroke, STEMI and pediatric centers.'","blurb:'Trauma, burn, stroke, STEMI. Who has what?'")]:
    rep(a,b)
rep("const tier=d=>d<0.05?'Perfect':d<0.25?'Bullseye':d<0.75?'Close':d<2?'In the area':d<5?'Wrong part of town':'Way off';",
    "const tier=d=>d<0.05?'Bullseye!':d<0.25?'Right on top of it':d<0.75?'Close. Real close.':d<2?'Right neighborhood':d<5?'Wrong side of the freeway':d<12?'Wrong town':'Are we still in the county?';\nconst headline=p=>p>=90?'Dispatch-ready.':p>=75?'First-due material.':p>=50?'Getting your bearings.':p>=25?'Keep the map book handy.':'Rookie run. Go again.';\nconst FLAME='<svg width=\"13\" height=\"13\"><use href=\"#g-flame\"/></svg>';")
span("function renderStudy(){setup.id=null;","function openSetup(",r'''function renderStudy(){setup.id=null;
 enter(`<p class="dept">Study</p><h1>Learn the county</h1><p class="area">Quick games on the real map. Pick one, choose how many, go.</p>
 <div class="cards">${GAMES.map(G=>{const b=best('fa-best2-'+G.id+(G.id==='find'?'-all':''));return`<button class="game" data-game="${G.id}"><span class="ill">${illus(G.id)}</span><strong>${esc(G.title)}</strong><span class="bl">${esc(G.blurb)}</span>${b?`<small>Best ${b}%</small>`:''}</button>`}).join('')}</div>`)}
''')
rep(' enter(`<div class="crumbs"><button data-act="studyhome">← Study</button></div><p class="dept">Study</p><h1>${esc(G.title)}</h1>',' enter(`<div class="crumbs"><button data-act="studyhome">← Study</button></div><div class="hero-ill">${illus(G.id)}</div><h1>${esc(G.title)}</h1>')
rep("state.game={id:G.id,rounds,i:0,score:0,log:[],D:Dm};","state.game={id:G.id,rounds,i:0,score:0,log:[],D:Dm,streak:0};")
rep("c.p=ptsFor(c.d,g.D);g.score+=c.p;","c.p=ptsFor(c.d,g.D);g.score+=c.p;g.streak=c.p>=4000?g.streak+1:0;")
rep("if(c.ok)g.score++;g.log.push({c,ok:c.ok})}","if(c.ok)g.score++;g.streak=c.ok?g.streak+1:0;g.log.push({c,ok:c.ok})}")
rep("${c.ok?['Correct','Yes','Got it'][g.i%3]:'Not quite'}","${c.ok?['Correct','Nailed it','Yep','That\\'s the one'][g.i%4]:['Not quite','Close, but no','Nope'][g.i%3]}")
rep('<span class="nav prog">${g.phase===\'done\'?\'\':`${g.i+1} of ${n}`}</span>','<span class="nav prog">${g.phase!==\'done\'&&g.streak>=3?`<span class="streak">${FLAME}${g.streak} in a row</span>`:\'\'}${g.phase===\'done\'?\'\':`${g.i+1} of ${n}`}</span>')
rep('h+=`<p class="dept">${esc(G.title)}</p><div class="final">','h+=`<p class="dept">${esc(G.title)}</p><h1 class="prompt sm">${headline(g.pct)}</h1><div class="final">')
open(p,'w').write(s);print("patched")
