# Sesiunea 1: Începuturi cu Foundry Local

## Rezumat

Învață să instalezi, configurezi și să rulezi primele modele AI folosind Microsoft Foundry Local. Această sesiune practică oferă o introducere pas cu pas în inferența locală, de la instalare până la construirea primei aplicații de chat utilizând modele precum Phi-4, Qwen și DeepSeek.

## Obiective de învățare

Până la finalul acestei sesiuni, vei putea:

- **Instala și Configura**: Configura Foundry Local cu verificarea corectă a instalării
- **Stăpâni operațiunile CLI**: Utiliza CLI-ul Foundry Local pentru gestionarea și implementarea modelelor
- **Rula primul model**: Implementa și interacționa cu un model AI local
- **Construi o aplicație de chat**: Crea o aplicație de chat de bază folosind Foundry Local Python SDK
- **Înțelege AI local**: Înțelege fundamentele inferenței locale și gestionării modelelor

## Cerințe preliminare

### Cerințe de sistem

- **Windows**: Windows 11 (22H2 sau mai recent) SAU **macOS**: macOS 11+ (suport limitat)
- **RAM**: Minimum 8GB, recomandat 16GB+
- **Spațiu de stocare**: Minimum 10GB liber pentru modele
- **Python**: Instalată versiunea 3.10 sau mai recentă
- **Acces Administrator**: Privilegii de administrator pentru instalare

### Mediu de dezvoltare

- Visual Studio Code cu extensia Python (recomandat)
- Acces la linia de comandă (PowerShell pe Windows, Terminal pe macOS)
- Git pentru clonarea depozitelor (opțional)

## Fluxul atelierului (30 de minute)

### Pasul 1: Instalarea Foundry Local (5 minute)

#### Instalare pe Windows

Instalează Foundry Local folosind managerul de pachete Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativ: Descarcă direct de la [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalare pe macOS (Suport limitat)

> [!NOTE] 
> Suportul pentru macOS este în prezent în versiune de previzualizare. Verifică documentația oficială pentru cele mai recente informații.

Dacă este disponibil, instalează folosind Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativ pentru utilizatorii macOS:**
- Folosește o mașină virtuală Windows 11 (Parallels/UTM) și urmează pașii pentru Windows
- Rulează prin container, dacă este disponibil, și configurează `FOUNDRY_LOCAL_ENDPOINT`

### Pasul 2: Verificarea instalării (3 minute)

După instalare, repornește terminalul și verifică funcționarea Foundry Local:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Rezultatul așteptat ar trebui să afișeze informații despre versiune și comenzi disponibile.

### Pasul 3: Configurarea mediului Python (5 minute)

Creează un mediu Python dedicat pentru acest atelier:

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

### Pasul 4: Rulează primul model (7 minute)

Acum să rulăm primul model AI local!

#### Începe cu Phi-4 Mini (Modelul recomandat pentru început)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Această comandă descarcă modelul (prima dată) și pornește automat serviciul Foundry Local.

#### Verifică ce rulează

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Încearcă modele diferite

După ce phi-4-mini funcționează, experimentează cu alte modele:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Pasul 5: Construiește prima aplicație de chat (10 minute)

Acum să creăm o aplicație Python care folosește modelele pe care tocmai le-am pornit.

#### Creează scriptul de chat

Creează un fișier nou numit `my_first_chat.py` (sau folosește exemplul furnizat):

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
> **Exemple relevante**: Pentru utilizare avansată, vezi:
>
> - **Exemplu Python**: `Workshop/samples/session01/chat_bootstrap.py` - Include răspunsuri în flux și gestionarea erorilor
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Versiune interactivă cu explicații detaliate

#### Testează aplicația de chat

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativ: Folosește direct exemplele furnizate

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Sau explorează notebook-ul interactiv  
Deschide Workshop/notebooks/session01_chat_bootstrap.ipynb în VS Code

Încearcă aceste conversații exemplu:

- "Ce este Microsoft Foundry Local?"
- "Listează 3 beneficii ale rulării modelelor AI local"
- "Ajută-mă să înțeleg AI-ul edge"

## Ce ai realizat

Felicitări! Ai reușit să:

1. ✅ **Instalezi Foundry Local** și să verifici funcționarea acestuia
2. ✅ **Pornești primul model AI** (phi-4-mini) local
3. ✅ **Testezi modele diferite** prin linia de comandă
4. ✅ **Construiești o aplicație de chat** care se conectează la AI-ul local
5. ✅ **Experimentezi inferența AI locală** fără dependențe de cloud

## Înțelegerea procesului

### Inferența AI locală

- Modelele AI rulează complet pe computerul tău
- Nicio dată nu este trimisă în cloud
- Răspunsurile sunt generate local folosind CPU/GPU-ul tău
- Confidențialitatea și securitatea sunt menținute

### Gestionarea modelelor

- `foundry model run` descarcă și pornește modelele
- **FoundryLocalManager SDK** gestionează automat pornirea serviciului și încărcarea modelelor
- Modelele sunt stocate local pentru utilizări viitoare
- Pot fi descărcate mai multe modele, dar de obicei rulează unul singur la un moment dat
- Serviciul gestionează automat ciclul de viață al modelului

### Abordări SDK vs CLI

- **Abordarea CLI**: Gestionarea manuală a modelelor cu `foundry model run <model>`
- **Abordarea SDK**: Gestionarea automată a serviciului și a modelelor cu `FoundryLocalManager(alias)`
- **Recomandare**: Folosește SDK pentru aplicații, CLI pentru testare și explorare

## Referință comenzi comune

### Comenzi esențiale CLI

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

### Recomandări pentru modele

- **phi-4-mini**: Cel mai bun model pentru început - rapid, ușor, calitate bună
- **qwen2.5-0.5b**: Inferență rapidă, consum minim de memorie
- **gpt-oss-20b**: Răspunsuri de calitate superioară, necesită mai multe resurse
- **deepseek-coder-1.3b**: Optimizat pentru sarcini de programare și codare

## Depanare

### "Comanda Foundry nu a fost găsită"

**Soluție:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Modelul nu a putut fi încărcat"

**Soluție:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Conexiune refuzată pe localhost"

**Soluție:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Pași următori

### Acțiuni imediate

1. **Experimentează** cu modele și solicitări diferite
2. **Modifică** aplicația de chat pentru a încerca modele diferite
3. **Creează** propriile tale solicitări și testează răspunsurile
4. **Explorează** Sesiunea 2: Construirea aplicațiilor RAG

### Cale de învățare avansată

1. **Sesiunea 2**: Construiește soluții AI cu RAG (Generare Augmentată prin Recuperare)
2. **Sesiunea 3**: Compară diferite modele open-source
3. **Sesiunea 4**: Lucrează cu modele de ultimă generație
4. **Sesiunea 5**: Construiește sisteme AI multi-agent

## Variabile de mediu (Opțional)

Pentru utilizare avansată, poți seta aceste variabile de mediu:

| Variabilă | Scop | Exemplu |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Modelul implicit de utilizat | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Suprascrie URL-ul endpoint-ului | `http://localhost:5273/v1` |

Creează un fișier `.env` în directorul proiectului:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Resurse suplimentare

### Documentație

- [Referință Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Ghid de instalare Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catalogul de modele](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Cod exemplu

- **Exemplu Python Sesiunea01**: `Workshop/samples/session01/chat_bootstrap.py` - Aplicație completă de chat cu streaming
- **Notebook Sesiunea01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutorial interactiv  
- [Exemplu Modul08 01](../Module08/samples/01/README.md) - Introducere rapidă în REST Chat
- [Exemplu Modul08 02](../Module08/samples/02/README.md) - Integrare OpenAI SDK
- [Exemplu Modul08 03](../Module08/samples/03/README.md) - Descoperirea și evaluarea modelelor

### Comunitate

- [Discuții GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Comunitatea Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durata sesiunii**: 30 de minute practică + 15 minute întrebări și răspunsuri  
**Nivel de dificultate**: Începător  
**Cerințe preliminare**: Windows 11/macOS 11+, Python 3.10+, Acces administrator

## Scenariu exemplu pentru atelier

### Context real

**Scenariu**: O echipă IT dintr-o companie trebuie să evalueze inferența AI pe dispozitiv pentru procesarea feedback-ului sensibil al angajaților fără a trimite date către servicii externe.

**Obiectivul tău**: Demonstrează că modelele AI locale pot oferi răspunsuri de calitate cu o latență sub o secundă, menținând în același timp confidențialitatea completă a datelor.

### Solicitări de testare

Folosește aceste solicitări pentru a valida configurarea:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Criterii de succes

- ✅ Toate solicitările primesc răspunsuri în mai puțin de 2 secunde
- ✅ Nicio dată nu părăsește computerul local
- ✅ Răspunsurile sunt relevante și utile
- ✅ Aplicația ta de chat funcționează fără probleme

Această validare asigură că configurarea ta Foundry Local este pregătită pentru atelierele avansate din Sesiunile 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->