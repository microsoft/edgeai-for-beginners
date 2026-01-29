# Exemplo 01: Chat Rápido com OpenAI SDK

Um exemplo simples de chat que demonstra como usar o OpenAI SDK com o Microsoft Foundry Local para inferência de IA local.

## Visão Geral

Este exemplo mostra como:
- Usar o OpenAI Python SDK com Foundry Local
- Lidar com configurações tanto do Azure OpenAI quanto do Foundry Local
- Implementar tratamento de erros adequado e estratégias de fallback
- Utilizar o FoundryLocalManager para gerenciamento de serviços

## Pré-requisitos

- **Foundry Local**: Instalado e disponível no PATH
- **Python**: Versão 3.8 ou superior
- **Modelo**: Um modelo carregado no Foundry Local (por exemplo, `phi-4-mini`)

## Instalação

1. **Configurar o ambiente Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalar dependências:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Iniciar o serviço Foundry Local e carregar um modelo:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Uso

### Foundry Local (Padrão)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Funcionalidades do Código

### Integração com FoundryLocalManager

O exemplo utiliza o SDK oficial do Foundry Local para gerenciamento adequado de serviços:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Tratamento de Erros

Tratamento robusto de erros com fallback para configuração manual:
- Descoberta automática de serviços
- Degradação graciosa caso o SDK não esteja disponível
- Mensagens de erro claras para solução de problemas

## Variáveis de Ambiente

| Variável | Descrição | Padrão | Obrigatório |
|----------|-------------|---------|----------|
| `MODEL` | Alias ou nome do modelo | `phi-4-mini` | Não |
| `BASE_URL` | URL base do Foundry Local | `http://localhost:8000` | Não |
| `API_KEY` | Chave de API (geralmente não necessária para local) | `""` | Não |
| `AZURE_OPENAI_ENDPOINT` | Endpoint do Azure OpenAI | - | Para Azure |
| `AZURE_OPENAI_API_KEY` | Chave de API do Azure OpenAI | - | Para Azure |
| `AZURE_OPENAI_API_VERSION` | Versão da API do Azure | `2024-08-01-preview` | Não |

## Solução de Problemas

### Problemas Comuns

1. **Aviso "Não foi possível usar o Foundry SDK":**
   - Instale o foundry-local-sdk: `pip install foundry-local-sdk`
   - Ou configure as variáveis de ambiente manualmente

2. **Conexão recusada:**
   - Certifique-se de que o Foundry Local está em execução: `foundry service status`
   - Verifique se um modelo está carregado: `foundry service ps`

3. **Modelo não encontrado:**
   - Liste os modelos disponíveis: `foundry model list`
   - Carregue um modelo: `foundry model run phi-4-mini`

### Verificação

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Referências

- [Documentação do Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local no GitHub](https://github.com/microsoft/Foundry-Local)
- [Referência de API compatível com OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

