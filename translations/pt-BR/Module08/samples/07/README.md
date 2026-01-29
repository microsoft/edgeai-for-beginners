# Exemplo de Foundry Local como API

Este exemplo demonstra como usar o Microsoft Foundry Local como um serviço de API REST sem depender do SDK OpenAI. Ele mostra padrões de integração HTTP direta para máximo controle e personalização.

## Visão Geral

Baseado nos padrões oficiais do Microsoft Foundry Local, este exemplo fornece:
- Integração direta com API REST usando FoundryLocalManager
- Implementação personalizada de cliente HTTP
- Gerenciamento de modelos e monitoramento de saúde
- Manipulação de respostas em streaming e não-streaming
- Tratamento de erros e lógica de repetição pronta para produção

## Pré-requisitos

1. **Instalação do Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Dependências do Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arquitetura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Principais Funcionalidades

### 1. **Integração HTTP Direta**
- Chamadas puras à API REST sem dependências de SDK
- Autenticação e cabeçalhos personalizados
- Controle total sobre o tratamento de requisições/respostas

### 2. **Gerenciamento de Modelos**
- Carregamento e descarregamento dinâmico de modelos
- Monitoramento de saúde e verificações de status
- Coleta de métricas de desempenho

### 3. **Padrões de Produção**
- Mecanismos de repetição com backoff exponencial
- Circuit breaker para tolerância a falhas
- Registro e monitoramento abrangentes

### 4. **Manipulação Flexível de Respostas**
- Respostas em streaming para aplicações em tempo real
- Processamento em lote para cenários de alta demanda
- Análise e validação personalizada de respostas

## Exemplos de Uso

### Integração Básica com API
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Integração com Streaming
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Monitoramento de Saúde
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Estrutura de Arquivos

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Integração com Microsoft Foundry Local

Este exemplo segue os padrões oficiais da Microsoft:

1. **Integração com SDK**: Usa `FoundryLocalManager` para gerenciamento de serviços
2. **Endpoints REST**: Chamadas diretas para `/v1/chat/completions` e outros endpoints
3. **Autenticação**: Manipulação adequada de chaves de API para serviços locais
4. **Gerenciamento de Modelos**: Listagem de catálogo, download e padrões de carregamento
5. **Tratamento de Erros**: Códigos de erro e respostas recomendados pela Microsoft

## Primeiros Passos

1. **Instalar Dependências**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar Exemplo Básico**
   ```bash
   python examples/basic_usage.py
   ```

3. **Testar Streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Configuração para Produção**
   ```bash
   python examples/production.py
   ```

## Configuração

Variáveis de ambiente para personalização:
- `FOUNDRY_MODEL`: Modelo padrão a ser usado (padrão: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Tempo limite de requisição em segundos (padrão: 30)
- `FOUNDRY_RETRIES`: Número de tentativas de repetição (padrão: 3)
- `FOUNDRY_LOG_LEVEL`: Nível de registro (padrão: "INFO")

## Melhores Práticas

1. **Gerenciamento de Conexões**: Reutilizar conexões HTTP para melhor desempenho
2. **Tratamento de Erros**: Implementar lógica de repetição adequada com backoff exponencial
3. **Monitoramento de Recursos**: Acompanhar o uso de memória e desempenho do modelo
4. **Segurança**: Usar autenticação adequada mesmo para serviços locais
5. **Testes**: Incluir testes unitários e de integração

## Solução de Problemas

### Problemas Comuns

**Serviço Não Está Funcionando**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemas de Carregamento de Modelos**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Erros de Conexão**
- Verifique se o Foundry Local está rodando na porta correta
- Cheque as configurações de firewall
- Certifique-se de que os cabeçalhos de autenticação estão corretos

## Otimização de Desempenho

1. **Pooling de Conexões**: Usar objetos de sessão para múltiplas requisições
2. **Operações Assíncronas**: Aproveitar asyncio para requisições concorrentes
3. **Cache**: Cache de respostas de modelos onde for apropriado
4. **Monitoramento**: Acompanhar tempos de resposta e ajustar limites de tempo

## Resultados de Aprendizado

Após completar este exemplo, você entenderá:
- Integração direta com API REST do Foundry Local
- Padrões de implementação de cliente HTTP personalizado
- Tratamento de erros e monitoramento prontos para produção
- Arquitetura de serviços do Microsoft Foundry Local
- Técnicas de otimização de desempenho para serviços de IA locais

## Próximos Passos

- Explore o Exemplo 08: Aplicativo de Chat no Windows 11
- Experimente o Exemplo 09: Orquestração Multi-Agente
- Aprenda com o Exemplo 10: Foundry Local como Integração de Ferramentas

---

