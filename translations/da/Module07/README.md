# Kapitel 07: EdgeAI Eksempler

Edge AI repræsenterer sammensmeltningen af kunstig intelligens og edge computing, hvilket muliggør intelligent databehandling direkte på enheder uden behov for cloud-forbindelse. Dette kapitel udforsker fem forskellige EdgeAI-implementeringer på tværs af forskellige platforme og frameworks, der viser alsidigheden og styrken ved at køre AI-modeller på kanten.

## 1. EdgeAI på NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano markerer et gennembrud inden for tilgængelig edge AI-computing og leverer op til 67 TOPS AI-ydeevne i et kompakt format på størrelse med et kreditkort. Denne kraftfulde edge AI-platform demokratiserer udviklingen af generativ AI for hobbyister, studerende og professionelle udviklere.

### Nøglefunktioner
- Leverer op til 67 TOPS AI-ydeevne—en 1,7X forbedring i forhold til sin forgænger
- 1024 CUDA-kerner og op til 32 Tensor Cores til AI-behandling
- 6-core Arm Cortex-A78AE v8.2 64-bit CPU med en maksimal frekvens på 1,5 GHz
- Prissat til kun $249, hvilket gør det til den mest overkommelige og tilgængelige platform for udviklere, studerende og skabere

### Anvendelser
Jetson Orin Nano er fremragende til at køre moderne generative AI-modeller, herunder vision transformers, store sprogmodeller og vision-sprogmodeller. Den er specifikt designet til GenAI-brugsscenarier, og nu kan du køre flere LLM'er på en håndholdt enhed. Populære anvendelser inkluderer AI-drevne robotter, smarte droner, intelligente kameraer og autonome edge-enheder.

**Læs mere**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI i Mobilapplikationer med .NET MAUI og ONNX Runtime GenAI

Denne løsning viser, hvordan man integrerer Generativ AI og Store Sprogmodeller (LLMs) i tværplatforms mobilapplikationer ved hjælp af .NET MAUI (Multi-platform App UI) og ONNX Runtime GenAI. Denne tilgang gør det muligt for .NET-udviklere at bygge avancerede AI-drevne mobilapplikationer, der kører lokalt på Android- og iOS-enheder.

### Nøglefunktioner
- Bygget på .NET MAUI-framework, der giver en enkelt kodebase til både Android- og iOS-applikationer
- ONNX Runtime GenAI-integration muliggør kørsel af generative AI-modeller direkte på mobile enheder
- Understøtter forskellige hardwareacceleratorer tilpasset mobile enheder, herunder CPU, GPU og specialiserede mobile AI-processorer
- Platformsspecifikke optimeringer som CoreML til iOS og NNAPI til Android via ONNX Runtime
- Implementerer hele den generative AI-loop, herunder for- og efterbehandling, inferens, logits-behandling, søgning og sampling samt KV-cachehåndtering

### Udviklingsfordele
.NET MAUI-tilgangen giver udviklere mulighed for at udnytte deres eksisterende C#- og .NET-kompetencer, mens de bygger tværplatforms AI-applikationer. ONNX Runtime GenAI-frameworket understøtter flere modelarkitekturer, herunder Llama, Mistral, Phi, Gemma og mange andre. Optimerede ARM64-kerner accelererer INT4-kvantisering af matrixmultiplikation, hvilket sikrer effektiv ydeevne på mobilhardware, samtidig med at den velkendte .NET-udviklingsoplevelse bevares.

### Brugsscenarier
Denne løsning er ideel for udviklere, der ønsker at bygge AI-drevne mobilapplikationer ved hjælp af .NET-teknologier, herunder intelligente chatbots, billedgenkendelsesapps, sprogover-sættelsesværktøjer og personlige anbefalingssystemer, der kører helt lokalt for forbedret privatliv og offline-funktionalitet.

**Læs mere**: [.NET MAUI ONNX Runtime GenAI Eksempel](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI i Azure med Small Language Models Engine

Microsofts Azure-baserede EdgeAI-løsning fokuserer på effektivt at implementere Small Language Models (SLMs) i cloud-edge hybridmiljøer. Denne tilgang bygger bro mellem cloud-skala AI-tjenester og edge-implementeringskrav.

### Arkitekturfordele
- Problemfri integration med Azure AI-tjenester
- Kør SLMs/LLMs og multimodale modeller på enheder og i skyen med ONNX Runtime
- Optimeret til implementering i virksomhedsskala
- Understøttelse af kontinuerlige modelopdateringer og -styring

### Brugsscenarier
Azure EdgeAI-implementeringen er fremragende i scenarier, der kræver AI-implementering i virksomhedsklasse med cloud-styringsmuligheder. Dette inkluderer intelligent dokumentbehandling, realtidsanalyse og hybride AI-arbejdsgange, der udnytter både cloud- og edge-computingressourcer.

**Læs mere**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI med Windows ML](./windowdeveloper.md)

Windows ML repræsenterer Microsofts avancerede runtime, der er optimeret til effektiv modelinferens på enheder og forenklet implementering. Det fungerer som fundamentet for Windows AI Foundry. Denne platform gør det muligt for udviklere at skabe AI-drevne Windows-applikationer, der udnytter hele spektret af PC-hardware.

### Platformens kapaciteter
- Fungerer på alle Windows 11-PC'er, der kører version 24H2 (build 26100) eller nyere
- Fungerer på alle x64- og ARM64-PC-hardware, selv PC'er uden NPUs eller GPUs
- Giver udviklere mulighed for at medbringe deres egne modeller og implementere dem effektivt på tværs af silikonepartnerøkosystemet, herunder AMD, Intel, NVIDIA og Qualcomm, der spænder over CPU, GPU, NPU
- Ved at udnytte infrastruktur-API'er behøver udviklere ikke længere at oprette flere builds af deres app for at målrette forskellige silikoner

### Udviklerfordele
Windows ML abstraherer hardware og eksekveringsudbydere, så du kan fokusere på at skrive din kode. Derudover opdateres Windows ML automatisk for at understøtte de nyeste NPUs, GPUs og CPUs, efterhånden som de frigives. Platformen giver en samlet ramme for AI-udvikling på tværs af det mangfoldige Windows-hardwareøkosystem.

**Læs mere**: 
- [Windows ML Oversigt](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Udviklingsguide](./windowdeveloper.md) - Omfattende guide til Windows Edge AI-udvikling

## [5. EdgeAI med Foundry Local Applikationer](./foundrylocal.md)

Foundry Local gør det muligt for Windows- og Mac-udviklere at bygge Retrieval Augmented Generation (RAG)-applikationer ved hjælp af lokale ressourcer i .NET, der kombinerer lokale sprogmodeller med semantiske søgefunktioner. Denne tilgang giver privatlivsfokuserede AI-løsninger, der fungerer helt på lokal infrastruktur.

### Teknisk arkitektur
- Kombinerer Phi-sprogmodellen, lokale embeddings og Semantic Kernel for at skabe et RAG-scenarie
- Bruger embeddings som vektorer (arrays) af flydende punktværdier, der repræsenterer indhold og dets semantiske betydning
- Semantic Kernel fungerer som den primære orkestrator, der integrerer Phi og Smart Components for at skabe en problemfri RAG-pipeline
- Understøttelse af lokale vektordatabaser, herunder SQLite og Qdrant

### Implementeringsfordele
RAG, eller Retrieval Augmented Generation, er blot en fancy måde at sige "slå noget op og inkludér det i prompten". Denne lokale implementering sikrer databeskyttelse, samtidig med at den leverer intelligente svar baseret på brugerdefinerede vidensbaser. Tilgangen er særlig værdifuld for virksomhedsscenarier, der kræver datasuverænitet og offline-funktionalitet.

**Læs mere**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Eksempler](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local tilbyder en OpenAI-kompatibel REST-server drevet af ONNX Runtime til at køre modeller lokalt på Windows. Nedenfor er en hurtig, valideret oversigt; se officielle dokumenter for fulde detaljer.

- Kom godt i gang: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Fuld Windows-guide i dette repo: [foundrylocal.md](./foundrylocal.md)

Installer eller opgrader på Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Udforsk CLI-kategorier:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Kør en model og opdag den dynamiske endpoint:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Hurtig REST-check for at liste modeller (erstat PORT fra status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tips:
- SDK-integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Medbring din egen model (kompilér): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI Udviklingsressourcer

For udviklere, der specifikt retter sig mod Windows-platformen, har vi skabt en omfattende guide, der dækker hele Windows EdgeAI-økosystemet. Denne ressource giver detaljeret information om Windows AI Foundry, herunder API'er, værktøjer og bedste praksis for EdgeAI-udvikling på Windows.

### Windows AI Foundry Platform
Windows AI Foundry-platformen tilbyder en omfattende suite af værktøjer og API'er, der er specielt designet til Edge AI-udvikling på Windows-enheder. Dette inkluderer specialiseret understøttelse af NPU-accelereret hardware, Windows ML-integration og platformsspecifikke optimeringsteknikker.

**Omfattende guide**: [Windows EdgeAI Udviklingsguide](../windowdeveloper.md)

Guiden dækker:
- Windows AI Foundry-platformens oversigt og komponenter
- Phi Silica API til effektiv inferens på NPU-hardware
- Computer Vision API'er til billedbehandling og OCR
- Windows ML runtime-integration og optimering
- Foundry Local CLI til lokal udvikling og test
- Hardwareoptimeringsstrategier for Windows-enheder
- Praktiske implementeringseksempler og bedste praksis

### [AI Toolkit til Edge AI Udvikling](./aitoolkit.md)
For udviklere, der bruger Visual Studio Code, tilbyder AI Toolkit-udvidelsen et omfattende udviklingsmiljø, der er specielt designet til at bygge, teste og implementere Edge AI-applikationer. Dette værktøjssæt strømliner hele Edge AI-udviklingsarbejdsgangen inden for VS Code.

**Udviklingsguide**: [AI Toolkit til Edge AI Udvikling](./aitoolkit.md)

AI Toolkit-guiden dækker:
- Modelopdagelse og -valg til edge-implementering
- Lokale test- og optimeringsarbejdsgange
- ONNX og Ollama-integration til edge-modeller
- Modelkonvertering og kvantiseringsteknikker
- Agentudvikling til edge-scenarier
- Ydelsesevaluering og overvågning
- Implementeringsforberedelse og bedste praksis

## Konklusion

Disse fem EdgeAI-implementeringer demonstrerer modenheden og mangfoldigheden af de edge AI-løsninger, der er tilgængelige i dag. Fra hardwareaccelererede edge-enheder som Jetson Orin Nano til softwareframeworks som ONNX Runtime GenAI og Windows ML har udviklere enestående muligheder for at implementere intelligente applikationer på kanten.

Den fælles tråd på tværs af alle disse platforme er demokratiseringen af AI-kapaciteter, der gør avanceret maskinlæring tilgængelig for udviklere på tværs af forskellige kompetenceniveauer og brugsscenarier. Uanset om du bygger mobilapplikationer, desktopsoftware eller indlejrede systemer, giver disse EdgeAI-løsninger fundamentet for næste generation af intelligente applikationer, der fungerer effektivt og privat på kanten.

Hver platform tilbyder unikke fordele: Jetson Orin Nano til hardwareaccelereret edge computing, ONNX Runtime GenAI til tværplatforms mobiludvikling, Azure EdgeAI til virksomhedens cloud-edge-integration, Windows ML til Windows-native applikationer og Foundry Local til privatlivsfokuserede RAG-implementeringer. Sammen repræsenterer de et omfattende økosystem for EdgeAI-udvikling.

[Next AI Toolkit](aitoolkit.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.