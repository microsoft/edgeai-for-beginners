<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T22:57:57+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "tr"
}
-->
# Oturum 4: En Son Modelleri Keşfet – LLM'ler, SLM'ler ve Cihaz Üzerinde Çıkarım

## Özet

Yerel ve bulut çıkarım senaryoları için Büyük Dil Modelleri (LLM'ler) ve Küçük Dil Modelleri (SLM'ler) karşılaştırmasını yapın. ONNX Runtime hızlandırması, WebGPU yürütmesi ve hibrit RAG deneyimlerini kullanarak dağıtım modellerini öğrenin. Yerel bir modelle Chainlit RAG demosu ve isteğe bağlı OpenWebUI keşfi içerir. WebGPU çıkarım başlangıcını uyarlayacak ve Phi ile GPT-OSS-20B'nin yetenek ve maliyet/performans dengelerini değerlendireceksiniz.

## Öğrenme Hedefleri

- **Karşılaştır** SLM ve LLM'yi gecikme, bellek ve kalite eksenlerinde
- **Dağıt** modelleri ONNXRuntime ve (desteklendiği yerlerde) WebGPU ile
- **Çalıştır** tarayıcı tabanlı çıkarım (gizliliği koruyan etkileşimli demo)
- **Entegre et** bir Chainlit RAG hattını yerel bir SLM arka ucu ile
- **Değerlendir** hafif kalite + maliyet ölçütleri kullanarak

## Ön Koşullar

- Oturumlar 1–3 tamamlandı
- `chainlit` yüklü (Module08 için `requirements.txt` içinde zaten mevcut)
- WebGPU destekli tarayıcı (Windows 11'de Edge / Chrome en son sürüm)
- Foundry Local çalışıyor (`foundry service status`)

### Platformlar Arası Notlar

Windows birincil hedef ortam olmaya devam ediyor. Yerel macOS ikili dosyalarını bekleyen geliştiriciler için:
1. Foundry Local'ı bir Windows 11 VM'de (Parallels / UTM) veya uzak bir Windows iş istasyonunda çalıştırın.
2. Hizmeti açın (varsayılan port 5273) ve macOS'ta ayarlayın:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Önceki oturumlarda olduğu gibi aynı Python sanal ortam adımlarını kullanın.

Chainlit kurulumu (her iki platformda):
```bash
pip install chainlit
```

## Demo Akışı (30 dk)

### 1. Phi (SLM) ve GPT-OSS-20B (LLM) Karşılaştırması (6 dk)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Takip edin: yanıt derinliği, gerçek doğruluk, stilistik zenginlik, gecikme.

GPU etkinleştirildikten sonra throughput değişikliklerini gözlemleyin (yalnızca CPU).

### 3. Tarayıcıda WebGPU Çıkarımı (6 dk)

Başlangıç `04-webgpu-inference` dosyasını uyarlayın (oluşturun `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Dosyayı bir tarayıcıda açın; düşük gecikmeli yerel dönüşü gözlemleyin.

### 4. Chainlit RAG Sohbet Uygulaması (7 dk)

Minimal `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Çalıştırın:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Başlangıç Projesi: `04-webgpu-inference` Uyarlayın (6 dk)

Teslimatlar:
- Yer tutucu fetch mantığını akış tokenları ile değiştirin (`stream=True` endpoint varyantını etkinleştirdikten sonra kullanın)
- Gecikme grafiği ekleyin (istemci tarafı) phi ve gpt-oss-20b geçişleri için
- RAG bağlamını satır içi yerleştirin (referans belgeler için metin alanı)

## Değerlendirme Ölçütleri

| Kategori | Phi-4-mini | GPT-OSS-20B | Gözlem |
|----------|------------|-------------|-------------|
| Gecikme (soğuk) | Hızlı | Daha yavaş | SLM hızlı ısınır |
| Bellek | Düşük | Yüksek | Cihaz uygunluğu |
| Bağlam uyumu | İyi | Güçlü | Daha büyük model daha ayrıntılı olabilir |
| Maliyet (yerel) | Minimal | Daha yüksek (kaynak) | Enerji/zaman dengesi |
| En iyi kullanım durumu | Edge uygulamaları | Derin akıl yürütme | Hibrit hat mümkün |

## Ortamı Doğrulama

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Sorun Giderme

| Belirti | Sebep | Çözüm |
|---------|-------|--------|
| Web sayfası fetch başarısız | CORS veya hizmet kapalı | Endpoint'i doğrulamak için `curl` kullanın; gerekirse CORS proxy etkinleştirin |
| Chainlit boş | Ortam aktif değil | Venv'i etkinleştirin ve bağımlılıkları yeniden yükleyin |
| Yüksek gecikme | Model yeni yüklendi | Küçük bir prompt dizisiyle ısıtın |

## Referanslar

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Belgeleri: https://docs.chainlit.io
- RAG Değerlendirme (Ragas): https://docs.ragas.io

---

**Oturum Süresi**: 30 dk  
**Zorluk**: İleri

## Örnek Senaryo ve Atölye Eşleştirmesi

| Atölye Materyalleri | Senaryo | Hedef | Veri / Prompt Kaynağı |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Yönetici özeti oluşturucu için SLM ve LLM değerlendiren mimari ekip | Gecikme + token kullanım farkını ölçmek | Tek `COMPARE_PROMPT` ortam değişkeni |
| `chainlit_app.py` (RAG demo) | Dahili bilgi asistanı prototipi | Kısa yanıtları minimal sözcüksel geri alımla temellendirmek | Dosyadaki satır içi `DOCS` listesi |
| `webgpu_demo.html` | Gelecekteki cihaz üzerinde tarayıcı çıkarım önizlemesi | Düşük gecikmeli yerel dönüş + UX anlatımı göster | Yalnızca canlı kullanıcı prompt'u |

### Senaryo Anlatımı
Ürün organizasyonu bir yönetici brifing oluşturucu istiyor. Hafif bir SLM (phi‑4‑mini) özetler oluşturur; daha büyük bir LLM (gpt‑oss‑20b) yalnızca yüksek öncelikli raporları iyileştirebilir. Oturum betikleri hibrit bir tasarımı haklı çıkarmak için ampirik gecikme ve token metriklerini yakalar, Chainlit demosu ise küçük model yanıtlarını gerçekçi tutan temellendirilmiş geri alımı gösterir. WebGPU konsept sayfası, tarayıcı hızlanması olgunlaştığında tamamen istemci tarafı işleme için bir vizyon yolu sağlar.

### Minimal RAG Bağlamı (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hibrit Taslak→İyileştirme Akışı (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Her iki gecikme bileşenini izleyerek karışık ortalama maliyeti raporlayın.

### İsteğe Bağlı Geliştirmeler

| Odak | Geliştirme | Neden | Uygulama İpucu |
|-------|------------|-----|---------------------|
| Karşılaştırmalı Metrikler | Token kullanımı + ilk token gecikmesini izleyin | Kapsamlı performans görünümü | Geliştirilmiş benchmark betiğini kullanın (Oturum 3) `BENCH_STREAM=1` ile |
| Hibrit Hat | SLM taslak → LLM iyileştirme | Gecikme ve maliyeti azaltın | Phi-4-mini ile oluşturun, özeti gpt-oss-20b ile iyileştirin |
| Akışlı UI | Chainlit'te daha iyi UX | Kademeli geri bildirim | Yerel akış etkinleştirildiğinde `stream=True` kullanın; parçaları biriktirin |
| WebGPU Önbellekleme | Daha hızlı JS başlatma | Yeniden derleme yükünü azaltın | Derlenmiş shader eserlerini önbelleğe alın (gelecekteki runtime yeteneği) |
| Deterministik QA Seti | Adil model karşılaştırması | Varyansı kaldırın | Sabit prompt listesi + değerlendirme çalışmaları için `temperature=0` |
| Çıktı Puanlama | Yapılandırılmış kalite lensi | Anlatıların ötesine geçin | Basit bir rubrik: tutarlılık / gerçeklik / kısalık (1–5) |
| Enerji / Kaynak Notları | Sınıf tartışması | Ticaret dengelerini gösterin | OS monitörlerini kullanın (Görev Yöneticisi, `nvidia-smi`) + benchmark betik çıktıları |
| Maliyet Simülasyonu | Bulut öncesi gerekçe | Ölçeklendirme planı | Tokenları TCO anlatımı için varsayımsal bulut fiyatlandırmasına eşleyin |
| Gecikme Ayrıştırması | Darboğazları belirleyin | Optimizasyonları hedefleyin | Prompt hazırlama, istek gönderme, ilk token, tam tamamlama ölçümü |
| RAG + LLM Geri Dönüş | Kalite güvenlik ağı | Zor soruları iyileştirin | SLM yanıt uzunluğu < eşik veya düşük güven → yükseltme |

#### Örnek Hibrit Taslak/İyileştirme Deseni

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Gecikme Ayrıntısı Taslağı

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Adil karşılaştırmalar için modeller arasında tutarlı ölçüm çerçevesi kullanın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->