<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:20:26+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "tr"
}
-->
# Oturum 1: Foundry Local ile Başlangıç

## Özet

Foundry Local ile yolculuğunuza Windows 11 üzerinde kurulum ve yapılandırma ile başlayın. CLI'yi nasıl ayarlayacağınızı, donanım hızlandırmayı nasıl etkinleştireceğinizi ve modelleri hızlı yerel çıkarım için nasıl önbelleğe alacağınızı öğrenin. Bu uygulamalı oturum, Phi, Qwen, DeepSeek ve GPT-OSS-20B gibi modelleri tekrarlanabilir CLI komutlarıyla çalıştırmayı adım adım anlatıyor.

## Öğrenme Hedefleri

Bu oturumun sonunda şunları yapabileceksiniz:

- **Kurulum ve Yapılandırma**: Foundry Local'ı Windows 11 üzerinde en iyi performans ayarlarıyla kurun
- **CLI İşlemlerinde Ustalaşma**: Foundry Local CLI'yi model yönetimi ve dağıtımı için kullanın
- **Donanım Hızlandırmayı Etkinleştirme**: ONNXRuntime veya WebGPU ile GPU hızlandırmayı yapılandırın
- **Birden Fazla Model Dağıtımı**: phi-4, GPT-OSS-20B, Qwen ve DeepSeek modellerini yerel olarak çalıştırın
- **İlk Uygulamanızı Oluşturun**: Mevcut örnekleri Foundry Local Python SDK'sını kullanacak şekilde uyarlayın

# Modeli Test Etme (etkileşimli olmayan tek bir istem)
foundry model run phi-4-mini --prompt "Merhaba, kendini tanıt"

- Windows 11 (22H2 veya daha yeni)
# Kullanılabilir katalog modellerini listeleme (çalıştırılan modeller görünür)
foundry model list
## NOT: Şu anda özel bir `--running` bayrağı yok; hangi modellerin yüklü olduğunu görmek için bir sohbet başlatın veya hizmet günlüklerini inceleyin.
- Python 3.10+ yüklü
- Python uzantısı ile Visual Studio Code
- Kurulum için yönetici yetkileri

### (Opsiyonel) Ortam Değişkenleri

Komut dosyalarını taşınabilir hale getirmek için bir `.env` oluşturun (veya kabukta ayarlayın):
# Yanıtları Karşılaştırma (etkileşimli olmayan)
foundry model run gpt-oss-20b --prompt "Edge AI'yi basit terimlerle açıklayın"
| Değişken | Amaç | Örnek |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Tercih edilen model takma adı (katalog en iyi varyantı otomatik seçer) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Endpoint'i geçersiz kılma (aksi takdirde yöneticiden otomatik alınır) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Akış demosunu etkinleştirme | `true` |

> Eğer `FOUNDRY_LOCAL_ENDPOINT=auto` (veya ayarlanmamış) ise, bunu SDK yöneticisinden türetiyoruz.

## Demo Akışı (30 dakika)

### 1. Foundry Local'ı Kurma ve CLI Kurulumunu Doğrulama (10 dakika)

# Önbelleğe alınmış modelleri listeleme
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Önizleme / Destekleniyorsa)**

Eğer bir yerel macOS paketi sağlanmışsa (en son sürüm için resmi belgeleri kontrol edin):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Eğer macOS yerel ikili dosyaları henüz mevcut değilse, yine de şunları yapabilirsiniz: 
1. Windows 11 ARM/Intel VM (Parallels / UTM) kullanarak Windows adımlarını takip edin. 
2. Modelleri bir konteyner aracılığıyla çalıştırın (eğer konteyner görüntüsü yayınlanmışsa) ve `FOUNDRY_LOCAL_ENDPOINT`'i açılan porta ayarlayın. 

**Python Sanal Ortamı Oluşturma (Platformlar Arası)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

pip'i yükseltin ve temel bağımlılıkları yükleyin:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Adım 1.2: Kurulumu Doğrulama

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Adım 1.3: Ortamı Yapılandırma

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Başlatma (Önerilir)

Hizmeti manuel olarak başlatıp modelleri çalıştırmak yerine, **Foundry Local Python SDK** her şeyi başlatabilir:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Eğer açık kontrol tercih ediyorsanız, CLI + OpenAI istemcisini daha sonra gösterildiği gibi kullanabilirsiniz.

### 2. Modelleri CLI ile Yerel Olarak Çalıştırma (10 dakika)

#### Adım 3.1: Phi-4 Modelini Dağıtma

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Adım 3.2: GPT-OSS-20B Modelini Dağıtma

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Adım 3.3: Ek Modelleri Yükleme

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Başlangıç Projesi: 01-run-phi'yi Foundry Local için Uyarlama (5 dakika)

#### Adım 4.1: Temel Sohbet Uygulaması Oluşturma

`samples/01-foundry-quickstart/chat_quickstart.py` dosyasını oluşturun (varsa yöneticiyi kullanacak şekilde güncellendi):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Adım 4.2: Uygulamayı Test Etme

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Ele Alınan Temel Kavramlar

### 1. Foundry Local Mimarisi

- **Yerel Çıkarım Motoru**: Modelleri tamamen cihazınızda çalıştırır
- **OpenAI SDK Uyumluluğu**: Mevcut OpenAI koduyla sorunsuz entegrasyon
- **Model Yönetimi**: Birden fazla modeli verimli bir şekilde indirir, önbelleğe alır ve çalıştırır
- **Donanım Optimizasyonu**: GPU, NPU ve CPU hızlandırmayı kullanır

### 2. CLI Komut Referansı

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK Entegrasyonu

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Yaygın Sorunları Giderme

### Sorun 1: "Foundry komutu bulunamadı"

**Çözüm:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Sorun 2: "Model yüklenemedi"

**Çözüm:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Sorun 3: "localhost:5273 üzerinde bağlantı reddedildi"

**Çözüm:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Performans Optimizasyon İpuçları

### 1. Model Seçim Stratejisi

- **Phi-4-mini**: Genel görevler için en iyisi, düşük bellek kullanımı
- **Qwen2.5-0.5b**: En hızlı çıkarım, minimum kaynak kullanımı
- **GPT-OSS-20B**: En yüksek kalite, daha fazla kaynak gerektirir
- **DeepSeek-Coder**: Programlama görevleri için optimize edilmiştir

### 2. Donanım Optimizasyonu

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Performansı İzleme

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Opsiyonel Geliştirmeler

| Geliştirme | Ne | Nasıl |
|-------------|------|-----|
| Paylaşılan Yardımcı Araçlar | Yinelenen istemci/başlatma mantığını kaldırın | `Workshop/samples/workshop_utils.py` kullanın (`get_client`, `chat_once`) |
| Token Kullanımı Görünürlüğü | Maliyet/verimlilik düşüncesini erken öğretin | `SHOW_USAGE=1` ayarlayın ve istem/tamamlama/toplam tokenleri yazdırın |
| Deterministik Karşılaştırmalar | Kararlı kıyaslama ve regresyon kontrolleri | `temperature=0`, `top_p=1`, tutarlı istem metni kullanın |
| İlk Token Gecikmesi | Algılanan yanıt verme ölçütü | Akışla (`BENCH_STREAM=1`) kıyaslama komut dosyasını uyarlayın |
| Geçici Hatalarda Yeniden Deneme | Soğuk başlangıçta dayanıklı demolar | `RETRY_ON_FAIL=1` (varsayılan) ve `RETRY_BACKOFF` ayarlayın |
| Duman Testi | Ana akışlar arasında hızlı doğruluk | Bir atölyeden önce `python Workshop/tests/smoke.py` çalıştırın |
| Model Takma Adı Profilleri | Makineler arasında model setini hızlıca değiştirin | `.env` dosyasını `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` ile koruyun |
| Önbellek Verimliliği | Çoklu örnek çalıştırmada tekrar eden ısınmaları önleyin | Yardımcı araçlar önbellek yöneticilerini kullanır; komut dosyaları/not defterleri arasında yeniden kullanın |
| İlk Çalıştırma Isınması | p95 gecikme dalgalanmalarını azaltın | `FoundryLocalManager` oluşturulduktan sonra küçük bir istem gönderin |

Deterministik sıcak başlangıç örneği (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

İkinci çalıştırmada benzer çıktı ve aynı token sayısını görmelisiniz, bu deterministikliği doğrular.

## Sonraki Adımlar

Bu oturumu tamamladıktan sonra:

1. **Oturum 2'yi Keşfedin**: Azure AI Foundry RAG ile AI çözümleri oluşturun
2. **Farklı Modelleri Deneyin**: Qwen, DeepSeek ve diğer model ailelerini deneyin
3. **Performansı Optimize Edin**: Donanımınıza özel ayarları ince ayar yapın
4. **Özel Uygulamalar Oluşturun**: Foundry Local SDK'yı kendi projelerinizde kullanın

## Ek Kaynaklar

### Belgeler
- [Foundry Local Python SDK Referansı](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Kurulum Kılavuzu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Kataloğu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Örnek Kod
- [Modül08 Örnek 01](./samples/01/README.md) - REST Sohbet Hızlı Başlangıç
- [Modül08 Örnek 02](./samples/02/README.md) - OpenAI SDK Entegrasyonu
- [Modül08 Örnek 03](./samples/03/README.md) - Model Keşfi ve Kıyaslama

### Topluluk
- [Foundry Local GitHub Tartışmaları](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Topluluğu](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Oturum Süresi**: 30 dakika uygulamalı + 15 dakika Soru-Cevap
**Zorluk Seviyesi**: Başlangıç
**Ön Koşullar**: Windows 11, Python 3.10+, Yönetici erişimi

## Örnek Senaryo ve Atölye Eşleştirme

| Atölye Komut Dosyası / Not Defteri | Senaryo | Amaç | Örnek Girdi(ler) | Gerekli Veri Seti |
|----------------------------|----------|------|------------------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Gizlilik değerlendirme portalı için cihaz üzerinde çıkarımı değerlendiren iç IT ekibi | Yerel SLM'nin standart istemlerde alt saniye gecikme ile yanıt verdiğini kanıtlayın | "Yerel çıkarımın iki faydasını listeleyin." | Yok (tek istem) |
| Hızlı başlangıç uyarlama kod bloğu | Mevcut bir OpenAI komut dosyasını Foundry Local'a taşıyan geliştirici | Uyumluluğu gösterin | "Yerel çıkarımın iki faydasını verin." | Sadece satır içi istem |

### Senaryo Anlatımı
Güvenlik ve uyumluluk ekibi, hassas prototip verilerinin yerel olarak işlenip işlenemeyeceğini doğrulamalıdır. Başlatma komut dosyasını birkaç istemle (gizlilik, gecikme, maliyet) deterministik temperature=0 modunda çalıştırarak daha sonra karşılaştırma için temel çıktıları yakalarlar (Oturum 3 kıyaslama ve Oturum 4 SLM vs LLM karşılaştırması).

### Minimal İstem Seti JSON (opsiyonel)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Bu listeyi tekrarlanabilir bir değerlendirme döngüsü oluşturmak veya gelecekteki bir regresyon test çerçevesini başlatmak için kullanabilirsiniz.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.