<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T21:15:29+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "en"
}
-->
# Session 1: Getting Started with Foundry Local

## Abstract

Learn how to install, configure, and run your first AI models using Microsoft Foundry Local. This hands-on session provides a step-by-step guide to local inference, from installation to building your first chat application using models like Phi-4, Qwen, and DeepSeek.

## Learning Objectives

By the end of this session, you will:

- **Install and Configure**: Set up Foundry Local and verify the installation
- **Master CLI Operations**: Use Foundry Local CLI for managing and deploying models
- **Run Your First Model**: Deploy and interact with a local AI model successfully
- **Build a Chat App**: Develop a basic chat application using the Foundry Local Python SDK
- **Understand Local AI**: Learn the basics of local inference and model management

## Prerequisites

### System Requirements

- **Windows**: Windows 11 (22H2 or later) OR **macOS**: macOS 11+ (limited support)
- **RAM**: Minimum 8GB, recommended 16GB+
- **Storage**: At least 10GB free space for models
- **Python**: Version 3.10 or later installed
- **Admin Access**: Administrator privileges for installation

### Development Environment

- Visual Studio Code with Python extension (recommended)
- Command line access (PowerShell for Windows, Terminal for macOS)
- Git for cloning repositories (optional)

## Workshop Flow (30 minutes)

### Step 1: Install Foundry Local (5 minutes)

#### Windows Installation

Install Foundry Local using the Windows package manager:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternative: Download directly from [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### macOS Installation (Limited Support)

> [!NOTE] 
> macOS support is currently in preview. Check official documentation for the latest updates.

If available, install using Homebrew:

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
- Use a Windows 11 VM (Parallels/UTM) and follow the Windows installation steps
- Run via container if available and configure `FOUNDRY_LOCAL_ENDPOINT`

### Step 2: Verify Installation (3 minutes)

After installation, restart your terminal and confirm Foundry Local is working:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Expected output should display version information and available commands.

### Step 3: Set Up Python Environment (5 minutes)

Create a dedicated Python environment for this workshop:

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

Now, let's run our first AI model locally!

#### Start with Phi-4 Mini (Recommended First Model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> This command downloads the model (on first use) and starts the Foundry Local service automatically.

#### Check What's Running

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Try Different Models

Once phi-4-mini is running, experiment with other models:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Step 5: Build Your First Chat Application (10 minutes)

Now, let's create a Python application that uses the models you just started.

#### Create the Chat Script

Create a new file called `my_first_chat.py` (or use the provided sample):

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
> **Related Examples**: For more advanced usage, see:
>
> - **Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - Includes streaming responses and error handling
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interactive version with detailed explanations

#### Test Your Chat Application

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternative: Use the provided samples directly

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Or explore the interactive notebook
Open Workshop/notebooks/session01_chat_bootstrap.ipynb in VS Code

Try these example conversations:

- "What is Microsoft Foundry Local?"
- "List 3 benefits of running AI models locally"
- "Help me understand edge AI"

## What You've Accomplished

Congratulations! You've successfully:

1. ✅ **Installed Foundry Local** and verified its functionality
2. ✅ **Started your first AI model** (phi-4-mini) locally
3. ✅ **Tested different models** via the command line
4. ✅ **Built a chat application** that connects to your local AI
5. ✅ **Experienced local AI inference** without relying on the cloud

## Understanding What Happened

### Local AI Inference

- Your AI models run entirely on your computer
- No data is sent to the cloud
- Responses are generated locally using your CPU/GPU
- Privacy and security are maintained

### Model Management

- `foundry model run` downloads and starts models
- **FoundryLocalManager SDK** automatically handles service startup and model loading
- Models are cached locally for future use
- Multiple models can be downloaded, but typically one runs at a time
- The service automatically manages the model lifecycle

### SDK vs CLI Approaches

- **CLI Approach**: Manual model management with `foundry model run <model>`
- **SDK Approach**: Automatic service and model management with `FoundryLocalManager(alias)`
- **Recommendation**: Use SDK for applications, CLI for testing and exploration

## Common Commands Reference

### Essential CLI Commands

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

- **phi-4-mini**: Best starter model - fast, lightweight, good quality
- **qwen2.5-0.5b**: Fastest inference, minimal memory usage
- **gpt-oss-20b**: Higher quality responses, requires more resources
- **deepseek-coder-1.3b**: Optimized for programming and code tasks

## Troubleshooting

### "Foundry command not found"

**Solution:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Model failed to load"

**Solution:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connection refused on localhost"

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

### Immediate Next Actions

1. **Experiment** with different models and prompts
2. **Modify** your chat application to try different models
3. **Create** your own prompts and test responses
4. **Explore** Session 2: Building RAG applications

### Advanced Learning Path

1. **Session 2**: Build AI solutions with RAG (Retrieval-Augmented Generation)
2. **Session 3**: Compare different open-source models
3. **Session 4**: Work with cutting-edge models
4. **Session 5**: Build multi-agent AI systems

## Environment Variables (Optional)

For more advanced usage, you can set these environment variables:

| Variable | Purpose | Example |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Default model to use | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Override endpoint URL | `http://localhost:5273/v1` |

Create a `.env` file in your project directory:
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

**Session Duration**: 30 minutes hands-on + 15 minutes Q&A  
**Difficulty Level**: Beginner  
**Prerequisites**: Windows 11/macOS 11+, Python 3.10+, Admin access

## Workshop Example Scenario

### Real-World Context

**Scenario**: An enterprise IT team needs to evaluate on-device AI inference for processing sensitive employee feedback without sending data to external services.

**Your Goal**: Demonstrate that local AI models can provide quality responses with sub-second latency while maintaining complete data privacy.

### Test Prompts

Use these prompts to validate your setup:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Success Criteria

- ✅ All prompts get responses in under 2 seconds
- ✅ No data leaves your local machine
- ✅ Responses are relevant and helpful
- ✅ Your chat application works smoothly

This validation ensures your Foundry Local setup is ready for the advanced workshops in Sessions 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->