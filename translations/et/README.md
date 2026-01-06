<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T10:09:55+00:00",
  "source_file": "README.md",
  "language_code": "et"
}
-->
# EdgeAI algajatele 


![Kursuse kaanekujutis](../../translated_images/cover.eb18d1b9605d754b.et.png)

[![GitHubi panustajad](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHubi probleemid](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHubi tõmbepäringud](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRid on teretulnud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHubi vaatlejad](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHubi kahvlid](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHubi tärnid](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Alusta nende ressursside kasutamist järgmiste sammudega:

1. **Tee hoidlast fork**: Vajuta [![GitHubi kahvlid](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Klooni hoidla**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Liitu Azure AI Foundry Discordiga ja kohtu ekspertide ning arendajatega**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Action kaudu (Automaatne ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh/README.md) | [Hiina (traditsiooniline, Hongkong)](../hk/README.md) | [Hiina (traditsiooniline, Macao)](../mo/README.md) | [Hiina (traditsiooniline, Taiwan)](../tw/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidžin](../pcm/README.md) | [Norra](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../br/README.md) | [Portugali (Portugal)](../pt/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirilitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suaheli](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagaloogi (filipiini)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Eelistad kloonimist lokaalselt?**

> See hoidla sisaldab 50+ keele tõlkeid, mis suurendavad oluliselt allalaadimismahu. Tõlgeteta kloonimiseks kasuta sparse checkouti:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> See annab sulle kõik vajaliku kursuse läbimiseks palju kiirema allalaadimiskiirusega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Kui soovid toetada täiendavaid tõlkekeeli, on need loetletud [siin](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Sissejuhatus

Tere tulemast **EdgeAI algajatele** – sinu põhjalik teekond servatehnoloogiate tehisintellekti ümberkujundavasse maailma. See kursus ühendab võimsad tehisintellekti võimalused praktilise, reaalse maailma juurutamisega servaseadmetel, võimaldades sul kasutada AI potentsiaali otse seal, kus andmeid luuakse ja otsuseid tuleb teha.

### Mida sa valdad

See kursus viib sind algteadmistest tootmisvalmis lahendusteni, hõlmates:
- **Väikesed keelemudelid (SLM-id)**, mis on optimeeritud serval töötamiseks
- **Riistvarateadlik optimiseerimine** erinevatel platvormidel
- **Reaalajas järeldamine** privaatsust kaitsvate võimalustega
- **Tootmisjuurutamise** strateegiad ettevõtetele

### Miks EdgeAI on oluline

Edge AI tähistab paradigmade muutust, mis lahendab olulisi kaasaegseid väljakutseid:
- **Privaatsus ja turvalisus**: Töötle tundlikke andmeid kohapeal ilma pilve avaldamata
- **Reaalajas jõudlus**: Vähenda võrgust põhjustatud latentsust ajakriitilistes rakendustes
- **Kuluefektiivsus**: Vähenda ribalaiuse ja pilvearvutuse kulusid
- **Vastupidav töökindlus**: Säilita funktsionaalsus võrgu katkemisel
- **Regulatiivne vastavus**: Järgi andmete suveräänsuse nõudeid

### Edge AI

Edge AI tähendab tehisintellekti algoritmide ja keelemudelite lokaalset käivitamist riistvaral, kus andmeid toodetakse, ilma pilve ressursse järeldamiseks kasutamata. See vähendab viivitust, suurendab privaatsust ja võimaldab reaalajas otsuseid teha.

### Peamised põhimõtted:
- **Sise-seadmes järeldamine**: AI mudelid jooksevad servaseadmetel (telefonid, ruuterid, mikrokontrollerid, tööstuslikud arvutid)
- **Võrguta funktsionaalsus**: Töötavad ilma püsiva internetiühenduseta
- **Madal latentsus**: Vahetud vastused sobivad reaalajas süsteemidele
- **Andmete suveräänsus**: Hoidke tundlikud andmed lokaalselt, suurendades turvalisust ja vastavust

### Väikesed keelemudelid (SLMs)

SLMid nagu Phi-4, Mistral-7B ja Gemma on optimeeritud suurte LLM-ide versioonid — treenitud või distilleeritud:
- **Vähenenud mälukasutus**: Piiratud servaseadme mälu tõhus kasutus
- **Madal arvutuskoormus**: Optimeeritud CPU ja serva GPU jõudluseks
- **Kiirem käivitus**: Kiire initsialiseerimine reageerivate rakenduste jaoks

Nad avavad võimsad NLP võimalused, säilitades nõuded:
- **Sisse ehitatud süsteemid**: IoT seadmed ja tööstuslikud kontrollerid
- **Mobiilsed seadmed**: Nutitelefonid ja tahvelarvutid võimega offline kasutada
- **IoT seadmed**: Andurid ja nutiseadmed piiratud ressurssidega
- **Servaserverid**: Kohalikud töötlemise üksused piiratud GPU ressurssidega
- **Isiklikud arvutid**: Lauaarvuti ja sülearvuti juurutusstsenaariumid

## Kursuse moodulid ja navigeerimine

| Moodul | Teema | Fookusala | Peamine sisu | Tase | Kestus |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Sissejuhatus EdgeAI-sse](./introduction.md) | Alused ja kontekst | EdgeAI ülevaade • Tööstusvaldkonna rakendused • SLM sissejuhatus • Õpieesmärgid | Algaja | 1-2 tundi |
| [📚 01](../../Module01) | [EdgeAI põhialused](./Module01/README.md) | Pilve vs serva AI võrdlus | EdgeAI põhialused • Reaalsed juhtumiuuringud • Rakendamise juhend • Servale juurutamine | Algaja | 3-4 tundi |
| [🧠 02](../../Module02) | [SLM mudeli alused](./Module02/README.md) | Mudeliperekonnad & arhitektuur | Phi perekond • Qwen perekond • Gemma perekond • BitNET • μMudel • Phi-Silica | Algaja | 4-5 tundi |
| [🚀 03](../../Module03) | [SLM juurutamise praktika](./Module03/README.md) | Kohalik ja pilvepõhine juurutus | Täiustatud õppimine • Kohalik keskkond • Pilve juurutamine | Kesktase | 4-5 tundi |
| [⚙️ 04](../../Module04) | [Mudelise optimeerimise tööriistad](./Module04/README.md) | Platvormideülene optimeerimine | Sissejuhatus • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Töövoo süntees | Kesktase | 5-6 tundi |
| [🔧 05](../../Module05) | [SLMOps tootmine](./Module05/README.md) | Tootmise operatsioonid | SLMOps ülevaade • Mudeli distilleerimine • Peenhäälestus • Tootmisjuurutus | Edasijõudnu | 5-6 tundi |
| [🤖 06](../../Module06) | [AI agendid ja funktsioonikõned](./Module06/README.md) | Agendi raamistikud ja MCP | Agendi ülevaade • Funktsioonikõned • Mudeli konteksti protokoll | Edasijõudnu | 4-5 tundi |
| [💻 07](../../Module07) | [Platvormi rakendamine](./Module07/README.md) | Platvormideüleste näidete esitamine | AI tööriistakast • Foundry Local • Windowsi arendus | Edasijõudnu | 3-4 tundi |
| [🏭 08](../../Module08) | [Foundry Local tööriistakomplekt](./Module08/README.md) | Tootmisvalmis näited | Näidiserakendused (vt allpool üksikasju) | Ekspert | 8-10 tundi |

### 🏭 **Moodul 08: Näidiserakendused**

- [01: REST Chat kiire stardijuhend](./Module08/samples/01/README.md)
- [02: OpenAI SDK integratsioon](./Module08/samples/02/README.md)
- [03: Mudeli avastamine ja võrdlus](./Module08/samples/03/README.md)
- [04: Chainlit RAG rakendus](./Module08/samples/04/README.md)
- [05: Mitme agendi orkestreerimine](./Module08/samples/05/README.md)
- [06: Mudelid kui tööriistad ruuter](./Module08/samples/06/README.md)
- [07: Otsene API klient](./Module08/samples/07/README.md)
- [08: Windows 11 Chat rakendus](./Module08/samples/08/README.md)
- [09: Täiustatud mitme agendi süsteem](./Module08/samples/09/README.md)
- [10: Foundry tööriistade raamistik](./Module08/samples/10/README.md)

### 🎓 **Töötoa käeline õppeteekond**

Kõikehõlmavad praktilised töötoa materjalid tootmisvalmis rakendustega:

- **[Töötoa juhend](./Workshop/Readme.md)** - Täielikud õpieesmärgid, tulemused ja ressursside navigeerimine
- **Python näited** (6 sessiooni) - Uuendatud parimate tavade, veakäsitluse ja põhjaliku dokumentatsiooniga
- **Jupyteri märkmikud** (8 interaktiivset) - Samm-sammult juhendid, koos võrdlustulemuste ja jõudluse jälgimisega
- **Sessioonijuhendid** - Põhjalikud markdown juhendid iga töötoa sessiooni jaoks
- **Kinnitamistööriistad** - Skriptid, mis kontrollivad koodi kvaliteeti ja käivitavad suitsutestid

**Mida sa ehitad:**
- Kohalikud AI vestlusrakendused voogedastustugiga
- RAG torujuhtmed kvaliteedi hindamisega (RAGAS)
- Mitme mudeli võrdlus- ja võrdlusrakendused
- Mitme agendi orkestreerimissüsteemid
- Intelligentsed mudelirouterid ülesandel põhineva valikuga

### 🎙️ **Agentlik töötoa praktiline osa - AI Podcast Stuudio**

Ehita AI jõul töötav podcast-tootmistorujuhe nullist! See kaasahaarav töötoa osa õpetab sind looma tervikliku mitme agendi süsteemi, mis muudab ideed professionaalseteks podcast episoodideks.
**[🎬 Alusta AI Podcast Stuudio töötuba](./WorkshopForAgentic/README.md)**

**Sinu missioon**: Käivita "Future Bytes" — tehnoloogiapodcast, mida juhivad täielikult sinu ise loodud AI agendid. Pole pilve sõltuvusi, pole API kulusid — kõik töötab kohapeal sinu arvutis.

**Mis teeb selle ainulaadseks:**
- **🤖 Tõeline mitme agendi orkestreerimine** - Ehita spetsialiseerunud AI agente, kes uurivad, kirjutavad ja toodavad heli
- **🎯 Täielik tootmisliin** - Alates teema valimisest kuni lõpliku podcastaudio väljundini
- **💻 100% Kohalik paigaldus** - Kasutab Ollamat ja kohalikke mudeleid (Qwen-3-8B) täieliku privaatsuse ja kontrolli jaoks
- **🎤 Tekst kõneks integratsioon** - Muuda skriptid loomulikult kõlavate mitme kõnelejaga vestlusteks
- **✋ Inimene protsessis** - Kinnituse väravad tagavad kvaliteedi ning säilitavad automatiseerimise

**Kolme peatükiga õpiteekond:**

| Peatükk | Fookus | Olulised oskused | Kestus |
|-----|-------|------------|----------|
| **[1. peatükk: Tutvu oma AI assistentidega](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Ehita oma esimene AI agent | Tööriistade integratsioon • Veebipõhine otsing • Probleemide lahendamine • Agentlik mõtlemine | 2-3 tundi |
| **[2. peatükk: Koosta oma tootmismeeskond](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkestreeri mitu agenti | Meeskonna koordineerimine • Kinnitusprotsessid • DevUI kasutajaliides • Inimese järelvalve | 3-4 tundi |
| **[3. peatükk: Too oma podcast ellu](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Genereeri podcasti heli | Tekst kõneks • Mitme kõneleja süntees • Pikkvormiline heli • Täielik automatiseerimine | 2-3 tundi |

**Kasutatavad tehnoloogiad:**
- **Microsoft Agent Framework** - Mitme agendi orkestreerimine ja koordineerimine
- **Ollama** - Kohalik AI mudelite käituskeskkond (pilve pole vaja)
- **Qwen-3-8B** - Avatud lähtekoodiga keelemudel, mis on optimeeritud agentlikeks ülesanneteks
- **Tekst kõneks APId** - Loomuliku hääle süntees podcastide loomiseks

**Riistvaraline tugi:**
- ✅ **CPU režiim** - Töötab igal kaasaegsel arvutil (soovitatav 8GB+ RAM)
- 🚀 **GPU kiirendus** - Tunduvalt kiirem järeldamise töö NVIDIA/AMD graafikakaartidega
- ⚡ **NPU tugi** - Järgmise põlvkonna närvivõrgu protsessorite kiirendus

**Sobib ideaalselt:**
- Arendajatele, kes õpivad mitme agentiga AI süsteeme
- Kõigile, kes on huvitatud AI automatiseerimisest ja töövoogudest
- Sisuloojatele, kes uurivad AI abil abistatavat tootmist
- Õpilastele, kes õpivad praktilisi AI orkestreerimise mustreid

**Alusta ehitamist**: [🎙️ AI Podcast Stuudio töötuba →](./WorkshopForAgentic/README.md)

### 📊 **Õpiteekonna kokkuvõte**
- **Kogukestus**: 36-45 tundi
- **Algajate tee**: Moodulid 01-02 (7-9 tundi)  
- **Kesktaseme tee**: Moodulid 03-04 (9-11 tundi)
- **Edasijõudnute tee**: Moodulid 05-07 (12-15 tundi)
- **Eksperti tee**: Moodul 08 (8-10 tundi)

## Mida Sa Ehitatud

### 🎯 Põhioskused
- **Serva AI arhitektuur**: Kujunda kohalikud AI süsteemid, millel on pilve integratsioon
- **Mudelite optimeerimine**: Kvantimine ja mudelite tihendamine serva juurutuseks (85% kiirendus, 75% mahu vähendus)
- **Mitme platvormi juurutus**: Windows, mobiilne, manustatud ja pilve-serv hübriidsüsteemid
- **Tootmise tegevused**: Serva AI jälgimine, skaleerimine ja hooldus tootmises

### 🏗️ Praktilised projektid
- **Foundry kohaliku vestluse rakendused**: Windows 11 natiivrakendus koos mudelite vahetamisega
- **Mitme agendi süsteemid**: Koordinaator ja spetsialistist agentide keerukate töövoogude jaoks  
- **RAG rakendused**: Kohalik dokumenditöötlus vektorotsinguga
- **Mudelite marsruuterid**: Tark mudelivalik ülesande analüüsi põhjal
- **API raamistikud**: Tootmisvalmis kliendid voogedastuse ja tervise jälgimisega
- **Platvormideülene tööriistad**: LangChain/Semantic Kernel integratsioonimustrid

### 🏢 Töönduse rakendused
**Tootmine** • **Tervishoid** • **Iseseisvad sõidukid** • **Targad linnad** • **Mobiilirakendused**

## Kiire algus

**Soovitatav õpitee** (kokku 20-30 tundi):

0. **📖 Sissejuhatus** ([Introduction.md](./introduction.md)): EdgeAI alus + tööstuse kontekst + õpiraamistik
1. **📚 Alused** (Moodulid 01-02): EdgeAI kontseptsioonid + SLM mudeliperekonnad
2. **⚙️ Optimeerimine** (Moodulid 03-04): Juurutus + kvantimise raamistikud  
3. **🚀 Tootmine** (Moodulid 05-06): SLMOps + AI agendid + funktsioonikutsed
4. **💻 Rakendamine** (Moodulid 07-08): Platvorminäited + Foundry Local tööriistakomplekt

Igas moodulis on teooria, praktilised harjutused ja tootmisvalmis koodinäited.

## Karjääri mõju

**Tehnilised rollid**: EdgeAI lahenduste arhitekt • Masinõppe insener (Edge) • IoT AI arendaja • Mobiili AI arendaja

**Tööstusharud**: Tootmine 4.0 • Tervishoiutehnoloogia • Iseseisvad süsteemid • FinTech • Tarbijaelektroonika

**Portfoolio projektid**: Mitme agendi süsteemid • Tootmis-RAG rakendused • Platvormideülene juurutus • Tulemuste optimeerimine

## Koodihoidla struktuur

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

## Kursuse esiletõstud

✅ **Progressiivne õppimine**: Teooria → Praktika → Tootmisse juurutamine  
✅ **Reaalsed juhtumiuuringud**: Microsoft, Japan Airlines, ettevõtete rakendused  
✅ **Praktilised näited**: 50+ näidet, 10 põhjalikku Foundry Local demot  
✅ **Tulemuslikkuse fookus**: 85% kiirendused, 75% mahu vähendused  
✅ **Mitme platvormi tugi**: Windows, mobiil, manustatud, pilve-serv hübriid  
✅ **Tootmisvalmidus**: Jälgimine, skaleerimine, turvalisus, vastavus

📖 **[Õpijuhend saadaval](STUDY_GUIDE.md)**: Struktureeritud 20-tunnine õpitee koos ajaplaneerimise ja enesehindamise tööriistadega.

---

**EdgeAI on AI juurutamise tulevik**: kohalik prioriteet, privaatsust säilitav ja tõhus. Oma järgmise põlvkonna intelligentsete rakenduste loomiseks valda neid oskusi.

## Teised kursused

Meie meeskond valmistab veel kursuseid! Vaata:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j algajatele](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js algajatele](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agendid
[![AZD algajatele](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI algajatele](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP algajatele](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentide algajatele](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivse AI seeria
[![Generatiivne AI algajatele](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Põhiõpe
[![ML algajatele](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Andmeteadus algajatele](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI algajatele](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Küberkaitse algajatele](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Veebiarendus algajatele](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT algajatele](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR arendus algajatele](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copiloti seeria
[![Copilot AI paarisprogrammeerimiseks](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Abi saamine

Kui jääd hätta või sul on küsimusi AI rakenduste loomise kohta, liitu:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kui sul on toote kohta tagasisidet või ehitamise käigus vigu, külasta:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, olge teadlikud, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleb pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tekkida võivate arusaamatuste või väärarusaamade eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->