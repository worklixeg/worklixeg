# -*- coding: utf-8 -*-
from generate import *
from part2 import ORG_SCHEMA, SERVICES

PRODUCTS = [
    {"slug": "cv-templates-pack", "name": "100 قالب CV احترافي", "short": "حزمة 100 قالب سيرة ذاتية بتصميمات متنوعة تناسب كل المجالات.", "details": "100 قالب Word جاهز للتعديل، تصميمات متنوعة بين الكلاسيكي والعصري، يناسب مختلف المجالات والمستويات الوظيفية.", "price": "150 ج.م", "keywords": "قوالب CV, قوالب سيرة ذاتية جاهزة, تحميل قوالب CV Word"},
    {"slug": "ats-resume-templates", "name": "قوالب CV متوافقة مع ATS", "short": "قوالب مُختبرة تمر بسلاسة عبر أنظمة الفرز الآلي.", "details": "مجموعة مختارة من القوالب المُختبرة على أنظمة ATS الشائعة، بتنسيق نظيف بدون جداول أو عناصر تُربك أنظمة الفرز.", "price": "120 ج.م", "keywords": "قوالب ATS, ATS resume templates, قوالب سيرة ذاتية متوافقة مع ATS"},
    {"slug": "interview-questions-guide", "name": "دليل أسئلة المقابلات PDF", "short": "أكثر أسئلة المقابلات شيوعًا مع طريقة إجابة نموذجية.", "details": "ملف PDF يغطي أكثر أسئلة المقابلات الشخصية والسلوكية شيوعًا، مع أمثلة إجابات وطريقة تركيب إجابتك بنفسك.", "price": "90 ج.م", "keywords": "أسئلة مقابلة شخصية PDF, دليل انترفيو, تحضير مقابلة عمل"},
    {"slug": "linkedin-guide-ebook", "name": "دليل LinkedIn الشامل", "short": "خطوات عملية لبناء ملف LinkedIn يجذب الفرص.", "details": "دليل رقمي يشرح خطوة بخطوة كيفية كتابة العنوان والملخص واختيار الكلمات المفتاحية وبناء شبكة علاقات مهنية فعالة.", "price": "100 ج.م", "keywords": "دليل لينكدإن, LinkedIn guide عربي, تحسين بروفايل لينكدإن"},
    {"slug": "career-planner-template", "name": "مخطط التطور المهني", "short": "قالب تخطيط يساعدك تحدد أهدافك المهنية للسنة القادمة.", "details": "قالب قابل للتعديل يساعدك تحلل وضعك الحالي، تحدد أهدافك المهنية، وتضع خطة عملية زمنية للوصول لها.", "price": "80 ج.م", "keywords": "مخطط مهني, career planner, خطة تطوير مهني"},
    {"slug": "ats-keywords-pack", "name": "حزمة كلمات ATS المفتاحية", "short": "قوائم كلمات مفتاحية جاهزة لأكثر من 15 مجال وظيفي.", "details": "قوائم كلمات مفتاحية منظمة حسب المجال (هندسة، محاسبة، تسويق، برمجة وغيرها) تساعدك تدمجها في سيرتك الذاتية بذكاء.", "price": "70 ج.م", "keywords": "كلمات مفتاحية ATS, ATS keywords, كلمات CV ATS"},
]

def wa_product_link(name):
    return wa_link(f"مرحبًا، أنا عايز أطلب/أحمّل: {name}")

def product_body(p, depth):
    order_href = wa_product_link(p["name"])
    others = [x for x in PRODUCTS if x["slug"] != p["slug"]][:3]
    related_links = [(o["name"], f"{o['slug']}.html", o["short"]) for o in others]
    body = hero_simple("منتج رقمي", p["name"], p["short"], cta_label="حمّل المنتج الآن", cta_href=order_href)
    body += f"""<section class="max-w-4xl mx-auto px-5 md:px-8 py-16">
  <div class="bg-white rounded-3xl border border-gray-100 p-10 grid md:grid-cols-2 gap-10 items-center">
    <div class="h-48 bg-gray-100 rounded-2xl flex items-center justify-center">
      <div class="w-24 h-32 bg-white rounded shadow-md border border-gray-200"></div>
    </div>
    <div>
      <h2 class="font-extrabold text-xl mb-3">تفاصيل المنتج</h2>
      <p class="text-gray-600 leading-relaxed mb-6">{p['details']}</p>
      <div class="flex items-center justify-between">
        <span class="font-latin font-bold text-2xl text-navy">{p['price']}</span>
        <a href="{order_href}" class="bg-orange text-white font-bold px-7 py-3 rounded-2xl hover:brightness-110 transition">تحميل الآن عبر واتساب</a>
      </div>
    </div>
  </div>
</section>"""
    body += internal_links_grid("منتجات تانية من المتجر", related_links)
    body += cta_band("محتاج نسخة مخصصة لمجالك؟", "تواصل معنا ونجهزلك نسخة مطابقة لاحتياجك بالضبط.", cta_href=order_href)
    return body

for p in PRODUCTS:
    canonical = f"{SITE_URL}/store/{p['slug']}.html"
    schema = ('[' + ORG_SCHEMA + ',' + '{"@context":"https://schema.org","@type":"Product","name":"%s","description":"%s","offers":{"@type":"Offer","priceCurrency":"EGP","price":"%s","availability":"https://schema.org/InStock"}}' % (p["name"], p["short"], p["price"].replace(" ج.م", "")) + ']')
    body = product_body(p, 1)
    html = page(depth=1, active="store", title=f"{p['name']} | متجر WORKLIXEG الرقمي", description=p["short"], keywords=p["keywords"], canonical=canonical, h1_breadcrumb=p["name"], breadcrumb_items=[("المتجر", "index.html"), (p["name"], None)], body=body, extra_schema=schema)
    write(f"store/{p['slug']}.html", html)

cards = ""
for p in PRODUCTS:
    cards += f"""<a href="{p['slug']}.html" class="bg-white rounded-3xl overflow-hidden border border-gray-100 card-hover block">
      <div class="h-40 bg-gray-100 flex items-center justify-center">
        <div class="w-20 h-28 bg-white rounded shadow-md border border-gray-200"></div>
      </div>
      <div class="p-6">
        <h3 class="font-bold mb-1">{p['name']}</h3>
        <p class="text-gray-500 text-sm mb-4">{p['short']}</p>
        <div class="flex items-center justify-between">
          <span class="font-latin font-bold text-navy">{p['price']}</span>
          <span class="text-sm font-semibold bg-navy text-white px-4 py-2 rounded-xl">تحميل</span>
        </div>
      </div>
    </a>"""
store_hub_body = hero_simple("المتجر الرقمي", "قوالب وأدلة رقمية جاهزة للتحميل الفوري", "منتجات رقمية مصممة باحتراف لتوفر وقتك: قوالب CV متوافقة مع ATS، أدلة مقابلات، وحزم كلمات مفتاحية جاهزة.")
store_hub_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{cards}</div>
</section>"""
store_hub_body += cta_band("محتاج تصميم مخصص بدل الجاهز؟", "خدماتنا المهنية بتقدملك حل مصمم خصيصًا لك.")
write("store/index.html", page(depth=1, active="store", title="متجر WORKLIXEG الرقمي | قوالب CV وأدلة توظيف جاهزة للتحميل", description="تصفح متجر WORKLIXEG الرقمي: قوالب سيرة ذاتية متوافقة مع ATS، أدلة مقابلات، دليل LinkedIn، وحزم كلمات مفتاحية جاهزة للتحميل الفوري.", keywords="متجر رقمي, قوالب CV, أدلة توظيف, منتجات رقمية للتوظيف, قوالب سيرة ذاتية للتحميل", canonical=f"{SITE_URL}/store/index.html", h1_breadcrumb="المتجر", breadcrumb_items=[("المتجر", None)], body=store_hub_body, extra_schema='[' + ORG_SCHEMA + ']'))

print("store done:", len(PRODUCTS))
