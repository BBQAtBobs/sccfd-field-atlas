import json, time, urllib.request, urllib.parse, sys
UA={"User-Agent":"SCCFD-Field-Atlas-prototype/0.1 (study tool)"}
VB="-122.25,37.50,-121.18,36.88"
def nom(q,bounded=True):
    p={"q":q,"format":"jsonv2","limit":1,"countrycodes":"us"}
    if bounded: p.update({"viewbox":VB,"bounded":1})
    r=json.load(urllib.request.urlopen(urllib.request.Request("https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode(p),headers=UA),timeout=25)); time.sleep(1.15)
    return r[0] if r else None
items=json.load(open("places_in.json"))
out=[]
for it in items:
    r=None
    for q in it["q"]:
        r=nom(q)
        if r: break
    print(("OK " if r else "-- ")+it["id"],(r["lat"],r["lon"],r["display_name"][:80]) if r else it["q"],flush=True)
    if r: out.append({**{k:v for k,v in it.items() if k!="q"},"lat":round(float(r["lat"]),5),"lon":round(float(r["lon"]),5),"osm":r["display_name"][:120]})
json.dump(out,open("places_out.json","w"),indent=1)
