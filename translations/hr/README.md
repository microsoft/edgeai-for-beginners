<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8de8ce76af1af156b1c2dee24ed23b0",
  "translation_date": "2025-12-25T01:19:43+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# EdgeAI za početnike 


![Slika naslovnice tečaja](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.hr.png)

[![Doprinosi na GitHubu](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problemi na GitHubu](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull zahtjevi na GitHubu](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR-ovi dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Pratitelji na GitHubu](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forkovi na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Zvijezde na GitHubu](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Slijedite ove korake da započnete s korištenjem ovih resursa:

1. **Forkajte spremište**: Kliknite [![Forkovi na GitHubu](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonirajte spremište**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discordu i upoznajte stručnjake i kolege programere**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Podrška za više jezika

#### Podržano putem GitHub Action (automatski i uvijek ažurno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arapski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bugarski](../bg/README.md) | [Burmanski (Mjanmar)](../my/README.md) | [Kineski (pojednostavljeni)](../zh/README.md) | [Kineski (tradicionalni, Hong Kong)](../hk/README.md) | [Kineski (tradicionalni, Makao)](../mo/README.md) | [Kineski (tradicionalni, Tajvan)](../tw/README.md) | [Hrvatski](./README.md) | [Češki](../cs/README.md) | [Danski](../da/README.md) | [Nizozemski](../nl/README.md) | [Estonski](../et/README.md) | [Finski](../fi/README.md) | [Francuski](../fr/README.md) | [Njemački](../de/README.md) | [Grčki](../el/README.md) | [Hebrejski](../he/README.md) | [Hindski](../hi/README.md) | [Mađarski](../hu/README.md) | [Indonezijski](../id/README.md) | [Talijanski](../it/README.md) | [Japanski](../ja/README.md) | [Kannada](../kn/README.md) | [Korejski](../ko/README.md) | [Litvanski](../lt/README.md) | [Malajski](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigerijski Pidgin](../pcm/README.md) | [Norveški](../no/README.md) | [Perzijski (Farsi)](../fa/README.md) | [Poljski](../pl/README.md) | [Portugalski (Brazil)](../br/README.md) | [Portugalski (Portugal)](../pt/README.md) | [Pandžapski (Gurmukhi)](../pa/README.md) | [Rumunjski](../ro/README.md) | [Ruski](../ru/README.md) | [Srpski (ćirilica)](../sr/README.md) | [Slovački](../sk/README.md) | [Slovenski](../sl/README.md) | [Španjolski](../es/README.md) | [Svahilski](../sw/README.md) | [Švedski](../sv/README.md) | [Tagalog (Filipinski)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajlandski](../th/README.md) | [Turski](../tr/README.md) | [Ukrajinski](../uk/README.md) | [Urdu](../ur/README.md) | [Vijetnamski](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ako želite podršku za dodatne prevoditeljske jezike, oni su navedeni [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Uvod

Dobrodošli u **EdgeAI za početnike** – vaše cjelovito putovanje u transformativni svijet Edge umjetne inteligencije. Ovaj tečaj premošćuje jaz između snažnih AI mogućnosti i praktičnog, stvarnog izbacivanja na uređaje na rubu mreže, omogućujući vam da iskoristite potencijal AI-ja izravno tamo gdje se podaci generiraju i gdje se moraju donositi odluke.

### Što ćete savladati

Ovaj tečaj vodi vas od temeljnih koncepata do implementacija spremnih za produkciju, pokrivajući:
- **Mali jezični modeli (SLM-ovi)** optimizirani za Edge implementaciju
- **Optimizacija svjesna hardvera** na različitim platformama
- **Inferencija u stvarnom vremenu** s mogućnostima zaštite privatnosti
- **Strategije za produkcijsko postavljanje** za poslovne aplikacije

### Zašto je EdgeAI važan

Edge AI predstavlja pomak paradigme koji rješava ključne moderne izazove:
- **Privatnost i sigurnost**: Obradite osjetljive podatke lokalno bez izlaganja cloudu
- **Performanse u stvarnom vremenu**: Eliminirajte mrežnu latenciju za aplikacije koje zahtijevaju brz odgovor
- **Isplativost**: Smanjite troškove propusnosti i računarstva u cloudu
- **Otpoperativnost**: Održava funkcionalnost tijekom prekida veze
- **Usklađenost s propisima**: Zadovoljava zahtjeve suvereniteta podataka

### Edge AI

Edge AI odnosi se na pokretanje AI algoritama i jezičnih modela lokalno na hardveru, blizu mjesta gdje se podaci generiraju, bez oslanjanja na cloud resurse za inferenciju. Smanjuje latenciju, poboljšava privatnost i omogućuje donošenje odluka u stvarnom vremenu.

### Temeljna načela:
- **Inferencija na uređaju**: AI modeli se izvršavaju na Edge uređajima (telefoni, ruteri, mikrokontroleri, industrijska računala)
- **Mogućnost rada offline**: Funkcionira bez stalne internet veze
- **Niska latencija**: Trenutni odgovori prikladni za sustave u stvarnom vremenu
- **Suverenitet podataka**: Drži osjetljive podatke lokalno, poboljšavajući sigurnost i usklađenost

### Mali jezični modeli (SLM-ovi)

SLM-ovi poput Phi-4, Mistral-7B i Gemma su optimizirane verzije većih LLM-ova—trenirane ili distilirane za:
- **Smanjeni memorijski otisak**: Učinkovito korištenje ograničene memorije Edge uređaja
- **Niže zahtjeve za računanjem**: Optimizirani za CPU i Edge GPU performanse
- **Brže vrijeme pokretanja**: Brza inicijalizacija za responzivne aplikacije

Otključavaju snažne NLP mogućnosti dok zadovoljavaju ograničenja:
- **Ugrađeni sustavi**: IoT uređaji i industrijski kontroleri
- **Mobilni uređaji**: Pametni telefoni i tablet uređaji s mogućnostima rada offline
- **IoT uređaji**: Senzori i pametni uređaji s ograničenim resursima
- **Edge poslužitelji**: Lokalni procesorski čvorovi s ograničenim GPU resursima
- **Osobna računala**: Scenariji implementacije na stolnim i prijenosnim računalima

## Moduli tečaja i navigacija

| Modul | Tema | Područje fokusa | Ključni sadržaj | Razina | Trajanje |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod u EdgeAI](./introduction.md) | Osnove i kontekst | Pregled EdgeAI • Primjene u industriji • Uvod u SLM • Ciljevi učenja | Početnik | 1-2 sata |
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Usporedba oblaka i Edge AI | Osnove EdgeAI • Studije slučaja iz stvarnog svijeta • Vodič za implementaciju • Edge implementacija | Početnik | 3-4 sata |
| [🧠 02](../../Module02) | [Osnove SLM modela](./Module02/README.md) | Obitelji modela i arhitektura | Phi obitelj • Qwen obitelj • Gemma obitelj • BitNET • μModel • Phi-Silica | Početnik | 4-5 sata |
| [🚀 03](../../Module03) | [Praksa implementacije SLM-a](./Module03/README.md) | Lokalna i cloud implementacija | Napredno učenje • Lokalno okruženje • Cloud implementacija | Srednja razina | 4-5 sata |
| [⚙️ 04](../../Module04) | [Alat za optimizaciju modela](./Module04/README.md) | Optimizacija za više platformi | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sintetiziranje tijeka rada | Srednja razina | 5-6 sata |
| [🔧 05](../../Module05) | [SLMOps u produkciji](./Module05/README.md) | Operacije u produkciji | Uvod u SLMOps • Distilacija modela • Fino dorađivanje • Produkcijsko postavljanje | Napredno | 5-6 sata |
| [🤖 06](../../Module06) | [AI agenti i pozivanje funkcija](./Module06/README.md) | Okviri za agente i MCP | Uvod u agente • Pozivanje funkcija • Protokol konteksta modela | Napredno | 4-5 sata |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Primjeri za više platformi | AI alatni set • Foundry Local • Razvoj za Windows | Napredno | 3-4 sata |
| [🏭 08](../../Module08) | [Foundry Local alatni set](./Module08/README.md) | Primjeri spremni za produkciju | Primjeri aplikacija (pogledajte detalje dolje) | Stručnjak | 8-10 sati |

### 🏭 **Modul 08: Primjeri aplikacija**

- [01: REST Chat Brzi početak](./Module08/samples/01/README.md)
- [02: OpenAI SDK integracija](./Module08/samples/02/README.md)
- [03: Otkrivanje modela i benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)
- [05: Orkestracija više agenata](./Module08/samples/05/README.md)
- [06: Usmjerivač modela-kao-alati](./Module08/samples/06/README.md)
- [07: Izravni API klijent](./Module08/samples/07/README.md)
- [08: Windows 11 chat aplikacija](./Module08/samples/08/README.md)
- [09: Napredni sustav više agenata](./Module08/samples/09/README.md)
- [10: Foundry Tools okvir](./Module08/samples/10/README.md)

### 🎓 **Radionica: Praktični put učenja**

Cjeloviti materijali za praktičnu radionicu s implementacijama spremnim za produkciju:

- **[Vodič za radionicu](./Workshop/Readme.md)** - Kompletni ciljevi učenja, očekivanja i navigacija resursima
- **Python primjeri** (6 sesija) - Ažurirani s najboljim praksama, rukovanjem pogreškama i opsežnom dokumentacijom
- **Jupyter bilježnice** (8 interaktivnih) - Korak-po-korak tutorijali s benchmarkovima i nadzorom performansi
- **Vodiči za sesije** - Detaljni markdown vodiči za svaku radionicu
- **Alati za validaciju** - Skripte za provjeru kvalitete koda i izvođenje osnovnih testova

**Što ćete izgraditi:**
- Lokalne AI chat aplikacije s podrškom za streaming
- RAG pipeline-ove s ocjenom kvalitete (RAGAS)
- Alate za benchmarking i usporedbu više modela
- Sustave za orkestraciju više agenata
- Inteligentno usmjeravanje modela s odabirom prema zadatku

### 📊 **Sažetak puta učenja**
- **Ukupno trajanje**: 36-45 sati
- **Put za početnike**: Moduli 01-02 (7-9 sati)  
- **Srednji put**: Moduli 03-04 (9-11 sati)
- **Napredni put**: Moduli 05-07 (12-15 sati)
- **Put za stručnjake**: Modul 08 (8-10 sati)

## Što ćete izgraditi

### 🎯 Temeljne kompetencije
- **Arhitektura Edge AI**: Dizajnirajte lokalno-prvo AI sustave s integracijom u cloud
- **Optimizacija modela**: Kvantizirajte i komprimirajte modele za raspoređivanje na rubu (85% ubrzanje, 75% smanjenje veličine)
- **Raspoređivanje na više platformi**: Windows, mobilni, ugrađeni i hibridni cloud-edge sustavi
- **Operacije u proizvodnji**: Nadgledanje, skaliranje i održavanje Edge AI u proizvodnji

### 🏗️ Praktični projekti
- **Foundry Local Chat Apps**: izvorna Windows 11 aplikacija s prebacivanjem modela
- **Sustavi s više agenata**: koordinator sa specijaliziranim agentima za složene tijekove rada  
- **RAG aplikacije**: lokalna obrada dokumenata s vektorskim pretraživanjem
- **Usmjerivači modela**: inteligentan odabir između modela temeljen na analizi zadatka
- **API okviri**: klijenti spremni za proizvodnju sa streamingom i nadzorom zdravlja
- **Alati za više platformi**: obrasci integracije LangChain/Semantic Kernel

### 🏢 Primjene u industriji
**Proizvodnja** • **Zdravstvo** • **Autonomna vozila** • **Pametni gradovi** • **Mobilne aplikacije**

## Brzi početak

**Preporučeni put učenja** (20-30 sati ukupno):

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Osnove EdgeAI + industrijski kontekst + okvir za učenje
1. **📚 Osnove** (Modules 01-02): koncepti EdgeAI + obitelji SLM modela
2. **⚙️ Optimizacija** (Modules 03-04): raspoređivanje + okviri za kvantizaciju  
3. **🚀 Proizvodnja** (Modules 05-06): SLMOps + AI agenti + pozivanja funkcija
4. **💻 Implementacija** (Modules 07-08): primjeri platforme + Foundry Local alatni paket

Svaki modul uključuje teoriju, praktične vježbe i uzorke koda spremne za proizvodnju.

## Utjecaj na karijeru

**Tehničke uloge**: Arhitekt rješenja za EdgeAI • ML inženjer (Edge) • IoT AI developer • Mobilni AI developer

**Industrijski sektori**: Proizvodnja 4.0 • Zdravstvena tehnologija • Autonomni sustavi • FinTech • Potrošačka elektronika

**Projekti za portfelj**: sustavi s više agenata • proizvodne RAG aplikacije • raspoređivanje na više platformi • optimizacija performansi

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

## Istaknuto tečaja

✅ **Postupno učenje**: Teorija → praksa → raspoređivanje u proizvodnju  
✅ **Studije slučaja**: Microsoft, Japan Airlines, implementacije u poduzećima  
✅ **Praktični primjeri**: 50+ primjera, 10 opsežnih Foundry Local demonstracija  
✅ **Fokus na performansama**: poboljšanja brzine 85%, smanjenja veličine 75%  
✅ **Višeplatformski**: Windows, mobilni, ugrađeni, hibrid cloud-edge  
✅ **Spremno za proizvodnju**: nadgledanje, skaliranje, sigurnost, okviri za usklađenost

📖 **[Dostupan vodič za učenje](STUDY_GUIDE.md)**: Strukturirani 20-satni put učenja s uputama za raspodjelu vremena i alatima za samoocjenu.

---

**EdgeAI predstavlja budućnost raspoređivanja AI-a**: lokalno u prvom planu, zaštita privatnosti i učinkovitost. Savladajte ove vještine da biste izgradili sljedeću generaciju inteligentnih aplikacija.

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
 
### Serija generativnog AI
[![Generativni AI za početnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativni AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativni AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativni AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Temeljno učenje
[![ML za početnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
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

Ako zapnete ili imate pitanja o izradi AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili pogreške tijekom izrade posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje odgovornosti**:
Ovaj je dokument preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim izvorom. Za važne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz uporabe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->