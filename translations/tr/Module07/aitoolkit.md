# Visual Studio Code için AI Toolkit - Edge AI Geliştirme Rehberi

## Giriş

Edge AI geliştirme için Visual Studio Code'daki AI Toolkit'i kullanma konusunda kapsamlı rehbere hoş geldiniz. Yapay zeka, merkezi bulut bilişimden dağıtılmış uç cihazlara doğru ilerlerken, geliştiricilerin kaynak kısıtlamalarından çevrimdışı çalışma gereksinimlerine kadar uç dağıtımın benzersiz zorluklarını ele alabilecek güçlü ve entegre araçlara ihtiyacı vardır.

Visual Studio Code için AI Toolkit, uç cihazlarda verimli bir şekilde çalışan yapay zeka uygulamaları oluşturmak, test etmek ve optimize etmek için özel olarak tasarlanmış eksiksiz bir geliştirme ortamı sunarak bu boşluğu doldurur. IoT sensörleri, mobil cihazlar, gömülü sistemler veya uç sunucular için geliştirme yapıyor olun, bu araç seti, tanıdık VS Code ortamında tüm geliştirme iş akışınızı kolaylaştırır.

Bu rehber, ilk model seçiminden üretim dağıtımına kadar Edge AI projelerinizde AI Toolkit'i kullanmak için gerekli kavramlar, araçlar ve en iyi uygulamalar konusunda size rehberlik edecektir.

## Genel Bakış

Visual Studio Code için AI Toolkit, ajan geliştirme ve yapay zeka uygulamaları oluşturmayı kolaylaştıran güçlü bir eklentidir. Bu araç seti, Anthropic, OpenAI, GitHub, Google gibi birçok sağlayıcıdan yapay zeka modellerini keşfetme, değerlendirme ve dağıtma için kapsamlı yetenekler sunar ve ONNX ve Ollama kullanarak yerel model çalıştırmayı destekler.

AI Toolkit'i diğerlerinden ayıran şey, yapay zeka geliştirme yaşam döngüsünün tamamına yönelik kapsamlı yaklaşımıdır. Geleneksel yapay zeka geliştirme araçları genellikle tek bir alana odaklanırken, AI Toolkit model keşfi, deney, ajan geliştirme, değerlendirme ve dağıtımı kapsayan entegre bir ortam sağlar - hepsi tanıdık VS Code ortamında.

Platform, hızlı prototipleme ve üretim dağıtımı için özel olarak tasarlanmıştır ve uç AI geliştirme için iş akışınızı verimli bir şekilde geliştirebilmeniz, test edebilmeniz ve optimize edebilmeniz anlamına gelir.

## Öğrenme Hedefleri

Bu rehberin sonunda şunları yapabileceksiniz:

### Temel Yetenekler
- Edge AI geliştirme iş akışları için Visual Studio Code'daki AI Toolkit'i **kurun ve yapılandırın**
- Model Kataloğu, Playground ve Agent Builder gibi AI Toolkit arayüzünü **kullanın ve gezin**
- Performans ve kaynak kısıtlamalarına dayalı olarak uç dağıtım için uygun yapay zeka modellerini **seçin ve değerlendirin**
- ONNX formatı ve kuantizasyon tekniklerini kullanarak modelleri uç cihazlar için **dönüştürün ve optimize edin**

### Edge AI Geliştirme Becerileri
- Entegre geliştirme ortamını kullanarak Edge AI uygulamaları **tasarlayın ve uygulayın**
- Yerel çıkarım ve kaynak izleme kullanarak uç benzeri koşullarda model testi **yapın**
- Uç dağıtım senaryoları için optimize edilmiş yapay zeka ajanları **oluşturun ve özelleştirin**
- Uç bilişimle ilgili metrikler (gecikme, bellek kullanımı, doğruluk) kullanarak model performansını **değerlendirin**

### Optimizasyon ve Dağıtım
- Model boyutunu azaltmak için kuantizasyon ve budama tekniklerini **uygulayın** ve kabul edilebilir performansı koruyun
- CPU, GPU ve NPU hızlandırma dahil olmak üzere belirli uç donanım platformları için modelleri **optimize edin**
- Kaynak yönetimi ve geri dönüş stratejileri gibi uç AI geliştirme için en iyi uygulamaları **uygulayın**
- Uç cihazlarda üretim dağıtımı için modelleri ve uygulamaları **hazırlayın**

### İleri Düzey Edge AI Kavramları
- ONNX Runtime, Windows ML ve TensorFlow Lite gibi uç AI çerçeveleriyle **entegre edin**
- Uç ortamlar için çoklu model mimarileri ve federatif öğrenme senaryolarını **uygulayın**
- Bellek kısıtlamaları, çıkarım hızı ve donanım uyumluluğu gibi yaygın uç AI sorunlarını **çözün**
- Üretimdeki uç AI uygulamaları için izleme ve günlükleme stratejileri **tasarlayın**

### Pratik Uygulama
- Model seçiminden dağıtıma kadar uçtan uca Edge AI çözümleri **oluşturun**
- Uç spesifik geliştirme iş akışları ve optimizasyon tekniklerinde **uzmanlık gösterin**
- IoT, mobil ve gömülü uygulamalar gibi gerçek dünya Edge AI kullanım durumlarına **öğrenilen kavramları uygulayın**
- Farklı uç AI dağıtım stratejilerini ve bunların avantajlarını **değerlendirin ve karşılaştırın**

## Edge AI Geliştirme için Temel Özellikler

### 1. Model Kataloğu ve Keşif
- **Çoklu Sağlayıcı Desteği**: Anthropic, OpenAI, GitHub, Google ve diğer sağlayıcılardan yapay zeka modellerini keşfedin ve erişin
- **Yerel Model Entegrasyonu**: ONNX ve Ollama modellerinin uç dağıtımı için basitleştirilmiş keşfi
- **GitHub Modelleri**: GitHub'ın model barındırma özelliği ile doğrudan entegrasyon
- **Model Karşılaştırması**: Uç cihaz kısıtlamaları için optimal dengeyi bulmak üzere modelleri yan yana karşılaştırın

### 2. Etkileşimli Playground
- **Etkileşimli Test Ortamı**: Kontrollü bir ortamda model yeteneklerini hızlıca deneyin
- **Çoklu Mod Desteği**: Uç senaryolarda tipik olan görüntüler, metinler ve diğer girdilerle test yapın
- **Gerçek Zamanlı Deney**: Model yanıtları ve performansı hakkında anında geri bildirim alın
- **Parametre Optimizasyonu**: Uç dağıtım gereksinimleri için model parametrelerini ince ayar yapın

### 3. Prompt (Ajan) Oluşturucu
- **Doğal Dil Üretimi**: Doğal dil açıklamaları kullanarak başlangıç promptları oluşturun
- **Yinelemeli İyileştirme**: Model yanıtlarına ve performansına dayalı olarak promptları geliştirin
- **Görev Ayrıştırma**: Prompt zincirleme ve yapılandırılmış çıktılarla karmaşık görevleri parçalayın
- **Değişken Desteği**: Dinamik ajan davranışı için promptlarda değişkenler kullanın
- **Üretim Kod Üretimi**: Hızlı uygulama geliştirme için üretime hazır kod oluşturun

### 4. Toplu Çalıştırma ve Değerlendirme
- **Çoklu Model Testi**: Seçilen modellerde birden fazla promptu aynı anda çalıştırın
- **Ölçekli Verimli Test**: Çeşitli girdileri ve yapılandırmaları verimli bir şekilde test edin
- **Özel Test Vakaları**: Ajanları işlevselliği doğrulamak için test vakalarıyla çalıştırın
- **Performans Karşılaştırması**: Farklı modeller ve yapılandırmalar arasında sonuçları karşılaştırın

### 5. Veri Setleri ile Model Değerlendirme
- **Standart Metrikler**: F1 skoru, alaka düzeyi, benzerlik, tutarlılık gibi yerleşik değerlendiricilerle yapay zeka modellerini test edin
- **Özel Değerlendiriciler**: Belirli kullanım durumları için kendi değerlendirme metriklerinizi oluşturun
- **Veri Seti Entegrasyonu**: Modelleri kapsamlı veri setlerine karşı test edin
- **Performans Ölçümü**: Uç dağıtım kararları için model performansını ölçün

### 6. İnce Ayar Yetkinlikleri
- **Model Özelleştirme**: Belirli kullanım durumları ve alanlar için modelleri özelleştirin
- **Uzmanlaşmış Uyarlama**: Modelleri özel alanlara ve gereksinimlere uyarlayın
- **Uç Optimizasyonu**: Modelleri özellikle uç dağıtım kısıtlamaları için ince ayar yapın
- **Alan-Specifik Eğitim**: Belirli uç kullanım durumlarına uygun modeller oluşturun

### 7. MCP Araç Entegrasyonu
- **Harici Araç Bağlantısı**: Ajanları Model Context Protocol sunucuları aracılığıyla harici araçlara bağlayın
- **Gerçek Dünya Eylemleri**: Ajanların veritabanlarını sorgulamasını, API'lere erişmesini veya özel mantık yürütmesini sağlayın
- **Mevcut MCP Sunucuları**: Komut (stdio) veya HTTP (server-sent event) protokollerinden araçları kullanın
- **Özel MCP Geliştirme**: Agent Builder'da test ederek yeni MCP sunucuları oluşturun ve taslak oluşturun

### 8. Ajan Geliştirme ve Test
- **Fonksiyon Çağırma Desteği**: Ajanların harici fonksiyonları dinamik olarak çağırmasını sağlayın
- **Gerçek Zamanlı Entegrasyon Testi**: Gerçek zamanlı çalıştırmalar ve araç kullanımı ile entegrasyonları test edin
- **Ajan Versiyonlama**: Değerlendirme sonuçları için karşılaştırma yetenekleriyle ajanlar için versiyon kontrolü
- **Hata Ayıklama ve İzleme**: Ajan geliştirme için yerel izleme ve hata ayıklama yetenekleri

## Edge AI Geliştirme İş Akışı

### Aşama 1: Model Keşfi ve Seçimi
1. **Model Kataloğunu Keşfedin**: Uç dağıtım için uygun modelleri bulmak için model kataloğunu kullanın
2. **Performansı Karşılaştırın**: Modelleri boyut, doğruluk ve çıkarım hızı açısından değerlendirin
3. **Yerel Olarak Test Edin**: Uç dağıtımdan önce Ollama veya ONNX modellerini yerel olarak test edin
4. **Kaynak Gereksinimlerini Değerlendirin**: Hedef uç cihazlar için bellek ve hesaplama ihtiyaçlarını belirleyin

### Aşama 2: Model Optimizasyonu
1. **ONNX'e Dönüştürün**: Seçilen modelleri uç uyumluluğu için ONNX formatına dönüştürün
2. **Kuantizasyon Uygulayın**: INT8 veya INT4 kuantizasyon ile model boyutunu azaltın
3. **Donanım Optimizasyonu**: Hedef uç donanım için optimize edin (ARM, x86, özel hızlandırıcılar)
4. **Performans Doğrulaması**: Optimize edilmiş modellerin kabul edilebilir doğruluğu koruduğunu doğrulayın

### Aşama 3: Uygulama Geliştirme
1. **Ajan Tasarımı**: Agent Builder'ı kullanarak uç optimize edilmiş yapay zeka ajanları oluşturun
2. **Prompt Mühendisliği**: Daha küçük uç modellerle etkili çalışan promptlar geliştirin
3. **Entegrasyon Testi**: Ajanları simüle edilmiş uç koşullarda test edin
4. **Kod Üretimi**: Uç dağıtım için optimize edilmiş üretim kodu oluşturun

### Aşama 4: Değerlendirme ve Test
1. **Toplu Değerlendirme**: Optimal uç ayarlarını bulmak için birden fazla yapılandırmayı test edin
2. **Performans Profili**: Çıkarım hızı, bellek kullanımı ve doğruluğu analiz edin
3. **Uç Simülasyonu**: Hedef uç dağıtım ortamına benzer koşullarda test yapın
4. **Stres Testi**: Çeşitli yük koşulları altında performansı değerlendirin

### Aşama 5: Dağıtım Hazırlığı
1. **Son Optimizasyon**: Test sonuçlarına dayalı olarak son optimizasyonları uygulayın
2. **Dağıtım Paketleme**: Modelleri ve kodu uç dağıtım için paketleyin
3. **Dokümantasyon**: Dağıtım gereksinimlerini ve yapılandırmayı belgeleyin
4. **İzleme Ayarı**: Uç dağıtım için izleme ve günlükleme hazırlayın

## Edge AI Geliştirme için Hedef Kitle

### Edge AI Geliştiricileri
- Yapay zeka destekli uç cihazlar ve IoT çözümleri geliştiren uygulama geliştiricileri
- Kaynak kısıtlı cihazlara yapay zeka yeteneklerini entegre eden gömülü sistem geliştiricileri
- Akıllı telefonlar ve tabletler için cihaz üzerinde yapay zeka uygulamaları oluşturan mobil geliştiriciler

### Edge AI Mühendisleri
- Uç dağıtım için modelleri optimize eden ve çıkarım hatlarını yöneten yapay zeka mühendisleri
- Dağıtılmış uç altyapısında yapay zeka modellerini dağıtan ve yöneten DevOps mühendisleri
- Uç donanım kısıtlamaları için yapay zeka iş yüklerini optimize eden performans mühendisleri

### Araştırmacılar ve Eğitimciler
- Uç bilişim için verimli modeller ve algoritmalar geliştiren yapay zeka araştırmacıları
- Uç yapay zeka kavramlarını öğreten ve optimizasyon tekniklerini gösteren eğitimciler
- Uç yapay zeka dağıtımındaki zorluklar ve çözümler hakkında bilgi edinen öğrenciler

## Edge AI Kullanım Durumları

### Akıllı IoT Cihazları
- **Gerçek Zamanlı Görüntü Tanıma**: IoT kameraları ve sensörlerinde bilgisayarlı görme modelleri dağıtımı
- **Ses İşleme**: Akıllı hoparlörlerde konuşma tanıma ve doğal dil işleme uygulaması
- **Tahmine Dayalı Bakım**: Endüstriyel uç cihazlarda anomali tespit modelleri çalıştırma
- **Çevresel İzleme**: Çevresel uygulamalar için sensör veri analizi modelleri dağıtımı

### Mobil ve Gömülü Uygulamalar
- **Cihaz Üzerinde Çeviri**: Çevrimdışı çalışan dil çeviri modelleri uygulaması
- **Artırılmış Gerçeklik**: AR uygulamaları için gerçek zamanlı nesne tanıma ve izleme dağıtımı
- **Sağlık İzleme**: Giyilebilir cihazlar ve tıbbi ekipmanlarda sağlık analizi modelleri çalıştırma
- **Otonom Sistemler**: Dronlar, robotlar ve araçlar için karar verme modelleri uygulaması

### Uç Bilişim Altyapısı
- **Uç Veri Merkezleri**: Düşük gecikmeli uygulamalar için uç veri merkezlerinde yapay zeka modelleri dağıtımı
- **CDN Entegrasyonu**: İçerik dağıtım ağlarına yapay zeka işleme yeteneklerini entegre etme
- **5G Uç**: 5G uç bilişimden yararlanarak yapay zeka destekli uygulamalar geliştirme
- **Sis Bilişim**: Sis bilişim ortamlarında yapay zeka işleme uygulaması

## Kurulum ve Ayar

### Eklenti Kurulumu
AI Toolkit eklentisini doğrudan Visual Studio Code Marketplace'ten yükleyin:

**Eklenti Kimliği**: `ms-windows-ai-studio.windows-ai-studio`

**Kurulum Yöntemleri**:
1. **VS Code Marketplace**: Extensions görünümünde "AI Toolkit" arayın
2. **Komut Satırı**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Doğrudan Kurulum**: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) adresinden indirin

### Edge AI Geliştirme için Ön Koşullar
- **Visual Studio Code**: En son sürüm önerilir
- **Python Ortamı**: Gerekli yapay zeka kütüphaneleriyle Python 3.8+
- **ONNX Runtime** (Opsiyonel): ONNX model çıkarımı için
- **Ollama** (Opsiyonel): Yerel model sunumu için
- **Donanım Hızlandırma Araçları**: CUDA, OpenVINO veya platforma özel hızlandırıcılar

### İlk Yapılandırma
1. **Eklenti Aktivasyonu**: VS Code'u açın ve AI Toolkit'in Activity Bar'da göründüğünü doğrulayın
2. **Model Sağlayıcı Ayarı**: GitHub, OpenAI, Anthropic veya diğer model sağlayıcılara erişimi yapılandırın
3. **Yerel Ortam**: Python ortamını ayarlayın ve gerekli paketleri yükleyin
4. **Donanım Hızlandırma**: GPU/NPU hızlandırmayı yapılandırın (varsa)
5. **MCP Entegrasyonu**: Gerekirse Model Context Protocol sunucularını ayarlayın

### İlk Kurulum Kontrol Listesi
- [ ] AI Toolkit eklentisi yüklendi ve etkinleştirildi
- [ ] Model kataloğu erişilebilir ve modeller keşfedilebilir
- [ ] Playground model testi için işlevsel
- [ ] Prompt geliştirme için Agent Builder erişilebilir
- [ ] Yerel geliştirme ortamı yapılandırıldı
- [ ] Donanım hızlandırma (varsa) doğru şekilde yapılandırıldı

## AI Toolkit ile Başlarken

### Hızlı Başlangıç Rehberi

En sorunsuz deneyim için GitHub tarafından barındırılan modellerle başlamanızı öneririz:

1. **Kurulum**: AI Toolkit'i cihazınıza kurmak için [kurulum rehberini](https://code.visualstudio.com
2. Doğal dil açıklamalarını kullanarak başlangıç istemleri oluşturun  
3. Model yanıtlarına göre istemleri yineleyin ve geliştirin  
4. Gelişmiş ajan yetenekleri için MCP araçlarını entegre edin  

#### Adım 3: Test ve Değerlendirme  
1. **Toplu Çalıştırma** kullanarak seçilen modellerde birden fazla istemi test edin  
2. Ajanları test senaryolarıyla çalıştırarak işlevselliği doğrulayın  
3. Dahili veya özel metrikler kullanarak doğruluk ve performansı değerlendirin  
4. Farklı modelleri ve yapılandırmaları karşılaştırın  

#### Adım 4: İnce Ayar ve Optimizasyon  
1. Modelleri belirli uç kullanım senaryoları için özelleştirin  
2. Alan odaklı ince ayar uygulayın  
3. Uç dağıtım kısıtlamaları için optimize edin  
4. Farklı ajan yapılandırmalarını sürümleyin ve karşılaştırın  

#### Adım 5: Dağıtım Hazırlığı  
1. Ajan Oluşturucu kullanarak üretime hazır kod oluşturun  
2. Üretim kullanımı için MCP sunucu bağlantılarını ayarlayın  
3. Uç cihazlar için dağıtım paketlerini hazırlayın  
4. İzleme ve değerlendirme metriklerini yapılandırın  

## AI Araç Seti Örnekleri  

Örneklerimizi Deneyin  
[AI Araç Seti örnekleri](https://github.com/Azure-Samples/AI_Toolkit_Samples), geliştiricilerin ve araştırmacıların AI çözümlerini etkili bir şekilde keşfetmelerine ve uygulamalarına yardımcı olmak için tasarlanmıştır.  

Örneklerimiz şunları içerir:  

Örnek Kod: Modelleri eğitme, dağıtma veya uygulamalara entegre etme gibi AI işlevlerini göstermek için önceden hazırlanmış örnekler.  
Dokümantasyon: Kullanıcıların AI Araç Seti özelliklerini ve bunları nasıl kullanacaklarını anlamalarına yardımcı olacak kılavuzlar ve eğitimler.  
Gereksinimler  

- Visual Studio Code  
- Visual Studio Code için AI Araç Seti  
- GitHub Hassas kişisel erişim belirteci (PAT)  
- Foundry Local  

## Uç AI Geliştirme için En İyi Uygulamalar  

### Model Seçimi  
- **Boyut Kısıtlamaları**: Hedef cihazların bellek sınırlamaları içinde yer alan modelleri seçin  
- **Çıkarım Hızı**: Gerçek zamanlı uygulamalar için hızlı çıkarım sürelerine sahip modelleri tercih edin  
- **Doğruluk Dengesi**: Model doğruluğunu kaynak kısıtlamalarıyla dengeleyin  
- **Format Uyumluluğu**: Uç dağıtım için ONNX veya donanım optimize edilmiş formatları tercih edin  

### Optimizasyon Teknikleri  
- **Kantifikasyon**: Model boyutunu küçültmek ve hızı artırmak için INT8 veya INT4 kantifikasyonu kullanın  
- **Budama**: Hesaplama gereksinimlerini azaltmak için gereksiz model parametrelerini kaldırın  
- **Bilgi Damıtma**: Daha büyük modellerin performansını koruyan daha küçük modeller oluşturun  
- **Donanım Hızlandırma**: Mevcut olduğunda NPU'lar, GPU'lar veya özel hızlandırıcıları kullanın  

### Geliştirme İş Akışı  
- **Yinelemeli Test**: Geliştirme sırasında uç benzeri koşullarda sık sık test yapın  
- **Performans İzleme**: Kaynak kullanımı ve çıkarım hızını sürekli izleyin  
- **Sürüm Kontrolü**: Model sürümlerini ve optimizasyon ayarlarını takip edin  
- **Dokümantasyon**: Tüm optimizasyon kararlarını ve performans dengelerini belgeleyin  

### Dağıtım Düşünceleri  
- **Kaynak İzleme**: Üretimde bellek, CPU ve güç kullanımını izleyin  
- **Geri Dönüş Stratejileri**: Model hataları için geri dönüş mekanizmaları uygulayın  
- **Güncelleme Mekanizmaları**: Model güncellemeleri ve sürüm yönetimi için plan yapın  
- **Güvenlik**: Uç AI uygulamaları için uygun güvenlik önlemleri uygulayın  

## Uç AI Çerçeveleri ile Entegrasyon  

### ONNX Runtime  
- **Çapraz Platform Dağıtımı**: ONNX modellerini farklı uç platformlarda dağıtın  
- **Donanım Optimizasyonu**: ONNX Runtime'ın donanıma özel optimizasyonlarından yararlanın  
- **Mobil Destek**: Akıllı telefon ve tablet uygulamaları için ONNX Runtime Mobile kullanın  
- **IoT Entegrasyonu**: ONNX Runtime'ın hafif dağıtımlarıyla IoT cihazlarında dağıtım yapın  

### Windows ML  
- **Windows Cihazları**: Windows tabanlı uç cihazlar ve PC'ler için optimize edin  
- **NPU Hızlandırma**: Windows cihazlarında Neural Processing Units'ten yararlanın  
- **DirectML**: Windows platformlarında GPU hızlandırma için DirectML kullanın  
- **UWP Entegrasyonu**: Universal Windows Platform uygulamalarıyla entegre edin  

### TensorFlow Lite  
- **Mobil Optimizasyon**: TensorFlow Lite modellerini mobil ve gömülü cihazlarda dağıtın  
- **Donanım Delegeleri**: Hızlandırma için özel donanım delegelerini kullanın  
- **Mikro Kontrolcüler**: TensorFlow Lite Micro kullanarak mikro kontrolcülerde dağıtım yapın  
- **Çapraz Platform Desteği**: Android, iOS ve gömülü Linux sistemlerinde dağıtım yapın  

### Azure IoT Edge  
- **Bulut-Uç Hibrit**: Bulut eğitimi ile uç çıkarımı birleştirin  
- **Modül Dağıtımı**: AI modellerini IoT Edge modülleri olarak dağıtın  
- **Cihaz Yönetimi**: Uç cihazları ve model güncellemelerini uzaktan yönetin  
- **Telemetri**: Uç dağıtımlardan performans verileri ve model metrikleri toplayın  

## Gelişmiş Uç AI Senaryoları  

### Çoklu Model Dağıtımı  
- **Model Toplulukları**: Daha iyi doğruluk veya yedeklilik için birden fazla model dağıtın  
- **A/B Testi**: Uç cihazlarda farklı modelleri aynı anda test edin  
- **Dinamik Seçim**: Mevcut cihaz koşullarına göre modelleri seçin  
- **Kaynak Paylaşımı**: Birden fazla dağıtılmış model arasında kaynak kullanımını optimize edin  

### Federatif Öğrenme  
- **Dağıtılmış Eğitim**: Modelleri birden fazla uç cihazda eğitin  
- **Gizlilik Koruma**: Eğitim verilerini yerel tutarken model iyileştirmelerini paylaşın  
- **İşbirlikçi Öğrenme**: Cihazların kolektif deneyimlerden öğrenmesini sağlayın  
- **Uç-Bulut Koordinasyonu**: Uç cihazlar ve bulut altyapısı arasında öğrenmeyi koordine edin  

### Gerçek Zamanlı İşleme  
- **Akış İşleme**: Uç cihazlarda sürekli veri akışlarını işleyin  
- **Düşük Gecikmeli Çıkarım**: Minimum çıkarım gecikmesi için optimize edin  
- **Toplu İşleme**: Uç cihazlarda veri gruplarını verimli bir şekilde işleyin  
- **Uyarlanabilir İşleme**: Mevcut cihaz yeteneklerine göre işlemi ayarlayın  

## Uç AI Geliştirme Sorun Giderme  

### Yaygın Sorunlar  
- **Bellek Kısıtlamaları**: Model hedef cihaz belleği için çok büyük  
- **Çıkarım Hızı**: Model çıkarımı gerçek zamanlı gereksinimler için çok yavaş  
- **Doğruluk Bozulması**: Optimizasyon model doğruluğunu kabul edilemez şekilde düşürüyor  
- **Donanım Uyumluluğu**: Model hedef donanımla uyumlu değil  

### Hata Ayıklama Stratejileri  
- **Performans Profili**: AI Araç Seti'nin izleme özelliklerini kullanarak darboğazları belirleyin  
- **Kaynak İzleme**: Geliştirme sırasında bellek ve CPU kullanımını izleyin  
- **Artımlı Test**: Sorunları izole etmek için optimizasyonları kademeli olarak test edin  
- **Donanım Simülasyonu**: Hedef donanımı simüle etmek için geliştirme araçlarını kullanın  

### Optimizasyon Çözümleri  
- **Daha Fazla Kantifikasyon**: Daha agresif kantifikasyon teknikleri uygulayın  
- **Model Mimarisi**: Uç için optimize edilmiş farklı model mimarilerini düşünün  
- **Ön İşleme Optimizasyonu**: Uç kısıtlamaları için veri ön işleme optimizasyonu yapın  
- **Çıkarım Optimizasyonu**: Donanıma özel çıkarım optimizasyonlarını kullanın  

## Kaynaklar ve Sonraki Adımlar  

### Resmi Dokümantasyon  
- [AI Araç Seti Geliştirici Dokümantasyonu](https://aka.ms/AIToolkit/doc)  
- [Kurulum ve Ayar Kılavuzu](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Akıllı Uygulamalar Dokümantasyonu](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Dokümantasyonu](https://modelcontextprotocol.io/)  

### Topluluk ve Destek  
- [AI Araç Seti GitHub Deposu](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Sorunlar ve Özellik Talepleri](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Topluluğu](https://aka.ms/azureaifoundry/discord)  
- [VS Code Uzantı Pazarı](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Teknik Kaynaklar  
- [ONNX Runtime Dokümantasyonu](https://onnxruntime.ai/)  
- [Ollama Dokümantasyonu](https://ollama.ai/)  
- [Windows ML Dokümantasyonu](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Dokümantasyonu](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Öğrenme Yolları  
- [Uç AI Temelleri Kursu](../Module01/README.md)  
- [Küçük Dil Modelleri Kılavuzu](../Module02/README.md)  
- [Uç Dağıtım Stratejileri](../Module03/README.md)  
- [Windows Uç AI Geliştirme](./windowdeveloper.md)  

### Ek Kaynaklar  
- **Depo İstatistikleri**: 1.8k+ yıldız, 150+ çatal, 18+ katkıda bulunan  
- **Lisans**: MIT Lisansı  
- **Güvenlik**: Microsoft güvenlik politikaları geçerlidir  
- **Telemetri**: VS Code telemetri ayarlarına saygı gösterir  

## Sonuç  

Visual Studio Code için AI Araç Seti, modern AI geliştirme için kapsamlı bir platform sunar ve özellikle Uç AI uygulamaları için değerli olan ajan geliştirme yeteneklerini sağlar. Anthropic, OpenAI, GitHub ve Google gibi sağlayıcıları destekleyen geniş model kataloğu ve ONNX ile Ollama üzerinden yerel çalıştırma ile araç seti, çeşitli uç dağıtım senaryoları için gereken esnekliği sunar.  

Araç setinin gücü, entegre yaklaşımında yatmaktadır—Playground'da model keşfi ve deneyden, Prompt Builder ile sofistike ajan geliştirmeye, kapsamlı değerlendirme yeteneklerine ve sorunsuz MCP araç entegrasyonuna kadar. Uç AI geliştiricileri için bu, ajanları uç dağıtımdan önce hızlı bir şekilde prototipleme ve test etme, kaynak kısıtlı ortamlar için hızlı bir şekilde yineleme ve optimize etme anlamına gelir.  

Uç AI geliştirme için temel avantajlar şunlardır:  
- **Hızlı Deney**: Uç dağıtıma geçmeden önce modelleri ve ajanları hızlı bir şekilde test edin  
- **Çoklu Sağlayıcı Esnekliği**: Uç çözümler için en uygun modelleri bulmak için çeşitli kaynaklardan modellere erişin  
- **Yerel Geliştirme**: Çevrimdışı ve gizlilik koruyucu geliştirme için ONNX ve Ollama ile test yapın  
- **Üretim Hazırlığı**: Üretime hazır kod oluşturun ve MCP aracılığıyla harici araçlarla entegre edin  
- **Kapsamlı Değerlendirme**: Uç AI performansını doğrulamak için dahili ve özel metrikler kullanın  

AI, uç dağıtım senaryolarına doğru ilerlemeye devam ederken, VS Code için AI Araç Seti, kaynak kısıtlı ortamlar için akıllı uygulamalar oluşturmak, test etmek ve optimize etmek için gereken geliştirme ortamını ve iş akışını sağlar. IoT çözümleri, mobil AI uygulamaları veya gömülü zeka sistemleri geliştiriyor olun, araç setinin kapsamlı özellik seti ve entegre iş akışı, uç AI geliştirme yaşam döngüsünün tamamını destekler.  

Sürekli gelişim ve aktif bir topluluk (1.8k+ GitHub yıldızı) ile AI Araç Seti, uç dağıtım senaryoları için modern AI geliştiricilerinin ihtiyaçlarını karşılamak üzere sürekli olarak evrimleşen AI geliştirme araçlarının ön saflarında yer almaktadır.  

[Sonraki Foundry Local](./foundrylocal.md)  

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.