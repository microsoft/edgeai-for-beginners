# نمونہ 01: اوپن اے آئی SDK کے ذریعے فوری چیٹ

ایک سادہ چیٹ کی مثال جو دکھاتی ہے کہ مائیکروسافٹ فاؤنڈری لوکل کے ساتھ اوپن اے آئی SDK کو کیسے استعمال کیا جائے۔

## جائزہ

یہ نمونہ درج ذیل چیزیں دکھاتا ہے:
- فاؤنڈری لوکل کے ساتھ اوپن اے آئی پائتھون SDK کا استعمال
- Azure OpenAI اور فاؤنڈری لوکل کنفیگریشنز کو ہینڈل کرنا
- مناسب ایرر ہینڈلنگ اور فال بیک حکمت عملیوں کو نافذ کرنا
- سروس مینجمنٹ کے لیے FoundryLocalManager کا استعمال

## ضروریات

- **فاؤنڈری لوکل**: انسٹال شدہ اور PATH پر دستیاب
- **پائتھون**: 3.8 یا اس سے جدید
- **ماڈل**: فاؤنڈری لوکل میں لوڈ شدہ ماڈل (مثلاً، `phi-4-mini`)

## انسٹالیشن

1. **پائتھون ماحول ترتیب دیں:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ضروریات انسٹال کریں:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **فاؤنڈری لوکل سروس شروع کریں اور ماڈل لوڈ کریں:**
   ```cmd
   foundry model run phi-4-mini
   ```


## استعمال

### فاؤنڈری لوکل (ڈیفالٹ)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```


### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## کوڈ کی خصوصیات

### FoundryLocalManager انٹیگریشن

نمونہ فاؤنڈری لوکل SDK کا استعمال کرتا ہے تاکہ سروس مینجمنٹ کو صحیح طریقے سے نافذ کیا جا سکے:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### ایرر ہینڈلنگ

مضبوط ایرر ہینڈلنگ کے ساتھ دستی کنفیگریشن پر فال بیک:
- خودکار سروس دریافت
- اگر SDK دستیاب نہ ہو تو گریسفل ڈیگریڈیشن
- خرابیوں کو حل کرنے کے لیے واضح ایرر میسیجز

## ماحول کے متغیرات

| متغیر | وضاحت | ڈیفالٹ | ضروری |
|-------|--------|---------|--------|
| `MODEL` | ماڈل کا عرف یا نام | `phi-4-mini` | نہیں |
| `BASE_URL` | فاؤنڈری لوکل بیس URL | `http://localhost:8000` | نہیں |
| `API_KEY` | API کلید (عام طور پر لوکل کے لیے ضروری نہیں) | `""` | نہیں |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI اینڈ پوائنٹ | - | Azure کے لیے |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API کلید | - | Azure کے لیے |
| `AZURE_OPENAI_API_VERSION` | Azure API ورژن | `2024-08-01-preview` | نہیں |

## خرابیوں کا پتہ لگانا

### عام مسائل

1. **"فاؤنڈری SDK استعمال نہیں کر سکا" انتباہ:**
   - فاؤنڈری لوکل SDK انسٹال کریں: `pip install foundry-local-sdk`
   - یا دستی کنفیگریشن کے لیے ماحول کے متغیرات سیٹ کریں

2. **کنکشن ریفیوزڈ:**
   - یقینی بنائیں کہ فاؤنڈری لوکل چل رہا ہے: `foundry service status`
   - چیک کریں کہ کوئی ماڈل لوڈ ہوا ہے: `foundry service ps`

3. **ماڈل نہیں ملا:**
   - دستیاب ماڈلز کی فہرست دیکھیں: `foundry model list`
   - ماڈل لوڈ کریں: `foundry model run phi-4-mini`

### تصدیق

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## حوالہ جات

- [فاؤنڈری لوکل دستاویزات](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [اوپن اے آئی پائتھون SDK](https://github.com/openai/openai-python)
- [فاؤنڈری لوکل گٹ ہب](https://github.com/microsoft/Foundry-Local)
- [اوپن اے آئی-کمپیٹیبل API حوالہ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

