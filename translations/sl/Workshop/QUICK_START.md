# Hitra navodila za delavnico

## Predpogoji

### 1. Namestite Foundry Local

Sledite uradnim navodilom za namestitev:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Namestite Python odvisnosti

Iz direktorija delavnice:

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

## Zagon primerov delavnice

### Seja 01: Osnovni klepet

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Okoljske spremenljivke:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Seja 02: RAG cevovod

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Okoljske spremenljivke:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Seja 02: RAG ocenjevanje (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Opomba**: Zahteva dodatne odvisnosti, nameščene prek `requirements.txt`

### Seja 03: Primerjava zmogljivosti

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Okoljske spremenljivke:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Izhod**: JSON z metriko zakasnitve, prepustnosti in prvega žetona

### Seja 04: Primerjava modelov

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Okoljske spremenljivke:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Seja 05: Orkestracija več agentov

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Okoljske spremenljivke:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Seja 06: Usmerjevalnik modelov

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testira logiko usmerjanja** z več nameni (koda, povzetek, klasifikacija)

### Seja 06: Cevovod

```bash
python -m session06.models_pipeline
```

**Kompleksen večstopenjski cevovod** z načrtovanjem, izvedbo in izboljšanjem

## Skripte

### Izvoz poročila o primerjavi zmogljivosti

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Izhod**: Markdown tabela + JSON metrike

### Preverjanje vzorcev CLI v Markdownu

```bash
python lint_markdown_cli.py --verbose
```

**Namen**: Zaznavanje zastarelih vzorcev CLI v dokumentaciji

## Testiranje

### Hitri testi

```bash
cd Workshop
python -m tests.smoke
```

**Testi**: Osnovna funkcionalnost ključnih primerov

## Odpravljanje težav

### Storitev ne deluje

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Napake pri uvozu modulov

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Napake pri povezavi

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model ni najden

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referenca okoljske spremenljivke

### Osnovna konfiguracija
| Spremenljivka | Privzeto | Opis |
|---------------|----------|------|
| `FOUNDRY_LOCAL_ALIAS` | Različno | Alias modela za uporabo |
| `FOUNDRY_LOCAL_ENDPOINT` | Samodejno | Prekliči končno točko storitve |
| `SHOW_USAGE` | `0` | Prikaži statistiko uporabe žetonov |
| `RETRY_ON_FAIL` | `1` | Omogoči logiko ponovnega poskusa |
| `RETRY_BACKOFF` | `1.0` | Začetna zakasnitev ponovnega poskusa (sekunde) |

### Specifično za sejo
| Spremenljivka | Privzeto | Opis |
|---------------|----------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model za vdelavo |
| `RAG_QUESTION` | Glej primer | Testno vprašanje za RAG |
| `BENCH_MODELS` | Različno | Modeli, ločeni z vejico |
| `BENCH_ROUNDS` | `3` | Iteracije primerjanja zmogljivosti |
| `BENCH_PROMPT` | Glej primer | Poziv za primerjavo zmogljivosti |
| `BENCH_STREAM` | `0` | Merjenje zakasnitve prvega žetona |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primarni model agenta |
| `AGENT_MODEL_EDITOR` | Primarni | Model agenta za urejanje |
| `SLM_ALIAS` | `phi-4-mini` | Majhen jezikovni model |
| `LLM_ALIAS` | `qwen2.5-7b` | Velik jezikovni model |
| `COMPARE_PROMPT` | Glej primer | Poziv za primerjavo |

## Priporočeni modeli

### Razvoj in testiranje
- **phi-4-mini** - Uravnotežena kakovost in hitrost
- **qwen2.5-0.5b** - Zelo hitro za klasifikacijo
- **gemma-2-2b** - Dobra kakovost, zmerna hitrost

### Proizvodni scenariji
- **phi-4-mini** - Splošna uporaba
- **deepseek-coder-1.3b** - Generiranje kode
- **qwen2.5-7b** - Visokokakovostni odgovori

## Dokumentacija SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Pomoč

1. Preverite stanje storitve: `foundry service status`
2. Preglejte dnevnike: Preverite dnevnike storitve Foundry Local
3. Preverite dokumentacijo SDK: https://github.com/microsoft/Foundry-Local
4. Preglejte vzorčno kodo: Vsi primeri imajo podrobne docstringe

## Naslednji koraki

1. Zaključite vse seje delavnice po vrsti
2. Eksperimentirajte z različnimi modeli
3. Prilagodite primere za svoje potrebe

---

**Zadnja posodobitev**: 2025-01-08  
**Različica delavnice**: Najnovejša  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->