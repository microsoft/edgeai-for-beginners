# Töötuba Märkmikud

> **Interaktiivsed Jupyter Notebookid praktiliseks Edge AI õppimiseks**
>
> Järjestikused, iseseisvalt läbitavad juhendid, mis arenevad lihtsatest vestluslahendustest kuni keerukate multi-agent süsteemideni, kasutades Microsoft Foundry Locali ja väikeseid keelemudeleid.

---

## 📖 Sissejuhatus

Tere tulemast **EdgeAI algajatele mõeldud töötuba märkmike** kogusse. Need interaktiivsed Jupyter Notebookid pakuvad praktilist õppimiskogemust, kus saate reaalajas kirjutada, käivitada ja katsetada Edge AI koodi.

### Miks Jupyter Notebookid?

Erinevalt traditsioonilistest juhenditest pakuvad need märkmikud:

- **Interaktiivne õppimine**: Käivitage koodirakke ja näete tulemusi kohe
- **Katsetamine**: Muutke parameetreid ja jälgige muudatusi reaalajas
- **Dokumentatsioon**: Sisseehitatud selgitused ja markdown-rakud juhendavad teid kontseptsioonide kaudu
- **Reprodutseeritavus**: Täielikud töötavad näited, mida saate viidata ja uuesti kasutada
- **Visualiseerimine**: Vaadake jõudlusmõõdikuid, vektorite paigutusi ja tulemusi otse märkmikus

### Mis teeb need märkmikud eriliseks?

Iga märkmik on loodud järgides **tootmisvalmis parimaid praktikaid**:

✅ **Põhjalik veakäsitlus** - Sujuv degradeerumine ja informatiivsed veateated  
✅ **Tüübiviited ja dokumentatsioon** - Selged funktsioonide signatuurid ja dokumendijuhised  
✅ **Jõudluse jälgimine** - Tokenite kasutuse jälgimine ja latentsuse mõõtmine  
✅ **Modulaarne disain** - Taaskasutatavad mustrid, mida saate oma projektides kohandada  
✅ **Järjestikune keerukus** - Süsteemne ülesehitus eelnevate sessioonide põhjal

---

## 🎯 Õpieesmärgid

### Põhioskused, mida arendate

Töötades läbi need märkmikud, omandate:

1. **Kohaliku AI teenuse haldamine**
   - Konfigureerige ja hallake Microsoft Foundry Local teenuseid
   - Valige ja laadige oma riistvarale sobivad mudelid
   - Jälgige ressursikasutust ja optimeerige jõudlust
   - Käsitlege teenuste avastamist ja tervisekontrolli

2. **AI rakenduste arendamine**
   - Rakendage OpenAI-ga ühilduvaid vestluslahendusi kohapeal
   - Looge voogesituse liidesed parema kasutajakogemuse jaoks
   - Kujundage tõhusad juhised väikestele keelemudelitele
   - Integreerige kohalikud mudelid rakendustesse

3. **Retrieval Augmented Generation (RAG)**
   - Looge semantiline otsing vektorite paigutustega
   - Siduge LLM-i vastused valdkonnaspetsiifiliste dokumentidega
   - Hinnake RAG kvaliteeti RAGAS mõõdikutega
   - Laiendage prototüübist tootmiseni

4. **Jõudluse optimeerimine**
   - Võrdlege süsteemselt mitut mudelit
   - Mõõtke latentsust, läbilaskevõimet ja esimese tokeni aega
   - Võrrelge väikeseid keelemudeleid suurte keelemudelitega
   - Valige optimaalsed mudelid jõudluse/kvaliteedi kompromisside põhjal

5. **Multi-agent orkestreerimine**
   - Kujundage spetsialiseeritud agendid erinevate ülesannete jaoks
   - Rakendage agentide mälu ja konteksti haldamist
   - Koordineerige mitut agenti keerukates töövoogudes
   - Looge koordinaatori mustrid agentide koostööks

6. **Intelligentne mudelite suunamine**
   - Rakendage kavatsuste tuvastamist ja mustrite sobitamist
   - Suunake päringud automaatselt sobivatele mudelitele
   - Looge mitmeastmelised torud (plaan → teostus → täpsustus)
   - Kujundage skaleeritavad mudelid-tööriistad arhitektuurid

---

## 🎓 Õpitulemused

### Mida te ehitate

| Märkmik | Tulemus | Näidatud oskused | Raskusaste |
|---------|---------|------------------|------------|
| **Sessioon 01** | Vestlusrakendus voogesitusega | Teenuse seadistamine, põhilised vestlused, voogesituse UX | ⭐ Algaja |
| **Sessioon 02 (RAG)** | RAG toru koos hindamisega | Vektorite paigutused, semantiline otsing, kvaliteedimõõdikud | ⭐⭐ Keskmine |
| **Sessioon 02 (Hindamine)** | RAG kvaliteedi hindaja | RAGAS mõõdikud, süsteemne hindamine | ⭐⭐ Keskmine |
| **Sessioon 03** | Multi-mudeli võrdlus | Jõudluse mõõtmine, mudelite võrdlus | ⭐⭐ Keskmine |
| **Sessioon 04** | SLM vs LLM võrdleja | Kompromisside analüüs, optimeerimisstrateegiad | ⭐⭐⭐ Edasijõudnud |
| **Sessioon 05** | Multi-agent orkestreerija | Agentide disain, mälu, koordineerimine | ⭐⭐⭐ Edasijõudnud |
| **Sessioon 06 (Router)** | Intelligentne suunamissüsteem | Kavatsuste tuvastamine, mudelite valik | ⭐⭐⭐ Edasijõudnud |
| **Sessioon 06 (Toru)** | Mitmeastmeline toru | Plaan/teostus/täpsustus töövood | ⭐⭐⭐ Edasijõudnud |

### Kompetentsuse areng

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Töötuba ajakava

### 🚀 Poolpäevane töötuba (3,5 tundi)

**Sobib: Meeskonna koolitused, häkatonid, konverentsi töötoad**

| Aeg | Kestus | Sessioon | Teemad | Tegevused |
|-----|--------|----------|--------|-----------|
| **0:00** | 30 min | Seadistamine ja sissejuhatus | Keskkonna seadistamine, Foundry Locali paigaldamine | Paigaldage sõltuvused, kontrollige seadistust |
| **0:30** | 30 min | Sessioon 01 | Põhilised vestlused, voogesitus | Käivitage märkmik, muutke juhiseid |
| **1:00** | 45 min | Sessioon 02 | RAG toru, vektorid, hindamine | Ehitage RAG süsteem, testige päringuid |
| **1:45** | 15 min | Paus | ☕ Kohv ja küsimused | — |
| **2:00** | 30 min | Sessioon 03 | Multi-mudeli võrdlus | Võrrelge 3+ mudelit |
| **2:30** | 30 min | Sessioon 04 | SLM vs LLM kompromissid | Analüüsige jõudlust/kvaliteeti |
| **3:00** | 30 min | Sessioon 05-06 | Multi-agent süsteemid ja suunamine | Uurige keerukaid mustreid |

**Tulemus**: Osalejad lahkuvad 6 töötava Edge AI rakenduse ja tootmisvalmis koodimustritega.

---

### 🎓 Täispäevane töötuba (6 tundi)

**Sobib: Süvitsi minev koolitus, bootcampid, ülikoolikursused**

| Aeg | Kestus | Sessioon | Teemad | Tegevused |
|-----|--------|----------|--------|-----------|
| **0:00** | 45 min | Seadistamine ja teooria | Keskkonna seadistamine, Edge AI põhialused | Paigaldage, kontrollige, arutage kasutusjuhtumeid |
| **0:45** | 45 min | Sessioon 01 | Vestluste süvitsi uurimine | Rakendage põhilised ja voogesituse vestlused |
| **1:30** | 30 min | Paus | ☕ Kohv ja võrgustumine | — |
| **2:00** | 60 min | Sessioon 02 (Mõlemad) | RAG toru + RAGAS hindamine | Ehitage täielik RAG süsteem |
| **3:00** | 30 min | Praktiline labor 1 | Kohandatud RAG teie valdkonnale | Rakendage oma dokumentidele |
| **3:30** | 30 min | Lõuna | 🍽️ | — |
| **4:00** | 45 min | Sessioon 03 | Võrdlusmetoodika | Süsteemne mudelite võrdlus |
| **4:45** | 45 min | Sessioon 04 | Optimeerimisstrateegiad | SLM vs LLM analüüs |
| **5:30** | 60 min | Sessioon 05-06 | Täiustatud orkestreerimine | Multi-agent süsteemid, suunamine |
| **6:30** | 30 min | Praktiline labor 2 | Ehitage kohandatud agentide süsteem | Kujundage oma orkestreerija |

**Tulemus**: Sügav arusaam Edge AI mustritest pluss 2 kohandatud projekti.

---

### 📚 Iseseisev õppimine (2 nädalat)

**Sobib: Individuaalsed õppijad, veebikursused, iseseisev õpe**

#### 1. nädal: Põhitõed (6 tundi)

| Päev | Fookus | Kestus | Märkmikud | Kodutöö |
|------|-------|--------|-----------|---------|
| **Esm** | Seadistamine ja põhialused | 1,5 tundi | Sessioon 01 | Muutke juhiseid, testige voogesitust |
| **Kolm** | RAG põhialused | 2 tundi | Sessioon 02 (mõlemad) | Lisage oma dokumendid |
| **Reed** | Võrdlus | 1,5 tundi | Sessioon 03 | Võrrelge täiendavaid mudeleid |
| **Laup** | Ülevaade ja praktika | 1 tund | Kõik 1. nädala | Täitke harjutused, siluge |

#### 2. nädal: Täiustatud (5 tundi)

| Päev | Fookus | Kestus | Märkmikud | Kodutöö |
|------|-------|--------|-----------|---------|
| **Esm** | Optimeerimine | 1,5 tundi | Sessioon 04 | Dokumenteerige kompromissid |
| **Kolm** | Multi-agent süsteemid | 2 tundi | Sessioon 05 | Kujundage kohandatud agendid |
| **Reed** | Intelligentne suunamine | 1,5 tundi | Sessioon 06 (mõlemad) | Ehitage suunamisloogika |
| **Laup** | Lõppprojekt | 2 tundi | Integratsioon | Kombineerige mitu mustrit |

**Tulemus**: Edge AI mustrite valdamine pluss portfoolio projekt.

---

## 📔 Märkmike kirjeldused

### 📘 Sessioon 01: Vestluse algus
**Fail**: `session01_chat_bootstrap.ipynb`  
**Kestus**: 20-30 minutit  
**Eeltingimused**: Puuduvad  
**Raskusaste**: ⭐ Algaja

**Mida õpite**:
- Paigaldage ja konfigureerige Foundry Local Python SDK
- Kasutage `FoundryLocalManager` automaatseks teenuste avastamiseks
- Rakendage põhilised vestlused OpenAI-ga ühilduva API-ga
- Looge voogesituse vastused parema kasutajakogemuse jaoks
- Käsitlege vigu ja teenuse kättesaamatust sujuvalt

**Põhikontseptsioonid**: Teenuse haldamine, vestlused, voogesitus, veakäsitlus

**Mida ehitate**: Interaktiivne vestlusrakendus voogesituse toega

---

### 📗 Sessioon 02: RAG toru
**Fail**: `session02_rag_pipeline.ipynb`  
**Kestus**: 30-45 minutit  
**Eeltingimused**: Sessioon 01  
**Raskusaste**: ⭐⭐ Keskmine

**Mida õpite**:
- Rakendage Retrieval Augmented Generation (RAG) mustrit
- Looge vektorite paigutused lause-transformeritega
- Ehitage semantiline otsing koos kosinuse sarnasusega
- Siduge LLM-i vastused valdkonna dokumentidega
- Käsitlege valikulisi sõltuvusi importimise kaitsetega

**Põhikontseptsioonid**: RAG arhitektuur, vektorite paigutused, semantiline otsing, vektorite sarnasus

**Mida ehitate**: Dokumentidega seotud küsimuste-vastuste süsteem

---

### 📗 Sessioon 02: RAG hindamine RAGAS-iga
**Fail**: `session02_rag_eval_ragas.ipynb`  
**Kestus**: 30-45 minutit  
**Eeltingimused**: Sessioon 02 RAG toru  
**Raskusaste**: ⭐⭐ Keskmine

**Mida õpite**:
- Hinnake RAG kvaliteeti tööstusharu standardsete mõõdikutega
- Mõõtke konteksti asjakohasust, vastuse asjakohasust, usaldusväärsust
- Kasutage RAGAS raamistikku süsteemseks hindamiseks
- Tuvastage ja parandage RAG kvaliteediprobleeme
- Looge hindamisandmestikud oma valdkonnale

**Põhikontseptsioonid**: RAG hindamine, RAGAS mõõdikud, kvaliteedi mõõtmine, süsteemne testimine

**Mida ehitate**: RAG kvaliteedi hindamise raamistik

---

### 📙 Sessioon 03: OSS mudelite võrdlus
**Fail**: `session03_benchmark_oss_models.ipynb`  
**Kestus**: 30-45 minutit  
**Eeltingimused**: Sessioon 01  
**Raskusaste**: ⭐⭐ Keskmine

**Mida õpite**:
- Süsteemselt võrrelge mitut mudelit
- Mõõtke latentsust, läbilaskevõimet, esimese tokeni aega
- Rakendage sujuvat degradeerumist mudelite rikete korral
- Võrrelge jõudlust mudelite perekondade vahel
- Visualiseerige ja analüüsige võrdlustulemusi

**Põhikontseptsioonid**: Jõudluse võrdlus, latentsuse mõõtmine, mudelite võrdlus, statistiline analüüs

**Mida ehitate**: Multi-mudeli võrdluskomplekt

---

### 📙 Sessioon 04: Mudelite võrdlus (SLM vs LLM)
**Fail**: `session04_model_compare.ipynb`  
**Kestus**: 30-45 minutit  
**Eeltingimused**: Sessioonid 01, 03  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud

**Mida õpite**:
- Võrrelge väikeseid keelemudeleid suurte keelemudelitega
- Analüüsige jõudluse ja kvaliteedi kompromisse
- Mõõtke serva-sobivuse mõõdikuid
- Valige optimaalsed mudelid juurutuspiirangute põhjal
- Dokumenteerige mudelite valiku otsustuskriteeriumid

**Põhikontseptsioonid**: Mudelite valik, kompromisside analüüs, optimeerimisstrateegiad, juurutusplaneerimine

**Mida ehitate**: SLM vs LLM võrdlusraamistik

---

### 📕 Sessioon 05: Multi-agent orkestreerija
**Fail**: `session05_agents_orchestrator.ipynb`  
**Kestus**: 45-60 minutit  
**Eeltingimused**: Sessioonid 01-02  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud

**Mida õpite**:
- Kujundage spetsialiseeritud agendid erinevate ülesannete jaoks
- Rakendage agentide mälu ja konteksti haldamist
- Looge koordinaatori mustrid agentide koostööks
- Käsitlege agentide suhtlust ja üleandmisi
- Jälgige multi-agent süsteemi jõudlust

**Põhikontseptsioonid**: Agentide arhitektuur, koordinaatori mustrid, mälu haldamine, agentide orkestreerimine

**Mida ehitate**: Multi-agent süsteem koos koordinaatori ja spetsialistidega

---

### 📕 Sessioon 06: Mudelite suunaja
**Fail**: `session06_models_router.ipynb`  
**Kestus**: 30-45 minutit  
**Eeltingimused**: Sessioonid 01, 03  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud
- Kujunda skaleeritavaid mudel-tööriistade arhitektuure

**Põhimõisted**: Toru arhitektuur, mitmeastmeline töötlemine, vigade taastamine, skaleeritavuse mustrid

**Sa lood**: Mitmeastmeline intelligentne toru koos suunamisega

---

## 🚀 Alustamine

### Eeltingimused

**Süsteeminõuded**:
- **OS**: Windows 10/11, macOS 11+ või Linux (Ubuntu 20.04+)
- **RAM**: Minimaalselt 8GB, soovitatavalt 16GB+
- **Salvestusruum**: Vaba ruumi vähemalt 10GB mudelite jaoks
- **Riistvara**: CPU koos AVX2; GPU (CUDA, Qualcomm NPU) valikuline

**Tarkvaranõuded**:
- **Python 3.8+** koos pip-iga
- **Jupyter Notebook** või **VS Code** Jupyter laiendiga
- **Microsoft Foundry Local** paigaldatud ja seadistatud
- **Git** (hoidla kloonimiseks)

### Paigaldamise sammud

#### 1. Paigalda Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Paigaldamise kontroll**:
```bash
foundry --version
```

#### 2. Seadista Python keskkond

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Käivita Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Ava Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Kiire kontroll

Käivita see Python-i lahtris, et kontrollida seadistust:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Oodatav väljund**: Tervitussõnum kohalikult mudelilt.

---

## 📝 Töötoa parimad praktikad

### Juhendajatele

**Enne töötuba**:
- ✅ Saada paigaldusjuhised 1 nädal enne
- ✅ Testi kõik märkmikud sihtseadmel
- ✅ Valmista ette tõrkeotsingu juhend levinud probleemide jaoks
- ✅ Hoia varumudelid valmis (phi-3.5-mini, kui phi-4-mini ebaõnnestub)
- ✅ Loo jagatud vestluskanal küsimuste jaoks

**Töötoa ajal**:
- ✅ Alusta kiire keskkonna kontrolliga (5 minutit)
- ✅ Jaga tõrkeotsingu ressursse kohe
- ✅ Julgusta katsetamist ja muudatusi
- ✅ Kasuta pause strateegiliselt (pärast iga 2 sessiooni)
- ✅ Hoia TAsid saadaval 1-1 abi jaoks

**Pärast töötuba**:
- ✅ Jaga täielikult töötavaid märkmikke ja lahendusi
- ✅ Paku linke lisamaterjalidele
- ✅ Loo tagasisideküsitlus parendamiseks
- ✅ Paku järelküsimuste jaoks konsultatsiooniaegu

### Õppijatele

**Maksimeeri oma õppimist**:
- ✅ Lõpeta seadistamine enne töötoa algust
- ✅ Käivita iga koodilahter ise (ära lihtsalt loe)
- ✅ Katseta parameetrite ja käskudega
- ✅ Tee märkmeid tähelepanekute ja probleemide kohta
- ✅ Küsi küsimusi, kui jääd hätta (teistel võib olla sama küsimus)

**Levinud vead, mida vältida**:
- ❌ Lahtrite käivitamise järjekorra vahelejätmine (käivita järjestikku)
- ❌ Vigade sõnumite hoolimatu lugemine
- ❌ Kiirustamine ilma mõistmata
- ❌ Markdown selgituste ignoreerimine
- ❌ Muudetud märkmike salvestamata jätmine

**Tõrkeotsingu näpunäited**:
1. **Teenust ei käivitu**: Kontrolli `foundry service status`
2. **Importimise vead**: Veendu, et virtuaalne keskkond on aktiveeritud
3. **Mudel puudub**: Käivita `foundry model ls`, et näha laaditud mudeleid
4. **Aeglane jõudlus**: Kontrolli RAM-i kasutust, sulge teised rakendused
5. **Ootamatud tulemused**: Taaskäivita kernel ja käivita kõik lahtrid algusest

---

## 🔗 Lisamaterjalid

### Töötoa materjalid

- **[Töötoa põhijuhend](../Readme.md)** - Ülevaade, õpieesmärgid, karjäärivõimalused
- **[Python näited](../../../../Workshop/samples)** - Vastavad Python skriptid iga sessiooni jaoks
- **[Sessiooni juhendid](../../../../Workshop)** - Üksikasjalikud markdown juhendid (Session01-06)
- **[Skriptid](../../../../Workshop/scripts)** - Valideerimise ja testimise tööriistad
- **[Tõrkeotsing](./TROUBLESHOOTING.md)** - Levinud probleemid ja lahendused
- **[Kiire algus](./quickstart.md)** - Kiire alustamise juhend

### Dokumentatsioon

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Microsofti ametlik dokumentatsioon
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK viide
- **[Sentence Transformers](https://www.sbert.net/)** - Embedding mudelite dokumentatsioon
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG hindamismõõdikud

### Kogukond

- **[GitHub Arutelud](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Küsi küsimusi, jaga projekte
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Reaalajas kogukonna tugi
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tehniline Q&A

---

## 🎯 Õppimise teekonna soovitused

### Algajate rada (alusta siit)

1. **Sessioon 01** - Vestluse algus
2. **Sessioon 02** - RAG toru
3. **Sessioon 03** - Mudelite võrdlus

**Aeg**: ~2 tundi | **Fookus**: Põhimustrid

---

### Kesktase

1. Lõpeta algajate rada
2. **Sessioon 02** - RAG hindamine
3. **Sessioon 04** - Mudelite võrdlus

**Aeg**: ~4 tundi | **Fookus**: Kvaliteet ja optimeerimine

---

### Edasijõudnute rada (täielik töötuba)

1. Lõpeta kesktase
2. **Sessioon 05** - Multi-agent orkestreerija
3. **Sessioon 06** - Mudelite suunaja
4. **Sessioon 06** - Mitmeastmeline toru

**Aeg**: ~6 tundi | **Fookus**: Tootmismustrid

---

### Kohandatud projekti rada

1. Lõpeta algajate rada (Sessioonid 01-03)
2. Vali ÜKS edasijõudnud sessioon vastavalt oma eesmärgile:
   - **RAG rakenduse loomine?** → Sessioon 02 hindamine
   - **Jõudluse optimeerimine?** → Sessioon 04 võrdlus
   - **Komplekssed töövood?** → Sessioon 05 orkestreerija
   - **Skaleeritav arhitektuur?** → Sessioon 06 suunaja + toru

**Aeg**: ~3 tundi | **Fookus**: Projekti-spetsiifilised oskused

---

## 📊 Edu mõõdikud

Jälgi oma edusamme nende verstapostidega:

- [ ] **Seadistamine lõpetatud** - Foundry Local töötab, kõik sõltuvused paigaldatud
- [ ] **Esimene vestlus** - Sessioon 01 lõpetatud, voogvestlus töötab
- [ ] **RAG loodud** - Sessioon 02 lõpetatud, dokumendi QA süsteem funktsionaalne
- [ ] **Mudelid võrreldud** - Sessioon 03 lõpetatud, jõudlusandmed kogutud
- [ ] **Kompromissid analüüsitud** - Sessioon 04 lõpetatud, mudeli valikukriteeriumid dokumenteeritud
- [ ] **Agentide orkestreerimine** - Sessioon 05 lõpetatud, multi-agent süsteem töötab
- [ ] **Suunamine rakendatud** - Sessioon 06 lõpetatud, intelligentne mudeli valik funktsionaalne
- [ ] **Kohandatud projekt** - Töötoa mustrid rakendatud oma kasutusjuhtumile

---

## 🤝 Kaasautoriks saamine

Leidsid probleemi või sul on ettepanek? Ootame panustamist!

- **Teata probleemidest**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Tee ettepanekuid**: [GitHub Arutelud](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Esita PR-id**: Järgi [Kaasautorluse juhiseid](../../AGENTS.md)

---

## 📄 Litsents

See töötuba on osa [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) hoidlast ja litsentseeritud [MIT litsentsi](../../../../LICENSE) alusel.

---

**Valmis looma tootmiskõlblikke Edge AI rakendusi?**  
**Alusta [Sessioon 01: Vestluse algus](./session01_chat_bootstrap.ipynb) →**

---

*Viimati uuendatud: 8. oktoober 2025 | Töötoa versioon: 2.0*

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.