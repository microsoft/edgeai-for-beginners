<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66985bbc1a3f888335c827173a58bc5e",
  "translation_date": "2025-10-28T21:50:05+00:00",
  "source_file": "Workshop/Session06-ModelsAsTools.md",
  "language_code": "tr"
}
-->
# Oturum 6: Foundry Local – Modelleri Araç Olarak Kullanma

## Özet

Modelleri yerel bir AI işletim katmanında birleştirilebilir araçlar olarak ele alın. Bu oturumda, birden fazla özel SLM/LLM çağrısını zincirleme, görevleri seçici bir şekilde yönlendirme ve uygulamalara birleşik bir SDK yüzeyi sunma yöntemleri gösterilmektedir. Hafif bir model yönlendirici + görev planlayıcı oluşturacak, bunu bir uygulama betiğine entegre edecek ve üretim iş yükleri için Azure AI Foundry'ye ölçeklendirme yolunu tasarlayacaksınız.

## Öğrenme Hedefleri

- **Modelleri** belirlenmiş yeteneklere sahip atomik araçlar olarak kavrayın
- **İstekleri** niyet / sezgisel puanlamaya göre yönlendirin
- **Çıktıları** çok adımlı görevler arasında zincirleyin (ayır → çöz → iyileştir)
- **Birleşik bir istemci API'sini** aşağı akış uygulamalarına entegre edin
- **Tasarımı** buluta ölçeklendirin (aynı OpenAI uyumlu sözleşme)

## Ön Koşullar

- Oturumlar 1–5 tamamlanmış olmalı
- Birden fazla yerel model önbelleğe alınmış olmalı (örneğin, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Platformlar Arası Ortam Kod Parçacığı

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS'tan Uzaktan/VM hizmet erişimi:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Akışı (30 dakika)

### 1. Araç Yetenek Bildirimi (5 dakika)

`samples/06-tools/models_catalog.py` oluşturun:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Niyet Algılama ve Yönlendirme (8 dakika)

`samples/06-tools/router.py` oluşturun:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Çok Adımlı Görev Zincirleme (7 dakika)

`samples/06-tools/pipeline.py` oluşturun:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Başlangıç Projesi: `06-models-as-tools`'u Uyarlayın (5 dakika)

Geliştirmeler:
- Akışkan token desteği ekleyin (kademeli UI güncellemesi)
- Güven puanlaması ekleyin: sözcüksel örtüşme veya istem kriteri
- İzleme JSON'u dışa aktarın (niyet → model → gecikme → token kullanımı)
- Tekrarlanan alt adımlar için önbellek yeniden kullanımını uygulayın

### 5. Azure'a Ölçeklendirme Yolu (5 dakika)

| Katman | Yerel (Foundry) | Bulut (Azure AI Foundry) | Geçiş Stratejisi |
|-------|-----------------|--------------------------|---------------------|
| Yönlendirme | Sezgisel Python | Dayanıklı mikro hizmet | API'yi kapsülleyin ve dağıtın |
| Modeller | SLM'ler önbelleğe alınmış | Yönetilen dağıtımlar | Yerel adları dağıtım kimliklerine eşleyin |
| Gözlemlenebilirlik | CLI istatistikleri / manuel | Merkezi günlükleme ve metrikler | Yapılandırılmış izleme olayları ekleyin |
| Güvenlik | Sadece yerel ana bilgisayar | Azure kimlik doğrulama / ağ | Gizli bilgiler için anahtar kasası tanıtın |
| Maliyet | Cihaz kaynağı | Tüketim faturalandırması | Bütçe koruma önlemleri ekleyin |

## Doğrulama Kontrol Listesi

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Niyet tabanlı model seçimi ve nihai iyileştirilmiş çıktı bekleniyor.

## Sorun Giderme

| Sorun | Sebep | Çözüm |
|---------|-------|-----|
| Tüm görevler aynı modele yönlendiriliyor | Zayıf kurallar | INTENT_RULES regex setini zenginleştirin |
| Boru hattı adım ortasında başarısız oluyor | Yüklenmiş model eksik | `foundry model run <model>` komutunu çalıştırın |
| Düşük çıktı tutarlılığı | İyileştirme aşaması yok | Özetleme/doğrulama geçişi ekleyin |

## Referanslar

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry Belgeleri: https://learn.microsoft.com/azure/ai-foundry
- İstem Kalitesi Kalıpları: Bkz. Oturum 2

---

**Oturum Süresi**: 30 dakika  
**Zorluk Seviyesi**: Uzman

## Örnek Senaryo ve Atölye Eşleştirmesi

| Atölye Betikleri / Not Defterleri | Senaryo | Amaç | Veri Seti / Katalog Kaynağı |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Karışık niyet istemlerini işleyen geliştirici asistanı (yeniden düzenleme, özetleme, sınıflandırma) | Sezgisel niyet → model takma adı yönlendirme ve token kullanımı | Satır içi `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Karmaşık kodlama yardım görevi için çok adımlı planlama ve iyileştirme | Ayır → özel yürütme → özetleme iyileştirme adımı | Aynı `CATALOG`; adımlar plan çıktısından türetilmiş |

### Senaryo Anlatımı
Bir mühendislik verimlilik aracı, heterojen görevler alır: kodu yeniden düzenleme, mimari notları özetleme, geri bildirimi sınıflandırma. Gecikmeyi ve kaynak kullanımını en aza indirmek için küçük bir genel model planlama ve özetleme yapar, kod uzmanı bir model yeniden düzenleme işlemini gerçekleştirir ve hafif bir sınıflandırma yeteneğine sahip model geri bildirimi etiketler. Boru hattı betiği zincirleme + iyileştirme gösterirken, yönlendirici betiği uyarlanabilir tek istem yönlendirmesini izole eder.

### Katalog Anlık Görüntüsü
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Örnek Test İstemleri
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### İzleme Uzantısı (İsteğe Bağlı)
`models_pipeline.py` için adım başına izleme JSON satırları ekleyin:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Yükseltme Sezgisi (Fikir)
Eğer planda "optimize", "security" gibi anahtar kelimeler varsa veya adım uzunluğu > 280 karakter ise → yalnızca o adım için daha büyük modele (örneğin, `gpt-oss-20b`) yükseltme yapın.

### İsteğe Bağlı Geliştirmeler

| Alan | Geliştirme | Değer | İpucu |
|------|-------------|-------|------|
| Önbellekleme | Yöneticiyi + istemci nesnelerini yeniden kullanın | Daha düşük gecikme, daha az yük | `workshop_utils.get_client` kullanın |
| Kullanım Metrikleri | Tokenları ve adım başına gecikmeyi yakalayın | Profil oluşturma ve optimizasyon | Her yönlendirilmiş çağrıyı zamanlayın; izleme listesinde saklayın |
| Uyarlanabilir Yönlendirme | Güven / maliyet farkındalığı | Daha iyi kalite-maliyet dengesi | Puanlama ekleyin: eğer istem > N karakter veya regex alanı eşleşirse → daha büyük modele yükseltin |
| Dinamik Yetenek Kaydı | Katalogu sıcak yükleme | Yeniden başlatma yeniden dağıtım yok | Çalışma zamanında `catalog.json` yükleyin; dosya zaman damgasını izleyin |
| Geri Dönüş Stratejisi | Hatalar altında sağlamlık | Daha yüksek kullanılabilirlik | Birincil dene → istisna durumunda yedek takma ad |
| Akışkan Boru Hattı | Erken geri bildirim | UX iyileştirme | Her adımı akışla gönderin ve nihai iyileştirme girdisini tamponlayın |
| Vektör Niyet Gömüleri | Daha ayrıntılı yönlendirme | Daha yüksek niyet doğruluğu | İstemi gömün, kümeleyin ve merkez → yetenek eşlemesi yapın |
| İzleme Dışa Aktarma | Denetlenebilir zincir | Uyumluluk/raporlama | JSON satırları yayınlayın: adım, niyet, model, gecikme_ms, tokenlar |
| Maliyet Simülasyonu | Bulut öncesi tahmin | Bütçe planlama | Model başına token başına varsayımsal maliyet atayın ve görev başına toplayın |
| Deterministik Mod | Yeniden üretilebilirlik | Kararlı kıyaslama | Ortam: `temperature=0`, sabit adım sayısı |

#### İzleme Yapısı Örneği

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Uyarlanabilir Yükseltme Taslağı

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Model Katalogu Sıcak Yükleme

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.