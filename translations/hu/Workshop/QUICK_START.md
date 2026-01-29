# Workshop Gyorsindítási Útmutató

## Előfeltételek

### 1. Telepítse a Foundry Local-t

Kövesse az hivatalos telepítési útmutatót:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Telepítse a Python függőségeket

A Workshop könyvtárból:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Workshop minták futtatása

### 01. szekció: Alapvető Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Környezeti változók:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### 02. szekció: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Környezeti változók:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### 02. szekció: RAG Értékelés (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Megjegyzés**: További függőségek szükségesek, telepítve a `requirements.txt` fájlon keresztül

### 03. szekció: Teljesítménytesztelés

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Környezeti változók:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Kimenet**: JSON, amely tartalmazza a késleltetést, áteresztőképességet és az első token metrikáit

### 04. szekció: Modell összehasonlítás

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Környezeti változók:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### 05. szekció: Többügynökös Orkesztráció

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Környezeti változók:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### 06. szekció: Modell Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**Teszteli az útválasztási logikát** több szándékkal (kód, összefoglalás, osztályozás)

### 06. szekció: Pipeline

```bash
python -m session06.models_pipeline
```

**Komplex több lépéses pipeline** tervezéssel, végrehajtással és finomítással

## Szkriptek

### Teljesítményjelentés exportálása

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Kimenet**: Markdown táblázat + JSON metrikák

### Markdown CLI minták lintelése

```bash
python lint_markdown_cli.py --verbose
```

**Cél**: Elavult CLI minták észlelése a dokumentációban

## Tesztelés

### Gyors tesztek

```bash
cd Workshop
python -m tests.smoke
```

**Tesztelés**: Kulcsfontosságú minták alapvető funkcionalitása

## Hibakeresés

### Szolgáltatás nem fut

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modul importálási hibák

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Kapcsolódási hibák

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modell nem található

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Környezeti változók referenciája

### Alapvető konfiguráció
| Változó | Alapértelmezett | Leírás |
|---------|-----------------|--------|
| `FOUNDRY_LOCAL_ALIAS` | Változó | Használandó modell alias |
| `FOUNDRY_LOCAL_ENDPOINT` | Automatikus | Szolgáltatás végpontjának felülírása |
| `SHOW_USAGE` | `0` | Token használati statisztikák megjelenítése |
| `RETRY_ON_FAIL` | `1` | Újrapróbálkozási logika engedélyezése |
| `RETRY_BACKOFF` | `1.0` | Kezdeti újrapróbálkozási késleltetés (másodpercben) |

### Szekció-specifikus
| Változó | Alapértelmezett | Leírás |
|---------|-----------------|--------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Beágyazási modell |
| `RAG_QUESTION` | Lásd minta | RAG teszt kérdés |
| `BENCH_MODELS` | Változó | Modellnevek vesszővel elválasztva |
| `BENCH_ROUNDS` | `3` | Teljesítményteszt iterációk |
| `BENCH_PROMPT` | Lásd minta | Teljesítményteszt prompt |
| `BENCH_STREAM` | `0` | Első token késleltetésének mérése |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Elsődleges ügynök modell |
| `AGENT_MODEL_EDITOR` | Elsődleges | Szerkesztő ügynök modell |
| `SLM_ALIAS` | `phi-4-mini` | Kis nyelvi modell |
| `LLM_ALIAS` | `qwen2.5-7b` | Nagy nyelvi modell |
| `COMPARE_PROMPT` | Lásd minta | Összehasonlítás prompt |

## Ajánlott modellek

### Fejlesztés és tesztelés
- **phi-4-mini** - Kiegyensúlyozott minőség és sebesség
- **qwen2.5-0.5b** - Nagyon gyors osztályozáshoz
- **gemma-2-2b** - Jó minőség, mérsékelt sebesség

### Gyártási forgatókönyvek
- **phi-4-mini** - Általános célú
- **deepseek-coder-1.3b** - Kódgenerálás
- **qwen2.5-7b** - Magas minőségű válaszok

## SDK Dokumentáció

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Segítség kérése

1. Ellenőrizze a szolgáltatás állapotát: `foundry service status`  
2. Nézze meg a naplókat: Ellenőrizze a Foundry Local szolgáltatás naplóit  
3. Nézze meg az SDK dokumentációt: https://github.com/microsoft/Foundry-Local  
4. Tekintse át a mintakódot: Minden minta részletes docstringekkel rendelkezik  

## Következő lépések

1. Végezze el az összes workshop szekciót sorrendben  
2. Kísérletezzen különböző modellekkel  
3. Módosítsa a mintákat saját felhasználási esetekhez  

---

**Utolsó frissítés**: 2025-01-08  
**Workshop verzió**: Legújabb  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->