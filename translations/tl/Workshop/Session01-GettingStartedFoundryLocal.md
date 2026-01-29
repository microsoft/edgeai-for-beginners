# Session 1: Pagsisimula sa Foundry Local

## Abstrak

Matutunan kung paano mag-install, mag-configure, at magpatakbo ng iyong unang AI models gamit ang Microsoft Foundry Local. Ang hands-on session na ito ay nagbibigay ng step-by-step na introduksyon sa lokal na inference, mula sa pag-install hanggang sa paggawa ng iyong unang chat application gamit ang mga model tulad ng Phi-4, Qwen, at DeepSeek.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng session na ito, magagawa mo ang sumusunod:

- **Mag-Install at Mag-Configure**: I-set up ang Foundry Local na may tamang pag-verify ng installation
- **Master CLI Operations**: Gumamit ng Foundry Local CLI para sa pamamahala at pag-deploy ng mga model
- **Patakbuhin ang Iyong Unang Model**: Magtagumpay sa pag-deploy at pakikipag-ugnayan sa isang lokal na AI model
- **Gumawa ng Chat App**: Lumikha ng basic na chat application gamit ang Foundry Local Python SDK
- **Unawain ang Lokal na AI**: Maunawaan ang mga pangunahing kaalaman sa lokal na inference at pamamahala ng model

## Mga Kinakailangan

### Mga Kinakailangan sa Sistema

- **Windows**: Windows 11 (22H2 o mas bago) O **macOS**: macOS 11+ (limitadong suporta)
- **RAM**: Minimum na 8GB, inirerekomenda ang 16GB+
- **Storage**: 10GB+ na libreng espasyo para sa mga model
- **Python**: 3.10 o mas bago na naka-install
- **Admin Access**: Pribilehiyo ng administrator para sa pag-install

### Kapaligiran ng Pag-develop

- Visual Studio Code na may Python extension (inirerekomenda)
- Access sa command line (PowerShell sa Windows, Terminal sa macOS)
- Git para sa pag-clone ng mga repository (opsyonal)

## Daloy ng Workshop (30 minuto)

### Hakbang 1: I-install ang Foundry Local (5 minuto)

#### Pag-install sa Windows

I-install ang Foundry Local gamit ang Windows package manager:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatibo: I-download nang direkta mula sa [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Pag-install sa macOS (Limitadong Suporta)

> [!NOTE] 
> Ang suporta sa macOS ay kasalukuyang nasa preview. Tingnan ang opisyal na dokumentasyon para sa pinakabagong availability.

Kung available, i-install gamit ang Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatibo para sa mga gumagamit ng macOS:**
- Gumamit ng Windows 11 VM (Parallels/UTM) at sundin ang mga hakbang sa Windows
- Patakbuhin gamit ang container kung available at i-configure ang `FOUNDRY_LOCAL_ENDPOINT`

### Hakbang 2: I-verify ang Pag-install (3 minuto)

Pagkatapos ng pag-install, i-restart ang iyong terminal at i-verify na gumagana ang Foundry Local:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Ang inaasahang output ay dapat magpakita ng impormasyon ng bersyon at mga available na command.

### Hakbang 3: I-set Up ang Python Environment (5 minuto)

Gumawa ng dedikadong Python environment para sa workshop na ito:

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

### Hakbang 4: Patakbuhin ang Iyong Unang Model (7 minuto)

Ngayon, patakbuhin natin ang ating unang AI model nang lokal!

#### Magsimula sa Phi-4 Mini (Inirerekomendang Unang Model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Ang command na ito ay magda-download ng model (sa unang pagkakataon) at awtomatikong sisimulan ang Foundry Local service.

#### Tingnan ang Mga Aktibong Model

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Subukan ang Iba't Ibang Model

Kapag gumagana na ang phi-4-mini, subukan ang iba pang mga model:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Hakbang 5: Gumawa ng Iyong Unang Chat Application (10 minuto)

Ngayon, gumawa tayo ng Python application na gumagamit ng mga model na sinimulan natin.

#### Gumawa ng Chat Script

Gumawa ng bagong file na tinatawag na `my_first_chat.py` (o gamitin ang ibinigay na sample):

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
> **Mga Kaugnay na Halimbawa**: Para sa mas advanced na paggamit, tingnan:
>
> - **Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - May kasamang streaming responses at error handling
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactive na bersyon na may detalyadong paliwanag

#### Subukan ang Iyong Chat Application

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatibo: Gamitin ang mga ibinigay na sample nang direkta

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

O tuklasin ang interactive notebook
Buksan ang Workshop/notebooks/session01_chat_bootstrap.ipynb sa VS Code

Subukan ang mga halimbawa ng pag-uusap:

- "Ano ang Microsoft Foundry Local?"
- "Magbigay ng 3 benepisyo ng pagpapatakbo ng AI models nang lokal"
- "Tulungan mo akong maunawaan ang edge AI"

## Ano ang Iyong Naabot

Binabati kita! Matagumpay mong:

1. ✅ **Na-install ang Foundry Local** at na-verify na gumagana ito
2. ✅ **Sinimulan ang iyong unang AI model** (phi-4-mini) nang lokal
3. ✅ **Nasubukan ang iba't ibang model** gamit ang command line
4. ✅ **Nakapagtayo ng chat application** na kumokonekta sa iyong lokal na AI
5. ✅ **Naranasan ang lokal na AI inference** nang walang cloud dependencies

## Pag-unawa sa Nangyari

### Lokal na AI Inference

- Ang iyong mga AI model ay tumatakbo nang buo sa iyong computer
- Walang data ang ipinapadala sa cloud
- Ang mga sagot ay nabubuo nang lokal gamit ang iyong CPU/GPU
- Ang privacy at seguridad ay napananatili

### Pamamahala ng Model

- Ang `foundry model run` ay nagda-download at nagsisimula ng mga model
- Ang **FoundryLocalManager SDK** ay awtomatikong humahawak sa pagsisimula ng serbisyo at pag-load ng model
- Ang mga model ay naka-cache nang lokal para sa susunod na paggamit
- Maraming model ang maaaring ma-download ngunit karaniwang isa lamang ang tumatakbo sa isang pagkakataon
- Ang serbisyo ay awtomatikong namamahala sa lifecycle ng model

### SDK vs CLI na Paraan

- **CLI Approach**: Manu-manong pamamahala ng model gamit ang `foundry model run <model>`
- **SDK Approach**: Awtomatikong serbisyo + pamamahala ng model gamit ang `FoundryLocalManager(alias)`
- **Rekomendasyon**: Gamitin ang SDK para sa mga application, CLI para sa testing at exploration

## Mga Karaniwang Command Reference

### Mahahalagang CLI Command

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

### Mga Rekomendasyon sa Model

- **phi-4-mini**: Pinakamahusay na panimulang model - mabilis, magaan, magandang kalidad
- **qwen2.5-0.5b**: Pinakamabilis na inference, minimal na memory usage
- **gpt-oss-20b**: Mas mataas na kalidad ng sagot, nangangailangan ng mas maraming resources
- **deepseek-coder-1.3b**: Na-optimize para sa programming at mga code task

## Pag-troubleshoot

### "Foundry command not found"

**Solusyon:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Solusyon:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

**Solusyon:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Mga Susunod na Hakbang

### Agarang Mga Aksyon

1. **Subukan** ang iba't ibang model at prompts
2. **Baguhin** ang iyong chat application para subukan ang iba't ibang model
3. **Gumawa** ng sarili mong prompts at subukan ang mga sagot
4. **Tuklasin** ang Session 2: Paggawa ng RAG applications

### Advanced na Landas ng Pag-aaral

1. **Session 2**: Gumawa ng AI solutions gamit ang RAG (Retrieval-Augmented Generation)
2. **Session 3**: Ihambing ang iba't ibang open-source models
3. **Session 4**: Gumamit ng mga cutting-edge models
4. **Session 5**: Gumawa ng multi-agent AI systems

## Mga Environment Variable (Opsyonal)

Para sa mas advanced na paggamit, maaari mong i-set ang mga environment variable na ito:

| Variable | Layunin | Halimbawa |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Default na model na gagamitin | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | I-override ang endpoint URL | `http://localhost:5273/v1` |

Gumawa ng `.env` file sa iyong project directory:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Karagdagang Resources

### Dokumentasyon

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Sample Code

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Kumpletong chat app na may streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactive na tutorial  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Komunidad

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Tagal ng Session**: 30 minuto hands-on + 15 minuto Q&A  
**Antas ng Kahirapan**: Baguhan  
**Mga Kinakailangan**: Windows 11/macOS 11+, Python 3.10+, Admin access

## Halimbawa ng Workshop Scenario

### Konteksto sa Tunay na Mundo

**Scenario**: Ang isang enterprise IT team ay kailangang mag-evaluate ng on-device AI inference para sa pagproseso ng sensitibong feedback ng empleyado nang hindi ipinapadala ang data sa mga external na serbisyo.

**Layunin Mo**: Ipakita na ang lokal na AI models ay maaaring magbigay ng de-kalidad na sagot na may sub-second latency habang pinapanatili ang kumpletong data privacy.

### Mga Test Prompts

Gamitin ang mga prompt na ito para i-validate ang iyong setup:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Pamantayan ng Tagumpay

- ✅ Ang lahat ng prompt ay may sagot sa loob ng 2 segundo
- ✅ Walang data ang lumalabas sa iyong lokal na makina
- ✅ Ang mga sagot ay may kaugnayan at kapaki-pakinabang
- ✅ Ang iyong chat application ay gumagana nang maayos

Ang validation na ito ay nagsisiguro na ang iyong Foundry Local setup ay handa para sa mga advanced na workshop sa Sessions 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->