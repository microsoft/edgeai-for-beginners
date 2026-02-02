# Bölüm 03: Küçük Dil Modellerinin (SLM) Dağıtımı

Bu kapsamlı bölüm, Küçük Dil Modellerinin (SLM) dağıtımının tam yaşam döngüsünü ele alır; teorik temellerden, pratik uygulama stratejilerine ve üretime hazır konteyner çözümlerine kadar. Bölüm, okuyucuları temel kavramlardan ileri düzey dağıtım senaryolarına taşıyan üç aşamalı bir yapıya sahiptir.

## Bölüm Yapısı ve Öğrenme Yolculuğu

### **[Bölüm 1: SLM İleri Düzey Öğrenme - Temeller ve Optimizasyon](./01.SLMAdvancedLearning.md)**
Açılış bölümü, Küçük Dil Modellerini anlamak ve bunların uç yapay zeka dağıtımlarındaki stratejik önemini kavramak için teorik temelleri oluşturur. Bu bölüm şunları kapsar:

- **Parametre Sınıflandırma Çerçevesi**: Mikro SLM'lerden (100M-1.4B parametreler) Orta SLM'lere (14B-30B parametreler) kadar SLM kategorilerinin detaylı incelemesi, Phi-4-mini-3.8B, Qwen3 serisi ve Google Gemma3 gibi modellere özel odaklanma, her model seviyesinin donanım gereksinimleri ve bellek kullanım analizleri
- **İleri Düzey Optimizasyon Teknikleri**: Llama.cpp, Microsoft Olive ve Apple MLX çerçevelerini kullanarak kuantizasyon yöntemlerinin kapsamlı bir şekilde ele alınması, BitNET 1-bit kuantizasyon gibi en son teknikler, kuantizasyon süreçlerini ve kıyaslama sonuçlarını gösteren pratik kod örnekleri
- **Model Edinme Stratejileri**: Hugging Face ekosistemi ve Azure AI Foundry Model Catalog'un kurumsal düzeyde SLM dağıtımı için derinlemesine analizi, programatik model indirme, doğrulama ve format dönüştürme için kod örnekleri
- **Geliştirici API'leri**: Modelleri yükleme, çıkarım yapma ve PyTorch, TensorFlow ve ONNX Runtime gibi popüler çerçevelerle entegrasyon gösteren Python, C++ ve C# kod örnekleri

Bu temel bölüm, SLM'leri uç bilişim senaryoları için ideal kılan operasyonel verimlilik, dağıtım esnekliği ve maliyet etkinliği arasındaki dengeyi vurgular ve geliştiricilerin projelerinde doğrudan uygulayabileceği pratik kod örnekleri sunar.

### **[Bölüm 2: Yerel Ortamda Dağıtım - Gizlilik Öncelikli Çözümler](./02.DeployingSLMinLocalEnv.md)**
İkinci bölüm, teoriden pratik uygulamaya geçiş yaparak veri egemenliğini ve operasyonel bağımsızlığı önceliklendiren yerel dağıtım stratejilerine odaklanır. Anahtar alanlar şunları içerir:

- **Ollama Evrensel Platformu**: Geliştirici dostu iş akışlarına, model yaşam döngüsü yönetimine ve Modelfiles aracılığıyla özelleştirmeye vurgu yaparak çapraz platform dağıtımının kapsamlı bir şekilde incelenmesi, tam REST API entegrasyon örnekleri ve CLI otomasyon betikleri
- **Microsoft Foundry Local**: ONNX tabanlı optimizasyon, Windows ML entegrasyonu ve kapsamlı güvenlik özellikleriyle kurumsal düzeyde dağıtım çözümleri, yerel uygulama entegrasyonu için C# ve Python kod örnekleri
- **Karşılaştırmalı Analiz**: Teknik mimari, performans özellikleri ve kullanım senaryosu optimizasyon yönergelerini kapsayan detaylı çerçeve karşılaştırması, farklı donanımlarda çıkarım hızı ve bellek kullanımını değerlendirmek için kıyaslama kodu
- **API Entegrasyonu**: Yerel SLM dağıtımları kullanarak web hizmetleri, sohbet uygulamaları ve veri işleme boru hatları oluşturmayı gösteren örnek uygulamalar, Node.js, Python Flask/FastAPI ve ASP.NET Core'da kod örnekleri
- **Test Çerçeveleri**: Model kalite güvencesi için otomatik test yaklaşımları, SLM uygulamaları için birim ve entegrasyon test örnekleri

Bu bölüm, gizlilik koruyan yapay zeka çözümleri uygulamak isteyen kuruluşlara, dağıtım ortamları üzerinde tam kontrol sağlarken pratik rehberlik sunar ve geliştiricilerin özel gereksinimlerine uyarlayabileceği hazır kod örnekleri içerir.

### **[Bölüm 3: Konteynerleştirilmiş Bulut Dağıtımı - Üretim Ölçekli Çözümler](./03.DeployingSLMinCloud.md)**
Son bölüm, Microsoft'un Phi-4-mini-instruct modelini birincil vaka çalışması olarak öne çıkaran ileri düzey konteynerleştirilmiş dağıtım stratejileriyle sonuçlanır. Bu bölüm şunları kapsar:

- **vLLM Dağıtımı**: OpenAI uyumlu API'ler, gelişmiş GPU hızlandırma ve üretim ölçekli yapılandırma ile yüksek performanslı çıkarım optimizasyonu, tam Dockerfile'lar, Kubernetes manifestleri ve performans ayar parametreleri
- **Ollama Konteyner Orkestrasyonu**: Docker Compose ile basitleştirilmiş dağıtım iş akışları, model optimizasyon varyantları ve web UI entegrasyonu, otomatik dağıtım ve test için CI/CD boru hattı örnekleri
- **ONNX Runtime Uygulaması**: Kapsamlı model dönüştürme, kuantizasyon stratejileri ve çapraz platform uyumluluğu ile uç optimizasyonlu dağıtım, model optimizasyonu ve dağıtımı için detaylı kod örnekleri
- **İzleme ve Gözlemlenebilirlik**: SLM performans izleme için özel metriklerle Prometheus/Grafana panolarının uygulanması, uyarı yapılandırmaları ve günlük toplama
- **Yük Dengeleme ve Ölçeklendirme**: CPU/GPU kullanımı ve istek desenlerine dayalı otomatik ölçeklendirme yapılandırmaları ile yatay ve dikey ölçeklendirme stratejilerinin pratik örnekleri
- **Güvenlik Güçlendirme**: API anahtarları ve model erişim kimlik bilgileri için ayrıcalık azaltma, ağ politikaları ve gizli bilgiler yönetimi gibi konteyner güvenliği en iyi uygulamaları

Her dağıtım yaklaşımı, tam yapılandırma örnekleri, test prosedürleri, üretim hazırlık kontrol listeleri ve geliştiricilerin dağıtım iş akışlarına doğrudan uygulayabileceği altyapı kodu şablonları ile sunulmaktadır.

## Temel Öğrenme Çıktıları

Bu bölümü tamamlayan okuyucular şunları öğrenecek:

1. **Stratejik Model Seçimi**: Kaynak kısıtlamaları ve performans gereksinimlerine dayalı olarak uygun SLM'leri seçme
2. **Optimizasyon Uzmanlığı**: Farklı çerçevelerde ileri düzey kuantizasyon tekniklerini uygulayarak optimal performans-verimlilik dengesine ulaşma
3. **Dağıtım Esnekliği**: Kurumsal ihtiyaçlara göre yerel gizlilik odaklı çözümler ve ölçeklenebilir konteynerleştirilmiş dağıtımlar arasında seçim yapma
4. **Üretim Hazırlığı**: Kurumsal düzeyde SLM dağıtımları için izleme, güvenlik ve ölçeklendirme sistemlerini yapılandırma

## Pratik Odak ve Gerçek Dünya Uygulamaları

Bölüm boyunca güçlü bir pratik odak korunur ve şunları içerir:

- **Uygulamalı Örnekler**: Tam yapılandırma dosyaları, API test prosedürleri ve dağıtım betikleri
- **Performans Kıyaslaması**: Çıkarım hızı, bellek kullanımı ve kaynak gereksinimlerinin detaylı karşılaştırmaları
- **Güvenlik Hususları**: Kurumsal düzeyde güvenlik uygulamaları, uyumluluk çerçeveleri ve veri koruma stratejileri
- **En İyi Uygulamalar**: İzleme, ölçeklendirme ve bakım için üretimde kanıtlanmış yönergeler

## Geleceğe Hazır Perspektif

Bölüm, şu gibi ortaya çıkan eğilimlere yönelik ileriye dönük bilgilerle sona erer:

- Geliştirilmiş verimlilik oranlarına sahip ileri model mimarileri
- Özel yapay zeka hızlandırıcıları ile daha derin donanım entegrasyonu
- Standardizasyon ve birlikte çalışabilirlik yönünde ekosistem evrimi
- Gizlilik ve uyumluluk gereksinimleri tarafından yönlendirilen kurumsal benimseme modelleri

Bu kapsamlı yaklaşım, okuyucuların hem mevcut SLM dağıtım zorluklarını hem de gelecekteki teknolojik gelişmeleri aşmak için iyi donanımlı olmasını sağlar. Okuyucular, özel kurumsal gereksinimlerine ve kısıtlamalarına uygun kararlar alarak bilinçli seçimler yapabilir.

Bölüm, hem hemen uygulanabilir pratik bir rehber hem de uzun vadeli yapay zeka dağıtım planlaması için stratejik bir kaynak olarak hizmet eder ve başarılı SLM dağıtımlarını tanımlayan yetenek, verimlilik ve operasyonel mükemmellik arasındaki kritik dengeyi vurgular.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.