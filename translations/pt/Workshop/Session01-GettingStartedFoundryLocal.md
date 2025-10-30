<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T21:30:29+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "pt"
}
-->
# Sessão 1: Introdução ao Foundry Local

## Resumo

Inicie a sua jornada com o Foundry Local instalando e configurando-o no Windows 11. Aprenda a configurar a CLI, ativar a aceleração de hardware e armazenar modelos em cache para inferência local rápida. Esta sessão prática aborda a execução de modelos como Phi, Qwen, DeepSeek e GPT-OSS-20B utilizando comandos CLI reproduzíveis.

## Objetivos de Aprendizagem

Ao final desta sessão, você será capaz de:

- **Instalar e Configurar**: Configurar o Foundry Local no Windows 11 com definições de desempenho otimizadas
- **Dominar Operações CLI**: Utilizar a CLI do Foundry Local para gestão e implementação de modelos
- **Ativar Aceleração de Hardware**: Configurar aceleração GPU com ONNXRuntime ou WebGPU
- **Implementar Múltiplos Modelos**: Executar os modelos phi-4, GPT-OSS-20B, Qwen e DeepSeek localmente
- **Construir a Sua Primeira Aplicação**: Adaptar exemplos existentes para usar o SDK Python do Foundry Local

# Testar o modelo (prompt único não interativo)
foundry model run phi-4-mini --prompt "Olá, apresente-se"

- Windows 11 (22H2 ou posterior)
# Listar modelos disponíveis no catálogo (modelos carregados aparecem após execução)
foundry model list
## NOTA: Atualmente não há uma flag dedicada `--running`; para ver quais estão carregados, inicie um chat ou inspecione os registos de serviço.
- Python 3.10+ instalado
- Visual Studio Code com extensão Python
- Privilégios de administrador para instalação

### (Opcional) Variáveis de Ambiente

Crie um `.env` (ou defina no shell) para tornar os scripts portáveis:
# Comparar respostas (não interativo)
foundry model run gpt-oss-20b --prompt "Explique inteligência artificial de borda em termos simples"
| Variável | Propósito | Exemplo |
|----------|-----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias preferido do modelo (o catálogo seleciona automaticamente a melhor variante) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Substituir endpoint (caso contrário, automático a partir do gestor) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Ativar demonstração de streaming | `true` |

> Se `FOUNDRY_LOCAL_ENDPOINT=auto` (ou não definido), derivamos do gestor SDK.

## Fluxo de Demonstração (30 minutos)

### 1. Instalar Foundry Local e Verificar Configuração CLI (10 minutos)

# Listar modelos em cache
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Prévia / Se Suportado)**

Se um pacote nativo para macOS for fornecido (verifique a documentação oficial para as últimas atualizações):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Se os binários nativos para macOS ainda não estiverem disponíveis, você pode:
1. Utilizar uma VM Windows 11 ARM/Intel (Parallels / UTM) e seguir os passos para Windows. 
2. Executar modelos via container (se a imagem do container for publicada) e definir `FOUNDRY_LOCAL_ENDPOINT` para a porta exposta.

**Criar Ambiente Virtual Python (Multiplataforma)**

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

Atualize o pip e instale as dependências principais:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Passo 1.2: Verificar Instalação

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Passo 1.3: Configurar Ambiente

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Inicialização do SDK (Recomendado)

Em vez de iniciar manualmente o serviço e executar modelos, o **SDK Python do Foundry Local** pode inicializar tudo:

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

Se preferir controle explícito, ainda pode usar a CLI + cliente OpenAI conforme mostrado mais tarde.

### 2. Executar Modelos Localmente via CLI (10 minutos)

#### Passo 3.1: Implementar Modelo Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Passo 3.2: Implementar GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Passo 3.3: Carregar Modelos Adicionais

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Projeto Inicial: Adaptar 01-run-phi para Foundry Local (5 minutos)

#### Passo 4.1: Criar Aplicação Básica de Chat

Crie `samples/01-foundry-quickstart/chat_quickstart.py` (atualizado para usar o gestor, se disponível):

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

#### Passo 4.2: Testar a Aplicação

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Conceitos-Chave Abordados

### 1. Arquitetura do Foundry Local

- **Motor de Inferência Local**: Executa modelos inteiramente no seu dispositivo
- **Compatibilidade com SDK OpenAI**: Integração perfeita com código OpenAI existente
- **Gestão de Modelos**: Baixar, armazenar em cache e executar múltiplos modelos de forma eficiente
- **Otimização de Hardware**: Aproveitar aceleração de GPU, NPU e CPU

### 2. Referência de Comandos CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integração com SDK Python

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

## Resolução de Problemas Comuns

### Problema 1: "Comando Foundry não encontrado"

**Solução:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problema 2: "Falha ao carregar o modelo"

**Solução:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problema 3: "Conexão recusada em localhost:5273"

**Solução:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Dicas de Otimização de Desempenho

### 1. Estratégia de Seleção de Modelos

- **Phi-4-mini**: Melhor para tarefas gerais, menor uso de memória
- **Qwen2.5-0.5b**: Inferência mais rápida, recursos mínimos
- **GPT-OSS-20B**: Qualidade mais alta, requer mais recursos
- **DeepSeek-Coder**: Otimizado para tarefas de programação

### 2. Otimização de Hardware

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitorização de Desempenho

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

### Melhorias Opcionais

| Melhoria | O que é | Como |
|----------|---------|------|
| Utilitários Compartilhados | Remover lógica duplicada de cliente/inicialização | Use `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Visibilidade de Uso de Tokens | Ensinar pensamento sobre custo/eficiência desde cedo | Defina `SHOW_USAGE=1` para imprimir tokens de prompt/completion/total |
| Comparações Determinísticas | Benchmarking estável e verificações de regressão | Use `temperature=0`, `top_p=1`, texto de prompt consistente |
| Latência do Primeiro Token | Métrica de responsividade percebida | Adapte script de benchmark com streaming (`BENCH_STREAM=1`) |
| Repetição em Erros Transitórios | Demonstrações resilientes em inicialização fria | `RETRY_ON_FAIL=1` (padrão) e ajuste `RETRY_BACKOFF` |
| Testes de Fumaça | Verificação rápida de fluxos principais | Execute `python Workshop/tests/smoke.py` antes de um workshop |
| Perfis de Alias de Modelos | Alterar rapidamente o conjunto de modelos entre máquinas | Mantenha `.env` com `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Eficiência de Cache | Evitar aquecimentos repetidos em execução de múltiplas amostras | Utilitários de gestão de cache; reutilize entre scripts/notebooks |
| Aquecimento na Primeira Execução | Reduzir picos de latência p95 | Dispare um prompt pequeno após a criação do `FoundryLocalManager`

Exemplo de base de aquecimento determinístico (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Você deve ver saída semelhante e contagens de tokens idênticas na segunda execução, confirmando o determinismo.

## Próximos Passos

Após completar esta sessão:

1. **Explore a Sessão 2**: Construa soluções de IA com Azure AI Foundry RAG
2. **Experimente Diferentes Modelos**: Teste Qwen, DeepSeek e outras famílias de modelos
3. **Otimize o Desempenho**: Ajuste configurações para o seu hardware específico
4. **Construa Aplicações Personalizadas**: Utilize o SDK Foundry Local nos seus próprios projetos

## Recursos Adicionais

### Documentação
- [Referência do SDK Python do Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guia de Instalação do Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catálogo de Modelos](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Código de Exemplo
- [Exemplo do Módulo08 01](./samples/01/README.md) - Introdução ao Chat REST
- [Exemplo do Módulo08 02](./samples/02/README.md) - Integração com SDK OpenAI
- [Exemplo do Módulo08 03](./samples/03/README.md) - Descoberta e Benchmarking de Modelos

### Comunidade
- [Discussões no GitHub do Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Comunidade Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Duração da Sessão**: 30 minutos de prática + 15 minutos de perguntas e respostas  
**Nível de Dificuldade**: Iniciante  
**Pré-requisitos**: Windows 11, Python 3.10+, acesso de administrador  

## Cenário de Exemplo e Mapeamento de Workshop

| Script / Notebook do Workshop | Cenário | Objetivo | Exemplo de Entrada(s) | Dataset Necessário |
|-------------------------------|---------|----------|-----------------------|--------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Equipa interna de TI avaliando inferência no dispositivo para um portal de avaliação de privacidade | Demonstrar que o SLM local responde com latência inferior a um segundo em prompts padrão | "Liste dois benefícios da inferência local." | Nenhum (prompt único) |
| Código de adaptação do quickstart | Desenvolvedor migrando um script OpenAI existente para Foundry Local | Mostrar compatibilidade imediata | "Dê dois benefícios da inferência local." | Apenas prompt inline |

### Narrativa do Cenário
A equipa de segurança e conformidade deve validar se dados sensíveis de protótipos podem ser processados localmente. Eles executam o script de inicialização com vários prompts (privacidade, latência, custo) utilizando um modo determinístico `temperature=0` para capturar saídas base para comparação posterior (benchmarking na Sessão 3 e contraste SLM vs LLM na Sessão 4).

### JSON de Prompt Mínimo (opcional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Use esta lista para criar um loop de avaliação reproduzível ou para iniciar um futuro conjunto de testes de regressão.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.