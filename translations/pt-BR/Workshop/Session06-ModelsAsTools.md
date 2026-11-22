# Sessão 6: Foundry Local – Modelos como Ferramentas

## Resumo

Trate os modelos como ferramentas composáveis dentro de uma camada operacional local de IA. Esta sessão mostra como encadear várias chamadas especializadas SLM/LLM, roteando tarefas seletivamente e expondo uma interface unificada de SDK para aplicações. Você construirá um roteador de modelo leve + planejador de tarefas, integrará isso a um script de aplicativo e delineará o caminho para escalar para Azure AI Foundry para cargas de trabalho de produção.

## Objetivos de Aprendizagem

- **Conceitualizar** modelos como ferramentas atômicas com capacidades declaradas
- **Roteamento** de solicitações com base em intenção / pontuação heurística
- **Encadear** saídas em tarefas multi-etapas (decompor → resolver → refinar)
- **Integrar** uma API de cliente unificada para aplicações downstream
- **Escalar** o design para a nuvem (mesmo contrato compatível com OpenAI)

## Pré-requisitos

- Sessões 1–5 concluídas
- Múltiplos modelos locais em cache (ex: `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Trecho de Ambiente Cross-Platform

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Acesso remoto/VM a partir de macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Fluxo da Demo (30 min)

### 1. Declaração de Capacidade da Ferramenta (5 min)

Crie `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```

### 2. Detecção de Intenção & Roteamento (8 min)

Crie `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Catalogar pontuação: combinar capacidade primeiro, depois prioridade
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Ordenar: combinar True primeiro, depois menor valor de prioridade
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```

### 3. Encadeamento de Tarefas Multi-etapas (7 min)

Crie `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```

### 4. Projeto Iniciante: Adapte `06-models-as-tools` (5 min)

Melhorias:
- Adicione suporte ao streaming de tokens (atualização progressiva da UI)
- Adicione pontuação de confiança: sobreposição lexical ou rubrica de prompt
- Exporte rastreamento JSON (intenção → modelo → latência → uso de tokens)
- Implemente reutilização de cache para sub-etapas repetidas

### 5. Caminho de Escalonamento para Azure (5 min)

| Camada | Local (Foundry) | Nuvem (Azure AI Foundry) | Estratégia de Transição |
|-------|-----------------|--------------------------|---------------------|
| Roteamento | Python heurístico | Microsserviço durável | Containerizar & implantar API |
| Modelos | SLMs em cache | Implantações gerenciadas | Mapear nomes locais para IDs de implantação |
| Observabilidade | Estatísticas CLI/manual | Logs centrais & métricas | Adicionar eventos estruturados de rastreamento |
| Segurança | Apenas host local | Autenticação Azure / rede | Introduzir key vault para segredos |
| Custo | Recurso do dispositivo | Cobrança por consumo | Adicionar limites de orçamento |

## Checklist de Validação

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Espere seleção de modelo baseada em intenção e saída final refinada.

## Solução de Problemas

| Problema | Causa | Correção |
|---------|-------|----------|
| Todas as tarefas roteadas para o mesmo modelo | Regras fracas | Enriqueça o conjunto regex das INTENT_RULES |
| Pipeline falha no meio da etapa | Modelo necessário não carregado | Execute `foundry model run <model>` |
| Baixa coesão da saída | Falta fase de refinamento | Adicione uma passagem de sumarização/validação |

## Referências

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentação Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Padrões de Qualidade de Prompt: Veja Sessão 2

---

**Duração da Sessão**: 30 min  
**Dificuldade**: Especialista

## Cenário de Exemplo & Mapeamento do Workshop

| Scripts / Notebooks do Workshop | Cenário | Objetivo | Fonte do Dataset / Catálogo |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Assistente de desenvolvedor lidando com prompts de intenções mistas (refatorar, resumir, classificar) | Roteamento heurístico intenção → alias modelo com uso de tokens | `CATALOG` embutido + `RULES` regex |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planejamento e refinamento multi-etapas para tarefa complexa de assistência em codificação | Decompor → execução especializada → passo de refinamento sumário | Mesmo `CATALOG`; passos derivados da saída do plano |

### Narrativa do Cenário
Uma ferramenta de produtividade de engenharia recebe tarefas heterogêneas: refatorar código, resumir notas arquitetônicas, classificar feedback. Para minimizar latência e uso de recursos, um modelo geral pequeno planeja e resume, um modelo especializado em código lida com refatoração, e um modelo leve capaz de classificação rotula o feedback. O script do pipeline demonstra encadeamento + refinamento; o script do roteador isola roteamento adaptativo de prompt único.

### Snapshot do Catálogo
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### Exemplos de Prompts para Teste
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### Extensão do Rastreamento (Opcional)
Adicione linhas JSON de rastreamento por passo para `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### Heurística de Escalonamento (Ideia)
Se o plano conter palavras-chave como "otimizar", "segurança" ou comprimento do passo > 280 caracteres → escale para um modelo maior (ex: `gpt-oss-20b`) apenas para essa etapa.

### Melhorias Opcionais

| Área | Melhoria | Valor | Dica |
|------|-------------|-------|------|
| Cache | Reutilizar objetos de gerenciador + cliente | Menor latência, menos overhead | Use `workshop_utils.get_client` |
| Métricas de Uso | Capturar tokens & latência por passo | Perfilamento & otimização | Cronometre cada chamada roteada; armazene na lista de rastreamento |
| Roteamento Adaptativo | Consciência de confiança / custo | Melhor trade-off qualidade-custo | Adicione pontuação: se prompt > N caracteres ou regex corresponder ao domínio → escale para modelo maior |
| Registro Dinâmico de Capacidades | Reload a quente do catálogo | Sem reinício/reimplantação | Carregue `catalog.json` em tempo de execução; monitore timestamp do arquivo |
| Estratégia de Fallback | Robustez em falhas | Maior disponibilidade | Tente primário → em exceção fallback para alias |
| Pipeline com Streaming | Feedback antecipado | Melhoria de UX | Faça streaming em cada etapa e buffer para entrada de refinamento final |
| Embeddings Vetoriais de Intenção | Roteamento mais nuançado | Maior precisão de intenção | Embede o prompt, agrupe & mapeie centróide → capacidade |
| Exportação de Rastreamento | Cadeia auditável | Conformidade/relatórios | Emitir linhas JSON: passo, intenção, modelo, latência_ms, tokens |
| Simulação de Custo | Estimativa pré-nuvem | Planejamento orçamentário | Atribua custo notional/token por modelo & agregue por tarefa |
| Modo Determinístico | Reprodutibilidade | Benchmarking estável | Env: `temperature=0`, contagem fixa de passos |

#### Exemplo de Estrutura do Rastreamento

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```

#### Esboço de Escalonamento Adaptativo

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalar para um modelo de raciocínio maior, se disponível
    alias = 'gpt-oss-20b'
```

#### Reload a Quente do Catálogo de Modelos

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->