# -*- coding: utf-8 -*-
from generate import *
from part2 import ORG_SCHEMA, SERVICES
from part3 import PRODUCTS
from part4 import ARTICLES

# ---------------------------------------------------------------------------
# PORTFOLIO
# ---------------------------------------------------------------------------
portfolio_items = [
    ("CV احترافي — قطاع الهندسة", "سيرة ذاتية بالإنجليزي بتنسيق ATS لمهندس اتصالات.", "bg-navy"),
    ("Portfolio تصميم — قطاع الجرافيك", "ملف PDF بصري يعرض مشاريع بهوية بصرية موحدة.", "bg-navy-3"),
    ("تحسين LinkedIn — قطاع المبيعات", "إعادة صياغة كاملة للعنوان والملخص مع كلمات مفتاحية للقطاع.", "bg-navy"),
    ("موقع Portfolio — قطاع البرمجة", "موقع شخصي متجاوب يعرض المشاريع ورابط GitHub مباشر.", "bg-navy-3"),
    ("CV ثنائي اللغة — قطاع المحاسبة", "نسخة عربي وإنجليزي متطابقتين للتقديم في مصر والخليج.", "bg-navy"),
    ("Cover Letter — خريجين جدد", "خطاب تقديم مخصص لبرنامج تدريب في شركة دولية.", "bg-navy-3"),
    ("لاندنج بيدج — قطاع طبي", "صفحة هبوط بحجز مواعيد أونلاين وسيو محلي لاسم المنطقة.", "bg-navy"),
    ("موقع شركة — قطاع صناعي", "موقع تعريفي بصفحات منفصلة لكل خط إنتاج وشهادات الجودة.", "bg-navy-3"),
]
cards = ""
for title, desc, bgcls in portfolio_items:
    cards += f"""<div class="rounded-3xl {bgcls} h-64 p-6 flex flex-col justify-end card-hover">
      <span class="text-white font-bold leading-snug">{title}</span>
      <span class="text-muted text-sm mt-1">{desc}</span>
    </div>"""
portfolio_body = hero_simple("أعمالنا", "أمثلة على أنواع الخدمات اللي بنقدمها", "نماذج توضيحية لأنواع المشاريع والقطاعات اللي نغطيها — مش لقطات فعلية من ملفات عملاء، حفاظًا على خصوصيتهم.")
portfolio_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
</section>"""
portfolio_body += cta_band("عايز نتيجة زي دي؟", "تواصل معنا وابدأ مشروعك المهني معنا.")
write("portfolio.html", page(
    depth=0, active="portfolio",
    title="أعمالنا | أنواع خدمات WORKLIXEG لسير ذاتية وبورتفوليو ومواقع",
    description="نماذج توضيحية لأنواع خدمات WORKLIXEG: سير ذاتية، بورتفوليو، تحسين LinkedIn، مواقع ولاندنج بيدجز لعملاء في مصر ودول الخليج.",
    keywords="أنواع خدمات CV, نماذج سيرة ذاتية, بورتفوليو أعمال, أمثلة سيرة ذاتية, نماذج مواقع",
    canonical=f"{SITE_URL}/portfolio.html",
    h1_breadcrumb="أعمالنا",
    breadcrumb_items=[("أعمالنا", None)],
    body=portfolio_body,
    extra_schema='[' + ORG_SCHEMA + ']',
))

# ---------------------------------------------------------------------------
# REVIEWS -- no fabricated Review/AggregateRating schema (Google policy risk +
# not honest until real client reviews exist). Cards kept as clearly-labeled
# illustrative examples, ready to be swapped for real testimonials later.
# ---------------------------------------------------------------------------
reviews_list = [
    ("قطاع الهندسة", "السيرة الذاتية اتعملت بتنسيق ATS وساعدت في التقديم على وظائف متعددة خلال فترة قصيرة."),
    ("قطاع الموارد البشرية", "الصياغة راعت متطلبات سوق الخليج ومصطلحاته المهنية."),
    ("قطاع البرمجة", "تحسين ملف LinkedIn ركز على الكلمات المفتاحية الخاصة بالمجال."),
    ("خريجين جدد", "جلسة التدريب على المقابلة ساعدت في ترتيب الإجابات والتعامل مع الأسئلة الشائعة."),
    ("قطاع المشاريع الإنشائية", "خطاب التقديم كان مخصصًا لمتطلبات الوظيفة والشركة المستهدفة."),
    ("قطاع المحاسبة", "التسليم تم في الموعد المتفق عليه مع جولة تعديلات سريعة."),
]
review_cards = ""
for role, text in reviews_list:
    review_cards += f"""<div class="bg-white rounded-3xl p-7 border border-gray-100 card-hover">
      <p class="text-gray-600 leading-relaxed mb-6">"{text}"</p>
      <div class="text-gray-400 text-sm font-semibold">{role}</div>
    </div>"""
reviews_body = hero_simple("آراء العملاء", "أمثلة على نوعية النتائج اللي بنستهدفها", "النماذج دي أمثلة توضيحية على نوعية الخدمة، في انتظار إضافة تقييمات حقيقية موثقة من عملائنا.")
reviews_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{review_cards}</div>
</section>"""
reviews_body += cta_band("عايز تكون قصة النجاح الجاية؟", "ابدأ معانا النهاردة.")
write("reviews.html", page(
    depth=0, active="reviews",
    title="آراء العملاء | نماذج نتائج خدمات WORKLIXEG",
    description="أمثلة توضيحية على نوعية النتائج اللي تقدمها WORKLIXEG في خدمات كتابة السيرة الذاتية وLinkedIn والتدريب على المقابلات في مصر ودول الخليج.",
    keywords="تقييمات WORKLIXEG, آراء العملاء, نتائج خدمة كتابة سيرة ذاتية",
    canonical=f"{SITE_URL}/reviews.html",
    h1_breadcrumb="آراء العملاء",
    breadcrumb_items=[("آراء العملاء", None)],
    body=reviews_body,
    extra_schema='[' + ORG_SCHEMA + ']',
))

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about_body = hero_simple("من نحن", "منصة مصرية لخدمات التطوير المهني وتصميم المواقع", "WORKLIXEG منصة متخصصة في مساعدة الباحثين عن عمل وأصحاب الأعمال في مصر ودول الخليج على تقديم أنفسهم ومشاريعهم بأفضل شكل ممكن.")
about_body += f"""<section class="max-w-4xl mx-auto px-5 md:px-8 py-16 space-y-10">
  <div>
    <h2 class="font-extrabold text-xl mb-3">رسالتنا</h2>
    <p class="text-gray-600 leading-relaxed">نساعد كل باحث عن عمل يوصل صوته المهني بوضوح للشركات، وكل صاحب عمل يبني حضور رقمي يبيع فعليًا، عن طريق أدوات وخدمات مصممة تحديدًا لسوق مصر ودول الخليج.</p>
  </div>
  <div>
    <h2 class="font-extrabold text-xl mb-3">ليه WORKLIXEG</h2>
    <p class="text-gray-600 leading-relaxed">فريقنا بيجمع بين خبرة كتابة المحتوى المهني، تصميم المواقع، ومعرفة عملية بمتطلبات أنظمة الفرز الآلي (ATS) وسوق العمل والأعمال في مصر والخليج.</p>
  </div>
</section>"""
about_body += cta_band("عايز تتعرف على خدماتنا أكتر؟", "استعرض خدماتنا أو تواصل معنا مباشرة.")
write("about.html", page(
    depth=0, active="about",
    title="من نحن | WORKLIXEG لخدمات التطوير المهني وتصميم المواقع",
    description="تعرف على WORKLIXEG، منصة خدمات التطوير المهني وتصميم المواقع المتخصصة في مصر ودول الخليج.",
    keywords="من نحن WORKLIXEG, عن الشركة, خدمات توظيف مصر والخليج, تصميم مواقع مصر",
    canonical=f"{SITE_URL}/about.html",
    h1_breadcrumb="من نحن",
    breadcrumb_items=[("من نحن", None)],
    body=about_body,
    extra_schema='[' + ORG_SCHEMA + ']',
))

# ---------------------------------------------------------------------------
# CONTACT -- form now actually works: JS reads the fields and builds a real
# WhatsApp message (see assets/main.js), instead of a static dead link.
# ---------------------------------------------------------------------------
contact_body = hero_simple("اتصل بنا", "تواصل معنا بالطريقة الأسهل ليك", "فريقنا جاهز يرد على استفساراتك ويساعدك تختار الخدمة المناسبة لهدفك المهني أو مشروعك.")
contact_body += f"""<section class="max-w-4xl mx-auto px-5 md:px-8 py-16 grid md:grid-cols-2 gap-8">
  <div class="bg-white rounded-3xl p-8 border border-gray-100">
    <h2 class="font-bold text-lg mb-4">تواصل مباشر</h2>
    <ul class="space-y-3 text-gray-600">
      <li class="flex items-center gap-3"><span class="w-9 h-9 rounded-full bg-orange/10 flex items-center justify-center text-orange">✆</span><span class="font-latin" dir="ltr">+20 112 610 4846</span></li>
      <li class="flex items-center gap-3"><span class="w-9 h-9 rounded-full bg-orange/10 flex items-center justify-center text-orange">✉</span><span class="font-latin" dir="ltr">info@worklixeg.com</span></li>
      <li class="flex items-center gap-3"><span class="w-9 h-9 rounded-full bg-orange/10 flex items-center justify-center text-orange">⏰</span><span>السبت – الخميس، 10ص – 10م</span></li>
    </ul>
    <a href="{WA_GENERIC}" class="inline-block mt-6 bg-orange text-white font-bold px-7 py-3 rounded-2xl hover:brightness-110 transition">راسلنا على واتساب</a>
  </div>
  <div class="bg-white rounded-3xl p-8 border border-gray-100">
    <h2 class="font-bold text-lg mb-4">نموذج تواصل سريع</h2>
    <p class="text-gray-400 text-xs mb-4">هيتم فتح واتساب برسالة جاهزة ببياناتك عند الإرسال.</p>
    <form class="space-y-4" onsubmit="return false;">
      <input id="contact-name" type="text" placeholder="الاسم" class="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm" />
      <input id="contact-phone" type="text" placeholder="رقم الموبايل" class="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm font-latin" dir="ltr" />
      <textarea id="contact-message" placeholder="رسالتك" rows="4" class="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm"></textarea>
      <button id="contact-submit-btn" type="button" class="block w-full text-center bg-navy text-white font-bold px-7 py-3 rounded-2xl hover:brightness-110 transition">إرسال عبر واتساب</button>
    </form>
  </div>
</section>"""
write("contact.html", page(
    depth=0, active="contact",
    title="اتصل بنا | WORKLIXEG",
    description="تواصل مع فريق WORKLIXEG عبر واتساب أو البريد الإلكتروني لطلب خدمات كتابة السيرة الذاتية، LinkedIn، أو تصميم المواقع.",
    keywords="اتصل بنا WORKLIXEG, رقم WORKLIXEG, تواصل خدمة كتابة سيرة ذاتية",
    canonical=f"{SITE_URL}/contact.html",
    h1_breadcrumb="اتصل بنا",
    breadcrumb_items=[("اتصل بنا", None)],
    body=contact_body,
    extra_schema='[' + ORG_SCHEMA + ']',
))

print("standalone pages done")
