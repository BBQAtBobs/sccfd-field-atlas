import json, time, urllib.request, urllib.parse, os
UA={"User-Agent":"SCCFD-Field-Atlas-prototype/0.1 (study tool; contact via claude.ai)"}
VB="-122.25,37.50,-121.18,36.88"
cache=json.load(open("places_cache.json")) if os.path.exists("places_cache.json") else {}
def nom(q):
    for a in range(4):
        try:
            r=json.load(urllib.request.urlopen(urllib.request.Request("https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode({"q":q,"format":"jsonv2","limit":1,"countrycodes":"us","viewbox":VB,"bounded":1}),headers=UA),timeout=25))
            time.sleep(2); return r[0] if r else None
        except Exception as e:
            print("retry",q,e,flush=True); time.sleep(20)
    return None
for it in json.load(open("places_in.json")):
    if it["id"] in cache: continue
    r=None
    for q in it["q"]:
        r=nom(q)
        if r: break
    cache[it["id"]]=r and {"lat":round(float(r["lat"]),5),"lon":round(float(r["lon"]),5),"osm":r["display_name"][:110]}
    print(it["id"],cache[it["id"]],flush=True)
    json.dump(cache,open("places_cache.json","w"))
