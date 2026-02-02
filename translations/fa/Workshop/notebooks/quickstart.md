# راهنمای سریع برای دفترچه‌های کارگاه

## فهرست مطالب

- [پیش‌نیازها](../../../../Workshop/notebooks)
- [تنظیمات اولیه](../../../../Workshop/notebooks)
- [جلسه ۰۴: مقایسه مدل‌ها](../../../../Workshop/notebooks)
- [جلسه ۰۵: هماهنگ‌کننده چند عاملی](../../../../Workshop/notebooks)
- [جلسه ۰۶: مسیریابی مدل مبتنی بر نیت](../../../../Workshop/notebooks)
- [متغیرهای محیطی](../../../../Workshop/notebooks)
- [دستورات عمومی](../../../../Workshop/notebooks)

---

## پیش‌نیازها

### ۱. نصب Foundry Local

**ویندوز:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
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

### راه‌اندازی سرویس Foundry Local

**ضروری قبل از اجرای هر دفترچه:**

```bash
# Start the service
foundry service start

# Verify it's running
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


### تأیید تنظیمات

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```


---

## جلسه ۰۴: مقایسه مدل‌ها

### هدف
مقایسه عملکرد بین مدل‌های زبان کوچک (SLM) و مدل‌های زبان بزرگ (LLM).

### تنظیم سریع

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```


### اجرای دفترچه

1. **باز کردن** `session04_model_compare.ipynb` در VS Code یا Jupyter  
2. **راه‌اندازی مجدد کرنل** (Kernel → Restart Kernel)  
3. **اجرای تمام سلول‌ها** به ترتیب  

### تنظیمات کلیدی

**مدل‌های پیش‌فرض:**
- **SLM:** `phi-4-mini` (~۴ گیگابایت رم، سریع‌تر)
- **LLM:** `qwen2.5-3b` (~۳ گیگابایت رم، بهینه‌شده برای حافظه)

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

**استفاده از مدل‌های مختلف:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**پیشنهاد سفارشی:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```


### چک‌لیست اعتبارسنجی

- [ ] سلول ۱۲ مدل‌های صحیح را نشان می‌دهد (phi-4-mini, qwen2.5-3b)  
- [ ] سلول ۱۲ نقطه پایانی صحیح را نشان می‌دهد (پورت ۵۹۹۵۹)  
- [ ] سلول ۱۶ تشخیص موفقیت‌آمیز را نشان می‌دهد (✅ سرویس در حال اجرا است)  
- [ ] سلول ۲۰ بررسی اولیه موفقیت‌آمیز است (هر دو مدل درست هستند)  
- [ ] سلول ۲۲ مقایسه را با مقادیر تأخیر کامل می‌کند  
- [ ] سلول ۲۴ اعتبارسنجی نشان می‌دهد 🎉 همه بررسی‌ها موفقیت‌آمیز بودند!  

### تخمین زمان
- **اولین اجرا:** ۵-۱۰ دقیقه (شامل دانلود مدل‌ها)  
- **اجراهای بعدی:** ۱-۲ دقیقه  

---

## جلسه ۰۵: هماهنگ‌کننده چند عاملی

### هدف
نمایش همکاری چند عامل با استفاده از Foundry Local SDK - عوامل با هم کار می‌کنند تا خروجی‌های بهینه تولید کنند.

### تنظیم سریع

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```


### اجرای دفترچه

1. **باز کردن** `session05_agents_orchestrator.ipynb`  
2. **راه‌اندازی مجدد کرنل**  
3. **اجرای تمام سلول‌ها** به ترتیب  

### تنظیمات کلیدی

**تنظیمات پیش‌فرض (همان مدل برای هر دو عامل):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**تنظیمات پیشرفته (مدل‌های مختلف):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
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

**افزودن عوامل بیشتر:**
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


### تخمین زمان
- **اولین اجرا:** ۳-۵ دقیقه  
- **اجراهای بعدی:** ۱-۲ دقیقه برای هر سوال  

---

## جلسه ۰۶: مسیریابی مدل مبتنی بر نیت

### هدف
مسیریابی هوشمند پیشنهادها به مدل‌های تخصصی بر اساس نیت شناسایی‌شده.

### تنظیم سریع

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**توجه:** جلسه ۰۶ به طور پیش‌فرض از مدل‌های CPU برای حداکثر سازگاری استفاده می‌کند.

### اجرای دفترچه

1. **باز کردن** `session06_models_router.ipynb`  
2. **راه‌اندازی مجدد کرنل**  
3. **اجرای تمام سلول‌ها** به ترتیب  

### تنظیمات کلیدی

**کاتالوگ پیش‌فرض (مدل‌های CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**جایگزین (مدل‌های GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```


### شناسایی نیت

روتر از الگوهای regex برای شناسایی نیت استفاده می‌کند:

| نیت | مثال‌های الگو | مسیریابی به |
|-----|---------------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | سایر موارد | phi-4-mini-cpu |

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

**افزودن نیت سفارشی:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**فعال‌سازی ردیابی توکن:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```


### تغییر به مدل‌های GPU

اگر ۸ گیگابایت یا بیشتر VRAM دارید:

1. در **سلول #۶**، کاتالوگ CPU را کامنت کنید  
2. کاتالوگ GPU را از حالت کامنت خارج کنید  
3. مدل‌های GPU را بارگذاری کنید:  
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. کرنل را مجدداً راه‌اندازی کرده و دفترچه را دوباره اجرا کنید  

### تخمین زمان
- **اولین اجرا:** ۵-۱۰ دقیقه (بارگذاری مدل)  
- **اجراهای بعدی:** ۳۰-۶۰ ثانیه برای هر آزمایش  

---

## متغیرهای محیطی

### تنظیمات کلی

قبل از شروع Jupyter/VS Code تنظیم کنید:

**ویندوز (Command Prompt):**
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


### تنظیمات درون دفترچه

در ابتدای هر دفترچه تنظیم کنید:

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

## دستورات عمومی

### مدیریت سرویس

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


### مدیریت مدل

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


### آزمایش نقاط پایانی

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


### دستورات تشخیصی

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

## بهترین شیوه‌ها

### قبل از شروع هر دفترچه

1. **بررسی کنید که سرویس در حال اجرا است:**
   ```bash
   foundry service status
   ```

2. **تأیید کنید که مدل‌ها بارگذاری شده‌اند:**
   ```bash
   foundry model ls
   ```

3. **کرنل دفترچه را مجدداً راه‌اندازی کنید** اگر دوباره اجرا می‌کنید  

4. **تمام خروجی‌ها را پاک کنید** برای یک اجرای تمیز  

### مدیریت منابع

1. **به طور پیش‌فرض از مدل‌های CPU استفاده کنید** برای سازگاری  
2. **فقط در صورت داشتن ۸ گیگابایت یا بیشتر VRAM به مدل‌های GPU تغییر دهید**  
3. **برنامه‌های دیگر GPU را قبل از اجرا ببندید**  
4. **سرویس را بین جلسات دفترچه در حال اجرا نگه دارید**  
5. **مصرف منابع را با Task Manager / nvidia-smi نظارت کنید**  

### عیب‌یابی

1. **همیشه ابتدا سرویس را بررسی کنید** قبل از اشکال‌زدایی کد  
2. **کرنل را مجدداً راه‌اندازی کنید** اگر تنظیمات قدیمی مشاهده کردید  
3. **سلول‌های تشخیصی را دوباره اجرا کنید** پس از هر تغییری  
4. **بررسی کنید که نام مدل‌ها** با مدل‌های بارگذاری‌شده مطابقت داشته باشد  
5. **تأیید کنید که پورت نقطه پایانی** با وضعیت سرویس مطابقت دارد  

---

## مرجع سریع: نام‌های مستعار مدل

### مدل‌های رایج

| نام مستعار | اندازه | بهترین کاربرد | RAM/VRAM | انواع |
|------------|--------|---------------|----------|-------|
| `phi-4-mini` | ~۴B | چت عمومی، خلاصه‌سازی | ۴-۶GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~۳.۵B | تولید کد، بازنویسی | ۳-۵GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~۳B | وظایف عمومی، کارآمد | ۳-۴GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~۱.۵B | سریع، منابع کم | ۲-۳GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~۰.۵B | طبقه‌بندی، منابع کم | ۱-۲GB | `-cpu`, `-cuda-gpu` |

### نام‌گذاری انواع

- **نام پایه** (مثلاً، `phi-4-mini`): به طور خودکار بهترین نوع برای سخت‌افزار شما را انتخاب می‌کند  
- **`-cpu`**: بهینه‌شده برای CPU، قابل اجرا در همه جا  
- **`-cuda-gpu`**: بهینه‌شده برای GPUهای NVIDIA، نیازمند ۸GB+ VRAM  
- **`-npu`**: بهینه‌شده برای NPUهای Qualcomm، نیازمند درایورهای NPU  

**توصیه:** از نام‌های پایه (بدون پسوند) استفاده کنید و اجازه دهید Foundry Local بهترین نوع را به طور خودکار انتخاب کند.

---

## شاخص‌های موفقیت

شما آماده هستید وقتی که:

✅ `foundry service status` نشان‌دهنده "در حال اجرا" باشد  
✅ `foundry model ls` مدل‌های مورد نیاز شما را نشان دهد  
✅ سرویس در نقطه پایانی صحیح قابل دسترسی باشد  
✅ بررسی سلامت 200 OK بازگرداند  
✅ سلول‌های تشخیصی دفترچه موفقیت‌آمیز باشند  
✅ هیچ خطای ارتباطی در خروجی وجود نداشته باشد  

---

## دریافت کمک

### مستندات
- **مخزن اصلی:** https://github.com/microsoft/Foundry-Local  
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **مرجع CLI:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **عیب‌یابی:** فایل `troubleshooting.md` در این دایرکتوری را ببینید  

### مشکلات GitHub
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**آخرین به‌روزرسانی:** ۸ اکتبر ۲۰۲۵  
**نسخه:** دفترچه‌های کارگاه ۲.۰  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.