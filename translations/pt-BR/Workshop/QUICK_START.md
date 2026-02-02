# Guia Rápido do Workshop

## Pré-requisitos

### 1. Instalar Foundry Local

Siga o guia oficial de instalação:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Instalar Dependências do Python

A partir do diretório do Workshop:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Executando Exemplos do Workshop

### Sessão 01: Chat Básico

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Variáveis de Ambiente:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sessão 02: Pipeline RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Variáveis de Ambiente:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sessão 02: Avaliação RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Nota**: Requer dependências adicionais instaladas via `requirements.txt`

### Sessão 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Variáveis de Ambiente:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Saída**: JSON com métricas de latência, throughput e primeiro token

### Sessão 04: Comparação de Modelos

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Variáveis de Ambiente:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sessão 05: Orquestração Multi-Agente

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Variáveis de Ambiente:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sessão 06: Roteador de Modelos

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testa lógica de roteamento** com múltiplas intenções (código, resumo, classificação)

### Sessão 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Pipeline complexo de múltiplas etapas** com planejamento, execução e refinamento

## Scripts

### Exportar Relatório de Benchmark

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Saída**: Tabela em Markdown + métricas em JSON

### Verificar Padrões de CLI no Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Objetivo**: Detectar padrões de CLI obsoletos na documentação

## Testes

### Testes de Fumaça

```bash
cd Workshop
python -m tests.smoke
```

**Testes**: Funcionalidade básica dos principais exemplos

## Solução de Problemas

### Serviço Não Está Funcionando

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Erros de Importação de Módulos

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Erros de Conexão

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Modelo Não Encontrado

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Referência de Variáveis de Ambiente

### Configuração Principal
| Variável | Padrão | Descrição |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Varia | Alias do modelo a ser usado |
| `FOUNDRY_LOCAL_ENDPOINT` | Automático | Substituir endpoint do serviço |
| `SHOW_USAGE` | `0` | Mostrar estatísticas de uso de tokens |
| `RETRY_ON_FAIL` | `1` | Habilitar lógica de repetição |
| `RETRY_BACKOFF` | `1.0` | Atraso inicial para repetição (segundos) |

### Específico da Sessão
| Variável | Padrão | Descrição |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modelo de embeddings |
| `RAG_QUESTION` | Ver exemplo | Pergunta de teste RAG |
| `BENCH_MODELS` | Varia | Modelos separados por vírgula |
| `BENCH_ROUNDS` | `3` | Iterações de benchmark |
| `BENCH_PROMPT` | Ver exemplo | Prompt de benchmark |
| `BENCH_STREAM` | `0` | Medir latência do primeiro token |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelo principal do agente |
| `AGENT_MODEL_EDITOR` | Principal | Modelo editor do agente |
| `SLM_ALIAS` | `phi-4-mini` | Modelo de linguagem pequeno |
| `LLM_ALIAS` | `qwen2.5-7b` | Modelo de linguagem grande |
| `COMPARE_PROMPT` | Ver exemplo | Prompt de comparação |

## Modelos Recomendados

### Desenvolvimento e Testes
- **phi-4-mini** - Qualidade e velocidade equilibradas
- **qwen2.5-0.5b** - Muito rápido para classificação
- **gemma-2-2b** - Boa qualidade, velocidade moderada

### Cenários de Produção
- **phi-4-mini** - Uso geral
- **deepseek-coder-1.3b** - Geração de código
- **qwen2.5-7b** - Respostas de alta qualidade

## Documentação do SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Obtendo Ajuda

1. Verificar status do serviço: `foundry service status`  
2. Ver logs: Checar os logs do serviço Foundry Local  
3. Consultar docs do SDK: https://github.com/microsoft/Foundry-Local  
4. Revisar código de exemplo: Todos os exemplos possuem docstrings detalhados  

## Próximos Passos

1. Complete todas as sessões do workshop na ordem  
2. Experimente diferentes modelos  
3. Modifique os exemplos para seus casos de uso  

---

**Última Atualização**: 08/01/2025  
**Versão do Workshop**: Mais recente  
**SDK**: Foundry Local Python SDK  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->