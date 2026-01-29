# Workshop-muistikirjat - Pikaopas

## Sisällysluettelo

- [Edellytykset](../../../../Workshop/notebooks)
- [Alkuasetukset](../../../../Workshop/notebooks)
- [Istunto 04: Mallien vertailu](../../../../Workshop/notebooks)
- [Istunto 05: Moniagenttinen orkestrointi](../../../../Workshop/notebooks)
- [Istunto 06: Aikomuspohjainen mallien reititys](../../../../Workshop/notebooks)
- [Ympäristömuuttujat](../../../../Workshop/notebooks)
- [Yleiset komennot](../../../../Workshop/notebooks)

---

## Edellytykset

### 1. Asenna Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Vahvista asennus:**
```bash
foundry --version
```

### 2. Asenna Python-riippuvuudet

```bash
cd Workshop
pip install -r requirements.txt
```

Tai asenna yksitellen:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Alkuasetukset

### Käynnistä Foundry Local -palvelu

**Vaaditaan ennen minkään muistikirjan suorittamista:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Odotettu tulos:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Lataa ja lataa mallit

Muistikirjat käyttävät oletuksena näitä malleja:

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

### Vahvista asetukset

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Istunto 04: Mallien vertailu

### Tarkoitus
Vertaa Small Language Models (SLM) ja Large Language Models (LLM) suorituskykyä.

### Pika-asetus

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Muistikirjan suorittaminen

1. **Avaa** `session04_model_compare.ipynb` VS Codessa tai Jupyterissä
2. **Käynnistä ydin uudelleen** (Kernel → Restart Kernel)
3. **Suorita kaikki solut** järjestyksessä

### Keskeiset asetukset

**Oletusmallit:**
- **SLM:** `phi-4-mini` (~4GB RAM, nopeampi)
- **LLM:** `qwen2.5-3b` (~3GB RAM, muistitehokas)

**Ympäristömuuttujat (valinnainen):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Odotettu tulos

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

### Mukauttaminen

**Käytä eri malleja:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Mukautettu kehotus:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Vahvistuslista

- [ ] Solu 12 näyttää oikeat mallit (phi-4-mini, qwen2.5-3b)
- [ ] Solu 12 näyttää oikean päätepisteen (portti 59959)
- [ ] Solu 16 diagnostiikka onnistuu (✅ Palvelu käynnissä)
- [ ] Solu 20 esitarkistus onnistuu (molemmat mallit ok)
- [ ] Solu 22 vertailu valmistuu viivearvoilla
- [ ] Solu 24 vahvistus näyttää 🎉 KAIKKI TARKISTUKSET ONNISTUIVAT!

### Aika-arvio
- **Ensimmäinen suoritus:** 5-10 minuuttia (sisältäen mallien lataukset)
- **Seuraavat suoritukset:** 1-2 minuuttia

---

## Istunto 05: Moniagenttinen orkestrointi

### Tarkoitus
Esittele moniagenttista yhteistyötä Foundry Local SDK:n avulla - agentit työskentelevät yhdessä tuottaakseen tarkennettuja tuloksia.

### Pika-asetus

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Muistikirjan suorittaminen

1. **Avaa** `session05_agents_orchestrator.ipynb`
2. **Käynnistä ydin uudelleen**
3. **Suorita kaikki solut** järjestyksessä

### Keskeiset asetukset

**Oletusasetus (Sama malli molemmille agenteille):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Edistynyt asetus (Eri mallit):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arkkitehtuuri

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

### Odotettu tulos

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

### Laajennukset

**Lisää lisää agentteja:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Erätestaus:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Aika-arvio
- **Ensimmäinen suoritus:** 3-5 minuuttia
- **Seuraavat suoritukset:** 1-2 minuuttia per kysymys

---

## Istunto 06: Aikomuspohjainen mallien reititys

### Tarkoitus
Reititä kehotukset älykkäästi erikoistuneille malleille havaittujen aikomusten perusteella.

### Pika-asetus

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Huom:** Istunto 06 käyttää oletuksena CPU-malleja maksimaalisen yhteensopivuuden vuoksi.

### Muistikirjan suorittaminen

1. **Avaa** `session06_models_router.ipynb`
2. **Käynnistä ydin uudelleen**
3. **Suorita kaikki solut** järjestyksessä

### Keskeiset asetukset

**Oletuskatalogi (CPU-mallit):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Vaihtoehto (GPU-mallit):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Aikomusten tunnistus

Reititin käyttää regex-kuvioita aikomusten tunnistamiseen:

| Aikomus | Esimerkki kuvioita | Reititetty |
|---------|--------------------|------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Kaikki muu | phi-4-mini-cpu |

### Odotettu tulos

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

### Mukauttaminen

**Lisää mukautettu aikomus:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Ota käyttöön token-seuranta:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Siirtyminen GPU-malleihin

Jos sinulla on 8GB+ VRAM:

1. Solussa **#6**, kommentoi CPU-katalogi
2. Poista GPU-katalogin kommentointi
3. Lataa GPU-mallit:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Käynnistä ydin uudelleen ja suorita muistikirja uudelleen

### Aika-arvio
- **Ensimmäinen suoritus:** 5-10 minuuttia (mallien lataus)
- **Seuraavat suoritukset:** 30-60 sekuntia per testi

---

## Ympäristömuuttujat

### Globaalit asetukset

Aseta ennen Jupyterin/VS Coden käynnistämistä:

**Windows (Komentokehote):**
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

### Muistikirjan sisäiset asetukset

Aseta minkä tahansa muistikirjan alussa:

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

## Yleiset komennot

### Palvelun hallinta

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

### Mallien hallinta

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

### Päätepisteiden testaus

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

### Diagnostiikkakomennot

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

## Parhaat käytännöt

### Ennen minkään muistikirjan aloittamista

1. **Tarkista, että palvelu on käynnissä:**
   ```bash
   foundry service status
   ```

2. **Vahvista, että mallit on ladattu:**
   ```bash
   foundry model ls
   ```

3. **Käynnistä muistikirjan ydin uudelleen** jos suoritat uudelleen

4. **Tyhjennä kaikki tulosteet** puhdasta suoritusta varten

### Resurssien hallinta

1. **Käytä CPU-malleja oletuksena** yhteensopivuuden vuoksi
2. **Vaihda GPU-malleihin** vain jos sinulla on 8GB+ VRAM
3. **Sulje muut GPU-sovellukset** ennen suorittamista
4. **Pidä palvelu käynnissä** muistikirjaistuntojen välillä
5. **Seuraa resurssien käyttöä** Task Managerilla / nvidia-smillä

### Vianetsintä

1. **Tarkista aina palvelu ensin** ennen koodin vianetsintää
2. **Käynnistä ydin uudelleen** jos näet vanhentuneen asetuksen
3. **Suorita diagnostiikkasolut uudelleen** muutosten jälkeen
4. **Tarkista mallien nimet** vastaavat ladattuja
5. **Vahvista päätepisteen portti** vastaa palvelun tilaa

---

## Pikaopas: Mallialiaset

### Yleiset mallit

| Alias | Koko | Paras käyttö | RAM/VRAM | Variantit |
|-------|------|-------------|----------|----------|
| `phi-4-mini` | ~4B | Yleinen keskustelu, tiivistys | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Koodin generointi, refaktorointi | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Yleiset tehtävät, tehokas | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Nopea, vähäiset resurssit | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Luokittelu, minimaaliset resurssit | 1-2GB | `-cpu`, `-cuda-gpu` |

### Varianttien nimeäminen

- **Perusnimi** (esim. `phi-4-mini`): Valitsee automaattisesti parhaan variantin laitteistollesi
- **`-cpu`**: CPU-optimoitu, toimii kaikkialla
- **`-cuda-gpu`**: NVIDIA GPU optimoitu, vaatii 8GB+ VRAM
- **`-npu`**: Qualcomm NPU optimoitu, vaatii NPU-ajurit

**Suositus:** Käytä perusnimiä (ilman jälkiliitettä) ja anna Foundry Localin valita automaattisesti paras variantti.

---

## Onnistumisen merkit

Olet valmis, kun näet:

✅ `foundry service status` näyttää "running"
✅ `foundry model ls` näyttää tarvittavat mallisi
✅ Palvelu käytettävissä oikeassa päätepisteessä
✅ Terveystarkistus palauttaa 200 OK
✅ Muistikirjan diagnostiikkasolut onnistuvat
✅ Ei yhteysvirheitä tulosteessa

---

## Apua saatavilla

### Dokumentaatio
- **Päärepository:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-viite:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Vianetsintä:** Katso `troubleshooting.md` tässä hakemistossa

### GitHub-ongelmat
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Viimeksi päivitetty:** 8. lokakuuta 2025  
**Versio:** Workshop-muistikirjat 2.0

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.