<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T10:03:21+00:00",
  "source_file": "README.md",
  "language_code": "sl"
}
-->
# EdgeAI za začetnike


![Slika naslovnice tečaja](../../translated_images/cover.eb18d1b9605d754b.sl.png)

[![Sodelujoči na GitHubu](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub težave](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull zahtevki](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub opazovalci](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub vilice](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub zvezde](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Sledite tem korakom, da začnete uporabljati te vire:

1. **Vilica repozitorija**: Kliknite [![GitHub vilice](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klonirajte repozitorij**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Pridružite se Azure AI Foundry Discordu in spoznajte strokovnjake ter druge razvijalce**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Podpora več jezikom

#### Podprto preko GitHub Action (avtomatizirano in vedno posodobljeno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabščina](../ar/README.md) | [Bengalščina](../bn/README.md) | [Bolgarščina](../bg/README.md) | [Burmanski (Myanmar)](../my/README.md) | [Kitajščina (poenostavljena)](../zh/README.md) | [Kitajščina (tradicionalna, Hong Kong)](../hk/README.md) | [Kitajščina (tradicionalna, Macau)](../mo/README.md) | [Kitajščina (tradicionalna, Taiwan)](../tw/README.md) | [Hrvaščina](../hr/README.md) | [Češčina](../cs/README.md) | [Danščina](../da/README.md) | [Nizozemščina](../nl/README.md) | [Estonščina](../et/README.md) | [Finščina](../fi/README.md) | [Francoščina](../fr/README.md) | [Nemščina](../de/README.md) | [Grščina](../el/README.md) | [Hebrejščina](../he/README.md) | [Hindujščina](../hi/README.md) | [Madžarščina](../hu/README.md) | [Indonezijščina](../id/README.md) | [Italijanščina](../it/README.md) | [Japonščina](../ja/README.md) | [Kannada](../kn/README.md) | [Korejščina](../ko/README.md) | [Litvijščina](../lt/README.md) | [Malajščina](../ms/README.md) | [Malajalščina](../ml/README.md) | [Maratščina](../mr/README.md) | [Nepalščina](../ne/README.md) | [Nigeryjski pidgin](../pcm/README.md) | [Norveščina](../no/README.md) | [Perzijščina (Farzi)](../fa/README.md) | [Poljščina](../pl/README.md) | [Portugalščina (Brazilija)](../br/README.md) | [Portugalščina (Portugalska)](../pt/README.md) | [Pandžabščina (Gurmukhi)](../pa/README.md) | [Romunščina](../ro/README.md) | [Ruščina](../ru/README.md) | [Srbščina (cirilica)](../sr/README.md) | [Slovaščina](../sk/README.md) | [Slovenščina](./README.md) | [Španščina](../es/README.md) | [Svahili](../sw/README.md) | [Švedščina](../sv/README.md) | [Tagalog (Filipini)](../tl/README.md) | [Tamilščina](../ta/README.md) | [Telugu](../te/README.md) | [Tajščina](../th/README.md) | [Turščina](../tr/README.md) | [Ukrajinščina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamščina](../vi/README.md)

> **Raje klonirate lokalno?**

> Ta repozitorij vključuje več kot 50 jezikovnih prevodov, kar znatno poveča velikost prenosa. Za kloniranje brez prevodov uporabite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tako dobite vse, kar potrebujete za dokončanje tečaja z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Če želite, da so podprti dodatni prevodni jeziki, so navedeni [tukaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Uvod

Dobrodošli v **EdgeAI za začetnike** – vašo celovito potovanje v prelomni svet umetne inteligence na robu. Ta tečaj premošča vrzel med močnimi zmožnostmi AI in praktično, resnično implementacijo na robnih napravah, kar vam omogoča, da izkoristite potencial AI neposredno tam, kjer se ustvarjajo podatki in je treba sprejeti odločitve.

### Česar se boste naučili

Ta tečaj vas popelje od osnovnih pojmov do izvedb, pripravljenih za produkcijo, ki pokrivajo:
- **Majhne jezikovne modele (SLM)**, optimizirane za robno uvajanje
- **Optimizacijo z ozaveščenostjo strojne opreme** na različnih platformah
- **Inferenco v realnem času** z zmožnostmi varovanja zasebnosti
- **Strategije uvajanja v proizvodnjo** za podjetniške aplikacije

### Zakaj je EdgeAI pomemben

Edge AI predstavlja premik paradigme, ki rešuje kritične sodobne izzive:
- **Zasebnost in varnost**: Obravnava občutljive podatke lokalno brez razkritja v oblaku
- **Izvedba v realnem času**: Odpravlja zakasnitve omrežja za aplikacije, ki zahtevajo hiter odziv
- **Stroškovna učinkovitost**: Zmanjšuje stroške pasovne širine in oblačnih storitev
- **Odpornost delovanja**: Ohranja funkcionalnost med izpadi omrežja
- **Skladnost z zakonodajo**: Izpolnjuje zahteve glede suverenosti podatkov

### Edge AI

Edge AI pomeni izvajanje AI algoritmov in jezikovnih modelov lokalno na strojni opremi, blizu mesta ustvarjanja podatkov, brez odvisnosti od oblačnih virov za inferenco. Zmanjšuje latenco, izboljšuje zasebnost in omogoča odločanje v realnem času.

### Temeljna načela:
- **Inferenca na napravi**: AI modeli delujejo na robnih napravah (telefoni, usmerjevalniki, mikrokontrolerji, industrijski PC-ji)
- **Funkcionalnost brez povezave**: Deluje brez stalne internetne povezave
- **Nizka latenca**: Takojšnji odzivi, primerni za sisteme v realnem času
- **Suverenost podatkov**: Ohranja občutljive podatke lokalno, izboljšuje varnost in skladnost

### Majhni jezikovni modeli (SLM)

SLM-ji, kot so Phi-4, Mistral-7B in Gemma, so optimizirane različice večjih LLM-jev—usposobljeni ali destilirani za:
- **Zmanjšan pomnilniški odtis**: Učinkovita uporaba omejenega pomnilnika na robnih napravah
- **Nižjo računsko zahtevnost**: Optimizirani za delovanje na CPU-ju in robnem GPU-ju
- **Hitrejši zagon**: Hitro inicializiranje za odzivne aplikacije

Odklenejo močne zmožnosti NLP, hkrati izpolnjujejo omejitve:
- **Vgrajeni sistemi**: IoT naprave in industrijski krmilniki
- **Mobilne naprave**: Pametni telefoni in tablice z delovanjem brez povezave
- **IoT naprave**: Senzorji in pametne naprave z omejenimi viri
- **Robni strežniki**: Lokalni procesni enoti z omejenimi GPU viri
- **Osebni računalniki**: Namizne in prenosne naprave za uporabo

## Moduli tečaja & navigacija

| Modul | Tema | Osrednje področje | Ključna vsebina | Nivo | Trajanje |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Uvod v EdgeAI](./introduction.md) | Osnove & kontekst | Pregled EdgeAI • Industrijske uporabe • Uvod v SLM • Cilji učenja | Začetnik | 1-2 uri |
| [📚 01](../../Module01) | [Osnove EdgeAI](./Module01/README.md) | Primerjava oblaka in roba | Osnove EdgeAI • Študije primerov iz resničnega sveta • Vodnik za implementacijo • Robno uvajanje | Začetnik | 3-4 ure |
| [🧠 02](../../Module02) | [Osnove SLM modelov](./Module02/README.md) | Družine modelov & arhitektura | Družina Phi • Družina Qwen • Družina Gemma • BitNET • μModel • Phi-Silica | Začetnik | 4-5 ur |
| [🚀 03](../../Module03) | [Praksa uvajanja SLM](./Module03/README.md) | Lokalno in oblačno uvajanje | Napredno učenje • Lokalno okolje • Oblačno uvajanje | Srednji | 4-5 ur |
| [⚙️ 04](../../Module04) | [Orodja za optimizacijo modela](./Module04/README.md) | Optimizacija med platformami | Uvod • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sestavljanje poteka dela | Srednji | 5-6 ur |
| [🔧 05](../../Module05) | [Proizvodni SLMOps](./Module05/README.md) | Proizvodne operacije | Uvod v SLMOps • Destilacija modela • Delo na fino nastavitev • Uvajanje v produkcijo | Napredno | 5-6 ur |
| [🤖 06](../../Module06) | [AI agenti in klic funkcij](./Module06/README.md) | Okviri agentov & MCP | Uvod v agente • Klic funkcij • Protokol konteksta modela | Napredno | 4-5 ur |
| [💻 07](../../Module07) | [Implementacija platforme](./Module07/README.md) | Vzorcev med platformami | Orodja AI • Foundry Local • Razvoj za Windows | Napredno | 3-4 ure |
| [🏭 08](../../Module08) | [Foundry Local orodja](./Module08/README.md) | Pripravljeni vzorci za produkcijo | Vzorec aplikacij (glej podrobnosti spodaj) | Strokovnjak | 8-10 ur |

### 🏭 **Modul 08: Vzorec aplikacij**

- [01: REST Chat hitri začetek](./Module08/samples/01/README.md)
- [02: Integracija OpenAI SDK](./Module08/samples/02/README.md)
- [03: Odkritje modelov in benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG aplikacija](./Module08/samples/04/README.md)
- [05: Večagentna orkestracija](./Module08/samples/05/README.md)
- [06: Usmerjevalnik modelov kot orodij](./Module08/samples/06/README.md)
- [07: Neposreden API klient](./Module08/samples/07/README.md)
- [08: Windows 11 klepetalna aplikacija](./Module08/samples/08/README.md)
- [09: Napredni večagentni sistem](./Module08/samples/09/README.md)
- [10: Foundry orodna ogrodja](./Module08/samples/10/README.md)

### 🎓 **Delavnica: Pot ročnega učenja**

Celovita gradiva za delavnico s praktičnimi vsebinami in izvajanjem, pripravljenim za produkcijo:

- **[Vodnik delavnice](./Workshop/Readme.md)** - Celotni cilji učenja, izidi in navigacija po virih
- **Python vzorci** (6 sej) - Posodobljeni z najboljšimi praksami, ravnanjem z napakami in obsežno dokumentacijo
- **Jupyter zvezki** (8 interaktivnih) - Korak za korakom vodiči z benchmarkingom in spremljanjem zmogljivosti
- **Vodniki za seje** - Podrobni markdown vodiči za vsako delavnico
- **Orodja za validacijo** - Skripte za preverjanje kakovosti kode in izvajanje dimnih testov

**Kaj boste zgradili:**
- Lokalno AI klepetalno aplikacijo s podporo pretakanju
- RAG cevovode z ocenjevanjem kakovosti (RAGAS)
- Orodja za benchmarking in primerjavo več modelov
- Sisteme za orkestracijo več agentov
- Inteligentno usmerjanje modelov z izbiro na podlagi nalog

### 🎙️ **Delavnica za Agentic: Praktično - AI Podcast Studio**

Zgradite produkcijsko cevovod za podcast, ki ga poganja umetna inteligenca, iz nič! Ta poglobljena delavnica vas uči, kako ustvariti celovit večagentni sistem, ki spremeni ideje v profesionalne epizode podcasta.
**[🎬 Začni delavnico AI Podcast Studia](./WorkshopForAgentic/README.md)**

**Tvoja naloga**: Zaženi "Future Bytes" — tehnološki podcast, ki ga poganjajo izključno AI agenti, ki jih boš sam ustvaril. Brez odvisnosti od oblaka, brez stroškov API-jev — vse teče lokalno na tvojem računalniku.

**Kaj to naredi edinstveno:**
- **🤖 Resnična orkestracija več agentov** - Ustvari specializirane AI agente, ki raziskujejo, pišejo in proizvajajo avdio
- **🎯 Popoln produkcijski proces** - Od izbire teme do končnega avdio posnetka podcasta
- **💻 100 % lokalna uporaba** - Uporablja Ollamo in lokalne modele (Qwen-3-8B) za popolno zasebnost in nadzor
- **🎤 Integracija besedilo-v-govorno** - Pretvori scenarije v naravno zveneče večglasne pogovore
- **✋ Delovni tokovi s človekom v zanki** - Vrata za odobritev zagotavljajo kakovost med avtomatizacijo

**Učenje v treh dejanjih:**

| Dejanje | Osredotočenost | Ključne spretnosti | Trajanje |
|---------|----------------|--------------------|----------|
| **[Dejanje 1: Spoznaj svoje AI asistente](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Ustvari svojega prvega AI agenta | Integracija orodij • Iskanje na spletu • Reševanje problemov • Agentično razmišljanje | 2-3 ure |
| **[Dejanje 2: Sestavi svojo produkcijsko ekipo](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestriraj več agentov | Koordinacija ekipe • Delovni tokovi odobritve • Vmesnik DevUI • Človeški nadzor | 3-4 ure |
| **[Dejanje 3: Oživitev tvojega podcasta](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generiraj avdio podcasta | Besedilo v govor • Sinteza več govorcev • Dolgi avdio • Polna avtomatizacija | 2-3 ure |

**Uporabljene tehnologije:**
- **Microsoft Agent Framework** - Orkestracija in koordinacija več agentov
- **Ollama** - Lokalno izvajanje modelov AI (brez oblaka)
- **Qwen-3-8B** - Odprt vir jezikovni model optimiziran za agentske naloge
- **API-ji za besedilo-v-govor** - Naravna sinteza glasu za generiranje podcasta

**Podpora strojne opreme:**
- ✅ **Način CPU** - Deluje na katerem koli sodobnem računalniku (priporočljivo 8GB+ RAM)
- 🚀 **Pospešek z GPU** - Znatno hitrejše sklepanje z NVIDIA/AMD GPU-ji
- ⚡ **Podpora NPU** - Pospeševanje z naslednjo generacijo nevronskih procesnih enot

**Popolno za:**
- Razvijalce, ki se učijo sistemov več agentov AI
- Vsakogar, ki ga zanima AI avtomatizacija in delovni tokovi
- Ustvarjalce vsebin, ki raziskujejo AI-podprto produkcijo
- Študente, ki preučujejo praktične vzorce AI orkestracije

**Začni graditi**: [🎙️ Delavnica AI Podcast Studia →](./WorkshopForAgentic/README.md)

### 📊 **Povzetek učne poti**
- **Skupno trajanje**: 36-45 ur
- **Pot začetnika**: Moduli 01-02 (7-9 ur)  
- **Srednje zahtevna pot**: Moduli 03-04 (9-11 ur)
- **Napredna pot**: Moduli 05-07 (12-15 ur)
- **Strokovna pot**: Modul 08 (8-10 ur)

## Kaj boš izdelal

### 🎯 Ključne kompetence
- **Robna AI arhitektura**: Oblikovanje sistemov AI z lokalno prvinsko zasnovo in integracijo v oblak
- **Optimizacija modela**: Kvantizacija in kompresija modelov za robno izvajanje (85 % pospešek hitrosti, 75 % zmanjšanje velikosti)
- **Večplatformska postavitev**: Windows, mobilno, vgrajeno in hibridno oblačno-robo okolje
- **Produkcijske operacije**: Nadzor, skaliranje in vzdrževanje robne AI v produkciji

### 🏗️ Praktični projekti
- **Foundry lokalne klepetalne aplikacije**: Windows 11 domača aplikacija s preklapljanjem modelov
- **Sistemi z več agenti**: Koordinator z specialističnimi agenti za kompleksne delovne tokove  
- **RAG aplikacije**: Lokalna obdelava dokumentov z vektorskim iskanjem
- **Preusmerjevalniki modelov**: Pametna izbira modelov glede na analizo naloge
- **API okvirji**: Produkcijsko pripravljeni klienti z pretočnim prenosom in nadzorom zdravja
- **Večplatformska orodja**: Vzorci integracije LangChain/Semantic Kernel

### 🏢 Industrijske aplikacije
**Proizvodnja** • **Zdravstvo** • **Avtonomna vozila** • **Pametna mesta** • **Mobilne aplikacije**

## Hitri začetek

**Priporočena učna pot** (skupno 20-30 ur):

0. **📖 Uvod** ([Introduction.md](./introduction.md)): Temelji EdgeAI + industrijski kontekst + učni okvir
1. **📚 Osnove** (Moduli 01-02): Koncepti EdgeAI + družine modelov SLM
2. **⚙️ Optimizacija** (Moduli 03-04): Postavitev + okvirji za kvantizacijo  
3. **🚀 Produkcija** (Moduli 05-06): SLMOps + AI agenti + klicanje funkcij
4. **💻 Implementacija** (Moduli 07-08): Vzorec platforme + Foundry Local orodjarna

Vsak modul vsebuje teorijo, praktične vaje in kode pripravljene za produkcijo.

## Vpliv na kariero

**Tehnične vloge**: Arhitekt rešitev EdgeAI • ML inženir (rob) • IoT AI razvijalec • Mobilni AI razvijalec

**Industrijski sektorji**: Proizvodnja 4.0 • Zdravstvena tehnologija • Avtonomni sistemi • FinTech • Potrošniška elektronika

**Projekti za portfelj**: Sistemi z več agenti • Produkcijske RAG aplikacije • Večplatformska postavitev • Optimizacija zmogljivosti

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

✅ **Postopen razvoj znanja**: Teorija → Praksa → Produkcijska postavitev  
✅ **Resnične študije primerov**: Microsoft, Japan Airlines, implementacije v podjetjih  
✅ **Praktični primeri**: 50+ primerov, 10 celovitih demonstracij Foundry Local  
✅ **Osredotočenost na zmogljivost**: 85 % izboljšave hitrosti, 75 % zmanjšanja velikosti  
✅ **Večplatformski**: Windows, mobilno, vgrajeno, oblačno-robo hibridno  
✅ **Pripravljen za produkcijo**: Nadzor, skaliranje, varnost, skladnostni okviri

📖 **[Na voljo študijski vodnik](STUDY_GUIDE.md)**: Strukturirana 20-urna učna pot z usmeritvijo glede časa in orodji za samoocenjevanje.

---

**EdgeAI predstavlja prihodnost uvajanja AI**: lokalno najprej, varovanje zasebnosti in učinkovitost. Obvladaj te spretnosti in ustvarjaj naslednjo generacijo inteligentnih aplikacij.

## Drugi tečaji

Naša ekipa izdeluje tudi druge tečaje! Oglej si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za začetnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za začetnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD za začetnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za začetnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za začetnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agenti za začetnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Generativne AI
[![Generativna AI za začetnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Osnovno učenje
[![ML za začetnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Podatkovna znanost za začetnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za začetnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetska varnost za začetnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Spletni razvoj za začetnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za začetnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR razvoj za začetnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot
[![Copilot za AI parno programiranje](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Pridobivanje pomoči

Če zaidete v težave ali imate vprašanja o ustvarjanju AI aplikacij, se pridružite:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali napake med razvojem, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorni jezik naj velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Za kakršnekoli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->