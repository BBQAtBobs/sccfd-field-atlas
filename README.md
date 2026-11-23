# SCCFD Field Atlas

An interactive map and study tool for Santa Clara County Fire Department stations,
apparatus, hospitals and landmarks. Built by a recruit, for recruits.

**Live site:** https://bbqatbobs.github.io/sccfd-field-atlas/

## Disclaimer

Unofficial study aid built from public documents. **Not an SCCFD product**, not
endorsed by the department, and not a dispatch or operational reference. Station
data, staffing and unit assignments are still being fact-checked against academy
materials — verify anything that matters against official sources.

## What's in it

- **Map** — 19 stations with battalion colors, apparatus filters, 11 hospitals with
  SCC EMS Policy 602 designations, and 42 landmarks. County, city, highway and water
  outlines drawn from Census TIGER data, so it works with no map tiles.
- **Station cards** — address, on-duty staffing, every unit, nearest stations,
  building details, photo, and links out to Street View and Google Maps.
- **Study** — six games: Drop the pin, Name that station, Numbers & names,
  Where's the rig?, Find it on the map, and Hospital designations.

## Structure

| Path | What it is |
|---|---|
| `index.html` | The entire app. One file, no build step, no framework. |
| `data/stations.json` | Source of truth: stations, battalions, apparatus, staffing, photos. |
| `data/places.json` | Hospitals with EMS designations, plus landmarks. |
| `data/geo.json` | County, city, highway and water geometry (Census TIGER). |
| `images/stations/` | Station photos from the SCCFD facilities page. |
| `build/` | One-off scripts used to geocode, fetch geometry and test. Not needed to run the site. |

Edit `data/stations.json` and every screen updates.

## Running it locally

It fetches its data files, so open it through a server rather than as a `file://` URL:

```
python3 -m http.server 8000
```

Then visit http://localhost:8000

## Sources

- SCCFD Facilities and Fire Stations page (stations, photos)
- SCCFD 2025 Annual Report (org chart, station list)
- SCCFD Fire Suppression & Rescue page (apparatus)
- Santa Clara County EMS Policy 602, Table B, eff. Sept 1 2025 (hospital designations)
- US Census TIGER (geometry)
