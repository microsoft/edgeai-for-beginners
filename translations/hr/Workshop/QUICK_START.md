<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-12T00:30:35+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "hr"
}
-->
# Brzi vodič za radionicu

## Preduvjeti

### 1. Instalirajte Foundry Local

Slijedite službeni vodič za instalaciju:
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instalirajte Python ovisnosti

Iz direktorija radionice:

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

## Pokretanje primjera iz radionice

### Sesija 01: Osnovni chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Varijable okruženja:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesija 02: RAG cjevovod

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Varijable okruženja:**
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesija 02: Procjena RAG-a (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Napomena**: Zahtijeva dodatne ovisnosti instalirane putem `requirements.txt`

### Sesija 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Varijable okruženja:**
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Izlaz**: JSON s metrikama kašnjenja, propusnosti i prvog tokena

### Sesija 04: Usporedba modela

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Varijable okruženja:**
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesija 05: Orkestracija više agenata

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Varijable okruženja:**
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesija 06: Usmjerivač modela

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testira logiku usmjeravanja** s više namjera (kod, sažimanje, klasifikacija)

### Sesija 06: Cjevovod

```bash
python -m session06.models_pipeline
```

**Složen višestupanjski cjevovod** s planiranjem, izvršenjem i doradom

## Skripte

### Izvoz izvješća o benchmarku

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Izlaz**: Markdown tablica + JSON metrike

### Provjera CLI uzoraka u Markdownu

```bash
python lint_markdown_cli.py --verbose
```

**Svrha**: Otkrivanje zastarjelih CLI uzoraka u dokumentaciji

## Testiranje

### Brzi testovi

```bash
cd Workshop
python -m tests.smoke
```

**Testovi**: Osnovna funkcionalnost ključnih primjera

## Rješavanje problema

### Usluga ne radi

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Pogreške pri uvozu modula

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Pogreške povezivanja

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model nije pronađen

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referenca varijabli okruženja

### Osnovna konfiguracija
| Varijabla | Zadano | Opis |
|-----------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | Varira | Alias modela za korištenje |
| `FOUNDRY_LOCAL_ENDPOINT` | Automatski | Prepisuje krajnju točku usluge |
| `SHOW_USAGE` | `0` | Prikazuje statistiku korištenja tokena |
| `RETRY_ON_FAIL` | `1` | Omogućuje logiku ponovnog pokušaja |
| `RETRY_BACKOFF` | `1.0` | Početno kašnjenje ponovnog pokušaja (sekunde) |

### Specifično za sesiju
| Varijabla | Zadano | Opis |
|-----------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model za ugrađivanje |
| `RAG_QUESTION` | Pogledajte primjer | Testno pitanje za RAG |
| `BENCH_MODELS` | Varira | Modeli odvojeni zarezom |
| `BENCH_ROUNDS` | `3` | Iteracije benchmarka |
| `BENCH_PROMPT` | Pogledajte primjer | Upit za benchmark |
| `BENCH_STREAM` | `0` | Mjerenje kašnjenja prvog tokena |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primarni model agenta |
| `AGENT_MODEL_EDITOR` | Primarni | Model agenta urednika |
| `SLM_ALIAS` | `phi-4-mini` | Mali jezični model |
| `LLM_ALIAS` | `qwen2.5-7b` | Veliki jezični model |
| `COMPARE_PROMPT` | Pogledajte primjer | Upit za usporedbu |

## Preporučeni modeli

### Razvoj i testiranje
- **phi-4-mini** - Uravnotežena kvaliteta i brzina
- **qwen2.5-0.5b** - Vrlo brz za klasifikaciju
- **gemma-2-2b** - Dobra kvaliteta, umjerena brzina

### Proizvodni scenariji
- **phi-4-mini** - Opća namjena
- **deepseek-coder-1.3b** - Generiranje koda
- **qwen2.5-7b** - Odgovori visoke kvalitete

## SDK dokumentacija

- **Foundry Local**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Dobivanje pomoći

1. Provjerite status usluge: `foundry service status`
2. Pregledajte logove: Provjerite logove usluge Foundry Local
3. Pregledajte SDK dokumentaciju: https://github.com/microsoft/Foundry-Local
4. Pregledajte primjere koda: Svi primjeri imaju detaljne docstringove

## Sljedeći koraci

1. Završite sve sesije radionice redoslijedom
2. Eksperimentirajte s različitim modelima
3. Prilagodite primjere za svoje slučajeve korištenja

---

**Zadnje ažuriranje**: 2025-01-08  
**Verzija radionice**: Najnovija  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->