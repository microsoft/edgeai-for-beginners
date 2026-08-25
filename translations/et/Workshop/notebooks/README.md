# Töötubade märkmikud

> **Interaktiivsed Jupyteri märkmikud praktiliseks Edge AI õppimiseks**
>
> Progressiivsed, iseseisvas tempos juhendatud õppetunnid, mis arenevad lihtsatest jutukompleti näidetest kuni keerukate mitmeagendiliste süsteemideni, kasutades Microsoft Foundry Locali ja väikeseid keelemudeleid.

---

## 📖 Sissejuhatus

Tere tulemast **EdgeAI algajate töötubade märkmike** kogumikku. Need interaktiivsed Jupyteri märkmikud pakuvad praktilist õppimiskogemust, kus kirjutate, käivitate ja katsetate Edge AI koodi reaalajas.

### Miks Jupyteri märkmikud?

Erinevalt traditsioonilistest juhenditest pakuvad need märkmikud:

- **Interaktiivne õppimine**: Käivitage koodiblokke ja näete koheseid tulemusi
- **Katsetamine**: Muutke parameetreid ja jälgige muudatusi reaalajas
- **Dokumentatsioon**: Selgitused ja markdown-rakud juhendavad teid kontseptsioonide kaudu
- **Taaskäivitatavus**: Töökindlad näited, mida saate uuesti kasutada ja viidata
- **Visualiseerimine**: Vaadake jõudlusmõõdikuid, manustusi ja tulemusi otse märkmikus

### Mis teeb need märkmikud eriliseks?

Iga märkmik on loodud järgides **tootmisvalmis parimaid tavasid**:

✅ **Täpne vigade käsitlemine** - Delikaatne katkestamine ja informatiivsed veateated  
✅ **Tüübi vihjed & dokumentatsioon** - Selged funktsioonide signatuurid ja dokumentatsioonitekstid  
✅ **Jõudluse jälgimine** - Tokeni kasutuse jälgimine ja latentsuse mõõtmised  
✅ **Mooduldisain** - Taaskasutatavad mustrid, mida saate oma projektides kohandada  
✅ **Järk-järguline keerukus** - Süsteemne ehitamine varasemate õppesessioonide põhjal

---

## 🎯 Õpieesmärgid

### Põhioskused, mida arendate

Nende märkmike läbimisega omandate:

1. **Kohaliku AI-teenuse haldamine**
   - Konfigureerige ja haldage Microsoft Foundry Local teenuseid
   - Valige ja laadige sobivad mudelid vastavalt riistvarale
   - Jälgige ressursikasutust ja optimeerige jõudlust
   - Halduge teenuse leidmise ja tervisekontrolliga

2. **AI rakenduste arendus**
   - Rakendage kohalikus keskkonnas OpenAI-ühilduvaid jutukomplekte
   - Looge voogedastuse liidesed parema kasutajakogemuse jaoks
   - Kujundage tõhusaid sisendeid väikestele keelemudelitele
   - Integreerige kohalikud mudelid rakendustesse

3. **Taastekstimislaiendatud genereerimine (RAG)**
   - Looge semantiline otsing vektorimanustustega
   - Põhjendage LLM vastuseid domeenispetsiifiliste dokumentidega
   - Hinnake RAG kvaliteeti RAGAS mõõdikutega
   - Skaalake prototüübist tootmiseni

4. **Jõudluse optimeerimine**
   - Võrrelge systemaalselt mitut mudelit
   - Mõõtke latentsust, läbilaskevõimet ja esimese tokeni aega
   - Võrrelge väikesi ja suuri keelemudeleid
   - Valige optimaalne mudel jõudluse ja kvaliteedi kompromisside põhjal

5. **Mitme agendi orkestreerimine**
   - Kujundage spetsialiseeritud agendid eri ülesannete jaoks
   - Rakendage agendi mälu ja konteksti haldust
   - Koordineerige mitut agenti keerulistes töövoogudes
   - Looge koordinaatorite mustrid agendite koostööks

6. **Intelligentne mudelite marsruutimine**
   - Rakendage kavatsuste tuvastamist ja mustrimatchimist
   - Marsruutige päringud sobivatele mudelitele automaatselt
   - Koostage mitmeastmelised töövood (planeeri → käivita → täienda)
   - Kujundage skaleeritavaid mudelitööriistade arhitektuure

---

## 🎓 Õpitulemused

### Mida te ehitate

| Märkmik | Toodang | Nähtavad oskused | Raskusaste |
|----------|-------------|---------------------|------------|
| **Sessioon 01** | Vestlusrakendus voogedastusega | Teenuse seadistamine, põhilised kompletid, voogedastus UX | ⭐ Algaja |
| **Sessioon 02 (RAG)** | RAG töövoog koos hindamisega | Manustused, semantiline otsing, kvaliteedimõõdikud | ⭐⭐ Kesktase |
| **Sessioon 02 (Hindamine)** | RAG kvaliteedihindaja | RAGAS mõõdikud, süstemaatiline hindamine | ⭐⭐ Kesktase |
| **Sessioon 03** | Mitmemudeline võrdlus | Jõudluse mõõtmine, mudelite võrdlus | ⭐⭐ Kesktase |
| **Sessioon 04** | SLM vs LLM võrdleja | Kompromisside analüüs, optimeerimisstrateegiad | ⭐⭐⭐ Edasijõudnud |
| **Sessioon 05** | Mitmeagendi orkestreerija | Agendi kujundus, mälu, koordineerimine | ⭐⭐⭐ Edasijõudnud |
| **Sessioon 06 (Marsruutija)** | Intelligentsed marsruutimissüsteemid | Kavatsuste tuvastamine, mudelivalik | ⭐⭐⭐ Edasijõudnud |
| **Sessioon 06 (Töövoog)** | Mitmeastmeline töövoog | Planeeri/käivita/täienda töövood | ⭐⭐⭐ Edasijõudnud |

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

**Sobib ideaalselt: meeskonnatöö koolitused, hackathonid, konverentsi töötubadeks**

| Kellaaeg | Kestus | Sessioon | Teemad | Tegevused |
|------|----------|---------|--------|------------|
| **0:00** | 30 min | Seadistus & Sissejuhatus | Keskkonna seadistamine, Foundry Local paigaldus | Paigalda sõltuvused, kontrolli seadistust |
| **0:30** | 30 min | Sessioon 01 | Põhilised jutukompletid, voogedastus | Käivita märkmik, muuda sisendeid |
| **1:00** | 45 min | Sessioon 02 | RAG töövoog, manustused, hindamine | Ehita RAG süsteem, testi päringuid |
| **1:45** | 15 min | Paus | ☕ Kohv ja küsimused | — |
| **2:00** | 30 min | Sessioon 03 | Mitmemudeline võrdlus | Võrdle 3+ mudelit |
| **2:30** | 30 min | Sessioon 04 | SLM vs LLM kompromissid | Analüüsi jõudlus/kvaliteet |
| **3:00** | 30 min | Sessioon 05-06 | Mitmeagendilised süsteemid & marsruutimine | Uuri edasiarendatud mustreid |

**Tulemus**: Osalejad lahkuvad 6 töötava Edge AI rakenduse ja tootmisvalmis koodimustritega.

---

### 🎓 Täispäevane töötuba (6 tundi)

**Sobib ideaalselt: põhjalik koolitus, bootcampid, ülikoolikursused**

| Kellaaeg | Kestus | Sessioon | Teemad | Tegevused |
|------|----------|---------|--------|------------|
| **0:00** | 45 min | Seadistus & Teooria | Keskkonna seadistamine, Edge AI põhialused | Paigalda, kontrolli, arutle kasutusjuhtumite üle |
| **0:45** | 45 min | Sessioon 01 | Sügav pilguheit jutukomplektidele | Rakenda põhilisi ja voogedastuse vestlusi |
| **1:30** | 30 min | Paus | ☕ Kohv ja võrgustiku loomine | — |
| **2:00** | 60 min | Sessioon 02 (mõlemad) | RAG töövoog + RAGAS hindamine | Ehita täielik RAG süsteem |
| **3:00** | 30 min | Praktiline labor 1 | Kohandatud RAG oma domeenile | Rakenda oma dokumentidele |
| **3:30** | 30 min | Lõunapaus | 🍽️ | — |
| **4:00** | 45 min | Sessioon 03 | Võrdlusmetoodika | Süsteemne mudelite võrdlus |
| **4:45** | 45 min | Sessioon 04 | Optimeerimisstrateegiad | SLM vs LLM analüüs |
| **5:30** | 60 min | Sessioon 05-06 | Edasijõudnud orkestreerimine | Mitmeagendilised süsteemid, marsruutimine |
| **6:30** | 30 min | Praktiline labor 2 | Ehita kohandatud agendisüsteem | Kujunda oma orkestreerija |

**Tulemus**: Sügav Edge AI mustrite mõistmine pluss 2 kohandatud projekti.

---

### 📚 Iseseisev õppimine (2 nädalat)

**Sobib ideaalselt: iseseisvad õppijad, veebikursused, iseseisev õpe**

#### 1. nädal: Alused (6 tundi)

| Päev | Fookus | Kestus | Märkmikud | Kodutöö |
|-----|-------|----------|-----------|----------|
| **Esmaspäev** | Seadistus & Alused | 1,5 tundi | Sessioon 01 | Muutke sisendeid, testige voogedastust |
| **Kolmapäev** | RAG alused | 2 tundi | Sessioon 02 (mõlemad) | Lisage oma dokumendid |
| **Reede** | Võrdlus | 1,5 tundi | Sessioon 03 | Võrrelge täiendavaid mudeleid |
| **Laupäev** | Kordamine & Praktika | 1 tund | Kõik 1. nädalast | Täitke harjutusi, siluge vigu |

#### 2. nädal: Edasijõudnud (5 tundi)

| Päev | Fookus | Kestus | Märkmikud | Kodutöö |
|-----|-------|----------|-----------|----------|
| **Esmaspäev** | Optimeerimine | 1,5 tundi | Sessioon 04 | Dokumenteerige kompromissid |
| **Kolmapäev** | Mitmeagendilised süsteemid | 2 tundi | Sessioon 05 | Kujundage kohandatud agendid |
| **Reede** | Intelligentsed marsruudid | 1,5 tundi | Sessioon 06 (mõlemad) | Looge marsruutimise loogika |
| **Laupäev** | Lõppprojekt | 2 tundi | Integreerimine | Kombineerige mitu mustrit |

**Tulemus**: Edge AI mustrite valdamine ja portfoolioprojekt.

---

## 📔 Märkmike kirjeldused

### 📘 Sessioon 01: Jutuka algus
**Fail**: `session01_chat_bootstrap.ipynb`  
**Kestus**: 20-30 minutit  
**Eeldused**: Puuduvad  
**Raskusaste**: ⭐ Algaja

**Mida õpite**:
- Paigaldage ja konfigureerige Foundry Local Python SDK
- Kasutage `FoundryLocalManager` automaatseks teenuste leidmiseks
- Rakendage põhilised vestluskõnede lõpetused OpenAI-ühilduva API-ga
- Looge voogedastuse vastused parema kasutajakogemuse tagamiseks
- Haldage vigu ja teenuse kättesaamatusi ladusalt

**Põhikontseptsioonid**: Teenuse haldus, jutukompletid, voogedastus, vigade käsitlemine

**Te ehitate**: Interaktiivne juturakendus koos voogedastuse toega

---

### 📗 Sessioon 02: RAG töövoog
**Fail**: `session02_rag_pipeline.ipynb`  
**Kestus**: 30-45 minutit  
**Eeldused**: Sessioon 01  
**Raskusaste**: ⭐⭐ Kesktase

**Mida õpite**:
- Rakendage Taastekstimislaiendatud genereerimise (RAG) mustrit
- Looge vektorimanustusi kasutades sentence-transformers raamistiku
- Looge semantiline otsing kas kooskõlapõhise lähendusega
- Põhjendage LLM vastuseid domeenidokumentidega
- Kasutage valikuliste sõltuvuste kontrollimiseks importi kaitseid

**Põhikontseptsioonid**: RAG arhitektuur, manustused, semantiline otsing, vektorsarnasus

**Te ehitate**: Dokumentidel põhinev küsimuste-vastuste süsteem

---

### 📗 Sessioon 02: RAG hindamine RAGAS-iga
**Fail**: `session02_rag_eval_ragas.ipynb`  
**Kestus**: 30-45 minutit  
**Eeldused**: Sessioon 02 RAG töövoog  
**Raskusaste**: ⭐⭐ Kesktase

**Mida õpite**:
- Hinnake RAG kvaliteeti tööstuslike standardite mõõdikute alusel
- Mõõtke konteksti asjakohasust, vastuseks asjakohasust, usaldusväärsust
- Kasutage RAGAS raamistiku süstemaatiliseks hindamiseks
- Tuvastage ja parandage RAG kvaliteediprobleeme
- Looge hindamisdomeenid oma domeeni jaoks

**Põhikontseptsioonid**: RAG hindamine, RAGAS mõõdikud, kvaliteedi mõõtmine, süstemaatiline testimine

**Te ehitate**: RAG kvaliteedihindamise raamistik

---

### 📙 Sessioon 03: OSS mudelite võrdlus
**Fail**: `session03_benchmark_oss_models.ipynb`  
**Kestus**: 30-45 minutit  
**Eeldused**: Sessioon 01  
**Raskusaste**: ⭐⭐ Kesktase

**Mida õpite**:
- Süsteemselt võrdle mitut mudelit
- Mõõda latentsust, läbilaskevõimet, esimese tokeni aega
- Rakenda ladusat katkestamist mudelirikkete korral
- Võrdle jõudlust mudelseeriate kaupa
- Visualiseeri ja analüüsi võrdluse tulemusi

**Põhikontseptsioonid**: Jõudluse võrdlus, latentsuse mõõtmine, mudelite võrdlus, statistiline analüüs

**Te ehitate**: Mitme mudeli võrdluse paket

---

### 📙 Sessioon 04: Mudelite võrdlus (SLM vs LLM)
**Fail**: `session04_model_compare.ipynb`  
**Kestus**: 30-45 minutit  
**Eeldused**: Sessioonid 01, 03  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud

**Mida õpite**:
- Võrrelge väikeseid ja suuri keelemudeleid
- Analüüsige jõudluse ja kvaliteedi kompromisse
- Mõõtke edge-seadmete sobivuse mõõdikuid
- Valige optimaalsed mudelid juurutuse piirangute jaoks
- Dokumenteerige mudelivaliku otsustuskriteeriumid

**Põhikontseptsioonid**: Mudeli valik, kompromisside analüüs, optimeerimisstrateegiad, juurutuse planeerimine

**Te ehitate**: SLM vs LLM võrdlusraamistik

---

### 📕 Sessioon 05: Mitme agendi orkestreerija
**Fail**: `session05_agents_orchestrator.ipynb`  
**Kestus**: 45-60 minutit  
**Eeldused**: Sessioonid 01-02  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud

**Mida õpite**:
- Kujundage spetsialiseeritud agendid erinevateks ülesanneteks
- Rakendage agendi mälu ja konteksti haldus
- Looge koordinaatormustrid agentide koostöö jaoks
- Haldage agentide suhtlust ja tööülekandeid
- Jälgige mitme agendi süsteemi jõudlust

**Põhikontseptsioonid**: Agendi arhitektuur, koordinaatori mustrid, mälu haldus, agentide orkestreerimine

**Te ehitate**: Mitmeagendilise süsteemi koos koordinaatori ja spetsialistidega

---

### 📕 Sessioon 06: Mudelite marsruutija
**Fail**: `session06_models_router.ipynb`  
**Kestus**: 30-45 minutit  
**Eeldused**: Sessioonid 01, 03  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud

**Mida õpite**:
- Rakendage kavatsuste tuvastamist ja mustrimatchimist
- Looge märksõnapõhised mudelite marsruutimised
- Marsruutige päringud sobivatele mudelitele automaatselt
- Konfigureerige mitme mudeli registrid
- Jälgige marsruutimisotsuseid ja jõudlust

**Põhikontseptsioonid**: Kavatsuste tuvastamine, mudeli marsruutimine, mustri sobitamine, intelligentne valik

**Te ehitate**: Intelligentsed mudelite marsruutimissüsteem

---

### 📕 Sessioon 06: Mitmeastmeline töövoog
**Fail**: `session06_models_pipeline.ipynb`  
**Kestus**: 30-45 minutit  
**Eeldused**: Sessioonid 01, 06 marsruutija  
**Raskusaste**: ⭐⭐⭐ Edasijõudnud

**Mida õpite**:
- Looge mitmeastmelised AI töövood (planeeri → käivita → täienda)
- Integreerige marsruutija intelligentseks mudelivalikuks
- Rakendage töövoogude vigade käsitlemine ja taastumine
- Jälgige töövoo jõudlust ja etappe
- Kujundage skaleeritavad mudel-tööriistade arhitektuurid


**Põhimõisted**: Torujuhtme arhitektuur, mitmeastmeline töötlemine, vigade taastumine, skaleeritavuse mustrid

**Sa ehitad**: Mitmeastmeline intelligentne torujuhe koos marsruutimisega

---

## 🚀 Alustamine

### Nõuded

**Süsteeminõuded**:
- **OS**: Windows 10/11, macOS 11+ või Linux (Ubuntu 20.04+)
- **RAM**: vähemalt 8GB, soovitatav 16GB+
- **Salvestusruum**: mudelite jaoks vähemalt 10GB vaba ruumi
- **Riistvara**: CPU AVX2-ga; GPU (CUDA, Qualcomm NPU) valikuline

**Tarkvaranõuded**:
- **Python 3.8+** koos pipiga
- **Jupyter Notebook** või **VS Code** koos Jupyteri laiendiga
- **Microsoft Foundry Local** installitud ja konfigureeritud
- **Git** (hoidla kloonimiseks)

### Paigaldusjuhised

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

**Paigalduse kontrollimine**:
```bash
foundry --version
```

#### 2. Loo Python keskkond

```bash
# Liigu kausta Workshop
cd Workshop

# Loo virtuaalne keskkond
python -m venv .venv

# Aktiveeri virtuaalne keskkond
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Paigalda sõltuvused
pip install -r requirements.txt
```

#### 3. Käivita Foundry Local

```bash
# Lae mudel (vajadusel laeb automaatselt alla)
foundry model run phi-4-mini

# Kontrolli, kas teenus töötab
foundry service status
```

#### 4. Ava Jupyter

```bash
# Käivita Jupyter Notebook
jupyter notebook notebooks/

# Või kasuta VS Code'i koos Jupyter laiendiga
code notebooks/
```

### Kiire kontroll

Käivita see Python rakus seadistuse kontrollimiseks:

```python
from foundry_local import FoundryLocalManager
import openai

# Initsialiseeri haldur (leiab teenuse automaatselt)
manager = FoundryLocalManager("phi-4-mini")

# Sea OpenAI klient
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Testi vestluse lõpetamist
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Oodatav väljund**: Tervituse vastus kohalikust mudelist.

---

## 📝 Töötuba: parimad tavad

### Juhendajatele

**Enne töötuba**:
- ✅ Saada paigaldusjuhised 1 nädal ette
- ✅ Testi kõiki märkmikke sihtseadmel
- ✅ Valmista ette tõrkeotsingu juhend tavapäraste probleemide jaoks
- ✅ Hoia varumudeleid valmis (phi-3.5-mini, kui phi-4-mini ebaõnnestub)
- ✅ Loo ühine vestluskanal küsimusteks

**Töötoa ajal**:
- ✅ Alusta kiire keskkonna kontrolliga (5 minutit)
- ✅ Jaga tõrkeotsingu ressursse kohe
- ✅ Julgusta eksperimenteerimist ja muudatusi
- ✅ Kasuta pauside strateegilist paigutamist (iga kahe seansi järel)
- ✅ Hoia assistendid saadaval individuaalseks abiks

**Pärast töötuba**:
- ✅ Jaga terveid töömärkmikke ja lahendusi
- ✅ Paku linke lisamaterjalidele
- ✅ Koosta tagasiside küsitlus parenduseks
- ✅ Paku järelkordamiste tunde küsimusteks

### Õppijatele

**Maksimeeri õppimist**:
- ✅ Lõpeta seadistamine enne töötuba
- ✅ Käivita ise iga koodirakk (ära ainult loe)
- ✅ Katseta parameetreid ja küsimusi
- ✅ Tee märkmeid tähelepanekute ja raskuste kohta
- ✅ Küsi abi takistuste korral (kaasalased võivad sama küsimusega)

**Tavalised vead, mida vältida**:
- ❌ Järjekorrast mööda hiilimine (käivita järjestikku)
- ❌ Vigade sõnumite tähelepanuta jätmine
- ❌ Kiirustamine arusaamata sisu
- ❌ Markdown selgituste ignoreerimine
- ❌ Muudetud märkmike salvestamata jätmine

**Silumise nipid**:
1. **Teenust ei käivitata**: Kontrolli `foundry service status`
2. **Importimisvead**: Veendu, et virtuaalne keskkond on aktiivne
3. **Mudelit ei leitud**: Käivita `foundry model ls` laetud mudelite loendamiseks
4. **Aeglane töö**: Kontrolli RAMi kasutust, sulge muud rakendused
5. **Ebakorrektsed tulemused**: Taaskäivita kernel ja käivita kõik rakud algusest peale

---

## 🔗 Lisamaterjalid

### Töötuba materjalid

- **[Töötoa peamine juhend](../Readme.md)** - Ülevaade, õppimise eesmärgid, karjäärivõimalused
- **[Python näited](../../../../Workshop/samples)** - Vastavad Python skriptid igale sessioonile
- **[Sessioonijuhendid](../../../../Workshop)** - Üksikasjalikud markdown juhendid (Sessioon01-06)
- **[Skriptid](../../../../Workshop/scripts)** - Kontrolli- ja testimisriistad
- **[Tõrkeotsing](./TROUBLESHOOTING.md)** - Tavapärased probleemid ja lahendused
- **[Kiire algus](./quickstart.md)** - Kiiresti otsast alustamise juhend

### Dokumentatsioon

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Microsofti ametlik dokumentatsioon
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK viide
- **[Sentence Transformers](https://www.sbert.net/)** - Sisutamise mudelite dokumentatsioon
- **[RAGAS raamistik](https://docs.ragas.io/)** - RAG hindamismõõdikud

### Kogukond

- **[GitHub Arutelud](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Küsi küsimusi, jaga projekte
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Reaalajas kogukonna tugi
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tehniline Q&A

---

## 🎯 Õppeteekonna soovitused

### Algajate rada (Alusta siit)

1. **Sessioon 01** - Vestluse alustus
2. **Sessioon 02** - RAG torujuhe
3. **Sessioon 03** - Mudelite võrdlus

**Aeg**: ~2 tundi | **Fookus**: Põhimustrid

---

### Kesktaseme rada

1. Lõpeta algajate rada
2. **Sessioon 02** - RAG hindamine
3. **Sessioon 04** - Mudelite võrdlemine

**Aeg**: ~4 tundi | **Fookus**: Kvaliteet ja optimeerimine

---

### Edasijõudnute rada (Täispikk töötuba)

1. Lõpeta kesktaseme rada
2. **Sessioon 05** - Mitme agendi orkestreerija
3. **Sessioon 06** - Mudelite marsruutija
4. **Sessioon 06** - Mitmeastmeline torujuhe

**Aeg**: ~6 tundi | **Fookus**: Tootmismustrid

---

### Kohandatud projekti rada

1. Lõpeta algajate rada (sessioonid 01-03)
2. Vali ÜKS edasijõudnud sessioon eesmärgipõhiselt:
   - **RAG rakenduse ehitus?** → Sessioon 02 hindamine
   - **Töökiiruse optimeerimine?** → Sessioon 04 võrdlus
   - **Kompleksne töövoog?** → Sessioon 05 orkestreerija
   - **Skaleeritav arhitektuur?** → Sessioon 06 marsruutija + torujuhe

**Aeg**: ~3 tundi | **Fookus**: Projekti spetsiifilised oskused

---

## 📊 Edu mõõdikud

Jälgi oma edenemist nende verstapostidega:

- [ ] **Seadistamine lõpetatud** - Foundry Local töötab, kõik sõltuvused paigaldatud
- [ ] **Esimene vestlus** - Sessioon 01 lõpetatud, voogedastus töötab
- [ ] **RAG ehitatud** - Sessioon 02 lõpetatud, dokumentide KKV süsteem toimib
- [ ] **Mudelite võrdlus tehtud** - Sessioon 03 lõpetatud, soorituse andmed kogutud
- [ ] **Kompromissid analüüsitud** - Sessioon 04 lõpetatud, mudeli valiku kriteeriumid dokumenteeritud
- [ ] **Agendid orkestreeritud** - Sessioon 05 lõpetatud, mitmeagendisüsteem töötab
- [ ] **Marsruutimine rakendatud** - Sessioon 06 lõpetatud, intelligentne mudelivalik toimib
- [ ] **Kohandatud projekt** - Töötoa mustrite rakendamine oma juhtumil

---

## 🤝 Panustamine

Leidsid vea või on ettepanek? Ootame panuseid!

- **Teata vigadest**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Pane etteparandusi**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Esita PR-e**: Järgi [panustamisjuhiseid](../../AGENTS.md)

---

## 📄 Litsents

See töötuba on osa [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) hoidlast ja on litsentseeritud all [MIT litsentsi](../../../../LICENSE) alusel.

---

**Valmis tootmiskõlblike Edge AI rakenduste ehitamiseks?**  
**Alusta [sessioonist 01: Vestluse alustus](./session01_chat_bootstrap.ipynb) →**

---

*Viimati uuendatud: 8. oktoober 2025 | Töötoa versioon: 2.0*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->