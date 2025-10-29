<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:33:01+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "pt"
}
-->
# Notas de Migração do SDK Local Foundry

## Visão Geral

Todos os ficheiros Python na pasta Workshop foram atualizados para seguir os padrões mais recentes do [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Resumo das Alterações

### Infraestrutura Principal (`workshop_utils.py`)

#### Funcionalidades Melhoradas:
- **Suporte para Substituição de Endpoint**: Adicionado suporte à variável de ambiente `FOUNDRY_LOCAL_ENDPOINT`
- **Melhoria no Tratamento de Erros**: Tratamento de exceções aprimorado com mensagens de erro detalhadas
- **Cache Aprimorado**: As chaves de cache agora incluem o endpoint para cenários com múltiplos endpoints
- **Backoff Exponencial**: A lógica de repetição agora utiliza backoff exponencial para maior confiabilidade
- **Anotações de Tipo**: Adicionadas dicas de tipo abrangentes para melhor suporte em IDEs

#### Novas Capacidades:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Aplicações de Exemplo

#### Sessão 01: Inicialização de Chat (`chat_bootstrap.py`)
- Modelo padrão atualizado de `phi-3.5-mini` para `phi-4-mini`
- Adicionado suporte para substituição de endpoint
- Documentação aprimorada com referências ao SDK

#### Sessão 02: Pipeline RAG (`rag_pipeline.py`)
- Atualizado para usar `phi-4-mini` como padrão
- Adicionado suporte para substituição de endpoint
- Documentação melhorada com detalhes sobre variáveis de ambiente

#### Sessão 02: Avaliação RAG (`rag_eval_ragas.py`)
- Atualizados os modelos padrão
- Adicionada configuração de endpoint
- Tratamento de erros aprimorado

#### Sessão 03: Benchmarking (`benchmark_oss_models.py`)
- Lista de modelos padrão atualizada para incluir `phi-4-mini`
- Documentação abrangente sobre variáveis de ambiente adicionada
- Documentação de funções melhorada
- Suporte para substituição de endpoint adicionado

#### Sessão 04: Comparação de Modelos (`model_compare.py`)
- LLM padrão atualizado de `gpt-oss-20b` para `qwen2.5-7b`
- Configuração de endpoint adicionada
- Documentação aprimorada

#### Sessão 05: Orquestração Multi-Agente (`agents_orchestrator.py`)
- Adicionadas dicas de tipo (alterado de `str | None` para `Optional[str]`)
- Documentação da classe Agent aprimorada
- Suporte para substituição de endpoint adicionado
- Padrão de inicialização melhorado

#### Sessão 06: Roteador de Modelos (`models_router.py`)
- Configuração de endpoint adicionada
- Documentação sobre deteção de intenção aprimorada
- Documentação da lógica de roteamento melhorada

#### Sessão 06: Pipeline (`models_pipeline.py`)
- Documentação abrangente de funções adicionada
- Documentação passo a passo melhorada
- Tratamento de erros aprimorado

### Scripts

#### Exportação de Benchmark (`export_benchmark_markdown.py`)
- Suporte para substituição de endpoint adicionado
- Modelos padrão atualizados
- Documentação de funções aprimorada
- Tratamento de erros melhorado

#### Linter CLI (`lint_markdown_cli.py`)
- Links de referência ao SDK adicionados
- Documentação de uso aprimorada

### Testes

#### Testes de Fumaça (`smoke.py`)
- Suporte para substituição de endpoint adicionado
- Documentação aprimorada
- Documentação de casos de teste melhorada
- Relatórios de erro mais detalhados

## Variáveis de Ambiente

Todas as amostras agora suportam estas variáveis de ambiente:

### Configuração Principal
- `FOUNDRY_LOCAL_ALIAS` - Alias do modelo a ser usado (padrão varia conforme a amostra)
- `FOUNDRY_LOCAL_ENDPOINT` - Substituir o endpoint do serviço (opcional)
- `SHOW_USAGE` - Mostrar estatísticas de uso de tokens (padrão: "0")
- `RETRY_ON_FAIL` - Ativar lógica de repetição (padrão: "1")
- `RETRY_BACKOFF` - Atraso inicial de repetição em segundos (padrão: "1.0")

### Específicas para Amostras
- `EMBED_MODEL` - Modelo de incorporação para amostras RAG
- `BENCH_MODELS` - Modelos separados por vírgula para benchmarking
- `BENCH_ROUNDS` - Número de rodadas de benchmarking
- `BENCH_PROMPT` - Prompt de teste para benchmarks
- `BENCH_STREAM` - Medir latência do primeiro token
- `RAG_QUESTION` - Pergunta de teste para amostras RAG
- `AGENT_MODEL_PRIMARY` - Modelo principal do agente
- `AGENT_MODEL_EDITOR` - Modelo editor do agente
- `SLM_ALIAS` - Alias de modelo de linguagem pequeno
- `LLM_ALIAS` - Alias de modelo de linguagem grande

## Melhores Práticas do SDK Implementadas

### 1. Inicialização Correta do Cliente
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Recuperação de Informações do Modelo
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Tratamento de Erros
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Lógica de Repetição com Backoff Exponencial
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Suporte a Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Guia de Migração para Amostras Personalizadas

Se estiver a criar novas amostras ou a atualizar as existentes:

1. **Utilize os auxiliares de `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Suporte para substituição de endpoint**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Adicione documentação abrangente**:
   - Variáveis de ambiente na docstring
   - Link de referência ao SDK
   - Exemplos de uso

4. **Utilize dicas de tipo**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Implemente tratamento de erros adequado**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testes

Todas as amostras podem ser testadas com:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Referências de Documentação do SDK

- **Repositório Principal**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentação da API**: Consulte o repositório do SDK para a documentação mais recente da API

## Alterações Disruptivas

### Nenhuma Esperada
Todas as alterações são retrocompatíveis. As atualizações principalmente:
- Adicionam novas funcionalidades opcionais (substituição de endpoint)
- Melhoram o tratamento de erros
- Aperfeiçoam a documentação
- Atualizam os nomes dos modelos padrão para recomendações atuais

### Melhorias Opcionais
Pode querer atualizar o seu código para usar:
- `FOUNDRY_LOCAL_ENDPOINT` para controlo explícito de endpoint
- `SHOW_USAGE=1` para visibilidade do uso de tokens
- Modelos padrão atualizados (`phi-4-mini` em vez de `phi-3.5-mini`)

## Problemas Comuns e Soluções

### Problema: "Falha na inicialização do cliente"
**Solução**: Certifique-se de que o serviço Foundry Local está em execução:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problema: "Modelo não encontrado"
**Solução**: Verifique os modelos disponíveis:
```bash
foundry model list
```

### Problema: Erros de conexão ao endpoint
**Solução**: Verifique o endpoint:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Próximos Passos

1. **Atualizar amostras do Módulo08**: Aplicar padrões semelhantes às amostras do Módulo08
2. **Adicionar testes de integração**: Criar uma suíte de testes abrangente
3. **Benchmark de desempenho**: Comparar desempenho antes/depois
4. **Atualizações na documentação**: Atualizar o README principal com os novos padrões

## Diretrizes de Contribuição

Ao adicionar novas amostras:
1. Utilize `workshop_utils.py` para consistência
2. Siga o padrão das amostras existentes
3. Adicione docstrings abrangentes
4. Inclua links de referência ao SDK
5. Suporte para substituição de endpoint
6. Adicione dicas de tipo adequadas
7. Inclua exemplos de uso na docstring

## Compatibilidade de Versão

Estas atualizações são compatíveis com:
- `foundry-local-sdk` (mais recente)
- `openai>=1.30.0`
- Python 3.8+

---

**Última Atualização**: 2025-01-08  
**Responsável**: Equipa EdgeAI Workshop  
**Versão do SDK**: Foundry Local SDK (mais recente 0.7.117+67073234e7)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.