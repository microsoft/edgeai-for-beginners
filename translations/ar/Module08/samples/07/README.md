# نموذج Foundry Local كواجهة برمجية API

يُظهر هذا النموذج كيفية استخدام Microsoft Foundry Local كخدمة REST API دون الاعتماد على OpenAI SDK. يوضح أنماط التكامل المباشر عبر HTTP للحصول على أقصى قدر من التحكم والتخصيص.

## نظرة عامة

استنادًا إلى أنماط Microsoft الرسمية لـ Foundry Local، يقدم هذا النموذج:
- تكامل مباشر مع واجهة REST API باستخدام FoundryLocalManager
- تنفيذ مخصص لعميل HTTP
- إدارة النماذج ومراقبة الحالة الصحية
- معالجة الاستجابات المتدفقة وغير المتدفقة
- معالجة الأخطاء وآليات إعادة المحاولة الجاهزة للإنتاج

## المتطلبات الأساسية

1. **تثبيت Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **اعتماديات Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## الهيكلية

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## الميزات الرئيسية

### 1. **التكامل المباشر عبر HTTP**
- استدعاءات REST API خالصة دون الاعتماد على SDK
- مصادقة مخصصة ورؤوس الطلبات
- التحكم الكامل في معالجة الطلبات والاستجابات

### 2. **إدارة النماذج**
- تحميل وتفريغ النماذج ديناميكيًا
- مراقبة الحالة الصحية وإجراء الفحوصات
- جمع مقاييس الأداء

### 3. **أنماط الإنتاج**
- آليات إعادة المحاولة مع التراجع الأسي
- قاطع الدائرة لتحمل الأخطاء
- تسجيل شامل ومراقبة دقيقة

### 4. **معالجة استجابات مرنة**
- استجابات متدفقة للتطبيقات في الوقت الفعلي
- معالجة دفعات للسيناريوهات ذات الإنتاجية العالية
- تحليل وتحقق مخصص للاستجابات

## أمثلة الاستخدام

### التكامل الأساسي مع API
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### التكامل المتدفق
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### مراقبة الحالة الصحية
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## هيكل الملفات

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## تكامل Microsoft Foundry Local

يتبع هذا النموذج الأنماط الرسمية لـ Microsoft:

1. **تكامل SDK**: يستخدم `FoundryLocalManager` لإدارة الخدمة
2. **نقاط النهاية REST**: استدعاءات مباشرة إلى `/v1/chat/completions` ونقاط أخرى
3. **المصادقة**: التعامل الصحيح مع مفاتيح API للخدمات المحلية
4. **إدارة النماذج**: إدراج الكتالوج، التنزيل، وأنماط التحميل
5. **معالجة الأخطاء**: رموز الأخطاء والاستجابات الموصى بها من Microsoft

## البدء

1. **تثبيت الاعتماديات**
   ```bash
   pip install -r requirements.txt
   ```

2. **تشغيل المثال الأساسي**
   ```bash
   python examples/basic_usage.py
   ```

3. **تجربة التكامل المتدفق**
   ```bash
   python examples/streaming.py
   ```

4. **إعداد الإنتاج**
   ```bash
   python examples/production.py
   ```

## التكوين

متغيرات البيئة للتخصيص:
- `FOUNDRY_MODEL`: النموذج الافتراضي للاستخدام (الافتراضي: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: مهلة الطلب بالثواني (الافتراضي: 30)
- `FOUNDRY_RETRIES`: عدد محاولات إعادة المحاولة (الافتراضي: 3)
- `FOUNDRY_LOG_LEVEL`: مستوى التسجيل (الافتراضي: "INFO")

## أفضل الممارسات

1. **إدارة الاتصال**: إعادة استخدام اتصالات HTTP لتحسين الأداء
2. **معالجة الأخطاء**: تنفيذ منطق إعادة المحاولة مع التراجع الأسي
3. **مراقبة الموارد**: تتبع استخدام ذاكرة النموذج والأداء
4. **الأمان**: استخدام المصادقة المناسبة حتى للخدمات المحلية
5. **الاختبار**: تضمين اختبارات الوحدة والاختبارات التكاملية

## استكشاف الأخطاء وإصلاحها

### المشكلات الشائعة

**الخدمة غير قيد التشغيل**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**مشكلات تحميل النموذج**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**أخطاء الاتصال**
- تحقق من تشغيل Foundry Local على المنفذ الصحيح
- تحقق من إعدادات جدار الحماية
- تأكد من وجود رؤوس المصادقة الصحيحة

## تحسين الأداء

1. **تجميع الاتصالات**: استخدام كائنات الجلسة للطلبات المتعددة
2. **العمليات غير المتزامنة**: الاستفادة من asyncio للطلبات المتزامنة
3. **التخزين المؤقت**: تخزين استجابات النموذج حيثما كان ذلك مناسبًا
4. **المراقبة**: تتبع أوقات الاستجابة وضبط المهلات

## نتائج التعلم

بعد إكمال هذا النموذج، ستفهم:
- التكامل المباشر مع REST API لـ Foundry Local
- أنماط تنفيذ عميل HTTP مخصص
- معالجة الأخطاء والمراقبة الجاهزة للإنتاج
- هيكلية خدمة Microsoft Foundry Local
- تقنيات تحسين الأداء لخدمات الذكاء الاصطناعي المحلية

## الخطوات التالية

- استكشاف النموذج 08: تطبيق الدردشة لنظام Windows 11
- تجربة النموذج 09: تنسيق الوكلاء المتعددين
- تعلم النموذج 10: Foundry Local كتكامل أدوات

---

