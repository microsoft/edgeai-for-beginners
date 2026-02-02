# EdgeAI za početnike - Radionica

> **Praktični put učenja za izgradnju Edge AI aplikacija spremnih za produkciju**
>
> Savladajte lokalno postavljanje AI-a uz Microsoft Foundry Local, od prve chat interakcije do orkestracije više agenata u 6 progresivnih sesija.

---

## 🎯 Uvod

Dobrodošli na **EdgeAI za početnike radionicu** - vaš praktični vodič za izgradnju inteligentnih aplikacija koje u potpunosti rade na lokalnom hardveru. Ova radionica pretvara teorijske koncepte Edge AI-a u stvarne vještine kroz progresivno izazovne vježbe koristeći Microsoft Foundry Local i male jezične modele (SLM).

### Zašto ova radionica?

**Revolucija Edge AI-a je ovdje**

Organizacije diljem svijeta prelaze s AI-a ovisnog o oblaku na edge računalstvo iz tri ključna razloga:

1. **Privatnost i usklađenost** - Obrada osjetljivih podataka lokalno bez prijenosa u oblak (HIPAA, GDPR, financijski propisi)
2. **Performanse** - Eliminacija mrežne latencije (50-500ms lokalno naspram 500-2000ms oblaka)
3. **Kontrola troškova** - Uklanjanje troškova po tokenu za API i skaliranje bez troškova oblaka

**Ali Edge AI je drugačiji**

Pokretanje AI-a na lokalnim uređajima zahtijeva nove vještine:
- Odabir i optimizacija modela za ograničene resurse
- Upravljanje lokalnim uslugama i hardverska akceleracija
- Inženjering upita za manje modele
- Obrasci implementacije za uređaje na rubu mreže

**Ova radionica pruža te vještine**

U 6 fokusiranih sesija (~3 sata ukupno), napredovat ćete od "Hello World" do implementacije sustava s više agenata spremnih za produkciju - sve lokalno na vašem računalu.

---

## 📚 Ciljevi učenja

Završetkom ove radionice, moći ćete:

### Osnovne kompetencije
1. **Postaviti i upravljati lokalnim AI uslugama**
   - Instalirati i konfigurirati Microsoft Foundry Local
   - Odabrati odgovarajuće modele za edge implementaciju
   - Upravljati životnim ciklusom modela (preuzimanje, učitavanje, keširanje)
   - Pratiti korištenje resursa i optimizirati performanse

2. **Izgraditi AI-pokretane aplikacije**
   - Implementirati lokalne OpenAI-kompatibilne chat interakcije
   - Dizajnirati učinkovite upite za male jezične modele
   - Upravljati streaming odgovorima za bolji korisnički doživljaj
   - Integrirati lokalne modele u postojeće aplikacije

3. **Kreirati RAG (Retrieval Augmented Generation) sustave**
   - Izgraditi semantičko pretraživanje pomoću ugrađivanja
   - Temeljiti odgovore LLM-a na specifičnom znanju domene
   - Procijeniti kvalitetu RAG-a koristeći industrijske standarde
   - Skalirati od prototipa do produkcije

4. **Optimizirati performanse modela**
   - Testirati više modela za vašu upotrebu
   - Mjeriti latenciju, propusnost i vrijeme prvog tokena
   - Odabrati optimalne modele na temelju kompromisa brzine/kvalitete
   - Usporediti SLM i LLM u stvarnim scenarijima

5. **Orkestrirati sustave s više agenata**
   - Dizajnirati specijalizirane agente za različite zadatke
   - Implementirati memoriju i upravljanje kontekstom agenata
   - Koordinirati agente u složenim radnim tokovima
   - Inteligentno usmjeravati zahtjeve između više modela

6. **Implementirati rješenja spremna za produkciju**
   - Implementirati rukovanje greškama i logiku ponovnog pokušaja
   - Pratiti korištenje tokena i sistemske resurse
   - Izgraditi skalabilne arhitekture s obrascima modela-kao-alata
   - Planirati migracijske putove od edge-a do hibridnih (edge + oblak)

---

## 🎓 Ishodi učenja

### Što ćete izgraditi

Do kraja ove radionice, izradit ćete:

| Sesija | Rezultat | Demonstrirane vještine |
|--------|----------|-------------------------|
| **1** | Chat aplikacija sa streamingom | Postavljanje usluge, osnovne interakcije, streaming UX |
| **2** | RAG sustav s evaluacijom | Ugrađivanja, semantičko pretraživanje, metričke kvalitete |
| **3** | Suite za usporedbu više modela | Mjerenje performansi, usporedba modela |
| **4** | Usporednik SLM vs LLM | Analiza kompromisa, strategije optimizacije |
| **5** | Orkestrator s više agenata | Dizajn agenata, upravljanje memorijom, koordinacija |
| **6** | Inteligentni sustav usmjeravanja | Detekcija namjere, odabir modela, skalabilnost |

### Matrica kompetencija

| Razina vještine | Sesija 1-2 | Sesija 3-4 | Sesija 5-6 |
|-----------------|------------|------------|------------|
| **Početnik** | ✅ Postavljanje i osnove | ⚠️ Izazovno | ❌ Previše napredno |
| **Srednji** | ✅ Brzi pregled | ✅ Ključno učenje | ⚠️ Ciljevi za napredak |
| **Napredni** | ✅ Lako prolazi | ✅ Usavršavanje | ✅ Obrasci za produkciju |

### Vještine spremne za karijeru

**Nakon ove radionice, bit ćete spremni za:**

✅ **Izgradnju aplikacija s prioritetom privatnosti**
- Zdravstvene aplikacije koje lokalno obrađuju PHI/PII
- Financijske usluge s zahtjevima za usklađenost
- Vladine sustave s potrebama za suverenitetom podataka

✅ **Optimizaciju za edge okruženja**
- IoT uređaje s ograničenim resursima
- Mobilne aplikacije koje rade offline
- Sustave u stvarnom vremenu s niskom latencijom

✅ **Dizajn inteligentnih arhitektura**
- Sustave s više agenata za složene radne tokove
- Hibridne edge-cloud implementacije
- Troškovno optimiziranu AI infrastrukturu

✅ **Vođenje Edge AI inicijativa**
- Procjenu izvedivosti Edge AI-a za projekte
- Odabir odgovarajućih modela i okvira
- Arhitekturu skalabilnih lokalnih AI rješenja

---

## 🗺️ Struktura radionice

### Pregled sesija (6 sesija × 30 minuta = 3 sata)

| Sesija | Tema | Fokus | Trajanje |
|--------|------|-------|----------|
| **1** | Početak s Foundry Local | Instalacija, validacija, prve interakcije | 30 min |
| **2** | Izgradnja AI rješenja s RAG | Inženjering upita, ugrađivanja, evaluacija | 30 min |
| **3** | Open Source modeli | Otkrivanje modela, benchmarking, odabir | 30 min |
| **4** | Najnoviji modeli | SLM vs LLM, optimizacija, okviri | 30 min |
| **5** | AI-pokretani agenti | Dizajn agenata, orkestracija, memorija | 30 min |
| **6** | Modeli kao alati | Usmjeravanje, povezivanje, strategije skaliranja | 30 min |

---

## 🚀 Brzi početak

### Preduvjeti

**Sistemski zahtjevi:**
- **OS**: Windows 10/11, macOS 11+ ili Linux (Ubuntu 20.04+)
- **RAM**: Minimalno 8GB, preporučeno 16GB+
- **Pohrana**: 10GB+ slobodnog prostora za modele
- **CPU**: Moderni procesor s podrškom za AVX2
- **GPU** (opcionalno): CUDA-kompatibilan ili Qualcomm NPU za akceleraciju

**Softverski zahtjevi:**
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

**Provjerite instalaciju:**
```bash
foundry --version
foundry service status
```

**Osigurajte da Azure AI Foundry Local radi s fiksnim portom**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Provjerite funkcionalnost:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Pronalaženje dostupnih modela**
Za pregled dostupnih modela u vašoj Foundry Local instanci, možete upitati endpoint modela:

```bash
# cmd/bash/powershell
foundry model list
```

Korištenje web endpointa 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klonirajte repozitorij i instalirajte ovisnosti

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

#### 3. Pokrenite svoj prvi primjer

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Uspjeh!** Trebali biste vidjeti streaming odgovor o edge AI-u.

---

## 📦 Resursi radionice

### Python primjeri

Progresivni praktični primjeri koji demonstriraju svaki koncept:

| Sesija | Primjer | Opis | Vrijeme izvođenja |
|--------|---------|------|-------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Osnovni i streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG s ugrađivanjima | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluacija kvalitete RAG-a | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking više modela | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Usporedba SLM i LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sustav s više agenata | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Usmjeravanje temeljeno na namjeri | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Višestepena pipeline | ~60s |

### Jupyter bilježnice

Interaktivno istraživanje s objašnjenjima i vizualizacijama:

| Sesija | Bilježnica | Opis | Težina |
|--------|------------|------|--------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Osnove chata i streaming | ⭐ Početnik |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Izgradnja RAG sustava | ⭐⭐ Srednji |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluacija kvalitete RAG-a | ⭐⭐ Srednji |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modela | ⭐⭐ Srednji |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Usporedba modela | ⭐⭐ Srednji |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orkestracija agenata | ⭐⭐⭐ Napredno |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Usmjeravanje namjera | ⭐⭐⭐ Napredno |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orkestracija pipeline-a | ⭐⭐⭐ Napredno |

### Dokumentacija

Sveobuhvatni vodiči i reference:

| Dokument | Opis | Kada koristiti |
|----------|------|----------------|
| [QUICK_START.md](./QUICK_START.md) | Vodič za brzo postavljanje | Početak od nule |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Brzi pregled naredbi i API-ja | Trebate brze odgovore |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Obrasci i primjeri SDK-a | Pisanje koda |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Vodič za varijable okruženja | Konfiguracija primjera |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Uobičajeni problemi i rješenja | Rješavanje problema |

---

## 🎓 Preporuke za put učenja

### Za početnike (3-4 sata)
1. ✅ Sesija 1: Početak (fokus na postavljanje i osnovni chat)
2. ✅ Sesija 2: Osnove RAG-a (preskočite evaluaciju za početak)
3. ✅ Sesija 3: Jednostavno benchmarking (samo 2 modela)
4. ⏭️ Preskočite sesije 4-6 za sada
5. 🔄 Vratite se na sesije 4-6 nakon izrade prve aplikacije

### Za srednje razvijene programere (3 sata)
1. ⚡ Sesija 1: Brza validacija postavljanja
2. ✅ Sesija 2: Kompletan RAG pipeline s evaluacijom
3. ✅ Sesija 3: Cijeli benchmarking suite
4. ✅ Sesija 4: Optimizacija modela
5. ✅ Sesije 5-6: Fokus na arhitekturne obrasce

### Za napredne praktičare (2-3 sata)
1. ⚡ Sesije 1-3: Brzi pregled i validacija
2. ✅ Sesija 4: Dubinska optimizacija
3. ✅ Sesija 5: Arhitektura s više agenata
4. ✅ Sesija 6: Obrasci za produkciju i skaliranje
5. 🚀 Proširite: Izradite prilagođenu logiku usmjeravanja i hibridne implementacije

---

## Paket sesija radionice (Fokusirani 30-minutni laboratoriji)

Ako pratite sažeti format radionice od 6 sesija, koristite ove posvećene vodiče (svaki se povezuje i nadopunjuje šire module dokumentacije iznad):

| Sesija radionice | Vodič | Glavni fokus |
|------------------|-------|--------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalacija, validacija, pokretanje phi & GPT-OSS-20B, akceleracija |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Inženjering upita, RAG obrasci, utemeljenje na CSV i dokumentima, migracija |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integracija s Hugging Face, benchmarking, odabir modela |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX akceleracija |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Uloge agenata, memorija, alati, orkestracija |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Usmjeravanje, povezivanje, skaliranje prema Azureu |

Svaka datoteka sesije uključuje: sažetak, ciljeve učenja, tijek demonstracije od 30 minuta, početni projekt, kontrolni popis za validaciju, rješavanje problema i reference na službeni Foundry Local Python SDK.

### Primjeri skripti

Instalacija ovisnosti za radionicu (Windows):

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

Ako pokrećete Foundry Local uslugu na drugom (Windows) računalu ili VM-u s macOS-a, izvezite krajnju točku:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesija | Skripta(e) | Opis |
|--------|------------|------|
| 1 | `samples/session01/chat_bootstrap.py` | Pokretanje usluge i streaming razgovora |
| 2 | `samples/session02/rag_pipeline.py` | Minimalni RAG (ugrađeni podaci u memoriji) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluacija RAG-a s metrikama ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking latencije i propusnosti za više modela |
| 4 | `samples/session04/model_compare.py` | Usporedba SLM-a i LLM-a (latencija i uzorci rezultata) |
| 5 | `samples/session05/agents_orchestrator.py` | Istraživački → urednički proces s dva agenta |
| 6 | `samples/session06/models_router.py` | Demonstracija usmjeravanja na temelju namjere |
|   | `samples/session06/models_pipeline.py` | Višekorak lanac planiranja/izvršavanja/poboljšanja |

### Varijable okruženja (zajedničke za sve primjere)

| Varijabla | Svrha | Primjer |
|-----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Zadani alias za jedan model za osnovne primjere | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Eksplicitni SLM naspram većeg modela za usporedbu | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Popis aliasa za benchmarking odvojen zarezima | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Broj ponavljanja benchmarka po modelu | `3` |
| `BENCH_PROMPT` | Prompt korišten u benchmarkingu | `Objasnite ukratko što je retrieval augmented generation.` |
| `EMBED_MODEL` | Model za ugrađivanje rečenica | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Zamjena testnog upita za RAG pipeline | `Zašto koristiti RAG s lokalnom inferencom?` |
| `AGENT_QUESTION` | Zamjena upita za pipeline agenata | `Objasnite zašto je edge AI važan za usklađenost.` |
| `AGENT_MODEL_PRIMARY` | Alias modela za istraživačkog agenta | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modela za uredničkog agenta (može se razlikovati) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kada je `1`, ispisuje korištenje tokena po završetku | `1` |
| `RETRY_ON_FAIL` | Kada je `1`, ponovno pokušava jednom kod privremenih grešaka u razgovoru | `1` |
| `RETRY_BACKOFF` | Sekunde čekanja prije ponovnog pokušaja | `1.0` |

Ako varijabla nije postavljena, skripte se vraćaju na razumne zadane vrijednosti. Za demonstracije s jednim modelom obično je potrebna samo `FOUNDRY_LOCAL_ALIAS`.

### Pomoćni modul

Svi primjeri sada dijele pomoćnu datoteku `samples/workshop_utils.py` koja omogućuje:

* Stvaranje keširanog `FoundryLocalManager` + OpenAI klijenta
* Pomoćnu funkciju `chat_once()` s opcionalnim ponovnim pokušajem + ispisom korištenja
* Jednostavno izvješćivanje o korištenju tokena (omogućeno putem `SHOW_USAGE=1`)

Ovo smanjuje dupliciranje i ističe najbolje prakse za učinkovitu lokalnu orkestraciju modela.

## Opcionalna poboljšanja (kroz sesije)

| Tema | Poboljšanje | Sesije | Okruženje / Prekidač |
|------|-------------|--------|----------------------|
| Determinizam | Fiksna temperatura + stabilni setovi promptova | 1–6 | Postavite `temperature=0`, `top_p=1` |
| Vidljivost korištenja tokena | Dosljedno podučavanje o troškovima/učinkovitosti | 1–6 | `SHOW_USAGE=1` |
| Streaming prvog tokena | Metrika percipirane latencije | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Otpornost na ponovni pokušaj | Rješava privremeni hladni start | Sve | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Više-modelski agenti | Heterogena specijalizacija uloga | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptivno usmjeravanje | Namjera + heuristika troškova | 6 | Proširite router s logikom eskalacije |
| Vektorska memorija | Dugoročno semantičko pamćenje | 2,5,6 | Integrirajte FAISS/Chroma indeks ugrađivanja |
| Izvoz tragova | Revizija i evaluacija | 2,5,6 | Dodajte JSON linije po koraku |
| Kvalitativni kriteriji | Praćenje kvalitete | 3–6 | Sekundarni promptovi za ocjenjivanje |
| Testovi provjere | Brza validacija prije radionice | Sve | `python Workshop/tests/smoke.py` |

### Deterministički brzi početak

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Očekujte stabilan broj tokena kroz ponovljene identične ulaze.

### Evaluacija RAG-a (Sesija 2)

Koristite `rag_eval_ragas.py` za izračun relevantnosti odgovora, vjerodostojnosti i preciznosti konteksta na malom sintetičkom skupu podataka:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Proširite dodavanjem većeg JSONL-a s pitanjima, kontekstima i istinitim podacima, a zatim ga pretvorite u Hugging Face `Dataset`.

## Dodatak za točnost CLI naredbi

Radionica namjerno koristi samo trenutno dokumentirane / stabilne Foundry Local CLI naredbe.

### Referencirane stabilne naredbe

| Kategorija | Naredba | Svrha |
|------------|---------|-------|
| Osnovno | `foundry --version` | Prikazuje instaliranu verziju |
| Usluga | `foundry service start` | Pokreće lokalnu uslugu (ako nije automatski) |
| Usluga | `foundry service status` | Prikazuje status usluge |
| Modeli | `foundry model list` | Popis kataloga / dostupnih modela |
| Modeli | `foundry model download <alias>` | Preuzima težine modela u keš |
| Modeli | `foundry model run <alias>` | Pokreće (učitava) model lokalno; kombinirajte s `--prompt` za jednokratni upit |
| Modeli | `foundry model unload <alias>` / `foundry model stop <alias>` | Isključuje model iz memorije (ako je podržano) |
| Keš | `foundry cache list` | Popis keširanih (preuzetih) modela |

### Jednokratni uzorak prompta

Umjesto zastarjele podnaredbe `model chat`, koristite:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Ovo izvršava jedan ciklus upita/odgovora, a zatim izlazi.

### Uklonjeni / izbjegnuti uzorci

| Zastarjelo / Nedokumentirano | Zamjena / Smjernice |
|------------------------------|---------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Koristite obični `foundry model list` + nedavne aktivnosti / logove |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Koristite Python skriptu za benchmark + OS alate (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking i telemetrija

- Latencija, p95, tokeni/sec: `samples/session03/benchmark_oss_models.py`
- Latencija prvog tokena (streaming): postavite `BENCH_STREAM=1`
- Korištenje resursa: OS monitori (Task Manager, Activity Monitor, `nvidia-smi`).

Kako nove CLI telemetrijske naredbe postanu stabilne, mogu se integrirati s minimalnim izmjenama sesijskih markdown datoteka.

### Automatska provjera sintakse

Automatski linter sprječava ponovno uvođenje zastarjelih CLI uzoraka unutar blokova koda u markdown datotekama:

Skripta: `Workshop/scripts/lint_markdown_cli.py`

Zastarjeli uzorci blokirani su unutar blokova koda.

Preporučene zamjene:
| Zastarjelo | Zamjena |
|------------|---------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Skripta za benchmark + alati sustava |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Pokrenite lokalno:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` pokreće se na svakom pushu i PR-u.

Opcionalni pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Brza tablica migracije CLI → SDK

| Zadatak | CLI Jednolinijska naredba | SDK (Python) Ekvivalent | Napomene |
|---------|---------------------------|-------------------------|----------|
| Pokreni model jednom (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automatski pokreće uslugu i keširanje |
| Preuzmi (keširaj) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # pokreće preuzimanje/učitavanje` | Manager bira najbolju varijantu ako alias mapira na više verzija |
| Popis kataloga | `foundry model list` | `# koristite manager za svaki alias ili održavajte poznati popis` | CLI agregira; SDK trenutno po aliasu |
| Popis keširanih modela | `foundry cache list` | `manager.list_cached_models()` | Nakon inicijalizacije managera (bilo koji alias) |
| Dohvati URL krajnje točke | (implicitno) | `manager.endpoint` | Koristi se za stvaranje OpenAI-kompatibilnog klijenta |
| Zagrij model | `foundry model run <alias>` zatim prvi prompt | `chat_once(alias, messages=[...])` (pomoćna funkcija) | Pomoćne funkcije rješavaju početnu latenciju hladnog starta |
| Mjeri latenciju | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (ili nova skripta za izvoz) | Preferirajte skriptu za dosljedne metrike |
| Zaustavi / isključi model | `foundry model unload <alias>` | (Nije izloženo – ponovno pokrenite uslugu / proces) | Obično nije potrebno za tijek radionice |
| Dohvati korištenje tokena | (pogledajte izlaz) | `resp.usage.total_tokens` | Dostupno ako backend vraća objekt korištenja |

## Izvoz benchmarka u Markdown

Koristite skriptu `Workshop/scripts/export_benchmark_markdown.py` za pokretanje svježeg benchmarka (ista logika kao `samples/session03/benchmark_oss_models.py`) i generiranje GitHub-prijateljske Markdown tablice plus sirovog JSON-a.

### Primjer

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Generirane datoteke:
| Datoteka | Sadržaj |
|----------|---------|
| `benchmark_report.md` | Markdown tablica + interpretacijski savjeti |
| `benchmark_report.json` | Sirovi niz metrika (za usporedbu / praćenje trendova) |

Postavite `BENCH_STREAM=1` u okruženju za uključivanje latencije prvog tokena ako je podržano.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->