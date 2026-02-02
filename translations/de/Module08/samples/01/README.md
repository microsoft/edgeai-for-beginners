# Beispiel 01: Schneller Chat über OpenAI SDK

Ein einfaches Chat-Beispiel, das zeigt, wie man das OpenAI SDK mit Microsoft Foundry Local für lokale KI-Inferenz verwendet.

## Überblick

Dieses Beispiel zeigt, wie man:
- Das OpenAI Python SDK mit Foundry Local verwendet
- Sowohl Azure OpenAI- als auch lokale Foundry-Konfigurationen handhabt
- Fehlerbehandlung und Fallback-Strategien korrekt implementiert
- Den FoundryLocalManager für die Serviceverwaltung nutzt

## Voraussetzungen

- **Foundry Local**: Installiert und im PATH verfügbar
- **Python**: Version 3.8 oder höher
- **Modell**: Ein Modell, das in Foundry Local geladen ist (z. B. `phi-4-mini`)

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

3. **Foundry Local-Service starten und ein Modell laden:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Verwendung

### Foundry Local (Standard)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Code-Funktionen

### Integration des FoundryLocalManager

Das Beispiel verwendet das offizielle Foundry Local SDK für eine korrekte Serviceverwaltung:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Fehlerbehandlung

Robuste Fehlerbehandlung mit Fallback auf manuelle Konfiguration:
- Automatische Service-Erkennung
- Sanfte Degradierung, falls das SDK nicht verfügbar ist
- Klare Fehlermeldungen zur Fehlerbehebung

## Umgebungsvariablen

| Variable | Beschreibung | Standardwert | Erforderlich |
|----------|--------------|--------------|--------------|
| `MODEL` | Modellalias oder -name | `phi-4-mini` | Nein |
| `BASE_URL` | Foundry Local Basis-URL | `http://localhost:8000` | Nein |
| `API_KEY` | API-Schlüssel (normalerweise nicht erforderlich für lokal) | `""` | Nein |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI-Endpunkt | - | Für Azure |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API-Schlüssel | - | Für Azure |
| `AZURE_OPENAI_API_VERSION` | Azure API-Version | `2024-08-01-preview` | Nein |

## Fehlerbehebung

### Häufige Probleme

1. **Warnung: "Foundry SDK konnte nicht verwendet werden":**
   - Foundry Local SDK installieren: `pip install foundry-local-sdk`
   - Oder Umgebungsvariablen für manuelle Konfiguration setzen

2. **Verbindung verweigert:**
   - Sicherstellen, dass Foundry Local läuft: `foundry service status`
   - Überprüfen, ob ein Modell geladen ist: `foundry service ps`

3. **Modell nicht gefunden:**
   - Verfügbare Modelle auflisten: `foundry model list`
   - Ein Modell laden: `foundry model run phi-4-mini`

### Verifizierung

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Referenzen

- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-kompatible API-Referenz](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

