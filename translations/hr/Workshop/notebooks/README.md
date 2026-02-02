# Radionice s bilježnicama

> **Interaktivne Jupyter bilježnice za praktično učenje Edge AI-a**
>
> Progresivni, samostalni vodiči koji se razvijaju od osnovnih chat funkcija do naprednih sustava s više agenata koristeći Microsoft Foundry Local i male jezične modele.

---

## 📖 Uvod

Dobrodošli u kolekciju **EdgeAI za početnike radionica s bilježnicama**. Ove interaktivne Jupyter bilježnice pružaju praktično iskustvo učenja gdje ćete pisati, izvršavati i eksperimentirati s Edge AI kodom u stvarnom vremenu.

### Zašto Jupyter bilježnice?

Za razliku od tradicionalnih vodiča, ove bilježnice nude:

- **Interaktivno učenje**: Pokrenite ćelije koda i odmah vidite rezultate
- **Eksperimentiranje**: Promijenite parametre i promatrajte promjene u stvarnom vremenu
- **Dokumentacija**: Objašnjenja unutar bilježnica i markdown ćelije vode vas kroz koncepte
- **Reproducibilnost**: Potpuni radni primjeri koje možete koristiti i ponovno koristiti
- **Vizualizacija**: Pregledajte metrike performansi, ugrađivanja i rezultate unutar bilježnice

### Što čini ove bilježnice posebnima?

Svaka bilježnica je dizajnirana prema **najboljim praksama za proizvodnju**:

✅ **Sveobuhvatno rukovanje greškama** - Postupno degradiranje i informativne poruke o greškama  
✅ **Tipovi podataka i dokumentacija** - Jasni potpisi funkcija i docstrings  
✅ **Praćenje performansi** - Praćenje korištenja tokena i mjerenje kašnjenja  
✅ **Modularni dizajn** - Obrasci koji se mogu ponovno koristiti i prilagoditi vašim projektima  
✅ **Progresivna složenost** - Sustavno se nadovezuje na prethodne sesije  

---

## 🎯 Ciljevi učenja

### Ključne vještine koje ćete razviti

Radom kroz ove bilježnice, savladat ćete:

1. **Upravljanje lokalnim AI uslugama**
   - Konfiguriranje i upravljanje Microsoft Foundry Local uslugama
   - Odabir i učitavanje odgovarajućih modela za vaš hardver
   - Praćenje korištenja resursa i optimizacija performansi
   - Rukovanje otkrivanjem usluga i provjerom zdravlja sustava

2. **Razvoj AI aplikacija**
   - Implementacija lokalnih chat funkcija kompatibilnih s OpenAI-jem
   - Izrada streaming sučelja za bolje korisničko iskustvo
   - Dizajniranje učinkovitih upita za male jezične modele
   - Integracija lokalnih modela u aplikacije

3. **Generacija uz pomoć pretraživanja (RAG)**
   - Stvaranje semantičkog pretraživanja pomoću vektorskih ugrađivanja
   - Utemeljivanje odgovora LLM-a u dokumentima specifičnim za domenu
   - Procjena kvalitete RAG-a pomoću RAGAS metrika
   - Skaliranje od prototipa do proizvodnje

4. **Optimizacija performansi**
   - Sustavno uspoređivanje više modela
   - Mjerenje kašnjenja, propusnosti i vremena prvog tokena
   - Usporedba malih jezičnih modela (SLM) i velikih jezičnih modela (LLM)
   - Odabir optimalnih modela na temelju kompromisa između performansi i kvalitete

5. **Orkestracija više agenata**
   - Dizajniranje specijaliziranih agenata za različite zadatke
   - Implementacija memorije agenata i upravljanje kontekstom
   - Koordinacija više agenata u složenim radnim tokovima
   - Izrada obrazaca koordinacije za suradnju agenata

6. **Pametno usmjeravanje modela**
   - Implementacija detekcije namjere i prepoznavanja obrazaca
   - Automatsko usmjeravanje upita prema odgovarajućim modelima
   - Izrada višekoraknih cjevovoda (plan → izvrši → poboljšaj)
   - Dizajniranje skalabilnih arhitektura modela kao alata

---

## 🎓 Ishodi učenja

### Što ćete izraditi

| Bilježnica | Rezultat | Demonstrirane vještine | Težina |
|------------|----------|------------------------|--------|
| **Sesija 01** | Chat aplikacija sa streamingom | Postavljanje usluge, osnovne funkcije, streaming UX | ⭐ Početnik |
| **Sesija 02 (RAG)** | RAG cjevovod s evaluacijom | Ugrađivanja, semantičko pretraživanje, kvalitativne metrike | ⭐⭐ Srednje |
| **Sesija 02 (Eval)** | Evaluator kvalitete RAG-a | RAGAS metrike, sustavna evaluacija | ⭐⭐ Srednje |
| **Sesija 03** | Benchmark više modela | Mjerenje performansi, usporedba modela | ⭐⭐ Srednje |
| **Sesija 04** | Usporedba SLM-a i LLM-a | Analiza kompromisa, strategije optimizacije | ⭐⭐⭐ Napredno |
| **Sesija 05** | Orkestrator više agenata | Dizajn agenata, memorija, koordinacija | ⭐⭐⭐ Napredno |
| **Sesija 06 (Router)** | Pametni sustav usmjeravanja | Detekcija namjere, odabir modela | ⭐⭐⭐ Napredno |
| **Sesija 06 (Pipeline)** | Višekorakni cjevovod | Plan/izvrši/poboljšaj radni tokovi | ⭐⭐⭐ Napredno |

### Napredak kompetencija

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Raspored radionice

### 🚀 Poludnevna radionica (3,5 sata)

**Idealno za: Timsku obuku, hackathone, konferencijske radionice**

| Vrijeme | Trajanje | Sesija | Teme | Aktivnosti |
|---------|----------|--------|------|------------|
| **0:00** | 30 min | Postavljanje i uvod | Postavljanje okruženja, instalacija Foundry Local | Instalacija ovisnosti, provjera postavki |
| **0:30** | 30 min | Sesija 01 | Osnovne chat funkcije, streaming | Pokretanje bilježnice, izmjena upita |
| **1:00** | 45 min | Sesija 02 | RAG cjevovod, ugrađivanja, evaluacija | Izrada RAG sustava, testiranje upita |
| **1:45** | 15 min | Pauza | ☕ Kava i pitanja | — |
| **2:00** | 30 min | Sesija 03 | Benchmark više modela | Usporedba 3+ modela |
| **2:30** | 30 min | Sesija 04 | Kompromisi SLM-a i LLM-a | Analiza performansi/kvalitete |
| **3:00** | 30 min | Sesija 05-06 | Sustavi s više agenata i usmjeravanje | Istraživanje naprednih obrazaca |

**Rezultat**: Sudionici odlaze s 6 funkcionalnih Edge AI aplikacija i uzorcima koda spremnim za proizvodnju.

---

### 🎓 Cjelodnevna radionica (6 sati)

**Idealno za: Detaljnu obuku, bootcampove, sveučilišne tečajeve**

| Vrijeme | Trajanje | Sesija | Teme | Aktivnosti |
|---------|----------|--------|------|------------|
| **0:00** | 45 min | Postavljanje i teorija | Postavljanje okruženja, osnove Edge AI-a | Instalacija, provjera, rasprava o slučajevima |
| **0:45** | 45 min | Sesija 01 | Detaljno o chat funkcijama | Implementacija osnovnih i streaming chat funkcija |
| **1:30** | 30 min | Pauza | ☕ Kava i umrežavanje | — |
| **2:00** | 60 min | Sesija 02 (Obje) | RAG cjevovod + evaluacija RAGAS-a | Izrada kompletnog RAG sustava |
| **3:00** | 30 min | Praktična radionica 1 | Prilagođeni RAG za vašu domenu | Primjena na vlastite dokumente |
| **3:30** | 30 min | Ručak | 🍽️ | — |
| **4:00** | 45 min | Sesija 03 | Metodologija benchmarkinga | Sustavna usporedba modela |
| **4:45** | 45 min | Sesija 04 | Strategije optimizacije | Analiza SLM-a i LLM-a |
| **5:30** | 60 min | Sesija 05-06 | Napredna orkestracija | Sustavi s više agenata, usmjeravanje |
| **6:30** | 30 min | Praktična radionica 2 | Izrada prilagođenog sustava agenata | Dizajn vlastitog orkestratora |

**Rezultat**: Duboko razumijevanje Edge AI obrazaca plus 2 prilagođena projekta.

---

### 📚 Samostalno učenje (2 tjedna)

**Idealno za: Pojedinačne učenike, online tečajeve, samostalno učenje**

#### 1. tjedan: Osnove (6 sati)

| Dan | Fokus | Trajanje | Bilježnice | Zadaća |
|-----|-------|----------|------------|--------|
| **Pon** | Postavljanje i osnove | 1,5 sat | Sesija 01 | Izmjena upita, testiranje streaminga |
| **Sri** | Osnove RAG-a | 2 sata | Sesija 02 (obje) | Dodavanje vlastitih dokumenata |
| **Pet** | Benchmarking | 1,5 sat | Sesija 03 | Usporedba dodatnih modela |
| **Sub** | Pregled i praksa | 1 sat | Sve iz 1. tjedna | Dovršavanje vježbi, otklanjanje grešaka |

#### 2. tjedan: Napredno (5 sati)

| Dan | Fokus | Trajanje | Bilježnice | Zadaća |
|-----|-------|----------|------------|--------|
| **Pon** | Optimizacija | 1,5 sat | Sesija 04 | Dokumentiranje kompromisa |
| **Sri** | Sustavi s više agenata | 2 sata | Sesija 05 | Dizajn prilagođenih agenata |
| **Pet** | Pametno usmjeravanje | 1,5 sat | Sesija 06 (obje) | Izrada logike usmjeravanja |
| **Sub** | Završni projekt | 2 sata | Integracija | Kombiniranje više obrazaca |

**Rezultat**: Ovladavanje Edge AI obrascima plus projekt za portfelj.

---

## 📔 Opisi bilježnica

### 📘 Sesija 01: Osnove chata
**Datoteka**: `session01_chat_bootstrap.ipynb`  
**Trajanje**: 20-30 minuta  
**Preduvjeti**: Nema  
**Težina**: ⭐ Početnik

**Što ćete naučiti**:
- Instalacija i konfiguracija Foundry Local Python SDK-a
- Korištenje `FoundryLocalManager` za automatsko otkrivanje usluga
- Implementacija osnovnih chat funkcija s API-jem kompatibilnim s OpenAI-jem
- Izrada streaming odgovora za bolje korisničko iskustvo
- Rukovanje greškama i nedostupnosti usluga

**Ključni koncepti**: Upravljanje uslugama, chat funkcije, streaming, rukovanje greškama

**Što ćete izraditi**: Interaktivna chat aplikacija sa streaming podrškom

---

### 📗 Sesija 02: RAG cjevovod
**Datoteka**: `session02_rag_pipeline.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduvjeti**: Sesija 01  
**Težina**: ⭐⭐ Srednje

**Što ćete naučiti**:
- Implementacija obrasca Retrieval Augmented Generation (RAG)
- Stvaranje vektorskih ugrađivanja pomoću sentence-transformers
- Izrada semantičkog pretraživanja pomoću kosinusne sličnosti
- Utemeljivanje odgovora LLM-a u dokumentima specifičnim za domenu
- Rukovanje opcionalnim ovisnostima pomoću zaštite pri uvozu

**Ključni koncepti**: RAG arhitektura, ugrađivanja, semantičko pretraživanje, vektorska sličnost

**Što ćete izraditi**: Sustav za odgovaranje na pitanja temeljen na dokumentima

---

### 📗 Sesija 02: Evaluacija RAG-a pomoću RAGAS-a
**Datoteka**: `session02_rag_eval_ragas.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduvjeti**: Sesija 02 RAG cjevovod  
**Težina**: ⭐⭐ Srednje

**Što ćete naučiti**:
- Evaluacija kvalitete RAG-a pomoću industrijskih standardnih metrika
- Mjerenje relevantnosti konteksta, relevantnosti odgovora, vjerodostojnosti
- Korištenje RAGAS okvira za sustavnu evaluaciju
- Identifikacija i ispravljanje problema kvalitete RAG-a
- Izrada evaluacijskih skupova podataka za vašu domenu

**Ključni koncepti**: Evaluacija RAG-a, RAGAS metrike, mjerenje kvalitete, sustavno testiranje

**Što ćete izraditi**: Okvir za evaluaciju kvalitete RAG-a

---

### 📙 Sesija 03: Benchmark OSS modela
**Datoteka**: `session03_benchmark_oss_models.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduvjeti**: Sesija 01  
**Težina**: ⭐⭐ Srednje

**Što ćete naučiti**:
- Sustavno uspoređivanje više modela
- Mjerenje kašnjenja, propusnosti, vremena prvog tokena
- Implementacija postupnog degradiranja za neuspjehe modela
- Usporedba performansi među obiteljima modela
- Vizualizacija i analiza rezultata benchmarkinga

**Ključni koncepti**: Benchmarking performansi, mjerenje kašnjenja, usporedba modela, statistička analiza

**Što ćete izraditi**: Suite za benchmarking više modela

---

### 📙 Sesija 04: Usporedba modela (SLM vs LLM)
**Datoteka**: `session04_model_compare.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduvjeti**: Sesije 01, 03  
**Težina**: ⭐⭐⭐ Napredno

**Što ćete naučiti**:
- Usporedba malih jezičnih modela (SLM) i velikih jezičnih modela (LLM)
- Analiza kompromisa između performansi i kvalitete
- Mjerenje metrika prikladnosti za rubne uređaje
- Odabir optimalnih modela za ograničenja implementacije
- Dokumentiranje kriterija za odabir modela

**Ključni koncepti**: Odabir modela, analiza kompromisa, strategije optimizacije, planiranje implementacije

**Što ćete izraditi**: Okvir za usporedbu SLM-a i LLM-a

---

### 📕 Sesija 05: Orkestrator više agenata
**Datoteka**: `session05_agents_orchestrator.ipynb`  
**Trajanje**: 45-60 minuta  
**Preduvjeti**: Sesije 01-02  
**Težina**: ⭐⭐⭐ Napredno

**Što ćete naučiti**:
- Dizajniranje specijaliziranih agenata za različite zadatke
- Implementacija memorije agenata i upravljanje kontekstom
- Izrada obrazaca koordinacije za suradnju agenata
- Rukovanje komunikacijom agenata i prijenosima
- Praćenje performansi sustava s više agenata

**Ključni koncepti**: Arhitektura agenata, obrasci koordinacije, upravljanje memorijom, orkestracija agenata

**Što ćete izraditi**: Sustav s više agenata s koordinatorom i specijalistima

---

### 📕 Sesija 06: Usmjerivač modela
**Datoteka**: `session06_models_router.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduvjeti**: Sesije 01, 03  
**Težina**: ⭐⭐⭐ Napredno

**Što ćete naučiti**:
- Implementacija detekcije namjere i prepoznavanja obrazaca
- Izrada usmjeravanja modela temeljenog na ključnim riječima
- Automatsko usmjeravanje upita prema odgovarajućim modelima
- Konfiguracija registara za više modela
- Praćenje odluka o usmjeravanju i performansi

**Ključni koncepti**: Detekcija namjere, usmjeravanje modela, prepoznavanje obrazaca, pametan odabir

**Što ćete izraditi**: Pametni sustav usmjeravanja modela

---

### 📕 Sesija 06: Višekorakni cjevovod
**Datoteka**: `session06_models_pipeline.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduvjeti**: Sesije 01
- Dizajnirajte skalabilne arhitekture modela kao alata

**Ključni pojmovi**: Arhitektura cjevovoda, višestupanjska obrada, oporavak od grešaka, obrasci skalabilnosti

**Što ćete izgraditi**: Inteligentni višestupanjski cjevovod s usmjeravanjem

---

## 🚀 Početak

### Preduvjeti

**Sistemski zahtjevi**:
- **OS**: Windows 10/11, macOS 11+ ili Linux (Ubuntu 20.04+)
- **RAM**: Minimalno 8GB, preporučeno 16GB+
- **Pohrana**: 10GB+ slobodnog prostora za modele
- **Hardver**: CPU s AVX2; GPU (CUDA, Qualcomm NPU) opcionalno

**Softverski zahtjevi**:
- **Python 3.8+** s pip-om
- **Jupyter Notebook** ili **VS Code** s Jupyter ekstenzijom
- **Microsoft Foundry Local** instaliran i konfiguriran
- **Git** (za kloniranje repozitorija)

### Koraci instalacije

#### 1. Instalirajte Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Provjera instalacije**:
```bash
foundry --version
```

#### 2. Postavite Python okruženje

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

#### 3. Pokrenite Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Pokrenite Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Brza provjera

Pokrenite ovo u Python ćeliji za provjeru postavki:

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

**Očekivani izlaz**: Pozdravna poruka od lokalnog modela.

---

## 📝 Najbolje prakse za radionicu

### Za instruktore

**Prije radionice**:
- ✅ Pošaljite upute za instalaciju tjedan dana unaprijed
- ✅ Testirajte sve bilježnice na ciljnom hardveru
- ✅ Pripremite vodič za rješavanje uobičajenih problema
- ✅ Imajte rezervne modele spremne (phi-3.5-mini ako phi-4-mini ne uspije)
- ✅ Postavite zajednički kanal za pitanja

**Tijekom radionice**:
- ✅ Započnite s brzom provjerom okruženja (5 minuta)
- ✅ Odmah podijelite resurse za rješavanje problema
- ✅ Potaknite eksperimentiranje i izmjene
- ✅ Strategijski koristite pauze (nakon svake 2 sesije)
- ✅ Osigurajte pomoć asistenata za individualnu podršku

**Nakon radionice**:
- ✅ Podijelite kompletne radne bilježnice i rješenja
- ✅ Pružite poveznice na dodatne resurse
- ✅ Kreirajte anketu za povratne informacije
- ✅ Ponudite termine za dodatna pitanja

### Za polaznike

**Maksimalno iskoristite učenje**:
- ✅ Dovršite postavke prije početka radionice
- ✅ Pokrenite svaku ćeliju koda sami (nemojte samo čitati)
- ✅ Eksperimentirajte s parametrima i upitima
- ✅ Vodite bilješke o uvidima i problemima
- ✅ Postavljajte pitanja kad zapnete (vjerojatno i drugi imaju isto pitanje)

**Uobičajene greške koje treba izbjegavati**:
- ❌ Preskakanje redoslijeda izvršavanja ćelija (pokrenite ih redom)
- ❌ Nepažljivo čitanje poruka o greškama
- ❌ Prebrzo prolazak bez razumijevanja
- ❌ Ignoriranje objašnjenja u markdownu
- ❌ Ne spremanje izmijenjenih bilježnica

**Savjeti za otklanjanje grešaka**:
1. **Servis ne radi**: Provjerite `foundry service status`
2. **Greške pri uvozu**: Provjerite je li virtualno okruženje aktivirano
3. **Model nije pronađen**: Pokrenite `foundry model ls` za popis učitanih modela
4. **Spori rad**: Provjerite korištenje RAM-a, zatvorite druge aplikacije
5. **Neočekivani rezultati**: Ponovno pokrenite kernel i pokrenite sve ćelije od početka

---

## 🔗 Dodatni resursi

### Materijali za radionicu

- **[Glavni vodič za radionicu](../Readme.md)** - Pregled, ciljevi učenja, karijerni ishodi
- **[Python primjeri](../../../../Workshop/samples)** - Odgovarajući Python skripti za svaku sesiju
- **[Vodiči za sesije](../../../../Workshop)** - Detaljni vodiči u markdownu (Sesija01-06)
- **[Skripte](../../../../Workshop/scripts)** - Alati za validaciju i testiranje
- **[Rješavanje problema](./TROUBLESHOOTING.md)** - Uobičajeni problemi i rješenja
- **[Brzi početak](./quickstart.md)** - Vodič za brzo pokretanje

### Dokumentacija

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Službena Microsoft dokumentacija
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referenca za OpenAI SDK
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentacija za modele ugrađivanja
- **[RAGAS Framework](https://docs.ragas.io/)** - Metodologija evaluacije RAG-a

### Zajednica

- **[GitHub rasprave](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Postavljajte pitanja, dijelite projekte
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Podrška zajednice u stvarnom vremenu
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Tehnička pitanja i odgovori

---

## 🎯 Preporuke za put učenja

### Početnička razina (Počnite ovdje)

1. **Sesija 01** - Pokretanje chata
2. **Sesija 02** - RAG cjevovod
3. **Sesija 03** - Benchmarking modela

**Vrijeme**: ~2 sata | **Fokus**: Osnovni obrasci

---

### Srednja razina

1. Dovršite početničku razinu
2. **Sesija 02** - Evaluacija RAG-a
3. **Sesija 04** - Usporedba modela

**Vrijeme**: ~4 sata | **Fokus**: Kvaliteta i optimizacija

---

### Napredna razina (Cijela radionica)

1. Dovršite srednju razinu
2. **Sesija 05** - Orkestrator više agenata
3. **Sesija 06** - Usmjerivač modela
4. **Sesija 06** - Višestupanjski cjevovod

**Vrijeme**: ~6 sati | **Fokus**: Obrasci za produkciju

---

### Prilagođeni projektni put

1. Dovršite početničku razinu (Sesije 01-03)
2. Odaberite JEDNU naprednu sesiju prema svom cilju:
   - **Izrada RAG aplikacije?** → Sesija 02 Evaluacija
   - **Optimizacija performansi?** → Sesija 04 Usporedba
   - **Složeni tijekovi rada?** → Sesija 05 Orkestrator
   - **Skalabilna arhitektura?** → Sesija 06 Usmjerivač + Cjevovod

**Vrijeme**: ~3 sata | **Fokus**: Vještine specifične za projekt

---

## 📊 Metrike uspjeha

Pratite svoj napredak pomoću ovih prekretnica:

- [ ] **Postavke dovršene** - Foundry Local radi, sve ovisnosti instalirane
- [ ] **Prvi chat** - Sesija 01 dovršena, streaming chata radi
- [ ] **RAG izgrađen** - Sesija 02 dovršena, sustav QA za dokumente funkcionalan
- [ ] **Modeli benchmarkirani** - Sesija 03 dovršena, prikupljeni podaci o performansama
- [ ] **Analizirani kompromisi** - Sesija 04 dovršena, dokumentirani kriteriji za odabir modela
- [ ] **Agenti orkestrirani** - Sesija 05 dovršena, sustav više agenata funkcionalan
- [ ] **Usmjeravanje implementirano** - Sesija 06 dovršena, inteligentni odabir modela funkcionalan
- [ ] **Prilagođeni projekt** - Primijenjeni obrasci radionice na vlastiti slučaj uporabe

---

## 🤝 Doprinos

Pronašli ste problem ili imate prijedlog? Pozdravljamo doprinose!

- **Prijavite probleme**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Predložite poboljšanja**: [GitHub rasprave](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Pošaljite PR-ove**: Slijedite [Smjernice za doprinos](../../AGENTS.md)

---

## 📄 Licenca

Ova radionica dio je repozitorija [EdgeAI za početnike](https://github.com/microsoft/edgeai-for-beginners) i licencirana je pod [MIT licencom](../../../../LICENSE).

---

**Spremni za izradu Edge AI aplikacija spremnih za produkciju?**  
**Započnite s [Sesijom 01: Pokretanje chata](./session01_chat_bootstrap.ipynb) →**

---

*Zadnje ažuriranje: 8. listopada 2025 | Verzija radionice: 2.0*

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.