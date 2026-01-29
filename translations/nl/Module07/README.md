# Hoofdstuk 07: EdgeAI Voorbeelden

Edge AI combineert kunstmatige intelligentie met edge computing, waardoor intelligente verwerking direct op apparaten mogelijk wordt zonder afhankelijk te zijn van cloudconnectiviteit. Dit hoofdstuk verkent vijf verschillende EdgeAI-implementaties op diverse platforms en frameworks, en toont de veelzijdigheid en kracht van AI-modellen die aan de rand worden uitgevoerd.

## 1. EdgeAI op NVIDIA Jetson Orin Nano

De NVIDIA Jetson Orin Nano is een doorbraak in toegankelijke edge AI-computing en biedt tot 67 TOPS aan AI-prestaties in een compacte, creditcardformaat. Dit krachtige edge AI-platform democratiseert generatieve AI-ontwikkeling voor hobbyisten, studenten en professionele ontwikkelaars.

### Belangrijkste Kenmerken
- Biedt tot 67 TOPS aan AI-prestaties—een 1,7X verbetering ten opzichte van zijn voorganger
- 1024 CUDA-cores en tot 32 Tensor Cores voor AI-verwerking
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU met een maximale frequentie van 1,5 GHz
- Geprijsd op slechts $249, waardoor het de meest betaalbare en toegankelijke platform is voor ontwikkelaars, studenten en makers

### Toepassingen
De Jetson Orin Nano blinkt uit in het uitvoeren van moderne generatieve AI-modellen, waaronder vision transformers, grote taalmodellen en vision-language modellen. Het is specifiek ontworpen voor GenAI-toepassingen en maakt het mogelijk om verschillende LLMs op een handapparaat te draaien. Populaire toepassingen zijn onder andere AI-gestuurde robotica, slimme drones, intelligente camera's en autonome edge-apparaten.

**Meer informatie**: [NVIDIA's Jetson Orin Nano SuperComputer: De Volgende Grote Stap in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI in Mobiele Applicaties met .NET MAUI en ONNX Runtime GenAI

Deze oplossing laat zien hoe Generatieve AI en Grote Taalmodellen (LLMs) kunnen worden geïntegreerd in cross-platform mobiele applicaties met behulp van .NET MAUI (Multi-platform App UI) en ONNX Runtime GenAI. Deze aanpak stelt .NET-ontwikkelaars in staat om geavanceerde AI-gestuurde mobiele applicaties te bouwen die native draaien op Android- en iOS-apparaten.

### Belangrijkste Kenmerken
- Gebouwd op het .NET MAUI-framework, met een enkele codebase voor zowel Android- als iOS-applicaties
- ONNX Runtime GenAI-integratie maakt het mogelijk om generatieve AI-modellen direct op mobiele apparaten uit te voeren
- Ondersteunt verschillende hardwareversnellers die zijn afgestemd op mobiele apparaten, waaronder CPU, GPU en gespecialiseerde mobiele AI-processors
- Platformspecifieke optimalisaties zoals CoreML voor iOS en NNAPI voor Android via ONNX Runtime
- Implementeert de volledige generatieve AI-cyclus, inclusief pre- en postverwerking, inferentie, logits-verwerking, zoeken en sampling, en KV-cachebeheer

### Voordelen voor Ontwikkelaars
De .NET MAUI-aanpak stelt ontwikkelaars in staat hun bestaande C#- en .NET-vaardigheden te benutten bij het bouwen van cross-platform AI-applicaties. Het ONNX Runtime GenAI-framework ondersteunt meerdere modelarchitecturen, waaronder Llama, Mistral, Phi, Gemma en vele anderen. Geoptimaliseerde ARM64-kernels versnellen INT4-gekwantificeerde matrixvermenigvuldiging, wat zorgt voor efficiënte prestaties op mobiele hardware terwijl de vertrouwde .NET-ontwikkelervaring behouden blijft.

### Toepassingen
Deze oplossing is ideaal voor ontwikkelaars die AI-gestuurde mobiele applicaties willen bouwen met behulp van .NET-technologieën, zoals intelligente chatbots, beeldherkenningsapps, taalvertalingstools en gepersonaliseerde aanbevelingssystemen die volledig op het apparaat draaien voor verbeterde privacy en offline mogelijkheden.

**Meer informatie**: [.NET MAUI ONNX Runtime GenAI Voorbeeld](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI in Azure met Small Language Models Engine

Microsoft's Azure-gebaseerde EdgeAI-oplossing richt zich op het efficiënt inzetten van Small Language Models (SLMs) in hybride cloud-edge-omgevingen. Deze aanpak overbrugt de kloof tussen AI-diensten op cloudniveau en edge-implementatievereisten.

### Voordelen van Architectuur
- Naadloze integratie met Azure AI-diensten
- Voer SLMs/LLMs en multimodale modellen uit op apparaten en in de cloud met ONNX Runtime
- Geoptimaliseerd voor implementatie op ondernemingsniveau
- Ondersteuning voor continue modelupdates en -beheer

### Toepassingen
De Azure EdgeAI-implementatie blinkt uit in scenario's die AI-implementatie op ondernemingsniveau vereisen met cloudbeheerfunctionaliteiten. Dit omvat intelligente documentverwerking, realtime analytics en hybride AI-workflows die zowel cloud- als edge-computingbronnen benutten.

**Meer informatie**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI met Windows ML](./windowdeveloper.md)

Windows ML is Microsoft's geavanceerde runtime, geoptimaliseerd voor efficiënte modelinferentie op apparaten en vereenvoudigde implementatie. Het vormt de basis van Windows AI Foundry en stelt ontwikkelaars in staat AI-gestuurde Windows-applicaties te maken die gebruikmaken van de volledige hardwaremogelijkheden van pc's.

### Platformmogelijkheden
- Werkt op alle Windows 11-pc's met versie 24H2 (build 26100) of hoger
- Werkt op alle x64- en ARM64-pc-hardware, zelfs pc's zonder NPUs of GPUs
- Stelt ontwikkelaars in staat hun eigen modellen mee te nemen en efficiënt te implementeren binnen het ecosysteem van siliciumpartners, waaronder AMD, Intel, NVIDIA en Qualcomm, met CPU, GPU, NPU
- Dankzij infrastructuur-API's hoeven ontwikkelaars niet langer meerdere builds van hun app te maken om verschillende silicium te targeten

### Voordelen voor Ontwikkelaars
Windows ML abstraheert de hardware en uitvoeringsproviders, zodat je je kunt concentreren op het schrijven van je code. Bovendien wordt Windows ML automatisch bijgewerkt om de nieuwste NPUs, GPUs en CPUs te ondersteunen zodra ze worden uitgebracht. Het platform biedt een uniforme framework voor AI-ontwikkeling binnen het diverse Windows-hardware-ecosysteem.

**Meer informatie**: 
- [Windows ML Overzicht](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Ontwikkelingsgids](./windowdeveloper.md) - Uitgebreide gids voor Windows Edge AI-ontwikkeling

## [5. EdgeAI met Foundry Local Applicaties](./foundrylocal.md)

Foundry Local stelt Windows- en Mac-ontwikkelaars in staat Retrieval Augmented Generation (RAG)-applicaties te bouwen met lokale bronnen in .NET, waarbij lokale taalmodellen worden gecombineerd met semantische zoekmogelijkheden. Deze aanpak biedt privacygerichte AI-oplossingen die volledig op lokale infrastructuur werken.

### Technische Architectuur
- Combineert het Phi-taalmodel, lokale embeddings en Semantic Kernel om een RAG-scenario te creëren
- Gebruikt embeddings als vectoren (arrays) van drijvende-kommawaarden die inhoud en de semantische betekenis ervan vertegenwoordigen
- Semantic Kernel fungeert als de belangrijkste orkestrator, die Phi en Smart Components integreert om een naadloze RAG-pijplijn te creëren
- Ondersteuning voor lokale vector-databases, waaronder SQLite en Qdrant

### Voordelen van Implementatie
RAG, of Retrieval Augmented Generation, is gewoon een chique manier om te zeggen "zoek wat informatie op en voeg het toe aan de prompt". Deze lokale implementatie zorgt voor gegevensprivacy terwijl intelligente antwoorden worden gegeven die gebaseerd zijn op aangepaste kennisbanken. De aanpak is bijzonder waardevol voor ondernemingsscenario's die gegevenssoevereiniteit en offline operationele mogelijkheden vereisen.

**Meer informatie**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Voorbeelden](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local biedt een OpenAI-compatibele REST-server aangedreven door ONNX Runtime voor het lokaal uitvoeren van modellen op Windows. Hieronder een snelle, gevalideerde samenvatting; zie officiële documentatie voor volledige details.

- Aan de slag: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architectuur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-referentie: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Volledige Windows-gids in deze repo: [foundrylocal.md](./foundrylocal.md)

Installeren of upgraden op Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Verken CLI-categorieën:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Voer een model uit en ontdek de dynamische endpoint:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Snelle REST-controle om modellen te lijst (vervang PORT van status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK-integratie: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Eigen model meenemen (compileren): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Ontwikkelingsbronnen

Voor ontwikkelaars die specifiek op het Windows-platform richten, hebben we een uitgebreide gids gemaakt die het volledige Windows EdgeAI-ecosysteem behandelt. Deze bron biedt gedetailleerde informatie over Windows AI Foundry, inclusief API's, tools en best practices voor EdgeAI-ontwikkeling op Windows.

### Windows AI Foundry Platform
Het Windows AI Foundry-platform biedt een uitgebreide suite van tools en API's die specifiek zijn ontworpen voor Edge AI-ontwikkeling op Windows-apparaten. Dit omvat gespecialiseerde ondersteuning voor NPU-versnelde hardware, Windows ML-integratie en platformspecifieke optimalisatietechnieken.

**Uitgebreide Gids**: [Windows EdgeAI Ontwikkelingsgids](../windowdeveloper.md)

Deze gids behandelt:
- Overzicht en componenten van het Windows AI Foundry-platform
- Phi Silica API voor efficiënte inferentie op NPU-hardware
- Computer Vision API's voor beeldverwerking en OCR
- Windows ML runtime-integratie en optimalisatie
- Foundry Local CLI voor lokale ontwikkeling en testen
- Hardware-optimalisatiestrategieën voor Windows-apparaten
- Praktische implementatievoorbeelden en best practices

### [AI Toolkit voor Edge AI Ontwikkeling](./aitoolkit.md)
Voor ontwikkelaars die Visual Studio Code gebruiken, biedt de AI Toolkit-extensie een uitgebreide ontwikkelomgeving die specifiek is ontworpen voor het bouwen, testen en implementeren van Edge AI-applicaties. Deze toolkit stroomlijnt de volledige Edge AI-ontwikkelworkflow binnen VS Code.

**Ontwikkelingsgids**: [AI Toolkit voor Edge AI Ontwikkeling](./aitoolkit.md)

De AI Toolkit-gids behandelt:
- Modelontdekking en selectie voor edge-implementatie
- Lokale test- en optimalisatieworkflows
- ONNX- en Ollama-integratie voor edge-modellen
- Modelconversie en kwantiseringstechnieken
- Agentontwikkeling voor edge-scenario's
- Prestatie-evaluatie en monitoring
- Implementatievoorbereiding en best practices

## Conclusie

Deze vijf EdgeAI-implementaties tonen de volwassenheid en diversiteit van edge AI-oplossingen die vandaag beschikbaar zijn. Van hardwareversnelde edge-apparaten zoals de Jetson Orin Nano tot softwareframeworks zoals ONNX Runtime GenAI en Windows ML, ontwikkelaars hebben ongekende mogelijkheden om intelligente applicaties aan de rand te implementeren.

De gemeenschappelijke factor tussen al deze platforms is de democratisering van AI-mogelijkheden, waardoor geavanceerde machine learning toegankelijk wordt voor ontwikkelaars met verschillende vaardigheidsniveaus en toepassingen. Of je nu mobiele applicaties, desktopsoftware of embedded systemen bouwt, deze EdgeAI-oplossingen bieden de basis voor de volgende generatie intelligente applicaties die efficiënt en privé aan de rand werken.

Elk platform biedt unieke voordelen: Jetson Orin Nano voor hardwareversnelde edge computing, ONNX Runtime GenAI voor cross-platform mobiele ontwikkeling, Azure EdgeAI voor cloud-edge-integratie op ondernemingsniveau, Windows ML voor Windows-native applicaties, en Foundry Local voor privacygerichte RAG-implementaties. Samen vormen ze een uitgebreid ecosysteem voor EdgeAI-ontwikkeling.

[Volgende AI Toolkit](aitoolkit.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.