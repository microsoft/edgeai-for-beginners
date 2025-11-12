<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-11T23:01:55+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "tr"
}
-->
# Atölye Örnekleri - Hızlı Referans Kartı

**Son Güncelleme**: 8 Ekim 2025

---

## 🚀 Hızlı Başlangıç

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Örnek Genel Bakış

| Oturum | Örnek | Amaç | Süre |
|--------|-------|------|------|
| 01 | `chat_bootstrap.py` | Temel sohbet + akış | ~30s |
| 02 | `rag_pipeline.py` | Embedding ile RAG | ~45s |
| 02 | `rag_eval_ragas.py` | RAG değerlendirme | ~60s |
| 03 | `benchmark_oss_models.py` | Model karşılaştırma | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Çoklu ajan sistemi | ~60s |
| 06 | `models_router.py` | Niyet yönlendirme | ~45s |
| 06 | `models_pipeline.py` | Çok adımlı işlem hattı | ~60s |

---

## 🛠️ Ortam Değişkenleri

### Temel
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Oturuma Özel
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Doğrulama ve Test

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Sorun Giderme

### Bağlantı Hatası
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### İçe Aktarma Hatası
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Model Bulunamadı
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Yavaş Performans
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Yaygın Kalıplar

### Temel Sohbet
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### İstemci Alma
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Hata Yönetimi
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Akış
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Model Seçimi

| Model | Boyut | En İyi Kullanım Alanı | Hız |
|-------|-------|------------------------|-----|
| `qwen2.5-0.5b` | 0.5B | Hızlı sınıflandırma | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Hızlı kod üretimi | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Yaratıcı yazım | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Kod, yeniden düzenleme | ⚡⚡ |
| `phi-4-mini` | 4B | Genel, özetleme | ⚡⚡ |
| `qwen2.5-7b` | 7B | Karmaşık akıl yürütme | ⚡ |

---

## 🔗 Kaynaklar

- **SDK Belgeleri**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hızlı Referans**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 İpuçları

1. **İstemcileri önbelleğe alın**: `workshop_utils` sizin için önbelleğe alır
2. **Daha küçük modeller kullanın**: Test için `qwen2.5-0.5b` ile başlayın
3. **Kullanım istatistiklerini etkinleştirin**: Token takibi için `SHOW_USAGE=1` ayarını yapın
4. **Toplu işlem yapın**: Birden fazla istemi sırayla işleyin
5. **max_tokens değerini düşürün**: Hızlı yanıtlar için gecikmeyi azaltır

---

## 🎯 Örnek İş Akışları

### Her Şeyi Test Et
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Modelleri Karşılaştır
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG İşlem Hattı
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Çoklu Ajan Sistemi
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Hızlı Yardım**: `samples` dizininden herhangi bir örneği `--help` ile çalıştırın veya docstring'e göz atın:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Tüm örnekler Ekim 2025'te Foundry Local SDK en iyi uygulamalarıyla güncellendi** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->