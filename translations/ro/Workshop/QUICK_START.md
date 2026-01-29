# Ghid Rapid pentru Workshop

## Cerințe preliminare

### 1. Instalează Foundry Local

Urmează ghidul oficial de instalare:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instalează Dependențele Python

Din directorul Workshop:

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

## Rularea Exemplelor din Workshop

### Sesiunea 01: Chat de Bază

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Variabile de Mediu:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesiunea 02: Pipeline RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Variabile de Mediu:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesiunea 02: Evaluarea RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Notă**: Necesită dependențe suplimentare instalate prin `requirements.txt`

### Sesiunea 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Variabile de Mediu:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Output**: JSON cu latență, throughput și metrici pentru primul token

### Sesiunea 04: Compararea Modelului

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Variabile de Mediu:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesiunea 05: Orchestrarea Multi-Agent

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Variabile de Mediu:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesiunea 06: Router de Model

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testează logica de rutare** cu mai multe intenții (cod, sumarizare, clasificare)

### Sesiunea 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline complex în mai mulți pași** cu planificare, execuție și rafinare

## Scripturi

### Export Raport de Benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Output**: Tabel Markdown + metrici JSON

### Lint pentru Modele CLI Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Scop**: Detectează modele CLI depășite în documentație

## Testare

### Teste de Verificare

```bash
cd Workshop
python -m tests.smoke
```

**Teste**: Funcționalitatea de bază a exemplelor cheie

## Depanare

### Serviciul Nu Rulează

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Erori la Importul Modulului

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Erori de Conexiune

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modelul Nu a Fost Găsit

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referință pentru Variabile de Mediu

### Configurație de Bază
| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Variază | Alias-ul modelului utilizat |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Suprascrie endpoint-ul serviciului |
| `SHOW_USAGE` | `0` | Afișează statistici de utilizare a token-urilor |
| `RETRY_ON_FAIL` | `1` | Activează logica de reîncercare |
| `RETRY_BACKOFF` | `1.0` | Întârzierea inițială pentru reîncercare (secunde) |

### Specific Sesiunii
| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model de încorporare |
| `RAG_QUESTION` | Vezi exemplu | Întrebarea de test RAG |
| `BENCH_MODELS` | Variază | Modele separate prin virgulă |
| `BENCH_ROUNDS` | `3` | Iterații de benchmark |
| `BENCH_PROMPT` | Vezi exemplu | Prompt de benchmark |
| `BENCH_STREAM` | `0` | Măsoară latența primului token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelul principal al agentului |
| `AGENT_MODEL_EDITOR` | Primar | Modelul editorului agentului |
| `SLM_ALIAS` | `phi-4-mini` | Model de limbaj mic |
| `LLM_ALIAS` | `qwen2.5-7b` | Model de limbaj mare |
| `COMPARE_PROMPT` | Vezi exemplu | Prompt de comparație |

## Modele Recomandate

### Dezvoltare & Testare
- **phi-4-mini** - Calitate și viteză echilibrate
- **qwen2.5-0.5b** - Foarte rapid pentru clasificare
- **gemma-2-2b** - Calitate bună, viteză moderată

### Scenarii de Producție
- **phi-4-mini** - Scop general
- **deepseek-coder-1.3b** - Generare de cod
- **qwen2.5-7b** - Răspunsuri de calitate înaltă

## Documentație SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Obținerea Ajutorului

1. Verifică statusul serviciului: `foundry service status`  
2. Vizualizează logurile: Verifică logurile serviciului Foundry Local  
3. Consultă documentația SDK: https://github.com/microsoft/Foundry-Local  
4. Revizuiește codul exemplu: Toate exemplele au docstring-uri detaliate  

## Pași Următori

1. Completează toate sesiunile workshop-ului în ordine  
2. Experimentează cu modele diferite  
3. Modifică exemplele pentru cazurile tale de utilizare  

---

**Ultima actualizare**: 2025-01-08  
**Versiunea Workshop-ului**: Ultima  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->