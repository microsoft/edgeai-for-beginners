# ورکشاپ نوٹ بکس - فوری آغاز گائیڈ

## مواد کی فہرست

- [ضروریات](../../../../Workshop/notebooks)
- [ابتدائی سیٹ اپ](../../../../Workshop/notebooks)
- [سیشن 04: ماڈل موازنہ](../../../../Workshop/notebooks)
- [سیشن 05: ملٹی ایجنٹ آرکیسٹریٹر](../../../../Workshop/notebooks)
- [سیشن 06: ارادے پر مبنی ماڈل روٹنگ](../../../../Workshop/notebooks)
- [ماحولیاتی متغیرات](../../../../Workshop/notebooks)
- [عام کمانڈز](../../../../Workshop/notebooks)

---

## ضروریات

### 1. فاؤنڈری لوکل انسٹال کریں

**ونڈوز:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**انسٹالیشن کی تصدیق کریں:**
```bash
foundry --version
```

### 2. پائتھون ڈیپینڈنسیز انسٹال کریں

```bash
cd Workshop
pip install -r requirements.txt
```

یا انفرادی طور پر انسٹال کریں:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## ابتدائی سیٹ اپ

### فاؤنڈری لوکل سروس شروع کریں

**کسی بھی نوٹ بک چلانے سے پہلے ضروری ہے:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

متوقع آؤٹ پٹ:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### ماڈلز ڈاؤن لوڈ اور لوڈ کریں

نوٹ بکس ان ماڈلز کو ڈیفالٹ کے طور پر استعمال کرتی ہیں:

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

### سیٹ اپ کی تصدیق کریں

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## سیشن 04: ماڈل موازنہ

### مقصد
چھوٹے زبان ماڈلز (SLM) اور بڑے زبان ماڈلز (LLM) کے درمیان کارکردگی کا موازنہ کریں۔

### فوری سیٹ اپ

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### نوٹ بک چلانا

1. **کھولیں** `session04_model_compare.ipynb` VS کوڈ یا Jupyter میں
2. **کرنل ری اسٹارٹ کریں** (Kernel → Restart Kernel)
3. **تمام سیلز کو ترتیب وار چلائیں**

### کلیدی کنفیگریشن

**ڈیفالٹ ماڈلز:**
- **SLM:** `phi-4-mini` (~4GB RAM، تیز)
- **LLM:** `qwen2.5-3b` (~3GB RAM، میموری کے لیے بہتر)

**ماحولیاتی متغیرات (اختیاری):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### متوقع آؤٹ پٹ

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

### حسب ضرورت

**مختلف ماڈلز استعمال کریں:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**حسب ضرورت پرامپٹ:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### توثیق چیک لسٹ

- [ ] سیل 12 درست ماڈلز دکھاتا ہے (phi-4-mini، qwen2.5-3b)
- [ ] سیل 12 درست اینڈ پوائنٹ دکھاتا ہے (پورٹ 59959)
- [ ] سیل 16 تشخیصی پاس کرتا ہے (✅ سروس چل رہی ہے)
- [ ] سیل 20 پری فلائٹ چیک پاس کرتا ہے (دونوں ماڈلز ٹھیک ہیں)
- [ ] سیل 22 موازنہ مکمل کرتا ہے لیٹنسی ویلیوز کے ساتھ
- [ ] سیل 24 توثیق دکھاتا ہے 🎉 تمام چیکس پاس ہو گئے!

### وقت کا تخمینہ
- **پہلی بار چلانا:** 5-10 منٹ (ماڈلز ڈاؤن لوڈ سمیت)
- **بعد کے رنز:** 1-2 منٹ

---

## سیشن 05: ملٹی ایجنٹ آرکیسٹریٹر

### مقصد
فاؤنڈری لوکل SDK کا استعمال کرتے ہوئے ملٹی ایجنٹ تعاون کا مظاہرہ کریں - ایجنٹس مل کر بہتر نتائج پیدا کرتے ہیں۔

### فوری سیٹ اپ

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### نوٹ بک چلانا

1. **کھولیں** `session05_agents_orchestrator.ipynb`
2. **کرنل ری اسٹارٹ کریں**
3. **تمام سیلز کو ترتیب وار چلائیں**

### کلیدی کنفیگریشن

**ڈیفالٹ سیٹ اپ (دونوں ایجنٹس کے لیے ایک ہی ماڈل):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**ایڈوانس سیٹ اپ (مختلف ماڈلز):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### آرکیٹیکچر

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

### متوقع آؤٹ پٹ

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

### توسیعات

**مزید ایجنٹس شامل کریں:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**بیچ ٹیسٹنگ:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### وقت کا تخمینہ
- **پہلی بار چلانا:** 3-5 منٹ
- **بعد کے رنز:** ہر سوال کے لیے 1-2 منٹ

---

## سیشن 06: ارادے پر مبنی ماڈل روٹنگ

### مقصد
ارادے کا پتہ لگا کر پرامپٹس کو خصوصی ماڈلز کی طرف ذہانت سے روٹ کریں۔

### فوری سیٹ اپ

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**نوٹ:** سیشن 06 زیادہ سے زیادہ مطابقت کے لیے CPU ماڈلز کو ڈیفالٹ کرتا ہے۔

### نوٹ بک چلانا

1. **کھولیں** `session06_models_router.ipynb`
2. **کرنل ری اسٹارٹ کریں**
3. **تمام سیلز کو ترتیب وار چلائیں**

### کلیدی کنفیگریشن

**ڈیفالٹ کیٹلاگ (CPU ماڈلز):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**متبادل (GPU ماڈلز):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### ارادے کا پتہ لگانا

روٹر ارادے کا پتہ لگانے کے لیے regex پیٹرنز استعمال کرتا ہے:

| ارادہ | پیٹرن کی مثالیں | روٹ کیا گیا |
|-------|-----------------|-----------|
| `code` | "refactor"، "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize"، "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize"، "tl;dr" | phi-4-mini-cpu |
| `general` | باقی سب | phi-4-mini-cpu |

### متوقع آؤٹ پٹ

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

### حسب ضرورت

**حسب ضرورت ارادہ شامل کریں:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**ٹوکین ٹریکنگ فعال کریں:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### GPU ماڈلز پر سوئچ کرنا

اگر آپ کے پاس 8GB+ VRAM ہے:

1. **سیل #6** میں، CPU کیٹلاگ کو کمنٹ کریں
2. GPU کیٹلاگ کو ان کمنٹ کریں
3. GPU ماڈلز لوڈ کریں:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. کرنل ری اسٹارٹ کریں اور نوٹ بک دوبارہ چلائیں

### وقت کا تخمینہ
- **پہلی بار چلانا:** 5-10 منٹ (ماڈل لوڈنگ)
- **بعد کے رنز:** ہر ٹیسٹ کے لیے 30-60 سیکنڈ

---

## ماحولیاتی متغیرات

### عالمی کنفیگریشن

Jupyter/VS کوڈ شروع کرنے سے پہلے سیٹ کریں:

**ونڈوز (کمانڈ پرامپٹ):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**ونڈوز (پاور شیل):**
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

### نوٹ بک میں کنفیگریشن

کسی بھی نوٹ بک کے آغاز میں سیٹ کریں:

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

## عام کمانڈز

### سروس مینجمنٹ

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

### ماڈل مینجمنٹ

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

### اینڈ پوائنٹس کی جانچ

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

### تشخیصی کمانڈز

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

## بہترین طریقے

### کسی بھی نوٹ بک شروع کرنے سے پہلے

1. **چیک کریں کہ سروس چل رہی ہے:**
   ```bash
   foundry service status
   ```

2. **تصدیق کریں کہ ماڈلز لوڈ ہیں:**
   ```bash
   foundry model ls
   ```

3. **نوٹ بک کرنل ری اسٹارٹ کریں** اگر دوبارہ چلانا ہو

4. **تمام آؤٹ پٹس صاف کریں** ایک صاف رن کے لیے

### وسائل کا انتظام

1. **ڈیفالٹ کے طور پر CPU ماڈلز استعمال کریں** مطابقت کے لیے
2. **GPU ماڈلز پر سوئچ کریں** صرف اگر آپ کے پاس 8GB+ VRAM ہو
3. **دیگر GPU ایپلیکیشنز بند کریں** چلانے سے پہلے
4. **سروس کو چلتا رکھیں** نوٹ بک سیشنز کے درمیان
5. **وسائل کے استعمال کی نگرانی کریں** ٹاسک مینیجر / nvidia-smi کے ساتھ

### خرابیوں کا سراغ لگانا

1. **ہمیشہ پہلے سروس چیک کریں** کوڈ ڈیبگ کرنے سے پہلے
2. **کرنل ری اسٹارٹ کریں** اگر آپ کو پرانی کنفیگریشن نظر آئے
3. **تشخیصی سیلز دوبارہ چلائیں** کسی بھی تبدیلی کے بعد
4. **ماڈل کے نام چیک کریں** جو لوڈ کیے گئے ہیں
5. **اینڈ پوائنٹ پورٹ کی تصدیق کریں** کہ سروس اسٹیٹس سے میل کھاتا ہے

---

## فوری حوالہ: ماڈل کے عرفی نام

### عام ماڈلز

| عرفی نام | سائز | بہترین استعمال | RAM/VRAM | ویریئنٹس |
|---------|------|----------------|----------|----------|
| `phi-4-mini` | ~4B | عمومی چیٹ، خلاصہ | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | کوڈ جنریشن، ریفیکٹرنگ | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | عمومی کام، موثر | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | تیز، کم وسائل | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | درجہ بندی، کم سے کم وسائل | 1-2GB | `-cpu`, `-cuda-gpu` |

### ویریئنٹ نام

- **بنیادی نام** (جیسے، `phi-4-mini`): آپ کے ہارڈویئر کے لیے بہترین ویریئنٹ خود بخود منتخب کرتا ہے
- **`-cpu`**: CPU کے لیے بہتر، ہر جگہ کام کرتا ہے
- **`-cuda-gpu`**: NVIDIA GPU کے لیے بہتر، 8GB+ VRAM کی ضرورت ہے
- **`-npu`**: Qualcomm NPU کے لیے بہتر، NPU ڈرائیورز کی ضرورت ہے

**تجویز:** بنیادی نام استعمال کریں (بغیر لاحقہ کے) اور فاؤنڈری لوکل کو بہترین ویریئنٹ خود بخود منتخب کرنے دیں۔

---

## کامیابی کے اشارے

آپ تیار ہیں جب آپ دیکھیں:

✅ `foundry service status` "running" دکھاتا ہے  
✅ `foundry model ls` آپ کے مطلوبہ ماڈلز دکھاتا ہے  
✅ سروس درست اینڈ پوائنٹ پر قابل رسائی ہے  
✅ ہیلتھ چیک 200 OK واپس کرتا ہے  
✅ نوٹ بک تشخیصی سیلز پاس کرتے ہیں  
✅ آؤٹ پٹ میں کوئی کنکشن ایرر نہیں ہے  

---

## مدد حاصل کرنا

### دستاویزات
- **مین ریپوزٹری**: https://github.com/microsoft/Foundry-Local
- **پائتھون SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI حوالہ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **خرابیوں کا سراغ لگانا**: اس ڈائریکٹری میں `troubleshooting.md` دیکھیں

### GitHub مسائل
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**آخری اپ ڈیٹ:** 8 اکتوبر، 2025  
**ورژن:** ورکشاپ نوٹ بکس 2.0  

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔