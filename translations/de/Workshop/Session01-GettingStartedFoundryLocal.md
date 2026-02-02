# Sitzung 1: Einführung in Foundry Local

## Zusammenfassung

Lernen Sie, wie Sie Ihre ersten KI-Modelle mit Microsoft Foundry Local installieren, konfigurieren und ausführen. Diese praktische Sitzung bietet eine schrittweise Einführung in die lokale Inferenz, von der Installation bis hin zur Erstellung Ihrer ersten Chat-Anwendung mit Modellen wie Phi-4, Qwen und DeepSeek.

## Lernziele

Am Ende dieser Sitzung werden Sie:

- **Installieren und Konfigurieren**: Foundry Local korrekt einrichten und die Installation überprüfen
- **CLI-Operationen meistern**: Foundry Local CLI für Modellverwaltung und -bereitstellung nutzen
- **Ihr erstes Modell ausführen**: Ein lokales KI-Modell erfolgreich bereitstellen und damit interagieren
- **Eine Chat-App erstellen**: Eine einfache Chat-Anwendung mit dem Foundry Local Python SDK entwickeln
- **Lokale KI verstehen**: Die Grundlagen der lokalen Inferenz und Modellverwaltung begreifen

## Voraussetzungen

### Systemanforderungen

- **Windows**: Windows 11 (22H2 oder später) ODER **macOS**: macOS 11+ (eingeschränkte Unterstützung)
- **RAM**: Mindestens 8GB, empfohlen 16GB+
- **Speicherplatz**: Mindestens 10GB freier Speicherplatz für Modelle
- **Python**: Version 3.10 oder später installiert
- **Administratorzugriff**: Administratorrechte für die Installation

### Entwicklungsumgebung

- Visual Studio Code mit Python-Erweiterung (empfohlen)
- Zugriff auf die Kommandozeile (PowerShell unter Windows, Terminal unter macOS)
- Git zum Klonen von Repositories (optional)

## Ablauf des Workshops (30 Minuten)

### Schritt 1: Foundry Local installieren (5 Minuten)

#### Installation unter Windows

Installieren Sie Foundry Local mit dem Windows-Paketmanager:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternative: Direkt herunterladen von [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Installation unter macOS (eingeschränkte Unterstützung)

> [!NOTE] 
> Die Unterstützung für macOS befindet sich derzeit in der Vorschau. Überprüfen Sie die offizielle Dokumentation für die neuesten Informationen.

Falls verfügbar, installieren Sie Foundry Local mit Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternative für macOS-Nutzer:**
- Verwenden Sie eine Windows 11 VM (Parallels/UTM) und folgen Sie den Windows-Schritten
- Führen Sie Foundry Local über einen Container aus, falls verfügbar, und konfigurieren Sie `FOUNDRY_LOCAL_ENDPOINT`

### Schritt 2: Installation überprüfen (3 Minuten)

Starten Sie nach der Installation Ihr Terminal neu und überprüfen Sie, ob Foundry Local funktioniert:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Die erwartete Ausgabe sollte Versionsinformationen und verfügbare Befehle anzeigen.

### Schritt 3: Python-Umgebung einrichten (5 Minuten)

Erstellen Sie eine dedizierte Python-Umgebung für diesen Workshop:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Schritt 4: Ihr erstes Modell ausführen (7 Minuten)

Jetzt führen wir unser erstes KI-Modell lokal aus!

#### Starten Sie mit Phi-4 Mini (empfohlenes erstes Modell)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Dieser Befehl lädt das Modell (beim ersten Mal) herunter und startet den Foundry Local-Dienst automatisch.

#### Überprüfen, was läuft

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Verschiedene Modelle ausprobieren

Sobald phi-4-mini funktioniert, experimentieren Sie mit anderen Modellen:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Schritt 5: Ihre erste Chat-Anwendung erstellen (10 Minuten)

Jetzt erstellen wir eine Python-Anwendung, die die Modelle nutzt, die wir gerade gestartet haben.

#### Das Chat-Skript erstellen

Erstellen Sie eine neue Datei namens `my_first_chat.py` (oder verwenden Sie das bereitgestellte Beispiel):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Verwandte Beispiele**: Für fortgeschrittene Nutzung siehe:
>
> - **Python-Beispiel**: `Workshop/samples/session01/chat_bootstrap.py` - Enthält Streaming-Antworten und Fehlerbehandlung
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktive Version mit detaillierten Erklärungen

#### Ihre Chat-Anwendung testen

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternative: Verwenden Sie direkt die bereitgestellten Beispiele

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Oder erkunden Sie das interaktive Notebook  
Öffnen Sie Workshop/notebooks/session01_chat_bootstrap.ipynb in VS Code

Probieren Sie diese Beispielgespräche aus:

- "Was ist Microsoft Foundry Local?"
- "Nennen Sie 3 Vorteile der Ausführung von KI-Modellen lokal"
- "Helfen Sie mir, Edge-KI zu verstehen"

## Was Sie erreicht haben

Herzlichen Glückwunsch! Sie haben erfolgreich:

1. ✅ **Foundry Local installiert** und überprüft, dass es funktioniert
2. ✅ **Ihr erstes KI-Modell gestartet** (phi-4-mini) lokal
3. ✅ **Verschiedene Modelle getestet** über die Kommandozeile
4. ✅ **Eine Chat-Anwendung erstellt**, die mit Ihrer lokalen KI verbunden ist
5. ✅ **Lokale KI-Inferenz erlebt** ohne Cloud-Abhängigkeiten

## Verständnis der Vorgänge

### Lokale KI-Inferenz

- Ihre KI-Modelle laufen vollständig auf Ihrem Computer
- Es werden keine Daten in die Cloud gesendet
- Antworten werden lokal mit Ihrer CPU/GPU generiert
- Datenschutz und Sicherheit bleiben erhalten

### Modellverwaltung

- `foundry model run` lädt und startet Modelle
- **FoundryLocalManager SDK** startet automatisch Dienste und lädt Modelle
- Modelle werden lokal zwischengespeichert für zukünftige Nutzung
- Mehrere Modelle können heruntergeladen werden, aber typischerweise läuft nur eines gleichzeitig
- Der Dienst verwaltet den Lebenszyklus der Modelle automatisch

### SDK- vs CLI-Ansätze

- **CLI-Ansatz**: Manuelle Modellverwaltung mit `foundry model run <model>`
- **SDK-Ansatz**: Automatische Dienst- und Modellverwaltung mit `FoundryLocalManager(alias)`
- **Empfehlung**: SDK für Anwendungen nutzen, CLI für Tests und Erkundung

## Referenz für häufige Befehle

### Wichtige CLI-Befehle

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Modell-Empfehlungen

- **phi-4-mini**: Bestes Einstiegsmodell - schnell, leichtgewichtig, gute Qualität
- **qwen2.5-0.5b**: Schnellste Inferenz, minimaler Speicherverbrauch
- **gpt-oss-20b**: Höhere Qualität der Antworten, benötigt mehr Ressourcen
- **deepseek-coder-1.3b**: Optimiert für Programmier- und Codeaufgaben

## Fehlerbehebung

### "Foundry-Befehl nicht gefunden"

**Lösung:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Modell konnte nicht geladen werden"

**Lösung:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Verbindung zu localhost verweigert"

**Lösung:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Nächste Schritte

### Sofortige nächste Aktionen

1. **Experimentieren** Sie mit verschiedenen Modellen und Eingaben
2. **Modifizieren** Sie Ihre Chat-Anwendung, um verschiedene Modelle auszuprobieren
3. **Erstellen** Sie eigene Eingaben und testen Sie die Antworten
4. **Erkunden** Sie Sitzung 2: Aufbau von RAG-Anwendungen

### Fortgeschrittener Lernpfad

1. **Sitzung 2**: KI-Lösungen mit RAG (Retrieval-Augmented Generation) entwickeln
2. **Sitzung 3**: Vergleich verschiedener Open-Source-Modelle
3. **Sitzung 4**: Arbeiten mit modernsten Modellen
4. **Sitzung 5**: Aufbau von Multi-Agenten-KI-Systemen

## Umgebungsvariablen (optional)

Für fortgeschrittene Nutzung können Sie diese Umgebungsvariablen setzen:

| Variable | Zweck | Beispiel |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Standardmodell | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Endpunkt-URL überschreiben | `http://localhost:5273/v1` |

Erstellen Sie eine `.env`-Datei in Ihrem Projektverzeichnis:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Zusätzliche Ressourcen

### Dokumentation

- [Foundry Local Python SDK Referenz](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installationsanleitung](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Modellkatalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Beispielcode

- **Session01 Python-Beispiel**: `Workshop/samples/session01/chat_bootstrap.py` - Vollständige Chat-App mit Streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktives Tutorial  
- [Modul08 Beispiel 01](../Module08/samples/01/README.md) - REST Chat Schnellstart
- [Modul08 Beispiel 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Modul08 Beispiel 03](../Module08/samples/03/README.md) - Modellentdeckung & Benchmarking

### Community

- [Foundry Local GitHub Diskussionen](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Dauer der Sitzung**: 30 Minuten Praxis + 15 Minuten Q&A  
**Schwierigkeitsgrad**: Anfänger  
**Voraussetzungen**: Windows 11/macOS 11+, Python 3.10+, Administratorzugriff

## Beispiel-Szenario des Workshops

### Kontext aus der Praxis

**Szenario**: Ein IT-Team eines Unternehmens muss die lokale KI-Inferenz evaluieren, um sensible Mitarbeiterfeedbacks zu verarbeiten, ohne Daten an externe Dienste zu senden.

**Ihr Ziel**: Zeigen Sie, dass lokale KI-Modelle qualitativ hochwertige Antworten mit einer Latenzzeit von unter einer Sekunde liefern können, während die Daten vollständig privat bleiben.

### Testeingaben

Verwenden Sie diese Eingaben, um Ihre Einrichtung zu validieren:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Erfolgskriterien

- ✅ Alle Eingaben liefern Antworten in unter 2 Sekunden
- ✅ Es werden keine Daten von Ihrem lokalen Rechner gesendet
- ✅ Antworten sind relevant und hilfreich
- ✅ Ihre Chat-Anwendung funktioniert reibungslos

Diese Validierung stellt sicher, dass Ihre Foundry Local-Einrichtung bereit ist für die fortgeschrittenen Workshops in den Sitzungen 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->