<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T20:24:09+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "fa"
}
-->
# جلسه ۱: شروع کار با Foundry Local

## چکیده

سفر خود را با Foundry Local آغاز کنید و آن را روی ویندوز ۱۱ نصب و پیکربندی کنید. یاد بگیرید چگونه CLI را تنظیم کنید، شتاب سخت‌افزاری را فعال کنید و مدل‌ها را برای استنتاج سریع محلی کش کنید. این جلسه عملی شامل اجرای مدل‌هایی مانند Phi، Qwen، DeepSeek و GPT-OSS-20B با استفاده از دستورات CLI قابل بازتولید است.

## اهداف یادگیری

در پایان این جلسه، شما قادر خواهید بود:

- **نصب و پیکربندی**: Foundry Local را روی ویندوز ۱۱ با تنظیمات بهینه نصب کنید.
- **تسلط بر عملیات CLI**: از CLI Foundry Local برای مدیریت و استقرار مدل‌ها استفاده کنید.
- **فعال‌سازی شتاب سخت‌افزاری**: شتاب GPU را با ONNXRuntime یا WebGPU پیکربندی کنید.
- **استقرار چندین مدل**: مدل‌های phi-4، GPT-OSS-20B، Qwen و DeepSeek را به صورت محلی اجرا کنید.
- **ساخت اولین برنامه خود**: نمونه‌های موجود را برای استفاده از Foundry Local Python SDK تطبیق دهید.

# تست مدل (پاسخ غیرتعاملی به یک درخواست)
foundry model run phi-4-mini --prompt "سلام، خودت را معرفی کن"

- ویندوز ۱۱ (نسخه 22H2 یا بالاتر)
# لیست مدل‌های موجود در کاتالوگ (مدل‌های بارگذاری‌شده پس از اجرا ظاهر می‌شوند)
foundry model list  
## توجه: در حال حاضر هیچ فلگ اختصاصی `--running` وجود ندارد؛ برای دیدن مدل‌های بارگذاری‌شده، یک چت را شروع کنید یا لاگ‌های سرویس را بررسی کنید.
- نصب پایتون 3.10+  
- Visual Studio Code با افزونه پایتون  
- دسترسی ادمین برای نصب  

### (اختیاری) متغیرهای محیطی

یک فایل `.env` ایجاد کنید (یا در شل تنظیم کنید) تا اسکریپت‌ها قابل حمل شوند:
# مقایسه پاسخ‌ها (غیرتعاملی)
foundry model run gpt-oss-20b --prompt "هوش مصنوعی لبه‌ای را به زبان ساده توضیح بده"
| متغیر | هدف | مثال |
|-------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | نام مستعار مدل ترجیحی (کاتالوگ بهترین نسخه را به طور خودکار انتخاب می‌کند) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | جایگزینی نقطه پایانی (در غیر این صورت به طور خودکار از مدیر گرفته می‌شود) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | فعال‌سازی دمو استریمینگ | `true` |

> اگر `FOUNDRY_LOCAL_ENDPOINT=auto` (یا تنظیم نشده باشد)، از مدیر SDK استخراج می‌شود.

## جریان دمو (۳۰ دقیقه)

### ۱. نصب Foundry Local و تأیید تنظیمات CLI (۱۰ دقیقه)

# لیست مدل‌های کش‌شده
foundry cache list  

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```
  
**macOS (پیش‌نمایش / در صورت پشتیبانی)**  

اگر بسته بومی macOS ارائه شده است (برای آخرین اطلاعات به مستندات رسمی مراجعه کنید):  

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```
  
اگر باینری‌های بومی macOS هنوز در دسترس نیستند، همچنان می‌توانید:  
1. از یک ماشین مجازی ویندوز ۱۱ ARM/Intel (Parallels / UTM) استفاده کنید و مراحل ویندوز را دنبال کنید.  
2. مدل‌ها را از طریق کانتینر اجرا کنید (در صورت انتشار تصویر کانتینر) و `FOUNDRY_LOCAL_ENDPOINT` را به پورت باز شده تنظیم کنید.  

**ایجاد محیط مجازی پایتون (چند پلتفرمی)**  

Windows PowerShell:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```
  
macOS / Linux:  
```bash
python3 -m venv .venv
source .venv/bin/activate
```
  
ارتقاء pip و نصب وابستگی‌های اصلی:  
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
#### مرحله ۱.۲: تأیید نصب  

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```
  
#### مرحله ۱.۳: پیکربندی محیط  

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```
  
### بوت‌استرپینگ SDK (توصیه‌شده)  

به جای راه‌اندازی دستی سرویس و اجرای مدل‌ها، **Foundry Local Python SDK** می‌تواند همه چیز را بوت‌استرپ کند:  

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```
  
اگر کنترل صریح را ترجیح می‌دهید، همچنان می‌توانید از CLI + کلاینت OpenAI همان‌طور که در ادامه نشان داده شده استفاده کنید.  

### ۲. اجرای مدل‌ها به صورت محلی از طریق CLI (۱۰ دقیقه)  

#### مرحله ۳.۱: استقرار مدل Phi-4  

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```
  
#### مرحله ۳.۲: استقرار GPT-OSS-20B  

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```
  
#### مرحله ۳.۳: بارگذاری مدل‌های اضافی  

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```
  
### ۴. پروژه شروع‌کننده: تطبیق 01-run-phi برای Foundry Local (۵ دقیقه)  

#### مرحله ۴.۱: ایجاد برنامه چت پایه  

ایجاد `samples/01-foundry-quickstart/chat_quickstart.py` (به‌روزرسانی‌شده برای استفاده از مدیر در صورت موجود بودن):  

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```
  
#### مرحله ۴.۲: تست برنامه  

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```
  
## مفاهیم کلیدی پوشش داده‌شده  

### ۱. معماری Foundry Local  

- **موتور استنتاج محلی**: اجرای مدل‌ها به طور کامل روی دستگاه شما  
- **سازگاری با OpenAI SDK**: یکپارچگی بدون درز با کد موجود OpenAI  
- **مدیریت مدل**: دانلود، کش و اجرای چندین مدل به صورت کارآمد  
- **بهینه‌سازی سخت‌افزار**: استفاده از شتاب GPU، NPU و CPU  

### ۲. مرجع دستورات CLI  

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```
  
### ۳. یکپارچه‌سازی Python SDK  

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```
  
## رفع مشکلات رایج  

### مشکل ۱: "دستور Foundry پیدا نشد"  

**راه‌حل:**  
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```
  
### مشکل ۲: "مدل بارگذاری نشد"  

**راه‌حل:**  
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```
  
### مشکل ۳: "اتصال به localhost:5273 رد شد"  

**راه‌حل:**  
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```
  
## نکات بهینه‌سازی عملکرد  

### ۱. استراتژی انتخاب مدل  

- **Phi-4-mini**: بهترین برای وظایف عمومی، مصرف حافظه کمتر  
- **Qwen2.5-0.5b**: سریع‌ترین استنتاج، منابع حداقلی  
- **GPT-OSS-20B**: بالاترین کیفیت، نیازمند منابع بیشتر  
- **DeepSeek-Coder**: بهینه‌شده برای وظایف برنامه‌نویسی  

### ۲. بهینه‌سازی سخت‌افزار  

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```
  
### ۳. نظارت بر عملکرد  

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```
  
### بهبودهای اختیاری  

| بهبود | چیست | چگونه |
|-------|------|-------|
| ابزارهای مشترک | حذف منطق تکراری کلاینت/بوت‌استرپ | استفاده از `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| نمایش استفاده از توکن | آموزش تفکر هزینه/کارایی در مراحل اولیه | تنظیم `SHOW_USAGE=1` برای نمایش توکن‌های درخواست/پاسخ/کل |
| مقایسه‌های قطعی | معیارگذاری پایدار و بررسی رگرسیون | استفاده از `temperature=0`، `top_p=1`، متن درخواست ثابت |
| تأخیر اولین توکن | معیار پاسخگویی درک‌شده | تطبیق اسکریپت معیار با استریمینگ (`BENCH_STREAM=1`) |
| تلاش مجدد در خطاهای موقت | دموهای مقاوم در شروع سرد | `RETRY_ON_FAIL=1` (پیش‌فرض) و تنظیم `RETRY_BACKOFF` |
| تست دود | بررسی سریع جریان‌های کلیدی | اجرای `python Workshop/tests/smoke.py` قبل از کارگاه |
| پروفایل‌های نام مستعار مدل | تغییر سریع مجموعه مدل بین ماشین‌ها | نگهداری `.env` با `FOUNDRY_LOCAL_ALIAS`، `SLM_ALIAS`، `LLM_ALIAS` |
| کارایی کش | جلوگیری از گرم‌کردن‌های مکرر در اجرای چند نمونه | استفاده از مدیران کش؛ استفاده مجدد در اسکریپت‌ها/دفترچه‌ها |
| گرم‌کردن اولیه | کاهش نوسانات تأخیر p95 | ارسال یک درخواست کوچک پس از ایجاد `FoundryLocalManager` |

مثال پایه گرم قطعی (PowerShell):  

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```
  
باید خروجی مشابهی ببینید و تعداد توکن‌های یکسانی در اجرای دوم تأیید شود که قطعی بودن را نشان می‌دهد.  

## گام‌های بعدی  

پس از اتمام این جلسه:  

1. **بررسی جلسه ۲**: ساخت راه‌حل‌های هوش مصنوعی با Azure AI Foundry RAG  
2. **آزمایش مدل‌های مختلف**: آزمایش با Qwen، DeepSeek و دیگر خانواده‌های مدل  
3. **بهینه‌سازی عملکرد**: تنظیم دقیق تنظیمات برای سخت‌افزار خاص خود  
4. **ساخت برنامه‌های سفارشی**: استفاده از Foundry Local SDK در پروژه‌های خود  

## منابع اضافی  

### مستندات  
- [مرجع Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)  
- [راهنمای نصب Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)  
- [کاتالوگ مدل](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)  

### کد نمونه  
- [نمونه Module08 شماره 01](./samples/01/README.md) - شروع سریع چت REST  
- [نمونه Module08 شماره 02](./samples/02/README.md) - یکپارچه‌سازی OpenAI SDK  
- [نمونه Module08 شماره 03](./samples/03/README.md) - کشف مدل و معیارگذاری  

### جامعه  
- [بحث‌های GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)  
- [جامعه هوش مصنوعی Azure](https://techcommunity.microsoft.com/category/artificialintelligence)  

---

**مدت زمان جلسه**: ۳۰ دقیقه عملی + ۱۵ دقیقه پرسش و پاسخ  
**سطح دشواری**: مبتدی  
**پیش‌نیازها**: ویندوز ۱۱، پایتون 3.10+، دسترسی ادمین  

## سناریوی نمونه و نقشه‌برداری کارگاه  

| اسکریپت / دفترچه کارگاه | سناریو | هدف | ورودی‌های نمونه | داده‌های مورد نیاز |
|-------------------------|--------|------|-----------------|-------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | تیم فناوری اطلاعات داخلی که ارزیابی استنتاج روی دستگاه را برای یک پورتال ارزیابی حریم خصوصی انجام می‌دهد | اثبات اینکه SLM محلی در پاسخ به درخواست‌های استاندارد در کمتر از یک ثانیه پاسخ می‌دهد | "دو مزیت استنتاج محلی را فهرست کنید." | هیچ (فقط یک درخواست) |
| کد تطبیق سریع شروع | توسعه‌دهنده‌ای که یک اسکریپت OpenAI موجود را به Foundry Local منتقل می‌کند | نشان دادن سازگاری سریع | "دو مزیت استنتاج محلی را بگویید." | فقط درخواست داخلی |

### روایت سناریو  
تیم امنیت و انطباق باید تأیید کند که آیا داده‌های حساس نمونه می‌توانند به صورت محلی پردازش شوند. آن‌ها اسکریپت بوت‌استرپ را با چندین درخواست (حریم خصوصی، تأخیر، هزینه) در حالت دمای قطعی=0 اجرا می‌کنند تا خروجی‌های پایه را برای مقایسه‌های بعدی (معیارگذاری جلسه ۳ و مقایسه SLM و LLM در جلسه ۴) ثبت کنند.  

### مجموعه درخواست‌های حداقلی JSON (اختیاری)  
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```
  
از این لیست برای ایجاد یک حلقه ارزیابی قابل بازتولید یا برای شروع یک چارچوب تست رگرسیون آینده استفاده کنید.  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.