(function () {
  const sections = document.querySelectorAll('[id]');
  const navLinks = document.querySelectorAll('.quick-nav a');
  function onScroll() {
    let current = '';
    sections.forEach(sec => {
      if (sec.getBoundingClientRect().top <= 120) current = sec.getAttribute('id');
    });
    navLinks.forEach(a => {
      a.style.background = a.getAttribute('href') === '#' + current
        ? 'rgba(255,255,255,0.95)'
        : 'rgba(255,255,255,0.65)';
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
})();
(function(){
  if(localStorage.getItem('cwc_cookie_consent')) { document.getElementById('cwc-cookie-banner').style.display='none'; return; }
  document.getElementById('cwc-cookie-banner').style.display='flex';
  document.getElementById('cwc-accept').onclick = function(){ localStorage.setItem('cwc_cookie_consent','accepted'); document.getElementById('cwc-cookie-banner').style.display='none'; };
  document.getElementById('cwc-decline').onclick = function(){ localStorage.setItem('cwc_cookie_consent','declined'); document.getElementById('cwc-cookie-banner').style.display='none'; };
})();
