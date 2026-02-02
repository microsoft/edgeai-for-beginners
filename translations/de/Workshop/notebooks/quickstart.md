# Workshop-Notebooks - Schnellstartanleitung

## Inhaltsverzeichnis

- [Voraussetzungen](../../../../Workshop/notebooks)
- [Erste Einrichtung](../../../../Workshop/notebooks)
- [Session 04: Modellvergleich](../../../../Workshop/notebooks)
- [Session 05: Multi-Agent-Orchestrator](../../../../Workshop/notebooks)
- [Session 06: Intent-basierte Modellweiterleitung](../../../../Workshop/notebooks)
- [Umgebungsvariablen](../../../../Workshop/notebooks)
- [Häufige Befehle](../../../../Workshop/notebooks)

---

## Voraussetzungen

### 1. Foundry Local installieren

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installation überprüfen:**
```bash
foundry --version
```

### 2. Python-Abhängigkeiten installieren

```bash
cd Workshop
pip install -r requirements.txt
```

Oder einzeln installieren:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Erste Einrichtung

### Foundry Local Service starten

**Erforderlich vor dem Ausführen eines Notebooks:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Erwartete Ausgabe:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Modelle herunterladen und laden

Die Notebooks verwenden standardmäßig diese Modelle:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Einrichtung überprüfen

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04: Modellvergleich

### Ziel
Vergleich der Leistung zwischen Small Language Models (SLM) und Large Language Models (LLM).

### Schnelle Einrichtung

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Notebook ausführen

1. **Öffnen** Sie `session04_model_compare.ipynb` in VS Code oder Jupyter
2. **Kernel neu starten** (Kernel → Kernel neu starten)
3. **Alle Zellen ausführen** in der richtigen Reihenfolge

### Wichtige Konfiguration

**Standardmodelle:**
- **SLM:** `phi-4-mini` (~4GB RAM, schneller)
- **LLM:** `qwen2.5-3b` (~3GB RAM, speicheroptimiert)

**Umgebungsvariablen (optional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Erwartete Ausgabe

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Anpassung

**Andere Modelle verwenden:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Benutzerdefinierte Eingabeaufforderung:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Validierungs-Checkliste

- [ ] Zelle 12 zeigt die richtigen Modelle (phi-4-mini, qwen2.5-3b)
- [ ] Zelle 12 zeigt den richtigen Endpunkt (Port 59959)
- [ ] Zelle 16 Diagnosetest bestanden (✅ Service läuft)
- [ ] Zelle 20 Vorabprüfung bestanden (beide Modelle ok)
- [ ] Zelle 22 Vergleich abgeschlossen mit Latenzwerten
- [ ] Zelle 24 Validierung zeigt 🎉 ALLE TESTS BESTANDEN!

### Zeitaufwand
- **Erster Durchlauf:** 5-10 Minuten (einschließlich Modell-Downloads)
- **Weitere Durchläufe:** 1-2 Minuten

---

## Session 05: Multi-Agent-Orchestrator

### Ziel
Demonstration der Zusammenarbeit mehrerer Agenten mit dem Foundry Local SDK - Agenten arbeiten zusammen, um verfeinerte Ergebnisse zu erzielen.

### Schnelle Einrichtung

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Notebook ausführen

1. **Öffnen** Sie `session05_agents_orchestrator.ipynb`
2. **Kernel neu starten**
3. **Alle Zellen ausführen** in der richtigen Reihenfolge

### Wichtige Konfiguration

**Standardkonfiguration (gleiches Modell für beide Agenten):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Erweiterte Konfiguration (verschiedene Modelle):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architektur

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Erwartete Ausgabe

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Erweiterungen

**Weitere Agenten hinzufügen:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Batch-Tests durchführen:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Zeitaufwand
- **Erster Durchlauf:** 3-5 Minuten
- **Weitere Durchläufe:** 1-2 Minuten pro Frage

---

## Session 06: Intent-basierte Modellweiterleitung

### Ziel
Eingaben intelligent an spezialisierte Modelle weiterleiten, basierend auf erkanntem Intent.

### Schnelle Einrichtung

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Hinweis:** Session 06 verwendet standardmäßig CPU-Modelle für maximale Kompatibilität.

### Notebook ausführen

1. **Öffnen** Sie `session06_models_router.ipynb`
2. **Kernel neu starten**
3. **Alle Zellen ausführen** in der richtigen Reihenfolge

### Wichtige Konfiguration

**Standardkatalog (CPU-Modelle):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternative (GPU-Modelle):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Intent-Erkennung

Der Router verwendet Regex-Muster zur Intent-Erkennung:

| Intent | Musterbeispiele | Weitergeleitet an |
|--------|-----------------|-------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Alles andere | phi-4-mini-cpu |

### Erwartete Ausgabe

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Anpassung

**Benutzerdefinierten Intent hinzufügen:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Token-Tracking aktivieren:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Wechsel zu GPU-Modellen

Falls Sie über 8GB+ VRAM verfügen:

1. Kommentieren Sie in **Zelle #6** den CPU-Katalog aus
2. Heben Sie die Auskommentierung des GPU-Katalogs auf
3. Laden Sie GPU-Modelle:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Kernel neu starten und Notebook erneut ausführen

### Zeitaufwand
- **Erster Durchlauf:** 5-10 Minuten (Modell-Laden)
- **Weitere Durchläufe:** 30-60 Sekunden pro Test

---

## Umgebungsvariablen

### Globale Konfiguration

Vor dem Start von Jupyter/VS Code festlegen:

**Windows (Eingabeaufforderung):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Konfiguration im Notebook

Am Anfang eines Notebooks festlegen:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Häufige Befehle

### Service-Verwaltung

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Modell-Verwaltung

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Endpunkte testen

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Diagnose-Befehle

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Best Practices

### Vor dem Start eines Notebooks

1. **Überprüfen, ob der Service läuft:**
   ```bash
   foundry service status
   ```

2. **Verifizieren, dass Modelle geladen sind:**
   ```bash
   foundry model ls
   ```

3. **Notebook-Kernel neu starten**, falls erneut ausgeführt

4. **Alle Ausgaben löschen** für einen sauberen Durchlauf

### Ressourcenmanagement

1. **Standardmäßig CPU-Modelle verwenden** für Kompatibilität
2. **Zu GPU-Modellen wechseln**, nur wenn Sie über 8GB+ VRAM verfügen
3. **Andere GPU-Anwendungen schließen**, bevor Sie starten
4. **Service zwischen Notebook-Sitzungen laufen lassen**
5. **Ressourcennutzung überwachen** mit Task-Manager / nvidia-smi

### Fehlerbehebung

1. **Service immer zuerst überprüfen**, bevor Sie den Code debuggen
2. **Kernel neu starten**, falls veraltete Konfiguration angezeigt wird
3. **Diagnosezellen erneut ausführen** nach Änderungen
4. **Modellnamen überprüfen**, ob sie geladen sind
5. **Endpunkt-Port verifizieren**, ob er mit dem Service-Status übereinstimmt

---

## Schnellreferenz: Modell-Aliase

### Häufige Modelle

| Alias | Größe | Am besten geeignet für | RAM/VRAM | Varianten |
|-------|-------|-------------------------|----------|-----------|
| `phi-4-mini` | ~4B | Allgemeiner Chat, Zusammenfassungen | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Code-Generierung, Refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Allgemeine Aufgaben, effizient | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Schnell, geringe Ressourcen | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klassifikation, minimale Ressourcen | 1-2GB | `-cpu`, `-cuda-gpu` |

### Varianten-Namensgebung

- **Basisname** (z. B. `phi-4-mini`): Wählt automatisch die beste Variante für Ihre Hardware aus
- **`-cpu`**: CPU-optimiert, funktioniert überall
- **`-cuda-gpu`**: NVIDIA GPU-optimiert, erfordert 8GB+ VRAM
- **`-npu`**: Qualcomm NPU-optimiert, erfordert NPU-Treiber

**Empfehlung:** Verwenden Sie Basisnamen (ohne Suffix) und lassen Sie Foundry Local die beste Variante automatisch auswählen.

---

## Erfolgsindikatoren

Sie sind bereit, wenn Sie Folgendes sehen:

✅ `foundry service status` zeigt "running"
✅ `foundry model ls` zeigt Ihre benötigten Modelle
✅ Service ist am richtigen Endpunkt zugänglich
✅ Gesundheitsprüfung gibt 200 OK zurück
✅ Notebook-Diagnosezellen bestehen
✅ Keine Verbindungsfehler in der Ausgabe

---

## Hilfe erhalten

### Dokumentation
- **Hauptrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-Referenz**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Fehlerbehebung**: Siehe `troubleshooting.md` in diesem Verzeichnis

### GitHub-Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Letzte Aktualisierung:** 8. Oktober 2025  
**Version:** Workshop-Notebooks 2.0

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.