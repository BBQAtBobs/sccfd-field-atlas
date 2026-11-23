import json, time, urllib.request, urllib.parse
UA={"User-Agent":"SCCFD-Field-Atlas-prototype/0.1 (study tool)"}
def census(a):
    q=urllib.parse.urlencode({"address":a,"benchmark":"Public_AR_Current","format":"json"})
    try:
        r=json.load(urllib.request.urlopen("https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?"+q,timeout=30))
        m=r["result"]["addressMatches"]
        return [(x["coordinates"]["y"],x["coordinates"]["x"],x["matchedAddress"]) for x in m]
    except Exception as e: return str(e)
def nom(q,extra={}):
    p={"q":q,"format":"jsonv2","limit":5,"countrycodes":"us"};p.update(extra)
    r=json.load(urllib.request.urlopen(urllib.request.Request("https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode(p),headers=UA),timeout=20))
    time.sleep(1.2)
    return [(x["lat"],x["lon"],x["type"],x["display_name"][:100]) for x in r]
for k,a in {67:"16075 Vineyard Blvd, Morgan Hill, CA 95037",69:"3052 Hecker Pass Hwy, Gilroy, CA 95020",70:"10031 Pacheco Pass Hwy, Hollister, CA 95023",84:"21452 Madrone Dr, Los Gatos, CA 95033",68:"10810 No Name Uno, Gilroy, CA 95020"}.items():
    print(k,"census:",census(a))
for q in ["Vineyard Fire Station Morgan Hill","Treehaven Fire Station","Casa de Fruta fire station","Redwood Fire Station Los Gatos","Masten Fire Station","fire station San Martin","fire station Hecker Pass","Casa de Fruta"]:
    print(q,"->",nom(q))
