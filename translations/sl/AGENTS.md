<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T14:57:22+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sl"
}
-->
# AGENTS.md

> **Razvijalčev vodnik za prispevanje k EdgeAI za začetnike**
> 
> Ta dokument ponuja obsežne informacije za razvijalce, AI agente in sodelujoče, ki delajo s tem repozitorijem. Pokriva nastavitev, delovne tokove razvoja, testiranje in najboljše prakse.
> 
> **Zadnja posodobitev**: 30. oktober 2025 | **Različica dokumenta**: 3.0

## Kazalo vsebine

- [Pregled projekta](../..)
- [Struktura repozitorija](../..)
- [Predpogoji](../..)
- [Ukazi za nastavitev](../..)
- [Delovni tok razvoja](../..)
- [Navodila za testiranje](../..)
- [Smernice za slog kode](../..)
- [Smernice za zahteve za združitev](../..)
- [Sistem za prevajanje](../..)
- [Integracija Foundry Local](../..)
- [Gradnja in uvajanje](../..)
- [Pogoste težave in odpravljanje napak](../..)
- [Dodatni viri](../..)
- [Opombe, specifične za projekt](../..)
- [Pomoč](../..)

## Pregled projekta

EdgeAI za začetnike je obsežen izobraževalni repozitorij, ki poučuje razvoj Edge AI z malimi jezikovnimi modeli (SLM). Tečaj pokriva osnove EdgeAI, uvajanje modelov, tehnike optimizacije in implementacije, pripravljene za produkcijo, z uporabo Microsoft Foundry Local in različnih AI ogrodij.

**Ključne tehnologije:**
- Python 3.8+ (glavni jezik za AI/ML vzorce)
- .NET C# (AI/ML vzorci)
- JavaScript/Node.js z Electron (za namizne aplikacije)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI ogrodja: LangChain, Semantic Kernel, Chainlit
- Optimizacija modelov: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Vrsta repozitorija:** Izobraževalni repozitorij z 8 moduli in 10 obsežnimi vzorčnimi aplikacijami

**Arhitektura:** Večmodulna učna pot s praktičnimi vzorci, ki prikazujejo vzorce uvajanja Edge AI

## Struktura repozitorija

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

## Predpogoji

### Zahtevana orodja

- **Python 3.8+** - Za AI/ML vzorce in beležke
- **Node.js 16+** - Za vzorčno aplikacijo Electron
- **Git** - Za nadzor različic
- **Microsoft Foundry Local** - Za lokalno izvajanje AI modelov

### Priporočena orodja

- **Visual Studio Code** - Z razširitvami Python, Jupyter in Pylance
- **Windows Terminal** - Za boljšo izkušnjo ukazne vrstice (uporabniki Windows)
- **Docker** - Za razvoj v kontejnerjih (neobvezno)

### Sistemske zahteve

- **RAM**: najmanj 8GB, priporočljivo 16GB+ za scenarije z več modeli
- **Shramba**: najmanj 10GB prostega prostora za modele in odvisnosti
- **OS**: Windows 10/11, macOS 11+ ali Linux (Ubuntu 20.04+)
- **Strojna oprema**: CPU s podporo za AVX2; GPU (CUDA, Qualcomm NPU) neobvezno, vendar priporočljivo

### Predhodno znanje

- Osnovno razumevanje programiranja v Pythonu
- Seznanjenost z ukaznimi vrsticami
- Razumevanje konceptov AI/ML (za razvoj vzorcev)
- Git delovni tokovi in procesi zahtev za združitev

## Ukazi za nastavitev

### Nastavitev repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Nastavitev Python vzorcev (Modul08 in delavniški vzorci)

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

### Nastavitev Node.js vzorcev (Vzorec 08 - Windows Chat App)

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

### Nastavitev Foundry Local

Foundry Local je potreben za izvajanje vzorcev. Prenesite in namestite iz uradnega repozitorija:

**Namestitev:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ročno**: Prenesite z [strani z izdajami](https://github.com/microsoft/Foundry-Local/releases)

**Hitri začetek:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Opomba**: Foundry Local samodejno izbere najboljšo različico modela za vašo strojno opremo (CUDA GPU, Qualcomm NPU ali CPU).

## Delovni tok razvoja

### Razvoj vsebine

Ta repozitorij vsebuje predvsem **Markdown izobraževalno vsebino**. Pri spreminjanju:

1. Uredite `.md` datoteke v ustreznih modulskih imenikih
2. Upoštevajte obstoječe vzorce oblikovanja
3. Poskrbite, da so primeri kode točni in preizkušeni
4. Po potrebi posodobite ustrezno prevedeno vsebino (ali pustite, da to opravi avtomatizacija)

### Razvoj vzorčnih aplikacij

Za Python vzorce Modula08 (vzorce 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Za delavniške Python vzorce:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Za vzorec Electron (vzorec 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testiranje vzorčnih aplikacij

Python vzorci nimajo avtomatiziranih testov, vendar jih je mogoče preveriti z zagonom:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Vzorec Electron ima infrastrukturo za testiranje:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Navodila za testiranje

### Preverjanje vsebine

Repozitorij uporablja avtomatizirane delovne tokove za prevajanje. Ročno testiranje prevodov ni potrebno.

**Ročno preverjanje sprememb vsebine:**
1. Preglejte upodabljanje Markdown z ogledom `.md` datotek
2. Preverite, ali vse povezave kažejo na veljavne cilje
3. Preizkusite vse kode, vključene v dokumentacijo
4. Preverite, ali se slike pravilno nalagajo

### Testiranje vzorčnih aplikacij

**Module08/samples/08 (Electron aplikacija) ima obsežno testiranje:**
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

**Python vzorce je treba testirati ročno:**
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

## Smernice za slog kode

### Markdown vsebina

- Uporabljajte dosledno hierarhijo naslovov (# za naslov, ## za glavne razdelke, ### za podrazdelke)
- Vključite kode z določenimi jeziki: ```python, ```bash, ```javascript
- Upoštevajte obstoječe oblikovanje za tabele, sezname in poudarke
- Naj bodo vrstice berljive (cilj ~80-100 znakov, vendar ne strogo)
- Uporabljajte relativne povezave za notranje reference

### Slog kode Python

- Upoštevajte konvencije PEP 8
- Uporabljajte tipe, kjer je primerno
- Vključite docstring za funkcije in razrede
- Uporabljajte smiselna imena spremenljivk
- Naj bodo funkcije osredotočene in jedrnate

### Slog kode JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Ključne konvencije:**
- Konfiguracija ESLint je na voljo v vzorcu 08
- Prettier za oblikovanje kode
- Uporabljajte sodobno sintakso ES6+
- Upoštevajte obstoječe vzorce v kodi

## Smernice za zahteve za združitev

### Delovni tok prispevkov

1. **Forkajte repozitorij** in ustvarite novo vejo iz `main`
2. **Naredite spremembe** v skladu s smernicami za slog kode
3. **Temeljito testirajte** z uporabo zgoraj navedenih navodil za testiranje
4. **Zavežite z jasnimi sporočili** v skladu s formatom konvencionalnih zavez
5. **Potisnite v svoj fork** in ustvarite zahtevo za združitev
6. **Odgovorite na povratne informacije** vzdrževalcev med pregledom

### Konvencija poimenovanja vej

- `feature/<modul>-<opis>` - Za nove funkcije ali vsebino
- `fix/<modul>-<opis>` - Za odpravo napak
- `docs/<opis>` - Za izboljšave dokumentacije
- `refactor/<opis>` - Za prestrukturiranje kode

### Format sporočila zavez

Sledite [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Primeri:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format naslova
```
[ModuleXX] Brief description of change
```
ali
```
[Module08/samples/XX] Description for sample changes
```

### Kodeks ravnanja

Vsi sodelujoči morajo upoštevati [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Pred prispevanjem preglejte [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

### Pred oddajo

**Za spremembe vsebine:**
- Predogled vseh spremenjenih Markdown datotek
- Preverite, ali povezave in slike delujejo
- Preverite tipkarske in slovnične napake

**Za spremembe vzorčne kode (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Za spremembe Python vzorcev:**
- Preverite, ali vzorec uspešno deluje
- Preverite, ali obravnava napak deluje
- Preverite združljivost s Foundry Local

### Postopek pregleda

- Spremembe izobraževalne vsebine se pregledajo glede točnosti in jasnosti
- Vzorci kode se testirajo glede funkcionalnosti
- Posodobitve prevodov se obravnavajo samodejno prek GitHub Actions

## Sistem za prevajanje

**POMEMBNO:** Ta repozitorij uporablja avtomatizirano prevajanje prek GitHub Actions.

- Prevedene datoteke so v imeniku `/translations/` (50+ jezikov)
- Avtomatizirano prek delovnega toka `co-op-translator.yml`
- **NE urejajte ročno prevedenih datotek** - te bodo prepisane
- Urejajte samo izvorne datoteke v angleščini v korenskem in modulskih imenikih
- Prevajanja se samodejno generirajo ob potisku v vejo `main`

## Integracija Foundry Local

Večina vzorcev Modula08 zahteva, da Microsoft Foundry Local deluje.

### Namestitev in nastavitev

**Namestite Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Namestite Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Zagon Foundry Local
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

### Uporaba SDK (Python)
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

### Preverjanje Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Spremenljivke okolja za vzorce

Večina vzorcev uporablja te spremenljivke okolja:
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

**Opomba**: Pri uporabi `FoundryLocalManager` SDK samodejno upravlja odkrivanje storitev in nalaganje modelov. Alias modelov (kot `phi-3.5-mini`) zagotavlja izbiro najboljše različice za vašo strojno opremo.

## Gradnja in uvajanje

### Uvajanje vsebine

Ta repozitorij je predvsem dokumentacija - proces gradnje za vsebino ni potreben.

### Gradnja vzorčnih aplikacij

**Electron aplikacija (Module08/samples/08):**
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

**Python vzorci:**
Proces gradnje ni potreben - vzorci se izvajajo neposredno z interpreterjem Python.

## Pogoste težave in odpravljanje napak

> **Nasvet**: Preverite [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) za znane težave in rešitve.

### Kritične težave (blokirajoče)

#### Foundry Local ne deluje
**Težava:** Vzorci ne uspejo zaradi napak povezave

**Rešitev:**
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

### Pogoste težave (zmerne)

#### Težave z virtualnim okoljem Python
**Težava:** Napake pri uvozu modulov

**Rešitev:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Težave pri gradnji Electron
**Težava:** Napake pri `npm install` ali gradnji

**Rešitev:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Težave z delovnim tokom (manjše)

#### Konflikti delovnega toka prevajanja
**Težava:** Konflikti prevajalskih PR-jev z vašimi spremembami

**Rešitev:**
- Urejajte samo izvorne datoteke v angleščini
- Pustite, da avtomatizirani delovni tok prevajanja obravnava prevode
- Če pride do konfliktov, združite `main` v svojo vejo po združitvi prevodov

#### Napake pri prenosu modelov
**Težava:** Foundry Local ne uspe prenesti modelov

**Rešitev:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Dodatni viri

### Učne poti
- **Pot za začetnike:** Moduli 01-02 (7-9 ur)
- **Pot za srednje napredne:** Moduli 03-04 (9-11 ur)
- **Pot za napredne:** Moduli 05-07 (12-15 ur)
- **Pot za strokovnjake:** Modul 08 (8-10 ur)
- **Praktična delavnica:** Gradivo za delavnico (6-8 ur)

### Ključna vsebina modulov
- **Modul01:** Osnove EdgeAI in študije primerov iz resničnega sveta
- **Modul02:** Družine in arhitekture malih jezikovnih modelov (SLM)
- **Modul03:** Strategije lokalnega in oblačnega uvajanja
- **Modul04:** Optimizacija modelov z več ogrodji (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - operacije v produkciji
- **Modul06:** AI agenti in klicanje funkcij
- **Modul07:** Implementacije, specifične za platformo
- **Modul08:** Orodje Foundry Local z 10 obsežnimi vzorci

### Zunanje odvisnosti
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokalni runtime AI modelov z OpenAI-kompatibilnim API-jem
  - [Dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Ogrodje za optimizacijo
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Orodje za optimizacijo modelov
- [OpenVINO](https://docs.openvino.ai/) - Intelovo orodje za optimizacijo

## Opombe, specifične za projekt

### Vzorčne aplikacije Modula08

Repozitorij vključuje 10 obsežnih vzorčnih aplikacij:

1. **01-REST Chat Quickstart** - Osnovna integracija OpenAI SDK
2. **02-OpenAI SDK Integration** - Napredne funkcije SDK
3. **03-Model Discovery & Benchmarking** - Orodja za primerjavo modelov
4. **04-Chainlit RAG Application** - Generacija, podprta z iskanjem
5. **05-Multi-Agent Orchestration** - Osnovna koordinacija agentov
6. **06-Models-as-Tools Router** - Inteligentno usmerjanje modelov
7. **07-Direct API Client** - Nizkoročnostna integracija API-ja
8. **08-Windows 11 Chat App** - Domača namizna aplikacija Electron
9. **09-Advanced Multi-Agent System** - Kompleksna orkestracija agentov
10. **10-Orodja Foundry Framework** - Integracija LangChain/Semantic Kernel

### Primeri aplikacij delavnice

Delavnica vključuje 6 progresivnih sej s praktičnimi implementacijami:

1. **Seja 01** - Zagon klepeta z integracijo Foundry Local
2. **Seja 02** - RAG cevovod in ocenjevanje z RAGAS
3. **Seja 03** - Primerjalno testiranje odprtokodnih modelov
4. **Seja 04** - Primerjava in izbira modelov
5. **Seja 05** - Sistemi za orkestracijo več agentov
6. **Seja 06** - Usmerjanje modelov in upravljanje cevovodov

Vsak primer prikazuje različne vidike razvoja Edge AI z Foundry Local.

### Upoštevanje zmogljivosti

- SLM-ji so optimizirani za robno uporabo (2-16GB RAM)
- Lokalno sklepanje omogoča odzivne čase med 50-500ms
- Tehnike kvantizacije dosežejo 75% zmanjšanje velikosti z 85% ohranitvijo zmogljivosti
- Zmožnosti pogovorov v realnem času z lokalnimi modeli

### Varnost in zasebnost

- Vsa obdelava poteka lokalno - podatki se ne pošiljajo v oblak
- Primerno za aplikacije, občutljive na zasebnost (zdravstvo, finance)
- Izpolnjuje zahteve glede suverenosti podatkov
- Foundry Local deluje popolnoma na lokalni strojni opremi

## Pomoč

### Dokumentacija

- **Glavni README**: [README.md](README.md) - Pregled repozitorija in učne poti
- **Učni vodič**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Učni viri in časovni načrt
- **Podpora**: [SUPPORT.md](SUPPORT.md) - Kako dobiti pomoč
- **Varnost**: [SECURITY.md](SECURITY.md) - Poročanje o varnostnih težavah

### Podpora skupnosti

- **GitHub Issues**: [Prijava napak ali zahteva za funkcije](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Postavite vprašanja in delite ideje](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Težave Foundry Local**: [Tehnične težave s Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Vzdrževalci**: Glejte [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Varnostne težave**: Sledite odgovornemu razkritju v [SECURITY.md](SECURITY.md)
- **Microsoft podpora**: Za podporo podjetjem se obrnite na Microsoftovo službo za stranke

### Dodatni viri

- **Microsoft Learn**: [Učne poti za AI in strojno učenje](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Dokumentacija Foundry Local**: [Uradna dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Primeri skupnosti**: Preverite [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) za prispevke skupnosti

---

**To je izobraževalni repozitorij, osredotočen na poučevanje razvoja Edge AI. Glavni vzorec prispevkov je izboljšanje izobraževalne vsebine in dodajanje/izboljšanje primerov aplikacij, ki prikazujejo koncepte Edge AI.**

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.