# -*- coding: utf-8 -*-
from generate import SITE_URL, ROOT
from part2 import SERVICES, LANDING_NICHES
from part3 import PRODUCTS
from part4 import ARTICLES
import os

urls = ["index.html", "services/index.html", "store/index.html", "blog/index.html",
        "portfolio.html", "reviews.html", "about.html", "contact.html"]
urls += [f"services/{s['slug']}.html" for s in SERVICES]
urls += [f"services/{n['slug']}.html" for n in LANDING_NICHES]
urls += [f"store/{p['slug']}.html" for p in PRODUCTS]
urls += [f"blog/{a['slug']}.html" for a in ARTICLES]

entries = "\n".join(
    f"  <url>\n    <loc>{SITE_URL}/{u}</loc>\n  </url>" for u in urls
)
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)

print("sitemap + robots done, total urls:", len(urls))
