# Workshop Notebooks - Guia de Resolução de Problemas

## Índice

- [Problemas Comuns e Soluções](../../../../Workshop/notebooks)
- [Problemas Específicos da Sessão 04](../../../../Workshop/notebooks)
- [Problemas Específicos da Sessão 05](../../../../Workshop/notebooks)
- [Problemas Específicos da Sessão 06](../../../../Workshop/notebooks)
- [Problemas Específicos de Hardware](../../../../Workshop/notebooks)
- [Comandos de Diagnóstico](../../../../Workshop/notebooks)
- [Obter Ajuda](../../../../Workshop/notebooks)

---

## Problemas Comuns e Soluções

### 🔴 CUDA Out of Memory

**Mensagem de Erro:**
```
CUDA failure 2: out of memory
```
  
**Causa Raiz:** A GPU não tem VRAM suficiente para carregar o modelo.

**Soluções:**

#### Opção 1: Usar Variantes de CPU (Recomendado)
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
  
#### Opção 4: Aumentar Memória da GPU (se possível)
- Fechar separadores do navegador, editores de vídeo ou outras aplicações que utilizem GPU
- Reduzir os efeitos visuais do Windows
- Usar GPU dedicada se tiver integrada + dedicada

---

### 🔴 APIConnectionError: Connection Error

**Mensagem de Erro:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**Causa Raiz:** O serviço Foundry Local não está em execução ou não está acessível.

**Soluções:**

#### Passo 1: Verificar o Estado do Serviço
```bash
foundry service status
```
  
#### Passo 2: Iniciar o Serviço se Estiver Parado
```bash
foundry service start
```
  
#### Passo 3: Verificar Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### Passo 4: Carregar os Modelos Necessários
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### Passo 5: Reiniciar o Kernel do Notebook  
Depois de iniciar o serviço e carregar os modelos, reinicie o kernel do notebook e execute todas as células novamente.

---

### 🔴 Modelo Não Encontrado no Catálogo

**Mensagem de Erro:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**Causa Raiz:** O modelo não foi descarregado ou carregado no Foundry Local.

**Soluções:**

#### Opção 1: Descarregar e Carregar Modelos
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
  
#### Opção 2: Usar Modo de Seleção Automática  
Atualize o CATALOG para usar nomes base de modelos (sem o sufixo `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
O SDK Foundry Local selecionará automaticamente a melhor variante (CPU, GPU ou NPU) para o seu hardware.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Mensagem de Erro:**
```
HttpResponseError: 500 - Failed loading model
```
  
**Causa Raiz:** O ficheiro do modelo está corrompido ou é incompatível com o hardware.

**Soluções:**

#### Descarregar o Modelo Novamente
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

### � Primeira Solicitação Lenta

**Sintoma:** A primeira conclusão demora mais de 30 segundos, enquanto as solicitações subsequentes são rápidas.

**Causa Raiz:** Este comportamento é normal - o serviço está a carregar o modelo na memória na primeira solicitação.

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

**Problema:** O notebook está a conectar-se à porta errada (55769 vs 59959 vs 57127)

**Solução:**

1. Verifique qual porta o Foundry Local está a usar:
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

### Seleção Errada de Modelo

**Problema:** O notebook mostra gpt-oss-20b ou qwen2.5-7b em vez de qwen2.5-3b

**Solução:**

1. Reinicie o kernel do notebook (limpa o estado antigo das variáveis)
2. Execute novamente a Célula 10 (Definir Aliases de Modelo)
3. Execute novamente a Célula 12 (Exibir Configuração)
4. **Verifique:** A Célula 12 deve mostrar `LLM Model: qwen2.5-3b`

---

### Falha na Célula de Diagnóstico

**Problema:** A Célula 16 mostra "❌ Foundry Local service not found!"

**Solução:**

1. Verifique se o serviço está em execução:
```bash
foundry service status
```
  
2. Teste o endpoint manualmente:
```bash
curl http://localhost:59959/v1/models
```
  
3. Se o curl funcionar mas o notebook não:
   - Reinicie o kernel do notebook
   - Execute novamente as células na ordem: 6, 8, 10, 12, 14, 16

4. Se o curl falhar:
   - Inicie o serviço: `foundry service start`
   - Carregue os modelos: `foundry model run phi-4-mini` e `foundry model run qwen2.5-3b`

---

### Falha na Verificação Prévia

**Problema:** A Célula 20 mostra erros de conexão, embora o diagnóstico tenha passado

**Solução:**

1. Verifique se os modelos estão carregados:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. Se os modelos estiverem em falta:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. Execute novamente a Célula 20 depois de carregar os modelos

---

### Falha na Comparação com Valores None

**Problema:** A Célula 22 conclui, mas mostra latência como None

**Solução:**

1. Verifique se a verificação prévia passou primeiro (Célula 20)
2. Execute novamente a Célula 22 - os modelos podem precisar de aquecer na primeira solicitação
3. Verifique se ambos os modelos estão carregados: `foundry model ls`

---

## Problemas Específicos da Sessão 05

### Agente Usando Modelo Errado

**Problema:** O agente não está a usar o modelo esperado

**Solução:**

Verifique a configuração:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
Reinicie o kernel se os modelos estiverem incorretos.

---

### Overflow de Contexto de Memória

**Problema:** As respostas do agente degradam-se ao longo do tempo

**Solução:** Já tratado automaticamente - os agentes mantêm apenas as últimas 6 mensagens na memória.

---

## Problemas Específicos da Sessão 06

### Confusão entre Modelos de CPU e GPU

**Problema:** Erros CUDA ao usar a configuração padrão

**Solução:** A configuração padrão agora usa modelos de CPU. Se vir erros CUDA:

1. Verifique se está a usar o catálogo padrão de CPU:
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

### Deteção de Intenção Não Funciona

**Problema:** Os prompts estão a ser encaminhados para modelos errados

**Solução:**

Teste a deteção de intenção:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
Atualize as RULES se os padrões precisarem de ajustes.

---

## Problemas Específicos de Hardware

### GPU NVIDIA

**Verificar Estado da GPU:**
```bash
nvidia-smi
```
  
**Problemas Comuns:**
- **Driver desatualizado**: Atualize os drivers NVIDIA
- **Incompatibilidade de versão CUDA**: Reinstale o Foundry Local
- **Memória da GPU fragmentada**: Reinicie o sistema

### NPU Qualcomm

**Verificar Estado da NPU:**
```bash
foundry device info
```
  
**Problemas Comuns:**
- **Drivers da NPU não instalados**: Instale os drivers Qualcomm NPU
- **Variante NPU não disponível**: Use a variante de CPU
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
- Use os modelos mais pequenos
- Reduza max_tokens
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

## Obter Ajuda

### 1. Verificar Logs
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. Problemas no GitHub
- Pesquisar problemas existentes: https://github.com/microsoft/Foundry-Local/issues
- Criar um novo problema com:
  - Mensagem de erro (texto completo)
  - Saída de `foundry service status`
  - Saída de `foundry --version`
  - Informações da GPU/NPU (nvidia-smi, etc.)
  - Passos para reproduzir

### 3. Documentação
- **Repositório Principal**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referência CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Resolução de Problemas**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Lista de Verificação de Correções Rápidas

Quando algo correr mal, tente o seguinte por ordem:

- [ ] Verifique se o serviço está em execução: `foundry service status`
- [ ] Reinicie o serviço: `foundry service stop && foundry service start`
- [ ] Verifique se o modelo existe: `foundry model ls | grep phi-4-mini`
- [ ] Carregue os modelos necessários: `foundry model run phi-4-mini`
- [ ] Verifique a memória da GPU: `nvidia-smi` (se NVIDIA)
- [ ] Experimente a variante de CPU: Use `phi-4-mini-cpu` em vez de `phi-4-mini`
- [ ] Reinicie o kernel do notebook
- [ ] Limpe as saídas do notebook e execute todas as células novamente
- [ ] Reinstale o SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Reinicie o sistema (último recurso)

---

## Dicas de Prevenção

### Melhores Práticas

1. **Verifique sempre o serviço primeiro:**
   ```bash
   foundry service status
   ```
  
2. **Use variantes de CPU por padrão:**
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
   - Deixe-o em execução em segundo plano entre sessões

5. **Monitore os recursos:**
   - Verifique a memória da GPU antes de executar
   - Feche aplicações desnecessárias que utilizem GPU
   - Use o Gestor de Tarefas / nvidia-smi

6. **Atualize regularmente:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**Última Atualização:** 8 de outubro de 2025

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.