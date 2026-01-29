# Workshop-Notebooks

> **Interaktive Jupyter-Notebooks für praxisnahes Lernen mit Edge AI**
>
> Fortschrittliche, selbstgesteuerte Tutorials, die von einfachen Chat-Komplettierungen bis hin zu fortgeschrittenen Multi-Agenten-Systemen mit Microsoft Foundry Local und Small Language Models reichen.

---

## 📖 Einführung

Willkommen bei der Sammlung der **EdgeAI für Anfänger Workshop-Notebooks**. Diese interaktiven Jupyter-Notebooks bieten eine praktische Lernerfahrung, bei der Sie Edge-AI-Code in Echtzeit schreiben, ausführen und experimentieren können.

### Warum Jupyter-Notebooks?

Im Gegensatz zu traditionellen Tutorials bieten diese Notebooks:

- **Interaktives Lernen**: Führen Sie Code-Zellen aus und sehen Sie sofort Ergebnisse
- **Experimentieren**: Ändern Sie Parameter und beobachten Sie die Auswirkungen in Echtzeit
- **Dokumentation**: Inline-Erklärungen und Markdown-Zellen führen Sie durch die Konzepte
- **Reproduzierbarkeit**: Vollständige funktionierende Beispiele, die Sie als Referenz verwenden und wiederverwenden können
- **Visualisierung**: Anzeigen von Leistungskennzahlen, Einbettungen und Ergebnissen direkt im Notebook

### Was macht diese Notebooks besonders?

Jedes Notebook ist nach **produktiven Best-Practices** gestaltet:

✅ **Umfassende Fehlerbehandlung** - Sanfte Fehlerabfederung und informative Fehlermeldungen  
✅ **Typ-Hinweise & Dokumentation** - Klare Funktionssignaturen und Docstrings  
✅ **Leistungsüberwachung** - Verfolgung der Token-Nutzung und Messung der Latenz  
✅ **Modulares Design** - Wiederverwendbare Muster, die Sie an Ihre Projekte anpassen können  
✅ **Progressive Komplexität** - Systematischer Aufbau auf vorherigen Sitzungen  

---

## 🎯 Lernziele

### Kernkompetenzen, die Sie entwickeln werden

Durch die Arbeit mit diesen Notebooks werden Sie folgende Fähigkeiten meistern:

1. **Management lokaler AI-Dienste**
   - Konfigurieren und Verwalten von Microsoft Foundry Local-Diensten
   - Auswahl und Laden geeigneter Modelle für Ihre Hardware
   - Überwachung der Ressourcennutzung und Optimierung der Leistung
   - Umgang mit Dienstentdeckung und Gesundheitsprüfung

2. **Entwicklung von AI-Anwendungen**
   - Implementieren von OpenAI-kompatiblen Chat-Komplettierungen lokal
   - Aufbau von Streaming-Schnittstellen für eine bessere Benutzererfahrung
   - Gestaltung effektiver Prompts für Small Language Models
   - Integration lokaler Modelle in Anwendungen

3. **Retrieval Augmented Generation (RAG)**
   - Erstellen von semantischer Suche mit Vektoreinbettungen
   - Verankerung von LLM-Antworten in domänenspezifischen Dokumenten
   - Bewertung der RAG-Qualität mit RAGAS-Metriken
   - Skalierung vom Prototyp zur Produktion

4. **Leistungsoptimierung**
   - Systematisches Benchmarking mehrerer Modelle
   - Messung von Latenz, Durchsatz und Zeit bis zum ersten Token
   - Vergleich von Small Language Models und Large Language Models
   - Auswahl optimaler Modelle basierend auf Leistungs-/Qualitätsabwägungen

5. **Multi-Agenten-Orchestrierung**
   - Gestaltung spezialisierter Agenten für verschiedene Aufgaben
   - Implementierung von Agenten-Gedächtnis und Kontextmanagement
   - Koordination mehrerer Agenten in komplexen Workflows
   - Aufbau von Koordinator-Mustern für die Zusammenarbeit von Agenten

6. **Intelligentes Modell-Routing**
   - Implementierung von Intent-Erkennung und Musterabgleich
   - Automatische Weiterleitung von Anfragen an geeignete Modelle
   - Aufbau von mehrstufigen Pipelines (Plan → Ausführen → Verfeinern)
   - Gestaltung skalierbarer Modell-als-Tools-Architekturen

---

## 🎓 Lernergebnisse

### Was Sie erstellen werden

| Notebook | Ergebnis | Demonstrierte Fähigkeiten | Schwierigkeitsgrad |
|----------|----------|---------------------------|--------------------|
| **Session 01** | Chat-App mit Streaming | Dienst-Setup, grundlegende Komplettierungen, Streaming-UX | ⭐ Anfänger |
| **Session 02 (RAG)** | RAG-Pipeline mit Bewertung | Einbettungen, semantische Suche, Qualitätsmetriken | ⭐⭐ Mittel |
| **Session 02 (Eval)** | RAG-Qualitätsbewertung | RAGAS-Metriken, systematische Bewertung | ⭐⭐ Mittel |
| **Session 03** | Multi-Modell-Benchmark | Leistungsbewertung, Modellvergleich | ⭐⭐ Mittel |
| **Session 04** | SLM vs LLM Vergleich | Abwägungsanalyse, Optimierungsstrategien | ⭐⭐⭐ Fortgeschritten |
| **Session 05** | Multi-Agenten-Orchestrator | Agenten-Design, Gedächtnis, Koordination | ⭐⭐⭐ Fortgeschritten |
| **Session 06 (Router)** | Intelligentes Routing-System | Intent-Erkennung, Modellauswahl | ⭐⭐⭐ Fortgeschritten |
| **Session 06 (Pipeline)** | Mehrstufige Pipeline | Plan-/Ausführungs-/Verfeinerungs-Workflows | ⭐⭐⭐ Fortgeschritten |

### Kompetenzentwicklung

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshop-Zeitplan

### 🚀 Halbtages-Workshop (3,5 Stunden)

**Ideal für: Team-Trainings, Hackathons, Konferenz-Workshops**

| Zeit | Dauer | Sitzung | Themen | Aktivitäten |
|------|-------|---------|--------|-------------|
| **0:00** | 30 Min | Setup & Einführung | Einrichtung der Umgebung, Installation von Foundry Local | Abhängigkeiten installieren, Setup überprüfen |
| **0:30** | 30 Min | Session 01 | Grundlegende Chat-Komplettierungen, Streaming | Notebook ausführen, Prompts ändern |
| **1:00** | 45 Min | Session 02 | RAG-Pipeline, Einbettungen, Bewertung | RAG-System erstellen, Anfragen testen |
| **1:45** | 15 Min | Pause | ☕ Kaffee & Fragen | — |
| **2:00** | 30 Min | Session 03 | Multi-Modell-Benchmarking | Vergleich von 3+ Modellen |
| **2:30** | 30 Min | Session 04 | SLM vs LLM Abwägungen | Leistung/Qualität analysieren |
| **3:00** | 30 Min | Session 05-06 | Multi-Agenten-Systeme & Routing | Fortgeschrittene Muster erkunden |

**Ergebnis**: Teilnehmer verlassen den Workshop mit 6 funktionierenden Edge-AI-Anwendungen und produktionsreifen Code-Mustern.

---

### 🎓 Ganztages-Workshop (6 Stunden)

**Ideal für: Intensivtraining, Bootcamps, Universitätskurse**

| Zeit | Dauer | Sitzung | Themen | Aktivitäten |
|------|-------|---------|--------|-------------|
| **0:00** | 45 Min | Setup & Theorie | Einrichtung der Umgebung, Grundlagen von Edge AI | Installieren, überprüfen, Anwendungsfälle diskutieren |
| **0:45** | 45 Min | Session 01 | Tiefgehende Chat-Komplettierungen | Grundlegende & Streaming-Chats implementieren |
| **1:30** | 30 Min | Pause | ☕ Kaffee & Networking | — |
| **2:00** | 60 Min | Session 02 (beide) | RAG-Pipeline + RAGAS-Bewertung | Vollständiges RAG-System erstellen |
| **3:00** | 30 Min | Praxis-Labor 1 | Benutzerdefiniertes RAG für Ihre Domäne | Auf eigene Dokumente anwenden |
| **3:30** | 30 Min | Mittagessen | 🍽️ | — |
| **4:00** | 45 Min | Session 03 | Benchmarking-Methodik | Systematischer Modellvergleich |
| **4:45** | 45 Min | Session 04 | Optimierungsstrategien | SLM vs LLM Analyse |
| **5:30** | 60 Min | Session 05-06 | Fortgeschrittene Orchestrierung | Multi-Agenten-Systeme, Routing |
| **6:30** | 30 Min | Praxis-Labor 2 | Benutzerdefiniertes Agenten-System erstellen | Eigenen Orchestrator entwerfen |

**Ergebnis**: Tiefes Verständnis von Edge-AI-Mustern plus 2 benutzerdefinierte Projekte.

---

### 📚 Selbstgesteuertes Lernen (2 Wochen)

**Ideal für: Einzelne Lernende, Online-Kurse, Selbststudium**

#### Woche 1: Grundlagen (6 Stunden)

| Tag | Fokus | Dauer | Notebooks | Hausaufgaben |
|-----|-------|-------|-----------|--------------|
| **Mo** | Setup & Grundlagen | 1,5 Std | Session 01 | Prompts ändern, Streaming testen |
| **Mi** | RAG-Grundlagen | 2 Std | Session 02 (beide) | Eigene Dokumente hinzufügen |
| **Fr** | Benchmarking | 1,5 Std | Session 03 | Zusätzliche Modelle vergleichen |
| **Sa** | Überprüfung & Übung | 1 Std | Alle Woche 1 | Übungen abschließen, Fehler beheben |

#### Woche 2: Fortgeschrittene Themen (5 Stunden)

| Tag | Fokus | Dauer | Notebooks | Hausaufgaben |
|-----|-------|-------|-----------|--------------|
| **Mo** | Optimierung | 1,5 Std | Session 04 | Abwägungen dokumentieren |
| **Mi** | Multi-Agenten-Systeme | 2 Std | Session 05 | Benutzerdefinierte Agenten entwerfen |
| **Fr** | Intelligentes Routing | 1,5 Std | Session 06 (beide) | Routing-Logik erstellen |
| **Sa** | Abschlussprojekt | 2 Std | Integration | Mehrere Muster kombinieren |

**Ergebnis**: Beherrschung von Edge-AI-Mustern plus Portfolio-Projekt.

---

## 📔 Notebook-Beschreibungen

### 📘 Session 01: Chat-Bootstrap
**Datei**: `session01_chat_bootstrap.ipynb`  
**Dauer**: 20-30 Minuten  
**Voraussetzungen**: Keine  
**Schwierigkeitsgrad**: ⭐ Anfänger

**Was Sie lernen werden**:
- Installation und Konfiguration des Foundry Local Python SDK
- Verwendung von `FoundryLocalManager` für automatische Dienstentdeckung
- Implementierung grundlegender Chat-Komplettierungen mit OpenAI-kompatibler API
- Aufbau von Streaming-Antworten für eine bessere Benutzererfahrung
- Fehlerbehandlung und Umgang mit Dienstunverfügbarkeit

**Schlüsselkonzepte**: Dienstmanagement, Chat-Komplettierungen, Streaming, Fehlerbehandlung

**Was Sie erstellen werden**: Interaktive Chat-Anwendung mit Streaming-Unterstützung

---

### 📗 Session 02: RAG-Pipeline
**Datei**: `session02_rag_pipeline.ipynb`  
**Dauer**: 30-45 Minuten  
**Voraussetzungen**: Session 01  
**Schwierigkeitsgrad**: ⭐⭐ Mittel

**Was Sie lernen werden**:
- Implementierung des Retrieval Augmented Generation (RAG)-Musters
- Erstellung von Vektoreinbettungen mit Sentence-Transformers
- Aufbau semantischer Suche mit Kosinus-Ähnlichkeit
- Verankerung von LLM-Antworten in Domänendokumenten
- Umgang mit optionalen Abhängigkeiten durch Importguards

**Schlüsselkonzepte**: RAG-Architektur, Einbettungen, semantische Suche, Vektorähnlichkeit

**Was Sie erstellen werden**: Dokumentbasierte Frage-Antwort-Systeme

---

### 📗 Session 02: RAG-Bewertung mit RAGAS
**Datei**: `session02_rag_eval_ragas.ipynb`  
**Dauer**: 30-45 Minuten  
**Voraussetzungen**: Session 02 RAG-Pipeline  
**Schwierigkeitsgrad**: ⭐⭐ Mittel

**Was Sie lernen werden**:
- Bewertung der RAG-Qualität mit branchenüblichen Metriken
- Messung von Kontextrelevanz, Antwortrelevanz, Glaubwürdigkeit
- Verwendung des RAGAS-Frameworks für systematische Bewertung
- Identifizierung und Behebung von RAG-Qualitätsproblemen
- Erstellung von Bewertungsdatensätzen für Ihre Domäne

**Schlüsselkonzepte**: RAG-Bewertung, RAGAS-Metriken, Qualitätsmessung, systematisches Testen

**Was Sie erstellen werden**: RAG-Qualitätsbewertungs-Framework

---

### 📙 Session 03: Benchmark OSS-Modelle
**Datei**: `session03_benchmark_oss_models.ipynb`  
**Dauer**: 30-45 Minuten  
**Voraussetzungen**: Session 01  
**Schwierigkeitsgrad**: ⭐⭐ Mittel

**Was Sie lernen werden**:
- Systematisches Benchmarking mehrerer Modelle
- Messung von Latenz, Durchsatz, Zeit bis zum ersten Token
- Implementierung sanfter Fehlerabfederung bei Modellfehlern
- Vergleich der Leistung zwischen Modellfamilien
- Visualisierung und Analyse von Benchmark-Ergebnissen

**Schlüsselkonzepte**: Leistungsbenchmarking, Latenzmessung, Modellvergleich, statistische Analyse

**Was Sie erstellen werden**: Multi-Modell-Benchmarking-Suite

---

### 📙 Session 04: Modellvergleich (SLM vs LLM)
**Datei**: `session04_model_compare.ipynb`  
**Dauer**: 30-45 Minuten  
**Voraussetzungen**: Sessions 01, 03  
**Schwierigkeitsgrad**: ⭐⭐⭐ Fortgeschritten

**Was Sie lernen werden**:
- Vergleich von Small Language Models und Large Language Models
- Analyse von Leistungs- vs Qualitätsabwägungen
- Messung von Edge-Eignungsmetriken
- Auswahl optimaler Modelle für Einsatzbeschränkungen
- Dokumentation von Entscheidungskriterien für die Modellauswahl

**Schlüsselkonzepte**: Modellauswahl, Abwägungsanalyse, Optimierungsstrategien, Einsatzplanung

**Was Sie erstellen werden**: SLM vs LLM Vergleichs-Framework

---

### 📕 Session 05: Multi-Agenten-Orchestrator
**Datei**: `session05_agents_orchestrator.ipynb`  
**Dauer**: 45-60 Minuten  
**Voraussetzungen**: Sessions 01-02  
**Schwierigkeitsgrad**: ⭐⭐⭐ Fortgeschritten

**Was Sie lernen werden**:
- Gestaltung spezialisierter Agenten für verschiedene Aufgaben
- Implementierung von Agenten-Gedächtnis und Kontextmanagement
- Aufbau von Koordinator-Mustern für die Zusammenarbeit von Agenten
- Umgang mit Agenten-Kommunikation und Übergaben
- Überwachung der Leistung von Multi-Agenten-Systemen

**Schlüsselkonzepte**: Agenten-Architektur, Koordinator-Muster, Gedächtnismanagement, Agenten-Orchestrierung

**Was Sie erstellen werden**: Multi-Agenten-System mit Koordinator und Spezialisten

---

### 📕 Session 06: Modell-Router
**Datei**: `session06_models_router.ipynb`  
**Dauer**: 30-45 Minuten  
**Voraussetzungen**: Sessions 01, 03  
**Schwierigkeitsgrad**: ⭐⭐⭐ Fortgeschritten

**Was Sie lernen werden**:
- Implementierung von Intent-Erkennung und Musterabgleich
- Aufbau von keyword-basiertem Modell-Routing
- Automatische Weiterleitung von Anfragen an geeignete Modelle
- Konfiguration von Multi-Modell-Registern
- Überwachung von Routing-Entscheidungen und Leistung

**Schlüsselkonzepte**: Intent-Erkennung, Modell-Routing, Musterabgleich, intelligente Auswahl

**Was Sie erstellen werden**: Intelligentes Modell-Routing-System

---

### 📕 Session 06: Mehrstufige Pipeline
**Datei**: `session06_models_pipeline.ipynb`  
**Dauer**: 30-45 Minuten  
**Voraussetzungen**: Sessions 01, 06 Router  
**Schwierigkeitsgrad**: ⭐⭐⭐ Fortgeschritten

**Was Sie lernen werden**:
- Aufbau von mehrstufigen AI-Pipelines (Plan → Ausführen → Verfeinern)
- Integration des Routers für intelligente Modellauswahl
- Implementierung von Fehlerbehandlung und Wiederherstellung in der Pipeline
- Überwachung der Pipeline-Leistung und -Phasen
- Entwerfen skalierbare Architekturen für Modelle-als-Werkzeuge

**Wichtige Konzepte**: Pipeline-Architektur, mehrstufige Verarbeitung, Fehlerbehebung, Skalierungsmuster

**Was Sie erstellen werden**: Mehrstufige intelligente Pipeline mit Routing

---

## 🚀 Erste Schritte

### Voraussetzungen

**Systemanforderungen**:
- **Betriebssystem**: Windows 10/11, macOS 11+ oder Linux (Ubuntu 20.04+)
- **RAM**: Mindestens 8GB, empfohlen 16GB+
- **Speicherplatz**: Mindestens 10GB freier Speicherplatz für Modelle
- **Hardware**: CPU mit AVX2; GPU (CUDA, Qualcomm NPU) optional

**Softwareanforderungen**:
- **Python 3.8+** mit pip
- **Jupyter Notebook** oder **VS Code** mit Jupyter-Erweiterung
- **Microsoft Foundry Local** installiert und konfiguriert
- **Git** (zum Klonen des Repositorys)

### Installationsschritte

#### 1. Foundry Local installieren

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installation überprüfen**:
```bash
foundry --version
```

#### 2. Python-Umgebung einrichten

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Foundry Local starten

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Jupyter starten

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Schnelle Überprüfung

Führen Sie dies in einer Python-Zelle aus, um die Einrichtung zu überprüfen:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Erwartete Ausgabe**: Eine Begrüßungsantwort vom lokalen Modell.

---

## 📝 Best Practices für Workshops

### Für Kursleiter

**Vor dem Workshop**:
- ✅ Installationsanweisungen eine Woche im Voraus senden
- ✅ Alle Notebooks auf der Zielhardware testen
- ✅ Leitfaden zur Fehlerbehebung für häufige Probleme vorbereiten
- ✅ Backup-Modelle bereithalten (phi-3.5-mini, falls phi-4-mini fehlschlägt)
- ✅ Gemeinsamen Chat-Kanal für Fragen einrichten

**Während des Workshops**:
- ✅ Mit einer schnellen Überprüfung der Umgebung beginnen (5 Minuten)
- ✅ Ressourcen zur Fehlerbehebung sofort teilen
- ✅ Experimentieren und Modifikationen fördern
- ✅ Pausen strategisch einsetzen (nach jeweils 2 Sitzungen)
- ✅ TAs für individuelle Unterstützung bereithalten

**Nach dem Workshop**:
- ✅ Vollständige funktionierende Notebooks und Lösungen teilen
- ✅ Links zu zusätzlichen Ressourcen bereitstellen
- ✅ Feedback-Umfrage zur Verbesserung erstellen
- ✅ Sprechstunden für Nachfragen anbieten

### Für Lernende

**Maximieren Sie Ihr Lernen**:
- ✅ Einrichtung vor Beginn des Workshops abschließen
- ✅ Jede Code-Zelle selbst ausführen (nicht nur lesen)
- ✅ Mit Parametern und Eingabeaufforderungen experimentieren
- ✅ Notizen zu Erkenntnissen und Stolpersteinen machen
- ✅ Fragen stellen, wenn Sie nicht weiterkommen (andere haben wahrscheinlich dieselbe Frage)

**Häufige Fehler vermeiden**:
- ❌ Reihenfolge der Zellenausführung überspringen (nacheinander ausführen)
- ❌ Fehlermeldungen nicht sorgfältig lesen
- ❌ Ohne Verständnis durchrushen
- ❌ Markdown-Erklärungen ignorieren
- ❌ Ihre modifizierten Notebooks nicht speichern

**Tipps zur Fehlerbehebung**:
1. **Dienst läuft nicht**: Überprüfen Sie `foundry service status`
2. **Importfehler**: Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist
3. **Modell nicht gefunden**: Führen Sie `foundry model ls` aus, um geladene Modelle aufzulisten
4. **Langsame Leistung**: RAM-Auslastung überprüfen, andere Anwendungen schließen
5. **Unerwartete Ergebnisse**: Kernel neu starten und alle Zellen von oben ausführen

---

## 🔗 Zusätzliche Ressourcen

### Workshop-Materialien

- **[Workshop-Hauptleitfaden](../Readme.md)** - Überblick, Lernziele, Karriereperspektiven
- **[Python-Beispiele](../../../../Workshop/samples)** - Entsprechende Python-Skripte für jede Sitzung
- **[Sitzungsleitfäden](../../../../Workshop)** - Detaillierte Markdown-Leitfäden (Session01-06)
- **[Skripte](../../../../Workshop/scripts)** - Validierungs- und Testwerkzeuge
- **[Fehlerbehebung](./TROUBLESHOOTING.md)** - Häufige Probleme und Lösungen
- **[Schnellstart](./quickstart.md)** - Schnellstart-Leitfaden

### Dokumentation

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Offizielle Microsoft-Dokumentation
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK-Referenz
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentation zu Einbettungsmodellen
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG-Bewertungsmetriken

### Community

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Fragen stellen, Projekte teilen
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Echtzeit-Community-Support
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technische Q&A

---

## 🎯 Empfehlungen für Lernpfade

### Anfängerpfad (Hier starten)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG-Pipeline
3. **Session 03** - Modelle benchmarken

**Zeit**: ~2 Stunden | **Fokus**: Grundlagenmuster

---

### Mittelstufenpfad

1. Anfängerpfad abschließen
2. **Session 02** - RAG-Bewertung
3. **Session 04** - Modellvergleich

**Zeit**: ~4 Stunden | **Fokus**: Qualität und Optimierung

---

### Fortgeschrittener Pfad (Vollständiger Workshop)

1. Mittelstufenpfad abschließen
2. **Session 05** - Multi-Agent-Orchestrator
3. **Session 06** - Modell-Router
4. **Session 06** - Mehrstufige Pipeline

**Zeit**: ~6 Stunden | **Fokus**: Produktionsmuster

---

### Individueller Projektpfad

1. Anfängerpfad abschließen (Sessions 01-03)
2. Wählen Sie EINE fortgeschrittene Sitzung basierend auf Ihrem Ziel:
   - **RAG-App erstellen?** → Session 02 Bewertung
   - **Leistung optimieren?** → Session 04 Vergleich
   - **Komplexe Workflows?** → Session 05 Orchestrator
   - **Skalierbare Architektur?** → Session 06 Router + Pipeline

**Zeit**: ~3 Stunden | **Fokus**: Projektspezifische Fähigkeiten

---

## 📊 Erfolgsmessung

Verfolgen Sie Ihren Fortschritt mit diesen Meilensteinen:

- [ ] **Einrichtung abgeschlossen** - Foundry Local läuft, alle Abhängigkeiten installiert
- [ ] **Erster Chat** - Session 01 abgeschlossen, Streaming-Chat funktioniert
- [ ] **RAG erstellt** - Session 02 abgeschlossen, Dokument-QA-System funktionsfähig
- [ ] **Modelle benchmarken** - Session 03 abgeschlossen, Leistungsdaten gesammelt
- [ ] **Trade-offs analysiert** - Session 04 abgeschlossen, Kriterien für Modellauswahl dokumentiert
- [ ] **Agenten orchestriert** - Session 05 abgeschlossen, Multi-Agent-System funktionsfähig
- [ ] **Routing implementiert** - Session 06 abgeschlossen, intelligente Modellauswahl funktionsfähig
- [ ] **Individuelles Projekt** - Workshop-Muster auf Ihren eigenen Anwendungsfall angewendet

---

## 🤝 Mitwirken

Ein Problem gefunden oder eine Idee? Wir freuen uns über Beiträge!

- **Probleme melden**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Verbesserungen vorschlagen**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **PRs einreichen**: Folgen Sie den [Beitragsrichtlinien](../../AGENTS.md)

---

## 📄 Lizenz

Dieser Workshop ist Teil des [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners)-Repositorys und unter der [MIT-Lizenz](../../../../LICENSE) lizenziert.

---

**Bereit, produktionsreife Edge-AI-Anwendungen zu erstellen?**  
**Starten Sie mit [Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Letzte Aktualisierung: 8. Oktober 2025 | Workshop-Version: 2.0*

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.