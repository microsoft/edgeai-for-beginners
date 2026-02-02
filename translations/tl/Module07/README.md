# Kabanata 07: Mga Halimbawa ng EdgeAI

Ang Edge AI ay ang pagsasanib ng artificial intelligence at edge computing, na nagbibigay-daan sa matalinong pagproseso direkta sa mga device nang hindi umaasa sa koneksyon sa cloud. Ang kabanatang ito ay nagtatampok ng limang magkakaibang implementasyon ng EdgeAI sa iba't ibang platform at framework, na nagpapakita ng kakayahan at lakas ng pagpapatakbo ng AI models sa edge.

## 1. EdgeAI sa NVIDIA Jetson Orin Nano

Ang NVIDIA Jetson Orin Nano ay isang makabagong teknolohiya sa abot-kayang edge AI computing, na nagbibigay ng hanggang 67 TOPS ng AI performance sa isang compact na laki na kasing laki ng credit card. Ang makapangyarihang edge AI platform na ito ay nagbibigay-daan sa pag-develop ng generative AI para sa mga hobbyist, estudyante, at propesyonal na developer.

### Pangunahing Katangian
- Nagbibigay ng hanggang 67 TOPS ng AI performance—1.7X na mas mataas kumpara sa naunang modelo
- 1024 CUDA cores at hanggang 32 Tensor Cores para sa AI processing
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU na may maximum frequency na 1.5 GHz
- Presyo na $249 lamang, na nagbibigay sa mga developer, estudyante, at tagalikha ng pinaka-abot-kayang platform

### Mga Aplikasyon
Ang Jetson Orin Nano ay mahusay sa pagpapatakbo ng modernong generative AI models tulad ng vision transformers, large language models, at vision-language models. Ito ay partikular na idinisenyo para sa mga GenAI use cases, at maaari nang magpatakbo ng ilang LLMs sa isang maliit na device. Ang mga popular na aplikasyon ay kinabibilangan ng AI-powered robotics, smart drones, intelligent cameras, at autonomous edge devices.

**Matuto Pa**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI sa Mobile Applications gamit ang .NET MAUI at ONNX Runtime GenAI

Ang solusyong ito ay nagpapakita kung paano isama ang Generative AI at Large Language Models (LLMs) sa cross-platform mobile applications gamit ang .NET MAUI (Multi-platform App UI) at ONNX Runtime GenAI. Ang approach na ito ay nagbibigay-daan sa mga .NET developer na gumawa ng advanced na AI-powered mobile applications na tumatakbo nang natively sa Android at iOS devices.

### Pangunahing Katangian
- Batay sa .NET MAUI framework, na nagbibigay ng isang codebase para sa parehong Android at iOS applications
- ONNX Runtime GenAI integration na nagbibigay-daan sa pagpapatakbo ng generative AI models direkta sa mobile devices
- Sinusuportahan ang iba't ibang hardware accelerators na angkop para sa mobile devices, kabilang ang CPU, GPU, at mga espesyal na mobile AI processors
- Platform-specific optimizations tulad ng CoreML para sa iOS at NNAPI para sa Android sa pamamagitan ng ONNX Runtime
- Nagpapatupad ng kumpletong generative AI loop kabilang ang pre at post processing, inference, logits processing, search at sampling, at KV cache management

### Mga Benepisyo sa Pag-develop
Ang .NET MAUI approach ay nagbibigay-daan sa mga developer na gamitin ang kanilang kasalukuyang C# at .NET skills habang gumagawa ng cross-platform AI applications. Ang ONNX Runtime GenAI framework ay sumusuporta sa iba't ibang model architectures kabilang ang Llama, Mistral, Phi, Gemma, at marami pang iba. Ang optimized ARM64 kernels ay nagpapabilis sa INT4 quantized matrix multiplication, na tinitiyak ang mahusay na performance sa mobile hardware habang pinapanatili ang pamilyar na .NET development experience.

### Mga Aplikasyon
Ang solusyong ito ay perpekto para sa mga developer na nais gumawa ng AI-powered mobile applications gamit ang .NET technologies, kabilang ang intelligent chatbots, image recognition apps, language translation tools, at personalized recommendation systems na tumatakbo nang buo sa device para sa mas mataas na privacy at offline capability.

**Matuto Pa**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI sa Azure gamit ang Small Language Models Engine

Ang Azure-based EdgeAI solution ng Microsoft ay nakatuon sa mahusay na pag-deploy ng Small Language Models (SLMs) sa cloud-edge hybrid environments. Ang approach na ito ay nagtataguyod ng tulay sa pagitan ng cloud-scale AI services at mga pangangailangan sa edge deployment.

### Mga Bentahe ng Arkitektura
- Seamless integration sa Azure AI services
- Pagpapatakbo ng SLMs/LLMs at multi-modal models sa device at sa cloud gamit ang ONNX Runtime
- Na-optimize para sa enterprise-scale deployment
- Suporta para sa tuloy-tuloy na pag-update at pamamahala ng modelo

### Mga Aplikasyon
Ang Azure EdgeAI implementation ay mahusay sa mga senaryo na nangangailangan ng enterprise-grade AI deployment na may cloud management capabilities. Kasama dito ang intelligent document processing, real-time analytics, at hybrid AI workflows na gumagamit ng parehong cloud at edge computing resources.

**Matuto Pa**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI gamit ang Windows ML](./windowdeveloper.md)

Ang Windows ML ay kumakatawan sa cutting-edge runtime ng Microsoft na na-optimize para sa performant on-device model inference at pinasimpleng deployment, na nagsisilbing pundasyon ng Windows AI Foundry. Ang platform na ito ay nagbibigay-daan sa mga developer na gumawa ng AI-powered Windows applications na gumagamit ng buong spectrum ng PC hardware.

### Mga Kakayahan ng Platform
- Gumagana sa lahat ng Windows 11 PCs na may bersyon 24H2 (build 26100) o mas mataas
- Gumagana sa lahat ng x64 at ARM64 PC hardware, kahit sa mga PC na walang NPUs o GPUs
- Nagbibigay-daan sa mga developer na magdala ng kanilang sariling mga modelo at i-deploy ang mga ito nang mahusay sa ecosystem ng silicon partner kabilang ang AMD, Intel, NVIDIA, at Qualcomm na sumasaklaw sa CPU, GPU, NPU
- Sa paggamit ng infrastructure APIs, hindi na kailangang gumawa ng maraming build ng app para i-target ang iba't ibang silicon

### Mga Benepisyo sa Developer
Ang Windows ML ay nag-aabstract ng hardware at execution providers, kaya maaari kang mag-focus sa pagsusulat ng iyong code. Bukod pa rito, ang Windows ML ay awtomatikong nag-a-update upang suportahan ang pinakabagong NPUs, GPUs, at CPUs habang inilalabas ang mga ito. Ang platform ay nagbibigay ng unified framework para sa AI development sa iba't ibang Windows hardware ecosystem.

**Matuto Pa**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Komprehensibong gabay para sa Windows Edge AI development

## [5. EdgeAI gamit ang Foundry Local Applications](./foundrylocal.md)

Ang Foundry Local ay nagbibigay-daan sa mga Windows at Mac developer na gumawa ng Retrieval Augmented Generation (RAG) applications gamit ang lokal na resources sa .NET, na pinagsasama ang local language models sa semantic search capabilities. Ang approach na ito ay nagbibigay ng privacy-focused AI solutions na gumagana nang buo sa lokal na infrastructure.

### Arkitektura ng Teknolohiya
- Pinagsasama ang Phi language model, Local Embeddings, at Semantic Kernel upang lumikha ng RAG scenario
- Gumagamit ng embeddings bilang vectors (arrays) ng floating-point values na kumakatawan sa content at semantic meaning nito
- Ang Semantic Kernel ang pangunahing tagapag-ayos, na nag-iintegrate ng Phi at Smart Components upang lumikha ng seamless RAG pipeline
- Suporta para sa lokal na vector databases kabilang ang SQLite at Qdrant

### Mga Benepisyo sa Implementasyon
Ang RAG, o Retrieval Augmented Generation, ay simpleng paraan ng pagsasabi ng "maghanap ng impormasyon at isama ito sa prompt". Ang lokal na implementasyon na ito ay tinitiyak ang data privacy habang nagbibigay ng matalinong sagot na nakabatay sa custom knowledge bases. Ang approach na ito ay partikular na mahalaga para sa mga enterprise scenarios na nangangailangan ng data sovereignty at offline operation capabilities.

**Matuto Pa**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Ang Microsoft Foundry Local ay nagbibigay ng OpenAI‑compatible REST server na pinapagana ng ONNX Runtime para sa pagpapatakbo ng mga modelo nang lokal sa Windows. Narito ang mabilis na validated summary; tingnan ang opisyal na dokumentasyon para sa buong detalye.

- Simulan: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Buong Windows guide sa repo na ito: [foundrylocal.md](./foundrylocal.md)

I-install o i-upgrade sa Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

I-explore ang mga kategorya ng CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Magpatakbo ng modelo at tuklasin ang dynamic endpoint:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Mabilis na REST check para ilista ang mga modelo (palitan ang PORT mula sa status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Mga Tips:
- SDK integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Magdala ng sariling modelo (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Mga Resources sa Windows EdgeAI Development

Para sa mga developer na partikular na nagta-target sa Windows platform, gumawa kami ng komprehensibong gabay na sumasaklaw sa buong Windows EdgeAI ecosystem. Ang resource na ito ay nagbibigay ng detalyadong impormasyon tungkol sa Windows AI Foundry, kabilang ang APIs, tools, at best practices para sa EdgeAI development sa Windows.

### Windows AI Foundry Platform
Ang Windows AI Foundry platform ay nagbibigay ng komprehensibong suite ng tools at APIs na partikular na idinisenyo para sa Edge AI development sa Windows devices. Kasama dito ang espesyal na suporta para sa NPU-accelerated hardware, Windows ML integration, at platform-specific optimization techniques.

**Komprehensibong Gabay**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Ang gabay na ito ay sumasaklaw sa:
- Windows AI Foundry platform overview at components
- Phi Silica API para sa efficient inference sa NPU hardware
- Computer Vision APIs para sa image processing at OCR
- Windows ML runtime integration at optimization
- Foundry Local CLI para sa lokal na development at testing
- Mga estratehiya sa hardware optimization para sa Windows devices
- Mga praktikal na halimbawa ng implementasyon at best practices

### [AI Toolkit para sa Edge AI Development](./aitoolkit.md)
Para sa mga developer na gumagamit ng Visual Studio Code, ang AI Toolkit extension ay nagbibigay ng komprehensibong development environment na partikular na idinisenyo para sa paggawa, testing, at pag-deploy ng Edge AI applications. Ang toolkit na ito ay pinadadali ang buong Edge AI development workflow sa loob ng VS Code.

**Development Guide**: [AI Toolkit para sa Edge AI Development](./aitoolkit.md)

Ang AI Toolkit guide ay sumasaklaw sa:
- Model discovery at selection para sa edge deployment
- Lokal na testing at optimization workflows
- ONNX at Ollama integration para sa edge models
- Model conversion at quantization techniques
- Agent development para sa edge scenarios
- Performance evaluation at monitoring
- Deployment preparation at best practices

## Konklusyon

Ang limang implementasyon ng EdgeAI na ito ay nagpapakita ng maturity at diversity ng mga solusyon sa edge AI na available ngayon. Mula sa hardware-accelerated edge devices tulad ng Jetson Orin Nano hanggang sa software frameworks tulad ng ONNX Runtime GenAI at Windows ML, ang mga developer ay may hindi pa nagagawang mga opsyon para sa pag-deploy ng matatalinong applications sa edge.

Ang karaniwang tema sa lahat ng mga platform na ito ay ang democratization ng AI capabilities, na ginagawang accessible ang advanced machine learning sa mga developer sa iba't ibang skill levels at use cases. Kung gumagawa ng mobile applications, desktop software, o embedded systems, ang mga EdgeAI solutions na ito ay nagbibigay ng pundasyon para sa susunod na henerasyon ng matatalinong applications na gumagana nang mahusay at pribado sa edge.

Ang bawat platform ay nag-aalok ng natatanging mga bentahe: Jetson Orin Nano para sa hardware-accelerated edge computing, ONNX Runtime GenAI para sa cross-platform mobile development, Azure EdgeAI para sa enterprise cloud-edge integration, Windows ML para sa Windows-native applications, at Foundry Local para sa privacy-focused RAG implementations. Sama-sama, sila ay kumakatawan sa isang komprehensibong ecosystem para sa EdgeAI development.

[Next AI Toolkit](aitoolkit.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.