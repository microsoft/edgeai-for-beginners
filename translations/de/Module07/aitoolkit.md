# AI Toolkit für Visual Studio Code - Leitfaden zur Edge-AI-Entwicklung

## Einführung

Willkommen beim umfassenden Leitfaden zur Nutzung des AI Toolkit für Visual Studio Code in der Edge-AI-Entwicklung. Während künstliche Intelligenz von zentralisiertem Cloud-Computing zu verteilten Edge-Geräten übergeht, benötigen Entwickler leistungsstarke, integrierte Tools, die die einzigartigen Herausforderungen der Edge-Bereitstellung bewältigen können – von Ressourcenbeschränkungen bis hin zu Anforderungen an den Offline-Betrieb.

Das AI Toolkit für Visual Studio Code schließt diese Lücke, indem es eine vollständige Entwicklungsumgebung bietet, die speziell für die Erstellung, das Testen und die Optimierung von KI-Anwendungen entwickelt wurde, die effizient auf Edge-Geräten laufen. Egal, ob Sie für IoT-Sensoren, mobile Geräte, eingebettete Systeme oder Edge-Server entwickeln, dieses Toolkit vereinfacht Ihren gesamten Entwicklungsworkflow innerhalb der vertrauten VS Code-Umgebung.

Dieser Leitfaden führt Sie durch die wesentlichen Konzepte, Tools und Best Practices, um das AI Toolkit in Ihren Edge-AI-Projekten optimal zu nutzen – von der Auswahl des Modells bis hin zur Produktionsbereitstellung.

## Überblick

Das AI Toolkit für Visual Studio Code ist eine leistungsstarke Erweiterung, die die Entwicklung von Agenten und die Erstellung von KI-Anwendungen vereinfacht. Das Toolkit bietet umfassende Funktionen zur Erkundung, Bewertung und Bereitstellung von KI-Modellen von einer Vielzahl von Anbietern – darunter Anthropic, OpenAI, GitHub und Google – und unterstützt die lokale Modellausführung mit ONNX und Ollama.

Was das AI Toolkit auszeichnet, ist sein ganzheitlicher Ansatz für den gesamten KI-Entwicklungszyklus. Im Gegensatz zu traditionellen KI-Entwicklungstools, die sich auf einzelne Aspekte konzentrieren, bietet das AI Toolkit eine integrierte Umgebung, die Modellentdeckung, Experimentierung, Agentenentwicklung, Bewertung und Bereitstellung abdeckt – alles innerhalb der vertrauten VS Code-Umgebung.

Die Plattform ist speziell für schnelles Prototyping und Produktionsbereitstellung konzipiert, mit Funktionen wie Prompt-Generierung, Schnellstart, nahtlose MCP (Model Context Protocol)-Tool-Integrationen und umfangreiche Bewertungsmöglichkeiten. Für die Edge-AI-Entwicklung bedeutet dies, dass Sie KI-Anwendungen für Edge-Bereitstellungsszenarien effizient entwickeln, testen und optimieren können, während Sie den vollständigen Entwicklungsworkflow in VS Code beibehalten.

## Lernziele

Am Ende dieses Leitfadens werden Sie in der Lage sein:

### Kernkompetenzen
- **Installieren und konfigurieren** des AI Toolkit für Visual Studio Code für Edge-AI-Entwicklungsworkflows
- **Navigieren und nutzen** der AI Toolkit-Oberfläche, einschließlich Model Catalog, Playground und Agent Builder
- **Auswählen und bewerten** von KI-Modellen, die für Edge-Bereitstellungen geeignet sind, basierend auf Leistung und Ressourcenbeschränkungen
- **Konvertieren und optimieren** von Modellen mit ONNX-Format und Quantisierungstechniken für Edge-Geräte

### Fähigkeiten in der Edge-AI-Entwicklung
- **Entwerfen und implementieren** von Edge-AI-Anwendungen mit der integrierten Entwicklungsumgebung
- **Modelltests durchführen** unter edge-ähnlichen Bedingungen mit lokaler Inferenz und Ressourcenüberwachung
- **Erstellen und anpassen** von KI-Agenten, die für Edge-Bereitstellungsszenarien optimiert sind
- **Bewerten der Modellleistung** anhand von Metriken, die für Edge-Computing relevant sind (Latenz, Speicherverbrauch, Genauigkeit)

### Optimierung und Bereitstellung
- **Quantisierung und Pruning anwenden**, um die Modellgröße zu reduzieren und gleichzeitig akzeptable Leistung beizubehalten
- **Modelle optimieren** für spezifische Edge-Hardwareplattformen, einschließlich CPU-, GPU- und NPU-Beschleunigung
- **Best Practices implementieren** für die Edge-AI-Entwicklung, einschließlich Ressourcenmanagement und Fallback-Strategien
- **Modelle und Anwendungen vorbereiten** für die Produktionsbereitstellung auf Edge-Geräten

### Fortgeschrittene Edge-AI-Konzepte
- **Integration mit Edge-AI-Frameworks** wie ONNX Runtime, Windows ML und TensorFlow Lite
- **Multi-Modell-Architekturen und föderierte Lern-Szenarien** für Edge-Umgebungen implementieren
- **Häufige Edge-AI-Probleme beheben**, einschließlich Speicherbeschränkungen, Inferenzgeschwindigkeit und Hardwarekompatibilität
- **Überwachungs- und Protokollierungsstrategien entwerfen** für Edge-AI-Anwendungen in der Produktion

### Praktische Anwendung
- **End-to-End-Edge-AI-Lösungen erstellen** von der Modellauswahl bis zur Bereitstellung
- **Kompetenz demonstrieren** in edge-spezifischen Entwicklungsworkflows und Optimierungstechniken
- **Erlernte Konzepte anwenden** auf reale Edge-AI-Anwendungsfälle, einschließlich IoT, mobiler und eingebetteter Anwendungen
- **Unterschiedliche Edge-AI-Bereitstellungsstrategien bewerten und vergleichen** sowie deren Kompromisse analysieren

## Hauptfunktionen für die Edge-AI-Entwicklung

### 1. Modellkatalog und Entdeckung
- **Unterstützung mehrerer Anbieter**: Durchsuchen und greifen Sie auf KI-Modelle von Anthropic, OpenAI, GitHub, Google und anderen Anbietern zu
- **Integration lokaler Modelle**: Vereinfachte Entdeckung von ONNX- und Ollama-Modellen für Edge-Bereitstellungen
- **GitHub-Modelle**: Direkte Integration mit GitHubs Modell-Hosting für einen optimierten Zugriff
- **Modellvergleich**: Vergleichen Sie Modelle nebeneinander, um ein optimales Gleichgewicht für Edge-Geräte zu finden

### 2. Interaktiver Playground
- **Interaktive Testumgebung**: Schnelle Experimente mit Modellfähigkeiten in einer kontrollierten Umgebung
- **Multimodale Unterstützung**: Testen Sie mit Bildern, Texten und anderen Eingaben, die in Edge-Szenarien typisch sind
- **Echtzeit-Experimente**: Sofortiges Feedback zu Modellantworten und Leistung
- **Parameteroptimierung**: Feinabstimmung von Modellparametern für Edge-Bereitstellungsanforderungen

### 3. Prompt (Agent) Builder
- **Natürliche Sprachgenerierung**: Starter-Prompts mit natürlichen Sprachbeschreibungen generieren
- **Iterative Verfeinerung**: Prompts basierend auf Modellantworten und Leistung verbessern
- **Aufgabenzerlegung**: Komplexe Aufgaben mit Prompt-Chaining und strukturierten Ausgaben aufteilen
- **Variablenunterstützung**: Variablen in Prompts für dynamisches Agentenverhalten verwenden
- **Produktionscode-Generierung**: Produktionsbereiten Code für schnelle App-Entwicklung generieren

### 4. Massenlauf und Bewertung
- **Multi-Modell-Tests**: Mehrere Prompts gleichzeitig über ausgewählte Modelle ausführen
- **Effizientes Testen im großen Maßstab**: Verschiedene Eingaben und Konfigurationen effizient testen
- **Benutzerdefinierte Testfälle**: Agenten mit Testfällen ausführen, um die Funktionalität zu validieren
- **Leistungsvergleich**: Ergebnisse über verschiedene Modelle und Konfigurationen hinweg vergleichen

### 5. Modellbewertung mit Datensätzen
- **Standardmetriken**: KI-Modelle mit integrierten Evaluatoren testen (F1-Score, Relevanz, Ähnlichkeit, Kohärenz)
- **Benutzerdefinierte Evaluatoren**: Eigene Bewertungsmetriken für spezifische Anwendungsfälle erstellen
- **Datensatzintegration**: Modelle gegen umfassende Datensätze testen
- **Leistungsmessung**: Modellleistung für Edge-Bereitstellungsentscheidungen quantifizieren

### 6. Feinabstimmungsfunktionen
- **Modellanpassung**: Modelle für spezifische Anwendungsfälle und Domänen anpassen
- **Spezialisierte Anpassung**: Modelle an spezialisierte Domänen und Anforderungen anpassen
- **Edge-Optimierung**: Modelle speziell für Edge-Bereitstellungsbeschränkungen feinabstimmen
- **Domänenspezifisches Training**: Modelle erstellen, die auf spezifische Edge-Anwendungsfälle zugeschnitten sind

### 7. MCP-Tool-Integration
- **Externe Tool-Konnektivität**: Agenten mit externen Tools über Model Context Protocol-Server verbinden
- **Aktionen in der realen Welt**: Agenten ermöglichen, Datenbanken abzufragen, APIs zu nutzen oder benutzerdefinierte Logik auszuführen
- **Bestehende MCP-Server**: Tools aus Kommandozeilen- (stdio) oder HTTP- (server-sent event) Protokollen verwenden
- **Benutzerdefinierte MCP-Entwicklung**: Neue MCP-Server erstellen und mit Tests im Agent Builder testen

### 8. Agentenentwicklung und -tests
- **Funktionsaufruf-Unterstützung**: Agenten ermöglichen, externe Funktionen dynamisch aufzurufen
- **Echtzeit-Integrationstests**: Integrationen mit Echtzeitläufen und Tool-Nutzung testen
- **Agenten-Versionierung**: Versionskontrolle für Agenten mit Vergleichsmöglichkeiten für Bewertungsergebnisse
- **Debugging und Tracing**: Lokale Tracing- und Debugging-Funktionen für die Agentenentwicklung

## Workflow für die Edge-AI-Entwicklung

### Phase 1: Modellentdeckung und -auswahl
1. **Modellkatalog erkunden**: Verwenden Sie den Modellkatalog, um Modelle zu finden, die für Edge-Bereitstellungen geeignet sind
2. **Leistung vergleichen**: Modelle basierend auf Größe, Genauigkeit und Inferenzgeschwindigkeit bewerten
3. **Lokal testen**: Ollama- oder ONNX-Modelle lokal testen, bevor sie auf Edge-Geräten bereitgestellt werden
4. **Ressourcenanforderungen bewerten**: Speicher- und Rechenanforderungen für Ziel-Edge-Geräte bestimmen

### Phase 2: Modelloptimierung
1. **In ONNX konvertieren**: Ausgewählte Modelle in das ONNX-Format für Edge-Kompatibilität konvertieren
2. **Quantisierung anwenden**: Modellgröße durch INT8- oder INT4-Quantisierung reduzieren
3. **Hardware-Optimierung**: Optimierung für Ziel-Edge-Hardware (ARM, x86, spezialisierte Beschleuniger)
4. **Leistungsvalidierung**: Validieren, dass optimierte Modelle akzeptable Genauigkeit beibehalten

### Phase 3: Anwendungsentwicklung
1. **Agenten-Design**: Mit dem Agent Builder Edge-optimierte KI-Agenten erstellen
2. **Prompt-Engineering**: Prompts entwickeln, die effektiv mit kleineren Edge-Modellen arbeiten
3. **Integrationstests**: Agenten unter simulierten Edge-Bedingungen testen
4. **Code-Generierung**: Produktionscode für Edge-Bereitstellungen optimieren und generieren

### Phase 4: Bewertung und Tests
1. **Batch-Bewertung**: Mehrere Konfigurationen testen, um optimale Edge-Einstellungen zu finden
2. **Leistungsprofiling**: Inferenzgeschwindigkeit, Speicherverbrauch und Genauigkeit analysieren
3. **Edge-Simulation**: Tests unter Bedingungen durchführen, die der Ziel-Edge-Bereitstellungsumgebung ähneln
4. **Stresstests**: Leistung unter verschiedenen Lastbedingungen bewerten

### Phase 5: Bereitstellungsvorbereitung
1. **Endgültige Optimierung**: Letzte Optimierungen basierend auf Testergebnissen anwenden
2. **Bereitstellungspaketierung**: Modelle und Code für Edge-Bereitstellungen paketieren
3. **Dokumentation**: Bereitstellungsanforderungen und Konfiguration dokumentieren
4. **Überwachungs-Setup**: Überwachung und Protokollierung für Edge-Bereitstellungen vorbereiten

## Zielgruppe für die Edge-AI-Entwicklung

### Edge-AI-Entwickler
- Anwendungsentwickler, die KI-gestützte Edge-Geräte und IoT-Lösungen erstellen
- Entwickler eingebetteter Systeme, die KI-Funktionen in ressourcenbeschränkte Geräte integrieren
- Mobile Entwickler, die KI-Anwendungen für Smartphones und Tablets erstellen

### Edge-AI-Ingenieure
- KI-Ingenieure, die Modelle für Edge-Bereitstellungen optimieren und Inferenz-Pipelines verwalten
- DevOps-Ingenieure, die KI-Modelle über verteilte Edge-Infrastrukturen bereitstellen und verwalten
- Performance-Ingenieure, die KI-Workloads für Edge-Hardware-Beschränkungen optimieren

### Forscher und Pädagogen
- KI-Forscher, die effiziente Modelle und Algorithmen für Edge-Computing entwickeln
- Pädagogen, die Edge-AI-Konzepte lehren und Optimierungstechniken demonstrieren
- Studenten, die die Herausforderungen und Lösungen bei der Edge-AI-Bereitstellung kennenlernen

## Edge-AI-Anwendungsfälle

### Intelligente IoT-Geräte
- **Echtzeit-Bilderkennung**: Computer-Vision-Modelle auf IoT-Kameras und Sensoren bereitstellen
- **Sprachverarbeitung**: Sprach- und natürliche Sprachverarbeitung auf Smart-Speakern implementieren
- **Prädiktive Wartung**: Anomalieerkennungsmodelle auf industriellen Edge-Geräten ausführen
- **Umweltüberwachung**: Sensor-Datenanalysemodelle für Umweltanwendungen bereitstellen

### Mobile und eingebettete Anwendungen
- **Übersetzung auf dem Gerät**: Sprachübersetzungsmodelle implementieren, die offline funktionieren
- **Erweiterte Realität**: Echtzeit-Objekterkennung und -verfolgung für AR-Anwendungen bereitstellen
- **Gesundheitsüberwachung**: Gesundheitsanalysemodelle auf Wearables und medizinischen Geräten ausführen
- **Autonome Systeme**: Entscheidungsmodelle für Drohnen, Roboter und Fahrzeuge implementieren

### Edge-Computing-Infrastruktur
- **Edge-Datenzentren**: KI-Modelle in Edge-Datenzentren für Anwendungen mit niedriger Latenz bereitstellen
- **CDN-Integration**: KI-Verarbeitungsfunktionen in Content-Delivery-Netzwerke integrieren
- **5G-Edge**: 5G-Edge-Computing für KI-gestützte Anwendungen nutzen
- **Fog-Computing**: KI-Verarbeitung in Fog-Computing-Umgebungen implementieren

## Installation und Einrichtung

### Erweiterungsinstallation
Installieren Sie die AI Toolkit-Erweiterung direkt aus dem Visual Studio Code Marketplace:

**Erweiterungs-ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installationsmethoden**:
1. **VS Code Marketplace**: Suchen Sie im Erweiterungsbereich nach "AI Toolkit"
2. **Befehlszeile**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direkte Installation**: Herunterladen von [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Voraussetzungen für die Edge-AI-Entwicklung
- **Visual Studio Code**: Neueste Version empfohlen
- **Python-Umgebung**: Python 3.8+ mit erforderlichen KI-Bibliotheken
- **ONNX Runtime** (Optional): Für ONNX-Modellinferenz
- **Ollama** (Optional): Für lokale Modellbereitstellung
- **Hardware-Beschleunigungstools**: CUDA, OpenVINO oder plattformspezifische Beschleuniger

### Erstanpassung
1. **Erweiterungsaktivierung**: Öffnen Sie VS Code und überprüfen Sie, ob das AI Toolkit in der Aktivitätsleiste erscheint
2. **Modellanbieter-Einrichtung**: Zugriff auf GitHub, OpenAI, Anthropic oder andere Modellanbieter konfigurieren
3. **Lokale Umgebung**: Python-Umgebung einrichten und erforderliche Pakete installieren
4. **Hardware-Beschleunigung**: GPU/NPU-Beschleunigung konfigurieren, falls verfügbar
5. **MCP-Integration**: Model Context Protocol-Server einrichten, falls erforderlich

### Checkliste für die Ersteinrichtung
- [ ] AI Toolkit-Erweiterung installiert und aktiviert
- [ ] Modellkatalog zugänglich und Modelle auffindbar
- [ ] Playground funktionsfähig für Modelltests
- [ ] Agent Builder zugänglich für Prompt-Entwicklung
- [ ] Lokale Entwicklungsumgebung konfiguriert
- [ ] Hardware-Beschleunigung (falls verfügbar) korrekt konfiguriert

## Erste Schritte mit dem AI Toolkit

### Schnellstart-Anleitung

Wir empfehlen, mit Modellen zu beginnen, die von GitHub gehostet werden, um die Erfahrung zu optimieren:

1. **Installation**: Folgen Sie der [Installationsanleitung](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup), um das AI Toolkit auf Ihrem Gerät einzurichten
2. **Modellentdeckung**: Wählen Sie im Erweiterungsbaum **CATALOG > Models**, um verfügbare Modelle zu erkunden
3. **GitHub-Modelle**: Beginnen Sie mit Modellen, die von GitHub gehostet werden, für eine optimale Integration
4. **Playground-Tests**: Wählen Sie auf einer Modellkarte **Try in Playground**, um mit den Modellfähigkeiten zu experimentieren

### Schritt-für-Schritt-Anleitung zur Edge-AI-Entwicklung

#### Schritt 1: Modellentdeckung und -auswahl
1. Öffnen Sie die AI Toolkit-Ansicht in der VS Code-Aktivitätsleiste
2. Durchsuchen Sie den Modellkatalog nach Modellen, die für Edge-Bereitstellungen geeignet sind
3. Filtern Sie nach Anbieter (GitHub, ONNX, Ollama) basierend auf Ihren Edge-Anforderungen
4. Verwenden Sie **Try in Playground**, um Modellfähigkeiten sofort zu testen

#### Schritt 2: Agentenentwicklung
1. Verwenden Sie den **Prompt (Agent) Builder**, um Edge-optimierte KI-Agenten zu erstellen
2. Starter-Prompts mit natürlichen Sprachbeschreibungen erstellen  
3. Prompts basierend auf Modellantworten iterativ verfeinern  
4. MCP-Tools für erweiterte Agentenfähigkeiten integrieren  

#### Schritt 3: Testen und Evaluieren  
1. **Bulk Run** verwenden, um mehrere Prompts über ausgewählte Modelle zu testen  
2. Agenten mit Testfällen ausführen, um die Funktionalität zu validieren  
3. Genauigkeit und Leistung mit integrierten oder benutzerdefinierten Metriken bewerten  
4. Verschiedene Modelle und Konfigurationen vergleichen  

#### Schritt 4: Feinabstimmung und Optimierung  
1. Modelle für spezifische Edge-Anwendungsfälle anpassen  
2. Domänenspezifische Feinabstimmung anwenden  
3. Optimierung für Einschränkungen bei Edge-Bereitstellungen  
4. Versionierung und Vergleich verschiedener Agentenkonfigurationen  

#### Schritt 5: Vorbereitung der Bereitstellung  
1. Produktionsbereiten Code mit dem Agent Builder generieren  
2. MCP-Serververbindungen für den Produktionseinsatz einrichten  
3. Bereitstellungspakete für Edge-Geräte vorbereiten  
4. Überwachungs- und Bewertungsmetriken konfigurieren  

## Beispiele für das AI Toolkit  

Probieren Sie unsere Beispiele aus  
Die [AI Toolkit Beispiele](https://github.com/Azure-Samples/AI_Toolkit_Samples) wurden entwickelt, um Entwicklern und Forschern zu helfen, KI-Lösungen effektiv zu erkunden und umzusetzen.  

Unsere Beispiele umfassen:  

Beispielcode: Vorgefertigte Beispiele, die KI-Funktionen demonstrieren, wie Training, Bereitstellung oder Integration von Modellen in Anwendungen.  
Dokumentation: Anleitungen und Tutorials, die Benutzern helfen, die Funktionen des AI Toolkits zu verstehen und zu nutzen.  
Voraussetzungen  

- Visual Studio Code  
- AI Toolkit für Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Best Practices für die Entwicklung von Edge-KI  

### Modellauswahl  
- **Größenbeschränkungen**: Modelle auswählen, die innerhalb der Speicherbegrenzungen der Zielgeräte passen  
- **Inference-Geschwindigkeit**: Modelle mit schneller Inferenzzeit für Echtzeitanwendungen priorisieren  
- **Genauigkeitskompromisse**: Modellgenauigkeit mit Ressourcenbeschränkungen ausbalancieren  
- **Formatkompatibilität**: ONNX oder hardwareoptimierte Formate für Edge-Bereitstellungen bevorzugen  

### Optimierungstechniken  
- **Quantisierung**: INT8- oder INT4-Quantisierung verwenden, um die Modellgröße zu reduzieren und die Geschwindigkeit zu verbessern  
- **Pruning**: Unnötige Modellparameter entfernen, um die Rechenanforderungen zu senken  
- **Knowledge Distillation**: Kleinere Modelle erstellen, die die Leistung größerer Modelle beibehalten  
- **Hardware-Beschleunigung**: NPUs, GPUs oder spezialisierte Beschleuniger nutzen, wenn verfügbar  

### Entwicklungsworkflow  
- **Iteratives Testen**: Häufig in Edge-ähnlichen Bedingungen während der Entwicklung testen  
- **Leistungsüberwachung**: Ressourcenverbrauch und Inferenzgeschwindigkeit kontinuierlich überwachen  
- **Versionskontrolle**: Modellversionen und Optimierungseinstellungen verfolgen  
- **Dokumentation**: Alle Optimierungsentscheidungen und Leistungskompromisse dokumentieren  

### Bereitstellungsüberlegungen  
- **Ressourcenüberwachung**: Speicher-, CPU- und Stromverbrauch in der Produktion überwachen  
- **Fallback-Strategien**: Mechanismen für Modellfehler implementieren  
- **Update-Mechanismen**: Planung für Modellaktualisierungen und Versionsmanagement  
- **Sicherheit**: Angemessene Sicherheitsmaßnahmen für Edge-KI-Anwendungen implementieren  

## Integration mit Edge-KI-Frameworks  

### ONNX Runtime  
- **Plattformübergreifende Bereitstellung**: ONNX-Modelle auf verschiedenen Edge-Plattformen bereitstellen  
- **Hardware-Optimierung**: Hardware-spezifische Optimierungen der ONNX Runtime nutzen  
- **Mobile Unterstützung**: ONNX Runtime Mobile für Smartphone- und Tablet-Anwendungen verwenden  
- **IoT-Integration**: Leichte Distributionen der ONNX Runtime für IoT-Geräte nutzen  

### Windows ML  
- **Windows-Geräte**: Optimierung für Windows-basierte Edge-Geräte und PCs  
- **NPU-Beschleunigung**: Neural Processing Units auf Windows-Geräten nutzen  
- **DirectML**: GPU-Beschleunigung auf Windows-Plattformen mit DirectML verwenden  
- **UWP-Integration**: Integration mit Universal Windows Platform-Anwendungen  

### TensorFlow Lite  
- **Mobile Optimierung**: TensorFlow Lite-Modelle auf mobilen und eingebetteten Geräten bereitstellen  
- **Hardware-Delegates**: Spezialisierte Hardware-Delegates für Beschleunigung verwenden  
- **Mikrocontroller**: TensorFlow Lite Micro für Mikrocontroller-Bereitstellungen nutzen  
- **Plattformübergreifende Unterstützung**: Bereitstellung auf Android, iOS und eingebetteten Linux-Systemen  

### Azure IoT Edge  
- **Cloud-Edge-Hybrid**: Cloud-Training mit Edge-Inferenz kombinieren  
- **Modulbereitstellung**: KI-Modelle als IoT Edge-Module bereitstellen  
- **Geräteverwaltung**: Edge-Geräte und Modellaktualisierungen aus der Ferne verwalten  
- **Telemetrie**: Leistungsdaten und Modellmetriken aus Edge-Bereitstellungen sammeln  

## Fortgeschrittene Edge-KI-Szenarien  

### Multi-Modell-Bereitstellung  
- **Modell-Ensembles**: Mehrere Modelle für verbesserte Genauigkeit oder Redundanz bereitstellen  
- **A/B-Tests**: Verschiedene Modelle gleichzeitig auf Edge-Geräten testen  
- **Dynamische Auswahl**: Modelle basierend auf aktuellen Gerätebedingungen auswählen  
- **Ressourcenteilung**: Ressourcenverbrauch über mehrere bereitgestellte Modelle optimieren  

### Federated Learning  
- **Verteiltes Training**: Modelle über mehrere Edge-Geräte hinweg trainieren  
- **Datenschutz**: Trainingsdaten lokal halten, während Modellverbesserungen geteilt werden  
- **Kollaboratives Lernen**: Geräten ermöglichen, aus kollektiven Erfahrungen zu lernen  
- **Edge-Cloud-Koordination**: Lernen zwischen Edge-Geräten und Cloud-Infrastruktur koordinieren  

### Echtzeitverarbeitung  
- **Stream-Verarbeitung**: Kontinuierliche Datenströme auf Edge-Geräten verarbeiten  
- **Niedrige Latenz bei Inferenz**: Optimierung für minimale Inferenzlatenz  
- **Batch-Verarbeitung**: Effiziente Verarbeitung von Datenbatches auf Edge-Geräten  
- **Adaptive Verarbeitung**: Verarbeitung basierend auf aktuellen Gerätefähigkeiten anpassen  

## Fehlerbehebung bei der Entwicklung von Edge-KI  

### Häufige Probleme  
- **Speicherbeschränkungen**: Modell zu groß für den Gerätespeicher  
- **Inferenzgeschwindigkeit**: Modellinferenz zu langsam für Echtzeitanforderungen  
- **Genauigkeitsverlust**: Optimierung reduziert Modellgenauigkeit unakzeptabel  
- **Hardware-Kompatibilität**: Modell nicht kompatibel mit Zielhardware  

### Debugging-Strategien  
- **Leistungsprofiling**: Tracing-Funktionen des AI Toolkits verwenden, um Engpässe zu identifizieren  
- **Ressourcenüberwachung**: Speicher- und CPU-Nutzung während der Entwicklung überwachen  
- **Inkrementelles Testen**: Optimierungen schrittweise testen, um Probleme zu isolieren  
- **Hardware-Simulation**: Entwicklungstools verwenden, um Zielhardware zu simulieren  

### Optimierungslösungen  
- **Weitere Quantisierung**: Aggressivere Quantisierungstechniken anwenden  
- **Modellarchitektur**: Andere Modellarchitekturen in Betracht ziehen, die für Edge optimiert sind  
- **Optimierung der Vorverarbeitung**: Datenvorverarbeitung für Edge-Beschränkungen optimieren  
- **Inferenzoptimierung**: Hardware-spezifische Inferenzoptimierungen nutzen  

## Ressourcen und nächste Schritte  

### Offizielle Dokumentation  
- [AI Toolkit Entwicklerdokumentation](https://aka.ms/AIToolkit/doc)  
- [Installations- und Einrichtungsanleitung](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Dokumentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Dokumentation](https://modelcontextprotocol.io/)  

### Community und Support  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues und Feature Requests](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technische Ressourcen  
- [ONNX Runtime Dokumentation](https://onnxruntime.ai/)  
- [Ollama Dokumentation](https://ollama.ai/)  
- [Windows ML Dokumentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Lernpfade  
- [Edge-KI Grundlagenkurs](../Module01/README.md)  
- [Leitfaden für kleine Sprachmodelle](../Module02/README.md)  
- [Strategien für Edge-Bereitstellungen](../Module03/README.md)  
- [Windows Edge-KI-Entwicklung](./windowdeveloper.md)  

### Zusätzliche Ressourcen  
- **Repository-Statistiken**: 1.8k+ Sterne, 150+ Forks, 18+ Mitwirkende  
- **Lizenz**: MIT-Lizenz  
- **Sicherheit**: Microsoft-Sicherheitsrichtlinien gelten  
- **Telemetrie**: Respektiert VS Code Telemetrie-Einstellungen  

## Fazit  

Das AI Toolkit für Visual Studio Code stellt eine umfassende Plattform für moderne KI-Entwicklung dar und bietet optimierte Agentenentwicklungsfunktionen, die besonders für Edge-KI-Anwendungen wertvoll sind. Mit seinem umfangreichen Modellkatalog, der Anbieter wie Anthropic, OpenAI, GitHub und Google unterstützt, sowie lokaler Ausführung durch ONNX und Ollama bietet das Toolkit die Flexibilität, die für diverse Edge-Bereitstellungsszenarien erforderlich ist.  

Die Stärke des Toolkits liegt in seinem integrierten Ansatz – von der Modellentdeckung und -experimentierung im Playground über die anspruchsvolle Agentenentwicklung mit dem Prompt Builder, umfassende Bewertungsmöglichkeiten bis hin zur nahtlosen Integration von MCP-Tools. Für Edge-KI-Entwickler bedeutet dies schnelles Prototyping und Testen von KI-Agenten vor der Edge-Bereitstellung mit der Möglichkeit, schnell zu iterieren und für ressourcenbeschränkte Umgebungen zu optimieren.  

Wesentliche Vorteile für die Edge-KI-Entwicklung umfassen:  
- **Schnelle Experimentierung**: Modelle und Agenten schnell testen, bevor sie für die Edge-Bereitstellung festgelegt werden  
- **Multi-Anbieter-Flexibilität**: Zugriff auf Modelle aus verschiedenen Quellen, um optimale Edge-Lösungen zu finden  
- **Lokale Entwicklung**: Testen mit ONNX und Ollama für Offline- und datenschutzfreundliche Entwicklung  
- **Produktionsreife**: Produktionsbereiten Code generieren und mit externen Tools über MCP integrieren  
- **Umfassende Bewertung**: Eingebaute und benutzerdefinierte Metriken zur Validierung der Edge-KI-Leistung nutzen  

Da KI zunehmend in Richtung Edge-Bereitstellungsszenarien geht, bietet das AI Toolkit für VS Code die Entwicklungsumgebung und den Workflow, die erforderlich sind, um intelligente Anwendungen für ressourcenbeschränkte Umgebungen zu erstellen, zu testen und zu optimieren. Ob Sie IoT-Lösungen, mobile KI-Anwendungen oder eingebettete Intelligenzsysteme entwickeln, die umfassenden Funktionen und der integrierte Workflow des Toolkits unterstützen den gesamten Entwicklungszyklus für Edge-KI.  

Mit kontinuierlicher Weiterentwicklung und einer aktiven Community (1.8k+ GitHub-Sterne) bleibt das AI Toolkit an der Spitze der KI-Entwicklungstools und entwickelt sich ständig weiter, um die Bedürfnisse moderner KI-Entwickler zu erfüllen, die für Edge-Bereitstellungsszenarien bauen.  

[Next Foundry Local](./foundrylocal.md)  

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.