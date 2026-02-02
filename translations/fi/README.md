# EdgeAI Aloittelijoille


![Kurssin kansikuva](../../translated_images/fi/cover.eb18d1b9605d754b.webp)

[![GitHubin kontribuuttorit](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub-ongelmat](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub-pull-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR: tä Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub-katselijat](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub-forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub-tähdet](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Seuraa näitä ohjeita aloittaaksesi näiden resurssien käytön:

1. **Haarauta varasto**: Klikkaa [![GitHub-forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Kloonaa varasto**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Liity Azure AI Foundry Discordiin ja tapaa asiantuntijoita ja muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (Automaattinen & aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**

> Tämä varasto sisältää yli 50 käännöstä, mikä lisää merkittävästi latauskokoa. Kloonatakseen ilman käännöksiä, käytä sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Näin saat kaiken tarvittavan kurssin suorittamiseen paljon nopeammin.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jos haluat tukea lisäkielillä, tuetut kielet on listattu [täällä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Johdanto

Tervetuloa **EdgeAI Aloittelijoille** – kattavaan matkaasi Edge-tekoälyn mullistavaan maailmaan. Tämä kurssi yhdistää voimakkaat tekoälyominaisuudet käytännön, reaalimaailman käyttöönottoon reunalaitteissa, antaen sinulle voiman hyödyntää tekoälyn potentiaalia suoraan siellä, missä dataa syntyy ja päätökset on tehtävä.

### Mitä opit hallitsemaan

Tämä kurssi vie sinut perustavanlaatuisista käsitteistä tuotantovalmiisiin toteutuksiin, kattaen:
- **Pienet kielimallit (SLM:t)**, jotka on optimoitu reunalaitteiden käyttöön
- **Laitteistotietoinen optimointi** eri alustoilla
- **Reaaliaikainen inferenssi** yksityisyyttä suojaavin ominaisuuksin
- **Tuotantoon käyttöönoton** strategiat yrityssovelluksiin

### Miksi EdgeAI on tärkeää

Edge AI edustaa paradigmamuutosta, joka vastaa keskeisiin nykyaikaisiin haasteisiin:
- **Yksityisyys & tietoturva**: Käsittele arkaluontoista dataa paikallisesti ilman pilven altistamista
- **Reaaliaikainen suorituskyky**: Poista verkkoviiveet aikakriittisissä sovelluksissa
- **Kustannustehokkuus**: Vähennä kaistanleveys- ja pilvilaskentakustannuksia
- **Kestävä toiminta**: Säilytä toimivuus verkkokatkosten aikana
- **Säädösten noudattaminen**: Täytä datan suvereniteettivaatimukset

### Edge AI

Edge AI tarkoittaa tekoälyalgoritmien ja kielimallien suorittamista paikallisesti laitteilla lähellä datan syntypaikkaa ilman, että inferenssiä tehdään pilvipalvelimilla. Se vähentää latenssia, parantaa yksityisyyttä ja mahdollistaa reaaliaikaisen päätöksenteon.

### Perusperiaatteet:
- **Laitteella inferenssi**: Tekoälymallit ajetaan reunalaitteissa (puhelimet, reitittimet, mikrokontrollerit, teollisuus-PC:t)
- **Offline-kyky**: Toimii ilman jatkuvaa internet-yhteyttä
- **Pieni viive**: Välittömät vastaukset reaaliaikajärjestelmiin sopivia
- **Datansuoja**: Arkaluonteinen data pysyy paikallisena, parantaen turvallisuutta ja säädösten mukaista toimintaa

### Pienet kielimallit (SLM:t)

SLM:t kuten Phi-4, Mistral-7B ja Gemma ovat suurempien LLM:ien optimoituja versioita — koulutettuja tai tiivistettyjä seuraaviin tarkoituksiin:
- **Pienennetty muistinkulutus**: Tehokas käytös reunalaitteiden rajallisessa muistissa
- **Alhaisempi laskentavaade**: Optimoitu CPU- ja reunakäyttöön GPU-suorituskykyä ajatellen
- **Nopeammat käynnistysajat**: Nopeaa aloitusta reagoiville sovelluksille

Ne avaavat tehokkaat NLP-ominaisuudet ja täyttävät seuraavat rajat:
- **Sulautetut järjestelmät**: IoT-laitteet ja teollisuuden ohjaimet
- **Mobiililaitteet**: Älypuhelimet ja tabletit offline-toiminnolla
- **IoT-laitteet**: Anturit ja älylaitteet, joissa on rajalliset resurssit
- **Reunapalvelimet**: Paikalliset prosessointiyksiköt, joissa rajoitetut GPU-resurssit
- **Henkilökohtaiset tietokoneet**: Työpöytä- ja kannettavat käyttökohteet

## Kurssimoduulit & navigointi

| Moduuli | Aihe | Painopistealue | Keskeinen sisältö | Taso | Kesto |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Johdanto EdgeAI:hin](./introduction.md) | Perusteet & konteksti | EdgeAI Yleiskatsaus • Teollisuuden sovellukset • SLM Johdanto • Oppimistavoitteet | Aloittelija | 1-2 h |
| [📚 01](../../Module01) | [EdgeAI Perusteet](./Module01/README.md) | Pilvi vs Edge AI vertailu | EdgeAI Perusteet • Todellisia esimerkkitapauksia • Toteutusopas • Reunalle käyttöönotto | Aloittelija | 3-4 h |
| [🧠 02](../../Module02) | [SLM Mallin perusteet](./Module02/README.md) | Malliperheet & arkkitehtuuri | Phi-perhe • Qwen-perhe • Gemma-perhe • BitNET • μModel • Phi-Silica | Aloittelija | 4-5 h |
| [🚀 03](../../Module03) | [SLM Käyttöönotto käytännössä](./Module03/README.md) | Paikallinen & pilvikäyttöönotto | Edistynyt oppiminen • Paikallinen ympäristö • Pilven käyttöönotto | Keskitaso | 4-5 h |
| [⚙️ 04](../../Module04) | [Mallin optimointityökalut](./Module04/README.md) | Alustariippumaton optimointi | Johdanto • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Työnkulun syntetisointi | Keskitaso | 5-6 h |
| [🔧 05](../../Module05) | [SLMOps Tuotannossa](./Module05/README.md) | Tuotantotoiminnot | SLMOps Johdanto • Mallin tiivistys • Hienosäätö • Tuotantokäyttöön otto | Edistynyt | 5-6 h |
| [🤖 06](../../Module06) | [Tekoälyagentit & Funktiokutsut](./Module06/README.md) | Agenttikehykset & MCP | Agenttien johdanto • Funktiokutsut • Mallin kontekstiprotokolla | Edistynyt | 4-5 h |
| [💻 07](../../Module07) | [Alustan toteutus](./Module07/README.md) | Alustariippumattomat esimerkit | AI-työkalut • Foundry Local • Windows-kehitys | Edistynyt | 3-4 h |
| [🏭 08](../../Module08) | [Foundry Local Työkalut](./Module08/README.md) | Tuotantovalmita esimerkkejä | Esimerkkisovellukset (katso alla tarkemmin) | Asiantuntija | 8-10 h |

### 🏭 **Moduuli 08: Esimerkkisovellukset**

- [01: REST Chat Aloitusopas](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integraatio](./Module08/samples/02/README.md)
- [03: Mallin löytäminen & vertailu](./Module08/samples/03/README.md)
- [04: Chainlit RAG sovellus](./Module08/samples/04/README.md)
- [05: Moniagenttien orkestrointi](./Module08/samples/05/README.md)
- [06: Mallit työkaluna reititin](./Module08/samples/06/README.md)
- [07: Suora API-asiakas](./Module08/samples/07/README.md)
- [08: Windows 11 Chat-sovellus](./Module08/samples/08/README.md)
- [09: Edistynyt moniagenttijärjestelmä](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Työpaja: Käytännön oppimispolku**

Kattavat käytännön työpajamateriaalit tuotantovalmiilla toteutuksilla:

- **[Työpajaopas](./Workshop/Readme.md)** - Täydelliset oppimistavoitteet, tulokset ja resurssinavigointi
- **Python-esimerkit** (6 istuntoa) - Päivitetty parhailla käytännöillä, virheenkäsittelyllä ja kattavalla dokumentaatiolla
- **Jupyter-muistikirjat** (8 interaktiivista) - Askel askeleelta oppaat, suorituskyvyn benchmarkit ja seuranta
- **Istuntojen oppaat** - Yksityiskohtaiset Markdown-oppaat jokaiseen työpajaistuntoon
- **Varmennustyökalut** - Skriptit koodin laadun tarkistamiseen ja pikakokeisiin

**Mitä rakennat:**
- Paikalliset tekoälychat-sovellukset suoratoistolla
- RAG-putket laadunarvioinnilla (RAGAS)
- Monimallien benchmarkkaus- ja vertailutyökalut
- Moniagenttien orkestrointijärjestelmät
- Älykäs mallien reititys tehtävävalinnalla

### 🎙️ **Workshop For Agentic: Hands-On - The AI Podcast Studio**

Rakenna tekoälyllä toimiva podcast-tuotantoputki alusta alkaen! Tämä kokemuksellinen työpaja opettaa sinulle, miten luodaan kokonainen moniagenttijärjestelmä, joka muuttaa ideat ammattimaisiksi podcast-jaksoiksi.
**[🎬 Aloita AI Podcast Studio -työpaja](./WorkshopForAgentic/README.md)**

**Tehtäväsi**: Käynnistä "Future Bytes" — täysin AI-agenttien voimalla toimiva teknologiapodcast, jonka rakennat itse. Ei pilvipalveluriippuvuuksia, ei API-maksuja — kaikki toimii paikallisesti koneellasi.

**Mikä tekee tästä ainutlaatuisen:**
- **🤖 Aito monen agentin orkestrointi** - Rakenna erikoistuneita AI-agentteja, jotka tutkivat, kirjoittavat ja tuottavat ääntä
- **🎯 Täydellinen tuotantoputki** - Aiheluettelo valinnasta loppupodcastin äänituotantoon
- **💻 Täysin paikallinen käyttöönotto** - Käyttää Ollamaa ja paikallisia malleja (Qwen-3-8B) täyteen yksityisyyteen ja hallintaan
- **🎤 Teksti puheeksi -integraatio** - Muunna käsikirjoitukset luonnollisen kuuloisiksi monipuheisiksi keskusteluiksi
- **✋ Ihmisen valvoma työnkulku** - Hyväksymisportit takaavat laadun ja pitävät automaation hallinnassa

**Kolmiosainen oppimismatka:**

| Näytös | Keskittyminen | Tärkeimmät taidot | Kesto |
|-----|-------|------------|----------|
| **[Näytös 1: Tapaa AI-avustajasi](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Rakenna ensimmäinen AI-agenttisi | Työkalujen integrointi • Verkkohaku • Ongelmanratkaisu • Agenttilogiikka | 2-3 tuntia |
| **[Näytös 2: Kokoa tuotantotiimisi](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestroi useita agentteja | Tiimikoordinointi • Hyväksymisprosessit • DevUI-käyttöliittymä • Ihmisen valvonta | 3-4 tuntia |
| **[Näytös 3: Herätä podcastisi eloon](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Tuota podcast-ääntä | Teksti puheeksi • Monipuheinen synteesi • Pitkämuotoinen ääni • Täysi automaatio | 2-3 tuntia |

**Käytetyt teknologiat:**
- **Microsoft Agent Framework** - Moniagenttien orkestrointi ja koordinointi
- **Ollama** - Paikallinen AI-mallin suoritusympäristö (ei pilveä)
- **Qwen-3-8B** - Avoimen lähdekoodin kielen malli, optimoitu agenttitehtäviin
- **Teksti puheeksi -rajapinnat** - Luonnollisen äänen synteesi podcastin tuotantoon

**Laitetuki:**
- ✅ **CPU-tila** - Toimii millä tahansa nykyaikaisella tietokoneella (8 Gt RAM suositellaan)
- 🚀 **GPU-kiihdytys** - Huomattavasti nopeampi päätelaskenta NVIDIA/AMD-GPUilla
- ⚡ **NPU-tuki** - Uuden sukupolven hermoverkkoprosessorin kiihdytys

**Täydellinen:**
- Kehittäjille, jotka opiskelevat moniagenttisia AI-järjestelmiä
- Kuka tahansa, joka on kiinnostunut AI-automaatioista ja työnkuluista
- Sisällöntuottajille, jotka tutkivat AI-avustettua tuotantoa
- Opiskelijoille, jotka opiskelevat käytännön AI-orkestrointimalleja

**Aloita rakentaminen**: [🎙️ AI Podcast Studio -työpaja →](./WorkshopForAgentic/README.md)

### 📊 **Oppimispolun yhteenveto**
- **Kokonaiskesto**: 36-45 tuntia
- **Aloittelijan polku**: Modulut 01-02 (7-9 tuntia)  
- **Keskitaso**: Modulut 03-04 (9-11 tuntia)
- **Edistynyt taso**: Modulut 05-07 (12-15 tuntia)
- **Asiantuntijapolku**: Moduuli 08 (8-10 tuntia)

## Mitä rakennat

### 🎯 Keskeiset osaamisalueet
- **Edge AI -arkkitehtuuri**: Suunnittele paikallisesti ensisijaisia AI-järjestelmiä pilviyhteyksillä
- **Mallin optimointi**: Kvantointi ja pakkauksen käyttö reunaympäristössä (85 % nopeampi, 75 % pienempi)
- **Monialustainen käyttöönotto**: Windows, mobiili, upotetut järjestelmät ja pilvi-reuna-hybridit
- **Tuotantotoiminnot**: Seuranta, skaalaus ja reunaympäristön ylläpito tuotannossa

### 🏗️ Käytännön projektit
- **Foundry Local -chat-sovellukset**: Windows 11:n natiivisovellus mallinvaihdolla
- **Moniagenttijärjestelmät**: Koordinaattori ja erikoistuneet agentit monimutkaisiin työnkulkuihin  
- **RAG-sovellukset**: Paikallinen asiakirjakäsittely vektorihaulla
- **Mallireitittimet**: Älykäs valinta mallien välillä tehtäväanalyysin perusteella
- **API-kehykset**: Tuotantovalmiit klientit striimauksella ja seurantatoiminnoilla
- **Monialustatyökalut**: LangChain/Semantic Kernel -integraatiomallit

### 🏢 Teollisuuden sovellukset
**Valmistus** • **Terveysala** • **Autonomiset ajoneuvot** • **Älykkäät kaupungit** • **Mobiilisovellukset**

## Pikakäynnistys

**Suositeltu oppimispolku** (yhteensä 20-30 tuntia):

0. **📖 Johdanto** ([Introduction.md](./introduction.md)): EdgeAI:n perusteet + toimiala + oppimiskehys
1. **📚 Perusteet** (moduulit 01-02): EdgeAI:n konseptit + SLM-malliperheet
2. **⚙️ Optimointi** (moduulit 03-04): Käyttöönotto + kvantisointikehykset  
3. **🚀 Tuotanto** (moduulit 05-06): SLMOps + AI-agentit + toiminnonkutsut
4. **💻 Toteutus** (moduulit 07-08): Alustanäytteet + Foundry Local -työkalupakki

Jokainen moduuli sisältää teoriaa, käytännön harjoituksia ja tuotantovalmiita koodiesimerkkejä.

## Uramahdollisuudet

**Tekniset roolit**: EdgeAI-ratkaisuarkkitehti • ML-insinööri (Edge) • IoT AI-kehittäjä • Mobiili AI-kehittäjä

**Toimialat**: Valmistus 4.0 • Terveydenhuollon teknologia • Autonomiset järjestelmät • FinTech • Kulutuselektroniikka

**Portfoliohankkeet**: Moniagenttijärjestelmät • Tuotannon RAG-sovellukset • Monialustainen käyttöönotto • Suorituskyvyn optimointi

## Repositorion rakenne

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Kurssin kohokohtia

✅ **Jatkuva oppiminen**: Teoria → käytäntö → tuotantokäyttö  
✅ **Todelliset tapaustutkimukset**: Microsoft, Japan Airlines, yritystoteutukset  
✅ **Käytännön esimerkit**: 50+ esimerkkiä, 10 laajaa Foundry Local -demoa  
✅ **Suorituskyvyn parannus**: 85 % nopeampi, 75 % pienempi koko  
✅ **Monialustainen**: Windows, mobiili, upotettu, pilvi-reuna-hybridi  
✅ **Tuotantovalmius**: Seuranta, skaalaus, turvallisuus, vaatimustenmukaisuus

📖 **[Opas studiota varten](STUDY_GUIDE.md)**: Jäsennelty 20 tunnin oppimispolku ajankäytön ohjauksella ja itsearviointityökaluilla.

---

**EdgeAI edustaa tekoälyn tulevaisuutta**: paikallinen, yksityisyys säilyttävä ja tehokas. Hallitse nämä taidot rakentaaksesi älykkäiden sovellusten seuraavaa sukupolvea.

## Muita kursseja

Tiimimme tuottaa myös muita kursseja! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agentit
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivinen AI -sarja
[![Generatiivinen AI aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Ydintieto
[![ML aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-sarja
[![Copilot tekoälypariohjelmointiin](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Avun saaminen

Jos jumitut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on tuotepalaute tai kohtaat virheitä rakentamisen aikana, käy osoitteessa:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä dokumentti on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä dokumenttia sen omalla kielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->