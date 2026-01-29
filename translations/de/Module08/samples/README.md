# Modul 08 Beispiele: Leitfaden für die lokale Entwicklung mit Foundry

## Überblick

Diese umfassende Sammlung zeigt sowohl Ansätze mit dem **Foundry Local SDK** als auch mit **Shell-Befehlen** zur Entwicklung von produktionsreifen KI-Anwendungen. Jedes Beispiel beleuchtet verschiedene Aspekte der Edge-KI-Entwicklung, von grundlegender REST-Integration bis hin zu fortgeschrittenen Multi-Agenten-Systemen.

## Entwicklungsansatz: SDK vs. Shell-Befehle

### Verwenden Sie das Foundry Local SDK, wenn:

- **Programmgesteuerte Kontrolle**: Sie benötigen vollständige Kontrolle über den Lebenszyklus von Agenten, Evaluierungs- oder Bereitstellungs-Workflows
- **Individuelle Tools**: Automatisierung rund um Foundry Local erstellen (CI/CD-Integration, Multi-Agenten-Orchestrierung)
- **Feingranularer Zugriff**: Detaillierte Agenten-Metadaten, Versionierung oder Kontrolle des Evaluierungsrunners erforderlich sind
- **Python-Integration**: Arbeiten in Python-lastigen Umgebungen oder Einbettung von Foundry-Logik in umfassendere Anwendungen
- **Unternehmens-Workflows**: Modulare Workflows und reproduzierbare Evaluierungspipelines implementieren, die mit Microsoft-Referenzarchitekturen übereinstimmen

### Verwenden Sie Shell-Befehle, wenn:

- **Schnelles Testen**: Schnelle lokale Tests, manuelle Agentenstarts oder Überprüfung der Einrichtung durchführen
- **CLI-Einfachheit**: Einfache CLI-Operationen benötigen, um Agenten zu starten/stoppen, Logs zu überprüfen oder grundlegende Evaluierungen durchzuführen
- **Leichte Automatisierung**: Einfache Automatisierungsskripte ohne vollständige SDK-Integrationsanforderungen erstellen
- **Schnelle Iteration**: Debugging- und Entwicklungszyklen, insbesondere in eingeschränkten Umgebungen oder bei Bereitstellungen auf Ressourcengruppenebene
- **Einrichtung & Validierung**: Erste Konfiguration der Umgebung und schnelle Überprüfungsaufgaben durchführen

## Best Practices & Empfohlener Workflow

Basierend auf Prinzipien des Agenten-Lebenszyklusmanagements, der Abhängigkeitsverfolgung und der reproduzierbaren Nutzung mit minimalen Berechtigungen:

### Phase 1: Grundlagen & Einrichtung
1. **Beginnen Sie mit Shell-Befehlen** für die erste Einrichtung und schnelle Validierung
2. **Überprüfen Sie die Umgebung** mit CLI-Tools und grundlegender Modellbereitstellung
3. **Testen Sie die Konnektivität** mit einfachen REST-Aufrufen und Gesundheitschecks

### Phase 2: Entwicklung & Integration
1. **Wechseln Sie zum SDK** für skalierbare und nachvollziehbare Workflows
2. **Implementieren Sie programmgesteuerte Kontrolle** für komplexe Agenten-Interaktionen
3. **Erstellen Sie individuelle Tools** für community-fähige Vorlagen und Azure OpenAI-Integration

### Phase 3: Produktion & Skalierung
1. **Hybrider Ansatz**: Kombination von CLI für Betrieb und SDK für Anwendungslogik
2. **Unternehmensintegration** mit Monitoring, Logging und Bereitstellungspipelines
3. **Community-Beitrag** durch wiederverwendbare Vorlagen und Best Practices

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.