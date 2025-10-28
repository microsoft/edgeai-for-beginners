<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:22:36+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "fi"
}
-->
# Istunto 1: Aloitetaan Foundry Localin kanssa

## Tiivistelmä

Aloita matkasi Foundry Localin parissa asentamalla ja konfiguroimalla se Windows 11:ssä. Opettele CLI:n käyttöönotto, laitteistokiihdytyksen aktivointi ja mallien välimuistiin tallentaminen nopeaa paikallista päättelyä varten. Tämä käytännön istunto opastaa mallien, kuten Phi, Qwen, DeepSeek ja GPT-OSS-20B, suorittamisessa toistettavilla CLI-komentoilla.

## Oppimistavoitteet

Istunnon lopussa osaat:

- **Asentaa ja konfiguroida**: Ottaa Foundry Localin käyttöön Windows 11:ssä optimaalisilla suoritusasetuksilla
- **Hallita CLI-toimintoja**: Käyttää Foundry Local CLI:tä mallien hallintaan ja käyttöönottoon
- **Aktivoida laitteistokiihdytyksen**: Konfiguroida GPU-kiihdytys ONNXRuntime- tai WebGPU-tekniikalla
- **Käyttää useita malleja**: Suorittaa phi-4, GPT-OSS-20B, Qwen ja DeepSeek -malleja paikallisesti
- **Rakentaa ensimmäisen sovelluksesi**: Mukauttaa olemassa olevia esimerkkejä Foundry Local Python SDK:n käyttöön

# Testaa mallia (ei-interaktiivinen yksittäinen kehotus)
foundry model run phi-4-mini --prompt "Hei, esittäydy"

- Windows 11 (22H2 tai uudempi)
# Listaa saatavilla olevat katalogimallit (ladatut mallit näkyvät suorittamisen jälkeen)
foundry model list
## NOTE: Tällä hetkellä ei ole erillistä `--running`-lippua; ladattujen mallien näkemiseksi aloita keskustelu tai tarkista palvelulokit.
- Python 3.10+ asennettuna
- Visual Studio Code Python-laajennuksella
- Järjestelmänvalvojan oikeudet asennusta varten

### (Valinnainen) Ympäristömuuttujat

Luo `.env` (tai aseta shellissä) skriptien siirrettävyyden parantamiseksi:
# Vertaa vastauksia (ei-interaktiivinen)
foundry model run gpt-oss-20b --prompt "Selitä edge AI yksinkertaisesti"
| Muuttuja | Tarkoitus | Esimerkki |
|----------|-----------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | Suosittu mallialias (katalogi valitsee automaattisesti parhaan variantin) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ohita oletuspalvelin (muuten automaattinen managerista) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Aktivoi suoratoistodemo | `true` |

> Jos `FOUNDRY_LOCAL_ENDPOINT=auto` (tai ei asetettu), se johdetaan SDK-managerista.

## Demo Flow (30 minuuttia)

### 1. Asenna Foundry Local ja varmista CLI-asennus (10 minuuttia)

# Listaa välimuistiin tallennetut mallit
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Esikatselu / Jos tuettu)**

Jos natiivi macOS-paketti on saatavilla (tarkista viralliset dokumentit uusimmasta versiosta):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Jos macOS-natiivit binäärit eivät ole vielä saatavilla, voit silti: 
1. Käyttää Windows 11 ARM/Intel VM:ää (Parallels / UTM) ja seurata Windows-ohjeita. 
2. Suorittaa malleja kontissa (jos konttikuva julkaistu) ja asettaa `FOUNDRY_LOCAL_ENDPOINT` altistettuun porttiin. 

**Luo Python-virtuaaliympäristö (Ristiin‑alustainen)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Päivitä pip ja asenna ydinkirjastot:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Vaihe 1.2: Varmista asennus

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Vaihe 1.3: Konfiguroi ympäristö

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK:n käynnistäminen (suositeltu)

Sen sijaan, että käynnistäisit palvelun ja suorittaisit malleja manuaalisesti, **Foundry Local Python SDK** voi käynnistää kaiken automaattisesti:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Jos haluat tarkempaa hallintaa, voit silti käyttää CLI:tä + OpenAI-asiakasta myöhemmin näytetyllä tavalla.

### 2. Suorita malleja paikallisesti CLI:n kautta (10 minuuttia)

#### Vaihe 3.1: Ota Phi-4-malli käyttöön

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Vaihe 3.2: Ota GPT-OSS-20B käyttöön

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Vaihe 3.3: Lataa lisämalleja

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Aloitusprojekti: Mukauta 01-run-phi Foundry Localille (5 minuuttia)

#### Vaihe 4.1: Luo yksinkertainen keskustelusovellus

Luo `samples/01-foundry-quickstart/chat_quickstart.py` (päivitetty käyttämään manageria, jos saatavilla):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Vaihe 4.2: Testaa sovellus

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Keskeiset käsitteet

### 1. Foundry Local -arkkitehtuuri

- **Paikallinen päättelymoottori**: Suorittaa mallit kokonaan laitteellasi
- **OpenAI SDK -yhteensopivuus**: Saumaton integrointi olemassa olevaan OpenAI-koodiin
- **Mallien hallinta**: Lataa, tallenna välimuistiin ja suorita useita malleja tehokkaasti
- **Laitteiston optimointi**: Hyödynnä GPU-, NPU- ja CPU-kiihdytystä

### 2. CLI-komentoviite

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK -integraatio

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Yleisimpien ongelmien ratkaisu

### Ongelma 1: "Foundry-komentoa ei löydy"

**Ratkaisu:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Ongelma 2: "Mallin lataus epäonnistui"

**Ratkaisu:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Ongelma 3: "Yhteys hylätty osoitteessa localhost:5273"

**Ratkaisu:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Suorituskyvyn optimointivinkit

### 1. Mallin valintastrategia

- **Phi-4-mini**: Paras yleisiin tehtäviin, pienempi muistinkulutus
- **Qwen2.5-0.5b**: Nopein päättely, vähäiset resurssivaatimukset
- **GPT-OSS-20B**: Korkein laatu, vaatii enemmän resursseja
- **DeepSeek-Coder**: Optimoitu ohjelmointitehtäviin

### 2. Laitteiston optimointi

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Suorituskyvyn seuranta

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Valinnaiset parannukset

| Parannus | Mitä | Kuinka |
|----------|------|-------|
| Jaetut apuohjelmat | Poista päällekkäinen asiakas-/käynnistyslogiikka | Käytä `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Tokenien käytön näkyvyys | Opeta kustannus-/tehokkuusajattelua aikaisin | Aseta `SHOW_USAGE=1` tulostamaan kehotus/vastaus/kokonais-tokenit |
| Deterministiset vertailut | Vakaa vertailu ja regressiotestit | Käytä `temperature=0`, `top_p=1`, johdonmukaista kehotustekstiä |
| Ensimmäisen tokenin viive | Koettu reagointinopeus | Mukauta vertailuskripti suoratoistolla (`BENCH_STREAM=1`) |
| Uudelleenyritä tilapäisissä virheissä | Kestävä demotus kylmäkäynnistyksessä | `RETRY_ON_FAIL=1` (oletus) ja säädä `RETRY_BACKOFF` |
| Savutestaus | Nopea tarkistus keskeisille toiminnoille | Suorita `python Workshop/tests/smoke.py` ennen työpajaa |
| Mallialiasprofiilit | Vaihda nopeasti malliasetusta koneiden välillä | Ylläpidä `.env` tiedostoa `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Välimuistin tehokkuus | Vältä toistuvia lämmityksiä moninäyteajossa | Apuohjelmat välimuistinhallintaan; käytä uudelleen skripteissä/muistikirjoissa |
| Ensimmäisen ajon lämmitys | Vähennä p95 viivepiikkejä | Suorita pieni kehotus `FoundryLocalManager`-luonnin jälkeen |

Esimerkki deterministisestä lämpimästä perustasosta (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Sinun pitäisi nähdä samanlainen tulos ja identtiset tokenimäärät toisella ajokerralla, mikä vahvistaa determinismin.

## Seuraavat askeleet

Kun olet suorittanut tämän istunnon:

1. **Tutustu istuntoon 2**: Rakenna tekoälyratkaisuja Azure AI Foundry RAG:lla
2. **Kokeile eri malleja**: Testaa Qwen-, DeepSeek- ja muita malliperheitä
3. **Optimoi suorituskyky**: Hienosäädä asetuksia laitteistosi mukaan
4. **Rakenna omia sovelluksia**: Käytä Foundry Local SDK:ta omissa projekteissasi

## Lisäresurssit

### Dokumentaatio
- [Foundry Local Python SDK -viite](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local asennusopas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Mallikatalogi](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Esimerkkikoodi
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK -integraatio
- [Module08 Sample 03](./samples/03/README.md) - Mallien löytäminen ja vertailu

### Yhteisö
- [Foundry Local GitHub-keskustelut](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI -yhteisö](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Istunnon kesto**: 30 minuuttia käytännön harjoittelua + 15 minuuttia kysymyksiä ja vastauksia
**Vaikeustaso**: Aloittelija
**Esivaatimukset**: Windows 11, Python 3.10+, Järjestelmänvalvojan oikeudet

## Esimerkkiskenaario ja työpajan kartoitus

| Työpajaskripti / Muistikirja | Skenaario | Tavoite | Esimerkkisyöte(t) | Tarvittava datasetti |
|-----------------------------|-----------|---------|-------------------|----------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Sisäinen IT-tiimi arvioi laitteistopohjaista päättelyä yksityisyyden arviointialustalle | Todista, että paikallinen SLM vastaa alle sekunnin viiveellä standardikehotuksiin | "Listaa kaksi hyötyä paikallisesta päättelystä." | Ei mitään (yksittäinen kehotus) |
| Quickstart-mukautuskoodilohko | Kehittäjä siirtää olemassa olevan OpenAI-skriptin Foundry Localiin | Näytä yhteensopivuus | "Anna kaksi hyötyä paikallisesta päättelystä." | Vain sisäinen kehotus |

### Skenaarion kuvaus
Turvallisuus- ja vaatimustenmukaisuustiimin on varmistettava, että arkaluontoista prototyyppidataa voidaan käsitellä paikallisesti. He suorittavat käynnistysskriptin useilla kehotuksilla (yksityisyys, viive, kustannukset) käyttäen determinististä temperature=0-tilaa tallentaakseen perustason tulokset myöhempää vertailua varten (istunto 3 vertailu ja istunto 4 SLM vs LLM -kontrasti).

### Vähimmäiskehotusjoukon JSON (valinnainen)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Käytä tätä listaa luodaksesi toistettavan arviointisilmukan tai siementääksesi tulevan regressiotestauksen.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.