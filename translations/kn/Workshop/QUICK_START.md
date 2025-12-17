<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-12-15T20:34:53+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "kn"
}
-->
# ಕಾರ್ಯಾಗಾರ ತ್ವರಿತ ಪ್ರಾರಂಭ ಮಾರ್ಗದರ್ಶಿ

## ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

### 1. ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ

ಅಧಿಕೃತ ಸ್ಥಾಪನಾ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಅನುಸರಿಸಿ:  
https://github.com/microsoft/Foundry-Local

```bash
# ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಸೇವೆಯನ್ನು ಪ್ರಾರಂಭಿಸಿ
foundry service start

# ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ (ಕಾರ್ಯಾಗಾರದಿಗಾಗಿ phi-4-mini ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)
foundry model run phi-4-mini

# ಸೇವೆ ಚಾಲನೆಯಲ್ಲಿ ಇದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
foundry service status
```

### 2. ಪೈಥಾನ್ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

ಕಾರ್ಯಾಗಾರ ಡೈರೆಕ್ಟರಿಯಿಂದ:

```bash
# ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)
python -m venv .venv

# ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
# ವಿಂಡೋಸ್:
.venv\Scripts\activate
# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನಲ್ಲಿ:
source .venv/bin/activate

# ಅಗತ್ಯಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
pip install -r requirements.txt
```

## ಕಾರ್ಯಾಗಾರ ಮಾದರಿಗಳನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

### ಸೆಷನ್ 01: ಮೂಲ ಚಾಟ್

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**ಪರಿಸರ ಚರಗಳು:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### ಸೆಷನ್ 02: RAG ಪೈಪ್ಲೈನ್

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**ಪರಿಸರ ಚರಗಳು:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### ಸೆಷನ್ 02: RAG ಮೌಲ್ಯಮಾಪನ (ರಾಗಾಸ್)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**ಗಮನಿಸಿ**: `requirements.txt` ಮೂಲಕ ಹೆಚ್ಚುವರಿ ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸುವ ಅಗತ್ಯವಿದೆ

### ಸೆಷನ್ 03: ಬೆಂಚ್ಮಾರ್ಕಿಂಗ್

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**ಪರಿಸರ ಚರಗಳು:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**ಫಲಿತಾಂಶ**: ವಿಳಂಬ, ಥ್ರೂಪುಟ್ ಮತ್ತು ಮೊದಲ ಟೋಕನ್ ಮೆಟ್ರಿಕ್ಸ್ ಹೊಂದಿರುವ JSON

### ಸೆಷನ್ 04: ಮಾದರಿ ಹೋಲಿಕೆ

```bash
cd Workshop/samples
python -m session04.model_compare
```

**ಪರಿಸರ ಚರಗಳು:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### ಸೆಷನ್ 05: ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**ಪರಿಸರ ಚರಗಳು:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### ಸೆಷನ್ 06: ಮಾದರಿ ರೌಟರ್

```bash
cd Workshop/samples
python -m session06.models_router
```

**ಪರೀಕ್ಷೆಗಳು**: ಬಹು ಉದ್ದೇಶಗಳ (ಕೋಡ್, ಸಾರಾಂಶ, ವರ್ಗೀಕರಣ) ರೌಟಿಂಗ್ ಲಾಜಿಕ್ ಪರೀಕ್ಷೆ

### ಸೆಷನ್ 06: ಪೈಪ್ಲೈನ್

```bash
python -m session06.models_pipeline
```

**ಸಂಕೀರ್ಣ ಬಹು ಹಂತದ ಪೈಪ್ಲೈನ್** ಯೋಜನೆ, ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಮತ್ತು ಪರಿಷ್ಕರಣೆ ಸಹಿತ

## ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು

### ಬೆಂಚ್ಮಾರ್ಕ್ ವರದಿ ರಫ್ತು

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**ಫಲಿತಾಂಶ**: ಮಾರ್ಕ್‌ಡೌನ್ ಟೇಬಲ್ + JSON ಮೆಟ್ರಿಕ್ಸ್

### ಮಾರ್ಕ್‌ಡೌನ್ CLI ಮಾದರಿಗಳನ್ನು ಲಿಂಟ್ ಮಾಡಿ

```bash
python lint_markdown_cli.py --verbose
```

**ಉದ್ದೇಶ**: ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ನಲ್ಲಿ ಹಳೆಯ CLI ಮಾದರಿಗಳನ್ನು ಪತ್ತೆಮಾಡುವುದು

## ಪರೀಕ್ಷೆ

### ಸ್ಮೋಕ್ ಪರೀಕ್ಷೆಗಳು

```bash
cd Workshop
python -m tests.smoke
```

**ಪರೀಕ್ಷೆಗಳು**: ಪ್ರಮುಖ ಮಾದರಿಗಳ ಮೂಲ ಕಾರ್ಯಕ್ಷಮತೆ

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಸೇವೆ ಚಾಲನೆಯಲ್ಲಿಲ್ಲ

```bash
# ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
foundry service status

# ಚಾಲನೆಯಲ್ಲದಿದ್ದರೆ ಪ್ರಾರಂಭಿಸಿ
foundry service start

# ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ
foundry model run phi-4-mini
```

### ಮೋಡ್ಯೂಲ್ ಆಮದು ದೋಷಗಳು

```bash
# ವರ್ಚುವಲ್ ಪರಿಸರ ಸಕ್ರಿಯವಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
.venv\Scripts\activate  # ವಿಂಡೋಸ್
source .venv/bin/activate  # ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ

# ಅವಲಂಬನೆಗಳನ್ನು ಮರುಸ್ಥಾಪಿಸಿ
pip install -r requirements.txt
```

### ಸಂಪರ್ಕ ದೋಷಗಳು

```bash
# ಎಂಡ್‌ಪಾಯಿಂಟ್ ಪರಿಶೀಲಿಸಿ
foundry service status

# ಅಗತ್ಯವಿದ್ದರೆ ಸ್ಪಷ್ಟ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಹೊಂದಿಸಿ
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### ಮಾದರಿ ಕಂಡುಬರಲಿಲ್ಲ

```bash
# ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
foundry model list

# ಮಾದರಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ಚಾಲನೆ ಮಾಡಿ
foundry model run phi-4-mini
```

## ಪರಿಸರ ಚರಗಳ ಉಲ್ಲೇಖ

### ಕೋರ್ ಸಂರಚನೆ
| ಚರ | ಡೀಫಾಲ್ಟ್ | ವಿವರಣೆ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | ಬದಲಾಗುತ್ತದೆ | ಬಳಸುವ ಮಾದರಿ ಅಲಿಯಾಸ್ |
| `FOUNDRY_LOCAL_ENDPOINT` | ಸ್ವಯಂಚಾಲಿತ | ಸೇವೆ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮೀರಿಸುವಿಕೆ |
| `SHOW_USAGE` | `0` | ಟೋಕನ್ ಬಳಕೆ ಅಂಕಿಅಂಶಗಳನ್ನು ತೋರಿಸಿ |
| `RETRY_ON_FAIL` | `1` | ಮರುಪ್ರಯತ್ನ ಲಾಜಿಕ್ ಸಕ್ರಿಯಗೊಳಿಸಿ |
| `RETRY_BACKOFF` | `1.0` | ಪ್ರಾಥಮಿಕ ಮರುಪ್ರಯತ್ನ ವಿಳಂಬ (ಸೆಕೆಂಡುಗಳು) |

### ಸೆಷನ್-ನಿರ್ದಿಷ್ಟ
| ಚರ | ಡೀಫಾಲ್ಟ್ | ವಿವರಣೆ |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ಎम्बೆಡ್ಡಿಂಗ್ ಮಾದರಿ |
| `RAG_QUESTION` | ಮಾದರಿ ನೋಡಿ | RAG ಪರೀಕ್ಷಾ ಪ್ರಶ್ನೆ |
| `BENCH_MODELS` | ಬದಲಾಗುತ್ತದೆ | ಕಾಮಾ ವಿಭಜಿತ ಮಾದರಿಗಳು |
| `BENCH_ROUNDS` | `3` | ಬೆಂಚ್ಮಾರ್ಕ್ ಪುನರಾವೃತ್ತಿಗಳು |
| `BENCH_PROMPT` | ಮಾದರಿ ನೋಡಿ | ಬೆಂಚ್ಮಾರ್ಕ್ ಪ್ರಾಂಪ್ಟ್ |
| `BENCH_STREAM` | `0` | ಮೊದಲ ಟೋಕನ್ ವಿಳಂಬವನ್ನು ಅಳೆಯಿರಿ |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ಪ್ರಾಥಮಿಕ ಏಜೆಂಟ್ ಮಾದರಿ |
| `AGENT_MODEL_EDITOR` | ಪ್ರಾಥಮಿಕ | ಸಂಪಾದಕ ಏಜೆಂಟ್ ಮಾದರಿ |
| `SLM_ALIAS` | `phi-4-mini` | ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ |
| `LLM_ALIAS` | `qwen2.5-7b` | ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿ |
| `COMPARE_PROMPT` | ಮಾದರಿ ನೋಡಿ | ಹೋಲಿಕೆ ಪ್ರಾಂಪ್ಟ್ |

## ಶಿಫಾರಸು ಮಾಡಲಾದ ಮಾದರಿಗಳು

### ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಪರೀಕ್ಷೆ
- **phi-4-mini** - ಸಮತೋಲನ ಗುಣಮಟ್ಟ ಮತ್ತು ವೇಗ
- **qwen2.5-0.5b** - ವರ್ಗೀಕರಣಕ್ಕೆ ಅತ್ಯಂತ ವೇಗವಾಗಿ
- **gemma-2-2b** - ಉತ್ತಮ ಗುಣಮಟ್ಟ, ಮಧ್ಯಮ ವೇಗ

### ಉತ್ಪಾದನಾ ಸಂದರ್ಭಗಳು
- **phi-4-mini** - ಸಾಮಾನ್ಯ ಉದ್ದೇಶ
- **deepseek-coder-1.3b** - ಕೋಡ್ ಉತ್ಪಾದನೆ
- **qwen2.5-7b** - ಉನ್ನತ ಗುಣಮಟ್ಟದ ಪ್ರತಿಕ್ರಿಯೆಗಳು

## SDK ಡಾಕ್ಯುಮೆಂಟೇಶನ್

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## ಸಹಾಯ ಪಡೆಯುವುದು

1. ಸೇವೆ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ: `foundry service status`  
2. ಲಾಗ್‌ಗಳನ್ನು ವೀಕ್ಷಿಸಿ: Foundry Local ಸೇವೆ ಲಾಗ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ  
3. SDK ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ: https://github.com/microsoft/Foundry-Local  
4. ಮಾದರಿ ಕೋಡ್ ಪರಿಶೀಲಿಸಿ: ಎಲ್ಲಾ ಮಾದರಿಗಳಿಗೆ ವಿವರವಾದ ಡಾಕ್‌ಸ್ಟ್ರಿಂಗ್‌ಗಳಿವೆ

## ಮುಂದಿನ ಹಂತಗಳು

1. ಎಲ್ಲಾ ಕಾರ್ಯಾಗಾರ ಸೆಷನ್‌ಗಳನ್ನು ಕ್ರಮವಾಗಿ ಪೂರ್ಣಗೊಳಿಸಿ  
2. ವಿಭಿನ್ನ ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರಯೋಗ ಮಾಡಿ  
3. ನಿಮ್ಮ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಮಾದರಿಗಳನ್ನು ತಿದ್ದುಪಡಿ ಮಾಡಿ

---

**ಕೊನೆಯದಾಗಿ ನವೀಕರಿಸಲಾಗಿದೆ**: 2025-01-08  
**ಕಾರ್ಯಾಗಾರ ಆವೃತ್ತಿ**: ಇತ್ತೀಚಿನದು  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->