# Windows Edge AI Geliştirme Rehberi

## Giriş

Windows Edge AI Geliştirmeye hoş geldiniz - Microsoft'un Windows AI Foundry platformunu kullanarak cihaz üzerindeki yapay zekanın gücünü kullanan akıllı uygulamalar oluşturmanız için kapsamlı rehberiniz. Bu rehber, uygulamalarına en yeni Edge AI yeteneklerini entegre etmek isteyen ve Windows donanım hızlandırmasının tüm yelpazesinden yararlanmak isteyen Windows geliştiricileri için özel olarak tasarlanmıştır.

### Windows AI Avantajı

Windows AI Foundry, model seçimi ve ince ayardan CPU, GPU, NPU ve hibrit bulut mimarileri arasında optimizasyon ve dağıtıma kadar tam AI geliştirici yaşam döngüsünü destekleyen birleşik, güvenilir ve güvenli bir platformu temsil eder. Bu platform, AI geliştirmeyi demokratikleştirir ve şunları sağlar:

- **Donanım Soyutlama**: AMD, Intel, NVIDIA ve Qualcomm silikonları arasında sorunsuz dağıtım
- **Cihaz Üzerinde Zekâ**: Gizliliği koruyan, tamamen yerel donanım üzerinde çalışan AI
- **Optimize Edilmiş Performans**: Windows donanım yapılandırmaları için önceden optimize edilmiş modeller
- **Kurumsal Hazır**: Üretim düzeyi güvenlik ve uyumluluk özellikleri

### Windows ML 
Windows Makine Öğrenimi (ML), C#, C++ ve Python geliştiricilerinin, farklı donanımlar (CPU'lar, GPU'lar, NPU'lar) için otomatik yürütücü yönetimi ile ONNX Runtime aracılığıyla Windows PC'lerde yerel olarak ONNX AI modellerini çalıştırmalarını sağlar. [ONNX Runtime](https://onnxruntime.ai/docs/) PyTorch, Tensorflow/Keras, TFLite, scikit-learn ve diğer çerçevelerden modellerle kullanılabilir.


![WindowsML Cihaz üzerinde çalışan bir ONNX modelinin Windows ML aracılığıyla NPU'lara, GPU'lara ve CPU'lara ulaştığını gösteren bir diyagram.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML, ONNX Runtime'ın Windows çapında paylaşılan bir kopyasını ve yürütücü sağlayıcıları (EP'ler) dinamik olarak indirme yeteneğini sağlar.

### Neden Edge AI için Windows?

**Evrensel Donanım Desteği**
Windows ML, tüm Windows ekosisteminde otomatik donanım optimizasyonu sunar, böylece AI uygulamalarınız altta yatan silikon mimarisinden bağımsız olarak en iyi performansı gösterir.

**Entegre AI Çalışma Zamanı**
Yerleşik Windows ML çıkarım motoru, karmaşık kurulum gereksinimlerini ortadan kaldırır ve geliştiricilerin altyapı kaygıları yerine uygulama mantığına odaklanmasını sağlar.

**Copilot+ PC Optimizasyonu**
Özel olarak Sinirsel İşleme Birimleri (NPU'lar) ile donatılmış yeni nesil Windows cihazları için tasarlanmış özel API'ler, watt başına olağanüstü performans sunar.

**Geliştirici Ekosistemi**
Visual Studio entegrasyonu, kapsamlı dokümantasyon ve geliştirme döngülerini hızlandıran örnek uygulamalar dahil zengin araçlar.

## Öğrenme Hedefleri

Bu Windows Edge AI geliştirme rehberini tamamlayarak, Windows platformunda üretime hazır AI uygulamaları oluşturmak için temel becerilere hakim olacaksınız.

### Temel Teknik Yeterlilikler

**Windows AI Foundry Ustalığı**
- Windows AI Foundry platformunun mimarisini ve bileşenlerini anlayın
- Windows ekosistemindeki tam AI geliştirme yaşam döngüsünde gezinme
- Cihaz üzerindeki AI uygulamaları için güvenlik en iyi uygulamalarını uygulama
- Farklı Windows donanım yapılandırmaları için uygulamaları optimize etme

**API Entegrasyonu Uzmanlığı**
- Metin, görsel ve multimodal uygulamalar için Windows AI API'lerini ustaca kullanma
- Metin üretimi ve muhakeme için Phi Silica dil modeli entegrasyonunu uygulama
- Yerleşik görüntü işleme API'leriyle bilgisayarla görme yetenekleri dağıtma
- LoRA (Düşük Dereceli Uyarlama) teknikleriyle önceden eğitilmiş modelleri özelleştirme

**Foundry Yerel Uygulama**
- Foundry Local CLI kullanarak açık kaynak dil modellerini inceleyin, değerlendirin ve dağıtın
- Yerel dağıtım için model optimizasyonu ve kantlaştırmayı anlayın
- İnternet bağlantısı olmadan çalışan çevrimdışı AI özelliklerini uygulayın
- Üretim ortamlarında model yaşam döngülerini ve güncellemelerini yönetin

**Windows ML Dağıtımı**
- Özel ONNX modellerini Windows uygulamalarına Windows ML kullanarak getirin
- CPU, GPU ve NPU mimarileri arasında otomatik donanım hızlandırmasından yararlanın
- Optimal kaynak kullanımıyla gerçek zamanlı çıkarım uygulayın
- Çeşitli Windows cihaz kategorileri için ölçeklenebilir AI uygulamaları tasarlayın

### Uygulama Geliştirme Becerileri

**Çapraz Platform Windows Geliştirme**
- Evrensel Windows dağıtımı için .NET MAUI kullanarak AI destekli uygulamalar oluşturun
- Win32, UWP ve İlerleyen Web Uygulamalarına AI yetenekleri entegre edin
- AI işlem durumlarına uyum sağlayan duyarlı kullanıcı arayüzü tasarımları uygulayın
- Asenkron AI işlemlerini uygun kullanıcı deneyimi desenleri ile yönetin

**Performans Optimizasyonu**
- Farklı donanım yapılandırmalarında AI çıkarım performansını profilleyin ve optimize edin
- Büyük dil modelleri için verimli bellek yönetimi uygulayın
- Mevcut donanım yeteneklerine göre düzgün şekilde düşen uygulamalar tasarlayın
- Sık kullanılan AI işlemleri için önbellekleme stratejileri uygulayın

**Üretime Hazırlık**
- Kapsamlı hata işleme ve yedekleme mekanizmaları uygulayın
- AI uygulama performansı için telemetri ve izleme tasarlayın
- Yerel AI model depolama ve yürütme için güvenlik en iyi uygulamalarını uygulayın
- Kurumsal ve tüketici uygulamaları için dağıtım stratejileri planlayın

### İş ve Stratejik Anlayış

**AI Uygulama Mimarisi**
- Yerel ve bulut AI işlemleri arasında optimizasyon sağlayan hibrit mimariler tasarlayın
- Model boyutu, doğruluk ve çıkarım hızı arasında ticari kararları değerlendirin
- Gizliliği korurken zekâ sağlayan veri akış mimarilerini planlayın
- Kullanıcı talepleriyle ölçeklenen maliyet-etkin AI çözümleri uygulayın

**Pazar Konumlandırması**
- Windows'a özgü AI uygulamalarının rekabet avantajlarını anlayın
- Cihaz üzerindeki AI'nın üstün kullanıcı deneyimleri sunduğu kullanım durumlarını belirleyin
- AI geliştirilmiş Windows uygulamaları için pazara giriş stratejileri geliştirin
- Uygulamaları Windows ekosistemi avantajlarından yararlanacak şekilde konumlandırın

## Windows App SDK AI Örnekleri

Windows App SDK, AI entegrasyonunu çoklu çerçeveler ve dağıtım senaryoları üzerinden gösteren kapsamlı örnekler sunar. Bu örnekler, Windows AI geliştirme kalıplarını anlamak için temel referanslardır.

### Windows AI Foundry Örnekleri

| Örnek | Çerçeve | Odak Alanı | Ana Özellikler |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API Entegrasyonu | Windows AI API'lerini gösteren tam WinUI uygulaması, ARM64 optimizasyonu, paketlenmiş dağıtım |

**Temel Teknolojiler:**
- Windows AI API'leri
- WinUI 3 çerçevesi
- ARM64 platform optimizasyonu
- Copilot+ PC uyumluluğu
- Paketlenmiş uygulama dağıtımı

**Ön Gereksinimler:**
- Copilot+ PC ile Windows 11 önerilir
- Visual Studio 2022
- ARM64 derleme yapılandırması
- Windows App SDK 1.8.1+

### Windows ML Örnekleri

#### C++ Örnekleri

| Örnek | Tür | Odak Alanı | Ana Özellikler |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Temel Windows ML | EP keşfi, komut satırı seçenekleri, model derleme |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Çerçeve Dağıtımı | Paylaşılan çalışma zamanı, daha küçük dağıtım boyutu |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsol Uygulaması | Tam Bağımsız Dağıtım | Bağımsız dağıtım, çalışma zamanı bağımlılığı yok |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Kütüphane Kullanımı | Paylaşılan kütüphanede WindowsML, bellek yönetimi |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Eğitimi | Model dönüşümü, EP derlemesi, Build 2025 eğitimi |

#### C# Örnekleri

**Konsol Uygulamaları**

| Örnek | Tür | Odak Alanı | Ana Özellikler |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsol Uygulaması | Temel C# Entegrasyonu | Paylaşılan yardımcı kullanım, komut satırı arayüzü |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Eğitimi | Model dönüşümü, EP derlemesi, Build 2025 eğitimi |

**GUI Uygulamaları**

| Örnek | Çerçeve | Odak Alanı | Ana Özellikler |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Masaüstü GUI | WPF arayüzü ile görüntü sınıflandırma |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Geleneksel GUI | Windows Forms ile görüntü sınıflandırma |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | WinUI 3 arayüzü ile görüntü sınıflandırma |

#### Python Örnekleri

| Örnek | Dil | Odak Alanı | Ana Özellikler |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Görüntü Sınıflandırma | WinML Python bağlayıcıları, toplu görüntü işleme |

### Örnek Ön Gereksinimleri

**Sistem Gereksinimleri:**
- Sürüm 24H2 (yapı 26100) veya üstü çalışan Windows 11 PC
- C++ ve .NET iş yükleri ile Visual Studio 2022
- Windows App SDK 1.8.1 veya üstü
- x64 ve ARM64 cihazlarda Python 3.10-3.13 (Python örnekleri için)

**Windows AI Foundry Özel:**
- Optimal performans için Copilot+ PC önerilir
- Windows AI örnekleri için ARM64 derleme yapılandırması
- Paket kimliği gereklidir (paketsiz uygulamalar artık desteklenmemektedir)

### Yaygın Örnek İş Akışı

Çoğu Windows ML örneği aşağıdaki standart kalıbı izler:

1. **Ortamı Başlat** - ONNX Runtime ortamı oluşturun
2. **Yürütme Sağlayıcıları Kaydet** - Mevcut donanım hızlandırıcılarını (CPU, GPU, NPU) keşfedin ve kaydedin
3. **Modeli Yükle** - ONNX modelini yükleyin, isteğe bağlı olarak hedef donanım için derleyin
4. **Girdiyi Önişleme** - Görüntüleri/verileri modele uygun formata dönüştürün
5. **Çıkarımı Çalıştır** - Modeli çalıştırın ve tahminleri alın
6. **Sonuçları İşle** - softmax uygulayın ve üst tahminleri gösterin

### Kullanılan Model Dosyaları

| Model | Amaç | Dahil Edildi | Notlar |
|-------|---------|----------|-------|
| SqueezeNet | Hafif görüntü sınıflandırma | ✅ Dahil | Önceden eğitilmiş, kullanıma hazır |
| ResNet-50 | Yüksek doğruluklu görüntü sınıflandırma | ❌ Dönüşüm gerektirir | Dönüşüm için [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) kullanın |

### Donanım Desteği

Tüm örnekler mevcut donanımı otomatik olarak algılar ve kullanır:
- **CPU** - Tüm Windows cihazlarında evrensel destek
- **GPU** - Mevcut grafik donanımı için otomatik algılama ve optimizasyon
- **NPU** - Desteklenen cihazlarda Sinirsel İşleme Birimlerinden yararlanır (Copilot+ PC'ler)

## Windows AI Foundry Platform Bileşenleri

### 1. Windows AI API'leri

Windows AI API'leri, minimal kurulumla Copilot+ PC cihazlarında verimlilik ve performans için optimize edilmiş, cihaz üzeri modellerle çalışan kullanıma hazır AI özellikleri sağlar.

#### Temel API Kategorileri

**Phi Silica Dil Modeli**
- Metin üretimi ve muhakeme için küçük ama güçlü dil modeli
- Minimal güç tüketimiyle gerçek zamanlı çıkarım için optimize edilmiş
- LoRA teknikleri kullanılarak özel ince ayar desteği
- Windows anlamsal arama ve bilgi getirimi ile entegrasyon

**Bilgisayarla Görme API’leri**
- **Metin Tanıma (OCR)**: Görüntülerden yüksek doğrulukta metin çıkarma
- **Görüntü Yüksek Çözünürlük**: Yerel AI modelleri kullanarak görüntüleri büyütme
- **Görüntü Segmentasyonu**: Görüntülerde belirli nesneleri tanımlama ve izole etme
- **Görüntü Açıklaması**: Görsel içerik için ayrıntılı metinsel açıklamalar oluşturma
- **Nesne Silme**: AI destekli boyama ile istenmeyen nesneleri görüntülerden kaldırma

**Multimodal Yetenekler**
- **Görsel-Dil Entegrasyonu**: Metin ve görüntü anlayışını birleştirme
- **Anlamsal Arama**: Multimedya içeriklerinde doğal dil sorguları etkinleştirme
- **Bilgi Getirimi**: Yerel verilerle akıllı arama deneyimleri oluşturma

### 2. Foundry Local

Foundry Local, geliştiricilere Windows Silikon üzerinde kullanıma hazır açık kaynak dil modellerine hızlı erişim sağlar; modelleri inceleme, test etme, etkileşimde bulunma ve yerel uygulamalarda dağıtma olanağı sunar.

#### Foundry Local Örnek Uygulamaları

[Foundry Local deposu](https://github.com/microsoft/Foundry-Local/tree/main/samples), çeşitli programlama dillerinde ve çerçevelerde kapsamlı örnekler sunar; çeşitli entegrasyon kalıplarını ve kullanım durumlarını gösterir.

| Örnek | Dil/Çerçeve | Odak Alanı | Ana Özellikler |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Uygulaması | Anlamsal Kernel entegrasyonu, Qdrant vektör deposu, JINA gömme, belge alma, akış sohbeti |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Masaüstü Sohbet Uygulaması | Çok platformlu sohbet, yerel/bulut model geçişi, OpenAI SDK entegrasyonu, gerçek zamanlı akış |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Temel Entegrasyon | Basit SDK kullanımı, model başlatma, temel sohbet işlevi |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Temel Entegrasyon | Python SDK kullanımı, akış yanıtları, OpenAI uyumlu API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistem Entegrasyonu | Düşük seviyeli SDK kullanımı, eşzamansız işlemler, reqwest HTTP istemcisi |

#### Kullanım Amacına Göre Örnek Kategorileri

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Semantic Kernel, Qdrant vektör veritabanı ve JINA gömme teknikleri kullanılarak tam RAG uygulaması
- **Mimari**: Belge alımı → Metin parçalama → Vektör gömmeleri → Benzerlik araması → Bağlama duyarlı yanıtlar
- **Teknolojiler**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX gömmeleri, akışlı sohbet tamamlama

**Masaüstü Uygulamaları**
- **electron/foundry-chat**: Yerel/bulut model geçişi ile üretim hazır sohbet uygulaması
- **Özellikler**: Model seçici, akışlı yanıtlar, hata yönetimi, çapraz platform dağıtımı
- **Mimari**: Electron ana işlemi, IPC iletişimi, güvenli preload betikleri

**SDK Entegrasyon Örnekleri**
- **JavaScript (Node.js)**: Temel model etkileşimi ve akışlı yanıtlar
- **Python**: OpenAI uyumlu API kullanımı ve eşzamansız akış
- **Rust**: reqwest ve tokio ile düşük seviyeli entegrasyon ve eşzamansız işlemler

#### Foundry Local Örnekleri için Önkoşullar

**Sistem Gereksinimleri:**
- Foundry Local yüklü Windows 11
- JavaScript/Electron örnekleri için Node.js v16+
- C# örnekleri için .NET 8.0+
- Python örnekleri için Python 3.10+
- Rust örnekleri için Rust 1.70+

**Kurulum:**
```powershell
# Foundry Local'ı kur
winget install Microsoft.FoundryLocal

# Kurulumu doğrula
foundry --version
foundry model list
```

#### Örneklere Özel Kurulum

**dotNET RAG Örneği:**
```powershell
# Gerekli paketleri NuGet üzerinden yükleyin
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Qdrant vektör veritabanını başlat
docker run -p 6333:6333 qdrant/qdrant

# Jupyter defterini çalıştır
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat Örneği:**
```powershell
# Bulut yedekleme için ortam değişkenlerini ayarla
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Bağımlılıkları yükle ve çalıştır
npm install
npm start
```

**JavaScript/Python/Rust Örnekleri:**
```powershell
# Modeli indir (phi-3.5-mini örneği)
foundry model run phi-3.5-mini

# İlgili örneği çalıştır
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Temel Özellikler

**Model Kataloğu**
- Önceden optimize edilmiş açık kaynak modellerin kapsamlı koleksiyonu
- CPU, GPU ve NPU'larda hemen dağıtım için optimize edilmiş modeller
- Llama, Mistral, Phi ve özel alan modelleri dahil popüler model aileleri desteği

**CLI Entegrasyonu**
- Model yönetimi ve dağıtımı için komut satırı arayüzü
- Otomatik optimizasyon ve kuantizasyon iş akışları
- Popüler geliştirme ortamları ve CI/CD boru hatları ile entegrasyon

**Yerel Dağıtım**
- Bulut bağımlılığı olmayan tam çevrimdışı operasyon
- Özelleştirilmiş model formatları ve yapılandırmalar için destek
- Otomatik donanım optimizasyonlu verimli model servisi

### 3. Windows ML

Windows ML, Windows üzerinde çekirdek AI platformu ve entegre çıkarım çalışma zamanı olarak hizmet vererek, geliştiricilerin özel modelleri geniş Windows donanım ekosistemi genelinde verimli şekilde dağıtmasını sağlar.

#### Mimari Avantajlar

**Evrensel Donanım Desteği**
- AMD, Intel, NVIDIA ve Qualcomm silikonları için otomatik optimizasyon
- CPU, GPU ve NPU çalıştırma desteği ve şeffaf geçiş
- Platforma özgü optimizasyon çalışmalarını ortadan kaldıran donanım soyutlaması

**Model Esnekliği**
- Popüler frameworklerden otomatik dönüşüm ile ONNX model formatı desteği
- Üretim kalitesinde performansla özel model dağıtımı
- Mevcut Windows uygulama mimarileriyle entegrasyon

**Kurumsal Entegrasyon**
- Windows güvenlik ve uyumluluk çerçeveleriyle uyumlu
- Kurumsal dağıtım ve yönetim araçları desteği
- Windows cihaz yönetimi ve izleme sistemleriyle entegrasyon

## Geliştirme İş Akışı

### Aşama 1: Ortam Kurulumu ve Araç Yapılandırması

**Geliştirme Ortamı Hazırlığı**
1. C++ ve .NET iş yükleri ile Visual Studio 2022'yi kurun
2. Windows App SDK 1.8.1 veya sonrasını kurun
3. Windows AI Foundry CLI araçlarını yapılandırın
4. Visual Studio Code için AI Toolkit eklentisini kurun
5. Performans profil oluşturma ve izleme araçlarını kurun
6. Copilot+ PC optimizasyonu için ARM64 yapı yapılandırmasını sağlayın

**Örnek Depo Kurulumu**
1. [Windows App SDK Örnekleri deposunu](https://github.com/microsoft/WindowsAppSDK-Samples) klonlayın
2. Windows AI API örnekleri için `Samples/WindowsAIFoundry/cs-winui` dizinine gidin
3. Kapsamlı Windows ML örnekleri için `Samples/WindowsML` dizinine gidin
4. Hedef platformlar için [derleme gereksinimlerini](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) inceleyin

**AI Dev Galeri Keşfi**
- Örnek uygulamalar ve referans uygulamaları keşfedin
- Etkileşimli demolarla Windows AI API'lerini test edin
- Kaynak kodu en iyi uygulamalar ve desenler açısından inceleyin
- Özel kullanım senaryolarınız için ilgili örnekleri belirleyin

### Aşama 2: Model Seçimi ve Entegrasyon

**Gereksinim Analizi**
- AI yetenekleri için fonksiyonel gereksinimleri tanımlayın
- Performans kısıtlamaları ve optimizasyon hedeflerini belirleyin
- Gizlilik ve güvenlik gereksinimlerini değerlendirin
- Dağıtım mimarisi ve ölçeklendirme stratejilerini planlayın

**Model Değerlendirmesi**
- Kullanım durumunuz için açık kaynak modelleri Foundry Local ile test edin
- Windows AI API'lerini özel model gereksinimleriyle karşılaştırın
- Model boyutu, doğruluk ve çıkarım hızı arasındaki dengeyi değerlendirin
- Seçilen modeller ile entegrasyon prototipleri oluşturun

### Aşama 3: Uygulama Geliştirme

**Çekirdek Entegrasyon**
- Windows AI API entegrasyonunu uygun hata yönetimi ile uygulayın
- AI işlem iş akışlarını destekleyen kullanıcı arayüzleri tasarlayın
- Model çıkarımı için önbellekleme ve optimizasyon stratejileri uygulayın
- AI işlem performansı için telemetri ve izleme ekleyin

**Test ve Doğrulama**
- Farklı Windows donanım yapılandırmalarında uygulamaları test edin
- Çeşitli yük koşullarında performans metriklerini doğrulayın
- AI fonksiyon güvenilirliği için otomatik testler uygulayın
- AI destekli özelliklerle kullanıcı deneyimi testleri yapın

### Aşama 4: Optimizasyon ve Dağıtım

**Performans Optimizasyonu**
- Hedef donanım yapılandırmaları için uygulama performans profili oluşturun
- Bellek kullanımı ve model yükleme stratejilerini optimize edin
- Mevcut donanım özelliklerine göre uyarlanabilir davranışlar uygulayın
- Farklı performans senaryoları için kullanıcı deneyimini iyileştirin

**Üretim Dağıtımı**
- AI model bağımlılıklarıyla birlikte uygulamaları paketleyin
- Model ve uygulama mantığı için güncelleme mekanizmalarını uygulayın
- Üretim ortamları için izleme ve analiz yapılandırın
- Kurumsal ve tüketici dağıtımları için yaygınlaştırma stratejileri planlayın

## Pratik Uygulama Örnekleri

### Örnek 1: Akıllı Belge İşleme Uygulaması

Bir Windows uygulaması oluşturun; belgeleri birden çok AI yeteneğiyle işlesin:

**Kullanılan Teknolojiler:**
- Belge özetleme ve soru yanıtlama için Phi Silica
- Tarama belgelerden metin çıkarmak için OCR API'leri
- Grafik ve diyagram analizi için Görüntü Tanımlama API'leri
- Belge sınıflandırması için özel ONNX modelleri

**Uygulama Yaklaşımı:**
- Tak-çıkar AI bileşenleri ile modüler mimari tasarlayın
- Büyük belge grupları için eşzamansız işlem uygulayın
- Uzun süren işlemler için ilerleme göstergeleri ve iptal desteği ekleyin
- Hassas belge işleme için çevrimdışı yetenek dahil edin

### Örnek 2: Perakende Stok Yönetim Sistemi

Perakende uygulamaları için AI destekli stok sistemi oluşturun:

**Kullanılan Teknolojiler:**
- Ürün tanımlama için Görüntü Bölütleme
- Marka ve kategori sınıflandırması için özel görsel modeller
- Foundry Local ile özel perakende dil modelleri dağıtımı
- Mevcut POS ve stok sistemleri ile entegrasyon

**Uygulama Yaklaşımı:**
- Gerçek zamanlı ürün taraması için kamera entegrasyonu oluşturun
- Barkod ve görsel ürün tanıma uygulayın
- Yerel dil modelleri ile doğal dil stok sorguları ekleyin
- Çoklu mağaza dağıtımı için ölçeklenebilir mimari tasarlayın

### Örnek 3: Sağlık Belgeleri Asistanı

Gizliliği koruyan sağlık dokümantasyon aracı geliştirin:

**Kullanılan Teknolojiler:**
- Tıbbi not oluşturma ve klinik karar desteği için Phi Silica
- El yazısı tıbbi kayıtları dijitalleştirmek için OCR
- Windows ML ile dağıtılmış özel tıbbi dil modelleri
- Tıbbi bilgi erişimi için yerel vektör depolama

**Uygulama Yaklaşımı:**
- Hasta gizliliği için tam çevrimdışı çalışmayı sağlayın
- Tıbbi terminoloji doğrulama ve öneriler uygulayın
- Düzenleyici uyumluluk için denetim günlüğü ekleyin
- Mevcut Elektronik Sağlık Kayıt sistemleri ile entegrasyon tasarlayın

## Performans Optimizasyon Stratejileri

### Donanım Farkındalıklı Geliştirme

**NPU Optimizasyonu**
- Copilot+ PC'lerde NPU yeteneklerini kullanacak uygulamalar tasarlayın
- NPU olmayan cihazlarda GPU/CPU'ya yumuşak geçiş uygulayın
- NPU'ya özgü hızlandırma için model formatlarını optimize edin
- NPU kullanım ve termal özelliklerini izleyin

**Bellek Yönetimi**
- Verimli model yükleme ve önbellekleme stratejileri uygulayın
- Başlangıç süresini azaltmak için büyük modeller için bellek eşlemeyi kullanın
- Kaynak kısıtlı cihazlar için bellek dostu uygulamalar tasarlayın
- Bellek optimizasyonu için model kuantizasyonu uygulayın

**Pil Verimliliği**
- Minimum güç tüketimi için AI işlemlerini optimize edin
- Pil durumuna göre uyarlanabilir işlem uygulayın
- Sürekli AI işlemleri için verimli arka plan işlemi tasarlayın
- Enerji kullanımını optimize etmek için güç profil araçlarını kullanın

### Ölçeklenebilirlik Dikkatleri

**Çoklu İş Parçacığı**
- Eşzamanlı işlem için iş parçacığı güvenli AI işlemleri tasarlayın
- Mevcut çekirdekler arasında verimli iş dağılımı uygulayın
- Engellemeyen AI işlemleri için async/await desenlerini kullanın
- Farklı donanım yapılandırmaları için iş parçacığı havuzu optimizasyonu planlayın

**Önbellekleme Stratejileri**
- Sık kullanılan AI işlemleri için akıllı önbellekleme uygulayın
- Model güncellemeleri için önbellek geçersiz kılma stratejileri tasarlayın
- Maliyetli ön işleme işlemleri için kalıcı önbellekleme kullanın
- Çok kullanıcılı senaryolar için dağıtılmış önbellekleme uygulayın

## Güvenlik ve Gizlilik En İyi Uygulamaları

### Veri Koruma

**Yerel İşleme**
- Hassas verilerin asla yerel cihaz dışına çıkmamasını sağlayın
- AI modelleri ve geçici veriler için güvenli depolama uygulayın
- Uygulama sandboxing için Windows güvenlik özelliklerini kullanın
- Saklanan modeller ve ara işlem sonuçları için şifreleme uygulayın

**Model Güvenliği**
- Yükleme ve yürütme öncesi model bütünlüğünü doğrulayın
- Güvenli model güncelleme mekanizmaları uygulayın
- Müdahaleyi önlemek için imzalı modeller kullanın
- Model dosyaları ve yapılandırma için erişim kontrolleri uygulayın

### Uyumluluk Dikkatleri

**Düzenleyici Uyum**
- GDPR, HIPAA ve diğer düzenleyici gereksinimlere uygun uygulamalar tasarlayın
- AI karar süreçleri için denetim kaydı ekleyin
- AI tarafından üretilen sonuçlar için şeffaflık özellikleri sağlayın
- AI veri işleme üzerinde kullanıcı kontrolü mümkün kılın

**Kurumsal Güvenlik**
- Windows kurumsal güvenlik politikalarıyla entegrasyon sağlayın
- Kurumsal yönetim araçları ile yönetilen dağıtımı destekleyin
- AI özellikleri için rol tabanlı erişim kontrolleri uygulayın
- AI işlevselliği için yönetim kontrolü sağlayın

## Sorun Giderme ve Hata Ayıklama

### Yaygın Geliştirme Zorlukları

**Derleme Yapılandırması Sorunları**
- Windows AI API örnekleri için ARM64 platform yapılandırmasını sağlayın
- Windows App SDK sürüm uyumluluğunu doğrulayın (1.8.1+ gerekli)
- Paket kimliğinin Windows AI API'leri için uygun yapılandırıldığını kontrol edin
- Hedef framework sürümünü destekleyen yapı araçlarını doğrulayın

**Model Yükleme Sorunları**
- Windows ML ile ONNX model uyumluluğunu doğrulayın
- Model dosyası bütünlüğü ve format gereksinimlerini kontrol edin
- Belirli modeller için donanım yetenek gereksinimlerini doğrulayın
- Model yükleme sırasında bellek tahsis sorunlarını hata ayıklayın
- Donanım hızlandırması için yürütme sağlayıcı kaydını sağlayın

**Dağıtım Modu Dikkatleri**
- **Self-Contained Mode**: Tam desteklenir; daha büyük dağıtım boyutu ile
- **Framework-Dependent Mode**: Daha küçük boyut ama paylaşılan çalışma zamanı gerektirir
- **Paketlenmemiş Uygulamalar**: Windows AI API'leri için artık desteklenmemektedir
- Self-contained ARM64 dağıtımı için `dotnet run -p:Platform=ARM64 -p:SelfContained=true` kullanın

**Performans Sorunları**
- Farklı donanım yapılandırmaları için uygulama performansı profili oluşturun
- AI işleme boru hatlarındaki darboğazları belirleyin
- Veri ön işleme ve son işleme işlemlerini optimize edin
- Performans izleme ve uyarı sistemleri uygulayın

**Entegrasyon Zorlukları**
- Doğru hata yönetimi ile API entegrasyon sorunlarını hata ayıklayın
- Girdi veri formatları ve ön işleme gereksinimlerini doğrulayın
- Uç durumlar ve hata koşullarını kapsamlı test edin
- Üretim sorunları için kapsamlı günlükleme uygulayın

### Hata Ayıklama Araçları ve Teknikleri

**Visual Studio Entegrasyonu**
- Model yürütme analizi için AI Toolkit hata ayıklayıcısını kullanın
- AI işlemleri için performans profil oluşturun
- Eşzamansız AI işlemlerini uygun istisna yönetimi ile hata ayıklayın
- Optimizasyon için bellek profil araçlarını kullanın

**Windows AI Foundry Araçları**
- Model testi ve doğrulama için Foundry Local CLI'dan faydalanın
- Entegrasyon doğrulaması için Windows AI API test araçlarını kullanın
- AI işlem izleme için özel günlükleme uygulayın
- AI fonksiyon güvenliği için otomatik testler oluşturun

## Uygulamalarınız İçin Geleceğe Hazırlık

### Gelişen Teknolojiler

**Yeni Nesil Donanım**
- Geleceğin NPU yeteneklerini kullanacak uygulamalar tasarlayın
- Artan model boyutları ve karmaşıklığını planlayın
- Gelişen donanımlara uyumlu uyarlanabilir mimariler uygulayın
- Geleceğe uyum için kuantum hazır algoritmaları göz önünde bulundurun

**Gelişmiş AI Yetenekleri**
- Daha fazla veri türü için çok modlu AI entegrasyonuna hazırlanın
- Çoklu cihazlar arasında gerçek zamanlı işbirlikçi AI planlayın
- Federated learning yetenekleri için tasarım yapın
- Kenar-bulut hibrit zeka mimarilerini değerlendirin

### Sürekli Öğrenme ve Uyarlama

**Model Güncellemeleri**
- Kesintisiz model güncelleme mekanizmaları uygulayın
- İyileşmiş model yeteneklerine uyum sağlamak için uygulamalar tasarlayın
- Mevcut modellerle geriye dönük uyumluluğu planlayın
- Model performans değerlendirmesi için A/B testleri uygulayın

**Özellik Gelişimi**
- Yeni AI yeteneklerini karşılayacak modüler mimariler tasarlayın
- Gelişmekte olan Windows AI API entegrasyonunu planlayın
- Kademeli yetenek yayılımı için özellik bayrakları uygulayın
- Gelişmiş AI özelliklerine uyumlu kullanıcı arayüzleri tasarlayın

## Sonuç

Windows Edge AI geliştirme, güçlü AI yeteneklerinin sağlam, güvenli ve ölçeklenebilir Windows platformu ile birleşmesini temsil eder. Windows AI Foundry ekosistemini ustalıkla kullanarak geliştiriciler, en yüksek gizlilik, güvenlik ve performans standartlarını korurken olağanüstü kullanıcı deneyimleri sunan akıllı uygulamalar yaratabilirler.

Windows AI API'leri, Foundry Local ve Windows ML birleşimi, bir sonraki nesil akıllı Windows uygulamalarını oluşturmak için eşsiz bir temel sağlar. AI geliştikçe, Windows platformu, uygulamalarınızın gelişen teknolojilere uyum sağlamasını ve çeşitli Windows donanım ekosisteminde uyumluluk ve performansı sürdürmesini garanti eder.

Tüketici uygulamaları, kurumsal çözümler veya özel sektör araçları geliştiriyor olun, Windows Edge AI geliştirme, modern Windows cihazlarının tam potansiyelini kullanarak akıllı, duyarlı ve derinlemesine entegre deneyimler yaratmanızı sağlar.

## Ek Kaynaklar

### Dokümantasyon ve Öğrenme
- [Windows AI Foundry Dokümantasyonu](https://learn.microsoft.com/windows/ai/)
- [Windows AI API'leri Referansı](https://learn.microsoft.com/windows/ai/apis/)
- [Windows AI API'leriyle uygulama oluşturma başlangıcı](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Başlarken](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Genel Bakış](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK Sistem Gereksinimleri](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windows Uygulama SDK Geliştirme Ortamı Kurulumu](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Örnek Depolar ve Kodlar
- [Windows Uygulama SDK Örnekleri - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows Uygulama SDK Örnekleri - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Çıkarım Örnekleri](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows Uygulama SDK Örnek Deposu](https://github.com/microsoft/WindowsAppSDK-Samples)

### Geliştirme Araçları
- [Visual Studio Code için AI Araç Seti](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Geliştirici Galerisi](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Örnekleri](https://learn.microsoft.com/windows/ai/samples/)
- [Model Dönüştürme Araçları](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Teknik Destek
- [Windows ML Dokümantasyonu](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokümantasyonu](https://onnxruntime.ai/docs/)
- [Windows Uygulama SDK Dokümantasyonu](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Sorun Bildir - Windows Uygulama SDK Örnekleri](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Topluluk ve Destek
- [Windows Geliştirici Topluluğu](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogu](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Eğitimi](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Bu rehber, hızla gelişen Windows AI ekosistemi ile birlikte evrimleşecek şekilde tasarlanmıştır. Düzenli güncellemeler, en son platform yetenekleri ve geliştirme en iyi uygulamaları ile uyumluluğu sağlar.*

[08. Microsoft Foundry Local ile Pratik - Tam Geliştirici Araç Seti](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->