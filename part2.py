# -*- coding: utf-8 -*-
from generate import *

ORG_SCHEMA = '{"@context":"https://schema.org","@type":"ProfessionalService","name":"WORKLIXEG","description":"منصة خدمات مهنية لكتابة السيرة الذاتية المتوافقة مع ATS وتحسين LinkedIn وتصميم بورتفوليو لمصر ودول الخليج.","areaServed":["EG","SA","AE","QA","KW","BH","OM"],"telephone":"+201126104846","url":"%s"}' % SITE_URL

SERVICES = [
    {
        "slug": "cv-ats-writing",
        "name": "كتابة CV احترافي متوافق مع ATS",
        "short": "سيرة ذاتية مصاغة باحترافية تجتاز أنظمة الفرز الآلي وتصل لعين مسؤول التوظيف.",
        "audience": "خريجين، موظفين يبحثون عن ترقية أو تغيير مجال، ومتقدمين لشركات كبرى تستخدم أنظمة فرز آلي.",
        "deliver": "ملف CV بصيغتي Word وPDF، بالعربي أو الإنجليزي، مبني على كلمات مفتاحية لمجالك، مع تصميم نظيف يقرأه البشر والأنظمة معًا.",
        "price": "يبدأ من 300 ج.م",
        "duration": "24 ساعة (يوجد تسليم عاجل خلال 12 ساعة)",
        "examples": "مهندسين، محاسبين، مطوري برمجيات، موظفي مبيعات وتسويق، وكوادر طبية.",
        "keywords": "كتابة سيرة ذاتية, CV احترافي, سيرة ذاتية ATS, عمل CV مصر, كتابة CV السعودية, ATS resume Egypt",
        "faqs": [
            ("إيه معنى إن السيرة الذاتية متوافقة مع ATS؟", "يعني إن تنسيقها وكلماتها المفتاحية مصممة عشان تتقرأ صح من برامج فرز السير الذاتية اللي تستخدمها الشركات الكبرى قبل ما توصل لمسؤول التوظيف."),
            ("هل ينفع تبعتلي بس بيانات ووظيفة مستهدفة وتكتبولي الباقي؟", "أيوه، بترسل بياناتك وخبراتك والوظيفة المستهدفة، وفريقنا يصيغ السيرة كاملة بأسلوب احترافي."),
        ],
    },
    {
        "slug": "cover-letter-writing",
        "name": "كتابة Cover Letter احترافي",
        "short": "خطاب تقديم مخصص لكل وظيفة يوضح ليه أنت الاختيار الصح.",
        "audience": "متقدمين لوظائف تطلب خطاب تقديم، وخصوصًا التقديم على شركات أجنبية أو دول الخليج.",
        "deliver": "خطاب تقديم مخصص بالعربي أو الإنجليزي، مبني على إعلان الوظيفة وخبراتك، بصيغة Word وPDF.",
        "price": "يبدأ من 150 ج.م",
        "duration": "24 ساعة",
        "examples": "متقدمين لوظائف في شركات دولية، برامج تدريب، ومنح دراسية مرتبطة بالعمل.",
        "keywords": "كتابة كوفر ليتر, Cover Letter عربي, خطاب تقديم وظيفة, Cover Letter مصر, خطاب تقديم الخليج",
        "faqs": [
            ("هل ينفع Cover Letter واحد لكل الوظائف؟", "الأفضل إن كل خطاب يتخصص للوظيفة والشركة، وده بالظبط اللي بنعمله، مش نسخة عامة بتتكرر."),
            ("هل تقدر تكتبه بالإنجليزي للتقديم على شركات أجنبية؟", "أيوه، نكتبه بالعربي أو الإنجليزي حسب متطلبات الوظيفة."),
        ],
    },
    {
        "slug": "linkedin-profile-optimization",
        "name": "تحسين ملف LinkedIn",
        "short": "ملف شخصي احترافي يظهر في نتائج بحث مسؤولي التوظيف ويعكس خبراتك الحقيقية.",
        "audience": "أي شخص يبحث عن فرصة عمل أو يريد بناء حضور مهني قوي على LinkedIn.",
        "deliver": "إعادة صياغة العنوان (Headline) والملخص (About) والخبرات، مع اختيار كلمات مفتاحية تزيد ظهورك في البحث.",
        "price": "يبدأ من 250 ج.م",
        "duration": "24-48 ساعة",
        "examples": "باحثين عن عمل، فريلانسرز، ومديرين يريدون بناء علامة شخصية مهنية.",
        "keywords": "تحسين لينكدإن, LinkedIn Optimization Egypt, عمل بروفايل لينكدإن احترافي, LinkedIn عربي",
        "faqs": [
            ("هل تعملوا الصور والتصميم كمان ولا الكتابة بس؟", "التركيز الأساسي على المحتوى: العنوان، الملخص، والخبرات، وممكن نقترح تحسينات للصورة والغلاف كمان."),
            ("هل ده هيزود ظهوري في البحث فعلًا؟", "استخدام كلمات مفتاحية دقيقة في العنوان والملخص بيزود احتمالية ظهور بروفايلك لما مسؤولي التوظيف يدوروا في مجالك."),
        ],
    },
    {
        "slug": "portfolio-pdf-design",
        "name": "تصميم Portfolio PDF",
        "short": "ملف عرض أعمال بصري يبرز مشاريعك بشكل احترافي وسهل المشاركة.",
        "audience": "مصممين، مهندسين معماريين، مسوقين، ومبدعين محتاجين يعرضوا شغلهم بصريًا.",
        "deliver": "ملف PDF مصمم بهوية بصرية موحدة، يعرض مشاريعك وأدواتك ونبذة عنك، جاهز للإرسال أو المشاركة أونلاين.",
        "price": "يبدأ من 400 ج.م",
        "duration": "2-3 أيام",
        "examples": "مصممين جرافيك، مهندسين معماريين وديكور، مصورين، وصناع محتوى.",
        "keywords": "تصميم بورتفوليو PDF, عمل Portfolio احترافي, بورتفوليو مصمم جرافيك, Portfolio مصر",
        "faqs": [
            ("محتاج كام مشروع عشان أعمل بورتفوليو؟", "بنقدر نصمم بورتفوليو مبدئي حتى بـ3-4 مشاريع قوية، والأهم جودة العرض مش العدد."),
            ("هل ينفع أستخدمه أونلاين مش بس PDF؟", "أيوه، الملف بيتصمم بشكل يسهل رفعه أونلاين أو إرساله مباشرة لأي جهة."),
        ],
    },
    {
        "slug": "portfolio-website-design",
        "name": "تصميم موقع Portfolio شخصي",
        "short": "موقع تعريفي احترافي دائم يعرض أعمالك ومهاراتك ويعزز حضورك أونلاين.",
        "audience": "مطورين، مصممين، فريلانسرز، ومحترفين يريدون حضور رقمي دائم بدل ملف واحد.",
        "deliver": "موقع شخصي متجاوب يعرض نبذة عنك، مهاراتك، مشاريعك، وطريقة التواصل، مع تحسين أساسي لمحركات البحث.",
        "price": "يبدأ من 1200 ج.م",
        "duration": "4-7 أيام",
        "examples": "مطوري برمجيات، مصممي UI/UX، كتاب محتوى، ومستشارين مستقلين.",
        "keywords": "تصميم موقع بورتفوليو, Portfolio Website, موقع شخصي احترافي, عمل موقع portfolio مصر",
        "faqs": [
            ("هل الموقع بيفضل ملكي وأقدر أعدله بعدين؟", "أيوه، الموقع بيكون ملكك بالكامل مع إمكانية التعديل أو الاستضافة على دومين خاص بيك."),
            ("هل يشمل السعر الاستضافة والدومين؟", "السعر المبدئي للتصميم والبناء، والاستضافة والدومين بيتحددوا حسب احتياجك ونناقشهم معاك قبل البدء."),
        ],
    },
    {
        "slug": "interview-preparation-coaching",
        "name": "تدريب على المقابلات الشخصية",
        "short": "جلسة محاكاة حقيقية لمقابلة العمل مع ملاحظات عملية تزود ثقتك.",
        "audience": "أي شخص عنده مقابلة قريبة ومحتاج يتمرن على الأسئلة الشائعة وأسلوب الإجابة.",
        "deliver": "جلسة تدريب أونلاين تحاكي مقابلة حقيقية، مع تغذية راجعة مفصلة على الإجابات ولغة الجسد وطريقة العرض.",
        "price": "يبدأ من 350 ج.م",
        "duration": "جلسة تُحجز بموعد مسبق",
        "examples": "خريجين جدد قبل أول مقابلة، ومحترفين مستعدين لمقابلات ترقية أو تغيير مجال.",
        "keywords": "تدريب مقابلة شخصية, تحضير لمقابلة العمل, أسئلة انترفيو, تدريب انترفيو مصر",
        "faqs": [
            ("الجلسة بتكون أونلاين ولا حضوري؟", "الجلسات أونلاين عن طريق مكالمة فيديو، عشان تقدر تحجز من أي مكان في مصر أو الخليج."),
            ("هل التدريب بيكون على أسئلة عامة ولا خاصة بمجالي؟", "بنجهز الأسئلة حسب مجالك والوظيفة المتقدم لها بالتحديد، مش أسئلة عامة بس."),
        ],
    },
    {
        "slug": "career-consultation",
        "name": "استشارة مهنية",
        "short": "جلسة توجيه لتحديد مسارك المهني القادم بوضوح.",
        "audience": "من يشعر بالتوهان في اختيار المسار المهني، أو يفكر في تغيير مجال العمل.",
        "deliver": "جلسة نقاش تحلل خبراتك وأهدافك، وتخرج بخطوات عملية للمسار القادم، مع توصيات لتطوير مهاراتك.",
        "price": "يبدأ من 300 ج.م",
        "duration": "جلسة تُحجز بموعد مسبق",
        "examples": "خريجين حديثين، موظفين يفكرون في تغيير المجال، وعائدين لسوق العمل بعد انقطاع.",
        "keywords": "استشارة مهنية, career coaching Egypt, توجيه مهني, تطوير مسار وظيفي",
        "faqs": [
            ("هل الاستشارة مناسبة لو لسه مش عارف مجالي؟", "أيوه، دي بالظبط الحالة اللي الجلسة بتساعد فيها؛ بنحلل معاك خبراتك واهتماماتك عشان نوصل لمسار واضح."),
            ("هل في متابعة بعد الجلسة؟", "بنقدملك خطوات عملية مكتوبة بعد الجلسة تقدر تتابع بيها بنفسك."),
        ],
    },
    {
        "slug": "cv-translation",
        "name": "ترجمة السيرة الذاتية",
        "short": "ترجمة احترافية دقيقة للسيرة الذاتية بمصطلحات كل مجال.",
        "audience": "متقدمين لوظائف تتطلب سيرة ذاتية بلغة غير لغتهم الأصلية، خصوصًا للتقديم في الخليج أو شركات أجنبية.",
        "deliver": "ترجمة كاملة للسيرة الذاتية من العربي للإنجليزي أو العكس، مع مراعاة المصطلحات التقنية لكل مجال.",
        "price": "يبدأ من 200 ج.م",
        "duration": "24 ساعة",
        "examples": "مهندسين، أطباء، محاسبين، ومتخصصين في مجالات تقنية.",
        "keywords": "ترجمة سيرة ذاتية, ترجمة CV انجليزي عربي, ترجمة سيرة ذاتية احترافية",
        "faqs": [
            ("هل الترجمة بتكون حرفية ولا بتراعي أسلوب السيرة الذاتية؟", "بنراعي أسلوب كتابة السيرة الذاتية في اللغة المستهدفة، مش ترجمة حرفية جامدة."),
            ("هل تقدروا تراجعوا سيرة مترجمة قبل كده؟", "أيوه، نقدر نراجع وننقح أي سيرة ذاتية مترجمة مسبقًا."),
        ],
    },
    {
        "slug": "website-landing-page-design",
        "name": "تصميم مواقع وصفحات هبوط (Landing Pages)",
        "short": "مواقع وصفحات هبوط احترافية بعنوان قوي وسيو كامل تحول الزائر إلى عميل، لمصر ودول الخليج.",
        "audience": "أصحاب الأعمال، الشركات الناشئة، المتاجر الإلكترونية، ومقدمي الخدمات المحتاجين حضور رقمي يبيع فعليًا.",
        "deliver": "موقع أو صفحة هبوط مصممة باحتراف بعنوان رئيسي قوي، هيكلة صفحات واضحة، تحسين متكامل لمحركات البحث (Schema، Sitemap، Robots، عناوين وأوصاف مختلفة لكل صفحة)، وربط بوسائل التواصل والطلب.",
        "price": "يبدأ من 1500 ج.م",
        "duration": "3-7 أيام حسب حجم الموقع",
        "examples": "عيادات ومراكز طبية، مطاعم وكافيهات، مكاتب عقارية، شركات ومصانع، ومقدمي خدمات مستقلين.",
        "keywords": "تصميم مواقع, تصميم لاندنج بيدج, عمل موقع الكتروني مصر, لاندنج بيدج السعودية, تصميم موقع شركة الخليج, سيو مواقع",
        "faqs": [
            ("هل الموقع بيتصمم بعنوان وسيو مخصص لكل صفحة؟", "أيوه، كل صفحة بناخدها بعنوان (Title) ووصف (Meta Description) وكلمات مفتاحية مختلفة، مع هيكلة داخلية للروابط تخدم ظهورك في جوجل."),
            ("هل تقدروا تستهدفوا سوق الخليج تحديدًا؟", "أيوه، بنراعي الكلمات المفتاحية ولغة المحتوى المناسبة لسوق مصر أو أي دولة خليجية تستهدفها تحديدًا."),
            ("هل الموقع بيشمل صفحات هبوط منفصلة لكل خدمة أو منتج؟", "أيوه، بنصمم صفحات تابعة منفصلة لكل خدمة أو قطاع تستهدفه، بعنوان وسيو خاص بكل صفحة، وده اللي بيزود فرص الظهور في نتائج البحث."),
        ],
    },
]

def wa_service_link(service_name):
    return wa_link(f"مرحبًا، أنا عايز أطلب خدمة: {service_name}")

def service_body(s, depth):
    order_href = wa_service_link(s["name"])
    faqs_html = faq_block(s["faqs"])
    other_services = [x for x in SERVICES if x["slug"] != s["slug"]][:3]
    related_links = [(o["name"], f"{o['slug']}.html", o["short"]) for o in other_services]
    related = internal_links_grid("خدمات تانية ممكن تهمك", related_links)
    body = hero_simple("خدمة WORKLIXEG", s["name"], s["short"], cta_href=order_href)
    body += f"""<section class="max-w-5xl mx-auto px-5 md:px-8 py-16 grid md:grid-cols-2 gap-10">
  <div>
    <h2 class="font-extrabold text-xl mb-3">لمن تناسب هذه الخدمة</h2>
    <p class="text-gray-600 leading-relaxed">{s['audience']}</p>
  </div>
  <div>
    <h2 class="font-extrabold text-xl mb-3">ماذا ستحصل عليه</h2>
    <p class="text-gray-600 leading-relaxed">{s['deliver']}</p>
  </div>
  <div>
    <h2 class="font-extrabold text-xl mb-3">السعر</h2>
    <p class="text-gray-600 leading-relaxed font-latin" dir="rtl">{s['price']}</p>
  </div>
  <div>
    <h2 class="font-extrabold text-xl mb-3">مدة التنفيذ</h2>
    <p class="text-gray-600 leading-relaxed">{s['duration']}</p>
  </div>
  <div class="md:col-span-2">
    <h2 class="font-extrabold text-xl mb-3">أمثلة على من طلب هذه الخدمة</h2>
    <p class="text-gray-600 leading-relaxed">{s['examples']}</p>
  </div>
  <div class="md:col-span-2 text-center pt-4">
    <a href="{order_href}" class="inline-block bg-navy text-white font-bold px-9 py-4 rounded-2xl hover:brightness-110 transition">اطلب هذه الخدمة الآن عبر واتساب</a>
  </div>
</section>"""
    body += faqs_html
    body += related
    body += cta_band("جاهز تبدأ؟", "تواصل معنا واحصل على " + s["name"] + " المناسب لك.", cta_href=order_href)
    return body

for s in SERVICES:
    canonical = f"{SITE_URL}/services/{s['slug']}.html"
    schema = ('[' + ORG_SCHEMA + ',' +
        '{"@context":"https://schema.org","@type":"Service","name":"%s","description":"%s","areaServed":["EG","SA","AE","QA","KW","BH"],"provider":{"@type":"ProfessionalService","name":"WORKLIXEG"}},' % (s["name"], s["short"]) +
        faq_schema(s["faqs"]) + ']')
    body = service_body(s, 1)
    html = page(
        depth=1, active="services",
        title=f"{s['name']} | WORKLIXEG",
        description=s["short"] + " تسليم سريع لمصر ودول الخليج.",
        keywords=s["keywords"],
        canonical=canonical,
        h1_breadcrumb=s["name"],
        breadcrumb_items=[("الخدمات", "index.html"), (s["name"], None)],
        body=body,
        extra_schema=schema,
    )
    write(f"services/{s['slug']}.html", html)

LANDING_NICHES = [
    {
        "slug": "real-estate-landing-page-design",
        "title": "تصميم لاندنج بيدج للمكاتب العقارية",
        "desc": "صفحة هبوط مخصصة للمكاتب العقارية تعرض المشاريع والوحدات وتحول الزائر لعميل جاد عبر نموذج تواصل مباشر.",
        "keywords": "لاندنج بيدج عقارات, تصميم موقع مكتب عقاري, صفحة هبوط مشروع عقاري مصر والخليج",
        "body_extra": "الصفحة بتتضمن عرض للمشروع أو الوحدات، صور ومخططات، مقارنة الأسعار، ونموذج حجز معاينة، مع سيو يستهدف اسم المنطقة والمشروع.",
    },
    {
        "slug": "restaurant-cafe-landing-page-design",
        "title": "تصميم لاندنج بيدج للمطاعم والكافيهات",
        "desc": "صفحة هبوط تعرض المنيو وصور الأطباق وتتيح الحجز أو الطلب المباشر عبر واتساب.",
        "keywords": "لاندنج بيدج مطاعم, تصميم موقع مطعم مصر, صفحة هبوط كافيه الخليج",
        "body_extra": "الصفحة بتتضمن عرض المنيو بالصور، موقع الفرع على الخريطة، تقييمات العملاء، وزر طلب أو حجز طاولة مباشر.",
    },
    {
        "slug": "clinic-medical-center-landing-page-design",
        "title": "تصميم موقع للعيادات والمراكز الطبية",
        "desc": "موقع احترافي للعيادات يعرض التخصصات والأطباء ويتيح حجز الكشف أونلاين.",
        "keywords": "تصميم موقع عيادة, لاندنج بيدج مركز طبي مصر, موقع عيادة أسنان الخليج",
        "body_extra": "الموقع بيتضمن صفحات منفصلة لكل تخصص أو طبيب، نظام حجز مواعيد مبسط، وأسئلة شائعة تخص كل خدمة طبية.",
    },
    {
        "slug": "corporate-business-website-design",
        "title": "تصميم مواقع الشركات والمصانع",
        "desc": "موقع تعريفي احترافي للشركات والمصانع يعرض الخدمات والمنتجات ويعزز الثقة أمام العملاء والموردين.",
        "keywords": "تصميم موقع شركة, موقع مصنع مصر, تصميم موقع شركات الخليج",
        "body_extra": "الموقع بيتضمن صفحة عن الشركة، صفحات منفصلة للخدمات أو خطوط الإنتاج، شهادات وعملاء سابقين، ونموذج طلب عرض سعر.",
    },
]

def landing_niche_body(item, depth):
    order_href = wa_service_link(item["title"])
    others = [x for x in LANDING_NICHES if x["slug"] != item["slug"]]
    related_links = [(o["title"], f"{o['slug']}.html", o["desc"]) for o in others]
    body = hero_simple("تصميم مواقع WORKLIXEG", item["title"], item["desc"], cta_href=order_href)
    body += f"""<section class="max-w-3xl mx-auto px-5 md:px-8 py-16">
  <p class="text-gray-600 leading-relaxed text-lg">{item['body_extra']}</p>
  <div class="text-center pt-10">
    <a href="{order_href}" class="inline-block bg-navy text-white font-bold px-9 py-4 rounded-2xl hover:brightness-110 transition">اطلب هذا التصميم الآن عبر واتساب</a>
  </div>
</section>"""
    body += internal_links_grid("أنواع تانية من صفحات الهبوط", related_links)
    body += cta_band("عندك فكرة مختلفة؟", "احنا نصمملك موقع أو لاندنج بيدج يناسب مجالك بالظبط.", cta_href=order_href)
    return body

for item in LANDING_NICHES:
    canonical = f"{SITE_URL}/services/{item['slug']}.html"
    schema = ('[' + ORG_SCHEMA + ',' +
        '{"@context":"https://schema.org","@type":"Service","name":"%s","description":"%s","areaServed":["EG","SA","AE","QA","KW","BH"],"provider":{"@type":"ProfessionalService","name":"WORKLIXEG"}}' % (item["title"], item["desc"]) + ']')
    body = landing_niche_body(item, 1)
    html = page(
        depth=1, active="services",
        title=f"{item['title']} | WORKLIXEG",
        description=item["desc"],
        keywords=item["keywords"],
        canonical=canonical,
        h1_breadcrumb=item["title"],
        breadcrumb_items=[("الخدمات", "index.html"), ("تصميم مواقع ولاندنج بيدجز", "website-landing-page-design.html"), (item["title"], None)],
        body=body,
        extra_schema=schema,
    )
    write(f"services/{item['slug']}.html", html)

web_design_service = next(s for s in SERVICES if s["slug"] == "website-landing-page-design")
niche_links = [(n["title"], f"{n['slug']}.html", n["desc"]) for n in LANDING_NICHES]
wd_body = service_body(web_design_service, 1)
wd_body += internal_links_grid("صفحات هبوط ومواقع حسب مجالك", niche_links)
wd_canonical = f"{SITE_URL}/services/website-landing-page-design.html"
wd_schema = ('[' + ORG_SCHEMA + ',' +
    '{"@context":"https://schema.org","@type":"Service","name":"%s","description":"%s","areaServed":["EG","SA","AE","QA","KW","BH"],"provider":{"@type":"ProfessionalService","name":"WORKLIXEG"}},' % (web_design_service["name"], web_design_service["short"]) +
    faq_schema(web_design_service["faqs"]) + ']')
write("services/website-landing-page-design.html", page(
    depth=1, active="services",
    title=f"{web_design_service['name']} | WORKLIXEG",
    description=web_design_service["short"] + " تسليم سريع لمصر ودول الخليج.",
    keywords=web_design_service["keywords"],
    canonical=wd_canonical,
    h1_breadcrumb=web_design_service["name"],
    breadcrumb_items=[("الخدمات", "index.html"), (web_design_service["name"], None)],
    body=wd_body,
    extra_schema=wd_schema,
))

cards = ""
for s in SERVICES:
    cards += f"""<a href="{s['slug']}.html" class="bg-white rounded-3xl p-7 border border-gray-100 card-hover flex flex-col">
      <h3 class="font-bold text-lg mb-2">{s['name']}</h3>
      <p class="text-gray-500 text-sm leading-relaxed mb-5 flex-1">{s['short']}</p>
      <div class="flex items-center justify-between">
        <span class="font-latin font-bold text-navy">{s['price']}</span>
        <span class="text-orange font-semibold text-sm">التفاصيل ←</span>
      </div>
    </a>"""
services_hub_body = hero_simple(
    "خدماتنا", "كل خدمات التطوير المهني وتصميم المواقع في مكان واحد",
    "من كتابة السيرة الذاتية المتوافقة مع ATS، إلى تحسين LinkedIn، وحتى تصميم المواقع وصفحات الهبوط الاحترافية — خدمات مصممة لسوق العمل والأعمال في مصر ودول الخليج."
)
services_hub_body += f"""<section class="max-w-7xl mx-auto px-5 md:px-8 py-16">
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
</section>"""
services_hub_body += cta_band("مش متأكد أنهي خدمة تناسبك؟", "تواصل معانا ونساعدك تختار الخدمة المناسبة لهدفك.")
services_hub_schema = '[' + ORG_SCHEMA + ']'
write("services/index.html", page(
    depth=1, active="services",
    title="خدمات WORKLIXEG | كتابة CV، LinkedIn، Portfolio، تصميم مواقع ولاندنج بيدجز",
    description="استعرض كل خدمات WORKLIXEG: كتابة سيرة ذاتية ATS، Cover Letter، تحسين LinkedIn، بورتفوليو، تدريب مقابلات، وتصميم مواقع وصفحات هبوط لمصر ودول الخليج.",
    keywords="خدمات مهنية, كتابة سيرة ذاتية, تحسين لينكدإن, بورتفوليو, تدريب مقابلات, تصميم مواقع, لاندنج بيدج مصر والخليج",
    canonical=f"{SITE_URL}/services/index.html",
    h1_breadcrumb="الخدمات",
    breadcrumb_items=[("الخدمات", None)],
    body=services_hub_body,
    extra_schema=services_hub_schema,
))

print("services done:", len(SERVICES), "+ niches:", len(LANDING_NICHES))
