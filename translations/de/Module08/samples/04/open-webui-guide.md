# Open WebUI + Foundry Local Integrationsleitfaden

Dieser Leitfaden zeigt, wie Open WebUI mit Microsoft Foundry Local verbunden werden kann, um eine professionelle ChatGPT-ähnliche Oberfläche mit Ihren lokalen KI-Modellen zu nutzen.

## Überblick

Open WebUI bietet eine moderne, benutzerfreundliche Chat-Oberfläche, die mit jeder OpenAI-kompatiblen API verbunden werden kann. Durch die Verbindung mit Foundry Local erhalten Sie:

- **Professionelle Benutzeroberfläche**: ChatGPT-ähnliche Oberfläche mit modernem Design
- **Lokale Privatsphäre**: Alle Verarbeitungen erfolgen auf Ihrem Gerät
- **Modellwechsel**: Einfaches Umschalten zwischen verschiedenen lokalen Modellen
- **Gesprächsverlauf**: Persistente Chat-Historie und Kontext
- **Datei-Uploads**: Dokumentenanalyse und Dateiverarbeitungsfunktionen
- **Individuelle Personas**: System-Prompts und Rollenanpassung

## Voraussetzungen

### Erforderliche Software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Ein Modell laden

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Schnelle Einrichtung (Empfohlen)

### Schritt 1: Open WebUI mit Docker starten

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Schritt 2: Erste Einrichtung

1. **Browser öffnen**: Navigieren Sie zu `http://localhost:3000`
2. **Konto erstellen**: Richten Sie einen Admin-Benutzer ein (der erste Benutzer wird Admin)
3. **Verbindung überprüfen**: Modelle sollten automatisch im Dropdown-Menü erscheinen

### Schritt 3: Verbindung testen

1. Wählen Sie Ihr Modell aus dem Dropdown-Menü (z. B. "phi-4-mini")
2. Geben Sie eine Testnachricht ein: "Hallo! Können Sie sich vorstellen?"
3. Sie sollten eine Streaming-Antwort von Ihrem lokalen Modell sehen

## Erweiterte Konfiguration

### Umgebungsvariablen

| Variable | Zweck | Standard | Beispiel |
|----------|-------|----------|----------|
| `OPENAI_API_BASE_URL` | Foundry Local-Endpunkt | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-Schlüssel (erforderlich, aber lokal nicht verwendet) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Schlüssel zur Sitzungsverschlüsselung | automatisch generiert | `your-secret-key` |
| `ENABLE_SIGNUP` | Registrierung neuer Benutzer erlauben | `True` | `False` |

### Manuelle Konfiguration (Alternative)

Falls Umgebungsvariablen nicht funktionieren, manuelle Konfiguration:

1. **Einstellungen öffnen**: Klicken Sie auf das Zahnrad-Symbol
2. **Zu Verbindungen navigieren**: Einstellungen → Verbindungen → OpenAI
3. **API-Details eingeben**:
   - API-Basis-URL: `http://host.docker.internal:51211/v1`
   - API-Schlüssel: `foundry-local-key` (beliebiger Wert funktioniert)
4. **Speichern und testen**: Klicken Sie auf "Speichern" und testen Sie mit einem Modell

### Persistente Datenspeicherung

Um Gespräche und Einstellungen zu speichern:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Fehlerbehebung

### Verbindungsprobleme

**Problem**: "Verbindung verweigert" oder Modelle werden nicht geladen

**Lösungen**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Modell wird nicht angezeigt

**Problem**: Open WebUI zeigt keine Modelle im Dropdown-Menü an

**Fehlerbehebungsschritte**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Lösung**: Stellen Sie sicher, dass das Modell korrekt geladen ist:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker-Netzwerkprobleme

**Problem**: `host.docker.internal` wird nicht aufgelöst

**Windows-Lösung**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Alternative**: Finden Sie die IP-Adresse Ihres Geräts:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Leistungsprobleme

**Langsame Antworten**:
1. Überprüfen Sie, ob das Modell GPU-Beschleunigung verwendet: `foundry service ps`
2. Stellen Sie sicher, dass genügend Systemressourcen (RAM/GPU-Speicher) verfügbar sind
3. Verwenden Sie ein kleineres Modell für Tests

**Speicherprobleme**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Benutzerhandbuch

### Basis-Chat

1. **Modell auswählen**: Wählen Sie ein Modell aus dem Dropdown-Menü (zeigt Foundry Local-Modelle)
2. **Nachricht eingeben**: Verwenden Sie das Texteingabefeld unten
3. **Senden**: Drücken Sie Enter oder klicken Sie auf die Schaltfläche "Senden"
4. **Antwort anzeigen**: Sehen Sie die Streaming-Antwort in Echtzeit

### Erweiterte Funktionen

**Datei-Upload**:
1. Klicken Sie auf das Büroklammer-Symbol
2. Laden Sie ein Dokument hoch (PDF, TXT usw.)
3. Stellen Sie Fragen zum Inhalt
4. Das Modell analysiert und antwortet basierend auf dem Dokument

**Individuelle System-Prompts**:
1. Einstellungen → Personalisierung
2. Benutzerdefinierten System-Prompt festlegen
3. Erzeugt eine konsistente KI-Persönlichkeit/Verhalten

**Gesprächsverwaltung**:
- **Neuer Chat**: Klicken Sie auf "+" für ein neues Gespräch
- **Chat-Historie**: Greifen Sie auf vorherige Gespräche in der Seitenleiste zu
- **Exportieren**: Laden Sie die Chat-Historie als Text/JSON herunter

**Modellvergleich**:
1. Öffnen Sie mehrere Browser-Tabs mit derselben Open WebUI
2. Wählen Sie in jedem Tab unterschiedliche Modelle aus
3. Vergleichen Sie Antworten auf dieselben Eingaben

### Integrationsmuster

**Entwicklungsworkflow**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Produktionsbereitstellung

### Sichere Einrichtung

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Mehrbenutzer-Einrichtung

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Überwachung und Protokollierung

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Bereinigung

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Nächste Schritte

### Verbesserungsideen

1. **Benutzerdefinierte Modelle**: Fügen Sie Ihre eigenen feinabgestimmten Modelle zu Foundry Local hinzu
2. **API-Integration**: Verbinden Sie externe APIs über Open WebUI-Funktionen
3. **Dokumentenverarbeitung**: Richten Sie erweiterte RAG-Pipelines ein
4. **Multi-Modal**: Konfigurieren Sie Vision-Modelle für die Bildanalyse

### Skalierungsüberlegungen

- **Lastverteilung**: Mehrere Foundry Local-Instanzen hinter einem Reverse-Proxy
- **Modell-Routing**: Unterschiedliche Modelle für verschiedene Anwendungsfälle
- **Ressourcenmanagement**: GPU-Speicheroptimierung für gleichzeitige Benutzer
- **Backup-Strategie**: Regelmäßige Sicherung von Gesprächsdaten und Konfigurationen

## Referenzen

- [Open WebUI Dokumentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installationsanleitung](https://docs.docker.com/get-docker/)

---

