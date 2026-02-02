# নমুনা ০২: OpenAI SDK ইন্টিগ্রেশন

OpenAI Python SDK-এর সাথে উন্নত ইন্টিগ্রেশন প্রদর্শন করে, যা Microsoft Foundry Local এবং Azure OpenAI উভয়কেই সমর্থন করে, স্ট্রিমিং রেসপন্স এবং সঠিক ত্রুটি পরিচালনার সাথে।

## সংক্ষিপ্ত বিবরণ

এই নমুনাটি প্রদর্শন করে:
- Foundry Local এবং Azure OpenAI-এর মধ্যে সহজে সুইচিং
- ব্যবহারকারীর অভিজ্ঞতা উন্নত করার জন্য স্ট্রিমিং চ্যাট কমপ্লিশন
- FoundryLocalManager SDK-এর সঠিক ব্যবহার
- শক্তিশালী ত্রুটি পরিচালনা এবং ব্যাকআপ ব্যবস্থা
- প্রোডাকশন-রেডি কোড প্যাটার্ন

## প্রয়োজনীয়তা

- **Foundry Local**: ইনস্টল করা এবং চালু (লোকাল ইনফারেন্সের জন্য)
- **Python**: ৩.৮ বা তার পরবর্তী সংস্করণ OpenAI SDK সহ
- **Azure OpenAI**: বৈধ এন্ডপয়েন্ট এবং API কী (ক্লাউড ইনফারেন্সের জন্য)

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

3. **Foundry Local শুরু করুন (লোকাল মোডের জন্য):**
   ```cmd
   foundry model run phi-4-mini
   ```


## ব্যবহারিক দৃশ্যপট

### Foundry Local (ডিফল্ট)

**বিকল্প ১: FoundryLocalManager ব্যবহার করে (প্রস্তাবিত)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**বিকল্প ২: ম্যানুয়াল কনফিগারেশন**
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


## কোড আর্কিটেকচার

### ক্লায়েন্ট ফ্যাক্টরি প্যাটার্ন

নমুনাটি উপযুক্ত ক্লায়েন্ট তৈরি করতে একটি ফ্যাক্টরি প্যাটার্ন ব্যবহার করে:

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


### স্ট্রিমিং রেসপন্স

নমুনাটি রিয়েল-টাইম রেসপন্স জেনারেশনের জন্য স্ট্রিমিং প্রদর্শন করে:

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


## পরিবেশ ভেরিয়েবল

### Foundry Local কনফিগারেশন

| ভেরিয়েবল | বিবরণ | ডিফল্ট | প্রয়োজনীয় |
|-----------|--------|--------|-------------|
| `MODEL` | ব্যবহারের জন্য মডেল এলিয়াস | `phi-4-mini` | না |
| `BASE_URL` | Foundry Local এন্ডপয়েন্ট | `http://localhost:8000` | না |
| `API_KEY` | API কী (লোকালের জন্য ঐচ্ছিক) | `""` | না |

### Azure OpenAI কনফিগারেশন

| ভেরিয়েবল | বিবরণ | ডিফল্ট | প্রয়োজনীয় |
|-----------|--------|--------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI রিসোর্স এন্ডপয়েন্ট | - | হ্যাঁ |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API কী | - | হ্যাঁ |
| `AZURE_OPENAI_API_VERSION` | API সংস্করণ | `2024-08-01-preview` | না |
| `MODEL` | Azure ডিপ্লয়মেন্ট নাম | `your-deployment-name` | হ্যাঁ |

## উন্নত বৈশিষ্ট্য

### স্বয়ংক্রিয় সার্ভিস ডিসকভারি

নমুনাটি পরিবেশ ভেরিয়েবলের উপর ভিত্তি করে উপযুক্ত সার্ভিস স্বয়ংক্রিয়ভাবে সনাক্ত করে:

1. **Azure মোড**: যদি `AZURE_OPENAI_ENDPOINT` এবং `AZURE_OPENAI_API_KEY` সেট করা থাকে
2. **Foundry SDK মোড**: যদি Foundry Local SDK উপলব্ধ থাকে
3. **ম্যানুয়াল মোড**: ম্যানুয়াল কনফিগারেশনে ব্যাকআপ

### ত্রুটি পরিচালনা

- SDK থেকে ম্যানুয়াল কনফিগারেশনে গ্রেসফুল ব্যাকআপ
- সমস্যার সমাধানের জন্য স্পষ্ট ত্রুটি বার্তা
- নেটওয়ার্ক সমস্যার জন্য সঠিক এক্সসেপশন হ্যান্ডলিং
- প্রয়োজনীয় পরিবেশ ভেরিয়েবলের বৈধতা যাচাই

## কর্মক্ষমতা বিবেচনা

### লোকাল বনাম ক্লাউড ট্রেড-অফ

**Foundry Local সুবিধা:**
- ✅ API খরচ নেই
- ✅ ডেটা গোপনীয়তা (ডেটা ডিভাইস ছেড়ে যায় না)
- ✅ সমর্থিত মডেলের জন্য কম লেটেন্সি
- ✅ অফলাইনে কাজ করে

**Azure OpenAI সুবিধা:**
- ✅ সর্বশেষ বড় মডেলগুলিতে অ্যাক্সেস
- ✅ উচ্চ থ্রুপুট
- ✅ লোকাল কম্পিউটের প্রয়োজন নেই
- ✅ এন্টারপ্রাইজ-গ্রেড SLA

## সমস্যা সমাধান

### সাধারণ সমস্যা

1. **"Foundry SDK ব্যবহার করা যায়নি" সতর্কবার্তা:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure প্রমাণীকরণ ত্রুটি:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **মডেল উপলব্ধ নয়:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### স্বাস্থ্য পরীক্ষা

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## পরবর্তী পদক্ষেপ

- **নমুনা ০৩**: মডেল ডিসকভারি এবং বেঞ্চমার্কিং
- **নমুনা ০৪**: একটি Chainlit RAG অ্যাপ্লিকেশন তৈরি করা
- **নমুনা ০৫**: মাল্টি-এজেন্ট অর্কেস্ট্রেশন
- **নমুনা ০৬**: মডেল-এজ-টুল রাউটিং

## রেফারেন্স

- [Azure OpenAI ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK রেফারেন্স](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK ডকুমেন্টেশন](https://github.com/openai/openai-python)
- [স্ট্রিমিং কমপ্লিশন গাইড](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

