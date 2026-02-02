# Rýchly sprievodca workshopom

## Predpoklady

### 1. Nainštalujte Foundry Local

Postupujte podľa oficiálneho návodu na inštaláciu:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Nainštalujte Python závislosti

Z adresára Workshop:

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

## Spúšťanie ukážok z workshopu

### Session 01: Základný chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Environment Variables:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Session 02: RAG Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Environment Variables:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Session 02: Hodnotenie RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Poznámka**: Vyžaduje dodatočné závislosti nainštalované cez `requirements.txt`

### Session 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Environment Variables:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Výstup**: JSON s metrikami latencie, priepustnosti a prvého tokenu

### Session 04: Porovnanie modelov

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Environment Variables:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Session 05: Orchestrácia viacerých agentov

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Environment Variables:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Session 06: Model Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testuje logiku smerovania** s viacerými zámermi (kód, sumarizácia, klasifikácia)

### Session 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Komplexný viacstupňový pipeline** s plánovaním, vykonaním a zdokonalením

## Skripty

### Export Benchmark Report

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Výstup**: Markdown tabuľka + JSON metriky

### Lint Markdown CLI Patterns

```bash
python lint_markdown_cli.py --verbose
```

**Účel**: Detekcia zastaraných CLI vzorov v dokumentácii

## Testovanie

### Smoke Tests

```bash
cd Workshop
python -m tests.smoke
```

**Testy**: Základná funkcionalita kľúčových ukážok

## Riešenie problémov

### Služba nebeží

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Chyby pri importe modulov

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Chyby pripojenia

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model nebol nájdený

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referencia premenných prostredia

### Základná konfigurácia
| Premenná | Predvolená hodnota | Popis |
|----------|--------------------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Rôzne | Alias modelu na použitie |
| `FOUNDRY_LOCAL_ENDPOINT` | Automaticky | Prepis koncového bodu služby |
| `SHOW_USAGE` | `0` | Zobraziť štatistiky používania tokenov |
| `RETRY_ON_FAIL` | `1` | Povoliť logiku opakovania |
| `RETRY_BACKOFF` | `1.0` | Počiatočné oneskorenie opakovania (sekundy) |

### Špecifické pre session
| Premenná | Predvolená hodnota | Popis |
|----------|--------------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model na vkladanie |
| `RAG_QUESTION` | Pozri ukážku | Testovacia otázka pre RAG |
| `BENCH_MODELS` | Rôzne | Modely oddelené čiarkou |
| `BENCH_ROUNDS` | `3` | Iterácie benchmarku |
| `BENCH_PROMPT` | Pozri ukážku | Prompt pre benchmark |
| `BENCH_STREAM` | `0` | Meranie latencie prvého tokenu |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primárny model agenta |
| `AGENT_MODEL_EDITOR` | Primárny | Editor model agenta |
| `SLM_ALIAS` | `phi-4-mini` | Malý jazykový model |
| `LLM_ALIAS` | `qwen2.5-7b` | Veľký jazykový model |
| `COMPARE_PROMPT` | Pozri ukážku | Prompt na porovnanie |

## Odporúčané modely

### Vývoj a testovanie
- **phi-4-mini** - Vyvážená kvalita a rýchlosť
- **qwen2.5-0.5b** - Veľmi rýchly pre klasifikáciu
- **gemma-2-2b** - Dobrá kvalita, stredná rýchlosť

### Produkčné scenáre
- **phi-4-mini** - Všeobecné použitie
- **deepseek-coder-1.3b** - Generovanie kódu
- **qwen2.5-7b** - Vysokokvalitné odpovede

## Dokumentácia SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Získanie pomoci

1. Skontrolujte stav služby: `foundry service status`  
2. Prezrite si logy: Skontrolujte logy služby Foundry Local  
3. Prezrite si dokumentáciu SDK: https://github.com/microsoft/Foundry-Local  
4. Prezrite si ukážkový kód: Všetky ukážky obsahujú podrobné docstringy

## Ďalšie kroky

1. Dokončite všetky session workshopu v poradí  
2. Experimentujte s rôznymi modelmi  
3. Upravte ukážky pre vaše prípady použitia  

---

**Posledná aktualizácia**: 2025-01-08  
**Verzia workshopu**: Najnovšia  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->