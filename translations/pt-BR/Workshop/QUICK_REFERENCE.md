# Exemplos de Workshop - Cartão de Referência Rápida

**Última Atualização**: 8 de outubro de 2025

---

## 🚀 Início Rápido

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Visão Geral dos Exemplos

| Sessão | Exemplo | Propósito | Tempo |
|--------|---------|-----------|-------|
| 01 | `chat_bootstrap.py` | Chat básico + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG com embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Avaliação de RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Benchmark de modelos | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Sistema multi-agente | ~60s |
| 06 | `models_router.py` | Roteamento de intenções | ~45s |
| 06 | `models_pipeline.py` | Pipeline de múltiplas etapas | ~60s |

---

## 🛠️ Variáveis de Ambiente

### Essenciais
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Específicas da Sessão
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Validação e Testes

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Solução de Problemas

### Erro de Conexão
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Erro de Importação
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modelo Não Encontrado
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Desempenho Lento
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Padrões Comuns

### Chat Básico
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Obter Cliente
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Tratamento de Erros
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Seleção de Modelos

| Modelo | Tamanho | Melhor Para | Velocidade |
|--------|---------|-------------|------------|
| `qwen2.5-0.5b` | 0.5B | Classificação rápida | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Geração de código rápida | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Escrita criativa | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Código, refatoração | ⚡⚡ |
| `phi-4-mini` | 4B | Geral, resumo | ⚡⚡ |
| `qwen2.5-7b` | 7B | Raciocínio complexo | ⚡ |

---

## 🔗 Recursos

- **Documentação SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referência Rápida**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Dicas

1. **Cache de clientes**: `workshop_utils` faz o cache para você
2. **Use modelos menores**: Comece com `qwen2.5-0.5b` para testes
3. **Ative estatísticas de uso**: Configure `SHOW_USAGE=1` para monitorar tokens
4. **Processamento em lote**: Processe múltiplos prompts sequencialmente
5. **Reduza max_tokens**: Diminui a latência para respostas rápidas

---

## 🎯 Fluxos de Trabalho de Exemplos

### Teste Tudo
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark de Modelos
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### Pipeline RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Sistema Multi-Agente
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Ajuda Rápida**: Execute qualquer exemplo com `--help` no diretório `samples` ou verifique a docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Todos os exemplos atualizados em outubro de 2025 com as melhores práticas do Foundry Local SDK** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->