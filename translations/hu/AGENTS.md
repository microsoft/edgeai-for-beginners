# AGENTS.md

> **Fejlesztői útmutató kezdőknek szánt EdgeAI hozzájáruláshoz**
> 
> Ez a dokumentum átfogó információkat nyújt a fejlesztőknek, AI ügynököknek és közreműködőknek, akik ezen a táron dolgoznak. Tartalmazza a beállítást, fejlesztési munkafolyamatokat, tesztelést és legjobb gyakorlatokat.
> 
> **Utolsó frissítés**: 2025. október 30. | **Dokumentum verzió**: 3.0

## Tartalomjegyzék

- [Projekt áttekintés](../..)
- [Tároló struktúra](../..)
- [Előfeltételek](../..)
- [Beállítási parancsok](../..)
- [Fejlesztési munkafolyamat](../..)
- [Tesztelési utasítások](../..)
- [Kódstílus irányelvek](../..)
- [Pull Request irányelvek](../..)
- [Fordítási rendszer](../..)
- [Foundry Local integráció](../..)
- [Build és telepítés](../..)
- [Gyakori problémák és hibaelhárítás](../..)
- [További források](../..)
- [Projekt-specifikus megjegyzések](../..)
- [Segítség kérése](../..)

## Projekt áttekintés

Az EdgeAI for Beginners egy átfogó oktatási tároló, amely az Edge AI fejlesztést tanítja Kis Nyelvi Modellekkel (SLM-ek). A kurzus az EdgeAI alapjait, modell telepítést, optimalizálási technikákat és gyártásra kész megvalósításokat tárgyalja a Microsoft Foundry Local és különböző AI keretrendszerek használatával.

**Kulcstechnológiák:**
- Python 3.8+ (AI/ML minták elsődleges nyelve)
- .NET C# (AI/ML minták)
- JavaScript/Node.js Electronnal (asztali alkalmazásokhoz)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI keretrendszerek: LangChain, Semantic Kernel, Chainlit
- Modell optimalizálás: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tároló típusa:** Oktatási tartalom tároló 8 modul és 10 átfogó mintapéldával

**Architektúra:** Többmodulos tanulási útvonal gyakorlati mintákkal, amelyek bemutatják az Edge AI telepítési mintákat

## Tároló struktúra

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

## Előfeltételek

### Szükséges eszközök

- **Python 3.8+** - AI/ML mintákhoz és jegyzetfüzetekhez
- **Node.js 16+** - Electron mintapéldához
- **Git** - Verziókezeléshez
- **Microsoft Foundry Local** - AI modellek helyi futtatásához

### Ajánlott eszközök

- **Visual Studio Code** - Python, Jupyter és Pylance bővítményekkel
- **Windows Terminal** - Jobb parancssori élményhez (Windows felhasználók számára)
- **Docker** - Konténeres fejlesztéshez (opcionális)

### Rendszerkövetelmények

- **RAM**: Minimum 8GB, ajánlott 16GB+ többmodell-szcenáriókhoz
- **Tárhely**: Legalább 10GB szabad hely modellekhez és függőségekhez
- **Operációs rendszer**: Windows 10/11, macOS 11+, vagy Linux (Ubuntu 20.04+)
- **Hardver**: AVX2 támogatással rendelkező CPU; GPU (CUDA, Qualcomm NPU) opcionális, de ajánlott

### Tudás előfeltételek

- Alapvető Python programozási ismeretek
- Parancssori felületek ismerete
- AI/ML fogalmak megértése (minták fejlesztéséhez)
- Git munkafolyamatok és pull request folyamatok ismerete

## Beállítási parancsok

### Tároló beállítása

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python minták beállítása (Module08 és Workshop minták)

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

### Node.js minták beállítása (Minta 08 - Windows Chat App)

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

### Foundry Local beállítása

A Foundry Local szükséges a minták futtatásához. Töltse le és telepítse az hivatalos tárolóból:

**Telepítés:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuális**: Töltse le a [kiadások oldaláról](https://github.com/microsoft/Foundry-Local/releases)

**Gyors kezdés:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Megjegyzés**: A Foundry Local automatikusan kiválasztja a legjobb modellváltozatot a hardveréhez (CUDA GPU, Qualcomm NPU vagy CPU).

## Fejlesztési munkafolyamat

### Tartalomfejlesztés

Ez a tároló elsősorban **Markdown oktatási tartalmat** tartalmaz. Módosítások végrehajtásakor:

1. Szerkessze a megfelelő modul könyvtárakban található `.md` fájlokat
2. Kövesse a meglévő formázási mintákat
3. Biztosítsa, hogy a kódpéldák pontosak és teszteltek legyenek
4. Frissítse a megfelelő fordított tartalmat, ha szükséges (vagy hagyja, hogy az automatizálás elvégezze)

### Mintapéldák fejlesztése

A Module08 Python mintákhoz (minták 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python mintákhoz:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron mintához (minta 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Mintapéldák tesztelése

A Python minták nem rendelkeznek automatizált tesztekkel, de futtatással ellenőrizhetők:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Az Electron mintának van tesztinfrastruktúrája:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Tesztelési utasítások

### Tartalom ellenőrzése

A tároló automatizált fordítási munkafolyamatokat használ. A fordítások manuális tesztelése nem szükséges.

**Manuális ellenőrzés tartalomváltozások esetén:**
1. Ellenőrizze a Markdown megjelenítést `.md` fájlok előnézetével
2. Győződjön meg róla, hogy minden hivatkozás érvényes célra mutat
3. Tesztelje a dokumentációban szereplő kódrészleteket
4. Ellenőrizze, hogy a képek helyesen töltődnek be

### Mintapéldák tesztelése

**Module08/minták/08 (Electron app) átfogó tesztelést tartalmaz:**
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

**Python minták manuálisan tesztelendők:**
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

## Kódstílus irányelvek

### Markdown tartalom

- Használjon következetes címsor hierarchiát (# a címhez, ## a fő szakaszokhoz, ### az alfejezetekhez)
- Tartalmazzon kódrészleteket nyelvi megjelöléssel: ```python, ```bash, ```javascript
- Kövesse a meglévő formázást táblázatok, listák és kiemelések esetén
- Tartsa olvasható sorokat (~80-100 karakter, de nem szigorú)
- Használjon relatív hivatkozásokat belső referenciákhoz

### Python kódstílus

- Kövesse a PEP 8 konvenciókat
- Használjon típusjelöléseket, ahol szükséges
- Tartalmazzon dokumentációs szövegeket a függvényekhez és osztályokhoz
- Használjon értelmes változóneveket
- Tartsa a függvényeket fókuszáltan és tömören

### JavaScript/Node.js kódstílus

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kulcskonvenciók:**
- ESLint konfiguráció a 08-as mintában
- Prettier a kódformázáshoz
- Használjon modern ES6+ szintaxist
- Kövesse a meglévő mintákat a kódbázisban

## Pull Request irányelvek

### Hozzájárulási munkafolyamat

1. **Forkolja a tárolót**, és hozzon létre egy új ágat a `main`-ből
2. **Végezze el a módosításokat** a kódstílus irányelvek szerint
3. **Tesztelje alaposan** a fent leírt tesztelési utasítások alapján
4. **Készítsen egyértelmű üzeneteket** a commitokhoz a konvencionális commit formátum szerint
5. **Pusholja a forkjára**, és hozzon létre egy pull requestet
6. **Válaszoljon a karbantartók visszajelzéseire** az áttekintés során

### Ágnevezési konvenció

- `feature/<modul>-<leírás>` - Új funkciók vagy tartalom esetén
- `fix/<modul>-<leírás>` - Hibajavításokhoz
- `docs/<leírás>` - Dokumentációs fejlesztésekhez
- `refactor/<leírás>` - Kód átalakításához

### Commit üzenet formátum

Kövesse a [Conventional Commits](https://www.conventionalcommits.org/) irányelveit:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Példák:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Cím formátum
```
[ModuleXX] Brief description of change
```
vagy
```
[Module08/samples/XX] Description for sample changes
```

### Magatartási kódex

Minden közreműködőnek követnie kell a [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) irányelveit. Kérjük, tekintse át a [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) fájlt mielőtt hozzájárulna.

### Beküldés előtt

**Tartalomváltozások esetén:**
- Tekintse meg az összes módosított Markdown fájlt
- Ellenőrizze, hogy a hivatkozások és képek működnek
- Ellenőrizze a helyesírási és nyelvtani hibákat

**Mintakód változások esetén (Module08/minták/08):**
```bash
npm run lint
npm test
```

**Python minták változásai esetén:**
- Tesztelje, hogy a minta sikeresen fut
- Ellenőrizze a hibakezelés működését
- Ellenőrizze a kompatibilitást a Foundry Local-lal

### Áttekintési folyamat

- Oktatási tartalom változásait pontosság és érthetőség szempontjából vizsgálják
- Kódmintákat funkcionalitás szempontjából tesztelik
- Fordítási frissítéseket automatikusan a GitHub Actions kezeli

## Fordítási rendszer

**FONTOS:** Ez a tároló automatizált fordítást használ a GitHub Actions segítségével.

- A fordítások a `/translations/` könyvtárban találhatók (50+ nyelv)
- Automatizált a `co-op-translator.yml` munkafolyamat által
- **NE szerkessze manuálisan a fordítási fájlokat** - felülíródnak
- Csak az angol forrásfájlokat szerkessze a gyökérben és a modul könyvtárakban
- A fordítások automatikusan generálódnak a `main` ágra történő push után

## Foundry Local integráció

A legtöbb Module08 minta a Microsoft Foundry Local futtatását igényli.

### Telepítés és beállítás

**Foundry Local telepítése:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK telepítése:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local indítása
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

### SDK használata (Python)
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

### Foundry Local ellenőrzése
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Környezeti változók mintákhoz

A legtöbb minta ezeket a környezeti változókat használja:
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

**Megjegyzés**: A `FoundryLocalManager` használatakor az SDK automatikusan kezeli a szolgáltatás felfedezését és a modell betöltését. Modell aliasok (például `phi-3.5-mini`) biztosítják, hogy a legjobb változat legyen kiválasztva a hardveréhez.

## Build és telepítés

### Tartalom telepítése

Ez a tároló elsősorban dokumentáció - nincs szükség build folyamatra a tartalomhoz.

### Mintapéldák építése

**Electron alkalmazás (Module08/minták/08):**
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

**Python minták:**
Nincs build folyamat - a minták közvetlenül a Python interpreterrel futtathatók.

## Gyakori problémák és hibaelhárítás

> **Tipp**: Nézze meg a [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) oldalt ismert problémák és megoldások miatt.

### Kritikus problémák (blokkoló)

#### Foundry Local nem fut
**Probléma:** Minták csatlakozási hibákkal meghiúsulnak

**Megoldás:**
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

### Gyakori problémák (mérsékelt)

#### Python virtuális környezet problémák
**Probléma:** Modul importálási hibák

**Megoldás:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron build problémák
**Probléma:** npm install vagy build hibák

**Megoldás:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Munkafolyamat problémák (kisebb)

#### Fordítási munkafolyamat konfliktusok
**Probléma:** Fordítás PR ütközik a változásaival

**Megoldás:**
- Csak az angol forrásfájlokat szerkessze
- Hagyja, hogy az automatizált fordítási munkafolyamat kezelje a fordításokat
- Ha konfliktusok lépnek fel, merge-ölje a `main`-t az ágába, miután a fordítások merge-ölve lettek

#### Modell letöltési hibák
**Probléma:** Foundry Local nem tudja letölteni a modelleket

**Megoldás:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## További források

### Tanulási útvonalak
- **Kezdő útvonal:** Modulok 01-02 (7-9 óra)
- **Középhaladó útvonal:** Modulok 03-04 (9-11 óra)
- **Haladó útvonal:** Modulok 05-07 (12-15 óra)
- **Szakértői útvonal:** Modul 08 (8-10 óra)
- **Gyakorlati workshop:** Workshop anyagok (6-8 óra)

### Kulcsmodul tartalom
- **Module01:** EdgeAI alapok és valós esettanulmányok
- **Module02:** Kis Nyelvi Modell (SLM) családok és architektúrák
- **Module03:** Helyi és felhő telepítési stratégiák
- **Module04:** Modell optimalizálás több keretrendszerrel (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - gyártási műveletek
- **Module06:** AI ügynökök és funkcióhívások
- **Module07:** Platform-specifikus megvalósítások
- **Module08:** Foundry Local eszközkészlet 10 átfogó mintával

### Külső függőségek
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Helyi AI modell futtatási környezet OpenAI-kompatibilis API-val
  - [Dokumentáció](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimalizációs keretrendszer
- [
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel integráció

### Workshop Mintapéldák

A workshop 6 egymásra épülő szekciót tartalmaz gyakorlati megvalósításokkal:

1. **01. szekció** - Chat indítása Foundry Local integrációval
2. **02. szekció** - RAG folyamat és értékelés RAGAS segítségével
3. **03. szekció** - Nyílt forráskódú modellek összehasonlítása
4. **04. szekció** - Modellek összehasonlítása és kiválasztása
5. **05. szekció** - Több ügynököt kezelő rendszerek
6. **06. szekció** - Modellirányítás és folyamatkezelés

Minden minta bemutatja az Edge AI fejlesztés különböző aspektusait Foundry Local segítségével.

### Teljesítmény Szempontok

- Az SLM-ek optimalizálva vannak Edge környezetben való használatra (2-16GB RAM)
- Helyi következtetés 50-500ms válaszidőt biztosít
- Kvantálási technikák 75%-os méretcsökkentést érnek el 85%-os teljesítménymegtartással
- Valós idejű beszélgetési képességek helyi modellekkel

### Biztonság és Adatvédelem

- Minden feldolgozás helyben történik - nincs adatküldés a felhőbe
- Alkalmas adatvédelmi szempontból érzékeny alkalmazásokhoz (egészségügy, pénzügy)
- Megfelel az adat-szuverenitási követelményeknek
- A Foundry Local teljes mértékben helyi hardveren fut

## Segítség Kérése

### Dokumentáció

- **Fő README**: [README.md](README.md) - A repozitórium áttekintése és tanulási útvonalak
- **Tanulmányi Útmutató**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Tanulási források és idővonal
- **Támogatás**: [SUPPORT.md](SUPPORT.md) - Hogyan kérj segítséget
- **Biztonság**: [SECURITY.md](SECURITY.md) - Biztonsági problémák jelentése

### Közösségi Támogatás

- **GitHub Issues**: [Hibák jelentése vagy funkciók kérése](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Kérdések feltevése és ötletek megosztása](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technikai problémák a Foundry Local kapcsán](https://github.com/microsoft/Foundry-Local/issues)

### Kapcsolat

- **Karbantartók**: Lásd [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Biztonsági Problémák**: Kövesd a felelős bejelentési eljárást a [SECURITY.md](SECURITY.md) dokumentumban
- **Microsoft Támogatás**: Vállalati támogatásért lépj kapcsolatba a Microsoft ügyfélszolgálatával

### További Források

- **Microsoft Learn**: [AI és Gépi Tanulás Tanulási Útvonalak](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentáció**: [Hivatalos Dokumentáció](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Közösségi Minták**: Nézd meg a [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) oldalt közösségi hozzájárulásokért

---

**Ez egy oktatási repozitórium, amely az Edge AI fejlesztés tanítására fókuszál. Az elsődleges hozzájárulási forma az oktatási tartalom fejlesztése és olyan mintapéldák hozzáadása vagy javítása, amelyek bemutatják az Edge AI koncepcióit.**

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.