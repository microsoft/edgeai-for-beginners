# دفترچه‌های کارگاه - راهنمای شروع سریع

## فهرست مطالب

- [پیش‌نیازها](#پیش‌نیازها)
- [تنظیمات اولیه](#codeblock3-یا-به-صورت-جداگانه-نصب-کنید-codeblock4)
- [جلسه ۰۴: مقایسه مدل‌ها](#تأیید-تنظیمات)
- [جلسه ۰۵: هماهنگ‌کننده چندعامله](#چک‌لیست-اعتبارسنجی)
- [جلسه ۰۶: مسیریابی مدل مبتنی بر نیت](#گسترش‌ها)
- [متغیرهای محیطی](#جابجایی-به-مدل‌های-gpu)
- [دستورات رایج](#پیکربندی-جهانی)

---

## پیش‌نیازها

### ۱. نصب Foundry Local

**ویندوز:**
```bash
winget install Microsoft.FoundryLocal
```

**مک‌او‌اس:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**تأیید نصب:**
```bash
foundry --version
```

### ۲. نصب وابستگی‌های پایتون

```bash
cd Workshop
pip install -r requirements.txt
```

یا به صورت جداگانه نصب کنید:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## تنظیمات اولیه

### راه اندازی سرویس Foundry Local

**پیش‌نیاز اجرای هر دفترچه:**

```bash
# شروع سرویس
foundry service start

# اطمینان حاصل کنید که در حال اجرا است
foundry service status
```

خروجی مورد انتظار:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### دانلود و بارگذاری مدل‌ها

دفترچه‌ها به طور پیش‌فرض از این مدل‌ها استفاده می‌کنند:

```bash
# دانلود مدل‌ها (فقط برای بار اول - ممکن است چند دقیقه طول بکشد)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# بارگذاری مدل‌ها در حافظه
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### تأیید تنظیمات

```bash
# مدل‌های بارگذاری شده را فهرست کنید
foundry model ls

# سلامت سرویس را بررسی کنید
curl http://localhost:59959/v1/models
```

---

## جلسه ۰۴: مقایسه مدل‌ها

### هدف
مقایسه عملکرد بین مدل‌های زبان کوچک (SLM) و مدل‌های زبان بزرگ (LLM).

### راه‌اندازی سریع

```bash
# شروع سرویس (اگر قبلاً در حال اجرا نیست)
foundry service start

# بارگذاری مدل‌های مورد نیاز
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### اجرای دفترچه

۱. **بازکردن** `session04_model_compare.ipynb` در VS Code یا Jupyter
۲. **راه‌اندازی مجدد هسته** (Kernel → Restart Kernel)
۳. **اجرای همه سلول‌ها** به ترتیب

### پیکربندی کلیدی

**مدل‌های پیش‌فرض:**
- **SLM:** `phi-4-mini` (~۴ گیگابایت رم، سریع‌تر)
- **LLM:** `qwen2.5-3b` (~۳ گیگابایت رم، بهینه شده برای حافظه)

**متغیرهای محیطی (اختیاری):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### خروجی مورد انتظار

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

### سفارشی‌سازی

**استفاده از مدل‌های متفاوت:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**پرومپت سفارشی:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### چک‌لیست اعتبارسنجی

- [ ] سلول ۱۲ مدل‌های درست را نشان می‌دهد (phi-4-mini، qwen2.5-3b)
- [ ] سلول ۱۲ نقطه انتهایی درست را نشان می‌دهد (پورت ۵۹۹۵۹)
- [ ] سلول ۱۶ تست تشخیصی قبول می‌شود (✅ سرویس در حال اجرا است)
- [ ] سلول ۲۰ تست پیش‌پرواز قبول می‌شود (هر دو مدل درست‌اند)
- [ ] سلول ۲۲ مقایسه با مقادیر تأخیر کامل می‌شود
- [ ] سلول ۲۴ اعتبارسنجی نمایش می‌دهد 🎉 همه چک‌ها موفق بودند!

### زمان برآوردی
- **اولین اجرا:** ۵-۱۰ دقیقه (شامل دانلود مدل‌ها)
- **اجراهای بعدی:** ۱-۲ دقیقه

---

## جلسه ۰۵: هماهنگ‌کننده چندعامله

### هدف
نمایش همکاری چندعامله با استفاده از Foundry Local SDK - عوامل با هم کار می‌کنند تا خروجی‌های بهبود یافته تولید کنند.

### راه‌اندازی سریع

```bash
# شروع سرویس
foundry service start

# بارگذاری مدل‌ها
foundry model run phi-4-mini  # مدل اصلی
foundry model run qwen2.5-7b  # اختیاری: ویرایشگر با کیفیت بالاتر
```

### اجرای دفترچه

۱. **بازکردن** `session05_agents_orchestrator.ipynb`
۲. **راه‌اندازی مجدد هسته**
۳. **اجرای همه سلول‌ها** به ترتیب

### پیکربندی کلیدی

**تنظیمات پیش‌فرض (مدل یکسان برای هر دو عامل):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # از همان مدل استفاده می‌کند
```

**تنظیمات پیشرفته (مدل‌های متفاوت):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # سریع برای پژوهش
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # کیفیت بالا برای ویرایش
```

### معماری

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

### خروجی مورد انتظار

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

### گسترش‌ها

**اضافه کردن عوامل بیشتر:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**آزمایش دسته‌ای:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### زمان برآوردی
- **اولین اجرا:** ۳-۵ دقیقه
- **اجراهای بعدی:** ۱-۲ دقیقه برای هر سوال

---

## جلسه ۰۶: مسیریابی مدل مبتنی بر نیت

### هدف
مسیر دادن هوشمندانه پرامپت‌ها به مدل‌های تخصصی بر اساس نیت شناسایی شده.

### راه‌اندازی سریع

```bash
# راه‌اندازی سرویس
foundry service start

# بارگذاری تمام مدل‌های مسیریابی (نسخه‌های CPU توصیه می‌شود)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**توجه:** جلسه ۰۶ به طور پیش‌فرض از مدل‌های CPU برای بیشترین سازگاری استفاده می‌کند.

### اجرای دفترچه

۱. **بازکردن** `session06_models_router.ipynb`
۲. **راه‌اندازی مجدد هسته**
۳. **اجرای همه سلول‌ها** به ترتیب

### پیکربندی کلیدی

**کتالوگ پیش‌فرض (مدل‌های CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**جایگزین (مدل‌های GPU):**
```python
# اگر VRAM کافی (۸ گیگابایت یا بیشتر) دارید، در سلول شماره ۶ کاتالوگ GPU را فعال کنید
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### تشخیص نیت

مسیریاب از الگوهای regex برای تشخیص نیت استفاده می‌کند:

| نیت | نمونه الگوها | هدایت شده به |
|--------|-----------------|-----------|
| `کد` | "بازنویسی"، "پیاده‌سازی تابع" | phi-3.5-mini-cpu |
| `دسته‌بندی` | "دسته‌بندی"، "این را طبقه‌بندی کن" | qwen2.5-0.5b-cpu |
| `خلاصه` | "خلاصه"، "tl;dr" | phi-4-mini-cpu |
| `عمومی` | بقیه موارد | phi-4-mini-cpu |

### خروجی مورد انتظار

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

### سفارشی‌سازی

**اضافه کردن نیت سفارشی:**
```python
import re

# اضافه کردن به قوانین
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# افزودن قابلیت فهرست‌بندی
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**فعال کردن پیگیری توکن:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### جابجایی به مدل‌های GPU

اگر ۸ گیگابایت یا بیشتر VRAM دارید:

۱. در **سلول شماره ۶**، کاتالوگ CPU را کامنت کنید
۲. کاتالوگ GPU را از کامنت خارج کنید
۳. مدل‌های GPU را بارگذاری کنید:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
۴. هسته را مجددا راه‌اندازی کرده و دفترچه را دوباره اجرا کنید

### زمان برآوردی
- **اولین اجرا:** ۵-۱۰ دقیقه (بارگذاری مدل)
- **اجراهای بعدی:** ۳۰-۶۰ ثانیه برای هر تست

---

## متغیرهای محیطی

### پیکربندی جهانی

قبل از شروع Jupyter/VS Code تنظیم کنید:

**ویندوز (خط فرمان):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**ویندوز (PowerShell):**
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

### پیکربندی درون دفترچه

در ابتدای هر دفترچه تنظیم کنید:

```python
import os

# پیکربندی محلی Foundry
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# انتخاب مدل
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# مدل‌های عامل
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# اشکال‌زدایی
os.environ['SHOW_USAGE'] = '1'       # نمایش استفاده از توکن
os.environ['RETRY_ON_FAIL'] = '1'    # فعال کردن تلاش‌های مجدد
os.environ['RETRY_BACKOFF'] = '2.0'  # تاخیر تلاش مجدد
```

---

## دستورات رایج

### مدیریت سرویس

```bash
# شروع سرویس
foundry service start

# بررسی وضعیت
foundry service status

# توقف سرویس
foundry service stop

# مشاهده‌ی گزارش‌ها
foundry service logs
```

### مدیریت مدل‌ها

```bash
# تمام مدل‌های موجود در کاتالوگ را فهرست کن
foundry model catalog

# مدل‌های بارگذاری شده را فهرست کن
foundry model ls

# یک مدل را دانلود کن
foundry model download phi-4-mini

# یک مدل را بارگذاری کن
foundry model run phi-4-mini

# یک مدل را بارگذاری‌برداری کن
foundry model unload phi-4-mini

# یک مدل را حذف کن
foundry model remove phi-4-mini

# اطلاعات مدل را دریافت کن
foundry model info phi-4-mini
```

### آزمایش نقاط انتهایی

```bash
# بررسی سلامت سرویس
curl http://localhost:59959/health

# فهرست مدل‌های موجود از طریق API
curl http://localhost:59959/v1/models

# آزمایش تکمیل مدل
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### دستورات تشخیصی

```bash
# همه چیز را بررسی کنید
foundry --version
foundry service status
foundry model ls
foundry device info

# وضعیت GPU (انویدیا)
nvidia-smi

# وضعیت NPU (کوالکام)
foundry device info
```

---

## بهترین شیوه‌ها

### قبل از شروع هر دفترچه

۱. **بررسی کنید سرویس در حال اجرا باشد:**
   ```bash
   foundry service status
   ```

۲. **تأیید کنید مدل‌ها بارگذاری شده‌اند:**
   ```bash
   foundry model ls
   ```

۳. **هسته دفترچه را در صورت اجرای مجدد راه‌اندازی کنید**

۴. **همه خروجی‌ها را پاک کنید** برای اجرای پاک

### مدیریت منابع

۱. **به طور پیش‌فرض از مدل‌های CPU استفاده کنید** برای سازگاری
۲. **تنها در صورتی به مدل‌های GPU سوئیچ کنید که ۸ گیگابایت یا بیشتر VRAM دارید**
۳. **قبل از اجرا سایر برنامه‌های GPU را ببندید**
۴. **سرویس را بین جلسات دفترچه روشن نگه دارید**
۵. **مصرف منابع را با Task Manager / nvidia-smi مانیتور کنید**

### عیب‌یابی

۱. **همیشه ابتدا سرویس را بررسی کنید** قبل از دیباگ کد
۲. **هسته را مجدداً راه‌اندازی کنید** اگر پیکربندی قدیمی دیده‌اید
۳. **پس از هر تغییر سلول‌های تشخیصی را دوباره اجرا کنید**
۴. **بررسی کنید نام مدل‌ها با آنچه بارگیری شده مطابقت داشته باشد**
۵. **تأیید کنید پورت نقطه انتهایی با وضعیت سرویس تطابق دارد**

---

## مرجع سریع: نام‌های مستعار مدل‌ها

### مدل‌های رایج

| نام مستعار | اندازه | مناسب برای | رم/وی‌رام | گونه‌ها |
|-------|------|----------|----------|----------|
| `phi-4-mini` | تقریباً ۴ میلیارد | گپ عمومی، خلاصه‌سازی | ۴-۶ گیگابایت | `-cpu`، `-cuda-gpu`، `-npu` |
| `phi-3.5-mini` | تقریباً ۳.۵ میلیارد | تولید کد، بازنویسی | ۳-۵ گیگابایت | `-cpu`، `-cuda-gpu`، `-npu` |
| `qwen2.5-3b` | تقریباً ۳ میلیارد | کارهای عمومی، کارآمد | ۳-۴ گیگابایت | `-cpu`، `-cuda-gpu` |
| `qwen2.5-1.5b` | تقریباً ۱.۵ میلیارد | سریع، کم‌مصرف | ۲-۳ گیگابایت | `-cpu`، `-cuda-gpu` |
| `qwen2.5-0.5b` | تقریباً ۰.۵ میلیارد | دسته‌بندی، کم‌مصرف | ۱-۲ گیگابایت | `-cpu`، `-cuda-gpu` |

### نام‌گذاری گونه‌ها

- **نام پایه** (مثلاً `phi-4-mini`): خودکار بهترین گونه را برای سخت‌افزار شما انتخاب می‌کند
- **`-cpu`**: بهینه شده برای CPU، در همه جا کار می‌کند
- **`-cuda-gpu`**: بهینه شده برای GPU انویدیا، نیاز به ۸ گیگابایت یا بیشتر VRAM دارد
- **`-npu`**: بهینه شده برای Qualcomm NPU، نیاز به درایورهای NPU دارد

**توصیه:** از نام‌های پایه (بدون پسوند) استفاده کنید و اجازه دهید Foundry Local بهترین گونه را خودکار انتخاب کند.

---

## شاخص‌های موفقیت

شما آماده‌اید وقتی که ببینید:

✅ `foundry service status` نمایش می‌دهد "running"
✅ `foundry model ls` مدل‌های مورد نیاز شما را نشان می‌دهد
✅ سرویس در نقطه انتهایی صحیح قابل دسترسی است
✅ بررسی سلامت پاسخ ۲۰۰ OK باز می‌گرداند
✅ سلول‌های تشخیصی دفترچه قبول می‌شوند
✅ هیچ خطای اتصال در خروجی نیست

---

## دریافت کمک

### مستندات
- **مخزن اصلی**: https://github.com/microsoft/Foundry-Local
- **کتابخانه پایتون SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **مرجع CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **عیب‌یابی**: فایل `troubleshooting.md` در همین پوشه را ببینید

### مشکلات GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**آخرین بروزرسانی:** ۸ اکتبر ۲۰۲۵
**نسخه:** دفترچه‌های کارگاه ۲.۰

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->