# Workshop-muistikirjat - Vianmääritysopas

## Sisällysluettelo

- [Yleiset ongelmat ja ratkaisut](../../../../Workshop/notebooks)
- [Istunto 04 -kohtaiset ongelmat](../../../../Workshop/notebooks)
- [Istunto 05 -kohtaiset ongelmat](../../../../Workshop/notebooks)
- [Istunto 06 -kohtaiset ongelmat](../../../../Workshop/notebooks)
- [Laitteistokohtaiset ongelmat](../../../../Workshop/notebooks)
- [Diagnostiikkakomennot](../../../../Workshop/notebooks)
- [Apua ongelmatilanteisiin](../../../../Workshop/notebooks)

---

## Yleiset ongelmat ja ratkaisut

### 🔴 CUDA-muisti täynnä

**Virheilmoitus:**
```
CUDA failure 2: out of memory
```

**Syy:** GPU:lla ei ole tarpeeksi VRAM-muistia mallin lataamiseen.

**Ratkaisut:**

#### Vaihtoehto 1: Käytä CPU-versioita (suositeltu)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Vaihtoehto 2: Käytä pienempiä malleja GPU:lla
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Vaihtoehto 3: Tyhjennä GPU-muisti
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Vaihtoehto 4: Lisää GPU-muistia (jos mahdollista)
- Sulje selainvälilehdet, videoeditorit tai muut GPU:ta käyttävät sovellukset
- Vähennä Windowsin visuaalisia tehosteita
- Käytä erillistä GPU:ta, jos sinulla on sekä integroitu että erillinen GPU

---

### 🔴 APIConnectionError: Yhteysvirhe

**Virheilmoitus:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Syy:** Foundry Local -palvelu ei ole käynnissä tai ei ole käytettävissä.

**Ratkaisut:**

#### Vaihe 1: Tarkista palvelun tila
```bash
foundry service status
```

#### Vaihe 2: Käynnistä palvelu, jos se on pysäytetty
```bash
foundry service start
```

#### Vaihe 3: Varmista päätepiste
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Vaihe 4: Lataa tarvittavat mallit
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Vaihe 5: Käynnistä muistikirjan ydin uudelleen
Kun palvelu on käynnistetty ja mallit ladattu, käynnistä muistikirjan ydin uudelleen ja suorita kaikki solut uudelleen.

---

### 🔴 Mallia ei löydy katalogista

**Virheilmoitus:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Syy:** Mallia ei ole ladattu tai se ei ole käytettävissä Foundry Localissa.

**Ratkaisut:**

#### Vaihtoehto 1: Lataa ja lataa mallit
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

#### Vaihtoehto 2: Käytä automaattista valintatilaa
Päivitä CATALOG käyttämään perusmallien nimiä (ilman `-cpu`-päätettä):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK valitsee automaattisesti parhaan version (CPU, GPU tai NPU) laitteistosi mukaan.

---

### 🔴 HttpResponseError: 500 - Mallin lataus epäonnistui

**Virheilmoitus:**
```
HttpResponseError: 500 - Failed loading model
```

**Syy:** Mallitiedosto on vioittunut tai ei ole yhteensopiva laitteiston kanssa.

**Ratkaisut:**

#### Lataa malli uudelleen
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Käytä eri versiota
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Moduulia ei löydy

**Virheilmoitus:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Syy:** foundry-local-sdk-pakettia ei ole asennettu.

**Ratkaisut:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Hidas ensimmäinen pyyntö

**Oire:** Ensimmäinen suoritus kestää yli 30 sekuntia, seuraavat pyynnöt ovat nopeampia.

**Syy:** Tämä on normaalia - palvelu lataa mallin muistiin ensimmäisen pyynnön yhteydessä.

**Ratkaisut:**

#### Lataa mallit etukäteen
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Pidä palvelu käynnissä
```bash
# Start service manually and leave it running
foundry service start
```

---

## Istunto 04 -kohtaiset ongelmat

### Väärä porttiasetus

**Ongelma:** Muistikirja yhdistää väärään porttiin (55769 vs 59959 vs 57127)

**Ratkaisu:**

1. Tarkista, mitä porttia Foundry Local käyttää:
```bash
foundry service status
# Note the port number displayed
```

2. Päivitä solun 10 asetukset muistikirjassa:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Käynnistä ydin uudelleen ja suorita solut 6, 8, 10, 12, 16, 20, 22

---

### Väärä mallivalinta

**Ongelma:** Muistikirja näyttää gpt-oss-20b tai qwen2.5-7b mallin sijaan qwen2.5-3b

**Ratkaisu:**

1. Käynnistä muistikirjan ydin uudelleen (tyhjentää vanhat muuttujat)
2. Suorita solu 10 uudelleen (Aseta mallialiaset)
3. Suorita solu 12 uudelleen (Näytä kokoonpano)
4. **Varmista:** Solu 12 näyttää `LLM Model: qwen2.5-3b`

---

### Diagnostiikkasolu epäonnistuu

**Ongelma:** Solu 16 näyttää "❌ Foundry Local service not found!"

**Ratkaisu:**

1. Varmista, että palvelu on käynnissä:
```bash
foundry service status
```

2. Testaa päätepiste manuaalisesti:
```bash
curl http://localhost:59959/v1/models
```

3. Jos curl toimii, mutta muistikirja ei:
   - Käynnistä muistikirjan ydin uudelleen
   - Suorita solut järjestyksessä: 6, 8, 10, 12, 14, 16

4. Jos curl ei toimi:
   - Käynnistä palvelu: `foundry service start`
   - Lataa mallit: `foundry model run phi-4-mini` ja `foundry model run qwen2.5-3b`

---

### Esitarkistus epäonnistuu

**Ongelma:** Solu 20 näyttää yhteysvirheitä, vaikka diagnostiikka onnistui

**Ratkaisu:**

1. Tarkista, että mallit on ladattu:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Jos mallit puuttuvat:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Suorita solu 20 uudelleen, kun mallit on ladattu

---

### Vertailu epäonnistuu None-arvoilla

**Ongelma:** Solu 22 suoritetaan, mutta latenssi näkyy None-arvona

**Ratkaisu:**

1. Varmista, että esitarkistus onnistui ensin (solu 20)
2. Suorita solu 22 uudelleen - mallien täytyy latautua ensimmäisen pyynnön yhteydessä
3. Varmista, että molemmat mallit on ladattu: `foundry model ls`

---

## Istunto 05 -kohtaiset ongelmat

### Agentti käyttää väärää mallia

**Ongelma:** Agentti ei käytä odotettua mallia

**Ratkaisu:**

Varmista kokoonpano:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Käynnistä ydin uudelleen, jos mallit ovat väärin.

---

### Muistikontekstin ylivuoto

**Ongelma:** Agentin vastaukset heikkenevät ajan myötä

**Ratkaisu:** Tämä on jo automaattisesti käsitelty - agentit säilyttävät vain viimeiset 6 viestiä muistissa.

---

## Istunto 06 -kohtaiset ongelmat

### CPU- vs GPU-mallien sekaannus

**Ongelma:** CUDA-virheitä oletusasetuksia käytettäessä

**Ratkaisu:** Oletusasetukset käyttävät nyt CPU-malleja. Jos näet CUDA-virheitä:

1. Varmista, että käytät oletus-CPU-katalogia:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Käynnistä ydin uudelleen ja suorita kaikki solut uudelleen

---

### Aikomusten tunnistus ei toimi

**Ongelma:** Kehotukset ohjautuvat väärille malleille

**Ratkaisu:**

Testaa aikomusten tunnistus:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Päivitä RULES, jos kaavat tarvitsevat säätöä.

---

## Laitteistokohtaiset ongelmat

### NVIDIA GPU

**Tarkista GPU:n tila:**
```bash
nvidia-smi
```

**Yleiset ongelmat:**
- **Ajuri vanhentunut**: Päivitä NVIDIA-ajurit
- **CUDA-versio ei täsmää**: Asenna Foundry Local uudelleen
- **GPU-muisti pirstoutunut**: Käynnistä järjestelmä uudelleen

### Qualcomm NPU

**Tarkista NPU:n tila:**
```bash
foundry device info
```

**Yleiset ongelmat:**
- **NPU-ajurit eivät ole asennettu**: Asenna Qualcomm NPU -ajurit
- **NPU-versio ei ole saatavilla**: Käytä CPU-versiota
- **Windows-versio liian vanha**: Päivitä uusimpaan Windows 11 -versioon

### Vain CPU-järjestelmät

**Suositellut mallit:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Suorituskykyvinkit:**
- Käytä pienimpiä malleja
- Vähennä max_tokens-arvoa
- Varaudu ensimmäisen pyynnön hitauteen

---

## Diagnostiikkakomennot

### Tarkista kaikki
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

### Pythonissa
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

## Apua ongelmatilanteisiin

### 1. Tarkista lokit
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub-ongelmat
- Etsi olemassa olevia ongelmia: https://github.com/microsoft/Foundry-Local/issues
- Luo uusi ongelma seuraavilla tiedoilla:
  - Virheilmoitus (koko teksti)
  - `foundry service status` -komennon tulos
  - `foundry --version` -komennon tulos
  - GPU/NPU-tiedot (nvidia-smi, jne.)
  - Toistettavat vaiheet

### 3. Dokumentaatio
- **Pääsivusto**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI-viite**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Vianmääritys**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Pikakorjausten tarkistuslista

Kun ongelmia ilmenee, kokeile näitä järjestyksessä:

- [ ] Tarkista, että palvelu on käynnissä: `foundry service status`
- [ ] Käynnistä palvelu uudelleen: `foundry service stop && foundry service start`
- [ ] Varmista, että malli on olemassa: `foundry model ls | grep phi-4-mini`
- [ ] Lataa tarvittavat mallit: `foundry model run phi-4-mini`
- [ ] Tarkista GPU-muisti: `nvidia-smi` (jos NVIDIA)
- [ ] Kokeile CPU-versiota: Käytä `phi-4-mini-cpu` mallia `phi-4-mini` sijaan
- [ ] Käynnistä muistikirjan ydin uudelleen
- [ ] Tyhjennä muistikirjan tulosteet ja suorita kaikki solut uudelleen
- [ ] Asenna SDK uudelleen: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Käynnistä järjestelmä uudelleen (viimeinen keino)

---

## Ennaltaehkäisyvinkit

### Parhaat käytännöt

1. **Tarkista aina ensin palvelu:**
   ```bash
   foundry service status
   ```

2. **Käytä oletuksena CPU-versioita:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Lataa mallit etukäteen ennen muistikirjojen suorittamista:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Pidä palvelu käynnissä:**
   - Älä pysäytä/käynnistä palvelua tarpeettomasti
   - Anna sen pyöriä taustalla istuntojen välillä

5. **Seuraa resursseja:**
   - Tarkista GPU-muisti ennen suorittamista
   - Sulje tarpeettomat GPU-sovellukset
   - Käytä Tehtävienhallintaa / nvidia-smi

6. **Päivitä säännöllisesti:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Viimeksi päivitetty:** 8. lokakuuta 2025

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.