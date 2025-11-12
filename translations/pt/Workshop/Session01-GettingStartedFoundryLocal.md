<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T22:41:25+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "pt"
}
-->
# Sessão 1: Introdução ao Foundry Local

## Resumo

Aprenda a instalar, configurar e executar os seus primeiros modelos de IA utilizando o Microsoft Foundry Local. Esta sessão prática oferece uma introdução passo a passo à inferência local, desde a instalação até à criação da sua primeira aplicação de chat utilizando modelos como Phi-4, Qwen e DeepSeek.

## Objetivos de Aprendizagem

Ao final desta sessão, você será capaz de:

- **Instalar e Configurar**: Configurar o Foundry Local com verificação adequada da instalação
- **Dominar Operações CLI**: Utilizar o CLI do Foundry Local para gestão e implementação de modelos
- **Executar o Seu Primeiro Modelo**: Implementar e interagir com um modelo de IA local com sucesso
- **Criar uma Aplicação de Chat**: Desenvolver uma aplicação de chat básica utilizando o Foundry Local Python SDK
- **Compreender IA Local**: Entender os fundamentos da inferência local e gestão de modelos

## Pré-requisitos

### Requisitos do Sistema

- **Windows**: Windows 11 (22H2 ou posterior) OU **macOS**: macOS 11+ (suporte limitado)
- **RAM**: Mínimo de 8GB, recomendado 16GB+
- **Armazenamento**: 10GB+ de espaço livre para modelos
- **Python**: Versão 3.10 ou posterior instalada
- **Acesso de Administrador**: Privilégios de administrador para instalação

### Ambiente de Desenvolvimento

- Visual Studio Code com extensão Python (recomendado)
- Acesso à linha de comando (PowerShell no Windows, Terminal no macOS)
- Git para clonar repositórios (opcional)

## Fluxo do Workshop (30 minutos)

### Passo 1: Instalar o Foundry Local (5 minutos)

#### Instalação no Windows

Instale o Foundry Local utilizando o gerenciador de pacotes do Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativa: Faça o download diretamente de [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalação no macOS (Suporte Limitado)

> [!NOTE] 
> O suporte ao macOS está atualmente em prévia. Consulte a documentação oficial para obter as informações mais recentes.

Se disponível, instale utilizando o Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativa para utilizadores de macOS:**
- Utilize uma VM com Windows 11 (Parallels/UTM) e siga os passos para Windows
- Execute via container, se disponível, e configure `FOUNDRY_LOCAL_ENDPOINT`

### Passo 2: Verificar a Instalação (3 minutos)

Após a instalação, reinicie o terminal e verifique se o Foundry Local está funcionando:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

A saída esperada deve mostrar informações de versão e comandos disponíveis.

### Passo 3: Configurar o Ambiente Python (5 minutos)

Crie um ambiente Python dedicado para este workshop:

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

### Passo 4: Executar o Seu Primeiro Modelo (7 minutos)

Agora vamos executar o nosso primeiro modelo de IA localmente!

#### Comece com Phi-4 Mini (Modelo Recomendado)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Este comando faz o download do modelo (na primeira vez) e inicia automaticamente o serviço Foundry Local.

#### Verifique o que está em execução

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Experimente Outros Modelos

Depois de o phi-4-mini estar funcionando, experimente outros modelos:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Passo 5: Criar a Sua Primeira Aplicação de Chat (10 minutos)

Agora vamos criar uma aplicação Python que utiliza os modelos que acabámos de iniciar.

#### Criar o Script de Chat

Crie um novo ficheiro chamado `my_first_chat.py` (ou utilize o exemplo fornecido):

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
> **Exemplos Relacionados**: Para uso mais avançado, veja:
>
> - **Exemplo em Python**: `Workshop/samples/session01/chat_bootstrap.py` - Inclui respostas em streaming e tratamento de erros
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Versão interativa com explicações detalhadas

#### Testar a Sua Aplicação de Chat

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativa: Utilize diretamente os exemplos fornecidos

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Ou explore o notebook interativo  
Abra Workshop/notebooks/session01_chat_bootstrap.ipynb no VS Code

Experimente estas conversas de exemplo:

- "O que é o Microsoft Foundry Local?"
- "Liste 3 benefícios de executar modelos de IA localmente"
- "Ajude-me a entender IA de borda"

## O Que Você Conquistou

Parabéns! Você conseguiu:

1. ✅ **Instalar o Foundry Local** e verificar que está funcionando
2. ✅ **Iniciar o seu primeiro modelo de IA** (phi-4-mini) localmente
3. ✅ **Testar diferentes modelos** via linha de comando
4. ✅ **Criar uma aplicação de chat** que se conecta à sua IA local
5. ✅ **Experimentar inferência de IA local** sem dependências na nuvem

## Compreendendo o Que Aconteceu

### Inferência de IA Local

- Os seus modelos de IA são executados inteiramente no seu computador
- Nenhum dado é enviado para a nuvem
- As respostas são geradas localmente utilizando o seu CPU/GPU
- Privacidade e segurança são mantidas

### Gestão de Modelos

- `foundry model run` faz o download e inicia os modelos
- **FoundryLocalManager SDK** lida automaticamente com o início do serviço e carregamento de modelos
- Os modelos são armazenados em cache localmente para uso futuro
- Vários modelos podem ser baixados, mas geralmente apenas um é executado por vez
- O serviço gere automaticamente o ciclo de vida dos modelos

### Abordagens SDK vs CLI

- **Abordagem CLI**: Gestão manual de modelos com `foundry model run <model>`
- **Abordagem SDK**: Gestão automática de serviços e modelos com `FoundryLocalManager(alias)`
- **Recomendação**: Utilize o SDK para aplicações, CLI para testes e exploração

## Referência de Comandos Comuns

### Comandos Essenciais do CLI

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

### Recomendações de Modelos

- **phi-4-mini**: Melhor modelo inicial - rápido, leve, boa qualidade
- **qwen2.5-0.5b**: Inferência mais rápida, uso mínimo de memória
- **gpt-oss-20b**: Respostas de maior qualidade, requer mais recursos
- **deepseek-coder-1.3b**: Otimizado para tarefas de programação e código

## Resolução de Problemas

### "Comando Foundry não encontrado"

**Solução:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Falha ao carregar o modelo"

**Solução:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Conexão recusada no localhost"

**Solução:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Próximos Passos

### Ações Imediatas

1. **Experimente** diferentes modelos e prompts
2. **Modifique** a sua aplicação de chat para testar diferentes modelos
3. **Crie** os seus próprios prompts e teste as respostas
4. **Explore** a Sessão 2: Construção de aplicações RAG

### Caminho de Aprendizagem Avançado

1. **Sessão 2**: Desenvolver soluções de IA com RAG (Geração Aumentada por Recuperação)
2. **Sessão 3**: Comparar diferentes modelos de código aberto
3. **Sessão 4**: Trabalhar com modelos de ponta
4. **Sessão 5**: Construir sistemas de IA multiagente

## Variáveis de Ambiente (Opcional)

Para uso mais avançado, pode configurar estas variáveis de ambiente:

| Variável | Finalidade | Exemplo |
|----------|------------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Modelo padrão a utilizar | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Substituir URL do endpoint | `http://localhost:5273/v1` |

Crie um ficheiro `.env` no diretório do seu projeto:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Recursos Adicionais

### Documentação

- [Referência do Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guia de Instalação do Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catálogo de Modelos](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Código de Exemplo

- **Exemplo em Python da Sessão01**: `Workshop/samples/session01/chat_bootstrap.py` - Aplicação de chat completa com streaming
- **Notebook da Sessão01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutorial interativo  
- [Exemplo do Módulo08 01](../Module08/samples/01/README.md) - Introdução ao Chat REST
- [Exemplo do Módulo08 02](../Module08/samples/02/README.md) - Integração com OpenAI SDK
- [Exemplo do Módulo08 03](../Module08/samples/03/README.md) - Descoberta e Benchmarking de Modelos

### Comunidade

- [Discussões no GitHub do Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Comunidade Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Duração da Sessão**: 30 minutos práticos + 15 minutos de perguntas e respostas  
**Nível de Dificuldade**: Iniciante  
**Pré-requisitos**: Windows 11/macOS 11+, Python 3.10+, Acesso de administrador

## Cenário de Exemplo do Workshop

### Contexto Real

**Cenário**: Uma equipa de TI empresarial precisa avaliar a inferência de IA no dispositivo para processar feedback sensível de funcionários sem enviar dados para serviços externos.

**Seu Objetivo**: Demonstrar que modelos de IA locais podem fornecer respostas de qualidade com latência inferior a um segundo, mantendo total privacidade dos dados.

### Prompts de Teste

Utilize estes prompts para validar a sua configuração:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Critérios de Sucesso

- ✅ Todos os prompts recebem respostas em menos de 2 segundos
- ✅ Nenhum dado sai do seu computador local
- ✅ As respostas são relevantes e úteis
- ✅ A sua aplicação de chat funciona sem problemas

Esta validação garante que a sua configuração do Foundry Local está pronta para os workshops avançados das Sessões 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->