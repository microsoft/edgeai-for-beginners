# मॉड्यूल 08: Microsoft Foundry Local के साथ व्यावहारिक अनुभव - पूर्ण डेवलपर टूलकिट

## अवलोकन

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) एज AI विकास की अगली पीढ़ी का प्रतिनिधित्व करता है, जो डेवलपर्स को शक्तिशाली उपकरण प्रदान करता है ताकि वे स्थानीय स्तर पर AI एप्लिकेशन बना सकें, तैनात कर सकें और स्केल कर सकें, साथ ही Azure AI Foundry के साथ सहज एकीकरण बनाए रख सकें। यह मॉड्यूल Foundry Local की स्थापना से लेकर उन्नत एजेंट विकास तक का व्यापक कवरेज प्रदान करता है।

**मुख्य तकनीकें:**
- Microsoft Foundry Local CLI और SDK
- Azure AI Foundry एकीकरण
- ऑन-डिवाइस मॉडल इन्फरेंस
- स्थानीय मॉडल कैशिंग और ऑप्टिमाइज़ेशन
- एजेंट-आधारित आर्किटेक्चर

## सीखने के उद्देश्य

इस मॉड्यूल को पूरा करने के बाद, आप:

- **Foundry Local में महारत हासिल करेंगे**: Windows 11 विकास के लिए स्थापना, कॉन्फ़िगरेशन और अनुकूलन
- **विविध मॉडल तैनात करेंगे**: CLI कमांड के साथ phi, qwen, deepseek और GPT मॉडल को स्थानीय रूप से चलाएंगे
- **उत्पादन समाधान बनाएंगे**: उन्नत प्रॉम्प्ट इंजीनियरिंग और डेटा एकीकरण के साथ AI एप्लिकेशन बनाएंगे
- **ओपन-सोर्स इकोसिस्टम का लाभ उठाएंगे**: Hugging Face मॉडल और सामुदायिक योगदान को एकीकृत करेंगे
- **AI एजेंट विकसित करेंगे**: ग्राउंडिंग और ऑर्केस्ट्रेशन क्षमताओं के साथ बुद्धिमान एजेंट बनाएंगे
- **एंटरप्राइज़ पैटर्न लागू करेंगे**: उत्पादन तैनाती के लिए मॉड्यूलर, स्केलेबल AI समाधान बनाएंगे

## सत्र संरचना

### [1: Foundry Local के साथ शुरुआत](./01.FoundryLocalSetup.md)
**फोकस**: स्थापना, CLI सेटअप, मॉडल तैनाती, और हार्डवेयर अनुकूलन

**मुख्य विषय**: पूर्ण स्थापना • CLI कमांड • मॉडल कैशिंग • हार्डवेयर एक्सेलेरेशन • मल्टी-मॉडल तैनाती

**उदाहरण**: [REST चैट क्विकस्टार्ट](./samples/01/README.md) • [OpenAI SDK एकीकरण](./samples/02/README.md) • [मॉडल डिस्कवरी और बेंचमार्किंग](./samples/03/README.md)

**अवधि**: 2-3 घंटे | **स्तर**: शुरुआती

---

### [2: Azure AI Foundry के साथ AI समाधान बनाना](./02.AzureAIFoundryIntegration.md)
**फोकस**: उन्नत प्रॉम्प्ट इंजीनियरिंग, डेटा एकीकरण, और क्लाउड कनेक्टिविटी

**मुख्य विषय**: प्रॉम्प्ट इंजीनियरिंग • डेटा एकीकरण • Azure वर्कफ़्लो • प्रदर्शन अनुकूलन • निगरानी

**उदाहरण**: [Chainlit RAG एप्लिकेशन](./samples/04/README.md)

**अवधि**: 2-3 घंटे | **स्तर**: मध्यवर्ती

---

### [3: ओपन-सोर्स मॉडल Foundry Local](./03.OpenSourceModels.md)
**फोकस**: Hugging Face एकीकरण, BYOM रणनीतियाँ, और सामुदायिक मॉडल

**मुख्य विषय**: HuggingFace एकीकरण • अपना मॉडल लाएं • Model Mondays अंतर्दृष्टि • सामुदायिक योगदान • मॉडल चयन

**उदाहरण**: [मल्टी-एजेंट ऑर्केस्ट्रेशन](./samples/05/README.md)

**अवधि**: 2-3 घंटे | **स्तर**: मध्यवर्ती

---

### [4: अत्याधुनिक मॉडल का अन्वेषण करें](./04.CuttingEdgeModels.md)
**फोकस**: LLMs बनाम SLMs, EdgeAI कार्यान्वयन, और उन्नत डेमो

**मुख्य विषय**: मॉडल तुलना • एज बनाम क्लाउड इन्फरेंस • Phi + ONNX Runtime • Chainlit RAG ऐप • WebGPU अनुकूलन

**उदाहरण**: [Models-as-Tools Router](./samples/06/README.md)

**अवधि**: 3-4 घंटे | **स्तर**: उन्नत

---

### [5: AI-संचालित एजेंट तेजी से बनाएं](./05.AIPoweredAgents.md)
**फोकस**: एजेंट आर्किटेक्चर, सिस्टम प्रॉम्प्ट, ग्राउंडिंग, और ऑर्केस्ट्रेशन

**मुख्य विषय**: एजेंट डिज़ाइन पैटर्न • सिस्टम प्रॉम्प्ट इंजीनियरिंग • ग्राउंडिंग तकनीकें • मल्टी-एजेंट सिस्टम • उत्पादन तैनाती

**उदाहरण**: [मल्टी-एजेंट ऑर्केस्ट्रेशन](./samples/05/README.md) • [उन्नत मल्टी-एजेंट सिस्टम](./samples/09/README.md)

**अवधि**: 3-4 घंटे | **स्तर**: उन्नत

---

### [6: Foundry Local - उपकरण के रूप में मॉडल](./06.ModelsAsTools.md)
**फोकस**: मॉड्यूलर AI समाधान, एंटरप्राइज़ स्केलिंग, और उत्पादन पैटर्न

**मुख्य विषय**: उपकरण के रूप में मॉडल • ऑन-डिवाइस तैनाती • SDK/API एकीकरण • एंटरप्राइज़ आर्किटेक्चर • स्केलिंग रणनीतियाँ

**उदाहरण**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**अवधि**: 3-4 घंटे | **स्तर**: विशेषज्ञ

---

### [7: डायरेक्ट API एकीकरण पैटर्न](./samples/07/README.md)
**फोकस**: SDK निर्भरता के बिना शुद्ध REST API एकीकरण अधिकतम नियंत्रण के लिए

**मुख्य विषय**: HTTP क्लाइंट कार्यान्वयन • कस्टम प्रमाणीकरण • मॉडल स्वास्थ्य निगरानी • स्ट्रीमिंग प्रतिक्रियाएँ • उत्पादन त्रुटि हैंडलिंग

**उदाहरण**: [डायरेक्ट API क्लाइंट](./samples/07/README.md)

**अवधि**: 2-3 घंटे | **स्तर**: मध्यवर्ती

---

### [8: Windows 11 नेटिव चैट एप्लिकेशन](./samples/08/README.md)
**फोकस**: Foundry Local एकीकरण के साथ आधुनिक नेटिव चैट एप्लिकेशन बनाना

**मुख्य विषय**: Electron विकास • Fluent Design System • नेटिव Windows एकीकरण • रीयल-टाइम स्ट्रीमिंग • चैट इंटरफ़ेस डिज़ाइन

**उदाहरण**: [Windows 11 चैट एप्लिकेशन](./samples/08/README.md)

**अवधि**: 3-4 घंटे | **स्तर**: उन्नत

---

### [9: उन्नत मल्टी-एजेंट ऑर्केस्ट्रेशन](./samples/09/README.md)
**फोकस**: परिष्कृत एजेंट समन्वय, विशेष कार्य प्रतिनिधि, और सहयोगात्मक AI वर्कफ़्लो

**मुख्य विषय**: बुद्धिमान एजेंट समन्वय • फ़ंक्शन कॉलिंग पैटर्न • क्रॉस-एजेंट संचार • वर्कफ़्लो ऑर्केस्ट्रेशन • गुणवत्ता आश्वासन तंत्र

**उदाहरण**: [उन्नत मल्टी-एजेंट सिस्टम](./samples/09/README.md)

**अवधि**: 4-5 घंटे | **स्तर**: विशेषज्ञ

---

### [10: Foundry Local को उपकरण फ्रेमवर्क के रूप में उपयोग करना](./samples/10/README.md)
**फोकस**: Foundry Local को मौजूदा एप्लिकेशन और फ्रेमवर्क में एकीकृत करने के लिए टूल-फर्स्ट आर्किटेक्चर

**मुख्य विषय**: LangChain एकीकरण • Semantic Kernel फ़ंक्शन • REST API फ्रेमवर्क • CLI उपकरण • Jupyter एकीकरण • उत्पादन तैनाती पैटर्न

**उदाहरण**: [Foundry Tools Framework](./samples/10/README.md)

**अवधि**: 4-5 घंटे | **स्तर**: विशेषज्ञ

## आवश्यकताएँ

### सिस्टम आवश्यकताएँ
- **ऑपरेटिंग सिस्टम**: Windows 11 (22H2 या बाद का संस्करण)
- **मेमोरी**: 16GB RAM (बड़े मॉडल के लिए 32GB अनुशंसित)
- **स्टोरेज**: मॉडल कैशिंग के लिए 50GB खाली स्थान
- **हार्डवेयर**: NPU-सक्षम डिवाइस अनुशंसित (Copilot+ PC), GPU वैकल्पिक
- **नेटवर्क**: प्रारंभिक मॉडल डाउनलोड के लिए हाई-स्पीड इंटरनेट

### विकास पर्यावरण
- AI Toolkit एक्सटेंशन के साथ Visual Studio Code
- Python 3.10+ और pip
- संस्करण नियंत्रण के लिए Git
- PowerShell या Command Prompt
- Azure CLI (क्लाउड एकीकरण के लिए वैकल्पिक)

### ज्ञान आवश्यकताएँ
- AI/ML अवधारणाओं की बुनियादी समझ
- कमांड लाइन परिचितता
- Python प्रोग्रामिंग की मूल बातें
- REST API अवधारणाएँ
- प्रॉम्प्टिंग और मॉडल इन्फरेंस का बुनियादी ज्ञान

## मॉड्यूल टाइमलाइन

**कुल अनुमानित समय**: 30-38 घंटे

| सत्र | फोकस क्षेत्र | उदाहरण | समय | जटिलता |
|------|--------------|--------|------|---------|
|  1 | सेटअप और मूल बातें | 01, 02, 03 | 2-3 घंटे | शुरुआती |
|  2 | AI समाधान | 04 | 2-3 घंटे | मध्यवर्ती |
|  3 | ओपन सोर्स | 05 | 2-3 घंटे | मध्यवर्ती |
|  4 | उन्नत मॉडल | 06 | 3-4 घंटे | उन्नत |
|  5 | AI एजेंट | 05, 09 | 3-4 घंटे | उन्नत |
|  6 | एंटरप्राइज़ उपकरण | 06, 10 | 3-4 घंटे | विशेषज्ञ |
|  7 | डायरेक्ट API एकीकरण | 07 | 2-3 घंटे | मध्यवर्ती |
|  8 | Windows 11 चैट ऐप | 08 | 3-4 घंटे | उन्नत |
|  9 | उन्नत मल्टी-एजेंट | 09 | 4-5 घंटे | विशेषज्ञ |
| 10 | उपकरण फ्रेमवर्क | 10 | 4-5 घंटे | विशेषज्ञ |

## मुख्य संसाधन

**आधिकारिक दस्तावेज़:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - स्रोत कोड और आधिकारिक उदाहरण
- [Azure AI Foundry दस्तावेज़](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - पूर्ण सेटअप और उपयोग गाइड
- [Model Mondays सीरीज़](https://aka.ms/model-mondays) - साप्ताहिक मॉडल हाइलाइट्स और ट्यूटोरियल

**सामुदायिक और समर्थन:**
- [Foundry Local चर्चाएँ](https://github.com/microsoft/Foundry-Local/discussions) - सामुदायिक Q&A और फीचर अनुरोध
- [Microsoft AI डेवलपर समुदाय](https://techcommunity.microsoft.com/category/artificialintelligence) - नवीनतम समाचार और सर्वोत्तम प्रथाएँ

## सीखने के परिणाम

इस मॉड्यूल को पूरा करने के बाद, आप सक्षम होंगे:

### तकनीकी महारत
- **तैनात और प्रबंधित करें**: विकास और उत्पादन वातावरण में Foundry Local इंस्टॉलेशन
- **मॉडल एकीकृत करें**: Microsoft, Hugging Face, और सामुदायिक स्रोतों से विविध मॉडल परिवारों के साथ सहजता से काम करें
- **एप्लिकेशन बनाएं**: उन्नत सुविधाओं और अनुकूलन के साथ उत्पादन-तैयार AI एप्लिकेशन बनाएं
- **एजेंट विकसित करें**: ग्राउंडिंग, तर्क, और उपकरण एकीकरण के साथ परिष्कृत AI एजेंट लागू करें

### रणनीतिक समझ
- **आर्किटेक्चर निर्णय**: स्थानीय बनाम क्लाउड तैनाती के बीच सूचित विकल्प बनाएं
- **प्रदर्शन अनुकूलन**: विभिन्न हार्डवेयर कॉन्फ़िगरेशन में इन्फरेंस प्रदर्शन को अनुकूलित करें
- **एंटरप्राइज़ स्केलिंग**: स्थानीय प्रोटोटाइप से एंटरप्राइज़ तैनाती तक स्केल करने वाले एप्लिकेशन डिज़ाइन करें
- **गोपनीयता और सुरक्षा**: स्थानीय इन्फरेंस के साथ गोपनीयता-संरक्षण AI समाधान लागू करें

### नवाचार क्षमताएँ
- **तेज़ प्रोटोटाइपिंग**: सभी 10 नमूना पैटर्न में AI एप्लिकेशन अवधारणाओं को जल्दी से बनाएं और परीक्षण करें
- **सामुदायिक एकीकरण**: ओपन-सोर्स मॉडल का लाभ उठाएं और इकोसिस्टम में योगदान करें
- **उन्नत पैटर्न**: RAG, एजेंट, और उपकरण एकीकरण सहित अत्याधुनिक AI पैटर्न लागू करें
- **फ्रेमवर्क महारत**: LangChain, Semantic Kernel, Chainlit, और Electron के साथ विशेषज्ञ-स्तरीय एकीकरण
- **उत्पादन तैनाती**: स्थानीय प्रोटोटाइप से एंटरप्राइज़ सिस्टम तक स्केलेबल AI समाधान तैनात करें
- **भविष्य-तैयार विकास**: उभरती AI तकनीकों और पैटर्न के लिए तैयार एप्लिकेशन बनाएं

## शुरुआत करें

1. **पर्यावरण सेटअप**: Windows 11 को अनुशंसित हार्डवेयर के साथ सुनिश्चित करें (देखें आवश्यकताएँ)
2. **Foundry Local इंस्टॉल करें**: सत्र 1 का पालन करें पूरी स्थापना और कॉन्फ़िगरेशन के लिए
3. **नमूना 01 चलाएँ**: सेटअप सत्यापित करने के लिए बुनियादी REST API एकीकरण से शुरू करें
4. **नमूनों के माध्यम से प्रगति करें**: व्यापक महारत के लिए नमूना 01-10 पूरा करें

## सफलता मीट्रिक्स

सभी 10 व्यापक नमूनों के माध्यम से अपनी प्रगति को ट्रैक करें:

### फाउंडेशन स्तर (नमूने 01-03)
- [ ] Foundry Local को सफलतापूर्वक इंस्टॉल और कॉन्फ़िगर करें
- [ ] REST API एकीकरण पूरा करें (नमूना 01)
- [ ] OpenAI SDK संगतता लागू करें (नमूना 02)
- [ ] मॉडल डिस्कवरी और बेंचमार्किंग करें (नमूना 03)

### एप्लिकेशन स्तर (नमूने 04-06)
- [ ] कम से कम 4 विभिन्न मॉडल परिवारों को तैनात और चलाएँ
- [ ] एक कार्यात्मक RAG चैट एप्लिकेशन बनाएं (नमूना 04)
- [ ] मल्टी-एजेंट ऑर्केस्ट्रेशन सिस्टम बनाएं (नमूना 05)
- [ ] बुद्धिमान मॉडल रूटिंग लागू करें (नमूना 06)

### उन्नत एकीकरण स्तर (नमूने 07-10)
- [ ] उत्पादन-तैयार API क्लाइंट बनाएं (नमूना 07)
- [ ] Windows 11 नेटिव चैट एप्लिकेशन विकसित करें (नमूना 08)
- [ ] उन्नत मल्टी-एजेंट सिस्टम लागू करें (नमूना 09)
- [ ] व्यापक उपकरण फ्रेमवर्क बनाएं (नमूना 10)

### महारत संकेतक
- [ ] सभी 10 नमूनों को बिना त्रुटियों के सफलतापूर्वक चलाएँ
- [ ] विशिष्ट उपयोग मामलों के लिए कम से कम 3 नमूनों को अनुकूलित करें
- [ ] उत्पादन-जैसे वातावरण में 2+ नमूनों को तैनात करें
- [ ] नमूना कोड में सुधार या विस्तार में योगदान करें
- [ ] व्यक्तिगत/पेशेवर परियोजनाओं में Foundry Local पैटर्न को एकीकृत करें

## क्विक स्टार्ट गाइड - सभी 10 नमूने

### पर्यावरण सेटअप (सभी नमूनों के लिए आवश्यक)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### कोर फाउंडेशन नमूने (01-06)

**नमूना 01: REST चैट क्विकस्टार्ट**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**नमूना 02: OpenAI SDK एकीकरण**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**नमूना 03: मॉडल डिस्कवरी और बेंचमार्किंग**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**नमूना 04: Chainlit RAG एप्लिकेशन**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**नमूना 05: मल्टी-एजेंट ऑर्केस्ट्रेशन**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**नमूना 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### उन्नत एकीकरण नमूने (07-10)

**नमूना 07: डायरेक्ट API क्लाइंट**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**नमूना 08: Windows 11 चैट एप्लिकेशन**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**नमूना 09: उन्नत मल्टी-एजेंट सिस्टम**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**नमूना 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### सामान्य समस्याओं का निवारण

**Foundry Local कनेक्शन त्रुटियाँ**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**मॉडल लोडिंग समस्याएँ**
@@CODE_BLOCK
यह मॉड्यूल एज एआई विकास के सबसे उन्नत स्तर का प्रतिनिधित्व करता है, जिसमें माइक्रोसॉफ्ट के एंटरप्राइज़-ग्रेड टूल्स को ओपन-सोर्स इकोसिस्टम की लचीलापन और नवाचार के साथ जोड़ा गया है। Foundry Local के सभी 10 व्यापक नमूनों को सीखकर, आप एआई एप्लिकेशन विकास के अग्रणी स्थान पर होंगे।

**पूर्ण शिक्षण पथ:**
- **आधार** (नमूने 01-03): API एकीकरण और मॉडल प्रबंधन  
- **एप्लिकेशन** (नमूने 04-06): RAG, एजेंट्स, और इंटेलिजेंट रूटिंग  
- **उन्नत** (नमूने 07-10): उत्पादन फ्रेमवर्क और एंटरप्राइज़ एकीकरण  

Azure OpenAI एकीकरण (सत्र 2) के लिए, आवश्यक पर्यावरण वेरिएबल्स और API संस्करण सेटिंग्स के लिए व्यक्तिगत नमूने के README फाइल देखें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।