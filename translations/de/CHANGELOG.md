<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T10:39:27+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "de"
}
-->
# Änderungsprotokoll

Alle wichtigen Änderungen an EdgeAI for Beginners sind hier dokumentiert. Dieses Projekt verwendet datumsbasierte Einträge und den Stil von Keep a Changelog (Hinzugefügt, Geändert, Behoben, Entfernt, Dokumentation, Verschoben).

## 2025-10-30

### Hinzugefügt - Umfassende Erweiterung der Module06 AI Agents
- **Integration des Microsoft Agent Frameworks** (`Module06/01.IntroduceAgent.md`):
  - Vollständiger Abschnitt über das Microsoft Agent Framework für die Entwicklung produktionsreifer Agenten
  - Detaillierte Integrationsmuster mit Foundry Local für Edge-Bereitstellungen
  - Beispiele für die Orchestrierung von Multi-Agenten mit spezialisierten SLM-Modellen
  - Muster für Unternehmensbereitstellungen mit Ressourcenmanagement und Überwachung
  - Sicherheits- und Compliance-Funktionen für Edge-Agentensysteme
  - Beispiele für reale Implementierungen (Einzelhandel, Gesundheitswesen, Kundenservice)

- **Strategien für die Bereitstellung von Produktions-SLM-Agenten**:
  - **Foundry Local**: Vollständige Dokumentation der Unternehmens-Edge-AI-Laufzeit mit Installation, Konfiguration und Produktionsmustern
  - **Ollama**: Verbesserte Community-orientierte Bereitstellung mit umfassender Überwachung und Modellmanagement
  - **VLLM**: Hochleistungs-Inferenz-Engine mit fortschrittlichen Optimierungstechniken und Unternehmensfunktionen
  - Checklisten für Produktionsbereitstellungen und Vergleichstabellen für alle drei Plattformen

- **Erweiterung der Edge-optimierten SLM-Frameworks**:
  - **ONNX Runtime**: Neuer umfassender Abschnitt für plattformübergreifende SLM-Agenten-Bereitstellung
  - Universelle Bereitstellungsmuster für Windows, Linux, macOS, iOS und Android
  - Hardware-Beschleunigungsoptionen (CPU, GPU, NPU) mit automatischer Erkennung
  - Produktionsreife Funktionen und agentenspezifische Optimierungen
  - Vollständige Implementierungsbeispiele mit Integration des Microsoft Agent Frameworks

- **Referenzen und weiterführende Literatur**:
  - Umfassende Ressourcenbibliothek mit über 100 maßgeblichen Quellen
  - Kernforschungspapiere zu KI-Agenten und Small Language Models
  - Offizielle Dokumentation für alle wichtigen Frameworks und Tools
  - Branchenberichte, Marktanalysen und technische Benchmarks
  - Bildungsressourcen, Konferenzen und Community-Foren
  - Standards, Spezifikationen und Compliance-Frameworks

### Geändert - Modernisierung der Inhalte von Module06
- **Erweiterte Lernziele**: Hinzugefügt wurde die Beherrschung des Microsoft Agent Frameworks und der Edge-Bereitstellungsfähigkeiten
- **Produktionsfokus**: Wechsel von konzeptionellen zu umsetzungsbereiten Anleitungen mit Produktionsbeispielen
- **Code-Beispiele**: Aktualisierung aller Beispiele mit modernen SDK-Mustern und Best Practices
- **Architekturmuster**: Hinzugefügt wurden hierarchische Agentenarchitekturen und Edge-to-Cloud-Koordination
- **Leistungsoptimierung**: Verbesserungen mit Ressourcenmanagement und Empfehlungen zur automatischen Skalierung

### Dokumentation - Strukturverbesserung von Module06
- **Umfassende Abdeckung des Agent Frameworks**: Von grundlegenden Konzepten bis hin zur Unternehmensbereitstellung
- **Strategien für Produktionsbereitstellungen**: Vollständige Anleitungen für Foundry Local, Ollama und VLLM
- **Plattformübergreifende Optimierung**: Hinzugefügt wurde ONNX Runtime für universelle Bereitstellungen
- **Ressourcenbibliothek**: Umfangreiche Referenzen für kontinuierliches Lernen und Implementierung

### Hinzugefügt - Aktualisierung der Dokumentation des Module06 Model Context Protocol (MCP)
- **Modernisierung der MCP-Einführung** (`Module06/03.IntroduceMCP.md`):
  - Aktualisiert mit den neuesten MCP-Spezifikationen von modelcontextprotocol.io (Version vom 18.06.2025)
  - Hinzugefügt wurde die offizielle USB-C-Analogie für standardisierte KI-Anwendungsanschlüsse
  - Aktualisierung des Architekturabschnitts mit offiziellem Zwei-Schichten-Design (Datenebene + Transporteebene)
  - Erweiterte Dokumentation der Kernprimitive mit Server-Primitiven (Tools, Ressourcen, Prompts) und Client-Primitiven (Sampling, Elicitation, Logging)

- **Umfassende MCP-Referenzen und Ressourcen**:
  - Hinzugefügt wurde der Link **MCP für Anfänger** (https://aka.ms/mcp-for-beginners)
  - Offizielle MCP-Dokumentation und Spezifikationen (modelcontextprotocol.io)
  - Entwicklungsressourcen einschließlich MCP Inspector und Referenzimplementierungen
  - Technische Standards (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Hinzugefügt - Qualcomm QNN-Integration in Module04
- **Neuer Abschnitt 7: Qualcomm QNN Optimierungssuite** (`Module04/05.QualcommQNN.md`):
  - Umfassender Leitfaden mit über 400 Zeilen zu Qualcomms einheitlichem KI-Inferenz-Framework
  - Detaillierte Abdeckung des heterogenen Computing (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardwarebewusste Optimierung für Snapdragon-Plattformen mit intelligenter Arbeitslastverteilung
  - Fortgeschrittene Quantisierungstechniken (INT8, INT16, gemischte Präzision) für mobile Bereitstellungen
  - Energieeffiziente Inferenzoptimierung für batteriebetriebene Geräte und Echtzeitanwendungen
  - Vollständiger Installationsleitfaden mit QNN-SDK-Setup und Konfiguration der Umgebung
  - Praktische Beispiele: PyTorch-zu-QNN-Konvertierung, Multi-Backend-Optimierung, Kontext-Binärgenerierung
  - Fortgeschrittene Nutzungsmuster: benutzerdefinierte Backend-Konfiguration, dynamische Quantisierung, Leistungsprofilierung
  - Umfassender Abschnitt zur Fehlerbehebung und Community-Ressourcen

- **Verbesserte Struktur von Module04**:
  - Aktualisierte README.md, um 7 progressive Abschnitte einzuschließen (vorher 6)
  - Hinzugefügt wurde Qualcomm QNN zur Leistungstabelle (5-15x Geschwindigkeitsverbesserung, 50-80% Speicherreduktion)
  - Umfassende Lernziele für mobile KI-Bereitstellung und Energieoptimierung

### Geändert - Dokumentationsaktualisierungen für Module04
- **Verbesserung der Microsoft Olive-Dokumentation** (`Module04/03.MicrosoftOlive.md`):
  - Hinzugefügt wurde der umfassende Abschnitt "Olive Recipes Repository" mit über 100 vorgefertigten Optimierungsrezepten
  - Detaillierte Abdeckung unterstützter Modellfamilien (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktische Anwendungsbeispiele für Rezeptanpassung und Community-Beiträge
  - Verbesserungen mit Leistungsbenchmarks und Integrationsanleitungen

- **Abschnittsreihenfolge in Module04 geändert**:
  - Apple MLX verschoben auf Abschnitt 5 (vorher Abschnitt 6)
  - Workflow-Synthese verschoben auf Abschnitt 6 (vorher Abschnitt 7)
  - Qualcomm QNN positioniert als Abschnitt 7 (spezialisierter Fokus auf mobile/Edge-Bereitstellung)
  - Alle Dateireferenzen und Navigationslinks entsprechend aktualisiert

### Behoben - Validierung von Workshop-Beispielen
- **chat_bootstrap.py Validierung und Reparatur**:
  - Korrigierte beschädigte Importanweisung (`util.util.workshop_utils` → `util.workshop_utils`)
  - Erstellte fehlende `__init__.py` im util-Paket für ordnungsgemäße Python-Modulauflösung
  - Installierte erforderliche Abhängigkeiten (openai, foundry-local-sdk) in der Conda-Umgebung
  - Erfolgreich validierte Beispielausführung mit sowohl Standard- als auch benutzerdefinierten Prompts
  - Bestätigte Integration mit Foundry Local-Dienst und Modellladung (phi-4-mini mit CUDA-Optimierung)

### Dokumentation - Umfassende Leitfadenaktualisierungen
- **Module04 README.md komplett umstrukturiert**:
  - Hinzugefügt wurde Qualcomm QNN als wichtiges Optimierungsframework neben OpenVINO, Olive, MLX
  - Aktualisierte Kapitel-Lernziele, um mobile KI-Bereitstellung und Energieoptimierung einzuschließen
  - Verbesserte Leistungstabelle mit QNN-Metriken und mobilen/Edge-Anwendungsfällen
  - Logische Progression von Unternehmenslösungen zu plattformspezifischen Optimierungen beibehalten

- **Querverweise und Navigation**:
  - Aktualisierte alle internen Links und Dateireferenzen für neue Abschnittsnummerierung
  - Verbesserte Beschreibung der Workflow-Synthese, um mobile, Desktop- und Cloud-Umgebungen einzuschließen
  - Hinzugefügt wurden umfassende Ressourcenlinks für das Qualcomm-Entwickler-Ökosystem

## 2025-10-08

### Hinzugefügt - Umfassendes Workshop-Update
- **Workshop README.md komplett neu geschrieben**:
  - Umfassende Einführung hinzugefügt, die den Wert von Edge AI erklärt (Datenschutz, Leistung, Kosten)
  - 6 Kernlernziele mit detaillierten Kompetenzen erstellt
  - Lernziel-Tabelle mit Ergebnissen und Kompetenzmatrix hinzugefügt
  - Abschnitt zu karrierebereiten Fähigkeiten für Branchenrelevanz hinzugefügt
  - Schnellstartanleitung mit Voraussetzungen und 3-Schritt-Setup hinzugefügt
  - Ressourcentabellen für Python-Beispiele erstellt (8 Dateien mit Laufzeiten)
  - Jupyter-Notebook-Tabelle hinzugefügt (8 Notebooks mit Schwierigkeitsbewertungen)
  - Dokumentationstabelle erstellt (7 wichtige Dokumente mit "Verwendungszweck"-Hinweisen)
  - Lernpfadempfehlungen für verschiedene Fähigkeitsstufen hinzugefügt

- **Validierungs- und Testinfrastruktur für Workshops**:
  - `scripts/validate_samples.py` erstellt - Umfassendes Validierungstool für Syntax, Importe und Best Practices
  - `scripts/test_samples.py` erstellt - Smoke-Test-Runner für alle Python-Beispiele
  - Validierungsdokumentation zu `scripts/README.md` hinzugefügt

- **Umfassende Dokumentation**:
  - `SAMPLES_UPDATE_SUMMARY.md` erstellt - Detaillierter Leitfaden mit über 400 Zeilen zu allen Verbesserungen
  - `UPDATE_COMPLETE.md` erstellt - Zusammenfassung der Update-Fertigstellung
  - `QUICK_REFERENCE.md` erstellt - Schnellreferenzkarte für den Workshop

### Geändert - Modernisierung der Python-Beispiele im Workshop
- **Alle 8 Python-Beispiele mit Best Practices aktualisiert**:
  - Verbesserte Fehlerbehandlung mit try-except-Blöcken um alle I/O-Operationen
  - Typ-Hinweise und umfassende Docstrings hinzugefügt
  - Konsistentes [INFO]/[ERROR]/[RESULT]-Logging-Muster implementiert
  - Optionale Importe mit Installationshinweisen geschützt
  - Benutzerfeedback in allen Beispielen verbessert

- **session01/chat_bootstrap.py**:
  - Verbesserte Client-Initialisierung mit umfassenden Fehlermeldungen
  - Verbesserte Fehlerbehandlung beim Streaming mit Chunk-Validierung
  - Bessere Ausnahmebehandlung bei Dienstunverfügbarkeit hinzugefügt

- **session02/rag_pipeline.py**:
  - Importguards für sentence-transformers mit Installationshinweisen hinzugefügt
  - Verbesserte Fehlerbehandlung für Einbettungs- und Generierungsoperationen
  - Verbesserte Ausgabeformatierung mit strukturierten Ergebnissen

- **session02/rag_eval_ragas.py**:
  - Optionale Importe (ragas, datasets) mit benutzerfreundlichen Fehlermeldungen geschützt
  - Fehlerbehandlung für Bewertungsmetriken hinzugefügt
  - Verbesserte Ausgabeformatierung für Bewertungsergebnisse

- **session03/benchmark_oss_models.py**:
  - Implementierte sanfte Degradierung (fortgesetzt bei Modellfehlern)
  - Detaillierte Fortschrittsberichte und Fehlerbehandlung pro Modell hinzugefügt
  - Verbesserte Statistikberechnung mit umfassender Fehlerbehebung

- **session04/model_compare.py**:
  - Typ-Hinweise hinzugefügt (Tuple-Rückgabetypen)
  - Verbesserte Ausgabeformatierung mit strukturierten JSON-Ergebnissen
  - Fehlerbehandlung pro Modell mit Wiederherstellung implementiert

- **session05/agents_orchestrator.py**:
  - Agent.act() mit umfassenden Docstrings verbessert
  - Fehlerbehandlung in der Pipeline mit Stufen-Logging hinzugefügt
  - Verbesserte Speicherverwaltung und Statusverfolgung

- **session06/models_router.py**:
  - Funktionsdokumentation für alle Routing-Komponenten verbessert
  - Detailliertes Logging in der route()-Funktion hinzugefügt
  - Verbesserte Testausgabe mit strukturierten Ergebnissen

- **session06/models_pipeline.py**:
  - Fehlerbehandlung zur chat()-Hilfsfunktion hinzugefügt
  - Pipeline() mit Stufen-Logging und Fortschrittsberichten verbessert
  - main() mit umfassender Fehlerbehebung verbessert

### Dokumentation - Verbesserung der Workshop-Dokumentation
- Haupt-README.md mit Workshop-Abschnitt aktualisiert, der den praktischen Lernpfad hervorhebt
- STUDY_GUIDE.md mit umfassendem Workshop-Abschnitt verbessert, einschließlich:
  - Lernziele und Studienschwerpunkte
  - Selbstbewertungsfragen
  - Praktische Übungen mit Zeitangaben
  - Zeitaufteilung für konzentriertes und Teilzeitstudium
  - Workshop zur Fortschrittsverfolgungsvorlage hinzugefügt
- Zeitaufteilung von 20 Stunden auf 30 Stunden aktualisiert (einschließlich Workshop)
- Workshop-Beispielbeschreibungen und Lernziele zur README hinzugefügt

### Behoben
- Inkonsistente Fehlerbehandlungsmuster in Workshop-Beispielen behoben
- Fehler bei optionalen Abhängigkeitsimporten mit ordnungsgemäßen Guards behoben
- Fehlende Typ-Hinweise in kritischen Funktionen korrigiert
- Unzureichendes Benutzerfeedback in Fehlerszenarien adressiert
- Validierungsprobleme mit umfassender Testinfrastruktur behoben

---

## 2025-09-23

### Geändert - Große Modernisierung von Module 08
- **Umfassende Angleichung an Microsoft Foundry-Local Repository-Muster**
  - Alle Code-Beispiele aktualisiert, um moderne `FoundryLocalManager`- und OpenAI-SDK-Integration zu verwenden
  - Veraltete manuelle `requests`-Aufrufe durch ordnungsgemäße SDK-Nutzung ersetzt
  - Implementierungsmuster an offizielle Microsoft-Dokumentation und Beispiele angepasst

- **05.AIPoweredAgents.md Modernisierung**:
  - Multi-Agenten-Orchestrierung aktualisiert, um moderne SDK-Muster zu verwenden
  - Verbesserte Koordinator-Implementierung mit erweiterten Funktionen (Feedback-Schleifen, Leistungsüberwachung)
  - Umfassende Fehlerbehandlung und Dienstgesundheitsprüfung hinzugefügt
  - Richtige Referenzen zu lokalen Beispielen (`samples/05/multi_agent_orchestration.ipynb`) integriert
  - Funktionsaufruf-Beispiele aktualisiert, um moderne `tools`-Parameter anstelle veralteter `functions` zu verwenden
  - Produktionsreife Muster mit Überwachung und Statistikverfolgung hinzugefügt

- **06.ModelsAsTools.md komplett neu geschrieben**:
  - Basis-Tool-Registry durch intelligente Modell-Router-Implementierung ersetzt
  - Schlüsselwortbasierte Modellauswahl für verschiedene Aufgabentypen (allgemein, logisches Denken, Code, kreativ)
  - Umgebungsgestützte Konfiguration mit flexibler Modellzuweisung integriert
  - Verbesserungen mit umfassender Dienstgesundheitsüberwachung und Fehlerbehandlung
  - Produktionsbereitstellungsmuster mit Anforderungsüberwachung und Leistungsnachverfolgung hinzugefügt
  - Angleichung an lokale Implementierung in `samples/06/router.py` und `samples/06/model_router.ipynb`

- **Verbesserungen der Dokumentationsstruktur**:
  - Übersichtskapitel hinzugefügt, die Modernisierung und SDK-Angleichung hervorheben
  - Verbesserungen mit Emojis und besserer Formatierung für verbesserte Lesbarkeit
  - Richtige Referenzen zu lokalen Beispieldateien in der gesamten Dokumentation hinzugefügt
  - Produktionsreife Implementierungsanleitungen und Best Practices enthalten

### Hinzugefügt
- Umfassende Übersichtskapitel in Module 08-Dateien, die moderne SDK-Integration hervorheben
- Architektur-Highlights mit erweiterten Funktionen (Multi-Agenten-Systeme, intelligentes Routing)
- Direkte Referenzen zu lokalen Beispielimplementierungen für praktische Erfahrungen
- Produktionsbereitstellungsanleitungen mit Überwachungs- und Fehlerbehandlungsmustern
- Interaktive Jupyter-Notebook-Beispiele mit erweiterten Funktionen und Benchmarks

### Behoben
- Abweichungen zwischen Dokumentation und tatsächlichen Beispielimplementierungen
- Veraltete SDK-Nutzungsmuster in Module 08
- Fehlende Referenzen zur umfassenden lokalen Beispielsammlung
- Inkonsistente Implementierungsansätze in verschiedenen Abschnitten

---

## 2025-09-18

### Hinzugefügt
- Module 08: Microsoft Foundry Local – Komplettes Entwickler-Toolkit
  - Sechs Sitzungen: Einrichtung, Azure AI Foundry-Integration, Open-Source-Modelle, modernste Demos, Agenten und Modelle-als-Tools
  - Ausführbare Beispiele unter `Module08/samples/01`–`06` mit Windows-Cmd-Anweisungen
    - `01` REST Schnellstart Chat (`chat_quickstart.py`)
    - `02` SDK Schnellstart mit OpenAI/Foundry Local und Azure OpenAI Unterstützung (`sdk_quickstart.py`)
    - `03` CLI Liste-und-Benchmark (`list_and_bench.cmd`)
    - `04` Chainlit Demo (`app.py`)
    - `05` Multi-Agent-Orchestrierung (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools Router (`router.py`)
- Azure OpenAI Unterstützung im SDK-Beispiel von Sitzung 2 mit Konfiguration über Umgebungsvariablen
- `.vscode/settings.json` zeigt auf `Module08/.venv` und verbessert die Python-Analyseauflösung
- `.env` mit `PYTHONPATH` Hinweis für VS Code/Pylance-Erkennung

### Geändert
- Standardmodell auf `phi-4-mini` in allen Module 08-Dokumenten und Beispielen aktualisiert; verbleibende Erwähnungen von `phi-3.5` innerhalb von Module 08 entfernt
- Verbesserungen am Router (`Module08/samples/06/router.py`):
  - Endpunkt-Erkennung über `foundry service status` mit Regex-Parsing
  - `/v1/models` Gesundheitsprüfung beim Start
  - Modellregistrierung über Umgebungsvariablen konfigurierbar (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Anforderungen aktualisiert: `Module08/requirements.txt` enthält jetzt `openai` (zusätzlich zu `requests`, `chainlit`)
- Anleitung für Chainlit-Beispiele klargestellt und Fehlerbehebung hinzugefügt; Importauflösung über Arbeitsbereichseinstellungen

### Behoben
- Importprobleme gelöst:
  - Router hängt nicht mehr von einem nicht existierenden `utils` Modul ab; Funktionen wurden integriert
  - Koordinator verwendet relativen Import (`from .specialists import ...`) und wird über den Modulpfad aufgerufen
  - VS Code/Pylance Konfiguration zur Auflösung von `chainlit` und Paketimporten
- Kleinere Tippfehler in `STUDY_GUIDE.md` korrigiert und Module 08 Abdeckung hinzugefügt

### Entfernt
- Nicht verwendetes `Module08/infra/obs.py` gelöscht und das leere `infra/` Verzeichnis entfernt; Beobachtungsmuster bleiben optional in den Dokumenten erhalten

### Verschoben
- Module 08 Demos unter `Module08/samples` mit nach Sitzungen nummerierten Ordnern konsolidiert
  - Chainlit App nach `samples/04` verschoben
  - Agents nach `samples/05` verschoben und `__init__.py` Dateien für Paketauflösung hinzugefügt

### Dokumentation
- Module 08 Sitzungsdokumente und alle Beispiel-READMEs mit Microsoft Learn und vertrauenswürdigen Anbieterreferenzen angereichert
- `Module08/README.md` mit Übersicht über Beispiele, Router-Konfiguration und Validierungstipps aktualisiert
- `Module07/README.md` Windows Foundry Local Abschnitt anhand der Learn-Dokumente validiert
- `STUDY_GUIDE.md` aktualisiert:
  - Module 08 zur Übersicht, Zeitplänen, Fortschrittsverfolgung hinzugefügt
  - Umfassender Referenzabschnitt hinzugefügt (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (Zusammenfassung)
- Kursarchitektur und Module etabliert (Module 01–07)
- Iterative Modernisierung der Inhalte, Standardisierung der Formatierung und Hinzufügen von Fallstudien
- Erweiterte Abdeckung von Optimierungsframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Unveröffentlicht / Backlog (Vorschläge)
- Optionale Smoke-Tests pro Beispiel zur Validierung der Verfügbarkeit von Foundry Local
- Überprüfung von Übersetzungen zur Angleichung von Modellreferenzen (z. B. `phi-4-mini`) wo angebracht
- Hinzufügen einer minimalen Pyright-Konfiguration, falls Teams arbeitsbereichsweite Strenge bevorzugen

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.