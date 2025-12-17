<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-12-15T20:30:56+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "kn"
}
-->
# ಪರಿಸರ ಸಂರಚನಾ ಮಾರ್ಗದರ್ಶಿ

## ಅವಲೋಕನ

ವರ್ಕ್‌ಶಾಪ್ ಮಾದರಿಗಳು ಸಂರಚನೆಗಾಗಿ ಪರಿಸರ ಚರಗಳನ್ನು ಬಳಸುತ್ತವೆ, ಅವು ಸಂಗ್ರಹಣೆಯ ಮೂಲದಲ್ಲಿ `.env` ಫೈಲ್‌ನಲ್ಲಿ ಕೇಂದ್ರಿತವಾಗಿವೆ. ಇದರಿಂದ ಕೋಡ್ ಬದಲಾಯಿಸದೆ ಸುಲಭವಾಗಿ ಕಸ್ಟಮೈಸ್ ಮಾಡಬಹುದು.

## ತ್ವರಿತ ಪ್ರಾರಂಭ

### 1. ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳನ್ನು ಪರಿಶೀಲಿಸಿ

```bash
# ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಸ್ಥಾಪಿತವಾಗಿದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
foundry --version

# ಸೇವೆ ಚಾಲನೆಯಲ್ಲಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
foundry service status

# ಒಂದು ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ
foundry model run phi-4-mini
```

### 2. ಪರಿಸರವನ್ನು ಸಂರಚಿಸಿ

`.env` ಫೈಲ್ ಈಗಾಗಲೇ ಸೂಕ್ತ ಡೀಫಾಲ್ಟ್‌ಗಳೊಂದಿಗೆ ಸಂರಚಿಸಲಾಗಿದೆ. ಬಹುತೇಕ ಬಳಕೆದಾರರು ಏನನ್ನೂ ಬದಲಾಯಿಸುವ ಅಗತ್ಯವಿಲ್ಲ.

**ಐಚ್ಛಿಕ**: ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಕಸ್ಟಮೈಸ್ ಮಾಡಿ:
```bash
# .env ಫೈಲ್ ಸಂಪಾದಿಸಿ
notepad .env  # ವಿಂಡೋಸ್
nano .env     # ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನ್
```

### 3. ಸಂರಚನೆಯನ್ನು ಅನ್ವಯಿಸಿ

**Python ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳಿಗೆ:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# ಪರಿಸರ ಚರಗಳು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಲೋಡ್ ಮಾಡಲ್ಪಟ್ಟಿವೆ
```

**ನೋಟ್‌ಬುಕ್‌ಗಳಿಗೆ:**
```python
# .env ಬದಲಾವಣೆಗಳ ನಂತರ ಕರ್ಣಲ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ
# ಸೆಲ್‌ಗಳು ಕಾರ್ಯಗತಗೊಳ್ಳುವಾಗ ಚರಗಳು ಲೋಡ್ ಆಗುತ್ತವೆ
```

## ಪರಿಸರ ಚರಗಳ ಉಲ್ಲೇಖ

### ಮೂಲ ಸಂರಚನೆ

| ಚರ | ಡೀಫಾಲ್ಟ್ | ವಿವರಣೆ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | ಮಾದರಿಗಳ ಡೀಫಾಲ್ಟ್ ಮಾದರಿ |
| `FOUNDRY_LOCAL_ENDPOINT` | (ಖಾಲಿ) | ಸೇವಾ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಮೀರಿಸುವುದು |
| `PYTHONPATH` | ವರ್ಕ್‌ಶಾಪ್ ಮಾರ್ಗಗಳು | Python ಮೋಡ್ಯೂಲ್ ಹುಡುಕುವ ಮಾರ್ಗ |

**FOUNDRY_LOCAL_ENDPOINT ಅನ್ನು ಯಾವಾಗ ಸೆಟ್ ಮಾಡಬೇಕು:**
- ರಿಮೋಟ್ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಉದಾಹರಣೆ
- ಕಸ್ಟಮ್ ಪೋರ್ಟ್ ಸಂರಚನೆ
- ಅಭಿವೃದ್ಧಿ/ಉತ್ಪಾದನೆ ವಿಭಜನೆ

**ಉದಾಹರಣೆ:**
```bash
# ಸ್ಥಳೀಯ ಕಸ್ಟಮ್ ಪೋರ್ಟ್
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# ದೂರದ ಉದಾಹರಣೆ
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### ಸೆಷನ್-ನಿರ್ದಿಷ್ಟ ಚರಗಳು

#### ಸೆಷನ್ 02: RAG ಪೈಪ್‌ಲೈನ್
| ಚರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ಎम्बೆಡ್ಡಿಂಗ್ ಮಾದರಿ |
| `RAG_QUESTION` | ಪೂರ್ವ ಸಂರಚಿತ | ಪರೀಕ್ಷಾ ಪ್ರಶ್ನೆ |

#### ಸೆಷನ್ 03: ಬೆಂಚ್‌ಮಾರ್ಕಿಂಗ್
| ಚರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | ಬೆಂಚ್‌ಮಾರ್ಕ್ ಮಾಡಲು ಮಾದರಿಗಳು |
| `BENCH_ROUNDS` | `3` | ಪ್ರತಿ ಮಾದರಿಗಾಗಿ ಪುನರಾವೃತ್ತಿಗಳು |
| `BENCH_PROMPT` | ಪೂರ್ವ ಸಂರಚಿತ | ಪರೀಕ್ಷಾ ಪ್ರಾಂಪ್ಟ್ |
| `BENCH_STREAM` | `0` | ಮೊದಲ ಟೋಕನ್ ವಿಳಂಬವನ್ನು ಅಳೆಯುವುದು |

#### ಸೆಷನ್ 04: ಮಾದರಿ ಹೋಲಿಕೆ
| ಚರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ |
| `LLM_ALIAS` | `qwen2.5-7b` | ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿ |
| `COMPARE_PROMPT` | ಪೂರ್ವ ಸಂರಚಿತ | ಹೋಲಿಕೆ ಪ್ರಾಂಪ್ಟ್ |
| `COMPARE_RETRIES` | `2` | ಮರುಪ್ರಯತ್ನಗಳ ಸಂಖ್ಯೆ |

#### ಸೆಷನ್ 05: ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ
| ಚರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ಸಂಶೋಧಕ ಏಜೆಂಟ್ ಮಾದರಿ |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | ಸಂಪಾದಕ ಏಜೆಂಟ್ ಮಾದರಿ |
| `AGENT_QUESTION` | ಪೂರ್ವ ಸಂರಚಿತ | ಪರೀಕ್ಷಾ ಪ್ರಶ್ನೆ |

### ವಿಶ್ವಾಸಾರ್ಹತೆ ಸಂರಚನೆ

| ಚರ | ಡೀಫಾಲ್ಟ್ | ಉದ್ದೇಶ |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | ಟೋಕನ್ ಬಳಕೆಯನ್ನು ಮುದ್ರಿಸಿ |
| `RETRY_ON_FAIL` | `1` | ಮರುಪ್ರಯತ್ನ ಲಾಜಿಕ್ ಸಕ್ರಿಯಗೊಳಿಸಿ |
| `RETRY_BACKOFF` | `1.0` | ಮರುಪ್ರಯತ್ನ ವಿಳಂಬ (ಸೆಕೆಂಡುಗಳಲ್ಲಿ) |

## ಸಾಮಾನ್ಯ ಸಂರಚನೆಗಳು

### ಅಭಿವೃದ್ಧಿ ಸೆಟ್‌ಅಪ್ (ವೇಗದ ಪುನರಾವೃತ್ತಿ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### ಉತ್ಪಾದನಾ ಸೆಟ್‌ಅಪ್ (ಗುಣಮಟ್ಟದ ಮೇಲೆ ಗಮನ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### ಬೆಂಚ್‌ಮಾರ್ಕಿಂಗ್ ಸೆಟ್‌ಅಪ್
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### ಬಹು-ಏಜೆಂಟ್ ವಿಶೇಷೀಕರಣ
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # ಸಂಶೋಧನೆಗಾಗಿ ವೇಗವಾಗಿ
AGENT_MODEL_EDITOR=qwen2.5-7b         # ಸಂಪಾದನೆಗಾಗಿ ಗುಣಮಟ್ಟ
```

### ರಿಮೋಟ್ ಅಭಿವೃದ್ಧಿ
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## ಶಿಫಾರಸು ಮಾಡಲಾದ ಮಾದರಿಗಳು

### ಬಳಕೆಯ ಪ್ರಕಾರ

**ಸಾಮಾನ್ಯ ಉದ್ದೇಶ:**
- `phi-4-mini` - ಸಮತೋಲನ ಗುಣಮಟ್ಟ ಮತ್ತು ವೇಗ

**ವೇಗದ ಪ್ರತಿಕ್ರಿಯೆಗಳು:**
- `qwen2.5-0.5b` - ಅತ್ಯಂತ ವೇಗವಾಗಿ, ವರ್ಗೀಕರಣಕ್ಕೆ ಉತ್ತಮ
- `phi-4-mini` - ಉತ್ತಮ ಗುಣಮಟ್ಟದೊಂದಿಗೆ ವೇಗ

**ಉನ್ನತ ಗುಣಮಟ್ಟ:**
- `qwen2.5-7b` - ಅತ್ಯುತ್ತಮ ಗುಣಮಟ್ಟ, ಹೆಚ್ಚಿನ ಸಂಪನ್ಮೂಲ ಬಳಕೆ
- `phi-4-mini` - ಉತ್ತಮ ಗುಣಮಟ್ಟ, ಕಡಿಮೆ ಸಂಪನ್ಮೂಲಗಳು

**ಕೋಡ್ ರಚನೆ:**
- `deepseek-coder-1.3b` - ಕೋಡ್‌ಗೆ ವಿಶೇಷೀಕೃತ
- `phi-4-mini` - ಸಾಮಾನ್ಯ ಉದ್ದೇಶದ ಕೋಡಿಂಗ್

### ಸಂಪನ್ಮೂಲ ಲಭ್ಯತೆ ಪ್ರಕಾರ

**ಕಡಿಮೆ ಸಂಪನ್ಮೂಲಗಳು (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**ಮಧ್ಯಮ ಸಂಪನ್ಮೂಲಗಳು (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**ಹೆಚ್ಚು ಸಂಪನ್ಮೂಲಗಳು (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## ಉನ್ನತ ಸಂರಚನೆ

### ಕಸ್ಟಮ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು

```bash
# ಅಭಿವೃದ್ಧಿ ಪರಿಸರ
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# ಸ್ಟೇಜಿಂಗ್ ಪರಿಸರ
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# ಉತ್ಪಾದನಾ ಪರಿಸರ
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### ತಾಪಮಾನ ಮತ್ತು ಸ್ಯಾಂಪ್ಲಿಂಗ್ (ಕೋಡ್‌ನಲ್ಲಿ ಮೀರಿಸುವುದು)

```python
# ನಿಮ್ಮ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು/ನೋಟ್‌ಬುಕ್‌ಗಳಲ್ಲಿ
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### ಅಜೂರ್ ಓಪನ್‌ಎಐ ಹೈಬ್ರಿಡ್ ಸೆಟ್‌ಅಪ್

```bash
# ಅಭಿವೃದ್ಧಿಗಾಗಿ ಸ್ಥಳೀಯವನ್ನು ಬಳಸಿ
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# ಉತ್ಪಾದನೆ ಬ್ಯಾಕ್ಅಪ್‌ಗಾಗಿ ಅಜೂರ್ ಅನ್ನು ಸಂರಚಿಸಿ
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## ಸಮಸ್ಯೆ ಪರಿಹಾರ

### ಪರಿಸರ ಚರಗಳು ಲೋಡ್ ಆಗಿಲ್ಲ

**ಲಕ್ಷಣಗಳು:**
- ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು ತಪ್ಪು ಮಾದರಿಗಳನ್ನು ಬಳಸುತ್ತವೆ
- ಸಂಪರ್ಕ ದೋಷಗಳು
- ಚರಗಳು ಗುರುತಿಸಲ್ಪಡುತ್ತಿಲ್ಲ

**ಪರಿಹಾರಗಳು:**
```bash
# 1. ರೆಪೊಸಿಟರಿ ರೂಟ್‌ನಲ್ಲಿ .env ಇರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ
ls -la .env  # macOS/Linux
dir .env     # ವಿಂಡೋಸ್

# 2. ಫೈಲ್ .env.txt ಅಲ್ಲ ಎಂದು ಪರಿಶೀಲಿಸಿ (ವಿಂಡೋಸ್)
# ಯಾವುದೇ ಗುಪ್ತ ವಿಸ್ತರಣೆ ಇಲ್ಲದಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ

# 3. ನೋಟ್ಬುಕ್‌ಗಳಿಗೆ: ಕರ್ಣಲ್ ಮರುಪ್ರಾರಂಭಿಸಿ
# ಕರ್ಣಲ್ > ಮರುಪ್ರಾರಂಭಿಸಿ

# 4. ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳಿಗೆ: ಕಾರ್ಯನಿರ್ವಹಣಾ ಡೈರೆಕ್ಟರಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
pwd  # ವರ್ಕ್‌ಶಾಪ್ ಅಥವಾ ರೆಪೊಸಿಟರಿ ರೂಟ್‌ನಲ್ಲಿ ಇರಬೇಕು
```

### ಸೇವಾ ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳು

**ಲಕ್ಷಣಗಳು:**
- "ಸಂಪರ್ಕ ನಿರಾಕರಿಸಲಾಗಿದೆ" ದೋಷಗಳು
- "ಸೇವೆಯು ಲಭ್ಯವಿಲ್ಲ"
- ಟೈಮೌಟ್ ದೋಷಗಳು

**ಪರಿಹಾರಗಳು:**
```bash
# 1. ಸೇವೆಯ ಸ್ಥಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ
foundry service status

# 2. ಚಾಲನೆಯಲ್ಲದಿದ್ದರೆ ಪ್ರಾರಂಭಿಸಿ
foundry service start

# 3. ಎಂಡ್‌ಪಾಯಿಂಟ್ ಪರಿಶೀಲಿಸಿ
# ಸ್ಥಿತಿ ಔಟ್‌ಪುಟ್‌ನಲ್ಲಿ ಪೋರ್ಟ್ ಪರಿಶೀಲಿಸಿ
foundry service status | grep "Port"

# 4. ಅಗತ್ಯವಿದ್ದರೆ .env ನವೀಕರಿಸಿ
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### ಮಾದರಿ ಕಂಡುಬರಲಿಲ್ಲ

**ಲಕ್ಷಣಗಳು:**
- "ಮಾದರಿ ಕಂಡುಬರಲಿಲ್ಲ" ದೋಷಗಳು
- "ಅಲಿಯಾಸ್ ಗುರುತಿಸಲ್ಪಡಲಿಲ್ಲ"

**ಪರಿಹಾರಗಳು:**
```bash
# 1. ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
foundry model list

# 2. ಅಗತ್ಯವಿರುವ ಮಾದರಿಯನ್ನು ಲೋಡ್ ಮಾಡಿ
foundry model run phi-4-mini

# 3. ಲಭ್ಯವಿರುವ ಮಾದರಿಯೊಂದಿಗೆ .env ಅನ್ನು ನವೀಕರಿಸಿ
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### ಆಮದು ದೋಷಗಳು

**ಲಕ್ಷಣಗಳು:**
- "ಮೋಡ್ಯೂಲ್ ಕಂಡುಬರಲಿಲ್ಲ" ದೋಷಗಳು

**ಪರಿಹಾರಗಳು:**

```bash
# 1. ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
.venv\Scripts\activate  # ವಿಂಡೋಸ್
source .venv/bin/activate  # ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ

# 2. ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ
pip install -r requirements.txt
```

## ಪರೀಕ್ಷಾ ಸಂರಚನೆ

### ಪರಿಸರ ಲೋಡಿಂಗ್ ಪರಿಶೀಲಿಸಿ

```python
# ಪರೀಕ್ಷಾ_ಪರಿಸರ.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು

### 1. ರಹಸ್ಯಗಳನ್ನು ಎಂದಿಗೂ ಕಮಿಟ್ ಮಾಡಬೇಡಿ

```bash
# .gitignore ನಲ್ಲಿ ಸೇರಿಸಬೇಕು:
.env
.env.local
*.key
```

### 2. ಪ್ರತ್ಯೇಕ .env ಫೈಲ್‌ಗಳನ್ನು ಬಳಸಿ

```bash
.env              # ಡೀಫಾಲ್ಟ್ ಸಂರಚನೆ
.env.local        # ಸ್ಥಳೀಯ ಮೀರಿಕೆಗಳು (ಗಿಟ್ ನಿರ್ಲಕ್ಷಿಸಲಾಗಿದೆ)
.env.production   # ಉತ್ಪಾದನಾ ಸಂರಚನೆ (ಸುರಕ್ಷಿತ ಸಂಗ್ರಹಣೆ)
```

### 3. API ಕೀಗಳನ್ನು ತಿರುಗಿಸಿ

```bash
# ಅಜೂರ್ ಓಪನ್‌ಎಐ ಅಥವಾ ಇತರ ಕ್ಲೌಡ್ ಸೇವೆಗಳಿಗಾಗಿ
# ನಿಯಮಿತವಾಗಿ ಕೀಗಳನ್ನು ಬದಲಾಯಿಸಿ ಮತ್ತು .env ಅನ್ನು ನವೀಕರಿಸಿ
```

### 4. ಪರಿಸರ-ನಿರ್ದಿಷ್ಟ ಸಂರಚನೆಯನ್ನು ಬಳಸಿ

```bash
# ಅಭಿವೃದ್ಧಿ
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# ಉತ್ಪಾದನೆ (ರಹಸ್ಯ ನಿರ್ವಹಣೆಯನ್ನು ಬಳಸಿ)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK ಡಾಕ್ಯುಮೆಂಟೇಶನ್

- **ಮುಖ್ಯ ಸಂಗ್ರಹಣೆ**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API ಡಾಕ್ಯುಮೆಂಟೇಶನ್**: ಇತ್ತೀಚಿನ ಮಾಹಿತಿಗಾಗಿ SDK ಸಂಗ್ರಹಣೆಯನ್ನು ಪರಿಶೀಲಿಸಿ

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- `QUICK_START.md` - ಪ್ರಾರಂಭಿಸುವ ಮಾರ್ಗದರ್ಶಿ
- `Workshop/samples/*/README.md` - ಮಾದರಿ-ನಿರ್ದಿಷ್ಟ ಮಾರ್ಗದರ್ಶಿಗಳು

---

**ಕೊನೆಯದಾಗಿ ನವೀಕರಿಸಲಾಗಿದೆ**: 2025-01-08  
**ಆವೃತ್ತಿ**: 2.0  
**SDK**: ಫೌಂಡ್ರಿ ಲೋಕಲ್ Python SDK (ಇತ್ತೀಚಿನ)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->