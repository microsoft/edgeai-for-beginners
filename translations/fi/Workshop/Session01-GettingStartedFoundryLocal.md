<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T23:26:09+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "fi"
}
-->
# Istunto 1: Aloitus Foundry Localin kanssa

## Tiivistelmä

Opi asentamaan, konfiguroimaan ja suorittamaan ensimmäiset tekoälymallisi Microsoft Foundry Localin avulla. Tämä käytännönläheinen istunto tarjoaa vaiheittaisen johdannon paikalliseen inferenssiin, alkaen asennuksesta aina ensimmäisen chat-sovelluksen rakentamiseen käyttäen malleja kuten Phi-4, Qwen ja DeepSeek.

## Oppimistavoitteet

Istunnon lopussa osaat:

- **Asentaa ja konfiguroida**: Määrittää Foundry Localin ja varmistaa asennuksen onnistuminen
- **Hallita CLI-toimintoja**: Käyttää Foundry Localin komentorivikäyttöliittymää mallien hallintaan ja käyttöönottoon
- **Suorittaa ensimmäisen mallisi**: Ottaa käyttöön ja käyttää paikallista tekoälymallia
- **Rakentaa chat-sovelluksen**: Luoda yksinkertaisen chat-sovelluksen Foundry Local Python SDK:n avulla
- **Ymmärtää paikallista tekoälyä**: Sisäistää paikallisen inferenssin ja mallien hallinnan perusteet

## Esivaatimukset

### Järjestelmävaatimukset

- **Windows**: Windows 11 (22H2 tai uudempi) TAI **macOS**: macOS 11+ (rajoitettu tuki)
- **RAM**: Vähintään 8GB, suositus 16GB+
- **Tallennustila**: Vähintään 10GB vapaata tilaa malleille
- **Python**: Asennettuna versio 3.10 tai uudempi
- **Ylläpitäjän oikeudet**: Asennusta varten

### Kehitysympäristö

- Visual Studio Code Python-laajennuksella (suositeltu)
- Pääsy komentoriville (PowerShell Windowsissa, Terminal macOS:ssä)
- Git repositorioiden kloonaamiseen (valinnainen)

## Työpajan kulku (30 minuuttia)

### Vaihe 1: Asenna Foundry Local (5 minuuttia)

#### Windows-asennus

Asenna Foundry Local Windowsin pakettienhallinnan avulla:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Vaihtoehto: Lataa suoraan [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### macOS-asennus (rajoitettu tuki)

> [!NOTE] 
> macOS-tuki on tällä hetkellä esikatselussa. Tarkista virallinen dokumentaatio uusimmasta saatavuudesta.

Jos saatavilla, asenna Homebrewin avulla:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Vaihtoehto macOS-käyttäjille:**
- Käytä Windows 11 VM:ää (Parallels/UTM) ja seuraa Windows-ohjeita
- Suorita kontissa, jos saatavilla, ja konfiguroi `FOUNDRY_LOCAL_ENDPOINT`

### Vaihe 2: Vahvista asennus (3 minuuttia)

Asennuksen jälkeen käynnistä komentorivi uudelleen ja varmista, että Foundry Local toimii:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Odotettu tulos näyttää version tiedot ja käytettävissä olevat komennot.

### Vaihe 3: Määritä Python-ympäristö (5 minuuttia)

Luo omistettu Python-ympäristö tätä työpajaa varten:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Vaihe 4: Suorita ensimmäinen mallisi (7 minuuttia)

Nyt suoritetaan ensimmäinen tekoälymalli paikallisesti!

#### Aloita Phi-4 Mini -mallilla (suositeltu aloitusmalli)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Tämä komento lataa mallin (ensimmäisellä kerralla) ja käynnistää Foundry Local -palvelun automaattisesti.

#### Tarkista käynnissä olevat palvelut

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Kokeile muita malleja

Kun phi-4-mini toimii, kokeile muita malleja:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Vaihe 5: Rakenna ensimmäinen chat-sovelluksesi (10 minuuttia)

Nyt luodaan Python-sovellus, joka käyttää juuri käynnistettyjä malleja.

#### Luo chat-skripti

Luo uusi tiedosto nimeltä `my_first_chat.py` (tai käytä annettua esimerkkiä):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Liittyvät esimerkit**: Edistyneempään käyttöön katso:
>
> - **Python-esimerkki**: `Workshop/samples/session01/chat_bootstrap.py` - Sisältää suoratoistovastaukset ja virheenkäsittelyn
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiivinen versio yksityiskohtaisilla selityksillä

#### Testaa chat-sovelluksesi

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Vaihtoehto: Käytä suoraan annettuja esimerkkejä

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Tai tutki interaktiivista notebookia
Avaa Workshop/notebooks/session01_chat_bootstrap.ipynb VS Codessa

Kokeile näitä esimerkkikeskusteluja:

- "Mikä on Microsoft Foundry Local?"
- "Listaa 3 hyötyä tekoälymallien paikallisesta käytöstä"
- "Auttaako minua ymmärtämään edge AI:ta"

## Mitä olet saavuttanut

Onnittelut! Olet onnistuneesti:

1. ✅ **Asentanut Foundry Localin** ja varmistanut sen toimivuuden
2. ✅ **Käynnistänyt ensimmäisen tekoälymallisi** (phi-4-mini) paikallisesti
3. ✅ **Testannut eri malleja** komentorivillä
4. ✅ **Rakentanut chat-sovelluksen**, joka yhdistyy paikalliseen tekoälyyn
5. ✅ **Kokenut paikallisen tekoälyn inferenssin** ilman pilvipalveluriippuvuutta

## Ymmärrä, mitä tapahtui

### Paikallinen tekoälyn inferenssi

- Tekoälymallisi toimii täysin omalla tietokoneellasi
- Dataa ei lähetetä pilveen
- Vastaukset luodaan paikallisesti CPU/GPU:ta käyttäen
- Yksityisyys ja tietoturva säilyvät

### Mallien hallinta

- `foundry model run` lataa ja käynnistää malleja
- **FoundryLocalManager SDK** käynnistää palvelun ja lataa mallin automaattisesti
- Mallit tallennetaan paikallisesti tulevaa käyttöä varten
- Useita malleja voidaan ladata, mutta yleensä yksi toimii kerrallaan
- Palvelu hallitsee mallien elinkaaren automaattisesti

### SDK vs CLI -lähestymistavat

- **CLI-lähestymistapa**: Mallien manuaalinen hallinta komennolla `foundry model run <malli>`
- **SDK-lähestymistapa**: Automaattinen palvelu- ja mallinhallinta `FoundryLocalManager(alias)` avulla
- **Suositus**: Käytä SDK:ta sovelluksiin, CLI:tä testaukseen ja tutkimiseen

## Yleisimpien komentojen viite

### Keskeiset CLI-komennot

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Mallisuositukset

- **phi-4-mini**: Paras aloitusmalli - nopea, kevyt, hyvä laatu
- **qwen2.5-0.5b**: Nopein inferenssi, vähäinen muistin käyttö
- **gpt-oss-20b**: Korkealaatuiset vastaukset, vaatii enemmän resursseja
- **deepseek-coder-1.3b**: Optimoitu ohjelmointi- ja kooditehtäviin

## Vianetsintä

### "Foundry-komentoa ei löydy"

**Ratkaisu:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Mallin lataus epäonnistui"

**Ratkaisu:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Yhteys localhostiin hylätty"

**Ratkaisu:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Seuraavat askeleet

### Välittömät toimenpiteet

1. **Kokeile** eri malleja ja kysymyksiä
2. **Muokkaa** chat-sovellustasi kokeillaksesi eri malleja
3. **Luo** omia kysymyksiä ja testaa vastauksia
4. **Tutki** Istunto 2: RAG-sovellusten rakentaminen

### Edistynyt oppimispolku

1. **Istunto 2**: Rakenna tekoälyratkaisuja RAG:lla (Retrieval-Augmented Generation)
2. **Istunto 3**: Vertaa eri avoimen lähdekoodin malleja
3. **Istunto 4**: Työskentele huippumallien kanssa
4. **Istunto 5**: Rakenna monen agentin tekoälyjärjestelmiä

## Ympäristömuuttujat (valinnainen)

Edistyneempää käyttöä varten voit asettaa nämä ympäristömuuttujat:

| Muuttuja | Tarkoitus | Esimerkki |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Oletusmalli käytettäväksi | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Ylikirjoita päätepisteen URL | `http://localhost:5273/v1` |

Luo `.env`-tiedosto projektikansioosi:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Lisäresurssit

### Dokumentaatio

- [Foundry Local Python SDK -viite](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local -asennusopas](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Mallikatalogi](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Esimerkkikoodi

- **Session01 Python-esimerkki**: `Workshop/samples/session01/chat_bootstrap.py` - Täydellinen chat-sovellus suoratoistolla
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktiivinen opas  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK -integraatio
- [Module08 Sample 03](../Module08/samples/03/README.md) - Mallien löytäminen ja vertailu

### Yhteisö

- [Foundry Local GitHub -keskustelut](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI -yhteisö](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Istunnon kesto**: 30 minuuttia käytännön harjoittelua + 15 minuuttia kysymyksiä ja vastauksia  
**Vaikeustaso**: Aloittelija  
**Esivaatimukset**: Windows 11/macOS 11+, Python 3.10+, ylläpitäjän oikeudet

## Työpajan esimerkkitilanne

### Todellinen konteksti

**Tilanne**: Yrityksen IT-tiimi haluaa arvioida laitteessa tapahtuvaa tekoälyn inferenssiä käsitelläkseen arkaluontoista työntekijäpalautetta ilman datan lähettämistä ulkoisiin palveluihin.

**Tavoitteesi**: Todista, että paikalliset tekoälymallit voivat tuottaa laadukkaita vastauksia alle sekunnin viiveellä samalla, kun tietosuoja säilyy täysin.

### Testikysymykset

Käytä näitä kysymyksiä varmistaaksesi asetuksesi:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Onnistumisen kriteerit

- ✅ Kaikki kysymykset saavat vastaukset alle 2 sekunnissa
- ✅ Data ei poistu paikalliselta koneeltasi
- ✅ Vastaukset ovat osuvia ja hyödyllisiä
- ✅ Chat-sovelluksesi toimii sujuvasti

Tämä validointi varmistaa, että Foundry Local -asennuksesi on valmis edistyneempiin työpajoihin istunnoissa 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa ensisijaiseksi lähteeksi. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->