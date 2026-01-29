# Open WebUI + Foundry Local ইন্টিগ্রেশন গাইড

এই গাইডটি দেখায় কীভাবে Open WebUI-কে Microsoft Foundry Local-এর সাথে সংযুক্ত করা যায়, যা আপনার স্থানীয় AI মডেল দ্বারা চালিত একটি পেশাদার ChatGPT-এর মতো ইন্টারফেস প্রদান করে।

## সংক্ষিপ্ত বিবরণ

Open WebUI একটি আধুনিক, ব্যবহারকারী-বান্ধব চ্যাট ইন্টারফেস প্রদান করে যা যেকোনো OpenAI-সামঞ্জস্যপূর্ণ API-তে সংযুক্ত হতে পারে। Foundry Local-এর সাথে সংযুক্ত করে আপনি পাবেন:

- **পেশাদার UI**: আধুনিক ডিজাইনের ChatGPT-এর মতো ইন্টারফেস
- **স্থানীয় গোপনীয়তা**: সমস্ত প্রসেসিং আপনার ডিভাইসে ঘটে
- **মডেল পরিবর্তন**: বিভিন্ন স্থানীয় মডেলের মধ্যে সহজে পরিবর্তন
- **কথোপকথনের ইতিহাস**: স্থায়ী চ্যাট ইতিহাস এবং প্রসঙ্গ
- **ফাইল আপলোড**: ডকুমেন্ট বিশ্লেষণ এবং ফাইল প্রসেসিং ক্ষমতা
- **কাস্টম পার্সোনা**: সিস্টেম প্রম্পট এবং ভূমিকা কাস্টমাইজেশন

## প্রয়োজনীয়তা

### প্রয়োজনীয় সফটওয়্যার

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### একটি মডেল লোড করুন

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## দ্রুত সেটআপ (প্রস্তাবিত)

### ধাপ ১: Docker দিয়ে Open WebUI চালান

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### ধাপ ২: প্রাথমিক সেটআপ

1. **ব্রাউজার খুলুন**: `http://localhost:3000`-এ যান
2. **অ্যাকাউন্ট তৈরি করুন**: অ্যাডমিন ব্যবহারকারী সেট আপ করুন (প্রথম ব্যবহারকারী অ্যাডমিন হয়ে যায়)
3. **সংযোগ যাচাই করুন**: মডেলগুলি স্বয়ংক্রিয়ভাবে ড্রপডাউনে প্রদর্শিত হওয়া উচিত

### ধাপ ৩: সংযোগ পরীক্ষা করুন

1. ড্রপডাউন থেকে আপনার মডেল নির্বাচন করুন (যেমন, "phi-4-mini")
2. একটি টেস্ট বার্তা টাইপ করুন: "হ্যালো! আপনি কি নিজেকে পরিচয় করিয়ে দিতে পারেন?"
3. আপনি আপনার স্থানীয় মডেল থেকে একটি স্ট্রিমিং প্রতিক্রিয়া দেখতে পাবেন

## উন্নত কনফিগারেশন

### পরিবেশ ভেরিয়েবল

| ভেরিয়েবল | উদ্দেশ্য | ডিফল্ট | উদাহরণ |
|-----------|----------|---------|---------|
| `OPENAI_API_BASE_URL` | Foundry Local এন্ডপয়েন্ট | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API কী (প্রয়োজনীয় কিন্তু স্থানীয়ভাবে ব্যবহৃত নয়) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | সেশন এনক্রিপশন কী | স্বয়ংক্রিয়ভাবে তৈরি | `your-secret-key` |
| `ENABLE_SIGNUP` | নতুন ব্যবহারকারী নিবন্ধন অনুমতি দিন | `True` | `False` |

### ম্যানুয়াল কনফিগারেশন (বিকল্প)

যদি পরিবেশ ভেরিয়েবল কাজ না করে, ম্যানুয়ালি কনফিগার করুন:

1. **সেটিংস খুলুন**: সেটিংস (গিয়ার আইকন) ক্লিক করুন
2. **Connections-এ যান**: Settings → Connections → OpenAI
3. **API বিবরণ সেট করুন**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (যেকোনো মান কাজ করবে)
4. **সংরক্ষণ এবং পরীক্ষা করুন**: "Save" ক্লিক করুন তারপর একটি মডেল দিয়ে পরীক্ষা করুন

### স্থায়ী ডেটা সংরক্ষণ

কথোপকথন এবং সেটিংস সংরক্ষণ করতে:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## সমস্যা সমাধান

### সংযোগ সমস্যা

**সমস্যা**: "Connection refused" বা মডেল লোড হচ্ছে না

**সমাধান**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### মডেল প্রদর্শিত হচ্ছে না

**সমস্যা**: Open WebUI ড্রপডাউনে কোনো মডেল দেখায় না

**ডিবাগিং ধাপ**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**সমাধান**: নিশ্চিত করুন মডেলটি সঠিকভাবে লোড হয়েছে:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker নেটওয়ার্ক সমস্যা

**সমস্যা**: `host.docker.internal` সমাধান হচ্ছে না

**Windows সমাধান**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**বিকল্প**: আপনার মেশিনের IP খুঁজুন:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### কর্মক্ষমতা সমস্যা

**ধীর প্রতিক্রিয়া**:
1. নিশ্চিত করুন মডেল GPU অ্যাক্সিলারেশন ব্যবহার করছে: `foundry service ps`
2. পর্যাপ্ত সিস্টেম রিসোর্স (RAM/GPU মেমরি) যাচাই করুন
3. পরীক্ষার জন্য একটি ছোট মডেল ব্যবহার করার কথা বিবেচনা করুন

**মেমরি সমস্যা**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## ব্যবহার নির্দেশিকা

### সাধারণ চ্যাট

1. **মডেল নির্বাচন করুন**: ড্রপডাউন থেকে নির্বাচন করুন (Foundry Local মডেল দেখায়)
2. **বার্তা টাইপ করুন**: নিচের টেক্সট ইনপুট ব্যবহার করুন
3. **পাঠান**: Enter চাপুন বা Send বোতাম ক্লিক করুন
4. **প্রতিক্রিয়া দেখুন**: রিয়েল-টাইমে স্ট্রিমিং প্রতিক্রিয়া দেখুন

### উন্নত বৈশিষ্ট্য

**ফাইল আপলোড**:
1. পেপারক্লিপ আইকন ক্লিক করুন
2. ডকুমেন্ট আপলোড করুন (PDF, TXT, ইত্যাদি)
3. বিষয়বস্তুর উপর প্রশ্ন করুন
4. মডেল ডকুমেন্ট বিশ্লেষণ করবে এবং উত্তর দেবে

**কাস্টম সিস্টেম প্রম্পট**:
1. Settings → Personalization
2. কাস্টম সিস্টেম প্রম্পট সেট করুন
3. একটি ধারাবাহিক AI ব্যক্তিত্ব/আচরণ তৈরি করে

**কথোপকথন ব্যবস্থাপনা**:
- **নতুন চ্যাট**: "+" ক্লিক করে নতুন কথোপকথন শুরু করুন
- **চ্যাট ইতিহাস**: সাইডবার থেকে পূর্ববর্তী কথোপকথনে প্রবেশ করুন
- **এক্সপোর্ট**: চ্যাট ইতিহাস টেক্সট/JSON হিসাবে ডাউনলোড করুন

**মডেল তুলনা**:
1. একই Open WebUI-তে একাধিক ব্রাউজার ট্যাব খুলুন
2. প্রতিটি ট্যাবে বিভিন্ন মডেল নির্বাচন করুন
3. একই প্রম্পটের প্রতিক্রিয়া তুলনা করুন

### ইন্টিগ্রেশন প্যাটার্ন

**ডেভেলপমেন্ট ওয়ার্কফ্লো**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## প্রোডাকশন ডিপ্লয়মেন্ট

### নিরাপদ সেটআপ

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### মাল্টি-ইউজার সেটআপ

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### মনিটরিং এবং লগিং

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## ক্লিনআপ

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## পরবর্তী ধাপ

### উন্নয়নের ধারণা

1. **কাস্টম মডেল**: Foundry Local-এ আপনার নিজস্ব ফাইন-টিউনড মডেল যোগ করুন
2. **API ইন্টিগ্রেশন**: Open WebUI ফাংশনের মাধ্যমে বাহ্যিক API-তে সংযোগ করুন
3. **ডকুমেন্ট প্রসেসিং**: উন্নত RAG পাইপলাইন সেট আপ করুন
4. **মাল্টি-মডাল**: ইমেজ বিশ্লেষণের জন্য ভিশন মডেল কনফিগার করুন

### স্কেলিং বিবেচনা

- **লোড ব্যালেন্সিং**: রিভার্স প্রক্সির পিছনে একাধিক Foundry Local ইনস্ট্যান্স
- **মডেল রাউটিং**: বিভিন্ন ব্যবহারের ক্ষেত্রে বিভিন্ন মডেল
- **রিসোর্স ম্যানেজমেন্ট**: একাধিক ব্যবহারকারীর জন্য GPU মেমরি অপ্টিমাইজেশন
- **ব্যাকআপ স্ট্র্যাটেজি**: কথোপকথনের ডেটা এবং কনফিগারেশনের নিয়মিত ব্যাকআপ

## রেফারেন্স

- [Open WebUI ডকুমেন্টেশন](https://docs.openwebui.com/)
- [Open WebUI GitHub রিপোজিটরি](https://github.com/open-webui/open-webui)
- [Foundry Local ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker ইনস্টলেশন গাইড](https://docs.docker.com/get-docker/)

---

