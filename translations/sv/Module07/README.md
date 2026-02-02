# Kapitel 07: EdgeAI-exempel

Edge AI representerar sammansmältningen av artificiell intelligens och edge computing, vilket möjliggör intelligent bearbetning direkt på enheter utan att vara beroende av molnanslutning. Detta kapitel utforskar fem olika EdgeAI-implementeringar på olika plattformar och ramverk, och visar mångsidigheten och kraften i att köra AI-modeller vid kanten.

## 1. EdgeAI med NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano representerar ett genombrott inom tillgänglig edge AI-datoranvändning och levererar upp till 67 TOPS AI-prestanda i ett kompakt format, lika stort som ett kreditkort. Denna kraftfulla edge AI-plattform demokratiserar utvecklingen av generativ AI för hobbyister, studenter och professionella utvecklare.

### Viktiga funktioner
- Levererar upp till 67 TOPS AI-prestanda—en förbättring med 1,7X jämfört med sin föregångare
- 1024 CUDA-kärnor och upp till 32 Tensor Cores för AI-bearbetning
- 6-kärnig Arm Cortex-A78AE v8.2 64-bitars CPU med maximal frekvens på 1,5 GHz
- Prissatt till endast $249, vilket gör det till den mest prisvärda och tillgängliga plattformen för utvecklare, studenter och skapare

### Användningsområden
Jetson Orin Nano utmärker sig vid körning av moderna generativa AI-modeller, inklusive vision transformers, stora språkmodeller och vision-språkmodeller. Den är specifikt designad för GenAI-användningsfall och nu kan du köra flera LLM:er på en handhållen enhet. Populära användningsområden inkluderar AI-drivna robotar, smarta drönare, intelligenta kameror och autonoma edge-enheter.

**Läs mer**: [NVIDIA:s Jetson Orin Nano SuperComputer: Nästa stora grej inom EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI i mobila applikationer med .NET MAUI och ONNX Runtime GenAI

Denna lösning visar hur man integrerar Generativ AI och Stora Språkmodeller (LLMs) i plattformsoberoende mobila applikationer med hjälp av .NET MAUI (Multi-platform App UI) och ONNX Runtime GenAI. Detta tillvägagångssätt gör det möjligt för .NET-utvecklare att bygga sofistikerade AI-drivna mobila applikationer som körs nativt på Android- och iOS-enheter.

### Viktiga funktioner
- Byggd på .NET MAUI-ramverket, vilket ger en enda kodbas för både Android- och iOS-applikationer
- ONNX Runtime GenAI-integrering möjliggör körning av generativa AI-modeller direkt på mobila enheter
- Stödjer olika hårdvaruacceleratorer anpassade för mobila enheter, inklusive CPU, GPU och specialiserade mobila AI-processorer
- Plattformsspecifika optimeringar som CoreML för iOS och NNAPI för Android via ONNX Runtime
- Implementerar hela generativa AI-loopen inklusive för- och efterbearbetning, inferens, logitsbearbetning, sökning och sampling samt KV-cachehantering

### Utvecklingsfördelar
.NET MAUI-ansatsen gör det möjligt för utvecklare att utnyttja sina befintliga C#- och .NET-kunskaper samtidigt som de bygger plattformsoberoende AI-applikationer. ONNX Runtime GenAI-ramverket stödjer flera modellarkitekturer, inklusive Llama, Mistral, Phi, Gemma och många andra. Optimerade ARM64-kärnor accelererar INT4-kvantiserad matrismultiplikation, vilket säkerställer effektiv prestanda på mobil hårdvara samtidigt som den bekanta .NET-utvecklingsupplevelsen bibehålls.

### Användningsområden
Denna lösning är idealisk för utvecklare som vill bygga AI-drivna mobila applikationer med .NET-teknologier, inklusive intelligenta chatbotar, bildigenkänningsappar, språköversättningsverktyg och personliga rekommendationssystem som körs helt på enheten för förbättrad integritet och offlinekapacitet.

**Läs mer**: [.NET MAUI ONNX Runtime GenAI Exempel](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI i Azure med Small Language Models Engine

Microsofts Azure-baserade EdgeAI-lösning fokuserar på att effektivt distribuera Small Language Models (SLMs) i hybridmiljöer mellan moln och edge. Detta tillvägagångssätt överbryggar klyftan mellan AI-tjänster i molnskala och krav på edge-distribution.

### Arkitekturella fördelar
- Sömlös integrering med Azure AI-tjänster
- Kör SLMs/LLMs och multimodala modeller på enheten och i molnet med ONNX Runtime
- Optimerad för företagsdistribution i stor skala
- Stöd för kontinuerliga modelluppdateringar och hantering

### Användningsområden
Azure EdgeAI-implementeringen utmärker sig i scenarier som kräver AI-distribution i företagsklass med molnhanteringskapacitet. Detta inkluderar intelligent dokumentbearbetning, realtidsanalys och hybrid AI-arbetsflöden som utnyttjar både moln- och edge-beräkningsresurser.

**Läs mer**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI med Windows ML](./windowdeveloper.md)

Windows ML representerar Microsofts avancerade runtime optimerad för effektiv modellinferens på enheten och förenklad distribution, och fungerar som grunden för Windows AI Foundry. Denna plattform gör det möjligt för utvecklare att skapa AI-drivna Windows-applikationer som utnyttjar hela spektrumet av PC-hårdvara.

### Plattformskapacitet
- Fungerar på alla Windows 11-datorer som kör version 24H2 (build 26100) eller senare
- Fungerar på all x64- och ARM64-PC-hårdvara, även datorer som saknar NPUs eller GPUs
- Gör det möjligt för utvecklare att ta med sina egna modeller och distribuera dem effektivt över ekosystemet av kiselpartners, inklusive AMD, Intel, NVIDIA och Qualcomm, som sträcker sig över CPU, GPU, NPU
- Genom att utnyttja infrastruktur-API:er behöver utvecklare inte längre skapa flera versioner av sin app för att rikta in sig på olika kisel

### Utvecklarfördelar
Windows ML abstraherar hårdvaran och exekveringsleverantörerna, så att du kan fokusera på att skriva din kod. Dessutom uppdateras Windows ML automatiskt för att stödja de senaste NPUs, GPUs och CPUs när de släpps. Plattformen tillhandahåller ett enhetligt ramverk för AI-utveckling över det mångsidiga Windows-hårdvaruekosystemet.

**Läs mer**: 
- [Windows ML Översikt](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Utvecklingsguide](./windowdeveloper.md) - Omfattande guide för Windows Edge AI-utveckling

## [5. EdgeAI med Foundry Local-applikationer](./foundrylocal.md)

Foundry Local gör det möjligt för Windows- och Mac-utvecklare att bygga Retrieval Augmented Generation (RAG)-applikationer med lokala resurser i .NET, och kombinerar lokala språkmodeller med semantiska sökfunktioner. Detta tillvägagångssätt erbjuder integritetsfokuserade AI-lösningar som fungerar helt på lokal infrastruktur.

### Teknisk arkitektur
- Kombinerar Phi-språkmodellen, lokala embeddings och Semantic Kernel för att skapa ett RAG-scenario
- Använder embeddings som vektorer (arrayer) av flyttalsvärden som representerar innehåll och dess semantiska betydelse
- Semantic Kernel fungerar som huvudorkestrator och integrerar Phi och Smart Components för att skapa en sömlös RAG-pipeline
- Stöd för lokala vektordatabaser inklusive SQLite och Qdrant

### Implementeringsfördelar
RAG, eller Retrieval Augmented Generation, är bara ett fint sätt att säga "sök upp lite information och lägg till det i prompten". Denna lokala implementering säkerställer dataintegritet samtidigt som den tillhandahåller intelligenta svar baserade på anpassade kunskapsbaser. Tillvägagångssättet är särskilt värdefullt för företagsmiljöer som kräver datasuveränitet och offlinekapacitet.

**Läs mer**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Exempel](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local tillhandahåller en OpenAI-kompatibel REST-server som drivs av ONNX Runtime för att köra modeller lokalt på Windows. Nedan finns en snabb, validerad sammanfattning; se officiell dokumentation för fullständiga detaljer.

- Kom igång: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-referens: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Fullständig Windows-guide i detta repo: [foundrylocal.md](./foundrylocal.md)

Installera eller uppgradera på Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Utforska CLI-kategorier:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Kör en modell och upptäck den dynamiska slutpunkten:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Snabb REST-kontroll för att lista modeller (ersätt PORT från status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK-integrering: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Ta med din egen modell (kompilera): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Utvecklingsresurser

För utvecklare som specifikt riktar sig mot Windows-plattformen har vi skapat en omfattande guide som täcker hela Windows EdgeAI-ekosystemet. Denna resurs tillhandahåller detaljerad information om Windows AI Foundry, inklusive API:er, verktyg och bästa praxis för EdgeAI-utveckling på Windows.

### Windows AI Foundry Plattform
Windows AI Foundry-plattformen tillhandahåller en omfattande uppsättning verktyg och API:er som är specifikt designade för Edge AI-utveckling på Windows-enheter. Detta inkluderar specialiserat stöd för NPU-accelererad hårdvara, Windows ML-integrering och plattformsspecifika optimeringstekniker.

**Omfattande guide**: [Windows EdgeAI Utvecklingsguide](../windowdeveloper.md)

Denna guide täcker:
- Översikt och komponenter för Windows AI Foundry-plattformen
- Phi Silica API för effektiv inferens på NPU-hårdvara
- Datorvisions-API:er för bildbearbetning och OCR
- Windows ML runtime-integrering och optimering
- Foundry Local CLI för lokal utveckling och testning
- Strategier för hårdvaruoptimering för Windows-enheter
- Praktiska implementeringsexempel och bästa praxis

### [AI Toolkit för Edge AI-utveckling](./aitoolkit.md)
För utvecklare som använder Visual Studio Code tillhandahåller AI Toolkit-tillägget en omfattande utvecklingsmiljö som är specifikt designad för att bygga, testa och distribuera Edge AI-applikationer. Detta verktyg förenklar hela Edge AI-utvecklingsarbetsflödet inom VS Code.

**Utvecklingsguide**: [AI Toolkit för Edge AI-utveckling](./aitoolkit.md)

AI Toolkit-guiden täcker:
- Modellupptäckt och urval för edge-distribution
- Lokala test- och optimeringsarbetsflöden
- ONNX och Ollama-integrering för edge-modeller
- Modellkonvertering och kvantiseringstekniker
- Agentutveckling för edge-scenarier
- Prestandautvärdering och övervakning
- Förberedelse för distribution och bästa praxis

## Slutsats

Dessa fem EdgeAI-implementeringar visar mognaden och mångfalden av edge AI-lösningar som finns tillgängliga idag. Från hårdvaruaccelererade edge-enheter som Jetson Orin Nano till mjukvaruramverk som ONNX Runtime GenAI och Windows ML, har utvecklare oöverträffade alternativ för att distribuera intelligenta applikationer vid kanten.

Den gemensamma nämnaren för alla dessa plattformar är demokratiseringen av AI-kapaciteter, vilket gör sofistikerad maskininlärning tillgänglig för utvecklare med olika kompetensnivåer och användningsområden. Oavsett om du bygger mobila applikationer, skrivbordsprogram eller inbyggda system, tillhandahåller dessa EdgeAI-lösningar grunden för nästa generation av intelligenta applikationer som fungerar effektivt och privat vid kanten.

Varje plattform erbjuder unika fördelar: Jetson Orin Nano för hårdvaruaccelererad edge computing, ONNX Runtime GenAI för plattformsoberoende mobilutveckling, Azure EdgeAI för företagsintegration mellan moln och edge, Windows ML för Windows-nativa applikationer och Foundry Local för integritetsfokuserade RAG-implementeringar. Tillsammans representerar de ett omfattande ekosystem för EdgeAI-utveckling.

[Nästa AI Toolkit](aitoolkit.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.