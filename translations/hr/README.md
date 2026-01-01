<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T12:30:34+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# EdgeAI za početnike 


![Slika naslovnice tečaja](../../translated_images/cover.eb18d1b9605d754b.hr.png)

[![Suradnici na GitHubu](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problemi na GitHubu](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Zahtjevi za povlačenje na GitHubu](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR-ovi dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Pratitelji na GitHubu](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forkovi na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Zvjezdice na GitHubu](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Slijedite ove korake da biste započeli s korištenjem ovih resursa:

1. **Forkajte Repozitorij**: Kliknite [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonirajte Repozitorij**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discordu i upoznajte stručnjake i kolege programere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Višejezična podrška

#### Podržano putem GitHub Action (Automatski & Uvijek ažurno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](./README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ako želite da budu podržani dodatni jezici za prijevod, popis je naveden [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Uvod

Dobrodošli u **EdgeAI za početnike** – vaše sveobuhvatno putovanje u transformativni svijet rubne (Edge) umjetne inteligencije. Ovaj tečaj premošćuje jaz između moćnih AI mogućnosti i praktičnog, stvarnog uvođenja na rubne uređaje, osnažujući vas da iskoristite potencijal AI-ja izravno tamo gdje se podaci generiraju i gdje je potrebno donositi odluke.

### Što ćete savladati

Ovaj tečaj vodi vas od temeljnih pojmova do implementacija spremnih za proizvodnju, pokrivajući:
- **Mali jezični modeli (SLM-ovi)** optimizirani za deploy na rubu
- **Optimizaciju svjesnu hardvera** preko različitih platformi
- **Inferencu u stvarnom vremenu** s mogućnostima očuvanja privatnosti
- **Strategije za deploy u produkciju** za enterprise aplikacije

### Zašto je EdgeAI važan

Edge AI predstavlja pomak paradigme koji rješava ključne suvremene izazove:
- **Privatnost i sigurnost**: Obrada osjetljivih podataka lokalno bez izlaganja oblaku
- **Performanse u stvarnom vremenu**: Uklanjanje mrežnog kašnjenja za aplikacije kojima vrijeme reagiranja igra ključnu ulogu
- **Učinkovitost troškova**: Smanjenje troškova propusnosti i obrade u oblaku
- **Otpornost operacija**: Održavanje funkcionalnosti tijekom prekida mreže
- **Usklađenost s propisima**: Zadovoljavanje zahtjeva o suverenitetu podataka

### Edge AI

Edge AI odnosi se na pokretanje AI algoritama i jezičnih modela lokalno na hardveru, blizu mjesta gdje se podaci generiraju, bez oslanjanja na oblačne resurse za inferencu. Smanjuje latenciju, poboljšava privatnost i omogućuje donošenje odluka u stvarnom vremenu.

### Temeljna načela:
- **Inferenca na uređaju**: AI modeli rade na edge uređajima (telefoni, ruteri, mikrokontroleri, industrijska računala)
- **Mogućnost rada offline**: Funkcionira bez stalne internetske veze
- **Niska latencija**: Trenutni odgovori pogodni za sustave u stvarnom vremenu
- **Suverenitet podataka**: Osjetljivi podaci ostaju lokalno, poboljšavajući sigurnost i usklađenost

### Mali jezični modeli (SLM-ovi)

SLM-ovi poput Phi-4, Mistral-7B i Gemma su optimizirane verzije većih LLM-ova—trenirane ili destilirane za:
- **Smanjeni memorijski otisak**: Učinkovito korištenje ograničene memorije edge uređaja
- **Niže zahtjeve za računanjem**: Optimizirano za CPU i edge GPU performanse
- **Brže vrijeme pokretanja**: Brza inicijalizacija za responzivne aplikacije

Oni otključavaju moćne NLP mogućnosti dok zadovoljavaju ograničenja:
- **Ugrađeni sustavi**: IoT uređaji i industrijski kontroleri
- **Mobilni uređaji**: Pametni telefoni i tableti s mogućnostima rada offline
- **IoT uređaji**: Senzori i pametni uređaji s ograničenim resursima
- **Edge poslužitelji**: Lokalne jedinice za obradu s ograničenim GPU resursima
- **Osobna računala**: Scenariji deploya na stolnim i prijenosnim računalima

## Moduli tečaja & Navigacija

| Modul | Tema | Područje fokusa | Ključni sadržaj | Razina | Trajanje |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod u EdgeAI](./introduction.md) | Osnove & Kontekst | Pregled EdgeAI • Primjene u industriji • Uvod u SLM • Ciljevi učenja | Početnik | 1-2 sata |
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Usporedba Cloud vs Edge AI | Osnove EdgeAI • Studije slučaja iz stvarnog svijeta • Vodič za implementaciju • Edge implementacija | Početnik | 3-4 sata |
| [🧠 02](../../Module02) | [Osnove SLM modela](./Module02/README.md) | Obitelji modela & arhitektura | Phi obitelj • Qwen obitelj • Gemma obitelj • BitNET • μModel • Phi-Silica | Početnik | 4-5 sata |
| [🚀 03](../../Module03) | [Praksa deploya SLM-a](./Module03/README.md) | Lokalni & cloud deploy | Napredno učenje • Lokalno okruženje • Cloud deploy | Srednja razina | 4-5 sata |
| [⚙️ 04](../../Module04) | [Alatni kit za optimizaciju modela](./Module04/README.md) | Optimizacija za više platformi | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza radnih tokova | Srednja razina | 5-6 sata |
| [🔧 05](../../Module05) | [SLMOps u proizvodnji](./Module05/README.md) | Operacije u proizvodnji | Uvod u SLMOps • Distilacija modela • Fino podešavanje • Deploy u produkciji | Napredno | 5-6 sata |
| [🤖 06](../../Module06) | [AI agenti & Pozivanje funkcija](./Module06/README.md) | Okviri agenata & MCP | Uvod u agente • Pozivanje funkcija • Model Context Protocol | Napredno | 4-5 sata |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Primjeri za više platformi | AI alatni set • Foundry Local • Windows razvoj | Napredno | 3-4 sata |
| [🏭 08](../../Module08) | [Foundry Local alatni kit](./Module08/README.md) | Primjeri spremni za proizvodnju | Primjeri aplikacija (vidi detalje dolje) | Stručnjak | 8-10 sata |

### 🏭 **Modul 08: Primjeri Aplikacija**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Model Discovery & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Application](./Module08/samples/04/README.md)
- [05: Multi-Agent Orchestration](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Direct API Client](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Advanced Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Radionica: Praktični put učenja**

Sveobuhvatni materijali za praktičnu radionicu s implementacijama spremnim za produkciju:

- **[Vodič za radionicu](./Workshop/Readme.md)** - Potpuni ciljevi učenja, ishodi i navigacija resursima
- **Python primjeri** (6 sesija) - Ažurirano s najboljim praksama, rukovanjem greškama i sveobuhvatnom dokumentacijom
- **Jupyter bilježnice** (8 interaktivnih) - Korak-po-korak tutorijali s benchmarkovima i praćenjem performansi
- **Vodiči za sesije** - Detaljni markdown vodiči za svaku radionicu
- **Alati za provjeru** - Skripte za verificiranje kvalitete koda i izvođenje osnovnih testova

**Što ćete izgraditi:**
- Lokalne AI chat aplikacije s podrškom za streaming
- RAG pipelineove s evaluacijom kvalitete (RAGAS)
- Alate za benchmark i usporedbu više modela
- Sustave za orkestraciju više agenata
- Inteligentno usmjeravanje modela s odabirom prema zadatku

### 📊 **Sažetak puta učenja**
- **Ukupno trajanje**: 36-45 sati
- **Put za početnike**: Moduli 01-02 (7-9 sati)  
- **Srednji put**: Moduli 03-04 (9-11 sati)
- **Napredni put**: Moduli 05-07 (12-15 sati)
- **Stručni put**: Modul 08 (8-10 sati)

## Što ćete izgraditi

### 🎯 Ključne kompetencije
- **Edge AI arhitektura**: Dizajnirajte AI sustave koji su lokalno-prvo s integracijom oblaka
- **Optimizacija modela**: Kvantizacija i kompresija modela za implementaciju na rubnim uređajima (85% ubrzanje, 75% smanjenje veličine)
- **Višeplatformsko raspoređivanje**: Windows, mobilne, ugrađene i hibridni cloud-edge sustavi
- **Produkcijske operacije**: Nadgledavanje, skaliranje i održavanje AI na rubu u produkciji

### 🏗️ Praktični projekti
- **Foundry Local Chat aplikacije**: nativna aplikacija za Windows 11 s prebacivanjem modela
- **Sistemi s više agenata**: Koordinator sa specijaliziranim agentima za složene tokove rada  
- **RAG aplikacije**: Lokalna obrada dokumenata s vektorskom pretragom
- **Usmjerivači modela**: Inteligentni odabir među modelima temeljen na analizi zadatka
- **API okviri**: Klijenti spremni za produkciju s streamingom i nadzorom zdravlja
- **Alati za više platformi**: Obrasci integracije LangChain/Semantic Kernel

### 🏢 Industrijske primjene
**Proizvodnja** • **Zdravstvo** • **Autonomna vozila** • **Pametni gradovi** • **Mobilne aplikacije**

## Brzi početak

**Preporučeni put učenja** (20–30 sati ukupno):

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + industrijski kontekst + okvir za učenje
1. **📚 Osnove** (Moduli 01-02): Koncepti EdgeAI + obitelji SLM modela
2. **⚙️ Optimizacija** (Moduli 03-04): Raspoređivanje + okviri za kvantizaciju  
3. **🚀 Produkcija** (Moduli 05-06): SLMOps + AI agenti + pozivanje funkcija
4. **💻 Implementacija** (Moduli 07-08): Primjeri platformi + Foundry Local alatni paket

Svaki modul uključuje teoriju, praktične vježbe i uzorke koda spremne za produkciju.

## Utjecaj na karijeru

**Tehničke uloge**: Arhitekt rješenja za EdgeAI • Inženjer strojnog učenja (Edge) • Razvijač AI za IoT • Razvijač AI za mobilne uređaje

**Industrijske grane**: Proizvodnja 4.0 • Zdravstvena tehnologija • Autonomni sustavi • FinTech • Potrošačka elektronika

**Projekti za portfolio**: Sustavi s više agenata • Produkcijske RAG aplikacije • Višeplatformsko raspoređivanje • Optimizacija performansi

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

## Istaknuto u tečaju

✅ **Postupno učenje**: Teorija → Praksa → Produkcijsko raspoređivanje  
✅ **Studije stvarnih slučajeva**: Microsoft, Japan Airlines, implementacije u poduzećima  
✅ **Praktični primjeri**: 50+ primjera, 10 iscrpnih Foundry Local demoa  
✅ **Usmjerenost na performanse**: 85% poboljšanje brzine, 75% smanjenje veličine  
✅ **Višeplatformsko**: Windows, mobilno, ugrađeno, cloud-edge hibrid  
✅ **Spremno za produkciju**: Okviri za nadgledanje, skaliranje, sigurnost i usklađenost

📖 **[Dostupan vodič za učenje](STUDY_GUIDE.md)**: Strukturirani 20-satni put učenja s uputama za raspodjelu vremena i alatima za samoocjenu.

---

**EdgeAI predstavlja budućnost implementacije AI-a**: prvenstveno lokalno, uz očuvanje privatnosti i učinkovitost. Savladajte ove vještine kako biste izgradili sljedeću generaciju inteligentnih aplikacija.

## Ostali tečajevi

Naš tim proizvodi i druge tečajeve! Pogledajte:

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
 
### Serija Generativne AI
[![Generativna AI za početnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Temeljno učenje
[![Strojno učenje za početnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Znanost o podacima za početnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za početnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetička sigurnost za početnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web razvoj za početnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za početnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR razvoj za početnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot
[![Copilot za AI parno programiranje](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot za C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Avantura](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Dobivanje pomoći

Ako zapnete ili imate pitanja o izgradnji AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili pogreške tijekom izrade posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Odricanje odgovornosti:
Ovaj dokument preveden je pomoću AI prevoditeljske usluge Co-op Translator (https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se angažiranje profesionalnog prevoditelja. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz upotrebe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->