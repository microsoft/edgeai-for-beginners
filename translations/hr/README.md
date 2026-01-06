<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T10:01:59+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# EdgeAI za početnike 


![Naslovna slika tečaja](../../translated_images/cover.eb18d1b9605d754b.hr.png)

[![GitHub suradnici](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub prijavljene greške](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub zahtjevi za povlačenje](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub promatrači](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forkovi](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub zvjezdice](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Slijedite ove korake za početak korištenja ovih resursa:

1. **Forkajte spremište**: Kliknite [![GitHub forkovi](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Kloni spremište**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discordu i upoznajte stručnjake i kolege programere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Višejezična podrška

#### Podržano putem GitHub akcije (automatizirano i uvijek ažurirano)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arapski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bugarski](../bg/README.md) | [Burmanski (Myanmar)](../my/README.md) | [Kineski (Pojednostavljeni)](../zh/README.md) | [Kineski (Tradicionalni, Hong Kong)](../hk/README.md) | [Kineski (Tradicionalni, Makao)](../mo/README.md) | [Kineski (Tradicionalni, Tajvan)](../tw/README.md) | [Hrvatski](./README.md) | [Češki](../cs/README.md) | [Danski](../da/README.md) | [Nizozemski](../nl/README.md) | [Estonski](../et/README.md) | [Finski](../fi/README.md) | [Francuski](../fr/README.md) | [Njemački](../de/README.md) | [Grčki](../el/README.md) | [Hebrejski](../he/README.md) | [Hindski](../hi/README.md) | [Mađarski](../hu/README.md) | [Indonezijski](../id/README.md) | [Talijanski](../it/README.md) | [Japanski](../ja/README.md) | [Kannada](../kn/README.md) | [Korejski](../ko/README.md) | [Litvanski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalamski](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigerijski pidžin](../pcm/README.md) | [Norveški](../no/README.md) | [Perzijski (Farsi)](../fa/README.md) | [Poljski](../pl/README.md) | [Portugalski (Brazil)](../br/README.md) | [Portugalski (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumunjski](../ro/README.md) | [Ruski](../ru/README.md) | [Srpski (Ćirilica)](../sr/README.md) | [Slovački](../sk/README.md) | [Slovenski](../sl/README.md) | [Španjolski](../es/README.md) | [Svahili](../sw/README.md) | [Švedski](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tajlandski](../th/README.md) | [Turski](../tr/README.md) | [Ukrajinski](../uk/README.md) | [Urdu](../ur/README.md) | [Vijetnamski](../vi/README.md)

> **Radije klonirati lokalno?**

> Ovo spremište uključuje prijevode na više od 50 jezika što bitno povećava veličinu preuzimanja. Za kloniranje bez prijevoda, koristite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ovo vam daje sve što vam treba za dovršetak tečaja s mnogo bržim preuzimanjem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ako želite dodatne podržane prijevodne jezike oni su navedeni [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Uvod

Dobrodošli u **EdgeAI za početnike** – vaše sveobuhvatno putovanje u transformativni svijet Edge umjetne inteligencije. Ovaj tečaj premošćuje jaz između moćnih AI mogućnosti i praktične, stvarne implementacije na edge uređajima, omogućujući vam da iskoristite potencijal AI-a izravno tamo gdje se podaci generiraju i gdje je potrebno donositi odluke.

### Što ćete savladati

Ovaj tečaj vodi vas od osnovnih pojmova do implementacija spremnih za proizvodnju, uključujući:
- **Mali jezični modeli (SLM-ovi)** optimizirani za edge implementaciju
- **Optimizacija svjesna hardvera** na različitim platformama
- **Računanje u stvarnom vremenu** s mogućnostima očuvanja privatnosti
- **Strategije implementacije u proizvodnju** za poslovne aplikacije

### Zašto je EdgeAI važan

Edge AI predstavlja paradigmu koja rješava ključne suvremene izazove:
- **Privatnost i sigurnost**: Obrada osjetljivih podataka lokalno bez izlaganja oblaku
- **Performanse u stvarnom vremenu**: Uklanja kašnjenje mreže za aplikacije osjetljive na vrijeme
- **Isplativost**: Smanjuje troškove propusnosti i računalstva u oblaku
- **Otpornost u radu**: Održava funkcionalnost tijekom prekida mreže
- **Usuglašenost s regulativama**: Zadovoljava zahtjeve suvereniteta podataka

### Edge AI

Edge AI odnosi se na izvođenje AI algoritama i jezičnih modela lokalno na hardveru, blizu mjesta gdje se podaci generiraju, bez oslanjanja na oblačne resurse za izvođenje. Smanjuje kašnjenje, povećava privatnost i omogućuje donošenje odluka u stvarnom vremenu.

### Temeljna načela:
- **Izvođenje modela na uređaju**: AI modeli rade na edge uređajima (telefoni, usmjerivači, mikrokontroleri, industrijska računala)
- **Mogućnost rada bez mreže**: Funkcionira bez stalne internetske veze
- **Nisko kašnjenje**: Trenutni odgovori prikladni za sustave u stvarnom vremenu
- **Suverenitet podataka**: Drži osjetljive podatke lokalno, poboljšavajući sigurnost i usklađenost

### Mali jezični modeli (SLM-ovi)

SLM-ovi poput Phi-4, Mistral-7B i Gemma su optimizirane verzije većih LLM-ova — trenirani ili destilirani za:
- **Smanjeni memorijski otisak**: Efikasno korištenje ograničene memorije edge uređaja
- **Smanjene zahtjeve za procesorskom snagom**: Optimizirani za CPU i edge GPU performanse
- **Brža vrijeme pokretanja**: Brzo inicijaliziranje za responzivne aplikacije

Oni omogućuju moćne NLP mogućnosti uz poštivanje ograničenja:
- **Ugrađeni sustavi**: IoT uređaji i industrijski kontroleri
- **Mobilni uređaji**: Pametni telefoni i tableti s mogućnošću rada offline
- **IoT uređaji**: Senzori i pametni uređaji s ograničenim resursima
- **Edge serveri**: Lokalni procesorski uređaji s ograničenim GPU resursima
- **Osobna računala**: Scenariji implementacije na stolnim i prijenosnim računalima

## Moduli tečaja i navigacija

| Modul | Tema | Fokus područje | Ključni sadržaj | Razina | Trajanje |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod u EdgeAI](./introduction.md) | Osnove i kontekst | Pregled EdgeAI • Industrijske primjene • Uvod u SLM • Ciljevi učenja | Početnik | 1-2 sata |
| [📚 01](../../Module01) | [Temeljni pojmovi EdgeAI](./Module01/README.md) | Usporedba Clouda i Edge AI | Osnove EdgeAI • Studije slučaja iz stvarnog svijeta • Vodič za implementaciju • Edge implementacija | Početnik | 3-4 sata |
| [🧠 02](../../Module02) | [Temelji SLM modela](./Module02/README.md) | Obitelji modela i arhitektura | Phi obitelj • Qwen obitelj • Gemma obitelj • BitNET • μModel • Phi-Silica | Početnik | 4-5 sati |
| [🚀 03](../../Module03) | [Praksa implementacije SLM](./Module03/README.md) | Lokalna i cloud implementacija | Napredno učenje • Lokalno okruženje • Cloud implementacija | Srednja | 4-5 sati |
| [⚙️ 04](../../Module04) | [Alatni paket za optimizaciju modela](./Module04/README.md) | Optimizacija na više platformi | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sintetiziranje tijeka rada | Srednja | 5-6 sati |
| [🔧 05](../../Module05) | [SLMOps u produkciji](./Module05/README.md) | Operacije u produkciji | Uvod u SLMOps • Destilacija modela • Fino podešavanje • Implementacija u produkciju | Napredno | 5-6 sati |
| [🤖 06](../../Module06) | [AI agenti i pozivanje funkcija](./Module06/README.md) | Okviri za agente i MCP | Uvod u agente • Pozivanje funkcija • Protokol model konteksta | Napredno | 4-5 sati |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Primjeri za više platformi | AI alatni paket • Foundry Local • Windows razvoj | Napredno | 3-4 sata |
| [🏭 08](../../Module08) | [Foundry lokalni alatni paket](./Module08/README.md) | Primjeri spremni za produkciju | Primjer aplikacija (pogledajte detalje dolje) | Stručnjak | 8-10 sati |

### 🏭 **Modul 08: Primjer aplikacija**

- [01: Brzi početak REST Chat](./Module08/samples/01/README.md)
- [02: Integracija OpenAI SDK](./Module08/samples/02/README.md)
- [03: Otkriće modela & benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)
- [05: Orkestracija više agenata](./Module08/samples/05/README.md)
- [06: Modeli-kao-alati usmjerivač](./Module08/samples/06/README.md)
- [07: Direktni API klijent](./Module08/samples/07/README.md)
- [08: Windows 11 Chat aplikacija](./Module08/samples/08/README.md)
- [09: Napredni sustav više agenata](./Module08/samples/09/README.md)
- [10: Foundry alatni okvir](./Module08/samples/10/README.md)

### 🎓 **Radionica: Put učenje kroz praktičan rad**

Sveobuhvatni materijali radionice s implementacijama spremnim za produkciju:

- **[Vodič radionice](./Workshop/Readme.md)** - Potpuni ciljevi učenja, ishodi i navigacija resursa
- **Python primjeri** (6 sesija) - Ažurirani s najboljim praksama, rukovanjem pogreškama i opširnom dokumentacijom
- **Jupyter bilježnice** (8 interaktivnih) - Korak-po-korak vodiči s benchmark testovima i praćenjem performansi
- **Vodiči za sesije** - Detaljni markdown vodiči za svaku sesiju radionice
- **Alati za validaciju** - Skripte za provjeru kvalitete koda i pokretanje osnovnih testova

**Što ćete izgraditi:**
- Lokalne AI chat aplikacije s podrškom za streaming
- RAG pipelineove s procjenom kvalitete (RAGAS)
- Alate za benchmark i usporedbu više modela
- Sustave orkestracije više agenata
- Inteligentno usmjeravanje modela po zadatcima

### 🎙️ **Radionica za Agentic: Praktično - AI podcast studio**

Izgradite pipeline za produkciju podcasta pokretan AI-jem od nule! Ova interaktivna radionica uči vas kako stvoriti kompletan sustav više agenata koji pretvara ideje u profesionalne epizode podcasta.
**[🎬 Započni radionicu AI Podcast Studija](./WorkshopForAgentic/README.md)**

**Tvoja misija**: Pokreni "Future Bytes" — tech podcast u potpunosti pokretan AI agentima koje ćeš sam izraditi. Bez ovisnosti o oblaku, bez troškova API-ja — sve se pokreće lokalno na tvom računalu.

**Što ovo čini jedinstvenim:**
- **🤖 Prava orkestracija više agenata** - Izradi specijalizirane AI agente koji istražuju, pišu i proizvode audio
- **🎯 Potpuni produkcijski lanac** - Od odabira teme do konačnog audio zapisa podcasta
- **💻 100% lokalna implementacija** - Koristi Ollama i lokalne modele (Qwen-3-8B) za potpunu privatnost i kontrolu
- **🎤 Integracija pretvaranja teksta u govor** - Pretvori skripte u prirodno zvučeće razgovore s više govornika
- **✋ Radni procesi s uključenim čovjekom** - Vrata odobrenja osiguravaju kvalitetu dok održavaju automatizaciju

**Učenje u tri čina:**

| Čin | Fokus | Ključne vještine | Trajanje |
|-----|-------|-----------------|---------|
| **[Čin 1: Upoznaj svoje AI asistente](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Izradi svog prvog AI agenta | Integracija alata • Pretraživanje weba • Rješavanje problema • Agentičko rezoniranje | 2-3 sata |
| **[Čin 2: Sastavi svoj produkcijski tim](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestriraj više agenata | Koordinacija tima • Radni procesi odobrenja • DevUI sučelje • Nadzor ljudi | 3-4 sata |
| **[Čin 3: Oživi svoj podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generiraj audio podcasta | Pretvaranje teksta u govor • Sinteza multi-govornika • Dugi audio • Potpuna automatizacija | 2-3 sata |

**Korištene tehnologije:**
- **Microsoft Agent Framework** - Orkestracija i koordinacija više agenata
- **Ollama** - Lokalno okruženje za AI modele (bez oblačne povezanosti)
- **Qwen-3-8B** - Open-source jezični model optimiziran za agente
- **API-ji za tekst u govor** - Prirodna sinteza glasa za generiranje podcasta

**Podrška hardvera:**
- ✅ **CPU način rada** - Radi na bilo kojem modernom računalu (preporučeno 8GB+ RAM-a)
- 🚀 **GPU ubrzanje** - Znatno brža inferencija s NVIDIA/AMD GPU-ima
- ⚡ **NPU podrška** - Ubrzanje sljedeće generacije neuronskih procesora

**Idealno za:**
- Programere koji uče sustave s više AI agenata
- Sve zainteresirane za AI automatizaciju i radne procese
- Kreatore sadržaja koji istražuju AI-podržanu produkciju
- Studente koji proučavaju praktične obrasce AI orkestracije

**Započni izgradnju**: [🎙️ Radionica AI Podcast Studija →](./WorkshopForAgentic/README.md)

### 📊 **Sažetak puta učenja**
- **Ukupno trajanje**: 36-45 sati
- **Put za početnike**: Moduli 01-02 (7-9 sati)  
- **Srednji put**: Moduli 03-04 (9-11 sati)
- **Napredni put**: Moduli 05-07 (12-15 sati)
- **Ekspertni put**: Modul 08 (8-10 sati)

## Što ćeš izgraditi

### 🎯 Ključne kompetencije
- **Edge AI arhitektura**: Dizajniraj lokalno-prvo AI sustave s integracijom oblaka
- **Optimizacija modela**: Kvantizacija i kompresija modela za edge implementaciju (85% ubrzanje, 75% smanjenje veličine)
- **Višeplatformska implementacija**: Windows, mobilno, ugrađeni sustavi i hibridni cloud-edge sustavi
- **Operacije produkcije**: Praćenje, skaliranje i održavanje edge AI-a u produkciji

### 🏗️ Praktični projekti
- **Foundry lokalne chat aplikacije**: Windows 11 nativna aplikacija s mijenjanjem modela
- **Sustavi s više agenata**: Koordinator sa specijalističkim agentima za složene radne tokove  
- **RAG aplikacije**: Lokalna obrada dokumenata sa vektorskim pretraživanjem
- **Preusmjerivači modela**: Inteligentan odabir između modela temeljen na analizi zadataka
- **API okviri**: Klijenti spremni za produkciju s podrškom za streaming i nadzor zdravlja
- **Višeplatformski alati**: Obrasci integracije LangChain/Semantic Kernel

### 🏢 Industrijske primjene
**Proizvodnja** • **Zdravstvo** • **Autonomna vozila** • **Pametni gradovi** • **Mobilne aplikacije**

## Brzi početak

**Preporučeni put učenja** (ukupno 20-30 sati):

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + industrijski kontekst + okviri učenja
1. **📚 Osnove** (moduli 01-02): Koncepti EdgeAI + SLM obitelji modela
2. **⚙️ Optimizacija** (moduli 03-04): Implementacija + kvantizacijski okviri  
3. **🚀 Produkcija** (moduli 05-06): SLMOps + AI agenti + pozivi funkcija
4. **💻 Implementacija** (moduli 07-08): Primjeri platformi + Foundry Local alatni set

Svaki modul sadrži teoriju, praktične vježbe i kod spreman za produkciju.

## Karijerni utjecaj

**Tehničke uloge**: EdgeAI arhitekt rješenja • ML inženjer (Edge) • IoT AI programer • Mobilni AI programer

**Industrijski sektori**: Proizvodnja 4.0 • Zdravstvena tehnologija • Autonomni sustavi • FinTech • Potrošačka elektronika

**Projekti za portfelj**: Sustavi s više agenata • Produkcijske RAG aplikacije • Višeplatformska implementacija • Optimizacija performansi

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

## Istaknuto iz tečaja

✅ **Postupno učenje**: Teorija → Praksa → Produkcijska implementacija  
✅ **Pravi primjeri**: Microsoft, Japan Airlines, implementacije u poduzećima  
✅ **Praktični primjeri**: 50+ primjera, 10 cjelovitih Foundry Local demonstracija  
✅ **Fokus na performanse**: 85% poboljšanja brzine, 75% smanjenje veličine  
✅ **Višeplatformski**: Windows, mobilno, ugrađeno, hibrid cloud-edge  
✅ **Spremno za produkciju**: Praćenje, skaliranje, sigurnost, okvir za usklađenost

📖 **[Dostupan vodič za učenje](STUDY_GUIDE.md)**: Strukturirani 20-satni plan učenja s vodstvom za raspodjelu vremena i alatima za samoocjenu.

---

**EdgeAI predstavlja budućnost AI implementacije**: lokalno-prvo, čuvanje privatnosti i učinkovito. Ovladavanjem ovim vještinama izgradi sljedeću generaciju inteligentnih aplikacija.

## Ostali tečajevi

Naš tim proizvodi i druge tečajeve! Pogledaj:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za početnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za početnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD za početnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za početnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za početnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti za početnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativna AI serija
[![Generative AI za početnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Osnovno učenje
[![ML za početnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science za početnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za početnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity za početnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web razvoj za početnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za početnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR razvoj za početnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot
[![Copilot za AI programsko sparivanje](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Dobivanje pomoći

Ako zapnete ili imate pitanja o izradi AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili prijavite greške tijekom izrade, posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo biti točni, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->