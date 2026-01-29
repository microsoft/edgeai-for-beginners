# راهنمای اتصال Open WebUI + Foundry Local

این راهنما نحوه اتصال Open WebUI به Microsoft Foundry Local را برای یک رابط حرفه‌ای مشابه ChatGPT که توسط مدل‌های هوش مصنوعی محلی شما قدرت گرفته است، نشان می‌دهد.

## مرور کلی

Open WebUI یک رابط چت مدرن و کاربرپسند ارائه می‌دهد که می‌تواند به هر API سازگار با OpenAI متصل شود. با اتصال آن به Foundry Local، شما موارد زیر را دریافت می‌کنید:

- **رابط کاربری حرفه‌ای**: رابطی مشابه ChatGPT با طراحی مدرن
- **حریم خصوصی محلی**: تمام پردازش‌ها روی دستگاه شما انجام می‌شود
- **تغییر مدل**: تغییر آسان بین مدل‌های محلی مختلف
- **تاریخچه مکالمه**: تاریخچه چت و زمینه مکالمه پایدار
- **آپلود فایل**: قابلیت تحلیل اسناد و پردازش فایل‌ها
- **شخصیت‌های سفارشی**: تنظیمات سیستم و سفارشی‌سازی نقش‌ها

## پیش‌نیازها

### نرم‌افزار مورد نیاز

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### بارگذاری یک مدل

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## راه‌اندازی سریع (توصیه‌شده)

### مرحله 1: اجرای Open WebUI با Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### مرحله 2: تنظیم اولیه

1. **باز کردن مرورگر**: به آدرس `http://localhost:3000` بروید
2. **ایجاد حساب کاربری**: کاربر مدیر را تنظیم کنید (اولین کاربر مدیر می‌شود)
3. **تأیید اتصال**: مدل‌ها باید به‌طور خودکار در منوی کشویی ظاهر شوند

### مرحله 3: آزمایش اتصال

1. مدل خود را از منوی کشویی انتخاب کنید (مثلاً "phi-4-mini")
2. یک پیام آزمایشی تایپ کنید: "سلام! می‌توانید خودتان را معرفی کنید؟"
3. باید یک پاسخ جریان‌دار از مدل محلی خود مشاهده کنید

## تنظیمات پیشرفته

### متغیرهای محیطی

| متغیر | هدف | پیش‌فرض | مثال |
|-------|------|---------|-------|
| `OPENAI_API_BASE_URL` | نقطه پایانی Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | کلید API (ضروری اما محلی استفاده نمی‌شود) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | کلید رمزگذاری جلسه | خودکار تولید می‌شود | `your-secret-key` |
| `ENABLE_SIGNUP` | اجازه ثبت‌نام کاربران جدید | `True` | `False` |

### تنظیم دستی (جایگزین)

اگر متغیرهای محیطی کار نکردند، به‌صورت دستی تنظیم کنید:

1. **باز کردن تنظیمات**: روی تنظیمات (آیکون چرخ‌دنده) کلیک کنید
2. **رفتن به اتصالات**: تنظیمات → اتصالات → OpenAI
3. **تنظیم جزئیات API**:
   - آدرس پایه API: `http://host.docker.internal:51211/v1`
   - کلید API: `foundry-local-key` (هر مقداری کار می‌کند)
4. **ذخیره و آزمایش**: روی "ذخیره" کلیک کنید و سپس با یک مدل آزمایش کنید

### ذخیره‌سازی داده‌های پایدار

برای حفظ مکالمات و تنظیمات:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## رفع مشکلات

### مشکلات اتصال

**مشکل**: "اتصال رد شد" یا مدل‌ها بارگذاری نمی‌شوند

**راه‌حل‌ها**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### مدل ظاهر نمی‌شود

**مشکل**: Open WebUI هیچ مدلی در منوی کشویی نشان نمی‌دهد

**مراحل اشکال‌زدایی**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**رفع مشکل**: اطمینان حاصل کنید که مدل به‌درستی بارگذاری شده است:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### مشکلات شبکه Docker

**مشکل**: `host.docker.internal` حل نمی‌شود

**راه‌حل ویندوز**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**جایگزین**: آدرس IP دستگاه خود را پیدا کنید:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### مشکلات عملکرد

**پاسخ‌های کند**:
1. بررسی کنید که مدل از شتاب‌دهی GPU استفاده می‌کند: `foundry service ps`
2. اطمینان حاصل کنید که منابع سیستم کافی هستند (رم/حافظه GPU)
3. برای آزمایش از یک مدل کوچک‌تر استفاده کنید

**مشکلات حافظه**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## راهنمای استفاده

### چت پایه

1. **انتخاب مدل**: از منوی کشویی انتخاب کنید (مدل‌های Foundry Local نمایش داده می‌شوند)
2. **تایپ پیام**: از ورودی متن در پایین استفاده کنید
3. **ارسال**: Enter را فشار دهید یا روی دکمه ارسال کلیک کنید
4. **مشاهده پاسخ**: پاسخ جریان‌دار را در زمان واقعی مشاهده کنید

### ویژگی‌های پیشرفته

**آپلود فایل**:
1. روی آیکون گیره کاغذ کلیک کنید
2. سندی را آپلود کنید (PDF، TXT و غیره)
3. درباره محتوای سند سؤال کنید
4. مدل سند را تحلیل کرده و بر اساس آن پاسخ می‌دهد

**سیستم‌های سفارشی**:
1. تنظیمات → شخصی‌سازی
2. تنظیم سیستم سفارشی
3. ایجاد شخصیت/رفتار ثابت برای هوش مصنوعی

**مدیریت مکالمه**:
- **چت جدید**: روی "+" کلیک کنید تا مکالمه جدیدی شروع شود
- **تاریخچه چت**: به مکالمات قبلی از نوار کناری دسترسی پیدا کنید
- **صادرات**: تاریخچه چت را به‌صورت متن/JSON دانلود کنید

**مقایسه مدل‌ها**:
1. چندین تب مرورگر را به همان Open WebUI باز کنید
2. مدل‌های مختلف را در هر تب انتخاب کنید
3. پاسخ‌ها را به همان درخواست‌ها مقایسه کنید

### الگوهای یکپارچه‌سازی

**جریان کاری توسعه**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## استقرار در محیط تولید

### تنظیمات امن

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### تنظیمات چندکاربره

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### نظارت و ثبت گزارش

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## پاکسازی

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## مراحل بعدی

### ایده‌های بهبود

1. **مدل‌های سفارشی**: مدل‌های تنظیم‌شده خود را به Foundry Local اضافه کنید
2. **یکپارچه‌سازی API**: اتصال به API‌های خارجی از طریق توابع Open WebUI
3. **پردازش اسناد**: تنظیم خطوط پیشرفته RAG
4. **چندوجهی**: پیکربندی مدل‌های تصویری برای تحلیل تصاویر

### ملاحظات مقیاس‌پذیری

- **تعادل بار**: چندین نمونه Foundry Local پشت پروکسی معکوس
- **مسیر‌یابی مدل**: مدل‌های مختلف برای موارد استفاده مختلف
- **مدیریت منابع**: بهینه‌سازی حافظه GPU برای کاربران همزمان
- **استراتژی پشتیبان‌گیری**: پشتیبان‌گیری منظم از داده‌های مکالمه و تنظیمات

## منابع

- [مستندات Open WebUI](https://docs.openwebui.com/)
- [مخزن GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [مستندات Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [راهنمای نصب Docker](https://docs.docker.com/get-docker/)

---

