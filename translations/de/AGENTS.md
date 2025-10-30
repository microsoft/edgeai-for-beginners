<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58a69ffb43295827eb8cf45c0617a245",
  "translation_date": "2025-10-30T10:40:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "de"
}
-->
# AGENTS.md

> **Entwicklerhandbuch für Beiträge zu EdgeAI für Anfänger**
> 
> Dieses Dokument bietet umfassende Informationen für Entwickler, KI-Agenten und Mitwirkende, die mit diesem Repository arbeiten. Es behandelt Einrichtung, Entwicklungsabläufe, Tests und bewährte Praktiken.
> 
> **Letzte Aktualisierung**: 30. Oktober 2025 | **Dokumentversion**: 3.0

## Inhaltsverzeichnis

- [Projektübersicht](../..)
- [Repository-Struktur](../..)
- [Voraussetzungen](../..)
- [Einrichtungsbefehle](../..)
- [Entwicklungsablauf](../..)
- [Testanweisungen](../..)
- [Richtlinien für Code-Stil](../..)
- [Richtlinien für Pull Requests](../..)
- [Übersetzungssystem](../..)
- [Foundry Local Integration](../..)
- [Build und Bereitstellung](../..)
- [Häufige Probleme und Fehlerbehebung](../..)
- [Zusätzliche Ressourcen](../..)
- [Projektspezifische Hinweise](../..)
- [Hilfe erhalten](../..)

## Projektübersicht

EdgeAI für Anfänger ist ein umfassendes Bildungs-Repository, das die Entwicklung von Edge AI mit Small Language Models (SLMs) lehrt. Der Kurs behandelt die Grundlagen von EdgeAI, die Bereitstellung von Modellen, Optimierungstechniken und produktionsreife Implementierungen mit Microsoft Foundry Local und verschiedenen KI-Frameworks.

**Wichtige Technologien:**
- Python 3.8+ (Primärsprache für AI/ML-Beispiele)
- .NET C# (AI/ML-Beispiele)
- JavaScript/Node.js mit Electron (für Desktop-Anwendungen)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- KI-Frameworks: LangChain, Semantic Kernel, Chainlit
- Modelloptimierung: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Repository-Typ:** Bildungsinhalts-Repository mit 8 Modulen und 10 umfassenden Beispielanwendungen

**Architektur:** Mehrmoduliger Lernpfad mit praktischen Beispielen, die Edge AI-Bereitstellungsmuster demonstrieren

## Repository-Struktur

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Voraussetzungen

### Erforderliche Tools

- **Python 3.8+** - Für AI/ML-Beispiele und Notebooks
- **Node.js 16+** - Für die Electron-Beispielanwendung
- **Git** - Für Versionskontrolle
- **Microsoft Foundry Local** - Für das lokale Ausführen von KI-Modellen

### Empfohlene Tools

- **Visual Studio Code** - Mit Python-, Jupyter- und Pylance-Erweiterungen
- **Windows Terminal** - Für eine bessere Kommandozeilenerfahrung (Windows-Nutzer)
- **Docker** - Für containerisierte Entwicklung (optional)

### Systemanforderungen

- **RAM**: Mindestens 8GB, empfohlen 16GB+ für Multi-Modell-Szenarien
- **Speicherplatz**: Mindestens 10GB freier Speicherplatz für Modelle und Abhängigkeiten
- **Betriebssystem**: Windows 10/11, macOS 11+ oder Linux (Ubuntu 20.04+)
- **Hardware**: CPU mit AVX2-Unterstützung; GPU (CUDA, Qualcomm NPU) optional, aber empfohlen

### Wissensvoraussetzungen

- Grundlegendes Verständnis der Python-Programmierung
- Vertrautheit mit Kommandozeilen-Schnittstellen
- Verständnis von AI/ML-Konzepten (für die Entwicklung von Beispielen)
- Git-Workflows und Pull-Request-Prozesse

## Einrichtungsbefehle

### Repository-Einrichtung

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python-Beispiel-Einrichtung (Module08 und Workshop-Beispiele)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.js-Beispiel-Einrichtung (Beispiel 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local Einrichtung

Foundry Local ist erforderlich, um die Beispiele auszuführen. Laden Sie es aus dem offiziellen Repository herunter und installieren Sie es:

**Installation:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuell**: Download von der [Releases-Seite](https://github.com/microsoft/Foundry-Local/releases)

**Schnellstart:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Hinweis**: Foundry Local wählt automatisch die beste Modellvariante für Ihre Hardware aus (CUDA GPU, Qualcomm NPU oder CPU).

## Entwicklungsablauf

### Inhaltsentwicklung

Dieses Repository enthält hauptsächlich **Markdown-Bildungsinhalte**. Beim Bearbeiten:

1. Bearbeiten Sie `.md`-Dateien in den entsprechenden Modulverzeichnissen
2. Folgen Sie den bestehenden Formatierungsmustern
3. Stellen Sie sicher, dass Codebeispiele korrekt und getestet sind
4. Aktualisieren Sie die entsprechenden übersetzten Inhalte, falls erforderlich (oder lassen Sie die Automatisierung dies übernehmen)

### Entwicklung von Beispielanwendungen

Für Python-Beispiele aus Modul08 (Beispiele 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Für Workshop-Python-Beispiele:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Für Electron-Beispiel (Beispiel 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testen von Beispielanwendungen

Python-Beispiele haben keine automatisierten Tests, können jedoch durch Ausführung validiert werden:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Das Electron-Beispiel verfügt über eine Testinfrastruktur:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Testanweisungen

### Inhaltsvalidierung

Das Repository verwendet automatisierte Übersetzungs-Workflows. Manuelles Testen ist für Übersetzungen nicht erforderlich.

**Manuelle Validierung für Inhaltsänderungen:**
1. Überprüfen Sie die Markdown-Darstellung durch Vorschau der `.md`-Dateien
2. Stellen Sie sicher, dass alle Links auf gültige Ziele verweisen
3. Testen Sie alle im Dokument enthaltenen Code-Snippets
4. Überprüfen Sie, ob Bilder korrekt geladen werden

### Testen von Beispielanwendungen

**Modul08/Beispiele/08 (Electron-App) verfügt über umfassende Tests:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python-Beispiele sollten manuell getestet werden:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Richtlinien für Code-Stil

### Markdown-Inhalt

- Verwenden Sie eine konsistente Überschriftenhierarchie (# für Titel, ## für Hauptabschnitte, ### für Unterabschnitte)
- Fügen Sie Codeblöcke mit Sprachspezifikatoren ein: ```python, ```bash, ```javascript
- Folgen Sie der bestehenden Formatierung für Tabellen, Listen und Hervorhebungen
- Halten Sie Zeilen lesbar (zielen Sie auf ~80-100 Zeichen, aber nicht strikt)
- Verwenden Sie relative Links für interne Verweise

### Python-Code-Stil

- Befolgen Sie die PEP 8-Konventionen
- Verwenden Sie Typ-Hinweise, wo angebracht
- Fügen Sie Docstrings für Funktionen und Klassen hinzu
- Verwenden Sie aussagekräftige Variablennamen
- Halten Sie Funktionen fokussiert und prägnant

### JavaScript/Node.js Code-Stil

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Wichtige Konventionen:**
- ESLint-Konfiguration im Beispiel 08 bereitgestellt
- Prettier für Code-Formatierung
- Verwenden Sie moderne ES6+-Syntax
- Folgen Sie bestehenden Mustern im Codebase

## Richtlinien für Pull Requests

### Beitragsablauf

1. **Forken Sie das Repository** und erstellen Sie einen neuen Branch von `main`
2. **Nehmen Sie Ihre Änderungen vor** gemäß den Richtlinien für den Code-Stil
3. **Testen Sie gründlich** gemäß den oben genannten Testanweisungen
4. **Commiten Sie mit klaren Nachrichten** gemäß dem Format für konventionelle Commits
5. **Pushen Sie zu Ihrem Fork** und erstellen Sie einen Pull-Request
6. **Reagieren Sie auf Feedback** von Maintainer während der Überprüfung

### Branch-Namenskonvention

- `feature/<module>-<beschreibung>` - Für neue Funktionen oder Inhalte
- `fix/<module>-<beschreibung>` - Für Fehlerbehebungen
- `docs/<beschreibung>` - Für Dokumentationsverbesserungen
- `refactor/<beschreibung>` - Für Code-Refactoring

### Commit-Nachrichtenformat

Befolgen Sie [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Beispiele:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Titel-Format
```
[ModuleXX] Brief description of change
```
oder
```
[Module08/samples/XX] Description for sample changes
```

### Verhaltenskodex

Alle Mitwirkenden müssen den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) befolgen. Bitte lesen Sie [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), bevor Sie Beiträge leisten.

### Vor dem Einreichen

**Für Inhaltsänderungen:**
- Vorschau aller geänderten Markdown-Dateien
- Überprüfen Sie, ob Links und Bilder funktionieren
- Überprüfen Sie auf Tippfehler und grammatikalische Fehler

**Für Änderungen an Beispielcode (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Für Änderungen an Python-Beispielen:**
- Testen Sie, ob das Beispiel erfolgreich ausgeführt wird
- Überprüfen Sie, ob die Fehlerbehandlung funktioniert
- Überprüfen Sie die Kompatibilität mit Foundry Local

### Überprüfungsprozess

- Änderungen an Bildungsinhalten werden auf Genauigkeit und Klarheit überprüft
- Codebeispiele werden auf Funktionalität getestet
- Übersetzungsaktualisierungen werden automatisch von GitHub Actions gehandhabt

## Übersetzungssystem

**WICHTIG:** Dieses Repository verwendet automatisierte Übersetzung über GitHub Actions.

- Übersetzungen befinden sich im Verzeichnis `/translations/` (50+ Sprachen)
- Automatisiert über `co-op-translator.yml` Workflow
- **Bearbeiten Sie Übersetzungsdateien NICHT manuell** - sie werden überschrieben
- Bearbeiten Sie nur englische Quelldateien im Root- und Modulverzeichnis
- Übersetzungen werden automatisch bei Push auf den `main`-Branch generiert

## Foundry Local Integration

Die meisten Modul08-Beispiele erfordern, dass Microsoft Foundry Local ausgeführt wird.

### Installation & Einrichtung

**Installieren Sie Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installieren Sie das Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local starten
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK-Nutzung (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local überprüfen
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Umgebungsvariablen für Beispiele

Die meisten Beispiele verwenden diese Umgebungsvariablen:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Hinweis**: Bei Verwendung von `FoundryLocalManager` übernimmt das SDK automatisch die Dienstsuche und das Laden von Modellen. Modell-Aliase (wie `phi-3.5-mini`) stellen sicher, dass die beste Variante für Ihre Hardware ausgewählt wird.

## Build und Bereitstellung

### Inhaltsbereitstellung

Dieses Repository besteht hauptsächlich aus Dokumentation - kein Build-Prozess erforderlich für Inhalte.

### Build von Beispielanwendungen

**Electron-Anwendung (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python-Beispiele:**
Kein Build-Prozess - Beispiele werden direkt mit dem Python-Interpreter ausgeführt.

## Häufige Probleme und Fehlerbehebung

> **Tipp**: Überprüfen Sie [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) für bekannte Probleme und Lösungen.

### Kritische Probleme (Blockierend)

#### Foundry Local läuft nicht
**Problem:** Beispiele schlagen mit Verbindungsfehlern fehl

**Lösung:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Häufige Probleme (Moderat)

#### Probleme mit Python-Virtual Environment
**Problem:** Modulimportfehler

**Lösung:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron-Build-Probleme
**Problem:** npm install oder Build-Fehler

**Lösung:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Workflow-Probleme (Geringfügig)

#### Konflikte im Übersetzungs-Workflow
**Problem:** Übersetzungs-PR steht im Konflikt mit Ihren Änderungen

**Lösung:**
- Bearbeiten Sie nur englische Quelldateien
- Lassen Sie den automatisierten Übersetzungs-Workflow die Übersetzungen übernehmen
- Wenn Konflikte auftreten, führen Sie `main` in Ihren Branch zusammen, nachdem die Übersetzungen zusammengeführt wurden

#### Modell-Download-Fehler
**Problem:** Foundry Local kann Modelle nicht herunterladen

**Lösung:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Zusätzliche Ressourcen

### Lernpfade
- **Anfängerpfad:** Module 01-02 (7-9 Stunden)
- **Fortgeschrittenenpfad:** Module 03-04 (9-11 Stunden)
- **Expertenpfad:** Module 05-07 (12-15 Stunden)
- **Meisterpfad:** Modul 08 (8-10 Stunden)
- **Praxis-Workshop:** Workshop-Materialien (6-8 Stunden)

### Wichtige Modul-Inhalte
- **Modul01:** Grundlagen von EdgeAI und Fallstudien aus der Praxis
- **Modul02:** Small Language Model (SLM)-Familien und Architekturen
- **Modul03:** Lokale und Cloud-Bereitstellungsstrategien
- **Modul04:** Modelloptimierung mit mehreren Frameworks (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - Produktionsbetrieb
- **Modul06:** KI-Agenten und Funktionsaufrufe
- **Modul07:** Plattform-spezifische Implementierungen
- **Modul08:** Foundry Local Toolkit mit 10 umfassenden Beispielen

### Externe Abhängigkeiten
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokale KI-Modell-Laufzeit mit OpenAI-kompatibler API
  - [Dokumentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Optimierungsframework
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Modelloptimierungstoolkit
- [OpenVINO](https://docs.openvino.ai/) - Intels Optimierungstoolkit

## Projektspezifische Hinweise

### Modul08 Beispielanwendungen

Das Repository enthält 10 umfassende Beispielanwendungen:

1. **01-REST Chat Quickstart** - Grundlegende OpenAI SDK-Integration
2. **02-OpenAI SDK Integration** - Erweiterte SDK-Funktionen
3. **03-Modellentdeckung & Benchmarking** - Modellvergleichstools
4. **04-Chainlit RAG Anwendung** - Retrieval-augmented generation
5. **05-Multi-Agenten-Orchestrierung** - Grundlegende Agentenkoordination
6. **06-Models-as-Tools Router** - Intelligentes Modell-Routing
7. **07-Direct API Client** - Low-Level API-Integration
8. **08-Windows 11 Chat App** - Native Electron-Desktopanwendung
9. **09-Erweiterte Multi-Agenten-Systeme** - Komplexe Agentenkoordination
10. **10-Foundry Tools Framework** - Integration von LangChain/Semantic Kernel

### Workshop-Beispielanwendungen

Der Workshop umfasst 6 aufeinander aufbauende Sitzungen mit praktischen Umsetzungen:

1. **Sitzung 01** - Chat-Bootstrap mit Foundry Local-Integration
2. **Sitzung 02** - RAG-Pipeline und Bewertung mit RAGAS
3. **Sitzung 03** - Benchmarking von Open-Source-Modellen
4. **Sitzung 04** - Modellvergleich und -auswahl
5. **Sitzung 05** - Multi-Agent-Orchestrierungssysteme
6. **Sitzung 06** - Modell-Routing und Pipeline-Management

Jedes Beispiel zeigt verschiedene Aspekte der Edge-AI-Entwicklung mit Foundry Local.

### Leistungsüberlegungen

- SLMs sind für Edge-Einsatz optimiert (2-16GB RAM)
- Lokale Inferenz bietet Antwortzeiten von 50-500ms
- Quantisierungstechniken reduzieren die Größe um 75% bei 85% Leistungserhalt
- Echtzeit-Gesprächsfähigkeiten mit lokalen Modellen

### Sicherheit und Datenschutz

- Alle Verarbeitung erfolgt lokal – keine Daten werden in die Cloud gesendet
- Geeignet für datenschutzsensible Anwendungen (Gesundheitswesen, Finanzen)
- Erfüllt Anforderungen an Datenhoheit
- Foundry Local läuft vollständig auf lokaler Hardware

## Hilfe erhalten

### Dokumentation

- **Haupt-README**: [README.md](README.md) - Überblick über das Repository und Lernpfade
- **Studienleitfaden**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Lernressourcen und Zeitplan
- **Support**: [SUPPORT.md](SUPPORT.md) - Wie man Hilfe bekommt
- **Sicherheit**: [SECURITY.md](SECURITY.md) - Melden von Sicherheitsproblemen

### Community-Support

- **GitHub Issues**: [Fehler melden oder Funktionen anfordern](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Fragen stellen und Ideen teilen](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Technische Probleme mit Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Maintainer**: Siehe [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Sicherheitsprobleme**: Verantwortungsvolle Offenlegung gemäß [SECURITY.md](SECURITY.md)
- **Microsoft Support**: Für Unternehmenssupport kontaktieren Sie den Microsoft-Kundendienst

### Zusätzliche Ressourcen

- **Microsoft Learn**: [Lernpfade zu KI und maschinellem Lernen](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentation**: [Offizielle Dokumentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Community-Beispiele**: Schauen Sie in [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) nach Beiträgen der Community

---

**Dies ist ein Bildungs-Repository, das sich auf die Vermittlung der Entwicklung von Edge-AI konzentriert. Das Hauptziel ist die Verbesserung von Bildungsinhalten und das Hinzufügen/Erweitern von Beispielanwendungen, die Edge-AI-Konzepte demonstrieren.**

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.