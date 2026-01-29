# নমুনা ০১: OpenAI SDK ব্যবহার করে দ্রুত চ্যাট

Microsoft Foundry Local-এর মাধ্যমে স্থানীয় AI ইনফারেন্সের জন্য OpenAI SDK ব্যবহারের একটি সহজ চ্যাট উদাহরণ।

## সংক্ষিপ্ত বিবরণ

এই নমুনাটি দেখায় কীভাবে:
- Foundry Local-এর সাথে OpenAI Python SDK ব্যবহার করবেন
- Azure OpenAI এবং স্থানীয় Foundry কনফিগারেশন পরিচালনা করবেন
- সঠিক ত্রুটি পরিচালনা এবং ব্যাকআপ কৌশল বাস্তবায়ন করবেন
- FoundryLocalManager ব্যবহার করে পরিষেবা পরিচালনা করবেন

## প্রয়োজনীয়তা

- **Foundry Local**: ইনস্টল করা এবং PATH-এ উপলব্ধ
- **Python**: ৩.৮ বা তার পরবর্তী সংস্করণ
- **মডেল**: Foundry Local-এ লোড করা একটি মডেল (যেমন, `phi-4-mini`)

## ইনস্টলেশন

1. **Python পরিবেশ সেট আপ করুন:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ডিপেনডেন্সি ইনস্টল করুন:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local পরিষেবা শুরু করুন এবং একটি মডেল লোড করুন:**
   ```cmd
   foundry model run phi-4-mini
   ```


## ব্যবহার

### Foundry Local (ডিফল্ট)

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


## কোড বৈশিষ্ট্য

### FoundryLocalManager ইন্টিগ্রেশন

নমুনাটি সঠিক পরিষেবা পরিচালনার জন্য Foundry Local SDK ব্যবহার করে:

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


### ত্রুটি পরিচালনা

শক্তিশালী ত্রুটি পরিচালনা যা ম্যানুয়াল কনফিগারেশনে ব্যাকআপ দেয়:
- স্বয়ংক্রিয় পরিষেবা সনাক্তকরণ
- SDK অনুপলব্ধ থাকলে গ্রেসফুল ডিগ্রেডেশন
- সমস্যা সমাধানের জন্য পরিষ্কার ত্রুটি বার্তা

## পরিবেশ ভেরিয়েবল

| ভেরিয়েবল | বিবরণ | ডিফল্ট | প্রয়োজনীয় |
|-----------|--------|--------|-------------|
| `MODEL` | মডেলের উপনাম বা নাম | `phi-4-mini` | না |
| `BASE_URL` | Foundry Local বেস URL | `http://localhost:8000` | না |
| `API_KEY` | API কী (সাধারণত স্থানীয়ের জন্য প্রয়োজন হয় না) | `""` | না |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI এন্ডপয়েন্ট | - | Azure-এর জন্য |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API কী | - | Azure-এর জন্য |
| `AZURE_OPENAI_API_VERSION` | Azure API সংস্করণ | `2024-08-01-preview` | না |

## সমস্যা সমাধান

### সাধারণ সমস্যা

1. **"Foundry SDK ব্যবহার করা যায়নি" সতর্কবার্তা:**
   - Foundry Local SDK ইনস্টল করুন: `pip install foundry-local-sdk`
   - অথবা ম্যানুয়াল কনফিগারেশনের জন্য পরিবেশ ভেরিয়েবল সেট করুন

2. **সংযোগ প্রত্যাখ্যান:**
   - নিশ্চিত করুন Foundry Local চলছে: `foundry service status`
   - নিশ্চিত করুন একটি মডেল লোড করা হয়েছে: `foundry service ps`

3. **মডেল পাওয়া যায়নি:**
   - উপলব্ধ মডেল তালিকাভুক্ত করুন: `foundry model list`
   - একটি মডেল লোড করুন: `foundry model run phi-4-mini`

### যাচাই

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## রেফারেন্স

- [Foundry Local ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-সামঞ্জস্যপূর্ণ API রেফারেন্স](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

