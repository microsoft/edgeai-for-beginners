# دليل دمج Open WebUI مع Foundry Local

يشرح هذا الدليل كيفية ربط Open WebUI بـ Microsoft Foundry Local للحصول على واجهة احترافية مشابهة لـ ChatGPT مدعومة بنماذج الذكاء الاصطناعي المحلية لديك.

## نظرة عامة

يوفر Open WebUI واجهة دردشة حديثة وسهلة الاستخدام يمكنها الاتصال بأي واجهة برمجة تطبيقات متوافقة مع OpenAI. من خلال ربطه بـ Foundry Local، ستحصل على:

- **واجهة احترافية**: واجهة مشابهة لـ ChatGPT بتصميم عصري
- **خصوصية محلية**: تتم جميع المعالجة على جهازك
- **تبديل النماذج**: سهولة التبديل بين النماذج المحلية المختلفة
- **تاريخ المحادثات**: سجل محادثات مستمر وسياق محفوظ
- **رفع الملفات**: تحليل المستندات ومعالجة الملفات
- **شخصيات مخصصة**: تخصيص الأدوار والمطالبات النظامية

## المتطلبات الأساسية

### البرامج المطلوبة

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### تحميل نموذج

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## الإعداد السريع (موصى به)

### الخطوة 1: تشغيل Open WebUI باستخدام Docker

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

### الخطوة 2: الإعداد الأولي

1. **فتح المتصفح**: انتقل إلى `http://localhost:3000`
2. **إنشاء حساب**: قم بإعداد مستخدم مسؤول (أول مستخدم يصبح مسؤولاً)
3. **التحقق من الاتصال**: يجب أن تظهر النماذج تلقائيًا في القائمة المنسدلة

### الخطوة 3: اختبار الاتصال

1. اختر النموذج من القائمة المنسدلة (مثل "phi-4-mini")
2. اكتب رسالة اختبار: "مرحبًا! هل يمكنك تقديم نفسك؟"
3. يجب أن ترى استجابة متدفقة من النموذج المحلي لديك

## الإعدادات المتقدمة

### متغيرات البيئة

| المتغير | الغرض | الافتراضي | المثال |
|---------|-------|-----------|--------|
| `OPENAI_API_BASE_URL` | نقطة نهاية Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | مفتاح API (مطلوب ولكن غير مستخدم محليًا) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | مفتاح تشفير الجلسة | يتم إنشاؤه تلقائيًا | `your-secret-key` |
| `ENABLE_SIGNUP` | السماح بتسجيل مستخدمين جدد | `True` | `False` |

### الإعداد اليدوي (بديل)

إذا لم تعمل متغيرات البيئة، قم بالإعداد يدويًا:

1. **فتح الإعدادات**: انقر على الإعدادات (رمز الترس)
2. **الانتقال إلى الاتصالات**: الإعدادات → الاتصالات → OpenAI
3. **تعيين تفاصيل API**:
   - عنوان قاعدة API: `http://host.docker.internal:51211/v1`
   - مفتاح API: `foundry-local-key` (أي قيمة تعمل)
4. **الحفظ والاختبار**: انقر على "حفظ" ثم اختبر باستخدام نموذج

### تخزين البيانات المستمر

لحفظ المحادثات والإعدادات:

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

## استكشاف الأخطاء وإصلاحها

### مشاكل الاتصال

**المشكلة**: "رفض الاتصال" أو عدم تحميل النماذج

**الحلول**:
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

### النموذج غير ظاهر

**المشكلة**: Open WebUI لا يظهر أي نماذج في القائمة المنسدلة

**خطوات التصحيح**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**الإصلاح**: تأكد من تحميل النموذج بشكل صحيح:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### مشاكل شبكة Docker

**المشكلة**: `host.docker.internal` لا يعمل

**الحل لنظام Windows**:
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

**البديل**: العثور على عنوان IP لجهازك:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### مشاكل الأداء

**الاستجابات البطيئة**:
1. تحقق من أن النموذج يستخدم تسريع GPU: `foundry service ps`
2. تأكد من وجود موارد كافية للنظام (RAM/ذاكرة GPU)
3. فكر في استخدام نموذج أصغر للاختبار

**مشاكل الذاكرة**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## دليل الاستخدام

### الدردشة الأساسية

1. **اختيار النموذج**: اختر من القائمة المنسدلة (تظهر نماذج Foundry Local)
2. **كتابة الرسالة**: استخدم حقل النص في الأسفل
3. **الإرسال**: اضغط Enter أو انقر على زر الإرسال
4. **عرض الاستجابة**: شاهد الاستجابة المتدفقة في الوقت الفعلي

### الميزات المتقدمة

**رفع الملفات**:
1. انقر على رمز المشبك الورقي
2. قم برفع مستند (PDF، TXT، إلخ)
3. اطرح أسئلة حول المحتوى
4. سيقوم النموذج بتحليل المستند والرد بناءً على المحتوى

**مطالبات النظام المخصصة**:
1. الإعدادات → التخصيص
2. قم بتعيين مطالبة نظام مخصصة
3. يخلق شخصية/سلوك ثابت للذكاء الاصطناعي

**إدارة المحادثات**:
- **محادثة جديدة**: انقر على "+" لبدء محادثة جديدة
- **تاريخ المحادثات**: الوصول إلى المحادثات السابقة من الشريط الجانبي
- **التصدير**: تنزيل تاريخ المحادثات كملف نصي/JSON

**مقارنة النماذج**:
1. افتح عدة علامات تبويب في المتصفح لنفس Open WebUI
2. اختر نماذج مختلفة في كل علامة تبويب
3. قارن الاستجابات لنفس المطالبات

### أنماط التكامل

**سير العمل التطويري**:
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

## النشر في بيئة الإنتاج

### الإعداد الآمن

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

### إعداد متعدد المستخدمين

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

### المراقبة والتسجيل

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## التنظيف

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

## الخطوات التالية

### أفكار للتحسين

1. **نماذج مخصصة**: أضف نماذجك الخاصة التي تم تحسينها إلى Foundry Local
2. **تكامل API**: قم بالاتصال بـ APIs خارجية عبر وظائف Open WebUI
3. **معالجة المستندات**: إعداد خطوط أنابيب RAG متقدمة
4. **متعدد الوسائط**: تكوين نماذج الرؤية لتحليل الصور

### اعتبارات التوسع

- **موازنة التحميل**: تشغيل عدة مثيلات من Foundry Local خلف وكيل عكسي
- **توجيه النماذج**: استخدام نماذج مختلفة لحالات استخدام مختلفة
- **إدارة الموارد**: تحسين ذاكرة GPU للمستخدمين المتزامنين
- **استراتيجية النسخ الاحتياطي**: النسخ الاحتياطي المنتظم لبيانات المحادثات والإعدادات

## المراجع

- [وثائق Open WebUI](https://docs.openwebui.com/)
- [مستودع GitHub لـ Open WebUI](https://github.com/open-webui/open-webui)
- [وثائق Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [دليل تثبيت Docker](https://docs.docker.com/get-docker/)

---

