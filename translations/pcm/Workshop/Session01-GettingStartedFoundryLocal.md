# Session 1: How to Start with Foundry Local

## Abstract

Learn how to install, set up, and run your first AI models with Microsoft Foundry Local. This na practical session wey go show you step-by-step how to do local inference, from installation to building your first chat app with models like Phi-4, Qwen, and DeepSeek.

## Learning Objectives

By the time we finish this session, you go don sabi:

- **Install and Configure**: How to set up Foundry Local and confirm say e dey work well
- **Master CLI Operations**: How to use Foundry Local CLI to manage and deploy models
- **Run Your First Model**: How to deploy and interact with local AI model
- **Build a Chat App**: How to create simple chat app with Foundry Local Python SDK
- **Understand Local AI**: Learn the basics of local inference and model management

## Prerequisites

### System Requirements

- **Windows**: Windows 11 (22H2 or later) OR **macOS**: macOS 11+ (limited support)
- **RAM**: At least 8GB, but 16GB+ go better
- **Storage**: At least 10GB free space for models
- **Python**: Version 3.10 or higher
- **Admin Access**: You go need admin rights to install am

### Development Environment

- Visual Studio Code with Python extension (recommended)
- Command line access (PowerShell for Windows, Terminal for macOS)
- Git for cloning repositories (optional)

## Workshop Flow (30 minutes)

### Step 1: Install Foundry Local (5 minutes)

#### Windows Installation

Install Foundry Local with Windows package manager:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternative: Download am directly from [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### macOS Installation (Limited Support)

> [!NOTE] 
> macOS support still dey preview. Check official documentation for latest update.

If e dey available, install am with Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternative for macOS users:**
- Use Windows 11 VM (Parallels/UTM) and follow Windows steps
- Run am with container if e dey available and configure `FOUNDRY_LOCAL_ENDPOINT`

### Step 2: Verify Installation (3 minutes)

After you don install am, restart your terminal and confirm say Foundry Local dey work:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

You suppose see output wey go show version info and available commands.

### Step 3: Set Up Python Environment (5 minutes)

Create one Python environment wey go dey for this workshop:

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

### Step 4: Run Your First Model (7 minutes)

Now, make we run our first AI model for your computer!

#### Start with Phi-4 Mini (Recommended First Model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> This command go download the model (first time) and start the Foundry Local service automatically.

#### Check Wetin Dey Run

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Try Other Models

After phi-4-mini don work, test other models:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Step 5: Build Your First Chat Application (10 minutes)

Now, make we create Python app wey go use the models wey we don start.

#### Create the Chat Script

Create new file wey you go call `my_first_chat.py` (or use the sample wey dem provide):

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
> **Related Examples**: For more advanced usage, check:
>
> - **Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - E get streaming responses and error handling
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactive version wey explain am well

#### Test Your Chat Application

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternative: Use the samples wey dem provide directly

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Or check the interactive notebook
Open Workshop/notebooks/session01_chat_bootstrap.ipynb for VS Code

Try these example conversations:

- "Wetin be Microsoft Foundry Local?"
- "List 3 benefits of running AI models locally"
- "Help me understand edge AI"

## Wetin You Don Achieve

Congrats! You don successfully:

1. ✅ **Install Foundry Local** and confirm say e dey work
2. ✅ **Start your first AI model** (phi-4-mini) for your computer
3. ✅ **Test different models** with command line
4. ✅ **Build chat app** wey dey connect to your local AI
5. ✅ **Experience local AI inference** without cloud wahala

## Understand Wetin Happen

### Local AI Inference

- Your AI models dey run for your computer
- No data dey go cloud
- Responses dey generate locally with your CPU/GPU
- Privacy and security dey intact

### Model Management

- `foundry model run` dey download and start models
- **FoundryLocalManager SDK** dey handle service startup and model loading automatically
- Models dey save for your computer for future use
- You fit download many models but na only one go dey run at a time
- The service dey manage model lifecycle by itself

### SDK vs CLI Approaches

- **CLI Approach**: You go manage models manually with `foundry model run <model>`
- **SDK Approach**: E dey handle service and model management automatically with `FoundryLocalManager(alias)`
- **Recommendation**: Use SDK for apps, CLI for testing and exploration

## Common Commands Reference

### Important CLI Commands

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

### Model Recommendations

- **phi-4-mini**: Best model to start with - e fast, light, and good quality
- **qwen2.5-0.5b**: Fast inference, small memory usage
- **gpt-oss-20b**: Better quality responses, but e need more resources
- **deepseek-coder-1.3b**: E dey good for programming and code tasks

## Troubleshooting

### "Foundry command no dey work"

**Solution:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model no fit load"

**Solution:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection no dey work for localhost"

**Solution:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Next Steps

### Wetin You Fit Do Next

1. **Try** different models and prompts
2. **Change** your chat app to test different models
3. **Create** your own prompts and test responses
4. **Check** Session 2: Building RAG applications

### Advanced Learning Path

1. **Session 2**: Build AI solutions with RAG (Retrieval-Augmented Generation)
2. **Session 3**: Compare different open-source models
3. **Session 4**: Work with latest models
4. **Session 5**: Build multi-agent AI systems

## Environment Variables (Optional)

For advanced usage, you fit set these environment variables:

| Variable | Purpose | Example |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Default model wey you go use | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Change endpoint URL | `http://localhost:5273/v1` |

Create `.env` file for your project directory:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Additional Resources

### Documentation

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Sample Code

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Complete chat app with streaming
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactive tutorial  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](../Module08/samples/03/README.md) - Model Discovery & Benchmarking

### Community

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Session Duration**: 30 minutes practical + 15 minutes Q&A  
**Difficulty Level**: Beginner  
**Prerequisites**: Windows 11/macOS 11+, Python 3.10+, Admin access

## Workshop Example Scenario

### Real-Life Example

**Scenario**: One IT team for company wan test how dem fit use AI for their computer to process sensitive feedback from workers without sending data go external services.

**Your Goal**: Show say local AI models fit give better responses fast fast and still keep data private.

### Test Prompts

Use these prompts to test your setup:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Success Criteria

- ✅ All prompts dey get response under 2 seconds
- ✅ No data dey leave your computer
- ✅ Responses dey relevant and helpful
- ✅ Your chat app dey work well

This test go show say your Foundry Local setup don ready for advanced workshops for Sessions 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->