# အခန်း ၀၇ : EdgeAI နမူနာများ

Edge AI သည် အတန်းမြင့် ဉာဏ်ရည်တုကို edge computing နှင့် ပေါင်းစပ်ထားသော နည်းပညာဖြစ်ပြီး၊ cloud ချိတ်ဆက်မှုမရှိဘဲ စက်ပစ္စည်းပေါ်တွင် တိုက်ရိုက် အဆင့်မြင့် အချက်အလက်များကို ဆောင်ရွက်နိုင်စေသည်။ ဤအခန်းတွင် အခြားအခြားသော ပလက်ဖောင်းများနှင့် framework များပေါ်တွင် EdgeAI ကို အကောင်အထည်ဖော်ထားသော နမူနာ ၅ ခုကို လေ့လာမည်ဖြစ်ပြီး၊ AI မော်ဒယ်များကို edge တွင် အကောင်အထည်ဖော်နိုင်စေရန်ရှိသော အခွင့်အလမ်းများနှင့် စွမ်းရည်များကို ပြသထားသည်။

## ၁။ NVIDIA Jetson Orin Nano တွင် EdgeAI

NVIDIA Jetson Orin Nano သည် edge AI computing အတွက် အရေးပါသော တိုးတက်မှုတစ်ခုဖြစ်ပြီး၊ 67 TOPS အထိ AI စွမ်းဆောင်ရည်ကို credit-card အရွယ်အစားဖြင့် ပေးစွမ်းနိုင်သည်။ ဤစွမ်းဆောင်ရည်မြင့် edge AI ပလက်ဖောင်းသည် hobbyists, ကျောင်းသားများနှင့် professional developers များအတွက် generative AI ဖွံ့ဖြိုးတိုးတက်မှုကို ပိုမိုလွယ်ကူစေသည်။

### အဓိက အင်္ဂါရပ်များ
- 67 TOPS အထိ AI စွမ်းဆောင်ရည်ကို ပေးစွမ်းနိုင်ခြင်း—ယခင်မော်ဒယ်ထက် 1.7X တိုးတက်မှု
- AI ဆောင်ရွက်မှုအတွက် 1024 CUDA cores နှင့် 32 Tensor Cores အထိ
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU (1.5 GHz အမြင့်ဆုံး frequency)
- $249 သာရှိသော စျေးနှုန်းဖြင့် developer, ကျောင်းသားများနှင့် maker များအတွက် အလွယ်တကူရရှိနိုင်သော ပလက်ဖောင်း

### အသုံးချမှုများ
Jetson Orin Nano သည် vision transformers, large language models, vision-language models အပါအဝင် ယနေ့ခေတ် generative AI မော်ဒယ်များကို အကောင်းဆုံး ဆောင်ရွက်နိုင်သည်။ GenAI အသုံးချမှုများအတွက် အထူးဒီဇိုင်းပြုလုပ်ထားပြီး၊ palm device ပေါ်တွင် LLM များစွာကို အလွယ်တကူ run လို့ရနိုင်ပါပြီ။ အသုံးချမှုများတွင် AI-powered robotics, smart drones, intelligent cameras, autonomous edge devices အပါအဝင် အများအပြားပါဝင်သည်။

**ပိုမိုလေ့လာရန်**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## ၂။ .NET MAUI နှင့် ONNX Runtime GenAI ဖြင့် Mobile Applications တွင် EdgeAI

ဤနည်းလမ်းသည် Generative AI နှင့် Large Language Models (LLMs) ကို .NET MAUI (Multi-platform App UI) နှင့် ONNX Runtime GenAI ကို အသုံးပြု၍ cross-platform mobile applications တွင် ပေါင်းစပ်ထားပုံကို ပြသသည်။ ဤနည်းလမ်းသည် Android နှင့် iOS စက်ပစ္စည်းများပေါ်တွင် native အနေဖြင့် run လို့ရသော AI-powered mobile applications များကို ဖန်တီးရန် .NET developer များအတွက် အခွင့်အလမ်းပေးသည်။

### အဓိက အင်္ဂါရပ်များ
- .NET MAUI framework ပေါ်တွင် တည်ဆောက်ထားပြီး၊ Android နှင့် iOS applications များအတွက် single codebase ပေးစွမ်း
- ONNX Runtime GenAI ပေါင်းစပ်မှုသည် mobile devices ပေါ်တွင် generative AI မော်ဒယ်များကို run လို့ရစေသည်
- CPU, GPU နှင့် mobile AI processors အထူးပြု hardware accelerators များကို ပံ့ပိုး
- ONNX Runtime မှတဆင့် iOS အတွက် CoreML နှင့် Android အတွက် NNAPI ကဲ့သို့သော platform-specific optimizations
- Generative AI loop အပြည့်အစုံကို ဆောင်ရွက်နိုင်ခြင်း (pre/post processing, inference, logits processing, search and sampling, KV cache management အပါအဝင်)

### ဖွံ့ဖြိုးတိုးတက်မှု အကျိုးကျေးဇူးများ
.NET MAUI နည်းလမ်းသည် developer များကို C# နှင့် .NET ကျွမ်းကျင်မှုများကို အသုံးပြု၍ cross-platform AI applications များကို ဖန်တီးနိုင်စေသည်။ ONNX Runtime GenAI framework သည် Llama, Mistral, Phi, Gemma အပါအဝင် မော်ဒယ် architecture များစွာကို ပံ့ပိုးသည်။ Optimized ARM64 kernels သည် INT4 quantized matrix multiplication ကို မြန်ဆန်စွာ ဆောင်ရွက်နိုင်စေပြီး၊ mobile hardware ပေါ်တွင် စွမ်းဆောင်ရည်မြင့်စွာ ဆောင်ရွက်နိုင်စေသည်။

### အသုံးချမှုများ
ဤနည်းလမ်းသည် .NET နည်းပညာများကို အသုံးပြု၍ AI-powered mobile applications များကို ဖန်တီးလိုသော developer များအတွက် အထူးသင့်လျော်သည်။ intelligent chatbots, image recognition apps, language translation tools, personalized recommendation systems ကဲ့သို့သော applications များကို privacy မြင့်မားပြီး offline အနေဖြင့် run လို့ရစေသည်။

**ပိုမိုလေ့လာရန်**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## ၃။ Azure EdgeAI နှင့် Small Language Models Engine

Microsoft ၏ Azure-based EdgeAI နည်းလမ်းသည် Small Language Models (SLMs) များကို cloud-edge hybrid ပတ်ဝန်းကျင်များတွင် ထိရောက်စွာ deploy လုပ်နိုင်ရန် အာရုံစိုက်ထားသည်။ ဤနည်းလမ်းသည် cloud-scale AI services နှင့် edge deployment လိုအပ်ချက်များအကြား ချိတ်ဆက်မှုကို ပံ့ပိုးသည်။

### Architecture အကျိုးကျေးဇူးများ
- Azure AI services နှင့် seamless integration
- ONNX Runtime ဖြင့် SLMs/LLMs နှင့် multi-modal models များကို စက်ပစ္စည်းပေါ်တွင်နှင့် cloud တွင် run လို့ရ
- Enterprise-scale deployment အတွက် optimize လုပ်ထား
- မော်ဒယ်များကို ဆက်လက် update နှင့် စီမံခန့်ခွဲမှုကို ပံ့ပိုး

### အသုံးချမှုများ
Azure EdgeAI implementation သည် enterprise-grade AI deployment ကို cloud management capabilities ဖြင့် ပံ့ပိုးရန် အထူးသင့်လျော်သည်။ intelligent document processing, real-time analytics, hybrid AI workflows ကဲ့သို့သော အသုံးချမှုများတွင် cloud နှင့် edge computing resources ကို ပေါင်းစပ်အသုံးပြုသည်။

**ပိုမိုလေ့လာရန်**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [၄။ Windows ML ဖြင့် EdgeAI](./windowdeveloper.md)

Windows ML သည် Microsoft ၏ cutting-edge runtime ဖြစ်ပြီး၊ on-device model inference ကို ထိရောက်စွာ ဆောင်ရွက်နိုင်စေသည်။ Windows AI Foundry ၏ အခြေခံအနေဖြင့် AI-powered Windows applications များကို ဖန်တီးရန် developer များအတွက် အခွင့်အလမ်းပေးသည်။

### Platform စွမ်းရည်များ
- Windows 11 PCs (version 24H2 build 26100) အထက်ရှိသော PCs များတွင် အလုပ်လုပ်နိုင်
- x64 နှင့် ARM64 PC hardware အားလုံးတွင် အလုပ်လုပ်နိုင်၊ NPU/GPU မရှိသော PCs များတွင်ပါ အလုပ်လုပ်နိုင်
- Developer များကို မော်ဒယ်များကို ကိုယ်တိုင် ယူဆောင်လာပြီး၊ AMD, Intel, NVIDIA, Qualcomm စသည်တို့၏ silicon partner ecosystem အတွင်း အလွယ်တကူ deploy လုပ်နိုင်စေသည်
- Infrastructure APIs ကို အသုံးပြု၍ silicon မတူကွဲပြားမှုများအတွက် app build များစွာ ဖန်တီးရန် မလိုအပ်တော့

### Developer အကျိုးကျေးဇူးများ
Windows ML သည် hardware နှင့် execution providers ကို abstract လုပ်ထားပြီး၊ developer များကို ကိုယ်ပိုင် code ရေးသားရန် အာရုံစိုက်နိုင်စေသည်။ Windows ML သည် NPU, GPU, CPU များကို အဆင့်မြှင့်တင်ပြီး၊ AI development အတွက် Windows hardware ecosystem အတွင်း unified framework ကို ပံ့ပိုးသည်။

**ပိုမိုလေ့လာရန်**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Windows Edge AI ဖွံ့ဖြိုးတိုးတက်မှုအတွက် လမ်းညွှန်ချက်

## [၅။ Foundry Local Applications ဖြင့် EdgeAI](./foundrylocal.md)

Foundry Local သည် Windows နှင့် Mac developer များကို Retrieval Augmented Generation (RAG) applications များကို .NET ဖြင့် local resources အသုံးပြု၍ ဖန်တီးနိုင်စေသည်။ ဤနည်းလမ်းသည် local language models နှင့် semantic search capabilities ကို ပေါင်းစပ်ထားပြီး privacy အထူးပြု AI ဖြေရှင်းချက်များကို ပံ့ပိုးသည်။

### Technical Architecture
- Phi language model, Local Embeddings, Semantic Kernel ကို ပေါင်းစပ်ထားပြီး RAG scenario ဖန်တီး
- Embeddings ကို floating-point values (vectors) အဖြစ် အသုံးပြု၍ content နှင့် semantic meaning ကို ကိုယ်စားပြု
- Semantic Kernel သည် Phi နှင့် Smart Components ကို ပေါင်းစပ်ထားပြီး seamless RAG pipeline ဖန်တီး
- SQLite နှင့် Qdrant ကဲ့သို့သော local vector databases များကို ပံ့ပိုး

### Implementation အကျိုးကျေးဇူးများ
RAG သည် "အချက်အလက်များကို ရှာဖွေပြီး prompt ထဲသို့ ထည့်ခြင်း" ကို ရိုးရှင်းစွာ ဆိုလိုသည်။ ဤ local implementation သည် data privacy ကို အထူးပြုထားပြီး၊ custom knowledge bases အပေါ် အခြေခံထားသော intelligent responses ကို ပေးစွမ်းသည်။ ဤနည်းလမ်းသည် data sovereignty နှင့် offline operation capabilities လိုအပ်သော enterprise scenarios များအတွက် အထူးသင့်လျော်သည်။

**ပိုမိုလေ့လာရန်**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local သည် ONNX Runtime powered OpenAI-compatible REST server ကို Windows ပေါ်တွင် local မော်ဒယ်များ run လုပ်ရန် ပံ့ပိုးသည်။ အောက်တွင် validated အကျဉ်းချုပ်ကို ဖော်ပြထားပြီး၊ အပြည့်အစုံကို official docs တွင် ကြည့်ရှုနိုင်သည်။

- စတင်အသုံးပြုရန်: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- ဤ repo တွင် Windows guide အပြည့်အစုံ: [foundrylocal.md](./foundrylocal.md)

Windows (cmd.exe) တွင် install သို့မဟုတ် upgrade:
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI categories ကို explore:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

မော်ဒယ် run လုပ်ပြီး dynamic endpoint ကို ရှာဖွေ:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

REST check ကို models list လုပ်ရန် (status မှ PORT ကို အစားထိုးပါ):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- ကိုယ်ပိုင်မော်ဒယ် (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Development Resources

Windows platform ကို အထူးပစ်မှတ်ထားသော developer များအတွက် Windows EdgeAI ecosystem အပြည့်အစုံကို ဖော်ပြထားသော လမ်းညွှန်ချက်ကို ဖန်တီးထားသည်။ ဤ resource သည် Windows AI Foundry အပါအဝင် EdgeAI ဖွံ့ဖြိုးတိုးတက်မှုအတွက် APIs, tools, best practices များကို အသေးစိတ်ဖော်ပြထားသည်။

### Windows AI Foundry Platform
Windows AI Foundry platform သည် Windows စက်ပစ္စည်းများပေါ်တွင် Edge AI ဖွံ့ဖြိုးတိုးတက်မှုအတွက် အထူးဒီဇိုင်းပြုလုပ်ထားသော tools နှင့် APIs များကို ပေးစွမ်းသည်။ NPU-accelerated hardware, Windows ML integration, platform-specific optimization techniques အပါအဝင် အထူးပံ့ပိုးမှုများပါဝင်သည်။

**Comprehensive Guide**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

ဤလမ်းညွှန်ချက်တွင် ပါဝင်သည်-
- Windows AI Foundry platform overview နှင့် components
- NPU hardware ပေါ်တွင် ထိရောက်စွာ inference ဆောင်ရွက်ရန် Phi Silica API
- Computer Vision APIs (image processing နှင့် OCR)
- Windows ML runtime integration နှင့် optimization
- Foundry Local CLI (local development နှင့် testing)
- Windows devices အတွက် hardware optimization strategies
- Practical implementation examples နှင့် best practices

### [AI Toolkit for Edge AI Development](./aitoolkit.md)
Visual Studio Code ကို အသုံးပြုသော developer များအတွက် AI Toolkit extension သည် Edge AI applications များကို ဖန်တီး, စမ်းသပ်, deploy လုပ်ရန် အထူးဒီဇိုင်းပြုလုပ်ထားသော development environment ကို ပေးစွမ်းသည်။ ဤ toolkit သည် Edge AI development workflow အားလုံးကို VS Code အတွင်း streamline လုပ်ပေးသည်။

**Development Guide**: [AI Toolkit for Edge AI Development](./aitoolkit.md)

AI Toolkit လမ်းညွှန်ချက်တွင် ပါဝင်သည်-
- Edge deployment အတွက် မော်ဒယ် ရှာဖွေမှုနှင့် ရွေးချယ်မှု
- Local testing နှင့် optimization workflows
- Edge မော်ဒယ်များအတွက် ONNX နှင့် Ollama integration
- မော်ဒယ် conversion နှင့် quantization techniques
- Edge scenarios အတွက် agent development
- စွမ်းဆောင်ရည် အကဲဖြတ်မှုနှင့် monitoring
- Deployment ပြင်ဆင်မှုနှင့် best practices

## နိဂုံး

ဤ EdgeAI implementations ၅ ခုသည် ယနေ့ခေတ် Edge AI ဖြေရှင်းချက်များ၏ အဆင့်မြင့်မှုနှင့် အမျိုးမျိုးသောမျိုးစုံကို ပြသသည်။ Jetson Orin Nano ကဲ့သို့ hardware-accelerated edge devices မှ ONNX Runtime GenAI နှင့် Windows ML ကဲ့သို့ software frameworks အထိ၊ developer များအတွက် edge တွင် intelligent applications များကို deploy လုပ်ရန် မတူကွဲပြားသော အခွင့်အလမ်းများကို ပေးစွမ်းသည်။

ဤ platform များအားလုံးတွင် AI စွမ်းရည်များကို democratize လုပ်ထားခြင်းသည်共通အချက်ဖြစ်ပြီး၊ developer များအတွက် skill level များနှင့် use case များအမျိုးမျိုးအတွက် sophisticated machine learning ကို လွယ်ကူစွာ အသုံးပြုနိုင်စေသည်။ Mobile applications, desktop software, embedded systems များကို ဖန်တီးခြင်းဖြင့်၊ EdgeAI solutions များသည် edge တွင် ထိရောက်စွာနှင့် privacy အထူးပြု intelligent applications များကို ဖန်တီးရန် အခြေခံအနေဖြင့် ပံ့ပိုးသည်။

Jetson Orin Nano သည် hardware-accelerated edge computing အတွက် အထူးသင့်လျော်ပြီး၊ ONNX Runtime GenAI သည် cross-platform mobile development အတွက် အထူးသင့်လျော်သည်။ Azure EdgeAI သည် enterprise cloud-edge integration အတွက် အထူးသင့်လျော်ပြီး၊ Windows ML သည် Windows-native applications အတွက် အထူးသင့်လျော်သည်။ Foundry Local သည် privacy-focused RAG implementations အတွက် အထူးသင့်လျော်သည်။ ဤ platform များသည် EdgeAI development အတွက် comprehensive ecosystem ကို ဖော်ဆောင်ပေးသည်။

[Next AI Toolkit](aitoolkit.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။