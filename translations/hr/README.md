# EdgeAI za Početnike 


![Course cover image](../../translated_images/hr/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Slijedite ove korake za početak korištenja ovih resursa:

1. **Forkajte repozitorij**: Kliknite [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonirajte repozitorij**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discord zajednici i upoznajte stručnjake i kolege developere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Višejezična Podrška

#### Podržano preko GitHub Akcije (Automatski i Uvijek Ažurirano)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](./README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Preferirate li kloniranje lokalno?**

> Ovaj repozitorij uključuje više od 50 prevoda na različite jezike što značajno povećava veličinu preuzimanja. Za kloniranje bez prijevoda koristite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ovo vam daje sve što trebate da završite tečaj s puno bržim preuzimanjem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ako želite dodatnu podršku za prijevode na drugim jezicima, popis podržanih jezika nalazi se [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Uvod

Dobrodošli u **EdgeAI za Početnike** – vaše sveobuhvatno putovanje u transformativni svijet Edge umjetne inteligencije. Ovaj tečaj premošćuje jaz između moćnih AI mogućnosti i praktične, stvarne primjene na edge uređajima, omogućujući vam da iskoristite potencijal AI-ja izravno tamo gdje se podaci generiraju i gdje je potrebno donositi odluke.

### Što ćete ovladati

Ovaj tečaj vodi vas od osnovnih pojmova do proizvodno spremnih implementacija, pokrivajući:
- **Male Jezične Modele (SLM)** optimizirane za edge implementaciju
- **Optimizaciju svjesnu hardvera** na raznolikim platformama
- **Realtimsku inferencu** s mogućnostima zaštite privatnosti
- **Strategije proizvodnog postavljanja** za korporativne aplikacije

### Zašto je EdgeAI važan

Edge AI predstavlja paradigmu koja odgovara na ključne moderne izazove:
- **Privatnost i sigurnost**: Obrada osjetljivih podataka lokalno bez izlaganja oblaku
- **Realtimske performanse**: Eliminacija mrežnog kašnjenja za aplikacije koje zahtijevaju trenutne odgovore
- **Učinkovitost troškova**: Smanjenje troškova propusnosti i računarstva u oblaku
- **Otpornost rada**: Održavanje funkcionalnosti tijekom prekida mreže
- **Zadovoljavanje regulativa**: Ispunjavanje zahtjeva za suverenitetom podataka

### Edge AI

Edge AI označava pokretanje AI algoritama i jezičnih modela lokalno na hardveru, blizu mjesta gdje se podaci generiraju, bez oslanjanja na oblačne resurse za inferencu. To smanjuje kašnjenje, povećava privatnost i omogućava donošenje odluka u stvarnom vremenu.

### Temeljna načela:
- **Inferenca na uređaju**: AI modeli se izvršavaju na edge uređajima (telefoni, ruteri, mikrokontroleri, industrijska računala)
- **Funkcioniranje offline**: Radi bez stalne internetske veze
- **Nisko kašnjenje**: Trenutni odgovori prikladni za sustave u stvarnom vremenu
- **Suverenitet podataka**: Čuva osjetljive podatke lokalno, poboljšavajući sigurnost i usklađenost

### Mali Jezični Modeli (SLM)

SLM-ovi poput Phi-4, Mistral-7B i Gemma su optimizirane verzije većih LLM-ova — trenirani ili destilirani za:
- **Smanjenu memorijsku potrošnju**: Efikasno korištenje ograničene memorije edge uređaja
- **Manju potrošnju računarske snage**: Optimizirani za performanse CPU-a i edge GPU-a
- **Brže vrijeme pokretanja**: Brza inicijalizacija za responzivne aplikacije

Oni otključavaju moćne NLP mogućnosti, uz poštivanje ograničenja:
- **Ugrađeni sustavi**: IoT uređaji i industrijski kontroleri
- **Mobilni uređaji**: Pametni telefoni i tableti s offline sposobnostima
- **IoT uređaji**: Senzori i pametni uređaji s ograničenim resursima
- **Edge serveri**: Lokalni procesni jedinice s ograničenim GPU resursima
- **Osobna računala**: Scenariji implementacije na desktop i prijenosnim računalima

## Moduli tečaja i navigacija

| Modul | Tema | Fokus područje | Ključni sadržaj | Razina | Trajanje |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod u EdgeAI](./introduction.md) | Osnove i kontekst | Pregled EdgeAI • Primjeri iz industrije • Uvod u SLM • Ciljevi učenja | Početnik | 1-2 sata |
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Usporedba Cloud i Edge AI | Osnove EdgeAI • Primjeri iz stvarnog svijeta • Vodič za implementaciju • Edge postavljanje | Početnik | 3-4 sata |
| [🧠 02](../../Module02) | [Osnove SLM Modela](./Module02/README.md) | Obitelji modela & arhitektura | Phi obitelj • Qwen obitelj • Gemma obitelj • BitNET • μModel • Phi-Silica | Početnik | 4-5 sati |
| [🚀 03](../../Module03) | [Praksa postavljanja SLM-a](./Module03/README.md) | Lokalno & cloud postavljanje | Napredna učenja • Lokalno okruženje • Cloud implementacija | Srednji | 4-5 sati |
| [⚙️ 04](../../Module04) | [Toolkit za optimizaciju modela](./Module04/README.md) | Optimizacija na više platformi | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza toka rada | Srednji | 5-6 sati |
| [🔧 05](../../Module05) | [SLMOps u proizvodnji](./Module05/README.md) | Proizvodne operacije | Uvod u SLMOps • Destilacija modela • Fine-tuning • Proizvodno postavljanje | Napredni | 5-6 sati |
| [🤖 06](../../Module06) | [AI agenti & pozivanje funkcija](./Module06/README.md) | Okviri agenata & MCP | Uvod u agente • Pozivanje funkcija • Protokol konteksta modela | Napredni | 4-5 sati |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Uzorci za više platformi | AI Toolkit • Foundry Local • Razvoj na Windowsu | Napredni | 3-4 sata |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Uzorci spremni za proizvodnju | Uzorci aplikacija (pogledajte detalje ispod) | Stručnjak | 8-10 sati |

### 🏭 **Modul 08: Uzorci aplikacija**

- [01: REST Chat Brzi početak](./Module08/samples/01/README.md)
- [02: OpenAI SDK integracija](./Module08/samples/02/README.md)
- [03: Otkriće modela i benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)
- [05: Orkestracija više agenata](./Module08/samples/05/README.md)
- [06: Usmjerivač modela kao alata](./Module08/samples/06/README.md)
- [07: Direktni API klijent](./Module08/samples/07/README.md)
- [08: Chat aplikacija za Windows 11](./Module08/samples/08/README.md)
- [09: Napredni sustav više agenata](./Module08/samples/09/README.md)
- [10: Foundry alatni okvir](./Module08/samples/10/README.md)

### 🎓 **Radionica: Praktični put učenja**

Sveobuhvatni materijali za praktične radionice s proizvodno spremnim implementacijama:

- **[Vodič kroz radionicu](./Workshop/Readme.md)** - Potpuni ciljevi učenja, ishodi i navigacija resursima
- **Python uzorci** (6 sesija) - Ažurirani s najboljim praksama, rukovanjem pogreškama i opširnom dokumentacijom
- **Jupyter bilježnice** (8 interaktivnih) - Tutorijali korak po korak s mjerama i praćenjem performansi
- **Vodiči za sesije** - Detaljni markdown vodiči za svaku radionicu
- **Alati za validaciju** - Skripte za provjeru kvalitete koda i provođenje smoke testova

**Što ćete izgraditi:**
- Lokalne AI chat aplikacije s podrškom za streaming
- RAG pipeline-e s evaluacijom kvalitete (RAGAS)
- Alate za benchmark i usporedbu više modela
- Sustave orkestracije više agenata
- Inteligentno usmjeravanje modela s odabirom na temelju zadataka

### 🎙️ **Radionica za Agentic: Praktično - AI Podcast Studio**

Izgradite proizvodni pipeline za podcast pokretan AI-jem od nule! Ova imerzivna radionica vas uči kako kreirati kompletan sustav više agenata koji pretvara ideje u profesionalne epizode podcasta.
**[🎬 Pokreni radionicu AI Podcast Studija](./WorkshopForAgentic/README.md)**

**Tvoj zadatak**: Pokreni "Future Bytes" — tech podcast koji u potpunosti pokreću AI agenti koje ćeš sam izgraditi. Bez ovisnosti o oblaku, bez troškova API-ja — sve radi lokalno na tvom računalu.

**Što ovo čini jedinstvenim:**
- **🤖 Prava višestruka orkestracija agenata** - Izgradi specijalizirane AI agente koji istražuju, pišu i produciraju zvuk
- **🎯 Potpuni produkcijski tijek** - Od izbora teme do konačnog audio zapisa podcasta
- **💻 100% lokalno izvođenje** - Koristi Ollamu i lokalne modele (Qwen-3-8B) za potpunu privatnost i kontrolu
- **🎤 Integracija pretvorbe teksta u govor** - Pretvori skripte u prirodne višegovorne razgovore
- **✋ Radni tokovi s ljudskom kontrolom** - Kapije za odobrenje osiguravaju kvalitetu uz automatizaciju

**Učenje u tri čina:**

| Čin | Fokus | Ključne vještine | Trajanje |
|-----|-------|------------|----------|
| **[Čin 1: Upoznaj svoje AI asistente](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Izgradi svog prvog AI agenta | Integracija alata • Pretraživanje weba • Rješavanje problema • Agentno razmišljanje | 2-3 sata |
| **[Čin 2: Sastavi svoj produkcijski tim](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestriraj više agenata | Koordinacija tima • Radni tokovi odobrenja • DevUI sučelje • Ljudski nadzor | 3-4 sata |
| **[Čin 3: Oživi svoj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generiraj audio podcasta | Pretvorba teksta u govor • Sinteza višegovornosti • Dugi audio zapisi • Potpuna automatizacija | 2-3 sata |

**Korištene tehnologije:**
- **Microsoft Agent Framework** - Orkestracija i koordinacija višestrukih agenata
- **Ollama** - Lokalno izvođenje AI modela (bez potrebe za oblakom)
- **Qwen-3-8B** - Open-source jezični model optimiziran za agentne zadatke
- **API-ji za pretvorbu teksta u govor** - Prirodna sinteza glasa za generiranje podcasta

**Podrška hardvera:**
- ✅ **Način rada na CPU-u** - Radi na bilo kojem modernom računalu (preporučeno 8GB+ RAM)
- 🚀 **GPU ubrzanje** - Značajno brže izvođenje sa NVIDIA/AMD grafičkim karticama
- ⚡ **Podrška za NPU** - Ubrzanje sljedeće generacije neuronskih procesorskih jedinica

**Savršeno za:**
- Programere koji uče sustave višestrukih AI agenata
- Svakoga zainteresiranog za AI automatizaciju i radne tokove
- Kreatore sadržaja koji istražuju AI-pomoćenu produkciju
- Studente koji proučavaju praktične uzorke AI orkestracije

**Počni graditi**: [🎙️ Radionica AI Podcast Studija →](./WorkshopForAgentic/README.md)

### 📊 **Sažetak puta učenja**
- **Ukupno trajanje**: 36-45 sati
- **Put za početnike**: Moduli 01-02 (7-9 sati)  
- **Srednji put**: Moduli 03-04 (9-11 sati)
- **Napredni put**: Moduli 05-07 (12-15 sati)
- **Put za eksperte**: Modul 08 (8-10 sati)

## Što ćeš izgraditi

### 🎯 Temeljne kompetencije
- **Edge AI arhitektura**: Dizajniraj AI sustave s pristupom prvenstveno lokalnom izvođenju, a s integracijom oblaka
- **Optimizacija modela**: Kvantizacija i kompresija modela za izvođenje na rubu (85% ubrzanje, 75% smanjenje veličine)
- **Višestruka platforma**: Windows, mobilno, ugrađeno i hibridni sustavi oblak-rub
- **Produkcijske operacije**: Praćenje, skaliranje i održavanje Edge AI u produkciji

### 🏗️ Praktični projekti
- **Foundry Local chat aplikacije**: Izvorna Windows 11 aplikacija s mogućnošću mijenjanja modela
- **Sustavi s više agenata**: Koordinator s specijaliziranim agentima za složene radne tokove  
- **RAG aplikacije**: Lokalna obrada dokumenata s vektorskim pretraživanjem
- **Ruter modela**: Inteligentni odabir modela temeljen na analizi zadataka
- **API okviri**: Klijenti spremni za produkciju sa streamingom i nadzorom zdravlja
- **Alati za više platformi**: Uzorci integracija LangChain/Semantic Kernel

### 🏢 Industrijske primjene
**Proizvodnja** • **Zdravstvo** • **Autonomna vozila** • **Pametni gradovi** • **Mobilne aplikacije**

## Brzi početak

**Preporučeni put učenja** (ukupno 20-30 sati):

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + kontekst industrije + okvir za učenje
1. **📚 Osnove** (Moduli 01-02): Pojmovi EdgeAI + SLM obitelji modela
2. **⚙️ Optimizacija** (Moduli 03-04): Izvođenje + kvantizacijski okviri  
3. **🚀 Produkcija** (Moduli 05-06): SLMOps + AI agenti + pozivanje funkcija
4. **💻 Implementacija** (Moduli 07-08): Primjeri platforme + Foundry Local alatni paket

Svaki modul uključuje teoriju, praktične vježbe i produkcijski spremne primjere koda.

## Utjecaj na karijeru

**Tehničke uloge**: Arhitekt EdgeAI rješenja • Inženjer strojnog učenja (Edge) • IoT AI programer • Mobilni AI programer

**Industrijski sektori**: Proizvodnja 4.0 • Zdravstvena tehnologija • Autonomni sustavi • FinTech • Potrošačka elektronika

**Projekti za portfolio**: Sustavi s više agenata • RAG proizvodne aplikacije • Izvođenje na više platformi • Optimizacija performansi

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

## Istaknuti dijelovi tečaja

✅ **Postepeno učenje**: Teorija → praksa → produkcijsko izvođenje  
✅ **Pravi studiji slučaja**: Microsoft, Japan Airlines, implementacije u poduzećima  
✅ **Praktični primjeri**: 50+ primjera, 10 sveobuhvatnih Foundry Local demo aplikacija  
✅ **Fokus na performanse**: 85% poboljšanja brzine, 75% smanjenja veličine  
✅ **Višeplatformski pristup**: Windows, mobilno, ugrađeno, hibrid oblak-rub  
✅ **Spremno za proizvodnju**: Praćenje, skaliranje, sigurnosni i usklađeni okviri

📖 **[Dostupan vodič za učenje](STUDY_GUIDE.md)**: Strukturiran put učenja od 20 sati s uputama za raspored vremena i alatima za samoprocjenu.

---

**EdgeAI predstavlja budućnost AI izvođenja**: s fokusom na lokalno izvođenje, očuvanje privatnosti i efikasnost. Ovladavaj ovim vještinama da izgradiš sljedeću generaciju inteligentnih aplikacija.

## Ostali tečajevi

Naš tim stvara i druge tečajeve! Pogledaj:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za početnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za početnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain za početnike](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD za početnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za početnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za početnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti za početnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Generativnog AI
[![Generativni AI za početnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativni AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativni AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativni AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Temeljno učenje
[![ML za početnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science za početnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za početnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity za početnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web razvoj za početnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za početnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR razvoj za početnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot  

[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Dobivanje pomoći

Ako zapnete ili imate bilo kakvih pitanja o izradi AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili pogreške tijekom izrade, posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->