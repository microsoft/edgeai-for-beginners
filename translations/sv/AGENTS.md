<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:01:06+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sv"
}
-->
# AGENTS.md

> **Utvecklingsguide för att bidra till EdgeAI för nybörjare**
> 
> Detta dokument ger omfattande information för utvecklare, AI-agenter och bidragsgivare som arbetar med detta repository. Det täcker installation, utvecklingsarbetsflöden, testning och bästa praxis.
> 
> **Senast uppdaterad**: 30 oktober 2025 | **Dokumentversion**: 3.0

## Innehållsförteckning

- [Projektöversikt](../..)
- [Repositorystruktur](../..)
- [Förutsättningar](../..)
- [Installationskommandon](../..)
- [Utvecklingsarbetsflöde](../..)
- [Testinstruktioner](../..)
- [Riktlinjer för kodstil](../..)
- [Riktlinjer för pull requests](../..)
- [Översättningssystem](../..)
- [Foundry Local-integration](../..)
- [Bygg och distribution](../..)
- [Vanliga problem och felsökning](../..)
- [Ytterligare resurser](../..)
- [Projekt-specifika anteckningar](../..)
- [Få hjälp](../..)

## Projektöversikt

EdgeAI för nybörjare är ett omfattande utbildningsrepository som lär ut Edge AI-utveckling med Small Language Models (SLMs). Kursen täcker EdgeAI-grunder, modellimplementering, optimeringstekniker och produktionsklara implementationer med Microsoft Foundry Local och olika AI-ramverk.

**Nyckelteknologier:**
- Python 3.8+ (huvudspråk för AI/ML-exempel)
- .NET C# (AI/ML-exempel)
- JavaScript/Node.js med Electron (för desktop-applikationer)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-ramverk: LangChain, Semantic Kernel, Chainlit
- Modelloptimering: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repositorytyp:** Utbildningsinnehållsrepository med 8 moduler och 10 omfattande exempelapplikationer

**Arkitektur:** Flermoduls lärandebana med praktiska exempel som demonstrerar Edge AI-implementeringsmönster

## Repositorystruktur

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

## Förutsättningar

### Nödvändiga verktyg

- **Python 3.8+** - För AI/ML-exempel och notebooks
- **Node.js 16+** - För Electron-exempelapplikation
- **Git** - För versionskontroll
- **Microsoft Foundry Local** - För att köra AI-modeller lokalt

### Rekommenderade verktyg

- **Visual Studio Code** - Med Python-, Jupyter- och Pylance-tillägg
- **Windows Terminal** - För bättre kommandoradsupplevelse (Windows-användare)
- **Docker** - För containerbaserad utveckling (valfritt)

### Systemkrav

- **RAM**: Minst 8GB, 16GB+ rekommenderas för scenarier med flera modeller
- **Lagring**: Minst 10GB ledigt utrymme för modeller och beroenden
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **Hårdvara**: CPU med AVX2-stöd; GPU (CUDA, Qualcomm NPU) valfritt men rekommenderas

### Kunskapsförutsättningar

- Grundläggande förståelse för Python-programmering
- Bekantskap med kommandoradsgränssnitt
- Förståelse för AI/ML-koncept (för utveckling av exempel)
- Git-arbetsflöden och pull request-processer

## Installationskommandon

### Repositoryinstallation

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-exempelinstallation (Modul08 och workshop-exempel)

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

### Node.js-exempelinstallation (Exempel 08 - Windows Chat App)

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

### Foundry Local-installation

Foundry Local krävs för att köra exemplen. Ladda ner och installera från det officiella repositoryt:

**Installation:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuell**: Ladda ner från [releases-sidan](https://github.com/microsoft/Foundry-Local/releases)

**Snabbstart:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Obs**: Foundry Local väljer automatiskt den bästa modellvarianten för din hårdvara (CUDA GPU, Qualcomm NPU eller CPU).

## Utvecklingsarbetsflöde

### Innehållsutveckling

Detta repository innehåller främst **Markdown-utbildningsinnehåll**. Vid ändringar:

1. Redigera `.md`-filer i lämpliga modulkataloger
2. Följ befintliga formateringsmönster
3. Säkerställ att kodexempel är korrekta och testade
4. Uppdatera motsvarande översatt innehåll om nödvändigt (eller låt automatisering hantera det)

### Utveckling av exempelapplikationer

För Modul08 Python-exempel (exempel 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

För workshop Python-exempel:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

För Electron-exempel (exempel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testning av exempelapplikationer

Python-exempel har inga automatiserade tester men kan valideras genom att köra dem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-exempel har testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testinstruktioner

### Validering av innehåll

Repositoryt använder automatiserade översättningsarbetsflöden. Ingen manuell testning krävs för översättningar.

**Manuell validering för innehållsändringar:**
1. Förhandsgranska Markdown-rendering genom att visa `.md`-filer
2. Kontrollera att alla länkar pekar på giltiga mål
3. Testa eventuella kodsnuttar som ingår i dokumentationen
4. Kontrollera att bilder laddas korrekt

### Testning av exempelapplikationer

**Modul08/exempel/08 (Electron-app) har omfattande tester:**
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

**Python-exempel bör testas manuellt:**
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

## Riktlinjer för kodstil

### Markdown-innehåll

- Använd konsekvent rubrikhierarki (# för titel, ## för huvudsektioner, ### för undersektioner)
- Inkludera kodblock med språkspecifikationer: ```python, ```bash, ```javascript
- Följ befintlig formatering för tabeller, listor och betoning
- Håll rader läsbara (sikta på ~80-100 tecken, men inte strikt)
- Använd relativa länkar för interna referenser

### Python-kodstil

- Följ PEP 8-konventioner
- Använd typanvisningar där det är lämpligt
- Inkludera docstrings för funktioner och klasser
- Använd meningsfulla variabelnamn
- Håll funktioner fokuserade och koncisa

### JavaScript/Node.js-kodstil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Viktiga konventioner:**
- ESLint-konfiguration tillhandahålls i exempel 08
- Prettier för kodformatering
- Använd modern ES6+ syntax
- Följ befintliga mönster i kodbasen

## Riktlinjer för pull requests

### Arbetsflöde för bidrag

1. **Forka repositoryt** och skapa en ny gren från `main`
2. **Gör dina ändringar** enligt riktlinjerna för kodstil
3. **Testa noggrant** med hjälp av testinstruktionerna ovan
4. **Commit med tydliga meddelanden** enligt formatet för konventionella commits
5. **Push till din fork** och skapa en pull request
6. **Svara på feedback** från underhållare under granskningen

### Namngivningskonvention för grenar

- `feature/<modul>-<beskrivning>` - För nya funktioner eller innehåll
- `fix/<modul>-<beskrivning>` - För buggfixar
- `docs/<beskrivning>` - För förbättringar av dokumentation
- `refactor/<beskrivning>` - För kodomstrukturering

### Format för commit-meddelanden

Följ [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Exempel:**
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

### Uppförandekod

Alla bidragsgivare måste följa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Läs [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) innan du bidrar.

### Innan du skickar in

**För innehållsändringar:**
- Förhandsgranska alla ändrade Markdown-filer
- Kontrollera att länkar och bilder fungerar
- Kontrollera stavfel och grammatiska fel

**För ändringar i exempelkod (Modul08/exempel/08):**
```bash
npm run lint
npm test
```

**För ändringar i Python-exempel:**
- Testa att exemplet körs framgångsrikt
- Kontrollera att felhantering fungerar
- Kontrollera kompatibilitet med Foundry Local

### Granskningsprocess

- Ändringar i utbildningsinnehåll granskas för noggrannhet och tydlighet
- Kodexempel testas för funktionalitet
- Uppdateringar av översättningar hanteras automatiskt av GitHub Actions

## Översättningssystem

**VIKTIGT:** Detta repository använder automatiserad översättning via GitHub Actions.

- Översättningar finns i katalogen `/translations/` (50+ språk)
- Automatiserad via arbetsflödet `co-op-translator.yml`
- **REDIGERA INTE översättningsfiler manuellt** - de kommer att skrivas över
- Redigera endast engelska källfiler i root- och modulkataloger
- Översättningar genereras automatiskt vid push till `main`-grenen

## Foundry Local-integration

De flesta Modul08-exempel kräver att Microsoft Foundry Local körs.

### Installation och inställning

**Installera Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installera Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Starta Foundry Local
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

### SDK-användning (Python)
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

### Verifiera Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Miljövariabler för exempel

De flesta exempel använder dessa miljövariabler:
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

**Obs**: När du använder `FoundryLocalManager` hanterar SDK automatiskt tjänstupptäckt och modellinladdning. Modellalias (som `phi-3.5-mini`) säkerställer att den bästa varianten väljs för din hårdvara.

## Bygg och distribution

### Innehållsdistribution

Detta repository är främst dokumentation - ingen byggprocess krävs för innehåll.

### Byggande av exempelapplikationer

**Electron-applikation (Modul08/exempel/08):**
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

**Python-exempel:**
Ingen byggprocess - exemplen körs direkt med Python-tolk.

## Vanliga problem och felsökning

> **Tips**: Kontrollera [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) för kända problem och lösningar.

### Kritiska problem (blockerande)

#### Foundry Local körs inte
**Problem:** Exempel misslyckas med anslutningsfel

**Lösning:**
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

### Vanliga problem (måttliga)

#### Problem med Python-virtuella miljöer
**Problem:** Fel vid modulimport

**Lösning:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problem med Electron-bygge
**Problem:** npm install eller byggfel

**Lösning:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Arbetsflödesproblem (mindre)

#### Konflikter i översättningsarbetsflöde
**Problem:** Översättnings-PR konflikter med dina ändringar

**Lösning:**
- Redigera endast engelska källfiler
- Låt det automatiserade översättningsarbetsflödet hantera översättningar
- Om konflikter uppstår, slå samman `main` till din gren efter att översättningar har slagits samman

#### Problem med nedladdning av modeller
**Problem:** Foundry Local misslyckas med att ladda ner modeller

**Lösning:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Ytterligare resurser

### Lärandebanor
- **Nybörjarbana:** Moduler 01-02 (7-9 timmar)
- **Mellanliggande bana:** Moduler 03-04 (9-11 timmar)
- **Avancerad bana:** Moduler 05-07 (12-15 timmar)
- **Expertbana:** Modul 08 (8-10 timmar)
- **Praktisk workshop:** Workshopmaterial (6-8 timmar)

### Viktigt modulinnehåll
- **Modul01:** EdgeAI-grunder och verkliga fallstudier
- **Modul02:** Small Language Model (SLM)-familjer och arkitekturer
- **Modul03:** Lokala och molnbaserade implementeringsstrategier
- **Modul04:** Modelloptimering med flera ramverk (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - produktionsdrift
- **Modul06:** AI-agenter och funktionsanrop
- **Modul07:** Plattformsspecifika implementationer
- **Modul08:** Foundry Local-verktygssats med 10 omfattande exempel

### Externa beroenden
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokal AI-modellruntime med OpenAI-kompatibel API
  - [Dokumentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimeringsramverk
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modelloptimeringsverktyg
- [OpenVINO](https://docs.openvino.ai/) - Intels optimeringsverktyg

## Projekt-specifika anteckningar

### Modul08 exempelapplikationer

Repositoryt innehåller 10 omfattande exempelapplikationer:

1. **01-REST Chat Quickstart** - Grundläggande OpenAI SDK-integration
2. **02-OpenAI SDK Integration** - Avancerade SDK-funktioner
3. **03-Model Discovery & Benchmarking** - Verktyg för modelljämförelse
4. **04-Chainlit RAG Application** - Generering med återhämtning
5. **05-Multi-Agent Orchestration** - Grundläggande agentkoordinering
6. **06-Models-as-Tools Router** - Intelligent modellroutning
7. **07-Direct API Client** - Låg nivå API-integration
8. **08-Windows 11 Chat App** - Native Electron desktop-applikation
9. **09-Avancerat multi-agent system** - Komplex agentkoordinering
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integration

### Workshop Exempelapplikationer

Workshopen innehåller 6 progressiva sessioner med praktiska implementationer:

1. **Session 01** - Chat-start med Foundry Local integration
2. **Session 02** - RAG-pipeline och utvärdering med RAGAS
3. **Session 03** - Benchmarking av open-source modeller
4. **Session 04** - Modelljämförelse och urval
5. **Session 05** - Orkestreringssystem för flera agenter
6. **Session 06** - Modellroutning och pipelinehantering

Varje exempel demonstrerar olika aspekter av Edge AI-utveckling med Foundry Local.

### Prestandaöverväganden

- SLMs är optimerade för edge-distribution (2-16GB RAM)
- Lokal inferens ger svarstider på 50-500ms
- Kvantiseringstekniker uppnår 75% storleksreduktion med 85% prestandabehållning
- Realtidskonversationsmöjligheter med lokala modeller

### Säkerhet och integritet

- All bearbetning sker lokalt - ingen data skickas till molnet
- Lämplig för integritetskänsliga applikationer (sjukvård, finans)
- Uppfyller krav på datasuveränitet
- Foundry Local körs helt på lokal hårdvara

## Få hjälp

### Dokumentation

- **Huvud README**: [README.md](README.md) - Översikt över repository och lärandespår
- **Studieguide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Läranderesurser och tidslinje
- **Support**: [SUPPORT.md](SUPPORT.md) - Hur man får hjälp
- **Säkerhet**: [SECURITY.md](SECURITY.md) - Rapportering av säkerhetsproblem

### Community Support

- **GitHub Issues**: [Rapportera buggar eller begär funktioner](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Ställ frågor och dela idéer](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Tekniska problem med Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Underhållare**: Se [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Säkerhetsproblem**: Följ ansvarsfull rapportering i [SECURITY.md](SECURITY.md)
- **Microsoft Support**: För företagsstöd, kontakta Microsoft kundtjänst

### Ytterligare resurser

- **Microsoft Learn**: [AI och maskininlärning lärandespår](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentation**: [Officiell dokumentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Community Exempel**: Kolla [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) för community-bidrag

---

**Detta är ett utbildningsrepository som fokuserar på att lära ut Edge AI-utveckling. Det primära bidragsmönstret är att förbättra utbildningsinnehållet och lägga till/förbättra exempelapplikationer som demonstrerar Edge AI-koncept.**

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.