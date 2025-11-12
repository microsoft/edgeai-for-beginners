<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T22:47:32+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "br"
}
-->
# Sessão 3: Modelos Open-Source no Foundry Local

## Resumo

Descubra como integrar modelos do Hugging Face e outros modelos open-source no Foundry Local. Aprenda estratégias de seleção, fluxos de trabalho de contribuição da comunidade, metodologia de comparação de desempenho e como estender o Foundry com registros personalizados de modelos. Esta sessão está alinhada aos temas semanais de exploração "Model Mondays" e prepara você para avaliar e operacionalizar modelos open-source localmente antes de escalar para o Azure.

## Objetivos de Aprendizagem

Ao final, você será capaz de:

- **Descobrir & Avaliar**: Identificar modelos candidatos (mistral, gemma, qwen, deepseek) usando trade-offs entre qualidade e recursos.
- **Carregar & Executar**: Utilizar o CLI do Foundry Local para baixar, armazenar em cache e executar modelos da comunidade.
- **Benchmark**: Aplicar heurísticas consistentes de latência + throughput de tokens + qualidade.
- **Estender**: Registrar ou adaptar um wrapper de modelo personalizado seguindo padrões compatíveis com o SDK.
- **Comparar**: Produzir comparações estruturadas para decisões de seleção entre SLM e LLM de médio porte.

## Pré-requisitos

- Sessões 1 e 2 concluídas
- Ambiente Python com `foundry-local-sdk` instalado
- Pelo menos 15GB de espaço livre em disco para múltiplos caches de modelos

### Início Rápido em Ambiente Multiplataforma

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Ao realizar benchmarks no macOS contra um serviço host no Windows, configure:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Fluxo de Demonstração (30 min)

### 1. Carregar Modelos do Hugging Face via CLI (8 min)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Executar & Teste Rápido (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Script de Benchmark (8 min)

Crie `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Execute:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Comparar Desempenho (5 min)

Discuta os trade-offs: tempo de carregamento, uso de memória (observe o Gerenciador de Tarefas / `nvidia-smi` / monitor de recursos do sistema operacional), qualidade de saída versus velocidade. Use o script de benchmark em Python (Sessão 3) para latência e throughput; repita após habilitar aceleração por GPU.

### 5. Projeto Inicial (4 min)

Crie um gerador de relatórios de comparação de modelos (estenda o script de benchmark com exportação em markdown).

## Projeto Inicial: Estender `03-huggingface-models`

Melhore o exemplo existente ao:

1. Adicionar agregação de benchmarks + saída em CSV/Markdown.
2. Implementar pontuação qualitativa simples (conjunto de prompts + arquivo de anotação manual).
3. Introduzir um arquivo de configuração JSON (`models.json`) para lista de modelos plugáveis e conjunto de prompts.

## Lista de Verificação de Validação

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Todos os modelos-alvo devem aparecer e responder a uma solicitação de chat de teste.

## Cenário de Exemplo & Mapeamento do Workshop

| Script do Workshop | Cenário | Objetivo | Fonte do Prompt / Dataset |
|--------------------|---------|----------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Equipe de plataforma de borda selecionando SLM padrão para sumarizador embutido | Produzir comparação de latência + p95 + tokens/segundo entre modelos candidatos | Variável `PROMPT` inline + lista de ambiente `BENCH_MODELS` |

### Narrativa do Cenário

A equipe de engenharia de produto deve escolher um modelo leve padrão de sumarização para um recurso offline de notas de reunião. Eles realizam benchmarks determinísticos controlados (temperature=0) em um conjunto fixo de prompts (veja exemplo abaixo) e coletam métricas de latência + throughput com e sem aceleração por GPU.

### Exemplo de Conjunto de Prompts em JSON (expansível)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Itere cada prompt por modelo, capture a latência por prompt para derivar métricas de distribuição e detectar outliers.

## Estrutura de Seleção de Modelos

| Dimensão | Métrica | Por que é importante |
|----------|---------|----------------------|
| Latência | média / p95 | Consistência na experiência do usuário |
| Throughput | tokens/segundo | Escalabilidade em lote e streaming |
| Memória | tamanho residente | Compatibilidade com dispositivos e concorrência |
| Qualidade | prompts de avaliação | Adequação à tarefa |
| Espaço | cache em disco | Distribuição e atualizações |
| Licença | permissão de uso | Conformidade comercial |

## Estendendo com Modelo Personalizado

Padrão de alto nível (pseudo):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Consulte o repositório oficial para interfaces de adaptadores em evolução:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Solução de Problemas

| Problema | Causa | Solução |
|----------|-------|---------|
| OOM no mistral-7b | RAM/GPU insuficiente | Pare outros modelos; tente uma variante menor |
| Resposta inicial lenta | Carregamento frio | Mantenha aquecido com um prompt leve periódico |
| Download travado | Instabilidade na rede | Tente novamente; pré-carregue durante horários de menor uso |

## Referências

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Descoberta de Modelos no Hugging Face: https://huggingface.co/models

---

**Duração da Sessão**: 30 min (+ aprofundamento opcional)  
**Dificuldade**: Intermediário

### Melhorias Opcionais

| Melhoria | Benefício | Como |
|----------|-----------|------|
| Latência do Primeiro Token em Streaming | Mede a responsividade percebida | Execute benchmark com `BENCH_STREAM=1` (script aprimorado em `Workshop/samples/session03`) |
| Modo Determinístico | Comparações estáveis de regressão | `temperature=0`, conjunto fixo de prompts, capture saídas JSON sob controle de versão |
| Pontuação por Rubrica de Qualidade | Adiciona dimensão qualitativa | Mantenha `prompts.json` com facetas esperadas; anote pontuações (1–5) manualmente ou via modelo secundário |
| Exportação em CSV / Markdown | Relatório compartilhável | Estenda o script para escrever `benchmark_report.md` com tabela e destaques |
| Tags de Capacidade do Modelo | Ajuda no roteamento automatizado posteriormente | Mantenha `models.json` com `{alias: {capabilities:[], size_mb:..}}` |
| Fase de Aquecimento de Cache | Reduz viés de inicialização fria | Execute uma rodada de aquecimento antes do loop de temporização (já implementado) |
| Precisão Percentil | Latência robusta de cauda | Use numpy percentile (já no script refatorado) |
| Aproximação de Custo por Token | Comparação econômica | Custo aprox = (tokens/seg * média de tokens por solicitação) * heurística de energia |
| Pular Modelos com Falha Automaticamente | Resiliência em execuções em lote | Envolva cada benchmark em try/except e marque o campo de status |

#### Trecho Mínimo de Exportação em Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Exemplo de Conjunto de Prompts Determinístico

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Itere a lista estática em vez de prompts aleatórios para métricas comparáveis entre commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->