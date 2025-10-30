<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T13:15:25+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fi"
}
-->
# AGENTS.md

> **Kehittäjän opas EdgeAI for Beginners -projektiin osallistumiseksi**
> 
> Tämä dokumentti tarjoaa kattavaa tietoa kehittäjille, AI-agenteille ja kontribuoijille, jotka työskentelevät tämän repositorion parissa. Se kattaa asennuksen, kehitystyönkulut, testauksen ja parhaat käytännöt.
> 
> **Viimeksi päivitetty**: 30. lokakuuta 2025 | **Dokumentin versio**: 3.0

## Sisällysluettelo

- [Projektin yleiskatsaus](../..)
- [Repositorion rakenne](../..)
- [Edellytykset](../..)
- [Asennuskomennot](../..)
- [Kehitystyönkulku](../..)
- [Testausohjeet](../..)
- [Koodityylin ohjeet](../..)
- [Pull Request -ohjeet](../..)
- [Käännösjärjestelmä](../..)
- [Foundry Local -integraatio](../..)
- [Rakennus ja käyttöönotto](../..)
- [Yleiset ongelmat ja vianetsintä](../..)
- [Lisäresurssit](../..)
- [Projektikohtaiset huomiot](../..)
- [Apua saaminen](../..)

## Projektin yleiskatsaus

EdgeAI for Beginners on kattava opetusrepositorio, joka opettaa Edge AI -kehitystä pienillä kielimalleilla (SLM). Kurssi kattaa EdgeAI:n perusteet, mallien käyttöönoton, optimointitekniikat ja tuotantovalmiit toteutukset Microsoft Foundry Localin ja eri AI-kehysten avulla.

**Keskeiset teknologiat:**
- Python 3.8+ (pääasiallinen kieli AI/ML-esimerkeille)
- .NET C# (AI/ML-esimerkit)
- JavaScript/Node.js Electronin kanssa (työpöytäsovelluksille)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI-kehykset: LangChain, Semantic Kernel, Chainlit
- Mallien optimointi: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repositorion tyyppi:** Opetussisältöä sisältävä repositorio, jossa on 8 moduulia ja 10 kattavaa esimerkkisovellusta

**Arkkitehtuuri:** Monimoduulinen oppimispolku, jossa käytännön esimerkkejä Edge AI -käyttöönoton malleista

## Repositorion rakenne

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

## Edellytykset

### Tarvittavat työkalut

- **Python 3.8+** - AI/ML-esimerkeille ja muistikirjoille
- **Node.js 16+** - Electron-esimerkkisovellukselle
- **Git** - Versionhallintaan
- **Microsoft Foundry Local** - AI-mallien paikalliseen suorittamiseen

### Suositellut työkalut

- **Visual Studio Code** - Python-, Jupyter- ja Pylance-laajennuksilla
- **Windows Terminal** - Parempaan komentorivikokemukseen (Windows-käyttäjille)
- **Docker** - Konttipohjaiseen kehitykseen (valinnainen)

### Järjestelmävaatimukset

- **RAM**: Vähintään 8GB, suositeltu 16GB+ monimallitilanteisiin
- **Tallennustila**: Vähintään 10GB vapaata tilaa malleille ja riippuvuuksille
- **Käyttöjärjestelmä**: Windows 10/11, macOS 11+ tai Linux (Ubuntu 20.04+)
- **Laitteisto**: CPU, jossa AVX2-tuki; GPU (CUDA, Qualcomm NPU) valinnainen mutta suositeltu

### Tietämyksen edellytykset

- Python-ohjelmoinnin perusteiden ymmärtäminen
- Komentorivikäyttöliittymien tuntemus
- AI/ML-konseptien ymmärtäminen (esimerkkien kehittämiseen)
- Git-työnkulut ja pull request -prosessit

## Asennuskomennot

### Repositorion asennus

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-esimerkkien asennus (Moduuli08 ja Workshop-esimerkit)

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

### Node.js-esimerkin asennus (Esimerkki 08 - Windows Chat App)

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

### Foundry Local -asennus

Foundry Local vaaditaan esimerkkien suorittamiseen. Lataa ja asenna virallisesta repositoriosta:

**Asennus:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuaalinen**: Lataa [julkaisusivulta](https://github.com/microsoft/Foundry-Local/releases)

**Pika-aloitus:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Huom:** Foundry Local valitsee automaattisesti parhaan mallivaihtoehdon laitteistosi mukaan (CUDA GPU, Qualcomm NPU tai CPU).

## Kehitystyönkulku

### Sisällön kehittäminen

Tämä repositorio sisältää pääasiassa **Markdown-opetussisältöä**. Muutoksia tehdessä:

1. Muokkaa `.md`-tiedostoja oikeissa moduulikansioissa
2. Noudata olemassa olevia muotoilumalleja
3. Varmista, että koodiesimerkit ovat tarkkoja ja testattuja
4. Päivitä vastaava käännetty sisältö tarvittaessa (tai anna automaation hoitaa se)

### Esimerkkisovellusten kehittäminen

Moduuli08 Python-esimerkeille (esimerkit 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Workshop Python-esimerkeille:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron-esimerkille (esimerkki 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Esimerkkisovellusten testaus

Python-esimerkeillä ei ole automatisoituja testejä, mutta ne voidaan validoida suorittamalla:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron-esimerkissä on testausinfrastruktuuri:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testausohjeet

### Sisällön validointi

Repositoriossa käytetään automatisoituja käännöstyönkulkuja. Käännösten manuaalista testausta ei tarvita.

**Manuaalinen validointi sisällön muutoksille:**
1. Esikatsele Markdown-tiedostojen renderöintiä
2. Varmista, että kaikki linkit osoittavat oikeisiin kohteisiin
3. Testaa dokumentaatiossa olevat koodiesimerkit
4. Tarkista, että kuvat latautuvat oikein

### Esimerkkisovellusten testaus

**Moduuli08/esimerkit/08 (Electron-sovellus) sisältää kattavan testauksen:**
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

**Python-esimerkit tulee testata manuaalisesti:**
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

## Koodityylin ohjeet

### Markdown-sisältö

- Käytä johdonmukaista otsikkohierarkiaa (# otsikolle, ## pääosioille, ### aliosioille)
- Sisällytä koodilohkot kielimäärityksillä: ```python, ```bash, ```javascript
- Noudata olemassa olevaa muotoilua taulukoille, listoille ja korostuksille
- Pidä rivit luettavina (pyri ~80-100 merkkiin, mutta ei tiukasti)
- Käytä suhteellisia linkkejä sisäisiin viittauksiin

### Python-koodityyli

- Noudata PEP 8 -konventioita
- Käytä tyyppivihjeitä, kun se on tarkoituksenmukaista
- Sisällytä docstringit funktioille ja luokille
- Käytä merkityksellisiä muuttujanimiä
- Pidä funktiot keskittyneinä ja tiiviinä

### JavaScript/Node.js-koodityyli

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Keskeiset konventiot:**
- ESLint-konfiguraatio mukana esimerkissä 08
- Prettier koodin muotoiluun
- Käytä modernia ES6+ syntaksia
- Noudata olemassa olevia malleja koodikannassa

## Pull Request -ohjeet

### Kontribuution työnkulku

1. **Forkkaa repositorio** ja luo uusi haara `main`-haarasta
2. **Tee muutoksesi** noudattaen koodityylin ohjeita
3. **Testaa huolellisesti** käyttäen yllä olevia testausohjeita
4. **Commitoi selkeillä viesteillä** noudattaen konventionaalista commit-muotoa
5. **Pushaa forkkiisi** ja luo pull request
6. **Vastaa palautteeseen** ylläpitäjiltä tarkistuksen aikana

### Haaran nimeämiskonventio

- `feature/<moduuli>-<kuvaus>` - Uusille ominaisuuksille tai sisällölle
- `fix/<moduuli>-<kuvaus>` - Virheenkorjauksille
- `docs/<kuvaus>` - Dokumentaation parannuksille
- `refactor/<kuvaus>` - Koodin refaktoroinnille

### Commit-viestin muoto

Noudata [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Esimerkkejä:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Otsikon muoto
```
[ModuleXX] Brief description of change
```
tai
```
[Module08/samples/XX] Description for sample changes
```

### Käytösohjeet

Kaikkien kontribuoijien tulee noudattaa [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Tutustu [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) ennen kontribuointia.

### Ennen lähettämistä

**Sisällön muutoksille:**
- Esikatsele kaikki muokatut Markdown-tiedostot
- Varmista, että linkit ja kuvat toimivat
- Tarkista kirjoitusvirheet ja kielioppivirheet

**Esimerkkikoodin muutoksille (Moduuli08/esimerkit/08):**
```bash
npm run lint
npm test
```

**Python-esimerkkien muutoksille:**
- Testaa, että esimerkki toimii onnistuneesti
- Varmista virheenkäsittelyn toimivuus
- Tarkista yhteensopivuus Foundry Localin kanssa

### Tarkistusprosessi

- Opetussisällön muutokset tarkistetaan tarkkuuden ja selkeyden osalta
- Koodiesimerkit testataan toimivuuden osalta
- Käännöspäivitykset hoidetaan automaattisesti GitHub Actionsin avulla

## Käännösjärjestelmä

**TÄRKEÄÄ:** Tämä repositorio käyttää automatisoitua käännöstä GitHub Actionsin kautta.

- Käännökset sijaitsevat `/translations/`-hakemistossa (yli 50 kieltä)
- Automatisoitu `co-op-translator.yml`-työnkulun avulla
- **ÄLÄ muokkaa käännöstiedostoja manuaalisesti** - ne ylikirjoitetaan
- Muokkaa vain englanninkielisiä lähdetiedostoja juurihakemistossa ja moduulikansioissa
- Käännökset generoidaan automaattisesti, kun `main`-haaraan tehdään push

## Foundry Local -integraatio

Useimmat Moduuli08-esimerkit vaativat Microsoft Foundry Localin käynnissä.

### Asennus ja käyttöönotto

**Asenna Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Asenna Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Localin käynnistäminen
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

### SDK:n käyttö (Python)
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

### Foundry Localin validointi
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Ympäristömuuttujat esimerkeille

Useimmat esimerkit käyttävät näitä ympäristömuuttujia:
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

**Huom:** Kun käytetään `FoundryLocalManageria`, SDK hoitaa automaattisesti palvelun löytämisen ja mallien lataamisen. Mallialiaset (kuten `phi-3.5-mini`) varmistavat parhaan vaihtoehdon valinnan laitteistollesi.

## Rakennus ja käyttöönotto

### Sisällön käyttöönotto

Tämä repositorio on pääasiassa dokumentaatiota - sisällölle ei vaadita rakennusprosessia.

### Esimerkkisovellusten rakentaminen

**Electron-sovellus (Moduuli08/esimerkit/08):**
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

**Python-esimerkit:**
Ei rakennusprosessia - esimerkit suoritetaan suoraan Python-tulkilla.

## Yleiset ongelmat ja vianetsintä

> **Vinkki**: Tarkista [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) tunnettuja ongelmia ja ratkaisuja varten.

### Kriittiset ongelmat (Estävät)

#### Foundry Local ei käynnissä
**Ongelma:** Esimerkit epäonnistuvat yhteysvirheillä

**Ratkaisu:**
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

### Yleiset ongelmat (Kohtalaiset)

#### Python-virtuaaliympäristön ongelmat
**Ongelma:** Moduulin tuontivirheet

**Ratkaisu:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron-rakennusongelmat
**Ongelma:** npm install tai rakennusvirheet

**Ratkaisu:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Työnkulkuongelmat (Pienet)

#### Käännöstyönkulun konfliktit
**Ongelma:** Käännös-PR on ristiriidassa muutostesi kanssa

**Ratkaisu:**
- Muokkaa vain englanninkielisiä lähdetiedostoja
- Anna automatisoidun käännöstyönkulun hoitaa käännökset
- Jos konflikteja ilmenee, yhdistä `main` haarasi jälkeen, kun käännökset on yhdistetty

#### Mallin latausvirheet
**Ongelma:** Foundry Local epäonnistuu mallien lataamisessa

**Ratkaisu:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Lisäresurssit

### Oppimispolut
- **Aloittelijapolku:** Moduulit 01-02 (7-9 tuntia)
- **Keskitaso:** Moduulit 03-04 (9-11 tuntia)
- **Edistynyt polku:** Moduulit 05-07 (12-15 tuntia)
- **Asiantuntijapolku:** Moduuli 08 (8-10 tuntia)
- **Käytännön workshop:** Workshop-materiaalit (6-8 tuntia)

### Keskeinen moduulisisältö
- **Moduuli01:** EdgeAI:n perusteet ja tosielämän tapaustutkimukset
- **Moduuli02:** Pienten kielimallien (SLM) perheet ja arkkitehtuurit
- **Moduuli03:** Paikalliset ja pilvikäyttöönoton strategiat
- **Moduuli04:** Mallien optimointi useilla kehyksillä (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Moduuli05:** SLMOps - tuotantotoiminnot
- **Moduuli06:** AI-agentit ja funktiokutsut
- **Moduuli07:** Alustakohtaiset toteutukset
- **Moduuli08:** Foundry Local -työkalupakki 10 kattavalla esimerkillä

### Ulkoiset riippuvuudet
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Paikallinen AI-mallien suoritusympäristö OpenAI-yhteensopivalla API:lla
  - [Dokumentaatio](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimointikehys
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Mallien optimointityökalu
- [OpenVINO](https://docs.openvino.ai/) - Intelin optimointityökalu

## Projektikohtaiset huomiot

### Moduuli08-esimerkkisovellukset

Repositoriossa on 10 kattavaa esimerkkisovellusta:

1. **01-REST Chat Quickstart** - Perus OpenAI SDK -integraatio
2. **02-OpenAI SDK Integration** - Edistyneet SDK-ominaisuudet
3. **03-Model Discovery & Benchmarking** - Mallien vertailutyökalut
4. **04-Chainlit RAG Application** - Hakuun perustuva generointi
5. **05-Multi-Agent Orchestration** - Perus agenttien koordinointi
6. **06-Models-as-Tools Router** - Älykäs mallien reititys
7. **07-Direct API Client** - Matalan
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel -integraatio

### Työpajan esimerkkisovellukset

Työpaja sisältää 6 edistyvää istuntoa käytännön toteutuksilla:

1. **Istunto 01** - Chatin käynnistys Foundry Local -integraatiolla
2. **Istunto 02** - RAG-putkisto ja arviointi RAGAS:illa
3. **Istunto 03** - Avoimen lähdekoodin mallien vertailu
4. **Istunto 04** - Mallien vertailu ja valinta
5. **Istunto 05** - Moniagenttisten orkestrointijärjestelmien hallinta
6. **Istunto 06** - Mallien reititys ja putkiston hallinta

Jokainen esimerkki esittelee eri näkökulmia Edge AI -kehityksestä Foundry Localilla.

### Suorituskykyhuomiot

- SLM:t on optimoitu reunalaitteille (2-16GB RAM)
- Paikallinen päättely tarjoaa 50-500ms vasteajat
- Kvantisointitekniikat pienentävät kokoa 75 % säilyttäen 85 % suorituskyvystä
- Reaaliaikainen keskustelukyvykkyys paikallisilla malleilla

### Tietoturva ja yksityisyys

- Kaikki käsittely tapahtuu paikallisesti - dataa ei lähetetä pilveen
- Soveltuu yksityisyyttä vaativiin sovelluksiin (terveydenhuolto, rahoitus)
- Täyttää datan suvereniteettivaatimukset
- Foundry Local toimii täysin paikallisella laitteistolla

## Apua saatavilla

### Dokumentaatio

- **Pääasiallinen README**: [README.md](README.md) - Repositorion yleiskatsaus ja oppimispolut
- **Opas**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Oppimisresurssit ja aikataulu
- **Tuki**: [SUPPORT.md](SUPPORT.md) - Kuinka saada apua
- **Tietoturva**: [SECURITY.md](SECURITY.md) - Tietoturvaongelmien raportointi

### Yhteisön tuki

- **GitHub Issues**: [Raportoi virheitä tai pyydä ominaisuuksia](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Esitä kysymyksiä ja jaa ideoita](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Tekniset ongelmat Foundry Localin kanssa](https://github.com/microsoft/Foundry-Local/issues)

### Yhteystiedot

- **Ylläpitäjät**: Katso [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Tietoturvaongelmat**: Noudata vastuullista ilmoittamista [SECURITY.md](SECURITY.md)
- **Microsoft-tuki**: Yritystukea varten ota yhteyttä Microsoftin asiakaspalveluun

### Lisäresurssit

- **Microsoft Learn**: [AI- ja koneoppimisen oppimispolut](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentaatio**: [Viralliset dokumentit](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Yhteisön esimerkit**: Katso [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) yhteisön kontribuutioita

---

**Tämä on opetusrepositorio, joka keskittyy Edge AI -kehityksen opettamiseen. Pääasiallinen kontribuutiomalli on opetusmateriaalin parantaminen ja esimerkkisovellusten lisääminen/täydentäminen, jotka havainnollistavat Edge AI -konsepteja.**

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.