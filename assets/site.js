(function(){
  // Google Ads dönüşüm etiketleri: Ads > Hedefler > Dönüşümler'deki etiketi '/' sonrasına yazın.
  // Etiket girilene kadar dönüşüm gönderilmez (generate_lead ve dataLayer olayları yine çalışır).
  var CONFIG = {
    call:     { ads: 'AW-18133483046/ARAMA_ETIKETI' },
    whatsapp: { ads: 'AW-18133483046/WHATSAPP_ETIKETI' }
  };
  var WA_DEFAULT = 'Merhaba, yerden ısıtma sistemleri hakkında bilgi almak istiyorum.';

  // WhatsApp linklerine hazır mesaj ekle
  document.querySelectorAll('.wa-link').forEach(function(a){
    a.href = 'https://wa.me/905342842623?text=' + encodeURIComponent(a.getAttribute('data-msg') || WA_DEFAULT);
  });

  document.addEventListener('click', function(e){
    var el = e.target.closest('[data-track]');
    if (!el) return;
    var type = el.getAttribute('data-track'), loc = el.getAttribute('data-loc') || '';
    var cfg = CONFIG[type];
    if (typeof window.gtag === 'function') {
      if (cfg && cfg.ads && !/_ETIKETI$/.test(cfg.ads)) gtag('event', 'conversion', { send_to: cfg.ads });
      gtag('event', type === 'call' || type === 'whatsapp' ? 'generate_lead' : 'click', { method: type, location: loc });
    }
    if (typeof window.fbq === 'function' && (type === 'call' || type === 'whatsapp')) {
      fbq('track', 'Contact', { method: type, location: loc });
    }
    (window.dataLayer = window.dataLayer || []).push({ event: 'lead_click', lead_type: type, lead_location: loc });
  });

  var y = document.getElementById('yil'); if (y) y.textContent = new Date().getFullYear();
})();
