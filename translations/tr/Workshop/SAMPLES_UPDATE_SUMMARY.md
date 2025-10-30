<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:50:32+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "tr"
}
-->
# Atölye Örnekleri - Foundry Local SDK Güncelleme Özeti

## Genel Bakış

`Workshop/samples` dizinindeki tüm Python örnekleri, Foundry Local SDK en iyi uygulamalarına uygun hale getirilmiş ve atölye boyunca tutarlılık sağlanmıştır.

**Tarih**: 8 Ekim 2025  
**Kapsam**: 6 atölye oturumunda 9 Python dosyası  
**Ana Odak**: Hata yönetimi, dokümantasyon, SDK kalıpları, kullanıcı deneyimi

---

## Güncellenen Dosyalar

### Oturum 01: Başlangıç
- ✅ `chat_bootstrap.py` - Temel sohbet ve akış örnekleri

### Oturum 02: RAG Çözümleri
- ✅ `rag_pipeline.py` - Embedding ile RAG uygulaması
- ✅ `rag_eval_ragas.py` - RAGAS metrikleri ile RAG değerlendirmesi

### Oturum 03: Açık Kaynak Modeller
- ✅ `benchmark_oss_models.py` - Çoklu model karşılaştırması

### Oturum 04: En Son Modeller
- ✅ `model_compare.py` - SLM ve LLM karşılaştırması

### Oturum 05: Yapay Zeka Destekli Ajanlar
- ✅ `agents_orchestrator.py` - Çoklu ajan koordinasyonu

### Oturum 06: Araç Olarak Modeller
- ✅ `models_router.py` - Niyet tabanlı model yönlendirme
- ✅ `models_pipeline.py` - Çok adımlı yönlendirilmiş işlem hattı

### Destekleyici Altyapı
- ✅ `workshop_utils.py` - Zaten en iyi uygulamalara uygun (değişiklik yapılmadı)

---

## Ana İyileştirmeler

### 1. Geliştirilmiş Hata Yönetimi

**Önce:**
```python
manager, client, model_id = get_client(alias)
```

**Sonra:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Faydalar:**
- Açık hata mesajları ile zarif hata yönetimi
- Eyleme geçirilebilir sorun giderme ipuçları
- Betik çalıştırma için uygun çıkış kodları

### 2. Daha İyi İçe Aktarma Yönetimi

**Önce:**
```python
from sentence_transformers import SentenceTransformer
```

**Sonra:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Faydalar:**
- Eksik bağımlılıklar için net rehberlik
- Anlaşılmaz içe aktarma hatalarını önler
- Kullanıcı dostu kurulum talimatları

### 3. Kapsamlı Dokümantasyon

**Tüm örneklere eklenenler:**
- Ortam değişkeni dokümantasyonu (docstring içinde)
- SDK referans bağlantıları
- Kullanım örnekleri
- Ayrıntılı fonksiyon/parametre dokümantasyonu
- Daha iyi IDE desteği için tür ipuçları

**Örnek:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Geliştirilmiş Kullanıcı Geri Bildirimi

**Bilgilendirici günlükler eklendi:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**İlerleme göstergeleri:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Yapılandırılmış çıktı:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Güçlü Karşılaştırma

**Oturum 03 iyileştirmeleri:**
- Model başına hata yönetimi (hata durumunda devam eder)
- Ayrıntılı ilerleme raporlaması
- Isınma turları düzgün bir şekilde yürütüldü
- İlk token gecikme ölçümü desteği
- Aşamaların net ayrımı

### 6. Tutarlı Tür İpuçları

**Her yerde eklendi:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Faydalar:**
- Daha iyi IDE otomatik tamamlama
- Erken hata tespiti
- Kendini açıklayan kod

### 7. Geliştirilmiş Model Yönlendirici

**Oturum 06 iyileştirmeleri:**
- Kapsamlı niyet algılama dokümantasyonu
- Model seçimi algoritması açıklaması
- Ayrıntılı yönlendirme günlükleri
- Test çıktısı formatlama
- Toplu testlerde hata kurtarma

### 8. Çoklu Ajan Orkestrasyonu

**Oturum 05 iyileştirmeleri:**
- Aşama bazında ilerleme raporlaması
- Ajan başına hata yönetimi
- Net işlem hattı yapısı
- Daha iyi bellek yönetimi dokümantasyonu

---

## Test Kontrol Listesi

### Ön Koşullar
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Her Örneği Test Et

#### Oturum 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Oturum 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Oturum 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Oturum 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Oturum 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Oturum 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Ortam Değişkenleri Referansı

### Genel (Tüm Örnekler)
| Değişken | Açıklama | Varsayılan |
|----------|-------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Kullanılacak model takma adı | Örneğe göre değişir |
| `FOUNDRY_LOCAL_ENDPOINT` | Hizmet uç noktasını geçersiz kıl | Otomatik algılanır |
| `SHOW_USAGE` | Token kullanımını göster | `0` |
| `RETRY_ON_FAIL` | Yeniden deneme mantığını etkinleştir | `1` |
| `RETRY_BACKOFF` | İlk yeniden deneme gecikmesi | `1.0` |

### Örnek Bazlı
| Değişken | Kullanıldığı Yer | Açıklama |
|----------|------------------|-------------|
| `EMBED_MODEL` | Oturum 02 | Embedding model adı |
| `RAG_QUESTION` | Oturum 02 | RAG için test sorusu |
| `BENCH_MODELS` | Oturum 03 | Karşılaştırılacak modeller (virgülle ayrılmış) |
| `BENCH_ROUNDS` | Oturum 03 | Karşılaştırma turları sayısı |
| `BENCH_PROMPT` | Oturum 03 | Karşılaştırma için test istemi |
| `BENCH_STREAM` | Oturum 03 | İlk token gecikmesini ölç |
| `SLM_ALIAS` | Oturum 04 | Küçük dil modeli |
| `LLM_ALIAS` | Oturum 04 | Büyük dil modeli |
| `COMPARE_PROMPT` | Oturum 04 | Karşılaştırma test istemi |
| `AGENT_MODEL_PRIMARY` | Oturum 05 | Birincil ajan modeli |
| `AGENT_MODEL_EDITOR` | Oturum 05 | Editör ajan modeli |
| `AGENT_QUESTION` | Oturum 05 | Ajanlar için test sorusu |
| `PIPELINE_TASK` | Oturum 06 | İşlem hattı için görev |

---

## Önemli Değişiklikler

**Yok** - Tüm değişiklikler geriye dönük uyumludur.

Mevcut betikler çalışmaya devam edecek. Yeni özellikler:
- İsteğe bağlı ortam değişkenleri
- Geliştirilmiş hata mesajları (işlevselliği bozmaz)
- Ek günlükler (gizlenebilir)
- Daha iyi tür ipuçları (çalışma zamanında etkisi yok)

---

## Uygulanan En İyi Uygulamalar

### 1. Her Zaman Workshop Utils Kullanın
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Doğru Hata Yönetimi Kalıbı
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Bilgilendirici Günlükler
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Tür İpuçları
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Kapsamlı Docstring'ler
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Ortam Değişkeni Desteği
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Zarif Degradasyon
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Yaygın Sorunlar ve Çözümler

### Sorun: İçe Aktarma Hataları
**Çözüm:** Eksik bağımlılıkları yükleyin
```bash
pip install sentence-transformers ragas datasets numpy
```

### Sorun: Bağlantı Hataları
**Çözüm:** Foundry Local'ın çalıştığından emin olun
```bash
foundry service status
foundry model run phi-4-mini
```

### Sorun: Model Bulunamadı
**Çözüm:** Mevcut modelleri kontrol edin
```bash
foundry model ls
foundry model download <alias>
```

### Sorun: Yavaş Performans
**Çözüm:** Daha küçük modeller kullanın veya parametreleri ayarlayın
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Sonraki Adımlar

### 1. Tüm Örnekleri Test Edin
Yukarıdaki test kontrol listesini kullanarak tüm örneklerin doğru çalıştığını doğrulayın.

### 2. Dokümantasyonu Güncelleyin
- Oturum markdown dosyalarını yeni örneklerle güncelleyin
- Ana README dosyasına sorun giderme bölümü ekleyin
- Hızlı referans kılavuzu oluşturun

### 3. Entegrasyon Testleri Oluşturun
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Performans Karşılaştırmaları Ekleyin
Hata yönetimi iyileştirmelerinden kaynaklanan performans gelişmelerini takip edin.

### 5. Kullanıcı Geri Bildirimi
Atölye katılımcılarından şu konularda geri bildirim toplayın:
- Hata mesajlarının açıklığı
- Dokümantasyonun tamlığı
- Kullanım kolaylığı

---

## Kaynaklar

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Hızlı Referans**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Geçiş Notları**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Ana Depo**: https://github.com/microsoft/Foundry-Local

---

## Bakım

### Yeni Örnekler Eklemek
Yeni örnekler oluştururken şu kalıpları izleyin:

1. `workshop_utils` kullanarak istemci yönetimi
2. Kapsamlı hata yönetimi ekleyin
3. Ortam değişkeni desteği ekleyin
4. Tür ipuçları ve docstring'ler ekleyin
5. Bilgilendirici günlükler sağlayın
6. Docstring içinde kullanım örnekleri ekleyin
7. SDK dokümantasyonuna bağlantı ekleyin

### Güncellemeleri Gözden Geçirme
Örnek güncellemelerini gözden geçirirken şunları kontrol edin:
- [ ] Tüm I/O işlemlerinde hata yönetimi
- [ ] Genel işlevlerde tür ipuçları
- [ ] Kapsamlı docstring'ler
- [ ] Ortam değişkeni dokümantasyonu
- [ ] Bilgilendirici kullanıcı geri bildirimi
- [ ] SDK referans bağlantıları
- [ ] Tutarlı kod stili

---

**Özet**: Tüm Atölye Python örnekleri artık Foundry Local SDK en iyi uygulamalarına uygun hale getirilmiş, geliştirilmiş hata yönetimi, kapsamlı dokümantasyon ve iyileştirilmiş kullanıcı deneyimi sunmaktadır. Hiçbir işlevsellik bozulmadan mevcut özellikler korunmuş ve geliştirilmiştir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.