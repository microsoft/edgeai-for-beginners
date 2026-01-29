# Guião Rápido - Cadernos de Trabalho

## Índice

- [Pré-requisitos](../../../../Workshop/notebooks)
- [Configuração Inicial](../../../../Workshop/notebooks)
- [Sessão 04: Comparação de Modelos](../../../../Workshop/notebooks)
- [Sessão 05: Orquestrador Multi-Agente](../../../../Workshop/notebooks)
- [Sessão 06: Encaminhamento Baseado em Intenções](../../../../Workshop/notebooks)
- [Variáveis de Ambiente](../../../../Workshop/notebooks)
- [Comandos Comuns](../../../../Workshop/notebooks)

---

## Pré-requisitos

### 1. Instalar o Foundry Local

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

**Necessário antes de executar qualquer caderno:**

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

### Transferir e Carregar Modelos

Os cadernos utilizam os seguintes modelos por padrão:

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

### Objetivo
Comparar o desempenho entre Modelos de Linguagem Pequenos (SLM) e Modelos de Linguagem Grandes (LLM).

### Configuração Rápida

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Executar o Caderno

1. **Abrir** `session04_model_compare.ipynb` no VS Code ou Jupyter
2. **Reiniciar o kernel** (Kernel → Reiniciar Kernel)
3. **Executar todas as células** na ordem

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
- [ ] A célula 16 passa no diagnóstico (✅ Serviço em execução)
- [ ] A célula 20 passa na verificação prévia (ambos os modelos ok)
- [ ] A célula 22 conclui a comparação com valores de latência
- [ ] A célula 24 validação mostra 🎉 TODOS OS TESTES PASSARAM!

### Estimativa de Tempo
- **Primeira execução:** 5-10 minutos (incluindo transferências de modelos)
- **Execuções subsequentes:** 1-2 minutos

---

## Sessão 05: Orquestrador Multi-Agente

### Objetivo
Demonstrar a colaboração multi-agente utilizando o Foundry Local SDK - agentes trabalham juntos para produzir resultados refinados.

### Configuração Rápida

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Executar o Caderno

1. **Abrir** `session05_agents_orchestrator.ipynb`
2. **Reiniciar o kernel**
3. **Executar todas as células** na ordem

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

## Sessão 06: Encaminhamento Baseado em Intenções

### Objetivo
Encaminhar inteligentemente prompts para modelos especializados com base na intenção detetada.

### Configuração Rápida

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Nota:** A Sessão 06 utiliza modelos CPU por padrão para máxima compatibilidade.

### Executar o Caderno

1. **Abrir** `session06_models_router.ipynb`
2. **Reiniciar o kernel**
3. **Executar todas as células** na ordem

### Configuração Principal

**Catálogo Padrão (Modelos CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (Modelos GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Deteção de Intenções

O roteador utiliza padrões regex para detetar intenções:

| Intenção | Exemplos de Padrões | Encaminhado Para |
|----------|---------------------|------------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Tudo o resto | phi-4-mini-cpu |

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

**Ativar rastreamento de tokens:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Alterar para Modelos GPU

Se tiver 8GB+ de VRAM:

1. Na **Célula #6**, comente o catálogo CPU
2. Descomente o catálogo GPU
3. Carregue os modelos GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Reinicie o kernel e reexecute o caderno

### Estimativa de Tempo
- **Primeira execução:** 5-10 minutos (carregamento de modelos)
- **Execuções subsequentes:** 30-60 segundos por teste

---

## Variáveis de Ambiente

### Configuração Global

Definir antes de iniciar o Jupyter/VS Code:

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

### Configuração no Caderno

Definir no início de qualquer caderno:

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

### Gestão de Serviços

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

### Gestão de Modelos

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

### Testar Endpoints

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

## Boas Práticas

### Antes de Iniciar Qualquer Caderno

1. **Verifique se o serviço está em execução:**
   ```bash
   foundry service status
   ```

2. **Verifique se os modelos estão carregados:**
   ```bash
   foundry model ls
   ```

3. **Reinicie o kernel do caderno** se for reexecutar

4. **Limpe todas as saídas** para uma execução limpa

### Gestão de Recursos

1. **Utilize modelos CPU por padrão** para compatibilidade
2. **Altere para modelos GPU** apenas se tiver 8GB+ de VRAM
3. **Feche outras aplicações GPU** antes de executar
4. **Mantenha o serviço em execução** entre sessões de cadernos
5. **Monitore o uso de recursos** com o Gestor de Tarefas / nvidia-smi

### Resolução de Problemas

1. **Verifique sempre o serviço primeiro** antes de depurar o código
2. **Reinicie o kernel** se vir configurações desatualizadas
3. **Reexecute as células de diagnóstico** após quaisquer alterações
4. **Verifique se os nomes dos modelos** correspondem aos carregados
5. **Confirme se a porta do endpoint** corresponde ao estado do serviço

---

## Referência Rápida: Aliases de Modelos

### Modelos Comuns

| Alias | Tamanho | Melhor Para | RAM/VRAM | Variantes |
|-------|---------|-------------|----------|-----------|
| `phi-4-mini` | ~4B | Chat geral, sumarização | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Geração de código, refatoração | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Tarefas gerais, eficiente | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Rápido, poucos recursos | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Classificação, poucos recursos | 1-2GB | `-cpu`, `-cuda-gpu` |

### Nomeação de Variantes

- **Nome base** (ex.: `phi-4-mini`): Seleciona automaticamente a melhor variante para o seu hardware
- **`-cpu`**: Otimizado para CPU, funciona em qualquer lugar
- **`-cuda-gpu`**: Otimizado para GPU NVIDIA, requer 8GB+ de VRAM
- **`-npu`**: Otimizado para NPU Qualcomm, requer drivers NPU

**Recomendação:** Utilize nomes base (sem sufixo) e deixe o Foundry Local selecionar automaticamente a melhor variante.

---

## Indicadores de Sucesso

Está pronto quando vir:

✅ `foundry service status` mostra "running"  
✅ `foundry model ls` mostra os modelos necessários  
✅ Serviço acessível no endpoint correto  
✅ Verificação de saúde retorna 200 OK  
✅ Células de diagnóstico do caderno passam  
✅ Sem erros de conexão na saída  

---

## Obter Ajuda

### Documentação
- **Repositório Principal**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Referência CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **Resolução de Problemas**: Consulte `troubleshooting.md` neste diretório  

### Problemas no GitHub
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**Última Atualização:** 8 de outubro de 2025  
**Versão:** Workshop Notebooks 2.0

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.