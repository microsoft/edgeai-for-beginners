# Beispiel 02: OpenAI SDK-Integration

Demonstriert eine fortgeschrittene Integration mit dem OpenAI Python SDK, unterstützt sowohl Microsoft Foundry Local als auch Azure OpenAI mit Streaming-Antworten und ordnungsgemäßer Fehlerbehandlung.

## Übersicht

Dieses Beispiel zeigt:
- Nahtloses Umschalten zwischen Foundry Local und Azure OpenAI
- Streaming-Chat-Antworten für eine bessere Benutzererfahrung
- Richtige Verwendung des FoundryLocalManager SDK
- Robuste Fehlerbehandlung und Fallback-Mechanismen
- Produktionsreife Code-Muster

## Voraussetzungen

- **Foundry Local**: Installiert und ausgeführt (für lokale Inferenz)
- **Python**: Version 3.8 oder höher mit OpenAI SDK
- **Azure OpenAI**: Gültiger Endpunkt und API-Schlüssel (für Cloud-Inferenz)

## Installation

1. **Python-Umgebung einrichten:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Abhängigkeiten installieren:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local starten (für lokalen Modus):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Anwendungsfälle

### Foundry Local (Standard)

**Option 1: Verwendung von FoundryLocalManager (empfohlen)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Option 2: Manuelle Konfiguration**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Code-Architektur

### Client Factory Pattern

Das Beispiel verwendet ein Factory-Pattern, um geeignete Clients zu erstellen:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Streaming-Antworten

Das Beispiel zeigt Streaming für die Echtzeit-Antwortgenerierung:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Umgebungsvariablen

### Foundry Local Konfiguration

| Variable | Beschreibung | Standardwert | Erforderlich |
|----------|--------------|--------------|--------------|
| `MODEL` | Zu verwendender Modellalias | `phi-4-mini` | Nein |
| `BASE_URL` | Foundry Local Endpunkt | `http://localhost:8000` | Nein |
| `API_KEY` | API-Schlüssel (optional für lokal) | `""` | Nein |

### Azure OpenAI Konfiguration

| Variable | Beschreibung | Standardwert | Erforderlich |
|----------|--------------|--------------|--------------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI Ressourcen-Endpunkt | - | Ja |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-Schlüssel | - | Ja |
| `AZURE_OPENAI_API_VERSION` | API-Version | `2024-08-01-preview` | Nein |
| `MODEL` | Azure Bereitstellungsname | `your-deployment-name` | Ja |

## Erweiterte Funktionen

### Automatische Dienst-Erkennung

Das Beispiel erkennt automatisch den passenden Dienst basierend auf Umgebungsvariablen:

1. **Azure-Modus**: Wenn `AZURE_OPENAI_ENDPOINT` und `AZURE_OPENAI_API_KEY` gesetzt sind
2. **Foundry SDK-Modus**: Wenn Foundry Local SDK verfügbar ist
3. **Manueller Modus**: Fallback zur manuellen Konfiguration

### Fehlerbehandlung

- Sanfter Fallback vom SDK zur manuellen Konfiguration
- Klare Fehlermeldungen zur Fehlerbehebung
- Ordentliche Ausnahmebehandlung bei Netzwerkproblemen
- Validierung der erforderlichen Umgebungsvariablen

## Leistungsüberlegungen

### Lokale vs. Cloud-Vor- und Nachteile

**Vorteile von Foundry Local:**
- ✅ Keine API-Kosten
- ✅ Datenschutz (keine Daten verlassen das Gerät)
- ✅ Niedrige Latenz für unterstützte Modelle
- ✅ Funktioniert offline

**Vorteile von Azure OpenAI:**
- ✅ Zugriff auf die neuesten großen Modelle
- ✅ Höherer Durchsatz
- ✅ Keine lokalen Hardwareanforderungen
- ✅ Unternehmensgerechte SLA

## Fehlerbehebung

### Häufige Probleme

1. **"Foundry SDK konnte nicht verwendet werden"-Warnung:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure-Authentifizierungsfehler:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modell nicht verfügbar:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Gesundheitschecks

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Nächste Schritte

- **Beispiel 03**: Modell-Erkennung und Benchmarking
- **Beispiel 04**: Aufbau einer Chainlit RAG-Anwendung
- **Beispiel 05**: Multi-Agent-Orchestrierung
- **Beispiel 06**: Modelle-als-Tools-Routing

## Referenzen

- [Azure OpenAI Dokumentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Referenz](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Dokumentation](https://github.com/openai/openai-python)
- [Streaming-Antworten Leitfaden](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

