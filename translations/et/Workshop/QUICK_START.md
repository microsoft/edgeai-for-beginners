<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-12T01:00:26+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "et"
}
-->
# Töötuba Kiire Alustamise Juhend

## Eeltingimused

### 1. Paigalda Foundry Local

Järgi ametlikku paigaldusjuhendit:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Paigalda Python sõltuvused

Töötuba kataloogist:  

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

## Töötuba näidete käivitamine

### Sessioon 01: Põhiline vestlus

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Keskkonnamuutujad:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sessioon 02: RAG torujuhe

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Keskkonnamuutujad:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sessioon 02: RAG hindamine (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Märkus**: Vajab täiendavaid sõltuvusi, mis on paigaldatud `requirements.txt` kaudu

### Sessioon 03: Võrdlusuuringud

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Keskkonnamuutujad:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Väljund**: JSON latentsuse, läbilaskevõime ja esimese märgi mõõdikutega

### Sessioon 04: Mudelite võrdlus

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Keskkonnamuutujad:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sessioon 05: Multi-agent orkestreerimine

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Keskkonnamuutujad:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sessioon 06: Mudeli suunaja

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testib suunamisloogikat** mitme kavatsusega (kood, kokkuvõte, klassifikatsioon)

### Sessioon 06: Torujuhe

```bash
python -m session06.models_pipeline
```

**Kompleksne mitmeastmeline torujuhe** koos planeerimise, täitmise ja täiendamisega

## Skriptid

### Ekspordi võrdlusuuringu aruanne

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Väljund**: Markdown tabel + JSON mõõdikud

### Kontrolli Markdown CLI mustreid

```bash
python lint_markdown_cli.py --verbose
```

**Eesmärk**: Tuvastada vananenud CLI mustrid dokumentatsioonis

## Testimine

### Kiirtestid

```bash
cd Workshop
python -m tests.smoke
```

**Testid**: Põhifunktsionaalsus peamiste näidete jaoks

## Tõrkeotsing

### Teenus ei tööta

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Mooduli importimise vead

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Ühenduse vead

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Mudelit ei leitud

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Keskkonnamuutujate viide

### Põhikonfiguratsioon
| Muutuja | Vaikimisi | Kirjeldus |
|---------|-----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Muutuv | Kasutatav mudeli alias |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Teenuse lõpp-punkti ülekirjutamine |
| `SHOW_USAGE` | `0` | Näita märgi kasutamise statistikat |
| `RETRY_ON_FAIL` | `1` | Luba uuesti proovimise loogika |
| `RETRY_BACKOFF` | `1.0` | Esialgne uuesti proovimise viivitus (sekundites) |

### Sessioonipõhine
| Muutuja | Vaikimisi | Kirjeldus |
|---------|-----------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding mudel |
| `RAG_QUESTION` | Vaata näidet | RAG testküsimus |
| `BENCH_MODELS` | Muutuv | Komaga eraldatud mudelid |
| `BENCH_ROUNDS` | `3` | Võrdlusuuringu iteratsioonid |
| `BENCH_PROMPT` | Vaata näidet | Võrdlusuuringu küsimus |
| `BENCH_STREAM` | `0` | Mõõda esimese märgi latentsust |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Peamine agent mudel |
| `AGENT_MODEL_EDITOR` | Peamine | Toimetaja agent mudel |
| `SLM_ALIAS` | `phi-4-mini` | Väike keelemudel |
| `LLM_ALIAS` | `qwen2.5-7b` | Suur keelemudel |
| `COMPARE_PROMPT` | Vaata näidet | Võrdluse küsimus |

## Soovitatud mudelid

### Arendus ja testimine
- **phi-4-mini** - Tasakaalustatud kvaliteet ja kiirus
- **qwen2.5-0.5b** - Väga kiire klassifikatsiooniks
- **gemma-2-2b** - Hea kvaliteet, mõõdukas kiirus

### Tootmistsenaariumid
- **phi-4-mini** - Üldotstarbeline
- **deepseek-coder-1.3b** - Koodi genereerimine
- **qwen2.5-7b** - Kõrge kvaliteediga vastused

## SDK dokumentatsioon

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Abi saamine

1. Kontrolli teenuse olekut: `foundry service status`  
2. Vaata logisid: Kontrolli Foundry Local teenuse logisid  
3. Vaata SDK dokumentatsiooni: https://github.com/microsoft/Foundry-Local  
4. Vaata näidiskoodi: Kõigil näidetel on üksikasjalikud docstringid  

## Järgmised sammud

1. Täida kõik töötoa sessioonid järjekorras  
2. Katseta erinevaid mudeleid  
3. Kohanda näiteid oma kasutusjuhtude jaoks  

---

**Viimati uuendatud**: 2025-01-08  
**Töötoa versioon**: Viimane  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun olge teadlik, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->