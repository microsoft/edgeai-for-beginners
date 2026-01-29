# Ortam Yapılandırma Kılavuzu

## Genel Bakış

Workshop örnekleri, yapılandırma için depo kökünde bulunan `.env` dosyasında merkezi olarak yer alan ortam değişkenlerini kullanır. Bu, kodu değiştirmeden kolay özelleştirme sağlar.

## Hızlı Başlangıç

### 1. Ön Koşulları Doğrulayın

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Ortamı Yapılandırın

`.env` dosyası zaten mantıklı varsayılanlarla yapılandırılmıştır. Çoğu kullanıcı herhangi bir değişiklik yapmaya ihtiyaç duymaz.

**Opsiyonel**: Ayarları gözden geçirin ve özelleştirin:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Yapılandırmayı Uygulayın

**Python Scriptleri İçin:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Notebooklar İçin:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Ortam Değişkenleri Referansı

### Temel Yapılandırma

| Değişken | Varsayılan | Açıklama |
|----------|------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Örnekler için varsayılan model |
| `FOUNDRY_LOCAL_ENDPOINT` | (boş) | Servis uç noktasını geçersiz kıl |
| `PYTHONPATH` | Workshop yolları | Python modül arama yolu |

**FOUNDRY_LOCAL_ENDPOINT ne zaman ayarlanmalı:**
- Uzaktan Foundry Local örneği
- Özel port yapılandırması
- Geliştirme/üretim ayrımı

**Örnek:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Oturum Bazlı Değişkenler

#### Oturum 02: RAG Pipeline
| Değişken | Varsayılan | Amaç |
|----------|------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Gömme modeli |
| `RAG_QUESTION` | Önceden yapılandırılmış | Test sorusu |

#### Oturum 03: Benchmarking
| Değişken | Varsayılan | Amaç |
|----------|------------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Karşılaştırılacak modeller |
| `BENCH_ROUNDS` | `3` | Model başına yineleme |
| `BENCH_PROMPT` | Önceden yapılandırılmış | Test istemi |
| `BENCH_STREAM` | `0` | İlk token gecikmesini ölç |

#### Oturum 04: Model Karşılaştırması
| Değişken | Varsayılan | Amaç |
|----------|------------|------|
| `SLM_ALIAS` | `phi-4-mini` | Küçük dil modeli |
| `LLM_ALIAS` | `qwen2.5-7b` | Büyük dil modeli |
| `COMPARE_PROMPT` | Önceden yapılandırılmış | Karşılaştırma istemi |
| `COMPARE_RETRIES` | `2` | Yeniden deneme sayısı |

#### Oturum 05: Çoklu Ajan Orkestrasyonu
| Değişken | Varsayılan | Amaç |
|----------|------------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Araştırmacı ajan modeli |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Editör ajan modeli |
| `AGENT_QUESTION` | Önceden yapılandırılmış | Test sorusu |

### Güvenilirlik Yapılandırması

| Değişken | Varsayılan | Amaç |
|----------|------------|------|
| `SHOW_USAGE` | `1` | Token kullanımını yazdır |
| `RETRY_ON_FAIL` | `1` | Yeniden deneme mantığını etkinleştir |
| `RETRY_BACKOFF` | `1.0` | Yeniden deneme gecikmesi (saniye) |

## Yaygın Yapılandırmalar

### Geliştirme Kurulumu (Hızlı Yineleme)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Üretim Kurulumu (Kalite Odaklı)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking Kurulumu
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Çoklu Ajan Uzmanlaşması
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Uzaktan Geliştirme
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Önerilen Modeller

### Kullanım Amacına Göre

**Genel Amaçlı:**
- `phi-4-mini` - Dengeli kalite ve hız

**Hızlı Yanıtlar:**
- `qwen2.5-0.5b` - Çok hızlı, sınıflandırma için iyi
- `phi-4-mini` - Hızlı ve iyi kalite

**Yüksek Kalite:**
- `qwen2.5-7b` - En iyi kalite, daha fazla kaynak kullanımı
- `phi-4-mini` - İyi kalite, daha az kaynak

**Kod Üretimi:**
- `deepseek-coder-1.3b` - Kod için özel
- `phi-4-mini` - Genel amaçlı kodlama

### Kaynak Mevcudiyetine Göre

**Düşük Kaynaklar (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Orta Kaynaklar (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Yüksek Kaynaklar (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Gelişmiş Yapılandırma

### Özel Uç Noktalar

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Sıcaklık ve Örnekleme (Kodda Geçersiz Kılma)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI Hibrit Kurulumu

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Sorun Giderme

### Ortam Değişkenleri Yüklenmedi

**Belirtiler:**
- Scriptler yanlış modelleri kullanıyor
- Bağlantı hataları
- Değişkenler tanınmıyor

**Çözümler:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Servis Bağlantı Sorunları

**Belirtiler:**
- "Bağlantı reddedildi" hataları
- "Servis mevcut değil"
- Zaman aşımı hataları

**Çözümler:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Model Bulunamadı

**Belirtiler:**
- "Model bulunamadı" hataları
- "Alias tanınmadı"

**Çözümler:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### İçe Aktarma Hataları

**Belirtiler:**
- "Modül bulunamadı" hataları

**Çözümler:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Yapılandırmayı Test Etme

### Ortam Yüklemesini Doğrulayın

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Foundry Local Bağlantısını Test Edin

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Güvenlik En İyi Uygulamaları

### 1. Asla Gizli Bilgileri Commit Etmeyin

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Ayrı .env Dosyaları Kullanın

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API Anahtarlarını Döndürün

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Ortama Özgü Yapılandırma Kullanın

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK Belgeleri

- **Ana Depo**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Belgeleri**: En son bilgiler için SDK deposunu kontrol edin

## Ek Kaynaklar

- `QUICK_START.md` - Başlangıç kılavuzu
- `Workshop/samples/*/README.md` - Örnek bazlı kılavuzlar

---

**Son Güncelleme**: 2025-01-08  
**Sürüm**: 2.0  
**SDK**: Foundry Local Python SDK (en son)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->