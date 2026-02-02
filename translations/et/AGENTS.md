# AGENTS.md

> **Arendajate juhend EdgeAI algajatele**
> 
> See dokument pakub põhjalikku teavet arendajatele, AI agentidele ja kaastöötajatele, kes töötavad selle repositooriumiga. See hõlmab seadistamist, arendustöövooge, testimist ja parimaid praktikaid.
> 
> **Viimati uuendatud**: 30. oktoober 2025 | **Dokumendi versioon**: 3.0

## Sisukord

- [Projekti ülevaade](../..)
- [Repositooriumi struktuur](../..)
- [Eeltingimused](../..)
- [Seadistuskäsud](../..)
- [Arendustöövoog](../..)
- [Testimisjuhised](../..)
- [Koodistiili juhised](../..)
- [Pull Request'i juhised](../..)
- [Tõlkesüsteem](../..)
- [Foundry Local integratsioon](../..)
- [Ehitus ja juurutamine](../..)
- [Levinud probleemid ja tõrkeotsing](../..)
- [Täiendavad ressursid](../..)
- [Projektispetsiifilised märkused](../..)
- [Abi saamine](../..)

## Projekti ülevaade

EdgeAI algajatele on põhjalik hariduslik repositoorium, mis õpetab Edge AI arendust väikeste keelemudelitega (SLM). Kursus hõlmab EdgeAI põhialuseid, mudelite juurutamist, optimeerimistehnikaid ja tootmisvalmis rakendusi, kasutades Microsoft Foundry Local'i ja erinevaid AI raamistikke.

**Peamised tehnoloogiad:**
- Python 3.8+ (peamine keel AI/ML näidete jaoks)
- .NET C# (AI/ML näited)
- JavaScript/Node.js koos Electroniga (töölauarakenduste jaoks)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI raamistikud: LangChain, Semantic Kernel, Chainlit
- Mudeli optimeerimine: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repositooriumi tüüp:** Hariduslik sisurepositoorium 8 mooduli ja 10 põhjaliku näidisrakendusega

**Arhitektuur:** Mitme mooduliga õppeprogramm praktiliste näidetega, mis demonstreerivad Edge AI juurutusmustreid

## Repositooriumi struktuur

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

## Eeltingimused

### Vajalikud tööriistad

- **Python 3.8+** - AI/ML näidete ja märkmike jaoks
- **Node.js 16+** - Electroni näidisrakenduse jaoks
- **Git** - Versioonihalduseks
- **Microsoft Foundry Local** - AI mudelite lokaalseteks käitusteks

### Soovitatavad tööriistad

- **Visual Studio Code** - Python'i, Jupyter'i ja Pylance'i laiendustega
- **Windows Terminal** - Parema käsureakogemuse jaoks (Windowsi kasutajatele)
- **Docker** - Konteineripõhiseks arenduseks (valikuline)

### Süsteeminõuded

- **RAM**: Minimaalselt 8GB, soovitatavalt 16GB+ mitme mudeli stsenaariumide jaoks
- **Salvestusruum**: 10GB+ vaba ruumi mudelite ja sõltuvuste jaoks
- **OS**: Windows 10/11, macOS 11+ või Linux (Ubuntu 20.04+)
- **Riistvara**: CPU AVX2 toega; GPU (CUDA, Qualcomm NPU) valikuline, kuid soovitatav

### Teadmiste eeltingimused

- Põhiteadmised Python'i programmeerimisest
- Käsurealiideste tundmine
- AI/ML kontseptsioonide mõistmine (näidiste arendamiseks)
- Git'i töövood ja pull request'i protsessid

## Seadistuskäsud

### Repositooriumi seadistamine

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python'i näidiste seadistamine (Moodul08 ja töötoa näidised)

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

### Node.js näidiste seadistamine (Näidis 08 - Windowsi vestlusrakendus)

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

### Foundry Local'i seadistamine

Foundry Local on vajalik näidiste käitamiseks. Laadi alla ja installi ametlikust repositooriumist:

**Paigaldamine:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuaalne**: Laadi alla [väljalaske lehelt](https://github.com/microsoft/Foundry-Local/releases)

**Kiire alustamine:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Märkus**: Foundry Local valib automaatselt parima mudelivariandi teie riistvara jaoks (CUDA GPU, Qualcomm NPU või CPU).

## Arendustöövoog

### Sisu arendamine

See repositoorium sisaldab peamiselt **Markdown haridussisu**. Muudatuste tegemisel:

1. Redigeeri `.md` faile vastavates moodulite kataloogides
2. Järgi olemasolevaid vormindusmustreid
3. Veendu, et koodinäited on täpsed ja testitud
4. Uuenda vastavat tõlgitud sisu, kui vajalik (või lase automatiseerimisel seda teha)

### Näidisrakenduste arendamine

Moodul08 Python'i näidiste jaoks (näidised 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Töötoa Python'i näidiste jaoks:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electroni näidise jaoks (näidis 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Näidisrakenduste testimine

Python'i näidistel puuduvad automaatsed testid, kuid neid saab valideerida käivitamise teel:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electroni näidisel on testimistaristu:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testimisjuhised

### Sisu valideerimine

Repositoorium kasutab automaatseid tõlkeworkflow'sid. Tõlgete jaoks pole käsitsi testimist vaja.

**Käsitsi valideerimine sisu muudatuste korral:**
1. Vaata Markdown'i renderdamist `.md` failide eelvaates
2. Kontrolli, et kõik lingid viivad kehtivatele sihtkohtadele
3. Testi dokumentatsioonis sisalduvaid koodinäiteid
4. Veendu, et pildid laaditakse korrektselt

### Näidisrakenduste testimine

**Moodul08/näidised/08 (Electroni rakendus) sisaldab põhjalikku testimist:**
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

**Python'i näidised tuleks testida käsitsi:**
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

## Koodistiili juhised

### Markdown sisu

- Kasuta järjepidevat pealkirjade hierarhiat (# pealkirja jaoks, ## põhiosade jaoks, ### alajaotuste jaoks)
- Lisa koodiplokid keele määratlustega: ```python, ```bash, ```javascript
- Järgi olemasolevat vormindust tabelite, loendite ja rõhutuste jaoks
- Hoia read loetavad (umbes 80-100 tähemärki, kuid mitte rangelt)
- Kasuta sisemiste viidete jaoks suhtelisi linke

### Python'i koodistiil

- Järgi PEP 8 konventsioone
- Kasuta tüüpviiteid, kui sobilik
- Lisa funktsioonidele ja klassidele docstring'id
- Kasuta tähenduslikke muutujanimesid
- Hoia funktsioonid keskendunud ja lühikesed

### JavaScript/Node.js koodistiil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Peamised konventsioonid:**
- ESLint konfiguratsioon on näidises 08
- Prettier koodi vormindamiseks
- Kasuta kaasaegset ES6+ süntaksit
- Järgi olemasolevaid mustreid koodibaasis

## Pull Request'i juhised

### Kaastöövoog

1. **Fork'i repositoorium** ja loo uus haru `main` harust
2. **Tee oma muudatused**, järgides koodistiili juhiseid
3. **Testi põhjalikult**, kasutades ülaltoodud testimisjuhiseid
4. **Commit'i selgete sõnumitega**, järgides konventsionaalsete commit'ide formaati
5. **Push'i oma fork'i** ja loo pull request
6. **Vasta tagasisidele**, mida hooldajad ülevaatuse käigus annavad

### Haru nimetamise konventsioon

- `feature/<moodul>-<kirjeldus>` - Uute funktsioonide või sisu jaoks
- `fix/<moodul>-<kirjeldus>` - Vigade parandamiseks
- `docs/<kirjeldus>` - Dokumentatsiooni täiustamiseks
- `refactor/<kirjeldus>` - Koodi refaktoreerimiseks

### Commit'i sõnumi formaat

Järgi [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Näited:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Pealkirja formaat
```
[ModuleXX] Brief description of change
```
või
```
[Module08/samples/XX] Description for sample changes
```

### Käitumisjuhend

Kõik kaastöötajad peavad järgima [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Palun vaata üle [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) enne kaastööd.

### Enne esitamist

**Sisu muudatuste korral:**
- Vaata üle kõik muudetud Markdown failid
- Kontrolli linkide ja piltide toimimist
- Kontrolli kirjavigu ja grammatikat

**Näidiskoodi muudatuste korral (Moodul08/näidised/08):**
```bash
npm run lint
npm test
```

**Python'i näidiste muudatuste korral:**
- Testi, et näidis töötab edukalt
- Kontrolli veakäsitlust
- Veendu ühilduvuses Foundry Local'iga

### Ülevaatusprotsess

- Haridussisu muudatused vaadatakse üle täpsuse ja selguse osas
- Koodinäidised testitakse funktsionaalsuse osas
- Tõlkeuuendused hallatakse automaatselt GitHub Actions'i poolt

## Tõlkesüsteem

**TÄHTIS:** See repositoorium kasutab automaatset tõlget GitHub Actions'i kaudu.

- Tõlked asuvad `/translations/` kataloogis (50+ keelt)
- Automatiseeritud `co-op-translator.yml` töövoo kaudu
- **ÄRA muuda tõlkefaile käsitsi** - need kirjutatakse üle
- Muuda ainult ingliskeelseid algfaile juur- ja moodulikataloogides
- Tõlked genereeritakse automaatselt `main` harule push'imisel

## Foundry Local integratsioon

Enamik Moodul08 näidiseid nõuab Microsoft Foundry Local'i käitamist.

### Paigaldamine ja seadistamine

**Paigalda Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Paigalda Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local'i käivitamine
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

### SDK kasutamine (Python)
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

### Foundry Local'i valideerimine
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Keskkonnamuutujad näidiste jaoks

Enamik näidiseid kasutab järgmisi keskkonnamuutujaid:
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

**Märkus**: Kasutades `FoundryLocalManager'it`, haldab SDK automaatselt teenuste avastamist ja mudelite laadimist. Mudeli aliased (näiteks `phi-3.5-mini`) tagavad parima variandi valiku teie riistvara jaoks.

## Ehitus ja juurutamine

### Sisu juurutamine

See repositoorium on peamiselt dokumentatsioon - sisu jaoks pole ehitusprotsessi vaja.

### Näidisrakenduste ehitamine

**Electroni rakendus (Moodul08/näidised/08):**
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

**Python'i näidised:**
Ehitusprotsessi pole - näidised käivitatakse otse Python'i tõlgiga.

## Levinud probleemid ja tõrkeotsing

> **Näpunäide**: Vaata [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) teadaolevate probleemide ja lahenduste jaoks.

### Kriitilised probleemid (blokeerivad)

#### Foundry Local ei tööta
**Probleem:** Näidised ebaõnnestuvad ühenduse vigadega

**Lahendus:**
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

### Levinud probleemid (mõõdukad)

#### Python'i virtuaalse keskkonna probleemid
**Probleem:** Mooduli importimise vead

**Lahendus:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electroni ehitusprobleemid
**Probleem:** npm installimise või ehitamise vead

**Lahendus:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Töövoo probleemid (väikesed)

#### Tõlkeworkflow konfliktid
**Probleem:** Tõlke PR konfliktib teie muudatustega

**Lahendus:**
- Muuda ainult ingliskeelseid algfaile
- Lase automaatsel tõlkeworkflow'l tõlked hallata
- Kui konfliktid tekivad, ühenda `main` oma harusse pärast tõlgete ühendamist

#### Mudeli allalaadimise vead
**Probleem:** Foundry Local ei suuda mudeleid alla laadida

**Lahendus:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Täiendavad ressursid

### Õppeprogrammid
- **Algajate programm:** Moodulid 01-02 (7-9 tundi)
- **Kesktaseme programm:** Moodulid 03-04 (9-11 tundi)
- **Edasijõudnute programm:** Moodulid 05-07 (12-15 tundi)
- **Ekspertide programm:** Moodul 08 (8-10 tundi)
- **Praktiline töötuba:** Töötoa materjalid (6-8 tundi)

### Peamised mooduli sisud
- **Moodul01:** EdgeAI põhialused ja reaalsed juhtumiuuringud
- **Moodul02:** Väikeste keelemudelite (SLM) perekonnad ja arhitektuurid
- **Moodul03:** Kohalikud ja pilvepõhised juurutusstrateegiad
- **Moodul04:** Mudeli optimeerimine mitme raamistikuga (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Moodul05:** SLMOps - tootmisoperatsioonid
- **Moodul06:** AI agendid ja funktsioonide kutsumine
- **Moodul07:** Platvormispetsiifilised rakendused
- **Moodul08:** Foundry Local tööriistakomplekt 10 põhjaliku näidisega

### Välised sõltuvused
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Kohalik AI mudeli käitusaeg OpenAI-ühilduva API-ga
  - [Dokumentatsioon](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimeerimisraamistik
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Mudeli optimeerimise tööriistakomplekt
- [OpenVINO](https://docs.openvino.ai/) - Inteli optimeerimise tööriistakomplekt

## Projektispetsiifilised märkused

### Moodul08 näidisrakendused

Repositoorium sisaldab 10 põhjalikku näidisrakendust:

1. **01-REST vestluse kiirstart** - Põhiline OpenAI SDK integratsioon
2. **02-OpenAI SDK integratsioon** - Täiustatud SDK funktsioonid
3. **03-Mudelite avastamine ja võrdlemine** - Mudelite võrdlustööriistad
4. **04-Chainlit RAG rakendus** - Otsingupõhine generatsioon
5. **05-Multi-Agent orkestreerimine** - Põhiline agentide koordineerimine
6. **06-Mudelid-tööriistadena suunaja** - Nutikas mudelite suunamine
7. **07-Otsene API klient** - Madala taseme API integratsioon
8. **08-Windows 11 vestlusrakendus** - Kohalik Electroni töölauarakendus
9. **09-Täiustatud Multi-Agent süsteem** - Kompleksne agentide orkestreerimine
10. **10-Valukoja Tööriistade Raamistik** - LangChain/Semantic Kernel integratsioon

### Töötuba Näidisrakendused

Töötuba sisaldab 6 järjestikust sessiooni praktiliste rakendustega:

1. **Sessioon 01** - Vestluse käivitamine koos Foundry Local integratsiooniga
2. **Sessioon 02** - RAG torujuhtme ja hindamine RAGAS-iga
3. **Sessioon 03** - Avatud lähtekoodiga mudelite võrdlus
4. **Sessioon 04** - Mudelite võrdlemine ja valik
5. **Sessioon 05** - Mitme agendi orkestreerimissüsteemid
6. **Sessioon 06** - Mudelite suunamine ja torujuhtme haldamine

Iga näidis illustreerib erinevaid aspekte serva AI arenduses koos Foundry Localiga.

### Jõudluse kaalutlused

- SLM-id on optimeeritud serva kasutuselevõtuks (2-16GB RAM)
- Kohalik järeldamine tagab 50-500ms vastuse ajad
- Kvantiseerimistehnikad saavutavad 75% suuruse vähendamise 85% jõudluse säilitamisega
- Reaalajas vestlusvõimalused kohalike mudelitega

### Turvalisus ja privaatsus

- Kogu töötlemine toimub kohapeal - andmeid ei saadeta pilve
- Sobib privaatsustundlikele rakendustele (tervishoid, rahandus)
- Vastab andmesuveräänsuse nõuetele
- Foundry Local töötab täielikult kohalikul riistvaral

## Abi saamine

### Dokumentatsioon

- **Peamine README**: [README.md](README.md) - Repositooriumi ülevaade ja õppejuhised
- **Õppejuhend**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Õpperessursid ja ajakava
- **Tugi**: [SUPPORT.md](SUPPORT.md) - Kuidas abi saada
- **Turvalisus**: [SECURITY.md](SECURITY.md) - Turvalisuse probleemide raporteerimine

### Kogukonna tugi

- **GitHub Issues**: [Teata vigadest või taotle funktsioone](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Esita küsimusi ja jaga ideid](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Tehnilised probleemid Foundry Localiga](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Hooldajad**: Vaata [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Turvalisuse probleemid**: Järgi vastutustundlikku avalikustamist [SECURITY.md](SECURITY.md)
- **Microsofti tugi**: Ettevõtte toe jaoks võtke ühendust Microsofti klienditeenindusega

### Täiendavad ressursid

- **Microsoft Learn**: [AI ja masinõppe õpperajad](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentatsioon**: [Ametlikud dokumendid](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Kogukonna näidised**: Vaata [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) kogukonna panuste jaoks

---

**See on hariduslik repositoorium, mis keskendub serva AI arenduse õpetamisele. Peamine panustamise muster on haridusliku sisu täiustamine ja näidisrakenduste lisamine/parendamine, mis illustreerivad serva AI kontseptsioone.**

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.