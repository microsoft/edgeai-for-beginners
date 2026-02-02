# Bölüm 02: Küçük Dil Modeli Temelleri

Bu kapsamlı temel bölüm, Küçük Dil Modelleri (SLM) üzerine teorik prensipler, pratik uygulama stratejileri ve üretime hazır dağıtım çözümlerini içeren önemli bir keşif sunar. Bölüm, modern verimli yapay zeka mimarilerini ve bunların çeşitli hesaplama ortamlarında stratejik dağıtımını anlamak için kritik bilgi tabanını oluşturur.

## Bölüm Yapısı ve İlerlemeli Öğrenme Çerçevesi

### **[Bölüm 1: Microsoft Phi Model Ailesi Temelleri](./01.PhiFamily.md)**
Açılış bölümü, Microsoft'un çığır açan Phi model ailesini tanıtarak, kompakt ve verimli modellerin, önemli ölçüde azaltılmış hesaplama gereksinimlerini korurken nasıl olağanüstü performans sergilediğini gösterir. Bu temel bölüm şunları kapsar:

- **Tasarım Felsefesi Evrimi**: Phi-1'den Phi-4'e kadar Microsoft'un Phi ailesinin gelişiminin kapsamlı bir keşfi, "ders kitabı kalitesinde" eğitim metodolojisi ve çıkarım zamanı ölçeklendirme vurgusu
- **Verimlilik-Öncelikli Mimari**: Parametre verimliliği optimizasyonu, çok modlu entegrasyon yetenekleri ve CPU, GPU ve uç cihazlar için donanım odaklı optimizasyonların detaylı analizi
- **Özel Yetenekler**: Matematiksel görevler için Phi-4-mini-reasoning, görsel-dil işleme için Phi-4-multimodal ve Windows 11'e entegre dağıtım için Phi-3-Silica gibi alanlara özgü varyantların derinlemesine incelemesi

Bu bölüm, model verimliliği ve yeteneklerin yenilikçi eğitim metodolojileri ve mimari optimizasyon yoluyla bir arada var olabileceği temel prensibi ortaya koyar.

### **[Bölüm 2: Qwen Model Ailesi Temelleri](./02.QwenFamily.md)**
İkinci bölüm, Alibaba'nın kapsamlı açık kaynak yaklaşımına geçiş yaparak, şeffaf ve erişilebilir modellerin, dağıtım esnekliğini korurken rekabetçi performansa nasıl ulaşabileceğini gösterir. Ana odak noktaları şunlardır:

- **Açık Kaynak Mükemmelliği**: Qwen 1.0'dan Qwen3'e kadar Qwen evriminin kapsamlı bir keşfi, büyük ölçekli eğitim (36 trilyon token) ve 119 dilde çok dilli yetenekler
- **Gelişmiş Akıl Yürütme Mimarisi**: Qwen3'ün yenilikçi "düşünme modu" yetenekleri, uzman karışımı uygulamaları ve kodlama (Qwen-Coder) ve matematik (Qwen-Math) için özel varyantların detaylı incelemesi
- **Ölçeklenebilir Dağıtım Seçenekleri**: Mobil cihazlardan kurumsal kümelere kadar dağıtım senaryolarını mümkün kılan 0.5B'den 235B parametreye kadar parametre aralıklarının derinlemesine analizi

Bu bölüm, açık kaynak erişilebilirliği aracılığıyla yapay zeka teknolojisinin demokratikleşmesini vurgularken rekabetçi performans özelliklerini korur.

### **[Bölüm 3: Gemma Model Ailesi Temelleri](./03.GemmaFamily.md)**
Üçüncü bölüm, Google'ın araştırma odaklı geliştirme yoluyla erişilebilir ancak güçlü yapay zeka yetenekleri sunan açık kaynaklı çok modlu yapay zeka yaklaşımını inceler. Bu bölüm şunları kapsar:

- **Araştırma Odaklı Yenilik**: Per-Layer Embeddings (PLE) teknolojisi ve mobil öncelikli optimizasyon stratejileri içeren Gemma 3 ve Gemma 3n mimarilerinin kapsamlı incelemesi
- **Çok Modlu Mükemmellik**: Görsel-dil entegrasyonu, ses işleme yetenekleri ve kapsamlı yapay zeka deneyimlerini mümkün kılan işlev çağırma özelliklerinin detaylı keşfi
- **Mobil Öncelikli Mimari**: 2B-4B parametre performansını yalnızca 2-3GB bellek kullanımıyla sunan Gemma 3n'nin devrim niteliğindeki verimlilik başarılarının derinlemesine analizi

Bu bölüm, ileri düzey araştırmaların pratik, erişilebilir yapay zeka çözümlerine nasıl dönüştürülebileceğini gösterir ve yeni uygulama kategorilerini mümkün kılar.

### **[Bölüm 4: BitNET Model Ailesi Temelleri](./04.BitNETFamily.md)**
Dördüncü bölüm, ultra verimli yapay zeka dağıtımının sınırını temsil eden Microsoft'un devrim niteliğindeki 1-bit kuantizasyon yaklaşımını sunar. Bu ileri düzey bölüm şunları kapsar:

- **Devrim Niteliğinde Kuantizasyon**: {-1, 0, +1} üçlü ağırlıklar kullanarak 1.58-bit kuantizasyonun kapsamlı keşfi, %55-82 enerji tasarrufu ile 1.37x ila 6.17x hız artışları
- **Optimize Edilmiş Çıkarım Çerçevesi**: [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet) adresindeki bitnet.cpp uygulaması, özel çekirdekler ve çapraz platform optimizasyonlarının detaylı incelemesi
- **Sürdürülebilir Yapay Zeka Liderliği**: Çevresel faydalar, demokratikleşmiş dağıtım yetenekleri ve aşırı verimlilikle mümkün kılınan yeni uygulama senaryolarının derinlemesine analizi

Bu bölüm, devrim niteliğindeki kuantizasyon tekniklerinin yapay zeka verimliliğini önemli ölçüde artırırken rekabetçi performansı nasıl koruyabileceğini gösterir.

### **[Bölüm 5: Microsoft Mu Modeli Temelleri](./05.mumodel.md)**
Beşinci bölüm, Windows cihazlarında yerinde dağıtım için özel olarak tasarlanmış Microsoft'un çığır açan Mu modelini inceler. Bu özel bölüm şunları kapsar:

- **Cihaz-Öncelikli Mimari**: Windows 11 cihazlarına entegre edilmiş Microsoft'un özel yerinde modelinin kapsamlı keşfi
- **Sistem Entegrasyonu**: Yerel uygulama yoluyla yapay zekanın sistem işlevselliğini nasıl artırabileceğini gösteren Windows 11 entegrasyonunun detaylı analizi
- **Gizlilik Koruyucu Tasarım**: Kullanıcı verilerini cihazda tutan çevrimdışı çalışma, yerel işleme ve gizlilik öncelikli mimarinin derinlemesine incelemesi

Bu bölüm, özel modellerin Windows 11 işletim sistemi işlevselliğini gizlilik ve performansı koruyarak nasıl artırabileceğini gösterir.

### **[Bölüm 6: Phi-Silica Temelleri](./06.phisilica.md)**
Son bölüm, Microsoft'un Windows 11 için NPU donanımlı Copilot+ PC'lere entegre edilmiş ultra verimli dil modeli Phi-Silica'yı inceler. Bu ileri düzey bölüm şunları kapsar:

- **Olağanüstü Verimlilik Ölçütleri**: Sadece 1.5 watt güç tüketimiyle saniyede 650 token sunan Phi-Silica'nın dikkat çekici performans yeteneklerinin kapsamlı analizi
- **NPU Optimizasyonu**: Windows 11 Copilot+ PC'lerdeki Neural Processing Units için tasarlanmış özel mimarinin detaylı keşfi
- **Geliştirici Entegrasyonu**: Windows App SDK entegrasyonu, prompt mühendisliği teknikleri ve Windows 11 uygulamalarında Phi-Silica'nın uygulanması için en iyi uygulamaların derinlemesine incelemesi

Bu bölüm, özel model mimarilerinin özel sinir donanımıyla birleştirilerek Windows 11 tüketici cihazlarında olağanüstü yapay zeka performansı sunabileceğini gösterir.

## Kapsamlı Öğrenme Çıktıları

Bu temel bölümü tamamladıktan sonra okuyucular şunlarda ustalık kazanacaktır:

1. **Mimari Anlayış**: Farklı SLM tasarım felsefelerinin ve bunların dağıtım senaryoları üzerindeki etkilerinin derinlemesine kavranması
2. **Performans-Verimlilik Dengesi**: Hesaplama kısıtlamaları ve performans gereksinimlerine dayalı uygun model mimarilerini seçme konusunda stratejik karar verme yetenekleri
3. **Dağıtım Esnekliği**: Özel optimizasyon (Phi), açık kaynak erişilebilirliği (Qwen), araştırma odaklı yenilik (Gemma) ve devrim niteliğindeki verimlilik (BitNET) arasındaki ödünleşimleri anlama
4. **Geleceğe Hazır Perspektif**: Verimli yapay zeka mimarisindeki ortaya çıkan eğilimler ve bunların gelecek nesil dağıtım stratejileri üzerindeki etkileri hakkında içgörüler

## Pratik Uygulama Odaklılık

Bölüm, baştan sona güçlü bir pratik odaklanma sağlar ve şunları içerir:

- **Tam Kod Örnekleri**: Her model ailesi için üretime hazır uygulama örnekleri, ince ayar prosedürleri, optimizasyon stratejileri ve dağıtım yapılandırmaları
- **Kapsamlı Karşılaştırmalar**: Farklı model mimarileri arasında detaylı performans karşılaştırmaları, verimlilik ölçütleri, yetenek değerlendirmeleri ve kullanım senaryosu optimizasyonu
- **Kurumsal Güvenlik**: Üretim düzeyinde güvenlik uygulamaları, izleme stratejileri ve güvenilir dağıtım için en iyi uygulamalar
- **Çerçeve Entegrasyonu**: Hugging Face Transformers, vLLM, ONNX Runtime ve özel optimizasyon araçları gibi popüler çerçevelerle entegrasyon için pratik rehberlik

## Stratejik Teknoloji Yol Haritası

Bölüm, ileriye dönük analizle sona erer:

- **Mimari Evrim**: Verimli model tasarımı ve optimizasyondaki ortaya çıkan eğilimler
- **Donanım Entegrasyonu**: Özel yapay zeka hızlandırıcılarındaki ilerlemeler ve bunların dağıtım stratejileri üzerindeki etkisi
- **Ekosistem Gelişimi**: Farklı model aileleri arasında standartlaştırma çabaları ve birlikte çalışabilirlik iyileştirmeleri
- **Kurumsal Benimseme**: Organizasyonel yapay zeka dağıtım planlaması için stratejik değerlendirmeler

## Gerçek Dünya Uygulama Senaryoları

Her bölüm, pratik uygulamaların kapsamlı bir şekilde ele alınmasını sağlar:

- **Mobil ve Uç Hesaplama**: Kaynak kısıtlı ortamlar için optimize edilmiş dağıtım stratejileri
- **Kurumsal Uygulamalar**: İş zekası, otomasyon ve müşteri hizmetleri için ölçeklenebilir çözümler
- **Eğitim Teknolojisi**: Kişiselleştirilmiş öğrenme ve içerik üretimi için erişilebilir yapay zeka
- **Küresel Dağıtım**: Çok dilli ve kültürler arası yapay zeka uygulamaları

## Teknik Mükemmellik Standartları

Bölüm, üretime hazır uygulamayı şu şekilde vurgular:

- **Optimizasyon Ustalığı**: İleri düzey kuantizasyon teknikleri, çıkarım optimizasyonu ve kaynak yönetimi
- **Performans İzleme**: Kapsamlı ölçüm toplama, uyarı sistemleri ve performans analitiği
- **Güvenlik Uygulaması**: Kurumsal düzeyde güvenlik önlemleri, gizlilik koruması ve uyumluluk çerçeveleri
- **Ölçeklenebilirlik Planlaması**: Artan hesaplama talepleri için yatay ve dikey ölçeklendirme stratejileri

Bu temel bölüm, ileri düzey SLM dağıtım stratejileri için gerekli olan hem teorik anlayışı hem de pratik yetenekleri sağlayarak başarılı uygulama için gerekli olan temel ön koşul olarak hizmet eder. Kapsamlı kapsama alanı, okuyucuların bilinçli mimari kararlar almasını ve belirli organizasyonel gereksinimlerini karşılayan sağlam, verimli yapay zeka çözümleri uygulamasını sağlarken gelecekteki teknolojik gelişmelere hazırlıklı olmalarını sağlar.

Bölüm, modern SLM mimarilerinin operasyonel verimlilik, maliyet etkinliği ve çevresel sürdürülebilirliği korurken olağanüstü performans sunabileceğini vurgulayarak ileri düzey yapay zeka araştırmaları ile pratik dağıtım gerçeklikleri arasındaki boşluğu doldurur.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.