<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e8d157e0a282083a1e1c7bb5dda28646",
  "translation_date": "2025-10-30T10:44:02+00:00",
  "source_file": "Module04/README.md",
  "language_code": "de"
}
-->
# Kapitel 04: Modellformatkonvertierung und Quantisierung - Kapitelübersicht

Die Entwicklung von EdgeAI hat die Modellformatkonvertierung und Quantisierung zu unverzichtbaren Technologien gemacht, um anspruchsvolle maschinelle Lernfähigkeiten auf ressourcenbeschränkten Geräten bereitzustellen. Dieses umfassende Kapitel bietet eine vollständige Anleitung zum Verständnis, zur Implementierung und Optimierung von Modellen für Edge-Deployment-Szenarien.

## 📚 Kapitelstruktur und Lernpfad

Dieses Kapitel ist in sieben aufeinander aufbauende Abschnitte gegliedert, die zusammen ein umfassendes Verständnis der Modelloptimierung für Edge-Computing schaffen:

---

## [Abschnitt 1: Grundlagen der Modellformatkonvertierung und Quantisierung](./01.Introduce.md)

### 🎯 Überblick
Dieser grundlegende Abschnitt legt das theoretische Fundament für die Modelloptimierung in Edge-Computing-Umgebungen und behandelt Quantisierungsgrenzen von 1-Bit bis 8-Bit Präzisionsstufen sowie wichtige Strategien zur Formatkonvertierung.

**Wichtige Themen:**
- Präzisionsklassifizierungsrahmen (ultra-niedrig, niedrig, mittlere Präzision)
- Vorteile und Anwendungsfälle von GGUF- und ONNX-Formaten
- Vorteile der Quantisierung für Betriebseffizienz und Flexibilität bei der Bereitstellung
- Leistungsbenchmarks und Vergleich des Speicherbedarfs

**Lernziele:**
- Verständnis der Quantisierungsgrenzen und Klassifikationen
- Identifikation geeigneter Formatkonvertierungstechniken
- Erlernen fortgeschrittener Optimierungsstrategien für Edge-Deployment

---

## [Abschnitt 2: Llama.cpp Implementierungsanleitung](./02.Llamacpp.md)

### 🎯 Überblick
Ein umfassendes Tutorial zur Implementierung von Llama.cpp, einem leistungsstarken C++-Framework, das effiziente Inferenz von großen Sprachmodellen mit minimalem Setup auf verschiedenen Hardwarekonfigurationen ermöglicht.

**Wichtige Themen:**
- Installation auf Windows-, macOS- und Linux-Plattformen
- GGUF-Formatkonvertierung und verschiedene Quantisierungsstufen (Q2_K bis Q8_0)
- Hardwarebeschleunigung mit CUDA, Metal, OpenCL und Vulkan
- Python-Integration und Strategien für die Produktionsbereitstellung

**Lernziele:**
- Beherrschung der plattformübergreifenden Installation und des Build-Prozesses aus dem Quellcode
- Implementierung von Modellquantisierungs- und Optimierungstechniken
- Bereitstellung von Modellen im Servermodus mit REST-API-Integration

---

## [Abschnitt 3: Microsoft Olive Optimierungssuite](./03.MicrosoftOlive.md)

### 🎯 Überblick
Erkundung von Microsoft Olive, einem hardwarebewussten Modelloptimierungstoolkit mit über 40 integrierten Optimierungskomponenten, das für die unternehmensgerechte Bereitstellung von Modellen auf verschiedenen Hardwareplattformen entwickelt wurde.

**Wichtige Themen:**
- Auto-Optimierungsfunktionen mit dynamischer und statischer Quantisierung
- Hardwarebewusste Intelligenz für CPU-, GPU- und NPU-Bereitstellung
- Unterstützung beliebter Modelle (Llama, Phi, Qwen, Gemma) direkt einsatzbereit
- Unternehmensintegration mit Azure ML und Produktionsworkflows

**Lernziele:**
- Nutzung automatisierter Optimierung für verschiedene Modellarchitekturen
- Implementierung plattformübergreifender Bereitstellungsstrategien
- Aufbau unternehmensgerechter Optimierungspipelines

---

## [Abschnitt 4: OpenVINO Toolkit Optimierungssuite](./04.openvino.md)

### 🎯 Überblick
Umfassende Erkundung des OpenVINO-Toolkits von Intel, einer Open-Source-Plattform für die Bereitstellung leistungsstarker KI-Lösungen in Cloud-, On-Premises- und Edge-Umgebungen mit fortschrittlichen Funktionen des Neural Network Compression Framework (NNCF).

**Wichtige Themen:**
- Plattformübergreifende Bereitstellung mit Hardwarebeschleunigung (CPU, GPU, VPU, KI-Beschleuniger)
- Neural Network Compression Framework (NNCF) für fortschrittliche Quantisierung und Pruning
- OpenVINO GenAI für die Optimierung und Bereitstellung großer Sprachmodelle
- Unternehmensgerechte Modellserver-Funktionen und skalierbare Bereitstellungsstrategien

**Lernziele:**
- Beherrschung der OpenVINO-Modellkonvertierungs- und Optimierungsworkflows
- Implementierung fortschrittlicher Quantisierungstechniken mit NNCF
- Bereitstellung optimierter Modelle auf verschiedenen Hardwareplattformen mit Model Server

---

## [Abschnitt 5: Apple MLX Framework im Detail](./05.AppleMLX.md)

### 🎯 Überblick
Umfassende Abdeckung von Apple MLX, einem revolutionären Framework, das speziell für effizientes maschinelles Lernen auf Apple Silicon entwickelt wurde, mit Schwerpunkt auf Fähigkeiten großer Sprachmodelle und lokaler Bereitstellung.

**Wichtige Themen:**
- Vorteile der einheitlichen Speicherarchitektur und Metal Performance Shaders
- Unterstützung für LLaMA, Mistral, Phi-3, Qwen und Code Llama Modelle
- LoRA-Feinabstimmung für effiziente Modellanpassung
- Integration von Hugging Face und Quantisierungsunterstützung (4-Bit und 8-Bit)

**Lernziele:**
- Optimierung von Apple Silicon für die Bereitstellung von LLMs
- Implementierung von Feinabstimmungs- und Modellanpassungstechniken
- Aufbau von Unternehmens-KI-Anwendungen mit erweiterten Datenschutzfunktionen

---

## [Abschnitt 6: Synthese des Edge-AI-Entwicklungsworkflows](./06.workflow-synthesis.md)

### 🎯 Überblick
Umfassende Synthese aller Optimierungsframeworks in einheitliche Workflows, Entscheidungsbäume und Best Practices für produktionsreife Edge-AI-Bereitstellung auf verschiedenen Plattformen und Anwendungsfällen, einschließlich mobiler Geräte, Desktop und Cloud-Umgebungen.

**Wichtige Themen:**
- Einheitliche Workflow-Architektur, die mehrere Optimierungsframeworks integriert
- Entscheidungsbäume zur Auswahl von Frameworks und Analyse von Leistungskompromissen
- Validierung der Produktionsbereitschaft und umfassende Bereitstellungsstrategien
- Zukunftssichere Strategien für aufkommende Hardware und Modellarchitekturen

**Lernziele:**
- Systematische Auswahl von Frameworks basierend auf Anforderungen und Einschränkungen
- Implementierung produktionsreifer Edge-AI-Pipelines mit umfassendem Monitoring
- Gestaltung anpassungsfähiger Workflows, die sich mit neuen Technologien und Anforderungen weiterentwickeln

---

## [Abschnitt 7: Qualcomm QNN Optimierungssuite](./07.QualcommQNN.md)

### 🎯 Überblick
Umfassende Erkundung von Qualcomm QNN (Qualcomm Neural Network), einem einheitlichen KI-Inferenz-Framework, das darauf ausgelegt ist, die heterogene Computerarchitektur von Qualcomm, einschließlich Hexagon NPU, Adreno GPU und Kryo CPU, für maximale Leistung und Energieeffizienz auf mobilen und Edge-Geräten zu nutzen.

**Wichtige Themen:**
- Heterogenes Computing mit einheitlichem Zugriff auf NPU, GPU und CPU
- Hardwarebewusste Optimierung für Snapdragon-Plattformen mit intelligenter Arbeitslastverteilung
- Fortgeschrittene Quantisierungstechniken (INT8, INT16, gemischte Präzision) für mobile Bereitstellung
- Energieeffiziente Inferenz optimiert für batteriebetriebene Geräte und Echtzeitanwendungen

**Lernziele:**
- Beherrschung der Qualcomm-Hardwarebeschleunigung für mobile KI-Bereitstellung
- Implementierung energieeffizienter Optimierungsstrategien für Edge-Computing
- Bereitstellung produktionsreifer Modelle im Qualcomm-Ökosystem mit optimaler Leistung

---

## 🎯 Lernziele des Kapitels

Nach Abschluss dieses umfassenden Kapitels werden die Leser folgende Fähigkeiten erreichen:

### **Technische Kompetenz**
- Tiefes Verständnis der Quantisierungsgrenzen und praktischen Anwendungen
- Praktische Erfahrung mit mehreren Optimierungsframeworks
- Fähigkeiten zur Produktionsbereitstellung für Edge-Computing-Umgebungen

### **Strategisches Verständnis**
- Fähigkeiten zur Auswahl hardwarebewusster Optimierungen
- Fundierte Entscheidungsfindung bei Leistungskompromissen
- Unternehmensgerechte Bereitstellungs- und Überwachungsstrategien

### **Leistungsbenchmarks**

| Framework | Quantisierung | Speicherverbrauch | Geschwindigkeitsverbesserung | Anwendungsfall |
|-----------|---------------|-------------------|------------------------------|----------------|
| Llama.cpp | Q4_K_M | ~4GB | 2-3x | Plattformübergreifende Bereitstellung |
| Olive | INT4 | 60-75% Reduktion | 2-6x | Unternehmensworkflows |
| OpenVINO | INT8/INT4 | 50-75% Reduktion | 2-5x | Intel-Hardware-Optimierung |
| QNN | INT8/INT4 | 50-80% Reduktion | 5-15x | Qualcomm Mobile/Edge |
| MLX | 4-Bit | ~4GB | 2-4x | Apple Silicon Optimierung |

## 🚀 Nächste Schritte und fortgeschrittene Anwendungen

Dieses Kapitel bietet eine vollständige Grundlage für:
- Entwicklung benutzerdefinierter Modelle für spezifische Domänen
- Forschung in der Edge-AI-Optimierung
- Entwicklung kommerzieller KI-Anwendungen
- Großflächige Unternehmensbereitstellungen von Edge-AI

Das Wissen aus diesen sieben Abschnitten bietet ein umfassendes Toolkit, um sich in der sich schnell entwickelnden Landschaft der Edge-AI-Modelloptimierung und -Bereitstellung zurechtzufinden.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.