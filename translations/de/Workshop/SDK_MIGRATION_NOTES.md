<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:12:28+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "de"
}
-->
# Foundry Local SDK Migrationshinweise

## Überblick

Alle Python-Dateien im Workshop-Ordner wurden aktualisiert, um den neuesten Mustern des offiziellen [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) zu folgen.

## Zusammenfassung der Änderungen

### Kerninfrastruktur (`workshop_utils.py`)

#### Verbesserte Funktionen:
- **Unterstützung für Endpoint-Override**: Unterstützung der Umgebungsvariable `FOUNDRY_LOCAL_ENDPOINT` hinzugefügt
- **Verbesserte Fehlerbehandlung**: Bessere Ausnahmebehandlung mit detaillierten Fehlermeldungen
- **Erweiterte Zwischenspeicherung**: Cache-Schlüssel beinhalten jetzt den Endpoint für Szenarien mit mehreren Endpoints
- **Exponentielles Backoff**: Die Wiederholungslogik verwendet jetzt exponentielles Backoff für bessere Zuverlässigkeit
- **Typannotationen**: Umfassende Typ-Hinweise für bessere IDE-Unterstützung hinzugefügt

#### Neue Funktionen:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Beispielanwendungen

#### Sitzung 01: Chat Bootstrap (`chat_bootstrap.py`)
- Standardmodell von `phi-3.5-mini` auf `phi-4-mini` aktualisiert
- Unterstützung für Endpoint-Override hinzugefügt
- Dokumentation mit SDK-Referenzen verbessert

#### Sitzung 02: RAG-Pipeline (`rag_pipeline.py`)
- Aktualisiert, um `phi-4-mini` als Standard zu verwenden
- Unterstützung für Endpoint-Override hinzugefügt
- Dokumentation mit Details zu Umgebungsvariablen verbessert

#### Sitzung 02: RAG-Evaluierung (`rag_eval_ragas.py`)
- Standardmodelle aktualisiert
- Endpoint-Konfiguration hinzugefügt
- Fehlerbehandlung verbessert

#### Sitzung 03: Benchmarking (`benchmark_oss_models.py`)
- Standardmodellliste aktualisiert, um `phi-4-mini` einzuschließen
- Umfassende Dokumentation zu Umgebungsvariablen hinzugefügt
- Funktionsdokumentation verbessert
- Unterstützung für Endpoint-Override durchgehend hinzugefügt

#### Sitzung 04: Modellvergleich (`model_compare.py`)
- Standard-LLM von `gpt-oss-20b` auf `qwen2.5-7b` aktualisiert
- Endpoint-Konfiguration hinzugefügt
- Dokumentation verbessert

#### Sitzung 05: Multi-Agent-Orchestrierung (`agents_orchestrator.py`)
- Typ-Hinweise hinzugefügt (geändert von `str | None` zu `Optional[str]`)
- Dokumentation der Agent-Klasse verbessert
- Unterstützung für Endpoint-Override hinzugefügt
- Initialisierungsmuster verbessert

#### Sitzung 06: Modell-Router (`models_router.py`)
- Endpoint-Konfiguration hinzugefügt
- Dokumentation zur Intent-Erkennung verbessert
- Dokumentation der Routing-Logik verbessert

#### Sitzung 06: Pipeline (`models_pipeline.py`)
- Umfassende Funktionsdokumentation hinzugefügt
- Schritt-für-Schritt-Dokumentation verbessert
- Fehlerbehandlung verbessert

### Skripte

#### Benchmark-Export (`export_benchmark_markdown.py`)
- Unterstützung für Endpoint-Override hinzugefügt
- Standardmodelle aktualisiert
- Funktionsdokumentation verbessert
- Fehlerbehandlung verbessert

#### CLI-Linter (`lint_markdown_cli.py`)
- SDK-Referenzlinks hinzugefügt
- Nutzungsdokumentation verbessert

### Tests

#### Smoke-Tests (`smoke.py`)
- Unterstützung für Endpoint-Override hinzugefügt
- Dokumentation verbessert
- Dokumentation der Testfälle verbessert
- Bessere Fehlerberichte

## Umgebungsvariablen

Alle Beispiele unterstützen jetzt diese Umgebungsvariablen:

### Kernkonfiguration
- `FOUNDRY_LOCAL_ALIAS` - Zu verwendender Modellalias (Standard variiert je nach Beispiel)
- `FOUNDRY_LOCAL_ENDPOINT` - Service-Endpoint überschreiben (optional)
- `SHOW_USAGE` - Token-Nutzungsstatistiken anzeigen (Standard: "0")
- `RETRY_ON_FAIL` - Wiederholungslogik aktivieren (Standard: "1")
- `RETRY_BACKOFF` - Anfangsverzögerung für Wiederholungen in Sekunden (Standard: "1.0")

### Beispiel-spezifisch
- `EMBED_MODEL` - Einbettungsmodell für RAG-Beispiele
- `BENCH_MODELS` - Komma-separierte Modelle für Benchmarking
- `BENCH_ROUNDS` - Anzahl der Benchmark-Runden
- `BENCH_PROMPT` - Test-Prompt für Benchmarks
- `BENCH_STREAM` - Latenz des ersten Tokens messen
- `RAG_QUESTION` - Testfrage für RAG-Beispiele
- `AGENT_MODEL_PRIMARY` - Primäres Agent-Modell
- `AGENT_MODEL_EDITOR` - Editor-Agent-Modell
- `SLM_ALIAS` - Alias für kleines Sprachmodell
- `LLM_ALIAS` - Alias für großes Sprachmodell

## Implementierte SDK-Best Practices

### 1. Richtige Client-Initialisierung
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Abruf von Modellinformationen
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Fehlerbehandlung
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Wiederholungslogik mit exponentiellem Backoff
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Unterstützung für Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Migrationsleitfaden für benutzerdefinierte Beispiele

Wenn Sie neue Beispiele erstellen oder bestehende aktualisieren:

1. **Verwenden Sie die Hilfsfunktionen von `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Unterstützen Sie Endpoint-Override**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Fügen Sie umfassende Dokumentation hinzu**:
   - Umgebungsvariablen in der Docstring
   - SDK-Referenzlink
   - Anwendungsbeispiele

4. **Verwenden Sie Typ-Hinweise**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implementieren Sie eine ordnungsgemäße Fehlerbehandlung**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Tests

Alle Beispiele können getestet werden mit:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK-Dokumentationsreferenzen

- **Hauptrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API-Dokumentation**: Aktuelle API-Dokumentation im SDK-Repository einsehen

## Breaking Changes

### Keine erwartet
Alle Änderungen sind rückwärtskompatibel. Die Updates:
- Fügen neue optionale Funktionen hinzu (Endpoint-Override)
- Verbessern die Fehlerbehandlung
- Erweitern die Dokumentation
- Aktualisieren die Standardmodellnamen auf aktuelle Empfehlungen

### Optionale Verbesserungen
Es wird empfohlen, den Code zu aktualisieren, um:
- `FOUNDRY_LOCAL_ENDPOINT` für explizite Endpoint-Steuerung zu verwenden
- `SHOW_USAGE=1` für die Sichtbarkeit der Token-Nutzung zu aktivieren
- Aktualisierte Standardmodelle (`phi-4-mini` statt `phi-3.5-mini`) zu verwenden

## Häufige Probleme & Lösungen

### Problem: "Client-Initialisierung fehlgeschlagen"
**Lösung**: Sicherstellen, dass der Foundry Local Service läuft:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problem: "Modell nicht gefunden"
**Lösung**: Verfügbare Modelle überprüfen:
```bash
foundry model list
```

### Problem: Verbindungsfehler beim Endpoint
**Lösung**: Endpoint überprüfen:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Nächste Schritte

1. **Module08-Beispiele aktualisieren**: Ähnliche Muster auf Module08/samples anwenden
2. **Integrationstests hinzufügen**: Umfassende Test-Suite erstellen
3. **Leistungs-Benchmarking**: Vorher/Nachher-Leistung vergleichen
4. **Dokumentationsupdates**: Haupt-README mit neuen Mustern aktualisieren

## Beitragsrichtlinien

Beim Hinzufügen neuer Beispiele:
1. Verwenden Sie `workshop_utils.py` für Konsistenz
2. Folgen Sie dem Muster in bestehenden Beispielen
3. Fügen Sie umfassende Docstrings hinzu
4. Integrieren Sie SDK-Referenzlinks
5. Unterstützen Sie Endpoint-Override
6. Fügen Sie ordnungsgemäße Typ-Hinweise hinzu
7. Integrieren Sie Anwendungsbeispiele in die Docstring

## Versionskompatibilität

Diese Updates sind kompatibel mit:
- `foundry-local-sdk` (neueste Version)
- `openai>=1.30.0`
- Python 3.8+

---

**Letzte Aktualisierung**: 08.01.2025  
**Betreuer**: EdgeAI Workshop Team  
**SDK-Version**: Foundry Local SDK (neueste 0.7.117+67073234e7)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.