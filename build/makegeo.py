import json, math
d=json.load(open("geo_raw.json"))
R=lambda c:[round(c[0],4),round(c[1],4)]
def clean_ring(r):
    out=[]
    for c in r:
        c=R(c)
        if not out or out[-1]!=c: out.append(c)
    return out
def polys(f):
    g=f["geometry"]
    if not g: return []
    ps=g["coordinates"] if g["type"]=="MultiPolygon" else [g["coordinates"]]
    return [[clean_ring(r) for r in p if len(r)>3] for p in ps]
def lines(f):
    g=f["geometry"]
    if not g: return []
    ls=g["coordinates"] if g["type"]=="MultiLineString" else [g["coordinates"]]
    return [clean_ring(l) for l in ls if len(l)>1]
def area(p):
    r=p[0]; return abs(sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1)))/2
SCCFD={"Campbell city","Cupertino city","Los Altos city","Los Altos Hills town","Los Gatos town","Monte Sereno city","Saratoga city","San Martin CDP"}
geo={"counties":[],"places":[],"roads":[],"water":[]}
for f in d["counties"]["features"]:
    geo["counties"].append({"name":f["properties"]["NAME"].replace(" County",""),"home":f["properties"]["NAME"]=="Santa Clara County","p":polys(f)})
for f in d["places"]["features"]+d["cdps"]["features"]:
    n=f["properties"]["NAME"]
    if f in d["cdps"]["features"] and n not in SCCFD|{"Loyola CDP","Lexington Hills CDP","Cambrian Park CDP","Stanford CDP"}: continue
    geo["places"].append({"name":n.rsplit(" ",1)[0],"sccfd":n in SCCFD,"cdp":n.endswith("CDP"),"p":polys(f)})
def ref(name):
    n=name.replace("I- ","I-")
    m={"W Valley Fwy":"85","Sinclair Fwy":"280","Junipero Serra Fwy":"280","Bayshore Fwy":"101","S Valley Fwy":"101","Nimitz Fwy":"880","Guadalupe Pkwy":"87"}
    if n in m: return m[n]
    for p in ("I-","State Rte ","State Hwy ","US Hwy "):
        if n.startswith(p): return n[len(p):].split()[0]
    return None
for f in d["primary"]["features"]:
    r=ref(f["properties"]["NAME"])
    if r is None: continue
    geo["roads"].append({"ref":r,"cls":"fwy","l":lines(f)})
for f in d["secondary"]["features"]:
    if f["properties"]["RTTYP"] not in ("S","U"): continue
    r=ref(f["properties"]["NAME"] or "")
    if r is None or "Bus" in (f["properties"]["NAME"] or ""): continue
    geo["roads"].append({"ref":r,"cls":"hwy","l":lines(f)})
for f in d["water"]["features"]:
    for p in polys(f):
        if area(p)>2e-5:
            geo["water"].append({"name":f["properties"]["NAME"],"p":[p]})
geo["bbox"]=[-122.25,36.88,-121.18,37.50]
s=json.dumps(geo,separators=(",",":"))
open("../data/geo.json","w").write(s)
print(len(s)//1024,"KB", {k:len(v) for k,v in geo.items() if isinstance(v,list)})
print(sorted({w["name"] for w in geo["water"] if w["name"]}))
