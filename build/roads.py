import json, urllib.request, urllib.parse, math
B="https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Transportation/MapServer/%d/query?"
g=json.load(open("google_pins.json"))
out={}
for n,(lat,lon) in g.items():
    d=0.0022
    env=f"{lon-d},{lat-d},{lon+d},{lat+d}"
    feats=[]
    for layer in (2,6,8):
        p={"where":"1=1","outFields":"NAME,MTFCC","outSR":"4326","f":"geojson","geometry":env,"geometryType":"esriGeometryEnvelope","inSR":"4326","spatialRel":"esriSpatialRelIntersects"}
        try:
            r=json.load(urllib.request.urlopen(B%layer+urllib.parse.urlencode(p),timeout=60))
            feats+=r.get("features",[])
        except Exception as e: print("err",n,layer,e)
    out[n]=feats
    print(n,sorted({(f["properties"].get("NAME") or f["properties"].get("FULLNAME") or "?") for f in feats}))
json.dump(out,open("roads_near.json","w"))
