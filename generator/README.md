# WORKLIXEG — Site Generator

The whole site (`index.html`, `services/`, `store/`, `blog/`, etc.) is generated
from these Python scripts. The site is **static** (plain HTML/CSS/JS) — these
scripts are only a build tool, not something the live site depends on.

## Why it's built this way
Every page shares the same header, footer, fonts, and SEO meta-tag structure.
Instead of duplicating that markup in 30+ separate HTML files, one shared
template (`generate.py`) is reused, and each `partN.py` file holds the actual
content (services, products, blog posts, etc.) as plain Python data.

## How to regenerate the site after an edit

1. Install requirements (Python 3, Pillow, arabic_reshaper, python-bidi — only
   needed if you also regenerate the logo/OG image):
   ```
   pip install --break-system-packages pillow arabic_reshaper python-bidi
   ```
2. Edit the content you want to change — e.g. add a new service by adding a
   dict to the `SERVICES` list in `part2.py`, or edit an existing FAQ answer,
   price, or description directly in the relevant `partN.py` file.
3. From this folder, run the scripts in order (each depends on the previous):
   ```
   python3 part2.py
   python3 part3.py
   python3 part4.py
   python3 part5.py
   python3 part6.py
   python3 part7.py
   ```
   This regenerates every HTML page, `sitemap.xml`, and `robots.txt` into the
   site root (one folder up from `generator/`).
4. If you changed any HTML class names or added new Tailwind utility classes,
   rebuild the compiled CSS (from the site root, one folder up):
   ```
   ./tailwindcss -i input.css -o assets/tailwind.css --minify
   ```
   (Download the standalone CLI first if you don't have it: see
   https://github.com/tailwindlabs/tailwindcss/releases — grab the
   `tailwindcss-linux-x64` or matching binary for your OS.)
5. Commit and push the changed files to GitHub as usual.

## File map
- `generate.py` — shared header/footer/head/meta template, WhatsApp link
  builder, and small reusable HTML section helpers (hero, FAQ block, CTA
  band, internal links grid).
- `part2.py` — all 9 services + 4 landing-page niche pages, and the services
  hub page.
- `part3.py` — the 6 digital store products and the store hub page.
- `part4.py` — the 6 blog articles and the blog hub page.
- `part5.py` — portfolio, reviews, about, and contact pages.
- `part6.py` — the homepage.
- `part7.py` — `sitemap.xml` and `robots.txt`.

## Notes on honesty / content
The portfolio and reviews pages intentionally use generic, sector-based
placeholder examples (e.g. "قطاع الهندسة") rather than named fake clients or
fabricated star ratings — there is no fake Review/AggregateRating schema.
When real client testimonials and case studies exist, swap the placeholder
lists in `part5.py` (`portfolio_items`, `reviews_list`) for real ones.
