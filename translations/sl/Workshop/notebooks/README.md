# Delavnica Zvezki

> **Interaktivni Jupyter zvezki za praktično učenje Edge AI**
>
> Postopni, samostojni vodiči, ki se razvijajo od osnovnih klepetalnih zaključkov do naprednih večagentnih sistemov z uporabo Microsoft Foundry Local in majhnih jezikovnih modelov.

---

## 📖 Uvod

Dobrodošli v zbirki **EdgeAI za začetnike - delavnica zvezkov**. Ti interaktivni Jupyter zvezki omogočajo praktično učenje, kjer boste pisali, izvajali in eksperimentirali s kodo Edge AI v realnem času.

### Zakaj Jupyter zvezki?

Za razliko od tradicionalnih vodičev ti zvezki ponujajo:

- **Interaktivno učenje**: Zaženite kode in takoj vidite rezultate
- **Eksperimentiranje**: Spreminjajte parametre in opazujte spremembe v realnem času
- **Dokumentacija**: Vgrajena pojasnila in markdown celice vas vodijo skozi koncepte
- **Ponovljivost**: Popolni delujoči primeri, ki jih lahko uporabite in ponovno uporabite
- **Vizualizacija**: Oglejte si meritve zmogljivosti, vdelave in rezultate neposredno v zvezku

### Kaj naredi te zvezke posebne?

Vsak zvezek je zasnovan po **najboljših praksah za produkcijo**:

✅ **Celovito obravnavanje napak** - Prilagodljivo delovanje in informativna sporočila o napakah  
✅ **Namigi tipov in dokumentacija** - Jasni podpisi funkcij in docstringi  
✅ **Spremljanje zmogljivosti** - Sledenje uporabi žetonov in merjenje zakasnitve  
✅ **Modularna zasnova** - Vzorce, ki jih lahko prilagodite svojim projektom  
✅ **Postopna kompleksnost** - Sistematično nadgrajevanje na podlagi prejšnjih sej

---

## 🎯 Cilji učenja

### Ključne veščine, ki jih boste razvili

Z delom skozi te zvezke boste obvladali:

1. **Upravljanje lokalnih AI storitev**
   - Konfiguriranje in upravljanje storitev Microsoft Foundry Local
   - Izbira in nalaganje ustreznih modelov za vašo strojno opremo
   - Spremljanje uporabe virov in optimizacija zmogljivosti
   - Upravljanje odkrivanja storitev in preverjanje zdravja

2. **Razvoj AI aplikacij**
   - Implementacija lokalnih klepetalnih zaključkov, združljivih z OpenAI
   - Gradnja pretočnih vmesnikov za boljšo uporabniško izkušnjo
   - Oblikovanje učinkovitih pozivov za majhne jezikovne modele
   - Integracija lokalnih modelov v aplikacije

3. **Generacija z obogatenim iskanjem (RAG)**
   - Ustvarjanje semantičnega iskanja z vektorskimi vdelavami
   - Utemeljevanje odgovorov LLM v dokumentih specifičnih za domeno
   - Ocena kakovosti RAG z metrikami RAGAS
   - Razširitev od prototipa do produkcije

4. **Optimizacija zmogljivosti**
   - Sistematično primerjanje več modelov
   - Merjenje zakasnitve, prepustnosti in časa prvega žetona
   - Primerjava majhnih jezikovnih modelov z velikimi jezikovnimi modeli
   - Izbira optimalnih modelov na podlagi kompromisov med zmogljivostjo in kakovostjo

5. **Orkestracija več agentov**
   - Oblikovanje specializiranih agentov za različne naloge
   - Implementacija spomina agentov in upravljanje konteksta
   - Koordinacija več agentov v kompleksnih delovnih tokovih
   - Gradnja vzorcev koordinatorjev za sodelovanje agentov

6. **Pametno usmerjanje modelov**
   - Implementacija zaznavanja namena in ujemanja vzorcev
   - Samodejno usmerjanje poizvedb na ustrezne modele
   - Gradnja večstopenjskih cevovodov (načrt → izvedba → izboljšava)
   - Oblikovanje skalabilnih arhitektur modelov kot orodij

---

## 🎓 Rezultati učenja

### Kaj boste zgradili

| Zvezek | Končni izdelek | Prikazane veščine | Težavnost |
|--------|----------------|-------------------|-----------|
| **Seja 01** | Klepetalna aplikacija s pretokom | Nastavitev storitve, osnovni zaključki, UX s pretokom | ⭐ Začetnik |
| **Seja 02 (RAG)** | RAG cevovod z oceno | Vdelave, semantično iskanje, metrične ocene | ⭐⭐ Srednje |
| **Seja 02 (Eval)** | Ocena kakovosti RAG | Metrične ocene RAGAS, sistematična ocena | ⭐⭐ Srednje |
| **Seja 03** | Primerjalnik več modelov | Merjenje zmogljivosti, primerjava modelov | ⭐⭐ Srednje |
| **Seja 04** | Primerjalnik SLM proti LLM | Analiza kompromisov, strategije optimizacije | ⭐⭐⭐ Napredno |
| **Seja 05** | Orkestrator več agentov | Oblikovanje agentov, spomin, koordinacija | ⭐⭐⭐ Napredno |
| **Seja 06 (Router)** | Pametni sistem usmerjanja | Zaznavanje namena, izbira modelov | ⭐⭐⭐ Napredno |
| **Seja 06 (Pipeline)** | Večstopenjski cevovod | Delovni tokovi načrt/izvedba/izboljšava | ⭐⭐⭐ Napredno |

### Napredovanje kompetenc

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Urnik delavnice

### 🚀 Pol-dnevna delavnica (3,5 ure)

**Idealno za: Usposabljanje ekip, hackathone, delavnice na konferencah**

| Čas | Trajanje | Seja | Teme | Aktivnosti |
|-----|----------|------|------|------------|
| **0:00** | 30 min | Nastavitev in uvod | Nastavitev okolja, namestitev Foundry Local | Namestitev odvisnosti, preverjanje nastavitev |
| **0:30** | 30 min | Seja 01 | Osnovni klepetalni zaključki, pretok | Zagon zvezka, spreminjanje pozivov |
| **1:00** | 45 min | Seja 02 | RAG cevovod, vdelave, ocena | Gradnja sistema RAG, testiranje poizvedb |
| **1:45** | 15 min | Odmor | ☕ Kava in vprašanja | — |
| **2:00** | 30 min | Seja 03 | Primerjava več modelov | Primerjava 3+ modelov |
| **2:30** | 30 min | Seja 04 | Kompromisi SLM proti LLM | Analiza zmogljivosti/kakovosti |
| **3:00** | 30 min | Seja 05-06 | Sistemi več agentov in usmerjanje | Raziskovanje naprednih vzorcev |

**Rezultat**: Udeleženci odidejo z 6 delujočimi Edge AI aplikacijami in vzorci kode, pripravljenimi za produkcijo.

---

### 🎓 Celodnevna delavnica (6 ur)

**Idealno za: Poglobljeno usposabljanje, bootcampi, univerzitetni tečaji**

| Čas | Trajanje | Seja | Teme | Aktivnosti |
|-----|----------|------|------|------------|
| **0:00** | 45 min | Nastavitev in teorija | Nastavitev okolja, osnove Edge AI | Namestitev, preverjanje, razprava o primerih uporabe |
| **0:45** | 45 min | Seja 01 | Poglobitev v klepetalne zaključke | Implementacija osnovnih in pretočnih klepetov |
| **1:30** | 30 min | Odmor | ☕ Kava in mreženje | — |
| **2:00** | 60 min | Seja 02 (obe) | RAG cevovod + ocena RAGAS | Gradnja popolnega sistema RAG |
| **3:00** | 30 min | Praktična vaja 1 | Prilagojen RAG za vašo domeno | Uporaba na lastnih dokumentih |
| **3:30** | 30 min | Kosilo | 🍽️ | — |
| **4:00** | 45 min | Seja 03 | Metodologija primerjanja | Sistematična primerjava modelov |
| **4:45** | 45 min | Seja 04 | Strategije optimizacije | Analiza SLM proti LLM |
| **5:30** | 60 min | Seja 05-06 | Napredna orkestracija | Sistemi več agentov, usmerjanje |
| **6:30** | 30 min | Praktična vaja 2 | Gradnja prilagojenega sistema agentov | Oblikovanje lastnega orkestratorja |

**Rezultat**: Poglobljeno razumevanje vzorcev Edge AI plus 2 prilagojena projekta.

---

### 📚 Samostojno učenje (2 tedna)

**Idealno za: Posamezne učence, spletne tečaje, samostojno študijo**

#### 1. teden: Osnove (6 ur)

| Dan | Fokus | Trajanje | Zvezki | Domača naloga |
|-----|-------|----------|--------|---------------|
| **Pon** | Nastavitev in osnove | 1,5 ure | Seja 01 | Spreminjanje pozivov, testiranje pretoka |
| **Sre** | Osnove RAG | 2 uri | Seja 02 (obe) | Dodajanje lastnih dokumentov |
| **Pet** | Primerjanje | 1,5 ure | Seja 03 | Primerjava dodatnih modelov |
| **Sob** | Pregled in praksa | 1 ura | Vsi 1. teden | Dokončanje vaj, odpravljanje napak |

#### 2. teden: Napredno (5 ur)

| Dan | Fokus | Trajanje | Zvezki | Domača naloga |
|-----|-------|----------|--------|---------------|
| **Pon** | Optimizacija | 1,5 ure | Seja 04 | Dokumentiranje kompromisov |
| **Sre** | Sistemi več agentov | 2 uri | Seja 05 | Oblikovanje prilagojenih agentov |
| **Pet** | Pametno usmerjanje | 1,5 ure | Seja 06 (obe) | Gradnja logike usmerjanja |
| **Sob** | Končni projekt | 2 uri | Integracija | Združevanje več vzorcev |

**Rezultat**: Obvladovanje vzorcev Edge AI plus projekt za portfelj.

---

## 📔 Opisi zvezkov

### 📘 Seja 01: Osnovni klepet
**Datoteka**: `session01_chat_bootstrap.ipynb`  
**Trajanje**: 20-30 minut  
**Predpogoji**: Nič  
**Težavnost**: ⭐ Začetnik

**Kaj se boste naučili**:
- Namestitev in konfiguracija Foundry Local Python SDK
- Uporaba `FoundryLocalManager` za samodejno odkrivanje storitev
- Implementacija osnovnih klepetalnih zaključkov z API-jem, združljivim z OpenAI
- Gradnja pretočnih odgovorov za boljšo uporabniško izkušnjo
- Prilagodljivo obravnavanje napak in nedostopnosti storitev

**Ključni koncepti**: Upravljanje storitev, klepetalni zaključki, pretok, obravnavanje napak

**Kaj boste zgradili**: Interaktivna klepetalna aplikacija s podporo za pretok

---

### 📗 Seja 02: RAG cevovod
**Datoteka**: `session02_rag_pipeline.ipynb`  
**Trajanje**: 30-45 minut  
**Predpogoji**: Seja 01  
**Težavnost**: ⭐⭐ Srednje

**Kaj se boste naučili**:
- Implementacija vzorca Retrieval Augmented Generation (RAG)
- Ustvarjanje vektorskih vdelav z uporabo sentence-transformers
- Gradnja semantičnega iskanja s kosinusno podobnostjo
- Utemeljevanje odgovorov LLM v dokumentih specifičnih za domeno
- Prilagodljivo upravljanje odvisnosti z varovali za uvoz

**Ključni koncepti**: Arhitektura RAG, vdelave, semantično iskanje, vektorska podobnost

**Kaj boste zgradili**: Sistem za odgovarjanje na vprašanja, utemeljen v dokumentih

---

### 📗 Seja 02: Ocena RAG z RAGAS
**Datoteka**: `session02_rag_eval_ragas.ipynb`  
**Trajanje**: 30-45 minut  
**Predpogoji**: Seja 02 RAG cevovod  
**Težavnost**: ⭐⭐ Srednje

**Kaj se boste naučili**:
- Ocena kakovosti RAG z industrijskimi standardnimi metrikami
- Merjenje ustreznosti konteksta, ustreznosti odgovora, zanesljivosti
- Uporaba okvira RAGAS za sistematično oceno
- Identifikacija in odpravljanje težav s kakovostjo RAG
- Gradnja ocenjevalnih podatkovnih zbirk za vašo domeno

**Ključni koncepti**: Ocena RAG, metrične ocene RAGAS, merjenje kakovosti, sistematično testiranje

**Kaj boste zgradili**: Okvir za oceno kakovosti RAG

---

### 📙 Seja 03: Primerjava OSS modelov
**Datoteka**: `session03_benchmark_oss_models.ipynb`  
**Trajanje**: 30-45 minut  
**Predpogoji**: Seja 01  
**Težavnost**: ⭐⭐ Srednje

**Kaj se boste naučili**:
- Sistematično primerjanje več modelov
- Merjenje zakasnitve, prepustnosti, časa prvega žetona
- Implementacija prilagodljivega delovanja ob napakah modelov
- Primerjava zmogljivosti med družinami modelov
- Vizualizacija in analiza rezultatov primerjanja

**Ključni koncepti**: Primerjanje zmogljivosti, merjenje zakasnitve, primerjava modelov, statistična analiza

**Kaj boste zgradili**: Suite za primerjanje več modelov

---

### 📙 Seja 04: Primerjava modelov (SLM proti LLM)
**Datoteka**: `session04_model_compare.ipynb`  
**Trajanje**: 30-45 minut  
**Predpogoji**: Seje 01, 03  
**Težavnost**: ⭐⭐⭐ Napredno

**Kaj se boste naučili**:
- Primerjava majhnih jezikovnih modelov proti velikim jezikovnim modelom
- Analiza kompromisov med zmogljivostjo in kakovostjo
- Merjenje metrik primernosti za robne naprave
- Izbira optimalnih modelov glede na omejitve pri uvajanju
- Dokumentiranje kriterijev za izbiro modelov

**Ključni koncepti**: Izbira modelov, analiza kompromisov, strategije optimizacije, načrtovanje uvajanja

**Kaj boste zgradili**: Okvir za primerjavo SLM proti LLM

---

### 📕 Seja 05: Orkestrator več agentov
**Datoteka**: `session05_agents_orchestrator.ipynb`  
**Trajanje**: 45-60 minut  
**Predpogoji**: Seje 01-02  
**Težavnost**: ⭐⭐⭐ Napredno

**Kaj se boste naučili**:
- Oblikovanje specializiranih agentov za različne naloge
- Implementacija spomina agentov in upravljanje konteksta
- Gradnja vzorcev koordinatorjev za sodelovanje agentov
- Upravljanje komunikacije med agenti in predajanje nalog
- Spremljanje zmogljivosti sistema več agentov

**Ključni koncepti**: Arhitektura agentov, vzorci koordinatorjev, upravljanje spomina, orkestracija agentov

**Kaj boste zgradili**: Sistem več agentov s koordinatorjem in specialisti

---

### 📕 Seja 06: Usmerjevalnik modelov
**Datoteka**: `session06_models_router.ipynb`  
**Trajanje**: 30-45 minut  
**Predpogoji**: Seje 01, 03  
**Težavnost**: ⭐⭐⭐ Napredno

**Kaj se boste naučili**:
- Implementacija zaznavanja namena in ujemanja vzorcev
- Gradnja usmerjanja modelov na podlagi ključnih besed
- Samodejno usmerjanje poizvedb na ustrezne modele
- Konfiguracija večmodelnih registracij
- Spremljanje odločitev o usmerjanju in zmogljivosti

**Ključni koncepti**: Zaznavanje namena, usmerjanje modelov, ujemanje vzorcev, pametna izbira

**Kaj boste zgradili**: Pametni sistem usmerjanja modelov

---

### 📕 Seja 06: Večstopenjski cevovod
**Datoteka**: `session06_models_pipeline.ipynb`  
**Trajanje**: 30-45 minut  
**Predpogoji**: Seje 01, 06 Usmerjevalnik  

- Oblikovanje skalabilnih arhitektur modelov kot orodij

**Ključni koncepti**: Arhitektura cevovoda, večstopenjska obdelava, odpravljanje napak, vzorci skalabilnosti

**Kaj boste zgradili**: Večstopenjski inteligentni cevovod z usmerjanjem

---

## 🚀 Začetek

### Predpogoji

**Sistemske zahteve**:
- **OS**: Windows 10/11, macOS 11+ ali Linux (Ubuntu 20.04+)
- **RAM**: najmanj 8 GB, priporočeno 16 GB+
- **Shramba**: najmanj 10 GB prostega prostora za modele
- **Strojna oprema**: CPU z AVX2; GPU (CUDA, Qualcomm NPU) opcijsko

**Programske zahteve**:
- **Python 3.8+** z nameščenim pip
- **Jupyter Notebook** ali **VS Code** z razširitvijo Jupyter
- **Microsoft Foundry Local** nameščen in konfiguriran
- **Git** (za kloniranje repozitorija)

### Koraki namestitve

#### 1. Namestite Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Preverite namestitev**:
```bash
foundry --version
```

#### 2. Nastavite Python okolje

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

#### 3. Zaženite Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Zaženite Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Hitro preverjanje

Za preverjanje namestitve zaženite to v Python celici:

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

**Pričakovani rezultat**: Pozdravni odziv lokalnega modela.

---

## 📝 Najboljše prakse za delavnico

### Za inštruktorje

**Pred delavnico**:
- ✅ Pošljite navodila za namestitev 1 teden vnaprej
- ✅ Preizkusite vse zvezke na ciljni strojni opremi
- ✅ Pripravite vodnik za odpravljanje pogostih težav
- ✅ Imejte pripravljene rezervne modele (phi-3.5-mini, če phi-4-mini ne deluje)
- ✅ Nastavite skupni kanal za vprašanja

**Med delavnico**:
- ✅ Začnite s hitrim preverjanjem okolja (5 minut)
- ✅ Takoj delite vire za odpravljanje težav
- ✅ Spodbujajte eksperimentiranje in prilagoditve
- ✅ Strategično načrtujte odmore (po vsakih 2 sejah)
- ✅ Poskrbite, da so asistenti na voljo za individualno pomoč

**Po delavnici**:
- ✅ Delite popolne delujoče zvezke in rešitve
- ✅ Zagotovite povezave do dodatnih virov
- ✅ Ustvarite anketo za povratne informacije
- ✅ Ponudite uradne ure za dodatna vprašanja

### Za udeležence

**Maksimizirajte svoje učenje**:
- ✅ Dokončajte nastavitev pred začetkom delavnice
- ✅ Sami zaženite vsako kodo (ne le preberite)
- ✅ Eksperimentirajte s parametri in pozivi
- ✅ Zapisujte si vpoglede in opozorila
- ✅ Postavljajte vprašanja, ko se zataknete (verjetno imajo drugi enako vprašanje)

**Pogoste napake, ki se jim izognite**:
- ❌ Preskakovanje vrstnega reda izvajanja celic (zaženite zaporedno)
- ❌ Nepozorno branje sporočil o napakah
- ❌ Hitenje brez razumevanja
- ❌ Ignoriranje razlag v markdownu
- ❌ Ne shranjevanje spremenjenih zvezkov

**Nasveti za odpravljanje težav**:
1. **Storitev ne deluje**: Preverite `foundry service status`
2. **Napake pri uvozu**: Preverite, ali je virtualno okolje aktivirano
3. **Model ni najden**: Zaženite `foundry model ls` za seznam naloženih modelov
4. **Počasno delovanje**: Preverite uporabo RAM-a, zaprite druge aplikacije
5. **Nepričakovani rezultati**: Znova zaženite jedro in zaženite vse celice od začetka

---

## 🔗 Dodatni viri

### Gradivo za delavnico

- **[Glavni vodnik delavnice](../Readme.md)** - Pregled, učni cilji, karierni izidi
- **[Python primeri](../../../../Workshop/samples)** - Ustrezni Python skripti za vsako sejo
- **[Vodniki sej](../../../../Workshop)** - Podrobni markdown vodniki (Session01-06)
- **[Skripti](../../../../Workshop/scripts)** - Orodja za validacijo in testiranje
- **[Odpravljanje težav](./TROUBLESHOOTING.md)** - Pogoste težave in rešitve
- **[Hitri začetek](./quickstart.md)** - Vodnik za hiter začetek

### Dokumentacija

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Uradna Microsoft dokumentacija
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referenca za OpenAI SDK
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentacija za modele vdelave
- **[RAGAS Framework](https://docs.ragas.io/)** - Metodologija za ocenjevanje RAG

### Skupnost

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Postavljajte vprašanja, delite projekte
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Podpora skupnosti v realnem času
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tehnična vprašanja in odgovori

---

## 🎯 Priporočila za učne poti

### Začetniška pot (začnite tukaj)

1. **Seja 01** - Zagon klepeta
2. **Seja 02** - RAG cevovod
3. **Seja 03** - Primerjava modelov

**Čas**: ~2 uri | **Osredotočenost**: Osnovni vzorci

---

### Srednja pot

1. Dokončajte začetniško pot
2. **Seja 02** - Ocena RAG
3. **Seja 04** - Primerjava modelov

**Čas**: ~4 ure | **Osredotočenost**: Kakovost in optimizacija

---

### Napredna pot (celotna delavnica)

1. Dokončajte srednjo pot
2. **Seja 05** - Orkestrator več agentov
3. **Seja 06** - Usmerjevalnik modelov
4. **Seja 06** - Večstopenjski cevovod

**Čas**: ~6 ur | **Osredotočenost**: Vzorci za produkcijo

---

### Pot po meri

1. Dokončajte začetniško pot (Seje 01-03)
2. Izberite ENO napredno sejo glede na svoj cilj:
   - **Gradite RAG aplikacijo?** → Seja 02 Ocena
   - **Optimizirate delovanje?** → Seja 04 Primerjava
   - **Kompleksni delovni tokovi?** → Seja 05 Orkestrator
   - **Skalabilna arhitektura?** → Seja 06 Usmerjevalnik + cevovod

**Čas**: ~3 ure | **Osredotočenost**: Spretnosti specifične za projekt

---

## 📊 Merila uspeha

Sledite svojemu napredku z naslednjimi mejniki:

- [ ] **Namestitev dokončana** - Foundry Local deluje, vse odvisnosti nameščene
- [ ] **Prvi klepet** - Seja 01 dokončana, pretočni klepet deluje
- [ ] **RAG zgrajen** - Seja 02 dokončana, sistem za vprašanja in odgovore deluje
- [ ] **Modeli primerjani** - Seja 03 dokončana, zbrani podatki o delovanju
- [ ] **Analizirani kompromisi** - Seja 04 dokončana, dokumentirana merila za izbiro modelov
- [ ] **Agentje orkestrirani** - Seja 05 dokončana, sistem več agentov deluje
- [ ] **Usmerjanje implementirano** - Seja 06 dokončana, inteligentna izbira modelov deluje
- [ ] **Projekt po meri** - Vzorce delavnice uporabljeni za vaš primer uporabe

---

## 🤝 Prispevanje

Ste našli težavo ali imate predlog? Veseli bomo vaših prispevkov!

- **Prijavite težave**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Predlagajte izboljšave**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Pošljite PR-je**: Sledite [Navodilom za prispevanje](../../AGENTS.md)

---

## 📄 Licenca

Ta delavnica je del repozitorija [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) in je licencirana pod [MIT licenco](../../../../LICENSE).

---

**Pripravljeni na gradnjo produkcijsko pripravljenih Edge AI aplikacij?**  
**Začnite z [Sejo 01: Zagon klepeta](./session01_chat_bootstrap.ipynb) →**

---

*Zadnja posodobitev: 8. oktober 2025 | Različica delavnice: 2.0*

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.