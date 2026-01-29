# Oturum 3: Foundry Local'da Açık Kaynak Modeller

## Özet

Hugging Face ve diğer açık kaynak modelleri Foundry Local'a nasıl entegre edeceğinizi keşfedin. Model seçimi stratejileri, topluluk katkı iş akışları, performans karşılaştırma metodolojisi ve Foundry'yi özel model kayıtlarıyla nasıl genişletebileceğinizi öğrenin. Bu oturum, haftalık "Model Pazartesileri" keşif temalarına uygun olarak açık kaynak modelleri yerel olarak değerlendirme ve operasyonel hale getirme becerisi kazandırır, ardından Azure'a ölçeklendirme yapılabilir.

## Öğrenme Hedefleri

Oturum sonunda şunları yapabileceksiniz:

- **Keşfet & Değerlendir**: Kalite ve kaynak dengesi kullanarak aday modelleri (mistral, gemma, qwen, deepseek) belirleyin.
- **Yükle & Çalıştır**: Foundry Local CLI kullanarak topluluk modellerini indirin, önbelleğe alın ve başlatın.
- **Karşılaştırma**: Tutarlı gecikme + token throughput + kalite ölçütlerini uygulayın.
- **Genişlet**: SDK uyumlu desenleri takip ederek özel bir model wrapper kaydedin veya uyarlayın.
- **Karşılaştır**: SLM ve orta boy LLM seçim kararları için yapılandırılmış karşılaştırmalar üretin.

## Ön Koşullar

- Oturum 1 ve 2 tamamlanmış olmalı
- Python ortamında `foundry-local-sdk` kurulu olmalı
- Birden fazla model önbelleği için en az 15GB boş disk alanı

### Platformlar Arası Ortam Hızlı Başlangıç

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS'tan bir Windows ana hizmetine karşı karşılaştırma yaparken ayarlayın:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Akışı (30 dakika)

### 1. CLI ile Hugging Face Modellerini Yükleme (8 dakika)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Çalıştır & Hızlı Test (5 dakika)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Karşılaştırma Scripti (8 dakika)

`samples/03-oss-models/benchmark_models.py` oluşturun:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Çalıştırın:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Performans Karşılaştırması (5 dakika)

Ticaretler hakkında konuşun: yükleme süresi, bellek kullanımı (Görev Yöneticisi / `nvidia-smi` / OS kaynak monitörünü gözlemleyin), çıktı kalitesi ve hız. Python karşılaştırma scriptini (Oturum 3) gecikme ve throughput için kullanın; GPU hızlandırmayı etkinleştirdikten sonra tekrarlayın.

### 5. Başlangıç Projesi (4 dakika)

Karşılaştırma scriptini markdown dışa aktarma ile genişleterek bir model karşılaştırma raporu oluşturun.

## Başlangıç Projesi: `03-huggingface-models` Genişletme

Mevcut örneği şu şekilde geliştirin:

1. Karşılaştırma toplama + CSV/Markdown çıktısı ekleyin.
2. Basit niteliksel puanlama uygulayın (prompt çift seti + manuel açıklama dosyası).
3. Eklentili model listesi ve prompt seti için bir JSON yapılandırması (`models.json`) tanıtın.

## Doğrulama Kontrol Listesi

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Tüm hedef modeller görünmeli ve bir test sohbet isteğine yanıt vermelidir.

## Örnek Senaryo ve Atölye Eşleştirme

| Atölye Scripti | Senaryo | Amaç | Prompt / Veri Seti Kaynağı |
|-----------------|----------|------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Gömülü özetleyici için varsayılan SLM seçen Edge platform ekibi | Aday modeller arasında gecikme + p95 + token/sn karşılaştırması üretin | Inline `PROMPT` var + ortam `BENCH_MODELS` listesi |

### Senaryo Anlatımı

Ürün mühendisliği, çevrimdışı toplantı notları özelliği için varsayılan hafif bir özetleme modeli seçmelidir. Sabit bir prompt seti (aşağıdaki örneğe bakın) üzerinden kontrollü deterministik karşılaştırmalar (temperature=0) yaparlar ve GPU hızlandırma ile ve olmadan gecikme + throughput metriklerini toplarlar.

### Örnek Prompt Set JSON (genişletilebilir)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Her modeli her bir prompt için döngüye alın, dağılım metriklerini türetmek ve aykırı değerleri tespit etmek için prompt başına gecikmeyi yakalayın.

## Model Seçim Çerçevesi

| Boyut | Metrik | Neden Önemli? |
|----------|--------|----------------|
| Gecikme | ortalama / p95 | Kullanıcı deneyimi tutarlılığı |
| Throughput | token/sn | Toplu ve akış ölçeklenebilirliği |
| Bellek | yerleşik boyut | Cihaz uyumu ve eşzamanlılık |
| Kalite | rubrik promptları | Görev uygunluğu |
| Ayak İzi | disk önbelleği | Dağıtım ve güncellemeler |
| Lisans | kullanım izni | Ticari uyumluluk |

## Özel Model ile Genişletme

Yüksek seviyeli desen (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Gelişen adaptör arayüzleri için resmi repo'ya danışın:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Sorun Giderme

| Sorun | Sebep | Çözüm |
|-------|-------|-----|
| mistral-7b'de OOM | Yetersiz RAM/GPU | Diğer modelleri durdurun; daha küçük bir varyant deneyin |
| İlk yanıt yavaş | Soğuk yükleme | Hafif bir prompt ile periyodik olarak sıcak tutun |
| İndirme duraklıyor | Ağ kararsızlığı | Tekrar deneyin; yoğun olmayan saatlerde önceden indirin |

## Referanslar

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Pazartesileri: https://aka.ms/model-mondays
- Hugging Face Model Keşfi: https://huggingface.co/models

---

**Oturum Süresi**: 30 dakika (+ isteğe bağlı derin dalış)  
**Zorluk Seviyesi**: Orta

### İsteğe Bağlı Geliştirmeler

| Geliştirme | Faydası | Nasıl |
|-------------|---------|-----|
| Akış İlk Token Gecikmesi | Algılanan yanıt hızını ölçer | `BENCH_STREAM=1` ile karşılaştırmayı çalıştırın (`Workshop/samples/session03` içindeki geliştirilmiş script) |
| Deterministik Mod | Kararlı regresyon karşılaştırmaları | `temperature=0`, sabit prompt seti, JSON çıktıları sürüm kontrolü altında yakalayın |
| Kalite Rubrik Puanlama | Niteliksel boyut ekler | Beklenen yönleri içeren `prompts.json` dosyasını koruyun; puanları (1–5) manuel olarak veya ikincil modelle açıklayın |
| CSV / Markdown Dışa Aktarma | Paylaşılabilir rapor | Scripti `benchmark_report.md` yazacak şekilde genişletin, tablo ve önemli noktalarla |
| Model Yetkinlik Etiketleri | Daha sonra otomatik yönlendirmeye yardımcı olur | `{alias: {capabilities:[], size_mb:..}}` içeren `models.json` dosyasını koruyun |
| Önbellek Isınma Aşaması | Soğuk başlangıç önyargısını azaltır | Zamanlama döngüsünden önce bir sıcak tur çalıştırın (zaten uygulanmış) |
| Yüzdelik Doğruluk | Sağlam uç gecikme | Numpy yüzdelik kullanın (zaten yeniden düzenlenmiş scriptte mevcut) |
| Token Maliyet Yaklaşımı | Ekonomik karşılaştırma | Yaklaşık maliyet = (token/sn * istek başına ortalama token) * enerji tahmini |
| Başarısız Modelleri Otomatik Atlama | Toplu çalışmalarda dayanıklılık | Her karşılaştırmayı try/except içinde sarın ve durum alanını işaretleyin |

#### Minimal Markdown Dışa Aktarma Parçası

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Deterministik Prompt Seti Örneği

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Karşılaştırılabilir metrikler için rastgele promptlar yerine statik listeyi döngüye alın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->