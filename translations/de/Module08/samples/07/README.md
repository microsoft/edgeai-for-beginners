# Foundry Local als API-Beispiel

Dieses Beispiel zeigt, wie Microsoft Foundry Local als REST-API-Dienst genutzt werden kann, ohne auf das OpenAI SDK angewiesen zu sein. Es demonstriert direkte HTTP-Integrationsmuster für maximale Kontrolle und Anpassung.

## Überblick

Basierend auf den offiziellen Mustern von Microsoft Foundry Local bietet dieses Beispiel:
- Direkte REST-API-Integration mit FoundryLocalManager
- Eigene HTTP-Client-Implementierung
- Modellverwaltung und Gesundheitsüberwachung
- Verarbeitung von Streaming- und Nicht-Streaming-Antworten
- Produktionsreife Fehlerbehandlung und Wiederholungslogik

## Voraussetzungen

1. **Foundry Local Installation**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python-Abhängigkeiten**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architektur

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Hauptfunktionen

### 1. **Direkte HTTP-Integration**
- Reine REST-API-Aufrufe ohne SDK-Abhängigkeiten
- Eigene Authentifizierung und Header
- Volle Kontrolle über Anfrage-/Antwortverarbeitung

### 2. **Modellverwaltung**
- Dynamisches Laden und Entladen von Modellen
- Gesundheitsüberwachung und Statusprüfungen
- Sammlung von Leistungsmetriken

### 3. **Produktionsmuster**
- Wiederholungsmechanismen mit exponentiellem Backoff
- Circuit Breaker für Fehlertoleranz
- Umfassendes Logging und Monitoring

### 4. **Flexible Antwortverarbeitung**
- Streaming-Antworten für Echtzeitanwendungen
- Batch-Verarbeitung für Szenarien mit hoher Durchsatzrate
- Eigene Antwortanalyse und Validierung

## Anwendungsbeispiele

### Grundlegende API-Integration
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Streaming-Integration
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Gesundheitsüberwachung
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Dateistruktur

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local Integration

Dieses Beispiel folgt den offiziellen Mustern von Microsoft:

1. **SDK-Integration**: Verwendet `FoundryLocalManager` für die Dienstverwaltung
2. **REST-Endpunkte**: Direkte Aufrufe von `/v1/chat/completions` und anderen Endpunkten
3. **Authentifizierung**: Korrekte Handhabung des API-Schlüssels für lokale Dienste
4. **Modellverwaltung**: Katalogauflistung, Herunterladen und Laden von Mustern
5. **Fehlerbehandlung**: Von Microsoft empfohlene Fehlercodes und Antworten

## Erste Schritte

1. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

2. **Grundlegendes Beispiel ausführen**
   ```bash
   python examples/basic_usage.py
   ```

3. **Streaming ausprobieren**
   ```bash
   python examples/streaming.py
   ```

4. **Produktionssetup**
   ```bash
   python examples/production.py
   ```

## Konfiguration

Umgebungsvariablen zur Anpassung:
- `FOUNDRY_MODEL`: Standardmodell (Standard: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Anfrage-Timeout in Sekunden (Standard: 30)
- `FOUNDRY_RETRIES`: Anzahl der Wiederholungsversuche (Standard: 3)
- `FOUNDRY_LOG_LEVEL`: Protokollierungsstufe (Standard: "INFO")

## Best Practices

1. **Verbindungsmanagement**: Wiederverwendung von HTTP-Verbindungen für bessere Leistung
2. **Fehlerbehandlung**: Implementierung einer geeigneten Wiederholungslogik mit exponentiellem Backoff
3. **Ressourcenüberwachung**: Überwachung der Speichernutzung und Leistung des Modells
4. **Sicherheit**: Verwendung einer korrekten Authentifizierung, auch für lokale Dienste
5. **Tests**: Einbindung von Unit- und Integrationstests

## Fehlerbehebung

### Häufige Probleme

**Dienst läuft nicht**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Probleme beim Laden des Modells**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Verbindungsfehler**
- Überprüfen, ob Foundry Local auf dem richtigen Port läuft
- Firewall-Einstellungen prüfen
- Sicherstellen, dass die Authentifizierungsheader korrekt sind

## Leistungsoptimierung

1. **Verbindungspooling**: Verwendung von Session-Objekten für mehrere Anfragen
2. **Asynchrone Operationen**: Nutzung von asyncio für gleichzeitige Anfragen
3. **Caching**: Zwischenspeicherung von Modellantworten, wo sinnvoll
4. **Monitoring**: Überwachung der Antwortzeiten und Anpassung der Timeouts

## Lernziele

Nach Abschluss dieses Beispiels verstehen Sie:
- Direkte REST-API-Integration mit Foundry Local
- Muster für die Implementierung eines eigenen HTTP-Clients
- Produktionsreife Fehlerbehandlung und Überwachung
- Architektur des Microsoft Foundry Local-Dienstes
- Techniken zur Leistungsoptimierung für lokale KI-Dienste

## Nächste Schritte

- Beispiel 08: Windows 11 Chat-Anwendung erkunden
- Beispiel 09: Multi-Agent-Orchestrierung ausprobieren
- Beispiel 10: Foundry Local als Tool-Integration kennenlernen

---

