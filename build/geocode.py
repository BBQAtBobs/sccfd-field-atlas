import json, time, urllib.request, urllib.parse, sys
addrs = {
 67:"16075 Vineyard Blvd, Morgan Hill, CA 95037",
 68:"10810 No Name Uno, Gilroy, CA 95020",
 69:"3052 Hecker Pass Hwy, Gilroy, CA 95020",
 70:"10031 Pacheco Pass Highway, Hollister, CA 95023",
 71:"20215 Stevens Creek Blvd, Cupertino, CA 95014",
 72:"21000 Seven Springs Pkwy, Cupertino, CA 95014",
 73:"14380 Saratoga Ave, Saratoga, CA 95070",
 74:"12355 El Monte Rd, Los Altos Hills, CA 94022",
 75:"10 Almond Ave, Los Altos, CA 94022",
 76:"765 Fremont Ave, Los Altos, CA 94024",
 77:"22620 Stevens Creek Blvd, Cupertino, CA 95014",
 78:"18870 Saratoga-Los Gatos Rd, Monte Sereno, CA 95030",
 79:"19800 Cox Ave, Saratoga, CA 95070",
 80:"485 W Sunnyoaks Ave, Campbell, CA 95008",
 81:"123 Union Ave, Campbell, CA 95008",
 82:"16565 Shannon Rd, Los Gatos, CA 95032",
 83:"306 University Ave, Los Gatos, CA 95030",
 84:"21452 Madrone Dr, Los Gatos, CA 95033",
 85:"14850 Winchester Blvd, Los Gatos, CA 95032",
 0:"1315 Dell Ave, Campbell, CA 95008",
}
out={}
for k,a in addrs.items():
    q=urllib.parse.urlencode({"q":a,"format":"jsonv2","limit":1,"countrycodes":"us","addressdetails":0})
    req=urllib.request.Request("https://nominatim.openstreetmap.org/search?"+q,headers={"User-Agent":"SCCFD-Field-Atlas-prototype/0.1 (study tool)"})
    r=json.load(urllib.request.urlopen(req,timeout=20))
    out[k]=r[0] if r else None
    print(k, (r[0]["lat"],r[0]["lon"],r[0]["addresstype"],r[0]["display_name"][:90]) if r else "NOT FOUND", flush=True)
    time.sleep(1.2)
json.dump(out,open("geocode_raw.json","w"),indent=1)
