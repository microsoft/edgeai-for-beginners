# اوپن ویب یو آئی + فاؤنڈری لوکل انٹیگریشن گائیڈ

یہ گائیڈ دکھاتی ہے کہ اوپن ویب یو آئی کو مائیکروسافٹ فاؤنڈری لوکل کے ساتھ کیسے جوڑا جائے تاکہ آپ کے لوکل AI ماڈلز کے ذریعے ایک پیشہ ورانہ چیٹ جی پی ٹی جیسا انٹرفیس حاصل کیا جا سکے۔

## جائزہ

اوپن ویب یو آئی ایک جدید، صارف دوست چیٹ انٹرفیس فراہم کرتا ہے جو کسی بھی اوپن اے آئی-کمپیٹیبل API سے جڑ سکتا ہے۔ اسے فاؤنڈری لوکل کے ساتھ جوڑنے سے آپ کو ملتا ہے:

- **پیشہ ورانہ UI**: چیٹ جی پی ٹی جیسا انٹرفیس جدید ڈیزائن کے ساتھ
- **لوکل پرائیویسی**: تمام پروسیسنگ آپ کے ڈیوائس پر ہوتی ہے
- **ماڈل سوئچنگ**: مختلف لوکل ماڈلز کے درمیان آسان سوئچنگ
- **گفتگو کی تاریخ**: مستقل چیٹ ہسٹری اور کانٹیکسٹ
- **فائل اپلوڈز**: دستاویزات کا تجزیہ اور فائل پروسیسنگ کی صلاحیتیں
- **کسٹم پرسناز**: سسٹم پرامپٹس اور رول کی تخصیص

## ضروریات

### مطلوبہ سافٹ ویئر

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### ماڈل لوڈ کریں

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## فوری سیٹ اپ (تجویز کردہ)

### مرحلہ 1: اوپن ویب یو آئی کو ڈاکر کے ساتھ چلائیں

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

**ونڈوز پاور شیل:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### مرحلہ 2: ابتدائی سیٹ اپ

1. **براؤزر کھولیں**: `http://localhost:3000` پر جائیں
2. **اکاؤنٹ بنائیں**: ایڈمن صارف سیٹ اپ کریں (پہلا صارف ایڈمن بن جاتا ہے)
3. **کنکشن کی تصدیق کریں**: ماڈلز خود بخود ڈراپ ڈاؤن میں ظاہر ہونے چاہئیں

### مرحلہ 3: کنکشن کا ٹیسٹ کریں

1. اپنے ماڈل کو ڈراپ ڈاؤن سے منتخب کریں (مثلاً، "phi-4-mini")
2. ایک ٹیسٹ میسج لکھیں: "ہیلو! کیا آپ اپنا تعارف کروا سکتے ہیں؟"
3. آپ کو اپنے لوکل ماڈل سے اسٹریمنگ رسپانس نظر آنا چاہیے

## ایڈوانسڈ کنفیگریشن

### ماحول کے متغیرات

| متغیر | مقصد | ڈیفالٹ | مثال |
|-------|-------|---------|-------|
| `OPENAI_API_BASE_URL` | فاؤنڈری لوکل اینڈ پوائنٹ | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API کی (ضروری لیکن لوکل میں استعمال نہیں ہوتی) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | سیشن انکرپشن کی | خودکار طور پر جنریٹڈ | `your-secret-key` |
| `ENABLE_SIGNUP` | نئے صارفین کی رجسٹریشن کی اجازت دیں | `True` | `False` |

### دستی کنفیگریشن (متبادل)

اگر ماحول کے متغیرات کام نہ کریں، تو دستی طور پر کنفیگر کریں:

1. **سیٹنگز کھولیں**: سیٹنگز (گیئر آئیکن) پر کلک کریں
2. **کنکشنز پر جائیں**: سیٹنگز → کنکشنز → اوپن اے آئی
3. **API کی تفصیلات سیٹ کریں**:
   - API بیس URL: `http://host.docker.internal:51211/v1`
   - API کی: `foundry-local-key` (کوئی بھی ویلیو کام کرے گی)
4. **محفوظ کریں اور ٹیسٹ کریں**: "محفوظ کریں" پر کلک کریں پھر ماڈل کے ساتھ ٹیسٹ کریں

### مستقل ڈیٹا اسٹوریج

گفتگو اور سیٹنگز کو محفوظ رکھنے کے لیے:

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

## مسائل کا حل

### کنکشن کے مسائل

**مسئلہ**: "کنکشن ریفیوزڈ" یا ماڈلز لوڈ نہیں ہو رہے

**حل**:
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

### ماڈل ظاہر نہیں ہو رہا

**مسئلہ**: اوپن ویب یو آئی ڈراپ ڈاؤن میں کوئی ماڈل نہیں دکھا رہا

**ڈی بگنگ کے مراحل**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**حل**: یقینی بنائیں کہ ماڈل صحیح طریقے سے لوڈ ہوا ہے:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### ڈاکر نیٹ ورک کے مسائل

**مسئلہ**: `host.docker.internal` حل نہیں ہو رہا

**ونڈوز حل**:
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

**متبادل**: اپنی مشین کا IP تلاش کریں:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### کارکردگی کے مسائل

**سست رسپانسز**:
1. چیک کریں کہ ماڈل GPU ایکسیلیریشن استعمال کر رہا ہے: `foundry service ps`
2. مناسب سسٹم وسائل (RAM/GPU میموری) کی تصدیق کریں
3. ٹیسٹنگ کے لیے چھوٹا ماڈل استعمال کرنے پر غور کریں

**میموری کے مسائل**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## استعمال کی گائیڈ

### بنیادی چیٹ

1. **ماڈل منتخب کریں**: ڈراپ ڈاؤن سے منتخب کریں (فاؤنڈری لوکل ماڈلز دکھاتا ہے)
2. **میسج لکھیں**: نیچے دیے گئے ٹیکسٹ ان پٹ کا استعمال کریں
3. **بھیجیں**: انٹر دبائیں یا بھیجنے کے بٹن پر کلک کریں
4. **رسپانس دیکھیں**: اسٹریمنگ رسپانس کو حقیقی وقت میں دیکھیں

### ایڈوانسڈ فیچرز

**فائل اپلوڈ**:
1. پیپر کلپ آئیکن پر کلک کریں
2. دستاویز اپلوڈ کریں (PDF، TXT، وغیرہ)
3. مواد کے بارے میں سوالات پوچھیں
4. ماڈل دستاویز کا تجزیہ کرے گا اور مواد کی بنیاد پر جواب دے گا

**کسٹم سسٹم پرامپٹس**:
1. سیٹنگز → پرسنلائزیشن
2. کسٹم سسٹم پرامپٹ سیٹ کریں
3. مستقل AI شخصیت/رویے تخلیق کریں

**گفتگو کا انتظام**:
- **نئی چیٹ**: "+" پر کلک کریں تاکہ نئی گفتگو شروع کریں
- **چیٹ ہسٹری**: سائڈبار سے پچھلی گفتگو تک رسائی حاصل کریں
- **ایکسپورٹ**: چیٹ ہسٹری کو ٹیکسٹ/JSON کے طور پر ڈاؤنلوڈ کریں

**ماڈل کا موازنہ**:
1. اوپن ویب یو آئی کو ایک ہی وقت میں کئی براؤزر ٹیبز میں کھولیں
2. ہر ٹیب میں مختلف ماڈلز منتخب کریں
3. ایک ہی پرامپٹس کے جوابات کا موازنہ کریں

### انٹیگریشن پیٹرنز

**ڈیولپمنٹ ورک فلو**:
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

## پروڈکشن ڈیپلائمنٹ

### محفوظ سیٹ اپ

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

### ملٹی یوزر سیٹ اپ

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

### مانیٹرنگ اور لاگنگ

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## صفائی

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

## اگلے مراحل

### بہتری کے خیالات

1. **کسٹم ماڈلز**: اپنے فائن ٹیونڈ ماڈلز کو فاؤنڈری لوکل میں شامل کریں
2. **API انٹیگریشن**: اوپن ویب یو آئی فنکشنز کے ذریعے بیرونی APIs سے جڑیں
3. **دستاویز پروسیسنگ**: ایڈوانسڈ RAG پائپ لائنز سیٹ اپ کریں
4. **ملٹی موڈل**: امیج تجزیہ کے لیے وژن ماڈلز کو کنفیگر کریں

### اسکیلنگ کے خیالات

- **لوڈ بیلنسنگ**: ریورس پراکسی کے پیچھے کئی فاؤنڈری لوکل انسٹینسز
- **ماڈل روٹنگ**: مختلف استعمال کے کیسز کے لیے مختلف ماڈلز
- **وسائل کا انتظام**: متوازی صارفین کے لیے GPU میموری کی اصلاح
- **بیک اپ حکمت عملی**: گفتگو کے ڈیٹا اور کنفیگریشنز کا باقاعدہ بیک اپ

## حوالہ جات

- [اوپن ویب یو آئی دستاویزات](https://docs.openwebui.com/)
- [اوپن ویب یو آئی گٹ ہب ریپوزٹری](https://github.com/open-webui/open-webui)
- [فاؤنڈری لوکل دستاویزات](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [ڈاکر انسٹالیشن گائیڈ](https://docs.docker.com/get-docker/)

---

