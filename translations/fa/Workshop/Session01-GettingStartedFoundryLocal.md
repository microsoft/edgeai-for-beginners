# جلسه ۱: شروع کار با Foundry Local

## خلاصه

یاد بگیرید چگونه مدل‌های هوش مصنوعی را با استفاده از Microsoft Foundry Local نصب، پیکربندی و اجرا کنید. این جلسه عملی، یک معرفی گام‌به‌گام از استنتاج محلی ارائه می‌دهد، از نصب تا ساخت اولین برنامه چت با استفاده از مدل‌هایی مانند Phi-4، Qwen و DeepSeek.

## اهداف یادگیری

در پایان این جلسه، شما قادر خواهید بود:

- **نصب و پیکربندی**: Foundry Local را با تأیید نصب صحیح راه‌اندازی کنید.
- **تسلط بر عملیات CLI**: از CLI Foundry Local برای مدیریت و استقرار مدل‌ها استفاده کنید.
- **اجرای اولین مدل**: یک مدل هوش مصنوعی محلی را با موفقیت اجرا و با آن تعامل کنید.
- **ساخت برنامه چت**: یک برنامه چت ساده با استفاده از Foundry Local Python SDK ایجاد کنید.
- **درک هوش مصنوعی محلی**: اصول استنتاج محلی و مدیریت مدل‌ها را بفهمید.

## پیش‌نیازها

### الزامات سیستم

- **ویندوز**: ویندوز ۱۱ (۲۲H۲ یا بالاتر) یا **macOS**: macOS 11+ (پشتیبانی محدود)
- **رم**: حداقل ۸ گیگابایت، توصیه شده ۱۶ گیگابایت یا بیشتر
- **فضای ذخیره‌سازی**: حداقل ۱۰ گیگابایت فضای آزاد برای مدل‌ها
- **پایتون**: نسخه ۳.۱۰ یا بالاتر نصب شده باشد
- **دسترسی ادمین**: دسترسی مدیر برای نصب

### محیط توسعه

- Visual Studio Code با افزونه پایتون (توصیه شده)
- دسترسی به خط فرمان (PowerShell در ویندوز، Terminal در macOS)
- Git برای کلون کردن مخازن (اختیاری)

## جریان کارگاه (۳۰ دقیقه)

### مرحله ۱: نصب Foundry Local (۵ دقیقه)

#### نصب در ویندوز

Foundry Local را با استفاده از مدیر بسته ویندوز نصب کنید:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

روش جایگزین: دانلود مستقیم از [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### نصب در macOS (پشتیبانی محدود)

> [!NOTE] 
> پشتیبانی macOS در حال حاضر در حالت پیش‌نمایش است. برای آخرین اطلاعات به مستندات رسمی مراجعه کنید.

در صورت امکان، با استفاده از Homebrew نصب کنید:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**روش جایگزین برای کاربران macOS:**
- از یک ماشین مجازی ویندوز ۱۱ (Parallels/UTM) استفاده کنید و مراحل ویندوز را دنبال کنید.
- از طریق کانتینر اجرا کنید (در صورت موجود بودن) و `FOUNDRY_LOCAL_ENDPOINT` را پیکربندی کنید.

### مرحله ۲: تأیید نصب (۳ دقیقه)

پس از نصب، ترمینال خود را مجدداً راه‌اندازی کنید و مطمئن شوید Foundry Local کار می‌کند:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

خروجی مورد انتظار باید اطلاعات نسخه و دستورات موجود را نشان دهد.

### مرحله ۳: تنظیم محیط پایتون (۵ دقیقه)

یک محیط پایتون اختصاصی برای این کارگاه ایجاد کنید:

**ویندوز:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### مرحله ۴: اجرای اولین مدل (۷ دقیقه)

حالا اولین مدل هوش مصنوعی خود را به صورت محلی اجرا کنید!

#### شروع با Phi-4 Mini (مدل پیشنهادی اولیه)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> این دستور مدل را (برای اولین بار) دانلود کرده و سرویس Foundry Local را به طور خودکار شروع می‌کند.

#### بررسی مدل‌های در حال اجرا

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### امتحان مدل‌های مختلف

پس از اجرای phi-4-mini، مدل‌های دیگر را آزمایش کنید:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### مرحله ۵: ساخت اولین برنامه چت (۱۰ دقیقه)

حالا یک برنامه پایتون ایجاد کنید که از مدل‌هایی که اجرا کردیم استفاده کند.

#### ایجاد اسکریپت چت

یک فایل جدید به نام `my_first_chat.py` ایجاد کنید (یا از نمونه ارائه شده استفاده کنید):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **نمونه‌های مرتبط**: برای استفاده پیشرفته‌تر، ببینید:
>
> - **نمونه پایتون**: `Workshop/samples/session01/chat_bootstrap.py` - شامل پاسخ‌های استریم و مدیریت خطا
> - **دفترچه Jupyter**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - نسخه تعاملی با توضیحات دقیق

#### آزمایش برنامه چت

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

روش جایگزین: از نمونه‌های ارائه شده مستقیماً استفاده کنید

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

یا دفترچه تعاملی را بررسی کنید  
Workshop/notebooks/session01_chat_bootstrap.ipynb را در VS Code باز کنید

این مکالمات نمونه را امتحان کنید:

- "Microsoft Foundry Local چیست؟"
- "۳ مزیت اجرای مدل‌های هوش مصنوعی به صورت محلی را لیست کنید."
- "به من کمک کن تا هوش مصنوعی لبه را بفهمم."

## دستاوردهای شما

تبریک! شما با موفقیت:

1. ✅ **Foundry Local را نصب کردید** و مطمئن شدید که کار می‌کند.
2. ✅ **اولین مدل هوش مصنوعی خود را اجرا کردید** (phi-4-mini) به صورت محلی.
3. ✅ **مدل‌های مختلف را آزمایش کردید** از طریق خط فرمان.
4. ✅ **یک برنامه چت ساختید** که به هوش مصنوعی محلی شما متصل می‌شود.
5. ✅ **استنتاج هوش مصنوعی محلی را تجربه کردید** بدون وابستگی به ابر.

## درک آنچه اتفاق افتاد

### استنتاج هوش مصنوعی محلی

- مدل‌های هوش مصنوعی شما کاملاً روی کامپیوتر شما اجرا می‌شوند.
- هیچ داده‌ای به ابر ارسال نمی‌شود.
- پاسخ‌ها به صورت محلی با استفاده از CPU/GPU شما تولید می‌شوند.
- حریم خصوصی و امنیت حفظ می‌شود.

### مدیریت مدل‌ها

- `foundry model run` مدل‌ها را دانلود و اجرا می‌کند.
- **FoundryLocalManager SDK** به طور خودکار راه‌اندازی سرویس و بارگذاری مدل‌ها را مدیریت می‌کند.
- مدل‌ها برای استفاده‌های آینده به صورت محلی ذخیره می‌شوند.
- چندین مدل می‌توانند دانلود شوند اما معمولاً یک مدل در یک زمان اجرا می‌شود.
- سرویس به طور خودکار چرخه عمر مدل را مدیریت می‌کند.

### رویکرد SDK در مقابل CLI

- **رویکرد CLI**: مدیریت دستی مدل‌ها با `foundry model run <model>`
- **رویکرد SDK**: مدیریت خودکار سرویس و مدل‌ها با `FoundryLocalManager(alias)`
- **توصیه**: از SDK برای برنامه‌ها استفاده کنید، از CLI برای آزمایش و کاوش.

## مرجع دستورات رایج

### دستورات CLI ضروری

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### توصیه‌های مدل

- **phi-4-mini**: بهترین مدل برای شروع - سریع، سبک، کیفیت خوب
- **qwen2.5-0.5b**: سریع‌ترین استنتاج، حداقل استفاده از حافظه
- **gpt-oss-20b**: پاسخ‌های با کیفیت بالاتر، نیازمند منابع بیشتر
- **deepseek-coder-1.3b**: بهینه شده برای برنامه‌نویسی و وظایف کدنویسی

## رفع مشکلات

### "دستور Foundry پیدا نشد"

**راه‌حل:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "مدل بارگذاری نشد"

**راه‌حل:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "اتصال به localhost رد شد"

**راه‌حل:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## مراحل بعدی

### اقدامات فوری بعدی

1. **آزمایش** مدل‌ها و درخواست‌های مختلف
2. **تغییر** برنامه چت خود برای امتحان مدل‌های مختلف
3. **ایجاد** درخواست‌های خود و آزمایش پاسخ‌ها
4. **کاوش** جلسه ۲: ساخت برنامه‌های RAG

### مسیر یادگیری پیشرفته

1. **جلسه ۲**: ساخت راه‌حل‌های هوش مصنوعی با RAG (تولید تقویت‌شده با بازیابی)
2. **جلسه ۳**: مقایسه مدل‌های متن‌باز مختلف
3. **جلسه ۴**: کار با مدل‌های پیشرفته
4. **جلسه ۵**: ساخت سیستم‌های هوش مصنوعی چندعاملی

## متغیرهای محیطی (اختیاری)

برای استفاده پیشرفته‌تر، می‌توانید این متغیرهای محیطی را تنظیم کنید:

| متغیر | هدف | مثال |
|-------|------|-------|
| `FOUNDRY_LOCAL_ALIAS` | مدل پیش‌فرض برای استفاده | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | تغییر آدرس URL نقطه پایانی | `http://localhost:5273/v1` |

یک فایل `.env` در دایرکتوری پروژه خود ایجاد کنید:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## منابع اضافی

### مستندات

- [مرجع Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [راهنمای نصب Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [کاتالوگ مدل‌ها](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### کد نمونه

- **نمونه پایتون جلسه ۰۱**: `Workshop/samples/session01/chat_bootstrap.py` - برنامه چت کامل با استریم
- **دفترچه جلسه ۰۱**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - آموزش تعاملی  
- [نمونه ۰۱ ماژول ۰۸](../Module08/samples/01/README.md) - شروع سریع چت REST
- [نمونه ۰۲ ماژول ۰۸](../Module08/samples/02/README.md) - یکپارچه‌سازی SDK OpenAI
- [نمونه ۰۳ ماژول ۰۸](../Module08/samples/03/README.md) - کشف و ارزیابی مدل‌ها

### جامعه

- [بحث‌های GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [جامعه Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**مدت زمان جلسه**: ۳۰ دقیقه عملی + ۱۵ دقیقه پرسش و پاسخ  
**سطح دشواری**: مبتدی  
**پیش‌نیازها**: ویندوز ۱۱/macOS 11+، پایتون ۳.۱۰+، دسترسی ادمین

## سناریوی مثال کارگاه

### زمینه واقعی

**سناریو**: یک تیم IT سازمانی نیاز دارد استنتاج هوش مصنوعی روی دستگاه را برای پردازش بازخورد حساس کارکنان بدون ارسال داده‌ها به سرویس‌های خارجی ارزیابی کند.

**هدف شما**: نشان دهید که مدل‌های هوش مصنوعی محلی می‌توانند پاسخ‌های با کیفیتی با تأخیر زیر یک ثانیه ارائه دهند و در عین حال حریم خصوصی داده‌ها را کاملاً حفظ کنند.

### درخواست‌های آزمایشی

از این درخواست‌ها برای اعتبارسنجی تنظیمات خود استفاده کنید:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### معیارهای موفقیت

- ✅ همه درخواست‌ها در کمتر از ۲ ثانیه پاسخ داده شوند.
- ✅ هیچ داده‌ای از دستگاه شما خارج نشود.
- ✅ پاسخ‌ها مرتبط و مفید باشند.
- ✅ برنامه چت شما به روانی کار کند.

این اعتبارسنجی تضمین می‌کند که تنظیمات Foundry Local شما برای کارگاه‌های پیشرفته در جلسات ۲ تا ۶ آماده است.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->