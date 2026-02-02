# Foundry Local as API Sample

এই উদাহরণটি Microsoft Foundry Local-কে REST API সার্ভিস হিসেবে ব্যবহার করার পদ্ধতি প্রদর্শন করে, যেখানে OpenAI SDK-এর উপর নির্ভরতা নেই। এটি সরাসরি HTTP ইন্টিগ্রেশন প্যাটার্ন দেখায় যা সর্বোচ্চ নিয়ন্ত্রণ এবং কাস্টমাইজেশনের জন্য উপযোগী।

## সংক্ষিপ্ত বিবরণ

Microsoft-এর অফিসিয়াল Foundry Local প্যাটার্নের উপর ভিত্তি করে এই উদাহরণটি প্রদান করে:
- FoundryLocalManager-এর সাথে সরাসরি REST API ইন্টিগ্রেশন
- কাস্টম HTTP ক্লায়েন্ট ইমপ্লিমেন্টেশন
- মডেল ব্যবস্থাপনা এবং স্বাস্থ্য পর্যবেক্ষণ
- স্ট্রিমিং এবং নন-স্ট্রিমিং রেসপন্স হ্যান্ডলিং
- প্রোডাকশন-রেডি ত্রুটি পরিচালনা এবং পুনরায় চেষ্টা করার লজিক

## পূর্বশর্ত

1. **Foundry Local ইনস্টলেশন**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python ডিপেন্ডেন্সি**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## আর্কিটেকচার

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## মূল বৈশিষ্ট্য

### 1. **সরাসরি HTTP ইন্টিগ্রেশন**
- SDK নির্ভরতা ছাড়াই সম্পূর্ণ REST API কল
- কাস্টম অথেন্টিকেশন এবং হেডার
- রিকোয়েস্ট/রেসপন্স হ্যান্ডলিং-এর উপর পূর্ণ নিয়ন্ত্রণ

### 2. **মডেল ব্যবস্থাপনা**
- ডায়নামিক মডেল লোডিং এবং আনলোডিং
- স্বাস্থ্য পর্যবেক্ষণ এবং স্ট্যাটাস চেক
- পারফরম্যান্স মেট্রিক সংগ্রহ

### 3. **প্রোডাকশন প্যাটার্ন**
- এক্সপোনেনশিয়াল ব্যাকঅফ সহ পুনরায় চেষ্টা করার মেকানিজম
- ফল্ট টলারেন্সের জন্য সার্কিট ব্রেকার
- বিস্তৃত লগিং এবং পর্যবেক্ষণ

### 4. **ফ্লেক্সিবল রেসপন্স হ্যান্ডলিং**
- রিয়েল-টাইম অ্যাপ্লিকেশনের জন্য স্ট্রিমিং রেসপন্স
- উচ্চ-থ্রুপুট পরিস্থিতির জন্য ব্যাচ প্রসেসিং
- কাস্টম রেসপন্স পার্সিং এবং ভ্যালিডেশন

## ব্যবহার উদাহরণ

### বেসিক API ইন্টিগ্রেশন
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

### স্ট্রিমিং ইন্টিগ্রেশন
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### স্বাস্থ্য পর্যবেক্ষণ
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## ফাইল স্ট্রাকচার

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

## Microsoft Foundry Local ইন্টিগ্রেশন

এই উদাহরণটি Microsoft-এর অফিসিয়াল প্যাটার্ন অনুসরণ করে:

1. **SDK ইন্টিগ্রেশন**: `FoundryLocalManager` ব্যবহার করে সার্ভিস ম্যানেজমেন্ট
2. **REST এন্ডপয়েন্ট**: `/v1/chat/completions` এবং অন্যান্য এন্ডপয়েন্টে সরাসরি কল
3. **অথেন্টিকেশন**: লোকাল সার্ভিসের জন্য সঠিক API কী ব্যবস্থাপনা
4. **মডেল ব্যবস্থাপনা**: ক্যাটালগ লিস্টিং, ডাউনলোডিং এবং লোডিং প্যাটার্ন
5. **ত্রুটি পরিচালনা**: Microsoft-প্রস্তাবিত ত্রুটি কোড এবং রেসপন্স

## শুরু করার ধাপ

1. **ডিপেন্ডেন্সি ইনস্টল করুন**
   ```bash
   pip install -r requirements.txt
   ```

2. **বেসিক উদাহরণ চালান**
   ```bash
   python examples/basic_usage.py
   ```

3. **স্ট্রিমিং চেষ্টা করুন**
   ```bash
   python examples/streaming.py
   ```

4. **প্রোডাকশন সেটআপ**
   ```bash
   python examples/production.py
   ```

## কনফিগারেশন

কাস্টমাইজেশনের জন্য পরিবেশ ভেরিয়েবল:
- `FOUNDRY_MODEL`: ব্যবহারের জন্য ডিফল্ট মডেল (ডিফল্ট: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: সেকেন্ডে রিকোয়েস্ট টাইমআউট (ডিফল্ট: 30)
- `FOUNDRY_RETRIES`: পুনরায় চেষ্টা করার সংখ্যা (ডিফল্ট: 3)
- `FOUNDRY_LOG_LEVEL`: লগিং লেভেল (ডিফল্ট: "INFO")

## সেরা অনুশীলন

1. **কানেকশন ব্যবস্থাপনা**: ভালো পারফরম্যান্সের জন্য HTTP কানেকশন পুনরায় ব্যবহার করুন
2. **ত্রুটি পরিচালনা**: এক্সপোনেনশিয়াল ব্যাকঅফ সহ সঠিক পুনরায় চেষ্টা করার লজিক ইমপ্লিমেন্ট করুন
3. **রিসোর্স পর্যবেক্ষণ**: মডেলের মেমরি ব্যবহার এবং পারফরম্যান্স ট্র্যাক করুন
4. **নিরাপত্তা**: লোকাল সার্ভিসের জন্য সঠিক অথেন্টিকেশন ব্যবহার করুন
5. **পরীক্ষা**: ইউনিট এবং ইন্টিগ্রেশন টেস্ট অন্তর্ভুক্ত করুন

## সমস্যা সমাধান

### সাধারণ সমস্যা

**সার্ভিস চালু নেই**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**মডেল লোডিং সমস্যা**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**কানেকশন ত্রুটি**
- নিশ্চিত করুন Foundry Local সঠিক পোর্টে চলছে
- ফায়ারওয়াল সেটিংস চেক করুন
- সঠিক অথেন্টিকেশন হেডার নিশ্চিত করুন

## পারফরম্যান্স অপ্টিমাইজেশন

1. **কানেকশন পুলিং**: একাধিক রিকোয়েস্টের জন্য সেশন অবজেক্ট ব্যবহার করুন
2. **অ্যাসিঙ্ক অপারেশন**: একাধিক রিকোয়েস্টের জন্য asyncio ব্যবহার করুন
3. **ক্যাশিং**: যেখানে প্রয়োজন মডেল রেসপন্স ক্যাশ করুন
4. **পর্যবেক্ষণ**: রেসপন্স টাইম ট্র্যাক করুন এবং টাইমআউট অ্যাডজাস্ট করুন

## শেখার ফলাফল

এই উদাহরণ সম্পন্ন করার পরে আপনি বুঝতে পারবেন:
- Foundry Local-এর সাথে সরাসরি REST API ইন্টিগ্রেশন
- কাস্টম HTTP ক্লায়েন্ট ইমপ্লিমেন্টেশন প্যাটার্ন
- প্রোডাকশন-রেডি ত্রুটি পরিচালনা এবং পর্যবেক্ষণ
- Microsoft Foundry Local সার্ভিস আর্কিটেকচার
- লোকাল AI সার্ভিসের জন্য পারফরম্যান্স অপ্টিমাইজেশন কৌশল

## পরবর্তী ধাপ

- উদাহরণ 08: Windows 11 চ্যাট অ্যাপ্লিকেশন অন্বেষণ করুন
- উদাহরণ 09: মাল্টি-এজেন্ট অর্কেস্ট্রেশন চেষ্টা করুন
- উদাহরণ 10: Foundry Local-কে টুলস ইন্টিগ্রেশনে শিখুন

---

