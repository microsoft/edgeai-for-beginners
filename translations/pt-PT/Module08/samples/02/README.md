# Exemplo 02: Integração com o SDK OpenAI

Demonstra integração avançada com o SDK OpenAI em Python, suportando tanto o Microsoft Foundry Local como o Azure OpenAI, com respostas em streaming e tratamento adequado de erros.

## Visão Geral

Este exemplo demonstra:
- Alternância fluida entre Foundry Local e Azure OpenAI
- Respostas em streaming para uma melhor experiência do utilizador
- Uso adequado do SDK FoundryLocalManager
- Mecanismos robustos de tratamento de erros e fallback
- Padrões de código prontos para produção

## Pré-requisitos

- **Foundry Local**: Instalado e em execução (para inferência local)
- **Python**: Versão 3.8 ou superior com o SDK OpenAI
- **Azure OpenAI**: Endpoint válido e chave API (para inferência na cloud)

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

3. **Iniciar Foundry Local (para modo local):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Cenários de Utilização

### Foundry Local (Padrão)

**Opção 1: Usar FoundryLocalManager (Recomendado)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opção 2: Configuração Manual**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Arquitetura do Código

### Padrão de Fábrica de Clientes

O exemplo utiliza um padrão de fábrica para criar os clientes apropriados:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Respostas em Streaming

O exemplo demonstra streaming para geração de respostas em tempo real:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Variáveis de Ambiente

### Configuração do Foundry Local

| Variável | Descrição | Padrão | Obrigatório |
|----------|-------------|---------|----------|
| `MODEL` | Alias do modelo a utilizar | `phi-4-mini` | Não |
| `BASE_URL` | Endpoint do Foundry Local | `http://localhost:8000` | Não |
| `API_KEY` | Chave API (opcional para local) | `""` | Não |

### Configuração do Azure OpenAI

| Variável | Descrição | Padrão | Obrigatório |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint do recurso Azure OpenAI | - | Sim |
| `AZURE_OPENAI_API_KEY` | Chave API do Azure OpenAI | - | Sim |
| `AZURE_OPENAI_API_VERSION` | Versão da API | `2024-08-01-preview` | Não |
| `MODEL` | Nome da implementação no Azure | `your-deployment-name` | Sim |

## Funcionalidades Avançadas

### Descoberta Automática de Serviços

O exemplo deteta automaticamente o serviço apropriado com base nas variáveis de ambiente:

1. **Modo Azure**: Se `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_API_KEY` estiverem configurados
2. **Modo SDK Foundry**: Se o SDK Foundry Local estiver disponível
3. **Modo Manual**: Fallback para configuração manual

### Tratamento de Erros

- Fallback suave do SDK para configuração manual
- Mensagens de erro claras para resolução de problemas
- Tratamento adequado de exceções para problemas de rede
- Validação das variáveis de ambiente obrigatórias

## Considerações de Desempenho

### Comparação entre Local e Cloud

**Vantagens do Foundry Local:**
- ✅ Sem custos de API
- ✅ Privacidade de dados (os dados não saem do dispositivo)
- ✅ Baixa latência para modelos suportados
- ✅ Funciona offline

**Vantagens do Azure OpenAI:**
- ✅ Acesso aos modelos grandes mais recentes
- ✅ Maior capacidade de processamento
- ✅ Sem necessidade de recursos locais
- ✅ SLA de nível empresarial

## Resolução de Problemas

### Problemas Comuns

1. **Aviso "Não foi possível usar o SDK Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Erros de autenticação no Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modelo não disponível:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Verificações de Saúde

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Próximos Passos

- **Exemplo 03**: Descoberta e benchmarking de modelos
- **Exemplo 04**: Construção de uma aplicação Chainlit RAG
- **Exemplo 05**: Orquestração multi-agente
- **Exemplo 06**: Roteamento de modelos como ferramentas

## Referências

- [Documentação do Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referência do SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Documentação do SDK OpenAI em Python](https://github.com/openai/openai-python)
- [Guia de Respostas em Streaming](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

