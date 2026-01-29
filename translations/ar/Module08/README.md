# الوحدة 08: العمل العملي مع Microsoft Foundry Local - مجموعة أدوات المطور الكاملة

## نظرة عامة

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) يمثل الجيل القادم من تطوير الذكاء الاصطناعي على الحافة، حيث يوفر للمطورين أدوات قوية لبناء وتوزيع وتوسيع تطبيقات الذكاء الاصطناعي محليًا مع الحفاظ على تكامل سلس مع Azure AI Foundry. تقدم هذه الوحدة تغطية شاملة لـ Foundry Local بدءًا من التثبيت وصولاً إلى تطوير الوكلاء المتقدم.

**التقنيات الرئيسية:**
- Microsoft Foundry Local CLI و SDK
- تكامل Azure AI Foundry
- استنتاج النماذج على الجهاز
- تخزين وتحسين النماذج محليًا
- بنى تعتمد على الوكلاء

## أهداف التعلم

عند إكمال هذه الوحدة، ستتمكن من:

- **إتقان Foundry Local**: تثبيت، تكوين، وتحسين التطوير على Windows 11
- **توزيع نماذج متنوعة**: تشغيل نماذج phi، qwen، deepseek، و GPT محليًا باستخدام أوامر CLI
- **بناء حلول إنتاجية**: إنشاء تطبيقات ذكاء اصطناعي باستخدام هندسة متقدمة للمطالبات ودمج البيانات
- **الاستفادة من النظام المفتوح المصدر**: دمج نماذج Hugging Face ومساهمات المجتمع
- **تطوير وكلاء ذكاء اصطناعي**: بناء وكلاء ذكيين بقدرات التأسيس والتنظيم
- **تنفيذ أنماط المؤسسات**: إنشاء حلول ذكاء اصطناعي معيارية وقابلة للتوسع للتوزيع الإنتاجي

## هيكل الجلسة

### [1: البدء مع Foundry Local](./01.FoundryLocalSetup.md)
**التركيز**: التثبيت، إعداد CLI، توزيع النماذج، وتحسين الأجهزة

**المواضيع الرئيسية**: التثبيت الكامل • أوامر CLI • تخزين النماذج • تسريع الأجهزة • توزيع نماذج متعددة

**العينة**: [البدء السريع للدردشة REST](./samples/01/README.md) • [تكامل OpenAI SDK](./samples/02/README.md) • [اكتشاف النماذج ومعايير الأداء](./samples/03/README.md)

**المدة**: 2-3 ساعات | **المستوى**: مبتدئ

---

### [2: بناء حلول ذكاء اصطناعي مع Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**التركيز**: هندسة المطالبات المتقدمة، دمج البيانات، والاتصال السحابي

**المواضيع الرئيسية**: هندسة المطالبات • دمج البيانات • سير العمل في Azure • تحسين الأداء • المراقبة

**العينة**: [تطبيق Chainlit RAG](./samples/04/README.md)

**المدة**: 2-3 ساعات | **المستوى**: متوسط

---

### [3: نماذج مفتوحة المصدر في Foundry Local](./03.OpenSourceModels.md)
**التركيز**: تكامل Hugging Face، استراتيجيات BYOM، ونماذج المجتمع

**المواضيع الرئيسية**: تكامل HuggingFace • جلب النموذج الخاص بك • رؤى Model Mondays • مساهمات المجتمع • اختيار النماذج

**العينة**: [تنظيم الوكلاء المتعددين](./samples/05/README.md)

**المدة**: 2-3 ساعات | **المستوى**: متوسط

---

### [4: استكشاف النماذج المتقدمة](./04.CuttingEdgeModels.md)
**التركيز**: مقارنة LLMs و SLMs، تنفيذ EdgeAI، والعروض التوضيحية المتقدمة

**المواضيع الرئيسية**: مقارنة النماذج • استنتاج الحافة مقابل السحابة • Phi + ONNX Runtime • تطبيق Chainlit RAG • تحسين WebGPU

**العينة**: [موجه النماذج كأدوات](./samples/06/README.md)

**المدة**: 3-4 ساعات | **المستوى**: متقدم

---

### [5: بناء وكلاء ذكاء اصطناعي بسرعة](./05.AIPoweredAgents.md)
**التركيز**: بنى الوكلاء، مطالبات النظام، التأسيس، والتنظيم

**المواضيع الرئيسية**: أنماط تصميم الوكلاء • هندسة مطالبات النظام • تقنيات التأسيس • أنظمة الوكلاء المتعددة • التوزيع الإنتاجي

**العينة**: [تنظيم الوكلاء المتعددين](./samples/05/README.md) • [نظام الوكلاء المتعدد المتقدم](./samples/09/README.md)

**المدة**: 3-4 ساعات | **المستوى**: متقدم

---

### [6: Foundry Local - النماذج كأدوات](./06.ModelsAsTools.md)
**التركيز**: حلول ذكاء اصطناعي معيارية، التوسع المؤسسي، وأنماط الإنتاج

**المواضيع الرئيسية**: النماذج كأدوات • التوزيع على الجهاز • تكامل SDK/API • بنى المؤسسات • استراتيجيات التوسع

**العينة**: [موجه النماذج كأدوات](./samples/06/README.md) • [إطار أدوات Foundry](./samples/10/README.md)

**المدة**: 3-4 ساعات | **المستوى**: خبير

---

### [7: أنماط تكامل API المباشر](./samples/07/README.md)
**التركيز**: تكامل REST API النقي بدون اعتماد على SDK لتحقيق أقصى قدر من التحكم

**المواضيع الرئيسية**: تنفيذ عميل HTTP • المصادقة المخصصة • مراقبة صحة النموذج • استجابات البث • معالجة الأخطاء الإنتاجية

**العينة**: [عميل API المباشر](./samples/07/README.md)

**المدة**: 2-3 ساعات | **المستوى**: متوسط

---

### [8: تطبيق دردشة أصلي على Windows 11](./samples/08/README.md)
**التركيز**: بناء تطبيقات دردشة حديثة مع تكامل Foundry Local

**المواضيع الرئيسية**: تطوير Electron • نظام التصميم Fluent • تكامل Windows الأصلي • البث في الوقت الحقيقي • تصميم واجهة الدردشة

**العينة**: [تطبيق دردشة Windows 11](./samples/08/README.md)

**المدة**: 3-4 ساعات | **المستوى**: متقدم

---

### [9: تنظيم الوكلاء المتعدد المتقدم](./samples/09/README.md)
**التركيز**: تنسيق الوكلاء المتقدم، تفويض المهام المتخصصة، وسير العمل التعاوني للذكاء الاصطناعي

**المواضيع الرئيسية**: تنسيق الوكلاء الذكي • أنماط استدعاء الوظائف • التواصل بين الوكلاء • تنظيم سير العمل • آليات ضمان الجودة

**العينة**: [نظام الوكلاء المتعدد المتقدم](./samples/09/README.md)

**المدة**: 4-5 ساعات | **المستوى**: خبير

---

### [10: Foundry Local كإطار أدوات](./samples/10/README.md)
**التركيز**: بنية تعتمد على الأدوات لتكامل Foundry Local مع التطبيقات والأطر الحالية

**المواضيع الرئيسية**: تكامل LangChain • وظائف Semantic Kernel • أطر REST API • أدوات CLI • تكامل Jupyter • أنماط التوزيع الإنتاجي

**العينة**: [إطار أدوات Foundry](./samples/10/README.md)

**المدة**: 4-5 ساعات | **المستوى**: خبير

## المتطلبات الأساسية

### متطلبات النظام
- **نظام التشغيل**: Windows 11 (22H2 أو أحدث)
- **الذاكرة**: 16GB RAM (32GB موصى بها للنماذج الأكبر)
- **التخزين**: 50GB مساحة خالية لتخزين النماذج
- **الأجهزة**: جهاز يدعم NPU موصى به (Copilot+ PC)، GPU اختياري
- **الشبكة**: إنترنت عالي السرعة لتنزيل النماذج الأولية

### بيئة التطوير
- Visual Studio Code مع امتداد AI Toolkit
- Python 3.10+ و pip
- Git للتحكم في الإصدارات
- PowerShell أو Command Prompt
- Azure CLI (اختياري للتكامل السحابي)

### المعرفة الأساسية المطلوبة
- فهم أساسي لمفاهيم الذكاء الاصطناعي/التعلم الآلي
- الإلمام بسطر الأوامر
- أساسيات برمجة Python
- مفاهيم REST API
- معرفة أساسية بالمطالبات واستنتاج النماذج

## الجدول الزمني للوحدة

**الوقت الإجمالي المقدر**: 30-38 ساعة

| الجلسة | مجال التركيز | العينات | الوقت | التعقيد |
|---------|------------|---------|------|------------|
|  1 | الإعداد والأساسيات | 01، 02، 03 | 2-3 ساعات | مبتدئ |
|  2 | حلول الذكاء الاصطناعي | 04 | 2-3 ساعات | متوسط |
|  3 | المصدر المفتوح | 05 | 2-3 ساعات | متوسط |
|  4 | النماذج المتقدمة | 06 | 3-4 ساعات | متقدم |
|  5 | وكلاء الذكاء الاصطناعي | 05، 09 | 3-4 ساعات | متقدم |
|  6 | أدوات المؤسسات | 06، 10 | 3-4 ساعات | خبير |
|  7 | تكامل API المباشر | 07 | 2-3 ساعات | متوسط |
|  8 | تطبيق دردشة Windows 11 | 08 | 3-4 ساعات | متقدم |
|  9 | تنظيم الوكلاء المتعدد | 09 | 4-5 ساعات | خبير |
| 10 | إطار الأدوات | 10 | 4-5 ساعات | خبير |

## الموارد الرئيسية

**التوثيق الرسمي:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - الكود المصدر والعينات الرسمية
- [توثيق Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - دليل الإعداد والاستخدام الكامل
- [سلسلة Model Mondays](https://aka.ms/model-mondays) - أبرز النماذج الأسبوعية والدروس التعليمية

**المجتمع والدعم:**
- [مناقشات Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - أسئلة وأجوبة المجتمع وطلبات الميزات
- [مجتمع مطوري Microsoft AI](https://techcommunity.microsoft.com/category/artificialintelligence) - أحدث الأخبار وأفضل الممارسات

## نتائج التعلم

عند إكمال هذه الوحدة، ستكون مجهزًا لـ:

### الإتقان الفني
- **التوزيع والإدارة**: تثبيت وإدارة Foundry Local عبر بيئات التطوير والإنتاج
- **دمج النماذج**: العمل بسلاسة مع عائلات النماذج المتنوعة من Microsoft، Hugging Face، ومصادر المجتمع
- **بناء التطبيقات**: إنشاء تطبيقات ذكاء اصطناعي جاهزة للإنتاج بميزات وتحسينات متقدمة
- **تطوير الوكلاء**: تنفيذ وكلاء ذكاء اصطناعي متقدمين بقدرات التأسيس، التفكير، وتكامل الأدوات

### الفهم الاستراتيجي
- **قرارات البنية**: اتخاذ خيارات مستنيرة بين التوزيع المحلي مقابل السحابي
- **تحسين الأداء**: تحسين أداء الاستنتاج عبر تكوينات الأجهزة المختلفة
- **التوسع المؤسسي**: تصميم تطبيقات تتوسع من النماذج الأولية المحلية إلى التوزيعات المؤسسية
- **الخصوصية والأمان**: تنفيذ حلول ذكاء اصطناعي تحافظ على الخصوصية مع الاستنتاج المحلي

### قدرات الابتكار
- **النماذج الأولية السريعة**: بناء واختبار مفاهيم تطبيقات الذكاء الاصطناعي بسرعة عبر جميع أنماط العينات العشرة
- **تكامل المجتمع**: الاستفادة من النماذج مفتوحة المصدر والمساهمة في النظام البيئي
- **أنماط متقدمة**: تنفيذ أنماط ذكاء اصطناعي متقدمة بما في ذلك RAG، الوكلاء، وتكامل الأدوات
- **إتقان الأطر**: التكامل على مستوى الخبراء مع LangChain، Semantic Kernel، Chainlit، و Electron
- **التوزيع الإنتاجي**: توزيع حلول ذكاء اصطناعي قابلة للتوسع من النماذج الأولية المحلية إلى الأنظمة المؤسسية
- **التطوير المستقبلي**: بناء تطبيقات جاهزة للتقنيات والأنماط الناشئة في الذكاء الاصطناعي

## البدء

1. **إعداد البيئة**: تأكد من وجود Windows 11 مع الأجهزة الموصى بها (راجع المتطلبات الأساسية)
2. **تثبيت Foundry Local**: اتبع الجلسة 1 للتثبيت والتكوين الكامل
3. **تشغيل العينة 01**: ابدأ بتكامل REST API الأساسي للتحقق من الإعداد
4. **التقدم عبر العينات**: أكمل العينات 01-10 لتحقيق الإتقان الشامل

## مقاييس النجاح

تتبع تقدمك عبر جميع العينات العشرة الشاملة:

### مستوى الأساس (العينات 01-03)
- [ ] تثبيت وتكوين Foundry Local بنجاح
- [ ] إكمال تكامل REST API (العينة 01)
- [ ] تنفيذ توافق OpenAI SDK (العينة 02)
- [ ] إجراء اكتشاف النماذج ومعايير الأداء (العينة 03)

### مستوى التطبيق (العينات 04-06)
- [ ] توزيع وتشغيل ما لا يقل عن 4 عائلات نماذج مختلفة
- [ ] بناء تطبيق دردشة RAG وظيفي (العينة 04)
- [ ] إنشاء نظام تنظيم الوكلاء المتعدد (العينة 05)
- [ ] تنفيذ توجيه النماذج الذكي (العينة 06)

### مستوى التكامل المتقدم (العينات 07-10)
- [ ] بناء عميل API جاهز للإنتاج (العينة 07)
- [ ] تطوير تطبيق دردشة أصلي على Windows 11 (العينة 08)
- [ ] تنفيذ نظام وكلاء متعدد متقدم (العينة 09)
- [ ] إنشاء إطار أدوات شامل (العينة 10)

### مؤشرات الإتقان
- [ ] تشغيل جميع العينات العشرة بنجاح دون أخطاء
- [ ] تخصيص ما لا يقل عن 3 عينات لحالات استخدام محددة
- [ ] توزيع أكثر من عينتين في بيئات مشابهة للإنتاج
- [ ] المساهمة بتحسينات أو إضافات إلى كود العينات
- [ ] دمج أنماط Foundry Local في المشاريع الشخصية/المهنية

## دليل البدء السريع - جميع العينات العشرة

### إعداد البيئة (مطلوب لجميع العينات)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### عينات الأساس الأساسية (01-06)

**العينة 01: البدء السريع للدردشة REST**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**العينة 02: تكامل OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**العينة 03: اكتشاف النماذج ومعايير الأداء**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**العينة 04: تطبيق Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**العينة 05: تنظيم الوكلاء المتعددين**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**العينة 06: موجه النماذج كأدوات**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### عينات التكامل المتقدم (07-10)

**العينة 07: عميل API المباشر**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**العينة 08: تطبيق دردشة Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**العينة 09: نظام الوكلاء المتعدد المتقدم**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**العينة 10: إطار أدوات Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### استكشاف الأخطاء الشائعة وإصلاحها

**أخطاء اتصال Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**مشاكل تحميل النماذج**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**مشاكل التبعيات**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## الملخص
يمثل هذا الوحدة أحدث ما توصلت إليه تقنيات الذكاء الاصطناعي الطرفي، حيث تجمع بين أدوات مايكروسوفت ذات المستوى المؤسسي ومرونة وابتكار النظام المفتوح المصدر. من خلال إتقان Foundry Local عبر جميع العينات العشر الشاملة، ستكون في طليعة تطوير تطبيقات الذكاء الاصطناعي.

**مسار التعلم الكامل:**
- **الأساسيات** (العينات 01-03): تكامل API وإدارة النماذج
- **التطبيقات** (العينات 04-06): RAG، الوكلاء، والتوجيه الذكي
- **المتقدم** (العينات 07-10): أطر العمل الإنتاجية والتكامل المؤسسي

لدمج Azure OpenAI (الجلسة 2)، يرجى الرجوع إلى ملفات README الخاصة بكل عينة للحصول على المتغيرات البيئية المطلوبة وإعدادات إصدار API.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.