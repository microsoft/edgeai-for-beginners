# Foundry Local بطور API نمونہ

یہ نمونہ دکھاتا ہے کہ Microsoft Foundry Local کو REST API سروس کے طور پر کیسے استعمال کیا جا سکتا ہے، بغیر OpenAI SDK پر انحصار کیے۔ یہ زیادہ سے زیادہ کنٹرول اور حسب ضرورت کے لیے براہ راست HTTP انضمام کے نمونے پیش کرتا ہے۔

## جائزہ

Microsoft کے سرکاری Foundry Local نمونوں کی بنیاد پر، یہ نمونہ فراہم کرتا ہے:
- FoundryLocalManager کے ساتھ براہ راست REST API انضمام
- حسب ضرورت HTTP کلائنٹ کا نفاذ
- ماڈل مینجمنٹ اور صحت کی نگرانی
- اسٹریمنگ اور غیر اسٹریمنگ ردعمل کی ہینڈلنگ
- پروڈکشن کے لیے تیار غلطی ہینڈلنگ اور دوبارہ کوشش کرنے کی منطق

## ضروریات

1. **Foundry Local انسٹالیشن**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python کی ضروریات**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## فن تعمیر

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## اہم خصوصیات

### 1. **براہ راست HTTP انضمام**
- SDK پر انحصار کیے بغیر خالص REST API کالز
- حسب ضرورت تصدیق اور ہیڈرز
- درخواست/جواب ہینڈلنگ پر مکمل کنٹرول

### 2. **ماڈل مینجمنٹ**
- متحرک ماڈل لوڈنگ اور ان لوڈنگ
- صحت کی نگرانی اور حیثیت کی جانچ
- کارکردگی میٹرکس کا مجموعہ

### 3. **پروڈکشن نمونے**
- ایکسپونینشل بیک آف کے ساتھ دوبارہ کوشش کرنے کے طریقے
- غلطی رواداری کے لیے سرکٹ بریکر
- جامع لاگنگ اور نگرانی

### 4. **لچکدار ردعمل کی ہینڈلنگ**
- حقیقی وقت کی ایپلیکیشنز کے لیے اسٹریمنگ ردعمل
- زیادہ throughput کے منظرناموں کے لیے بیچ پروسیسنگ
- حسب ضرورت ردعمل کی تجزیہ اور توثیق

## استعمال کی مثالیں

### بنیادی API انضمام
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

### اسٹریمنگ انضمام
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### صحت کی نگرانی
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## فائل کا ڈھانچہ

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

## Microsoft Foundry Local انضمام

یہ نمونہ Microsoft کے سرکاری نمونوں کی پیروی کرتا ہے:

1. **SDK انضمام**: سروس مینجمنٹ کے لیے `FoundryLocalManager` کا استعمال
2. **REST اینڈپوائنٹس**: `/v1/chat/completions` اور دیگر اینڈپوائنٹس پر براہ راست کالز
3. **تصدیق**: مقامی خدمات کے لیے مناسب API کلید ہینڈلنگ
4. **ماڈل مینجمنٹ**: کیٹلاگ لسٹنگ، ڈاؤن لوڈنگ، اور لوڈنگ کے نمونے
5. **غلطی ہینڈلنگ**: Microsoft کی تجویز کردہ غلطی کوڈز اور ردعمل

## شروعات

1. **ضروریات انسٹال کریں**
   ```bash
   pip install -r requirements.txt
   ```

2. **بنیادی مثال چلائیں**
   ```bash
   python examples/basic_usage.py
   ```

3. **اسٹریمنگ آزمائیں**
   ```bash
   python examples/streaming.py
   ```

4. **پروڈکشن سیٹ اپ**
   ```bash
   python examples/production.py
   ```

## ترتیب

حسب ضرورت کے لیے ماحول کے متغیرات:
- `FOUNDRY_MODEL`: استعمال کرنے کے لیے ڈیفالٹ ماڈل (ڈیفالٹ: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: سیکنڈز میں درخواست کا وقت ختم ہونا (ڈیفالٹ: 30)
- `FOUNDRY_RETRIES`: دوبارہ کوشش کرنے کی تعداد (ڈیفالٹ: 3)
- `FOUNDRY_LOG_LEVEL`: لاگنگ کی سطح (ڈیفالٹ: "INFO")

## بہترین طریقے

1. **کنکشن مینجمنٹ**: بہتر کارکردگی کے لیے HTTP کنکشنز کو دوبارہ استعمال کریں
2. **غلطی ہینڈلنگ**: ایکسپونینشل بیک آف کے ساتھ مناسب دوبارہ کوشش کرنے کی منطق نافذ کریں
3. **وسائل کی نگرانی**: ماڈل میموری کے استعمال اور کارکردگی کو ٹریک کریں
4. **سیکیورٹی**: مقامی خدمات کے لیے بھی مناسب تصدیق کا استعمال کریں
5. **ٹیسٹنگ**: یونٹ اور انضمام دونوں ٹیسٹ شامل کریں

## خرابیوں کا سراغ لگانا

### عام مسائل

**سروس چل نہیں رہی**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**ماڈل لوڈنگ کے مسائل**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**کنکشن کی غلطیاں**
- تصدیق کریں کہ Foundry Local صحیح پورٹ پر چل رہا ہے
- فائر وال کی ترتیبات چیک کریں
- مناسب تصدیق ہیڈرز کو یقینی بنائیں

## کارکردگی کی اصلاح

1. **کنکشن پولنگ**: متعدد درخواستوں کے لیے سیشن آبجیکٹس کا استعمال کریں
2. **ایسنک آپریشنز**: ہم وقتی درخواستوں کے لیے asyncio کا فائدہ اٹھائیں
3. **کیشنگ**: جہاں مناسب ہو ماڈل کے ردعمل کو کیش کریں
4. **نگرانی**: ردعمل کے اوقات کو ٹریک کریں اور ٹائم آؤٹس کو ایڈجسٹ کریں

## سیکھنے کے نتائج

اس نمونے کو مکمل کرنے کے بعد، آپ سمجھ جائیں گے:
- Foundry Local کے ساتھ براہ راست REST API انضمام
- حسب ضرورت HTTP کلائنٹ کے نفاذ کے نمونے
- پروڈکشن کے لیے تیار غلطی ہینڈلنگ اور نگرانی
- Microsoft Foundry Local سروس فن تعمیر
- مقامی AI خدمات کے لیے کارکردگی کی اصلاح کی تکنیکیں

## اگلے مراحل

- نمونہ 08: Windows 11 چیٹ ایپلیکیشن کو دریافت کریں
- نمونہ 09: ملٹی ایجنٹ آرکسٹریشن آزمائیں
- نمونہ 10: Foundry Local کو ٹولز انضمام کے طور پر سیکھیں

---

