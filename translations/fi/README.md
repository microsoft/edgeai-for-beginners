# EdgeAI Aloittelijoille


![Kurssin kansikuva](../../translated_images/fi/cover.eb18d1b9605d754b.webp)

[![GitHub-yhteistyöntekijät](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub ongelmat](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub vedä-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub seuraajat](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub haarukat](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub tähdet](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Seuraa näitä ohjeita aloittaaksesi näiden resurssien käyttämisen:

1. **Tee haarukka arkistosta**: Klikkaa [![GitHub haarukat](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Kloonaa arkisto**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Liity Azure AI Foundry Discordiin ja tapaa asiantuntijoita ja muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Monikielinen tuki

#### Tuettu GitHub-toiminnon kautta (Automaattinen & Aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Kiina (Yksinkertaistettu)](../zh-CN/README.md) | [Kiina (Perinteinen, Hong Kong)](../zh-HK/README.md) | [Kiina (Perinteinen, Macau)](../zh-MO/README.md) | [Kiina (Perinteinen, Taiwan)](../zh-TW/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norja](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../pt-BR/README.md) | [Portugali (Portugali)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (Kyrillinen)](../sr/README.md) | [Slovakki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (Filippiini)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Thaimaan kieli](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**

> Tämä arkisto sisältää yli 50 käännöskieltä, mikä lisää huomattavasti latauksen kokoa. Jos haluat kloonata ilman käännöksiä, käytä harvaa checkoutia:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tämä antaa sinulle kaiken tarvitsemasi kurssin suorittamiseen huomattavasti nopeammalla latausajalla.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jos haluat tukea lisäkielien käännöksiä, tuetut kielet löytyvät [täältä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Johdanto

Tervetuloa **EdgeAI Aloittelijoille** – kattava matkasi muutosvoimaiseen reunatietokoneälyn maailmaan. Tämä kurssi yhdistää tehokkaat tekoälyominaisuudet ja käytännön, todellisessa maailmassa tapahtuvan käyttöönoton reunalaitteilla, antaen sinulle mahdollisuuden hyödyntää tekoälyn potentiaalia suoraan siellä, missä dataa luodaan ja päätöksiä on tehtävä.

### Mitä hallitset

Tämä kurssi vie sinut perustavanlaatuisista käsitteistä tuotantovalmiisiin toteutuksiin, kattaen:
- **Pienet kielimallit (SLM)**, jotka on optimoitu reunalaitteille
- **Laitteistotietoinen optimointi** eri alustoilla
- **Reaaliaikainen inferenssi** yksityisyyttä suojaavilla ominaisuuksilla
- **Tuotantokäyttöönoton strategiat** yrityssovelluksille

### Miksi EdgeAI on tärkeää

Edge AI edustaa paradigmaattista muutosta, joka vastaa nykypäivän kriittisiin haasteisiin:
- **Yksityisyys & turvallisuus**: Käsittele arkaluontoista dataa paikallisesti ilman pilvivalvontaa
- **Reaaliaikainen suorituskyky**: Poista verkkoviive aikakriittisissä sovelluksissa
- **Kustannustehokkuus**: Vähennä kaistanleveyden ja pilvilaskennan kustannuksia
- **Kestävät toiminnot**: Säilytä toiminnallisuus verkko-ongelmien aikana
- **Sääntelyn noudattaminen**: Täytä datan suvereniteettivaatimukset

### Edge AI

Edge AI tarkoittaa tekoälyalgoritmien ja kielimallien ajamista paikallisesti laitteistolla, lähellä dataa, ilman pilvipalveluihin perustuvaa inferenssiä. Se vähentää viivettä, parantaa yksityisyyttä ja mahdollistaa reaaliaikaisen päätöksenteon.

### Keskeiset periaatteet:
- **Laitteistolla tehtävä inferenssi**: Tekoälymallit toimivat reunalaitteilla (puhelimet, reitittimet, mikrokontrollerit, teollisuus-PC:t)
- **Offline-toiminta**: Toimii ilman jatkuvaa internet-yhteyttä
- **Pieni viive**: Välittömät vastaukset reaaliaikaisiin järjestelmiin
- **Datan suvereniteetti**: Arkaluonteinen data pysyy paikallisena, parantaen turvallisuutta ja säädöstenmukaisuutta

### Pienet kielimallit (SLM)

SLMit kuten Phi-4, Mistral-7B ja Gemma ovat optimoituja versioita suuremmista LLM-malleista — koulutettuja tai tiivistettyjä:
- **Pienempi muistijalanjälki**: Tehokasta muistin käyttöä rajoitetuilla reunalaitteilla
- **Alhaisempi laskentavaatimukset**: Optimoitu CPU:lle ja reunan GPU-suorituskyvylle
- **Nopeampi käynnistysaika**: Pikainen alustus reagoiviin sovelluksiin

Ne avaavat tehokkaat NLP-ominaisuudet täyttäen samalla rajoitteet:
- **Sulautetut järjestelmät**: IoT-laitteet ja teollisuusohjaimet
- **Mobiililaitteet**: Älypuhelimet ja tabletit offline-toiminnoilla
- **IoT-laitteet**: Anturit ja älylaitteet rajallisilla resursseilla
- **Reunalaitteiden palvelimet**: Paikalliset yksiköt, joilla on rajallinen GPU
- **Henkilökohtaiset tietokoneet**: Työpöytä- ja kannettavat käyttötapaukset

## Kurssin moduulit & navigointi

| Moduuli | Aihe | Painopistealue | Keskeinen sisältö | Taso | Kesto |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Johdanto EdgeAIhin](./introduction.md) | Perusta & konteksti | EdgeAI Yleiskatsaus • Toimiala-sovellukset • SLM-esittely • Oppimistavoitteet | Aloittelija | 1-2 h |
| [📚 01](../../Module01) | [EdgeAI:n perusteet](./Module01/README.md) | Pilvi vs Reuna AI vertailu | EdgeAI-perusteet • Todelliset esimerkit • Toteutusohjeet • Reunan käyttöönotto | Aloittelija | 3-4 h |
| [🧠 02](../../Module02) | [SLM-mallien perusteet](./Module02/README.md) | Malliperheet & arkkitehtuuri | Phi-perhe • Qwen-perhe • Gemma-perhe • BitNET • μModel • Phi-Silica | Aloittelija | 4-5 h |
| [🚀 03](../../Module03) | [SLM-käyttöönoton käytäntö](./Module03/README.md) | Paikallinen & pilvikäyttö | Edistynyt oppiminen • Paikallinen ympäristö • Pilvikäyttöönotto | Keskitaso | 4-5 h |
| [⚙️ 04](../../Module04) | [Mallin optimointityökalut](./Module04/README.md) | Monialustainen optimointi | Johdanto • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Työnkulun synteesi | Keskitaso | 5-6 h |
| [🔧 05](../../Module05) | [SLMOps tuotannossa](./Module05/README.md) | Tuotantotoiminnot | SLMOps-esittely • Mallin tiivistäminen • Hienosäätö • Tuotantokäyttöönotto | Edistynyt | 5-6 h |
| [🤖 06](../../Module06) | [AI-agentit & funktiokutsut](./Module06/README.md) | Agenttikehykset & MCP | Agenttien esittely • Funktiokutsut • Mallin kontekstiprotokolla | Edistynyt | 4-5 h |
| [💻 07](../../Module07) | [Alustan toteutus](./Module07/README.md) | Monialustaiset esimerkit | AI-työkalut • Foundry Local • Windows-kehitys | Edistynyt | 3-4 h |
| [🏭 08](../../Module08) | [Foundry Local Työkalut](./Module08/README.md) | Tuotantovalmiita esimerkkejä | Esimerkkisovellukset (ks. tarkemmat tiedot alla) | Asiantuntija | 8-10 h |

### 🏭 **Moduuli 08: Esimerkkisovellukset**

- [01: REST Chat pikaohje](./Module08/samples/01/README.md)
- [02: OpenAI SDK integraatio](./Module08/samples/02/README.md)
- [03: Mallin löytäminen & vertailu](./Module08/samples/03/README.md)
- [04: Chainlit RAG -sovellus](./Module08/samples/04/README.md)
- [05: Moni-agenttien orkestrointi](./Module08/samples/05/README.md)
- [06: Mallit työkaluna reititin](./Module08/samples/06/README.md)
- [07: Suora API-asiakas](./Module08/samples/07/README.md)
- [08: Windows 11 chat-sovellus](./Module08/samples/08/README.md)
- [09: Edistynyt moni-agenttijärjestelmä](./Module08/samples/09/README.md)
- [10: Foundry Tools -kehys](./Module08/samples/10/README.md)

### 🎓 **Työpaja: Käytännön oppimispolku**

Kattavat käytännön työpajamateriaalit tuotantovalmiiden toteutusten kanssa:

- **[Työpajan opas](./Workshop/Readme.md)** - Täydelliset oppimistavoitteet, tulokset ja resurssinavigointi
- **Python-esimerkit** (6 osiota) - Päivitetty parhaiden käytäntöjen, virheenkäsittelyn ja kattavan dokumentaation kanssa
- **Jupyter-muistikirjat** (8 vuorovaikutteista) - Askeltavat tutoriaalit vertailuluvuilla ja suorituskyvyn seurannalla
- **Istunto-ohjeet** - Yksityiskohtaiset markdown-ohjeet jokaiselle työpajan istunnolle
- **Varmistustyökalut** - Skriptit koodin laadun tarkastukseen ja savutestien suorittamiseen

**Mitä rakennat:**
- Paikalliset tekoälychat-sovellukset virtaustuesta
- RAG-putket laadun arvioinnilla (RAGAS)
- Monimallien vertailu- ja benchmark-työkalut
- Moni-agenttien orkestrointijärjestelmät
- Älykäs mallien reititys tehtäväperusteisella valinnalla

### 🎙️ **Agenttic Workshop: Käytännön - AI Podcast Studio**

Rakenna tekoälyllä toimiva podcast-tuotantoputki alusta alkaen! Tämä immersiivinen työpaja opettaa sinut luomaan kokonaisen moni-agenttijärjestelmän, joka muuttaa ideat ammattimaisiksi podcast-jaksoiksi.
**[🎬 Aloita AI Podcast Studio -työpaja](./WorkshopForAgentic/README.md)**

**Tehtäväsi**: Julkaise "Future Bytes" — teknologia-aiheinen podcast, jota pyörittävät täysin itse rakentamasi AI-agentit. Ei pilvipalveluita, ei API-kuluja — kaikki toimii paikallisesti koneellasi.

**Mikä tekee tästä ainutlaatuisen:**
- **🤖 Todellinen monen agentin orkestrointi** - Rakenna erikoistuneita AI-agentteja, jotka tutkivat, kirjoittavat ja tuottavat ääntä
- **🎯 Täyden tuotantoputken hallinta** - Aiheet valinnasta aina lopulliseen podcast-äänitteeseen
- **💻 Täysin paikallinen käyttöönotto** - Käyttää Ollamaa ja paikallisia malleja (Qwen-3-8B) täyden yksityisyyden ja hallinnan takaamiseksi
- **🎤 Teksti puheeksi -integraatio** - Muuntaa käsikirjoitukset luonnollisen kuuloisiksi monipuheisiksi keskusteluiksi
- **✋ Ihminen osana prosessia** - Hyväksymisportit varmistavat laadun ja samalla automaation

**Kolmivaiheinen oppimismatka:**

| Näytös | Keskittyminen | Keskeiset taidot | Kesto |
|-----|-------|------------|----------|
| **[Näytös 1: Tutustu AI-avustajiisi](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Rakenna ensimmäinen AI-agenttisi | Työkalujen integrointi • Verkkohaku • Ongelmanratkaisu • Agenttipäätöksenteko | 2-3 h |
| **[Näytös 2: Kokoa tuotantotiimisi](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestroi useita agentteja | Tiimin koordinointi • Hyväksymisprosessit • DevUI-käyttöliittymä • Ihmisen valvonta | 3-4 h |
| **[Näytös 3: Herätä podcast eloon](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Luo podcast-äänite | Teksti puheeksi • Monipuheinen synteesi • Pitkän muodon ääni • Täysi automaatio | 2-3 h |

**Käytetyt teknologiat:**
- **Microsoft Agent Framework** - Monen agentin orkestrointi ja koordinointi
- **Ollama** - Paikallinen AI-mallin suoritusympäristö (ei pilveä tarpeen)
- **Qwen-3-8B** - Avoimen lähdekoodin kielimalli agenttitehtäviin optimoituna
- **Teksti puheeksi -rajapinnat** - Luonnollisen äänen synteesi podcast-tuotantoon

**Laitteistotuki:**
- ✅ **CPU-tila** - Toimii missä tahansa modernissa tietokoneessa (8GB+ RAM suositeltu)
- 🚀 **GPU-kiihdytys** - Paljon nopeampi suoritus NVIDIA/AMD-näytönohjaimilla
- ⚡ **NPU-tuki** - Uuden sukupolven hermoverkkoprosessorin kiihdytys

**Täydellinen sinulle, joka olet:**
- Kehittäjä oppimassa monen agentin AI-järjestelmiä
- Kiinnostunut AI-automaatioista ja työnkuluista
- Sisällöntuottaja, joka tutkii AI-avusteista tuotantoa
- Opiskelija, joka opiskelee käytännön AI-orkestrointimalleja

**Aloita rakentaminen**: [🎙️ AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Oppimispolun yhteenveto**
- **Kokonaiskesto**: 36–45 tuntia
- **Aloittelijan polku**: Modulien 01-02 (7-9 tuntia)  
- **Keskitaso**: Modulien 03-04 (9-11 tuntia)
- **Edistynyt taso**: Modulien 05-07 (12-15 tuntia)
- **Asiantuntijapolku**: Moduuli 08 (8-10 tuntia)

## Mitä rakennat

### 🎯 Keskeiset osaamisalueet
- **Edge AI -arkkitehtuuri**: Suunnittele paikallisesti toimivia AI-järjestelmiä pilviliitännällä
- **Mallin optimointi**: Kvantisoi ja pakkaa malleja reunalaitteille (85 % nopeutettu, 75 % pienempi koko)
- **Monialustainen käyttöönotto**: Windows, mobiili, sisäänrakennetut laitteet ja pilvi-reuna hybridi
- **Tuotantotoiminnot**: Valvonta, skaalaus ja reunalaitteiden AI:n ylläpito tuotannossa

### 🏗️ Käytännön projektit
- **Foundry Local -chat-sovellukset**: Windows 11:n natiivisovellus mallin vaihdolla
- **Moni-agenttijärjestelmät**: Koordinaattori ja erikoisagentit monimutkaisiin työnkulkuihin  
- **RAG-sovellukset**: Paikallinen dokumentinkäsittely ja vektorihaku
- **Mallireitittimet**: Älykäs mallien valinta tehtävän pohjalta
- **API-kehykset**: Tuotantovalmiit asiakkaat suoratoistolla ja tilanvalvonnalla
- **Monialustatyökalut**: LangChain/Semantic Kernel -integraatiomallit

### 🏢 Teolliset käyttötapaukset
**Valmistus** • **Terveydenhuolto** • **Autonomiset ajoneuvot** • **Älykkäät kaupungit** • **Mobiilisovellukset**

## Nopean aloituksen ohje

**Suositeltu oppimispolku** (yhteensä 20–30 tuntia):

0. **📖 Johdanto** ([Introduction.md](./introduction.md)): EdgeAI:n perusteet + teollisuuden konteksti + oppimisen rakenne
1. **📚 Perusteet** (Moduulit 01-02): EdgeAI-konseptit + SLM-malliperheet
2. **⚙️ Optimointi** (Moduulit 03-04): Käyttöönotto + kvantisointikehykset  
3. **🚀 Tuotanto** (Moduulit 05-06): SLMOps + AI-agentit + funktiokutsut
4. **💻 Toteutus** (Moduulit 07-08): Alustojen esimerkit + Foundry Local -työkalupakki

Jokainen moduuli sisältää teoriaa, käytännön harjoituksia ja tuotantovalmiita koodiesimerkkejä.

## Uramahdollisuudet

**Tekniset roolit**: EdgeAI-ratkaisusuunnittelija • ML-insinööri (Edge) • IoT AI-kehittäjä • Mobiili AI-kehittäjä

**Toimialat**: Valmistus 4.0 • Terveydenhuollon teknologia • Autonomiset järjestelmät • FinTech • Kulutuselektroniikka

**Portfolioprojektit**: Moni-agenttijärjestelmät • Tuotannon RAG-sovellukset • Monialustainen käyttöönotto • Suorituskyvyn optimointi

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

## Kurssin kohokohdat

✅ **Jatkuva oppiminen**: Teoria → Käytäntö → Tuotantoon käyttöönotto  
✅ **Aidot tapaustutkimukset**: Microsoft, Japan Airlines, yritysten toteutukset  
✅ **Käytännön esimerkit**: 50+ esimerkkiä, 10 kattavaa Foundry Local -demoa  
✅ **Suorituskyvyn painotus**: 85 % nopeuden parannus, 75 % koon pienennys  
✅ **Monialustainen**: Windows, mobiili, sisäänrakennettu, pilvi-reuna hybridi  
✅ **Tuotantovalmius**: Valvonta, skaalaus, turvallisuus, vaatimustenmukaisuus

📖 **[Opas saatavilla](STUDY_GUIDE.md)**: Rakenettu 20 tunnin oppimispolku, jossa ajoituksen ohjeet ja itsearviointityökalut.

---

**EdgeAI on AI:n käyttöönoton tulevaisuus**: paikallinen, yksityisyyttä suojaava ja tehokas. Hallitse nämä taidot rakentaaksesi seuraavan sukupolven älykkäitä sovelluksia.

## Muita kursseja

Tiimimme tuottaa myös muita kursseja! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain aloittelijoille](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
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
 
### Perusopetus
[![ML aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-sarja
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Apua

Jos jumitut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on palautetta tuotteesta tai kohtaat virheitä rakentaessasi, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä tulee pitää ensisijaisena ja virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->