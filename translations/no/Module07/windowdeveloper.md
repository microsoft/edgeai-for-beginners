# Windows Edge AI Utviklingsguide

## Introduksjon

Velkommen til Windows Edge AI-utvikling – din omfattende guide til å bygge intelligente applikasjoner som utnytter kraften av AI direkte på enheten ved hjelp av Microsofts Windows AI Foundry-plattform. Denne guiden er spesielt laget for Windows-utviklere som ønsker å integrere banebrytende Edge AI-funksjoner i sine applikasjoner, samtidig som de drar nytte av hele spekteret av Windows-maskinvareakselerasjon.

### Fordelene med Windows AI

Windows AI Foundry representerer en enhetlig, pålitelig og sikker plattform som støtter hele AI-utviklerens livssyklus – fra modellvalg og finjustering til optimalisering og distribusjon på tvers av CPU, GPU, NPU og hybride skyarkitekturer. Denne plattformen demokratiserer AI-utvikling ved å tilby:

- **Maskinvareabstraksjon**: Sømløs distribusjon på AMD-, Intel-, NVIDIA- og Qualcomm-silikon
- **Intelligens på enheten**: Personvernbevarende AI som kjører helt på lokal maskinvare
- **Optimalisert ytelse**: Modeller forhåndsoptimalisert for Windows-maskinvarekonfigurasjoner
- **Klar for bedrifter**: Produksjonsklare sikkerhets- og samsvarsfunksjoner

### Windows ML 
Windows Machine Learning (ML) gjør det mulig for utviklere som bruker C#, C++ og Python å kjøre ONNX AI-modeller lokalt på Windows-PCer via ONNX Runtime, med automatisk administrasjon av utførelsesleverandører for ulike maskinvaretyper (CPUer, GPUer, NPUer). [ONNX Runtime](https://onnxruntime.ai/docs/) kan brukes med modeller fra PyTorch, Tensorflow/Keras, TFLite, scikit-learn og andre rammeverk.

![WindowsML Et diagram som illustrerer en ONNX-modell som går gjennom Windows ML for deretter å nå NPUs, GPUs og CPUs.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML gir en delt Windows-omfattende kopi av ONNX Runtime, samt muligheten til å dynamisk laste ned utførelsesleverandører (EPs).

### Hvorfor Windows for Edge AI?

**Universell maskinvarestøtte**
Windows ML gir automatisk maskinvareoptimalisering på tvers av hele Windows-økosystemet, og sikrer at AI-applikasjonene dine yter optimalt uavhengig av den underliggende silisiumarkitekturen.

**Integrert AI-runtime**
Den innebygde Windows ML-inferensmotoren eliminerer komplekse oppsettkrav, slik at utviklere kan fokusere på applikasjonslogikk i stedet for infrastrukturproblemer.

**Copilot+ PC-optimalisering**
Formålstilpassede APIer designet spesielt for neste generasjons Windows-enheter med dedikerte Neural Processing Units (NPUs) som gir eksepsjonell ytelse per watt.

**Utviklerøkosystem**
Rike verktøy inkludert Visual Studio-integrasjon, omfattende dokumentasjon og eksempelapplikasjoner som akselererer utviklingssykluser.

## Læringsmål

Ved å fullføre denne Windows Edge AI-utviklingsguiden vil du mestre de essensielle ferdighetene for å bygge produksjonsklare AI-applikasjoner på Windows-plattformen.

### Kjernekompetanser

**Windows AI Foundry-mestring**
- Forstå arkitekturen og komponentene i Windows AI Foundry-plattformen
- Navigere gjennom hele AI-utviklingslivssyklusen innen Windows-økosystemet
- Implementere sikkerhetsbeste praksis for AI-applikasjoner på enheten
- Optimalisere applikasjoner for ulike Windows-maskinvarekonfigurasjoner

**API-integrasjonsekspertise**
- Mestre Windows AI APIer for tekst-, visjons- og multimodale applikasjoner
- Implementere Phi Silica-språkmodellintegrasjon for tekstgenerering og resonnement
- Distribuere datamaskinvisjonsfunksjoner ved hjelp av innebygde bildebehandlings-APIer
- Tilpasse forhåndstrente modeller ved hjelp av LoRA (Low-Rank Adaptation)-teknikker

**Foundry Local-implementering**
- Bla gjennom, evaluere og distribuere åpne språkmodeller ved hjelp av Foundry Local CLI
- Forstå modelloptimalisering og kvantisering for lokal distribusjon
- Implementere offline AI-funksjoner som fungerer uten internettforbindelse
- Administrere modellers livssyklus og oppdateringer i produksjonsmiljøer

**Windows ML-distribusjon**
- Ta med tilpassede ONNX-modeller til Windows-applikasjoner ved hjelp av Windows ML
- Utnytte automatisk maskinvareakselerasjon på tvers av CPU-, GPU- og NPU-arkitekturer
- Implementere sanntidsinferens med optimal ressursutnyttelse
- Designe skalerbare AI-applikasjoner for ulike Windows-enhetskategorier

### Applikasjonsutviklingsferdigheter

**Plattformuavhengig Windows-utvikling**
- Bygge AI-drevne applikasjoner ved hjelp av .NET MAUI for universell Windows-distribusjon
- Integrere AI-funksjoner i Win32-, UWP- og Progressive Web Applications
- Implementere responsive UI-design som tilpasser seg AI-behandlingsstatus
- Håndtere asynkrone AI-operasjoner med riktige brukeropplevelsesmønstre

**Ytelsesoptimalisering**
- Profilere og optimalisere AI-inferensytelse på tvers av ulike maskinvarekonfigurasjoner
- Implementere effektiv minnehåndtering for store språkmodeller
- Designe applikasjoner som degraderer grasiøst basert på tilgjengelige maskinvarekapasiteter
- Anvende caching-strategier for ofte brukte AI-operasjoner

**Produksjonsklarhet**
- Implementere omfattende feilhåndtering og fallback-mekanismer
- Designe telemetri og overvåking for AI-applikasjonsytelse
- Anvende sikkerhetsbeste praksis for lokal AI-modell lagring og utførelse
- Planlegge distribusjonsstrategier for bedrifts- og forbrukerapplikasjoner

### Forretnings- og strategisk forståelse

**AI-applikasjonsarkitektur**
- Designe hybride arkitekturer som optimaliserer mellom lokal og skybasert AI-behandling
- Evaluere avveininger mellom modellstørrelse, nøyaktighet og inferenshastighet
- Planlegge dataflytarkitekturer som opprettholder personvern samtidig som de muliggjør intelligens
- Implementere kostnadseffektive AI-løsninger som skalerer med brukerbehov

**Markedsposisjonering**
- Forstå konkurransefordelene med Windows-native AI-applikasjoner
- Identifisere bruksområder der AI på enheten gir overlegne brukeropplevelser
- Utvikle go-to-market-strategier for AI-forbedrede Windows-applikasjoner
- Posisjonere applikasjoner for å dra nytte av Windows-økosystemets fordeler

## Windows App SDK AI-eksempler

Windows App SDK gir omfattende eksempler som demonstrerer AI-integrasjon på tvers av flere rammeverk og distribusjonsscenarier. Disse eksemplene er essensielle referanser for å forstå Windows AI-utviklingsmønstre.

### Windows AI Foundry-eksempler

| Eksempel | Rammeverk | Fokusområde | Nøkkelfunksjoner |
|----------|-----------|-------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API-integrasjon | Komplett WinUI-app som demonstrerer Windows AI APIer, ARM64-optimalisering, pakket distribusjon |

**Nøkkelteknologier:**
- Windows AI APIer
- WinUI 3-rammeverk
- ARM64-plattformoptimalisering
- Copilot+ PC-kompatibilitet
- Pakket applikasjonsdistribusjon

**Forutsetninger:**
- Windows 11 med Copilot+ PC anbefalt
- Visual Studio 2022
- ARM64 byggekonfigurasjon
- Windows App SDK 1.8.1+

### Windows ML-eksempler

#### C++-eksempler

| Eksempel | Type | Fokusområde | Nøkkelfunksjoner |
|----------|------|-------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsollapp | Grunnleggende Windows ML | EP-oppdagelse, kommandolinjealternativer, modellkompilering |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsollapp | Rammeverksavhengig distribusjon | Delt runtime, mindre distribusjonsfotavtrykk |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsollapp | Selvstendig distribusjon | Frittstående distribusjon, ingen runtime-avhengigheter |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Bibliotekbruk | WindowsML i delt bibliotek, minnehåndtering |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet-opplæring | Modellkonvertering, EP-kompilering, Build 2025-opplæring |

#### C#-eksempler

**Konsollapplikasjoner**

| Eksempel | Type | Fokusområde | Nøkkelfunksjoner |
|----------|------|-------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsollapp | Grunnleggende C#-integrasjon | Delt hjelperbruk, kommandolinjegrensesnitt |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet-opplæring | Modellkonvertering, EP-kompilering, Build 2025-opplæring |

**GUI-applikasjoner**

| Eksempel | Rammeverk | Fokusområde | Nøkkelfunksjoner |
|----------|-----------|-------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Bildeklassifisering med WPF-grensesnitt |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradisjonell GUI | Bildeklassifisering med Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderne GUI | Bildeklassifisering med WinUI 3-grensesnitt |

#### Python-eksempler

| Eksempel | Språk | Fokusområde | Nøkkelfunksjoner |
|----------|-------|-------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Bildeklassifisering | WinML Python-bindinger, batch-bildebehandling |

### Eksempel-forutsetninger

**Systemkrav:**
- Windows 11-PC som kjører versjon 24H2 (build 26100) eller nyere
- Visual Studio 2022 med C++- og .NET-arbeidsbelastninger
- Windows App SDK 1.8.1 eller nyere
- Python 3.10-3.13 for Python-eksempler på x64- og ARM64-enheter

**Windows AI Foundry-spesifikt:**
- Copilot+ PC anbefalt for optimal ytelse
- ARM64 byggekonfigurasjon for Windows AI-eksempler
- Pakkeidentitet kreves (upakkede apper støttes ikke lenger)

### Vanlig arbeidsflyt for eksempler

De fleste Windows ML-eksempler følger dette standardmønsteret:

1. **Initialiser miljø** - Opprett ONNX Runtime-miljø
2. **Registrer utførelsesleverandører** - Oppdag og registrer tilgjengelige maskinvareakseleratorer (CPU, GPU, NPU)
3. **Last modell** - Last ONNX-modell, eventuelt kompiler for målmaskinvare
4. **Forbehandle input** - Konverter bilder/data til modellens inputformat
5. **Kjør inferens** - Utfør modell og få prediksjoner
6. **Behandle resultater** - Anvend softmax og vis toppresultater

### Modellfiler som brukes

| Modell | Formål | Inkludert | Notater |
|-------|--------|----------|---------|
| SqueezeNet | Lettvekts bildeklassifisering | ✅ Inkludert | Forhåndstrent, klar til bruk |
| ResNet-50 | Høy nøyaktighet bildeklassifisering | ❌ Krever konvertering | Bruk [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) for konvertering |

### Maskinvarestøtte

Alle eksempler oppdager og utnytter tilgjengelig maskinvare automatisk:
- **CPU** - Universell støtte på alle Windows-enheter
- **GPU** - Automatisk oppdagelse og optimalisering for tilgjengelig grafikkmaskinvare
- **NPU** - Utnytter Neural Processing Units på støttede enheter (Copilot+ PCer)

## Windows AI Foundry-plattformkomponenter

### 1. Windows AI APIer

Windows AI APIer gir klare AI-funksjoner drevet av modeller på enheten, optimalisert for effektivitet og ytelse på Copilot+ PC-enheter med minimal oppsett nødvendig.

#### Kjerne-API-kategorier

**Phi Silica-språkmodell**
- Liten, men kraftig språkmodell for tekstgenerering og resonnement
- Optimalisert for sanntidsinferens med minimalt strømforbruk
- Støtte for tilpasset finjustering ved hjelp av LoRA-teknikker
- Integrasjon med Windows semantisk søk og kunnskapshenting

**Datamaskinvisjons-APIer**
- **Tekstgjenkjenning (OCR)**: Ekstraher tekst fra bilder med høy nøyaktighet
- **Bildeoppløsning**: Forbedre bilder ved hjelp av lokale AI-modeller
- **Bildesegmentering**: Identifiser og isoler spesifikke objekter i bilder
- **Bildebeskrivelse**: Generer detaljerte tekstbeskrivelser for visuelt innhold
- **Objektfjerning**: Fjern uønskede objekter fra bilder med AI-drevet inpainting

**Multimodale funksjoner**
- **Visjon-språk-integrasjon**: Kombiner tekst- og bildeforståelse
- **Semantisk søk**: Aktiver naturlige språkspørsmål på tvers av multimedia-innhold
- **Kunnskapshenting**: Bygg intelligente søkeopplevelser med lokal data

### 2. Foundry Local

Foundry Local gir utviklere rask tilgang til klare åpne språkmodeller på Windows-silikon, med mulighet til å bla gjennom, teste, interagere og distribuere modeller i lokale applikasjoner.

#### Foundry Local-eksempelapplikasjoner

[Foundry Local-repositoriet](https://github.com/microsoft/Foundry-Local/tree/main/samples) gir omfattende eksempler på tvers av flere programmeringsspråk og rammeverk, som demonstrerer ulike integrasjonsmønstre og bruksområder.

| Eksempel | Språk/Rammeverk | Fokusområde | Nøkkelfunksjoner |
|----------|-----------------|-------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG-implementering | Semantisk Kernel-integrasjon, Qdrant vektorlagring, JINA-embeddings, dokumentinnhenting, streaming-chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop-chatapp | Plattformuavhengig chat, lokal/sky-modellbytte, OpenAI SDK-integrasjon, sanntidsstreaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Grunnleggende integrasjon | Enkel SDK-bruk, modellinitialisering, grunnleggende chatfunksjonalitet |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Grunnleggende integrasjon | Python SDK-bruk, streaming-responser, OpenAI-kompatibel API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Systemintegrasjon | Lavnivå SDK-bruk, asynkrone operasjoner, reqwest HTTP-klient |

#### Eksempelkategorier etter bruksområde

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Komplett RAG-implementasjon med Semantic Kernel, Qdrant vektordatabase og JINA embeddings
- **Arkitektur**: Dokumentinnhenting → Tekstdeling → Vektorembeddings → Likhetssøk → Kontekstbaserte svar
- **Teknologier**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, streaming chat fullføring

**Skrivebordsapplikasjoner**
- **electron/foundry-chat**: Produksjonsklar chat-applikasjon med lokal/sky-modellbytte
- **Funksjoner**: Modellvelger, streaming svar, feilhåndtering, plattformuavhengig distribusjon
- **Arkitektur**: Electron hovedprosess, IPC-kommunikasjon, sikre preload-skript

**SDK-integrasjonseksempler**
- **JavaScript (Node.js)**: Grunnleggende modellinteraksjon og streaming svar
- **Python**: OpenAI-kompatibel API-bruk med asynkron streaming
- **Rust**: Lavnivåintegrasjon med reqwest og tokio for asynkrone operasjoner

#### Forutsetninger for Foundry Local-eksempler

**Systemkrav:**
- Windows 11 med Foundry Local installert
- Node.js v16+ for JavaScript/Electron-eksempler
- .NET 8.0+ for C#-eksempler
- Python 3.10+ for Python-eksempler
- Rust 1.70+ for Rust-eksempler

**Installasjon:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Eksempelspecifik oppsett

**dotNET RAG-eksempel:**
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

**Electron Chat-eksempel:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust-eksempler:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Nøkkelfunksjoner

**Modellkatalog**
- Omfattende samling av forhåndsoptimaliserte open-source modeller
- Modeller optimalisert for CPUer, GPUer og NPUer for umiddelbar distribusjon
- Støtte for populære modellfamilier som Llama, Mistral, Phi og spesialiserte domenemodeller

**CLI-integrasjon**
- Kommandolinjegrensesnitt for modelladministrasjon og distribusjon
- Automatiserte optimaliserings- og kvantiseringsarbeidsflyter
- Integrasjon med populære utviklingsmiljøer og CI/CD-pipelines

**Lokal distribusjon**
- Fullstendig offline drift uten skyavhengigheter
- Støtte for tilpassede modellformater og konfigurasjoner
- Effektiv modellservering med automatisk maskinvareoptimalisering

### 3. Windows ML

Windows ML fungerer som den sentrale AI-plattformen og integrerte inferensmotoren på Windows, som gjør det mulig for utviklere å distribuere tilpassede modeller effektivt på tvers av Windows-maskinvareøkosystemet.

#### Arkitekturforder

**Universell maskinvarestøtte**
- Automatisk optimalisering for AMD-, Intel-, NVIDIA- og Qualcomm-silikon
- Støtte for CPU-, GPU- og NPU-eksekvering med transparent bytte
- Maskinvareabstraksjon som eliminerer plattformspesifikt optimaliseringsarbeid

**Modellfleksibilitet**
- Støtte for ONNX-modellformat med automatisk konvertering fra populære rammeverk
- Tilpasset modelldistribusjon med ytelse på produksjonsnivå
- Integrasjon med eksisterende Windows-applikasjonsarkitekturer

**Bedriftsintegrasjon**
- Kompatibel med Windows sikkerhets- og samsvarsrammeverk
- Støtte for bedriftsdistribusjon og administrasjonsverktøy
- Integrasjon med Windows enhetsadministrasjon og overvåkingssystemer

## Utviklingsarbeidsflyt

### Fase 1: Miljøoppsett og verktøykonfigurasjon

**Forberedelse av utviklingsmiljø**
1. Installer Visual Studio 2022 med C++- og .NET-arbeidsbelastninger
2. Installer Windows App SDK 1.8.1 eller nyere
3. Konfigurer Windows AI Foundry CLI-verktøy
4. Sett opp AI Toolkit-utvidelsen for Visual Studio Code
5. Etabler verktøy for ytelsesprofilering og overvåking
6. Sørg for ARM64 byggekonfigurasjon for Copilot+ PC-optimalisering

**Oppsett av eksempellager**
1. Klon [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Naviger til `Samples/WindowsAIFoundry/cs-winui` for Windows AI API-eksempler
3. Naviger til `Samples/WindowsML` for omfattende Windows ML-eksempler
4. Gå gjennom [build requirements](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) for dine målplattformer

**Utforskning av AI Dev Gallery**
- Utforsk eksempelapplikasjoner og referanseimplementasjoner
- Test Windows AI APIer med interaktive demonstrasjoner
- Gå gjennom kildekode for beste praksis og mønstre
- Identifiser relevante eksempler for ditt spesifikke bruksområde

### Fase 2: Modellvalg og integrasjon

**Kravsanalyse**
- Definer funksjonelle krav for AI-funksjoner
- Etabler ytelsesbegrensninger og optimaliseringsmål
- Evaluer personvern- og sikkerhetskrav
- Planlegg distribusjonsarkitektur og skaleringsstrategier

**Modellevaluering**
- Bruk Foundry Local til å teste open-source modeller for ditt bruksområde
- Benchmark Windows AI APIer mot tilpassede modellkrav
- Evaluer avveininger mellom modellstørrelse, nøyaktighet og inferenshastighet
- Prototype integrasjonsmetoder med valgte modeller

### Fase 3: Applikasjonsutvikling

**Kjerneintegrasjon**
- Implementer Windows AI API-integrasjon med riktig feilhåndtering
- Design brukergrensesnitt som tilpasser seg AI-prosessarbeidsflyter
- Implementer caching og optimaliseringsstrategier for modellinferens
- Legg til telemetri og overvåking for AI-ytelse

**Testing og validering**
- Test applikasjoner på tvers av forskjellige Windows-maskinvarekonfigurasjoner
- Valider ytelsesmetrikker under ulike belastningsforhold
- Implementer automatisert testing for AI-funksjonalitetens pålitelighet
- Utfør brukeropplevelsestesting med AI-forbedrede funksjoner

### Fase 4: Optimalisering og distribusjon

**Ytelsesoptimalisering**
- Profil applikasjonsytelse på tvers av målmaskinvarekonfigurasjoner
- Optimaliser minnebruk og modellinnlastingsstrategier
- Implementer adaptiv oppførsel basert på tilgjengelige maskinvarefunksjoner
- Finjuster brukeropplevelsen for forskjellige ytelsesscenarier

**Produksjonsdistribusjon**
- Pakk applikasjoner med riktige AI-modellavhengigheter
- Implementer oppdateringsmekanismer for modeller og applikasjonslogikk
- Konfigurer overvåking og analyse for produksjonsmiljøer
- Planlegg utrullingsstrategier for bedrifts- og forbrukerdistribusjoner

## Praktiske implementeringseksempler

### Eksempel 1: Intelligent dokumentbehandlingsapplikasjon

Bygg en Windows-applikasjon som behandler dokumenter ved hjelp av flere AI-funksjoner:

**Brukte teknologier:**
- Phi Silica for dokumentoppsummering og spørsmål/svar
- OCR APIer for tekstuttrekk fra skannede dokumenter
- Bildeskrive-APIer for analyse av diagrammer og grafer
- Tilpassede ONNX-modeller for dokumentklassifisering

**Implementeringsmetode:**
- Design modulær arkitektur med utskiftbare AI-komponenter
- Implementer asynkron behandling for store dokumentbunker
- Legg til fremdriftsindikatorer og avbrytelsesstøtte for langvarige operasjoner
- Inkluder offline-funksjonalitet for sensitiv dokumentbehandling

### Eksempel 2: System for detaljhandelslagerstyring

Lag et AI-drevet lagerstyringssystem for detaljhandelsapplikasjoner:

**Brukte teknologier:**
- Bildesegmentering for produktidentifikasjon
- Tilpassede visjonsmodeller for merke- og kategoriklassifisering
- Foundry Local-distribusjon av spesialiserte språkmodeller for detaljhandel
- Integrasjon med eksisterende POS- og lagersystemer

**Implementeringsmetode:**
- Bygg kameraintegrasjon for sanntidsskanning av produkter
- Implementer strekkode- og visuell produktgjenkjenning
- Legg til naturlige språkspørringer for lagerstyring med lokale språkmodeller
- Design skalerbar arkitektur for distribusjon på tvers av flere butikker

### Eksempel 3: Dokumentasjonsassistent for helsevesenet

Utvikle et personvernbevarende dokumentasjonsverktøy for helsevesenet:

**Brukte teknologier:**
- Phi Silica for generering av medisinske notater og klinisk beslutningsstøtte
- OCR for digitalisering av håndskrevne medisinske journaler
- Tilpassede medisinske språkmodeller distribuert via Windows ML
- Lokal vektorlagring for medisinsk kunnskapssøk

**Implementeringsmetode:**
- Sørg for fullstendig offline drift for pasientpersonvern
- Implementer validering og forslag for medisinsk terminologi
- Legg til revisjonslogging for samsvar med regelverk
- Design integrasjon med eksisterende elektroniske pasientjournalsystemer

## Ytelsesoptimaliseringsstrategier

### Maskinvarebevisst utvikling

**NPU-optimalisering**
- Design applikasjoner for å utnytte NPU-funksjoner på Copilot+ PCer
- Implementer smidig fallback til GPU/CPU på enheter uten NPU
- Optimaliser modellformater for NPU-spesifikk akselerasjon
- Overvåk NPU-utnyttelse og termiske egenskaper

**Minnehåndtering**
- Implementer effektive modellinnlastings- og cachingstrategier
- Bruk minnekartlegging for store modeller for å redusere oppstartstid
- Design minnebevisste applikasjoner for ressursbegrensede enheter
- Implementer modellkvantisering for minneoptimalisering

**Batterieffektivitet**
- Optimaliser AI-operasjoner for minimalt strømforbruk
- Implementer adaptiv behandling basert på batteristatus
- Design effektiv bakgrunnsbehandling for kontinuerlige AI-operasjoner
- Bruk verktøy for strømprofilering for å optimalisere energibruk

### Skalerbarhetsbetraktninger

**Multitråding**
- Design trådsikre AI-operasjoner for samtidig behandling
- Implementer effektiv arbeidsfordeling på tilgjengelige kjerner
- Bruk async/await-mønstre for ikke-blokkerende AI-operasjoner
- Planlegg optimalisering av trådpool for forskjellige maskinvarekonfigurasjoner

**Cachingstrategier**
- Implementer intelligent caching for ofte brukte AI-operasjoner
- Design cache-invalideringsstrategier for modelloppdateringer
- Bruk vedvarende caching for kostbare forhåndsbehandlingsoperasjoner
- Implementer distribuert caching for flerscenarier

## Sikkerhets- og personvernpraksis

### Databeskyttelse

**Lokal behandling**
- Sørg for at sensitiv data aldri forlater den lokale enheten
- Implementer sikker lagring for AI-modeller og midlertidige data
- Bruk Windows sikkerhetsfunksjoner for applikasjonssandboxing
- Anvend kryptering for lagrede modeller og mellomliggende behandlingsresultater

**Modellsikkerhet**
- Valider modellintegritet før innlasting og eksekvering
- Implementer sikre modelloppdateringsmekanismer
- Bruk signerte modeller for å forhindre manipulering
- Anvend tilgangskontroller for modellfiler og konfigurasjon

### Samsvarsbetraktninger

**Regulatorisk tilpasning**
- Design applikasjoner for å oppfylle GDPR-, HIPAA- og andre regulatoriske krav
- Implementer revisjonslogging for AI-beslutningsprosesser
- Gi transparensfunksjoner for AI-genererte resultater
- Aktiver brukerens kontroll over AI-databehandling

**Bedriftssikkerhet**
- Integrer med Windows bedriftsikkerhetspolicyer
- Støtt administrert distribusjon gjennom bedriftsadministrasjonsverktøy
- Implementer rollebaserte tilgangskontroller for AI-funksjoner
- Gi administrative kontroller for AI-funksjonalitet

## Feilsøking og debugging

### Vanlige utviklingsutfordringer

**Byggekonfigurasjonsproblemer**
- Sørg for ARM64 plattformkonfigurasjon for Windows AI API-eksempler
- Verifiser kompatibilitet med Windows App SDK-versjon (1.8.1+ kreves)
- Sjekk at pakkeidentitet er riktig konfigurert (kreves for Windows AI APIer)
- Valider at byggverktøy støtter målrammeversjonen

**Modellinnlastingsproblemer**
- Valider ONNX-modellkompatibilitet med Windows ML
- Sjekk modellfilintegritet og formatkrav
- Verifiser maskinvarekapabilitetskrav for spesifikke modeller
- Debug minneallokeringsproblemer under modellinnlasting
- Sørg for registrering av eksekveringsleverandør for maskinvareakselerasjon

**Distribusjonsmodusbetraktninger**
- **Selvstendig modus**: Fullt støttet med større distribusjonsstørrelse
- **Rammeverksavhengig modus**: Mindre fotavtrykk, men krever delt runtime
- **Utpakkede applikasjoner**: Ikke lenger støttet for Windows AI APIer
- Bruk `dotnet run -p:Platform=ARM64 -p:SelfContained=true` for selvstendig ARM64-distribusjon

**Ytelsesproblemer**
- Profil applikasjonsytelse på tvers av forskjellige maskinvarekonfigurasjoner
- Identifiser flaskehalser i AI-behandlingspipelines
- Optimaliser dataforbehandling og etterbehandlingsoperasjoner
- Implementer ytelsesovervåking og varsling

**Integrasjonsvansker**
- Debug API-integrasjonsproblemer med riktig feilhåndtering
- Valider inputdataformater og forbehandlingskrav
- Test kanttilfeller og feilforhold grundig
- Implementer omfattende logging for debugging av produksjonsproblemer

### Debugging-verktøy og teknikker

**Visual Studio-integrasjon**
- Bruk AI Toolkit debugger for modellutførelsesanalyse
- Implementer ytelsesprofilering for AI-operasjoner
- Debug asynkrone AI-operasjoner med riktig unntakshåndtering
- Bruk minneprofileringverktøy for optimalisering

**Windows AI Foundry-verktøy**
- Utnytt Foundry Local CLI for modelltesting og validering
- Bruk Windows AI API-testverktøy for integrasjonsverifisering
- Implementer tilpasset logging for AI-operasjonsovervåking
- Opprett automatisert testing for AI-funksjonalitetens pålitelighet

## Fremtidssikring av applikasjoner

### Fremvoksende teknologier

**Neste generasjons maskinvare**
- Design applikasjoner for å utnytte fremtidige NPU-funksjoner
- Planlegg for økte modellstørrelser og kompleksitet
- Implementer adaptive arkitekturer for utviklende maskinvare
- Vurder kvanteklare algoritmer for fremtidig kompatibilitet

**Avanserte AI-funksjoner**
- Forbered for multimodal AI-integrasjon på tvers av flere datatyper
- Planlegg for sanntids samarbeids-AI mellom flere enheter
- Design for federerte læringsfunksjoner
- Vurder edge-sky hybrid intelligensarkitekturer

### Kontinuerlig læring og tilpasning

**Modelloppdateringer**
- Implementer sømløse modelloppdateringsmekanismer
- Design applikasjoner for å tilpasse seg forbedrede modellfunksjoner
- Planlegg for bakoverkompatibilitet med eksisterende modeller
- Implementer A/B-testing for modellytelsesevaluering

**Funksjonsevolusjon**
- Design modulære arkitekturer som tilpasser seg nye AI-funksjoner
- Planlegg for integrasjon av fremvoksende Windows AI APIer
- Implementer funksjonsflagg for gradvis utrulling av funksjoner
- Design brukergrensesnitt som tilpasser seg forbedrede AI-funksjoner

## Konklusjon

Windows Edge AI-utvikling representerer konvergensen av kraftige AI-funksjoner med den robuste, sikre og skalerbare Windows-plattformen. Ved å mestre Windows AI Foundry-økosystemet kan utviklere lage intelligente applikasjoner som gir eksepsjonelle brukeropplevelser samtidig som de opprettholder de høyeste standardene for personvern, sikkerhet og ytelse.

Kombinasjonen av Windows AI APIer, Foundry Local og Windows ML gir et enestående grunnlag for å bygge neste generasjon av intelligente Windows-applikasjoner. Etter hvert som AI fortsetter å utvikle seg, sikrer Windows-plattformen at applikasjonene dine vil skalere med fremvoksende teknologier samtidig som de opprettholder kompatibilitet og ytelse på tvers av det mangfoldige Windows-maskinvareøkosystemet.

Enten du bygger forbrukerapplik
- [Windows ML Oversikt](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Systemkrav for Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Oppsett av utviklingsmiljø for Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Eksempellagre og kode
- [Windows App SDK Eksempler - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Eksempler - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Inference Eksempler](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Eksempellager](https://github.com/microsoft/WindowsAppSDK-Samples)

### Utviklingsverktøy
- [AI Toolkit for Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Eksempler](https://learn.microsoft.com/windows/ai/samples/)
- [Verktøy for modellkonvertering](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Teknisk støtte
- [Windows ML Dokumentasjon](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentasjon](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentasjon](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Rapporter problemer - Windows App SDK Eksempler](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Fellesskap og støtte
- [Windows Utviklerfellesskap](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogg](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Opplæring](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Denne veiledningen er laget for å utvikle seg i takt med det raskt fremvoksende Windows AI-økosystemet. Regelmessige oppdateringer sikrer samsvar med de nyeste plattformfunksjonene og beste praksis for utvikling.*

[08. Praktisk arbeid med Microsoft Foundry Local - Komplett utviklerverktøysett](../Module08/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.