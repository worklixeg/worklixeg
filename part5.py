# -*- coding: utf-8 -*-
from generate import *
from part2 import ORG_SCHEMA, SERVICES
from part3 import PRODUCTS
from part4 import ARTICLES

portfolio_items = [
    ("CV احترافي — مهندس اتصالات", "سيرة ذاتية بالإنجليزي بتنسيق ATS، أدت لـ3 مقابلات خلال أسبوعين.", "bg-navy"),
    ("Portfolio تصميم — مصمم جرافيك", "ملف PDF بصري يعرض 12 مشروع بهوية بصرية موحدة.", "bg-navy-3"),
    ("تحسين LinkedIn — مدير مبيعات", "إعادة صياغة كاملة للعنوان والملخص مع كلمات مفتاحية للقطاع.", "bg-navy"),
    ("موقع Portfolio — مطور برمجيات", "موقع شخصي متجاوب يعرض المشاريع ورابط GitHub مباشر.", "bg-navy-3"),
    ("CV ثنائي اللغة — محاسب", "نسخة عربي وإنجليزي متطابقتين للتقديم في مصر والخليج.", "bg-navy"),
    ("Cover Letter — خريجة حديثة", "خطاب تقديم مخصص لبرنامج تدريب في شركة دولية.", "bg-navy-3"),
    ("لاندنج بيدج — عيادة أسنان", "صفحة هبوط بحجز مواعيد أونلاين وسيو محلي لاسم المنطقة.", "bg-navy"),
    ("موقع شركة — مصنع أغذية", "موقع تعريفي بصفحات منفصلة لكل خط إنتاج وشهادات الجودة.", "bg-navy-3"),
]
cards = ""
for title, desc, bgcls in portfolio_items:
    cards += f"""<div class="rounded-3xl {bgcls} h-64 p-6 flex flex-col justify-end card-hover">
      <span class="text-white font-bold leading-snug">{title}</span>
      <span class="text-muted text-sm mt-1">{desc}</span>
    </div>"""
portfolio_body = hero_simple("أعمالنا", "نماذج من مشاريع حقيقية سلمناها", "أمثلة من خدمات حقيقية قدمناها لعملاء في مصر ودول الخليج، عبر مختلف المجالات والمستويات الوظيفية.")
portfolio_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
</section>"""
portfolio_body += cta_band("عايز نتيجة زي دي؟", "تواصل معنا وابدأ مشروعك المهني معنا.")
write("portfolio.html", page(
    depth=0, active="portfolio",
    title="أعمالنا | نماذج سير ذاتية وبورتفوليو ومواقع من WORKLIXEG",
    description="تصفح نماذج حقيقية من أعمال WORKLIXEG: سير ذاتية، بورتفوليو، تحسين LinkedIn، مواقع ولاندنج بيدجز لعملاء في مصر ودول الخليج.",
    keywords="نماذج CV, نماذج سيرة ذاتية, بورتفوليو أعمال, أمثلة سيرة ذاتية ناجحة, نماذج مواقع",
    canonical=f"{SITE_URL}/portfolio.html",
    h1_breadcrumb="أعمالنا",
    breadcrumb_items=[("أعمالنا", None)],
    body=portfolio_body,
    extra_schema='[' + ORG_SCHEMA + ']',
))

reviews_list = [
    ("أحمد س.", "مهندس مدني", "السيرة الذاتية اللي عملولي إياها غيّرت شكل تعاملي مع الشركات، حصلت على 3 مقابلات في أسبوعين."),
    ("هبة ع.", "أخصائية موارد بشرية", "خدمة محترفة فعلًا، الفريق فهم مجالي وطلع سيرة ذاتية مناسبة تمامًا لسوق الخليج."),
    ("محمد ن.", "مطور واجهات أمامية", "ملفي على LinkedIn بقى أقوى بكتير، وبدأت أوصلني رسائل من شركات مش كنت متخيل أوصلها."),
    ("سارة ط.", "خريجة حديثة", "التدريب على المقابلة ساعدني أرتب أفكاري وأجاوب بثقة أكتر بكتير من أول مرة."),
    ("علي ن.", "مدير مشاريع إنشائية", "خطاب التقديم للخليج كان محترف ومخصص فعلًا، حسيت إنه مكتوب لي شخصيًا."),
    ("رودينا ي.", "محاسبة", "سرعة التسليم كانت ممتازة والتعديلات اتعملت بسرعة من غير أي تعقيد."),
]
review_cards = ""
for name, role, text in reviews_list:
    review_cards += f"""<div class="bg-white rounded-3xl p-7 border border-gray-100 card-hover">
      <div class="text-orange mb-4">★★★★★</div>
      <p class="text-gray-600 leading-relaxed mb-6">"{text}"</p>
      <div class="font-bold">{name}</div>
      <div class="text-gray-400 text-sm">{role}</div>
    </div>"""
reviews_body = hero_simple("آراء العملاء", "قصص نجاح حقيقية من عملائنا", "آراء موثقة من عملاء استخدموا خدمات WORKLIXEG في كتابة السيرة الذاتية وتحسين LinkedIn والتدريب على المقابلات.")
reviews_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{review_cards}</div>
</section>"""
reviews_body += cta_band("عايز تكون قصة النجاح الجاية؟", "ابدأ معانا النهاردة.")
review_schema_items = []
for name, role, text in reviews_list:
    review_schema_items.append('{"@type":"Review","author":{"@type":"Person","name":"%s"},"reviewBody":"%s","reviewRating":{"@type":"Rating","ratingValue":"5"}}' % (name, text))
reviews_schema = '[' + ORG_SCHEMA + ',{"@context":"https://schema.org","@type":"ItemList","itemListElement":[' + ",".join(
    '{"@type":"ListItem","position":%d,"item":%s}' % (i+1, r) for i, r in enumerate(review_schema_items)
) + ']}]'
write("reviews.html", page(
    depth=0, active="reviews",
    title="آراء العملاء | تقييمات خدمات WORKLIXEG",
    description="اقرأ تقييمات حقيقية من عملاء WORKLIXEG استخدموا خدمات كتابة السيرة الذاتية وLinkedIn والتدريب على المقابلات في مصر ودول الخليج.",
    keywords="تقييمات WORKLIXEG, آراء العملاء, تقييم خدمة كتابة سيرة ذاتية",
    canonical=f"{SITE_URL}/reviews.html",
    h1_breadcrumb="آراء العملاء",
    breadcrumb_items=[("آراء العملاء", None)],
    body=reviews_body,
    extra_schema=reviews_schema,
))

about_body = hero_simple("من نحن", "منصة مصرية لخدمات التطوير المهني وتصميم المواقع", "WORKLIXEG منصة متخصصة في مساعدة الباحثين عن عمل وأصحاب الأعمال في مصر ودول الخليج على تقديم أنفسهم ومشاريعهم بأفضل شكل ممكن.")
about_body += f"""<section class="max-w-4xl mx-auto px-5 md:px-8 py-16 space-y-10">
  <div>
    <h2 class="font-extrabold text-xl mb-3">رسالتنا</h2>
    <p class="text-gray-600 leading-relaxed">نساعد كل باحث عن عمل يوصل صوته المهني بوضوح للشركات، وكل صاحب عمل يبني حضور رقمي يبيع فعليًا، عن طريق أدوات وخدمات مصممة تحديدًا لسوق مصر ودول الخليج، بعيدًا عن القوالب العامة اللي بتتكرر في كل مكان.</p>
  </div>
  <div class="grid sm:grid-cols-3 gap-6 text-center">
    <div class="bg-white rounded-2xl p-6 border border-gray-100">
      <div class="font-latin font-extrabold text-3xl text-navy">5000+</div>
      <div class="text-gray-500 text-sm mt-1">مشروع منجز</div>
    </div>
    <div class="bg-white rounded-2xl p-6 border border-gray-100">
      <div class="font-latin font-extrabold text-3xl text-navy">98%</div>
      <div class="text-gray-500 text-sm mt-1">رضا العملاء</div>
    </div>
    <div class="bg-white rounded-2xl p-6 border border-gray-100">
      <div class="font-latin font-extrabold text-3xl text-navy">24س</div>
      <div class="text-gray-500 text-sm mt-1">متوسط التسليم</div>
    </div>
  </div>
  <div>
    <h2 class="font-extrabold text-xl mb-3">ليه WORKLIXEG</h2>
    <p class="text-gray-600 leading-relaxed">فريقنا بيجمع بين خبرة كتابة المحتوى المهني، تصميم المواقع، ومعرفة عملية بمتطلبات أنظمة الفرز الآلي (ATS) وسوق العمل والأعمال في مصر والخليج، عشان كل خدمة بنقدمها تكون مبنية على أساس عملي مش تخمين.</p>
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
    <form class="space-y-4">
      <input type="text" placeholder="الاسم" class="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm" />
      <input type="text" placeholder="رقم الموبايل" class="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm font-latin" dir="ltr" />
      <textarea placeholder="رسالتك" rows="4" class="w-full border border-gray-200 rounded-xl px-4 py-3 text-sm"></textarea>
      <a href="{WA_GENERIC}" class="block text-center bg-navy text-white font-bold px-7 py-3 rounded-2xl hover:brightness-110 transition">إرسال عبر واتساب</a>
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
