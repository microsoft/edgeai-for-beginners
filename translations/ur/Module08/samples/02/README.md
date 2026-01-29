# نمونہ 02: OpenAI SDK انضمام

OpenAI Python SDK کے ساتھ جدید انضمام کو ظاہر کرتا ہے، جو Microsoft Foundry Local اور Azure OpenAI دونوں کے ساتھ اسٹریمنگ جوابات اور مناسب خرابی ہینڈلنگ کی حمایت کرتا ہے۔

## جائزہ

یہ نمونہ درج ذیل کو نمایاں کرتا ہے:
- Foundry Local اور Azure OpenAI کے درمیان آسان سوئچنگ
- بہتر صارف تجربے کے لیے اسٹریمنگ چیٹ مکملات
- FoundryLocalManager SDK کا مناسب استعمال
- مضبوط خرابی ہینڈلنگ اور بیک اپ میکانزم
- پروڈکشن کے لیے تیار کوڈ پیٹرنز

## ضروریات

- **Foundry Local**: انسٹال اور چل رہا ہو (مقامی انفرنس کے لیے)
- **Python**: 3.8 یا اس سے جدید ورژن کے ساتھ OpenAI SDK
- **Azure OpenAI**: درست اینڈ پوائنٹ اور API کلید (کلاؤڈ انفرنس کے لیے)

## تنصیب

1. **Python ماحول ترتیب دیں:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ضروریات انسٹال کریں:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local شروع کریں (مقامی موڈ کے لیے):**
   ```cmd
   foundry model run phi-4-mini
   ```


## استعمال کے منظرنامے

### Foundry Local (ڈیفالٹ)

**آپشن 1: FoundryLocalManager استعمال کریں (تجویز کردہ)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**آپشن 2: دستی ترتیب**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## کوڈ کی ساخت

### کلائنٹ فیکٹری پیٹرن

نمونہ فیکٹری پیٹرن استعمال کرتا ہے تاکہ مناسب کلائنٹس بنائے جا سکیں:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### اسٹریمنگ جوابات

نمونہ حقیقی وقت کے جواب کی تخلیق کے لیے اسٹریمنگ کو ظاہر کرتا ہے:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## ماحول متغیرات

### Foundry Local ترتیب

| متغیر | وضاحت | ڈیفالٹ | ضروری |
|-------|-------|--------|--------|
| `MODEL` | استعمال کرنے کے لیے ماڈل کا عرف | `phi-4-mini` | نہیں |
| `BASE_URL` | Foundry Local اینڈ پوائنٹ | `http://localhost:8000` | نہیں |
| `API_KEY` | API کلید (مقامی کے لیے اختیاری) | `""` | نہیں |

### Azure OpenAI ترتیب

| متغیر | وضاحت | ڈیفالٹ | ضروری |
|-------|-------|--------|--------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI ریسورس اینڈ پوائنٹ | - | ہاں |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API کلید | - | ہاں |
| `AZURE_OPENAI_API_VERSION` | API ورژن | `2024-08-01-preview` | نہیں |
| `MODEL` | Azure تعیناتی نام | `your-deployment-name` | ہاں |

## جدید خصوصیات

### خودکار سروس دریافت

نمونہ ماحول متغیرات کی بنیاد پر مناسب سروس کو خود بخود شناخت کرتا ہے:

1. **Azure موڈ**: اگر `AZURE_OPENAI_ENDPOINT` اور `AZURE_OPENAI_API_KEY` سیٹ ہیں
2. **Foundry SDK موڈ**: اگر Foundry Local SDK دستیاب ہے
3. **دستی موڈ**: دستی ترتیب پر بیک اپ

### خرابی ہینڈلنگ

- SDK سے دستی ترتیب پر ہموار بیک اپ
- خرابیوں کے حل کے لیے واضح پیغامات
- نیٹ ورک مسائل کے لیے مناسب استثنا ہینڈلنگ
- ضروری ماحول متغیرات کی توثیق

## کارکردگی کے تحفظات

### مقامی بمقابلہ کلاؤڈ فوائد

**Foundry Local فوائد:**
- ✅ کوئی API لاگت نہیں
- ✅ ڈیٹا کی رازداری (ڈیٹا ڈیوائس سے باہر نہیں جاتا)
- ✅ کم تاخیر سپورٹ شدہ ماڈلز کے لیے
- ✅ آف لائن کام کرتا ہے

**Azure OpenAI فوائد:**
- ✅ جدید بڑے ماڈلز تک رسائی
- ✅ زیادہ تھروپٹ
- ✅ کوئی مقامی کمپیوٹ کی ضرورت نہیں
- ✅ انٹرپرائز گریڈ SLA

## خرابیوں کا حل

### عام مسائل

1. **"Foundry SDK استعمال نہیں کر سکتے" انتباہ:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure تصدیق کی غلطیاں:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **ماڈل دستیاب نہیں:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### صحت کی جانچ

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## اگلے مراحل

- **نمونہ 03**: ماڈل دریافت اور بینچ مارکنگ
- **نمونہ 04**: Chainlit RAG ایپلیکیشن بنانا
- **نمونہ 05**: ملٹی ایجنٹ آرکسٹریشن
- **نمونہ 06**: ماڈلز-بطور-ٹولز روٹنگ

## حوالہ جات

- [Azure OpenAI دستاویزات](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK حوالہ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK دستاویزات](https://github.com/openai/openai-python)
- [اسٹریمنگ مکملات گائیڈ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

