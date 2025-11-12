<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T21:27:01+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "de"
}
-->
# Anleitung zur Konfiguration der Umgebung

## Überblick

Die Workshop-Beispiele verwenden Umgebungsvariablen zur Konfiguration, die zentral in der `.env`-Datei im Stammverzeichnis des Repositorys gespeichert sind. Dies ermöglicht eine einfache Anpassung, ohne den Code zu ändern.

## Schnellstart

### 1. Voraussetzungen überprüfen

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Umgebung konfigurieren

Die `.env`-Datei ist bereits mit sinnvollen Standardwerten konfiguriert. Die meisten Benutzer müssen nichts ändern.

**Optional**: Einstellungen überprüfen und anpassen:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Konfiguration anwenden

**Für Python-Skripte:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Für Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referenz der Umgebungsvariablen

### Kernkonfiguration

| Variable | Standardwert | Beschreibung |
|----------|--------------|--------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Standardmodell für Beispiele |
| `FOUNDRY_LOCAL_ENDPOINT` | (leer) | Service-Endpunkt überschreiben |
| `PYTHONPATH` | Workshop-Pfade | Suchpfad für Python-Module |

**Wann `FOUNDRY_LOCAL_ENDPOINT` gesetzt werden sollte:**
- Remote Foundry Local Instanz
- Anpassung der Portkonfiguration
- Trennung von Entwicklung und Produktion

**Beispiel:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Sitzungspezifische Variablen

#### Sitzung 02: RAG-Pipeline
| Variable | Standardwert | Zweck |
|----------|--------------|-------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Embedding-Modell |
| `RAG_QUESTION` | Vorkonfiguriert | Testfrage |

#### Sitzung 03: Benchmarking
| Variable | Standardwert | Zweck |
|----------|--------------|-------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Zu benchmarkende Modelle |
| `BENCH_ROUNDS` | `3` | Iterationen pro Modell |
| `BENCH_PROMPT` | Vorkonfiguriert | Test-Prompt |
| `BENCH_STREAM` | `0` | Latenz des ersten Tokens messen |

#### Sitzung 04: Modellvergleich
| Variable | Standardwert | Zweck |
|----------|--------------|-------|
| `SLM_ALIAS` | `phi-4-mini` | Kleines Sprachmodell |
| `LLM_ALIAS` | `qwen2.5-7b` | Großes Sprachmodell |
| `COMPARE_PROMPT` | Vorkonfiguriert | Vergleichs-Prompt |
| `COMPARE_RETRIES` | `2` | Wiederholungsversuche |

#### Sitzung 05: Multi-Agenten-Orchestrierung
| Variable | Standardwert | Zweck |
|----------|--------------|-------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modell des Forscher-Agenten |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Modell des Editor-Agenten |
| `AGENT_QUESTION` | Vorkonfiguriert | Testfrage |

### Zuverlässigkeitskonfiguration

| Variable | Standardwert | Zweck |
|----------|--------------|-------|
| `SHOW_USAGE` | `1` | Token-Nutzung ausgeben |
| `RETRY_ON_FAIL` | `1` | Wiederholungslogik aktivieren |
| `RETRY_BACKOFF` | `1.0` | Verzögerung bei Wiederholung (Sekunden) |

## Häufige Konfigurationen

### Entwicklungsumgebung (Schnelle Iteration)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Produktionsumgebung (Qualitätsfokus)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Benchmarking-Setup
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Multi-Agenten-Spezialisierung
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Remote-Entwicklung
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Empfohlene Modelle

### Nach Anwendungsfall

**Allgemeiner Zweck:**
- `phi-4-mini` - Ausgewogene Qualität und Geschwindigkeit

**Schnelle Antworten:**
- `qwen2.5-0.5b` - Sehr schnell, gut für Klassifikationen
- `phi-4-mini` - Schnell mit guter Qualität

**Hohe Qualität:**
- `qwen2.5-7b` - Beste Qualität, höherer Ressourcenverbrauch
- `phi-4-mini` - Gute Qualität, geringerer Ressourcenverbrauch

**Code-Generierung:**
- `deepseek-coder-1.3b` - Spezialisiert für Code
- `phi-4-mini` - Allgemeiner Zweck für Coding

### Nach Ressourcenverfügbarkeit

**Wenig Ressourcen (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Mittlere Ressourcen (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Hohe Ressourcen (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Erweiterte Konfiguration

### Benutzerdefinierte Endpunkte

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatur & Sampling (Überschreiben im Code)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI Hybrid-Setup

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Fehlerbehebung

### Umgebungsvariablen nicht geladen

**Symptome:**
- Skripte verwenden falsche Modelle
- Verbindungsfehler
- Variablen werden nicht erkannt

**Lösungen:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Verbindungsprobleme mit dem Service

**Symptome:**
- Fehler "Verbindung verweigert"
- "Service nicht verfügbar"
- Zeitüberschreitungsfehler

**Lösungen:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Modell nicht gefunden

**Symptome:**
- Fehler "Modell nicht gefunden"
- "Alias nicht erkannt"

**Lösungen:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Importfehler

**Symptome:**
- Fehler "Modul nicht gefunden"

**Lösungen:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Konfiguration testen

### Überprüfen des Ladens der Umgebung

```python
# test_env.py
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

### Verbindung zu Foundry Local testen

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

## Sicherheitsbest-Practices

### 1. Geheimnisse niemals committen

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Separate .env-Dateien verwenden

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API-Schlüssel regelmäßig rotieren

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Umgebungsspezifische Konfiguration verwenden

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK-Dokumentation

- **Haupt-Repository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-Dokumentation**: Siehe SDK-Repository für die neuesten Informationen

## Zusätzliche Ressourcen

- `QUICK_START.md` - Schnellstart-Anleitung
- `Workshop/samples/*/README.md` - Beispiel-spezifische Anleitungen

---

**Letzte Aktualisierung**: 08.01.2025  
**Version**: 2.0  
**SDK**: Foundry Local Python SDK (neueste Version)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->