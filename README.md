# Rrënjët Explorer

**Live site:** https://drini22.github.io/rrenjet-explorer/

Interactive web atlas of 2,183 Albanian Y-DNA samples, built on the public data of
[rrenjet.com](https://rrenjet.com) (The Albanian DNA Project). The source data is the
local mirror in `../ADN/rrenjet/` (refreshed 2026-08-19; the previous snapshot is
preserved in `../ADN/rrenjet/raw/pages_2026-05-21/`).

**Open `index.html` in any browser — no server needed.** Everything (D3, data, map
geometry) is inlined into one self-contained file.

## Features

- **Lineage tree** — zoomable sunburst of every SNP chain; click an arc to drill into a
  subclade, click the center to go back up.
- **Map** — pie markers per county/region across Albania, Kosovo, North Macedonia,
  Montenegro, Çamëria and the Preshevë valley, sized by sample count.
- **Arrival chronology** — timeline (Mesolithic → Ottoman) of when each clade's ancestors
  arrived in the Balkans, with arrival windows, expansion bursts, and per-clade stories;
  rows click-through to filter. Interpretive — based on within-clade diversity, ancient
  DNA, and rrenjet.com's own articles.
- **Migration map** — a Europe-scale map (Scandinavia → Levant) with a 9-stop era slider
  (Neolithic → Ottoman): simplified historical borders/cultural zones per era, 2–3 schematic
  arrows per clade, and a synced bilingual story panel explaining each movement. Scenes and
  arrows are hand-authored in `MIG` inside the template.
- **Regional composition** — 100% stacked bars of haplogroup share per county.
- **Compare your result** — paste a terminal SNP or full chain (`E-V13>Z5018>…`) to find
  samples with shared markers.
- **Sample table** — all records, paginated, with the full Y-DNA chain.
- Every view cross-filters the others; plus search, country/clan filters, a
  Shqip/English toggle, and automatic light/dark theming.

## Files

| File | Purpose |
|---|---|
| `app_template.html` | Source of the app (markup, CSS, JS) with `__D3__`/`__DATA__`/`__GEO__` placeholders |
| `build_data.py` | `../ADN/rrenjet/extracted/database_normalized.csv` → `data.json` |
| `build.py` | Assembles `index.html` (standalone) and `rrenjet-explorer.html` (artifact variant, no doctype wrapper) |
| `vendor/d3.v7.min.js` | D3 v7.9.0 (inlined at build time) |
| `vendor/balkans.geo.json` | Country outlines extracted from world-atlas countries-50m |
| `data.json` | Compact sample data: `[surname, fis, rreth, qark, country, [chain…]]` |

## Rebuilding

```bash
python3 build_data.py   # only if the source CSV changed
python3 build.py
```

Haplogroup colors are the 8-slot categorical palette (validated for colorblind safety in
light and dark modes) mapped in fixed order to E-V13, R1b-M269, J2b-L283, I2a-L460,
R1a-M417, J2a-M410, I1-M253, J1-M267; everything else folds into gray "Other".
Map pie positions are hand-placed county centroids in `QARK_LL` inside the template.
