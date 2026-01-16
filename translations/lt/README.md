<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T10:07:30+00:00",
  "source_file": "README.md",
  "language_code": "lt"
}
-->
# EdgeAI pradedantiesiems 


![Kurso viršelio paveikslėlis](../../translated_images/lt/cover.eb18d1b9605d754b.png)

[![GitHub bendradarbiai](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-užklausos](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub šakos](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub žvaigždės](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Sekite šiuos veiksmus, kad pradėtumėte naudoti šiuos išteklius:

1. **Sukurkite šaką (fork) saugykloje**: Spustelėkite [![GitHub šakos](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Atsisiųskite saugyklą (clone)**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Prisijunkite prie Azure AI Foundry Discord ir susipažinkite su ekspertais bei kitais kūrėjais**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Daugiakalbė palaikymas

#### Palaikoma per GitHub Action (automatinis ir visada atnaujinta)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Norite klonuoti vietoje?**

> Ši saugykla apima daugiau nei 50 kalbų vertimų, kurie gerokai padidina atsisiuntimo dydį. Norėdami klonuoti be vertimų, naudokite riboto pasirinkimo checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tai suteikia viską, ko reikia kurso užbaigimui, žymiai pagreitindama atsisiuntimą.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jei norite palaikyti papildomas vertimų kalbas, jų sąrašas pateiktas [čia](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Įvadas

Sveiki atvykę į **EdgeAI pradedantiesiems** – jūsų išsamų kelionę į transformuojantį "Edge" dirbtinio intelekto pasaulį. Šis kursas sujungia galingas DI galimybes su praktiniu, realių scenarijų diegimu ant krašto įrenginių, suteikdamas jums galimybę pasinaudoti DI potencialu tiesiog ten, kur generuojami duomenys ir reikia priimti sprendimus.

### Ko išmoksite

Šis kursas nuveda jus nuo pagrindinių sąvokų iki paruoštų gamybai įgyvendinimų, apimdamas:
- **Mažieji kalbų modeliai (SLM)** optimizuoti krašto diegimui
- **Įrangai pritaikyta optimizacija** įvairiose platformose
- **Realaus laiko spėjimas** su privatumo apsaugos funkcijomis
- **Gamybinis diegimas** verslo taikymams

### Kodėl svarbus EdgeAI

Edge AI reiškia paradigmos pokytį, kuris sprendžia svarbias šiuolaikines problemas:
- **Privatumas ir saugumas**: apdorokite jautrius duomenis vietoje, nenaudojant debesies
- **Realaus laiko našumas**: pašalinkite tinklo vėlavimą laiko kritinėse programose
- **Kaštų efektyvumas**: sumažinkite pralaidumo ir debesijos sąnaudas
- **Atsparios operacijos**: palaikykite veikimą tinklo gedimų atveju
- **Reguliacinis atitikimas**: atitinkite duomenų suvereniteto reikalavimus

### Edge AI

Edge AI reiškia DI algoritmų ir kalbų modelių vykdymą vietoje įrenginiuose, arti duomenų generavimo vietos, nenaudojant debesijos išteklių spėjimui. Tai sumažina delsą, pagerina privatumo lygį ir leidžia priimti sprendimus realiu laiku.

### Pagrindinės principai:
- **Vietinis spėjimas**: DI modeliai veikia krašto įrenginiuose (telefonuose, maršrutizatoriuose, mikrovaldikliuose, pramoniniuose kompiuteriuose)
- **Veikimas be interneto**: veikia be nuolatinio interneto ryšio
- **Mažas delsimas**: momentiniai atsakymai, tinkami realaus laiko sistemoms
- **Duomenų suverenitetas**: jautrių duomenų laikymas vietoje, gerinantis saugumą ir atitiktį

### Mažieji kalbų modeliai (SLM)

SLM, tokie kaip Phi-4, Mistral-7B ir Gemma, yra optimizuotos didesnių LLM versijos – apmokytos arba distiliuotos skirtos:
- **Mažesnė atminties sąnauda**: efektyvus ribotos atminties panaudojimas krašto įrenginiuose
- **Mažesnis skaičiavimo poreikis**: optimizuoti CPU ir krašto GPU našumui
- **Greitesnė paleidimo trukmė**: greita inicializacija reagavimo programas

Šie modeliai atveria galingas NLP galimybes tenkinant:
- **Įmontuotos sistemos**: daiktų interneto įrenginiai ir pramoniniai valdikliai
- **Mobilūs įrenginiai**: išmanieji telefonai ir planšetės su veikimu be interneto
- **IoT įrenginiai**: jutikliai ir protingi įrenginiai su ribotais ištekliais
- **Krašto serveriai**: vietinės apdorojimo stotys su ribotais GPU ištekliais
- **Asmeniniai kompiuteriai**: stalinių ir nešiojamų kompiuterių diegimo scenarijai

## Kurso moduliai ir navigacija

| Modulis | Tema | Dėmesio sritis | Pagrindinė medžiaga | Lygis | Trukmė |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Įvadas į EdgeAI](./introduction.md) | Pagrindai ir kontekstas | EdgeAI apžvalga • Pramonės taikymai • SLM įvadas • Mokymosi tikslai | Pradedantysis | 1-2 val. |
| [📚 01](../../Module01) | [EdgeAI pagrindai](./Module01/README.md) | Debesijos ir krašto DI palyginimas | EdgeAI pagrindai • Realios istorijos atvejai • Įgyvendinimo vadovas • Krašto diegimas | Pradedantysis | 3-4 val. |
| [🧠 02](../../Module02) | [SLM modelių pagrindai](./Module02/README.md) | Modelių šeimos ir architektūra | Phi šeima • Qwen šeima • Gemma šeima • BitNET • μModel • Phi-Silica | Pradedantysis | 4-5 val. |
| [🚀 03](../../Module03) | [SLM praktinis diegimas](./Module03/README.md) | Vietinis ir debesijos diegimas | Pažangus mokymasis • Vietinė aplinka • Debesijos diegimas | Vidutinis | 4-5 val. |
| [⚙️ 04](../../Module04) | [Modelių optimizavimo įrankiai](./Module04/README.md) | Kryžminė platformų optimizacija | Įvadas • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Darbo eigos sintezė | Vidutinis | 5-6 val. |
| [🔧 05](../../Module05) | [SLMOps gamyba](./Module05/README.md) | Gamybinė veikla | SLMOps įvadas • Modelių distiliacija • Tobulinimas • Produkcinis diegimas | Pažengęs | 5-6 val. |
| [🤖 06](../../Module06) | [DI agentai ir funkcijų kvietimas](./Module06/README.md) | Agentų karkasai ir MCP | Agentų įvadas • Funkcijų kvietimas • Modelių konteksto protokolas | Pažengęs | 4-5 val. |
| [💻 07](../../Module07) | [Platformų įgyvendinimas](./Module07/README.md) | Kryžminė platformų pavyzdžiai | DI įrankių rinkinys • Foundry Local • Windows kūrimas | Pažengęs | 3-4 val. |
| [🏭 08](../../Module08) | [Foundry Local įrankių rinkinys](./Module08/README.md) | Produkciniai pavyzdžiai | Pavyzdinės programėlės (žr. žemiau detales) | Ekspertas | 8-10 val. |

### 🏭 **Modulis 08: Pavyzdinės programos**

- [01: REST Chat greitas startas](./Module08/samples/01/README.md)
- [02: OpenAI SDK integracija](./Module08/samples/02/README.md)
- [03: Modelių atranka ir lyginimas](./Module08/samples/03/README.md)
- [04: Chainlit RAG programa](./Module08/samples/04/README.md)
- [05: Multi-agentų orkestracija](./Module08/samples/05/README.md)
- [06: Modeliai kaip įrankiai - maršrutizatorius](./Module08/samples/06/README.md)
- [07: Tiesioginis API klientas](./Module08/samples/07/README.md)
- [08: Windows 11 pokalbių programa](./Module08/samples/08/README.md)
- [09: Pažangi multi-agentų sistema](./Module08/samples/09/README.md)
- [10: Foundry įrankių karkasas](./Module08/samples/10/README.md)

### 🎓 **Dirbtuvės: Praktinis mokymosi kelias**

Išsamios praktinės dirbtuvės su gamybai paruoštais įgyvendinimais:

- **[Dirbtuvių vadovas](./Workshop/Readme.md)** - Pilni mokymosi tikslai, rezultatai ir išteklių naršymas
- **Python pavyzdžiai** (6 sesijos) - Atnaujinti su geriausiomis praktikomis, klaidų valdymu ir išsamiu dokumentavimu
- **Jupyter užrašų knygelės** (8 interaktyvios) - Žingsnis po žingsnio pamokos su lyginimais ir našumo stebėsena
- **Sesijų vadovai** - Išsamūs markdown vadovai kiekvienai dirbtuvių sesijai
- **Patvirtinimo įrankiai** - Skriptai kodo kokybei patikrinti ir dūmų testų vykdymui

**Ką sukursite:**
- Vietines DI pokalbių programas su srautinio perdavimo palaikymu
- RAG duomenų srautus su kokybės vertinimu (RAGAS)
- Multi-modelių lyginimo ir vertinimo įrankius
- Multi-agentų orkestravimo sistemas
- Išmanų modelių maršrutizavimą pagal užduotis

### 🎙️ **Agentiniams skirtos dirbtuvės: Praktinės - DI podcastų studija**

Sukurkite nuo nulio DI valdytą podcastų gamybos procesą! Šios intensyvios dirbtuvės moko kurti pilną multi-agentų sistemą, kuri keičia idėjas į profesionalius podcastų epizodus.
**[🎬 Pradėkite AI podcast studijos dirbtuves](./WorkshopForAgentic/README.md)**

**Jūsų užduotis**: Sukurkite „Future Bytes“ — technikos podcastą, kurį visiškai valdo patys sukurti AI agentai. Nėra debesų priklausomybių, nėra API sąnaudų — viskas veikia lokaliai jūsų kompiuteryje.

**Kas tai daro unikaliu:**
- **🤖 Tikras daugiagentinis koordinavimas** – Kurkite specializuotus AI agentus, kurie atlieka tyrimus, rašo tekstus ir gamina garso įrašus
- **🎯 Viso proceso gamyba** – Nuo temos pasirinkimo iki galutinio podcast garso išvesties
- **💻 100 % lokali diegimo aplinka** – Naudoja Ollama ir vietinius modelius (Qwen-3-8B) visiškam privatumui ir kontrolei
- **🎤 Teksto į kalbą integracija** – Paverskite scenarijus natūraliai skambančiais daugiakalbiais pokalbiais
- **✋ Žmogaus dalyvavimas procese** – Patvirtinimo taškai užtikrina kokybę, išlaikant automatizavimą

**Trijų veiksmų mokymosi kelionė:**

| Veiksmas | Fokusas | Pagrindiniai įgūdžiai | Trukmė |
|-----|-------|------------|----------|
| **[1 veiksmas: Susipažinkite su savo AI asistentais](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Sukurkite savo pirmąjį AI agentą | Įrankių integracija • Tinklo paieška • Problemos sprendimas • Agentinis mąstymas | 2-3 val. |
| **[2 veiksmas: Sudėkite savo gamybos komandą](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Koordinuokite kelis agentus | Komandos koordinavimas • Patvirtinimo darbo eigas • DevUI sąsaja • Žmogiška priežiūra | 3-4 val. |
| **[3 veiksmas: Atgaivinkite savo podcast'ą](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generuokite podcast garso įrašą | Teksto į kalbą • Daugiažodžiai sintezės įrankiai • Ilgo formato garsas • Pilna automatizacija | 2-3 val. |

**Naudojamos technologijos:**
- **Microsoft agentų sistema** – Daugiagentinė koordinacija ir valdymas
- **Ollama** – Vietinis AI modelių paleidimo variklis (nereikia debesies)
- **Qwen-3-8B** – Atviro kodo kalbos modelis, pritaikytas agentiniams uždaviniams
- **Teksto į kalbą API** – Natūralių balsų sintezė podcast gamybai

**Aparatinės įrangos palaikymas:**
- ✅ **CPU režimas** – Veikia bet kuriame moderniame kompiuteryje (rekomenduojama 8GB+ RAM)
- 🚀 **GPU pagreitinimas** – Žymiai spartesnis apdorojimas su NVIDIA/AMD GPU
- ⚡ **NPU palaikymas** – Naujos kartos neuroninio apdorojimo įrenginių pagreitinimas

**Puikiai tinka:**
- Programuotojams, mokantis daugiagentinės AI sistemos
- Visiems, besidomintiems AI automatizavimu ir darbo eigomis
- Turinį kuriantiems, tyrinėjantiems AI pagalbą gamyboje
- Studentams, besimokantiems praktinių AI koordinavimo metodų

**Pradėkite kurti**: [🎙️ AI podcast studijos dirbtuvės →](./WorkshopForAgentic/README.md)

### 📊 **Mokymosi kelio santrauka**
- **Bendra trukmė**: 36-45 valandos
- **Pradedančiojo kelias**: 01–02 moduliai (7-9 valandos)  
- **Tarpinis kelias**: 03–04 moduliai (9-11 valandų)  
- **Pažengęs kelias**: 05–07 moduliai (12-15 valandų)  
- **Ekspertų kelias**: 08 modulis (8-10 valandų)  

## Ką kursite

### 🎯 Pagrindiniai gebėjimai
- **Edge AI architektūra**: Projektuokite vietinius AI sprendimus su debesijos integracija
- **Modelių optimizavimas**: Kvantizavimas ir glaudinimas krašto įrenginiams (85 % greičio pagreitis, 75 % dydžio sumažinimas)
- **Daugiaplatformės diegimas**: Windows, mobiliosios, įterptos ir debesijos bei krašto hibridinės sistemos
- **Gamybos operacijos**: Stebėjimas, skalavimas ir krašto AI palaikymas gamyboje

### 🏗️ Praktiniai projektai
- **Foundry vietinės pokalbių programos**: Windows 11 gimtoji programa su modelio perjungimu
- **Daugiagentinės sistemos**: Koordinatorius su specialistų agentais sudėtingoms darbo eigoms  
- **RAG programos**: Vietinis dokumentų apdorojimas su vektorinė paieška
- **Modelių maršrutizatoriai**: Protingas modelių pasirinkimas pagal užduoties analizę
- **API sistemos**: Gamybai paruošti klientai su transliavimu ir sveikatos stebėsena
- **Kryžminės platformos įrankiai**: LangChain/Semantic Kernel integracijos šablonai

### 🏢 Pramonės taikymai
**Gamyba** • **Sveikatos priežiūra** • **Autonominiai automobiliai** • **Išmanieji miestai** • **Mobiliosios programėlės**

## Greitas startas

**Rekomenduojamas mokymosi kelias** (iš viso 20-30 valandų):

0. **📖 Įvadas** ([Introduction.md](./introduction.md)): EdgeAI pagrindai + pramonės kontekstas + mokymosi sistema  
1. **📚 Pagrindai** (01–02 moduliai): EdgeAI koncepcijos + SLM modelių šeimos  
2. **⚙️ Optimizavimas** (03–04 moduliai): Diegimas + kvantizacijos sistemos  
3. **🚀 Gamyba** (05–06 moduliai): SLMOps + AI agentai + funkcijų kvietimas  
4. **💻 Įgyvendinimas** (07–08 moduliai): Platformos pavyzdžiai + Foundry vietinių įrankių komplektas  

Kiekviename modulyje yra teorija, praktinės užduotys ir gamybai paruošti kodo pavyzdžiai.

## Karjeros perspektyvos

**Techninės pareigos**: EdgeAI sprendimų architektas • ML inžinierius (krašto įrenginiams) • IoT AI programuotojas • Mobiliojo AI programuotojas

**Pramonės sektoriai**: Gamyba 4.0 • Sveikatos technologijos • Autonominės sistemos • FinTech • Vartotojų elektronika

**Portfelio projektai**: Daugiagentinės sistemos • Gamybinės RAG programos • Kryžminės platformos diegimas • Veikimo optimizavimas

## Saugyklos struktūra

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

## Kurso akcentai

✅ **Progresyvus mokymasis**: teorija → praktika → gamybos diegimas  
✅ **Tikri atvejų tyrimai**: Microsoft, Japan Airlines, įmonių įgyvendinimai  
✅ **Praktiniai pavyzdžiai**: 50+ pavyzdžių, 10 išsamių Foundry vietinių demonstracijų  
✅ **Dėmesys našumui**: 85 % greičio pagerinimas, 75 % dydžio sumažinimas  
✅ **Daugiaplatformė palaikymas**: Windows, mobilioji, įterptoji, debesijos-krašto hibridas  
✅ **Gamybai paruošta**: stebėjimas, skalavimas, saugumo, atitikties sistemos

📖 **[Studijų vadovas prieinamas](STUDY_GUIDE.md)**: Struktūruotas 20 val. mokymosi planas su laiko paskirstymo gairėmis ir savarankiško vertinimo įrankiais.

---

**EdgeAI žymi ateitį AI diegime**: pirmenybė vietiniams sprendimams, privatumo išsaugojimui ir efektyvumui. Įvaldykite šiuos įgūdžius, kad kurtumėte naujos kartos išmanias programas.

## Kiti kursai

Mūsų komanda rengia ir kitus kursus! Peržiūrėkite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pradedantiesiems](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pradedantiesiems](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agentai
[![AZD pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatyvinis AI serija
[![Generatyvinis AI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pagrindinis mokymasis
[![ML pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Tinklalapių kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot serija
[![Copilot AI poriniam programavimui](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Gaunate pagalbą

Jei stringate ar turite klausimų apie DI programų kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite produkto atsiliepimų arba pastebite klaidas kūrimo metu, apsilankykite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->