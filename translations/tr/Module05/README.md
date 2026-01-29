# Bölüm 05 : SLMOps - Küçük Dil Modeli Operasyonlarına Kapsamlı Bir Rehber

## Genel Bakış

SLMOps (Küçük Dil Modeli Operasyonları), verimlilik, maliyet etkinliği ve uç bilişim yeteneklerini önceliklendiren devrim niteliğinde bir yapay zeka dağıtım yaklaşımını temsil eder. Bu kapsamlı rehber, temel kavramları anlamaktan üretime hazır dağıtımları uygulamaya kadar SLM operasyonlarının tüm yaşam döngüsünü kapsar.

---

## [Bölüm 1: SLMOps'a Giriş](./01.IntroduceSLMOps.md)

**Uçta Yapay Zeka Operasyonlarını Değiştirmek**

Bu temel bölüm, geleneksel büyük ölçekli yapay zeka operasyonlarından Küçük Dil Modeli Operasyonlarına (SLMOps) geçişi tanıtır. SLMOps'un, yapay zekayı ölçekli bir şekilde dağıtırken maliyet etkinliği ve gizlilik uyumluluğunu nasıl koruduğunu keşfedeceksiniz.

**Öğrenecekleriniz:**
- Modern yapay zeka stratejisinde SLMOps'un ortaya çıkışı ve önemi
- SLM'lerin performans ve kaynak verimliliği arasındaki boşluğu nasıl doldurduğu
- Akıllı kaynak yönetimi ve gizlilik odaklı mimari gibi temel operasyonel prensipler
- Gerçek dünya uygulama zorlukları ve çözümleri
- Stratejik iş etkisi ve rekabet avantajları

**Ana Fikir:** SLMOps, gelişmiş dil işleme yeteneklerini sınırlı teknik altyapıya sahip organizasyonlara erişilebilir hale getirerek daha hızlı geliştirme döngüleri ve daha öngörülebilir operasyonel maliyetler sağlar.

---

## [Bölüm 2: Model Damıtma - Teoriden Pratiğe](./02.SLMOps-Distillation.md)

**Bilgi Transferi ile Verimli Modeller Oluşturmak**

Model damıtma, daha büyük modellerin performansını koruyan daha küçük ve verimli modeller oluşturmak için temel bir tekniktir. Bu bölüm, büyük öğretmen modellerden kompakt öğrenci modellere bilgi transferi sağlayan damıtma iş akışlarını uygulamak için kapsamlı bir rehber sunar.

**Öğrenecekleriniz:**
- Model damıtmanın temel kavramları ve faydaları
- İki aşamalı damıtma süreci: sentetik veri üretimi ve öğrenci modeli eğitimi
- DeepSeek V3 ve Phi-4-mini gibi en son modelleri kullanarak pratik uygulama stratejileri
- Azure ML damıtma iş akışları ile uygulamalı örnekler
- Hiperparametre ayarlama ve değerlendirme stratejileri için en iyi uygulamalar
- Maliyet ve performans iyileştirmelerini gösteren gerçek dünya vaka çalışmaları

**Ana Fikir:** Model damıtma, organizasyonların çıkarım süresinde %85 azalma ve bellek gereksinimlerinde %95 düşüş sağlarken, orijinal model doğruluğunun %92'sini korumasını mümkün kılar, gelişmiş yapay zeka yeteneklerini pratik olarak uygulanabilir hale getirir.

---

## [Bölüm 3: İnce Ayar - Modelleri Belirli Görevler İçin Özelleştirme](./03.SLMOps-Finetuing.md)

**Önceden Eğitilmiş Modelleri Benzersiz Gereksinimlerinize Uygun Hale Getirmek**

İnce ayar, genel amaçlı modelleri belirli kullanım alanlarınıza ve alanlarınıza uygun özel çözümlere dönüştürür. Bu bölüm, temel parametre ayarından LoRA ve QLoRA gibi verimli model özelleştirme tekniklerine kadar her şeyi kapsar.

**Öğrenecekleriniz:**
- İnce ayar metodolojileri ve uygulamaları hakkında kapsamlı bir genel bakış
- Farklı ince ayar türleri: tam ince ayar, parametre verimli ince ayar (PEFT) ve görev odaklı yaklaşımlar
- Microsoft Olive kullanarak uygulamalı örneklerle ince ayar uygulaması
- Çoklu adaptör eğitimi ve hiperparametre optimizasyonu gibi ileri teknikler
- Veri hazırlığı, eğitim yapılandırması ve kaynak yönetimi için en iyi uygulamalar
- Başarılı ince ayar projeleri için yaygın zorluklar ve kanıtlanmış çözümler

**Ana Fikir:** Microsoft Olive gibi araçlarla ince ayar yapmak, organizasyonların önceden eğitilmiş modelleri belirli ihtiyaçlara verimli bir şekilde uyarlamasını sağlarken performans ve kaynak kısıtlamalarını optimize eder, gelişmiş yapay zekayı çeşitli uygulamalarda erişilebilir hale getirir.

---

## [Bölüm 4: Dağıtım - Üretime Hazır Model Uygulaması](./04.SLMOps.Deployment.md)

**İnce Ayarlı Modelleri Foundry Local ile Üretime Taşımak**

Son bölüm, model dönüştürme, kuantizasyon ve üretim yapılandırmasını kapsayan kritik dağıtım aşamasına odaklanır. İnce ayarlı kuantize edilmiş modelleri Foundry Local kullanarak optimal performans ve kaynak kullanımı için nasıl dağıtacağınızı öğreneceksiniz.

**Öğrenecekleriniz:**
- Tam ortam kurulumu ve araç yükleme prosedürleri
- Farklı dağıtım senaryoları için model dönüştürme ve kuantizasyon teknikleri
- Model spesifik optimizasyonlarla Foundry Local dağıtım yapılandırması
- Performans kıyaslama ve kalite doğrulama metodolojileri
- Yaygın dağıtım sorunlarını giderme ve optimizasyon stratejileri
- Üretim izleme ve bakım için en iyi uygulamalar

**Ana Fikir:** Kuantizasyon teknikleriyle doğru dağıtım yapılandırması, model kalitesini korurken %75'e varan boyut azaltımı sağlar ve çeşitli donanım yapılandırmalarında verimli üretim dağıtımları mümkün kılar.

---

## Başlarken

Bu rehber, temel kavramları anlamaktan üretime hazır dağıtımları uygulamaya kadar SLMOps yolculuğunuzu tamamlamanız için tasarlanmıştır. Her bölüm bir öncekini temel alarak hem teorik anlayış hem de pratik uygulama becerileri sunar.

İster model dağıtımını optimize etmek isteyen bir veri bilimci, ister yapay zeka operasyonlarını uygulayan bir DevOps mühendisi, ister organizasyonunuz için SLMOps'u değerlendiren bir teknik lider olun, bu kapsamlı rehber Küçük Dil Modeli Operasyonlarını başarıyla uygulamak için gereken bilgi ve araçları sağlar.

**Başlamaya hazır mısınız?** SLMOps'un temel prensiplerini anlamak ve sonraki bölümlerde ele alınan ileri uygulama teknikleri için temel oluşturmak için Bölüm 1 ile başlayın.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.