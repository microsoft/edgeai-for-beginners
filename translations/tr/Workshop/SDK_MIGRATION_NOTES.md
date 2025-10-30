<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:50:49+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "tr"
}
-->
# Foundry Yerel SDK Geçiş Notları

## Genel Bakış

Workshop klasöründeki tüm Python dosyaları, resmi [Foundry Yerel Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) tarafından önerilen en son kalıplara uygun olacak şekilde güncellendi.

## Değişiklik Özeti

### Temel Altyapı (`workshop_utils.py`)

#### Geliştirilmiş Özellikler:
- **Endpoint Geçersiz Kılma Desteği**: `FOUNDRY_LOCAL_ENDPOINT` ortam değişkeni desteği eklendi
- **Geliştirilmiş Hata Yönetimi**: Daha ayrıntılı hata mesajlarıyla daha iyi istisna yönetimi
- **Geliştirilmiş Önbellekleme**: Çoklu endpoint senaryoları için önbellek anahtarları artık endpoint içeriyor
- **Üstel Geri Alma**: Daha iyi güvenilirlik için üstel geri alma mantığı eklendi
- **Tip Anotasyonları**: Daha iyi IDE desteği için kapsamlı tip ipuçları eklendi

#### Yeni Yetkinlikler:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Örnek Uygulamalar

#### Oturum 01: Sohbet Başlatma (`chat_bootstrap.py`)
- Varsayılan model `phi-3.5-mini` yerine `phi-4-mini` olarak güncellendi
- Endpoint geçersiz kılma desteği eklendi
- SDK referanslarıyla belgeler geliştirildi

#### Oturum 02: RAG Pipeline (`rag_pipeline.py`)
- Varsayılan model `phi-4-mini` olarak güncellendi
- Endpoint geçersiz kılma desteği eklendi
- Ortam değişkeni detaylarıyla belgeler geliştirildi

#### Oturum 02: RAG Değerlendirme (`rag_eval_ragas.py`)
- Model varsayılanları güncellendi
- Endpoint yapılandırması eklendi
- Hata yönetimi geliştirildi

#### Oturum 03: Karşılaştırmalı Testler (`benchmark_oss_models.py`)
- Varsayılan model listesi `phi-4-mini`yi içerecek şekilde güncellendi
- Kapsamlı ortam değişkeni belgeleri eklendi
- Fonksiyon belgeleri geliştirildi
- Endpoint geçersiz kılma desteği eklendi

#### Oturum 04: Model Karşılaştırması (`model_compare.py`)
- Varsayılan LLM `gpt-oss-20b` yerine `qwen2.5-7b` olarak güncellendi
- Endpoint yapılandırması eklendi
- Belgeler geliştirildi

#### Oturum 05: Çoklu Ajan Orkestrasyonu (`agents_orchestrator.py`)
- Tip ipuçları eklendi (`str | None` yerine `Optional[str]` kullanıldı)
- Ajan sınıfı belgeleri geliştirildi
- Endpoint geçersiz kılma desteği eklendi
- Başlatma kalıbı geliştirildi

#### Oturum 06: Model Yönlendirici (`models_router.py`)
- Endpoint yapılandırması eklendi
- Niyet algılama belgeleri geliştirildi
- Yönlendirme mantığı belgeleri geliştirildi

#### Oturum 06: Pipeline (`models_pipeline.py`)
- Kapsamlı fonksiyon belgeleri eklendi
- Adım adım belgeler geliştirildi
- Hata yönetimi geliştirildi

### Scriptler

#### Karşılaştırmalı Test İhracı (`export_benchmark_markdown.py`)
- Endpoint geçersiz kılma desteği eklendi
- Varsayılan modeller güncellendi
- Fonksiyon belgeleri geliştirildi
- Hata yönetimi geliştirildi

#### CLI Linter (`lint_markdown_cli.py`)
- SDK referans bağlantıları eklendi
- Kullanım belgeleri geliştirildi

### Testler

#### Duman Testleri (`smoke.py`)
- Endpoint geçersiz kılma desteği eklendi
- Belgeler geliştirildi
- Test senaryosu belgeleri geliştirildi
- Daha iyi hata raporlama

## Ortam Değişkenleri

Tüm örnekler artık şu ortam değişkenlerini destekliyor:

### Temel Yapılandırma
- `FOUNDRY_LOCAL_ALIAS` - Kullanılacak model takma adı (örneğe göre varsayılan değişir)
- `FOUNDRY_LOCAL_ENDPOINT` - Servis endpointini geçersiz kılma (isteğe bağlı)
- `SHOW_USAGE` - Token kullanım istatistiklerini göster (varsayılan: "0")
- `RETRY_ON_FAIL` - Yeniden deneme mantığını etkinleştir (varsayılan: "1")
- `RETRY_BACKOFF` - İlk yeniden deneme gecikmesi saniye cinsinden (varsayılan: "1.0")

### Örnek-Specifik
- `EMBED_MODEL` - RAG örnekleri için gömme modeli
- `BENCH_MODELS` - Karşılaştırmalı test için virgülle ayrılmış modeller
- `BENCH_ROUNDS` - Karşılaştırmalı test tur sayısı
- `BENCH_PROMPT` - Karşılaştırmalı test için test istemi
- `BENCH_STREAM` - İlk token gecikmesini ölç
- `RAG_QUESTION` - RAG örnekleri için test sorusu
- `AGENT_MODEL_PRIMARY` - Birincil ajan modeli
- `AGENT_MODEL_EDITOR` - Editör ajan modeli
- `SLM_ALIAS` - Küçük dil modeli takma adı
- `LLM_ALIAS` - Büyük dil modeli takma adı

## Uygulanan SDK En İyi Uygulamaları

### 1. Doğru İstemci Başlatma
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Model Bilgisi Alma
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Hata Yönetimi
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Üstel Geri Alma ile Yeniden Deneme Mantığı
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Akış Desteği
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Özel Örnekler için Geçiş Kılavuzu

Yeni örnekler oluşturuyorsanız veya mevcut olanları güncelliyorsanız:

1. **`workshop_utils.py` yardımcılarını kullanın**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Endpoint geçersiz kılmayı destekleyin**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Kapsamlı belgeler ekleyin**:
   - Docstring içinde ortam değişkenleri
   - SDK referans bağlantısı
   - Kullanım örnekleri

4. **Tip ipuçlarını kullanın**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Doğru hata yönetimini uygulayın**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testler

Tüm örnekler şu şekilde test edilebilir:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK Dokümantasyon Referansları

- **Ana Depo**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API Dokümantasyonu**: En son API belgeleri için SDK deposunu kontrol edin

## Kırılma Değişiklikleri

### Beklenmiyor
Tüm değişiklikler geriye dönük uyumludur. Güncellemeler esas olarak:
- Yeni isteğe bağlı özellikler ekler (endpoint geçersiz kılma)
- Hata yönetimini iyileştirir
- Belgeleri geliştirir
- Varsayılan model adlarını mevcut önerilere günceller

### İsteğe Bağlı Geliştirmeler
Kodunuzu şu şekilde güncellemek isteyebilirsiniz:
- Açık endpoint kontrolü için `FOUNDRY_LOCAL_ENDPOINT` kullanımı
- Token kullanım görünürlüğü için `SHOW_USAGE=1`
- Güncellenmiş model varsayılanları (`phi-4-mini` yerine `phi-3.5-mini`)

## Yaygın Sorunlar ve Çözümler

### Sorun: "İstemci başlatma başarısız oldu"
**Çözüm**: Foundry Yerel servisin çalıştığından emin olun:
```bash
foundry service start
foundry model run phi-4-mini
```

### Sorun: "Model bulunamadı"
**Çözüm**: Mevcut modelleri kontrol edin:
```bash
foundry model list
```

### Sorun: Endpoint bağlantı hataları
**Çözüm**: Endpointi doğrulayın:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Sonraki Adımlar

1. **Module08 örneklerini güncelleyin**: Module08/samples için benzer kalıpları uygulayın
2. **Entegrasyon testleri ekleyin**: Kapsamlı bir test paketi oluşturun
3. **Performans karşılaştırması**: Öncesi/sonrası performansını karşılaştırın
4. **Belge güncellemeleri**: Ana README'yi yeni kalıplarla güncelleyin

## Katkı Sağlama Yönergeleri

Yeni örnekler eklerken:
1. Tutarlılık için `workshop_utils.py` kullanın
2. Mevcut örneklerdeki kalıbı takip edin
3. Kapsamlı docstringler ekleyin
4. SDK referans bağlantıları ekleyin
5. Endpoint geçersiz kılmayı destekleyin
6. Doğru tip ipuçları ekleyin
7. Docstring içinde kullanım örnekleri ekleyin

## Sürüm Uyumluluğu

Bu güncellemeler şu sürümlerle uyumludur:
- `foundry-local-sdk` (en son)
- `openai>=1.30.0`
- Python 3.8+

---

**Son Güncelleme**: 2025-01-08  
**Bakımcı**: EdgeAI Workshop Ekibi  
**SDK Sürümü**: Foundry Yerel SDK (en son 0.7.117+67073234e7)

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.