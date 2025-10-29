<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T23:11:14+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "ro"
}
-->
# EdgeAI pentru Începători - Atelier

> **Curs practic pentru dezvoltarea aplicațiilor Edge AI pregătite pentru producție**
>
> Stăpânește implementarea AI locală cu Microsoft Foundry Local, de la prima completare de chat până la orchestrarea multi-agent în 6 sesiuni progresive.

---

## 🎯 Introducere

Bine ați venit la **Atelierul EdgeAI pentru Începători** - ghidul dvs. practic pentru construirea aplicațiilor inteligente care rulează complet pe hardware local. Acest atelier transformă conceptele teoretice ale Edge AI în abilități practice prin exerciții progresive utilizând Microsoft Foundry Local și Small Language Models (SLMs).

### De ce acest atelier?

**Revoluția Edge AI este aici**

Organizațiile din întreaga lume trec de la AI dependent de cloud la calculul edge din trei motive critice:

1. **Confidențialitate & Conformitate** - Procesarea datelor sensibile local, fără transmiterea lor în cloud (HIPAA, GDPR, reglementări financiare)
2. **Performanță** - Eliminarea latenței rețelei (50-500ms local vs 500-2000ms tur-retur în cloud)
3. **Controlul Costurilor** - Eliminarea costurilor per token API și scalarea fără cheltuieli de cloud

**Dar Edge AI este diferit**

Rularea AI pe dispozitive locale necesită abilități noi:
- Selectarea și optimizarea modelelor pentru constrângerile de resurse
- Managementul serviciilor locale și accelerarea hardware
- Ingineria prompturilor pentru modele mai mici
- Modele de implementare pentru dispozitive edge

**Acest atelier oferă aceste abilități**

În 6 sesiuni concentrate (~3 ore în total), veți progresa de la "Hello World" la implementarea sistemelor multi-agent pregătite pentru producție - toate rulând local pe mașina dvs.

---

## 📚 Obiective de Învățare

Prin completarea acestui atelier, veți putea:

### Competențe de bază
1. **Implementați și gestionați servicii AI locale**
   - Instalați și configurați Microsoft Foundry Local
   - Selectați modele adecvate pentru implementarea edge
   - Gestionați ciclul de viață al modelelor (descărcare, încărcare, cache)
   - Monitorizați utilizarea resurselor și optimizați performanța

2. **Construiți aplicații alimentate de AI**
   - Implementați completări de chat compatibile cu OpenAI local
   - Proiectați prompturi eficiente pentru Small Language Models
   - Gestionați răspunsurile în flux pentru o experiență mai bună
   - Integrați modele locale în aplicații existente

3. **Creați sisteme RAG (Retrieval Augmented Generation)**
   - Construiți căutări semantice cu embeddings
   - Fundamentați răspunsurile LLM în cunoștințe specifice domeniului
   - Evaluați calitatea RAG cu metrici standard din industrie
   - Scalați de la prototip la producție

4. **Optimizați performanța modelelor**
   - Evaluați mai multe modele pentru cazul dvs. de utilizare
   - Măsurați latența, debitul și timpul primului token
   - Selectați modele optime bazate pe compromisuri între viteză și calitate
   - Comparați compromisurile SLM vs LLM în scenarii reale

5. **Orchestrați sisteme multi-agent**
   - Proiectați agenți specializați pentru diferite sarcini
   - Implementați memorie și gestionarea contextului pentru agenți
   - Coordonați agenții în fluxuri de lucru complexe
   - Direcționați cererile inteligent între mai multe modele

6. **Implementați soluții pregătite pentru producție**
   - Implementați gestionarea erorilor și logica de retry
   - Monitorizați utilizarea tokenurilor și resursele sistemului
   - Construiți arhitecturi scalabile cu modele ca instrumente
   - Planificați căi de migrare de la edge la hibrid (edge + cloud)

---

## 🎓 Rezultate de Învățare

### Ce veți construi

Până la finalul acestui atelier, veți fi creat:

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

**După acest atelier, veți fi pregătit să:**

✅ **Construiți Aplicații Centrate pe Confidențialitate**
- Aplicații de sănătate care gestionează PHI/PII local
- Servicii financiare cu cerințe de conformitate
- Sisteme guvernamentale cu nevoi de suveranitate a datelor

✅ **Optimizați pentru Medii Edge**
- Dispozitive IoT cu resurse limitate
- Aplicații mobile offline-first
- Sisteme în timp real cu latență redusă

✅ **Proiectați Arhitecturi Inteligente**
- Sisteme multi-agent pentru fluxuri de lucru complexe
- Implementări hibride edge-cloud
- Infrastructură AI optimizată pentru costuri

✅ **Conduceți Inițiative Edge AI**
- Evaluați fezabilitatea Edge AI pentru proiecte
- Selectați modele și cadre adecvate
- Arhitecturați soluții AI locale scalabile

---

## 🗺️ Structura Atelierului

### Prezentare Generală a Sesiunilor (6 Sesiuni × 30 Minute = 3 Ore)

| Sesiune | Subiect | Focus | Durată |
|---------|---------|-------|--------|
| **1** | Începeți cu Foundry Local | Instalare, validare, primele completări | 30 min |
| **2** | Construirea Soluțiilor AI cu RAG | Ingineria prompturilor, embeddings, evaluare | 30 min |
| **3** | Modele Open Source | Descoperirea modelelor, benchmarking, selecție | 30 min |
| **4** | Modele de Ultimă Generație | SLM vs LLM, optimizare, cadre | 30 min |
| **5** | Agenți Alimentați de AI | Proiectare agenți, orchestrare, memorie | 30 min |
| **6** | Modele ca Instrumente | Rutare, chaining, strategii de scalare | 30 min |

---

## 🚀 Start Rapid

### Cerințe Prealabile

**Cerințe de Sistem:**
- **OS**: Windows 10/11, macOS 11+, sau Linux (Ubuntu 20.04+)
- **RAM**: minim 8GB, recomandat 16GB+
- **Spațiu de Stocare**: 10GB+ liber pentru modele
- **CPU**: Procesor modern cu suport AVX2
- **GPU** (opțional): Compatibil CUDA sau Qualcomm NPU pentru accelerare

**Cerințe Software:**
- **Python 3.8+** ([Descărcare](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Ghid de Instalare](../../../Workshop))
- **Git** ([Descărcare](https://git-scm.com/downloads))
- **Visual Studio Code** (recomandat) ([Descărcare](https://code.visualstudio.com/))

### Configurare în 3 Pași

#### 1. Instalați Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificați Instalarea:**
```bash
foundry --version
foundry service status
```

**Asigurați-vă că Azure AI Foundry Local rulează pe un port fix**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verificați funcționarea:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Găsirea Modelelor Disponibile**
Pentru a vedea ce modele sunt disponibile în instanța dvs. Foundry Local, puteți interoga endpoint-ul modelelor:

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

#### 2. Clonați Repozitoriul & Instalați Dependențele

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

#### 3. Rulați Primul Exemplu

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Succes!** Ar trebui să vedeți un răspuns în flux despre Edge AI.

---

## 📦 Resurse pentru Atelier

### Exemple Python

Exemple practice progresive care demonstrează fiecare concept:

| Sesiune | Exemplu | Descriere | Timp de Rulare |
|---------|---------|-----------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat de bază & streaming | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG cu embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Evaluarea calității RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-model | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Comparație SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistem multi-agent | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Rutare bazată pe intenție | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline multi-pas | ~60s |

### Jupyter Notebooks

Explorare interactivă cu explicații și vizualizări:

| Sesiune | Notebook | Descriere | Dificultate |
|---------|----------|-----------|-------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Bazele chat-ului & streaming | ⭐ Începător |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Construirea sistemului RAG | ⭐⭐ Intermediar |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluarea calității RAG | ⭐⭐ Intermediar |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modele | ⭐⭐ Intermediar |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Comparație modele | ⭐⭐ Intermediar |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrarea agenților | ⭐⭐⭐ Avansat |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Rutare pe bază de intenție | ⭐⭐⭐ Avansat |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrarea pipeline-ului | ⭐⭐⭐ Avansat |

### Documentație

Ghiduri și referințe complete:

| Document | Descriere | Când să folosiți |
|----------|-----------|------------------|
| [QUICK_START.md](./QUICK_START.md) | Ghid rapid de configurare | Începeți de la zero |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Foaie de parcurs pentru comenzi & API | Aveți nevoie de răspunsuri rapide |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Modele SDK & exemple | Scrierea codului |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Ghid pentru variabilele de mediu | Configurarea exemplelor |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Îmbunătățiri recente ale exemplelor | Înțelegerea schimbărilor |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Ghid de migrare | Actualizarea codului |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Probleme comune & soluții | Depanarea problemelor |

---

## 🎓 Recomandări pentru Parcursul de Învățare

### Pentru Începători (3-4 ore)
1. ✅ Sesiunea 1: Începeți (focus pe configurare și chat de bază)
2. ✅ Sesiunea 2: Bazele RAG (săriți peste evaluare inițial)
3. ✅ Sesiunea 3: Benchmarking simplu (doar 2 modele)
4. ⏭️ Săriți peste Sesiunile 4-6 pentru moment
5. 🔄 Reveniți la Sesiunile 4-6 după construirea primei aplicații

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
5. 🚀 Extindeți: Construiți logică de rutare personalizată și implementări hibride

---

## Pachetul de Sesiuni ale Atelierului (Laboratoare Concentrate de 30 de Minute)

Dacă urmați formatul condensat al atelierului de 6 sesiuni, utilizați aceste ghiduri dedicate (fiecare se potrivește și completează documentația mai amplă de mai sus):

| Sesiunea Atelierului | Ghid | Focus Principal |
|----------------------|------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalare, validare, rulare phi & GPT-OSS-20B, accelerare |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Ingineria prompturilor, modele RAG, fundamentare CSV & documente, migrare |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrare Hugging Face, benchmarking, selecție modele |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, accelerare ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Roluri ale agenților, memorie, unelte, orchestrare |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Rutare, concatenare, scalare către Azure |

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
| 2 | `samples/session02/rag_pipeline.py` | RAG minimal (embedding-uri în memorie) |
|   | `samples/session02/rag_eval_ragas.py` | Evaluare RAG cu metrici ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking pentru latență & throughput multi-model |
| 4 | `samples/session04/model_compare.py` | Comparație SLM vs LLM (latență & rezultate exemplu) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline de cercetare cu doi agenți → editorial |
| 6 | `samples/session06/models_router.py` | Demonstrație de rutare bazată pe intenție |
|   | `samples/session06/models_pipeline.py` | Lanț multi-pas planificare/executare/perfecționare |

### Variabile de Mediu (Comune pentru Exemple)

| Variabilă | Scop | Exemplu |
|-----------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias-ul modelului unic implicit pentru exemplele de bază | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM explicit vs model mai mare pentru comparație | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Listă de alias-uri pentru benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Repetiții de benchmark per model | `3` |
| `BENCH_PROMPT` | Prompt utilizat în benchmark | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model de embedding sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Suprascriere întrebare de test pentru pipeline-ul RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Suprascriere întrebare pentru pipeline-ul agenților | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias-ul modelului pentru agentul de cercetare | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias-ul modelului pentru agentul editor (poate fi diferit) | `gpt-oss-20b` |
| `SHOW_USAGE` | Când este `1`, afișează utilizarea token-urilor per completare | `1` |
| `RETRY_ON_FAIL` | Când este `1`, încearcă din nou o dată în caz de erori temporare de chat | `1` |
| `RETRY_BACKOFF` | Secunde de așteptare înainte de a încerca din nou | `1.0` |

Dacă o variabilă nu este setată, scripturile revin la setările implicite. Pentru demonstrațiile cu un singur model, de obicei aveți nevoie doar de `FOUNDRY_LOCAL_ALIAS`.

### Modul Utilitar

Toate exemplele împărtășesc acum un helper `samples/workshop_utils.py` care oferă:

* Crearea cache-ului `FoundryLocalManager` + client OpenAI
* Helper `chat_once()` cu opțiuni de retry + afișare utilizare
* Raportare simplă a utilizării token-urilor (activată prin `SHOW_USAGE=1`)

Acest lucru reduce duplicarea și evidențiază cele mai bune practici pentru orchestrarea eficientă a modelelor locale.

## Îmbunătățiri Opționale (Între Sesiuni)

| Temă | Îmbunătățire | Sesiuni | Env / Toggle |
|------|--------------|---------|--------------|
| Determinism | Temperatură fixă + seturi stabile de prompt-uri | 1–6 | Setare `temperature=0`, `top_p=1` |
| Vizibilitate Utilizare Token | Predare consistentă cost/eficiență | 1–6 | `SHOW_USAGE=1` |
| Streaming Primul Token | Metrică de latență percepută | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Reziliență la Retry | Gestionarea pornirii reci temporare | Toate | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agenți Multi-Model | Specializare pe roluri eterogene | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Rutare Adaptivă | Intenție + euristici de cost | 6 | Extindeți router-ul cu logică de escaladare |
| Memorie Vectorială | Recapitulare semantică pe termen lung | 2,5,6 | Integrați indexul de embedding FAISS/Chroma |
| Export Traseu | Auditare & evaluare | 2,5,6 | Adăugați linii JSON per pas |
| Rubrici de Calitate | Urmărire calitativă | 3–6 | Prompt-uri secundare de evaluare |
| Teste de Fum | Validare rapidă înainte de workshop | Toate | `python Workshop/tests/smoke.py` |

### Start Rapid Determinist

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Așteptați număr stabil de token-uri pentru intrări identice repetate.

### Evaluare RAG (Sesiunea 2)

Utilizați `rag_eval_ragas.py` pentru a calcula relevanța răspunsului, fidelitatea și precizia contextului pe un set de date sintetic mic:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Extindeți prin furnizarea unui JSONL mai mare de întrebări, contexte și adevăruri de bază, apoi convertiți-l într-un `Dataset` Hugging Face.

## Anexă Comenzi CLI Precise

Workshop-ul utilizează deliberat doar comenzi CLI Foundry Local documentate / stabile.

### Comenzi Stabile Referite

| Categorie | Comandă | Scop |
|-----------|---------|------|
| Core | `foundry --version` | Afișează versiunea instalată |
| Core | `foundry init` | Inițializează configurația |
| Serviciu | `foundry service start` | Pornește serviciul local (dacă nu este auto) |
| Serviciu | `foundry status` | Afișează starea serviciului |
| Modele | `foundry model list` | Listează catalogul / modelele disponibile |
| Modele | `foundry model download <alias>` | Descarcă greutățile modelului în cache |
| Modele | `foundry model run <alias>` | Lansează (încarcă) un model local; combină cu `--prompt` pentru o singură execuție |
| Modele | `foundry model unload <alias>` / `foundry model stop <alias>` | Dezîncarcă un model din memorie (dacă este suportat) |
| Cache | `foundry cache list` | Listează modelele cache-ate (descărcate) |
| Sistem | `foundry system info` | Snapshot capacități hardware & accelerare |
| Sistem | `foundry system gpu-info` | Informații de diagnosticare GPU |
| Config | `foundry config list` | Afișează valorile curente ale configurației |
| Config | `foundry config set <key> <value>` | Actualizează configurația |

### Model Prompt Pattern One‑Shot

În loc de subcomanda `model chat` depreciată, utilizați:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Aceasta execută un ciclu prompt/răspuns unic și apoi se închide.

### Modele / Pattern-uri Evitate

| Depreciat / Nondocumentat | Înlocuire / Ghidare |
|---------------------------|---------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Utilizați simplu `foundry model list` + activitate recentă / loguri |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Utilizați scriptul de benchmark Python + unelte OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latență, p95, token-uri/sec: `samples/session03/benchmark_oss_models.py`
- Latență primului token (streaming): setați `BENCH_STREAM=1`
- Utilizare resurse: monitoare OS (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Pe măsură ce noi comenzi CLI de telemetrie se stabilizează, acestea pot fi integrate cu modificări minime în markdown-urile sesiunii.

### Gardă Automată de Lint

Un linter automat previne reintroducerea pattern-urilor CLI depreciate în interiorul blocurilor de cod ale fișierelor markdown:

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

Rulați local:
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

| Sarcină | Linie Unică CLI | Echivalent SDK (Python) | Note |
|---------|-----------------|--------------------------|------|
| Rulează un model o dată (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK inițializează serviciul & cache-ul automat |
| Descarcă (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Managerul alege cea mai bună variantă dacă alias-ul se potrivește cu mai multe versiuni |
| Listează catalogul | `foundry model list` | `# use manager for each alias or maintain known list` | CLI agregă; SDK în prezent instanțiere per-alias |
| Listează modelele cache-ate | `foundry cache list` | `manager.list_cached_models()` | După inițializarea managerului (orice alias) |
| Activează accelerarea GPU | `foundry config set compute.onnx.enable_gpu true` | `# CLI action; SDK assumes config already applied` | Configurația este efect extern |
| Obține URL-ul endpoint-ului | (implicit) | `manager.endpoint` | Utilizat pentru a crea client compatibil OpenAI |
| Încălzește un model | `foundry model run <alias>` apoi primul prompt | `chat_once(alias, messages=[...])` (utilitar) | Utilitarele gestionează încălzirea inițială a latenței reci |
| Măsoară latența | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (sau script nou de export) | Prefer scriptul pentru metrici consistente |
| Oprește / dezîncarcă modelul | `foundry model unload <alias>` | (Nu este expus – reporniți serviciul / procesul) | De obicei, nu este necesar pentru fluxul workshop-ului |
| Recuperează utilizarea token-urilor | (vizualizați output-ul) | `resp.usage.total_tokens` | Furnizat dacă backend-ul returnează obiectul de utilizare |

## Export Markdown Benchmark

Utilizați scriptul `Workshop/scripts/export_benchmark_markdown.py` pentru a rula un benchmark proaspăt (aceeași logică ca `samples/session03/benchmark_oss_models.py`) și a emite un tabel Markdown prietenos cu GitHub plus JSON brut.

### Exemplu

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Fișiere generate:
| Fișier | Conținut |
|--------|----------|
| `benchmark_report.md` | Tabel Markdown + indicații de interpretare |
| `benchmark_report.json` | Array de metrici brute (pentru comparare / urmărirea tendințelor) |

Setați `BENCH_STREAM=1` în mediu pentru a include latența primului token, dacă este suportată.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.