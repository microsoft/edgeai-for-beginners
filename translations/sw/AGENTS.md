<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:54:55+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sw"
}
-->
# AGENTS.md

> **Mwongozo wa Mwandishi kwa Kuchangia EdgeAI kwa Anzishi**
> 
> Hati hii inatoa maelezo ya kina kwa waendelezaji, mawakala wa AI, na wachangiaji wanaofanya kazi na hifadhi hii. Inashughulikia usanidi, mtiririko wa maendeleo, majaribio, na mbinu bora.
> 
> **Ilisasishwa Mwisho**: Oktoba 30, 2025 | **Toleo la Hati**: 3.0

## Jedwali la Yaliyomo

- [Muhtasari wa Mradi](../..)
- [Muundo wa Hifadhi](../..)
- [Mahitaji ya Awali](../..)
- [Amri za Usanidi](../..)
- [Mtiririko wa Maendeleo](../..)
- [Maelekezo ya Majaribio](../..)
- [Miongozo ya Mtindo wa Nambari](../..)
- [Miongozo ya Ombi la Kuvuta](../..)
- [Mfumo wa Tafsiri](../..)
- [Ujumuishaji wa Foundry Local](../..)
- [Ujenzi na Uwekaji](../..)
- [Masuala ya Kawaida na Utatuzi](../..)
- [Rasilimali za Ziada](../..)
- [Vidokezo Maalum vya Mradi](../..)
- [Kupata Msaada](../..)

## Muhtasari wa Mradi

EdgeAI kwa Anzishi ni hifadhi ya elimu ya kina inayofundisha maendeleo ya Edge AI kwa kutumia Small Language Models (SLMs). Kozi inashughulikia misingi ya EdgeAI, uwekaji wa modeli, mbinu za uboreshaji, na utekelezaji tayari kwa uzalishaji kwa kutumia Microsoft Foundry Local na mifumo mbalimbali ya AI.

**Teknolojia Muhimu:**
- Python 3.8+ (lugha kuu kwa sampuli za AI/ML)
- .NET C# (Sampuli za AI/ML)
- JavaScript/Node.js na Electron (kwa programu za desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Mifumo ya AI: LangChain, Semantic Kernel, Chainlit
- Uboreshaji wa Modeli: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Aina ya Hifadhi:** Hifadhi ya maudhui ya elimu yenye moduli 8 na programu 10 za sampuli za kina

**Muundo:** Njia ya kujifunza yenye moduli nyingi na sampuli za vitendo zinazoonyesha mifumo ya uwekaji wa Edge AI

## Muundo wa Hifadhi

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

## Mahitaji ya Awali

### Zana Zinazohitajika

- **Python 3.8+** - Kwa sampuli za AI/ML na daftari
- **Node.js 16+** - Kwa programu ya sampuli ya Electron
- **Git** - Kwa udhibiti wa toleo
- **Microsoft Foundry Local** - Kwa kuendesha modeli za AI kwa ndani

### Zana Zinazopendekezwa

- **Visual Studio Code** - Na viendelezi vya Python, Jupyter, na Pylance
- **Windows Terminal** - Kwa uzoefu bora wa mstari wa amri (watumiaji wa Windows)
- **Docker** - Kwa maendeleo ya kontena (hiari)

### Mahitaji ya Mfumo

- **RAM**: Angalau 8GB, 16GB+ inapendekezwa kwa hali za modeli nyingi
- **Hifadhi**: Angalau 10GB nafasi ya bure kwa modeli na utegemezi
- **OS**: Windows 10/11, macOS 11+, au Linux (Ubuntu 20.04+)
- **Vifaa**: CPU yenye msaada wa AVX2; GPU (CUDA, Qualcomm NPU) hiari lakini inapendekezwa

### Maarifa ya Awali

- Uelewa wa msingi wa programu ya Python
- Uzoefu na interface za mstari wa amri
- Uelewa wa dhana za AI/ML (kwa maendeleo ya sampuli)
- Mtiririko wa Git na michakato ya ombi la kuvuta

## Amri za Usanidi

### Usanidi wa Hifadhi

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Usanidi wa Sampuli za Python (Moduli08 na sampuli za Warsha)

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

### Usanidi wa Sampuli za Node.js (Sampuli 08 - Windows Chat App)

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

### Usanidi wa Foundry Local

Foundry Local inahitajika kuendesha sampuli. Pakua na usakinishe kutoka hifadhi rasmi:

**Usakinishaji:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Mwongozo**: Pakua kutoka [ukurasa wa matoleo](https://github.com/microsoft/Foundry-Local/releases)

**Kuanza Haraka:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Kumbuka**: Foundry Local huchagua kiotomatiki toleo bora la modeli kwa vifaa vyako (CUDA GPU, Qualcomm NPU, au CPU).

## Mtiririko wa Maendeleo

### Maendeleo ya Maudhui

Hifadhi hii ina maudhui ya elimu ya **Markdown**. Unapofanya mabadiliko:

1. Hariri faili za `.md` katika saraka za moduli zinazofaa
2. Fuata mifumo ya muundo iliyopo
3. Hakikisha mifano ya nambari ni sahihi na imejaribiwa
4. Sasisha maudhui yaliyotafsiriwa yanayolingana ikiwa ni lazima (au acha otomatiki ishughulikie)

### Maendeleo ya Programu ya Sampuli

Kwa sampuli za Python za Moduli08 (sampuli 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Kwa sampuli za Warsha za Python:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Kwa sampuli ya Electron (sampuli 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Majaribio ya Programu za Sampuli

Sampuli za Python hazina majaribio ya kiotomatiki lakini zinaweza kuthibitishwa kwa kuziendesha:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Sampuli ya Electron ina miundombinu ya majaribio:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Maelekezo ya Majaribio

### Uthibitishaji wa Maudhui

Hifadhi hutumia mtiririko wa tafsiri otomatiki. Hakuna majaribio ya mwongozo yanayohitajika kwa tafsiri.

**Uthibitishaji wa mwongozo kwa mabadiliko ya maudhui:**
1. Hakiki utoaji wa Markdown kwa kutazama faili za `.md`
2. Hakikisha viungo vyote vinaelekeza kwa malengo halali
3. Jaribu vipande vyovyote vya nambari vilivyojumuishwa katika nyaraka
4. Angalia kwamba picha zinapakia vizuri

### Majaribio ya Programu za Sampuli

**Moduli08/sampuli/08 (programu ya Electron) ina majaribio ya kina:**
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

**Sampuli za Python zinapaswa kujaribiwa kwa mwongozo:**
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

## Miongozo ya Mtindo wa Nambari

### Maudhui ya Markdown

- Tumia uhierakia thabiti ya vichwa (# kwa kichwa, ## kwa sehemu kuu, ### kwa sehemu ndogo)
- Jumuisha vizuizi vya nambari na viainishi vya lugha: ```python, ```bash, ```javascript
- Fuata muundo uliopo kwa meza, orodha, na msisitizo
- Weka mistari isomeke (lenga ~80-100 herufi, lakini si kali)
- Tumia viungo vya jamaa kwa marejeleo ya ndani

### Mtindo wa Nambari ya Python

- Fuata kanuni za PEP 8
- Tumia vidokezo vya aina inapofaa
- Jumuisha maelezo ya kazi na madarasa
- Tumia majina ya kutambulika ya mabadiliko
- Weka kazi zikiwa na lengo na fupi

### Mtindo wa Nambari ya JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kanuni Muhimu:**
- Usanidi wa ESLint umetolewa katika sampuli 08
- Prettier kwa muundo wa nambari
- Tumia sintaksia ya kisasa ya ES6+
- Fuata mifumo iliyopo katika hifadhidata

## Miongozo ya Ombi la Kuvuta

### Mtiririko wa Mchango

1. **Fanya fork ya hifadhi** na unda tawi jipya kutoka `main`
2. **Fanya mabadiliko yako** ukifuata miongozo ya mtindo wa nambari
3. **Jaribu kwa kina** ukitumia maelekezo ya majaribio hapo juu
4. **Fanya ahadi na ujumbe wazi** ukifuata muundo wa ahadi za kawaida
5. **Sukuma kwa fork yako** na unda ombi la kuvuta
6. **Jibu maoni** kutoka kwa wasimamizi wakati wa ukaguzi

### Muundo wa Majina ya Tawi

- `feature/<moduli>-<maelezo>` - Kwa vipengele vipya au maudhui
- `fix/<moduli>-<maelezo>` - Kwa marekebisho ya hitilafu
- `docs/<maelezo>` - Kwa maboresho ya nyaraka
- `refactor/<maelezo>` - Kwa urekebishaji wa nambari

### Muundo wa Ujumbe wa Ahadi

Fuata [Ahadi za Kawaida](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Mifano:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Muundo wa Kichwa
```
[ModuleXX] Brief description of change
```
au
```
[Module08/samples/XX] Description for sample changes
```

### Kanuni za Maadili

Wachangiaji wote lazima wafuate [Kanuni za Maadili za Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Tafadhali hakiki [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) kabla ya kuchangia.

### Kabla ya Kuwasilisha

**Kwa mabadiliko ya maudhui:**
- Hakiki faili zote za Markdown zilizorekebishwa
- Hakikisha viungo na picha zinafanya kazi
- Angalia makosa ya tahajia na sarufi

**Kwa mabadiliko ya nambari ya sampuli (Moduli08/sampuli/08):**
```bash
npm run lint
npm test
```

**Kwa mabadiliko ya sampuli za Python:**
- Jaribu sampuli inaendesha kwa mafanikio
- Hakikisha utunzaji wa hitilafu unafanya kazi
- Angalia utangamano na Foundry Local

### Mchakato wa Ukaguzi

- Mabadiliko ya maudhui ya elimu yanakaguliwa kwa usahihi na uwazi
- Sampuli za nambari zinajaribiwa kwa utendaji
- Sasisho za tafsiri zinashughulikiwa kiotomatiki na GitHub Actions

## Mfumo wa Tafsiri

**MUHIMU:** Hifadhi hii hutumia tafsiri otomatiki kupitia GitHub Actions.

- Tafsiri ziko katika saraka ya `/translations/` (lugha 50+)
- Otomatiki kupitia mtiririko wa `co-op-translator.yml`
- **USIHARIRI faili za tafsiri kwa mkono** - zitafutwa
- Hariri faili za chanzo za Kiingereza pekee katika saraka kuu na moduli
- Tafsiri zinazalishwa kiotomatiki wakati wa kusukuma kwa tawi la `main`

## Ujumuishaji wa Foundry Local

Sampuli nyingi za Moduli08 zinahitaji Microsoft Foundry Local kuendesha.

### Usakinishaji & Usanidi

**Sakinisha Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Sakinisha Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Kuanza Foundry Local
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

### Matumizi ya SDK (Python)
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

### Uthibitishaji wa Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Mabadiliko ya Mazingira kwa Sampuli

Sampuli nyingi hutumia mabadiliko haya ya mazingira:
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

**Kumbuka**: Unapotumia `FoundryLocalManager`, SDK hushughulikia kiotomatiki ugunduzi wa huduma na upakiaji wa modeli. Majina ya modeli (kama `phi-3.5-mini`) huhakikisha toleo bora linachaguliwa kwa vifaa vyako.

## Ujenzi na Uwekaji

### Uwekaji wa Maudhui

Hifadhi hii ni nyaraka hasa - hakuna mchakato wa ujenzi unaohitajika kwa maudhui.

### Ujenzi wa Programu za Sampuli

**Programu ya Electron (Moduli08/sampuli/08):**
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

**Sampuli za Python:**
Hakuna mchakato wa ujenzi - sampuli zinaendeshwa moja kwa moja na tafsiri ya Python.

## Masuala ya Kawaida na Utatuzi

> **Kidokezo**: Angalia [Masuala ya GitHub](https://github.com/microsoft/edgeai-for-beginners/issues) kwa matatizo yanayojulikana na suluhisho.

### Masuala Muhimu (Yanayozuia)

#### Foundry Local Haifanyi Kazi
**Tatizo:** Sampuli zinashindwa na hitilafu za muunganisho

**Suluhisho:**
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

### Masuala ya Kawaida (Ya Kati)

#### Masuala ya Mazingira ya Virtual ya Python
**Tatizo:** Hitilafu za uingizaji wa moduli

**Suluhisho:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Masuala ya Ujenzi wa Electron
**Tatizo:** Hitilafu za `npm install` au ujenzi

**Suluhisho:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Masuala ya Mtiririko (Madogo)

#### Migogoro ya Mtiririko wa Tafsiri
**Tatizo:** Migogoro ya PR ya tafsiri na mabadiliko yako

**Suluhisho:**
- Hariri faili za chanzo za Kiingereza pekee
- Acha mtiririko wa tafsiri otomatiki ushughulikie tafsiri
- Ikiwa migogoro itatokea, unganisha `main` kwenye tawi lako baada ya tafsiri kuunganishwa

#### Hitilafu za Upakuaji wa Modeli
**Tatizo:** Foundry Local inashindwa kupakua modeli

**Suluhisho:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Rasilimali za Ziada

### Njia za Kujifunza
- **Njia ya Anzishi:** Moduli 01-02 (saa 7-9)
- **Njia ya Kati:** Moduli 03-04 (saa 9-11)
- **Njia ya Juu:** Moduli 05-07 (saa 12-15)
- **Njia ya Mtaalamu:** Moduli 08 (saa 8-10)
- **Warsha ya Vitendo:** Vifaa vya warsha (saa 6-8)

### Maudhui Muhimu ya Moduli
- **Moduli01:** Misingi ya EdgeAI na masomo ya hali halisi
- **Moduli02:** Familia za Small Language Model (SLM) na miundo
- **Moduli03:** Mikakati ya uwekaji wa ndani na wingu
- **Moduli04:** Uboreshaji wa modeli na mifumo mbalimbali (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Moduli05:** SLMOps - operesheni za uzalishaji
- **Moduli06:** Mawakala wa AI na kupiga kazi
- **Moduli07:** Utekelezaji maalum wa jukwaa
- **Moduli08:** Zana ya Foundry Local na sampuli 10 za kina

### Utegemezi wa Nje
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Muda wa modeli ya AI ya ndani na API inayolingana na OpenAI
  - [Nyaraka](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Mfumo wa uboreshaji
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Zana ya uboreshaji wa modeli
- [OpenVINO](https://docs.openvino.ai/) - Zana ya uboreshaji ya Intel

## Vidokezo Maalum vya Mradi

### Programu za Sampuli za Moduli08

Hifadhi inajumuisha programu 10 za sampuli za kina:

1. **01-REST Chat Quickstart** - Ujumuishaji wa msingi wa OpenAI SDK
2. **02-OpenAI SDK Integration** - Vipengele vya SDK vya hali ya juu
3. **03-Model Discovery & Benchmarking** - Zana za kulinganisha modeli
4. **04-Chainlit RAG Application** - Uzalishaji unaosaidiwa na urejeshaji
5. **05-Multi-Agent Orchestration** - Uratibu wa wakala wa msingi
6. **06-Models-as-Tools Router** - Usambazaji wa modeli wenye
10. **10-Mfumo wa Zana za Foundry** - Muunganiko wa LangChain/Semantic Kernel

### Programu za Mfano za Warsha

Warsha inajumuisha vipindi 6 vya maendeleo na utekelezaji wa vitendo:

1. **Kipindi 01** - Kuanza mazungumzo kwa muunganiko wa Foundry Local
2. **Kipindi 02** - Njia ya RAG na tathmini kwa kutumia RAGAS
3. **Kipindi 03** - Kulinganisha mifano ya chanzo huria
4. **Kipindi 04** - Kulinganisha na kuchagua mifano
5. **Kipindi 05** - Mfumo wa uratibu wa mawakala wengi
6. **Kipindi 06** - Usimamizi wa njia za mifano na bomba

Kila mfano unaonyesha vipengele tofauti vya maendeleo ya AI ya ukingo kwa kutumia Foundry Local.

### Mazingatio ya Utendaji

- SLMs zimeboreshwa kwa ajili ya matumizi ya ukingo (RAM ya 2-16GB)
- Utoaji wa matokeo wa ndani hutoa nyakati za majibu za 50-500ms
- Mbinu za kupunguza ukubwa zinapunguza ukubwa kwa 75% huku zikihifadhi utendaji wa 85%
- Uwezo wa mazungumzo ya papo hapo kwa kutumia mifano ya ndani

### Usalama na Faragha

- Usindikaji wote unafanyika ndani - hakuna data inayotumwa kwa wingu
- Inafaa kwa programu zinazohitaji faragha (afya, fedha)
- Inakidhi mahitaji ya uhuru wa data
- Foundry Local inafanya kazi kikamilifu kwenye vifaa vya ndani

## Kupata Msaada

### Nyaraka

- **README Kuu**: [README.md](README.md) - Muhtasari wa hifadhi na njia za kujifunza
- **Mwongozo wa Kujifunza**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Rasilimali za kujifunza na ratiba
- **Msaada**: [SUPPORT.md](SUPPORT.md) - Jinsi ya kupata msaada
- **Usalama**: [SECURITY.md](SECURITY.md) - Kuripoti masuala ya usalama

### Msaada wa Jamii

- **Masuala ya GitHub**: [Ripoti hitilafu au omba vipengele](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Majadiliano ya GitHub**: [Uliza maswali na shiriki mawazo](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Masuala ya Foundry Local**: [Masuala ya kiufundi na Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Mawasiliano

- **Wadumishaji**: Tazama [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Masuala ya Usalama**: Fuata ufichuzi wa uwajibikaji katika [SECURITY.md](SECURITY.md)
- **Msaada wa Microsoft**: Kwa msaada wa kibiashara, wasiliana na huduma kwa wateja wa Microsoft

### Rasilimali za Ziada

- **Microsoft Learn**: [Njia za Kujifunza AI na Kujifunza kwa Mashine](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Nyaraka za Foundry Local**: [Nyaraka Rasmi](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Mifano ya Jamii**: Angalia [Majadiliano ya GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) kwa michango ya jamii

---

**Hii ni hifadhi ya kielimu inayolenga kufundisha maendeleo ya AI ya ukingo. Muundo mkuu wa mchango ni kuboresha maudhui ya kielimu na kuongeza/kuboresha programu za mfano zinazoonyesha dhana za AI ya ukingo.**

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.