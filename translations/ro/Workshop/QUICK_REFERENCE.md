<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4b84b08208b791e7822f88127e498f5",
  "translation_date": "2025-11-12T00:21:06+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ro"
}
-->
# Mostre Workshop - Carte de Referință Rapidă

**Ultima actualizare**: 8 octombrie 2025

---

## 🚀 Start Rapid

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Prezentare Generală a Mostrelor

| Sesiune | Mostră | Scop | Timp |
|---------|--------|------|------|
| 01 | `chat_bootstrap.py` | Chat de bază + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG cu embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Evaluare RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Benchmarking modele | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Sistem multi-agent | ~60s |
| 06 | `models_router.py` | Rutare intenții | ~45s |
| 06 | `models_pipeline.py` | Pipeline multi-pas | ~60s |

---

## 🛠️ Variabile de Mediu

### Esențiale
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Specifice Sesiunii
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Validare & Testare

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Depanare

### Eroare de Conexiune
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Eroare de Import
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modelul Nu a Fost Găsit
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Performanță Lentă
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Modele Comune

### Chat de Bază
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Obține Client
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Gestionarea Erorilor
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Selectarea Modelului

| Model | Dimensiune | Cel Mai Bun Pentru | Viteză |
|-------|------------|--------------------|-------|
| `qwen2.5-0.5b` | 0.5B | Clasificare rapidă | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Generare rapidă de cod | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Scriere creativă | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Cod, refactorizare | ⚡⚡ |
| `phi-4-mini` | 4B | General, sumarizare | ⚡⚡ |
| `qwen2.5-7b` | 7B | Raționament complex | ⚡ |

---

## 🔗 Resurse

- **Documentație SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referință Rapidă**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Sfaturi

1. **Cache pentru clienți**: `workshop_utils` face caching pentru tine
2. **Folosește modele mai mici**: Începe cu `qwen2.5-0.5b` pentru testare
3. **Activează statistici de utilizare**: Setează `SHOW_USAGE=1` pentru a urmări token-urile
4. **Procesare în loturi**: Procesează mai multe prompturi secvențial
5. **Redu max_tokens**: Scade latența pentru răspunsuri rapide

---

## 🎯 Fluxuri de Lucru Mostre

### Testează Tot
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmarking Modele
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### Pipeline RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Sistem Multi-Agent
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Ajutor Rapid**: Rulează orice mostră cu `--help` din directorul `samples` sau verifică docstring-ul:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Toate mostrele actualizate în octombrie 2025 cu cele mai bune practici Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->