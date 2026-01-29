# Workshop-Notebooks – Fehlerbehebung

## Inhaltsverzeichnis

- [Häufige Probleme und Lösungen](../../../../Workshop/notebooks)
- [Sitzung 04: Spezifische Probleme](../../../../Workshop/notebooks)
- [Sitzung 05: Spezifische Probleme](../../../../Workshop/notebooks)
- [Sitzung 06: Spezifische Probleme](../../../../Workshop/notebooks)
- [Hardware-spezifische Probleme](../../../../Workshop/notebooks)
- [Diagnosebefehle](../../../../Workshop/notebooks)
- [Hilfe erhalten](../../../../Workshop/notebooks)

---

## Häufige Probleme und Lösungen

### 🔴 CUDA Out of Memory

**Fehlermeldung:**
```
CUDA failure 2: out of memory
```
  
**Ursache:** Die GPU hat nicht genügend VRAM, um das Modell zu laden.

**Lösungen:**

#### Option 1: CPU-Varianten verwenden (empfohlen)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### Option 2: Kleinere Modelle auf der GPU verwenden
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### Option 3: GPU-Speicher freigeben
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### Option 4: GPU-Speicher erhöhen (falls möglich)
- Schließen Sie Browser-Tabs, Videoeditoren oder andere GPU-Anwendungen
- Reduzieren Sie die visuellen Effekte von Windows
- Verwenden Sie eine dedizierte GPU, falls Sie eine integrierte und eine dedizierte GPU haben

---

### 🔴 APIConnectionError: Verbindungsfehler

**Fehlermeldung:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Ursache:** Der Foundry Local-Dienst läuft nicht oder ist nicht erreichbar.

**Lösungen:**

#### Schritt 1: Dienststatus überprüfen
```bash
foundry service status
```
  
#### Schritt 2: Dienst starten, falls gestoppt
```bash
foundry service start
```
  
#### Schritt 3: Endpunkt überprüfen
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### Schritt 4: Erforderliche Modelle laden
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Schritt 5: Notebook-Kernel neu starten  
Nachdem der Dienst gestartet und die Modelle geladen wurden, starten Sie den Notebook-Kernel neu und führen Sie alle Zellen erneut aus.

---

### 🔴 Modell nicht im Katalog gefunden

**Fehlermeldung:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Ursache:** Das Modell wurde nicht heruntergeladen oder in Foundry Local geladen.

**Lösungen:**

#### Option 1: Modelle herunterladen und laden
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Option 2: Auto-Auswahlmodus verwenden  
Aktualisieren Sie Ihren KATALOG, um Basis-Modellnamen (ohne `-cpu`-Suffix) zu verwenden:

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK wählt automatisch die beste Variante (CPU, GPU oder NPU) für Ihre Hardware aus.

---

### 🔴 HttpResponseError: 500 - Modell konnte nicht geladen werden

**Fehlermeldung:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Ursache:** Die Modellsdatei ist beschädigt oder mit der Hardware nicht kompatibel.

**Lösungen:**

#### Modell erneut herunterladen
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### Andere Variante verwenden
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: Kein Modul gefunden

**Fehlermeldung:**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**Ursache:** Das Paket `foundry-local-sdk` ist nicht installiert.

**Lösungen:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � Langsame erste Anfrage

**Symptom:** Die erste Anfrage dauert über 30 Sekunden, nachfolgende Anfragen sind schnell.

**Ursache:** Dies ist normales Verhalten – der Dienst lädt das Modell bei der ersten Anfrage in den Speicher.

**Lösungen:**

#### Modelle vorab laden
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### Dienst laufen lassen
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## Sitzung 04: Spezifische Probleme

### Falsche Port-Konfiguration

**Problem:** Notebook verbindet sich mit dem falschen Port (55769 vs 59959 vs 57127)

**Lösung:**

1. Überprüfen Sie, welchen Port Foundry Local verwendet:
```bash
foundry service status
# Note the port number displayed
```
  
2. Aktualisieren Sie Zelle 10 im Notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. Starten Sie den Kernel neu und führen Sie die Zellen 6, 8, 10, 12, 16, 20, 22 erneut aus.

---

### Falsche Modellauswahl

**Problem:** Notebook zeigt `gpt-oss-20b` oder `qwen2.5-7b` anstelle von `qwen2.5-3b`

**Lösung:**

1. Starten Sie den Notebook-Kernel neu (löscht alte Variablenzustände)
2. Führen Sie Zelle 10 erneut aus (Modell-Aliase setzen)
3. Führen Sie Zelle 12 erneut aus (Konfiguration anzeigen)
4. **Überprüfen:** Zelle 12 sollte `LLM Model: qwen2.5-3b` anzeigen

---

### Diagnosezelle schlägt fehl

**Problem:** Zelle 16 zeigt "❌ Foundry Local service not found!"

**Lösung:**

1. Überprüfen Sie, ob der Dienst läuft:
```bash
foundry service status
```
  
2. Testen Sie den Endpunkt manuell:
```bash
curl http://localhost:59959/v1/models
```
  
3. Wenn `curl` funktioniert, aber das Notebook nicht:
   - Starten Sie den Notebook-Kernel neu
   - Führen Sie die Zellen in der Reihenfolge aus: 6, 8, 10, 12, 14, 16

4. Wenn `curl` fehlschlägt:
   - Dienst starten: `foundry service start`
   - Modelle laden: `foundry model run phi-4-mini` und `foundry model run qwen2.5-3b`

---

### Pre-flight-Check schlägt fehl

**Problem:** Zelle 20 zeigt Verbindungsfehler, obwohl die Diagnose erfolgreich war

**Lösung:**

1. Überprüfen Sie, ob Modelle geladen sind:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Falls Modelle fehlen:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Führen Sie Zelle 20 erneut aus, nachdem die Modelle geladen wurden.

---

### Vergleich schlägt mit None-Werten fehl

**Problem:** Zelle 22 wird abgeschlossen, zeigt jedoch Latenz als None

**Lösung:**

1. Überprüfen Sie, ob der Pre-flight-Check erfolgreich war (Zelle 20)
2. Führen Sie Zelle 22 erneut aus – Modelle müssen möglicherweise bei der ersten Anfrage aufgewärmt werden
3. Überprüfen Sie, ob beide Modelle geladen sind: `foundry model ls`

---

## Sitzung 05: Spezifische Probleme

### Agent verwendet falsches Modell

**Problem:** Agent verwendet nicht das erwartete Modell

**Lösung:**

Konfiguration überprüfen:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Kernel neu starten, falls Modelle falsch sind.

---

### Speicherüberlauf im Kontext

**Problem:** Agent-Antworten verschlechtern sich mit der Zeit

**Lösung:** Bereits automatisch gehandhabt – Agents behalten nur die letzten 6 Nachrichten im Speicher.

---

## Sitzung 06: Spezifische Probleme

### Verwirrung zwischen CPU- und GPU-Modellen

**Problem:** CUDA-Fehler bei Verwendung der Standardkonfiguration

**Lösung:** Die Standardkonfiguration verwendet jetzt CPU-Modelle. Falls Sie CUDA-Fehler sehen:

1. Überprüfen Sie, ob Sie den Standard-CPU-Katalog verwenden:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. Starten Sie den Kernel neu und führen Sie alle Zellen erneut aus.

---

### Intent-Erkennung funktioniert nicht

**Problem:** Eingaben werden an falsche Modelle weitergeleitet

**Lösung:**

Intent-Erkennung testen:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Regeln aktualisieren, falls Muster angepasst werden müssen.

---

## Hardware-spezifische Probleme

### NVIDIA GPU

**GPU-Status überprüfen:**
```bash
nvidia-smi
```
  
**Häufige Probleme:**
- **Veralteter Treiber:** NVIDIA-Treiber aktualisieren
- **CUDA-Version stimmt nicht überein:** Foundry Local neu installieren
- **GPU-Speicher fragmentiert:** System neu starten

### Qualcomm NPU

**NPU-Status überprüfen:**
```bash
foundry device info
```
  
**Häufige Probleme:**
- **NPU-Treiber nicht installiert:** Qualcomm NPU-Treiber installieren
- **NPU-Variante nicht verfügbar:** CPU-Variante verwenden
- **Windows-Version zu alt:** Auf die neueste Windows 11-Version aktualisieren

### Systeme nur mit CPU

**Empfohlene Modelle:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**Leistungstipps:**
- Kleinste Modelle verwenden
- `max_tokens` reduzieren
- Geduld bei der ersten Anfrage erhöhen

---

## Diagnosebefehle

### Alles überprüfen
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```
  
### In Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```
  
---

## Hilfe erhalten

### 1. Protokolle überprüfen
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub-Issues
- Bestehende Probleme durchsuchen: https://github.com/microsoft/Foundry-Local/issues
- Neues Problem erstellen mit:
  - Fehlermeldung (vollständiger Text)
  - Ausgabe von `foundry service status`
  - Ausgabe von `foundry --version`
  - GPU/NPU-Informationen (nvidia-smi, etc.)
  - Schritte zur Reproduktion

### 3. Dokumentation
- **Hauptrepository:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-Referenz:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Fehlerbehebung:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Schnelllösungs-Checkliste

Wenn Probleme auftreten, versuchen Sie diese Schritte in der Reihenfolge:

- [ ] Überprüfen Sie, ob der Dienst läuft: `foundry service status`
- [ ] Dienst neu starten: `foundry service stop && foundry service start`
- [ ] Überprüfen Sie, ob das Modell existiert: `foundry model ls | grep phi-4-mini`
- [ ] Erforderliche Modelle laden: `foundry model run phi-4-mini`
- [ ] GPU-Speicher überprüfen: `nvidia-smi` (falls NVIDIA)
- [ ] CPU-Variante ausprobieren: Verwenden Sie `phi-4-mini-cpu` anstelle von `phi-4-mini`
- [ ] Notebook-Kernel neu starten
- [ ] Notebook-Ausgaben löschen und alle Zellen erneut ausführen
- [ ] SDK neu installieren: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] System neu starten (letzter Ausweg)

---

## Präventionstipps

### Best Practices

1. **Dienst immer zuerst überprüfen:**
   ```bash
   foundry service status
   ```
  
2. **Standardmäßig CPU-Varianten verwenden:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **Modelle vorab laden, bevor Notebooks ausgeführt werden:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **Dienst laufen lassen:**
   - Dienst nicht unnötig stoppen/starten
   - Im Hintergrund zwischen Sitzungen laufen lassen

5. **Ressourcen überwachen:**
   - GPU-Speicher vor der Ausführung überprüfen
   - Unnötige GPU-Anwendungen schließen
   - Task-Manager / nvidia-smi verwenden

6. **Regelmäßig aktualisieren:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Letzte Aktualisierung:** 8. Oktober 2025

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.