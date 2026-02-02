# Guias Rápidos dos Notebooks do Workshop

## Índice

- [Pré-requisitos](../../../../Workshop/notebooks)
- [Configuração Inicial](../../../../Workshop/notebooks)
- [Sessão 04: Comparação de Modelos](../../../../Workshop/notebooks)
- [Sessão 05: Orquestrador Multi-Agente](../../../../Workshop/notebooks)
- [Sessão 06: Roteamento Baseado em Intenção](../../../../Workshop/notebooks)
- [Variáveis de Ambiente](../../../../Workshop/notebooks)
- [Comandos Comuns](../../../../Workshop/notebooks)

---

## Pré-requisitos

### 1. Instalar Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificar Instalação:**
```bash
foundry --version
```

### 2. Instalar Dependências do Python

```bash
cd Workshop
pip install -r requirements.txt
```

Ou instale individualmente:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Configuração Inicial

### Iniciar o Serviço Foundry Local

**Necessário antes de executar qualquer notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Saída esperada:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Baixar e Carregar Modelos

Os notebooks utilizam estes modelos por padrão:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Verificar Configuração

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sessão 04: Comparação de Modelos

### Propósito
Comparar o desempenho entre Modelos de Linguagem Pequenos (SLM) e Modelos de Linguagem Grandes (LLM).

### Configuração Rápida

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Executando o Notebook

1. **Abra** `session04_model_compare.ipynb` no VS Code ou Jupyter
2. **Reinicie o kernel** (Kernel → Reiniciar Kernel)
3. **Execute todas as células** na ordem

### Configuração Principal

**Modelos Padrão:**
- **SLM:** `phi-4-mini` (~4GB RAM, mais rápido)
- **LLM:** `qwen2.5-3b` (~3GB RAM, otimizado para memória)

**Variáveis de Ambiente (opcional):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Saída Esperada

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Personalização

**Usar modelos diferentes:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt personalizado:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Lista de Verificação de Validação

- [ ] A célula 12 mostra os modelos corretos (phi-4-mini, qwen2.5-3b)
- [ ] A célula 12 mostra o endpoint correto (porta 59959)
- [ ] Diagnóstico da célula 16 passa (✅ Serviço está em execução)
- [ ] Verificação prévia da célula 20 passa (ambos os modelos ok)
- [ ] Comparação da célula 22 completa com valores de latência
- [ ] Validação da célula 24 mostra 🎉 TODOS OS TESTES PASSARAM!

### Estimativa de Tempo
- **Primeira execução:** 5-10 minutos (incluindo downloads de modelos)
- **Execuções subsequentes:** 1-2 minutos

---

## Sessão 05: Orquestrador Multi-Agente

### Propósito
Demonstrar colaboração multi-agente usando o SDK Foundry Local - agentes trabalham juntos para produzir resultados refinados.

### Configuração Rápida

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Executando o Notebook

1. **Abra** `session05_agents_orchestrator.ipynb`
2. **Reinicie o kernel**
3. **Execute todas as células** na ordem

### Configuração Principal

**Configuração Padrão (Mesmo Modelo para Ambos os Agentes):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Configuração Avançada (Modelos Diferentes):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Arquitetura

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Saída Esperada

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Extensões

**Adicionar mais agentes:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Testes em lote:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Estimativa de Tempo
- **Primeira execução:** 3-5 minutos
- **Execuções subsequentes:** 1-2 minutos por pergunta

---

## Sessão 06: Roteamento Baseado em Intenção

### Propósito
Roteamento inteligente de prompts para modelos especializados com base na intenção detectada.

### Configuração Rápida

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Nota:** A Sessão 06 utiliza modelos de CPU por padrão para máxima compatibilidade.

### Executando o Notebook

1. **Abra** `session06_models_router.ipynb`
2. **Reinicie o kernel**
3. **Execute todas as células** na ordem

### Configuração Principal

**Catálogo Padrão (Modelos de CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (Modelos de GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Detecção de Intenção

O roteador utiliza padrões regex para detectar intenções:

| Intenção         | Exemplos de Padrões         | Roteado Para          |
|------------------|-----------------------------|-----------------------|
| `code`          | "refatorar", "implementar função" | phi-3.5-mini-cpu     |
| `classification`| "categorizar", "classificar isso" | qwen2.5-0.5b-cpu     |
| `summarize`     | "resumir", "tl;dr"          | phi-4-mini-cpu        |
| `general`       | Todo o resto                | phi-4-mini-cpu        |

### Saída Esperada

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Personalização

**Adicionar intenção personalizada:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Habilitar rastreamento de tokens:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Alternando para Modelos de GPU

Se você tiver 8GB+ de VRAM:

1. Na **Célula #6**, comente o catálogo de CPU
2. Descomente o catálogo de GPU
3. Carregue os modelos de GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Reinicie o kernel e reexecute o notebook

### Estimativa de Tempo
- **Primeira execução:** 5-10 minutos (carregamento de modelos)
- **Execuções subsequentes:** 30-60 segundos por teste

---

## Variáveis de Ambiente

### Configuração Global

Defina antes de iniciar o Jupyter/VS Code:

**Windows (Prompt de Comando):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Configuração no Notebook

Defina no início de qualquer notebook:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Comandos Comuns

### Gerenciamento de Serviço

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Gerenciamento de Modelos

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Testando Endpoints

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Comandos de Diagnóstico

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Melhores Práticas

### Antes de Iniciar Qualquer Notebook

1. **Verifique se o serviço está em execução:**
   ```bash
   foundry service status
   ```

2. **Confirme se os modelos estão carregados:**
   ```bash
   foundry model ls
   ```

3. **Reinicie o kernel do notebook** se estiver reexecutando

4. **Limpe todos os outputs** para uma execução limpa

### Gerenciamento de Recursos

1. **Use modelos de CPU por padrão** para compatibilidade
2. **Troque para modelos de GPU** apenas se tiver 8GB+ de VRAM
3. **Feche outros aplicativos de GPU** antes de executar
4. **Mantenha o serviço em execução** entre sessões de notebook
5. **Monitore o uso de recursos** com Gerenciador de Tarefas / nvidia-smi

### Solução de Problemas

1. **Sempre verifique o serviço primeiro** antes de depurar o código
2. **Reinicie o kernel** se você vir configurações antigas
3. **Reexecute células de diagnóstico** após qualquer alteração
4. **Verifique se os nomes dos modelos** correspondem aos carregados
5. **Confirme se a porta do endpoint** corresponde ao status do serviço

---

## Referência Rápida: Apelidos de Modelos

### Modelos Comuns

| Apelido         | Tamanho | Melhor Para               | RAM/VRAM | Variantes              |
|-----------------|---------|--------------------------|----------|-----------------------|
| `phi-4-mini`   | ~4B     | Chat geral, sumarização  | 4-6GB    | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B   | Geração de código        | 3-5GB    | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b`   | ~3B     | Tarefas gerais, eficiente| 3-4GB    | `-cpu`, `-cuda-gpu`         |
| `qwen2.5-1.5b` | ~1.5B   | Rápido, poucos recursos  | 2-3GB    | `-cpu`, `-cuda-gpu`         |
| `qwen2.5-0.5b` | ~0.5B   | Classificação, mínimo recurso | 1-2GB | `-cpu`, `-cuda-gpu`         |

### Nomeação de Variantes

- **Nome base** (ex.: `phi-4-mini`): Seleciona automaticamente a melhor variante para seu hardware
- **`-cpu`**: Otimizado para CPU, funciona em qualquer lugar
- **`-cuda-gpu`**: Otimizado para GPU NVIDIA, requer 8GB+ de VRAM
- **`-npu`**: Otimizado para NPU Qualcomm, requer drivers NPU

**Recomendação:** Use nomes base (sem sufixo) e deixe o Foundry Local selecionar automaticamente a melhor variante.

---

## Indicadores de Sucesso

Você está pronto quando:

✅ `foundry service status` mostra "running"  
✅ `foundry model ls` mostra os modelos necessários  
✅ Serviço acessível no endpoint correto  
✅ Verificação de saúde retorna 200 OK  
✅ Células de diagnóstico do notebook passam  
✅ Sem erros de conexão na saída  

---

## Obtendo Ajuda

### Documentação
- **Repositório Principal**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referência CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Solução de Problemas**: Veja `troubleshooting.md` neste diretório

### Problemas no GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Última Atualização:** 8 de outubro de 2025  
**Versão:** Workshop Notebooks 2.0

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.