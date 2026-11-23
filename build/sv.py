import json, math
g=json.load(open("google_pins.json")); R=json.load(open("roads_near.json"))
street={67:["Vineyard Blvd"],68:["No Name Uno Rd","Noname Uno"],69:["Hecker Pass Hwy","State Rte 152"],70:["Pacheco Pass Hwy","State Rte 152"],71:["Stevens Creek Blvd"],72:["Seven Springs Pkwy"],73:["Saratoga Ave"],74:["El Monte Rd"],75:["Almond Ave"],76:["Fremont Ave"],77:["Stevens Creek Blvd"],78:["Saratoga-Los Gatos Rd","Saratoga Los Gatos Rd","Los Gatos Saratoga Rd","State Rte 9"],79:["Cox Ave"],80:["W Sunnyoaks Ave"],81:["Union Ave"],82:["Shannon Rd"],83:["University Ave"],84:["Madrone Dr"],85:["Winchester Blvd"]}
def xy(lat,lon,lat0,lon0): return ((lon-lon0)*111320*math.cos(lat0*math.pi/180),(lat-lat0)*110540)
def ll(x,y,lat0,lon0): return (lat0+y/110540, lon0+x/(111320*math.cos(lat0*math.pi/180)))
out={}
for n,(lat,lon) in g.items():
    best=None
    for f in R[n]:
        if (f["properties"].get("NAME") or "") not in street[int(n)]: continue
        geom=f["geometry"]; ls=geom["coordinates"] if geom["type"]=="MultiLineString" else [geom["coordinates"]]
        for l in ls:
            for a,b in zip(l,l[1:]):
                ax,ay=xy(a[1],a[0],lat,lon); bx,by=xy(b[1],b[0],lat,lon)
                dx,dy=bx-ax,by-ay; L=dx*dx+dy*dy or 1e-9
                t=max(0,min(1,-(ax*dx+ay*dy)/L)); px,py=ax+t*dx,ay+t*dy; d=math.hypot(px,py)
                if best is None or d<best[0]: best=(d,px,py,math.degrees(math.atan2(dx,dy))%360)
    if not best: print(n,"NO STREET"); continue
    d,px,py,road_bearing=best
    heading=math.degrees(math.atan2(-px,-py))%360  # from road point to station
    vlat,vlon=ll(px,py,lat,lon)
    out[n]={"lat":round(vlat,6),"lon":round(vlon,6),"heading":round(heading),"setback_m":round(d)}
    print(n, out[n], "road bearing", round(road_bearing))
json.dump(out,open("streetview.json","w"),indent=1)
