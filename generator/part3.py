# -*- coding: utf-8 -*-
from generate import *
from part2 import ORG_SCHEMA, SERVICES

PAYMENT_NUMBER = "01068204700"

PRODUCTS = [
    {
        "slug": "cv-templates-pack",
        "name": "مجموعة قوالب CV احترافية (4 تصميمات)",
        "short": "4 تصميمات مختلفة لسيرة ذاتية احترافية، بصيغة Word قابلة للتعديل مباشرة.",
        "details": "4 قوالب Word حقيقية بتصميمات مختلفة (كحلي/برتقالي، رمادي غامق/تركواز، عنابي/ذهبي، أردوازي/أخضر)، كل قالب بعمود واحد بدون جداول أو عناصر تعقّد قراءة أنظمة ATS، جاهز تكتب بياناتك فيه مباشرة.",
        "price": "150 ج.م",
        "keywords": "قوالب CV, قوالب سيرة ذاتية Word, تحميل قوالب CV",
    },
    {
        "slug": "ats-resume-templates",
        "name": "قالبين CV مبسّطين متوافقين مع ATS",
        "short": "تصميمين بسيطين جدًا (بدون ألوان أو زخرفة) مُختبرين لسهولة قراءتهم من أنظمة الفرز الآلي.",
        "details": "قالبين Word بتنسيق نص عادي بالكامل (بدون جداول، بدون أعمدة، بدون عناصر تصميم قد تُربك أنظمة الفرز الآلي)، مناسبين للشركات اللي بتستخدم أنظمة ATS صارمة.",
        "price": "100 ج.م",
        "keywords": "قوالب ATS, ATS resume templates, قوالب سيرة ذاتية متوافقة مع ATS",
    },
    {
        "slug": "interview-questions-guide",
        "name": "دليل أسئلة المقابلات PDF",
        "short": "دليل حقيقي من عدة صفحات لأكثر أسئلة المقابلات شيوعًا مع طريقة تفكير للإجابة.",
        "details": "ملف PDF من عدة صفحات يغطي الأسئلة العامة، الأسئلة السلوكية بأسلوب STAR، أسئلة الطموح والراتب، أسئلة تسألها انت للمحاور، ونصائح للمقابلات الأونلاين.",
        "price": "80 ج.م",
        "keywords": "أسئلة مقابلة شخصية PDF, دليل انترفيو, تحضير مقابلة عمل",
    },
    {
        "slug": "linkedin-guide-ebook",
        "name": "دليل LinkedIn الشامل",
        "short": "دليل PDF حقيقي بخطوات عملية لتحسين كل جزء في ملفك على LinkedIn.",
        "details": "دليل PDF يشرح كتابة العنوان (Headline) والملخص (About)، عرض الخبرات بطريقة تجذب الانتباه، اختيار الكلمات المفتاحية، الصورة الشخصية، وبناء شبكة العلاقات.",
        "price": "80 ج.م",
        "keywords": "دليل لينكدإن, LinkedIn guide عربي, تحسين بروفايل لينكدإن",
    },
    {
        "slug": "career-planner-template",
        "name": "مخطط التطور المهني (ملف Excel تفاعلي)",
        "short": "ملف Excel حقيقي بخلايا وصيغ حسابية تلقائية لتقييم وضعك وتتبع أهدافك.",
        "details": "ملف Excel بخمس أوراق عمل: تقييم الوضع الحالي بمتوسط تلقائي، الأهداف المهنية بنسب إنجاز، تحليل فجوة المهارات بحساب الفجوة تلقائيًا، وخطة عمل شهرية بنسبة إنجاز تُحسب أوتوماتيكيًا.",
        "price": "70 ج.م",
        "keywords": "مخطط مهني, career planner, خطة تطوير مهني Excel",
    },
    {
        "slug": "ats-keywords-pack",
        "name": "حزمة كلمات ATS المفتاحية (10 مجالات)",
        "short": "قوائم كلمات مفتاحية حقيقية منظمة لـ10 مجالات وظيفية مختلفة.",
        "details": "ملف PDF بقوائم كلمات مفتاحية فعلية لـ10 مجالات (هندسة، محاسبة ومالية، تسويق ومبيعات، تكنولوجيا معلومات، موارد بشرية، خدمة عملاء، إدارة مشاريع، طبي وصحي، تعليم، لوجستيات)، لدمجها بذكاء في سيرتك الذاتية.",
        "price": "60 ج.م",
        "keywords": "كلمات مفتاحية ATS, ATS keywords, كلمات CV ATS",
    },
]

def payment_instructions_html(product_name=None, price=None):
    what = f"({product_name} — {price})" if product_name else ""
    return f"""<div class="bg-white rounded-3xl border border-gray-100 p-8 mt-8">
  <h2 class="font-extrabold text-lg mb-4">طريقة الدفع والاستلام</h2>
  <ol class="text-gray-600 leading-relaxed space-y-2 list-decimal list-inside">
    <li>حوّل قيمة المنتج {what} عبر <b>فودافون كاش</b> أو <b>InstaPay</b> على الرقم:
      <span class="font-latin font-bold text-navy" dir="ltr">{PAYMENT_NUMBER}</span>
    </li>
    <li>ابعتلنا لقطة شاشة (Screenshot) لإثبات التحويل على واتساب مع اسم المنتج.</li>
    <li>هيوصلك الملف مباشرة على واتساب أو البريد الإلكتروني خلال دقائق من تأكيد الدفع.</li>
  </ol>
</div>"""

def wa_product_link(name, price):
    return wa_link(f"مرحبًا، حولت قيمة منتج \"{name}\" ({price}) عبر فودافون كاش/InstaPay على الرقم {PAYMENT_NUMBER}. مرفق إثبات التحويل.")

def product_body(p, depth):
    order_href = wa_product_link(p["name"], p["price"])
    others = [x for x in PRODUCTS if x["slug"] != p["slug"]][:3]
    related_links = [(o["name"], f"{o['slug']}.html", o["short"]) for o in others]
    body = hero_simple("منتج رقمي", p["name"], p["short"], cta_label="اطلب الآن", cta_href=order_href)
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
        <a href="{order_href}" class="bg-orange text-white font-bold px-7 py-3 rounded-2xl hover:brightness-110 transition">اطلب الآن</a>
      </div>
    </div>
  </div>
  {payment_instructions_html(p["name"], p["price"])}
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
          <span class="text-sm font-semibold bg-navy text-white px-4 py-2 rounded-xl">اطلب الآن</span>
        </div>
      </div>
    </a>"""
store_hub_body = hero_simple("المتجر الرقمي", "قوالب وأدلة رقمية حقيقية جاهزة للاستخدام", "منتجات رقمية حقيقية: قوالب CV بصيغة Word، أدلة PDF، ومخطط Excel تفاعلي — تُرسل مباشرة بعد تأكيد الدفع.")
store_hub_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{cards}</div>
  {payment_instructions_html()}
</section>"""
store_hub_body += cta_band("محتاج تصميم مخصص بدل الجاهز؟", "خدماتنا المهنية بتقدملك حل مصمم خصيصًا لك.")
write("store/index.html", page(depth=1, active="store", title="متجر WORKLIXEG الرقمي | قوالب CV وأدلة توظيف حقيقية", description="تصفح متجر WORKLIXEG: قوالب سيرة ذاتية Word، أدلة PDF حقيقية، ومخطط Excel تفاعلي — دفع عبر فودافون كاش أو InstaPay.", keywords="متجر رقمي, قوالب CV, أدلة توظيف, منتجات رقمية للتوظيف, دفع فودافون كاش", canonical=f"{SITE_URL}/store/index.html", h1_breadcrumb="المتجر", breadcrumb_items=[("المتجر", None)], body=store_hub_body, extra_schema='[' + ORG_SCHEMA + ']'))

print("store done:", len(PRODUCTS))
