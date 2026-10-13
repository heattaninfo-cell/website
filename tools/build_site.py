#!/usr/bin/env python3
"""Heattan landing sitesini üretir: anasayfa, Ürünlerimiz sayfası ve ürün detay sayfaları.

Kullanım:  python3 tools/build_site.py
Ürün eklemek/düzenlemek için aşağıdaki PRODUCTS listesini değiştirip komutu yeniden çalıştırın.
Ortak stil: landing/assets/style.css, ortak JS (WhatsApp mesajı + dönüşüm takibi): landing/assets/site.js
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "landing")
PARTIALS = os.path.join(ROOT, "tools", "partials")

PHONE_TEL = "+905342842623"
PHONE_TXT = "0534 284 26 23"
WA = "https://wa.me/905342842623"

CATEGORIES = [
    ("karbon-film", "Karbon Film Yerden Isıtma",
     "İnce yapısı sayesinde parke ve laminat altına kolayca uygulanan, hızlı ısınan ve ısıyı homojen dağıtan zemin altı ısıtıcı paneller."),
    ("kablo", "Zemin Isıtıcı Kablolar",
     "Seramik, mermer ve beton gibi ısı iletiminin zor olduğu zeminlerde güvenli, dengeli ve uzun ömürlü ısıtma."),
    ("termostat", "Termostatlar",
     "Basit kullanımdan programlanabilir ve WiFi kontrollü modellere kadar yerden ısıtma için sıcaklık kontrol çözümleri."),
    ("pano", "Kontrol Panoları",
     "Küçük alanlardan büyük ölçekli projelere kadar ısıtma sistemlerini güvenli ve otomatik yöneten kontrol panoları."),
]

COMMON_FILM_FEATURES = [
    "Bütün ısıtma yüzeyinde aynı sıcaklık, homojen ısı dağılımı",
    "Esnek, dayanıklı ve 1 mm'den ince",
    "Termostat kontrolüyle ayarlanan sıcaklık sabit kalır, tüketim minimumda tutulur",
    "Kurulum ve işletme maliyeti eski ısıtma sistemlerinden daha ekonomik",
    "Doğalgazın olmadığı yerlerde ekonomik ısıtma çözümü",
    "Film üzerindeki sıcaklık ortalama 40-50°C, taban sensörüyle istenen ısıda sabitlenir",
    "Termostatsız kullanıma uygun değildir",
]

# Metinler heattan.com.tr/urunlerimiz sayfasından alınmıştır; teknik özellikler (specs) üretici sayfalarından.
PRODUCTS = [
    dict(slug="rexva-xt-308-220w-karbon-film", cat="karbon-film", name="Rexva XT-308 220W Karbon Film",
         img="rexva-xt-308-220w", badge="220W",
         short="Parke ve laminat zemin altı için yüksek verimli karbon film.",
         desc=["Rexva XT-308 220W karbon film, parke ve laminat zemin altı uygulamalar için geliştirilmiş yüksek verimli yerden ısıtma sistemidir. İnce ve esnek yapısı sayesinde zemin yüksekliğini artırmadan kolay montaj imkânı sunar.",
               "Homojen ısı dağılımı sağlayarak yaşam alanlarının her noktasında dengeli sıcaklık oluşturur. Düşük enerji tüketimi ve termostat uyumu sayesinde ekonomik ve uzun ömürlü bir ısıtma çözümüdür."],
         features=["Parke ve laminat altı uygulama", "Zemin yüksekliğini artırmaz", "Homojen ısı dağılımı", "Termostat uyumlu"],
         specs=[("Ürün kodu", "XT-308 220 W"), ("Ölçüler", "800 mm x 0,338 mm x 100 m"), ("Güç tüketimi", "220 W/m"),
                ("Paket uzunluğu", "100 m"), ("Ağırlık", "40 kg"), ("Film görünümü", "Şeffaf film (Transparent)")],
         details=COMMON_FILM_FEATURES),
    dict(slug="rexva-xt-308-240w-karbon-film", cat="karbon-film", name="Rexva XT-308 240W Karbon Film",
         img="rexva-xt-308-240w", badge="240W",
         short="Geniş alanlarda hızlı ve güçlü ısınma.",
         desc=["Rexva XT-308 240W karbon film, geniş alanlarda yüksek performans sunan güçlü yerden ısıtma sistemidir. Yüksek watt değeri sayesinde kısa sürede etkili ısınma sağlar.",
               "Homojen ısı dağılımı ile mekânın her noktasında eşit sıcaklık oluşturur ve büyük metrekareli alanlar için ideal çözümler sunar."],
         features=["Yüksek watt, hızlı ısınma", "Büyük metrekareli alanlar için", "Mekânın her noktasında eşit sıcaklık"]),
    dict(slug="hot-film-sh-308m-240w-karbon-film", cat="karbon-film", name="Hot Film SH-308M 240W Karbon Film",
         img="hot-film-sh-308m-240w", badge="240W",
         short="Profesyonel projeler için yüksek performans.",
         desc=["Hot Film SH-308M 240W karbon film, profesyonel projeler için geliştirilmiş yüksek performanslı ısıtma çözümüdür. Tüm yüzeyde eşit ısı sağlayarak maksimum konfor sunar.",
               "1 mm'den ince yapısı, esnekliği ve dayanıklılığı sayesinde kolay uygulanır ve uzun ömürlü kullanım sağlar. Termostat ile birlikte kullanıldığında enerji tüketimini optimize eder."],
         features=["1 mm'den ince yapı", "Esnek ve dayanıklı", "Tüm yüzeyde eşit ısı", "Termostat ile enerji optimizasyonu"]),
    dict(slug="hot-film-sh-303-t-67w-karbon-film", cat="karbon-film", name="Hot Film SH-303 T 67W Karbon Film",
         img="hot-film-sh-303t-67w", badge="67W",
         short="Dar alanlar ve özel uygulamalar için düşük tüketim.",
         desc=["Hot Film SH-303 T 67W karbon film, dar alanlar ve özel uygulamalar için tasarlanmış düşük tüketimli yerden ısıtma çözümüdür. Esnek yapısı sayesinde farklı yüzeylere kolayca uygulanabilir.",
               "Düşük watt değeri ile kontrollü ısıtma sağlayarak küçük alanlarda enerji tasarrufu sunar. Homojen ısı dağılımı sayesinde konforlu ve dengeli bir kullanım sağlar."],
         features=["Dar ve özel alanlar için", "Düşük tüketim, kontrollü ısıtma", "Farklı yüzeylere uygulanabilir"]),
    dict(slug="hot-film-sh-308m-220w-karbon-film", cat="karbon-film", name="Hot Film SH-308M 220W Karbon Film",
         img="hot-film-sh-308m-220w", badge="220W", light=True,
         short="Ev, ofis, cami, parke ve halı altı için 80 cm karbon film.",
         desc=["Hot Film SH-308M 220W karbon film; ev, ofis ve cami ısıtması ile parke altı ve halı altı uygulamalar için tasarlanmış, 80 cm genişliğinde mat görünümlü ısıtıcı filmdir.",
               "Tüm ısıtma yüzeyinde aynı sıcaklığı sağlayarak mekânın bazı yerlerinin sıcak, bazı yerlerinin soğuk kalmasını önler ve alanın tamamını eşit derecede ısıtır. Termostat kontrolü ile ayarlanan ortam sıcaklığı korunur, enerji tüketimi minimum seviyede kalır."],
         features=["Ev, ofis ve cami ısıtması", "Parke ve halı altı uygulama", "80 cm genişlik, 220 W/m", "Termostat kontrolüyle ekonomik"],
         specs=[("Ürün kodu", "SH-308M 220 W"), ("Ölçüler", "800 mm x 0,338 mm x 100 m"), ("Güç tüketimi", "220 W/m"),
                ("Paket uzunluğu", "100 m (metre ile de satılır)"), ("Ağırlık", "42 kg (100 m rulo)"), ("Film görünümü", "Mat film (Milk White)")],
         details=COMMON_FILM_FEATURES),
    dict(slug="rexva-xt-306-165w-karbon-film", cat="karbon-film", name="Rexva XT-306 165W Karbon Film",
         img="rexva-xt-306-165w", badge="165W", light=True,
         short="60 cm genişlikte, dar alanlara uygun karbon film.",
         desc=["Rexva XT-306 165W karbon film; ev, ofis ve cami ile parke altı ve halı altı uygulamalar için 60 cm genişliğinde, şeffaf görünümlü ısıtıcı filmdir. Daha dar genişliği sayesinde koridor ve küçük odalarda yerleşimi kolaylaştırır.",
               "Homojen ısı dağılımı ile mekânın tamamını eşit derecede ısıtır. Termostat kontrolü sayesinde ayarlanan ortam sıcaklığının sürekliliği sağlanır ve enerji tüketimi minimum seviyede kalır."],
         features=["60 cm genişlik, 165 W/m", "Parke ve halı altı uygulama", "Ev, ofis ve cami için", "Termostat kontrolüyle ekonomik"],
         specs=[("Ürün kodu", "XT-306 165 W"), ("Ölçüler", "600 mm x 0,338 mm x 100 m"), ("Güç tüketimi", "165 W/m"),
                ("Paket uzunluğu", "100 m"), ("Ağırlık", "40 kg"), ("Film görünümü", "Şeffaf film (Transparent)")],
         details=COMMON_FILM_FEATURES),
    dict(slug="hot-film-sh-305-e-200w-karbon-film", cat="karbon-film", name="Hot Film SH-305 E 200W Sauna Karbon Film",
         img="hot-film-sh-305-e-200w", badge="Sauna · 200W", light=True,
         short="Yüksek sıcaklık tipi, sauna uygulamaları için karbon film.",
         desc=["Hot Film SH-305 E 200W, yüksek sıcaklık (High Temperature) tipinde üretilmiş, sauna uygulamaları için önerilen 50 cm genişliğinde karbon filmdir. Ev, ofis ve cami ısıtmasında da kullanılabilir.",
               "Esnek ve dayanıklı yapısı, 1 mm'den ince kalınlığı ve homojen ısı dağılımı ile uygulandığı yüzeyin tamamında eşit sıcaklık sağlar. Termostat kontrolüyle ayarlanan sıcaklıkta sabit ve ekonomik çalışır."],
         features=["Yüksek sıcaklık tipi (sauna)", "50 cm genişlik, 200 W/m", "150 m rulo", "Termostat kontrolüyle ekonomik"],
         specs=[("Ürün kodu", "SH-305 E 200 W"), ("Ölçüler", "500 mm x 0,338 mm x 150 m"), ("Güç tüketimi", "200 W/m"),
                ("Paket uzunluğu", "150 m"), ("Ağırlık", "38 kg"), ("Film görünümü", "Yüksek sıcaklık (High Temperature)")],
         details=COMMON_FILM_FEATURES),
    dict(slug="zemin-isitici-kablo-mat", cat="kablo", name="Zemin Isıtıcı Kablo Mat",
         img="isitici-kablo-mat", badge="Kablo",
         short="Seramik, mermer ve beton zeminler için güvenli ısıtma.",
         desc=["Zemin altı ısıtma uygulamalarında güvenli, dengeli ve uzun ömürlü bir sıcaklık sağlamak üzere özel olarak tasarlanmıştır.",
               "Özellikle ısı iletiminde zorlu olan seramik, mermer ve beton zeminlerde yüksek performans göstererek yaşam alanlarınızda aradığınız konforu sunar."],
         features=["Seramik, mermer ve beton zeminler", "Güvenli ve dengeli ısıtma", "Uzun ömürlü kullanım"]),
    dict(slug="shr-2p-kablo-isitici", cat="kablo", name="SHR-2P Kablo Isıtıcı",
         img="shr-2p-kablo-isitici", badge="Kablo",
         short="Geniş alanlar için profesyonel kablo ısıtıcı serisi.",
         desc=["Yüksek performans ve üst düzey güvenlik gerektiren profesyonel uygulamalar için geliştirilmiş özel seridir.",
               "Özellikle geniş metrekareli alanlarda son derece etkili bir ısıtma sağlarken, enerji verimliliğini her zaman ön planda tutarak güçlü ve ekonomik bir çözüm sunar."],
         features=["Profesyonel uygulamalar için", "Geniş metrekareli alanlarda etkili", "Enerji verimli ve ekonomik"]),
    dict(slug="th-101-termostat", cat="termostat", name="TH-101 Termostat",
         img="th-101-termostat", badge="Termostat",
         short="Kolay kullanımlı, ekonomik sıcaklık kontrolü.",
         desc=["Pratiklik ve ekonomiyi bir arada arayanlar için ideal seçim. Yerden ısıtma sistemleri için özel olarak geliştirilen TH-101, kullanımı son derece kolay ve güvenilir bir sıcaklık kontrol çözümüdür.",
               "Temel ısı kontrol ihtiyaçlarınızı eksiksiz karşılayarak mekânınızda aradığınız sıcaklığı zahmetsizce sağlar."],
         features=["Yerden ısıtma için geliştirildi", "Kolay ve güvenilir kullanım", "Ekonomik çözüm"]),
    dict(slug="uth-200-termostat", cat="termostat", name="UTH-200 Programlanabilir Termostat",
         img="uth-200-termostat", badge="Programlanabilir",
         short="Günlük ve haftalık programla enerji tasarrufu.",
         desc=["Konforu ve enerji tasarrufunu kişiselleştirin. Gelişmiş programlanabilir özellikleri sayesinde UTH-200, günlük ve haftalık sıcaklık ayarları yapmanıza imkân tanır.",
               "Yaşam alışkanlıklarınıza ve rutininize uyum sağlayarak gereksiz enerji tüketiminin önüne geçer."],
         features=["Günlük ve haftalık programlama", "Rutininize uyum", "Gereksiz tüketimi önler"]),
    dict(slug="uth-2000-wifi-termostat", cat="termostat", name="UTH-2000 WiFi Termostat",
         img="uth-2000-wifi-termostat", badge="WiFi",
         short="Mobil uygulamayla her yerden kontrol.",
         desc=["Uzaktan erişim ve akıllı kontrol teknolojisiyle donatılan UTH-2000 WiFi, yerden ısıtma sisteminizde maksimum konfor sunar.",
               "Nerede olursanız olun, mobil uygulaması üzerinden evinizin veya ofisinizin sıcaklığını dilediğiniz gibi ayarlama ve kontrol etme özgürlüğü sağlar."],
         features=["WiFi ile uzaktan erişim", "Mobil uygulama ile kontrol", "Ev ve ofis için"]),
    dict(slug="klima-kontrol-panosu", cat="pano", name="Klima Kontrol Panosu",
         img="klima-kontrol-panosu", badge="Isıtma + Soğutma",
         short="Isıtma ve soğutmayı tek merkezden yönetin.",
         desc=["Mekânınızın sadece ısınmasını değil, tüm iklimini tek merkezden yönetin.",
               "Isıtma ve soğutma (klima) sistemlerinizin tam otomatik, güvenli ve zaman ayarlı şekilde, yüksek enerji verimliliğiyle çalışmasını sağlayan akıllı otomasyon ünitesidir."],
         features=["Isıtma ve klima tek merkezde", "Tam otomatik ve zaman ayarlı", "Enerji verimli çalışma"]),
    dict(slug="tp-6-kontrol-panosu", cat="pano", name="TP-6 Kontrol Panosu",
         img="tp-6-kontrol-panosu", badge="Kompakt",
         short="Küçük ve orta ölçekli alanlar için.",
         desc=["Kompakt yapısıyla küçük ve orta ölçekli alanlar için pratik ve stabil çalışma sunar."],
         features=["Kompakt yapı", "Küçük ve orta ölçekli alanlar", "Stabil çalışma"]),
    dict(slug="tp-12-63a-kontrol-panosu", cat="pano", name="TP-12 (63A) Kontrol Panosu",
         img="tp-12-63a-kontrol-panosu", badge="63A",
         short="Yüksek akım gerektiren profesyonel sistemler için.",
         desc=["Yüksek akım kapasitesi (63A) gerektiren, yoğun ve güçlü performans beklenen profesyonel sistemlerin çözümüdür."],
         features=["63A akım kapasitesi", "Profesyonel sistemler için", "Yoğun kullanıma uygun"]),
    dict(slug="tp-18-kontrol-panosu", cat="pano", name="TP-18 Kontrol Panosu",
         img="tp-18-kontrol-panosu", badge="Otomatik",
         short="Bileşenleri senkronize çalıştıran kontrol merkezi.",
         desc=["Sistem bileşenlerinizin uyum içinde çalışmasını sağlayan, güvenilir bir otomatik kontrol merkezidir."],
         features=["Otomatik kontrol", "Bileşen senkronizasyonu", "Güvenilir çalışma"]),
    dict(slug="tp-24-kontrol-panosu", cat="pano", name="TP-24 Kontrol Panosu",
         img="tp-24-kontrol-panosu", badge="Yüksek kapasite",
         short="Geniş çaplı projelerde çoklu bileşen yönetimi.",
         desc=["Geniş çaplı projelerde çoklu sistem bileşenlerini sorunsuz şekilde yönetebilen yüksek kapasiteli ünitemizdir."],
         features=["Yüksek kapasite", "Çoklu bileşen yönetimi", "Geniş çaplı projeler"]),
    dict(slug="tp-30-kontrol-panosu", cat="pano", name="TP-30 Kontrol Panosu",
         img="tp-30-kontrol-panosu", badge="En güçlü",
         short="Büyük ölçekli kapsamlı sistemler için.",
         desc=["Büyük ölçekli ve çok sayıda bileşen barındıran kapsamlı ısıtma sistemleri için tasarlanmış en güçlü yönetim çözümümüzdür."],
         features=["Büyük ölçekli sistemler", "Çok sayıda bileşen", "En güçlü yönetim çözümü"]),
    dict(slug="tp-06-50-wifi-kontrol-panosu", cat="pano", name="TP-06-50 WiFi'li Kontrol Panosu",
         img="tp-06-50-wifi-kontrol-panosu", badge="WiFi",
         short="Küçük ve orta ölçekli sistemler için akıllı pano.",
         desc=["Küçük ve orta ölçekli yerden ısıtma sistemleri için tasarlanmış, teknoloji odaklı merkezi yönetim çözümüdür. Kompakt ve ergonomik yapısına entegre edilen WiFi teknolojisi sayesinde ısı kontrolünü tamamen özgürleştirir.",
               "İnternet bağlantısının olduğu her yerden telefon veya tablet aracılığıyla sisteminize bağlanabilir, anlık durumunu izleyebilir ve sıcaklık ayarlarınızı kolayca değiştirebilirsiniz."],
         features=["WiFi ile uzaktan yönetim", "Anlık durum izleme", "Kompakt ve ergonomik"]),
    dict(slug="tp-12-80-wifi-kontrol-panosu", cat="pano", name="TP-12-80 WiFi'li Kontrol Panosu",
         img="tp-12-80-wifi-kontrol-panosu", badge="WiFi",
         short="Büyük projeler için IoT tabanlı akıllı yönetim.",
         desc=["Geniş çaplı, çok bileşenli ve yüksek güç kapasitesi gerektiren yerden ısıtma ile iklimlendirme sistemleri için geliştirilmiş profesyonel bir akıllı yönetim merkezidir.",
               "WiFi bağlantısı sayesinde sisteminizin tüm detaylarını uzaktan izleyebilir, merkezi ve güvenli şekilde yönetebilirsiniz. Yoğun kullanım alanlarında dahi büyük ölçekli mekânların enerji verimliliğini kontrol altında tutar."],
         features=["IoT / WiFi ile merkezi yönetim", "Yüksek güç kapasitesi", "Isıtma ve iklimlendirme"]),
]

HOME_FEATURED = ["rexva-xt-308-220w-karbon-film", "hot-film-sh-308m-220w-karbon-film", "rexva-xt-306-165w-karbon-film",
                 "hot-film-sh-305-e-200w-karbon-film", "uth-2000-wifi-termostat", "uth-200-termostat",
                 "tp-06-50-wifi-kontrol-panosu", "klima-kontrol-panosu"]

BY_SLUG = {p["slug"]: p for p in PRODUCTS}
CAT_NAME = {c[0]: c[1] for c in CATEGORIES}
e = html.escape


def read(name):
    with open(os.path.join(PARTIALS, name), encoding="utf-8") as f:
        return f.read()


def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def wa_btn(r, loc, msg, label="WhatsApp'tan Yaz", cls="btn btn-wa wa-link"):
    return (f'<a class="{cls}" href="{WA}" target="_blank" rel="noopener" data-track="whatsapp" '
            f'data-loc="{loc}" data-msg="{e(msg)}"><svg><use href="#i-wa"/></svg>{label}</a>')


def call_btn(loc, label="Hemen Ara", cls="btn btn-call"):
    return f'<a class="{cls}" href="tel:{PHONE_TEL}" data-track="call" data-loc="{loc}"><svg><use href="#i-phone"/></svg>{label}</a>'


def head(r, title, desc, og_img, extra=""):
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#16110d">
<link rel="icon" href="{r}img/ikon.png">
<link rel="stylesheet" href="{r}assets/style.css">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{r}{og_img}">
<meta property="og:locale" content="tr_TR">
<!-- Dönüşüm takibi: heattan.com.tr ile aynı etiketler (GTM-N9CRWDSP + AW-18133483046).
     Arama/WhatsApp dönüşüm etiketleri assets/site.js içindeki CONFIG'de. -->
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-N9CRWDSP');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18133483046"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-18133483046');
</script>
<!-- Meta Pixel: PIXEL_ID girip yorumu kaldırın.
<script>
  !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
  document,'script','https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', 'PIXEL_ID');
  fbq('track', 'PageView');
</script>
-->
{extra}</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N9CRWDSP" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""


def header(r, active):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    nav = "".join([
        link(f"{r}index.html", "Anasayfa", "home"),
        link(f"{r}urunlerimiz/index.html", "Ürünlerimiz", "urunler"),
        link(f"{r}index.html#hizmetler", "Hizmetlerimiz", "hizmetler"),
        link(f"{r}index.html#iletisim", "İletişim", "iletisim"),
    ])
    return f"""{read('sprite.svg')}

<header class="top">
  <div class="wrap">
    <a class="logo" href="{r}index.html" aria-label="Heattan Isıtma Sistemleri"><img src="{r}img/logo.png" alt="Heattan Isıtma Sistemleri" width="260" height="75"></a>
    <nav class="menu" aria-label="Ana menü">{nav}</nav>
    <div class="top-phone">
      <a class="num" href="tel:{PHONE_TEL}" data-track="call" data-loc="header-num"><small>Hemen arayın</small>{PHONE_TXT}</a>
      {call_btn("header", "Ara")}
    </div>
  </div>
  <nav class="menu-m" aria-label="Menü">{nav}</nav>
</header>
"""


def footer(r, wa_msg):
    return f"""
<footer>
  <div class="wrap">
    <img src="{r}img/logo.png" alt="Heattan" width="104" height="30" loading="lazy">
    <span>© <span id="yil">2026</span> Heattan Isıtma Sistemleri · Yenidoğan, Rami Kışla Cd. No:69, Bayrampaşa / İstanbul</span>
  </div>
</footer>

{wa_btn(r, "fab", wa_msg, label="", cls="fab wa-link").replace('data-track', 'aria-label="WhatsApp\'tan yazın" data-track')}

<nav class="mbar" aria-label="Hızlı iletişim">
  {call_btn("mobile-bar")}
  {wa_btn(r, "mobile-bar", wa_msg, label="WhatsApp")}
</nav>

<script src="{r}assets/site.js" defer></script>
</body>
</html>
"""


def card(r, p, loc):
    url = f"{r}urunlerimiz/{p['slug']}/index.html"
    return f"""<article class="pcard">
  <a class="pimg{' light' if p.get('light') else ''}" href="{url}"><img src="{r}img/urunler/{p['img']}.jpg" alt="{e(p['name'])}" width="640" height="560" loading="lazy"><span class="tag">{e(p['badge'])}</span></a>
  <div class="pbody">
    <span class="pcat">{e(CAT_NAME[p['cat']])}</span>
    <h3><a href="{url}">{e(p['name'])}</a></h3>
    <p>{e(p['short'])}</p>
    <div class="pact">
      <a class="btn btn-ghost btn-sm" href="{url}">Detaylar</a>
      {wa_btn(r, loc, f"Merhaba, {p['name']} hakkında fiyat bilgisi almak istiyorum.", label="Fiyat Sor", cls="btn btn-wa btn-sm wa-link")}
    </div>
  </div>
</article>"""


def cta_band(r, loc, msg, title="Ücretsiz bilgi ve fiyat için hemen ulaşın",
             text="Alanınızın ölçüsünü ve zemin tipini paylaşın, size en uygun çözümü önerelim."):
    return f"""<section style="padding-top:0">
    <div class="wrap">
      <div class="cta">
        <h2>{e(title)}</h2>
        <p>{e(text)}</p>
        <a class="phone-big" href="tel:{PHONE_TEL}" data-track="call" data-loc="{loc}-num">{PHONE_TXT}</a>
        <div class="btn-row">
          {call_btn(loc)}
          {wa_btn(r, loc, msg)}
        </div>
      </div>
    </div>
  </section>"""


def build_home():
    r = ""
    cards = "\n".join(card(r, BY_SLUG[s], "home-urunler") for s in HOME_FEATURED)
    products = f"""  <section id="urunler">
    <div class="wrap">
      <div class="sec-head center">
        <span class="eyebrow">Ürünlerimiz</span>
        <h2>Karbon film, kablo, termostat ve kontrol panoları</h2>
        <p class="lead">Projenize uygun ürünü seçin, detayları inceleyin ya da tek tıkla fiyat sorun.</p>
      </div>
      <div class="pgrid">
{cards}
      </div>
      <div class="center" style="margin-top:28px"><a class="btn btn-ghost" href="urunlerimiz/index.html">Tüm ürünleri gör ({len(PRODUCTS)})</a></div>
    </div>
  </section>
"""
    main = read("home_main.html").replace("{{HOME_PRODUCTS}}", products)
    ld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Heattan Isıtma Sistemleri","url":"https://heattan.com.tr/","telephone":"+905342842623","email":"heattaninfo@gmail.com","foundingDate":"2018","address":{"@type":"PostalAddress","streetAddress":"Yenidoğan Mah., Rami Kışla Cd. No:69","postalCode":"34030","addressLocality":"Bayrampaşa","addressRegion":"İstanbul","addressCountry":"TR"}}
</script>
<link rel="preload" as="image" href="img/uygulama.jpg">
"""
    page = (head(r, "Heattan Yerden Isıtma | Karbon Film ve Yerden Isıtma, İstanbul",
                 "Heattan Isıtma Sistemleri: yerden ısıtma, karbon film ve akıllı termostat çözümleri. Ücretsiz bilgi için hemen arayın veya WhatsApp'tan yazın. 2018'den beri İstanbul.",
                 "img/uygulama.jpg", ld)
            + header(r, "home") + "\n<main>\n" + main + "</main>\n"
            + footer(r, "Merhaba, yerden ısıtma sistemleri hakkında bilgi almak istiyorum."))
    write("index.html", page)


def build_list():
    r = "../"
    chips = "".join(f'<a href="#{c[0]}">{e(c[1])}</a>' for c in CATEGORIES)
    sections = []
    for key, name, intro in CATEGORIES:
        items = "\n".join(card(r, p, "urunler-liste") for p in PRODUCTS if p["cat"] == key)
        sections.append(f"""  <section class="cat" id="{key}">
    <div class="wrap">
      <div class="sec-head">
        <h2>{e(name)}</h2>
        <p class="lead">{e(intro)}</p>
      </div>
      <div class="pgrid">
{items}
      </div>
    </div>
  </section>""")
    main = f"""<main>
  <section class="page-hero">
    <div class="wrap">
      <nav class="crumbs" aria-label="Konum"><a href="{r}index.html">Anasayfa</a><span>/</span>Ürünlerimiz</nav>
      <h1>Ürünlerimiz</h1>
      <p class="lead">Zemin altı ısıtıcı panellerle enerji verimli ısıtma. Karbon film yerden ısıtma sistemleri ince yapısı sayesinde parke ve laminat zemin altına kolayca uygulanır, homojen ısı dağılımı ve hızlı ısınma sağlar. Konut, ofis ve ticari alanlar için tüm ürünlerimizi aşağıda bulabilirsiniz.</p>
      <div class="btn-row">
        {call_btn("urunler-hero")}
        {wa_btn(r, "urunler-hero", "Merhaba, ürünleriniz hakkında fiyat bilgisi almak istiyorum.")}
      </div>
      <div class="chips">{chips}</div>
    </div>
  </section>
{chr(10).join(sections)}
  {cta_band(r, "urunler-cta", "Merhaba, ürünleriniz hakkında fiyat bilgisi almak istiyorum.", title="Hangi ürün size uygun? Birlikte seçelim")}
</main>
"""
    page = (head(r, "Ürünlerimiz | Heattan Yerden Isıtma Sistemleri",
                 "Karbon film yerden ısıtma, zemin ısıtıcı kablolar, termostatlar ve kontrol panoları. Fiyat için hemen arayın veya WhatsApp'tan yazın.",
                 "img/urunler/rexva-xt-308-220w.jpg")
            + header(r, "urunler") + main
            + footer(r, "Merhaba, ürünleriniz hakkında fiyat bilgisi almak istiyorum."))
    write("urunlerimiz/index.html", page)


def build_detail(p):
    r = "../../"
    msg = f"Merhaba, {p['name']} hakkında fiyat bilgisi almak istiyorum."
    cat = CAT_NAME[p["cat"]]
    related = [q for q in PRODUCTS if q["cat"] == p["cat"] and q["slug"] != p["slug"]][:4]
    if len(related) < 4:
        related += [q for q in PRODUCTS if q["cat"] != p["cat"]][: 4 - len(related)]
    desc = "\n".join(f"<p>{e(t)}</p>" for t in p["desc"])
    feats = "\n".join(f"<li>{e(f)}</li>" for f in p["features"])
    extra = ""
    if p.get("specs"):
        rows = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in p["specs"])
        extra += f'<h2>Teknik özellikler</h2>\n<table class="specs">{rows}</table>\n'
    if p.get("details"):
        extra += "<h2>Özellikler</h2>\n<ul class=\"dlist\">" + "".join(f"<li>{e(d)}</li>" for d in p["details"]) + "</ul>\n"
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Product", "name": p["name"], "category": cat,
        "description": " ".join(p["desc"]), "brand": {"@type": "Brand", "name": p["name"].split()[0]},
    }, ensure_ascii=False)
    main = f"""<main>
  <section class="detail">
    <div class="wrap">
      <nav class="crumbs" aria-label="Konum"><a href="{r}index.html">Anasayfa</a><span>/</span><a href="../index.html">Ürünlerimiz</a><span>/</span><a href="../index.html#{p['cat']}">{e(cat)}</a></nav>
      <div class="dgrid">
        <div class="dimg{' light' if p.get('light') else ''}"><img src="{r}img/urunler/{p['img']}.jpg" alt="{e(p['name'])}" width="640" height="560" fetchpriority="high"><span class="tag">{e(p['badge'])}</span></div>
        <div>
          <span class="eyebrow">{e(cat)}</span>
          <h1>{e(p['name'])}</h1>
          <p class="lead">{e(p['short'])}</p>
          <ul class="checks">
{feats}
          </ul>
          <div class="btn-row">
            {call_btn("urun-detay", "Fiyat İçin Ara")}
            {wa_btn(r, "urun-detay", msg, label="WhatsApp'tan Fiyat Al")}
          </div>
          <p class="hero-note">Keşif, projelendirme ve montaj hizmetiyle birlikte · {PHONE_TXT}</p>
        </div>
      </div>
      <div class="dtext card">
        <h2>Ürün hakkında</h2>
        {desc}
        {extra}
      </div>
    </div>
  </section>
  <section class="alt">
    <div class="wrap">
      <div class="sec-head"><h2>Benzer ürünler</h2></div>
      <div class="pgrid">
{chr(10).join(card(r, q, "urun-benzer") for q in related)}
      </div>
    </div>
  </section>
  <div style="height:56px"></div>
  {cta_band(r, "urun-cta", msg, title=f"{p['name']} için fiyat alın", text="Alanınızın ölçüsünü paylaşın, ürün ve montaj dahil teklifimizi iletelim.")}
</main>
"""
    page = (head(r, f"{p['name']} | Heattan",
                 f"{p['name']}: {p['short']} Fiyat ve montaj bilgisi için hemen arayın veya WhatsApp'tan yazın.",
                 f"img/urunler/{p['img']}.jpg",
                 f'<script type="application/ld+json">{ld}</script>\n')
            + header(r, "urunler") + main + footer(r, msg))
    write(f"urunlerimiz/{p['slug']}/index.html", page)


if __name__ == "__main__":
    build_home()
    build_list()
    for p in PRODUCTS:
        build_detail(p)
    print(f"OK: anasayfa, ürünlerimiz ve {len(PRODUCTS)} ürün detay sayfası üretildi -> {OUT}")
