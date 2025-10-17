<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b994c57f1207012e4d7f58b7c0d1ae7",
  "translation_date": "2025-10-17T10:11:12+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "sr"
}
-->
# EdgeAI за почетнике - Radionica

> **Praktični vodič za izgradnju proizvodno spremnih Edge AI aplikacija**
>
> Savladajte lokalno postavljanje veštačke inteligencije uz Microsoft Foundry Local, od prve chat interakcije do orkestracije više agenata u 6 progresivnih sesija.

---

## 🎯 Uvod

Dobrodošli na **EdgeAI za početnike radionicu** - vaš praktični vodič za izgradnju inteligentnih aplikacija koje se u potpunosti pokreću na lokalnom hardveru. Ova radionica pretvara teorijske koncepte Edge AI u stvarne veštine kroz postepeno izazovne vežbe koristeći Microsoft Foundry Local i male jezičke modele (SLM).

### Zašto ova radionica?

**Revolucija Edge AI je počela**

Organizacije širom sveta prelaze sa AI zavisnog od oblaka na edge computing iz tri ključna razloga:

1. **Privatnost i usklađenost** - Obrada osetljivih podataka lokalno, bez prenosa u oblak (HIPAA, GDPR, finansijski propisi)
2. **Performanse** - Eliminacija mrežnog kašnjenja (50-500ms lokalno naspram 500-2000ms povratnog puta u oblaku)
3. **Kontrola troškova** - Uklanjanje troškova po tokenu API-ja i skaliranje bez troškova oblaka

**Ali Edge AI je drugačiji**

Pokretanje AI na lokalnim uređajima zahteva nove veštine:
- Izbor i optimizacija modela za ograničene resurse
- Upravljanje lokalnim servisima i ubrzanje hardvera
- Inženjering upita za manje modele
- Obrasci za proizvodno postavljanje na edge uređajima

**Ova radionica pruža te veštine**

U 6 fokusiranih sesija (~3 sata ukupno), napredovaćete od "Hello World" do postavljanja proizvodno spremnih sistema sa više agenata - sve lokalno na vašem računaru.

---

## 📚 Ciljevi učenja

Završetkom ove radionice, moći ćete:

### Osnovne kompetencije
1. **Postavljanje i upravljanje lokalnim AI servisima**
   - Instalacija i konfiguracija Microsoft Foundry Local
   - Izbor odgovarajućih modela za edge postavljanje
   - Upravljanje životnim ciklusom modela (preuzimanje, učitavanje, keširanje)
   - Praćenje korišćenja resursa i optimizacija performansi

2. **Izgradnja aplikacija sa AI podrškom**
   - Implementacija lokalnih chat interakcija kompatibilnih sa OpenAI
   - Dizajniranje efektivnih upita za male jezičke modele
   - Upravljanje strimovanjem odgovora za bolji korisnički doživljaj
   - Integracija lokalnih modela u postojeće aplikacije

3. **Kreiranje RAG (Retrieval Augmented Generation) sistema**
   - Izgradnja semantičke pretrage sa ugrađenim podacima
   - Utemeljenje odgovora LLM-a u specifičnom znanju domena
   - Evaluacija kvaliteta RAG-a koristeći industrijske standarde
   - Skaliranje od prototipa do proizvodnje

4. **Optimizacija performansi modela**
   - Benchmarking više modela za vaš slučaj upotrebe
   - Merenje kašnjenja, propusnosti i vremena prvog tokena
   - Izbor optimalnih modela na osnovu kompromisa brzine/kvaliteta
   - Poređenje SLM i LLM kompromisa u stvarnim scenarijima

5. **Orkestracija sistema sa više agenata**
   - Dizajniranje specijalizovanih agenata za različite zadatke
   - Implementacija memorije agenata i upravljanje kontekstom
   - Koordinacija agenata u složenim radnim tokovima
   - Pametno usmeravanje zahteva između više modela

6. **Postavljanje proizvodno spremnih rešenja**
   - Implementacija logike za rukovanje greškama i ponovnim pokušajima
   - Praćenje korišćenja tokena i sistemskih resursa
   - Izgradnja skalabilnih arhitektura sa obrascima modela-kao-alata
   - Planiranje migracionih puteva od edge do hibridnih (edge + oblak)

---

## 🎓 Ishodi učenja

### Šta ćete izgraditi

Do kraja ove radionice, kreiraćete:

| Sesija | Rezultat | Demonstrirane veštine |
|--------|----------|-----------------------|
| **1** | Chat aplikacija sa strimovanjem | Postavljanje servisa, osnovne interakcije, UX strimovanja |
| **2** | RAG sistem sa evaluacijom | Ugrađeni podaci, semantička pretraga, metrički kvalitet |
| **3** | Benchmarking više modela | Merenje performansi, poređenje modela |
| **4** | Poređenje SLM i LLM | Analiza kompromisa, strategije optimizacije |
| **5** | Orkestrator sa više agenata | Dizajn agenata, upravljanje memorijom, koordinacija |
| **6** | Sistem za inteligentno usmeravanje | Detekcija namere, izbor modela, skalabilnost |

### Matrica kompetencija

| Nivo veštine | Sesija 1-2 | Sesija 3-4 | Sesija 5-6 |
|--------------|------------|------------|------------|
| **Početnik** | ✅ Postavljanje i osnove | ⚠️ Izazovno | ❌ Previše napredno |
| **Srednji nivo** | ✅ Brzi pregled | ✅ Osnovno učenje | ⚠️ Ciljevi za napredak |
| **Napredni** | ✅ Lako prolazi | ✅ Usavršavanje | ✅ Obrasci za proizvodnju |

### Veštine spremne za karijeru

**Nakon ove radionice, bićete spremni da:**

✅ **Izgradite aplikacije sa prioritetom privatnosti**
- Zdravstvene aplikacije koje lokalno obrađuju PHI/PII
- Finansijske usluge sa zahtevima za usklađenost
- Vladini sistemi sa potrebama za suverenitetom podataka

✅ **Optimizujete za edge okruženja**
- IoT uređaji sa ograničenim resursima
- Mobilne aplikacije koje rade offline
- Sistemi u realnom vremenu sa niskim kašnjenjem

✅ **Dizajnirate inteligentne arhitekture**
- Sistemi sa više agenata za složene radne tokove
- Hibridna edge-cloud postavljanja
- AI infrastruktura optimizovana za troškove

✅ **Vodite Edge AI inicijative**
- Procena izvodljivosti Edge AI za projekte
- Izbor odgovarajućih modela i okvira
- Arhitektura skalabilnih lokalnih AI rešenja

---

## 🗺️ Struktura radionice

### Pregled sesija (6 sesija × 30 minuta = 3 sata)

| Sesija | Tema | Fokus | Trajanje |
|--------|------|-------|----------|
| **1** | Početak sa Foundry Local | Instalacija, validacija, prve interakcije | 30 min |
| **2** | Izgradnja AI rešenja sa RAG | Inženjering upita, ugrađeni podaci, evaluacija | 30 min |
| **3** | Open Source modeli | Otkrivanje modela, benchmarking, izbor | 30 min |
| **4** | Najnoviji modeli | SLM vs LLM, optimizacija, okviri | 30 min |
| **5** | Agenti sa AI podrškom | Dizajn agenata, orkestracija, memorija | 30 min |
| **6** | Modeli kao alati | Usmeravanje, povezivanje, strategije skaliranja | 30 min |

---

## 🚀 Brzi početak

### Preduslovi

**Sistemski zahtevi:**
- **OS**: Windows 10/11, macOS 11+, ili Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, preporučeno 16GB+
- **Skladište**: 10GB+ slobodnog prostora za modele
- **CPU**: Moderni procesor sa podrškom za AVX2
- **GPU** (opciono): CUDA-kompatibilan ili Qualcomm NPU za ubrzanje

**Softverski zahtevi:**
- **Python 3.8+** ([Preuzmi](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Vodič za instalaciju](../../../Workshop))
- **Git** ([Preuzmi](https://git-scm.com/downloads))
- **Visual Studio Code** (preporučeno) ([Preuzmi](https://code.visualstudio.com/))

### Postavljanje u 3 koraka

#### 1. Instalirajte Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Proverite instalaciju:**
```bash
foundry --version
foundry service status
```

**Uverite se da Azure AI Foundry Local radi sa fiksnim portom**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Proverite funkcionalnost:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Pronalaženje dostupnih modela**
Da biste videli koji modeli su dostupni u vašem Foundry Local instance, možete upitati endpoint modela:

```bash
# cmd/bash/powershell
foundry model list
```

Korišćenje web endpointa 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klonirajte repozitorijum i instalirajte zavisnosti

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

#### 3. Pokrenite svoj prvi primer

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Uspešno!** Trebalo bi da vidite strimovani odgovor o Edge AI.

---

## 📦 Resursi radionice

### Python primeri

Progresivni praktični primeri koji demonstriraju svaki koncept:

| Sesija | Primer | Opis | Vreme izvršavanja |
|--------|--------|------|-------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Osnovni & strimovani chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG sa ugrađenim podacima | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluacija kvaliteta RAG-a | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking više modela | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Poređenje SLM i LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistem sa više agenata | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Usmeravanje na osnovu namere | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Višestepena pipeline | ~60s |

### Jupyter beležnice

Interaktivno istraživanje sa objašnjenjima i vizualizacijama:

| Sesija | Beležnica | Opis | Težina |
|--------|-----------|------|--------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Osnove chata & strimovanje | ⭐ Početnik |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Izgradnja RAG sistema | ⭐⭐ Srednji nivo |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluacija kvaliteta RAG-a | ⭐⭐ Srednji nivo |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modela | ⭐⭐ Srednji nivo |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Poređenje modela | ⭐⭐ Srednji nivo |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orkestracija agenata | ⭐⭐⭐ Napredno |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Usmeravanje na osnovu namere | ⭐⭐⭐ Napredno |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orkestracija pipeline-a | ⭐⭐⭐ Napredno |

### Dokumentacija

Sveobuhvatni vodiči i reference:

| Dokument | Opis | Koristite kada |
|----------|------|----------------|
| [QUICK_START.md](./QUICK_START.md) | Vodič za brzo postavljanje | Početak od nule |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Komande & API vodič | Potrebni brzi odgovori |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK obrasci & primeri | Pisanje koda |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Vodič za konfiguraciju okruženja | Konfigurisanje primera |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Najnovija poboljšanja primera | Razumevanje promena |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Vodič za migraciju | Ažuriranje koda |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Uobičajeni problemi & rešenja | Otklanjanje problema |

---

## 🎓 Preporuke za put učenja

### Za početnike (3-4 sata)
1. ✅ Sesija 1: Početak (fokus na postavljanje i osnovni chat)
2. ✅ Sesija 2: Osnove RAG-a (preskočite evaluaciju za početak)
3. ✅ Sesija 3: Jednostavno benchmarking (samo 2 modela)
4. ⏭️ Preskočite sesije 4-6 za sada
5. 🔄 Vratite se na sesije 4-6 nakon izgradnje prve aplikacije

### Za programere srednjeg nivoa (3 sata)
1. ⚡ Sesija 1: Brza validacija postavljanja
2. ✅ Sesija 2: Kompletan RAG pipeline sa evaluacijom
3. ✅ Sesija 3: Kompletan benchmarking suite
4. ✅ Sesija 4: Optimizacija modela
5. ✅ Sesije 5-6: Fokus na arhitekturne obrasce

### Za napredne praktičare (2-3 sata)
1. ⚡ Sesije 1-3: Brzi pregled i validacija
2. ✅ Sesija 4: Dubinska optimizacija
3. ✅ Sesija 5: Arhitektura sa više agenata
4. ✅ Sesija 6: Obrasci za proizvodnju i skaliranje
5. 🚀 Proširenje: Izgradnja prilagođene logike usmeravanja i hibridnih postavljanja

---

## Paket sesija radionice (Fokusirane laboratorije od 30 minuta)

Ako pratite sažeti format radionice od 6 sesija, koristite ove posvećene vodiče (svaki se mapira i dopunjuje šire module dokumentacije iznad):

| Sesija radionice | Vodič | Glavni fokus |
|------------------|-------|-------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalacija, validacija, pokretanje phi & GPT-OSS-20B, ubrzanje |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Inženjering upita, RAG obrasci, CSV & dokumenti, migracija |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integracija Hugging Face, benchmarking, izbor modela |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM naspram LLM, WebGPU, Chainlit RAG, ONNX ubrzanje |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Uloge agenata, memorija, alati, orkestracija |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Usmeravanje, povezivanje, skaliranje na Azure |

Svaka datoteka sesije uključuje: apstrakt, ciljeve učenja, 30-minutni demo tok, početni projekat, kontrolnu listu za validaciju, rešavanje problema i reference na zvanični Foundry Local Python SDK.

### Primer skripti

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

Ako pokrećete Foundry Local servis na drugom (Windows) računaru ili VM sa macOS-a, izvezite endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesija | Skripta(e) | Opis |
|--------|------------|------|
| 1 | `samples/session01/chat_bootstrap.py` | Pokretanje servisa i streaming četa |
| 2 | `samples/session02/rag_pipeline.py` | Minimalni RAG (ugrađeni podaci u memoriji) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluacija RAG-a sa metrikama ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latencije i propusnosti za više modela |
| 4 | `samples/session04/model_compare.py` | Poređenje SLM i LLM (latencija i uzorci izlaza) |
| 5 | `samples/session05/agents_orchestrator.py` | Istraživački → urednički pipeline sa dva agenta |
| 6 | `samples/session06/models_router.py` | Demo usmeravanja zasnovanog na nameri |
|   | `samples/session06/models_pipeline.py` | Višestepeni lanac planiranja/izvršavanja/rafiniranja |

### Promenljive okruženja (zajedničke za sve primere)

| Promenljiva | Svrha | Primer |
|-------------|-------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Podrazumevani alias za jedan model za osnovne primere | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Eksplicitni SLM naspram većeg modela za poređenje | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Lista aliasa za benchmarking odvojena zarezima | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Broj ponavljanja benchmarka po modelu | `3` |
| `BENCH_PROMPT` | Prompt korišćen u benchmarkingu | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model za ugrađivanje rečenica-transformera | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Prepisivanje testnog upita za RAG pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Prepisivanje upita za pipeline agenata | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias modela za istraživačkog agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modela za uredničkog agenta (može se razlikovati) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kada je `1`, štampa potrošnju tokena po završetku | `1` |
| `RETRY_ON_FAIL` | Kada je `1`, ponovo pokušava jednom u slučaju grešaka u četu | `1` |
| `RETRY_BACKOFF` | Sekunde čekanja pre ponovnog pokušaja | `1.0` |

Ako promenljiva nije postavljena, skripte se oslanjaju na razumne podrazumevane vrednosti. Za demonstracije sa jednim modelom obično je potrebna samo `FOUNDRY_LOCAL_ALIAS`.

### Modul za pomoć

Svi primeri sada dele pomoćni `samples/workshop_utils.py` koji pruža:

* Keširani `FoundryLocalManager` + kreiranje OpenAI klijenta
* Pomoćnu funkciju `chat_once()` sa opcionalnim ponovnim pokušajem + štampanjem potrošnje
* Jednostavno izveštavanje o potrošnji tokena (omogućite preko `SHOW_USAGE=1`)

Ovo smanjuje duplikaciju i ističe najbolje prakse za efikasnu lokalnu orkestraciju modela.

## Opcionalna poboljšanja (među sesijama)

| Tema | Poboljšanje | Sesije | Okruženje / Prekidač |
|------|-------------|--------|----------------------|
| Determinizam | Fiksirana temperatura + stabilni setovi promptova | 1–6 | Postavite `temperature=0`, `top_p=1` |
| Vidljivost potrošnje tokena | Dosledno podučavanje o troškovima/efikasnosti | 1–6 | `SHOW_USAGE=1` |
| Streaming prvog tokena | Metrička latencija percepcije | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Otpornost na greške | Rukovanje prolaznim greškama pri hladnom startu | Sve | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-model agenti | Specijalizacija heterogenih uloga | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptivno usmeravanje | Namera + heuristika troškova | 6 | Proširite usmerivač logikom eskalacije |
| Vektorska memorija | Dugoročno semantičko pamćenje | 2,5,6 | Integracija FAISS/Chroma indeksa ugrađivanja |
| Izvoz tragova | Revizija i evaluacija | 2,5,6 | Dodavanje JSON linija po koraku |
| Kvalitativni kriterijumi | Praćenje kvaliteta | 3–6 | Sekundarni promptovi za ocenjivanje |
| Testovi validacije | Brza validacija pre radionice | Sve | `python Workshop/tests/smoke.py` |

### Deterministički brzi početak

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Očekujte stabilan broj tokena kroz ponovljene identične ulaze.

### Evaluacija RAG-a (Sesija 2)

Koristite `rag_eval_ragas.py` za izračunavanje relevantnosti odgovora, verodostojnosti i preciznosti konteksta na malom sintetičkom datasetu:

```powershell
python samples/session02/rag_eval_ragas.py
```

Proširite dodavanjem većeg JSONL-a sa pitanjima, kontekstima i istinitim podacima, zatim konvertovanjem u Hugging Face `Dataset`.

## Dodatak tačnosti CLI komandi

Radionica namerno koristi samo trenutno dokumentovane/stabilne Foundry Local CLI komande.

### Referencirane stabilne komande

| Kategorija | Komanda | Svrha |
|------------|---------|-------|
| Osnovno | `foundry --version` | Prikazuje instaliranu verziju |
| Osnovno | `foundry init` | Inicijalizuje konfiguraciju |
| Servis | `foundry service start` | Pokreće lokalni servis (ako nije automatski) |
| Servis | `foundry status` | Prikazuje status servisa |
| Modeli | `foundry model list` | Lista katalog/dostupne modele |
| Modeli | `foundry model download <alias>` | Preuzima težine modela u keš |
| Modeli | `foundry model run <alias>` | Pokreće (učitava) model lokalno; kombinujte sa `--prompt` za jednokratni |
| Modeli | `foundry model unload <alias>` / `foundry model stop <alias>` | Uklanja model iz memorije (ako je podržano) |
| Keš | `foundry cache list` | Lista keširanih (preuzetih) modela |
| Sistem | `foundry system info` | Snimak hardverskih i akceleracionih mogućnosti |
| Sistem | `foundry system gpu-info` | Dijagnostičke informacije o GPU-u |
| Konfiguracija | `foundry config list` | Prikazuje trenutne vrednosti konfiguracije |
| Konfiguracija | `foundry config set <key> <value>` | Ažurira konfiguraciju |

### Jednokratni prompt obrazac

Umesto zastarele `model chat` podkomande, koristite:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ovo izvršava jedan ciklus prompt/odgovor, zatim izlazi.

### Uklonjeni / izbegnuti obrasci

| Zastarelo / Nedokumentovano | Zamena / Preporuka |
|-----------------------------|--------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Koristite običan `foundry model list` + nedavne aktivnosti / logove |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Koristite Python skriptu za benchmarking + OS alate (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking i telemetrija

- Latencija, p95, tokeni/sec: `samples/session03/benchmark_oss_models.py`
- Latencija prvog tokena (streaming): postavite `BENCH_STREAM=1`
- Korišćenje resursa: OS monitori (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Kako nove CLI telemetrijske komande postanu stabilne, mogu se lako integrisati u markdown datoteke sesija.

### Automatska provera sintakse

Automatski linter sprečava ponovno uvođenje zastarelih CLI obrazaca unutar blokova koda u markdown datotekama:

Skripta: `Workshop/scripts/lint_markdown_cli.py`

Zastareli obrasci su blokirani unutar kodnih blokova.

Preporučene zamene:
| Zastarelo | Zamena |
|-----------|--------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Skripta za benchmarking + sistemski alati |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Pokrenite lokalno:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub akcija: `.github/workflows/markdown-cli-lint.yml` se pokreće pri svakom push-u i PR-u.

Opcionalni pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Brza migraciona tabela CLI → SDK

| Zadatak | CLI Jednolinijski | SDK (Python) Ekvivalent | Napomene |
|---------|--------------------|-------------------------|----------|
| Pokreni model jednom (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automatski pokreće servis i keširanje |
| Preuzmi (keširaj) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # pokreće preuzimanje/učitavanje` | Manager bira najbolju varijantu ako alias mapira na više verzija |
| Lista kataloga | `foundry model list` | `# koristite manager za svaki alias ili održavajte poznatu listu` | CLI agregira; SDK trenutno po alias instanciranju |
| Lista keširanih modela | `foundry cache list` | `manager.list_cached_models()` | Nakon inicijalizacije managera (bilo koji alias) |
| Omogući GPU ubrzanje | `foundry config set compute.onnx.enable_gpu true` | `# CLI akcija; SDK pretpostavlja da je konfiguracija već primenjena` | Konfiguracija je eksterni efekat |
| Dobij URL endpointa | (implicitno) | `manager.endpoint` | Koristi se za kreiranje OpenAI-kompatibilnog klijenta |
| Zagrej model | `foundry model run <alias>` zatim prvi prompt | `chat_once(alias, messages=[...])` (pomoćna funkcija) | Pomoćne funkcije rukovode početnom latencijom hladnog starta |
| Izmeri latenciju | `python benchmark_oss_models.py` | `import benchmark_oss_models` (ili nova skripta za izvoz) | Preferirajte skriptu za dosledne metrike |
| Zaustavi / ukloni model | `foundry model unload <alias>` | (Nije izloženo – ponovo pokrenite servis/proces) | Obično nije potrebno za tok radionice |
| Prikupi potrošnju tokena | (pogledajte izlaz) | `resp.usage.total_tokens` | Dostupno ako backend vraća objekat potrošnje |

## Izvoz benchmarka u Markdown

Koristite skriptu `Workshop/scripts/export_benchmark_markdown.py` za pokretanje svežeg benchmarka (ista logika kao `samples/session03/benchmark_oss_models.py`) i emitovanje GitHub-prijateljske Markdown tabele plus sirovog JSON-a.

### Primer

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generisane datoteke:
| Datoteka | Sadržaj |
|----------|---------|
| `benchmark_report.md` | Markdown tabela + saveti za interpretaciju |
| `benchmark_report.json` | Sirovi niz metrika (za praćenje razlika/trendova) |

Postavite `BENCH_STREAM=1` u okruženju da uključite latenciju prvog tokena ako je podržano.

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.