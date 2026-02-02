# Radionice Beležnice

> **Interaktivne Jupyter beležnice za praktično učenje Edge AI**
>
> Progresivni, samostalni tutorijali koji se razvijaju od osnovnih chat funkcija do naprednih sistema sa više agenata koristeći Microsoft Foundry Local i male jezičke modele.

---

## 📖 Uvod

Dobrodošli u kolekciju **EdgeAI za početnike radionica beležnica**. Ove interaktivne Jupyter beležnice pružaju praktično iskustvo učenja gde ćete pisati, izvršavati i eksperimentisati sa Edge AI kodom u realnom vremenu.

### Zašto Jupyter beležnice?

Za razliku od tradicionalnih tutorijala, ove beležnice nude:

- **Interaktivno učenje**: Pokrenite kod i odmah vidite rezultate
- **Eksperimentisanje**: Modifikujte parametre i posmatrajte promene u realnom vremenu
- **Dokumentacija**: Objašnjenja i markdown ćelije koje vas vode kroz koncepte
- **Reproducibilnost**: Kompletni radni primeri koje možete koristiti i prilagoditi
- **Vizualizacija**: Pregledajte performanse, ugrađene podatke i rezultate direktno u beležnici

### Šta čini ove beležnice posebnim?

Svaka beležnica je dizajnirana prema **najboljim praksama za produkciju**:

✅ **Sveobuhvatno rukovanje greškama** - Elegantno degradiranje i informativne poruke o greškama  
✅ **Tipovi podataka i dokumentacija** - Jasni potpisi funkcija i docstrings  
✅ **Praćenje performansi** - Praćenje korišćenja tokena i merenje kašnjenja  
✅ **Modularni dizajn** - Obrasci koji se mogu ponovo koristiti i prilagoditi vašim projektima  
✅ **Progresivna složenost** - Sistematski se nadovezuje na prethodne sesije  

---

## 🎯 Ciljevi učenja

### Osnovne veštine koje ćete razviti

Radom kroz ove beležnice, savladaćete:

1. **Upravljanje lokalnim AI servisima**
   - Konfigurisanje i upravljanje Microsoft Foundry Local servisima
   - Izbor i učitavanje odgovarajućih modela za vaš hardver
   - Praćenje korišćenja resursa i optimizacija performansi
   - Rukovanje otkrivanjem servisa i proverom zdravlja sistema

2. **Razvoj AI aplikacija**
   - Implementacija lokalnih chat funkcija kompatibilnih sa OpenAI
   - Izrada streaming interfejsa za bolje korisničko iskustvo
   - Dizajniranje efektivnih upita za male jezičke modele
   - Integracija lokalnih modela u aplikacije

3. **Generacija uz podršku pretrage (RAG)**
   - Kreiranje semantičke pretrage sa vektorskim ugrađivanjem
   - Povezivanje odgovora LLM-a sa dokumentima specifičnim za domen
   - Evaluacija kvaliteta RAG-a pomoću RAGAS metrika
   - Skaliranje od prototipa do produkcije

4. **Optimizacija performansi**
   - Sistematsko testiranje više modela
   - Merenje kašnjenja, propusnosti i vremena za prvi token
   - Poređenje malih jezičkih modela sa velikim jezičkim modelima
   - Izbor optimalnih modela na osnovu kompromisa između performansi i kvaliteta

5. **Orkestracija više agenata**
   - Dizajniranje specijalizovanih agenata za različite zadatke
   - Implementacija memorije agenata i upravljanje kontekstom
   - Koordinacija više agenata u složenim radnim tokovima
   - Izrada obrazaca za saradnju agenata

6. **Pametno usmeravanje modela**
   - Implementacija detekcije namere i prepoznavanja obrazaca
   - Automatsko usmeravanje upita ka odgovarajućim modelima
   - Izrada višestepenih radnih tokova (plan → izvrši → poboljšaj)
   - Dizajniranje skalabilnih arhitektura modela kao alata

---

## 🎓 Ishodi učenja

### Šta ćete izgraditi

| Beležnica | Rezultat | Demonstrirane veštine | Težina |
|-----------|----------|-----------------------|--------|
| **Sesija 01** | Chat aplikacija sa streamingom | Postavljanje servisa, osnovne funkcije, UX za streaming | ⭐ Početnik |
| **Sesija 02 (RAG)** | RAG sistem sa evaluacijom | Ugrađivanje, semantička pretraga, metrički kvalitet | ⭐⭐ Srednji nivo |
| **Sesija 02 (Eval)** | Evaluator kvaliteta RAG-a | RAGAS metrike, sistematska evaluacija | ⭐⭐ Srednji nivo |
| **Sesija 03** | Benchmark više modela | Merenje performansi, poređenje modela | ⭐⭐ Srednji nivo |
| **Sesija 04** | Poređenje SLM-a i LLM-a | Analiza kompromisa, strategije optimizacije | ⭐⭐⭐ Napredni nivo |
| **Sesija 05** | Orkestrator više agenata | Dizajn agenata, memorija, koordinacija | ⭐⭐⭐ Napredni nivo |
| **Sesija 06 (Router)** | Pametni sistem usmeravanja | Detekcija namere, izbor modela | ⭐⭐⭐ Napredni nivo |
| **Sesija 06 (Pipeline)** | Višestepeni radni tok | Plan/izvrši/poboljšaj radni tokovi | ⭐⭐⭐ Napredni nivo |

### Progres kompetencija

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

**Idealno za: Timsku obuku, hakatone, konferencijske radionice**

| Vreme | Trajanje | Sesija | Teme | Aktivnosti |
|-------|----------|--------|------|------------|
| **0:00** | 30 min | Postavljanje i uvod | Postavljanje okruženja, instalacija Foundry Local | Instalacija zavisnosti, provera sistema |
| **0:30** | 30 min | Sesija 01 | Osnovne chat funkcije, streaming | Pokretanje beležnice, modifikacija upita |
| **1:00** | 45 min | Sesija 02 | RAG sistem, ugrađivanje, evaluacija | Izrada RAG sistema, testiranje upita |
| **1:45** | 15 min | Pauza | ☕ Kafa i pitanja | — |
| **2:00** | 30 min | Sesija 03 | Benchmark više modela | Poređenje 3+ modela |
| **2:30** | 30 min | Sesija 04 | Kompromisi između SLM-a i LLM-a | Analiza performansi/kvaliteta |
| **3:00** | 30 min | Sesija 05-06 | Sistemi sa više agenata i usmeravanje | Istraživanje naprednih obrazaca |

**Rezultat**: Učesnici odlaze sa 6 funkcionalnih Edge AI aplikacija i kodom spremnim za produkciju.

---

### 🎓 Celodnevna radionica (6 sati)

**Idealno za: Detaljnu obuku, bootcampove, univerzitetske kurseve**

| Vreme | Trajanje | Sesija | Teme | Aktivnosti |
|-------|----------|--------|------|------------|
| **0:00** | 45 min | Postavljanje i teorija | Postavljanje okruženja, osnove Edge AI | Instalacija, provera, diskusija o slučajevima |
| **0:45** | 45 min | Sesija 01 | Detaljno o chat funkcijama | Implementacija osnovnih i streaming chat funkcija |
| **1:30** | 30 min | Pauza | ☕ Kafa i umrežavanje | — |
| **2:00** | 60 min | Sesija 02 (obe) | RAG sistem + evaluacija RAGAS-a | Izrada kompletnog RAG sistema |
| **3:00** | 30 min | Praktična laboratorija 1 | Prilagođeni RAG za vaš domen | Primena na sopstvene dokumente |
| **3:30** | 30 min | Ručak | 🍽️ | — |
| **4:00** | 45 min | Sesija 03 | Metodologija benchmarkinga | Sistematsko poređenje modela |
| **4:45** | 45 min | Sesija 04 | Strategije optimizacije | Analiza SLM-a i LLM-a |
| **5:30** | 60 min | Sesija 05-06 | Napredna orkestracija | Sistemi sa više agenata, usmeravanje |
| **6:30** | 30 min | Praktična laboratorija 2 | Izrada prilagođenog sistema agenata | Dizajn sopstvenog orkestratora |

**Rezultat**: Duboko razumevanje Edge AI obrazaca plus 2 prilagođena projekta.

---

### 📚 Samostalno učenje (2 nedelje)

**Idealno za: Individualne učenike, online kurseve, samostalno učenje**

#### Nedelja 1: Osnove (6 sati)

| Dan | Fokus | Trajanje | Beležnice | Domaći zadatak |
|-----|-------|----------|-----------|----------------|
| **Pon** | Postavljanje i osnove | 1,5 sat | Sesija 01 | Modifikacija upita, testiranje streaminga |
| **Sre** | Osnove RAG-a | 2 sata | Sesija 02 (obe) | Dodavanje sopstvenih dokumenata |
| **Pet** | Benchmarking | 1,5 sat | Sesija 03 | Poređenje dodatnih modela |
| **Sub** | Pregled i praksa | 1 sat | Sve iz nedelje 1 | Završavanje vežbi, otklanjanje grešaka |

#### Nedelja 2: Napredni nivo (5 sati)

| Dan | Fokus | Trajanje | Beležnice | Domaći zadatak |
|-----|-------|----------|-----------|----------------|
| **Pon** | Optimizacija | 1,5 sat | Sesija 04 | Dokumentovanje kompromisa |
| **Sre** | Sistemi sa više agenata | 2 sata | Sesija 05 | Dizajn prilagođenih agenata |
| **Pet** | Pametno usmeravanje | 1,5 sat | Sesija 06 (obe) | Izrada logike usmeravanja |
| **Sub** | Završni projekat | 2 sata | Integracija | Kombinovanje više obrazaca |

**Rezultat**: Savladavanje Edge AI obrazaca plus portfolio projekat.

---

## 📔 Opisi beležnica

### 📘 Sesija 01: Osnovni chat
**Fajl**: `session01_chat_bootstrap.ipynb`  
**Trajanje**: 20-30 minuta  
**Preduslovi**: Nema  
**Težina**: ⭐ Početnik

**Šta ćete naučiti**:
- Instalacija i konfiguracija Foundry Local Python SDK-a
- Korišćenje `FoundryLocalManager` za automatsko otkrivanje servisa
- Implementacija osnovnih chat funkcija kompatibilnih sa OpenAI API-jem
- Izrada streaming odgovora za bolje korisničko iskustvo
- Elegantno rukovanje greškama i nedostupnošću servisa

**Ključni koncepti**: Upravljanje servisima, chat funkcije, streaming, rukovanje greškama

**Šta ćete izgraditi**: Interaktivna chat aplikacija sa podrškom za streaming

---

### 📗 Sesija 02: RAG sistem
**Fajl**: `session02_rag_pipeline.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduslovi**: Sesija 01  
**Težina**: ⭐⭐ Srednji nivo

**Šta ćete naučiti**:
- Implementacija obrasca Retrieval Augmented Generation (RAG)
- Kreiranje vektorskih ugrađivanja pomoću sentence-transformers
- Izrada semantičke pretrage pomoću kosinusne sličnosti
- Povezivanje odgovora LLM-a sa dokumentima specifičnim za domen
- Rukovanje opcionalnim zavisnostima pomoću zaštite pri uvozu

**Ključni koncepti**: RAG arhitektura, ugrađivanje, semantička pretraga, vektorska sličnost

**Šta ćete izgraditi**: Sistem za odgovaranje na pitanja zasnovan na dokumentima

---

### 📗 Sesija 02: Evaluacija RAG-a pomoću RAGAS-a
**Fajl**: `session02_rag_eval_ragas.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduslovi**: Sesija 02 RAG sistem  
**Težina**: ⭐⭐ Srednji nivo

**Šta ćete naučiti**:
- Evaluacija kvaliteta RAG-a pomoću industrijskih standardnih metrika
- Merenje relevantnosti konteksta, relevantnosti odgovora, verodostojnosti
- Korišćenje RAGAS okvira za sistematsku evaluaciju
- Identifikacija i rešavanje problema kvaliteta RAG-a
- Izrada datasetova za evaluaciju specifičnih za vaš domen

**Ključni koncepti**: Evaluacija RAG-a, RAGAS metrike, merenje kvaliteta, sistematsko testiranje

**Šta ćete izgraditi**: Okvir za evaluaciju kvaliteta RAG-a

---

### 📙 Sesija 03: Benchmark OSS modela
**Fajl**: `session03_benchmark_oss_models.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduslovi**: Sesija 01  
**Težina**: ⭐⭐ Srednji nivo

**Šta ćete naučiti**:
- Sistematsko testiranje više modela
- Merenje kašnjenja, propusnosti, vremena za prvi token
- Implementacija elegantnog degradiranja za neuspehe modela
- Poređenje performansi između porodica modela
- Vizualizacija i analiza rezultata testiranja

**Ključni koncepti**: Benchmarking performansi, merenje kašnjenja, poređenje modela, statistička analiza

**Šta ćete izgraditi**: Suite za testiranje više modela

---

### 📙 Sesija 04: Poređenje modela (SLM vs LLM)
**Fajl**: `session04_model_compare.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduslovi**: Sesije 01, 03  
**Težina**: ⭐⭐⭐ Napredni nivo

**Šta ćete naučiti**:
- Poređenje malih jezičkih modela sa velikim jezičkim modelima
- Analiza kompromisa između performansi i kvaliteta
- Merenje metrika pogodnosti za edge sisteme
- Izbor optimalnih modela za ograničenja u implementaciji
- Dokumentovanje kriterijuma za izbor modela

**Ključni koncepti**: Izbor modela, analiza kompromisa, strategije optimizacije, planiranje implementacije

**Šta ćete izgraditi**: Okvir za poređenje SLM-a i LLM-a

---

### 📕 Sesija 05: Orkestrator više agenata
**Fajl**: `session05_agents_orchestrator.ipynb`  
**Trajanje**: 45-60 minuta  
**Preduslovi**: Sesije 01-02  
**Težina**: ⭐⭐⭐ Napredni nivo

**Šta ćete naučiti**:
- Dizajn specijalizovanih agenata za različite zadatke
- Implementacija memorije agenata i upravljanje kontekstom
- Izrada obrazaca za koordinaciju agenata
- Rukovanje komunikacijom i predajom između agenata
- Praćenje performansi sistema sa više agenata

**Ključni koncepti**: Arhitektura agenata, obrasci koordinacije, upravljanje memorijom, orkestracija agenata

**Šta ćete izgraditi**: Sistem sa više agenata sa koordinatorom i specijalistima

---

### 📕 Sesija 06: Usmeravanje modela
**Fajl**: `session06_models_router.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduslovi**: Sesije 01, 03  
**Težina**: ⭐⭐⭐ Napredni nivo

**Šta ćete naučiti**:
- Implementacija detekcije namere i prepoznavanja obrazaca
- Izrada usmeravanja modela zasnovanog na ključnim rečima
- Automatsko usmeravanje upita ka odgovarajućim modelima
- Konfiguracija registara za više modela
- Praćenje odluka o usmeravanju i performansi

**Ključni koncepti**: Detekcija namere, usmeravanje modela, prepoznavanje obrazaca, pametan izbor

**Šta ćete izgraditi**: Pametni sistem za usmeravanje modela

---

### 📕 Sesija 06: Višestepeni radni tok
**Fajl**: `session06_models_pipeline.ipynb`  
**Trajanje**: 30-45 minuta  
**Preduslovi**: Sesije 01, 06 Usmeravanje  
**Težina**: ⭐⭐⭐ Napredni nivo

**Šta ćete naučiti**:
- Izrada višestepenih AI radnih tokova (plan → izvrši → poboljšaj)
- Integracija usmerivača za pametan izbor modela
- Implementacija rukovanja greškama i oporavka u radnom toku
- Praćenje performansi i faza radnog toka
- Дизајнирајте архитектуре модела као алата које се могу скалирати

**Кључни концепти**: Архитектура цевовода, обрада у више фаза, опоравак од грешака, обрасци скалабилности

**Шта ћете направити**: Интелигентни цевовод са више корака и рутирањем

---

## 🚀 Почетак

### Предуслови

**Системски захтеви**:
- **ОС**: Windows 10/11, macOS 11+ или Linux (Ubuntu 20.04+)
- **РАМ**: Минимум 8GB, препоручено 16GB+
- **Складиште**: 10GB+ слободног простора за моделе
- **Хардвер**: CPU са AVX2; GPU (CUDA, Qualcomm NPU) опционо

**Софтверски захтеви**:
- **Python 3.8+** са pip
- **Jupyter Notebook** или **VS Code** са Jupyter екстензијом
- **Microsoft Foundry Local** инсталиран и конфигурисан
- **Git** (за клонирање репозиторијума)

### Кораци за инсталацију

#### 1. Инсталирајте Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Потврдите инсталацију**:
```bash
foundry --version
```

#### 2. Поставите Python окружење

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

#### 3. Покрените Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Покрените Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Брза провера

Покрените ово у Python ћелији да проверите подешавање:

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

**Очекивани резултат**: Одговор добродошлице од локалног модела.

---

## 📝 Најбоље праксе за радионицу

### За инструкторе

**Пре радионице**:
- ✅ Пошаљите упутства за инсталацију недељу дана унапред
- ✅ Тестирајте све бележнице на циљном хардверу
- ✅ Припремите водич за решавање уобичајених проблема
- ✅ Имајте резервне моделе спремне (phi-3.5-mini ако phi-4-mini не ради)
- ✅ Поставите заједнички канал за питања

**Током радионице**:
- ✅ Почните са брзом провером окружења (5 минута)
- ✅ Одмах поделите ресурсе за решавање проблема
- ✅ Подстакните експериментисање и модификације
- ✅ Стратешки користите паузе (након сваке 2 сесије)
- ✅ Имајте асистенте доступне за индивидуалну помоћ

**После радионице**:
- ✅ Поделите комплетне бележнице и решења
- ✅ Обезбедите линкове ка додатним ресурсима
- ✅ Направите анкету за повратне информације ради побољшања
- ✅ Понудите термине за додатна питања

### За учеснике

**Максимизирајте своје учење**:
- ✅ Завршите подешавање пре почетка радионице
- ✅ Покрените сваки код сами (не само читајте)
- ✅ Експериментишите са параметрима и упутствима
- ✅ Бележите увиде и важне напомене
- ✅ Питајте када сте заглављени (вероватно и други имају исто питање)

**Уобичајене грешке које треба избегавати**:
- ❌ Прескакање редоследа извршавања ћелија (покрените их редом)
- ❌ Непажљиво читање порука о грешкама
- ❌ Пролазак кроз материјал без разумевања
- ❌ Игнорисање објашњења у markdown-у
- ❌ Неснимање модификованих бележница

**Савети за решавање проблема**:
1. **Сервис не ради**: Проверите `foundry service status`
2. **Грешке при увозу**: Проверите да ли је виртуелно окружење активирано
3. **Модел није пронађен**: Покрените `foundry model ls` да листате учитане моделе
4. **Спор рад**: Проверите употребу РАМ-а, затворите друге апликације
5. **Неочекивани резултати**: Поново покрените kernel и покрените све ћелије од врха

---

## 🔗 Додатни ресурси

### Материјали за радионицу

- **[Главни водич за радионицу](../Readme.md)** - Преглед, циљеви учења, каријерни исходи
- **[Python примери](../../../../Workshop/samples)** - Одговарајући Python скриптови за сваку сесију
- **[Водичи за сесије](../../../../Workshop)** - Детаљни markdown водичи (Session01-06)
- **[Скриптови](../../../../Workshop/scripts)** - Алатке за валидацију и тестирање
- **[Решавање проблема](./TROUBLESHOOTING.md)** - Уобичајени проблеми и решења
- **[Брзи почетак](./quickstart.md)** - Водич за брзи почетак

### Документација

- **[Foundry Local документација](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Званична Microsoft документација
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Референца за OpenAI SDK
- **[Sentence Transformers](https://www.sbert.net/)** - Документација за моделе уграђивања
- **[RAGAS Framework](https://docs.ragas.io/)** - Метрике за евалуацију RAG-а

### Заједница

- **[GitHub дискусије](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Поставите питања, поделите пројекте
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Подршка у реалном времену
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Техничка питања и одговори

---

## 🎯 Препоруке за пут учења

### Почетни ниво (почните овде)

1. **Сесија 01** - Покретање чата
2. **Сесија 02** - RAG цевовод
3. **Сесија 03** - Бенчмарк модела

**Време**: ~2 сата | **Фокус**: Основни обрасци

---

### Средњи ниво

1. Завршите почетни ниво
2. **Сесија 02** - Евалуација RAG-а
3. **Сесија 04** - Поређење модела

**Време**: ~4 сата | **Фокус**: Квалитет и оптимизација

---

### Напредни ниво (целокупна радионица)

1. Завршите средњи ниво
2. **Сесија 05** - Оркестратор са више агената
3. **Сесија 06** - Рутер модела
4. **Сесија 06** - Цевовод са више корака

**Време**: ~6 сати | **Фокус**: Производни обрасци

---

### Пут прилагођен пројекту

1. Завршите почетни ниво (Сесије 01-03)
2. Изаберите ЈЕДНУ напредну сесију на основу вашег циља:
   - **Правите RAG апликацију?** → Сесија 02 Евалуација
   - **Оптимизујете перформансе?** → Сесија 04 Поређење
   - **Комплексни токови рада?** → Сесија 05 Оркестратор
   - **Скалабилна архитектура?** → Сесија 06 Рутер + Цевовод

**Време**: ~3 сата | **Фокус**: Вештине специфичне за пројекат

---

## 📊 Мерила успеха

Пратите свој напредак помоћу ових прекретница:

- [ ] **Подешавање завршено** - Foundry Local ради, све зависности инсталиране
- [ ] **Први чат** - Сесија 01 завршена, стриминг чата функционише
- [ ] **RAG направљен** - Сесија 02 завршена, систем за QA докумената функционалан
- [ ] **Модели бенчмаркирани** - Сесија 03 завршена, прикупљени подаци о перформансама
- [ ] **Анализирани компромиси** - Сесија 04 завршена, критеријуми за избор модела документовани
- [ ] **Оркестрирани агенти** - Сесија 05 завршена, систем са више агената функционише
- [ ] **Рутирање имплементирано** - Сесија 06 завршена, интелигентан избор модела функционалан
- [ ] **Прилагођен пројекат** - Примењени обрасци радионице на ваш случај употребе

---

## 🤝 Доприноси

Пронашли сте проблем или имате предлог? Добродошли су сви доприноси!

- **Пријавите проблеме**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Предложите побољшања**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Пошаљите PR-ове**: Пратите [Упутства за допринос](../../AGENTS.md)

---

## 📄 Лиценца

Ова радионица је део репозиторијума [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) и лиценцирана је под [MIT лиценцом](../../../../LICENSE).

---

**Спремни да направите Edge AI апликације спремне за производњу?**  
**Почните са [Сесијом 01: Покретање чата](./session01_chat_bootstrap.ipynb) →**

---

*Последње ажурирање: 8. октобар 2025 | Верзија радионице: 2.0*

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.