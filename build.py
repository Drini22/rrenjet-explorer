#!/usr/bin/env python3
"""Assemble the self-contained explorer from app_template.html.

Outputs:
  index.html            — full standalone page (open locally in any browser)
  rrenjet-explorer.html — same content without the <!doctype>/<html> wrapper
                          (for publishing as a Claude Artifact, which adds its own skeleton)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
read = lambda p: open(os.path.join(HERE, p), encoding="utf-8").read()

tpl = read("app_template.html")
content = (tpl
    .replace("/*__D3__*/", read("vendor/d3.v7.min.js"))
    .replace("/*__DATA__*/", read("data.json").strip())
    .replace("/*__GEO__*/", read("vendor/balkans.geo.json").strip())
    .replace("/*__EUROPE__*/", read("vendor/europe.geo.json").strip()))

with open(os.path.join(HERE, "rrenjet-explorer.html"), "w", encoding="utf-8") as f:
    f.write(content)

standalone = ('<!doctype html>\n<html lang="sq">\n<head>\n<meta charset="utf-8">\n'
              '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
              '</head>\n<body>\n' + content + '\n</body>\n</html>\n')
with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
    f.write(standalone)

print("index.html:", os.path.getsize(os.path.join(HERE, "index.html")), "bytes")
print("rrenjet-explorer.html:", os.path.getsize(os.path.join(HERE, "rrenjet-explorer.html")), "bytes")
