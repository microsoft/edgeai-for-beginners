# EdgeAI za začetnike 


![Naslovna slika tečaja](../../translated_images/sl/cover.eb18d1b9605d754b.webp)

[![GitHub sodelavci](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub težave](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requesti](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub opazovalci](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forki](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub zvezdice](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Sledite tem korakom, da začnete uporabljati te vire:

1. **Razvezi repozitorij**: Kliknite [![GitHub forki](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonirajte repozitorij**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discord in spoznajte strokovnjake ter druge razvijalce**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Podpora za več jezikov

#### Podprto preko GitHub Action (avtomatizirano in vedno posodobljeno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raje klonirate lokalno?**

> Ta repozitorij vključuje več kot 50 jezikovnih prevodov, kar znatno poveča velikost prenosa. Če želite klonirati brez prevodov, uporabite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tako dobite vse potrebno za dokončanje tečaja z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Če želite dodati podporo za dodatne jezike prevodov, so podprti jeziki navedeni [tukaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Uvod

Dobrodošli v **EdgeAI za začetnike** – vašo celovito potovanje v preoblikovalni svet robne umetne inteligence. Ta tečaj premošča vrzel med močnimi zmožnostmi umetne inteligence in praktično, dejansko uporabo na robnih napravah ter vam omogoča, da izkoristite potencial AI neposredno tam, kjer se podatki ustvarjajo in je potrebno sprejemati odločitve.

### Kaj boste obvladali

Ta tečaj vas popelje od osnovnih pojmov do izdelkov, pripravljenih za uporabo, pokrivajoč:
- **Majhni jezikovni modeli (SLM)**, optimizirani za robno uporabo
- **Optimizacijo z zavedanjem strojne opreme** na različnih platformah
- **Sprotno sklepanje** z zmožnostmi ohranjanja zasebnosti
- **Strategije uvajanja v produkcijo** za poslovne aplikacije

### Zakaj je EdgeAI pomemben

Edge AI predstavlja paradigmo, ki odgovarja na ključne sodobne izzive:
- **Zasebnost in varnost**: Obdelava občutljivih podatkov lokalno brez dostopa do oblaka
- **Sprotna zmogljivost**: Odprava zakasnitev omrežja za časovno kritične aplikacije
- **Učinkovitost stroškov**: Zmanjšanje pasovne širine in stroškov oblačnega računalništva
- **Odpornost delovanja**: Ohranjanje funkcionalnosti med izpadi omrežja
- **Skladnost z zakonodajo**: Izpolnjevanje zahtev glede suverenosti podatkov

### Edge AI

Edge AI pomeni izvajanje AI algoritmov in jezikovnih modelov lokalno na strojni opremi, blizu mesta nastanka podatkov, brez odvisnosti od oblačnih virov za sklepanje. Zmanjšuje zakasnitve, izboljšuje zasebnost ter omogoča trenutno sprejemanje odločitev.

### Temeljna načela:
- **Sklepanje na napravi**: AI modeli tečejo na robnih napravah (telefoni, usmerjevalniki, mikrokontrolerji, industrijski računalniki)
- **Sposobnost brez povezave**: Delovanje brez stalne internetne povezave
- **Nizka zakasnitev**: Neposredni odzivi, primerni za sisteme v realnem času
- **Suverenost podatkov**: Občutljivi podatki ostanejo lokalni, kar izboljšuje varnost in skladnost

### Majhni jezikovni modeli (SLM)

SLM kot so Phi-4, Mistral-7B in Gemma so optimizirane različice večjih velikih jezikovnih modelov — usposobljene ali destilirane za:
- **Zmanjšan porabnik pomnilnika**: Učinkovita raba omejenega pomnilnika na robnih napravah
- **Nižje računske zahteve**: Optimizirani za CPU in robne GPU-je
- **Hitrejši zagonski časi**: Hitro inicializiranje za odzivne aplikacije

Omogočajo močne zmogljivosti NLP, hkrati pa ustrezajo omejitvam:
- **Vgrajeni sistemi**: IoT naprave in industrijski krmilniki
- **Mobilne naprave**: Pametni telefoni in tablice z možnostjo delovanja brez povezave
- **IoT naprave**: Senzorji in pametne naprave z omejenimi viri
- **Robni strežniki**: Lokalne procesne enote z omejenimi GPU viri
- **Osebni računalniki**: Namizne in prenosne možnosti uvajanja

## Moduli tečaja in navigacija

| Modul | Tema | Osrednje področje | Ključna vsebina | Raven | Trajanje |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod v EdgeAI](./introduction.md) | Osnove in kontekst | Pregled EdgeAI • Industrijske aplikacije • Uvod v SLM • Cilji učenja | Začetnik | 1-2 h |
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Primerjava med oblakom in robom | Osnove EdgeAI • Primeri iz resničnega sveta • Vodnik po izvedbi • Robno uvajanje | Začetnik | 3-4 h |
| [🧠 02](../../Module02) | [Osnove SLM modelov](./Module02/README.md) | Družine modelov in arhitektura | Phi družina • Qwen družina • Gemma družina • BitNET • μModel • Phi-Silica | Začetnik | 4-5 h |
| [🚀 03](../../Module03) | [Praksa uvajanja SLM](./Module03/README.md) | Lokalno in oblačno uvajanje | Napredno učenje • Lokalno okolje • Oblačno uvajanje | Srednje | 4-5 h |
| [⚙️ 04](../../Module04) | [Orodja za optimizacijo modela](./Module04/README.md) | Optimizacija na različnih platformah | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza delovnega toka | Srednje | 5-6 h |
| [🔧 05](../../Module05) | [Produkcijsko upravljanje SLM](./Module05/README.md) | Produkcijsko delovanje | Uvod v SLMOps • Destilacija modelov • Natančno nastavljanje • Produkcijsko uvajanje | Napredno | 5-6 h |
| [🤖 06](../../Module06) | [AI agenti in klicanje funkcij](./Module06/README.md) | Okviri agentov in MCP | Uvod v agente • Klic funkcij • Protokol konteksta modela | Napredno | 4-5 h |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Vzorce za več platform | AI orodjarna • Foundry Local • Razvoj v Windows | Napredno | 3-4 h |
| [🏭 08](../../Module08) | [Foundry Local orodjarna](./Module08/README.md) | Vzorce pripravljeni za produkcijo | Vzorčne aplikacije (poglejte spodaj) | Strokovnjak | 8-10 h |

### 🏭 **Modul 08: Vzorčne aplikacije**

- [01: Hitri začetek z REST chat](./Module08/samples/01/README.md)
- [02: Integracija OpenAI SDK](./Module08/samples/02/README.md)
- [03: Odkritje modelov in benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)
- [05: Orkestracija več agentov](./Module08/samples/05/README.md)
- [06: Usmerjevalnik modelov kot orodij](./Module08/samples/06/README.md)
- [07: Neposredni API odjemalec](./Module08/samples/07/README.md)
- [08: Windows 11 chat aplikacija](./Module08/samples/08/README.md)
- [09: Napredni sistem z več agenti](./Module08/samples/09/README.md)
- [10: Okvir orodij Foundry](./Module08/samples/10/README.md)

### 🎓 **Delavnica: Praktična učna pot**

Celoviti materiali za prakso z izvedbami pripravljenimi za produkcijo:

- **[Vodnik po delavnici](./Workshop/Readme.md)** - Celotni cilji učenja, rezultati in navigacija virov
- **Python vzorci** (6 sej) - Posodobljeni z najboljšimi praksami, obravnavo napak in popolno dokumentacijo
- **Jupyter zvezki** (8 interaktivnih) - Korak za korakom vodiči z benchmarkingom in spremljanjem zmogljivosti
- **Vodniki sej** - Podrobni markdown vodiči za vsako delavnico
- **Orodja za preverjanje** - Skripte za preverjanje kakovosti kode in izvajanje hitrih testov

**Kaj boste zgradili:**
- Lokalni AI klepetalni programi s podporo pretakanja
- RAG cevovodi z ocenjevanjem kakovosti (RAGAS)
- Orodja za benchmarking in primerjavo več modelov
- Sistemi za orkestracijo več agentov
- Pametno usmerjanje modelov z izbiro glede na nalogo

### 🎙️ **Delavnica za agente: Praktično - AI podcast studio**

Zgradite produkcijsko cevovod za podcast, podprt z AI, iz nič! Ta poglobljena delavnica vas uči, kako ustvariti popoln sistem z več agenti, ki pretvori ideje v profesionalne epizode podcasta.
**[🎬 Začni delavnico AI Podcast Studia](./WorkshopForAgentic/README.md)**

**Tvoja naloga**: Zaženi "Future Bytes" — tehnološki podcast, ki ga poganjajo povsem AI agenti, ki jih boš zgradil sam. Brez odvisnosti od oblaka, brez stroškov API-jev — vse deluje lokalno na tvojem računalniku.

**Kaj naredi to edinstveno:**
- **🤖 Prava večagentna orkestracija** - Zgradi specializirane AI agente, ki raziskujejo, pišejo in proizvajajo zvok
- **🎯 Celoten produkcijski proces** - Od izbire teme do končnega podcast zvočnega izpisa
- **💻 100 % lokalna izvedba** - Uporablja Ollamo in lokalne modele (Qwen-3-8B) za popolno zasebnost in nadzor
- **🎤 Integracija besedila v govor** - Pretvori skripte v naravne večgovorne pogovore
- **✋ Človeški nadzor v procesu** - Dovolilna vrata zagotavljajo kakovost hkrati pa ohranjajo avtomatizacijo

**Učno potovanje v treh dejanjih:**

| Dejanje | Osredotočenost | Ključne spretnosti | Trajanje |
|---------|----------------|--------------------|----------|
| **[Dejanje 1: Spoznaj svoje AI asistente](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Zgradi svoj prve AI agent | Integracija orodij • Iskanje po spletu • Reševanje problemov • Agentno sklepanje | 2-3 ure |
| **[Dejanje 2: Zberi svojo produkcijsko ekipo](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestriraj več agentov | Koordinacija ekipe • Delovni procesi odobritve • DevUI vmesnik • Človeški nadzor | 3-4 ure |
| **[Dejanje 3: Oživi svoj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Ustvari zvok podcasta | Besedilo v govor • Sintetiziranje več govorcev • Dolgoročni zvok • Polna avtomatizacija | 2-3 ure |

**Uporabljene tehnologije:**
- **Microsoft Agent Framework** - Večagentna orkestracija in koordinacija
- **Ollama** - Lokalni AI modelni runtime (brez potrebe po oblaku)
- **Qwen-3-8B** - Odprtokodni jezikovni model optimiziran za agentne naloge
- **API-ji za besedilo v govor** - Naravna sinteza glasu za generiranje podcasta

**Podpora strojne opreme:**
- ✅ **CPU način** - Deluje na kateremkoli sodobnem računalniku (priporočljivo 8GB+ RAM)
- 🚀 **Pospeševanje GPU** - Za bistveno hitrejšo inferenco z NVIDIA/AMD GPU-ji
- ⚡ **Podpora NPU** - Pospeševanje naslednje generacije nevronskih procesnih enot

**Popolno za:**
- Razvijalce, ki se učijo večagentnih AI sistemov
- Vsakogar, ki ga zanima AI avtomatizacija in poteki dela
- Ustvarjalce vsebin, ki raziskujejo AI-podprto produkcijo
- Študente, ki študirajo praktične vzorce AI orkestracije

**Začni graditi**: [🎙️ Delavnica AI Podcast Studia →](./WorkshopForAgentic/README.md)

### 📊 **Povzetek učne poti**
- **Skupna dolžina**: 36-45 ur
- **Začetna pot**: Moduli 01-02 (7-9 ur)  
- **Srednje zahtevna pot**: Moduli 03-04 (9-11 ur)
- **Napredna pot**: Moduli 05-07 (12-15 ur)
- **Strokovna pot**: Modul 08 (8-10 ur)

## Kaj boš zgradil

### 🎯 Osnovne kompetence
- **Edge AI arhitektura**: Oblikuj lokalno-prednostne AI sisteme z oblačno integracijo
- **Optimizacija modelov**: Kvantiziraj in stisni modele za izvajanje na robu (85 % hitrejše, 75 % manjše)
- **Večplatformska izvedba**: Windows, mobilno, embedded in hibridni sistemi oblak-rob
- **Produkcijske operacije**: Nadzor, skaliranje in vzdrževanje edge AI v produkciji

### 🏗️ Praktični projekti
- **Foundry lokalne klepetalne aplikacije**: Nativna Windows 11 aplikacija z zamenjavo modelov
- **Večagentni sistemi**: Koordinator s specialističnimi agenti za kompleksne poteke dela  
- **RAG aplikacije**: Lokalno obdelovanje dokumentov z vektorskim iskanjem
- **Modelni usmerjevalniki**: Pametna izbira med modeli glede na analizo naloge
- **API ogrodja**: Produkcijsko pripravljeni klienti z urejenim pretakanjem in nadzorom zdravja
- **Večplatformna orodja**: Vzorci integracije LangChain/Semantic Kernel

### 🏢 Industrijske aplikacije
**Proizvodnja** • **Zdravstvo** • **Avtonomna vozila** • **Pametna mesta** • **Mobilne aplikacije**

## Hiter začetek

**Priporočena učna pot** (20-30 ur skupaj):

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + industrijski kontekst + učni okvir
1. **📚 Osnove** (Moduli 01-02): Koncepti EdgeAI + družine modelov SLM
2. **⚙️ Optimizacija** (Moduli 03-04): Implementacija + ogrodja za kvantizacijo  
3. **🚀 Produkcija** (Moduli 05-06): SLMOps + AI agenti + klici funkcij
4. **💻 Izvedba** (Moduli 07-08): Vzorci platform + orodja Foundry Local

Vsak modul vključuje teorijo, praktične vaje in produkcijsko pripravljene vzorce kode.

## Vpliv na kariero

**Tehnične vloge**: Arhitekt rešitve EdgeAI • Inženir ML (Edge) • IoT AI razvijalec • Mobilni AI razvijalec

**Industrijski sektorji**: Proizvodnja 4.0 • Zdravstvena tehnologija • Avtonomni sistemi • FinTech • Potrošniška elektronika

**Projekti v portfelju**: Večagentni sistemi • Produkcijske RAG aplikacije • Večplatformska implementacija • Optimizacija zmogljivosti

## Struktura repozitorija

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

## Poudarki tečaja

✅ **Postopno učenje**: Teorija → praksa → produkcijska izvedba  
✅ **Pravni primeri**: Microsoft, Japan Airlines, podjetniške implementacije  
✅ **Praktični vzorci**: 50+ primerov, 10 obsežnih demojev Foundry Local  
✅ **Usmerjenost na zmogljivost**: 85 % izboljšanje hitrosti, 75 % zmanjšanje velikosti  
✅ **Večplatformsko**: Windows, mobilno, embedded, oblak-rob hibrid  
✅ **Produkcijsko pripravljeno**: Nadzor, skaliranje, varnost, skladnost z okvirji

📖 **[Razpoložljivi študijski vodič](STUDY_GUIDE.md)**: Struktura 20-urne učne poti z navodili za časovno načrtovanje in orodja samoocenjevanja.

---

**EdgeAI predstavlja prihodnost izvedbe AI**: lokalno-prednostno, varovanje zasebnosti in učinkovito. Obvladaj te veščine za gradnjo naslednje generacije inteligentnih aplikacij.

## Drugi tečaji

Naša ekipa proizvaja tudi druge tečaje! Oglej si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za začetnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za začetnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain za začetnike](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD za začetnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za začetnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za začetnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agenti za začetnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Generative AI
[![Generative AI za začetnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Osnovno učenje
[![ML za začetnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Podatkovna znanost za začetnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za začetnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetska varnost za začetnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Spletni razvoj za začetnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za začetnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Razvoj XR za začetnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Iskanje pomoči

Če ste zataknjeni ali imate kakršnakoli vprašanja glede ustvarjanja AI aplikacij, se pridružite:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali napake med izdelavo, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatski prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem matičnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->