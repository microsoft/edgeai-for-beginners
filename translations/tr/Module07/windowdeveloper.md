# Windows Edge AI Geliştirme Rehberi

## Giriş

Windows Edge AI Geliştirme'ye hoş geldiniz - Microsoft'un Windows AI Foundry platformunu kullanarak cihaz üzerinde yapay zeka gücünden yararlanan akıllı uygulamalar oluşturmak için kapsamlı rehberiniz. Bu rehber, Windows geliştiricilerinin uygulamalarına en son Edge AI özelliklerini entegre ederken Windows donanım hızlandırmasının tüm yelpazesinden faydalanmalarını sağlamak için özel olarak tasarlanmıştır.

### Windows AI Avantajı

Windows AI Foundry, model seçimi ve ince ayar yapmaktan optimizasyon ve CPU, GPU, NPU ve hibrit bulut mimarileri arasında dağıtıma kadar tam bir yapay zeka geliştirici yaşam döngüsünü destekleyen birleşik, güvenilir ve güvenli bir platform sunar. Bu platform, aşağıdaki özelliklerle yapay zeka geliştirmeyi demokratikleştirir:

- **Donanım Soyutlama**: AMD, Intel, NVIDIA ve Qualcomm silikonları arasında sorunsuz dağıtım
- **Cihaz Üzerinde Zeka**: Tamamen yerel donanımda çalışan, gizliliği koruyan yapay zeka
- **Optimize Edilmiş Performans**: Windows donanım yapılandırmaları için önceden optimize edilmiş modeller
- **Kurumsal Hazır**: Üretim seviyesinde güvenlik ve uyumluluk özellikleri

### Windows ML 
Windows Machine Learning (ML), C#, C++ ve Python geliştiricilerinin ONNX AI modellerini Windows PC'lerde yerel olarak ONNX Runtime üzerinden çalıştırmasını sağlar ve farklı donanımlar (CPU, GPU, NPU) için otomatik yürütme sağlayıcı yönetimi sunar. [ONNX Runtime](https://onnxruntime.ai/docs/) PyTorch, Tensorflow/Keras, TFLite, scikit-learn ve diğer çerçevelerden gelen modellerle kullanılabilir.

![WindowsML ONNX modelinin Windows ML üzerinden NPU, GPU ve CPU'ya ulaşmasını gösteren bir diyagram.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML, Windows genelinde paylaşılan bir ONNX Runtime kopyası ve yürütme sağlayıcılarını (EP'ler) dinamik olarak indirme yeteneği sunar.

### Edge AI için Neden Windows?

**Evrensel Donanım Desteği**  
Windows ML, tüm Windows ekosistemi genelinde otomatik donanım optimizasyonu sağlar ve yapay zeka uygulamalarınızın temel silikon mimarisinden bağımsız olarak en iyi şekilde performans göstermesini garanti eder.

**Entegre AI Çalışma Zamanı**  
Yerleşik Windows ML çıkarım motoru, karmaşık kurulum gereksinimlerini ortadan kaldırır ve geliştiricilerin altyapı endişeleri yerine uygulama mantığına odaklanmasını sağlar.

**Copilot+ PC Optimizasyonu**  
Özel Neural Processing Unit'lere (NPU) sahip yeni nesil Windows cihazları için tasarlanmış API'ler, watt başına olağanüstü performans sunar.

**Geliştirici Ekosistemi**  
Visual Studio entegrasyonu, kapsamlı belgeler ve geliştirme döngülerini hızlandıran örnek uygulamalar gibi zengin araçlar.

## Öğrenme Hedefleri

Bu Windows Edge AI geliştirme rehberini tamamlayarak, Windows platformunda üretime hazır yapay zeka uygulamaları oluşturmak için gerekli temel becerileri öğreneceksiniz.

### Temel Teknik Yetkinlikler

**Windows AI Foundry Uzmanlığı**
- Windows AI Foundry platformunun mimarisini ve bileşenlerini anlayın
- Windows ekosisteminde tam yapay zeka geliştirme yaşam döngüsünü yönetin
- Cihaz üzerinde yapay zeka uygulamaları için güvenlik en iyi uygulamalarını uygulayın
- Farklı Windows donanım yapılandırmaları için uygulamaları optimize edin

**API Entegrasyonu Uzmanlığı**
- Metin, görsel ve çok modlu uygulamalar için Windows AI API'lerini öğrenin
- Phi Silica dil modeli entegrasyonunu metin üretimi ve akıl yürütme için uygulayın
- Yerleşik görüntü işleme API'lerini kullanarak bilgisayar görme yeteneklerini dağıtın
- LoRA (Low-Rank Adaptation) tekniklerini kullanarak önceden eğitilmiş modelleri özelleştirin

**Foundry Local Uygulaması**
- Foundry Local CLI kullanarak açık kaynaklı dil modellerini gözden geçirin, değerlendirin ve dağıtın
- Yerel dağıtım için model optimizasyonunu ve kuantizasyonu anlayın
- İnternet bağlantısı olmadan çalışan çevrimdışı yapay zeka yeteneklerini uygulayın
- Üretim ortamlarında model yaşam döngülerini ve güncellemelerini yönetin

**Windows ML Dağıtımı**
- Özel ONNX modellerini Windows ML kullanarak Windows uygulamalarına getirin
- CPU, GPU ve NPU mimarileri arasında otomatik donanım hızlandırmasından yararlanın
- Optimal kaynak kullanımı ile gerçek zamanlı çıkarım uygulayın
- Çeşitli Windows cihaz kategorileri için ölçeklenebilir yapay zeka uygulamaları tasarlayın

### Uygulama Geliştirme Becerileri

**Çapraz Platform Windows Geliştirme**
- Evrensel Windows dağıtımı için .NET MAUI kullanarak yapay zeka destekli uygulamalar oluşturun
- Yapay zeka yeteneklerini Win32, UWP ve İlerici Web Uygulamalarına entegre edin
- Yapay zeka işlem durumlarına uyum sağlayan duyarlı UI tasarımları uygulayın
- Asenkron yapay zeka işlemlerini uygun kullanıcı deneyimi desenleriyle yönetin

**Performans Optimizasyonu**
- Farklı donanım yapılandırmaları arasında yapay zeka çıkarım performansını profil oluşturun ve optimize edin
- Büyük dil modelleri için verimli bellek yönetimi uygulayın
- Mevcut donanım yeteneklerine göre zarif bir şekilde azalan uygulamalar tasarlayın
- Sık kullanılan yapay zeka işlemleri için önbellek stratejileri uygulayın

**Üretim Hazırlığı**
- Kapsamlı hata işleme ve geri dönüş mekanizmaları uygulayın
- Yapay zeka uygulama performansı için telemetri ve izleme tasarlayın
- Yerel yapay zeka model depolama ve çalıştırma için güvenlik en iyi uygulamalarını uygulayın
- Kurumsal ve tüketici uygulamaları için dağıtım stratejileri planlayın

### İş ve Stratejik Anlayış

**Yapay Zeka Uygulama Mimarisi**
- Yerel ve bulut yapay zeka işlemleri arasında optimize eden hibrit mimariler tasarlayın
- Model boyutu, doğruluk ve çıkarım hızı arasındaki ödünleşimleri değerlendirin
- Gizliliği korurken zekayı mümkün kılan veri akışı mimarileri planlayın
- Kullanıcı talepleriyle ölçeklenen maliyet etkin yapay zeka çözümleri uygulayın

**Pazar Konumlandırması**
- Windows'a özgü yapay zeka uygulamalarının rekabet avantajlarını anlayın
- Cihaz üzerinde yapay zekanın üstün kullanıcı deneyimleri sağladığı kullanım durumlarını belirleyin
- Yapay zeka destekli Windows uygulamaları için pazara giriş stratejileri geliştirin
- Uygulamaları Windows ekosisteminin avantajlarından yararlanacak şekilde konumlandırın

## Windows App SDK AI Örnekleri

Windows App SDK, birden fazla çerçeve ve dağıtım senaryosu genelinde yapay zeka entegrasyonunu gösteren kapsamlı örnekler sunar. Bu örnekler, Windows AI geliştirme desenlerini anlamak için temel referanslardır.

### Windows AI Foundry Örnekleri

| Örnek | Çerçeve | Odak Alanı | Ana Özellikler |
|-------|---------|------------|----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API'leri Entegrasyonu | Windows AI API'lerini, ARM64 optimizasyonunu, paketlenmiş dağıtımı gösteren tam bir WinUI uygulaması |

**Ana Teknolojiler:**
- Windows AI API'leri
- WinUI 3 çerçevesi
- ARM64 platform optimizasyonu
- Copilot+ PC uyumluluğu
- Paketlenmiş uygulama dağıtımı

**Ön Koşullar:**
- Windows 11, Copilot+ PC önerilir
- Visual Studio 2022
- ARM64 yapılandırması
- Windows App SDK 1.8.1+

### Windows ML Örnekleri

#### C++ Örnekleri

| Örnek | Tür | Odak Alanı | Ana Özellikler |
|-------|-----|------------|----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Temel Windows ML | EP keşfi, komut satırı seçenekleri, model derleme |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Çerçeve Dağıtımı | Paylaşılan çalışma zamanı, daha küçük dağıtım boyutu |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Bağımsız Dağıtım | Bağımsız dağıtım, çalışma zamanı bağımlılıkları yok |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Kütüphane Kullanımı | Paylaşılan kütüphanede WindowsML, bellek yönetimi |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Eğitimi | Model dönüşümü, EP derleme, Build 2025 eğitimi |

#### C# Örnekleri

**Konsol Uygulamaları**

| Örnek | Tür | Odak Alanı | Ana Özellikler |
|-------|-----|------------|----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsol Uygulaması | Temel C# Entegrasyonu | Paylaşılan yardımcı kullanım, komut satırı arayüzü |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Eğitimi | Model dönüşümü, EP derleme, Build 2025 eğitimi |

**GUI Uygulamaları**

| Örnek | Çerçeve | Odak Alanı | Ana Özellikler |
|-------|---------|------------|----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Masaüstü GUI | WPF arayüzü ile görüntü sınıflandırma |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Geleneksel GUI | Windows Forms ile görüntü sınıflandırma |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | WinUI 3 arayüzü ile görüntü sınıflandırma |

#### Python Örnekleri

| Örnek | Dil | Odak Alanı | Ana Özellikler |
|-------|-----|------------|----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Görüntü Sınıflandırma | WinML Python bağlamaları, toplu görüntü işleme |

### Örnek Ön Koşulları

**Sistem Gereksinimleri:**
- Windows 11 PC, sürüm 24H2 (yapı 26100) veya daha yüksek
- C++ ve .NET iş yükleri ile Visual Studio 2022
- Windows App SDK 1.8.1 veya daha yeni
- Python örnekleri için x64 ve ARM64 cihazlarda Python 3.10-3.13

**Windows AI Foundry Özel:**
- Optimal performans için Copilot+ PC önerilir
- Windows AI örnekleri için ARM64 yapılandırması
- Paket kimliği gerekli (paketlenmemiş uygulamalar artık desteklenmiyor)

### Ortak Örnek İş Akışı

Çoğu Windows ML örneği şu standart deseni takip eder:

1. **Ortamı Başlat** - ONNX Runtime ortamı oluşturun
2. **Yürütme Sağlayıcılarını Kaydedin** - Mevcut donanım hızlandırıcılarını (CPU, GPU, NPU) keşfedin ve kaydedin
3. **Modeli Yükle** - ONNX modelini yükleyin, isteğe bağlı olarak hedef donanım için derleyin
4. **Girdi Ön İşleme** - Görüntüleri/verileri model giriş formatına dönüştürün
5. **Çıkarım Çalıştır** - Modeli çalıştırın ve tahminler alın
6. **Sonuçları İşleyin** - Softmax uygulayın ve en iyi tahminleri görüntüleyin

### Kullanılan Model Dosyaları

| Model | Amaç | Dahil | Notlar |
|-------|------|-------|-------|
| SqueezeNet | Hafif görüntü sınıflandırma | ✅ Dahil | Önceden eğitilmiş, kullanıma hazır |
| ResNet-50 | Yüksek doğrulukta görüntü sınıflandırma | ❌ Dönüşüm gerekli | Dönüşüm için [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) kullanın |

### Donanım Desteği

Tüm örnekler mevcut donanımı otomatik olarak algılar ve kullanır:
- **CPU** - Tüm Windows cihazlarında evrensel destek
- **GPU** - Mevcut grafik donanımı için otomatik algılama ve optimizasyon
- **NPU** - Desteklenen cihazlarda Neural Processing Unit'lerden yararlanır (Copilot+ PC'ler)

## Windows AI Foundry Platform Bileşenleri

### 1. Windows AI API'leri

Windows AI API'leri, cihaz üzerinde modeller tarafından desteklenen, Copilot+ PC cihazlarında verimlilik ve performans için optimize edilmiş, kullanıma hazır yapay zeka yetenekleri sağlar.

#### Temel API Kategorileri

**Phi Silica Dil Modeli**
- Metin üretimi ve akıl yürütme için küçük ama güçlü dil modeli
- Minimum güç tüketimi ile gerçek zamanlı çıkarım için optimize edilmiş
- LoRA tekniklerini kullanarak özel ince ayar desteği
- Windows semantik arama ve bilgi alma ile entegrasyon

**Bilgisayar Görme API'leri**
- **Metin Tanıma (OCR)**: Görüntülerden yüksek doğrulukla metin çıkarma
- **Görüntü Süper Çözünürlük**: Yerel yapay zeka modelleri kullanarak görüntüleri büyütme
- **Görüntü Segmentasyonu**: Görüntülerdeki belirli nesneleri tanımlama ve ayırma
- **Görüntü Açıklaması**: Görsel içerik için ayrıntılı metin açıklamaları oluşturma
- **Nesne Silme**: Görüntülerden istenmeyen nesneleri yapay zeka destekli boyama ile kaldırma

**Çok Modlu Yetkinlikler**
- **Görsel-Metin Entegrasyonu**: Metin ve görüntü anlayışını birleştirme
- **Semantik Arama**: Multimedya içerik üzerinde doğal dil sorguları etkinleştirme
- **Bilgi Alma**: Yerel verilerle akıllı arama deneyimleri oluşturma

### 2. Foundry Local

Foundry Local, geliştiricilere Windows Silicon üzerinde kullanıma hazır açık kaynaklı dil modellerine hızlı erişim sağlar ve yerel uygulamalarda modelleri gözden geçirme, test etme, etkileşim kurma ve dağıtma yeteneği sunar.

#### Foundry Local Örnek Uygulamaları

[Foundry Local deposu](https://github.com/microsoft/Foundry-Local/tree/main/samples), çeşitli entegrasyon desenlerini ve kullanım durumlarını gösteren birden fazla programlama dili ve çerçeve genelinde kapsamlı örnekler sunar.

| Örnek | Dil/Çerçeve | Odak Alanı | Ana Özellikler |
|-------|-------------|------------|----------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Uygulaması | Semantik Kernel entegrasyonu, Qdrant vektör deposu, JINA gömümleri, belge alımı, akışlı sohbet |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Masaüstü Sohbet Uygulaması | Çapraz platform sohbet, yerel/bulut model geçişi, OpenAI SDK entegrasyonu, gerçek zamanlı akış |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Temel Entegrasyon | Basit SDK kullanımı, model başlatma, temel sohbet işlevselliği |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Temel Entegrasyon | Python SDK kullanımı, akışlı yanıtlar, OpenAI uyumlu API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistem Entegrasyonu | Düşük seviyeli SDK kullanımı, asenkron işlemler, reqwest HTTP istemcisi |

#### Kullanım Durumlarına Göre Örnek Kategorileri

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Semantic Kernel, Qdrant vektör veritabanı ve JINA gömüleri kullanılarak tam bir RAG uygulaması
- **Mimari**: Belge alımı → Metin parçalama → Vektör gömüleri → Benzerlik araması → Bağlama duyarlı yanıtlar
- **Teknolojiler**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX gömüleri, akışlı sohbet tamamlama

**Masaüstü Uygulamaları**
- **electron/foundry-chat**: Yerel/bulut model geçişi ile üretime hazır sohbet uygulaması
- **Özellikler**: Model seçici, akışlı yanıtlar, hata yönetimi, platformlar arası dağıtım
- **Mimari**: Electron ana işlem, IPC iletişimi, güvenli ön yükleme betikleri

**SDK Entegrasyon Örnekleri**
- **JavaScript (Node.js)**: Temel model etkileşimi ve akışlı yanıtlar
- **Python**: Asenkron akışlı yanıtlarla OpenAI uyumlu API kullanımı
- **Rust**: Asenkron işlemler için reqwest ve tokio ile düşük seviyeli entegrasyon

#### Foundry Local Örnekleri için Ön Koşullar

**Sistem Gereksinimleri:**
- Foundry Local yüklü Windows 11
- JavaScript/Electron örnekleri için Node.js v16+
- C# örnekleri için .NET 8.0+
- Python örnekleri için Python 3.10+
- Rust örnekleri için Rust 1.70+

**Kurulum:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Örnek Bazlı Kurulum

**dotNET RAG Örneği:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Sohbet Örneği:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust Örnekleri:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Temel Özellikler

**Model Kataloğu**
- Önceden optimize edilmiş açık kaynaklı modellerin kapsamlı koleksiyonu
- CPU, GPU ve NPU'lar arasında optimize edilmiş modellerle anında dağıtım
- Llama, Mistral, Phi ve özel alan modelleri gibi popüler model ailelerini destekler

**CLI Entegrasyonu**
- Model yönetimi ve dağıtımı için komut satırı arayüzü
- Otomatik optimizasyon ve kuantizasyon iş akışları
- Popüler geliştirme ortamları ve CI/CD boru hatları ile entegrasyon

**Yerel Dağıtım**
- Bulut bağımlılığı olmadan tamamen çevrimdışı çalışma
- Özel model formatları ve yapılandırmalarını destekler
- Otomatik donanım optimizasyonu ile verimli model sunumu

### 3. Windows ML

Windows ML, Windows üzerinde özel modellerin geniş donanım ekosistemi boyunca verimli bir şekilde dağıtılmasını sağlayan temel AI platformu ve entegre çıkarım çalıştırma ortamı olarak hizmet verir.

#### Mimari Avantajlar

**Evrensel Donanım Desteği**
- AMD, Intel, NVIDIA ve Qualcomm silikon için otomatik optimizasyon
- CPU, GPU ve NPU yürütme desteği ile şeffaf geçiş
- Platforma özgü optimizasyon çalışmalarını ortadan kaldıran donanım soyutlama

**Model Esnekliği**
- Popüler çerçevelerden otomatik dönüşüm ile ONNX model formatını destekler
- Üretim düzeyinde performansla özel model dağıtımı
- Mevcut Windows uygulama mimarileri ile entegrasyon

**Kurumsal Entegrasyon**
- Windows güvenlik ve uyumluluk çerçeveleri ile uyumlu
- Kurumsal dağıtım ve yönetim araçlarını destekler
- Windows cihaz yönetimi ve izleme sistemleri ile entegrasyon

## Geliştirme İş Akışı

### Aşama 1: Ortam Kurulumu ve Araç Yapılandırması

**Geliştirme Ortamı Hazırlığı**
1. C++ ve .NET iş yükleri ile Visual Studio 2022'yi yükleyin
2. Windows App SDK 1.8.1 veya daha yenisini yükleyin
3. Windows AI Foundry CLI araçlarını yapılandırın
4. Visual Studio Code için AI Toolkit uzantısını ayarlayın
5. Performans profilleme ve izleme araçlarını kurun
6. Copilot+ PC optimizasyonu için ARM64 yapı yapılandırmasını sağlayın

**Örnek Depo Kurulumu**
1. [Windows App SDK Samples deposunu](https://github.com/microsoft/WindowsAppSDK-Samples) klonlayın
2. Windows AI API örnekleri için `Samples/WindowsAIFoundry/cs-winui` dizinine gidin
3. Kapsamlı Windows ML örnekleri için `Samples/WindowsML` dizinine gidin
4. Hedef platformlarınız için [yapı gereksinimlerini](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) inceleyin

**AI Geliştirme Galerisi Keşfi**
- Örnek uygulamaları ve referans uygulamaları keşfedin
- Windows AI API'lerini etkileşimli demolarla test edin
- En iyi uygulamalar ve desenler için kaynak kodunu inceleyin
- Belirli kullanım durumunuz için ilgili örnekleri belirleyin

### Aşama 2: Model Seçimi ve Entegrasyonu

**Gereksinim Analizi**
- AI yetenekleri için işlevsel gereksinimleri tanımlayın
- Performans kısıtlamalarını ve optimizasyon hedeflerini belirleyin
- Gizlilik ve güvenlik gereksinimlerini değerlendirin
- Dağıtım mimarisi ve ölçekleme stratejilerini planlayın

**Model Değerlendirme**
- Kullanım durumunuz için açık kaynaklı modelleri test etmek için Foundry Local'ı kullanın
- Özel model gereksinimlerine karşı Windows AI API'lerini karşılaştırın
- Model boyutu, doğruluk ve çıkarım hızı arasındaki ödünleşimleri değerlendirin
- Seçilen modellerle entegrasyon yaklaşımlarını prototipleyin

### Aşama 3: Uygulama Geliştirme

**Temel Entegrasyon**
- Uygun hata yönetimi ile Windows AI API entegrasyonunu uygulayın
- AI işleme iş akışlarını destekleyen kullanıcı arayüzleri tasarlayın
- Model çıkarımı için önbellekleme ve optimizasyon stratejileri uygulayın
- AI işlem performansı için telemetri ve izleme ekleyin

**Test ve Doğrulama**
- Uygulamaları farklı Windows donanım yapılandırmalarında test edin
- Çeşitli yük koşulları altında performans ölçütlerini doğrulayın
- AI işlevselliği güvenilirliği için otomatik testler uygulayın
- AI destekli özelliklerle kullanıcı deneyimi testleri gerçekleştirin

### Aşama 4: Optimizasyon ve Dağıtım

**Performans Optimizasyonu**
- Hedef donanım yapılandırmaları arasında uygulama performansını profilleyin
- Bellek kullanımı ve model yükleme stratejilerini optimize edin
- Mevcut donanım yeteneklerine dayalı uyarlanabilir davranışlar uygulayın
- Farklı performans senaryoları için kullanıcı deneyimini ince ayar yapın

**Üretim Dağıtımı**
- Uygulamaları uygun AI model bağımlılıkları ile paketleyin
- Modeller ve uygulama mantığı için güncelleme mekanizmaları uygulayın
- Üretim ortamları için izleme ve analiz yapılandırın
- Kurumsal ve tüketici dağıtımları için yayılma stratejileri planlayın

## Pratik Uygulama Örnekleri

### Örnek 1: Akıllı Belge İşleme Uygulaması

Birden fazla AI yeteneği kullanarak belgeleri işleyen bir Windows uygulaması oluşturun:

**Kullanılan Teknolojiler:**
- Belge özetleme ve soru yanıtlama için Phi Silica
- Tarama belgelerinden metin çıkarımı için OCR API'leri
- Grafik ve diyagram analizi için Görüntü Açıklama API'leri
- Belge sınıflandırması için özel ONNX modelleri

**Uygulama Yaklaşımı:**
- Modüler AI bileşenleri ile tasarım mimarisi oluşturun
- Büyük belge grupları için asenkron işleme uygulayın
- Uzun süreli işlemler için ilerleme göstergeleri ve iptal desteği ekleyin
- Hassas belge işleme için çevrimdışı yetenekler dahil edin

### Örnek 2: Perakende Envanter Yönetim Sistemi

Perakende uygulamaları için AI destekli bir envanter sistemi oluşturun:

**Kullanılan Teknolojiler:**
- Ürün tanımlama için Görüntü Segmentasyonu
- Marka ve kategori sınıflandırması için özel görsel modeller
- Özel perakende dil modellerinin Foundry Local dağıtımı
- Mevcut POS ve envanter sistemleri ile entegrasyon

**Uygulama Yaklaşımı:**
- Gerçek zamanlı ürün taraması için kamera entegrasyonu oluşturun
- Barkod ve görsel ürün tanıma uygulayın
- Yerel dil modelleri kullanarak doğal dil envanter sorguları ekleyin
- Çok mağazalı dağıtım için ölçeklenebilir mimari tasarlayın

### Örnek 3: Sağlık Belgeleri Yardımcısı

Gizliliği koruyan bir sağlık belgeleri aracı geliştirin:

**Kullanılan Teknolojiler:**
- Tıbbi not oluşturma ve klinik karar desteği için Phi Silica
- El yazısı tıbbi kayıtları dijitalleştirmek için OCR
- Windows ML aracılığıyla dağıtılan özel tıbbi dil modelleri
- Tıbbi bilgi alımı için yerel vektör depolama

**Uygulama Yaklaşımı:**
- Hasta gizliliği için tamamen çevrimdışı çalışma sağlayın
- Tıbbi terminoloji doğrulama ve öneri uygulayın
- Düzenleyici uyumluluk için denetim kaydı ekleyin
- Mevcut Elektronik Sağlık Kaydı sistemleri ile entegrasyon tasarlayın

## Performans Optimizasyon Stratejileri

### Donanım Bilinçli Geliştirme

**NPU Optimizasyonu**
- Copilot+ PC'lerde NPU yeteneklerinden yararlanacak uygulamalar tasarlayın
- NPU olmayan cihazlarda GPU/CPU'ya zarif bir şekilde geçiş yapın
- NPU'ya özgü hızlandırma için model formatlarını optimize edin
- NPU kullanımını ve termal özelliklerini izleyin

**Bellek Yönetimi**
- Verimli model yükleme ve önbellekleme stratejileri uygulayın
- Başlangıç süresini azaltmak için büyük modeller için bellek eşleme kullanın
- Kaynak kısıtlı cihazlar için bellek bilinci uygulamalar tasarlayın
- Bellek optimizasyonu için model kuantizasyonu uygulayın

**Pil Verimliliği**
- Minimum güç tüketimi için AI işlemlerini optimize edin
- Pil durumuna göre uyarlanabilir işlem uygulayın
- Sürekli AI işlemleri için verimli arka plan işleme tasarlayın
- Enerji kullanımını optimize etmek için güç profilleme araçlarını kullanın

### Ölçeklenebilirlik Düşünceleri

**Çoklu İş Parçacığı**
- Eşzamanlı işleme için iş parçacığı güvenli AI işlemleri tasarlayın
- Mevcut çekirdekler arasında verimli iş dağıtımı uygulayın
- Engellemeyen AI işlemleri için async/await desenlerini kullanın
- Farklı donanım yapılandırmaları için iş parçacığı havuzu optimizasyonunu planlayın

**Önbellekleme Stratejileri**
- Sık kullanılan AI işlemleri için akıllı önbellekleme uygulayın
- Model güncellemeleri için önbellek geçersiz kılma stratejileri tasarlayın
- Pahalı ön işleme işlemleri için kalıcı önbellekleme kullanın
- Çok kullanıcılı senaryolar için dağıtılmış önbellekleme uygulayın

## Güvenlik ve Gizlilik En İyi Uygulamaları

### Veri Koruma

**Yerel İşleme**
- Hassas verilerin yerel cihazdan asla ayrılmadığından emin olun
- AI modelleri ve geçici veriler için güvenli depolama uygulayın
- Uygulama sandboxing için Windows güvenlik özelliklerini kullanın
- Depolanan modeller ve ara işleme sonuçları için şifreleme uygulayın

**Model Güvenliği**
- Yükleme ve yürütmeden önce model bütünlüğünü doğrulayın
- Güvenli model güncelleme mekanizmaları uygulayın
- Kurcalamayı önlemek için imzalı modeller kullanın
- Model dosyaları ve yapılandırma için erişim kontrolleri uygulayın

### Uyumluluk Düşünceleri

**Düzenleyici Uyum**
- Uygulamaları GDPR, HIPAA ve diğer düzenleyici gereksinimlere uygun şekilde tasarlayın
- AI karar verme süreçleri için denetim kaydı uygulayın
- AI tarafından oluşturulan sonuçlar için şeffaflık özellikleri sağlayın
- AI veri işleme üzerinde kullanıcı kontrolü etkinleştirin

**Kurumsal Güvenlik**
- Windows kurumsal güvenlik politikaları ile entegrasyon
- Kurumsal yönetim araçları aracılığıyla yönetilen dağıtımı destekleyin
- AI özellikleri için rol tabanlı erişim kontrolleri uygulayın
- AI işlevselliği için yönetim kontrolleri sağlayın

## Sorun Giderme ve Hata Ayıklama

### Yaygın Geliştirme Zorlukları

**Yapılandırma Sorunları**
- Windows AI API örnekleri için ARM64 platform yapılandırmasını sağlayın
- Windows App SDK sürüm uyumluluğunu doğrulayın (1.8.1+ gerekli)
- Paket kimliğinin düzgün yapılandırıldığını kontrol edin (Windows AI API'leri için gerekli)
- Hedef çerçeve sürümünü destekleyen yapı araçlarını doğrulayın

**Model Yükleme Sorunları**
- ONNX model uyumluluğunu Windows ML ile doğrulayın
- Model dosyası bütünlüğünü ve format gereksinimlerini kontrol edin
- Belirli modeller için donanım yetenek gereksinimlerini doğrulayın
- Model yükleme sırasında bellek tahsisi sorunlarını hata ayıklayın
- Donanım hızlandırma için yürütme sağlayıcı kaydını sağlayın

**Dağıtım Modu Düşünceleri**
- **Kendi Kendine İçerik Modu**: Daha büyük dağıtım boyutuyla tamamen desteklenir
- **Çerçeveye Bağımlı Mod**: Daha küçük ayak izi ancak paylaşılan çalışma zamanı gerektirir
- **Paketlenmemiş Uygulamalar**: Windows AI API'leri için artık desteklenmiyor
- Kendi kendine içerik ARM64 dağıtımı için `dotnet run -p:Platform=ARM64 -p:SelfContained=true` kullanın

**Performans Sorunları**
- Farklı donanım yapılandırmaları arasında uygulama performansını profilleyin
- AI işleme boru hatlarındaki darboğazları belirleyin
- Veri ön işleme ve son işleme işlemlerini optimize edin
- Performans izleme ve uyarı uygulayın

**Entegrasyon Zorlukları**
- Uygun hata yönetimi ile API entegrasyon sorunlarını hata ayıklayın
- Giriş veri formatlarını ve ön işleme gereksinimlerini doğrulayın
- Kenar durumları ve hata koşullarını kapsamlı bir şekilde test edin
- Üretim sorunlarını hata ayıklamak için kapsamlı günlük kaydı uygulayın

### Hata Ayıklama Araçları ve Teknikleri

**Visual Studio Entegrasyonu**
- Model yürütme analizi için AI Toolkit hata ayıklayıcıyı kullanın
- AI işlemleri için performans profilleme uygulayın
- Uygun istisna yönetimi ile asenkron AI işlemlerini hata ayıklayın
- Optimizasyon için bellek profilleme araçlarını kullanın

**Windows AI Foundry Araçları**
- Model testi ve doğrulama için Foundry Local CLI'den yararlanın
- Entegrasyon doğrulaması için Windows AI API test araçlarını kullanın
- AI işlem izleme için özel günlük kaydı uygulayın
- AI işlevselliği güvenilirliği için otomatik testler oluşturun

## Uygulamalarınızı Geleceğe Hazırlama

### Gelişen Teknolojiler

**Yeni Nesil Donanım**
- Gelecekteki NPU yeteneklerinden yararlanacak uygulamalar tasarlayın
- Artan model boyutları ve karmaşıklığı için plan yapın
- Gelişen donanım için uyarlanabilir mimariler uygulayın
- Gelecekteki uyumluluk için kuantum hazır algoritmaları düşünün

**Gelişmiş AI Yetenekleri**
- Daha fazla veri türü arasında çok modlu AI entegrasyonu için hazırlanın
- Birden fazla cihaz arasında gerçek zamanlı işbirlikçi AI planlayın
- Federated learning yetenekleri için tasarım yapın
- Edge-bulut hibrit zeka mimarilerini düşünün

### Sürekli Öğrenme ve Uyarlama

**Model Güncellemeleri**
- Sorunsuz model güncelleme mekanizmaları uygulayın
- Geliştirilmiş model yeteneklerine uyum sağlayacak uygulamalar tasarlayın
- Mevcut modellerle geriye dönük uyumluluk
- [Windows ML Genel Bakış](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK Sistem Gereksinimleri](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK Geliştirme Ortamı Kurulumu](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Örnek Depolar ve Kod
- [Windows App SDK Örnekleri - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Örnekleri - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Çıkarım Örnekleri](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Örnekleri Deposu](https://github.com/microsoft/WindowsAppSDK-Samples)

### Geliştirme Araçları
- [Visual Studio Code için AI Araç Seti](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Geliştirici Galerisi](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Örnekleri](https://learn.microsoft.com/windows/ai/samples/)
- [Model Dönüştürme Araçları](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Teknik Destek
- [Windows ML Belgeleri](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Belgeleri](https://onnxruntime.ai/docs/)
- [Windows App SDK Belgeleri](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Sorun Bildir - Windows App SDK Örnekleri](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Topluluk ve Destek
- [Windows Geliştirici Topluluğu](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogu](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Eğitimi](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Bu rehber, hızla gelişen Windows AI ekosistemine uyum sağlamak için tasarlanmıştır. Düzenli güncellemeler, en son platform yetenekleri ve geliştirme en iyi uygulamalarıyla uyumu garanti eder.*

[08. Microsoft Foundry Local ile Pratik - Tam Geliştirici Araç Seti](../Module08/README.md)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.