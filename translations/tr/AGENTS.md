# AGENTS.md

> **EdgeAI için Başlangıç Seviyesinde Katkıda Bulunanlar İçin Geliştirici Kılavuzu**
> 
> Bu belge, bu depo ile çalışan geliştiriciler, AI ajanları ve katkıda bulunanlar için kapsamlı bilgiler sunar. Kurulum, geliştirme iş akışları, test ve en iyi uygulamaları kapsar.
> 
> **Son Güncelleme**: 30 Ekim 2025 | **Belge Sürümü**: 3.0

## İçindekiler

- [Proje Genel Bakış](../..)
- [Depo Yapısı](../..)
- [Ön Koşullar](../..)
- [Kurulum Komutları](../..)
- [Geliştirme İş Akışı](../..)
- [Test Talimatları](../..)
- [Kod Stili Yönergeleri](../..)
- [Pull Request Yönergeleri](../..)
- [Çeviri Sistemi](../..)
- [Foundry Local Entegrasyonu](../..)
- [Derleme ve Dağıtım](../..)
- [Yaygın Sorunlar ve Sorun Giderme](../..)
- [Ek Kaynaklar](../..)
- [Proje Özel Notları](../..)
- [Yardım Alma](../..)

## Proje Genel Bakış

EdgeAI for Beginners, Küçük Dil Modelleri (SLM) ile Edge AI geliştirmeyi öğreten kapsamlı bir eğitim deposudur. Kurs, EdgeAI temellerini, model dağıtımını, optimizasyon tekniklerini ve Microsoft Foundry Local ve çeşitli AI çerçevelerini kullanarak üretime hazır uygulamaları kapsar.

**Anahtar Teknolojiler:**
- Python 3.8+ (AI/ML örnekleri için birincil dil)
- .NET C# (AI/ML örnekleri)
- JavaScript/Node.js ve Electron (masaüstü uygulamaları için)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI Çerçeveleri: LangChain, Semantic Kernel, Chainlit
- Model Optimizasyonu: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Depo Türü:** 8 modül ve 10 kapsamlı örnek uygulama içeren eğitim içeriği deposu

**Mimari:** Edge AI dağıtım modellerini gösteren pratik örneklerle çok modüllü öğrenme yolu

## Depo Yapısı

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Ön Koşullar

### Gerekli Araçlar

- **Python 3.8+** - AI/ML örnekleri ve not defterleri için
- **Node.js 16+** - Electron örnek uygulaması için
- **Git** - Sürüm kontrolü için
- **Microsoft Foundry Local** - AI modellerini yerel olarak çalıştırmak için

### Önerilen Araçlar

- **Visual Studio Code** - Python, Jupyter ve Pylance uzantıları ile
- **Windows Terminal** - Daha iyi bir komut satırı deneyimi için (Windows kullanıcıları)
- **Docker** - Konteyner tabanlı geliştirme için (isteğe bağlı)

### Sistem Gereksinimleri

- **RAM**: Minimum 8GB, çoklu model senaryoları için 16GB+ önerilir
- **Depolama**: Modeller ve bağımlılıklar için 10GB+ boş alan
- **İşletim Sistemi**: Windows 10/11, macOS 11+ veya Linux (Ubuntu 20.04+)
- **Donanım**: AVX2 destekli CPU; GPU (CUDA, Qualcomm NPU) isteğe bağlı ancak önerilir

### Bilgi Ön Koşulları

- Temel Python programlama bilgisi
- Komut satırı arayüzlerine aşinalık
- AI/ML kavramlarını anlama (örnek geliştirme için)
- Git iş akışları ve pull request süreçleri

## Kurulum Komutları

### Depo Kurulumu

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python Örnek Kurulumu (Modül08 ve Atölye örnekleri)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.js Örnek Kurulumu (Örnek 08 - Windows Sohbet Uygulaması)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local Kurulumu

Foundry Local, örnekleri çalıştırmak için gereklidir. Resmi depodan indirin ve yükleyin:

**Kurulum:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuel**: [releases page](https://github.com/microsoft/Foundry-Local/releases) adresinden indirin

**Hızlı Başlangıç:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Not**: Foundry Local, donanımınıza en uygun model varyantını otomatik olarak seçer (CUDA GPU, Qualcomm NPU veya CPU).

## Geliştirme İş Akışı

### İçerik Geliştirme

Bu depo öncelikle **Markdown eğitim içeriği** içerir. Değişiklik yaparken:

1. İlgili modül dizinlerindeki `.md` dosyalarını düzenleyin
2. Mevcut biçimlendirme kalıplarını takip edin
3. Kod örneklerinin doğru ve test edilmiş olduğundan emin olun
4. Gerekirse ilgili çeviri içeriğini güncelleyin (veya otomasyona bırakın)

### Örnek Uygulama Geliştirme

Modül08 Python örnekleri (örnekler 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Atölye Python örnekleri için:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron örneği (örnek 08) için:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Örnek Uygulamaların Test Edilmesi

Python örneklerinde otomatik testler yoktur ancak çalıştırılarak doğrulanabilir:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron örneği test altyapısına sahiptir:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Test Talimatları

### İçerik Doğrulama

Depo, otomatik çeviri iş akışları kullanır. Çeviriler için manuel test gerekmez.

**İçerik değişiklikleri için manuel doğrulama:**
1. Markdown dosyalarını önizleyerek biçimlendirmeyi kontrol edin
2. Tüm bağlantıların geçerli hedeflere yönlendirildiğini doğrulayın
3. Belgelerdeki kod parçacıklarını test edin
4. Görsellerin doğru şekilde yüklendiğinden emin olun

### Örnek Uygulama Testi

**Modül08/örnekler/08 (Electron uygulaması) kapsamlı testlere sahiptir:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python örnekleri manuel olarak test edilmelidir:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Kod Stili Yönergeleri

### Markdown İçeriği

- Tutarlı başlık hiyerarşisi kullanın (# başlık için, ## ana bölümler için, ### alt bölümler için)
- Dil belirteçleriyle kod blokları ekleyin: ```python, ```bash, ```javascript
- Tablo, liste ve vurgu için mevcut biçimlendirmeyi takip edin
- Satırları okunabilir tutun (~80-100 karakter hedefleyin, ancak katı değil)
- Dahili referanslar için göreceli bağlantılar kullanın

### Python Kod Stili

- PEP 8 kurallarına uyun
- Uygun yerlerde tür ipuçları kullanın
- Fonksiyonlar ve sınıflar için docstring ekleyin
- Anlamlı değişken adları kullanın
- Fonksiyonları odaklı ve öz tutun

### JavaScript/Node.js Kod Stili

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Anahtar kurallar:**
- Örnek 08'de sağlanan ESLint yapılandırması
- Kod biçimlendirme için Prettier kullanımı
- Modern ES6+ sözdizimini kullanın
- Kod tabanındaki mevcut kalıpları takip edin

## Pull Request Yönergeleri

### Katkı İş Akışı

1. **Depoyu fork edin** ve `main` dalından yeni bir dal oluşturun
2. **Değişikliklerinizi yapın** kod stili yönergelerine uygun olarak
3. **Testleri eksiksiz uygulayın** yukarıdaki test talimatlarını kullanarak
4. **Açık mesajlarla commit yapın** konvansiyonel commit formatını takip ederek
5. **Fork'unuza push yapın** ve bir pull request oluşturun
6. **Gözden geçirme sırasında** bakımcıların geri bildirimlerine yanıt verin

### Dal Adlandırma Konvansiyonu

- `feature/<modül>-<açıklama>` - Yeni özellikler veya içerik için
- `fix/<modül>-<açıklama>` - Hata düzeltmeleri için
- `docs/<açıklama>` - Belge iyileştirmeleri için
- `refactor/<açıklama>` - Kod yeniden düzenleme için

### Commit Mesaj Formatı

[Conventional Commits](https://www.conventionalcommits.org/) formatını takip edin:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Örnekler:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Başlık Formatı
```
[ModuleXX] Brief description of change
```
veya
```
[Module08/samples/XX] Description for sample changes
```

### Davranış Kuralları

Tüm katkıda bulunanlar [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/) kurallarına uymalıdır. Katkıda bulunmadan önce lütfen [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) dosyasını inceleyin.

### Göndermeden Önce

**İçerik değişiklikleri için:**
- Düzenlenen tüm Markdown dosyalarını önizleyin
- Bağlantıların ve görsellerin çalıştığını doğrulayın
- Yazım hatalarını ve dilbilgisi hatalarını kontrol edin

**Örnek kod değişiklikleri için (Modül08/örnekler/08):**
```bash
npm run lint
npm test
```

**Python örnek değişiklikleri için:**
- Örneğin başarıyla çalıştığını test edin
- Hata işleme mekanizmasının çalıştığını doğrulayın
- Foundry Local ile uyumluluğu kontrol edin

### Gözden Geçirme Süreci

- Eğitim içeriği değişiklikleri doğruluk ve açıklık açısından gözden geçirilir
- Kod örnekleri işlevsellik açısından test edilir
- Çeviri güncellemeleri GitHub Actions tarafından otomatik olarak gerçekleştirilir

## Çeviri Sistemi

**ÖNEMLİ:** Bu depo, GitHub Actions aracılığıyla otomatik çeviri kullanır.

- Çeviriler `/translations/` dizininde bulunur (50+ dil)
- `co-op-translator.yml` iş akışı ile otomatikleştirilmiştir
- **Çeviri dosyalarını manuel olarak düzenlemeyin** - üzerine yazılacaktır
- Yalnızca kök ve modül dizinlerindeki İngilizce kaynak dosyaları düzenleyin
- Çeviriler `main` dalına yapılan push işlemiyle otomatik olarak oluşturulur

## Foundry Local Entegrasyonu

Çoğu Modül08 örneği, Microsoft Foundry Local'ın çalışmasını gerektirir.

### Kurulum ve Ayar

**Foundry Local'ı Yükleyin:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK'yı Yükleyin:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local'ı Başlatma
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK Kullanımı (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local'ı Doğrulama
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Örnekler için Ortam Değişkenleri

Çoğu örnek şu ortam değişkenlerini kullanır:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Not**: `FoundryLocalManager` kullanıldığında, SDK hizmet keşfi ve model yüklemeyi otomatik olarak yönetir. Model takma adları (örneğin `phi-3.5-mini`) donanımınız için en iyi varyantın seçilmesini sağlar.

## Derleme ve Dağıtım

### İçerik Dağıtımı

Bu depo ağırlıklı olarak belgelerden oluşur - içerik için bir derleme süreci gerekmez.

### Örnek Uygulama Derleme

**Electron Uygulaması (Modül08/örnekler/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python Örnekleri:**
Derleme süreci yok - örnekler doğrudan Python yorumlayıcısı ile çalıştırılır.

## Yaygın Sorunlar ve Sorun Giderme

> **İpucu**: Bilinen sorunlar ve çözümler için [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) adresini kontrol edin.

### Kritik Sorunlar (Engelleyici)

#### Foundry Local Çalışmıyor
**Sorun:** Örnekler bağlantı hatalarıyla başarısız oluyor

**Çözüm:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Yaygın Sorunlar (Orta)

#### Python Sanal Ortam Sorunları
**Sorun:** Modül ithalat hataları

**Çözüm:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron Derleme Sorunları
**Sorun:** npm install veya derleme hataları

**Çözüm:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### İş Akışı Sorunları (Hafif)

#### Çeviri İş Akışı Çakışmaları
**Sorun:** Çeviri PR'ı değişikliklerinizle çakışıyor

**Çözüm:**
- Yalnızca İngilizce kaynak dosyaları düzenleyin
- Otomatik çeviri iş akışının çevirileri yönetmesine izin verin
- Çakışmalar meydana gelirse, çeviriler birleştirildikten sonra `main` dalını dalınıza birleştirin

#### Model İndirme Hataları
**Sorun:** Foundry Local modelleri indiremiyor

**Çözüm:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Ek Kaynaklar

### Öğrenme Yolları
- **Başlangıç Yolu:** Modüller 01-02 (7-9 saat)
- **Orta Seviye Yolu:** Modüller 03-04 (9-11 saat)
- **İleri Seviye Yolu:** Modüller 05-07 (12-15 saat)
- **Uzman Yolu:** Modül 08 (8-10 saat)
- **Uygulamalı Atölye:** Atölye materyalleri (6-8 saat)

### Anahtar Modül İçeriği
- **Modül01:** EdgeAI temelleri ve gerçek dünya vaka çalışmaları
- **Modül02:** Küçük Dil Modeli (SLM) aileleri ve mimarileri
- **Modül03:** Yerel ve bulut dağıtım stratejileri
- **Modül04:** Birden fazla çerçeve ile model optimizasyonu (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modül05:** SLMOps - üretim operasyonları
- **Modül06:** AI ajanları ve fonksiyon çağrısı
- **Modül07:** Platforma özel uygulamalar
- **Modül08:** Foundry Local araç seti ile 10 kapsamlı örnek

### Harici Bağımlılıklar
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI uyumlu API ile yerel AI model çalışma zamanı
  - [Dokümantasyon](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimizasyon çerçevesi
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Model optimizasyon araç seti
- [OpenVINO](https://docs.openvino.ai/) - Intel'in optimizasyon araç seti

## Proje Özel Notları

### Modül08 Örnek Uygulamaları

Depo, 10 kapsamlı örnek uygulama içerir:

1. **01-REST Sohbet Hızlı Başlangıç** - Temel OpenAI SDK entegrasyonu
2. **02-OpenAI SDK Entegrasyonu** - Gelişmiş SDK özellikleri
3. **03-Model Keşfi ve Karşılaştırma** - Model karşılaştırma araçları
4. **04-Chainlit RAG Uygulaması** - Retrieval-augmented generation
5. **05-Çoklu Ajan Orkestrasyonu** - Temel ajan koordinasyonu
6. **06-Modelleri Araç Olarak Yönlendirme** - Akıllı model yönlendirme
7. **07-Direkt API İstemcisi** - Düşük seviyeli API entegrasyonu
8. **08-Windows 11 Sohbet Uygulaması** - Yerel Electron masaüstü uygulaması
9. **09-Gelişmiş Çoklu Ajan Sistemi** - Karmaşık ajan orkestrasyonu
10. **10-Dökümhane Araçları Çerçevesi** - LangChain/Semantic Kernel entegrasyonu

### Atölye Örnek Uygulamaları

Atölye, pratik uygulamalarla 6 aşamalı ilerleyen oturumlar içerir:

1. **Oturum 01** - Foundry Local entegrasyonu ile sohbet başlangıcı
2. **Oturum 02** - RAG hattı ve RAGAS ile değerlendirme
3. **Oturum 03** - Açık kaynak modellerin karşılaştırmalı analizi
4. **Oturum 04** - Model karşılaştırması ve seçimi
5. **Oturum 05** - Çoklu ajan orkestrasyon sistemleri
6. **Oturum 06** - Model yönlendirme ve hat yönetimi

Her örnek, Foundry Local ile uç yapay zeka geliştirme konusunun farklı yönlerini göstermektedir.

### Performans Dikkat Edilmesi Gerekenler

- SLM'ler uç cihazlarda çalıştırma için optimize edilmiştir (2-16GB RAM)
- Yerel çıkarım 50-500ms yanıt süreleri sağlar
- Kuantizasyon teknikleri %75 boyut azaltımı ve %85 performans koruması sağlar
- Yerel modellerle gerçek zamanlı konuşma yetenekleri

### Güvenlik ve Gizlilik

- Tüm işlem yerel olarak gerçekleşir - buluta veri gönderilmez
- Gizlilik hassas uygulamalar için uygundur (sağlık, finans)
- Veri egemenliği gereksinimlerini karşılar
- Foundry Local tamamen yerel donanımda çalışır

## Yardım Alma

### Dokümantasyon

- **Ana README**: [README.md](README.md) - Depo genel bakışı ve öğrenme yolları
- **Çalışma Kılavuzu**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Öğrenme kaynakları ve zaman çizelgesi
- **Destek**: [SUPPORT.md](SUPPORT.md) - Nasıl yardım alınır
- **Güvenlik**: [SECURITY.md](SECURITY.md) - Güvenlik sorunlarını bildirme

### Topluluk Desteği

- **GitHub Sorunları**: [Hata bildirin veya özellik talep edin](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Tartışmaları**: [Sorular sorun ve fikirlerinizi paylaşın](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Sorunları**: [Foundry Local ile ilgili teknik sorunlar](https://github.com/microsoft/Foundry-Local/issues)

### İletişim

- **Bakımcılar**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) dosyasına bakın
- **Güvenlik Sorunları**: [SECURITY.md](SECURITY.md) dosyasındaki sorumlu açıklama adımlarını takip edin
- **Microsoft Desteği**: Kurumsal destek için Microsoft müşteri hizmetleriyle iletişime geçin

### Ek Kaynaklar

- **Microsoft Learn**: [AI ve Makine Öğrenimi Öğrenme Yolları](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokümantasyonu**: [Resmi Belgeler](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Topluluk Örnekleri**: Topluluk katkılarını görmek için [GitHub Tartışmaları](https://github.com/microsoft/edgeai-for-beginners/discussions) bölümüne göz atın

---

**Bu, Uç Yapay Zeka geliştirme öğretimine odaklanan bir eğitim deposudur. Ana katkı modeli, eğitim içeriğini geliştirmek ve Uç Yapay Zeka kavramlarını gösteren örnek uygulamalar eklemek/geliştirmektir.**

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.