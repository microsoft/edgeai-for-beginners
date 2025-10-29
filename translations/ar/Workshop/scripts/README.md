<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T20:22:32+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "ar"
}
-->
# نصوص ورشة العمل

يحتوي هذا الدليل على نصوص الأتمتة والدعم المستخدمة للحفاظ على الجودة والاتساق عبر مواد ورشة العمل.

## المحتويات

| الملف | الغرض |
|------|-------|
| `lint_markdown_cli.py` | يتحقق من صحة أسوار الكود في Markdown لمنع أنماط أوامر Foundry Local CLI القديمة. |
| `export_benchmark_markdown.py` | يشغل اختبار قياس الأداء متعدد النماذج ويصدر تقارير Markdown + JSON. |

## 1. مدقق أنماط Markdown CLI

يقوم `lint_markdown_cli.py` بفحص جميع ملفات `.md` غير المترجمة للبحث عن أنماط Foundry Local CLI غير المسموح بها **داخل أسوار الكود** (``` ... ```). يمكن للنصوص التوضيحية أن تذكر الأوامر القديمة للسياق التاريخي.

### الأنماط القديمة (المحظورة داخل أسوار الكود)

يقوم المدقق بحظر أنماط CLI القديمة. استخدم البدائل الحديثة بدلاً منها.

### البدائل المطلوبة
| القديم | استخدم بدلاً منه |
|-------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | نص قياس الأداء + أدوات النظام (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### رموز الخروج
| الرمز | المعنى |
|-------|-------|
| 0 | لم يتم اكتشاف أي انتهاكات |
| 1 | تم العثور على نمط أو أكثر من الأنماط القديمة |

### التشغيل محليًا
من جذر المستودع (موصى به):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### خطاف ما قبل الالتزام (اختياري)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
 يمنع الالتزامات التي تقدم أنماطًا قديمة.

### تكامل CI
يقوم سير عمل GitHub Action (`.github/workflows/markdown-cli-lint.yml`) بتشغيل المدقق عند كل دفع وسحب طلب إلى الفروع `main` و `Reactor`. يجب إصلاح الوظائف الفاشلة قبل الدمج.

### إضافة أنماط قديمة جديدة
1. افتح `lint_markdown_cli.py`.
2. أضف زوجًا `(regex, suggestion)` إلى قائمة `DEPRECATED`. استخدم سلسلة خامة وقم بتضمين حدود الكلمات `\b` حيثما كان ذلك مناسبًا.
3. قم بتشغيل المدقق محليًا للتحقق من الكشف.
4. قم بالالتزام والدفع؛ سيقوم CI بفرض القاعدة الجديدة.

إضافة مثال:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### السماح بذكرات توضيحية
نظرًا لأن أسوار الكود فقط يتم فرضها، يمكنك وصف الأوامر القديمة في النص السردي بأمان. إذا كنت *تحتاج* إلى عرضها داخل سياج للتباين، أضف كتلة مسيجة **بدون** ثلاث علامات اقتباس (مثل التراجع أو الاقتباس) أو أعد كتابتها إلى شكل زائف.

### تخطي ملفات محددة (متقدم)
إذا لزم الأمر، قم بتغليف الأمثلة القديمة في ملف منفصل خارج المستودع أو أعد تسميته بامتداد مختلف أثناء الكتابة. يتم تخطي النسخ المترجمة تلقائيًا (المسارات التي تحتوي على `translations`).

### استكشاف الأخطاء وإصلاحها
| المشكلة | السبب | الحل |
|---------|-------|------|
| المدقق يحدد سطرًا قمت بتحديثه | النمط واسع جدًا | قم بتضييق النمط بإضافة حدود كلمات إضافية (`\b`) أو نقاط ارتكاز |
| فشل CI ولكن النجاح محليًا | إصدار Python مختلف أو تغييرات غير ملتزمة | أعد التشغيل محليًا، تأكد من شجرة العمل النظيفة، تحقق من إصدار Python في سير العمل (3.11) |
| الحاجة إلى تجاوز مؤقت | إصلاح عاجل | قم بتطبيق الإصلاح فورًا بعد ذلك؛ ضع في اعتبارك استخدام فرع مؤقت وطلب متابعة (تجنب إضافة مفاتيح تجاوز) |

### المبرر
الحفاظ على الوثائق متوافقة مع واجهة CLI المستقرة *الحالية* يمنع الاحتكاك في الورشة، ويتجنب ارتباك المتعلمين، ويُركز قياس الأداء من خلال نصوص Python المُحافظة بدلاً من أوامر CLI المتغيرة.

---
يتم الحفاظ عليه كجزء من سلسلة أدوات جودة الورشة. لتحسينات (مثل اقتراحات الإصلاح التلقائي أو إنشاء تقارير HTML)، افتح قضية أو قدم طلب سحب.

## 2. نص التحقق من العينات

يقوم `validate_samples.py` بالتحقق من جميع ملفات العينات Python للتأكد من صحة بناء الجملة، الواردات، والامتثال لأفضل الممارسات.

### الاستخدام
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### ما الذي يتحقق منه
- ✅ صحة بناء الجملة في Python
- ✅ وجود الواردات المطلوبة
- ✅ تنفيذ معالجة الأخطاء (وضع تفصيلي)
- ✅ استخدام تلميحات النوع (وضع تفصيلي)
- ✅ توثيق الوظائف (وضع تفصيلي)
- ✅ روابط مرجعية لـ SDK (وضع تفصيلي)

### متغيرات البيئة
- `SKIP_IMPORT_CHECK=1` - تخطي التحقق من الواردات
- `SKIP_SYNTAX_CHECK=1` - تخطي التحقق من بناء الجملة

### رموز الخروج
- `0` - جميع العينات اجتازت التحقق
- `1` - فشلت عينة أو أكثر

## 3. مشغل اختبار العينات

يقوم `test_samples.py` بتشغيل اختبارات أولية على جميع العينات للتحقق من أنها تعمل بدون أخطاء.

### الاستخدام
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### المتطلبات الأساسية
- تشغيل خدمة Foundry Local: `foundry service start`
- تحميل النماذج: `foundry model run phi-4-mini`
- تثبيت التبعيات: `pip install -r requirements.txt`

### ما الذي يختبره
- ✅ يمكن تشغيل العينة بدون أخطاء وقت التشغيل
- ✅ يتم إنشاء المخرجات المطلوبة
- ✅ معالجة الأخطاء بشكل صحيح عند الفشل
- ✅ الأداء (وقت التنفيذ)

### متغيرات البيئة
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - النموذج المستخدم للاختبار
- `TEST_TIMEOUT=30` - المهلة لكل عينة بالثواني

### الفشل المتوقع
قد تفشل بعض الاختبارات إذا لم يتم تثبيت التبعيات الاختيارية (مثل `ragas`, `sentence-transformers`). قم بالتثبيت باستخدام:
```bash
pip install sentence-transformers ragas datasets
```

### رموز الخروج
- `0` - جميع الاختبارات اجتازت
- `1` - فشل اختبار أو أكثر

## 4. مُصدر Markdown لقياس الأداء

النص: `export_benchmark_markdown.py`

يُنشئ جدول أداء قابل للتكرار لمجموعة من النماذج.

### الاستخدام
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### المخرجات
| الملف | الوصف |
|-------|-------|
| `benchmark_report.md` | جدول Markdown (المتوسط، p95، الرموز/الثانية، أول رمز اختياري) |
| `benchmark_report.json` | مصفوفة المقاييس الخام للمقارنة والتاريخ |

### الخيارات
| العلم | الوصف | الافتراضي |
|-------|-------|----------|
| `--models` | أسماء النماذج مفصولة بفواصل | (مطلوب) |
| `--prompt` | النص المستخدم في كل جولة | (مطلوب) |
| `--rounds` | الجولات لكل نموذج | 3 |
| `--output` | ملف إخراج Markdown | `benchmark_report.md` |
| `--json` | ملف إخراج JSON | `benchmark_report.json` |
| `--fail-on-empty` | خروج غير صفري إذا فشلت جميع القياسات | معطل |

متغير البيئة `BENCH_STREAM=1` يضيف قياس زمن أول رمز.

### ملاحظات
- يعيد استخدام `workshop_utils` لتوحيد إعداد النماذج والتخزين المؤقت.
- إذا تم تشغيله من دليل عمل مختلف، يحاول النص إيجاد مسارات بديلة لتحديد موقع `workshop_utils`.
- للمقارنة بين وحدات معالجة الرسومات: قم بتشغيل مرة واحدة، قم بتمكين التسريع عبر إعداد CLI، أعد التشغيل وقارن JSON.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.