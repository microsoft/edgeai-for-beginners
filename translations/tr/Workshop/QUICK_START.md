# Atölye Hızlı Başlangıç Kılavuzu

## Ön Koşullar

### 1. Foundry Local'ı Yükleyin

Resmi yükleme kılavuzunu takip edin:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python Bağımlılıklarını Yükleyin

Atölye dizininden:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Atölye Örneklerini Çalıştırma

### Oturum 01: Temel Sohbet

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Ortam Değişkenleri:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Oturum 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Ortam Değişkenleri:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Oturum 02: RAG Değerlendirme (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Not**: Ek bağımlılıkların `requirements.txt` üzerinden yüklenmesi gerekir.

### Oturum 03: Performans Testi

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Ortam Değişkenleri:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Çıktı**: Gecikme, işlem hacmi ve ilk token metriklerini içeren JSON

### Oturum 04: Model Karşılaştırması

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Ortam Değişkenleri:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Oturum 05: Çoklu Ajan Orkestrasyonu

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Ortam Değişkenleri:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Oturum 06: Model Yönlendirici

```bash
cd Workshop/samples
python -m session06.models_router
```

**Yönlendirme mantığını test eder** farklı niyetlerle (kod, özetleme, sınıflandırma)

### Oturum 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Karmaşık çok adımlı pipeline** planlama, yürütme ve iyileştirme ile

## Betikler

### Performans Testi Raporu Dışa Aktarma

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Çıktı**: Markdown tablosu + JSON metrikleri

### Markdown CLI Kalıplarını Denetleme

```bash
python lint_markdown_cli.py --verbose
```

**Amaç**: Belgelerdeki eski CLI kalıplarını tespit etme

## Testler

### Hızlı Testler

```bash
cd Workshop
python -m tests.smoke
```

**Testler**: Temel örneklerin işlevselliği

## Sorun Giderme

### Servis Çalışmıyor

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modül İçe Aktarma Hataları

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Bağlantı Hataları

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model Bulunamadı

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Ortam Değişkeni Referansı

### Temel Yapılandırma
| Değişken | Varsayılan | Açıklama |
|----------|------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Değişken | Kullanılacak model takma adı |
| `FOUNDRY_LOCAL_ENDPOINT` | Otomatik | Servis uç noktasını geçersiz kıl |
| `SHOW_USAGE` | `0` | Token kullanım istatistiklerini göster |
| `RETRY_ON_FAIL` | `1` | Yeniden deneme mantığını etkinleştir |
| `RETRY_BACKOFF` | `1.0` | İlk yeniden deneme gecikmesi (saniye) |

### Oturuma Özel
| Değişken | Varsayılan | Açıklama |
|----------|------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Gömme modeli |
| `RAG_QUESTION` | Örnekten bakın | RAG test sorusu |
| `BENCH_MODELS` | Değişken | Virgülle ayrılmış modeller |
| `BENCH_ROUNDS` | `3` | Performans testi yinelemeleri |
| `BENCH_PROMPT` | Örnekten bakın | Performans testi istemi |
| `BENCH_STREAM` | `0` | İlk token gecikmesini ölç |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Birincil ajan modeli |
| `AGENT_MODEL_EDITOR` | Birincil | Editör ajan modeli |
| `SLM_ALIAS` | `phi-4-mini` | Küçük dil modeli |
| `LLM_ALIAS` | `qwen2.5-7b` | Büyük dil modeli |
| `COMPARE_PROMPT` | Örnekten bakın | Karşılaştırma istemi |

## Önerilen Modeller

### Geliştirme ve Test
- **phi-4-mini** - Dengeli kalite ve hız
- **qwen2.5-0.5b** - Sınıflandırma için çok hızlı
- **gemma-2-2b** - İyi kalite, orta hız

### Üretim Senaryoları
- **phi-4-mini** - Genel amaçlı
- **deepseek-coder-1.3b** - Kod üretimi
- **qwen2.5-7b** - Yüksek kaliteli yanıtlar

## SDK Belgeleri

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Yardım Alma

1. Servis durumunu kontrol edin: `foundry service status`  
2. Günlükleri görüntüleyin: Foundry Local servis günlüklerini kontrol edin  
3. SDK belgelerini kontrol edin: https://github.com/microsoft/Foundry-Local  
4. Örnek kodu inceleyin: Tüm örneklerde ayrıntılı açıklamalar bulunmaktadır  

## Sonraki Adımlar

1. Tüm atölye oturumlarını sırayla tamamlayın  
2. Farklı modellerle deney yapın  
3. Örnekleri kendi kullanım senaryolarınıza göre değiştirin  

---

**Son Güncelleme**: 2025-01-08  
**Atölye Sürümü**: En Son  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->