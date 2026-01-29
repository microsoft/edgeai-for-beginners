# AGENTS.md

> **Udviklervejledning til bidrag til EdgeAI for begyndere**
> 
> Dette dokument giver omfattende information til udviklere, AI-agenter og bidragydere, der arbejder med dette repository. Det dækker opsætning, udviklingsarbejdsgange, test og bedste praksis.
> 
> **Sidst opdateret**: 30. oktober 2025 | **Dokumentversion**: 3.0

## Indholdsfortegnelse

- [Projektoversigt](../..)
- [Repository-struktur](../..)
- [Forudsætninger](../..)
- [Opsætningskommandoer](../..)
- [Udviklingsarbejdsgang](../..)
- [Testinstruktioner](../..)
- [Retningslinjer for kodestil](../..)
- [Retningslinjer for pull requests](../..)
- [Oversættelsessystem](../..)
- [Foundry Local-integration](../..)
- [Bygning og udrulning](../..)
- [Almindelige problemer og fejlfinding](../..)
- [Yderligere ressourcer](../..)
- [Projekt-specifikke noter](../..)
- [Få hjælp](../..)

## Projektoversigt

EdgeAI for begyndere er et omfattende uddannelsesrepository, der underviser i Edge AI-udvikling med Small Language Models (SLMs). Kurset dækker EdgeAI-grundlæggende, modeludrulning, optimeringsteknikker og produktionsklare implementeringer ved hjælp af Microsoft Foundry Local og forskellige AI-rammer.

**Nøgleteknologier:**
- Python 3.8+ (primært sprog til AI/ML-eksempler)
- .NET C# (AI/ML-eksempler)
- JavaScript/Node.js med Electron (til desktop-applikationer)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-rammer: LangChain, Semantic Kernel, Chainlit
- Modeloptimering: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository-type:** Uddannelsesindhold med 8 moduler og 10 omfattende prøveapplikationer

**Arkitektur:** Multi-modul læringssti med praktiske eksempler, der demonstrerer Edge AI-udrulningsmønstre

## Repository-struktur

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Forudsætninger

### Påkrævede værktøjer

- **Python 3.8+** - Til AI/ML-eksempler og notebooks
- **Node.js 16+** - Til Electron-prøveapplikation
- **Git** - Til versionskontrol
- **Microsoft Foundry Local** - Til at køre AI-modeller lokalt

### Anbefalede værktøjer

- **Visual Studio Code** - Med Python-, Jupyter- og Pylance-udvidelser
- **Windows Terminal** - For en bedre kommandolinjeoplevelse (Windows-brugere)
- **Docker** - Til containerbaseret udvikling (valgfrit)

### Systemkrav

- **RAM**: Minimum 8GB, 16GB+ anbefales til multi-model scenarier
- **Lagerplads**: 10GB+ ledig plads til modeller og afhængigheder
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **Hardware**: CPU med AVX2-understøttelse; GPU (CUDA, Qualcomm NPU) valgfrit, men anbefales

### Vidensforudsætninger

- Grundlæggende forståelse af Python-programmering
- Fortrolighed med kommandolinjegrænseflader
- Forståelse af AI/ML-koncepter (til prøveudvikling)
- Git-arbejdsgange og pull request-processer

## Opsætningskommandoer

### Repository-opsætning

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Opsætning af Python-prøver (Modul08 og workshop-prøver)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Opsætning af Node.js-prøver (Prøve 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local-opsætning

Foundry Local er påkrævet for at køre prøverne. Download og installer fra det officielle repository:

**Installation:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuel**: Download fra [releases-siden](https://github.com/microsoft/Foundry-Local/releases)

**Hurtig start:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Bemærk**: Foundry Local vælger automatisk den bedste modelvariant til din hardware (CUDA GPU, Qualcomm NPU eller CPU).

## Udviklingsarbejdsgang

### Indholdsudvikling

Dette repository indeholder primært **Markdown-uddannelsesindhold**. Når du foretager ændringer:

1. Rediger `.md`-filer i de relevante modulmapper
2. Følg eksisterende formateringsmønstre
3. Sørg for, at kodeeksempler er nøjagtige og testede
4. Opdater tilsvarende oversat indhold, hvis nødvendigt (eller lad automatisering håndtere det)

### Udvikling af prøveapplikationer

For Modul08 Python-prøver (prøver 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

For workshop Python-prøver:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

For Electron-prøve (prøve 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Test af prøveapplikationer

Python-prøver har ikke automatiserede tests, men kan valideres ved at køre dem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-prøven har testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testinstruktioner

### Validering af indhold

Repositoryet bruger automatiserede oversættelsesarbejdsgange. Ingen manuel test er påkrævet for oversættelser.

**Manuel validering for indholdsændringer:**
1. Gennemse Markdown-visning ved at forhåndsvise `.md`-filer
2. Bekræft, at alle links peger på gyldige mål
3. Test eventuelle kodeuddrag inkluderet i dokumentationen
4. Kontroller, at billeder indlæses korrekt

### Test af prøveapplikationer

**Modul08/prøver/08 (Electron-app) har omfattende tests:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python-prøver bør testes manuelt:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Retningslinjer for kodestil

### Markdown-indhold

- Brug konsekvent overskriftshierarki (# til titel, ## til hovedafsnit, ### til underafsnit)
- Inkluder kodeblokke med sprogangivelser: ```python, ```bash, ```javascript
- Følg eksisterende formatering for tabeller, lister og fremhævning
- Hold linjer læsbare (sigte efter ~80-100 tegn, men ikke strengt)
- Brug relative links til interne referencer

### Python-kodestil

- Følg PEP 8-konventioner
- Brug type hints, hvor det er relevant
- Inkluder docstrings til funktioner og klasser
- Brug meningsfulde variabelnavne
- Hold funktioner fokuserede og korte

### JavaScript/Node.js-kodestil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Vigtige konventioner:**
- ESLint-konfiguration leveret i prøve 08
- Prettier til kodeformatering
- Brug moderne ES6+ syntaks
- Følg eksisterende mønstre i kodebasen

## Retningslinjer for pull requests

### Bidragsarbejdsgang

1. **Fork repositoryet** og opret en ny gren fra `main`
2. **Foretag dine ændringer** i henhold til kodestilsretningslinjerne
3. **Test grundigt** ved hjælp af testinstruktionerne ovenfor
4. **Commit med klare beskeder** i henhold til konventionelle commits-format
5. **Push til din fork** og opret en pull request
6. **Svar på feedback** fra vedligeholdere under gennemgang

### Navngivningskonvention for grene

- `feature/<modul>-<beskrivelse>` - Til nye funktioner eller indhold
- `fix/<modul>-<beskrivelse>` - Til fejlrettelser
- `docs/<beskrivelse>` - Til dokumentationsforbedringer
- `refactor/<beskrivelse>` - Til kodeomstrukturering

### Commit-beskedsformat

Følg [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Eksempler:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Titelformat
```
[ModuleXX] Brief description of change
```
eller
```
[Module08/samples/XX] Description for sample changes
```

### Adfærdskodeks

Alle bidragydere skal følge [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Gennemgå venligst [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), før du bidrager.

### Før indsendelse

**For indholdsændringer:**
- Forhåndsvis alle ændrede Markdown-filer
- Bekræft, at links og billeder fungerer
- Kontroller for stave- og grammatikfejl

**For ændringer i prøvekode (Modul08/prøver/08):**
```bash
npm run lint
npm test
```

**For ændringer i Python-prøver:**
- Test, at prøven kører korrekt
- Bekræft, at fejlbehandling fungerer
- Kontroller kompatibilitet med Foundry Local

### Gennemgangsproces

- Ændringer i uddannelsesindhold gennemgås for nøjagtighed og klarhed
- Kodeprøver testes for funktionalitet
- Oversættelsesopdateringer håndteres automatisk af GitHub Actions

## Oversættelsessystem

**VIGTIGT:** Dette repository bruger automatiseret oversættelse via GitHub Actions.

- Oversættelser findes i `/translations/`-mappen (50+ sprog)
- Automatiseret via `co-op-translator.yml`-arbejdsgang
- **REDIGER IKKE oversættelsesfiler manuelt** - de vil blive overskrevet
- Rediger kun engelske kildefiler i rod- og modulmapper
- Oversættelser genereres automatisk ved push til `main`-grenen

## Foundry Local-integration

De fleste Modul08-prøver kræver, at Microsoft Foundry Local kører.

### Installation & opsætning

**Installer Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installer Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Start Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK-brug (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verificering af Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Miljøvariabler til prøver

De fleste prøver bruger disse miljøvariabler:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Bemærk**: Når du bruger `FoundryLocalManager`, håndterer SDK'en automatisk tjenesteopdagelse og modelloading. Modelaliaser (som `phi-3.5-mini`) sikrer, at den bedste variant vælges til din hardware.

## Bygning og udrulning

### Indholdsudrulning

Dette repository er primært dokumentation - ingen byggeproces kræves for indhold.

### Bygning af prøveapplikationer

**Electron-applikation (Modul08/prøver/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python-prøver:**
Ingen byggeproces - prøver køres direkte med Python-fortolkeren.

## Almindelige problemer og fejlfinding

> **Tip**: Tjek [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) for kendte problemer og løsninger.

### Kritiske problemer (blokerende)

#### Foundry Local kører ikke
**Problem:** Prøver fejler med forbindelsesfejl

**Løsning:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Almindelige problemer (moderat)

#### Problemer med Python-virtuelt miljø
**Problem:** Fejl ved import af moduler

**Løsning:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemer med Electron-bygning
**Problem:** npm install eller byggefejl

**Løsning:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Arbejdsgangsproblemer (mindre)

#### Konflikter i oversættelsesarbejdsgang
**Problem:** Oversættelses-PR konflikter med dine ændringer

**Løsning:**
- Rediger kun engelske kildefiler
- Lad den automatiserede oversættelsesarbejdsgang håndtere oversættelser
- Hvis der opstår konflikter, så flet `main` ind i din gren, efter at oversættelserne er flettet

#### Fejl ved modeldownload
**Problem:** Foundry Local kan ikke downloade modeller

**Løsning:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Yderligere ressourcer

### Læringsstier
- **Begyndersti:** Moduler 01-02 (7-9 timer)
- **Mellemtrin:** Moduler 03-04 (9-11 timer)
- **Avanceret sti:** Moduler 05-07 (12-15 timer)
- **Ekspertsti:** Modul 08 (8-10 timer)
- **Hands-On Workshop:** Workshop-materialer (6-8 timer)

### Nøgleindhold i moduler
- **Modul01:** EdgeAI-grundlæggende og virkelige casestudier
- **Modul02:** Small Language Model (SLM)-familier og arkitekturer
- **Modul03:** Lokale og cloud-udrulningsstrategier
- **Modul04:** Modeloptimering med flere rammer (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - produktionsdrift
- **Modul06:** AI-agenter og funktionskald
- **Modul07:** Platform-specifikke implementeringer
- **Modul08:** Foundry Local-værktøjssæt med 10 omfattende prøver

### Eksterne afhængigheder
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokal AI-model runtime med OpenAI-kompatibel API
  - [Dokumentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimeringsramme
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modeloptimeringsværktøj
- [OpenVINO](https://docs.openvino.ai/) - Intels optimeringsværktøj

## Projekt-specifikke noter

### Modul08-prøveapplikationer

Repositoryet inkluderer 10 omfattende prøveapplikationer:

1. **01-REST Chat Quickstart** - Grundlæggende OpenAI SDK-integration
2. **02-OpenAI SDK Integration** - Avancerede SDK-funktioner
3. **03-Model Discovery & Benchmarking** - Værktøjer til model-sammenligning
4. **04-Chainlit RAG Application** - Retrieval-augmented generation
5. **05-Multi-Agent Orchestration** - Grundlæggende agentkoordinering
6. **06-Models-as-Tools Router** - Intelligent model-routing
7. **07-Direct API Client** - Lav-niveau API-integration
8. **08-Windows 11 Chat App** - Native Electron desktop-applikation
9. **09-Advanced Multi-Agent System** - Kompleks agentkoordinering
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integration

### Workshop Eksempelapplikationer

Workshoppen inkluderer 6 progressive sessioner med praktiske implementeringer:

1. **Session 01** - Chat bootstrap med Foundry Local integration
2. **Session 02** - RAG pipeline og evaluering med RAGAS
3. **Session 03** - Benchmarking af open-source modeller
4. **Session 04** - Model sammenligning og valg
5. **Session 05** - Multi-agent orkestreringssystemer
6. **Session 06** - Model routing og pipeline management

Hver prøve demonstrerer forskellige aspekter af edge AI-udvikling med Foundry Local.

### Ydeevneovervejelser

- SLM'er er optimeret til edge-implementering (2-16GB RAM)
- Lokal inferens giver svartider på 50-500ms
- Kvantiseringsteknikker opnår 75% størrelsesreduktion med 85% ydeevnebevarelse
- Realtids-samtaleegenskaber med lokale modeller

### Sikkerhed og Privatliv

- Al behandling sker lokalt - ingen data sendes til skyen
- Velegnet til applikationer med følsomme data (sundhedsvæsen, finans)
- Opfylder krav til datasuverænitet
- Foundry Local kører udelukkende på lokal hardware

## Få Hjælp

### Dokumentation

- **Hoved README**: [README.md](README.md) - Repository oversigt og læringsveje
- **Studieguide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Læringsressourcer og tidslinje
- **Support**: [SUPPORT.md](SUPPORT.md) - Hvordan man får hjælp
- **Sikkerhed**: [SECURITY.md](SECURITY.md) - Rapportering af sikkerhedsproblemer

### Fællesskabsstøtte

- **GitHub Issues**: [Rapportér fejl eller anmod om funktioner](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Diskussioner**: [Stil spørgsmål og del idéer](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Tekniske problemer med Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Vedligeholdere**: Se [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Sikkerhedsproblemer**: Følg ansvarlig rapportering i [SECURITY.md](SECURITY.md)
- **Microsoft Support**: For virksomhedssupport, kontakt Microsoft kundeservice

### Yderligere Ressourcer

- **Microsoft Learn**: [AI og Machine Learning Læringsveje](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentation**: [Officielle Dokumenter](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Fællesskabsprøver**: Tjek [GitHub Diskussioner](https://github.com/microsoft/edgeai-for-beginners/discussions) for bidrag fra fællesskabet

---

**Dette er et uddannelsesrepository fokuseret på at undervise i Edge AI-udvikling. Det primære bidragsmønster er at forbedre uddannelsesindhold og tilføje/forbedre prøveapplikationer, der demonstrerer Edge AI-koncepter.**

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.