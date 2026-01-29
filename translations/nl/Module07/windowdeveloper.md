# Windows Edge AI Ontwikkelingsgids

## Introductie

Welkom bij Windows Edge AI Ontwikkeling - jouw uitgebreide gids voor het bouwen van intelligente applicaties die gebruikmaken van on-device AI via het Windows AI Foundry-platform van Microsoft. Deze gids is speciaal ontworpen voor Windows-ontwikkelaars die geavanceerde Edge AI-functionaliteiten willen integreren in hun applicaties, terwijl ze profiteren van de volledige hardwareversnelling van Windows.

### Het Windows AI Voordeel

Windows AI Foundry biedt een verenigd, betrouwbaar en veilig platform dat de volledige AI-ontwikkelingscyclus ondersteunt - van modelselectie en verfijning tot optimalisatie en implementatie op CPU-, GPU-, NPU- en hybride cloudarchitecturen. Dit platform democratiseert AI-ontwikkeling door het volgende te bieden:

- **Hardwareabstractie**: Naadloze implementatie op AMD-, Intel-, NVIDIA- en Qualcomm-silicium
- **On-Device Intelligentie**: Privacyvriendelijke AI die volledig op lokale hardware draait
- **Geoptimaliseerde Prestaties**: Modellen vooraf geoptimaliseerd voor Windows-hardwareconfiguraties
- **Enterprise-Klaar**: Productiekwaliteit beveiliging en compliancefuncties

### Windows ML 
Windows Machine Learning (ML) stelt C#-, C++- en Python-ontwikkelaars in staat om ONNX AI-modellen lokaal op Windows-pc's uit te voeren via de ONNX Runtime, met automatische uitvoeringproviderbeheer voor verschillende hardware (CPU's, GPU's, NPU's). [ONNX Runtime](https://onnxruntime.ai/docs/) kan worden gebruikt met modellen van PyTorch, Tensorflow/Keras, TFLite, scikit-learn en andere frameworks.

![WindowsML Een diagram dat een ONNX-model illustreert dat via Windows ML naar NPU's, GPU's en CPU's gaat.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML biedt een gedeelde Windows-brede kopie van de ONNX Runtime, plus de mogelijkheid om dynamisch uitvoeringsproviders (EP's) te downloaden.

### Waarom Windows voor Edge AI?

**Universele Hardwareondersteuning**
Windows ML biedt automatische hardwareoptimalisatie in het hele Windows-ecosysteem, zodat jouw AI-applicaties optimaal presteren, ongeacht de onderliggende siliciumarchitectuur.

**Geïntegreerde AI Runtime**
De ingebouwde Windows ML-inferentie-engine elimineert complexe installatievereisten, waardoor ontwikkelaars zich kunnen concentreren op applicatielogica in plaats van infrastructuurproblemen.

**Copilot+ PC Optimalisatie**
Speciaal ontworpen API's voor de nieuwste generatie Windows-apparaten met toegewijde Neural Processing Units (NPU's) die uitzonderlijke prestaties per watt leveren.

**Ontwikkelaar Ecosysteem**
Rijke tools, waaronder Visual Studio-integratie, uitgebreide documentatie en voorbeeldapplicaties die ontwikkelingscycli versnellen.

## Leerdoelen

Door deze Windows Edge AI ontwikkelingsgids te voltooien, beheers je de essentiële vaardigheden voor het bouwen van productieklare AI-applicaties op het Windows-platform.

### Kerntechnische Competenties

**Windows AI Foundry Beheersing**
- Begrijp de architectuur en componenten van het Windows AI Foundry-platform
- Navigeer door de volledige AI-ontwikkelingscyclus binnen het Windows-ecosysteem
- Implementeer beveiligingsbest practices voor on-device AI-applicaties
- Optimaliseer applicaties voor verschillende Windows-hardwareconfiguraties

**API Integratie Expertise**
- Beheers Windows AI API's voor tekst-, visuele en multimodale applicaties
- Implementeer Phi Silica taalmodelintegratie voor tekstgeneratie en redenering
- Implementeer computervisiefunctionaliteiten met ingebouwde beeldverwerkings-API's
- Pas vooraf getrainde modellen aan met LoRA (Low-Rank Adaptation) technieken

**Foundry Local Implementatie**
- Blader door, evalueer en implementeer open-source taalmodellen met Foundry Local CLI
- Begrijp modeloptimalisatie en kwantisering voor lokale implementatie
- Implementeer offline AI-functionaliteiten die werken zonder internetverbinding
- Beheer modellevenscycli en updates in productieomgevingen

**Windows ML Implementatie**
- Breng aangepaste ONNX-modellen naar Windows-applicaties met Windows ML
- Maak gebruik van automatische hardwareversnelling op CPU-, GPU- en NPU-architecturen
- Implementeer real-time inferentie met optimale hulpbronnenbenutting
- Ontwerp schaalbare AI-applicaties voor diverse Windows-apparaatcategorieën

### Applicatieontwikkelingsvaardigheden

**Cross-Platform Windows Ontwikkeling**
- Bouw AI-aangedreven applicaties met .NET MAUI voor universele Windows-implementatie
- Integreer AI-functionaliteiten in Win32-, UWP- en Progressive Web Applications
- Implementeer responsieve UI-ontwerpen die zich aanpassen aan AI-verwerkingsstatussen
- Behandel asynchrone AI-operaties met passende gebruikerservaringspatronen

**Prestatieoptimalisatie**
- Profiel en optimaliseer AI-inferentieprestaties op verschillende hardwareconfiguraties
- Implementeer efficiënt geheugenbeheer voor grote taalmodellen
- Ontwerp applicaties die gracieus degraderen op basis van beschikbare hardwaremogelijkheden
- Pas cachingstrategieën toe voor vaak gebruikte AI-operaties

**Productieklaar**
- Implementeer uitgebreide foutafhandeling en fallbackmechanismen
- Ontwerp telemetrie en monitoring voor AI-applicatieprestaties
- Pas beveiligingsbest practices toe voor lokale AI-modelopslag en uitvoering
- Plan implementatiestrategieën voor zakelijke en consumententoepassingen

### Zakelijke en Strategische Inzichten

**AI Applicatie Architectuur**
- Ontwerp hybride architecturen die optimaliseren tussen lokale en cloud AI-verwerking
- Evalueer afwegingen tussen modelgrootte, nauwkeurigheid en inferentiesnelheid
- Plan datastroomarchitecturen die privacy behouden terwijl ze intelligentie mogelijk maken
- Implementeer kosteneffectieve AI-oplossingen die schalen met gebruikersvraag

**Marktpositionering**
- Begrijp de concurrentievoordelen van Windows-native AI-applicaties
- Identificeer use cases waar on-device AI superieure gebruikerservaringen biedt
- Ontwikkel go-to-market strategieën voor AI-verrijkte Windows-applicaties
- Positioneer applicaties om te profiteren van de voordelen van het Windows-ecosysteem

## Windows App SDK AI Voorbeelden

De Windows App SDK biedt uitgebreide voorbeelden die AI-integratie demonstreren in meerdere frameworks en implementatiescenario's. Deze voorbeelden zijn essentiële referenties voor het begrijpen van Windows AI-ontwikkelingspatronen.

### Windows AI Foundry Voorbeelden

| Voorbeeld | Framework | Focusgebied | Belangrijke Functies |
|-----------|-----------|-------------|-----------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API's Integratie | Complete WinUI-app die Windows AI API's demonstreert, ARM64-optimalisatie, verpakte implementatie |

**Belangrijke Technologieën:**
- Windows AI API's
- WinUI 3 framework
- ARM64 platformoptimalisatie
- Copilot+ PC compatibiliteit
- Verpakte app-implementatie

**Vereisten:**
- Windows 11 met Copilot+ PC aanbevolen
- Visual Studio 2022
- ARM64 buildconfiguratie
- Windows App SDK 1.8.1+

### Windows ML Voorbeelden

#### C++ Voorbeelden

| Voorbeeld | Type | Focusgebied | Belangrijke Functies |
|-----------|------|-------------|-----------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Basis Windows ML | EP-ontdekking, command-line opties, modelcompilatie |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Framework Implementatie | Gedeelde runtime, kleinere implementatievoetafdruk |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | Zelfstandige Implementatie | Standalone implementatie, geen runtime-afhankelijkheden |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Bibliotheekgebruik | WindowsML in gedeelde bibliotheek, geheugenbeheer |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet Tutorial | Modelconversie, EP-compilatie, Build 2025 tutorial |

#### C# Voorbeelden

**Console Applicaties**

| Voorbeeld | Type | Focusgebied | Belangrijke Functies |
|-----------|------|-------------|-----------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Console App | Basis C# Integratie | Gedeeld helpergebruik, command-line interface |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet Tutorial | Modelconversie, EP-compilatie, Build 2025 tutorial |

**GUI Applicaties**

| Voorbeeld | Framework | Focusgebied | Belangrijke Functies |
|-----------|-----------|-------------|-----------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Beeldclassificatie met WPF-interface |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditionele GUI | Beeldclassificatie met Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderne GUI | Beeldclassificatie met WinUI 3-interface |

#### Python Voorbeelden

| Voorbeeld | Taal | Focusgebied | Belangrijke Functies |
|-----------|------|-------------|-----------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Beeldclassificatie | WinML Python bindings, batch beeldverwerking |

### Voorbeeldvereisten

**Systeemvereisten:**
- Windows 11-pc met versie 24H2 (build 26100) of hoger
- Visual Studio 2022 met C++ en .NET workloads
- Windows App SDK 1.8.1 of later
- Python 3.10-3.13 voor Python-voorbeelden op x64 en ARM64-apparaten

**Windows AI Foundry Specifiek:**
- Copilot+ PC aanbevolen voor optimale prestaties
- ARM64 buildconfiguratie voor Windows AI-voorbeelden
- Pakketidentiteit vereist (niet-verpakte apps worden niet langer ondersteund)

### Algemene Voorbeeldworkflow

De meeste Windows ML-voorbeelden volgen dit standaardpatroon:

1. **Initialiseer Omgeving** - Maak ONNX Runtime-omgeving
2. **Registreer Uitvoeringsproviders** - Ontdek en registreer beschikbare hardwareversnellers (CPU, GPU, NPU)
3. **Laad Model** - Laad ONNX-model, optioneel compileren voor doelhardware
4. **Voorverwerk Invoer** - Converteer afbeeldingen/data naar modelinvoerformaat
5. **Voer Inferentie Uit** - Voer model uit en verkrijg voorspellingen
6. **Verwerk Resultaten** - Pas softmax toe en toon topvoorspellingen

### Gebruikte Modelfiles

| Model | Doel | Inbegrepen | Opmerkingen |
|-------|------|------------|-------------|
| SqueezeNet | Lichtgewicht beeldclassificatie | ✅ Inbegrepen | Vooraf getraind, klaar voor gebruik |
| ResNet-50 | Hoge nauwkeurigheid beeldclassificatie | ❌ Vereist conversie | Gebruik [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) voor conversie |

### Hardwareondersteuning

Alle voorbeelden detecteren en gebruiken automatisch beschikbare hardware:
- **CPU** - Universele ondersteuning op alle Windows-apparaten
- **GPU** - Automatische detectie en optimalisatie voor beschikbare grafische hardware
- **NPU** - Maakt gebruik van Neural Processing Units op ondersteunde apparaten (Copilot+ pc's)

## Windows AI Foundry Platformcomponenten

### 1. Windows AI API's

Windows AI API's bieden kant-en-klare AI-functionaliteiten aangedreven door on-device modellen, geoptimaliseerd voor efficiëntie en prestaties op Copilot+ pc-apparaten met minimale installatievereisten.

#### Kern API-categorieën

**Phi Silica Taalmodel**
- Klein maar krachtig taalmodel voor tekstgeneratie en redenering
- Geoptimaliseerd voor real-time inferentie met minimaal energieverbruik
- Ondersteuning voor aangepaste verfijning met LoRA-technieken
- Integratie met Windows semantische zoekopdrachten en kennisophaling

**Computervisie API's**
- **Tekstherkenning (OCR)**: Haal tekst uit afbeeldingen met hoge nauwkeurigheid
- **Beeldsuperresolutie**: Schaal afbeeldingen op met lokale AI-modellen
- **Beeldsegmentatie**: Identificeer en isoleer specifieke objecten in afbeeldingen
- **Beeldbeschrijving**: Genereer gedetailleerde tekstbeschrijvingen voor visuele inhoud
- **Objectverwijdering**: Verwijder ongewenste objecten uit afbeeldingen met AI-aangedreven inpainting

**Multimodale Functionaliteiten**
- **Visie-Taal Integratie**: Combineer tekst- en beeldbegrip
- **Semantische Zoekopdrachten**: Maak natuurlijke taalvragen mogelijk over multimedia-inhoud
- **Kennisophaling**: Bouw intelligente zoekervaringen met lokale data

### 2. Foundry Local

Foundry Local biedt ontwikkelaars snelle toegang tot kant-en-klare open-source taalmodellen op Windows Silicon, met de mogelijkheid om modellen te bekijken, testen, gebruiken en implementeren in lokale applicaties.

#### Foundry Local Voorbeeldapplicaties

De [Foundry Local repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) biedt uitgebreide voorbeelden in meerdere programmeertalen en frameworks, die verschillende integratiepatronen en use cases demonstreren.

| Voorbeeld | Taal/Framework | Focusgebied | Belangrijke Functies |
|-----------|----------------|-------------|-----------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG Implementatie | Semantische Kernel-integratie, Qdrant vector store, JINA embeddings, documentinvoer, streaming chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop Chat App | Cross-platform chat, lokaal/cloud modelwisseling, OpenAI SDK-integratie, real-time streaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Basisintegratie | Eenvoudig SDK-gebruik, modelinitialisatie, basis chatfunctionaliteit |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Basisintegratie | Python SDK-gebruik, streaming reacties, OpenAI-compatibele API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Systeemintegratie | Gebruik van low-level SDK, asynchrone operaties, reqwest HTTP-client |

#### Voorbeeldcategorieën op basis van gebruiksscenario

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Volledige RAG-implementatie met Semantic Kernel, Qdrant vector database en JINA embeddings
- **Architectuur**: Documentinvoer → Tekst opdelen → Vector embeddings → Gelijkeniszoektocht → Contextbewuste antwoorden
- **Technologieën**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, streaming chat voltooiing

**Desktoptoepassingen**
- **electron/foundry-chat**: Productieklaar chatprogramma met lokale/cloud modelwisseling
- **Functies**: Modelkiezer, streaming antwoorden, foutafhandeling, cross-platform implementatie
- **Architectuur**: Electron hoofdproces, IPC-communicatie, veilige preload scripts

**Voorbeelden van SDK-integratie**
- **JavaScript (Node.js)**: Basisinteractie met modellen en streaming antwoorden
- **Python**: OpenAI-compatibele API-gebruik met asynchrone streaming
- **Rust**: Low-level integratie met reqwest en tokio voor asynchrone operaties

#### Vereisten voor Foundry Local-voorbeelden

**Systeemvereisten:**
- Windows 11 met Foundry Local geïnstalleerd
- Node.js v16+ voor JavaScript/Electron-voorbeelden
- .NET 8.0+ voor C#-voorbeelden
- Python 3.10+ voor Python-voorbeelden
- Rust 1.70+ voor Rust-voorbeelden

**Installatie:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Specifieke setup voor voorbeelden

**dotNET RAG Voorbeeld:**
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

**Electron Chat Voorbeeld:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust Voorbeelden:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Belangrijke functies

**Modelcatalogus**
- Uitgebreide verzameling vooraf geoptimaliseerde open-source modellen
- Modellen geoptimaliseerd voor CPU's, GPU's en NPU's voor directe implementatie
- Ondersteuning voor populaire modelfamilies zoals Llama, Mistral, Phi en gespecialiseerde domeinmodellen

**CLI-integratie**
- Command-line interface voor modelbeheer en implementatie
- Geautomatiseerde optimalisatie- en kwantisatieworkflows
- Integratie met populaire ontwikkelomgevingen en CI/CD-pijplijnen

**Lokale implementatie**
- Volledig offline werken zonder afhankelijkheid van de cloud
- Ondersteuning voor aangepaste modelformaten en configuraties
- Efficiënte modelservering met automatische hardwareoptimalisatie

### 3. Windows ML

Windows ML fungeert als het kern-AI-platform en geïntegreerde inferentieruntime op Windows, waarmee ontwikkelaars aangepaste modellen efficiënt kunnen implementeren binnen het brede Windows-hardware-ecosysteem.

#### Voordelen van de architectuur

**Universele hardwareondersteuning**
- Automatische optimalisatie voor AMD-, Intel-, NVIDIA- en Qualcomm-silicium
- Ondersteuning voor CPU-, GPU- en NPU-uitvoering met transparante schakeling
- Hardwareabstractie die platformspecifiek optimalisatiewerk elimineert

**Model flexibiliteit**
- Ondersteuning voor ONNX-modelformaat met automatische conversie vanuit populaire frameworks
- Implementatie van aangepaste modellen met prestaties van productieniveau
- Integratie met bestaande Windows-toepassingsarchitecturen

**Enterprise-integratie**
- Compatibel met Windows beveiligings- en nalevingskaders
- Ondersteuning voor implementatie- en beheertools voor ondernemingen
- Integratie met Windows-apparaatbeheer en monitoringsystemen

## Ontwikkelworkflow

### Fase 1: Omgevingsinstelling en toolconfiguratie

**Voorbereiding van ontwikkelomgeving**
1. Installeer Visual Studio 2022 met C++- en .NET-workloads
2. Installeer Windows App SDK 1.8.1 of later
3. Configureer Windows AI Foundry CLI-tools
4. Stel AI Toolkit-extensie in voor Visual Studio Code
5. Stel tools in voor prestatieprofilering en monitoring
6. Zorg voor ARM64-buildconfiguratie voor Copilot+ PC-optimalisatie

**Setup van voorbeeldrepository**
1. Clone de [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigeer naar `Samples/WindowsAIFoundry/cs-winui` voor Windows AI API-voorbeelden
3. Navigeer naar `Samples/WindowsML` voor uitgebreide Windows ML-voorbeelden
4. Bekijk de [buildvereisten](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) voor uw doelplatforms

**Verkenning van AI Dev Gallery**
- Verken voorbeeldtoepassingen en referentie-implementaties
- Test Windows AI API's met interactieve demonstraties
- Bekijk broncode voor best practices en patronen
- Identificeer relevante voorbeelden voor uw specifieke gebruiksscenario

### Fase 2: Modelselectie en integratie

**Vereistenanalyse**
- Definieer functionele vereisten voor AI-mogelijkheden
- Stel prestatiebeperkingen en optimalisatiedoelen vast
- Evalueer privacy- en beveiligingsvereisten
- Plan implementatiearchitectuur en schaalstrategieën

**Model evaluatie**
- Gebruik Foundry Local om open-source modellen te testen voor uw gebruiksscenario
- Benchmark Windows AI API's tegen aangepaste modelvereisten
- Evalueer afwegingen tussen modelgrootte, nauwkeurigheid en inferentiesnelheid
- Prototype integratiebenaderingen met geselecteerde modellen

### Fase 3: Applicatieontwikkeling

**Kernintegratie**
- Implementeer Windows AI API-integratie met correcte foutafhandeling
- Ontwerp gebruikersinterfaces die AI-verwerkingsworkflows ondersteunen
- Implementeer caching- en optimalisatiestrategieën voor modelinferentie
- Voeg telemetrie en monitoring toe voor AI-prestaties

**Testen en validatie**
- Test toepassingen op verschillende Windows-hardwareconfiguraties
- Valideer prestatiestatistieken onder verschillende belastingcondities
- Implementeer geautomatiseerd testen voor betrouwbaarheid van AI-functionaliteit
- Voer gebruikerstests uit met AI-verbeterde functies

### Fase 4: Optimalisatie en implementatie

**Prestatieoptimalisatie**
- Profileer applicatieprestaties op doelhardwareconfiguraties
- Optimaliseer geheugengebruik en model laadstrategieën
- Implementeer adaptief gedrag op basis van beschikbare hardwaremogelijkheden
- Fijn afstemmen van gebruikerservaring voor verschillende prestatiescenario's

**Productie-implementatie**
- Verpak toepassingen met correcte AI-modelafhankelijkheden
- Implementeer update-mechanismen voor modellen en applicatielogica
- Configureer monitoring en analyse voor productieomgevingen
- Plan uitrolstrategieën voor ondernemingen en consumentenimplementaties

## Praktische implementatievoorbeelden

### Voorbeeld 1: Intelligente documentverwerkingstoepassing

Bouw een Windows-toepassing die documenten verwerkt met meerdere AI-mogelijkheden:

**Gebruikte technologieën:**
- Phi Silica voor samenvatting van documenten en vraag-antwoord
- OCR API's voor tekstextractie uit gescande documenten
- Image Description API's voor analyse van grafieken en diagrammen
- Aangepaste ONNX-modellen voor documentclassificatie

**Implementatiebenadering:**
- Ontwerp modulaire architectuur met inplugbare AI-componenten
- Implementeer asynchrone verwerking voor grote documentbatches
- Voeg voortgangsindicatoren en annuleringsondersteuning toe voor langdurige operaties
- Inclusief offline mogelijkheden voor gevoelige documentverwerking

### Voorbeeld 2: Retail voorraadbeheersysteem

Creëer een AI-aangedreven voorraadbeheersysteem voor retailtoepassingen:

**Gebruikte technologieën:**
- Beeldsegmentatie voor productidentificatie
- Aangepaste visiemodellen voor merk- en categorieclassificatie
- Foundry Local implementatie van gespecialiseerde retailtaalmodellen
- Integratie met bestaande POS- en voorraadbeheersystemen

**Implementatiebenadering:**
- Bouw cameraintegratie voor realtime productscanning
- Implementeer barcode- en visuele productherkenning
- Voeg natuurlijke taalvoorraadvragen toe met lokale taalmodellen
- Ontwerp schaalbare architectuur voor implementatie in meerdere winkels

### Voorbeeld 3: Zorgdocumentatie-assistent

Ontwikkel een privacybeschermend hulpmiddel voor zorgdocumentatie:

**Gebruikte technologieën:**
- Phi Silica voor medische notities en klinische besluitvorming
- OCR voor digitalisering van handgeschreven medische dossiers
- Aangepaste medische taalmodellen geïmplementeerd via Windows ML
- Lokale vectoropslag voor medische kennisopvraging

**Implementatiebenadering:**
- Zorg voor volledig offline werking voor patiëntprivacy
- Implementeer validatie en suggestie van medische terminologie
- Voeg auditlogging toe voor naleving van regelgeving
- Ontwerp integratie met bestaande elektronische patiëntendossiersystemen

## Prestatieoptimalisatiestrategieën

### Hardwarebewuste ontwikkeling

**NPU-optimalisatie**
- Ontwerp toepassingen om NPU-mogelijkheden op Copilot+ PC's te benutten
- Implementeer een soepele terugval naar GPU/CPU op apparaten zonder NPU
- Optimaliseer modelformaten voor NPU-specifieke versnelling
- Monitor NPU-gebruik en thermische kenmerken

**Geheugenbeheer**
- Implementeer efficiënte model laad- en cachingstrategieën
- Gebruik geheugenmapping voor grote modellen om opstarttijd te verminderen
- Ontwerp geheugenbewuste toepassingen voor apparaten met beperkte middelen
- Implementeer modelkwantisatie voor geheugenoptimalisatie

**Batterij-efficiëntie**
- Optimaliseer AI-operaties voor minimaal energieverbruik
- Implementeer adaptieve verwerking op basis van batterijstatus
- Ontwerp efficiënte achtergrondverwerking voor continue AI-operaties
- Gebruik energieprofileringstools om energiegebruik te optimaliseren

### Schaalbaarheidsconsideraties

**Multithreading**
- Ontwerp thread-veilige AI-operaties voor gelijktijdige verwerking
- Implementeer efficiënte werkverdeling over beschikbare cores
- Gebruik async/await-patronen voor niet-blokkerende AI-operaties
- Plan threadpool-optimalisatie voor verschillende hardwareconfiguraties

**Cachingstrategieën**
- Implementeer intelligente caching voor vaak gebruikte AI-operaties
- Ontwerp cache-invalidatiestrategieën voor modelupdates
- Gebruik persistente caching voor dure preprocessing-operaties
- Implementeer gedistribueerde caching voor scenario's met meerdere gebruikers

## Beveiligings- en privacybest practices

### Gegevensbescherming

**Lokale verwerking**
- Zorg ervoor dat gevoelige gegevens nooit het lokale apparaat verlaten
- Implementeer veilige opslag voor AI-modellen en tijdelijke gegevens
- Gebruik Windows beveiligingsfuncties voor applicatiesandboxing
- Pas encryptie toe voor opgeslagen modellen en tussentijdse verwerkingsresultaten

**Modelbeveiliging**
- Valideer modelintegriteit vóór laden en uitvoering
- Implementeer veilige modelupdate-mechanismen
- Gebruik ondertekende modellen om manipulatie te voorkomen
- Pas toegangscontroles toe voor modelfiles en configuratie

### Nalevingsoverwegingen

**Regelgevingsuitlijning**
- Ontwerp toepassingen om te voldoen aan GDPR, HIPAA en andere regelgeving
- Implementeer auditlogging voor AI-besluitvormingsprocessen
- Bied transparantiefuncties voor AI-gegenereerde resultaten
- Stel gebruikers in staat controle te hebben over AI-gegevensverwerking

**Enterprise beveiliging**
- Integreer met Windows enterprise beveiligingsbeleid
- Ondersteun beheerde implementatie via enterprise management tools
- Implementeer rolgebaseerde toegangscontroles voor AI-functies
- Bied administratieve controles voor AI-functionaliteit

## Problemen oplossen en debuggen

### Veelvoorkomende ontwikkelingsuitdagingen

**Buildconfiguratieproblemen**
- Zorg voor ARM64-platformconfiguratie voor Windows AI API-voorbeelden
- Controleer compatibiliteit van Windows App SDK-versie (1.8.1+ vereist)
- Controleer of pakketidentiteit correct is geconfigureerd (vereist voor Windows AI API's)
- Valideer dat buildtools de doelraamwerkversie ondersteunen

**Problemen met modelladen**
- Valideer ONNX-modelcompatibiliteit met Windows ML
- Controleer modelbestandintegriteit en formaatvereisten
- Verifieer hardwarevereisten voor specifieke modellen
- Debug geheugenallocatieproblemen tijdens modelladen
- Zorg voor registratie van uitvoeringsproviders voor hardwareversnelling

**Overwegingen bij implementatiemodus**
- **Zelfstandige modus**: Volledig ondersteund met grotere implementatiegrootte
- **Framework-afhankelijke modus**: Kleinere voetafdruk maar vereist gedeelde runtime
- **Niet-verpakte toepassingen**: Niet langer ondersteund voor Windows AI API's
- Gebruik `dotnet run -p:Platform=ARM64 -p:SelfContained=true` voor zelfstandige ARM64-implementatie

**Prestatieproblemen**
- Profileer applicatieprestaties op verschillende hardwareconfiguraties
- Identificeer knelpunten in AI-verwerkingspijplijnen
- Optimaliseer gegevensvoorverwerking en nabewerking
- Implementeer prestatiemonitoring en waarschuwingen

**Integratieproblemen**
- Debug API-integratieproblemen met correcte foutafhandeling
- Valideer invoergegevensformaten en vereisten voor voorverwerking
- Test randgevallen en foutcondities grondig
- Implementeer uitgebreide logging voor het debuggen van productieproblemen

### Debuggingtools en technieken

**Visual Studio-integratie**
- Gebruik AI Toolkit debugger voor analyse van modeluitvoering
- Implementeer prestatieprofilering voor AI-operaties
- Debug asynchrone AI-operaties met correcte uitzonderingafhandeling
- Gebruik geheugenprofileringstools voor optimalisatie

**Windows AI Foundry-tools**
- Maak gebruik van Foundry Local CLI voor modeltesten en validatie
- Gebruik Windows AI API-testtools voor verificatie van integratie
- Implementeer aangepaste logging voor monitoring van AI-operaties
- Creëer geautomatiseerd testen voor betrouwbaarheid van AI-functionaliteit

## Toekomstbestendig maken van uw toepassingen

### Opkomende technologieën

**Next-Generation Hardware**
- Ontwerp toepassingen om toekomstige NPU-mogelijkheden te benutten
- Plan voor grotere modelgroottes en complexiteit
- Implementeer adaptieve architecturen voor evoluerende hardware
- Overweeg quantum-ready algoritmen voor toekomstige compatibiliteit

**Geavanceerde AI-mogelijkheden**
- Bereid u voor op multimodale AI-integratie over meer datatypes
- Plan voor realtime collaboratieve AI tussen meerdere apparaten
- Ontwerp voor federatieve leerfunctionaliteiten
- Overweeg edge-cloud hybride intelligentiearchitecturen

### Continu leren en aanpassen

**Modelupdates**
- Implementeer naadloze modelupdate-mechanismen
- Ontwerp toepassingen om zich aan te passen aan verbeterde modelmogelijkheden
- Plan voor achterwaartse compatibiliteit met bestaande modellen
- Implementeer A/B-testen voor evaluatie van modelprestaties

**Functie-evolutie**
- Ontwerp modulaire architecturen die nieuwe AI-mogelijkheden accommoderen
- Plan voor integratie van opkomende Windows AI API's
- Implementeer functieflags voor geleidelijke uitrol van mogelijkheden
- Ontwerp gebruikersinterfaces die zich aanpassen aan verbeterde AI-functies

## Conclusie

Windows Edge AI-ontwikkeling vertegenwoordigt de convergentie van krachtige AI-mogelijkheden met het robuuste, veilige en schaalbare Windows-platform. Door het Windows AI Foundry-ecosysteem te beheersen, kunnen ontwikkelaars intelligente toepassingen creëren die uitzonderlijke gebruikerservaringen bieden en tegelijkertijd de hoogste normen van privacy, beveiliging en prestaties handhaven.

De combinatie van Windows AI API's, Foundry Local en Windows ML biedt een ongeëvenaarde basis voor het bouwen van de volgende generatie intelligente Windows-toepassingen. Terwijl AI blijft evolueren, zorgt het Windows-platform ervoor dat uw toepassingen meegroeien met opkomende technologieën en tegelijkertijd compatibiliteit en prestaties behouden binnen het diverse Windows-hardware-ecosysteem.

Of u nu consumententoepassingen, bedrijfsoplossingen of gespecialiseerde industriële tools bouwt, Windows Edge AI-ontwikkeling stelt u in staat om intelligente, responsieve en diep geïntegreerde ervaringen te creëren die het volledige potentieel van moderne Windows-apparaten benutten.

## Aanvullende bronnen

### Documentatie en leren
- [Windows AI Foundry Documentatie](https://learn.microsoft.com/windows/ai/)
- [Windows AI API's Referentie](https://learn.microsoft.com/windows/ai/apis/)
- [Aan de slag met het bouwen van een app met Windows AI API's](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Aan de slag](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Overzicht](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Systeemvereisten voor Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Ontwikkelomgeving instellen voor Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Voorbeeldrepositories en code
- [Windows App SDK Voorbeelden - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Voorbeelden - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Inference Voorbeelden](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Voorbeelden Repository](https://github.com/microsoft/WindowsAppSDK-Samples)

### Ontwikkeltools
- [AI Toolkit voor Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Voorbeelden](https://learn.microsoft.com/windows/ai/samples/)
- [Model Conversie Tools](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technische ondersteuning
- [Windows ML Documentatie](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Documentatie](https://onnxruntime.ai/docs/)
- [Windows App SDK Documentatie](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Problemen melden - Windows App SDK Voorbeelden](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Community en ondersteuning
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Training](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Deze gids is ontworpen om mee te groeien met het snel evoluerende Windows AI-ecosysteem. Regelmatige updates zorgen voor afstemming met de nieuwste platformmogelijkheden en ontwikkelbest practices.*

[08. Aan de slag met Microsoft Foundry Local - Complete ontwikkelaarstoolkit](../Module08/README.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.