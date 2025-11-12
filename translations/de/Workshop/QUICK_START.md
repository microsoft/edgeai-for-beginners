<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eee296ca63673b7520d15942f6a01826",
  "translation_date": "2025-11-11T21:25:59+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "de"
}
-->
# Workshop Schnellstartanleitung

## Voraussetzungen

### 1. Foundry Local installieren

Folgen Sie der offiziellen Installationsanleitung:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python-Abhängigkeiten installieren

Aus dem Workshop-Verzeichnis:

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

## Workshop-Beispiele ausführen

### Sitzung 01: Basis-Chat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Umgebungsvariablen:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sitzung 02: RAG-Pipeline

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Umgebungsvariablen:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sitzung 02: RAG-Auswertung (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Hinweis**: Erfordert zusätzliche Abhängigkeiten, die über `requirements.txt` installiert werden.

### Sitzung 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Umgebungsvariablen:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Ausgabe**: JSON mit Latenz-, Durchsatz- und First-Token-Metriken

### Sitzung 04: Modellvergleich

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Umgebungsvariablen:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sitzung 05: Multi-Agent-Orchestrierung

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Umgebungsvariablen:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sitzung 06: Modell-Router

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testet Routing-Logik** mit mehreren Intentionen (Code, Zusammenfassung, Klassifikation)

### Sitzung 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Komplexe mehrstufige Pipeline** mit Planung, Ausführung und Verfeinerung

## Skripte

### Benchmark-Bericht exportieren

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Ausgabe**: Markdown-Tabelle + JSON-Metriken

### Markdown CLI-Muster prüfen

```bash
python lint_markdown_cli.py --verbose
```

**Zweck**: Veraltete CLI-Muster in der Dokumentation erkennen

## Tests

### Smoke-Tests

```bash
cd Workshop
python -m tests.smoke
```

**Tests**: Grundlegende Funktionalität der wichtigsten Beispiele

## Fehlerbehebung

### Dienst läuft nicht

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Modul-Importfehler

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Verbindungsfehler

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modell nicht gefunden

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referenz für Umgebungsvariablen

### Kernkonfiguration
| Variable | Standardwert | Beschreibung |
|----------|--------------|--------------|
| `FOUNDRY_LOCAL_ALIAS` | Variiert | Zu verwendender Modellalias |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Dienst-Endpunkt überschreiben |
| `SHOW_USAGE` | `0` | Token-Nutzungsstatistiken anzeigen |
| `RETRY_ON_FAIL` | `1` | Wiederholungslogik aktivieren |
| `RETRY_BACKOFF` | `1.0` | Anfangsverzögerung für Wiederholungen (Sekunden) |

### Sitzungsbezogen
| Variable | Standardwert | Beschreibung |
|----------|--------------|--------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Einbettungsmodell |
| `RAG_QUESTION` | Siehe Beispiel | RAG-Testfrage |
| `BENCH_MODELS` | Variiert | Kommagetrennte Modelle |
| `BENCH_ROUNDS` | `3` | Benchmark-Wiederholungen |
| `BENCH_PROMPT` | Siehe Beispiel | Benchmark-Prompt |
| `BENCH_STREAM` | `0` | Latenz des ersten Tokens messen |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Primäres Agentenmodell |
| `AGENT_MODEL_EDITOR` | Primär | Editor-Agentenmodell |
| `SLM_ALIAS` | `phi-4-mini` | Kleines Sprachmodell |
| `LLM_ALIAS` | `qwen2.5-7b` | Großes Sprachmodell |
| `COMPARE_PROMPT` | Siehe Beispiel | Vergleichs-Prompt |

## Empfohlene Modelle

### Entwicklung & Tests
- **phi-4-mini** - Ausgewogene Qualität und Geschwindigkeit
- **qwen2.5-0.5b** - Sehr schnell für Klassifikation
- **gemma-2-2b** - Gute Qualität, moderate Geschwindigkeit

### Produktionsszenarien
- **phi-4-mini** - Allgemeiner Zweck
- **deepseek-coder-1.3b** - Code-Generierung
- **qwen2.5-7b** - Hochwertige Antworten

## SDK-Dokumentation

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Hilfe erhalten

1. Dienststatus prüfen: `foundry service status`  
2. Protokolle anzeigen: Foundry Local-Dienstprotokolle prüfen  
3. SDK-Dokumentation prüfen: https://github.com/microsoft/Foundry-Local  
4. Beispielcode überprüfen: Alle Beispiele enthalten ausführliche Docstrings  

## Nächste Schritte

1. Alle Workshop-Sitzungen der Reihe nach abschließen  
2. Mit verschiedenen Modellen experimentieren  
3. Beispiele für Ihre Anwendungsfälle anpassen  

---

**Letzte Aktualisierung**: 08.01.2025  
**Workshop-Version**: Aktuell  
**SDK**: Foundry Local Python SDK  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->