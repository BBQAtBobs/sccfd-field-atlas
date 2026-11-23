import json, urllib.request, urllib.parse, sys
B="https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/"
BBOX="-122.25,36.88,-121.18,37.50"
def q(svc,layer,where,fields,geom=True,offset=0.0004,bbox=BBOX):
    p={"where":where,"outFields":fields,"outSR":"4326","f":"geojson","returnGeometry":"true","maxAllowableOffset":offset}
    if bbox: p.update({"geometry":bbox,"geometryType":"esriGeometryEnvelope","inSR":"4326","spatialRel":"esriSpatialRelIntersects"})
    url=B+svc+"/MapServer/%d/query?"%layer+urllib.parse.urlencode(p)
    d=json.load(urllib.request.urlopen(url,timeout=120))
    print(svc,layer,len(d.get("features",[])),"features", d.get("error",""),file=sys.stderr)
    return d
out={}
out["counties"]=q("tigerWMS_Current",82,"STATE='06'","NAME,COUNTY",offset=0.0008)
out["places"]=q("tigerWMS_Current",28,"STATE='06'","NAME",offset=0.0003)
out["cdps"]=q("tigerWMS_Current",30,"STATE='06'","NAME",offset=0.0003)
out["primary"]=q("Transportation",2,"1=1","NAME,RTTYP",offset=0.0003)
out["secondary"]=q("Transportation",5,"1=1","NAME,RTTYP",offset=0.0003)
out["water"]=q("Hydro",1,"AREALAND IS NULL OR 1=1","NAME,MTFCC",offset=0.0004)
json.dump(out,open("geo_raw.json","w"))
