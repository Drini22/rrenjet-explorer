#!/usr/bin/env python3
"""Convert the rrenjet.com scrape into compact JSON for the explorer webapp.

Reads ../ADN/rrenjet/extracted/database_normalized.csv, fixes known data quirks,
and writes data.json: {"samples": [[surname, fis, rreth, qark, country, [chain...]], ...]}
"""
import csv, json, os

SRC = os.path.join(os.path.dirname(__file__), "..", "ADN", "rrenjet", "extracted", "database_normalized.csv")
OUT = os.path.join(os.path.dirname(__file__), "data.json")

# Merge inconsistent spellings of the same qark
QARK_FIX = {
    "Rajoni verilind.": "Rajoni verilindor",
}

def main():
    with open(SRC, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    samples = []
    for r in rows:
        chain = [s for s in r["chain_list"].split("|") if s]
        if not chain:
            continue
        qark = QARK_FIX.get(r["Qarku"].strip(), r["Qarku"].strip())
        samples.append([
            r["Mbiemri"].strip(),
            r["Fisi"].strip(),
            r["Rrethi"].strip(),
            qark,
            r["Shteti"].strip(),
            chain,
        ])
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"samples": samples}, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(samples)} samples -> {OUT} ({os.path.getsize(OUT)} bytes)")

if __name__ == "__main__":
    main()
