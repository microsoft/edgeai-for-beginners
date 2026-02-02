# Oturum 1: Foundry Local ile Başlangıç

## Özet

Microsoft Foundry Local kullanarak ilk yapay zeka modellerinizi nasıl kuracağınızı, yapılandıracağınızı ve çalıştıracağınızı öğrenin. Bu uygulamalı oturum, kurulumdan Phi-4, Qwen ve DeepSeek gibi modellerle ilk sohbet uygulamanızı oluşturmaya kadar yerel çıkarım için adım adım bir giriş sunar.

## Öğrenme Hedefleri

Bu oturumun sonunda:

- **Kurulum ve Yapılandırma**: Foundry Local'ı doğru bir şekilde kurup doğrulama yapmayı öğrenin
- **CLI İşlemlerinde Ustalaşma**: Foundry Local CLI'yi model yönetimi ve dağıtımı için kullanın
- **İlk Modelinizi Çalıştırın**: Yerel bir yapay zeka modelini başarıyla dağıtın ve etkileşimde bulunun
- **Sohbet Uygulaması Oluşturun**: Foundry Local Python SDK kullanarak temel bir sohbet uygulaması oluşturun
- **Yerel Yapay Zekayı Anlayın**: Yerel çıkarım ve model yönetiminin temellerini kavrayın

## Ön Koşullar

### Sistem Gereksinimleri

- **Windows**: Windows 11 (22H2 veya üstü) VEYA **macOS**: macOS 11+ (sınırlı destek)
- **RAM**: Minimum 8GB, önerilen 16GB+
- **Depolama**: Modeller için 10GB+ boş alan
- **Python**: 3.10 veya üstü kurulu
- **Yönetici Erişimi**: Kurulum için yönetici yetkileri

### Geliştirme Ortamı

- Python uzantısı ile Visual Studio Code (önerilir)
- Komut satırı erişimi (Windows'ta PowerShell, macOS'ta Terminal)
- Depoları klonlamak için Git (isteğe bağlı)

## Atölye Akışı (30 dakika)

### Adım 1: Foundry Local'ı Kurun (5 dakika)

#### Windows Kurulumu

Foundry Local'ı Windows paket yöneticisi kullanarak kurun:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatif: [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install) üzerinden doğrudan indirin

#### macOS Kurulumu (Sınırlı Destek)

> [!NOTE] 
> macOS desteği şu anda önizleme aşamasındadır. En son kullanılabilirlik için resmi belgeleri kontrol edin.

Homebrew kullanarak kurulum yapın:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOS kullanıcıları için alternatif:**
- Windows 11 VM (Parallels/UTM) kullanarak Windows adımlarını takip edin
- Mevcutsa bir konteyner üzerinden çalıştırın ve `FOUNDRY_LOCAL_ENDPOINT` yapılandırmasını yapın

### Adım 2: Kurulumu Doğrulayın (3 dakika)

Kurulumdan sonra terminalinizi yeniden başlatın ve Foundry Local'ın çalıştığını doğrulayın:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Beklenen çıktı, sürüm bilgilerini ve mevcut komutları göstermelidir.

### Adım 3: Python Ortamını Ayarlayın (5 dakika)

Bu atölye için özel bir Python ortamı oluşturun:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Adım 4: İlk Modelinizi Çalıştırın (7 dakika)

Şimdi ilk yapay zeka modelimizi yerel olarak çalıştıralım!

#### Phi-4 Mini ile Başlayın (Önerilen İlk Model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Bu komut modeli indirir (ilk kez) ve Foundry Local hizmetini otomatik olarak başlatır.

#### Çalışanları Kontrol Edin

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Farklı Modelleri Deneyin

Phi-4-mini çalıştıktan sonra diğer modelleri deneyin:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Adım 5: İlk Sohbet Uygulamanızı Oluşturun (10 dakika)

Şimdi başlattığımız modelleri kullanan bir Python uygulaması oluşturalım.

#### Sohbet Scriptini Oluşturun

`my_first_chat.py` adlı yeni bir dosya oluşturun (veya sağlanan örneği kullanın):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **İlgili Örnekler**: Daha gelişmiş kullanım için şunlara bakın:
>
> - **Python Örneği**: `Workshop/samples/session01/chat_bootstrap.py` - Akış yanıtları ve hata yönetimi içerir
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Ayrıntılı açıklamalarla interaktif versiyon

#### Sohbet Uygulamanızı Test Edin

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatif: Sağlanan örnekleri doğrudan kullanın

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Veya interaktif notebook'u keşfedin  
Workshop/notebooks/session01_chat_bootstrap.ipynb dosyasını VS Code'da açın

Bu örnek konuşmaları deneyin:

- "Microsoft Foundry Local nedir?"
- "Yerel yapay zeka modellerini çalıştırmanın 3 faydasını listele"
- "Edge AI'yi anlamama yardımcı ol"

## Başardıklarınız

Tebrikler! Başarıyla:

1. ✅ **Foundry Local'ı kurdunuz** ve çalıştığını doğruladınız
2. ✅ **İlk yapay zeka modelinizi** (phi-4-mini) yerel olarak başlattınız
3. ✅ **Farklı modelleri** komut satırı üzerinden test ettiniz
4. ✅ **Bir sohbet uygulaması oluşturdunuz** ve yerel yapay zekaya bağlandınız
5. ✅ **Yerel yapay zeka çıkarımını** bulut bağımlılığı olmadan deneyimlediniz

## Ne Olduğunu Anlama

### Yerel Yapay Zeka Çıkarımı

- Yapay zeka modelleriniz tamamen bilgisayarınızda çalışır
- Hiçbir veri buluta gönderilmez
- Yanıtlar CPU/GPU'nuz kullanılarak yerel olarak üretilir
- Gizlilik ve güvenlik korunur

### Model Yönetimi

- `foundry model run` modelleri indirir ve başlatır
- **FoundryLocalManager SDK** hizmet başlatma ve model yüklemeyi otomatik olarak yönetir
- Modeller gelecekteki kullanım için yerel olarak önbelleğe alınır
- Birden fazla model indirilebilir ancak genellikle bir model çalışır
- Hizmet model yaşam döngüsünü otomatik olarak yönetir

### SDK ve CLI Yaklaşımları

- **CLI Yaklaşımı**: `foundry model run <model>` ile manuel model yönetimi
- **SDK Yaklaşımı**: `FoundryLocalManager(alias)` ile otomatik hizmet + model yönetimi
- **Öneri**: Uygulamalar için SDK, test ve keşif için CLI kullanın

## Sık Kullanılan Komutlar Referansı

### Temel CLI Komutları

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Model Önerileri

- **phi-4-mini**: En iyi başlangıç modeli - hızlı, hafif, kaliteli
- **qwen2.5-0.5b**: En hızlı çıkarım, minimum bellek kullanımı
- **gpt-oss-20b**: Daha kaliteli yanıtlar, daha fazla kaynak gerektirir
- **deepseek-coder-1.3b**: Programlama ve kod görevleri için optimize edilmiş

## Sorun Giderme

### "Foundry komutu bulunamadı"

**Çözüm:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model yüklenemedi"

**Çözüm:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Localhost'ta bağlantı reddedildi"

**Çözüm:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Sonraki Adımlar

### Hemen Yapılacaklar

1. **Farklı modeller ve istemlerle** deney yapın
2. Sohbet uygulamanızı **değiştirerek** farklı modelleri deneyin
3. **Kendi istemlerinizi oluşturun** ve yanıtları test edin
4. **Oturum 2'yi keşfedin**: RAG uygulamaları oluşturma

### İleri Düzey Öğrenme Yolu

1. **Oturum 2**: RAG (Retrieval-Augmented Generation) ile yapay zeka çözümleri oluşturma
2. **Oturum 3**: Farklı açık kaynak modelleri karşılaştırma
3. **Oturum 4**: En son modellerle çalışma
4. **Oturum 5**: Çoklu ajan yapay zeka sistemleri oluşturma

## Ortam Değişkenleri (İsteğe Bağlı)

Daha gelişmiş kullanım için şu ortam değişkenlerini ayarlayabilirsiniz:

| Değişken | Amaç | Örnek |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Kullanılacak varsayılan model | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Endpoint URL'sini geçersiz kıl | `http://localhost:5273/v1` |

Proje dizininizde bir `.env` dosyası oluşturun:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Ek Kaynaklar

### Belgeler

- [Foundry Local Python SDK Referansı](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Kurulum Kılavuzu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Kataloğu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Örnek Kod

- **Session01 Python Örneği**: `Workshop/samples/session01/chat_bootstrap.py` - Akışlı tam sohbet uygulaması
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - İnteraktif eğitim  
- [Module08 Örnek 01](../Module08/samples/01/README.md) - REST Sohbet Hızlı Başlangıç
- [Module08 Örnek 02](../Module08/samples/02/README.md) - OpenAI SDK Entegrasyonu
- [Module08 Örnek 03](../Module08/samples/03/README.md) - Model Keşfi ve Karşılaştırma

### Topluluk

- [Foundry Local GitHub Tartışmaları](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Topluluğu](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Oturum Süresi**: 30 dakika uygulamalı + 15 dakika Soru-Cevap  
**Zorluk Seviyesi**: Başlangıç  
**Ön Koşullar**: Windows 11/macOS 11+, Python 3.10+, Yönetici erişimi

## Atölye Örnek Senaryosu

### Gerçek Dünya Bağlamı

**Senaryo**: Bir kurumsal BT ekibi, hassas çalışan geri bildirimlerini dış hizmetlere göndermeden işlemek için cihaz üzerinde yapay zeka çıkarımını değerlendirmek istiyor.

**Hedefiniz**: Yerel yapay zeka modellerinin, tam veri gizliliği sağlarken alt saniye gecikme ile kaliteli yanıtlar verebileceğini gösterin.

### Test İstemleri

Kurulumunuzu doğrulamak için bu istemleri kullanın:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Başarı Kriterleri

- ✅ Tüm istemler 2 saniyeden kısa sürede yanıt alır
- ✅ Hiçbir veri yerel makinenizden dışarı çıkmaz
- ✅ Yanıtlar alakalı ve yardımcıdır
- ✅ Sohbet uygulamanız sorunsuz çalışır

Bu doğrulama, Foundry Local kurulumunuzun Oturum 2-6'daki ileri düzey atölyeler için hazır olduğunu garanti eder.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->