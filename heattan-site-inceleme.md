# heattan.com.tr İnceleme Raporu

Tarih: 13 Ekim 2026. Klasörde kaynak kod olmadığı için canlı site incelendi (WordPress 7.1 + Elementor, "Reland" emlak teması).

## 🔴 Kritik (önce bunlar)

1. **Temanın demo içeriği Google'a açık.** Site haritasındaki 79 adresin yaklaşık 75'i temanın İngilizce emlak demosu: `/home-three/`, `/home-four/`… `/team-details/`, 26 proje sayfası (`/project/paragon-hotel-concept/` vb.), "Hello world" ve emlak blog yazıları, `architecture`, `real-estate` kategorileri/etiketleri, `new-york-city`, `santa-monica` konumları. Hepsi 200 dönüyor ve indekslenebilir. Bu, Google'ın siteyi "emlak sitesi" sanmasına ve gerçek 4 sayfanın değerinin düşmesine yol açar.
   → Demo sayfa/yazı/projeleri silin (veya taslağa alın), AIOSEO'da "project", kategori, etiket haritalarını kapatın, silinenleri Search Console'dan kaldırma isteğiyle temizleyin.

2. **Yanlış iletişim bilgileri.** Sayfada temadan kalma `mailto:relandgroup@mail.com` bağlantısı var. Footer'da "Heatten Hakkında" (yazım hatası), "Copyright © Heattan 2024. All Rights Reserved" (İngilizce ve eski yıl). Telefon bağlantısı `tel:+90 (534) 284 26 23` boşluk/parantezli; `tel:+905342842623` olmalı.

3. **Karışık içerik (HTTP/HTTPS) hatası.** Logo ve `base-desktop.css` `http://` ile yükleniyor; tarayıcı CSS dosyasını **engelliyor**, yani masaüstü stilleri bir kısmı hiç yüklenmiyor olabilir. Ayrıca `http://heattan.com.tr` HTTPS'e yönlenmiyor (200 dönüyor).
   → WordPress Ayarlar > Genel'de adresleri `https://` yapın, "Better Search Replace" ile veritabanında `http://heattan.com.tr` → `https://heattan.com.tr` değiştirin, Elementor > Araçlar > "CSS'i yeniden oluştur", sunucuda (Plesk) HTTP→HTTPS 301 yönlendirmesini açın.

4. **Gerçek kullanıcılarda sayfa yavaş.** Google'ın gerçek kullanıcı verisinde (CrUX) mobil LCP **7,0 sn** (iyi sınırı 2,5 sn). Sunucu ilk yanıtı ~1–1,2 sn (sayfa önbelleği yok). Sayfada 50 script, ~30 CSS dosyası, 3 farklı Google Font ailesi (Roboto ve Roboto Slab'ın tüm 18 ağırlığı) yükleniyor.
   → LiteSpeed Cache eklentisini kurun (sunucu zaten LiteSpeed): sayfa önbelleği, CSS/JS birleştirme-erteleme, görsel WebP ve lazy-load. Elementor'da Google Fonts'u kapatıp yalnız kullanılan 1-2 fontu yerel yükleyin. Kullanılmayan eklentileri (Instagram Feed, Mailchimp) kaldırın.

5. **Güvenlik ve bakım.** PHP **7.4** (2022'den beri desteksiz) — Plesk'ten 8.2/8.3'e geçin. `wp-json/wp/v2/users` yönetici kullanıcı adını (`heattanadmin`) herkese gösteriyor, `xmlrpc.php` açık, `readme.html` erişilebilir. İletişim formunda reCAPTCHA/spam koruması görünmüyor.
   → PHP'yi güncelleyin, bir güvenlik eklentisiyle (ör. Wordfence/Solid Security) kullanıcı listelemeyi ve XML-RPC'yi kapatın, formlara Cloudflare Turnstile veya reCAPTCHA ekleyin, yönetici şifresini güçlü + 2FA yapın.

## 🟠 Önemli (SEO ve içerik)

6. **Hiçbir sayfada H1 başlık yok.** Ana sayfa, Ürünler, Hizmetler, İletişim'de H1 bulunmuyor. Her sayfaya anahtar kelimeli tek bir H1 ekleyin (ör. "İstanbul Yerden Isıtma ve Karbon Film Isıtma Sistemleri").
7. **Meta açıklamalar otomatik ve bozuk.** Ana sayfa açıklaması "…sunuyoruz. İncele İncele MODERN ISITMA…" diye buton metinlerini içeriyor; İletişim sayfasınınki sadece "HEMEN İLETİŞİM". AIOSEO'da her sayfaya 150–160 karakterlik elle yazılmış açıklama girin. Site adı "Yerden Isıtma Sistemleri -" (sonunda tire) → "Heattan Isıtma Sistemleri" yapın.
8. **İçerik çok ince.** Ana sayfa ~290, Hizmetler ~70, İletişim ~50 kelime. Hizmetler sayfası sadece başlık listesi. Ürünler sayfası (~940 kelime) en iyisi. Öneriler: her hizmete ayrı sayfa (Karbon film, Kablolu ısıtma, Termostat, Projelendirme), "m² fiyatı / tüketim / montaj süresi" gibi soruları cevaplayan SSS bölümü, gerçek uygulama fotoğraflarıyla referans/proje galerisi, "Hakkımızda" sayfası (şu an `/hakkimizda/` 404).
9. **Yerel SEO eksik.** Schema'da işletme adı "Yerden Isıtma Sistemleri", tipi genel "Organization", adres/telefon yok. AIOSEO > Yerel SEO veya Schema ile `LocalBusiness`/`HVACBusiness` + adres, telefon, çalışma saatleri ekleyin. Google İşletme Profili yoksa açın ve aynı adres/telefonu kullanın. İletişim sayfasında adres, telefon, harita ve çalışma saatleri yok (sadece form var).
10. **404 sayfası İngilizce** ("The page you are looking for…", "Back to home"). Türkçeleştirin.
11. **Sosyal paylaşım görseli** 2560×734 logo PNG (82 KB). 1200×630 bir kapak görseli belirleyin. `og:type` ana sayfa için "website" olmalı.

## 🟡 Tasarım, mobil ve erişilebilirlik

12. **Mobilde logo okunmuyor.** Siyah logo koyu hero görselinin üstünde neredeyse kayboluyor. Koyu zeminde beyaz logo versiyonu kullanın.
13. **"İNCELE" butonu düşük kontrastlı** (koyu altın zemin üstünde soluk yazı); Lighthouse da kontrast hatası veriyor. Hero'da asıl hedef olan **"Ücretsiz Keşif İste" / "Hemen Ara"** gibi net bir çağrı butonu daha işe yarar.
14. **Mobilde boşluklar fazla.** Hizmet kutuları arasında ve "Hakkımızda" metninden sonra büyük boş alanlar var; ana sayfa mobilde çok uzun. Elementor'da mobil padding/margin değerlerini küçültün, hizmetleri 2'li grid yapın.
15. **Hizmet ikonları alakasız** (yaprak, avize, kalp ritmi, kilit — tema ikonları). Isıtma/termostat/zemin ikonlarıyla değiştirin.
16. **WhatsApp widget'ı İngilizce** ("Hi Hello 👋", "Scan the code", "Powered by Joinchat"). Joinchat ayarlarından Türkçeleştirin.
17. **Erişilebilirlik:** adı olmayan butonlar (menü/hamburger) ve linkler, sırasız başlık seviyeleri. Lighthouse erişilebilirlik puanı 86.
18. **Menüde "İletişim" yok** (sadece Anasayfa, Ürünlerimiz, Hizmetlerimiz). Ekleyin.

## 🟢 Küçük / iyi durumda olanlar

- HTTPS sertifikası, www→ana alan adı yönlendirmesi, Brotli sıkıştırma, statik dosya önbelleği (7 gün), `lang="tr"`, viewport, canonical ve robots.txt düzgün.
- Google Ads etiketi ve Site Kit kurulu. Çerez onay (KVKK) bandı görünmüyor; Google Ads çerezleri izinsiz yükleniyor. Bir çerez onay eklentisi (ör. Complianz / CookieYes) ekleyip Consent Mode v2'ye bağlayın.
- Lighthouse (mobil): SEO 100, Erişilebilirlik 86, En İyi Uygulamalar 54. SEO'nun 100 çıkması yanıltıcı; teknik etiketler var ama içerik ve demo sayfa sorunları puana yansımıyor.

## Önerilen sıra

1. Demo içeriği sil + site haritasını temizle (1-2 saat)
2. HTTP→HTTPS düzeltmesi, yanlış e-posta, footer metinleri (1 saat)
3. PHP güncelle, güvenlik eklentisi, form spam koruması (1 saat)
4. LiteSpeed Cache + font sadeleştirme (2-3 saat)
5. H1, meta açıklamalar, LocalBusiness schema, İletişim sayfası (yarım gün)
6. Hizmet alt sayfaları, SSS, referans galerisi (süreklilik isteyen iş)
