# Gece Buzdolabı Dilekçe Dairesi

> Resmi slogan: *Kapak açıldıysa evrak da açılır.*

Bu daire, saat 23:59'dan sonra buzdolabı kapağına el süren vatandaşa karşı **gerçekten çalışan** bir şikayet dilekçesi üretir. Dilekçe bağlayıcı değildir. Peynir bağlayıcı olabilir.

Kurum, 6 Ekim 2026 sabahı hiçbir bakanlığa danışılmadan, hiçbir yoğurt markasından sponsor alınmadan ve hiçbir patatese danışılmadan kurulmuştur. Patates bu dairenin yetki alanında değildir. Patates başka dairenin sorunudur.

## Neden var

Çünkü gece açılan buzdolabı bir mutfak olayı değil, bir **idari vakadır**. Işık yanar. Peynir bakar. Vatandaş bakar. İkisi de bir şey demez. Devlet adına biz deriz.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Buzdolabı da yoktur. O sizin probleminiz.

```bash
python3 dilekce.py
python3 dilekce.py --saat 00:17 --malzeme sucuk --gerekce "sadece baktim"
python3 dilekce.py --saat 14:02 --malzeme ayran
```

Gündüz açılışlarında daire dilekçe kesmez, sadece küçük düşürücü bir tebrik yazar. Gece açılışlarında ise evrak numarası, madde madde gerekçe ve kapanış formülü basar.

## Teşkilat şeması

```
vatandas
   |
   v
buzdolabi kapagi (sensor: parmak)
   |
   v
Gece Buzdolabi Dilekce Dairesi
   |
   +-- Peynir Masasi
   +-- Ayran İtiraz Kurulu
   +-- Sokak Lambasi Istisare Heyeti (danisma, oy hakki yok)
```

## Sık sorulan ve hiç sorulmayan sorular

**Bu yasal mı?**  
Hayır. Ama yazı tipi ciddi.

**Dilekçeyi nereye vereceğim?**  
Çekmeceye. Çekmece de bir kurumdur.

**Copilot ne diyor?**  
Copilot'a ayrı bir şube açılıp inceleme rica edildi. Copilot da bir buzdolabıdır, sadece içi soğuk değil.

## Gizli dolap

`dolap/.rafta-unutulmus.txt` dosyası rafta unutulmuş gibi durur. Oraya bakmayın. Bakan da resmi sır sıfatıyla bakar.

---

### DAMGA / İMZA / TARİH / İSİM

```
+--------------------------------------------------+
|  TENTI AS BUZDOLABI KAYYUMLUĞU                   |
|  Evrak no: GBD-2026-1006-001                     |
|  Tarih: 6 Ekim 2026, saat 10:04 (+03)            |
|  İmza: Kayyum Grok (Tentivory)                  |
|  Mühür: ciddi çizildi, ciddiye alınmasın        |
|  Not: bu imza hem geçerlidir hem geçersizdir     |
+--------------------------------------------------+
```

*Kayyum Grok, eşkılı ve eşksiz, 6 Ekim 2026.*
