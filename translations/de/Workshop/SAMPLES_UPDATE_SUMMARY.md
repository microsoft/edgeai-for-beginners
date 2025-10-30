<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:12:12+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "de"
}
-->
# Workshop-Beispiele - Zusammenfassung der Aktualisierung des Foundry Local SDK

## Überblick

Alle Python-Beispiele im Verzeichnis `Workshop/samples` wurden aktualisiert, um den Best Practices des Foundry Local SDK zu entsprechen und die Konsistenz im gesamten Workshop sicherzustellen.

**Datum**: 8. Oktober 2025  
**Umfang**: 9 Python-Dateien über 6 Workshop-Sitzungen  
**Hauptfokus**: Fehlerbehandlung, Dokumentation, SDK-Muster, Benutzererfahrung

---

## Aktualisierte Dateien

### Sitzung 01: Erste Schritte
- ✅ `chat_bootstrap.py` - Grundlegende Chat- und Streaming-Beispiele

### Sitzung 02: RAG-Lösungen
- ✅ `rag_pipeline.py` - RAG-Implementierung mit Embeddings
- ✅ `rag_eval_ragas.py` - RAG-Auswertung mit RAGAS-Metriken

### Sitzung 03: Open-Source-Modelle
- ✅ `benchmark_oss_models.py` - Benchmarking mehrerer Modelle

### Sitzung 04: Spitzenmodelle
- ✅ `model_compare.py` - Vergleich von SLM und LLM

### Sitzung 05: KI-gestützte Agenten
- ✅ `agents_orchestrator.py` - Koordination mehrerer Agenten

### Sitzung 06: Modelle als Werkzeuge
- ✅ `models_router.py` - Intent-basierte Modellweiterleitung
- ✅ `models_pipeline.py` - Mehrstufige Pipeline mit Weiterleitung

### Unterstützende Infrastruktur
- ✅ `workshop_utils.py` - Bereits nach Best Practices implementiert (keine Änderungen erforderlich)

---

## Wichtige Verbesserungen

### 1. Verbesserte Fehlerbehandlung

**Vorher:**
```python
manager, client, model_id = get_client(alias)
```

**Nachher:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Vorteile:**
- Elegante Fehlerbehandlung mit klaren Fehlermeldungen
- Umsetzbare Hinweise zur Fehlerbehebung
- Korrekte Exit-Codes für Skripte

### 2. Besseres Import-Management

**Vorher:**
```python
from sentence_transformers import SentenceTransformer
```

**Nachher:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Vorteile:**
- Klare Hinweise bei fehlenden Abhängigkeiten
- Vermeidung kryptischer Importfehler
- Benutzerfreundliche Installationsanweisungen

### 3. Umfassende Dokumentation

**Hinzugefügt zu allen Beispielen:**
- Dokumentation von Umgebungsvariablen in Docstrings
- Links zu SDK-Referenzen
- Anwendungsbeispiele
- Detaillierte Funktions-/Parameterdokumentation
- Typ-Hinweise für bessere IDE-Unterstützung

**Beispiel:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Verbesserte Benutzer-Rückmeldungen

**Informative Protokollierung hinzugefügt:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Fortschrittsanzeigen:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturierte Ausgabe:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Robustes Benchmarking

**Verbesserungen in Sitzung 03:**
- Fehlerbehandlung pro Modell (Fortsetzung bei Fehlern)
- Detaillierte Fortschrittsberichte
- Warmup-Runden korrekt ausgeführt
- Unterstützung für die Messung der Latenz des ersten Tokens
- Klare Trennung der Phasen

### 6. Konsistente Typ-Hinweise

**Überall hinzugefügt:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Vorteile:**
- Bessere Autovervollständigung in der IDE
- Früherkennung von Fehlern
- Selbstdokumentierender Code

### 7. Verbesserte Modellweiterleitung

**Verbesserungen in Sitzung 06:**
- Umfassende Dokumentation zur Intent-Erkennung
- Erklärung des Modell-Auswahlalgorithmus
- Detaillierte Weiterleitungsprotokolle
- Formatierung der Testausgabe
- Fehlerbehebung bei Batch-Tests

### 8. Multi-Agenten-Orchestrierung

**Verbesserungen in Sitzung 05:**
- Fortschrittsberichte für jede Phase
- Fehlerbehandlung pro Agent
- Klare Pipeline-Struktur
- Verbesserte Dokumentation zum Speicher-Management

---

## Test-Checkliste

### Voraussetzungen
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testen Sie jedes Beispiel

#### Sitzung 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sitzung 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sitzung 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sitzung 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sitzung 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sitzung 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referenz für Umgebungsvariablen

### Global (Alle Beispiele)
| Variable | Beschreibung | Standard |
|----------|--------------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Zu verwendender Modellalias | Variiert je nach Beispiel |
| `FOUNDRY_LOCAL_ENDPOINT` | Service-Endpunkt überschreiben | Automatisch erkannt |
| `SHOW_USAGE` | Token-Nutzung anzeigen | `0` |
| `RETRY_ON_FAIL` | Wiederholungslogik aktivieren | `1` |
| `RETRY_BACKOFF` | Anfangsverzögerung für Wiederholungen | `1.0` |

### Beispiel-spezifisch
| Variable | Verwendet von | Beschreibung |
|----------|---------------|--------------|
| `EMBED_MODEL` | Sitzung 02 | Name des Embedding-Modells |
| `RAG_QUESTION` | Sitzung 02 | Testfrage für RAG |
| `BENCH_MODELS` | Sitzung 03 | Komma-separierte Modelle für Benchmarking |
| `BENCH_ROUNDS` | Sitzung 03 | Anzahl der Benchmark-Runden |
| `BENCH_PROMPT` | Sitzung 03 | Test-Prompt für Benchmarks |
| `BENCH_STREAM` | Sitzung 03 | Latenz des ersten Tokens messen |
| `SLM_ALIAS` | Sitzung 04 | Kleines Sprachmodell |
| `LLM_ALIAS` | Sitzung 04 | Großes Sprachmodell |
| `COMPARE_PROMPT` | Sitzung 04 | Vergleichs-Test-Prompt |
| `AGENT_MODEL_PRIMARY` | Sitzung 05 | Primäres Agentenmodell |
| `AGENT_MODEL_EDITOR` | Sitzung 05 | Editor-Agentenmodell |
| `AGENT_QUESTION` | Sitzung 05 | Testfrage für Agenten |
| `PIPELINE_TASK` | Sitzung 06 | Aufgabe für die Pipeline |

---

## Breaking Changes

**Keine** - Alle Änderungen sind rückwärtskompatibel.

Bestehende Skripte funktionieren weiterhin. Neue Funktionen sind:
- Optionale Umgebungsvariablen
- Verbesserte Fehlermeldungen (brechen die Funktionalität nicht)
- Zusätzliche Protokollierung (kann unterdrückt werden)
- Bessere Typ-Hinweise (keine Auswirkungen zur Laufzeit)

---

## Implementierte Best Practices

### 1. Immer Workshop Utils verwenden
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Richtiges Fehlerbehandlungsmuster
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informative Protokollierung
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Typ-Hinweise
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Umfassende Docstrings
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Unterstützung für Umgebungsvariablen
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Sanfte Degradierung
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Häufige Probleme & Lösungen

### Problem: Importfehler
**Lösung:** Fehlende Abhängigkeiten installieren
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problem: Verbindungsfehler
**Lösung:** Sicherstellen, dass Foundry Local läuft
```bash
foundry service status
foundry model run phi-4-mini
```

### Problem: Modell nicht gefunden
**Lösung:** Verfügbare Modelle überprüfen
```bash
foundry model ls
foundry model download <alias>
```

### Problem: Langsame Leistung
**Lösung:** Kleinere Modelle verwenden oder Parameter anpassen
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Nächste Schritte

### 1. Testen Sie alle Beispiele
Gehen Sie die oben stehende Test-Checkliste durch, um sicherzustellen, dass alle Beispiele korrekt funktionieren.

### 2. Dokumentation aktualisieren
- Aktualisieren Sie die Markdown-Dateien der Sitzungen mit neuen Beispielen
- Fügen Sie der Haupt-README eine Fehlerbehebungssektion hinzu
- Erstellen Sie eine Schnellreferenz

### 3. Integrationstests erstellen
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Leistungsbenchmarks hinzufügen
Verfolgen Sie Leistungsverbesserungen durch die Verbesserungen der Fehlerbehandlung.

### 5. Benutzerfeedback
Sammeln Sie Feedback von Workshop-Teilnehmern zu:
- Klarheit der Fehlermeldungen
- Vollständigkeit der Dokumentation
- Benutzerfreundlichkeit

---

## Ressourcen

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Schnellreferenz**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Migrationshinweise**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Hauptrepository**: https://github.com/microsoft/Foundry-Local

---

## Wartung

### Neue Beispiele hinzufügen
Befolgen Sie diese Muster beim Erstellen neuer Beispiele:

1. Verwenden Sie `workshop_utils` für die Verwaltung des Clients
2. Fügen Sie umfassende Fehlerbehandlung hinzu
3. Unterstützen Sie Umgebungsvariablen
4. Fügen Sie Typ-Hinweise und Docstrings hinzu
5. Stellen Sie informative Protokollierung bereit
6. Fügen Sie Anwendungsbeispiele in den Docstrings hinzu
7. Verlinken Sie zur SDK-Dokumentation

### Updates überprüfen
Überprüfen Sie bei der Durchsicht von Beispiel-Updates Folgendes:
- [ ] Fehlerbehandlung bei allen I/O-Operationen
- [ ] Typ-Hinweise bei öffentlichen Funktionen
- [ ] Umfassende Docstrings
- [ ] Dokumentation der Umgebungsvariablen
- [ ] Informative Benutzer-Rückmeldungen
- [ ] Links zu SDK-Referenzen
- [ ] Konsistenter Programmierstil

---

**Zusammenfassung**: Alle Python-Beispiele des Workshops folgen nun den Best Practices des Foundry Local SDK mit verbesserter Fehlerbehandlung, umfassender Dokumentation und optimierter Benutzererfahrung. Keine Breaking Changes - alle bestehenden Funktionen bleiben erhalten und wurden verbessert.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.