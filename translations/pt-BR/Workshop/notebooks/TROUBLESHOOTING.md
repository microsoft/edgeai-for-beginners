# Cadernos do Workshop - Guia de Solução de Problemas

## Índice

- [Problemas Comuns e Soluções](../../../../Workshop/notebooks)
- [Problemas Específicos da Sessão 04](../../../../Workshop/notebooks)
- [Problemas Específicos da Sessão 05](../../../../Workshop/notebooks)
- [Problemas Específicos da Sessão 06](../../../../Workshop/notebooks)
- [Problemas Específicos de Hardware](../../../../Workshop/notebooks)
- [Comandos de Diagnóstico](../../../../Workshop/notebooks)
- [Obtendo Ajuda](../../../../Workshop/notebooks)

---

## Problemas Comuns e Soluções

### 🔴 CUDA Out of Memory

**Mensagem de Erro:**
```
CUDA failure 2: out of memory
```

**Causa Raiz:** A GPU não tem memória VRAM suficiente para carregar o modelo.

**Soluções:**

#### Opção 1: Usar Variantes para CPU (Recomendado)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opção 2: Usar Modelos Menores na GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opção 3: Limpar Memória da GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opção 4: Aumentar a Memória da GPU (se possível)
- Feche abas do navegador, editores de vídeo ou outros aplicativos que usam GPU
- Reduza os efeitos visuais do Windows
- Use a GPU dedicada se tiver integrada + dedicada

---

### 🔴 APIConnectionError: Connection Error

**Mensagem de Erro:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Causa Raiz:** O serviço Foundry Local não está em execução ou não é acessível.

**Soluções:**

#### Etapa 1: Verificar o Status do Serviço
```bash
foundry service status
```

#### Etapa 2: Iniciar o Serviço se Estiver Parado
```bash
foundry service start
```

#### Etapa 3: Verificar o Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Etapa 4: Carregar os Modelos Necessários
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Etapa 5: Reiniciar o Kernel do Notebook
Após iniciar o serviço e carregar os modelos, reinicie o kernel do notebook e execute todas as células novamente.

---

### 🔴 Modelo Não Encontrado no Catálogo

**Mensagem de Erro:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Causa Raiz:** O modelo não foi baixado ou carregado no Foundry Local.

**Soluções:**

#### Opção 1: Baixar e Carregar Modelos
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Opção 2: Usar o Modo de Seleção Automática
Atualize seu CATALOGO para usar os nomes base dos modelos (sem o sufixo `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

O SDK do Foundry Local selecionará automaticamente a melhor variante (CPU, GPU ou NPU) para o seu hardware.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Mensagem de Erro:**
```
HttpResponseError: 500 - Failed loading model
```

**Causa Raiz:** O arquivo do modelo está corrompido ou é incompatível com o hardware.

**Soluções:**

#### Baixar o Modelo Novamente
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Usar uma Variante Diferente
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Mensagem de Erro:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Causa Raiz:** O pacote foundry-local-sdk não está instalado.

**Soluções:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Solicitação Inicial Lenta

**Sintoma:** A primeira execução leva mais de 30 segundos, enquanto as solicitações subsequentes são rápidas.

**Causa Raiz:** Isso é um comportamento normal - o serviço está carregando o modelo na memória na primeira solicitação.

**Soluções:**

#### Pré-carregar Modelos
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Manter o Serviço em Execução
```bash
# Start service manually and leave it running
foundry service start
```

---

## Problemas Específicos da Sessão 04

### Configuração de Porta Errada

**Problema:** O notebook está conectando à porta errada (55769 vs 59959 vs 57127)

**Solução:**

1. Verifique qual porta o Foundry Local está usando:
```bash
foundry service status
# Note the port number displayed
```

2. Atualize a Célula 10 no notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Reinicie o kernel e execute novamente as células 6, 8, 10, 12, 16, 20, 22

---

### Seleção de Modelo Errada

**Problema:** O notebook está exibindo gpt-oss-20b ou qwen2.5-7b em vez de qwen2.5-3b

**Solução:**

1. Reinicie o kernel do notebook (limpa o estado antigo das variáveis)
2. Execute novamente a Célula 10 (Definir Aliases de Modelos)
3. Execute novamente a Célula 12 (Exibir Configuração)
4. **Verifique:** A Célula 12 deve exibir `LLM Model: qwen2.5-3b`

---

### Célula de Diagnóstico Falha

**Problema:** A Célula 16 exibe "❌ Foundry Local service not found!"

**Solução:**

1. Verifique se o serviço está em execução:
```bash
foundry service status
```

2. Teste o endpoint manualmente:
```bash
curl http://localhost:59959/v1/models
```

3. Se o curl funcionar, mas o notebook não:
   - Reinicie o kernel do notebook
   - Execute as células na ordem: 6, 8, 10, 12, 14, 16

4. Se o curl falhar:
   - Inicie o serviço: `foundry service start`
   - Carregue os modelos: `foundry model run phi-4-mini` e `foundry model run qwen2.5-3b`

---

### Verificação Prévia Falha

**Problema:** A Célula 20 exibe erros de conexão, mesmo que o diagnóstico tenha passado

**Solução:**

1. Verifique se os modelos estão carregados:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Se os modelos estiverem ausentes:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Execute novamente a Célula 20 após carregar os modelos

---

### Comparação Falha com Valores None

**Problema:** A Célula 22 é concluída, mas exibe a latência como None

**Solução:**

1. Verifique se a verificação prévia foi concluída primeiro (Célula 20)
2. Execute novamente a Célula 22 - os modelos podem precisar ser aquecidos na primeira solicitação
3. Verifique se ambos os modelos estão carregados: `foundry model ls`

---

## Problemas Específicos da Sessão 05

### Agente Usando Modelo Errado

**Problema:** O agente não está usando o modelo esperado

**Solução:**

Verifique a configuração:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Reinicie o kernel se os modelos estiverem incorretos.

---

### Estouro de Contexto de Memória

**Problema:** As respostas do agente estão degradando com o tempo

**Solução:** Já tratado automaticamente - os agentes mantêm apenas as últimas 6 mensagens na memória.

---

## Problemas Específicos da Sessão 06

### Confusão entre Modelos para CPU e GPU

**Problema:** Erros de CUDA ao usar a configuração padrão

**Solução:** A configuração padrão agora usa modelos para CPU. Se você encontrar erros de CUDA:

1. Verifique se está usando o catálogo padrão para CPU:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Reinicie o kernel e execute todas as células novamente

---

### Detecção de Intenção Não Funciona

**Problema:** Os prompts estão sendo direcionados para os modelos errados

**Solução:**

Teste a detecção de intenção:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Atualize as REGRAS se os padrões precisarem de ajustes.

---

## Problemas Específicos de Hardware

### GPU NVIDIA

**Verificar Status da GPU:**
```bash
nvidia-smi
```

**Problemas Comuns:**
- **Driver desatualizado**: Atualize os drivers da NVIDIA
- **Incompatibilidade de versão do CUDA**: Reinstale o Foundry Local
- **Memória da GPU fragmentada**: Reinicie o sistema

### NPU Qualcomm

**Verificar Status da NPU:**
```bash
foundry device info
```

**Problemas Comuns:**
- **Drivers da NPU não instalados**: Instale os drivers da NPU Qualcomm
- **Variante para NPU não disponível**: Use a variante para CPU
- **Versão do Windows muito antiga**: Atualize para o Windows 11 mais recente

### Sistemas Apenas com CPU

**Modelos Recomendados:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Dicas de Desempenho:**
- Use os modelos menores
- Reduza o max_tokens
- Tenha paciência para a primeira solicitação

---

## Comandos de Diagnóstico

### Verificar Tudo
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Em Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Obtendo Ajuda

### 1. Verifique os Logs
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Problemas no GitHub
- Pesquise problemas existentes: https://github.com/microsoft/Foundry-Local/issues
- Crie um novo problema com:
  - Mensagem de erro (texto completo)
  - Saída de `foundry service status`
  - Saída de `foundry --version`
  - Informações sobre GPU/NPU (nvidia-smi, etc.)
  - Passos para reproduzir

### 3. Documentação
- **Repositório Principal**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referência CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Solução de Problemas**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Lista de Verificação de Correções Rápidas

Quando algo der errado, tente estas etapas na ordem:

- [ ] Verifique se o serviço está em execução: `foundry service status`
- [ ] Reinicie o serviço: `foundry service stop && foundry service start`
- [ ] Verifique se o modelo existe: `foundry model ls | grep phi-4-mini`
- [ ] Carregue os modelos necessários: `foundry model run phi-4-mini`
- [ ] Verifique a memória da GPU: `nvidia-smi` (se for NVIDIA)
- [ ] Tente a variante para CPU: Use `phi-4-mini-cpu` em vez de `phi-4-mini`
- [ ] Reinicie o kernel do notebook
- [ ] Limpe as saídas do notebook e execute todas as células novamente
- [ ] Reinstale o SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Reinicie o sistema (último recurso)

---

## Dicas de Prevenção

### Melhores Práticas

1. **Sempre verifique o serviço primeiro:**
   ```bash
   foundry service status
   ```

2. **Use variantes para CPU por padrão:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Pré-carregue os modelos antes de executar os notebooks:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Mantenha o serviço em execução:**
   - Não pare/inicie o serviço desnecessariamente
   - Deixe-o rodando em segundo plano entre as sessões

5. **Monitore os recursos:**
   - Verifique a memória da GPU antes de executar
   - Feche aplicativos desnecessários que usam GPU
   - Use o Gerenciador de Tarefas / nvidia-smi

6. **Atualize regularmente:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Última Atualização:** 8 de outubro de 2025

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.