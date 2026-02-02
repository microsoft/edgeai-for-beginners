# دليل البدء السريع - دفاتر ورشة العمل

## جدول المحتويات

- [المتطلبات الأساسية](../../../../Workshop/notebooks)
- [الإعداد الأولي](../../../../Workshop/notebooks)
- [الجلسة 04: مقارنة النماذج](../../../../Workshop/notebooks)
- [الجلسة 05: منسق الوكلاء المتعددين](../../../../Workshop/notebooks)
- [الجلسة 06: توجيه النماذج بناءً على النوايا](../../../../Workshop/notebooks)
- [متغيرات البيئة](../../../../Workshop/notebooks)
- [الأوامر الشائعة](../../../../Workshop/notebooks)

---

## المتطلبات الأساسية

### 1. تثبيت Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**التحقق من التثبيت:**
```bash
foundry --version
```

### 2. تثبيت تبعيات Python

```bash
cd Workshop
pip install -r requirements.txt
```

أو تثبيتها بشكل فردي:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## الإعداد الأولي

### بدء خدمة Foundry Local

**مطلوب قبل تشغيل أي دفتر:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

المخرجات المتوقعة:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### تنزيل وتحميل النماذج

تستخدم الدفاتر هذه النماذج بشكل افتراضي:

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

### التحقق من الإعداد

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## الجلسة 04: مقارنة النماذج

### الهدف
مقارنة الأداء بين نماذج اللغة الصغيرة (SLM) ونماذج اللغة الكبيرة (LLM).

### الإعداد السريع

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### تشغيل الدفتر

1. **افتح** `session04_model_compare.ipynb` في VS Code أو Jupyter  
2. **أعد تشغيل النواة** (Kernel → Restart Kernel)  
3. **شغل جميع الخلايا** بالترتيب  

### التكوين الرئيسي

**النماذج الافتراضية:**
- **SLM:** `phi-4-mini` (~4GB RAM، أسرع)
- **LLM:** `qwen2.5-3b` (~3GB RAM، محسّن للذاكرة)

**متغيرات البيئة (اختياري):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### المخرجات المتوقعة

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

### التخصيص

**استخدام نماذج مختلفة:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**موجه مخصص:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### قائمة التحقق من التحقق

- [ ] تعرض الخلية 12 النماذج الصحيحة (phi-4-mini، qwen2.5-3b)  
- [ ] تعرض الخلية 12 نقطة النهاية الصحيحة (المنفذ 59959)  
- [ ] تمر الخلية 16 التشخيص (✅ الخدمة تعمل)  
- [ ] تمر الخلية 20 فحص ما قبل التشغيل (كلا النموذجين جيدان)  
- [ ] تنتهي الخلية 22 بالمقارنة مع قيم زمن الاستجابة  
- [ ] تعرض الخلية 24 التحقق 🎉 جميع الفحوصات ناجحة!  

### تقدير الوقت
- **التشغيل الأول:** 5-10 دقائق (بما في ذلك تنزيل النماذج)  
- **التشغيلات اللاحقة:** 1-2 دقيقة  

---

## الجلسة 05: منسق الوكلاء المتعددين

### الهدف
عرض التعاون بين الوكلاء باستخدام Foundry Local SDK - يعمل الوكلاء معًا لإنتاج مخرجات محسّنة.

### الإعداد السريع

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### تشغيل الدفتر

1. **افتح** `session05_agents_orchestrator.ipynb`  
2. **أعد تشغيل النواة**  
3. **شغل جميع الخلايا** بالترتيب  

### التكوين الرئيسي

**الإعداد الافتراضي (نفس النموذج لكلا الوكيلين):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**الإعداد المتقدم (نماذج مختلفة):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### الهيكلية

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

### المخرجات المتوقعة

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

### التوسعات

**إضافة المزيد من الوكلاء:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**اختبار الدفعات:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### تقدير الوقت
- **التشغيل الأول:** 3-5 دقائق  
- **التشغيلات اللاحقة:** 1-2 دقيقة لكل سؤال  

---

## الجلسة 06: توجيه النماذج بناءً على النوايا

### الهدف
توجيه الموجهات بذكاء إلى النماذج المتخصصة بناءً على النوايا المكتشفة.

### الإعداد السريع

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**ملاحظة:** تستخدم الجلسة 06 نماذج CPU افتراضيًا لتحقيق أقصى قدر من التوافق.

### تشغيل الدفتر

1. **افتح** `session06_models_router.ipynb`  
2. **أعد تشغيل النواة**  
3. **شغل جميع الخلايا** بالترتيب  

### التكوين الرئيسي

**الكتالوج الافتراضي (نماذج CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**البديل (نماذج GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### اكتشاف النوايا

يستخدم الموجه أنماط regex لاكتشاف النوايا:

| النية | أمثلة على الأنماط | يتم توجيهها إلى |
|-------|-------------------|-----------------|
| `code` | "refactor"، "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize"، "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize"، "tl;dr" | phi-4-mini-cpu |
| `general` | كل شيء آخر | phi-4-mini-cpu |

### المخرجات المتوقعة

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

### التخصيص

**إضافة نية مخصصة:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**تمكين تتبع الرموز:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### التبديل إلى نماذج GPU

إذا كان لديك ذاكرة VRAM بسعة 8GB+:

1. في **الخلية #6**، قم بتعليق كتالوج CPU  
2. قم بإلغاء تعليق كتالوج GPU  
3. تحميل نماذج GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. أعد تشغيل النواة وأعد تشغيل الدفتر  

### تقدير الوقت
- **التشغيل الأول:** 5-10 دقائق (تحميل النماذج)  
- **التشغيلات اللاحقة:** 30-60 ثانية لكل اختبار  

---

## متغيرات البيئة

### التكوين العالمي

قم بتعيينه قبل بدء Jupyter/VS Code:

**Windows (Command Prompt):**
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

### التكوين داخل الدفتر

قم بتعيينه في بداية أي دفتر:

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

## الأوامر الشائعة

### إدارة الخدمة

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

### إدارة النماذج

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

### اختبار نقاط النهاية

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

### أوامر التشخيص

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

## أفضل الممارسات

### قبل بدء أي دفتر

1. **تحقق من تشغيل الخدمة:**
   ```bash
   foundry service status
   ```

2. **تحقق من تحميل النماذج:**
   ```bash
   foundry model ls
   ```

3. **أعد تشغيل نواة الدفتر** إذا كنت تعيد التشغيل  

4. **امسح جميع المخرجات** للحصول على تشغيل نظيف  

### إدارة الموارد

1. **استخدم نماذج CPU افتراضيًا** لتحقيق التوافق  
2. **قم بالتبديل إلى نماذج GPU** فقط إذا كان لديك ذاكرة VRAM بسعة 8GB+  
3. **أغلق التطبيقات الأخرى التي تستخدم GPU** قبل التشغيل  
4. **احتفظ بالخدمة قيد التشغيل** بين جلسات الدفتر  
5. **راقب استخدام الموارد** باستخدام Task Manager / nvidia-smi  

### استكشاف الأخطاء وإصلاحها

1. **تحقق دائمًا من الخدمة أولاً** قبل تصحيح الأخطاء في الكود  
2. **أعد تشغيل النواة** إذا رأيت تكوينًا قديمًا  
3. **أعد تشغيل خلايا التشخيص** بعد أي تغييرات  
4. **تحقق من أسماء النماذج** لتتطابق مع ما تم تحميله  
5. **تحقق من منفذ نقطة النهاية** لتتطابق مع حالة الخدمة  

---

## المرجع السريع: أسماء النماذج

### النماذج الشائعة

| الاسم المستعار | الحجم | الأفضل لـ | RAM/VRAM | المتغيرات |
|----------------|-------|-----------|----------|-----------|
| `phi-4-mini` | ~4B | الدردشة العامة، التلخيص | 4-6GB | `-cpu`، `-cuda-gpu`، `-npu` |
| `phi-3.5-mini` | ~3.5B | إنشاء الأكواد، إعادة الهيكلة | 3-5GB | `-cpu`، `-cuda-gpu`، `-npu` |
| `qwen2.5-3b` | ~3B | المهام العامة، الكفاءة | 3-4GB | `-cpu`، `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | سريع، موارد منخفضة | 2-3GB | `-cpu`، `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | التصنيف، موارد قليلة جدًا | 1-2GB | `-cpu`، `-cuda-gpu` |

### تسمية المتغيرات

- **الاسم الأساسي** (مثل `phi-4-mini`): يختار تلقائيًا أفضل متغير لجهازك  
- **`-cpu`**: محسّن لـ CPU، يعمل في كل مكان  
- **`-cuda-gpu`**: محسّن لـ NVIDIA GPU، يتطلب ذاكرة VRAM بسعة 8GB+  
- **`-npu`**: محسّن لـ Qualcomm NPU، يتطلب برامج تشغيل NPU  

**التوصية:** استخدم الأسماء الأساسية (بدون لاحقة) ودع Foundry Local يختار أفضل متغير تلقائيًا.

---

## مؤشرات النجاح

أنت جاهز عندما ترى:

✅ `foundry service status` يظهر "running"  
✅ `foundry model ls` يظهر النماذج المطلوبة  
✅ الخدمة متاحة عند نقطة النهاية الصحيحة  
✅ فحص الصحة يعيد 200 OK  
✅ خلايا التشخيص في الدفتر تمر  
✅ لا توجد أخطاء اتصال في المخرجات  

---

## الحصول على المساعدة

### الوثائق
- **المستودع الرئيسي**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **مرجع CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **استكشاف الأخطاء وإصلاحها**: راجع `troubleshooting.md` في هذا الدليل  

### مشاكل GitHub
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**آخر تحديث:** 8 أكتوبر 2025  
**الإصدار:** دفاتر ورشة العمل 2.0  

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.