# دفاتر ورشة العمل - دليل استكشاف الأخطاء وإصلاحها

## جدول المحتويات

- [المشاكل الشائعة والحلول](../../../../Workshop/notebooks)
- [مشاكل محددة في الجلسة 04](../../../../Workshop/notebooks)
- [مشاكل محددة في الجلسة 05](../../../../Workshop/notebooks)
- [مشاكل محددة في الجلسة 06](../../../../Workshop/notebooks)
- [مشاكل متعلقة بالأجهزة](../../../../Workshop/notebooks)
- [أوامر التشخيص](../../../../Workshop/notebooks)
- [الحصول على المساعدة](../../../../Workshop/notebooks)

---

## المشاكل الشائعة والحلول

### 🔴 نفاد ذاكرة CUDA

**رسالة الخطأ:**
```
CUDA failure 2: out of memory
```

**السبب الجذري:** لا تحتوي وحدة معالجة الرسومات (GPU) على ذاكرة كافية لتحميل النموذج.

**الحلول:**

#### الخيار 1: استخدام إصدارات CPU (موصى به)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### الخيار 2: استخدام نماذج أصغر على GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### الخيار 3: مسح ذاكرة GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### الخيار 4: زيادة ذاكرة GPU (إذا كان ذلك ممكنًا)
- إغلاق علامات التبويب في المتصفح، برامج تحرير الفيديو، أو التطبيقات الأخرى التي تستخدم GPU
- تقليل تأثيرات العرض في Windows
- استخدام وحدة معالجة رسومات مخصصة إذا كنت تمتلك واحدة مدمجة وأخرى مخصصة

---

### 🔴 APIConnectionError: خطأ في الاتصال

**رسالة الخطأ:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**السبب الجذري:** خدمة Foundry Local غير قيد التشغيل أو غير متاحة.

**الحلول:**

#### الخطوة 1: التحقق من حالة الخدمة
```bash
foundry service status
```

#### الخطوة 2: تشغيل الخدمة إذا كانت متوقفة
```bash
foundry service start
```

#### الخطوة 3: التحقق من نقطة النهاية
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### الخطوة 4: تحميل النماذج المطلوبة
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### الخطوة 5: إعادة تشغيل نواة الدفتر
بعد تشغيل الخدمة وتحميل النماذج، أعد تشغيل نواة الدفتر وأعد تشغيل جميع الخلايا.

---

### 🔴 النموذج غير موجود في الكتالوج

**رسالة الخطأ:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**السبب الجذري:** لم يتم تنزيل النموذج أو تحميله في Foundry Local.

**الحلول:**

#### الخيار 1: تنزيل وتحميل النماذج
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

#### الخيار 2: استخدام وضع التحديد التلقائي
قم بتحديث CATALOG لاستخدام أسماء النماذج الأساسية (بدون اللاحقة `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

سيقوم Foundry Local SDK تلقائيًا باختيار أفضل إصدار (CPU، GPU، أو NPU) لجهازك.

---

### 🔴 HttpResponseError: 500 - فشل تحميل النموذج

**رسالة الخطأ:**
```
HttpResponseError: 500 - Failed loading model
```

**السبب الجذري:** ملف النموذج تالف أو غير متوافق مع الجهاز.

**الحلول:**

#### إعادة تنزيل النموذج
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### استخدام إصدار مختلف
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: لم يتم العثور على الوحدة

**رسالة الخطأ:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**السبب الجذري:** حزمة foundry-local-sdk غير مثبتة.

**الحلول:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � الطلب الأول بطيء

**الأعراض:** يستغرق الإكمال الأول أكثر من 30 ثانية، بينما الطلبات اللاحقة تكون سريعة.

**السبب الجذري:** هذا سلوك طبيعي - تقوم الخدمة بتحميل النموذج في الذاكرة عند الطلب الأول.

**الحلول:**

#### تحميل النماذج مسبقًا
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### إبقاء الخدمة قيد التشغيل
```bash
# Start service manually and leave it running
foundry service start
```

---

## مشاكل محددة في الجلسة 04

### تكوين منفذ خاطئ

**المشكلة:** الدفتر يتصل بمنفذ خاطئ (55769 مقابل 59959 مقابل 57127)

**الحل:**

1. تحقق من المنفذ الذي يستخدمه Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. قم بتحديث الخلية 10 في الدفتر:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. أعد تشغيل النواة وأعد تشغيل الخلايا 6، 8، 10، 12، 16، 20، 22

---

### اختيار نموذج خاطئ

**المشكلة:** الدفتر يعرض gpt-oss-20b أو qwen2.5-7b بدلاً من qwen2.5-3b

**الحل:**

1. أعد تشغيل نواة الدفتر (لتنظيف حالة المتغيرات القديمة)
2. أعد تشغيل الخلية 10 (تعيين أسماء النماذج)
3. أعد تشغيل الخلية 12 (عرض التكوين)
4. **تحقق:** يجب أن تعرض الخلية 12 `LLM Model: qwen2.5-3b`

---

### فشل خلية التشخيص

**المشكلة:** تعرض الخلية 16 "❌ لم يتم العثور على خدمة Foundry Local!"

**الحل:**

1. تحقق من أن الخدمة قيد التشغيل:
```bash
foundry service status
```

2. اختبر نقطة النهاية يدويًا:
```bash
curl http://localhost:59959/v1/models
```

3. إذا عمل curl ولكن الدفتر لم يعمل:
   - أعد تشغيل نواة الدفتر
   - أعد تشغيل الخلايا بالترتيب: 6، 8، 10، 12، 14، 16

4. إذا فشل curl:
   - قم بتشغيل الخدمة: `foundry service start`
   - قم بتحميل النماذج: `foundry model run phi-4-mini` و `foundry model run qwen2.5-3b`

---

### فشل التحقق المسبق

**المشكلة:** تعرض الخلية 20 أخطاء اتصال على الرغم من نجاح التشخيص

**الحل:**

1. تحقق من تحميل النماذج:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. إذا كانت النماذج مفقودة:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. أعد تشغيل الخلية 20 بعد تحميل النماذج

---

### فشل المقارنة مع قيم None

**المشكلة:** تكمل الخلية 22 ولكن تعرض زمن الاستجابة كـ None

**الحل:**

1. تحقق من نجاح التحقق المسبق أولاً (الخلية 20)
2. أعد تشغيل الخلية 22 - قد تحتاج النماذج إلى الإحماء عند الطلب الأول
3. تحقق من تحميل كلا النموذجين: `foundry model ls`

---

## مشاكل محددة في الجلسة 05

### الوكيل يستخدم نموذجًا خاطئًا

**المشكلة:** الوكيل لا يستخدم النموذج المتوقع

**الحل:**

تحقق من التكوين:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

أعد تشغيل النواة إذا كانت النماذج غير صحيحة.

---

### تجاوز ذاكرة السياق

**المشكلة:** تدهور استجابات الوكيل مع مرور الوقت

**الحل:** يتم التعامل مع هذه المشكلة تلقائيًا - يحتفظ الوكلاء بآخر 6 رسائل فقط في الذاكرة.

---

## مشاكل محددة في الجلسة 06

### ارتباك بين نماذج CPU و GPU

**المشكلة:** ظهور أخطاء CUDA عند استخدام التكوين الافتراضي

**الحل:** التكوين الافتراضي الآن يستخدم نماذج CPU. إذا رأيت أخطاء CUDA:

1. تحقق من أنك تستخدم كتالوج CPU الافتراضي:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. أعد تشغيل النواة وأعد تشغيل جميع الخلايا

---

### عدم عمل اكتشاف النوايا

**المشكلة:** يتم توجيه المطالبات إلى نماذج خاطئة

**الحل:**

اختبر اكتشاف النوايا:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

قم بتحديث RULES إذا كانت الأنماط بحاجة إلى تعديل.

---

## مشاكل متعلقة بالأجهزة

### وحدة معالجة الرسومات NVIDIA

**تحقق من حالة GPU:**
```bash
nvidia-smi
```

**المشاكل الشائعة:**
- **تعريف قديم:** قم بتحديث تعريفات NVIDIA
- **عدم توافق إصدار CUDA:** أعد تثبيت Foundry Local
- **تجزئة ذاكرة GPU:** أعد تشغيل النظام

### وحدة معالجة الشبكة العصبية Qualcomm NPU

**تحقق من حالة NPU:**
```bash
foundry device info
```

**المشاكل الشائعة:**
- **تعريفات NPU غير مثبتة:** قم بتثبيت تعريفات Qualcomm NPU
- **إصدار NPU غير متوفر:** استخدم إصدار CPU
- **إصدار Windows قديم جدًا:** قم بالتحديث إلى أحدث إصدار من Windows 11

### الأنظمة التي تعتمد فقط على CPU

**النماذج الموصى بها:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**نصائح لتحسين الأداء:**
- استخدم أصغر النماذج
- قلل max_tokens
- كن صبورًا مع الطلب الأول

---

## أوامر التشخيص

### تحقق من كل شيء
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

### في Python
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

## الحصول على المساعدة

### 1. تحقق من السجلات
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. قضايا GitHub
- ابحث عن القضايا الموجودة: https://github.com/microsoft/Foundry-Local/issues
- أنشئ قضية جديدة مع:
  - رسالة الخطأ (النص الكامل)
  - مخرجات `foundry service status`
  - مخرجات `foundry --version`
  - معلومات GPU/NPU (nvidia-smi، إلخ.)
  - خطوات إعادة الإنتاج

### 3. الوثائق
- **المستودع الرئيسي**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **مرجع CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **استكشاف الأخطاء وإصلاحها**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## قائمة التحقق للإصلاحات السريعة

عندما تسوء الأمور، جرب هذه الخطوات بالترتيب:

- [ ] تحقق من أن الخدمة قيد التشغيل: `foundry service status`
- [ ] أعد تشغيل الخدمة: `foundry service stop && foundry service start`
- [ ] تحقق من وجود النموذج: `foundry model ls | grep phi-4-mini`
- [ ] قم بتحميل النماذج المطلوبة: `foundry model run phi-4-mini`
- [ ] تحقق من ذاكرة GPU: `nvidia-smi` (إذا كنت تستخدم NVIDIA)
- [ ] جرب إصدار CPU: استخدم `phi-4-mini-cpu` بدلاً من `phi-4-mini`
- [ ] أعد تشغيل نواة الدفتر
- [ ] امسح مخرجات الدفتر وأعد تشغيل جميع الخلايا
- [ ] أعد تثبيت SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] أعد تشغيل النظام (كملاذ أخير)

---

## نصائح الوقاية

### أفضل الممارسات

1. **تحقق دائمًا من الخدمة أولاً:**
   ```bash
   foundry service status
   ```

2. **استخدم إصدارات CPU بشكل افتراضي:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **قم بتحميل النماذج مسبقًا قبل تشغيل الدفاتر:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **ابقِ الخدمة قيد التشغيل:**
   - لا توقف/تشغل الخدمة دون داعٍ
   - دعها تعمل في الخلفية بين الجلسات

5. **راقب الموارد:**
   - تحقق من ذاكرة GPU قبل التشغيل
   - أغلق التطبيقات غير الضرورية التي تستخدم GPU
   - استخدم مدير المهام / nvidia-smi

6. **قم بالتحديث بانتظام:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**آخر تحديث:** 8 أكتوبر 2025

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.