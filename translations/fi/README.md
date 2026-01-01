<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T11:29:44+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# EdgeAI aloittelijoille 


![Kurssin kansikuva](../../translated_images/cover.eb18d1b9605d754b.fi.png)

[![GitHub-avustajat](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub-issueet](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub-pull‑pyynnöt](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR:t tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Noudata näitä ohjeita aloittaaksesi näiden resurssien käytön:

1. **Tee fork arkistosta**: Klikkaa [![GitHub-forkit](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Kloonaa arkisto**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Liity Azure AI Foundry Discordiin ja tapaa asiantuntijoita sekä muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen ja aina ajantasainen)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**If you wish to have additional translations languages supported are listed [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Johdanto

Tervetuloa **EdgeAI aloittelijoille** – kattavaan matkaan Edge-tekoälyn mullistavaan maailmaan. Tämä kurssi yhdistää tehokkaat tekoälyominaisuudet ja käytännön, tuotantoon vietävät käyttöönotot reunalaitteilla, antaen sinulle mahdollisuuden hyödyntää tekoälyn voimaa suoraan siellä, missä data syntyy ja päätöksiä täytyy tehdä.

### Mitä opit

Tämä kurssi vie sinut perustavanlaatuisista käsitteistä tuotantovalmiisiin toteutuksiin ja kattaa:
- **Pienet kielimallit (SLM:t)**, jotka on optimoitu reunalaitteille
- **Laitin tunteva optimointi** eri alustoilla
- **Reaaliaikainen inferenssi** yksityisyyttä suojaavilla ominaisuuksilla
- **Tuotantokäyttöönotto** strategiat yrityssovelluksille

### Miksi EdgeAI on tärkeää

Edge AI edustaa paradigman muutosta, joka ratkaisee nykyajan kriittisiä haasteita:
- **Yksityisyys ja turvallisuus**: Käsittele arkaluontoista dataa paikallisesti ilman pilveen joutumista
- **Reaaliaikainen suorituskyky**: Poista verkkoviive aikakriittisissä sovelluksissa
- **Kustannustehokkuus**: Vähennä kaistanleveyden ja pilvilaskennan kuluja
- **Kestävä toiminta**: Säilytä toiminnallisuus verkkokatkosten aikana
- **Säädösten noudattaminen**: Täytä datan suvereniteettivaatimukset

### Edge AI

Edge AI tarkoittaa tekoälyalgoritmien ja kielimallien suorittamista paikallisesti laitteessa, lähellä datan syntypaikkaa ilman, että inferenssi vaatii pilvipalveluita. Se pienentää viivettä, parantaa yksityisyyttä ja mahdollistaa reaaliaikaisen päätöksenteon.

### Perusperiaatteet:
- **Laitteessa suoritettava inferenssi**: Mallit ajetaan reunalaitteilla (puhelimet, reitittimet, mikro-ohjaimet, teolliset PC:t)
- **Offline-kyvykkyys**: Toimii ilman pysyvää internet-yhteyttä
- **Matala viive**: Välittömät vastaukset reaaliaikaisiin järjestelmiin
- **Datan suvereniteetti**: Pidä arkaluonteinen data paikallisena, parantaen turvallisuutta ja vaatimustenmukaisuutta

### Pienet kielimallit (SLM:t)

SLM:t kuten Phi-4, Mistral-7B ja Gemma ovat optimoituja versioita suuremmista LLM-malleista — koulutettuja tai tiivistettyjä:
- **Pienempi muistikulutus**: Tehokas käyttö reunalaitteiden rajoitetussa muistissa
- **Alhaisempi laskentavaatimukset**: Optimoitu CPU:lle ja reunalaitteiden GPU:lle
- **Nopeammat käynnistysajat**: Nopea alustautuminen reagoiviin sovelluksiin

Ne avaavat tehokkaat NLP-ominaisuudet ja täyttävät samalla rajoitteet:
- **Sulautetut järjestelmät**: IoT-laitteet ja teolliset ohjaimet
- **Mobiililaitteet**: Älypuhelimet ja tabletit offline-kyvykkyydellä
- **IoT-laitteet**: Anturit ja älylaitteet, joilla on rajalliset resurssit
- **Reunalaitteet / Edge-palvelimet**: Paikalliset laskentayksiköt, joilla on rajalliset GPU-resurssit
- **Tietokoneet**: Pöytä- ja kannettavien käyttöönottotapaukset

## Kurssin moduulit ja navigointi

| Moduuli | Aihe | Painopistealue | Keskeinen sisältö | Taso | Kesto |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Johdanto EdgeAI:iin](./introduction.md) | Perusta ja konteksti | EdgeAI:n yleiskatsaus • Toimialasovellukset • SLM-esittely • Oppimistavoitteet | Aloittelija | 1–2 tuntia |
| [📚 01](../../Module01) | [EdgeAI:n perusteet](./Module01/README.md) | Pilvi vs Edge AI -vertailu | EdgeAI:n perusteet • Käytännön tapaustutkimukset • Toteutusopas • Edge-käyttöönotto | Aloittelija | 3–4 tuntia |
| [🧠 02](../../Module02) | [SLM-mallin perusteet](./Module02/README.md) | Malliperheet ja arkkitehtuuri | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | Aloittelija | 4–5 tuntia |
| [🚀 03](../../Module03) | [SLM:n käyttöönotto käytännössä](./Module03/README.md) | Paikallinen ja pilvikäyttöönotto | Edistynyt oppiminen • Paikallinen ympäristö • Pilvikäyttöönotto | Keskitaso | 4–5 tuntia |
| [⚙️ 04](../../Module04) | [Mallin optimointityökalut](./Module04/README.md) | Monialustainen optimointi | Johdanto • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Workflow Synthesis | Keskitaso | 5–6 tuntia |
| [🔧 05](../../Module05) | [SLMOps tuotannossa](./Module05/README.md) | Tuotantotoiminnot | SLMOps-esittely • Mallin distillaatio • Hienosäätö • Tuotantokäyttöönotto | Edistynyt | 5–6 tuntia |
| [🤖 06](../../Module06) | [AI-agentit ja funktiokutsut](./Module06/README.md) | Agenttikehykset ja MCP | Agentin esittely • Funktiokutsut • Mallin kontekstiprotokolla | Edistynyt | 4–5 tuntia |
| [💻 07](../../Module07) | [Alustan toteutus](./Module07/README.md) | Esimerkkejä eri alustoille | AI-työkalupakki • Foundry Local • Windows-kehitys | Edistynyt | 3–4 tuntia |
| [🏭 08](../../Module08) | [Foundry Local -työkalupakki](./Module08/README.md) | Tuotantovalmiit esimerkit | Esimerkkisovellukset (katso yksityiskohdat alla) | Asiantuntija | 8–10 tuntia |

### 🏭 **Moduuli 08: Esimerkkisovellukset**

- [01: REST Chat - pika-aloitus](./Module08/samples/01/README.md)
- [02: OpenAI SDK -integraatio](./Module08/samples/02/README.md)
- [03: Mallin löytäminen ja vertailu](./Module08/samples/03/README.md)
- [04: Chainlit RAG -sovellus](./Module08/samples/04/README.md)
- [05: Moni-agenttien orkestrointi](./Module08/samples/05/README.md)
- [06: Mallit työkaluna - reititin](./Module08/samples/06/README.md)
- [07: Suora API-asiakas](./Module08/samples/07/README.md)
- [08: Windows 11 Chat -sovellus](./Module08/samples/08/README.md)
- [09: Edistynyt moni-agenttijärjestelmä](./Module08/samples/09/README.md)
- [10: Foundry-työkalukehys](./Module08/samples/10/README.md)

### 🎓 **Työpaja: Käytännön oppimispolku**

Kattavat käytännön työpajamateriaalit tuotantovalmiilla toteutuksilla:

- **[Työpajaopas](./Workshop/Readme.md)** - Täydelliset oppimistavoitteet, tulokset ja resurssien navigointi
- **Python-esimerkit** (6 istuntoa) - Päivitetty parhailla käytännöillä, virheenkäsittelyllä ja kattavalla dokumentaatiolla
- **Jupyter Notebookit** (8 interaktiivista) - Askelsiirtymäoppaat, benchmarkit ja suorituskyvyn seuranta
- **Istunto-ohjeet** - Yksityiskohtaiset markdown-oppaat jokaiselle työpajaistunnolle
- **Varmennustyökalut** - Skriptit koodin laadun tarkistamiseen ja smoke-testien ajamiseen

**Mitä rakennat:**
- Paikallisia AI-chat-sovelluksia suoratoistotuen kanssa
- RAG-putkia laadun arvioinnilla (RAGAS)
- Monimallien vertailu- ja benchmark-työkaluja
- Moni-agenttien orkestrointijärjestelmiä
- Älykäs mallien reititys tehtäväkohtaisen valinnan perusteella

### 📊 **Oppimispolun yhteenveto**
- **Kokonaiskesto**: 36–45 tuntia
- **Aloittelijan polku**: Modulut 01-02 (7–9 tuntia)  
- **Keskitasoinen polku**: Modulut 03-04 (9–11 tuntia)
- **Edistynyt polku**: Modulut 05-07 (12–15 tuntia)
- **Asiantuntijan polku**: Moduuli 08 (8–10 tuntia)

## Mitä rakennat

### 🎯 Keskeiset osaamisalueet
- **Edge AI -arkkitehtuuri**: Suunnittele paikalliset ensisijaiset AI-järjestelmät pilvi-integraatiolla
- **Mallien optimointi**: Mallien kvantisointi ja pakkaaminen reunalaitteisiin (85% nopeutus, 75% koon vähennys)
- **Monialustainen käyttöönotto**: Windows, mobiili, sulautetut järjestelmät ja pilvi-reuna-hybridijärjestelmät
- **Tuotantotoiminnot**: Reuna-AI:n valvonta, skaalaus ja ylläpito tuotannossa

### 🏗️ Käytännön projektit
- **Foundry Local Chat -sovellukset**: Windows 11 -natiivisovellus, jossa mallin vaihto
- **Moni-agenttijärjestelmät**: Koordinaattori ja erikoisagentit monimutkaisiin työnkulkuihin  
- **RAG-sovellukset**: Paikallinen asiakirjakäsittely vektorihauilla
- **Mallireitittimet**: Älykäs mallivalinta tehtävän analyysin perusteella
- **API-kehykset**: Tuotantovalmiit asiakasohjelmistot suoratoistolla ja kunnonvalvonnalla
- **Monialustaiset työkalut**: LangChain/Semantic Kernel -integraatiomallit

### 🏢 Teollisuuden sovellukset
**Valmistus** • **Terveydenhuolto** • **Autonomiset ajoneuvot** • **Älykkäät kaupungit** • **Mobiilisovellukset**

## Nopea aloitus

**Suositeltu oppimispolku** (20-30 tuntia yhteensä):

0. **📖 Johdanto** ([Introduction.md](./introduction.md)): EdgeAI:n perusteet + teollisuuden konteksti + oppimiskehys
1. **📚 Perusteet** (Modules 01-02): EdgeAI-käsitteet + SLM-malliperheet
2. **⚙️ Optimointi** (Modules 03-04): Käyttöönotto + kvantisointikehykset  
3. **🚀 Tuotanto** (Modules 05-06): SLMOps + AI-agentit + funktiokutsut
4. **💻 Toteutus** (Modules 07-08): Alustojen esimerkit + Foundry Local -työkalupakki

Jokainen moduuli sisältää teoriaa, käytännön harjoituksia ja tuotantovalmiita koodiesimerkkejä.

## Uravaikutus

**Tekniset roolit**: EdgeAI-ratkaisuarkkitehti • ML-insinööri (Edge) • IoT AI -kehittäjä • Mobiili-AI-kehittäjä

**Toimialasektorit**: Valmistus 4.0 • Terveydenhuollon teknologia • Autonomiset järjestelmät • FinTech • Kulutuselektroniikka

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

✅ **Jatkuva oppiminen**: Teoria → Käytäntö → Tuotantokäyttöön  
✅ **Todelliset tapaustutkimukset**: Microsoft, Japan Airlines, yritysimplementaatiot  
✅ **Käytännön esimerkit**: 50+ esimerkkiä, 10 kattavaa Foundry Local -demoa  
✅ **Suorituskyvyn painotus**: 85% nopeuden parannukset, 75% koon pienennykset  
✅ **Monialustainen**: Windows, mobiili, sulautetut, pilvi-reuna-hybridi  
✅ **Tuotantovalmius**: Valvonta, skaalaus, turvallisuus, vaatimustenmukaisuuden kehykset

📖 **[Opas saatavilla](STUDY_GUIDE.md)**: Rakenteinen 20 tunnin oppimispolku ajankäyttöohjeineen ja itsearviointityökaluineen.

---

**EdgeAI edustaa tekoälyn käyttöönoton tulevaisuutta**: paikallislähtöinen, yksityisyyttä suojaava ja tehokas. Hallitse nämä taidot rakentaaksesi seuraavan sukupolven älykkäitä sovelluksia.

## Muut kurssit

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
[![AI-agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivinen AI -sarja
[![Generatiivinen AI aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Perusopinnot
[![Koneoppiminen aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data-analytiikka aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Tekoäly aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Verkkokehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-sarja
[![Copilot AI-pariohjelmointiin](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET- kehittäjille](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-seikkailu](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Apua

Jos jumitut tai sinulla on kysymyksiä AI-sovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on palautetta tuotteesta tai kohtaat virheitä rakentamisen aikana, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla Co-op Translator (https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattisissa käännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä on pidettävä ensisijaisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->