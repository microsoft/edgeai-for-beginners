<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b994c57f1207012e4d7f58b7c0d1ae7",
  "translation_date": "2025-10-17T10:07:18+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "ro"
}
-->
# EdgeAI pentru Începători - Atelier

> **Cale de învățare practică pentru construirea aplicațiilor Edge AI gata de producție**
>
> Stăpânește implementarea AI locală cu Microsoft Foundry Local, de la prima completare de chat la orchestrarea multi-agent în 6 sesiuni progresive.

---

## 🎯 Introducere

Bine ai venit la **Atelierul EdgeAI pentru Începători** - ghidul tău practic pentru construirea aplicațiilor inteligente care rulează complet pe hardware local. Acest atelier transformă conceptele teoretice ale Edge AI în abilități reale prin exerciții progresiv provocatoare utilizând Microsoft Foundry Local și Small Language Models (SLMs).

### De ce acest atelier?

**Revoluția Edge AI este aici**

Organizațiile din întreaga lume trec de la AI dependent de cloud la calculul edge din trei motive critice:

1. **Confidențialitate & Conformitate** - Procesează date sensibile local, fără transmitere în cloud (HIPAA, GDPR, reglementări financiare)
2. **Performanță** - Elimină latența rețelei (50-500ms local vs 500-2000ms tur-retur în cloud)
3. **Controlul Costurilor** - Elimină costurile API per-token și scalează fără cheltuieli de cloud

**Dar Edge AI este diferit**

Rularea AI on-premises necesită abilități noi:
- Selectarea și optimizarea modelelor pentru constrângeri de resurse
- Managementul serviciilor locale și accelerarea hardware
- Ingineria prompturilor pentru modele mai mici
- Modele de implementare pentru dispozitive edge

**Acest atelier oferă aceste abilități**

În 6 sesiuni concentrate (~3 ore în total), vei progresa de la "Hello World" la implementarea sistemelor multi-agent gata de producție - toate rulând local pe mașina ta.

---

## 📚 Obiective de Învățare

După finalizarea acestui atelier, vei putea:

### Competențe de bază
1. **Implementa și gestiona servicii AI locale**
   - Instalează și configurează Microsoft Foundry Local
   - Selectează modele adecvate pentru implementarea edge
   - Gestionează ciclul de viață al modelelor (descărcare, încărcare, cache)
   - Monitorizează utilizarea resurselor și optimizează performanța

2. **Construiește aplicații alimentate de AI**
   - Implementează completări de chat compatibile cu OpenAI local
   - Proiectează prompturi eficiente pentru Small Language Models
   - Gestionează răspunsuri în streaming pentru o experiență mai bună
   - Integrează modele locale în aplicații existente

3. **Creează sisteme RAG (Retrieval Augmented Generation)**
   - Construiește căutare semantică cu embeddings
   - Fundamentează răspunsurile LLM în cunoștințe specifice domeniului
   - Evaluează calitatea RAG cu metrici standard din industrie
   - Scalează de la prototip la producție

4. **Optimizează performanța modelelor**
   - Evaluează mai multe modele pentru cazul tău de utilizare
   - Măsoară latența, debitul și timpul primului token
   - Selectează modele optime bazate pe compromisuri viteză/calitate
   - Compară compromisurile SLM vs LLM în scenarii reale

5. **Orchestrează sisteme multi-agent**
   - Proiectează agenți specializați pentru diferite sarcini
   - Implementează memorie și gestionarea contextului pentru agenți
   - Coordonează agenți în fluxuri de lucru complexe
   - Direcționează cereri inteligent între mai multe modele

6. **Implementa soluții gata de producție**
   - Implementează gestionarea erorilor și logica de retry
   - Monitorizează utilizarea tokenurilor și resursele sistemului
   - Construiește arhitecturi scalabile cu modele ca instrumente
   - Planifică căi de migrare de la edge la hibrid (edge + cloud)

---

## 🎓 Rezultate de Învățare

### Ce vei construi

Până la finalul acestui atelier, vei fi creat:

| Sesiune | Rezultat | Abilități Demonstrate |
|---------|----------|-----------------------|
| **1** | Aplicație de chat cu streaming | Configurare serviciu, completări de bază, UX streaming |
| **2** | Sistem RAG cu evaluare | Embeddings, căutare semantică, metrici de calitate |
| **3** | Suită de benchmark multi-model | Măsurarea performanței, compararea modelelor |
| **4** | Comparator SLM vs LLM | Analiza compromisurilor, strategii de optimizare |
| **5** | Orchestrator multi-agent | Proiectare agenți, gestionarea memoriei, coordonare |
| **6** | Sistem de rutare inteligent | Detectarea intenției, selecția modelului, scalabilitate |

### Matrice de Competențe

| Nivel de Abilități | Sesiunea 1-2 | Sesiunea 3-4 | Sesiunea 5-6 |
|--------------------|--------------|--------------|--------------|
| **Începător** | ✅ Configurare & bază | ⚠️ Provocator | ❌ Prea avansat |
| **Intermediar** | ✅ Revizuire rapidă | ✅ Învățare de bază | ⚠️ Obiective extinse |
| **Avansat** | ✅ Ușor de parcurs | ✅ Perfecționare | ✅ Modele de producție |

### Abilități Pregătite pentru Carieră

**După acest atelier, vei fi pregătit să:**

✅ **Construiești Aplicații Centrate pe Confidențialitate**
- Aplicații de sănătate care gestionează PHI/PII local
- Servicii financiare cu cerințe de conformitate
- Sisteme guvernamentale cu nevoi de suveranitate a datelor

✅ **Optimizezi pentru Medii Edge**
- Dispozitive IoT cu resurse limitate
- Aplicații mobile offline-first
- Sisteme în timp real cu latență redusă

✅ **Proiectezi Arhitecturi Inteligente**
- Sisteme multi-agent pentru fluxuri de lucru complexe
- Implementări hibride edge-cloud
- Infrastructură AI optimizată pentru costuri

✅ **Conduci Inițiative Edge AI**
- Evaluează fezabilitatea Edge AI pentru proiecte
- Selectează modele și cadre adecvate
- Proiectează soluții AI locale scalabile

---

## 🗺️ Structura Atelierului

### Prezentare Generală a Sesiunilor (6 Sesiuni × 30 Minute = 3 Ore)

| Sesiune | Subiect | Focus | Durată |
|---------|---------|-------|--------|
| **1** | Început cu Foundry Local | Instalare, validare, primele completări | 30 min |
| **2** | Construirea Soluțiilor AI cu RAG | Ingineria prompturilor, embeddings, evaluare | 30 min |
| **3** | Modele Open Source | Descoperirea modelelor, benchmarking, selecție | 30 min |
| **4** | Modele de Ultimă Generație | SLM vs LLM, optimizare, cadre | 30 min |
| **5** | Agenți Alimentați de AI | Proiectare agenți, orchestrare, memorie | 30 min |
| **6** | Modele ca Instrumente | Rutare, lanțuri, strategii de scalare | 30 min |

---

## 🚀 Început Rapid

### Cerințe Prealabile

**Cerințe de Sistem:**
- **OS**: Windows 10/11, macOS 11+ sau Linux (Ubuntu 20.04+)
- **RAM**: Minim 8GB, recomandat 16GB+
- **Spațiu de stocare**: Minim 10GB liber pentru modele
- **CPU**: Procesor modern cu suport AVX2
- **GPU** (opțional): Compatibil CUDA sau Qualcomm NPU pentru accelerare

**Cerințe Software:**
- **Python 3.8+** ([Descărcare](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Ghid de Instalare](../../../Workshop))
- **Git** ([Descărcare](https://git-scm.com/downloads))
- **Visual Studio Code** (recomandat) ([Descărcare](https://code.visualstudio.com/))

### Configurare în 3 Pași

#### 1. Instalează Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifică Instalarea:**
```bash
foundry --version
foundry service status
```

**Asigură-te că Azure AI Foundry Local rulează cu un port fix**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verifică funcționarea:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Găsirea Modelelor Disponibile**
Pentru a vedea ce modele sunt disponibile în instanța ta Foundry Local, poți interoga endpoint-ul modelelor:

```bash
# cmd/bash/powershell
foundry model list
```

Utilizând Endpoint Web 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clonează Repozitoriul & Instalează Dependențele

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

#### 3. Rulează Primul Exemplu

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Succes!** Ar trebui să vezi un răspuns în streaming despre Edge AI.

---

## 📦 Resurse Atelier

### Exemple Python

Exemple progresive hands-on care demonstrează fiecare concept:

| Sesiune | Exemplu | Descriere | Timp de Rulare |
|---------|---------|-----------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat de bază & streaming | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG cu embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluarea calității RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-model | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Comparare SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistem multi-agent | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Rutare bazată pe intenție | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline multi-pas | ~60s |

### Jupyter Notebooks

Explorare interactivă cu explicații și vizualizări:

| Sesiune | Notebook | Descriere | Dificultate |
|---------|----------|-----------|-------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Bazele chatului & streaming | ⭐ Începător |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Construirea sistemului RAG | ⭐⭐ Intermediar |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluarea calității RAG | ⭐⭐ Intermediar |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modele | ⭐⭐ Intermediar |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Compararea modelelor | ⭐⭐ Intermediar |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrarea agenților | ⭐⭐⭐ Avansat |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Rutare bazată pe intenție | ⭐⭐⭐ Avansat |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrarea pipeline-ului | ⭐⭐⭐ Avansat |

### Documentație

Ghiduri și referințe complete:

| Document | Descriere | Utilizare |
|----------|-----------|-----------|
| [QUICK_START.md](./QUICK_START.md) | Ghid de configurare rapidă | Începând de la zero |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Foaie de parcurs pentru comenzi & API | Ai nevoie de răspunsuri rapide |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Modele SDK & exemple | Scrierea codului |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Ghid pentru variabilele de mediu | Configurarea exemplelor |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Îmbunătățiri recente ale exemplelor | Înțelegerea schimbărilor |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Ghid de migrare | Actualizarea codului |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Probleme comune & soluții | Depanarea problemelor |

---

## 🎓 Recomandări pentru Calea de Învățare

### Pentru Începători (3-4 ore)
1. ✅ Sesiunea 1: Început (focus pe configurare și chat de bază)
2. ✅ Sesiunea 2: Bazele RAG (sari peste evaluare inițial)
3. ✅ Sesiunea 3: Benchmarking simplu (doar 2 modele)
4. ⏭️ Sari peste Sesiunile 4-6 pentru moment
5. 🔄 Revino la Sesiunile 4-6 după construirea primei aplicații

### Pentru Dezvoltatori Intermediari (3 ore)
1. ⚡ Sesiunea 1: Validare rapidă a configurării
2. ✅ Sesiunea 2: Pipeline complet RAG cu evaluare
3. ✅ Sesiunea 3: Suită completă de benchmarking
4. ✅ Sesiunea 4: Optimizarea modelelor
5. ✅ Sesiunile 5-6: Focus pe modele de arhitectură

### Pentru Practicieni Avansați (2-3 ore)
1. ⚡ Sesiunile 1-3: Revizuire rapidă și validare
2. ✅ Sesiunea 4: Detalii despre optimizare
3. ✅ Sesiunea 5: Arhitectură multi-agent
4. ✅ Sesiunea 6: Modele de producție și scalare
5. 🚀 Extinde: Construiește logică de rutare personalizată și implementări hibride

---

## Pachet de Sesiuni Atelier (Laboratoare Concentrate de 30 de Minute)

Dacă urmezi formatul condensat de atelier cu 6 sesiuni, folosește aceste ghiduri dedicate (fiecare se potrivește și completează documentele modulelor mai largi de mai sus):

| Sesiune Atelier | Ghid | Focus Principal |
|-----------------|------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalare, validare, rulare phi & GPT-OSS-20B, accelerare |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Ingineria prompturilor, modele RAG, CSV & documente fundamentale, migrare |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrare Hugging Face, benchmarking, selecție modele |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, accelerare ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Roluri ale agenților, memorie, unelte, orchestrare |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Rutare, lanțuri, scalare către Azure |

Fiecare fișier de sesiune include: rezumat, obiective de învățare, demonstrație de 30 de minute, proiect de început, listă de verificare pentru validare, depanare și referințe la SDK-ul oficial Foundry Local Python.

### Scripturi Exemple

Instalare dependențe workshop (Windows):

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

Dacă serviciul Foundry Local rulează pe o altă mașină (Windows) sau VM de pe macOS, exportați endpoint-ul:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesiune | Script(uri) | Descriere |
|---------|-------------|-----------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap serviciu & chat streaming |
| 2 | `samples/session02/rag_pipeline.py` | RAG minimal (în memorie, embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluare RAG cu metrici ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking pentru latență & throughput multi-model |
| 4 | `samples/session04/model_compare.py` | Comparație SLM vs LLM (latență & rezultate exemplu) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline de cercetare → editorial cu doi agenți |
| 6 | `samples/session06/models_router.py` | Demonstrație de rutare bazată pe intenție |
|   | `samples/session06/models_pipeline.py` | Lanț multi-pas planificare/executare/perfecționare |

### Variabile de Mediu (Comune pentru Exemple)

| Variabilă | Scop | Exemplu |
|-----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias unic pentru modelul de bază în exemple simple | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM explicit vs model mai mare pentru comparație | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Listă de aliasuri pentru benchmark | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Repetiții de benchmark per model | `3` |
| `BENCH_PROMPT` | Prompt utilizat în benchmark | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model de embedding pentru sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Suprascriere query de test pentru pipeline-ul RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Suprascriere query pentru pipeline-ul agenților | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias model pentru agentul de cercetare | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias model pentru agentul editor (poate fi diferit) | `gpt-oss-20b` |
| `SHOW_USAGE` | Când este `1`, afișează utilizarea tokenilor per completare | `1` |
| `RETRY_ON_FAIL` | Când este `1`, reîncearcă o dată la erori tranzitorii de chat | `1` |
| `RETRY_BACKOFF` | Secunde de așteptare înainte de reîncercare | `1.0` |

Dacă o variabilă nu este setată, scripturile folosesc valori implicite rezonabile. Pentru demonstrațiile cu un singur model, de obicei aveți nevoie doar de `FOUNDRY_LOCAL_ALIAS`.

### Modul Utilitar

Toate exemplele împărtășesc acum un helper `samples/workshop_utils.py` care oferă:

* Creare cache pentru `FoundryLocalManager` + client OpenAI
* Helper `chat_once()` cu opțiuni de retry + afișare utilizare
* Raportare simplă a utilizării tokenilor (activată prin `SHOW_USAGE=1`)

Acest lucru reduce duplicarea și evidențiază cele mai bune practici pentru orchestrarea eficientă a modelelor locale.

## Îmbunătățiri Opționale (Între Sesiuni)

| Temă | Îmbunătățire | Sesiuni | Env / Toggle |
|------|--------------|---------|--------------|
| Determinism | Temperatură fixă + seturi stabile de prompturi | 1–6 | Setare `temperature=0`, `top_p=1` |
| Vizibilitate Utilizare Tokeni | Predare consistentă a costului/eficienței | 1–6 | `SHOW_USAGE=1` |
| Streaming Primul Token | Metrică de latență percepută | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Reziliență la Retry | Gestionare pornire rece tranzitorie | Toate | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agenți Multi-Model | Specializare roluri eterogene | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Rutare Adaptivă | Intenție + euristici de cost | 6 | Extinderea routerului cu logică de escaladare |
| Memorie Vectorială | Recapitulare semantică pe termen lung | 2,5,6 | Integrare FAISS/Chroma embedding index |
| Export Urmărire | Auditare & evaluare | 2,5,6 | Adăugare JSON per pas |
| Rubrici de Calitate | Urmărire calitativă | 3–6 | Prompturi secundare de evaluare |
| Teste de Fum | Validare rapidă pre-workshop | Toate | `python Workshop/tests/smoke.py` |

### Start Rapid Determinist

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Așteptați număr stabil de tokeni pentru intrări identice repetate.

### Evaluare RAG (Sesiunea 2)

Utilizați `rag_eval_ragas.py` pentru a calcula relevanța răspunsului, fidelitatea și precizia contextului pe un set de date sintetic mic:

```powershell
python samples/session02/rag_eval_ragas.py
```

Extindeți prin furnizarea unui JSONL mai mare de întrebări, contexte și adevăruri de bază, apoi convertiți-l într-un `Dataset` Hugging Face.

## Anexă Comenzi CLI Precise

Workshop-ul folosește deliberat doar comenzi CLI Foundry Local documentate / stabile.

### Comenzi Stabile Referite

| Categorie | Comandă | Scop |
|-----------|---------|------|
| Core | `foundry --version` | Afișează versiunea instalată |
| Core | `foundry init` | Inițializează configurația |
| Serviciu | `foundry service start` | Pornește serviciul local (dacă nu este auto) |
| Serviciu | `foundry status` | Afișează statusul serviciului |
| Modele | `foundry model list` | Listează catalogul / modelele disponibile |
| Modele | `foundry model download <alias>` | Descarcă greutățile modelului în cache |
| Modele | `foundry model run <alias>` | Rulează (încarcă) un model local; combină cu `--prompt` pentru o singură execuție |
| Modele | `foundry model unload <alias>` / `foundry model stop <alias>` | Dezîncarcă un model din memorie (dacă este suportat) |
| Cache | `foundry cache list` | Listează modelele cache-uite (descărcate) |
| Sistem | `foundry system info` | Snapshot capacități hardware & accelerare |
| Sistem | `foundry system gpu-info` | Info diagnostic GPU |
| Config | `foundry config list` | Afișează valorile configurației curente |
| Config | `foundry config set <key> <value>` | Actualizează configurația |

### Model Prompt One‑Shot

În loc de subcomanda `model chat` depreciată, utilizați:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Aceasta execută un ciclu prompt/răspuns unic și apoi se închide.

### Modele / Pattern-uri Evitate

| Depreciat / Nondocumentat | Înlocuire / Ghid |
|---------------------------|------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Utilizați `foundry model list` + activitate recentă / loguri |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Utilizați scriptul de benchmark Python + unelte OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latență, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- Latență primului token (streaming): setați `BENCH_STREAM=1`
- Utilizare resurse: monitoare OS (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Pe măsură ce noi comenzi CLI de telemetrie se stabilizează, acestea pot fi integrate cu modificări minime în markdown-urile sesiunilor.

### Lint Automatizat

Un linter automat previne reintroducerea pattern-urilor CLI depreciate în interiorul blocurilor de cod din fișierele markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

Pattern-urile depreciate sunt blocate în interiorul blocurilor de cod.

Înlocuiri recomandate:
| Depreciat | Înlocuire |
|-----------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script de benchmark + unelte de sistem |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Rulează local:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` rulează la fiecare push & PR.

Hook opțional pre-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabel Rapid Migrare CLI → SDK

| Sarcină | CLI One-Liner | Echivalent SDK (Python) | Note |
|--------|---------------|-------------------------|------|
| Rulează un model o dată (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK inițializează automat serviciul & cache-ul |
| Descarcă (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Managerul alege cea mai bună variantă dacă aliasul se mapază la mai multe versiuni |
| Listează catalogul | `foundry model list` | `# folosiți managerul pentru fiecare alias sau mențineți o listă cunoscută` | CLI agregă; SDK în prezent instanțiere per-alias |
| Listează modelele cache-uite | `foundry cache list` | `manager.list_cached_models()` | După inițializarea managerului (orice alias) |
| Activează accelerarea GPU | `foundry config set compute.onnx.enable_gpu true` | `# Acțiune CLI; SDK presupune că configurația este deja aplicată` | Configurația este un efect extern |
| Obține URL-ul endpoint-ului | (implicit) | `manager.endpoint` | Utilizat pentru a crea un client compatibil OpenAI |
| Încălzește un model | `foundry model run <alias>` apoi primul prompt | `chat_once(alias, messages=[...])` (utilitar) | Utilitarele gestionează inițializarea latenței reci |
| Măsoară latența | `python benchmark_oss_models.py` | `import benchmark_oss_models` (sau un nou script de export) | Preferă scriptul pentru metrici consistente |
| Oprește / dezîncarcă modelul | `foundry model unload <alias>` | (Nu este expus – reporniți serviciul / procesul) | De obicei, nu este necesar pentru fluxul workshop-ului |
| Recuperează utilizarea tokenilor | (vizualizați output-ul) | `resp.usage.total_tokens` | Furnizat dacă backend-ul returnează obiectul de utilizare |

## Export Markdown Benchmark

Utilizați scriptul `Workshop/scripts/export_benchmark_markdown.py` pentru a rula un benchmark proaspăt (aceeași logică ca `samples/session03/benchmark_oss_models.py`) și pentru a genera un tabel Markdown prietenos cu GitHub plus JSON brut.

### Exemplu

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Fișiere generate:
| Fișier | Conținut |
|--------|----------|
| `benchmark_report.md` | Tabel Markdown + indicații de interpretare |
| `benchmark_report.json` | Array de metrici brute (pentru comparare / urmărirea tendințelor) |

Setați `BENCH_STREAM=1` în mediu pentru a include latența primului token, dacă este suportată.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.