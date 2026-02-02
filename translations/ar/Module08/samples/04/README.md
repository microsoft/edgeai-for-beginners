# نموذج 04: تطبيقات الدردشة الإنتاجية باستخدام Chainlit

نموذج شامل يوضح طرق متعددة لبناء تطبيقات دردشة جاهزة للإنتاج باستخدام Microsoft Foundry Local، مع واجهات ويب حديثة، استجابات متدفقة، وتقنيات متقدمة للمتصفح.

## ما يتضمنه النموذج

- **🚀 تطبيق دردشة Chainlit** (`app.py`): تطبيق دردشة جاهز للإنتاج مع استجابات متدفقة
- **🌐 عرض WebGPU** (`webgpu-demo/`): استنتاج الذكاء الاصطناعي عبر المتصفح مع تسريع الأجهزة
- **🎨 تكامل واجهة Open WebUI** (`open-webui-guide.md`): واجهة احترافية مشابهة لـ ChatGPT
- **📚 دفتر تعليمي** (`chainlit_app.ipynb`): مواد تعليمية تفاعلية

## البدء السريع

### 1. تطبيق دردشة Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

يفتح على: `http://localhost:8080`

### 2. عرض WebGPU عبر المتصفح

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

يفتح على: `http://localhost:5173`

### 3. إعداد واجهة Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

يفتح على: `http://localhost:3000`

## أنماط الهندسة المعمارية

### مصفوفة اتخاذ القرار بين المحلي والسحابي

| السيناريو | التوصية | السبب |
|-----------|---------|-------|
| **البيانات الحساسة للخصوصية** | 🏠 محلي (Foundry) | البيانات لا تغادر الجهاز |
| **الاستنتاج المعقد** | ☁️ سحابي (Azure OpenAI) | الوصول إلى نماذج أكبر |
| **الدردشة في الوقت الفعلي** | 🏠 محلي (Foundry) | زمن استجابة أقل، استجابات أسرع |
| **تحليل المستندات** | 🔄 مختلط | محلي للاستخراج، سحابي للتحليل |
| **توليد الأكواد** | 🏠 محلي (Foundry) | الخصوصية + نماذج متخصصة |
| **مهام البحث** | ☁️ سحابي (Azure OpenAI) | قاعدة معرفة واسعة مطلوبة |

### مقارنة التقنيات

| التقنية | الاستخدام | المزايا | العيوب |
|---------|-----------|---------|--------|
| **Chainlit** | مطورو Python، النماذج الأولية السريعة | إعداد سهل، دعم الاستجابات المتدفقة | Python فقط |
| **WebGPU** | أقصى درجات الخصوصية، سيناريوهات غير متصلة | أصلي للمتصفح، لا حاجة للخادم | حجم النموذج محدود |
| **Open WebUI** | النشر الإنتاجي، الفرق | واجهة احترافية، إدارة المستخدمين | يتطلب Docker |

## المتطلبات الأساسية

- **Foundry Local**: مثبت ويعمل ([تحميل](https://aka.ms/foundry-local-installer))
- **Python**: الإصدار 3.10+ مع بيئة افتراضية
- **النموذج**: تحميل نموذج واحد على الأقل (`foundry model run phi-4-mini`)
- **المتصفح**: Chrome/Edge مع دعم WebGPU للعروض
- **Docker**: لـ Open WebUI (اختياري)

## التثبيت والإعداد

### 1. إعداد بيئة Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. إعداد Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## تطبيقات النموذج

### تطبيق دردشة Chainlit

**الميزات:**
- 🚀 **استجابات متدفقة في الوقت الفعلي**: ظهور الرموز أثناء توليدها
- 🛡️ **معالجة أخطاء قوية**: تدهور واسترداد سلس
- 🎨 **واجهة حديثة**: واجهة دردشة احترافية جاهزة
- 🔧 **تكوين مرن**: متغيرات البيئة والكشف التلقائي
- 📱 **تصميم متجاوب**: يعمل على أجهزة سطح المكتب والهواتف المحمولة

**البدء السريع:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### عرض WebGPU عبر المتصفح

**الميزات:**
- 🌐 **ذكاء اصطناعي أصلي للمتصفح**: لا حاجة للخادم، يعمل بالكامل في المتصفح
- ⚡ **تسريع WebGPU**: تسريع الأجهزة عند توفرها
- 🔒 **أقصى درجات الخصوصية**: البيانات لا تغادر جهازك أبدًا
- 🎯 **بدون تثبيت**: يعمل في أي متصفح متوافق
- 🔄 **تدهور سلس**: يتحول إلى CPU إذا كان WebGPU غير متوفر

**التشغيل:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### تكامل واجهة Open WebUI

**الميزات:**
- 🎨 **واجهة مشابهة لـ ChatGPT**: واجهة احترافية ومألوفة
- 👥 **دعم متعدد المستخدمين**: حسابات المستخدمين وسجل المحادثات
- 📁 **معالجة الملفات**: تحميل وتحليل المستندات
- 🔄 **تبديل النماذج**: تبديل سهل بين النماذج المختلفة
- 🐳 **نشر باستخدام Docker**: إعداد جاهز للإنتاج ومُحَوْسَب

**الإعداد السريع:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## مرجع التكوين

### متغيرات البيئة

| المتغير | الوصف | الافتراضي | المثال |
|---------|-------|----------|--------|
| `MODEL` | اسم النموذج المستخدم | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | نقطة نهاية Foundry Local | الكشف التلقائي | `http://localhost:51211` |
| `API_KEY` | مفتاح API (اختياري للمحلي) | `""` | `your-api-key` |

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

**تطبيق Chainlit:**

1. **الخدمة غير متوفرة:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **تعارض المنافذ:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **مشكلات بيئة Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**عرض WebGPU:**

1. **WebGPU غير مدعوم:**
   - التحديث إلى Chrome/Edge 113+
   - تمكين WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - التحقق من حالة GPU: `chrome://gpu`
   - العرض سيتحول تلقائيًا إلى CPU

2. **أخطاء تحميل النموذج:**
   - التأكد من اتصال الإنترنت لتحميل النموذج
   - التحقق من أخطاء CORS في وحدة تحكم المتصفح
   - التأكد من أنك تقدم عبر HTTP (وليس file://)

**Open WebUI:**

1. **رفض الاتصال:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **النماذج لا تظهر:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### قائمة التحقق من التحقق

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## الاستخدام المتقدم

### تحسين الأداء

**Chainlit:**
- استخدام الاستجابات المتدفقة لتحسين الأداء الظاهري
- تنفيذ تجميع الاتصالات لزيادة التزامن
- تخزين استجابات النموذج للاستفسارات المتكررة
- مراقبة استخدام الذاكرة مع سجلات المحادثات الكبيرة

**WebGPU:**
- استخدام WebGPU لأقصى درجات الخصوصية والسرعة
- تنفيذ تقليل حجم النموذج للنماذج الأصغر
- استخدام Web Workers للمعالجة الخلفية
- تخزين النماذج المجمعة في تخزين المتصفح

**Open WebUI:**
- استخدام وحدات تخزين دائمة لسجل المحادثات
- تكوين حدود الموارد لحاوية Docker
- تنفيذ استراتيجيات النسخ الاحتياطي لبيانات المستخدم
- إعداد وكيل عكسي لإنهاء SSL

### أنماط التكامل

**محلي/سحابي مختلط:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**خط أنابيب متعدد الوسائط:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## النشر الإنتاجي

### اعتبارات الأمان

- **مفاتيح API**: استخدام متغيرات البيئة، عدم تضمينها مباشرة
- **الشبكة**: استخدام HTTPS في الإنتاج، النظر في VPN للوصول الفريق
- **التحكم في الوصول**: تنفيذ المصادقة لـ Open WebUI
- **خصوصية البيانات**: مراجعة البيانات التي تبقى محلية مقابل التي تنتقل إلى السحابة
- **التحديثات**: الحفاظ على تحديث Foundry Local والحاويات

### المراقبة والصيانة

- **فحوصات الصحة**: تنفيذ مراقبة نقاط النهاية
- **التسجيل**: مركزية السجلات من جميع المكونات
- **المقاييس**: تتبع أوقات الاستجابة، معدلات الأخطاء، استخدام الموارد
- **النسخ الاحتياطي**: نسخ احتياطي منتظم لبيانات المحادثات والتكوينات

## المراجع والموارد

### الوثائق
- [وثائق Chainlit](https://docs.chainlit.io/) - دليل الإطار الكامل
- [وثائق Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - وثائق Microsoft الرسمية
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - تكامل WebGPU
- [وثائق Open WebUI](https://docs.openwebui.com/) - تكوين متقدم

### ملفات النموذج
- [`app.py`](../../../../../Module08/samples/04/app.py) - تطبيق Chainlit الإنتاجي
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - دفتر تعليمي
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - استنتاج الذكاء الاصطناعي عبر المتصفح
- [`open-webui-guide.md`](./open-webui-guide.md) - إعداد كامل لـ Open WebUI

### نماذج ذات صلة
- [وثائق الجلسة 4](../../04.CuttingEdgeModels.md) - دليل الجلسة الكامل
- [نماذج Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - نماذج رسمية

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.