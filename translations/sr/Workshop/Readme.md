<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T23:21:49+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "sr"
}
-->
# EdgeAI за почетнике - Радионица

> **Практични курс за изградњу Edge AI апликација спремних за производњу**
>
> Савладајте локално постављање вештачке интелигенције уз Microsoft Foundry Local, од првог завршетка разговора до оркестрације више агената у 6 прогресивних сесија.

---

## 🎯 Увод

Добродошли на **EdgeAI за почетнике радионицу** - ваш практични водич за изградњу интелигентних апликација које раде искључиво на локалном хардверу. Ова радионица претвара теоријске концепте Edge AI у стварне вештине кроз прогресивно изазовне вежбе користећи Microsoft Foundry Local и Small Language Models (SLMs).

### Зашто ова радионица?

**Револуција Edge AI је овде**

Организације широм света прелазе са AI зависног од облака на edge рачунарство из три кључна разлога:

1. **Приватност и усклађеност** - Обрада осетљивих података локално без преноса у облак (HIPAA, GDPR, финансијски прописи)
2. **Перформансе** - Елиминисање кашњења мреже (50-500ms локално наспрам 500-2000ms облак)
3. **Контрола трошкова** - Уклањање трошкова по токену API-ја и скалирање без облачних трошкова

**Али Edge AI је другачији**

Покретање AI-а на локалним уређајима захтева нове вештине:
- Избор и оптимизација модела за ограничене ресурсе
- Управљање локалним сервисима и хардверска убрзања
- Инжењеринг упита за мање моделе
- Шаблони за производну имплементацију на edge уређајима

**Ова радионица пружа те вештине**

У 6 фокусираних сесија (~3 сата укупно), напредоваћете од "Hello World" до постављања производно спремних система са више агената - све локално на вашем рачунару.

---

## 📚 Циљеви учења

Завршетком ове радионице, бићете у могућности да:

### Основне компетенције
1. **Поставите и управљате локалним AI сервисима**
   - Инсталирајте и конфигуришите Microsoft Foundry Local
   - Изаберите одговарајуће моделе за edge имплементацију
   - Управљајте животним циклусом модела (преузимање, учитавање, кеширање)
   - Пратите коришћење ресурса и оптимизујте перформансе

2. **Изградите апликације засноване на AI-у**
   - Имплементирајте OpenAI-компатибилне завршетке разговора локално
   - Дизајнирајте ефикасне упите за Small Language Models
   - Руковање стриминг одговорима за бољи UX
   - Интегришите локалне моделе у постојеће апликације

3. **Креирајте RAG (Retrieval Augmented Generation) системе**
   - Изградите семантичку претрагу са уграђеним функцијама
   - Заснујте одговоре LLM-а на знању специфичном за домен
   - Процените квалитет RAG-а користећи индустријске стандарде
   - Скалирајте од прототипа до производње

4. **Оптимизујте перформансе модела**
   - Тестирајте више модела за вашу употребу
   - Мерите кашњење, пропусност и време првог токена
   - Изаберите оптималне моделе на основу компромиса брзина/квалитет
   - Упоредите SLM и LLM компромисе у стварним сценаријима

5. **Оркестрирајте системе са више агената**
   - Дизајнирајте специјализоване агенте за различите задатке
   - Имплементирајте меморију агента и управљање контекстом
   - Координишите агенте у сложеним токовима рада
   - Паметно усмеравајте захтеве преко више модела

6. **Поставите решења спремна за производњу**
   - Имплементирајте руковање грешкама и логику поновног покушаја
   - Пратите коришћење токена и системских ресурса
   - Изградите скалабилне архитектуре са шаблонима модела као алата
   - Планирајте миграционе путеве од edge до хибридних (edge + облак)

---

## 🎓 Резултати учења

### Шта ћете изградити

До краја ове радионице, креираћете:

| Сесија | Испорука | Демонстриране вештине |
|--------|----------|-----------------------|
| **1** | Апликација за разговор са стримингом | Постављање сервиса, основни завршетци, UX стриминга |
| **2** | RAG систем са евалуацијом | Уграђене функције, семантичка претрага, метрике квалитета |
| **3** | Суита за бенчмаркинг више модела | Мерење перформанси, поређење модела |
| **4** | Компаратор SLM и LLM | Анализа компромиса, стратегије оптимизације |
| **5** | Оркестратор са више агената | Дизајн агента, управљање меморијом, координација |
| **6** | Систем за паметно усмеравање | Детекција намере, избор модела, скалабилност |

### Матрица компетенција

| Ниво вештина | Сесија 1-2 | Сесија 3-4 | Сесија 5-6 |
|--------------|------------|------------|------------|
| **Почетник** | ✅ Постављање и основе | ⚠️ Изазовно | ❌ Превише напредно |
| **Средњи ниво** | ✅ Брз преглед | ✅ Основно учење | ⚠️ Циљеви за напредак |
| **Напредни** | ✅ Лако пролазе | ✅ Унапређење | ✅ Шаблони за производњу |

### Вештине за каријеру

**Након ове радионице, бићете спремни да:**

✅ **Изградите апликације које прво воде рачуна о приватности**
- Апликације за здравство које локално обрађују PHI/PII
- Финансијске услуге са захтевима за усклађеност
- Владине системе са потребама за суверенитетом података

✅ **Оптимизујете за Edge окружења**
- IoT уређаје са ограниченим ресурсима
- Мобилне апликације које раде офлајн
- Системе за реално време са ниским кашњењем

✅ **Дизајнирате интелигентне архитектуре**
- Системе са више агената за сложене токове рада
- Хибридне edge-cloud имплементације
- AI инфраструктуру оптимизовану за трошкове

✅ **Водите Edge AI иницијативе**
- Процените изводљивост Edge AI за пројекте
- Изаберите одговарајуће моделе и оквире
- Дизајнирајте скалабилна локална AI решења

---

## 🗺️ Структура радионице

### Преглед сесија (6 сесија × 30 минута = 3 сата)

| Сесија | Тема | Фокус | Трајање |
|--------|------|-------|---------|
| **1** | Почетак са Foundry Local | Инсталација, валидација, први завршетци | 30 мин |
| **2** | Изградња AI решења са RAG | Инжењеринг упита, уграђене функције, евалуација | 30 мин |
| **3** | Модели отвореног кода | Откривање модела, бенчмаркинг, избор | 30 мин |
| **4** | Најсавременији модели | SLM vs LLM, оптимизација, оквири | 30 мин |
| **5** | Агенти засновани на AI-у | Дизајн агента, оркестрација, меморија | 30 мин |
| **6** | Модели као алати | Усмеравање, лансирање, стратегије скалирања | 30 мин |

---

## 🚀 Брзи почетак

### Предуслови

**Системски захтеви:**
- **OS**: Windows 10/11, macOS 11+, или Linux (Ubuntu 20.04+)
- **RAM**: Минимум 8GB, препоручено 16GB+
- **Складиште**: 10GB+ слободног простора за моделе
- **CPU**: Модеран процесор са AVX2 подршком
- **GPU** (опционо): CUDA-компатибилан или Qualcomm NPU за убрзање

**Софтверски захтеви:**
- **Python 3.8+** ([Преузми](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Упутство за инсталацију](../../../Workshop))
- **Git** ([Преузми](https://git-scm.com/downloads))
- **Visual Studio Code** (препоручено) ([Преузми](https://code.visualstudio.com/))

### Постављање у 3 корака

#### 1. Инсталирајте Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Потврдите инсталацију:**
```bash
foundry --version
foundry service status
```

**Уверите се да Azure AI Foundry Local ради са фиксним портом**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Потврдите да ради:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Проналажење доступних модела**
Да бисте видели који модели су доступни у вашој Foundry Local инстанци, можете упитати крајњу тачку модела:

```bash
# cmd/bash/powershell
foundry model list
```

Коришћење веб крајње тачке 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Клонирајте репозиторијум и инсталирајте зависности

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Покрените ваш први пример

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Успех!** Требало би да видите стриминг одговор о Edge AI-у.

---

## 📦 Ресурси радионице

### Python примери

Прогресивни практични примери који демонстрирају сваки концепт:

| Сесија | Пример | Опис | Време извршења |
|--------|--------|------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Основни & стриминг разговор | ~30с |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG са уграђеним функцијама | ~45с |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Евалуација квалитета RAG-а | ~60с |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Бенчмаркинг више модела | ~2-3м |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Компарација SLM и LLM | ~45с |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Систем са више агената | ~60с |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Усмеравање засновано на намери | ~45с |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Вишестепена оркестрација | ~60с |

### Jupyter бележнице

Интерактивно истраживање са објашњењима и визуализацијама:

| Сесија | Бележница | Опис | Тежина |
|--------|-----------|------|--------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Основе разговора & стриминг | ⭐ Почетник |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Изградња RAG система | ⭐⭐ Средњи ниво |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Евалуација квалитета RAG-а | ⭐⭐ Средњи ниво |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Бенчмаркинг модела | ⭐⭐ Средњи ниво |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Компарација модела | ⭐⭐ Средњи ниво |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Оркестрација агента | ⭐⭐⭐ Напредно |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Усмеравање намере | ⭐⭐⭐ Напредно |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Оркестрација токова | ⭐⭐⭐ Напредно |

### Документација

Свеобухватни водичи и референце:

| Документ | Опис | Када користити |
|----------|------|---------------|
| [QUICK_START.md](./QUICK_START.md) | Водич за брзо постављање | Почетак од нуле |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Листа команди и API-а | Потребни брзи одговори |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Шаблони SDK-а и примери | Писање кода |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Водич за конфигурацију променљивих окружења | Конфигурисање примера |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Најновија побољшања примера | Разумевање промена |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Водич за миграцију | Надоградња кода |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Уобичајени проблеми и решења | Решавање проблема |

---

## 🎓 Препоруке за пут учења

### За почетнике (3-4 сата)
1. ✅ Сесија 1: Почетак (фокус на постављање и основни разговор)
2. ✅ Сесија 2: Основе RAG-а (прескочите евалуацију у почетку)
3. ✅ Сесија 3: Једноставан бенчмаркинг (само 2 модела)
4. ⏭️ Прескочите сесије 4-6 за сада
5. 🔄 Вратите се на сесије 4-6 након изградње прве апликације

### За програмере средњег нивоа (3 сата)
1. ⚡ Сесија 1: Брза валидација постављања
2. ✅ Сесија 2: Комплетан RAG ток са евалуацијом
3. ✅ Сесија 3: Комплетна суита за бенчмаркинг
4. ✅ Сесија 4: Оптимизација модела
5. ✅ Сесије 5-6: Фокус на архитектонске шаблоне

### За напредне практичаре (2-3 сата)
1. ⚡ Сесије 1-3: Брз преглед и валидација
2. ✅ Сесија 4: Дубинска оптимизација
3. ✅ Сесија 5: Архитектура са више агената
4. ✅ Сесија 6: Шаблони за производњу и скалирање
5. 🚀 Проширите: Изградите прилагођену логику усмеравања и хибридне имплементације

---

## Пакет сесија радионице
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX ubrzanje |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Uloge agenata, memorija, alati, orkestracija |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Rutiranje, povezivanje, skaliranje na Azure |

Svaka datoteka sesije uključuje: apstrakt, ciljeve učenja, tok demonstracije od 30 minuta, početni projekat, kontrolnu listu za validaciju, rešavanje problema i reference na zvanični Foundry Local Python SDK.

### Primeri skripti

Instalacija zavisnosti za radionicu (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ako pokrećete Foundry Local servis na drugoj (Windows) mašini ili VM sa macOS-a, izvezite endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesija | Skripta(e) | Opis |
|--------|------------|------|
| 1 | `samples/session01/chat_bootstrap.py` | Pokretanje servisa i strimovanje četa |
| 2 | `samples/session02/rag_pipeline.py` | Minimalni RAG (ugrađivanja u memoriji) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluacija RAG-a sa ragas metrikama |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latencije i propusnosti za više modela |
| 4 | `samples/session04/model_compare.py` | Poređenje SLM i LLM (latencija i uzorci rezultata) |
| 5 | `samples/session05/agents_orchestrator.py` | Dvoagentna istraživačka → urednička pipeline |
| 6 | `samples/session06/models_router.py` | Demo rutiranja zasnovanog na nameri |
|   | `samples/session06/models_pipeline.py` | Višestepeni lanac planiranja/izvršavanja/usavršavanja |

### Promenljive okruženja (zajedničke za sve primere)

| Promenljiva | Svrha | Primer |
|-------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Podrazumevani alias za jedan model za osnovne primere | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Eksplicitni SLM naspram većeg modela za poređenje | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Lista aliasa za benchmarking | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Broj ponavljanja benchmarka po modelu | `3` |
| `BENCH_PROMPT` | Prompt korišćen u benchmarkingu | `Objasnite ukratko retrieval augmented generation.` |
| `EMBED_MODEL` | Sentence-transformers model za ugrađivanje | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Prepisivanje testnog upita za RAG pipeline | `Zašto koristiti RAG sa lokalnom inferencom?` |
| `AGENT_QUESTION` | Prepisivanje upita za pipeline agenata | `Objasnite zašto je edge AI važan za usklađenost.` |
| `AGENT_MODEL_PRIMARY` | Alias modela za istraživačkog agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modela za uredničkog agenta (može se razlikovati) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kada je `1`, prikazuje potrošnju tokena po završetku | `1` |
| `RETRY_ON_FAIL` | Kada je `1`, ponovo pokušava u slučaju privremenih grešaka u četu | `1` |
| `RETRY_BACKOFF` | Sekunde čekanja pre ponovnog pokušaja | `1.0` |

Ako promenljiva nije postavljena, skripte koriste razumne podrazumevane vrednosti. Za demonstracije sa jednim modelom obično je potrebna samo `FOUNDRY_LOCAL_ALIAS`.

### Pomoćni modul

Svi primeri sada dele pomoćni `samples/workshop_utils.py` koji pruža:

* Keširani `FoundryLocalManager` + kreiranje OpenAI klijenta
* Pomoćnu funkciju `chat_once()` sa opcionalnim ponovnim pokušajem + prikazom potrošnje
* Jednostavno izveštavanje o potrošnji tokena (omogućeno preko `SHOW_USAGE=1`)

Ovo smanjuje dupliranje i ističe najbolje prakse za efikasnu orkestraciju lokalnih modela.

## Opcionalna poboljšanja (za sve sesije)

| Tema | Poboljšanje | Sesije | Okruženje / Prekidač |
|------|-------------|--------|----------------------|
| Determinizam | Fiksirana temperatura + stabilni setovi promptova | 1–6 | Postavite `temperature=0`, `top_p=1` |
| Vidljivost potrošnje tokena | Dosledno podučavanje o troškovima/efikasnosti | 1–6 | `SHOW_USAGE=1` |
| Strimovanje prvog tokena | Metrička latencija u percepciji | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Otpornost na greške | Rukovanje privremenim greškama pri hladnom startu | Sve | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Višemodelni agenti | Specijalizacija uloga sa heterogenim modelima | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptivno rutiranje | Heuristika zasnovana na nameri + troškovima | 6 | Proširite router sa logikom eskalacije |
| Vektorska memorija | Dugoročno semantičko pamćenje | 2,5,6 | Integracija FAISS/Chroma indeksa ugrađivanja |
| Izvoz tragova | Revizija i evaluacija | 2,5,6 | Dodajte JSON linije po koraku |
| Kvalitativne metrike | Praćenje kvaliteta | 3–6 | Sekundarni promptovi za ocenjivanje |
| Brzi testovi | Brza validacija pre radionice | Sve | `python Workshop/tests/smoke.py` |

### Deterministički brzi početak

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Očekujte stabilan broj tokena kroz ponovljene identične ulaze.

### Evaluacija RAG-a (Sesija 2)

Koristite `rag_eval_ragas.py` za izračunavanje relevantnosti odgovora, verodostojnosti i preciznosti konteksta na malom sintetičkom skupu podataka:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Proširite dodavanjem većeg JSONL-a sa pitanjima, kontekstima i tačnim odgovorima, a zatim konvertujte u Hugging Face `Dataset`.

## Dodatak za tačnost CLI komandi

Radionica koristi samo trenutno dokumentovane/stabilne Foundry Local CLI komande.

### Stabilne komande koje se koriste

| Kategorija | Komanda | Svrha |
|------------|---------|-------|
| Osnovno | `foundry --version` | Prikazuje instaliranu verziju |
| Osnovno | `foundry init` | Inicijalizuje konfiguraciju |
| Servis | `foundry service start` | Pokreće lokalni servis (ako nije automatski) |
| Servis | `foundry status` | Prikazuje status servisa |
| Modeli | `foundry model list` | Prikazuje katalog / dostupne modele |
| Modeli | `foundry model download <alias>` | Preuzima težine modela u keš |
| Modeli | `foundry model run <alias>` | Pokreće (učitava) model lokalno; kombinujte sa `--prompt` za jednokratni upit |
| Modeli | `foundry model unload <alias>` / `foundry model stop <alias>` | Uklanja model iz memorije (ako je podržano) |
| Keš | `foundry cache list` | Prikazuje keširane (preuzete) modele |
| Sistem | `foundry system info` | Snimak hardverskih i akceleracionih mogućnosti |
| Sistem | `foundry system gpu-info` | Dijagnostičke informacije o GPU-u |
| Konfiguracija | `foundry config list` | Prikazuje trenutne vrednosti konfiguracije |
| Konfiguracija | `foundry config set <key> <value>` | Ažurira konfiguraciju |

### Jednokratni obrazac za prompt

Umesto zastarele podkomande `model chat`, koristite:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ovo izvršava jedan ciklus upit/odgovor, a zatim izlazi.

### Uklonjene / izbegnute šeme

| Zastarelo / Nedokumentovano | Zamena / Preporuka |
|-----------------------------|--------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Koristite običan `foundry model list` + nedavne aktivnosti / logove |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Koristite Python skriptu za benchmark + OS alate (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking i telemetrija

- Latencija, p95, tokeni/sek: `samples/session03/benchmark_oss_models.py`
- Latencija prvog tokena (strimovanje): postavite `BENCH_STREAM=1`
- Korišćenje resursa: OS monitori (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Kako nove CLI telemetrijske komande postanu stabilne, mogu se lako integrisati u markdown datoteke sesija.

### Automatska provera sintakse

Automatski linter sprečava ponovno uvođenje zastarelih CLI šema unutar blokova koda u markdown datotekama:

Skripta: `Workshop/scripts/lint_markdown_cli.py`

Zastarele šeme su blokirane unutar kodnih blokova.

Preporučene zamene:
| Zastarelo | Zamena |
|-----------|--------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Skripta za benchmark + sistemski alati |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Pokrenite lokalno:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub akcija: `.github/workflows/markdown-cli-lint.yml` pokreće se pri svakom push-u i PR-u.

Opcioni pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Brza tabela za migraciju CLI → SDK

| Zadatak | CLI Jednolinijski | SDK (Python) Ekvivalent | Napomene |
|---------|--------------------|-------------------------|----------|
| Pokreni model jednom (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automatski pokreće servis i keširanje |
| Preuzmi (keširaj) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # pokreće preuzimanje/učitavanje` | Menadžer bira najbolju varijantu ako alias mapira na više verzija |
| Prikaži katalog | `foundry model list` | `# koristite menadžer za svaki alias ili održavajte poznatu listu` | CLI agregira; SDK trenutno po alias instanciranju |
| Prikaži keširane modele | `foundry cache list` | `manager.list_cached_models()` | Nakon inicijalizacije menadžera (bilo koji alias) |
| Omogući GPU akceleraciju | `foundry config set compute.onnx.enable_gpu true` | `# CLI akcija; SDK pretpostavlja da je konfiguracija već primenjena` | Konfiguracija je spoljni efekat |
| Dobij URL endpoint-a | (implicitno) | `manager.endpoint` | Koristi se za kreiranje OpenAI-kompatibilnog klijenta |
| Zagrej model | `foundry model run <alias>` zatim prvi prompt | `chat_once(alias, messages=[...])` (pomoćna funkcija) | Pomoćne funkcije rukovode početnom latencijom hladnog starta |
| Izmeri latenciju | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (ili nova skripta za izvoz) | Preporučuje se skripta za dosledne metrike |
| Zaustavi / ukloni model | `foundry model unload <alias>` | (Nije izloženo – ponovo pokrenite servis/proces) | Obično nije potrebno za tok radionice |
| Prikaži potrošnju tokena | (prikaz u izlazu) | `resp.usage.total_tokens` | Dostupno ako backend vraća objekat potrošnje |

## Izvoz benchmark markdown-a

Koristite skriptu `Workshop/scripts/export_benchmark_markdown.py` za pokretanje novog benchmarka (ista logika kao `samples/session03/benchmark_oss_models.py`) i generisanje Markdown tabele prilagođene za GitHub plus sirovog JSON-a.

### Primer

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generisane datoteke:
| Datoteka | Sadržaj |
|----------|---------|
| `benchmark_report.md` | Markdown tabela + saveti za interpretaciju |
| `benchmark_report.json` | Niz sirovih metrika (za praćenje razlika/trendova) |

Postavite `BENCH_STREAM=1` u okruženju da uključite latenciju prvog tokena ako je podržano.

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.