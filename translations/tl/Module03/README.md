# Kabanata 03: Pag-deploy ng Maliit na Language Models (SLMs)

Ang komprehensibong kabanatang ito ay tumatalakay sa buong lifecycle ng pag-deploy ng Maliit na Language Models (SLMs), mula sa teoretikal na pundasyon, praktikal na mga estratehiya sa implementasyon, hanggang sa mga solusyong handa para sa produksyon gamit ang containerized na teknolohiya. Ang kabanata ay nahahati sa tatlong progresibong seksyon na nagdadala sa mga mambabasa mula sa mga pangunahing konsepto hanggang sa mga advanced na senaryo ng pag-deploy.

## Estruktura ng Kabanata at Paglalakbay sa Pagkatuto

### **[Seksiyon 1: Advanced na Pagkatuto sa SLM - Pundasyon at Pag-optimize](./01.SLMAdvancedLearning.md)**
Ang pambungad na seksyon ay nagtatatag ng teoretikal na pundasyon para sa pag-unawa sa Maliit na Language Models at ang kanilang estratehikong kahalagahan sa edge AI deployments. Ang seksyon na ito ay sumasaklaw sa:

- **Parameter Classification Framework**: Detalyadong talakayan sa mga kategorya ng SLM mula sa Micro SLMs (100M-1.4B parameters) hanggang Medium SLMs (14B-30B parameters), na may partikular na pokus sa mga modelo tulad ng Phi-4-mini-3.8B, Qwen3 series, at Google Gemma3, kabilang ang mga kinakailangan sa hardware at pagsusuri ng memory footprint para sa bawat antas ng modelo
- **Advanced Optimization Techniques**: Komprehensibong talakayan sa mga pamamaraan ng quantization gamit ang Llama.cpp, Microsoft Olive, at Apple MLX frameworks, kabilang ang cutting-edge na BitNET 1-bit quantization na may mga praktikal na halimbawa ng code na nagpapakita ng mga pipeline ng quantization at benchmarking na resulta
- **Model Acquisition Strategies**: Malalim na pagsusuri sa Hugging Face ecosystem at Azure AI Foundry Model Catalog para sa enterprise-grade na pag-deploy ng SLM, na may mga halimbawa ng code para sa programmatic na pag-download, pag-validate, at pag-convert ng format ng modelo
- **Developer APIs**: Mga halimbawa ng code sa Python, C++, at C# na nagpapakita kung paano mag-load ng mga modelo, magsagawa ng inference, at mag-integrate sa mga sikat na frameworks tulad ng PyTorch, TensorFlow, at ONNX Runtime

Ang pundasyong seksyon na ito ay nagbibigay-diin sa balanse sa pagitan ng operational efficiency, deployment flexibility, at cost-effectiveness na ginagawang ideal ang SLMs para sa edge computing scenarios, na may mga praktikal na halimbawa ng code na maaaring direktang gamitin ng mga developer sa kanilang mga proyekto.

### **[Seksiyon 2: Pag-deploy sa Lokal na Kapaligiran - Mga Solusyong Nakatuon sa Privacy](./02.DeployingSLMinLocalEnv.md)**
Ang ikalawang seksyon ay lumilipat mula sa teorya patungo sa praktikal na implementasyon, na nakatuon sa mga estratehiya ng lokal na pag-deploy na inuuna ang data sovereignty at operational independence. Mga pangunahing paksa:

- **Ollama Universal Platform**: Komprehensibong talakayan sa cross-platform deployment na may pokus sa developer-friendly workflows, pamamahala ng lifecycle ng modelo, at pagpapasadya gamit ang Modelfiles, kabilang ang kumpletong REST API integration examples at CLI automation scripts
- **Microsoft Foundry Local**: Mga solusyong pang-enterprise na may ONNX-based optimization, Windows ML integration, at komprehensibong mga tampok sa seguridad, na may mga halimbawa ng code sa C# at Python para sa native application integration
- **Comparative Analysis**: Detalyadong paghahambing ng mga framework na sumasaklaw sa teknikal na arkitektura, mga katangian ng performance, at mga alituntunin sa pag-optimize ng use case, na may benchmark code para suriin ang bilis ng inference at paggamit ng memorya sa iba't ibang hardware
- **API Integration**: Mga sample na aplikasyon na nagpapakita kung paano bumuo ng mga web services, chat applications, at data processing pipelines gamit ang lokal na SLM deployments, na may mga halimbawa ng code sa Node.js, Python Flask/FastAPI, at ASP.NET Core
- **Testing Frameworks**: Mga automated na pamamaraan ng testing para sa quality assurance ng modelo, kabilang ang mga halimbawa ng unit at integration tests para sa mga implementasyon ng SLM

Ang seksyon na ito ay nagbibigay ng praktikal na gabay para sa mga organisasyong naghahanap ng privacy-preserving AI solutions habang pinapanatili ang buong kontrol sa kanilang deployment environment, na may mga handa nang gamitin na halimbawa ng code na maaaring iakma ng mga developer sa kanilang partikular na pangangailangan.

### **[Seksiyon 3: Containerized Cloud Deployment - Mga Solusyong Pang-produksyon](./03.DeployingSLMinCloud.md)**
Ang huling seksyon ay nagtatapos sa mga advanced na estratehiya ng containerized deployment, na tampok ang Microsoft's Phi-4-mini-instruct bilang pangunahing case study. Ang seksyon na ito ay sumasaklaw sa:

- **vLLM Deployment**: Mataas na performance na inference optimization gamit ang OpenAI-compatible APIs, advanced GPU acceleration, at production-grade configuration, kabilang ang kumpletong Dockerfiles, Kubernetes manifests, at mga parameter ng performance tuning
- **Ollama Container Orchestration**: Pinadaling workflows ng deployment gamit ang Docker Compose, mga variant ng model optimization, at web UI integration, na may mga halimbawa ng CI/CD pipeline para sa automated deployment at testing
- **ONNX Runtime Implementation**: Edge-optimized deployment na may komprehensibong model conversion, mga estratehiya ng quantization, at cross-platform compatibility, kabilang ang detalyadong mga halimbawa ng code para sa model optimization at deployment
- **Monitoring & Observability**: Implementasyon ng Prometheus/Grafana dashboards na may custom metrics para sa monitoring ng performance ng SLM, kabilang ang mga alerting configurations at log aggregation
- **Load Balancing & Scaling**: Mga praktikal na halimbawa ng horizontal at vertical scaling strategies na may autoscaling configurations batay sa CPU/GPU utilization at mga pattern ng request
- **Security Hardening**: Mga pinakamahusay na kasanayan sa seguridad ng container kabilang ang privilege reduction, network policies, at secrets management para sa API keys at mga kredensyal sa pag-access ng modelo

Ang bawat estratehiya ng pag-deploy ay ipinapakita gamit ang kumpletong mga halimbawa ng configuration, mga pamamaraan ng testing, mga checklist para sa production readiness, at mga infrastructure-as-code templates na maaaring direktang gamitin ng mga developer sa kanilang deployment workflows.

## Mga Pangunahing Layunin sa Pagkatuto

Sa pagtatapos ng kabanatang ito, ang mga mambabasa ay magiging bihasa sa:

1. **Strategic Model Selection**: Pag-unawa sa mga parameter boundaries at pagpili ng angkop na SLMs batay sa mga limitasyon ng resources at mga kinakailangan sa performance
2. **Optimization Mastery**: Pagpapatupad ng mga advanced na pamamaraan ng quantization sa iba't ibang frameworks upang makamit ang balanse ng performance at efficiency
3. **Deployment Flexibility**: Pagpili sa pagitan ng mga lokal na solusyong nakatuon sa privacy at scalable containerized deployments batay sa pangangailangan ng organisasyon
4. **Production Readiness**: Pag-configure ng monitoring, seguridad, at scaling systems para sa enterprise-grade na pag-deploy ng SLM

## Praktikal na Pokus at Mga Aplikasyon sa Totoong Mundo

Ang kabanata ay nagpapanatili ng malakas na praktikal na oryentasyon sa kabuuan, na nagtatampok ng:

- **Hands-on Examples**: Kumpletong mga configuration files, mga pamamaraan ng API testing, at mga deployment scripts
- **Performance Benchmarking**: Detalyadong paghahambing ng bilis ng inference, paggamit ng memorya, at mga kinakailangan sa resources
- **Security Considerations**: Mga kasanayan sa seguridad na pang-enterprise, mga compliance frameworks, at mga estratehiya sa proteksyon ng data
- **Best Practices**: Mga alituntunin na napatunayan sa produksyon para sa monitoring, scaling, at maintenance

## Perspektibong Handa sa Hinaharap

Ang kabanata ay nagtatapos sa mga pananaw na nakatuon sa hinaharap, kabilang ang:

- Mga advanced na arkitektura ng modelo na may pinahusay na efficiency ratios
- Mas malalim na integrasyon ng hardware gamit ang mga espesyal na AI accelerators
- Ebolusyon ng ecosystem patungo sa standardization at interoperability
- Mga pattern ng pag-aampon ng enterprise na pinapatakbo ng privacy at mga kinakailangan sa compliance

Ang komprehensibong approach na ito ay tinitiyak na ang mga mambabasa ay handang harapin ang parehong kasalukuyang mga hamon sa pag-deploy ng SLM at mga umuusbong na teknolohikal na pag-unlad, na gumagawa ng mga desisyong naaayon sa kanilang partikular na pangangailangan at limitasyon ng organisasyon.

Ang kabanata ay nagsisilbing parehong praktikal na gabay para sa agarang implementasyon at estratehikong mapagkukunan para sa pangmatagalang pagpaplano ng AI deployment, na nagbibigay-diin sa kritikal na balanse sa pagitan ng kakayahan, efficiency, at operational excellence na nagtatakda ng matagumpay na pag-deploy ng SLM.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.