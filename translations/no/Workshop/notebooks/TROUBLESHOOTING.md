# Workshop Notebooks - Feilsøkingsguide

## Innholdsfortegnelse

- [Vanlige problemer og løsninger](../../../../Workshop/notebooks)
- [Spesifikke problemer for økt 04](../../../../Workshop/notebooks)
- [Spesifikke problemer for økt 05](../../../../Workshop/notebooks)
- [Spesifikke problemer for økt 06](../../../../Workshop/notebooks)
- [Maskinvare-spesifikke problemer](../../../../Workshop/notebooks)
- [Diagnostiske kommandoer](../../../../Workshop/notebooks)
- [Få hjelp](../../../../Workshop/notebooks)

---

## Vanlige problemer og løsninger

### 🔴 CUDA Out of Memory

**Feilmelding:**
```
CUDA failure 2: out of memory
```

**Årsak:** GPU har ikke nok VRAM til å laste modellen.

**Løsninger:**

#### Alternativ 1: Bruk CPU-varianter (anbefalt)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Alternativ 2: Bruk mindre modeller på GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Alternativ 3: Tøm GPU-minne
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Alternativ 4: Øk GPU-minne (hvis mulig)
- Lukk nettleserfaner, videoredigeringsprogrammer eller andre GPU-applikasjoner
- Reduser visuelle effekter i Windows
- Bruk dedikert GPU hvis du har både integrert og dedikert GPU

---

### 🔴 APIConnectionError: Tilkoblingsfeil

**Feilmelding:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Årsak:** Foundry Local-tjenesten kjører ikke eller er ikke tilgjengelig.

**Løsninger:**

#### Trinn 1: Sjekk tjenestestatus
```bash
foundry service status
```

#### Trinn 2: Start tjenesten hvis den er stoppet
```bash
foundry service start
```

#### Trinn 3: Verifiser endepunkt
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Trinn 4: Last inn nødvendige modeller
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Trinn 5: Start notebook-kjernen på nytt
Etter at tjenesten er startet og modellene er lastet inn, start notebook-kjernen på nytt og kjør alle celler på nytt.

---

### 🔴 Modell ikke funnet i katalogen

**Feilmelding:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Årsak:** Modellen er ikke lastet ned eller lastet inn i Foundry Local.

**Løsninger:**

#### Alternativ 1: Last ned og last inn modeller
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

#### Alternativ 2: Bruk Auto-Selection Mode
Oppdater katalogen din til å bruke basismodellnavn (uten `-cpu` suffiks):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK vil automatisk velge den beste varianten (CPU, GPU eller NPU) for maskinvaren din.

---

### 🔴 HttpResponseError: 500 - Feil ved lasting av modell

**Feilmelding:**
```
HttpResponseError: 500 - Failed loading model
```

**Årsak:** Modellfilen er korrupt eller inkompatibel med maskinvaren.

**Løsninger:**

#### Last ned modellen på nytt
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Bruk en annen variant
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Ingen modul funnet

**Feilmelding:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Årsak:** foundry-local-sdk-pakken er ikke installert.

**Løsninger:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Langsom første forespørsel

**Symptom:** Første fullføring tar 30+ sekunder, påfølgende forespørsler er raske.

**Årsak:** Dette er normal oppførsel - tjenesten laster modellen inn i minnet ved første forespørsel.

**Løsninger:**

#### Forhåndslast modeller
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Hold tjenesten i gang
```bash
# Start service manually and leave it running
foundry service start
```

---

## Spesifikke problemer for økt 04

### Feil portkonfigurasjon

**Problem:** Notebook kobler til feil port (55769 vs 59959 vs 57127)

**Løsning:**

1. Sjekk hvilken port Foundry Local bruker:
```bash
foundry service status
# Note the port number displayed
```

2. Oppdater celle 10 i notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Start kjernen på nytt og kjør cellene 6, 8, 10, 12, 16, 20, 22 på nytt

---

### Feil modellvalg

**Problem:** Notebook viser gpt-oss-20b eller qwen2.5-7b i stedet for qwen2.5-3b

**Løsning:**

1. Start notebook-kjernen på nytt (tømmer gamle variabler)
2. Kjør celle 10 på nytt (Sett modellaliaser)
3. Kjør celle 12 på nytt (Vis konfigurasjon)
4. **Verifiser:** Celle 12 skal vise `LLM Model: qwen2.5-3b`

---

### Diagnostisk celle feiler

**Problem:** Celle 16 viser "❌ Foundry Local service not found!"

**Løsning:**

1. Verifiser at tjenesten kjører:
```bash
foundry service status
```

2. Test endepunkt manuelt:
```bash
curl http://localhost:59959/v1/models
```

3. Hvis curl fungerer, men notebook ikke gjør det:
   - Start notebook-kjernen på nytt
   - Kjør cellene i rekkefølge: 6, 8, 10, 12, 14, 16

4. Hvis curl feiler:
   - Start tjenesten: `foundry service start`
   - Last inn modeller: `foundry model run phi-4-mini` og `foundry model run qwen2.5-3b`

---

### Pre-flight-sjekk feiler

**Problem:** Celle 20 viser tilkoblingsfeil selv om diagnostikken er bestått

**Løsning:**

1. Sjekk at modellene er lastet inn:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Hvis modeller mangler:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Kjør celle 20 på nytt etter at modellene er lastet inn

---

### Sammenligning feiler med None-verdier

**Problem:** Celle 22 fullføres, men viser latens som None

**Løsning:**

1. Sjekk at pre-flight er bestått først (Celle 20)
2. Kjør celle 22 på nytt - modellene kan trenge oppvarming ved første forespørsel
3. Verifiser at begge modellene er lastet inn: `foundry model ls`

---

## Spesifikke problemer for økt 05

### Agent bruker feil modell

**Problem:** Agenten bruker ikke forventet modell

**Løsning:**

Verifiser konfigurasjonen:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Start kjernen på nytt hvis modellene er feil.

---

### Minnekontekst overskrides

**Problem:** Agentens svar blir dårligere over tid

**Løsning:** Allerede håndtert automatisk - agenter beholder kun de siste 6 meldingene i minnet.

---

## Spesifikke problemer for økt 06

### Forvirring mellom CPU- og GPU-modeller

**Problem:** Får CUDA-feil når du bruker standardkonfigurasjonen

**Løsning:** Standardkonfigurasjonen bruker nå CPU-modeller. Hvis du ser CUDA-feil:

1. Verifiser at du bruker standard CPU-katalog:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Start kjernen på nytt og kjør alle celler på nytt

---

### Intent-gjenkjenning fungerer ikke

**Problem:** Prompter blir sendt til feil modeller

**Løsning:**

Test intent-gjenkjenning:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Oppdater RULES hvis mønstre trenger justering.

---

## Maskinvare-spesifikke problemer

### NVIDIA GPU

**Sjekk GPU-status:**
```bash
nvidia-smi
```

**Vanlige problemer:**
- **Utdatert driver**: Oppdater NVIDIA-drivere
- **CUDA-versjon mismatch**: Installer Foundry Local på nytt
- **Fragmentert GPU-minne**: Start systemet på nytt

### Qualcomm NPU

**Sjekk NPU-status:**
```bash
foundry device info
```

**Vanlige problemer:**
- **NPU-drivere ikke installert**: Installer Qualcomm NPU-drivere
- **NPU-variant ikke tilgjengelig**: Bruk CPU-variant
- **Windows-versjon for gammel**: Oppdater til nyeste Windows 11

### Kun CPU-systemer

**Anbefalte modeller:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Ytelsestips:**
- Bruk de minste modellene
- Reduser max_tokens
- Vær tålmodig med første forespørsel

---

## Diagnostiske kommandoer

### Sjekk alt
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

### I Python
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

## Få hjelp

### 1. Sjekk logger
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Søk etter eksisterende problemer: https://github.com/microsoft/Foundry-Local/issues
- Opprett nytt problem med:
  - Feilmelding (full tekst)
  - Output fra `foundry service status`
  - Output fra `foundry --version`
  - GPU/NPU-info (nvidia-smi, etc.)
  - Steg for å reprodusere

### 3. Dokumentasjon
- **Hovedrepository**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-referanse**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Feilsøking**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Sjekkliste for raske løsninger

Når ting går galt, prøv disse i rekkefølge:

- [ ] Sjekk at tjenesten kjører: `foundry service status`
- [ ] Start tjenesten på nytt: `foundry service stop && foundry service start`
- [ ] Verifiser at modellen eksisterer: `foundry model ls | grep phi-4-mini`
- [ ] Last inn nødvendige modeller: `foundry model run phi-4-mini`
- [ ] Sjekk GPU-minne: `nvidia-smi` (hvis NVIDIA)
- [ ] Prøv CPU-variant: Bruk `phi-4-mini-cpu` i stedet for `phi-4-mini`
- [ ] Start notebook-kjernen på nytt
- [ ] Tøm notebook-utganger og kjør alle celler på nytt
- [ ] Installer SDK på nytt: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Start systemet på nytt (siste utvei)

---

## Forebyggingstips

### Beste praksis

1. **Sjekk alltid tjenesten først:**
   ```bash
   foundry service status
   ```

2. **Bruk CPU-varianter som standard:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Forhåndslast modeller før du kjører notebooks:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Hold tjenesten i gang:**
   - Ikke stopp/start tjenesten unødvendig
   - La den kjøre i bakgrunnen mellom økter

5. **Overvåk ressurser:**
   - Sjekk GPU-minne før du kjører
   - Lukk unødvendige GPU-applikasjoner
   - Bruk Oppgavebehandling / nvidia-smi

6. **Oppdater regelmessig:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Sist oppdatert:** 8. oktober 2025

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.