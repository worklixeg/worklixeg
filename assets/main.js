// header scroll style
(function(){
  const header = document.getElementById('site-header');
  if(!header) return;
  function updateHeader(){
    if(window.scrollY > 40){
      header.style.background = 'rgba(11,18,32,0.85)';
      header.classList.add('header-blur','shadow-lg');
    } else {
      header.style.background = 'transparent';
    }
  }
  window.addEventListener('scroll', updateHeader);
  updateHeader();
})();

// mobile menu
(function(){
  const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if(!menuBtn || !mobileMenu) return;
  menuBtn.addEventListener('click', ()=> mobileMenu.classList.toggle('hidden'));
})();

// counters
(function(){
  const counters = document.querySelectorAll('.counter');
  if(!counters.length) return;
  const counterObserver = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        const el = entry.target;
        const target = parseInt(el.dataset.target,10);
        let cur = 0;
        const step = Math.max(1, Math.round(target/60));
        const tick = ()=>{
          cur += step;
          if(cur >= target){ el.textContent = target; return; }
          el.textContent = cur;
          requestAnimationFrame(tick);
        };
        tick();
        counterObserver.unobserve(el);
      }
    });
  }, {threshold:0.5});
  counters.forEach(c=>counterObserver.observe(c));
})();

// before/after slider
(function(){
  const baSlider = document.getElementById('ba-slider');
  const baAfter = document.querySelector('.ba-after');
  if(!baSlider || !baAfter) return;
  const isRTL = document.documentElement.dir === 'rtl';
  baSlider.addEventListener('input', (e)=>{
    const v = e.target.value;
    if(isRTL){
      baAfter.style.clipPath = `inset(0 ${100-v}% 0 0)`;
    } else {
      baAfter.style.clipPath = `inset(0 0 0 ${v}%)`;
    }
  });
})();

// FAQ accordion
(function(){
  document.querySelectorAll('.faq-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';
      document.querySelectorAll('.accordion-content').forEach(c=> c.style.maxHeight = '0px');
      document.querySelectorAll('.faq-icon').forEach(i=> i.textContent = '+');
      if(!isOpen){
        content.style.maxHeight = content.scrollHeight + 'px';
        icon.textContent = '−';
      }
    });
  });
})();

// reviews carousel
(function(){
  const reviewText = document.getElementById('review-text');
  const reviewName = document.getElementById('review-name');
  const nextBtn = document.getElementById('rev-next');
  const prevBtn = document.getElementById('rev-prev');
  if(!reviewText || !nextBtn) return;
  const reviews = [
    {text:'"السيرة الذاتية اللي عملولي إياها غيّرت شكل تعاملي مع الشركات، حصلت على 3 مقابلات في أسبوعين."', name:'أحمد س. — مهندس مدني'},
    {text:'"خدمة محترفة فعلًا، الفريق فهم مجالي وطلع سيرة ذاتية مناسبة تمامًا لسوق الخليج."', name:'هبة ع. — أخصائية موارد بشرية'},
    {text:'"ملفي على LinkedIn بقى أقوى بكتير، وبدأت أوصلني رسائل من شركات مش كنت متخيل أوصلها."', name:'محمد ن. — مطور واجهات أمامية'}
  ];
  let revIndex = 0;
  function render(){
    reviewText.textContent = reviews[revIndex].text;
    reviewName.textContent = reviews[revIndex].name;
  }
  nextBtn.addEventListener('click', ()=>{ revIndex = (revIndex+1) % reviews.length; render(); });
  if(prevBtn) prevBtn.addEventListener('click', ()=>{ revIndex = (revIndex-1+reviews.length) % reviews.length; render(); });
})();
