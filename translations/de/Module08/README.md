# Modul 08: Praxis mit Microsoft Foundry Local - Komplettes Entwickler-Toolkit

## Überblick

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) repräsentiert die nächste Generation der Edge-AI-Entwicklung und bietet Entwicklern leistungsstarke Werkzeuge, um KI-Anwendungen lokal zu erstellen, bereitzustellen und zu skalieren, während eine nahtlose Integration mit Azure AI Foundry erhalten bleibt. Dieses Modul bietet eine umfassende Einführung in Foundry Local, von der Installation bis hin zur Entwicklung fortgeschrittener Agenten.

**Wichtige Technologien:**
- Microsoft Foundry Local CLI und SDK
- Integration mit Azure AI Foundry
- Modellinferenz auf dem Gerät
- Lokale Modell-Caching und Optimierung
- Agentenbasierte Architekturen

## Lernziele

Nach Abschluss dieses Moduls werden Sie:

- **Foundry Local meistern**: Installation, Konfiguration und Optimierung für die Entwicklung unter Windows 11
- **Vielfältige Modelle bereitstellen**: Phi-, Qwen-, Deepseek- und GPT-Modelle lokal mit CLI-Befehlen ausführen
- **Produktionslösungen erstellen**: KI-Anwendungen mit fortgeschrittener Prompt-Entwicklung und Datenintegration erstellen
- **Open-Source-Ökosystem nutzen**: Hugging Face-Modelle und Community-Beiträge integrieren
- **KI-Agenten entwickeln**: Intelligente Agenten mit Grounding- und Orchestrierungsfähigkeiten erstellen
- **Enterprise-Muster implementieren**: Modulare, skalierbare KI-Lösungen für die Produktionsbereitstellung entwickeln

## Sitzungsstruktur

### [1: Einführung in Foundry Local](./01.FoundryLocalSetup.md)
**Schwerpunkt**: Installation, CLI-Einrichtung, Modellbereitstellung und Hardware-Optimierung

**Wichtige Themen**: Vollständige Installation • CLI-Befehle • Modell-Caching • Hardware-Beschleunigung • Multi-Modell-Bereitstellung

**Beispiel**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Modellentdeckung & Benchmarking](./samples/03/README.md)

**Dauer**: 2-3 Stunden | **Level**: Anfänger

---

### [2: KI-Lösungen mit Azure AI Foundry erstellen](./02.AzureAIFoundryIntegration.md)
**Schwerpunkt**: Fortgeschrittene Prompt-Entwicklung, Datenintegration und Cloud-Konnektivität

**Wichtige Themen**: Prompt-Entwicklung • Datenintegration • Azure-Workflows • Leistungsoptimierung • Überwachung

**Beispiel**: [Chainlit RAG Anwendung](./samples/04/README.md)

**Dauer**: 2-3 Stunden | **Level**: Mittelstufe

---

### [3: Open-Source-Modelle mit Foundry Local](./03.OpenSourceModels.md)
**Schwerpunkt**: Hugging Face-Integration, BYOM-Strategien und Community-Modelle

**Wichtige Themen**: Hugging Face-Integration • Bring-your-own-model • Model Mondays Einblicke • Community-Beiträge • Modellauswahl

**Beispiel**: [Multi-Agent Orchestrierung](./samples/05/README.md)

**Dauer**: 2-3 Stunden | **Level**: Mittelstufe

---

### [4: Erkundung modernster Modelle](./04.CuttingEdgeModels.md)
**Schwerpunkt**: LLMs vs SLMs, EdgeAI-Implementierung und fortgeschrittene Demos

**Wichtige Themen**: Modellvergleich • Edge- vs Cloud-Inferenz • Phi + ONNX Runtime • Chainlit RAG App • WebGPU-Optimierung

**Beispiel**: [Models-as-Tools Router](./samples/06/README.md)

**Dauer**: 3-4 Stunden | **Level**: Fortgeschritten

---

### [5: Schnelle Entwicklung KI-gestützter Agenten](./05.AIPoweredAgents.md)
**Schwerpunkt**: Agentenarchitekturen, System-Prompts, Grounding und Orchestrierung

**Wichtige Themen**: Agenten-Design-Muster • System-Prompt-Entwicklung • Grounding-Techniken • Multi-Agenten-Systeme • Produktionsbereitstellung

**Beispiel**: [Multi-Agent Orchestrierung](./samples/05/README.md) • [Fortgeschrittenes Multi-Agenten-System](./samples/09/README.md)

**Dauer**: 3-4 Stunden | **Level**: Fortgeschritten

---

### [6: Foundry Local - Modelle als Werkzeuge](./06.ModelsAsTools.md)
**Schwerpunkt**: Modulare KI-Lösungen, Enterprise-Skalierung und Produktionsmuster

**Wichtige Themen**: Modelle als Werkzeuge • Bereitstellung auf dem Gerät • SDK/API-Integration • Enterprise-Architekturen • Skalierungsstrategien

**Beispiel**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Dauer**: 3-4 Stunden | **Level**: Experte

---

### [7: Direkte API-Integrationsmuster](./samples/07/README.md)
**Schwerpunkt**: Pure REST API-Integration ohne SDK-Abhängigkeiten für maximale Kontrolle

**Wichtige Themen**: HTTP-Client-Implementierung • Benutzerdefinierte Authentifizierung • Modell-Gesundheitsüberwachung • Streaming-Antworten • Produktions-Fehlerbehandlung

**Beispiel**: [Direkter API-Client](./samples/07/README.md)

**Dauer**: 2-3 Stunden | **Level**: Mittelstufe

---

### [8: Native Chat-Anwendung für Windows 11](./samples/08/README.md)
**Schwerpunkt**: Entwicklung moderner nativer Chat-Anwendungen mit Foundry Local-Integration

**Wichtige Themen**: Electron-Entwicklung • Fluent Design System • Native Windows-Integration • Echtzeit-Streaming • Chat-Oberflächendesign

**Beispiel**: [Windows 11 Chat-Anwendung](./samples/08/README.md)

**Dauer**: 3-4 Stunden | **Level**: Fortgeschritten

---

### [9: Fortgeschrittene Multi-Agenten-Orchestrierung](./samples/09/README.md)
**Schwerpunkt**: Anspruchsvolle Agenten-Koordination, spezialisierte Aufgabenverteilung und kollaborative KI-Workflows

**Wichtige Themen**: Intelligente Agenten-Koordination • Funktionsaufruf-Muster • Kommunikation zwischen Agenten • Workflow-Orchestrierung • Qualitätssicherungsmechanismen

**Beispiel**: [Fortgeschrittenes Multi-Agenten-System](./samples/09/README.md)

**Dauer**: 4-5 Stunden | **Level**: Experte

---

### [10: Foundry Local als Werkzeug-Framework](./samples/10/README.md)
**Schwerpunkt**: Tool-zentrierte Architektur zur Integration von Foundry Local in bestehende Anwendungen und Frameworks

**Wichtige Themen**: LangChain-Integration • Semantic Kernel-Funktionen • REST API-Frameworks • CLI-Tools • Jupyter-Integration • Produktionsbereitstellungsmuster

**Beispiel**: [Foundry Tools Framework](./samples/10/README.md)

**Dauer**: 4-5 Stunden | **Level**: Experte

## Voraussetzungen

### Systemanforderungen
- **Betriebssystem**: Windows 11 (22H2 oder später)
- **Speicher**: 16GB RAM (32GB empfohlen für größere Modelle)
- **Speicherplatz**: 50GB freier Speicherplatz für Modell-Caching
- **Hardware**: NPU-fähiges Gerät empfohlen (Copilot+ PC), GPU optional
- **Netzwerk**: Hochgeschwindigkeitsinternet für anfängliche Modell-Downloads

### Entwicklungsumgebung
- Visual Studio Code mit AI Toolkit-Erweiterung
- Python 3.10+ und pip
- Git für Versionskontrolle
- PowerShell oder Eingabeaufforderung
- Azure CLI (optional für Cloud-Integration)

### Wissensvoraussetzungen
- Grundlegendes Verständnis von KI/ML-Konzepten
- Vertrautheit mit der Kommandozeile
- Grundkenntnisse in Python-Programmierung
- REST API-Konzepte
- Grundkenntnisse in Prompting und Modellinferenz

## Modul-Zeitplan

**Gesamtschätzzeit**: 30-38 Stunden

| Sitzung | Schwerpunkt | Beispiele | Zeit | Komplexität |
|---------|-------------|-----------|------|-------------|
|  1 | Einrichtung & Grundlagen | 01, 02, 03 | 2-3 Stunden | Anfänger |
|  2 | KI-Lösungen | 04 | 2-3 Stunden | Mittelstufe |
|  3 | Open Source | 05 | 2-3 Stunden | Mittelstufe |
|  4 | Fortgeschrittene Modelle | 06 | 3-4 Stunden | Fortgeschritten |
|  5 | KI-Agenten | 05, 09 | 3-4 Stunden | Fortgeschritten |
|  6 | Enterprise-Werkzeuge | 06, 10 | 3-4 Stunden | Experte |
|  7 | Direkte API-Integration | 07 | 2-3 Stunden | Mittelstufe |
|  8 | Windows 11 Chat-App | 08 | 3-4 Stunden | Fortgeschritten |
|  9 | Fortgeschrittene Multi-Agenten | 09 | 4-5 Stunden | Experte |
| 10 | Werkzeug-Framework | 10 | 4-5 Stunden | Experte |

## Wichtige Ressourcen

**Offizielle Dokumentation:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Quellcode und offizielle Beispiele
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Vollständige Einrichtung und Nutzung
- [Model Mondays Serie](https://aka.ms/model-mondays) - Wöchentliche Modell-Highlights und Tutorials

**Community & Support:**
- [Foundry Local Diskussionen](https://github.com/microsoft/Foundry-Local/discussions) - Community Q&A und Funktionsanfragen
- [Microsoft AI Entwickler-Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Neuigkeiten und Best Practices

## Lernergebnisse

Nach Abschluss dieses Moduls sind Sie in der Lage:

### Technische Fähigkeiten
- **Bereitstellen und Verwalten**: Foundry Local-Installationen in Entwicklungs- und Produktionsumgebungen
- **Modelle integrieren**: Nahtlose Arbeit mit verschiedenen Modellfamilien von Microsoft, Hugging Face und Community-Quellen
- **Anwendungen erstellen**: Produktionsreife KI-Anwendungen mit fortgeschrittenen Funktionen und Optimierungen erstellen
- **Agenten entwickeln**: Anspruchsvolle KI-Agenten mit Grounding, Reasoning und Tool-Integration implementieren

### Strategisches Verständnis
- **Architekturentscheidungen**: Informierte Entscheidungen zwischen lokaler und Cloud-Bereitstellung treffen
- **Leistungsoptimierung**: Inferenzleistung über verschiedene Hardware-Konfigurationen optimieren
- **Enterprise-Skalierung**: Anwendungen entwerfen, die von lokalen Prototypen bis zu Enterprise-Bereitstellungen skalieren
- **Datenschutz und Sicherheit**: Datenschutzfreundliche KI-Lösungen mit lokaler Inferenz implementieren

### Innovationsfähigkeiten
- **Schnelles Prototyping**: KI-Anwendungskonzepte schnell erstellen und testen, basierend auf allen 10 Beispielmustern
- **Community-Integration**: Open-Source-Modelle nutzen und zum Ökosystem beitragen
- **Fortgeschrittene Muster**: Modernste KI-Muster wie RAG, Agenten und Tool-Integration implementieren
- **Framework-Beherrschung**: Expertenintegration mit LangChain, Semantic Kernel, Chainlit und Electron
- **Produktionsbereitstellung**: Skalierbare KI-Lösungen von lokalen Prototypen bis zu Enterprise-Systemen bereitstellen
- **Zukunftssichere Entwicklung**: Anwendungen erstellen, die für aufkommende KI-Technologien und Muster bereit sind

## Erste Schritte

1. **Umgebung einrichten**: Stellen Sie sicher, dass Windows 11 mit empfohlener Hardware vorhanden ist (siehe Voraussetzungen)
2. **Foundry Local installieren**: Folgen Sie Sitzung 1 für vollständige Installation und Konfiguration
3. **Beispiel 01 ausführen**: Beginnen Sie mit der grundlegenden REST API-Integration, um die Einrichtung zu überprüfen
4. **Fortschritt durch Beispiele**: Schließen Sie die Beispiele 01-10 für umfassende Beherrschung ab

## Erfolgskriterien

Verfolgen Sie Ihren Fortschritt durch alle 10 umfassenden Beispiele:

### Grundlagenebene (Beispiele 01-03)
- [ ] Foundry Local erfolgreich installieren und konfigurieren
- [ ] REST API-Integration abschließen (Beispiel 01)
- [ ] OpenAI SDK-Kompatibilität implementieren (Beispiel 02)
- [ ] Modellentdeckung und Benchmarking durchführen (Beispiel 03)

### Anwendungsebene (Beispiele 04-06)
- [ ] Mindestens 4 verschiedene Modellfamilien bereitstellen und ausführen
- [ ] Funktionale RAG-Chat-Anwendung erstellen (Beispiel 04)
- [ ] Multi-Agenten-Orchestrierungssystem erstellen (Beispiel 05)
- [ ] Intelligentes Modell-Routing implementieren (Beispiel 06)

### Fortgeschrittene Integrationsebene (Beispiele 07-10)
- [ ] Produktionsreife API-Clients erstellen (Beispiel 07)
- [ ] Native Chat-Anwendung für Windows 11 entwickeln (Beispiel 08)
- [ ] Fortgeschrittenes Multi-Agenten-System implementieren (Beispiel 09)
- [ ] Umfassendes Werkzeug-Framework erstellen (Beispiel 10)

### Beherrschungsindikatoren
- [ ] Alle 10 Beispiele erfolgreich ohne Fehler ausführen
- [ ] Mindestens 3 Beispiele für spezifische Anwendungsfälle anpassen
- [ ] 2+ Beispiele in produktionsähnlichen Umgebungen bereitstellen
- [ ] Verbesserungen oder Erweiterungen zum Beispielcode beitragen
- [ ] Foundry Local-Muster in persönliche/professionelle Projekte integrieren

## Schnellstart-Anleitung - Alle 10 Beispiele

### Umgebungseinrichtung (Erforderlich für alle Beispiele)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Kern-Grundlagenbeispiele (01-06)

**Beispiel 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Beispiel 02: OpenAI SDK-Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Beispiel 03: Modellentdeckung & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Beispiel 04: Chainlit RAG-Anwendung**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Beispiel 05: Multi-Agenten-Orchestrierung**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Beispiel 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Fortgeschrittene Integrationsbeispiele (07-10)

**Beispiel 07: Direkter API-Client**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Beispiel 08: Windows 11 Chat-Anwendung**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Beispiel 09: Fortgeschrittenes Multi-Agenten-System**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Beispiel 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Häufige Probleme beheben

**Foundry Local-Verbindungsfehler**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Probleme beim Laden von Modellen**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Abhängigkeitsprobleme**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Zusammenfassung
Dieses Modul repräsentiert den neuesten Stand der Edge-AI-Entwicklung und kombiniert Microsofts Unternehmens-Tools mit der Flexibilität und Innovation des Open-Source-Ökosystems. Wenn Sie Foundry Local durch alle 10 umfassenden Beispiele meistern, werden Sie an der Spitze der Entwicklung von KI-Anwendungen stehen.

**Vollständiger Lernpfad:**
- **Grundlagen** (Beispiele 01-03): API-Integration und Modellverwaltung
- **Anwendungen** (Beispiele 04-06): RAG, Agenten und intelligente Weiterleitung
- **Fortgeschritten** (Beispiele 07-10): Produktionsframeworks und Unternehmensintegration

Für die Integration von Azure OpenAI (Session 2) finden Sie die erforderlichen Umgebungsvariablen und API-Versionseinstellungen in den README-Dateien der einzelnen Beispiele.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.