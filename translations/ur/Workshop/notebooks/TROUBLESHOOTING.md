# ورکشاپ نوٹ بکس - خرابیوں کا پتہ لگانے کی گائیڈ

## فہرستِ مضامین

- [عام مسائل اور ان کے حل](../../../../Workshop/notebooks)
- [سیشن 04 کے مخصوص مسائل](../../../../Workshop/notebooks)
- [سیشن 05 کے مخصوص مسائل](../../../../Workshop/notebooks)
- [سیشن 06 کے مخصوص مسائل](../../../../Workshop/notebooks)
- [ہارڈویئر کے مخصوص مسائل](../../../../Workshop/notebooks)
- [تشخیصی کمانڈز](../../../../Workshop/notebooks)
- [مدد حاصل کریں](../../../../Workshop/notebooks)

---

## عام مسائل اور ان کے حل

### 🔴 CUDA میموری ختم ہو گئی

**خرابی کا پیغام:**
```
CUDA failure 2: out of memory
```

**وجہ:** GPU کے پاس ماڈل لوڈ کرنے کے لیے کافی VRAM نہیں ہے۔

**حل:**

#### آپشن 1: CPU ویریئنٹس استعمال کریں (تجویز کردہ)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### آپشن 2: GPU پر چھوٹے ماڈلز استعمال کریں
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### آپشن 3: GPU میموری صاف کریں
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### آپشن 4: GPU میموری بڑھائیں (اگر ممکن ہو)
- براؤزر ٹیبز، ویڈیو ایڈیٹرز، یا دیگر GPU ایپس بند کریں
- ونڈوز کے بصری اثرات کم کریں
- اگر آپ کے پاس انٹیگریٹڈ + ڈیڈیکیٹڈ GPU ہے تو ڈیڈیکیٹڈ GPU استعمال کریں

---

### 🔴 APIConnectionError: کنکشن کی خرابی

**خرابی کا پیغام:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**وجہ:** Foundry Local سروس چل نہیں رہی یا قابل رسائی نہیں ہے۔

**حل:**

#### مرحلہ 1: سروس کی حالت چیک کریں
```bash
foundry service status
```

#### مرحلہ 2: سروس شروع کریں اگر بند ہو
```bash
foundry service start
```

#### مرحلہ 3: اینڈ پوائنٹ کی تصدیق کریں
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### مرحلہ 4: مطلوبہ ماڈلز لوڈ کریں
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### مرحلہ 5: نوٹ بک کرنل کو دوبارہ شروع کریں
سروس شروع کرنے اور ماڈلز لوڈ کرنے کے بعد، نوٹ بک کرنل کو دوبارہ شروع کریں اور تمام سیلز دوبارہ چلائیں۔

---

### 🔴 ماڈل کیٹلاگ میں نہیں ملا

**خرابی کا پیغام:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**وجہ:** ماڈل Foundry Local میں ڈاؤنلوڈ یا لوڈ نہیں ہوا۔

**حل:**

#### آپشن 1: ماڈلز ڈاؤنلوڈ اور لوڈ کریں
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### آپشن 2: آٹو-سیلیکشن موڈ استعمال کریں
اپنے CATALOG کو بیس ماڈل ناموں کے ساتھ اپ ڈیٹ کریں (بغیر `-cpu` لاحقہ کے):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK خود بخود آپ کے ہارڈویئر کے لیے بہترین ویریئنٹ (CPU، GPU، یا NPU) منتخب کرے گا۔

---

### 🔴 HttpResponseError: 500 - ماڈل لوڈ کرنے میں ناکامی

**خرابی کا پیغام:**
```
HttpResponseError: 500 - Failed loading model
```

**وجہ:** ماڈل فائل خراب یا ہارڈویئر کے ساتھ مطابقت نہیں رکھتی۔

**حل:**

#### ماڈل دوبارہ ڈاؤنلوڈ کریں
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### مختلف ویریئنٹ استعمال کریں
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: کوئی ماڈیول نہیں ملا

**خرابی کا پیغام:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**وجہ:** foundry-local-sdk پیکیج انسٹال نہیں ہے۔

**حل:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � پہلا درخواست سست

**علامت:** پہلی تکمیل میں 30+ سیکنڈ لگتے ہیں، بعد کی درخواستیں تیز ہوتی ہیں۔

**وجہ:** یہ عام بات ہے - سروس پہلی درخواست پر ماڈل کو میموری میں لوڈ کر رہی ہے۔

**حل:**

#### ماڈلز پہلے سے لوڈ کریں
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### سروس کو چلتا رہنے دیں
```bash
# Start service manually and leave it running
foundry service start
```

---

## سیشن 04 کے مخصوص مسائل

### غلط پورٹ کنفیگریشن

**مسئلہ:** نوٹ بک غلط پورٹ سے جڑ رہی ہے (55769 بمقابلہ 59959 بمقابلہ 57127)

**حل:**

1. چیک کریں کہ Foundry Local کون سی پورٹ استعمال کر رہا ہے:
```bash
foundry service status
# Note the port number displayed
```

2. نوٹ بک میں سیل 10 کو اپ ڈیٹ کریں:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. کرنل کو دوبارہ شروع کریں اور سیلز 6، 8، 10، 12، 16، 20، 22 دوبارہ چلائیں

---

### غلط ماڈل کا انتخاب

**مسئلہ:** نوٹ بک gpt-oss-20b یا qwen2.5-7b دکھا رہا ہے بجائے qwen2.5-3b کے

**حل:**

1. نوٹ بک کرنل کو دوبارہ شروع کریں (پرانا ویریبل اسٹیٹ صاف کرتا ہے)
2. سیل 10 دوبارہ چلائیں (ماڈل عرفیات سیٹ کریں)
3. سیل 12 دوبارہ چلائیں (کنفیگریشن دکھائیں)
4. **تصدیق کریں:** سیل 12 کو `LLM Model: qwen2.5-3b` دکھانا چاہیے

---

### تشخیصی سیل ناکام

**مسئلہ:** سیل 16 "❌ Foundry Local سروس نہیں ملی!" دکھاتا ہے

**حل:**

1. تصدیق کریں کہ سروس چل رہی ہے:
```bash
foundry service status
```

2. اینڈ پوائنٹ کو دستی طور پر ٹیسٹ کریں:
```bash
curl http://localhost:59959/v1/models
```

3. اگر curl کام کرتا ہے لیکن نوٹ بک نہیں:
   - نوٹ بک کرنل کو دوبارہ شروع کریں
   - سیلز کو ترتیب وار دوبارہ چلائیں: 6، 8، 10، 12، 14، 16

4. اگر curl ناکام ہو:
   - سروس شروع کریں: `foundry service start`
   - ماڈلز لوڈ کریں: `foundry model run phi-4-mini` اور `foundry model run qwen2.5-3b`

---

### پری-فلائٹ چیک ناکام

**مسئلہ:** سیل 20 کنکشن کی خرابی دکھاتا ہے حالانکہ تشخیص کامیاب ہوئی

**حل:**

1. چیک کریں کہ ماڈلز لوڈ ہیں:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. اگر ماڈلز غائب ہیں:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. ماڈلز لوڈ ہونے کے بعد سیل 20 دوبارہ چلائیں

---

### موازنہ None ویلیوز کے ساتھ ناکام

**مسئلہ:** سیل 22 مکمل ہوتا ہے لیکن لیٹنسی کو None دکھاتا ہے

**حل:**

1. پہلے پری-فلائٹ پاس ہونے کی تصدیق کریں (سیل 20)
2. سیل 22 دوبارہ چلائیں - ماڈلز کو پہلی درخواست پر گرم ہونے کی ضرورت ہو سکتی ہے
3. تصدیق کریں کہ دونوں ماڈلز لوڈ ہیں: `foundry model ls`

---

## سیشن 05 کے مخصوص مسائل

### ایجنٹ غلط ماڈل استعمال کر رہا ہے

**مسئلہ:** ایجنٹ متوقع ماڈل استعمال نہیں کر رہا

**حل:**

کنفیگریشن کی تصدیق کریں:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

اگر ماڈلز غلط ہیں تو کرنل کو دوبارہ شروع کریں۔

---

### میموری کانٹیکسٹ اوورفلو

**مسئلہ:** ایجنٹ کے جوابات وقت کے ساتھ خراب ہو رہے ہیں

**حل:** پہلے ہی خودکار طور پر ہینڈل کیا گیا ہے - ایجنٹس میموری میں صرف آخری 6 پیغامات رکھتے ہیں۔

---

## سیشن 06 کے مخصوص مسائل

### CPU بمقابلہ GPU ماڈل کنفیوژن

**مسئلہ:** ڈیفالٹ کنفیگریشن استعمال کرتے وقت CUDA کی خرابی ہو رہی ہے

**حل:** ڈیفالٹ کنفیگریشن اب CPU ماڈلز استعمال کرتا ہے۔ اگر آپ کو CUDA کی خرابی نظر آئے:

1. تصدیق کریں کہ آپ ڈیفالٹ CPU کیٹلاگ استعمال کر رہے ہیں:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. کرنل کو دوبارہ شروع کریں اور تمام سیلز دوبارہ چلائیں

---

### ارادے کی شناخت کام نہیں کر رہی

**مسئلہ:** پرامپٹس غلط ماڈلز کی طرف بھیجے جا رہے ہیں

**حل:**

ارادے کی شناخت ٹیسٹ کریں:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

اگر پیٹرنز کو ایڈجسٹ کرنے کی ضرورت ہو تو RULES کو اپ ڈیٹ کریں۔

---

## ہارڈویئر کے مخصوص مسائل

### NVIDIA GPU

**GPU کی حالت چیک کریں:**
```bash
nvidia-smi
```

**عام مسائل:**
- **ڈرائیور پرانا ہے**: NVIDIA ڈرائیورز اپ ڈیٹ کریں
- **CUDA ورژن کا عدم مطابقت**: Foundry Local دوبارہ انسٹال کریں
- **GPU میموری بکھری ہوئی ہے**: سسٹم کو دوبارہ شروع کریں

### Qualcomm NPU

**NPU کی حالت چیک کریں:**
```bash
foundry device info
```

**عام مسائل:**
- **NPU ڈرائیورز انسٹال نہیں ہیں**: Qualcomm NPU ڈرائیورز انسٹال کریں
- **NPU ویریئنٹ دستیاب نہیں ہے**: CPU ویریئنٹ استعمال کریں
- **ونڈوز ورژن بہت پرانا ہے**: تازہ ترین ونڈوز 11 پر اپ ڈیٹ کریں

### صرف CPU والے سسٹمز

**تجویز کردہ ماڈلز:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**کارکردگی کے نکات:**
- سب سے چھوٹے ماڈلز استعمال کریں
- max_tokens کم کریں
- پہلی درخواست کے لیے صبر بڑھائیں

---

## تشخیصی کمانڈز

### سب کچھ چیک کریں
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Python میں
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## مدد حاصل کریں

### 1. لاگز چیک کریں
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub مسائل
- موجودہ مسائل تلاش کریں: https://github.com/microsoft/Foundry-Local/issues
- نیا مسئلہ بنائیں:
  - خرابی کا پیغام (مکمل متن)
  - `foundry service status` کا آؤٹ پٹ
  - `foundry --version` کا آؤٹ پٹ
  - GPU/NPU معلومات (nvidia-smi، وغیرہ)
  - دوبارہ پیدا کرنے کے مراحل

### 3. دستاویزات
- **مین ریپوزٹری**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI حوالہ**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **خرابیوں کا پتہ لگانا**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## فوری حل چیک لسٹ

جب مسائل ہوں، تو ان کو ترتیب وار آزمائیں:

- [ ] چیک کریں کہ سروس چل رہی ہے: `foundry service status`
- [ ] سروس دوبارہ شروع کریں: `foundry service stop && foundry service start`
- [ ] تصدیق کریں کہ ماڈل موجود ہے: `foundry model ls | grep phi-4-mini`
- [ ] مطلوبہ ماڈلز لوڈ کریں: `foundry model run phi-4-mini`
- [ ] GPU میموری چیک کریں: `nvidia-smi` (اگر NVIDIA)
- [ ] CPU ویریئنٹ آزمائیں: `phi-4-mini-cpu` استعمال کریں بجائے `phi-4-mini`
- [ ] نوٹ بک کرنل کو دوبارہ شروع کریں
- [ ] نوٹ بک آؤٹ پٹس صاف کریں اور تمام سیلز دوبارہ چلائیں
- [ ] SDK دوبارہ انسٹال کریں: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] سسٹم کو دوبارہ شروع کریں (آخری حل)

---

## روک تھام کے نکات

### بہترین طریقے

1. **ہمیشہ پہلے سروس چیک کریں:**
   ```bash
   foundry service status
   ```

2. **ڈیفالٹ کے طور پر CPU ویریئنٹس استعمال کریں:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **نوٹ بکس چلانے سے پہلے ماڈلز لوڈ کریں:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **سروس کو چلتا رہنے دیں:**
   - سروس کو غیر ضروری طور پر بند/شروع نہ کریں
   - سیشنز کے درمیان پس منظر میں چلنے دیں

5. **وسائل کی نگرانی کریں:**
   - نوٹ بک چلانے سے پہلے GPU میموری چیک کریں
   - غیر ضروری GPU ایپلیکیشنز بند کریں
   - ٹاسک مینیجر / nvidia-smi استعمال کریں

6. **باقاعدگی سے اپ ڈیٹ کریں:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**آخری اپ ڈیٹ:** 8 اکتوبر، 2025

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔