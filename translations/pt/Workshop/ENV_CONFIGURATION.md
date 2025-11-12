<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T22:40:54+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "pt"
}
-->
# Guia de Configuração do Ambiente

## Visão Geral

Os exemplos do Workshop utilizam variáveis de ambiente para configuração, centralizadas no ficheiro `.env` na raiz do repositório. Isto permite uma personalização fácil sem modificar o código.

## Início Rápido

### 1. Verificar Pré-requisitos

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Configurar Ambiente

O ficheiro `.env` já está configurado com valores padrão sensatos. A maioria dos utilizadores não precisará alterar nada.

**Opcional**: Rever e personalizar configurações:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Aplicar Configuração

**Para Scripts Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Para Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referência de Variáveis de Ambiente

### Configuração Principal

| Variável | Padrão | Descrição |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Modelo padrão para exemplos |
| `FOUNDRY_LOCAL_ENDPOINT` | (vazio) | Substituir o endpoint do serviço |
| `PYTHONPATH` | Caminhos do Workshop | Caminho de pesquisa de módulos Python |

**Quando configurar FOUNDRY_LOCAL_ENDPOINT:**
- Instância remota do Foundry Local
- Configuração de porta personalizada
- Separação entre desenvolvimento/produção

**Exemplo:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Variáveis Específicas de Sessão

#### Sessão 02: Pipeline RAG
| Variável | Padrão | Propósito |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modelo de embeddings |
| `RAG_QUESTION` | Pré-configurado | Pergunta de teste |

#### Sessão 03: Benchmarking
| Variável | Padrão | Propósito |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modelos para benchmarking |
| `BENCH_ROUNDS` | `3` | Iterações por modelo |
| `BENCH_PROMPT` | Pré-configurado | Prompt de teste |
| `BENCH_STREAM` | `0` | Medir latência do primeiro token |

#### Sessão 04: Comparação de Modelos
| Variável | Padrão | Propósito |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | Modelo de linguagem pequeno |
| `LLM_ALIAS` | `qwen2.5-7b` | Modelo de linguagem grande |
| `COMPARE_PROMPT` | Pré-configurado | Prompt de comparação |
| `COMPARE_RETRIES` | `2` | Tentativas de repetição |

#### Sessão 05: Orquestração Multi-Agente
| Variável | Padrão | Propósito |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelo do agente pesquisador |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Modelo do agente editor |
| `AGENT_QUESTION` | Pré-configurado | Pergunta de teste |

### Configuração de Fiabilidade

| Variável | Padrão | Propósito |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | Imprimir uso de tokens |
| `RETRY_ON_FAIL` | `1` | Ativar lógica de repetição |
| `RETRY_BACKOFF` | `1.0` | Atraso na repetição (segundos) |

## Configurações Comuns

### Configuração de Desenvolvimento (Iteração Rápida)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Configuração de Produção (Foco na Qualidade)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Configuração de Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Especialização Multi-Agente
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Desenvolvimento Remoto
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Modelos Recomendados

### Por Caso de Uso

**Uso Geral:**
- `phi-4-mini` - Qualidade e velocidade equilibradas

**Respostas Rápidas:**
- `qwen2.5-0.5b` - Muito rápido, bom para classificação
- `phi-4-mini` - Rápido com boa qualidade

**Alta Qualidade:**
- `qwen2.5-7b` - Melhor qualidade, maior uso de recursos
- `phi-4-mini` - Boa qualidade, menos recursos

**Geração de Código:**
- `deepseek-coder-1.3b` - Especializado para código
- `phi-4-mini` - Propósito geral para programação

### Por Disponibilidade de Recursos

**Poucos Recursos (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Recursos Médios (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Altos Recursos (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Configuração Avançada

### Endpoints Personalizados

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatura e Amostragem (Substituir no Código)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Configuração Híbrida Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Resolução de Problemas

### Variáveis de Ambiente Não Carregadas

**Sintomas:**
- Scripts utilizam modelos errados
- Erros de conexão
- Variáveis não reconhecidas

**Soluções:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Problemas de Conexão ao Serviço

**Sintomas:**
- Erros de "Conexão recusada"
- "Serviço não disponível"
- Erros de timeout

**Soluções:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Modelo Não Encontrado

**Sintomas:**
- Erros de "Modelo não encontrado"
- "Alias não reconhecido"

**Soluções:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Erros de Importação

**Sintomas:**
- Erros de "Módulo não encontrado"

**Soluções:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testar Configuração

### Verificar Carregamento do Ambiente

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Testar Conexão ao Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Práticas de Segurança Recomendadas

### 1. Nunca Cometer Segredos

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Usar Ficheiros .env Separados

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rodar Chaves de API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Usar Configuração Específica para o Ambiente

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Documentação do SDK

- **Repositório Principal**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentação da API**: Verificar repositório do SDK para a versão mais recente

## Recursos Adicionais

- `QUICK_START.md` - Guia de início rápido
- `Workshop/samples/*/README.md` - Guias específicos para exemplos

---

**Última Atualização**: 2025-01-08  
**Versão**: 2.0  
**SDK**: Foundry Local Python SDK (mais recente)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->