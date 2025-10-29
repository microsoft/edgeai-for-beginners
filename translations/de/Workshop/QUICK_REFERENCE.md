<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:12:03+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "de"
}
-->
# Workshop-Beispiele - Schnellreferenzkarte

**Letzte Aktualisierung**: 8. Oktober 2025

---

## 🚀 Schnellstart

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

## 📂 Überblick über die Beispiele

| Sitzung | Beispiel | Zweck | Zeit |
|---------|----------|-------|------|
| 01 | `chat_bootstrap.py` | Basis-Chat + Streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG mit Embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | RAG-Auswertung | ~60s |
| 03 | `benchmark_oss_models.py` | Modell-Benchmarking | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Multi-Agent-System | ~60s |
| 06 | `models_router.py` | Intent-Routing | ~45s |
| 06 | `models_pipeline.py` | Mehrstufige Pipeline | ~60s |

---

## 🛠️ Umgebungsvariablen

### Wesentlich
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Sitzungs-spezifisch
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

## ✅ Validierung & Tests

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

## 🐛 Fehlerbehebung

### Verbindungsfehler
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Importfehler
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modell nicht gefunden
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Langsame Leistung
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Häufige Muster

### Basis-Chat
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Client abrufen
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Fehlerbehandlung
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

## 📊 Modellauswahl

| Modell | Größe | Am besten geeignet für | Geschwindigkeit |
|--------|-------|-------------------------|-----------------|
| `qwen2.5-0.5b` | 0.5B | Schnelle Klassifikation | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Schnelle Code-Generierung | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Kreatives Schreiben | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Code, Refactoring | ⚡⚡ |
| `phi-4-mini` | 4B | Allgemein, Zusammenfassung | ⚡⚡ |
| `qwen2.5-7b` | 7B | Komplexes Denken | ⚡ |

---

## 🔗 Ressourcen

- **SDK-Dokumentation**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Schnellreferenz**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Update-Zusammenfassung**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **Migrationshinweise**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 Tipps

1. **Clients cachen**: `workshop_utils` übernimmt das Caching für Sie
2. **Kleinere Modelle verwenden**: Beginnen Sie mit `qwen2.5-0.5b` für Tests
3. **Nutzungsstatistiken aktivieren**: Setzen Sie `SHOW_USAGE=1`, um Token zu verfolgen
4. **Batch-Verarbeitung**: Mehrere Prompts nacheinander verarbeiten
5. **Max_tokens reduzieren**: Verringert die Latenz für schnelle Antworten

---

## 🎯 Beispiel-Workflows

### Alles testen
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Modelle benchmarken
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG-Pipeline
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Multi-Agent-System
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Schnelle Hilfe**: Führen Sie ein beliebiges Beispiel mit `--help` aus dem Verzeichnis `samples` aus oder sehen Sie sich die docstring an:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Alle Beispiele wurden im Oktober 2025 mit den Best Practices des Foundry Local SDK aktualisiert** ✨

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.