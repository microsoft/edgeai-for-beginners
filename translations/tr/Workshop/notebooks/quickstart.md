# Atölye Not Defterleri - Hızlı Başlangıç Kılavuzu

## İçindekiler

- [Ön Koşullar](../../../../Workshop/notebooks)
- [İlk Kurulum](../../../../Workshop/notebooks)
- [Oturum 04: Model Karşılaştırması](../../../../Workshop/notebooks)
- [Oturum 05: Çoklu Ajan Orkestratörü](../../../../Workshop/notebooks)
- [Oturum 06: Niyet Tabanlı Model Yönlendirme](../../../../Workshop/notebooks)
- [Ortam Değişkenleri](../../../../Workshop/notebooks)
- [Ortak Komutlar](../../../../Workshop/notebooks)

---

## Ön Koşullar

### 1. Foundry Local'ı Yükleyin

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Kurulumu Doğrula:**
```bash
foundry --version
```

### 2. Python Bağımlılıklarını Yükleyin

```bash
cd Workshop
pip install -r requirements.txt
```

Ya da tek tek yükleyin:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## İlk Kurulum

### Foundry Local Servisini Başlatın

**Herhangi bir not defterini çalıştırmadan önce gereklidir:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Beklenen çıktı:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Modelleri İndirin ve Yükleyin

Not defterleri varsayılan olarak şu modelleri kullanır:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Kurulumu Doğrula

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Oturum 04: Model Karşılaştırması

### Amaç
Küçük Dil Modelleri (SLM) ile Büyük Dil Modelleri (LLM) arasındaki performansı karşılaştırın.

### Hızlı Kurulum

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Not Defterini Çalıştırma

1. **Açın** `session04_model_compare.ipynb` dosyasını VS Code veya Jupyter'de
2. **Çekirdeği yeniden başlatın** (Kernel → Restart Kernel)
3. **Tüm hücreleri sırayla çalıştırın**

### Temel Yapılandırma

**Varsayılan Modeller:**
- **SLM:** `phi-4-mini` (~4GB RAM, daha hızlı)
- **LLM:** `qwen2.5-3b` (~3GB RAM, bellek optimizasyonlu)

**Ortam Değişkenleri (isteğe bağlı):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Beklenen Çıktı

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Özelleştirme

**Farklı modeller kullanın:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Özel istem:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Doğrulama Kontrol Listesi

- [ ] Hücre 12 doğru modelleri gösteriyor (phi-4-mini, qwen2.5-3b)
- [ ] Hücre 12 doğru uç noktayı gösteriyor (port 59959)
- [ ] Hücre 16 tanılama geçiyor (✅ Servis çalışıyor)
- [ ] Hücre 20 ön kontrol geçiyor (her iki model tamam)
- [ ] Hücre 22 karşılaştırma gecikme değerleriyle tamamlanıyor
- [ ] Hücre 24 doğrulama 🎉 TÜM KONTROLLER GEÇTİ! mesajını gösteriyor

### Zaman Tahmini
- **İlk çalıştırma:** 5-10 dakika (model indirmeleri dahil)
- **Sonraki çalıştırmalar:** 1-2 dakika

---

## Oturum 05: Çoklu Ajan Orkestratörü

### Amaç
Foundry Local SDK kullanarak çoklu ajan iş birliğini gösterin - ajanlar birlikte çalışarak daha rafine çıktılar üretir.

### Hızlı Kurulum

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Not Defterini Çalıştırma

1. **Açın** `session05_agents_orchestrator.ipynb`
2. **Çekirdeği yeniden başlatın**
3. **Tüm hücreleri sırayla çalıştırın**

### Temel Yapılandırma

**Varsayılan Kurulum (Her İki Ajan İçin Aynı Model):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Gelişmiş Kurulum (Farklı Modeller):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Mimari

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Beklenen Çıktı

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Uzantılar

**Daha fazla ajan ekleyin:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Toplu test:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Zaman Tahmini
- **İlk çalıştırma:** 3-5 dakika
- **Sonraki çalıştırmalar:** Soru başına 1-2 dakika

---

## Oturum 06: Niyet Tabanlı Model Yönlendirme

### Amaç
Tespit edilen niyete göre istemleri özel modellere akıllıca yönlendirin.

### Hızlı Kurulum

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Not:** Oturum 06 maksimum uyumluluk için varsayılan olarak CPU modellerini kullanır.

### Not Defterini Çalıştırma

1. **Açın** `session06_models_router.ipynb`
2. **Çekirdeği yeniden başlatın**
3. **Tüm hücreleri sırayla çalıştırın**

### Temel Yapılandırma

**Varsayılan Katalog (CPU Modelleri):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatif (GPU Modelleri):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Niyet Tespiti

Yönlendirici niyeti tespit etmek için regex desenlerini kullanır:

| Niyet | Örnek Desenler | Yönlendirildiği Model |
|-------|-----------------|-----------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Diğer her şey | phi-4-mini-cpu |

### Beklenen Çıktı

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Özelleştirme

**Özel niyet ekleyin:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Token takibini etkinleştirin:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### GPU Modellerine Geçiş

8GB+ VRAM'e sahipseniz:

1. **Hücre #6**'da CPU kataloğunu yorum satırı yapın
2. GPU kataloğunu yorum satırı olmaktan çıkarın
3. GPU modellerini yükleyin:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Çekirdeği yeniden başlatın ve not defterini tekrar çalıştırın

### Zaman Tahmini
- **İlk çalıştırma:** 5-10 dakika (model yükleme)
- **Sonraki çalıştırmalar:** Test başına 30-60 saniye

---

## Ortam Değişkenleri

### Genel Yapılandırma

Jupyter/VS Code'u başlatmadan önce ayarlayın:

**Windows (Komut İstemi):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Not Defteri İçinde Yapılandırma

Herhangi bir not defterinin başında ayarlayın:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Ortak Komutlar

### Servis Yönetimi

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Model Yönetimi

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Uç Noktaları Test Etme

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Tanılama Komutları

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## En İyi Uygulamalar

### Herhangi Bir Not Defterine Başlamadan Önce

1. **Servisin çalıştığını kontrol edin:**
   ```bash
   foundry service status
   ```

2. **Modellerin yüklü olduğunu doğrulayın:**
   ```bash
   foundry model ls
   ```

3. **Not defteri çekirdeğini yeniden başlatın** eğer tekrar çalıştırıyorsanız

4. **Tüm çıktıları temizleyin** temiz bir çalışma için

### Kaynak Yönetimi

1. **Varsayılan olarak CPU modellerini kullanın** uyumluluk için
2. **GPU modellerine geçin** yalnızca 8GB+ VRAM'e sahipseniz
3. **Diğer GPU uygulamalarını kapatın** çalıştırmadan önce
4. **Servisi açık tutun** not defteri oturumları arasında
5. **Kaynak kullanımını izleyin** Görev Yöneticisi / nvidia-smi ile

### Sorun Giderme

1. **Önce her zaman servisi kontrol edin** kodu hata ayıklamadan önce
2. **Çekirdeği yeniden başlatın** eğer eski yapılandırma görüyorsanız
3. **Tanılama hücrelerini yeniden çalıştırın** herhangi bir değişiklikten sonra
4. **Model adlarının eşleştiğini kontrol edin** yüklenenlerle
5. **Uç nokta portunun eşleştiğini doğrulayın** servis durumu ile

---

## Hızlı Referans: Model Takma Adları

### Yaygın Modeller

| Takma Ad | Boyut | En İyi Kullanım Alanı | RAM/VRAM | Varyantlar |
|----------|-------|-----------------------|----------|------------|
| `phi-4-mini` | ~4B | Genel sohbet, özetleme | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Kod üretimi, yeniden düzenleme | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Genel görevler, verimli | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Hızlı, düşük kaynak | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Sınıflandırma, minimal kaynak | 1-2GB | `-cpu`, `-cuda-gpu` |

### Varyant İsimlendirme

- **Temel isim** (ör. `phi-4-mini`): Donanımınıza en uygun varyantı otomatik seçer
- **`-cpu`**: CPU için optimize edilmiş, her yerde çalışır
- **`-cuda-gpu`**: NVIDIA GPU için optimize edilmiş, 8GB+ VRAM gerektirir
- **`-npu`**: Qualcomm NPU için optimize edilmiş, NPU sürücüleri gerektirir

**Öneri:** Temel isimleri (son ek olmadan) kullanın ve Foundry Local'ın en iyi varyantı otomatik seçmesine izin verin.

---

## Başarı Göstergeleri

Hazırsınız, eğer:

✅ `foundry service status` "çalışıyor" gösteriyor  
✅ `foundry model ls` gerekli modellerinizi gösteriyor  
✅ Servis doğru uç noktada erişilebilir  
✅ Sağlık kontrolü 200 OK döndürüyor  
✅ Not defteri tanılama hücreleri geçiyor  
✅ Çıktıda bağlantı hatası yok  

---

## Yardım Alma

### Belgeler
- **Ana Depo:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referansı:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Sorun Giderme:** Bu dizindeki `troubleshooting.md` dosyasına bakın

### GitHub Sorunları
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Son Güncelleme:** 8 Ekim 2025  
**Sürüm:** Atölye Not Defterleri 2.0

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.