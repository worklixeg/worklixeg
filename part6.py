# -*- coding: utf-8 -*-
from generate import *
from part2 import ORG_SCHEMA, SERVICES
from part3 import PRODUCTS
from part4 import ARTICLES

hero = """<section class="relative bg-navy grain overflow-hidden pt-[76px]">
  <div class="absolute -top-40 -left-40 w-[500px] h-[500px] bg-orange/10 rounded-full blur-3xl"></div>
  <div class="absolute top-1/3 -right-32 w-[400px] h-[400px] bg-orange/5 rounded-full blur-3xl"></div>
  <div class="max-w-7xl mx-auto px-5 md:px-8 py-20 md:py-28 grid lg:grid-cols-2 gap-14 items-center relative z-10">
    <div class="text-white">
      <span class="inline-flex items-center gap-2 text-xs font-semibold tracking-wide bg-white/5 border border-line rounded-full px-4 py-2 text-orange mb-6">
        <span class="w-1.5 h-1.5 rounded-full bg-orange"></span>
        متوافق مع أنظمة ATS 100%
      </span>
      <h1 class="font-extrabold text-4xl md:text-6xl leading-[1.15] mb-6">
        احصل على <span class="text-orange">سيرة ذاتية</span> تفتح لك أبواب الشركات الكبرى
      </h1>
      <p class="text-muted text-lg md:text-xl leading-relaxed mb-9 max-w-lg">
        خدمات مهنية متكاملة لصياغة سيرتك الذاتية وتحسين حضورك المهني، وتصميم مواقع ولاندنج بيدجز احترافية، لزيادة فرصك في مصر ودول الخليج.
      </p>
      <div class="flex flex-wrap gap-4 mb-10">
        <a href=\"""" + WA_GENERIC + """\" class="bg-orange text-white font-bold px-8 py-4 rounded-2xl hover:brightness-110 transition shadow-xl shadow-orange-500/25 text-center">
          اطلب سيرتك الذاتية
        </a>
        <a href="portfolio.html" class="border border-white/20 text-white font-bold px-8 py-4 rounded-2xl hover:bg-white/5 transition text-center">
          شاهد نماذج الأعمال
        </a>
      </div>
      <div class="flex items-center gap-6 text-sm text-muted">
        <div class="flex -space-x-3 space-x-reverse">
          <div class="w-9 h-9 rounded-full bg-navy-3 border-2 border-navy flex items-center justify-center text-xs font-bold text-white">A</div>
          <div class="w-9 h-9 rounded-full bg-navy-3 border-2 border-navy flex items-center justify-center text-xs font-bold text-white">H</div>
          <div class="w-9 h-9 rounded-full bg-navy-3 border-2 border-navy flex items-center justify-center text-xs font-bold text-white">M</div>
        </div>
        <span>+5000 عميل واثق بخدماتنا</span>
      </div>
    </div>
    <div class="relative h-[460px] md:h-[560px] hidden sm:block">
      <div class="absolute inset-0 flex items-center justify-center">
        <div class="w-[320px] md:w-[400px] rounded-2xl bg-navy-2 border border-line p-4 shadow-2xl float-1">
          <div class="flex gap-1.5 mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-red-400/70"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-400/70"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-green-400/70"></span>
          </div>
          <div class="bg-white rounded-xl p-4 font-latin" dir="ltr">
            <div class="h-2.5 w-24 bg-navy/80 rounded mb-2"></div>
            <div class="h-2 w-32 bg-gray-300 rounded mb-4"></div>
            <div class="h-1.5 w-full bg-gray-200 rounded mb-1.5"></div>
            <div class="h-1.5 w-full bg-gray-200 rounded mb-1.5"></div>
            <div class="h-1.5 w-4/5 bg-gray-200 rounded mb-4"></div>
            <div class="h-2 w-20 bg-orange/70 rounded mb-2"></div>
            <div class="h-1.5 w-full bg-gray-200 rounded mb-1.5"></div>
            <div class="h-1.5 w-3/4 bg-gray-200 rounded"></div>
          </div>
        </div>
      </div>
      <div class="absolute top-4 right-2 md:right-6 bg-white rounded-2xl shadow-xl p-4 flex items-center gap-3 float-2">
        <div class="ats-ring w-14 h-14 rounded-full bg-navy flex items-center justify-center relative">
          <span class="font-latin font-extrabold text-orange text-sm">98%</span>
        </div>
        <div class="font-latin" dir="ltr">
          <div class="text-[11px] text-gray-400 font-semibold">ATS SCORE</div>
          <div class="text-sm font-bold text-navy">Excellent Match</div>
        </div>
      </div>
      <div class="absolute bottom-8 left-0 md:-left-4 bg-white rounded-2xl shadow-xl p-4 flex items-center gap-3 max-w-[230px] float-3">
        <div class="w-10 h-10 rounded-full bg-orange/15 flex items-center justify-center flex-shrink-0">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7Z" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </div>
        <div class="text-xs font-latin" dir="ltr">
          <div class="font-bold text-navy">Interview Invitation</div>
          <div class="text-gray-400">Google Careers · 2m ago</div>
        </div>
      </div>
      <div class="absolute bottom-0 right-4 md:right-10 bg-white rounded-2xl shadow-xl p-3 flex items-center gap-2 float-1">
        <div class="w-8 h-8 rounded-lg bg-[#0A66C2] flex items-center justify-center text-white font-latin font-bold text-xs">in</div>
        <div class="text-xs font-latin" dir="ltr">
          <div class="font-bold text-navy">Profile Optimized</div>
        </div>
      </div>
    </div>
  </div>
</section>"""

trust_bar = """<section class="bg-white border-b border-gray-100">
  <div class="max-w-7xl mx-auto px-5 md:px-8 py-12 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
    <div>
      <div class="font-latin font-extrabold text-3xl md:text-4xl text-navy counter" data-target="5000">0</div>
      <div class="text-sm text-gray-500 mt-1">مشروع منجز</div>
    </div>
    <div>
      <div class="font-latin font-extrabold text-3xl md:text-4xl text-navy"><span class="counter" data-target="98">0</span>%</div>
      <div class="text-sm text-gray-500 mt-1">رضا العملاء</div>
    </div>
    <div>
      <div class="font-latin font-extrabold text-3xl md:text-4xl text-navy"><span class="counter" data-target="24">0</span>س</div>
      <div class="text-sm text-gray-500 mt-1">متوسط وقت التسليم</div>
    </div>
    <div>
      <div class="font-latin font-extrabold text-3xl md:text-4xl text-orange">ATS</div>
      <div class="text-sm text-gray-500 mt-1">تنسيق معتمد ومُختبر</div>
    </div>
  </div>
</section>"""

why_choose = """<section class="max-w-7xl mx-auto px-5 md:px-8 py-24">
  <div class="text-center max-w-2xl mx-auto mb-16">
    <span class="text-orange font-bold text-sm tracking-wide">لماذا WORKLIXEG</span>
    <h2 class="font-extrabold text-3xl md:text-4xl mt-3">فريق حقيقي، ونتائج قابلة للقياس</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
    <div class="bg-white rounded-3xl p-8 border border-gray-100 card-hover">
      <div class="w-12 h-12 rounded-2xl bg-orange/10 flex items-center justify-center mb-5">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <h3 class="font-bold text-lg mb-2">كتّاب محترفون</h3>
      <p class="text-gray-500 text-sm leading-relaxed">فريق متخصص في صياغة السير الذاتية لكل قطاع ومستوى وظيفي.</p>
    </div>
    <div class="bg-white rounded-3xl p-8 border border-gray-100 card-hover">
      <div class="w-12 h-12 rounded-2xl bg-orange/10 flex items-center justify-center mb-5">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><path d="m9 12 2 2 4-4M12 3l8 4v5c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V7Z" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <h3 class="font-bold text-lg mb-2">متوافق مع ATS</h3>
      <p class="text-gray-500 text-sm leading-relaxed">تنسيق مُختبر يضمن قراءة سيرتك بشكل صحيح من أنظمة الفرز الآلي.</p>
    </div>
    <div class="bg-white rounded-3xl p-8 border border-gray-100 card-hover">
      <div class="w-12 h-12 rounded-2xl bg-orange/10 flex items-center justify-center mb-5">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <h3 class="font-bold text-lg mb-2">تسليم سريع</h3>
      <p class="text-gray-500 text-sm leading-relaxed">استلم مسودتك الأولى خلال 24 ساعة، مع خيار التسليم العاجل.</p>
    </div>
    <div class="bg-white rounded-3xl p-8 border border-gray-100 card-hover">
      <div class="w-12 h-12 rounded-2xl bg-orange/10 flex items-center justify-center mb-5">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <h3 class="font-bold text-lg mb-2">أسعار مناسبة</h3>
      <p class="text-gray-500 text-sm leading-relaxed">باقات مرنة تناسب الطلاب والخريجين والمحترفين وأصحاب الأعمال.</p>
    </div>
    <div class="bg-white rounded-3xl p-8 border border-gray-100 card-hover">
      <div class="w-12 h-12 rounded-2xl bg-orange/10 flex items-center justify-center mb-5">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><path d="M4 4v16h16M8 15l3-3 3 3 5-6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <h3 class="font-bold text-lg mb-2">تعديلات غير محدودة</h3>
      <p class="text-gray-500 text-sm leading-relaxed">نراجع معك كل تفصيلة حتى تصل للنسخة النهائية المرضية.</p>
    </div>
    <div class="bg-white rounded-3xl p-8 border border-gray-100 card-hover">
      <div class="w-12 h-12 rounded-2xl bg-orange/10 flex items-center justify-center mb-5">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FF7A00" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <h3 class="font-bold text-lg mb-2">خبراء توظيف وتصميم</h3>
      <p class="text-gray-500 text-sm leading-relaxed">استشارات مهنية ومواقع احترافية من متخصصين بسوقي مصر والخليج.</p>
    </div>
  </div>
</section>"""

before_after = """<section class="bg-navy py-24">
  <div class="max-w-5xl mx-auto px-5 md:px-8 text-center">
    <span class="text-orange font-bold text-sm tracking-wide">التحول</span>
    <h2 class="font-extrabold text-3xl md:text-4xl text-white mt-3 mb-4">من سيرة عادية إلى سيرة تُقابَل عليها</h2>
    <p class="text-muted mb-12 max-w-xl mx-auto">حرّك المؤشر لترى الفرق بنفسك.</p>
    <div class="ba-slider-wrap rounded-3xl overflow-hidden shadow-2xl mx-auto max-w-2xl aspect-[4/3] bg-white">
      <div class="absolute inset-0 p-8 font-latin text-right" dir="ltr">
        <div class="text-xs text-gray-400 mb-4">BEFORE</div>
        <div class="h-3 w-32 bg-gray-300 rounded mb-3"></div>
        <div class="h-2 w-full bg-gray-200 rounded mb-2"></div>
        <div class="h-2 w-full bg-gray-200 rounded mb-2"></div>
        <div class="h-2 w-5/6 bg-gray-200 rounded mb-2"></div>
        <div class="h-2 w-full bg-gray-200 rounded mb-2"></div>
        <div class="h-2 w-2/3 bg-gray-200 rounded"></div>
      </div>
      <div class="ba-after bg-gray-50">
        <div class="p-8 font-latin" dir="ltr">
          <div class="text-xs text-orange font-bold mb-4">AFTER</div>
          <div class="h-3 w-40 bg-navy rounded mb-3"></div>
          <div class="h-2 w-24 bg-orange/60 rounded mb-4"></div>
          <div class="h-2 w-full bg-navy/10 rounded mb-2"></div>
          <div class="h-2 w-full bg-navy/10 rounded mb-2"></div>
          <div class="h-2 w-4/5 bg-navy/10 rounded mb-4"></div>
          <div class="h-2 w-28 bg-orange/60 rounded mb-2"></div>
          <div class="h-2 w-full bg-navy/10 rounded"></div>
        </div>
      </div>
    </div>
    <input type="range" id="ba-slider" min="0" max="100" value="50" class="w-full max-w-2xl mt-6 accent-orange">
  </div>
</section>"""

svc_cards = ""
for s in SERVICES:
    svc_cards += f"""<a href="services/{s['slug']}.html" class="bg-white rounded-3xl p-7 border border-gray-100 card-hover flex flex-col">
      <h3 class="font-bold text-lg mb-2">{s['name']}</h3>
      <p class="text-gray-500 text-sm leading-relaxed mb-5 flex-1">{s['short']}</p>
      <div class="flex items-center justify-between">
        <span class="font-latin font-bold text-navy">{s['price']}</span>
        <span class="text-orange font-semibold text-sm">التفاصيل ←</span>
      </div>
    </a>"""
services_section = f"""<section id="services" class="max-w-7xl mx-auto px-5 md:px-8 py-24">
  <div class="text-center max-w-2xl mx-auto mb-16">
    <span class="text-orange font-bold text-sm tracking-wide">خدماتنا</span>
    <h2 class="font-extrabold text-3xl md:text-4xl mt-3">كل ما تحتاجه لبناء حضورك المهني وموقعك</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{svc_cards}</div>
  <div class="text-center mt-10">
    <a href="services/index.html" class="text-orange font-bold">استعرض كل الخدمات ←</a>
  </div>
</section>"""

store_cards = ""
for p in PRODUCTS[:6]:
    store_cards += f"""<a href="store/{p['slug']}.html" class="bg-white rounded-3xl overflow-hidden border border-gray-100 card-hover block">
      <div class="h-40 bg-gray-100 flex items-center justify-center">
        <div class="w-20 h-28 bg-white rounded shadow-md border border-gray-200"></div>
      </div>
      <div class="p-6">
        <h3 class="font-bold mb-1">{p['name']}</h3>
        <div class="flex items-center justify-between mt-4">
          <span class="font-latin font-bold text-navy">{p['price']}</span>
          <span class="text-sm font-semibold bg-navy text-white px-4 py-2 rounded-xl">تحميل</span>
        </div>
      </div>
    </a>"""
store_section = f"""<section id="store" class="bg-white py-24">
  <div class="max-w-7xl mx-auto px-5 md:px-8">
    <div class="text-center max-w-2xl mx-auto mb-16">
      <span class="text-orange font-bold text-sm tracking-wide">المتجر الرقمي</span>
      <h2 class="font-extrabold text-3xl md:text-4xl mt-3">قوالب وأدلة جاهزة للتحميل الفوري</h2>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">{store_cards}</div>
    <div class="text-center mt-10">
      <a href="store/index.html" class="text-orange font-bold">تصفح كل المتجر ←</a>
    </div>
  </div>
</section>"""

portfolio_preview = """<section id="portfolio" class="max-w-7xl mx-auto px-5 md:px-8 py-24">
  <div class="text-center max-w-2xl mx-auto mb-16">
    <span class="text-orange font-bold text-sm tracking-wide">أعمالنا</span>
    <h2 class="font-extrabold text-3xl md:text-4xl mt-3">نماذج من مشاريع حقيقية سلمناها</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="rounded-3xl bg-navy h-64 p-6 flex flex-col justify-end card-hover">
      <span class="text-white font-bold">CV احترافي</span>
      <span class="text-muted text-sm">مهندس اتصالات</span>
    </div>
    <div class="rounded-3xl bg-navy-3 h-64 p-6 flex flex-col justify-end card-hover">
      <span class="text-white font-bold">Portfolio تصميم</span>
      <span class="text-muted text-sm">مصمم جرافيك</span>
    </div>
    <div class="rounded-3xl bg-navy h-64 p-6 flex flex-col justify-end card-hover">
      <span class="text-white font-bold">LinkedIn</span>
      <span class="text-muted text-sm">مدير مبيعات</span>
    </div>
    <div class="rounded-3xl bg-navy-3 h-64 p-6 flex flex-col justify-end card-hover">
      <span class="text-white font-bold">موقع ولاندنج بيدج</span>
      <span class="text-muted text-sm">عيادة أسنان</span>
    </div>
  </div>
  <div class="text-center mt-10">
    <a href="portfolio.html" class="text-orange font-bold">شاهد كل الأعمال ←</a>
  </div>
</section>"""

reviews_section = """<section class="bg-navy py-24 overflow-hidden">
  <div class="max-w-4xl mx-auto px-5 md:px-8 text-center">
    <span class="text-orange font-bold text-sm tracking-wide">آراء العملاء</span>
    <h2 class="font-extrabold text-3xl md:text-4xl text-white mt-3 mb-14">قصص نجاح حقيقية</h2>
    <div class="relative">
      <div id="review-slide" class="bg-navy-2 border border-line rounded-3xl p-10">
        <div class="flex justify-center gap-1 mb-5 text-orange">
          <span>★★★★★</span>
        </div>
        <p id="review-text" class="text-white text-lg leading-relaxed mb-6">"السيرة الذاتية اللي عملولي إياها غيّرت شكل تعاملي مع الشركات، حصلت على 3 مقابلات في أسبوعين."</p>
        <div id="review-name" class="text-orange font-bold">أحمد س. — مهندس مدني</div>
      </div>
      <div class="flex justify-center gap-4 mt-6">
        <button id="rev-prev" class="w-10 h-10 rounded-full border border-line text-white flex items-center justify-center hover:bg-white/10">‹</button>
        <button id="rev-next" class="w-10 h-10 rounded-full border border-line text-white flex items-center justify-center hover:bg-white/10">›</button>
      </div>
    </div>
    <div class="mt-10">
      <a href="reviews.html" class="text-orange font-bold">اقرأ كل التقييمات ←</a>
    </div>
  </div>
</section>"""

blog_cards = ""
for a in ARTICLES[:4]:
    blog_cards += f"""<a href="blog/{a['slug']}.html" class="bg-white rounded-3xl p-6 border border-gray-100 card-hover block">
      <span class="text-xs font-bold text-orange">{a['category']}</span>
      <h3 class="font-bold mt-2 leading-snug">{a['title']}</h3>
    </a>"""
blog_section = f"""<section id="blog" class="max-w-7xl mx-auto px-5 md:px-8 py-24">
  <div class="text-center max-w-2xl mx-auto mb-16">
    <span class="text-orange font-bold text-sm tracking-wide">المدونة</span>
    <h2 class="font-extrabold text-3xl md:text-4xl mt-3">مقالات تساعدك تتوظف أسرع</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">{blog_cards}</div>
  <div class="text-center mt-10">
    <a href="blog/index.html" class="text-orange font-bold">اقرأ كل المقالات ←</a>
  </div>
</section>"""

home_faqs = [
    ("كم مدة تسليم السيرة الذاتية؟", "مدة التسليم القياسية 24 ساعة من استلام بياناتك، مع خيار تسليم عاجل لمن يحتاج وقتًا أقل."),
    ("هل السيرة متوافقة فعلًا مع أنظمة ATS؟", "نعم، نستخدم تنسيقًا مُختبرًا يمر بسلاسة عبر أنظمة الفرز الآلي المستخدمة في أغلب الشركات الكبرى."),
    ("هل يوجد تعديلات بعد التسليم؟", "نعم، جولات تعديل غير محدودة حتى تصل للنسخة اللي تمثلك بشكل كامل."),
    ("هل تقدموا خدمات لسوق الخليج؟", "نعم، لدينا خبرة في صياغة سير ذاتية وخطابات تقديم وتصميم مواقع مخصصة لمتطلبات سوق العمل والأعمال في دول الخليج."),
]
faq_section = faq_block(home_faqs).replace('class="bg-white py-20"', 'id="faq" class="bg-white py-24"')

final_cta = """<section class="bg-navy py-24 relative overflow-hidden grain">
  <div class="absolute inset-0 flex items-center justify-center">
    <div class="w-[600px] h-[600px] bg-orange/10 rounded-full blur-3xl"></div>
  </div>
  <div class="max-w-2xl mx-auto px-5 text-center relative z-10">
    <h2 class="font-extrabold text-3xl md:text-5xl text-white mb-6">جاهز تبدأ رحلتك المهنية؟</h2>
    <p class="text-muted text-lg mb-10">تواصل معنا الآن واحصل على سيرة ذاتية أو موقع تستحقه.</p>
    <a href=\"""" + WA_GENERIC + """\" class="inline-block bg-orange text-white font-bold px-10 py-4 rounded-2xl hover:brightness-110 transition shadow-xl shadow-orange-500/25">
      ابدأ الآن
    </a>
  </div>
</section>"""

home_body = (hero + trust_bar + why_choose + before_after + services_section +
             store_section + portfolio_preview + reviews_section + blog_section +
             faq_section + final_cta)

home_schema = ('[' + ORG_SCHEMA + ',' + faq_schema(home_faqs) + ']')

home_html = page(
    depth=0, active="home",
    title="WORKLIXEG | كتابة سيرة ذاتية ATS وتصميم مواقع ولاندنج بيدجز لمصر والخليج",
    description="منصة WORKLIXEG لخدمات التطوير المهني وتصميم المواقع: كتابة سيرة ذاتية متوافقة مع ATS، Cover Letter، تحسين LinkedIn، بورتفوليو، وتصميم مواقع ولاندنج بيدجز. تسليم سريع لمصر ودول الخليج.",
    keywords="كتابة سيرة ذاتية, CV احترافي, سيرة ذاتية ATS, تحسين لينكدإن, بورتفوليو, تصميم مواقع, لاندنج بيدج, وظائف مصر والخليج",
    canonical=f"{SITE_URL}/index.html",
    h1_breadcrumb=None,
    breadcrumb_items=None,
    body=home_body,
    extra_schema=home_schema,
)
write("index.html", home_html)
print("home done")
