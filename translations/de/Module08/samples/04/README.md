# Beispiel 04: Produktionsreife Chat-Anwendungen mit Chainlit

Ein umfassendes Beispiel, das verschiedene Ansätze zur Erstellung produktionsreifer Chat-Anwendungen mit Microsoft Foundry Local zeigt, einschließlich moderner Webschnittstellen, Streaming-Antworten und fortschrittlicher Browsertechnologien.

## Was ist enthalten?

- **🚀 Chainlit Chat App** (`app.py`): Produktionsreife Chat-Anwendung mit Streaming
- **🌐 WebGPU-Demo** (`webgpu-demo/`): KI-Inferenz im Browser mit Hardwarebeschleunigung
- **🎨 Open WebUI-Integration** (`open-webui-guide.md`): Professionelle ChatGPT-ähnliche Benutzeroberfläche
- **📚 Lehrmaterialien** (`chainlit_app.ipynb`): Interaktive Lerninhalte

## Schnellstart

### 1. Chainlit Chat-Anwendung

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Öffnet unter: `http://localhost:8080`

### 2. WebGPU-Browser-Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Öffnet unter: `http://localhost:5173`

### 3. Open WebUI-Setup

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Öffnet unter: `http://localhost:3000`

## Architektur-Muster

### Entscheidungsmatrix: Lokal vs. Cloud

| Szenario | Empfehlung | Grund |
|----------|------------|-------|
| **Datenschutzsensible Daten** | 🏠 Lokal (Foundry) | Daten verlassen das Gerät nicht |
| **Komplexe Logik** | ☁️ Cloud (Azure OpenAI) | Zugriff auf größere Modelle |
| **Echtzeit-Chat** | 🏠 Lokal (Foundry) | Niedrigere Latenz, schnellere Antworten |
| **Dokumentenanalyse** | 🔄 Hybrid | Lokal für Extraktion, Cloud für Analyse |
| **Code-Generierung** | 🏠 Lokal (Foundry) | Datenschutz + spezialisierte Modelle |
| **Forschungsaufgaben** | ☁️ Cloud (Azure OpenAI) | Breite Wissensbasis erforderlich |

### Technologie-Vergleich

| Technologie | Anwendungsfall | Vorteile | Nachteile |
|-------------|----------------|----------|-----------|
| **Chainlit** | Python-Entwickler, schnelles Prototyping | Einfache Einrichtung, Streaming-Unterstützung | Nur Python |
| **WebGPU** | Maximale Privatsphäre, Offline-Szenarien | Browser-nativ, kein Server erforderlich | Begrenzte Modellgröße |
| **Open WebUI** | Produktionsbereitstellung, Teams | Professionelle Benutzeroberfläche, Benutzerverwaltung | Erfordert Docker |

## Voraussetzungen

- **Foundry Local**: Installiert und ausgeführt ([Download](https://aka.ms/foundry-local-installer))
- **Python**: Version 3.10+ mit virtueller Umgebung
- **Modell**: Mindestens ein geladenes Modell (`foundry model run phi-4-mini`)
- **Browser**: Chrome/Edge mit WebGPU-Unterstützung für Demos
- **Docker**: Für Open WebUI (optional)

## Installation & Einrichtung

### 1. Python-Umgebung einrichten

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local einrichten

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Beispielanwendungen

### Chainlit Chat-Anwendung

**Funktionen:**
- 🚀 **Echtzeit-Streaming**: Tokens erscheinen, während sie generiert werden
- 🛡️ **Robuste Fehlerbehandlung**: Sanfte Degradierung und Wiederherstellung
- 🎨 **Moderne Benutzeroberfläche**: Professionelle Chat-Oberfläche direkt einsatzbereit
- 🔧 **Flexible Konfiguration**: Umgebungsvariablen und automatische Erkennung
- 📱 **Responsive Design**: Funktioniert auf Desktop- und Mobilgeräten

**Schnellstart:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU-Browser-Demo

**Funktionen:**
- 🌐 **Browser-native KI**: Kein Server erforderlich, läuft vollständig im Browser
- ⚡ **WebGPU-Beschleunigung**: Hardwarebeschleunigung, wenn verfügbar
- 🔒 **Maximale Privatsphäre**: Keine Daten verlassen Ihr Gerät
- 🎯 **Keine Installation**: Funktioniert in jedem kompatiblen Browser
- 🔄 **Sanfter Rückfall**: Fällt auf CPU zurück, wenn WebGPU nicht verfügbar ist

**Ausführung:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI-Integration

**Funktionen:**
- 🎨 **ChatGPT-ähnliche Benutzeroberfläche**: Professionell und vertraut
- 👥 **Multi-User-Unterstützung**: Benutzerkonten und Gesprächsverlauf
- 📁 **Dateiverarbeitung**: Hochladen und Analysieren von Dokumenten
- 🔄 **Modellwechsel**: Einfacher Wechsel zwischen verschiedenen Modellen
- 🐳 **Docker-Bereitstellung**: Produktionsreife containerisierte Einrichtung

**Schnelle Einrichtung:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Konfigurationsreferenz

### Umgebungsvariablen

| Variable | Beschreibung | Standard | Beispiel |
|----------|--------------|----------|----------|
| `MODEL` | Modellalias, der verwendet werden soll | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local-Endpunkt | Automatisch erkannt | `http://localhost:51211` |
| `API_KEY` | API-Schlüssel (optional für lokal) | `""` | `your-api-key` |

## Fehlerbehebung

### Häufige Probleme

**Chainlit-Anwendung:**

1. **Dienst nicht verfügbar:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Port-Konflikte:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Probleme mit der Python-Umgebung:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU-Demo:**

1. **WebGPU nicht unterstützt:**
   - Aktualisieren Sie auf Chrome/Edge 113+
   - Aktivieren Sie WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Überprüfen Sie den GPU-Status: `chrome://gpu`
   - Die Demo fällt automatisch auf die CPU zurück

2. **Fehler beim Laden des Modells:**
   - Stellen Sie sicher, dass eine Internetverbindung für den Modell-Download besteht
   - Überprüfen Sie die Browser-Konsole auf CORS-Fehler
   - Vergewissern Sie sich, dass Sie über HTTP (nicht file://) bereitstellen

**Open WebUI:**

1. **Verbindung verweigert:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modelle erscheinen nicht:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Validierungs-Checkliste

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Erweiterte Nutzung

### Leistungsoptimierung

**Chainlit:**
- Verwenden Sie Streaming für eine bessere wahrgenommene Leistung
- Implementieren Sie Connection-Pooling für hohe Parallelität
- Zwischenspeichern von Modellantworten für wiederholte Abfragen
- Überwachen Sie den Speicherverbrauch bei großen Gesprächsverläufen

**WebGPU:**
- Nutzen Sie WebGPU für maximale Privatsphäre und Geschwindigkeit
- Implementieren Sie Modellquantisierung für kleinere Modelle
- Verwenden Sie Web Workers für Hintergrundverarbeitung
- Zwischenspeichern Sie kompilierte Modelle im Browser-Speicher

**Open WebUI:**
- Verwenden Sie persistente Volumes für Gesprächsverläufe
- Konfigurieren Sie Ressourcenlimits für den Docker-Container
- Implementieren Sie Backup-Strategien für Benutzerdaten
- Richten Sie einen Reverse-Proxy für SSL-Terminierung ein

### Integrationsmuster

**Hybrid Lokal/Cloud:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Multi-Modale Pipeline:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Produktionsbereitstellung

### Sicherheitsüberlegungen

- **API-Schlüssel**: Verwenden Sie Umgebungsvariablen, niemals fest codieren
- **Netzwerk**: Verwenden Sie HTTPS in der Produktion, ziehen Sie VPN für Teamzugriff in Betracht
- **Zugriffskontrolle**: Implementieren Sie Authentifizierung für Open WebUI
- **Datenschutz**: Überprüfen Sie, welche Daten lokal bleiben und welche in die Cloud gehen
- **Updates**: Halten Sie Foundry Local und Container auf dem neuesten Stand

### Überwachung und Wartung

- **Health Checks**: Implementieren Sie Endpunktüberwachung
- **Protokollierung**: Zentralisieren Sie Protokolle aller Komponenten
- **Metriken**: Verfolgen Sie Antwortzeiten, Fehlerraten und Ressourcennutzung
- **Backup**: Regelmäßige Sicherung von Gesprächsdaten und Konfigurationen

## Referenzen und Ressourcen

### Dokumentation
- [Chainlit-Dokumentation](https://docs.chainlit.io/) - Vollständige Framework-Anleitung
- [Foundry Local-Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Offizielle Microsoft-Dokumentation
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU-Integration
- [Open WebUI-Dokumentation](https://docs.openwebui.com/) - Erweiterte Konfiguration

### Beispieldateien
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produktionsreife Chainlit-Anwendung
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Lehrmaterialien
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - KI-Inferenz im Browser
- [`open-webui-guide.md`](./open-webui-guide.md) - Vollständige Open WebUI-Einrichtung

### Verwandte Beispiele
- [Session 4 Dokumentation](../../04.CuttingEdgeModels.md) - Vollständige Sitzungsanleitung
- [Foundry Local Beispiele](https://github.com/microsoft/foundry-local/tree/main/samples) - Offizielle Beispiele

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.