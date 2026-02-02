# Windows Edge AI Utvecklingsguide

## Introduktion

Välkommen till Windows Edge AI-utveckling - din omfattande guide för att bygga intelligenta applikationer som utnyttjar kraften av AI direkt på enheten med hjälp av Microsofts Windows AI Foundry-plattform. Denna guide är specifikt utformad för Windows-utvecklare som vill integrera avancerade Edge AI-funktioner i sina applikationer samtidigt som de drar nytta av hela spektrumet av Windows hårdvaruacceleration.

### Fördelarna med Windows AI

Windows AI Foundry representerar en enhetlig, pålitlig och säker plattform som stödjer hela AI-utvecklingslivscykeln - från modellval och finjustering till optimering och distribution över CPU, GPU, NPU och hybridmolnarkitekturer. Denna plattform demokratiserar AI-utveckling genom att erbjuda:

- **Hårdvaruabstraktion**: Sömlös distribution över AMD-, Intel-, NVIDIA- och Qualcomm-silikon
- **Intelligens på enheten**: AI som bevarar integriteten och körs helt på lokal hårdvara
- **Optimerad prestanda**: Modeller föroptimerade för Windows hårdvarukonfigurationer
- **Färdig för företag**: Säkerhets- och efterlevnadsfunktioner i produktionsklass

### Windows ML 
Windows Machine Learning (ML) gör det möjligt för utvecklare som använder C#, C++ och Python att köra ONNX AI-modeller lokalt på Windows-datorer via ONNX Runtime, med automatisk hantering av exekveringsleverantörer för olika hårdvaror (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) kan användas med modeller från PyTorch, Tensorflow/Keras, TFLite, scikit-learn och andra ramverk.

![WindowsML En diagram som illustrerar en ONNX-modell som går genom Windows ML för att nå NPUs, GPUs och CPUs.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML tillhandahåller en delad Windows-övergripande kopia av ONNX Runtime, samt möjligheten att dynamiskt ladda ner exekveringsleverantörer (EPs).

### Varför Windows för Edge AI?

**Universellt stöd för hårdvara**  
Windows ML erbjuder automatisk hårdvaruoptimering över hela Windows-ekosystemet, vilket säkerställer att dina AI-applikationer presterar optimalt oavsett den underliggande silikonarkitekturen.

**Integrerad AI-runtime**  
Den inbyggda Windows ML-inferensmotorn eliminerar komplexa installationskrav, vilket gör att utvecklare kan fokusera på applikationslogik istället för infrastrukturbekymmer.

**Copilot+ PC-optimering**  
Skräddarsydda API:er designade specifikt för nästa generations Windows-enheter med dedikerade neurala processorenheter (NPUs) som levererar exceptionell prestanda per watt.

**Utvecklarekosystem**  
Rik verktygssats inklusive Visual Studio-integration, omfattande dokumentation och exempelapplikationer som påskyndar utvecklingscykler.

## Lärandemål

Genom att slutföra denna Windows Edge AI-utvecklingsguide kommer du att bemästra de grundläggande färdigheterna för att bygga produktionsklara AI-applikationer på Windows-plattformen.

### Kärntekniska kompetenser

**Windows AI Foundry-mästerskap**  
- Förstå arkitekturen och komponenterna i Windows AI Foundry-plattformen  
- Navigera genom hela AI-utvecklingslivscykeln inom Windows-ekosystemet  
- Implementera säkerhetsbästa praxis för AI-applikationer på enheten  
- Optimera applikationer för olika Windows hårdvarukonfigurationer  

**API-integrationskompetens**  
- Bemästra Windows AI API:er för text-, bild- och multimodala applikationer  
- Implementera Phi Silica-språkmodellintegration för textgenerering och resonemang  
- Distribuera datorseendefunktioner med inbyggda bildbehandlings-API:er  
- Anpassa förtränade modeller med LoRA-tekniker (Low-Rank Adaptation)  

**Foundry Local-implementering**  
- Bläddra, utvärdera och distribuera öppna språkmodeller med Foundry Local CLI  
- Förstå modelloptimering och kvantisering för lokal distribution  
- Implementera offline-AI-funktioner som fungerar utan internetanslutning  
- Hantera modellers livscykler och uppdateringar i produktionsmiljöer  

**Windows ML-distribution**  
- Ta med anpassade ONNX-modeller till Windows-applikationer med Windows ML  
- Dra nytta av automatisk hårdvaruacceleration över CPU-, GPU- och NPU-arkitekturer  
- Implementera realtidsinferens med optimal resursanvändning  
- Designa skalbara AI-applikationer för olika Windows-enhetskategorier  

### Applikationsutvecklingsfärdigheter

**Plattformsoberoende Windows-utveckling**  
- Bygg AI-drivna applikationer med .NET MAUI för universell Windows-distribution  
- Integrera AI-funktioner i Win32-, UWP- och progressiva webbapplikationer  
- Implementera responsiva UI-designs som anpassar sig till AI-bearbetningstillstånd  
- Hantera asynkrona AI-operationer med rätt användarupplevelsemönster  

**Prestandaoptimering**  
- Profilera och optimera AI-inferensprestanda över olika hårdvarukonfigurationer  
- Implementera effektiv minneshantering för stora språkmodeller  
- Designa applikationer som degraderar graciöst baserat på tillgängliga hårdvarukapaciteter  
- Använd cachingstrategier för ofta använda AI-operationer  

**Produktionsberedskap**  
- Implementera omfattande felhantering och fallback-mekanismer  
- Designa telemetri och övervakning för AI-applikationers prestanda  
- Använd säkerhetsbästa praxis för lokal AI-modellförvaring och exekvering  
- Planera distributionsstrategier för företags- och konsumentapplikationer  

### Affärs- och strategisk förståelse

**AI-applikationsarkitektur**  
- Designa hybridarkitekturer som optimerar mellan lokal och molnbaserad AI-bearbetning  
- Utvärdera avvägningar mellan modellstorlek, noggrannhet och inferenshastighet  
- Planera dataflödesarkitekturer som bibehåller integritet samtidigt som de möjliggör intelligens  
- Implementera kostnadseffektiva AI-lösningar som skalar med användarkrav  

**Marknadspositionering**  
- Förstå konkurrensfördelarna med Windows-inhemska AI-applikationer  
- Identifiera användningsfall där AI på enheten ger överlägsna användarupplevelser  
- Utveckla go-to-market-strategier för AI-förbättrade Windows-applikationer  
- Positionera applikationer för att dra nytta av Windows-ekosystemets fördelar  

## Windows App SDK AI-exempel

Windows App SDK tillhandahåller omfattande exempel som demonstrerar AI-integration över flera ramverk och distributionsscenarier. Dessa exempel är viktiga referenser för att förstå Windows AI-utvecklingsmönster.

### Windows AI Foundry-exempel

| Exempel | Ramverk | Fokusområde | Nyckelfunktioner |
|---------|---------|-------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API:er Integration | Komplett WinUI-app som demonstrerar Windows AI API:er, ARM64-optimering, paketerad distribution |

**Nyckelteknologier:**  
- Windows AI API:er  
- WinUI 3-ramverk  
- ARM64-plattformsoptimering  
- Copilot+ PC-kompatibilitet  
- Paketerad appdistribution  

**Förutsättningar:**  
- Windows 11 med Copilot+ PC rekommenderas  
- Visual Studio 2022  
- ARM64-byggkonfiguration  
- Windows App SDK 1.8.1+  

### Windows ML-exempel

#### C++-exempel

| Exempel | Typ | Fokusområde | Nyckelfunktioner |
|---------|-----|-------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolapp | Grundläggande Windows ML | EP-upptäckt, kommandoradsalternativ, modellkompilering |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolapp | Ramverksdistribution | Delad runtime, mindre distributionsfotavtryck |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolapp | Självständig distribution | Fristående distribution, inga runtime-beroenden |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Biblioteksanvändning | WindowsML i delat bibliotek, minneshantering |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet-handledning | Modellkonvertering, EP-kompilering, Build 2025-handledning |

#### C#-exempel

**Konsolapplikationer**

| Exempel | Typ | Fokusområde | Nyckelfunktioner |
|---------|-----|-------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsolapp | Grundläggande C#-integration | Delad hjälpanvändning, kommandoradsgränssnitt |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet-handledning | Modellkonvertering, EP-kompilering, Build 2025-handledning |

**GUI-applikationer**

| Exempel | Ramverk | Fokusområde | Nyckelfunktioner |
|---------|---------|-------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Bildklassificering med WPF-gränssnitt |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditionell GUI | Bildklassificering med Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | Bildklassificering med WinUI 3-gränssnitt |

#### Python-exempel

| Exempel | Språk | Fokusområde | Nyckelfunktioner |
|---------|-------|-------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Bildklassificering | WinML Python-bindningar, batchbildbearbetning |

### Förutsättningar för exempel

**Systemkrav:**  
- Windows 11 PC som kör version 24H2 (build 26100) eller senare  
- Visual Studio 2022 med C++- och .NET-arbetsbelastningar  
- Windows App SDK 1.8.1 eller senare  
- Python 3.10-3.13 för Python-exempel på x64- och ARM64-enheter  

**Windows AI Foundry-specifikt:**  
- Copilot+ PC rekommenderas för optimal prestanda  
- ARM64-byggkonfiguration för Windows AI-exempel  
- Paketidentitet krävs (opacketerade appar stöds inte längre)  

### Vanligt arbetsflöde för exempel

De flesta Windows ML-exempel följer detta standardmönster:

1. **Initiera miljö** - Skapa ONNX Runtime-miljö  
2. **Registrera exekveringsleverantörer** - Upptäck och registrera tillgängliga hårdvaruacceleratorer (CPU, GPU, NPU)  
3. **Ladda modell** - Ladda ONNX-modell, eventuellt kompilera för målplattform  
4. **Förbehandla indata** - Konvertera bilder/data till modellens indataformat  
5. **Kör inferens** - Kör modellen och få förutsägelser  
6. **Bearbeta resultat** - Använd softmax och visa toppförutsägelser  

### Modellfiler som används

| Modell | Syfte | Ingår | Anteckningar |
|-------|-------|-------|--------------|
| SqueezeNet | Lätt bildklassificering | ✅ Ingår | Förtränad, redo att användas |
| ResNet-50 | Bildklassificering med hög noggrannhet | ❌ Kräver konvertering | Använd [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) för konvertering |

### Hårdvarustöd

Alla exempel upptäcker och använder automatiskt tillgänglig hårdvara:  
- **CPU** - Universellt stöd över alla Windows-enheter  
- **GPU** - Automatisk upptäckt och optimering för tillgänglig grafikmaskinvara  
- **NPU** - Utnyttjar neurala processorenheter på stödda enheter (Copilot+ PCs)  

## Windows AI Foundry-plattformskomponenter

### 1. Windows AI API:er

Windows AI API:er tillhandahåller färdiga AI-funktioner som drivs av modeller på enheten, optimerade för effektivitet och prestanda på Copilot+ PC-enheter med minimal installationskrav.

#### Kärnkategorier för API:er

**Phi Silica-språkmodell**  
- Liten men kraftfull språkmodell för textgenerering och resonemang  
- Optimerad för realtidsinferens med minimal strömförbrukning  
- Stöd för anpassad finjustering med LoRA-tekniker  
- Integration med Windows semantisk sökning och kunskapsinhämtning  

**Datorseende-API:er**  
- **Textigenkänning (OCR)**: Extrahera text från bilder med hög noggrannhet  
- **Bildsuperupplösning**: Skala upp bilder med lokala AI-modeller  
- **Bildsegmentering**: Identifiera och isolera specifika objekt i bilder  
- **Bildbeskrivning**: Generera detaljerade textbeskrivningar för visuellt innehåll  
- **Objektborttagning**: Ta bort oönskade objekt från bilder med AI-driven inpainting  

**Multimodala funktioner**  
- **Integration av bild och text**: Kombinera text- och bildförståelse  
- **Semantisk sökning**: Möjliggör naturliga språkfrågor över multimedia-innehåll  
- **Kunskapsinhämtning**: Bygg intelligenta sökupplevelser med lokal data  

### 2. Foundry Local

Foundry Local ger utvecklare snabb tillgång till färdiga öppna språkmodeller på Windows Silicon, med möjlighet att bläddra, testa, interagera och distribuera modeller i lokala applikationer.

#### Foundry Local-exempelapplikationer

[Foundry Local-repositoriet](https://github.com/microsoft/Foundry-Local/tree/main/samples) tillhandahåller omfattande exempel över flera programmeringsspråk och ramverk, som demonstrerar olika integrationsmönster och användningsfall.

| Exempel | Språk/Ramverk | Fokusområde | Nyckelfunktioner |
|---------|---------------|-------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG-implementering | Semantisk Kernel-integration, Qdrant vektorlagring, JINA-embeddingar, dokumentingestion, streamingchatt |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop-chattapp | Plattformoberoende chatt, lokal/molnmodellväxling, OpenAI SDK-integration, realtidsstreaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Grundläggande integration | Enkel SDK-användning, modellinitiering, grundläggande chattfunktionalitet |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Grundläggande integration | Python SDK-användning, streamingrespons, OpenAI-kompatibel API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Systemintegration | Låg nivå SDK-användning, asynkrona operationer, reqwest HTTP-klient |

#### Exempelkategorier efter användningsområde

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Komplett RAG-implementering med Semantic Kernel, Qdrant vektordatabas och JINA-embeddingar
- **Arkitektur**: Dokumentingestion → Textuppdelning → Vektorembeddingar → Likhetssökning → Kontextmedvetna svar
- **Teknologier**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX-embeddingar, strömmande chattkomplettering

**Skrivbordsapplikationer**
- **electron/foundry-chat**: Produktionsklar chattapplikation med lokal/molnmodellväxling
- **Funktioner**: Modellväljare, strömmande svar, felhantering, plattformsoberoende distribution
- **Arkitektur**: Electron huvudprocess, IPC-kommunikation, säkra förladdningsskript

**Exempel på SDK-integration**
- **JavaScript (Node.js)**: Grundläggande modellinteraktion och strömmande svar
- **Python**: OpenAI-kompatibel API-användning med asynkron strömning
- **Rust**: Låg nivå-integration med reqwest och tokio för asynkrona operationer

#### Förutsättningar för Foundry Local-exempel

**Systemkrav:**
- Windows 11 med Foundry Local installerat
- Node.js v16+ för JavaScript/Electron-exempel
- .NET 8.0+ för C#-exempel
- Python 3.10+ för Python-exempel
- Rust 1.70+ för Rust-exempel

**Installation:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Exempelspecifik konfiguration

**dotNET RAG-exempel:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat-exempel:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust-exempel:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Nyckelfunktioner

**Modellkatalog**
- Omfattande samling av föroptimerade open source-modeller
- Modeller optimerade för CPU, GPU och NPU för omedelbar distribution
- Stöd för populära modellfamiljer inklusive Llama, Mistral, Phi och specialiserade domänmodeller

**CLI-integration**
- Kommandoradsgränssnitt för modellhantering och distribution
- Automatiserade optimerings- och kvantiseringsarbetsflöden
- Integration med populära utvecklingsmiljöer och CI/CD-pipelines

**Lokal distribution**
- Fullständig offlinefunktionalitet utan molnberoenden
- Stöd för anpassade modellformat och konfigurationer
- Effektiv modellservering med automatisk hårdvaruoptimering

### 3. Windows ML

Windows ML fungerar som den centrala AI-plattformen och integrerade inferensmotorn på Windows, vilket gör det möjligt för utvecklare att effektivt distribuera anpassade modeller över det breda Windows-hårdvaruekosystemet.

#### Arkitekturella fördelar

**Universellt hårdvarustöd**
- Automatisk optimering för AMD-, Intel-, NVIDIA- och Qualcomm-silikon
- Stöd för CPU-, GPU- och NPU-exekvering med transparent växling
- Hårdvaruabstraktion som eliminerar plattformspecifik optimeringsarbete

**Modellflexibilitet**
- Stöd för ONNX-modellformat med automatisk konvertering från populära ramverk
- Anpassad modelldistribution med produktionsklassad prestanda
- Integration med befintliga Windows-applikationsarkitekturer

**Företagsintegration**
- Kompatibel med Windows säkerhets- och efterlevnadsramverk
- Stöd för företagsdistribution och hanteringsverktyg
- Integration med Windows enhetshantering och övervakningssystem

## Utvecklingsarbetsflöde

### Fas 1: Miljöinställning och verktygskonfiguration

**Förberedelse av utvecklingsmiljö**
1. Installera Visual Studio 2022 med C++- och .NET-arbetsbelastningar
2. Installera Windows App SDK 1.8.1 eller senare
3. Konfigurera Windows AI Foundry CLI-verktyg
4. Ställ in AI Toolkit-tillägg för Visual Studio Code
5. Etablera verktyg för prestandaprofilering och övervakning
6. Säkerställ ARM64-byggkonfiguration för Copilot+ PC-optimering

**Exempelarkivinställning**
1. Klona [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigera till `Samples/WindowsAIFoundry/cs-winui` för Windows AI API-exempel
3. Navigera till `Samples/WindowsML` för omfattande Windows ML-exempel
4. Granska [byggkrav](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) för dina målplattformar

**Utforska AI Dev Gallery**
- Utforska exempelapplikationer och referensimplementeringar
- Testa Windows AI API:er med interaktiva demonstrationer
- Granska källkod för bästa praxis och mönster
- Identifiera relevanta exempel för ditt specifika användningsområde

### Fas 2: Modellval och integration

**Kravanalys**
- Definiera funktionella krav för AI-funktioner
- Etablera prestandabegränsningar och optimeringsmål
- Utvärdera integritets- och säkerhetskrav
- Planera distributionsarkitektur och skalningsstrategier

**Modellevaluering**
- Använd Foundry Local för att testa open source-modeller för ditt användningsområde
- Benchmarka Windows AI API:er mot anpassade modellkrav
- Utvärdera avvägningar mellan modellstorlek, noggrannhet och inferenshastighet
- Prototypa integrationsmetoder med valda modeller

### Fas 3: Applikationsutveckling

**Kärnintegration**
- Implementera Windows AI API-integration med korrekt felhantering
- Designa användargränssnitt som rymmer AI-bearbetningsarbetsflöden
- Implementera cache- och optimeringsstrategier för modellinferens
- Lägg till telemetri och övervakning för AI-prestanda

**Testning och validering**
- Testa applikationer över olika Windows-hårdvarukonfigurationer
- Validera prestandamått under olika belastningsförhållanden
- Implementera automatiserad testning för AI-funktioners tillförlitlighet
- Genomför användarupplevelsetestning med AI-förbättrade funktioner

### Fas 4: Optimering och distribution

**Prestandaoptimering**
- Profilera applikationsprestanda över målplattformar
- Optimera minnesanvändning och modellinläsningsstrategier
- Implementera adaptivt beteende baserat på tillgängliga hårdvarukapaciteter
- Finjustera användarupplevelsen för olika prestandascenarier

**Produktionsdistribution**
- Paketera applikationer med korrekta AI-modellberoenden
- Implementera uppdateringsmekanismer för modeller och applikationslogik
- Konfigurera övervakning och analys för produktionsmiljöer
- Planera utrullningsstrategier för företags- och konsumentdistributioner

## Praktiska implementeringsexempel

### Exempel 1: Intelligent dokumentbearbetningsapplikation

Bygg en Windows-applikation som bearbetar dokument med flera AI-funktioner:

**Använda teknologier:**
- Phi Silica för dokumentsammanfattning och frågesvar
- OCR API:er för textutvinning från skannade dokument
- Bildbeskrivnings-API:er för analys av diagram och grafer
- Anpassade ONNX-modeller för dokumentklassificering

**Implementeringsmetod:**
- Designa modulär arkitektur med pluggbara AI-komponenter
- Implementera asynkron bearbetning för stora dokumentbatcher
- Lägg till progressindikatorer och avbrytningsstöd för långvariga operationer
- Inkludera offlinefunktionalitet för känslig dokumentbearbetning

### Exempel 2: Detaljhandelsinventeringshanteringssystem

Skapa ett AI-drivet inventeringssystem för detaljhandelsapplikationer:

**Använda teknologier:**
- Bildsegmentering för produktidentifiering
- Anpassade visionsmodeller för varumärkes- och kategoriklassificering
- Foundry Local-distribution av specialiserade detaljhandelsmodeller
- Integration med befintliga POS- och inventeringssystem

**Implementeringsmetod:**
- Bygg kameraintegration för realtidsproduktskanning
- Implementera streckkod- och visuell produktigenkänning
- Lägg till naturliga språkfrågor för inventering med lokala språkmodeller
- Designa skalbar arkitektur för distribution över flera butiker

### Exempel 3: Dokumentationsassistent för sjukvården

Utveckla ett integritetsbevarande dokumentationsverktyg för sjukvården:

**Använda teknologier:**
- Phi Silica för medicinsk anteckningsgenerering och kliniskt beslutsstöd
- OCR för digitalisering av handskrivna medicinska journaler
- Anpassade medicinska språkmodeller distribuerade via Windows ML
- Lokal vektorlagring för medicinsk kunskapsåtervinning

**Implementeringsmetod:**
- Säkerställ fullständig offlinefunktionalitet för patientintegritet
- Implementera validering och förslag för medicinsk terminologi
- Lägg till revisionsloggning för regelöverensstämmelse
- Designa integration med befintliga elektroniska patientjournalsystem

## Prestandaoptimeringsstrategier

### Hårdvarumedveten utveckling

**NPU-optimering**
- Designa applikationer för att utnyttja NPU-kapaciteter på Copilot+ PC
- Implementera smidig fallback till GPU/CPU på enheter utan NPU
- Optimera modellformat för NPU-specifik acceleration
- Övervaka NPU-användning och termiska egenskaper

**Minneshantering**
- Implementera effektiva modellinläsnings- och cachestrategier
- Använd minnesmappning för stora modeller för att minska starttiden
- Designa minnesmedvetna applikationer för resursbegränsade enheter
- Implementera modellkvantisering för minnesoptimering

**Batterieffektivitet**
- Optimera AI-operationer för minimal strömförbrukning
- Implementera adaptiv bearbetning baserat på batteristatus
- Designa effektiv bakgrundsbearbetning för kontinuerliga AI-operationer
- Använd verktyg för strömprofilering för att optimera energianvändning

### Skalbarhetsöverväganden

**Multitrådning**
- Designa trådsäkra AI-operationer för samtidig bearbetning
- Implementera effektiv arbetsfördelning över tillgängliga kärnor
- Använd async/await-mönster för icke-blockerande AI-operationer
- Planera optimering av trådpooler för olika hårdvarukonfigurationer

**Cachestrategier**
- Implementera intelligent cache för ofta använda AI-operationer
- Designa cacheinvalideringsstrategier för modelluppdateringar
- Använd persistent cache för dyra förbearbetningsoperationer
- Implementera distribuerad cache för scenarier med flera användare

## Säkerhets- och integritetsbästa praxis

### Dataskydd

**Lokal bearbetning**
- Säkerställ att känslig data aldrig lämnar den lokala enheten
- Implementera säker lagring för AI-modeller och temporär data
- Använd Windows säkerhetsfunktioner för applikationssandboxning
- Tillämpa kryptering för lagrade modeller och mellanliggande bearbetningsresultat

**Modellsäkerhet**
- Validera modellintegritet före inläsning och exekvering
- Implementera säkra modelluppdateringsmekanismer
- Använd signerade modeller för att förhindra manipulering
- Tillämpa åtkomstkontroller för modellfiler och konfiguration

### Efterlevnadsöverväganden

**Regulatorisk anpassning**
- Designa applikationer för att uppfylla GDPR, HIPAA och andra regulatoriska krav
- Implementera revisionsloggning för AI-beslutsprocesser
- Tillhandahåll transparensfunktioner för AI-genererade resultat
- Möjliggör användarkontroll över AI-databearbetning

**Företagssäkerhet**
- Integrera med Windows företags säkerhetspolicyer
- Stöd hanterad distribution via företags hanteringsverktyg
- Implementera rollbaserade åtkomstkontroller för AI-funktioner
- Tillhandahåll administrativa kontroller för AI-funktionalitet

## Felsökning och debugging

### Vanliga utvecklingsutmaningar

**Byggkonfigurationsproblem**
- Säkerställ ARM64-plattformsinställning för Windows AI API-exempel
- Verifiera kompatibilitet med Windows App SDK-version (1.8.1+ krävs)
- Kontrollera att paketidentitet är korrekt konfigurerad (krävs för Windows AI API:er)
- Validera att byggverktyg stöder målramverksversionen

**Modellinläsningsproblem**
- Validera ONNX-modellkompatibilitet med Windows ML
- Kontrollera modellfilens integritet och formatkrav
- Verifiera hårdvarukapacitetskrav för specifika modeller
- Debugga minnesallokeringsproblem under modellinläsning
- Säkerställ registrering av exekveringsleverantör för hårdvaruacceleration

**Distributionslägesöverväganden**
- **Självständigt läge**: Fullt stöd med större distributionsstorlek
- **Ramverksberoende läge**: Mindre fotavtryck men kräver delad runtime
- **Opackade applikationer**: Stöds inte längre för Windows AI API:er
- Använd `dotnet run -p:Platform=ARM64 -p:SelfContained=true` för självständig ARM64-distribution

**Prestandaproblem**
- Profilera applikationsprestanda över olika hårdvarukonfigurationer
- Identifiera flaskhalsar i AI-bearbetningspipelines
- Optimera dataförbearbetning och efterbearbetning
- Implementera prestandaövervakning och varningar

**Integrationssvårigheter**
- Debugga API-integrationsproblem med korrekt felhantering
- Validera inmatningsdataformat och förbearbetningskrav
- Testa kantfall och felvillkor noggrant
- Implementera omfattande loggning för felsökning av produktionsproblem

### Debuggingverktyg och tekniker

**Visual Studio-integration**
- Använd AI Toolkit-debugger för analys av modellexekvering
- Implementera prestandaprofilering för AI-operationer
- Debugga asynkrona AI-operationer med korrekt undantagshantering
- Använd minnesprofilering för optimering

**Windows AI Foundry-verktyg**
- Utnyttja Foundry Local CLI för modelltestning och validering
- Använd Windows AI API-testverktyg för integrationsverifiering
- Implementera anpassad loggning för övervakning av AI-operationer
- Skapa automatiserad testning för AI-funktioners tillförlitlighet

## Framtidssäkring av dina applikationer

### Framväxande teknologier

**Nästa generations hårdvara**
- Designa applikationer för att utnyttja framtida NPU-kapaciteter
- Planera för ökade modellstorlekar och komplexitet
- Implementera adaptiva arkitekturer för utvecklande hårdvara
- Överväg kvantberäkningsklara algoritmer för framtida kompatibilitet

**Avancerade AI-funktioner**
- Förbered för multimodal AI-integration över fler datatyper
- Planera för realtids samarbets-AI mellan flera enheter
- Designa för federerade inlärningsfunktioner
- Överväg hybridintelligensarkitekturer mellan edge och moln

### Kontinuerligt lärande och anpassning

**Modelluppdateringar**
- Implementera sömlösa mekanismer för modelluppdateringar
- Designa applikationer för att anpassa sig till förbättrade modellfunktioner
- Planera för bakåtkompatibilitet med befintliga modeller
- Implementera A/B-testning för utvärdering av modellprestanda

**Funktionsutveckling**
- Designa modulära arkitekturer som rymmer nya AI-funktioner
- Planera för integration av framväxande Windows AI API:er
- Implementera funktionsflaggor för gradvis kapabilitetsutrullning
- Designa användargränssnitt som anpassar sig till förbättrade AI-funktioner

## Slutsats

Windows Edge AI-utveckling representerar konvergensen av kraftfulla AI-funktioner med den robusta, säkra och skalbara Windows-plattformen. Genom att bemästra Windows AI Foundry-ekosystemet kan utvecklare skapa intelligenta applikationer som erbjuder exceptionella användarupplevelser samtidigt som de upprätthåller högsta standard för integritet, säkerhet och prestanda.

Kombinationen av Windows AI API:er, Foundry Local och Windows ML ger en oöverträffad grund för att bygga nästa generation av intelligenta Windows-applikationer. När AI fortsätter att utvecklas säkerställer Windows-plattformen att dina applik
- [Windows ML Översikt](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Systemkrav för Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Konfigurera utvecklingsmiljö för Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Exempel på kod och repositories
- [Windows App SDK Exempel - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Exempel - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Inferens Exempel](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Exempel Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Utvecklingsverktyg
- [AI Toolkit för Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Exempel](https://learn.microsoft.com/windows/ai/samples/)
- [Verktyg för modellkonvertering](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Teknisk support
- [Windows ML Dokumentation](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentation](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentation](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Rapportera problem - Windows App SDK Exempel](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Community och support
- [Windows Utvecklarcommunity](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogg](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Utbildning](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Denna guide är utformad för att utvecklas i takt med det snabbt framväxande Windows AI-ekosystemet. Regelbundna uppdateringar säkerställer att den är i linje med de senaste plattformsfunktionerna och bästa praxis för utveckling.*

[08. Praktisk erfarenhet med Microsoft Foundry Local - Komplett utvecklarverktyg](../Module08/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.