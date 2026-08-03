# -*- coding: utf-8 -*-
import os
import urllib.parse

ROOT = "/home/claude/site"
WA = "https://wa.me/201126104846"
SITE_URL = "https://worklixeg.github.io/worklixeg"  # live GitHub Pages URL
OG_IMAGE_URL = f"{SITE_URL}/assets/og-image.png"

def wa_link(message):
    return f"{WA}?text=" + urllib.parse.quote(message)

WA_GENERIC = wa_link("مرحبًا، أنا عايز أطلب خدمة من WORKLIXEG.")

FONT_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

def nav(depth):
    p = "" if depth == 0 else "../"
    return {
        "home": f"{p}index.html",
        "services": f"{p}services/index.html",
        "store": f"{p}store/index.html",
        "portfolio": f"{p}portfolio.html",
        "blog": f"{p}blog/index.html",
        "reviews": f"{p}reviews.html",
        "about": f"{p}about.html",
        "contact": f"{p}contact.html",
        "assets": f"{p}assets/",
        "favicon": f"{p}favicon.ico",
        "manifest": f"{p}site.webmanifest",
        "icons": f"{p}assets/icons/",
    }

def header(depth, active=""):
    n = nav(depth)
    def cls(key):
        return "text-orange" if key == active else ""
    return f"""<header id="site-header" class="fixed top-0 inset-x-0 z-50 transition-all duration-300" style="background:transparent;">
  <div class="max-w-7xl mx-auto px-5 md:px-8">
    <div class="flex items-center justify-between h-[76px]">
      <a href="{n['home']}" class="flex items-center gap-2">
        <img src="{n['icons']}logo-mark.png" alt="WORKLIXEG" class="w-8 h-8 rounded-lg" width="32" height="32">
        <span class="font-latin font-extrabold text-2xl tracking-tight text-white">WORKLIX<span class="text-orange">EG</span></span>
      </a>
      <nav class="hidden lg:flex items-center gap-8 font-medium text-[15px] text-white" id="nav-links">
        <a href="{n['services']}" class="hover:text-orange transition {cls('services')}">الخدمات</a>
        <a href="{n['store']}" class="hover:text-orange transition {cls('store')}">المتجر</a>
        <a href="{n['portfolio']}" class="hover:text-orange transition {cls('portfolio')}">أعمالنا</a>
        <a href="{n['blog']}" class="hover:text-orange transition {cls('blog')}">المدونة</a>
        <a href="{n['reviews']}" class="hover:text-orange transition {cls('reviews')}">آراء العملاء</a>
        <a href="{n['about']}" class="hover:text-orange transition {cls('about')}">من نحن</a>
        <a href="{n['contact']}" class="hover:text-orange transition {cls('contact')}">اتصل بنا</a>
      </nav>
      <div class="hidden lg:flex items-center gap-4">
        <a href="{WA_GENERIC}" target="_blank" rel="noopener" class="bg-orange text-white font-bold text-sm px-6 py-3 rounded-2xl hover:brightness-110 transition shadow-lg shadow-orange-500/20">ابدأ الآن</a>
      </div>
      <button id="menu-btn" class="lg:hidden text-white p-2" aria-label="فتح القائمة">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
  <div id="mobile-menu" class="hidden lg:hidden bg-navy border-t border-line px-5 py-6 space-y-4 text-white">
    <a href="{n['services']}" class="block font-medium">الخدمات</a>
    <a href="{n['store']}" class="block font-medium">المتجر</a>
    <a href="{n['portfolio']}" class="block font-medium">أعمالنا</a>
    <a href="{n['blog']}" class="block font-medium">المدونة</a>
    <a href="{n['reviews']}" class="block font-medium">آراء العملاء</a>
    <a href="{n['about']}" class="block font-medium">من نحن</a>
    <a href="{n['contact']}" class="block font-medium">اتصل بنا</a>
    <a href="{WA_GENERIC}" class="block bg-orange text-center font-bold rounded-2xl py-3 mt-2">ابدأ الآن</a>
  </div>
</header>"""

def footer(depth):
    n = nav(depth)
    return f"""<footer id="footer-contact" class="bg-[#080D18] text-muted pt-20 pb-10">
  <div class="max-w-7xl mx-auto px-5 md:px-8 grid sm:grid-cols-2 lg:grid-cols-5 gap-10 mb-14">
    <div class="lg:col-span-2">
      <div class="flex items-center gap-2 mb-1">
        <img src="{n['icons']}logo-mark.png" alt="WORKLIXEG" class="w-8 h-8 rounded-lg" width="32" height="32">
        <span class="font-latin font-extrabold text-2xl text-white">WORKLIX<span class="text-orange">EG</span></span>
      </div>
      <p class="mt-4 text-sm leading-relaxed max-w-xs">منصة خدمات مهنية لبناء حضورك الوظيفي في مصر ودول الخليج: سيرة ذاتية، LinkedIn، بورتفوليو، واستشارات مهنية.</p>
      <div class="flex gap-3 mt-6">
        <a href="{WA_GENERIC}" class="w-9 h-9 rounded-full border border-line flex items-center justify-center hover:bg-white/10">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.3 5L2 22l5.2-1.4c1.4.8 3.1 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2z"/></svg>
        </a>
      </div>
    </div>
    <div>
      <h4 class="font-bold text-white mb-4">الشركة</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="{n['about']}" class="hover:text-orange">من نحن</a></li>
        <li><a href="{n['services']}" class="hover:text-orange">الخدمات</a></li>
        <li><a href="{n['store']}" class="hover:text-orange">المتجر</a></li>
        <li><a href="{n['blog']}" class="hover:text-orange">المدونة</a></li>
      </ul>
    </div>
    <div>
      <h4 class="font-bold text-white mb-4">روابط</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="{n['portfolio']}" class="hover:text-orange">أعمالنا</a></li>
        <li><a href="{n['reviews']}" class="hover:text-orange">آراء العملاء</a></li>
        <li><a href="{n['home']}#faq" class="hover:text-orange">الأسئلة الشائعة</a></li>
        <li><a href="{n['contact']}" class="hover:text-orange">اتصل بنا</a></li>
      </ul>
    </div>
    <div>
      <h4 class="font-bold text-white mb-4">تواصل معنا</h4>
      <ul class="space-y-2 text-sm font-latin" dir="ltr">
        <li>+20 112 610 4846</li>
        <li>info@worklixeg.com</li>
        <li dir="rtl">السبت – الخميس، 10ص – 10م</li>
        <li dir="rtl">الدفع: فودافون كاش / InstaPay</li>
      </ul>
    </div>
  </div>
  <div class="max-w-7xl mx-auto px-5 md:px-8 border-t border-line pt-8 text-xs text-center">
    © 2026 WORKLIXEG. جميع الحقوق محفوظة.
  </div>
</footer>"""

def breadcrumb_html(items, depth):
    n = nav(depth)
    parts = [f'<a href="{n["home"]}" class="hover:text-orange">الرئيسية</a>']
    for label, href in items:
        if href:
            parts.append(f'<span class="mx-1 text-gray-400">/</span><a href="{href}" class="hover:text-orange">{label}</a>')
        else:
            parts.append(f'<span class="mx-1 text-gray-400">/</span><span class="text-navy font-semibold">{label}</span>')
    return f'<nav class="breadcrumb max-w-7xl mx-auto px-5 md:px-8 pt-28 pb-2 text-sm text-gray-500" aria-label="breadcrumb">' + "".join(parts) + "</nav>"

def page(depth, active, title, description, keywords, canonical, h1_breadcrumb, breadcrumb_items, body, extra_schema="", og_type="website"):
    n = nav(depth)
    asset_prefix = n["assets"]
    bc = breadcrumb_html(breadcrumb_items, depth) if breadcrumb_items is not None else ""
    schema_block = ""
    if extra_schema:
        schema_block = f'<script type="application/ld+json">{extra_schema}</script>'
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canonical}">
<meta name="geo.region" content="EG">
<meta name="geo.placename" content="Cairo">
<meta name="theme-color" content="#0B1220">
<link rel="icon" href="{n['favicon']}" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{n['icons']}favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{n['icons']}favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{n['icons']}apple-touch-icon.png">
<link rel="manifest" href="{n['manifest']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="ar_EG">
<meta property="og:image" content="{OG_IMAGE_URL}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="WORKLIXEG">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{OG_IMAGE_URL}">
{FONT_LINKS}
<link rel="stylesheet" href="{asset_prefix}tailwind.css">
<link rel="stylesheet" href="{asset_prefix}style.css">
{schema_block}
</head>
<body class="antialiased">
<a href="#main" class="skip-link sr-only">تخطَّ إلى المحتوى</a>
{header(depth, active)}
{bc}
<main id="main">
{body}
</main>
{footer(depth)}
<script src="{asset_prefix}main.js"></script>
</body>
</html>
"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def hero_simple(eyebrow, h1, sub, cta_label="اطلب الخدمة الآن", cta_href=None):
    href = cta_href or WA_GENERIC
    return f"""<section class="relative bg-navy grain overflow-hidden pt-10">
  <div class="absolute -top-40 -left-40 w-[500px] h-[500px] bg-orange/10 rounded-full blur-3xl"></div>
  <div class="max-w-4xl mx-auto px-5 md:px-8 py-16 md:py-20 text-center relative z-10 text-white">
    <span class="inline-flex items-center gap-2 text-xs font-semibold tracking-wide bg-white/5 border border-line rounded-full px-4 py-2 text-orange mb-6">{eyebrow}</span>
    <h1 class="font-extrabold text-3xl md:text-5xl leading-[1.2] mb-6">{h1}</h1>
    <p class="text-muted text-lg leading-relaxed mb-9 max-w-2xl mx-auto">{sub}</p>
    <a href="{href}" class="inline-block bg-orange text-white font-bold px-9 py-4 rounded-2xl hover:brightness-110 transition shadow-xl shadow-orange-500/25">{cta_label}</a>
  </div>
</section>"""

def cta_band(heading, sub, cta_href=None):
    href = cta_href or WA_GENERIC
    return f"""<section class="bg-navy py-20 relative overflow-hidden grain">
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="w-[600px] h-[600px] bg-orange/10 rounded-full blur-3xl"></div>
  </div>
  <div class="max-w-2xl mx-auto px-5 text-center relative z-10">
    <h2 class="font-extrabold text-2xl md:text-4xl text-white mb-5">{heading}</h2>
    <p class="text-muted text-lg mb-8">{sub}</p>
    <a href="{href}" class="inline-block bg-orange text-white font-bold px-9 py-4 rounded-2xl hover:brightness-110 transition shadow-xl shadow-orange-500/25">تواصل معنا الآن</a>
  </div>
</section>"""

def faq_block(faqs, id_prefix="faq"):
    items = ""
    for i, (q, a) in enumerate(faqs):
        items += f"""<div class="border border-gray-200 rounded-2xl overflow-hidden">
        <button class="faq-btn w-full flex items-center justify-between p-5 font-bold text-right">
          {q}
          <span class="faq-icon text-orange text-xl">+</span>
        </button>
        <div class="accordion-content px-5">
          <p class="text-gray-500 pb-5">{a}</p>
        </div>
      </div>"""
    return f"""<section class="bg-white py-20">
  <div class="max-w-3xl mx-auto px-5 md:px-8">
    <div class="text-center mb-12">
      <span class="text-orange font-bold text-sm tracking-wide">الأسئلة الشائعة</span>
      <h2 class="font-extrabold text-2xl md:text-3xl mt-3">أسئلة يتكرر سؤالنا عنها</h2>
    </div>
    <div class="space-y-4">{items}</div>
  </div>
</section>"""

def faq_schema(faqs):
    entries = []
    for q, a in faqs:
        entries.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a))
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(entries) + "]}"

def internal_links_grid(title, links):
    cards = ""
    for label, href, desc in links:
        cards += f"""<a href="{href}" class="bg-white rounded-2xl p-6 border border-gray-100 card-hover block">
      <h3 class="font-bold mb-2">{label}</h3>
      <p class="text-gray-500 text-sm">{desc}</p>
    </a>"""
    return f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <h2 class="font-extrabold text-2xl md:text-3xl mb-8 text-center">{title}</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
</section>"""

print("helpers loaded")
