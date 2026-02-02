# Workshop Notebooks - Probleemoplossingsgids

## Inhoudsopgave

- [Veelvoorkomende Problemen en Oplossingen](../../../../Workshop/notebooks)
- [Specifieke Problemen bij Sessie 04](../../../../Workshop/notebooks)
- [Specifieke Problemen bij Sessie 05](../../../../Workshop/notebooks)
- [Specifieke Problemen bij Sessie 06](../../../../Workshop/notebooks)
- [Hardware-specifieke Problemen](../../../../Workshop/notebooks)
- [Diagnostische Commando's](../../../../Workshop/notebooks)
- [Hulp Krijgen](../../../../Workshop/notebooks)

---

## Veelvoorkomende Problemen en Oplossingen

### 🔴 CUDA Out of Memory

**Foutmelding:**
```
CUDA failure 2: out of memory
```

**Oorzaak:** De GPU heeft niet genoeg VRAM om het model te laden.

**Oplossingen:**

#### Optie 1: Gebruik CPU-varianten (Aanbevolen)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Optie 2: Gebruik Kleinere Modellen op GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Optie 3: Maak GPU-geheugen vrij
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Optie 4: Verhoog GPU-geheugen (indien mogelijk)
- Sluit browser-tabs, videobewerkingsprogramma's of andere GPU-apps
- Verminder visuele effecten in Windows
- Gebruik een dedicated GPU als je een geïntegreerde + dedicated GPU hebt

---

### 🔴 APIConnectionError: Verbinding Fout

**Foutmelding:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Oorzaak:** De Foundry Local-service draait niet of is niet toegankelijk.

**Oplossingen:**

#### Stap 1: Controleer de Servicestatus
```bash
foundry service status
```

#### Stap 2: Start de Service indien Gestopt
```bash
foundry service start
```

#### Stap 3: Controleer de Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Stap 4: Laad Vereiste Modellen
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Stap 5: Herstart de Notebook Kernel
Na het starten van de service en het laden van modellen, herstart de notebook kernel en voer alle cellen opnieuw uit.

---

### 🔴 Model Niet Gevonden in Catalogus

**Foutmelding:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Oorzaak:** Het model is niet gedownload of geladen in Foundry Local.

**Oplossingen:**

#### Optie 1: Download en Laad Modellen
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

#### Optie 2: Gebruik Auto-Selectiemodus
Werk je CATALOG bij om basismodelnamen te gebruiken (zonder `-cpu` suffix):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK selecteert automatisch de beste variant (CPU, GPU of NPU) voor je hardware.

---

### 🔴 HttpResponseError: 500 - Laden van Model Mislukt

**Foutmelding:**
```
HttpResponseError: 500 - Failed loading model
```

**Oorzaak:** Het modelfile is beschadigd of niet compatibel met de hardware.

**Oplossingen:**

#### Download Model Opnieuw
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Gebruik Een Andere Variant
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Geen Module Gevonden

**Foutmelding:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Oorzaak:** Het foundry-local-sdk pakket is niet geïnstalleerd.

**Oplossingen:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Trage Eerste Verzoek

**Symptoom:** De eerste voltooiing duurt meer dan 30 seconden, volgende verzoeken zijn snel.

**Oorzaak:** Dit is normaal gedrag - de service laadt het model in het geheugen bij het eerste verzoek.

**Oplossingen:**

#### Vooraf Laden van Modellen
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Houd de Service Actief
```bash
# Start service manually and leave it running
foundry service start
```

---

## Specifieke Problemen bij Sessie 04

### Verkeerde Poortconfiguratie

**Probleem:** Notebook maakt verbinding met verkeerde poort (55769 vs 59959 vs 57127)

**Oplossing:**

1. Controleer welke poort Foundry Local gebruikt:
```bash
foundry service status
# Note the port number displayed
```

2. Werk Cel 10 in de notebook bij:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Herstart kernel en voer cellen 6, 8, 10, 12, 16, 20, 22 opnieuw uit

---

### Verkeerde Modelselectie

**Probleem:** Notebook toont gpt-oss-20b of qwen2.5-7b in plaats van qwen2.5-3b

**Oplossing:**

1. Herstart de notebook kernel (leegt oude variabelen)
2. Voer Cel 10 opnieuw uit (Stel Model Aliassen in)
3. Voer Cel 12 opnieuw uit (Toon Configuratie)
4. **Controleer:** Cel 12 moet `LLM Model: qwen2.5-3b` tonen

---

### Diagnostische Cel Mislukt

**Probleem:** Cel 16 toont "❌ Foundry Local service niet gevonden!"

**Oplossing:**

1. Controleer of de service actief is:
```bash
foundry service status
```

2. Test de endpoint handmatig:
```bash
curl http://localhost:59959/v1/models
```

3. Als curl werkt maar de notebook niet:
   - Herstart de notebook kernel
   - Voer cellen opnieuw uit in volgorde: 6, 8, 10, 12, 14, 16

4. Als curl faalt:
   - Start de service: `foundry service start`
   - Laad modellen: `foundry model run phi-4-mini` en `foundry model run qwen2.5-3b`

---

### Pre-flight Check Mislukt

**Probleem:** Cel 20 toont verbindingsfouten, zelfs als de diagnostiek geslaagd is

**Oplossing:**

1. Controleer of modellen geladen zijn:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Als modellen ontbreken:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Voer Cel 20 opnieuw uit nadat modellen geladen zijn

---

### Vergelijking Mislukt met None Waarden

**Probleem:** Cel 22 voltooit maar toont latency als None

**Oplossing:**

1. Controleer eerst of de pre-flight geslaagd is (Cel 20)
2. Voer Cel 22 opnieuw uit - modellen moeten mogelijk opwarmen bij het eerste verzoek
3. Controleer of beide modellen geladen zijn: `foundry model ls`

---

## Specifieke Problemen bij Sessie 05

### Agent Gebruikt Verkeerd Model

**Probleem:** Agent gebruikt niet het verwachte model

**Oplossing:**

Controleer configuratie:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Herstart kernel als modellen incorrect zijn.

---

### Geheugen Context Overflow

**Probleem:** Reacties van agent verslechteren na verloop van tijd

**Oplossing:** Wordt automatisch afgehandeld - agents bewaren alleen de laatste 6 berichten in het geheugen.

---

## Specifieke Problemen bij Sessie 06

### Verwarring tussen CPU- en GPU-modellen

**Probleem:** CUDA-fouten bij gebruik van standaardconfiguratie

**Oplossing:** De standaardconfiguratie gebruikt nu CPU-modellen. Als je CUDA-fouten ziet:

1. Controleer of je de standaard CPU-catalogus gebruikt:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Herstart kernel en voer alle cellen opnieuw uit

---

### Intentdetectie Werkt Niet

**Probleem:** Prompts worden naar verkeerde modellen gestuurd

**Oplossing:**

Test intentdetectie:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Werk RULES bij als patronen moeten worden aangepast.

---

## Hardware-specifieke Problemen

### NVIDIA GPU

**Controleer GPU-status:**
```bash
nvidia-smi
```

**Veelvoorkomende Problemen:**
- **Verouderde driver**: Update NVIDIA-drivers
- **CUDA-versie mismatch**: Installeer Foundry Local opnieuw
- **Gefragmenteerd GPU-geheugen**: Herstart systeem

### Qualcomm NPU

**Controleer NPU-status:**
```bash
foundry device info
```

**Veelvoorkomende Problemen:**
- **NPU-drivers niet geïnstalleerd**: Installeer Qualcomm NPU-drivers
- **NPU-variant niet beschikbaar**: Gebruik CPU-variant
- **Windows-versie te oud**: Update naar de nieuwste Windows 11

### CPU-Only Systemen

**Aanbevolen Modellen:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Prestatie Tips:**
- Gebruik de kleinste modellen
- Verminder max_tokens
- Heb geduld bij het eerste verzoek

---

## Diagnostische Commando's

### Controleer Alles
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

## Hulp Krijgen

### 1. Controleer Logs
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Zoek bestaande issues: https://github.com/microsoft/Foundry-Local/issues
- Maak een nieuwe issue aan met:
  - Foutmelding (volledige tekst)
  - Output van `foundry service status`
  - Output van `foundry --version`
  - GPU/NPU-info (nvidia-smi, etc.)
  - Stappen om te reproduceren

### 3. Documentatie
- **Hoofdrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referentie**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Probleemoplossing**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Checklist voor Snelle Oplossingen

Als er iets misgaat, probeer deze stappen in volgorde:

- [ ] Controleer of de service actief is: `foundry service status`
- [ ] Herstart de service: `foundry service stop && foundry service start`
- [ ] Controleer of het model bestaat: `foundry model ls | grep phi-4-mini`
- [ ] Laad vereiste modellen: `foundry model run phi-4-mini`
- [ ] Controleer GPU-geheugen: `nvidia-smi` (indien NVIDIA)
- [ ] Probeer CPU-variant: Gebruik `phi-4-mini-cpu` in plaats van `phi-4-mini`
- [ ] Herstart de notebook kernel
- [ ] Wis notebook-uitvoer en voer alle cellen opnieuw uit
- [ ] Installeer SDK opnieuw: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Herstart systeem (laatste redmiddel)

---

## Preventietips

### Beste Praktijken

1. **Controleer altijd eerst de service:**
   ```bash
   foundry service status
   ```

2. **Gebruik standaard CPU-varianten:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Laad modellen vooraf voordat je notebooks uitvoert:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Houd de service actief:**
   - Stop/start de service niet onnodig
   - Laat het op de achtergrond draaien tussen sessies

5. **Monitor resources:**
   - Controleer GPU-geheugen voordat je begint
   - Sluit onnodige GPU-applicaties
   - Gebruik Taakbeheer / nvidia-smi

6. **Update regelmatig:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Laatst bijgewerkt:** 8 oktober 2025

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.