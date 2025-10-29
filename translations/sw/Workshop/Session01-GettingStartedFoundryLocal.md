<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T22:50:00+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "sw"
}
-->
# Kipindi cha 1: Kuanza na Foundry Local

## Muhtasari

Anza safari yako na Foundry Local kwa kuisakinisha na kuisanidi kwenye Windows 11. Jifunze jinsi ya kusanidi CLI, kuwezesha kasi ya vifaa, na kuhifadhi modeli kwa ajili ya utabiri wa haraka wa ndani. Kipindi hiki cha vitendo kinaelezea jinsi ya kuendesha modeli kama Phi, Qwen, DeepSeek, na GPT-OSS-20B kwa kutumia amri za CLI zinazoweza kurudiwa.

## Malengo ya Kujifunza

Mwisho wa kipindi hiki, utaweza:

- **Kusakinisha na Kusanidi**: Kuweka Foundry Local kwenye Windows 11 na mipangilio bora ya utendaji
- **Kumiliki Operesheni za CLI**: Kutumia Foundry Local CLI kwa usimamizi wa modeli na utekelezaji
- **Kuwezesha Kasi ya Vifaa**: Kusanidi kasi ya GPU kwa ONNXRuntime au WebGPU
- **Kutekeleza Modeli Nyingi**: Kuendesha modeli phi-4, GPT-OSS-20B, Qwen, na DeepSeek ndani ya kifaa
- **Kujenga Programu Yako ya Kwanza**: Kubadilisha sampuli zilizopo kutumia Foundry Local Python SDK

# Jaribu modeli (swali moja bila mwingiliano)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

- Windows 11 (22H2 au zaidi)
# Orodhesha modeli za katalogi zinazopatikana (modeli zilizopakuliwa zinaonekana baada ya kuendeshwa)
foundry model list
## NOTE: Kwa sasa hakuna bendera maalum ya `--running`; ili kuona ni zipi zimepakuliwa, anzisha mazungumzo au angalia kumbukumbu za huduma.
- Python 3.10+ imesakinishwa
- Visual Studio Code na kiendelezi cha Python
- Haki za msimamizi kwa usakinishaji

### (Hiari) Vigezo vya Mazingira

Unda `.env` (au weka kwenye shell) ili kufanya maandishi yaweze kuhamishika:
# Linganisha majibu (bila mwingiliano)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
| Kigezo | Kusudi | Mfano |
|--------|--------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Jina la modeli unalopendelea (katalogi huchagua toleo bora kiotomatiki) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Badilisha endpoint (vinginevyo hutolewa kiotomatiki kutoka kwa meneja) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Washa onyesho la utiririshaji | `true` |

> Ikiwa `FOUNDRY_LOCAL_ENDPOINT=auto` (au haijawekwa) tunaitoa kutoka kwa meneja wa SDK.

## Mtiririko wa Onyesho (Dakika 30)

### 1. Sakinisha Foundry Local na Thibitisha Usanidi wa CLI (Dakika 10)

# Orodhesha modeli zilizohifadhiwa
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Muonekano wa Awali / Ikiwa Inasaidiwa)**

Ikiwa kifurushi cha asili cha macOS kinapatikana (angalia nyaraka rasmi kwa za hivi karibuni):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Ikiwa binaries za asili za macOS bado hazipatikani, bado unaweza: 
1. Tumia Windows 11 ARM/Intel VM (Parallels / UTM) na fuata hatua za Windows. 
2. Endesha modeli kupitia kontena (ikiwa picha ya kontena imechapishwa) na weka `FOUNDRY_LOCAL_ENDPOINT` kwa bandari iliyofunguliwa. 

**Unda Mazingira ya Virtual ya Python (Kote‑Platform)**

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

Boresha pip na usakinishe utegemezi wa msingi:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Hatua ya 1.2: Thibitisha Usakinishaji

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Hatua ya 1.3: Sanidi Mazingira

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK Bootstrapping (Inapendekezwa)

Badala ya kuanzisha huduma na kuendesha modeli kwa mikono, **Foundry Local Python SDK** inaweza kuanzisha kila kitu:

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

Ikiwa unapendelea udhibiti wa moja kwa moja bado unaweza kutumia CLI + mteja wa OpenAI kama inavyoonyeshwa baadaye.

### 2. Endesha Modeli Ndani ya Kifaa Kupitia CLI (Dakika 10)

#### Hatua ya 3.1: Tekeleza Modeli ya Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Hatua ya 3.2: Tekeleza GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Hatua ya 3.3: Pakia Modeli Zingine

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Mradi wa Kuanza: Badilisha 01-run-phi kwa Foundry Local (Dakika 5)

#### Hatua ya 4.1: Unda Programu ya Msingi ya Mazungumzo

Unda `samples/01-foundry-quickstart/chat_quickstart.py` (imeboreshwa kutumia meneja ikiwa inapatikana):

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

#### Hatua ya 4.2: Jaribu Programu

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Dhana Muhimu Zilizofunikwa

### 1. Muundo wa Foundry Local

- **Injini ya Utabiri ya Ndani**: Inaendesha modeli kikamilifu kwenye kifaa chako
- **Ulinganifu wa SDK ya OpenAI**: Muunganisho rahisi na msimbo wa OpenAI uliopo
- **Usimamizi wa Modeli**: Pakua, hifadhi, na endesha modeli nyingi kwa ufanisi
- **Uboreshaji wa Vifaa**: Tumia kasi ya GPU, NPU, na CPU

### 2. Marejeleo ya Amri za CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Ujumuishaji wa Python SDK

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

## Kutatua Masuala ya Kawaida

### Tatizo 1: "Amri ya Foundry haijapatikana"

**Suluhisho:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Tatizo 2: "Modeli imeshindwa kupakia"

**Suluhisho:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Tatizo 3: "Muunganisho umekataliwa kwenye localhost:5273"

**Suluhisho:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Vidokezo vya Uboreshaji wa Utendaji

### 1. Mkakati wa Uchaguzi wa Modeli

- **Phi-4-mini**: Bora kwa kazi za jumla, matumizi ya kumbukumbu ya chini
- **Qwen2.5-0.5b**: Utabiri wa haraka, rasilimali ndogo
- **GPT-OSS-20B**: Ubora wa juu zaidi, unahitaji rasilimali zaidi
- **DeepSeek-Coder**: Imeboreshwa kwa kazi za programu

### 2. Uboreshaji wa Vifaa

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Ufuatiliaji wa Utendaji

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Uboreshaji wa Hiari

| Uboreshaji | Nini | Jinsi |
|------------|------|------|
| Huduma za Pamoja | Ondoa mantiki ya mteja/kuanzisha mara kwa mara | Tumia `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Uonekano wa Matumizi ya Tokeni | Fundisha kufikiria gharama/ufanisi mapema | Weka `SHOW_USAGE=1` ili kuchapisha tokeni za prompt/completion/total |
| Ulinganisho wa Kiamua | Kuweka alama thabiti & ukaguzi wa regression | Tumia `temperature=0`, `top_p=1`, maandishi thabiti ya prompt |
| Latency ya Tokeni ya Kwanza | Kipimo cha mwitikio kinachoonekana | Badilisha script ya benchmark na utiririshaji (`BENCH_STREAM=1`) |
| Jaribu tena kwa Makosa ya Muda | Onyesho lenye nguvu kwenye mwanzo baridi | `RETRY_ON_FAIL=1` (chaguo-msingi) & rekebisha `RETRY_BACKOFF` |
| Upimaji wa Moshi | Ukaguzi wa haraka kwenye mtiririko muhimu | Endesha `python Workshop/tests/smoke.py` kabla ya warsha |
| Profaili za Jina la Modeli | Badilisha seti ya modeli haraka kati ya mashine | Hifadhi `.env` na `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Ufanisi wa Kuhifadhi | Epuka kuanza upya mara kwa mara katika uendeshaji wa sampuli nyingi | Wasimamizi wa hifadhi ya matumizi; tumia tena kwenye maandishi/daftari |
| Kuwasha Mara ya Kwanza | Punguza milipuko ya latency ya p95 | Toa prompt ndogo baada ya kuundwa kwa `FoundryLocalManager` |

Mfano wa msingi wa joto thabiti (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Unapaswa kuona matokeo yanayofanana & hesabu ya tokeni sawa kwenye uendeshaji wa pili, ikithibitisha uamuzi.

## Hatua Zifuatazo

Baada ya kukamilisha kipindi hiki:

1. **Gundua Kipindi cha 2**: Jenga suluhisho za AI na Azure AI Foundry RAG
2. **Jaribu Modeli Tofauti**: Fanya majaribio na Qwen, DeepSeek, na familia nyingine za modeli
3. **Boresha Utendaji**: Rekebisha mipangilio kwa vifaa vyako maalum
4. **Jenga Programu za Kibinafsi**: Tumia Foundry Local SDK katika miradi yako mwenyewe

## Rasilimali za Ziada

### Nyaraka
- [Marejeleo ya Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Mwongozo wa Usakinishaji wa Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Katalogi ya Modeli](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Msimbo wa Sampuli
- [Mfano wa Moduli08 01](./samples/01/README.md) - Mwongozo wa Haraka wa REST Chat
- [Mfano wa Moduli08 02](./samples/02/README.md) - Ujumuishaji wa SDK ya OpenAI
- [Mfano wa Moduli08 03](./samples/03/README.md) - Ugunduzi wa Modeli & Uwekaji Alama

### Jamii
- [Majadiliano ya Foundry Local GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Jamii ya Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Muda wa Kipindi**: Dakika 30 za vitendo + Dakika 15 za Maswali na Majibu  
**Kiwango cha Ugumu**: Mwanzoni  
**Mahitaji ya Awali**: Windows 11, Python 3.10+, Haki za Msimamizi  

## Hali ya Mfano & Ulinganisho wa Warsha

| Maandishi ya Warsha / Daftari | Hali | Lengo | Mfano wa Ingizo | Dataset Inayohitajika |
|------------------------------|------|-------|-----------------|-----------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Timu ya IT ya ndani inatathmini utabiri wa ndani kwa portal ya tathmini ya faragha | Thibitisha SLM ya ndani inajibu ndani ya latency ya sekunde ndogo kwa maswali ya kawaida | "Taja faida mbili za utabiri wa ndani." | Hakuna (swali moja) |
| Msimbo wa marekebisho ya mwongozo wa haraka | Mendelezaji anayehama kutoka script ya OpenAI kwenda Foundry Local | Onyesha ulinganifu wa moja kwa moja | "Taja faida mbili za utabiri wa ndani." | Prompt ya ndani tu |

### Maelezo ya Hali
Kikosi cha usalama & ufuatiliaji kinapaswa kuthibitisha ikiwa data nyeti ya mfano inaweza kuchakatwa ndani ya kifaa. Wanakimbia script ya bootstrap na maswali kadhaa (faragha, latency, gharama) wakitumia hali ya uamuzi ya temperature=0 ili kukamata matokeo ya msingi kwa kulinganisha baadaye (Uwekaji alama wa Kipindi cha 3 na Ulinganisho wa SLM vs LLM wa Kipindi cha 4).

### Seti ya Prompt Ndogo ya JSON (hiari)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Tumia orodha hii kuunda mzunguko wa tathmini unaoweza kurudiwa au kuanzisha mfumo wa ukaguzi wa regression wa baadaye.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.