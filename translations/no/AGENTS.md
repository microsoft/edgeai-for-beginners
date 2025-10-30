<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:09:52+00:00",
  "source_file": "AGENTS.md",
  "language_code": "no"
}
-->
# AGENTS.md

> **Utviklerveiledning for å bidra til EdgeAI for nybegynnere**
> 
> Dette dokumentet gir omfattende informasjon for utviklere, AI-agenter og bidragsytere som jobber med dette repositoriet. Det dekker oppsett, utviklingsarbeidsflyter, testing og beste praksis.
> 
> **Sist oppdatert**: 30. oktober 2025 | **Dokumentversjon**: 3.0

## Innholdsfortegnelse

- [Prosjektoversikt](../..)
- [Repository-struktur](../..)
- [Forutsetninger](../..)
- [Oppsettskommandoer](../..)
- [Utviklingsarbeidsflyt](../..)
- [Testinstruksjoner](../..)
- [Retningslinjer for kodestil](../..)
- [Retningslinjer for pull requests](../..)
- [Oversettelsessystem](../..)
- [Foundry Local-integrasjon](../..)
- [Bygging og distribusjon](../..)
- [Vanlige problemer og feilsøking](../..)
- [Ekstra ressurser](../..)
- [Prosjektspesifikke notater](../..)
- [Få hjelp](../..)

## Prosjektoversikt

EdgeAI for nybegynnere er et omfattende utdanningsrepository som lærer Edge AI-utvikling med små språkmodeller (SLMs). Kurset dekker EdgeAI-grunnleggende, modellimplementering, optimaliseringsteknikker og produksjonsklare implementeringer ved bruk av Microsoft Foundry Local og ulike AI-rammeverk.

**Nøkkelteknologier:**
- Python 3.8+ (primærspråk for AI/ML-eksempler)
- .NET C# (AI/ML-eksempler)
- JavaScript/Node.js med Electron (for skrivebordsapplikasjoner)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-rammeverk: LangChain, Semantic Kernel, Chainlit
- Modelloptimalisering: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository-type:** Utdanningsinnhold med 8 moduler og 10 omfattende eksempelapplikasjoner

**Arkitektur:** Læringssti med flere moduler og praktiske eksempler som demonstrerer Edge AI-implementeringsmønstre

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

## Forutsetninger

### Nødvendige verktøy

- **Python 3.8+** - For AI/ML-eksempler og notatbøker
- **Node.js 16+** - For Electron-eksempelapplikasjon
- **Git** - For versjonskontroll
- **Microsoft Foundry Local** - For å kjøre AI-modeller lokalt

### Anbefalte verktøy

- **Visual Studio Code** - Med Python-, Jupyter- og Pylance-utvidelser
- **Windows Terminal** - For bedre kommandolinjeopplevelse (Windows-brukere)
- **Docker** - For containerbasert utvikling (valgfritt)

### Systemkrav

- **RAM**: Minimum 8GB, anbefalt 16GB+ for scenarier med flere modeller
- **Lagring**: 10GB+ ledig plass for modeller og avhengigheter
- **OS**: Windows 10/11, macOS 11+, eller Linux (Ubuntu 20.04+)
- **Maskinvare**: CPU med AVX2-støtte; GPU (CUDA, Qualcomm NPU) valgfritt, men anbefalt

### Kunnskapsforutsetninger

- Grunnleggende forståelse av Python-programmering
- Kjennskap til kommandolinjegrensesnitt
- Forståelse av AI/ML-konsepter (for utvikling av eksempler)
- Git-arbeidsflyter og pull request-prosesser

## Oppsettskommandoer

### Repository-oppsett

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-eksempeloppsett (Modul08 og Workshop-eksempler)

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

### Node.js-eksempeloppsett (Eksempel 08 - Windows Chat App)

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

### Foundry Local-oppsett

Foundry Local er nødvendig for å kjøre eksemplene. Last ned og installer fra det offisielle repositoriet:

**Installasjon:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuell**: Last ned fra [releases-siden](https://github.com/microsoft/Foundry-Local/releases)

**Hurtigstart:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Merk**: Foundry Local velger automatisk den beste modellvarianten for maskinvaren din (CUDA GPU, Qualcomm NPU eller CPU).

## Utviklingsarbeidsflyt

### Innholdsutvikling

Dette repositoriet inneholder primært **Markdown utdanningsinnhold**. Når du gjør endringer:

1. Rediger `.md`-filer i de relevante modulmappene
2. Følg eksisterende formateringsmønstre
3. Sørg for at kodeeksempler er nøyaktige og testet
4. Oppdater tilsvarende oversatt innhold hvis nødvendig (eller la automatisering håndtere det)

### Utvikling av eksempelapplikasjoner

For Modul08 Python-eksempler (eksempler 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

For Workshop Python-eksempler:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

For Electron-eksempel (eksempel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testing av eksempelapplikasjoner

Python-eksempler har ikke automatiserte tester, men kan valideres ved å kjøre dem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-eksemplet har testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testinstruksjoner

### Validering av innhold

Repositoriet bruker automatiserte oversettelsesarbeidsflyter. Ingen manuell testing kreves for oversettelser.

**Manuell validering for innholdsendringer:**
1. Forhåndsvis Markdown-rendering ved å se på `.md`-filer
2. Bekreft at alle lenker peker til gyldige mål
3. Test eventuelle kodeeksempler som er inkludert i dokumentasjonen
4. Sjekk at bilder lastes korrekt

### Testing av eksempelapplikasjoner

**Modul08/eksempler/08 (Electron-app) har omfattende testing:**
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

**Python-eksempler bør testes manuelt:**
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

### Markdown-innhold

- Bruk konsistent overskrifthierarki (# for tittel, ## for hovedseksjoner, ### for underseksjoner)
- Inkluder kodeblokker med språkspesifikasjoner: ```python, ```bash, ```javascript
- Følg eksisterende formatering for tabeller, lister og utheving
- Hold linjer lesbare (sikt på ~80-100 tegn, men ikke strengt)
- Bruk relative lenker for interne referanser

### Python-kodestil

- Følg PEP 8-konvensjoner
- Bruk typehint der det er hensiktsmessig
- Inkluder docstrings for funksjoner og klasser
- Bruk meningsfulle variabelnavn
- Hold funksjoner fokuserte og konsise

### JavaScript/Node.js-kodestil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Viktige konvensjoner:**
- ESLint-konfigurasjon er inkludert i eksempel 08
- Prettier for kodeformatering
- Bruk moderne ES6+ syntaks
- Følg eksisterende mønstre i kodebasen

## Retningslinjer for pull requests

### Bidragsarbeidsflyt

1. **Fork repositoriet** og opprett en ny gren fra `main`
2. **Gjør endringene dine** i henhold til kodestilretningslinjene
3. **Test grundig** ved å bruke testinstruksjonene ovenfor
4. **Commit med klare meldinger** i henhold til konvensjonelle commit-format
5. **Push til din fork** og opprett en pull request
6. **Svar på tilbakemeldinger** fra vedlikeholdere under gjennomgang

### Navnekonvensjon for grener

- `feature/<modul>-<beskrivelse>` - For nye funksjoner eller innhold
- `fix/<modul>-<beskrivelse>` - For feilrettinger
- `docs/<beskrivelse>` - For dokumentasjonsforbedringer
- `refactor/<beskrivelse>` - For kodeomstrukturering

### Commit-meldingsformat

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

### Tittelformat
```
[ModuleXX] Brief description of change
```
eller
```
[Module08/samples/XX] Description for sample changes
```

### Etiske retningslinjer

Alle bidragsytere må følge [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Vennligst les [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) før du bidrar.

### Før innsending

**For innholdsendringer:**
- Forhåndsvis alle endrede Markdown-filer
- Bekreft at lenker og bilder fungerer
- Sjekk for skrivefeil og grammatiske feil

**For endringer i eksempelkode (Modul08/eksempler/08):**
```bash
npm run lint
npm test
```

**For endringer i Python-eksempler:**
- Test at eksemplet kjører vellykket
- Bekreft at feilhåndtering fungerer
- Sjekk kompatibilitet med Foundry Local

### Gjennomgangsprosess

- Endringer i utdanningsinnhold gjennomgås for nøyaktighet og klarhet
- Kodeeksempler testes for funksjonalitet
- Oppdateringer av oversettelser håndteres automatisk av GitHub Actions

## Oversettelsessystem

**VIKTIG:** Dette repositoriet bruker automatisert oversettelse via GitHub Actions.

- Oversettelser finnes i `/translations/`-mappen (50+ språk)
- Automatisert via `co-op-translator.yml`-arbeidsflyt
- **IKKE rediger oversettelsesfiler manuelt** - de vil bli overskrevet
- Rediger kun engelske kildefiler i rot- og modulmapper
- Oversettelser genereres automatisk ved push til `main`-grenen

## Foundry Local-integrasjon

De fleste Modul08-eksempler krever at Microsoft Foundry Local kjører.

### Installasjon og oppsett

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

### Starte Foundry Local
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

### SDK-bruk (Python)
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

### Verifisere Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Miljøvariabler for eksempler

De fleste eksempler bruker disse miljøvariablene:
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

**Merk**: Når du bruker `FoundryLocalManager`, håndterer SDK automatisk tjenesteoppdagelse og modellinnlasting. Modellaliaser (som `phi-3.5-mini`) sikrer at den beste varianten velges for maskinvaren din.

## Bygging og distribusjon

### Innholdsdistribusjon

Dette repositoriet er primært dokumentasjon - ingen byggeprosess kreves for innhold.

### Bygging av eksempelapplikasjoner

**Electron-applikasjon (Modul08/eksempler/08):**
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

**Python-eksempler:**
Ingen byggeprosess - eksempler kjøres direkte med Python-tolk.

## Vanlige problemer og feilsøking

> **Tips**: Sjekk [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) for kjente problemer og løsninger.

### Kritiske problemer (blokkerende)

#### Foundry Local kjører ikke
**Problem:** Eksempler feiler med tilkoblingsfeil

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

### Vanlige problemer (moderat)

#### Problemer med Python-virtuelt miljø
**Problem:** Feil ved import av moduler

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

#### Problemer med Electron-bygging
**Problem:** npm install eller byggfeil

**Løsning:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Arbeidsflytproblemer (mindre)

#### Konflikter i oversettelsesarbeidsflyt
**Problem:** Oversettelses-PR konflikter med endringene dine

**Løsning:**
- Rediger kun engelske kildefiler
- La den automatiserte oversettelsesarbeidsflyten håndtere oversettelser
- Hvis konflikter oppstår, slå sammen `main` inn i grenen din etter at oversettelser er slått sammen

#### Feil ved nedlasting av modeller
**Problem:** Foundry Local feiler med å laste ned modeller

**Løsning:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Ekstra ressurser

### Læringsstier
- **Nybegynnersti:** Moduler 01-02 (7-9 timer)
- **Mellomnivåsti:** Moduler 03-04 (9-11 timer)
- **Avansert sti:** Moduler 05-07 (12-15 timer)
- **Ekspertsti:** Modul 08 (8-10 timer)
- **Praktisk workshop:** Workshop-materialer (6-8 timer)

### Nøkkelinnhold i moduler
- **Modul01:** EdgeAI-grunnleggende og virkelige casestudier
- **Modul02:** Små språkmodellfamilier og arkitekturer
- **Modul03:** Lokale og skybaserte implementeringsstrategier
- **Modul04:** Modelloptimalisering med flere rammeverk (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - produksjonsoperasjoner
- **Modul06:** AI-agenter og funksjonskall
- **Modul07:** Plattformspesifikke implementeringer
- **Modul08:** Foundry Local-verktøysett med 10 omfattende eksempler

### Eksterne avhengigheter
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokal AI-modell runtime med OpenAI-kompatibel API
  - [Dokumentasjon](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimaliseringsrammeverk
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modelloptimaliseringsverktøy
- [OpenVINO](https://docs.openvino.ai/) - Intels optimaliseringsverktøy

## Prosjektspesifikke notater

### Modul08 Eksempelapplikasjoner

Repositoriet inkluderer 10 omfattende eksempelapplikasjoner:

1. **01-REST Chat Quickstart** - Grunnleggende OpenAI SDK-integrasjon
2. **02-OpenAI SDK Integration** - Avanserte SDK-funksjoner
3. **03-Model Discovery & Benchmarking** - Verktøy for modell-sammenligning
4. **04-Chainlit RAG Application** - Generering med informasjonsinnhenting
5. **05-Multi-Agent Orchestration** - Grunnleggende agentkoordinering
6. **06-Models-as-Tools Router** - Intelligent modellruting
7. **07-Direct API Client** - Lavnivå API-integrasjon
8. **08-Windows 11 Chat App** - Native Electron skrivebordsapplikasjon
9. **09-Avansert Multi-Agent System** - Kompleks agentkoordinering
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel-integrasjon

### Workshop Eksempelapplikasjoner

Workshopen inkluderer 6 progressive økter med praktiske implementeringer:

1. **Økt 01** - Chat bootstrap med Foundry Local-integrasjon
2. **Økt 02** - RAG-pipeline og evaluering med RAGAS
3. **Økt 03** - Benchmarking av open-source modeller
4. **Økt 04** - Modell-sammenligning og valg
5. **Økt 05** - Orkestreringssystemer for multi-agent
6. **Økt 06** - Modellruting og pipeline-håndtering

Hver eksempelapplikasjon demonstrerer ulike aspekter av Edge AI-utvikling med Foundry Local.

### Ytelseshensyn

- SLM-er er optimalisert for edge-deployering (2-16GB RAM)
- Lokal inferens gir responstider på 50-500ms
- Kvantiseringsteknikker oppnår 75% størrelsesreduksjon med 85% ytelsesbevaring
- Sanntids samtalefunksjoner med lokale modeller

### Sikkerhet og Personvern

- All prosessering skjer lokalt - ingen data sendes til skyen
- Egnet for applikasjoner med høye personvernkrav (helse, finans)
- Oppfyller krav til datasuverenitet
- Foundry Local kjører helt på lokal maskinvare

## Få Hjelp

### Dokumentasjon

- **Hoved README**: [README.md](README.md) - Oversikt over repository og læringsveier
- **Studieguide**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Læringsressurser og tidslinje
- **Støtte**: [SUPPORT.md](SUPPORT.md) - Hvordan få hjelp
- **Sikkerhet**: [SECURITY.md](SECURITY.md) - Rapportering av sikkerhetsproblemer

### Fellesskapsstøtte

- **GitHub Issues**: [Rapporter feil eller foreslå funksjoner](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Still spørsmål og del ideer](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Tekniske problemer med Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Vedlikeholdere**: Se [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Sikkerhetsproblemer**: Følg ansvarlig rapportering i [SECURITY.md](SECURITY.md)
- **Microsoft Support**: For bedriftsstøtte, kontakt Microsoft kundeservice

### Ekstra Ressurser

- **Microsoft Learn**: [Læringsveier for AI og maskinlæring](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentasjon**: [Offisiell dokumentasjon](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Fellesskaps-eksempler**: Sjekk [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) for bidrag fra fellesskapet

---

**Dette er et utdanningsrepository som fokuserer på å lære Edge AI-utvikling. Det primære bidragsmønsteret er å forbedre utdanningsinnhold og legge til/forbedre eksempelapplikasjoner som demonstrerer Edge AI-konsepter.**

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.