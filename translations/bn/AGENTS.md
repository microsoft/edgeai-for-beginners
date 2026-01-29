# AGENTS.md

> **শুরু করার জন্য EdgeAI-এ অবদান রাখার জন্য ডেভেলপার গাইড**
> 
> এই ডকুমেন্টটি এই রিপোজিটরির সাথে কাজ করা ডেভেলপার, AI এজেন্ট এবং অবদানকারীদের জন্য বিস্তারিত তথ্য প্রদান করে। এটি সেটআপ, ডেভেলপমেন্ট ওয়ার্কফ্লো, টেস্টিং এবং সেরা অনুশীলনগুলি কভার করে।
> 
> **সর্বশেষ আপডেট**: ৩০ অক্টোবর, ২০২৫ | **ডকুমেন্ট ভার্সন**: ৩.০

## সূচিপত্র

- [প্রকল্পের সংক্ষিপ্ত বিবরণ](../..)
- [রিপোজিটরি কাঠামো](../..)
- [প্রয়োজনীয়তা](../..)
- [সেটআপ কমান্ড](../..)
- [ডেভেলপমেন্ট ওয়ার্কফ্লো](../..)
- [টেস্টিং নির্দেশনা](../..)
- [কোড স্টাইল নির্দেশিকা](../..)
- [পুল রিকোয়েস্ট নির্দেশিকা](../..)
- [অনুবাদ ব্যবস্থা](../..)
- [Foundry Local ইন্টিগ্রেশন](../..)
- [বিল্ড এবং ডিপ্লয়মেন্ট](../..)
- [সাধারণ সমস্যা এবং সমাধান](../..)
- [অতিরিক্ত সম্পদ](../..)
- [প্রকল্প-নির্দিষ্ট নোট](../..)
- [সহায়তা পাওয়া](../..)

## প্রকল্পের সংক্ষিপ্ত বিবরণ

EdgeAI for Beginners একটি ব্যাপক শিক্ষামূলক রিপোজিটরি যা ছোট ভাষার মডেল (SLMs) ব্যবহার করে Edge AI ডেভেলপমেন্ট শেখায়। এই কোর্সটি EdgeAI এর মৌলিক বিষয়, মডেল ডিপ্লয়মেন্ট, অপ্টিমাইজেশন কৌশল এবং Microsoft Foundry Local এবং বিভিন্ন AI ফ্রেমওয়ার্ক ব্যবহার করে প্রোডাকশন-রেডি ইমপ্লিমেন্টেশন কভার করে।

**মূল প্রযুক্তি:**
- Python 3.8+ (AI/ML নমুনার জন্য প্রধান ভাষা)
- .NET C# (AI/ML নমুনা)
- JavaScript/Node.js with Electron (ডেস্কটপ অ্যাপ্লিকেশনের জন্য)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ফ্রেমওয়ার্ক: LangChain, Semantic Kernel, Chainlit
- মডেল অপ্টিমাইজেশন: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**রিপোজিটরি টাইপ:** ৮টি মডিউল এবং ১০টি ব্যাপক নমুনা অ্যাপ্লিকেশন সহ শিক্ষামূলক কন্টেন্ট রিপোজিটরি

**আর্কিটেকচার:** মাল্টি-মডিউল লার্নিং পাথ যা Edge AI ডিপ্লয়মেন্ট প্যাটার্ন প্রদর্শন করে

## রিপোজিটরি কাঠামো

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## প্রয়োজনীয়তা

### প্রয়োজনীয় টুলস

- **Python 3.8+** - AI/ML নমুনা এবং নোটবুকের জন্য
- **Node.js 16+** - Electron নমুনা অ্যাপ্লিকেশনের জন্য
- **Git** - ভার্সন কন্ট্রোলের জন্য
- **Microsoft Foundry Local** - AI মডেল স্থানীয়ভাবে চালানোর জন্য

### সুপারিশকৃত টুলস

- **Visual Studio Code** - Python, Jupyter, এবং Pylance এক্সটেনশন সহ
- **Windows Terminal** - উন্নত কমান্ড-লাইন অভিজ্ঞতার জন্য (Windows ব্যবহারকারীদের জন্য)
- **Docker** - কন্টেইনারাইজড ডেভেলপমেন্টের জন্য (ঐচ্ছিক)

### সিস্টেমের প্রয়োজনীয়তা

- **RAM**: ন্যূনতম ৮GB, মাল্টি-মডেল পরিস্থিতির জন্য ১৬GB+ সুপারিশকৃত
- **স্টোরেজ**: মডেল এবং ডিপেন্ডেন্সির জন্য ১০GB+ ফ্রি স্পেস
- **OS**: Windows 10/11, macOS 11+, অথবা Linux (Ubuntu 20.04+)
- **হার্ডওয়্যার**: AVX2 সাপোর্ট সহ CPU; GPU (CUDA, Qualcomm NPU) ঐচ্ছিক কিন্তু সুপারিশকৃত

### জ্ঞানের প্রয়োজনীয়তা

- Python প্রোগ্রামিংয়ের মৌলিক ধারণা
- কমান্ড-লাইন ইন্টারফেসের সাথে পরিচিতি
- AI/ML ধারণা বোঝা (নমুনা ডেভেলপমেন্টের জন্য)
- Git ওয়ার্কফ্লো এবং পুল রিকোয়েস্ট প্রক্রিয়া

## সেটআপ কমান্ড

### রিপোজিটরি সেটআপ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python নমুনা সেটআপ (Module08 এবং Workshop নমুনা)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.js নমুনা সেটআপ (Sample 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local সেটআপ

Foundry Local নমুনাগুলি চালানোর জন্য প্রয়োজন। অফিসিয়াল রিপোজিটরি থেকে ডাউনলোড এবং ইনস্টল করুন:

**ইনস্টলেশন:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **ম্যানুয়াল**: [releases page](https://github.com/microsoft/Foundry-Local/releases) থেকে ডাউনলোড করুন

**দ্রুত শুরু:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**নোট**: Foundry Local স্বয়ংক্রিয়ভাবে আপনার হার্ডওয়্যারের জন্য সেরা মডেল ভ্যারিয়েন্ট নির্বাচন করে (CUDA GPU, Qualcomm NPU, অথবা CPU)।

## ডেভেলপমেন্ট ওয়ার্কফ্লো

### কন্টেন্ট ডেভেলপমেন্ট

এই রিপোজিটরিতে প্রধানত **Markdown শিক্ষামূলক কন্টেন্ট** রয়েছে। পরিবর্তন করার সময়:

1. সংশ্লিষ্ট মডিউল ডিরেক্টরিতে `.md` ফাইল সম্পাদনা করুন
2. বিদ্যমান ফরম্যাটিং প্যাটার্ন অনুসরণ করুন
3. কোড উদাহরণগুলি সঠিক এবং পরীক্ষিত কিনা নিশ্চিত করুন
4. প্রয়োজন হলে সংশ্লিষ্ট অনুবাদিত কন্টেন্ট আপডেট করুন (অথবা অটোমেশনকে এটি করতে দিন)

### নমুনা অ্যাপ্লিকেশন ডেভেলপমেন্ট

Module08 Python নমুনার জন্য (নমুনা ০১-০৭, ০৯-১০):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python নমুনার জন্য:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron নমুনার জন্য (নমুনা ০৮):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### নমুনা অ্যাপ্লিকেশন টেস্টিং

Python নমুনাগুলির কোনো অটোমেটেড টেস্ট নেই তবে সেগুলি চালিয়ে যাচাই করা যেতে পারে:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron নমুনার টেস্ট ইন্সট্রাকচার রয়েছে:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## টেস্টিং নির্দেশনা

### কন্টেন্ট যাচাইকরণ

রিপোজিটরি অটোমেটেড অনুবাদ ওয়ার্কফ্লো ব্যবহার করে। অনুবাদের জন্য কোনো ম্যানুয়াল টেস্টিং প্রয়োজন নেই।

**ম্যানুয়াল যাচাইকরণ কন্টেন্ট পরিবর্তনের জন্য:**
1. `.md` ফাইলগুলি প্রিভিউ করে Markdown রেন্ডারিং পর্যালোচনা করুন
2. নিশ্চিত করুন যে সমস্ত লিঙ্ক বৈধ টার্গেটে নির্দেশ করে
3. ডকুমেন্টেশনে অন্তর্ভুক্ত কোড স্নিপেটগুলি পরীক্ষা করুন
4. নিশ্চিত করুন যে ইমেজগুলি সঠিকভাবে লোড হচ্ছে

### নমুনা অ্যাপ্লিকেশন টেস্টিং

**Module08/samples/08 (Electron অ্যাপ) এর ব্যাপক টেস্টিং রয়েছে:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python নমুনাগুলি ম্যানুয়ালি পরীক্ষা করা উচিত:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## কোড স্টাইল নির্দেশিকা

### Markdown কন্টেন্ট

- ধারাবাহিক শিরোনাম হায়ারার্কি ব্যবহার করুন (# শিরোনামের জন্য, ## প্রধান সেকশন, ### উপ-সেকশন)
- ভাষার স্পেসিফায়ার সহ কোড ব্লক অন্তর্ভুক্ত করুন: ```python, ```bash, ```javascript
- টেবিল, তালিকা এবং জোর দেওয়ার জন্য বিদ্যমান ফরম্যাটিং অনুসরণ করুন
- লাইনগুলি পড়ার যোগ্য রাখুন (~৮০-১০০ অক্ষর লক্ষ্য করুন, তবে কঠোর নয়)
- অভ্যন্তরীণ রেফারেন্সের জন্য আপেক্ষিক লিঙ্ক ব্যবহার করুন

### Python কোড স্টাইল

- PEP 8 কনভেনশন অনুসরণ করুন
- প্রয়োজন হলে টাইপ হিন্ট ব্যবহার করুন
- ফাংশন এবং ক্লাসের জন্য ডকস্ট্রিং অন্তর্ভুক্ত করুন
- অর্থপূর্ণ ভেরিয়েবল নাম ব্যবহার করুন
- ফাংশনগুলি ফোকাসড এবং সংক্ষিপ্ত রাখুন

### JavaScript/Node.js কোড স্টাইল

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**মূল কনভেনশন:**
- নমুনা ০৮-এ প্রদত্ত ESLint কনফিগারেশন
- কোড ফরম্যাটিংয়ের জন্য Prettier ব্যবহার করুন
- আধুনিক ES6+ সিনট্যাক্স ব্যবহার করুন
- কোডবেসে বিদ্যমান প্যাটার্ন অনুসরণ করুন

## পুল রিকোয়েস্ট নির্দেশিকা

### অবদান রাখার ওয়ার্কফ্লো

1. **রিপোজিটরি ফর্ক করুন** এবং `main` থেকে একটি নতুন ব্রাঞ্চ তৈরি করুন
2. **আপনার পরিবর্তনগুলি করুন** কোড স্টাইল নির্দেশিকা অনুসরণ করে
3. **ভালোভাবে পরীক্ষা করুন** উপরের টেস্টিং নির্দেশনা ব্যবহার করে
4. **স্পষ্ট বার্তা সহ কমিট করুন** কনভেনশনাল কমিট ফরম্যাট অনুসরণ করে
5. **আপনার ফর্কে পুশ করুন** এবং একটি পুল রিকোয়েস্ট তৈরি করুন
6. **পর্যালোচনার সময় মেইনটেইনারদের প্রতিক্রিয়া দিন**

### ব্রাঞ্চ নামকরণের কনভেনশন

- `feature/<module>-<description>` - নতুন ফিচার বা কন্টেন্টের জন্য
- `fix/<module>-<description>` - বাগ সংশোধনের জন্য
- `docs/<description>` - ডকুমেন্টেশন উন্নতির জন্য
- `refactor/<description>` - কোড পুনর্গঠনের জন্য

### কমিট বার্তা ফরম্যাট

[Conventional Commits](https://www.conventionalcommits.org/) অনুসরণ করুন:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**উদাহরণ:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### শিরোনাম ফরম্যাট
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### আচরণবিধি

সমস্ত অবদানকারীকে [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) অনুসরণ করতে হবে। অবদান রাখার আগে [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) পর্যালোচনা করুন।

### জমা দেওয়ার আগে

**কন্টেন্ট পরিবর্তনের জন্য:**
- সমস্ত পরিবর্তিত Markdown ফাইল প্রিভিউ করুন
- লিঙ্ক এবং ইমেজ কাজ করছে কিনা যাচাই করুন
- টাইপো এবং ব্যাকরণগত ত্রুটি পরীক্ষা করুন

**নমুনা কোড পরিবর্তনের জন্য (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python নমুনা পরিবর্তনের জন্য:**
- নিশ্চিত করুন যে নমুনাটি সফলভাবে চলছে
- ত্রুটি পরিচালনা কাজ করছে কিনা যাচাই করুন
- Foundry Local এর সাথে সামঞ্জস্য পরীক্ষা করুন

### পর্যালোচনা প্রক্রিয়া

- শিক্ষামূলক কন্টেন্ট পরিবর্তনগুলি সঠিকতা এবং স্পষ্টতার জন্য পর্যালোচনা করা হয়
- কোড নমুনাগুলি কার্যকারিতার জন্য পরীক্ষা করা হয়
- অনুবাদ আপডেটগুলি GitHub Actions দ্বারা স্বয়ংক্রিয়ভাবে পরিচালিত হয়

## অনুবাদ ব্যবস্থা

**গুরুত্বপূর্ণ:** এই রিপোজিটরি GitHub Actions এর মাধ্যমে অটোমেটেড অনুবাদ ব্যবহার করে।

- অনুবাদগুলি `/translations/` ডিরেক্টরিতে রয়েছে (৫০+ ভাষা)
- `co-op-translator.yml` ওয়ার্কফ্লো দ্বারা অটোমেটেড
- **অনুবাদ ফাইলগুলি ম্যানুয়ালি সম্পাদনা করবেন না** - সেগুলি ওভাররাইট করা হবে
- শুধুমাত্র মূল ইংরেজি সোর্স ফাইলগুলি সম্পাদনা করুন রুট এবং মডিউল ডিরেক্টরিতে
- `main` ব্রাঞ্চে পুশ করার সময় অনুবাদগুলি স্বয়ংক্রিয়ভাবে তৈরি হয়

## Foundry Local ইন্টিগ্রেশন

Module08 এর বেশিরভাগ নমুনার জন্য Microsoft Foundry Local চালু থাকা প্রয়োজন।

### ইনস্টলেশন এবং সেটআপ

**Foundry Local ইনস্টল করুন:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK ইনস্টল করুন:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local শুরু করা
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK ব্যবহার (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local যাচাই করা
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### নমুনার জন্য পরিবেশ ভেরিয়েবল

বেশিরভাগ নমুনা এই পরিবেশ ভেরিয়েবলগুলি ব্যবহার করে:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**নোট**: `FoundryLocalManager` ব্যবহার করার সময়, SDK স্বয়ংক্রিয়ভাবে সার্ভিস ডিসকভারি এবং মডেল লোডিং পরিচালনা করে। মডেল এলিয়াস (যেমন `phi-3.5-mini`) নিশ্চিত করে যে আপনার হার্ডওয়্যারের জন্য সেরা ভ্যারিয়েন্ট নির্বাচন করা হয়েছে।

## বিল্ড এবং ডিপ্লয়মেন্ট

### কন্টেন্ট ডিপ্লয়মেন্ট

এই রিপোজিটরি প্রধানত ডকুমেন্টেশন - কন্টেন্টের জন্য কোনো বিল্ড প্রক্রিয়া প্রয়োজন নেই।

### নমুনা অ্যাপ্লিকেশন বিল্ডিং

**Electron অ্যাপ্লিকেশন (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python নমুনা:**
কোনো বিল্ড প্রক্রিয়া নেই - নমুনাগুলি সরাসরি Python ইন্টারপ্রেটার দিয়ে চালানো হয়।

## সাধারণ সমস্যা এবং সমাধান

> **টিপ**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) চেক করুন পরিচিত সমস্যা এবং সমাধানের জন্য।

### গুরুতর সমস্যা (ব্লকিং)

#### Foundry Local চালু নয়
**সমস্যা:** নমুনাগুলি সংযোগ ত্রুটির সাথে ব্যর্থ হয়

**সমাধান:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### সাধারণ সমস্যা (মাঝারি)

#### Python ভার্চুয়াল এনভায়রনমেন্ট সমস্যা
**সমস্যা:** মডিউল ইমপোর্ট ত্রুটি

**সমাধান:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron বিল্ড সমস্যা
**সমস্যা:** npm install বা বিল্ড ব্যর্থতা

**সমাধান:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ওয়ার্কফ্লো সমস্যা (মাইনর)

#### অনুবাদ ওয়ার্কফ্লো কনফ্লিক্ট
**সমস্যা:** আপনার পরিবর্তনের সাথে অনুবাদ PR কনফ্লিক্ট

**সমাধান:**
- শুধুমাত্র ইংরেজি সোর্স ফাইল সম্পাদনা করুন
- অটোমেটেড অনুবাদ ওয়ার্কফ্লোকে অনুবাদ পরিচালনা করতে দিন
- যদি কনফ্লিক্ট হয়, অনুবাদগুলি মার্জ হওয়ার পরে `main` আপনার ব্রাঞ্চে মার্জ করুন

#### মডেল ডাউনলোড ব্যর্থতা
**সমস্যা:** Foundry Local মডেল ডাউনলোড করতে ব্যর্থ হয়

**সমাধান:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## অতিরিক্ত সম্পদ

### লার্নিং পাথ
- **বিগিনার পাথ:** মডিউল ০১-০২ (৭-৯ ঘণ্টা)
- **ইন্টারমিডিয়েট পাথ:** মডিউল ০৩-০৪ (৯-১১ ঘণ্টা)
- **অ্যাডভান্সড পাথ:** মডিউল ০৫-০৭ (১২-১৫ ঘণ্টা)
- **এক্সপার্ট পাথ:** মডিউল ০৮ (৮-১০ ঘণ্টা)
- **হ্যান্ডস-অন ওয়ার্কশপ:** ওয়ার্কশপ উপকরণ (৬-৮ ঘণ্টা)

### মূল মডিউল কন্টেন্ট
- **Module01:** EdgeAI এর মৌলিক বিষয় এবং বাস্তব জীবনের কেস স্টাডি
- **Module02:** ছোট ভাষার মডেল (SLM) পরিবার এবং আর্কিটেকচার
- **Module03:** স্থানীয় এবং ক্লাউড ডিপ্লয়মেন্ট কৌশল
- **Module04:** একাধিক ফ্রেমওয়ার্ক দিয়ে মডেল অপ্টিমাইজেশন (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - প্রোডাকশন অপারেশন
- **Module06:** AI এজেন্ট এবং ফাংশন কলিং
- **Module07:** প্ল্যাটফর্ম-নির্দিষ্ট ইমপ্লিমেন্টেশন
- **Module08:** Foundry Local টুলকিট সহ ১০টি ব্যাপক নমুনা

### বাহ্যিক নির্ভরতা
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel ইন্টিগ্রেশন

### ওয়ার্কশপের নমুনা অ্যাপ্লিকেশন

ওয়ার্কশপে ৬টি প্রগতিশীল সেশন রয়েছে, যেখানে ব্যবহারিক বাস্তবায়ন দেখানো হয়েছে:

1. **সেশন ০১** - Foundry Local ইন্টিগ্রেশনের মাধ্যমে চ্যাট বুটস্ট্র্যাপ
2. **সেশন ০২** - RAG পাইপলাইন এবং RAGAS দিয়ে মূল্যায়ন
3. **সেশন ০৩** - ওপেন-সোর্স মডেলের বেঞ্চমার্কিং
4. **সেশন ০৪** - মডেল তুলনা এবং নির্বাচন
5. **সেশন ০৫** - মাল্টি-এজেন্ট অর্কেস্ট্রেশন সিস্টেম
6. **সেশন ০৬** - মডেল রাউটিং এবং পাইপলাইন ব্যবস্থাপনা

প্রতিটি নমুনা Foundry Local-এর মাধ্যমে এজ AI ডেভেলপমেন্টের বিভিন্ন দিক প্রদর্শন করে।

### পারফরম্যান্স বিবেচনা

- SLMs এজ ডিপ্লয়মেন্টের জন্য অপ্টিমাইজ করা হয়েছে (২-১৬GB RAM)
- লোকাল ইনফারেন্স ৫০-৫০০ms প্রতিক্রিয়া সময় প্রদান করে
- কোয়ান্টাইজেশন কৌশল ৭৫% সাইজ কমিয়ে ৮৫% পারফরম্যান্স ধরে রাখে
- লোকাল মডেলের মাধ্যমে রিয়েল-টাইম কথোপকথনের সক্ষমতা

### নিরাপত্তা এবং গোপনীয়তা

- সমস্ত প্রসেসিং লোকালভাবে ঘটে - কোনো ডেটা ক্লাউডে পাঠানো হয় না
- গোপনীয়তা-সংবেদনশীল অ্যাপ্লিকেশনের জন্য উপযুক্ত (স্বাস্থ্যসেবা, আর্থিক)
- ডেটা সার্বভৌমত্বের প্রয়োজনীয়তা পূরণ করে
- Foundry Local সম্পূর্ণরূপে লোকাল হার্ডওয়্যারে চলে

## সাহায্য পাওয়া

### ডকুমেন্টেশন

- **প্রধান README**: [README.md](README.md) - রিপোজিটরি ওভারভিউ এবং শেখার পথ
- **স্টাডি গাইড**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - শেখার সম্পদ এবং সময়সূচি
- **সাপোর্ট**: [SUPPORT.md](SUPPORT.md) - সাহায্য পাওয়ার উপায়
- **নিরাপত্তা**: [SECURITY.md](SECURITY.md) - নিরাপত্তা সমস্যা রিপোর্ট করা

### কমিউনিটি সাপোর্ট

- **GitHub Issues**: [বাগ রিপোর্ট করুন বা ফিচার অনুরোধ করুন](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [প্রশ্ন করুন এবং আইডিয়া শেয়ার করুন](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local-এর প্রযুক্তিগত সমস্যা](https://github.com/microsoft/Foundry-Local/issues)

### যোগাযোগ

- **মেইনটেইনারস**: দেখুন [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **নিরাপত্তা সমস্যা**: [SECURITY.md](SECURITY.md)-এ দায়িত্বশীল প্রকাশনা অনুসরণ করুন
- **Microsoft Support**: এন্টারপ্রাইজ সাপোর্টের জন্য Microsoft কাস্টমার সার্ভিসের সাথে যোগাযোগ করুন

### অতিরিক্ত সম্পদ

- **Microsoft Learn**: [AI এবং মেশিন লার্নিং শেখার পথ](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local ডকুমেন্টেশন**: [অফিশিয়াল ডকস](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **কমিউনিটি নমুনা**: কমিউনিটি কন্ট্রিবিউশন দেখতে [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) চেক করুন

---

**এটি একটি শিক্ষামূলক রিপোজিটরি যা এজ AI ডেভেলপমেন্ট শেখানোর উপর কেন্দ্রীভূত। প্রধান অবদান প্যাটার্ন হল শিক্ষামূলক বিষয়বস্তু উন্নত করা এবং এজ AI ধারণা প্রদর্শনকারী নমুনা অ্যাপ্লিকেশন যোগ করা/উন্নত করা।**

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।