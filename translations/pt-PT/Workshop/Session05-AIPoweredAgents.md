# Sessão 5: Crie Agentes com IA de Forma Rápida com Foundry Local

## Resumo

Projete e orquestre agentes de IA com múltiplos papéis utilizando o runtime de baixa latência e preservação de privacidade do Foundry Local. Você definirá papéis dos agentes, estratégias de memória, padrões de invocação de ferramentas e gráficos de execução. A sessão apresenta padrões de estruturação que podem ser estendidos com Chainlit ou LangGraph. O projeto inicial amplia o exemplo de arquitetura de agentes existente para adicionar persistência de memória e ganchos de avaliação.

## Objetivos de Aprendizagem

- **Definir Papéis**: Prompts do sistema e limites de capacidade
- **Implementar Memória**: Curto prazo (conversação), longo prazo (vetor/arquivo), blocos de notas temporários
- **Estruturar Fluxos de Trabalho**: Passos sequenciais, ramificados e paralelos dos agentes
- **Integrar Ferramentas**: Padrão leve de chamada de funções como ferramentas
- **Avaliar**: Rastreamento básico + pontuação de resultados baseada em critérios

## Pré-requisitos

- Sessões 1–4 concluídas
- Python com `foundry-local-sdk`, `openai`, opcional `chainlit`
- Modelos locais em execução (pelo menos `phi-4-mini`)

### Trecho de Ambiente Multiplataforma

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Se executar agentes no macOS contra um serviço remoto em Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Fluxo de Demonstração (30 min)

### 1. Definir Papéis e Memória dos Agentes (7 min)

Crie `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Padrão de Estruturação CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Adicionar Invocação de Ferramentas (7 min)

Estenda com `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

Modifique `agents_core.py` para permitir uma sintaxe simples de ferramentas: o utilizador escreve `#tool:get_time` e o agente expande a saída da ferramenta no contexto antes da geração.

### 4. Fluxo de Trabalho Orquestrado (6 min)

Crie `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Projeto Inicial: Estender `05-agent-architecture` (7 min)

Adicione:
1. Camada de memória persistente (por exemplo, anexação de linhas JSON de conversas)
2. Rubrica de avaliação simples: placeholders de factualidade / clareza / estilo
3. Front-end opcional com Chainlit (duas abas: conversação e rastreamentos)
4. Máquina de estados no estilo LangGraph opcional (se adicionar dependência) para decisões ramificadas

## Lista de Verificação de Validação

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Espere uma saída de pipeline estruturada com nota de injeção de ferramenta.

## Visão Geral das Estratégias de Memória

| Camada       | Propósito             | Exemplo               |
|--------------|-----------------------|-----------------------|
| Curto prazo  | Continuidade do diálogo | Últimas N mensagens   |
| Episódica    | Recordação da sessão  | JSON por sessão       |
| Semântica    | Recuperação de longo prazo | Armazenamento vetorial de resumos |
| Bloco de notas | Passos de raciocínio | Cadeia de pensamento inline (privado) |

## Ganchos de Avaliação (Conceito)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Resolução de Problemas

| Problema            | Causa                     | Solução                        |
|---------------------|---------------------------|--------------------------------|
| Respostas repetitivas | Janela de contexto muito grande/pequena | Ajustar parâmetro da janela de memória |
| Ferramenta não invocada | Sintaxe incorreta       | Usar formato `#tool:tool_name` |
| Orquestração lenta  | Múltiplos modelos frios   | Executar prompts de aquecimento previamente |

## Referências

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (conceito opcional): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Duração da Sessão**: 30 min  
**Dificuldade**: Avançado

## Cenário de Exemplo e Mapeamento do Workshop

| Script do Workshop | Cenário | Objetivo | Exemplo de Prompt |
|--------------------|---------|----------|-------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot de pesquisa de conhecimento que produz resumos para executivos | Pipeline de dois agentes (pesquisa → refinamento editorial) com modelos distintos opcionais | Explique por que a inferência local é importante para conformidade. |
| (Estendido) conceito `tools.py` | Adicionar ferramentas de estimativa de tempo e tokens | Demonstrar padrão leve de invocação de ferramentas | #tool:get_time |

### Narrativa do Cenário

A equipa de documentação de conformidade precisa de resumos internos rápidos, baseados em conhecimento local, sem enviar rascunhos para serviços na nuvem. Um agente pesquisador reúne pontos factuais concisos; um agente editor reescreve para clareza executiva. Aliases de modelos distintos podem ser atribuídos para otimizar latência (SLM rápido) versus refinamento estilístico (modelo maior apenas quando necessário).

### Exemplo de Ambiente Multi-Modelo

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Estrutura de Rastreamento (Opcional)

```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Persista cada etapa em um arquivo JSONL para posterior pontuação baseada em rubrica.

### Melhorias Opcionais

| Tema              | Melhoria                  | Benefício              | Esboço de Implementação       |
|-------------------|---------------------------|------------------------|--------------------------------|
| Papéis Multi-Modelo | Modelos distintos por agente (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Especialização e velocidade | Selecionar variáveis de ambiente de alias, chamar `chat_once` com alias por papel |
| Rastreamentos Estruturados | Rastreamento JSON de cada ato (ferramenta, entrada, latência, tokens) | Depuração e avaliação | Anexar dict a uma lista; escrever `.jsonl` no final |
| Persistência de Memória | Contexto de diálogo recarregável | Continuidade da sessão | Exportar `Agent.memory` para `sessions/<ts>.json` |
| Registro de Ferramentas | Descoberta dinâmica de ferramentas | Extensibilidade | Manter dict `TOOLS` e inspecionar nomes/descrições |
| Retry e Backoff | Cadeias longas robustas | Reduzir falhas transitórias | Envolver `act` com try/except + backoff exponencial |
| Pontuação de Rubrica | Etiquetas qualitativas automatizadas | Acompanhar melhorias | Passagem secundária solicitando ao modelo: "Avalie clareza de 1-5" |
| Memória Vetorial | Recuperação semântica | Contexto rico de longo prazo | Incorporar resumos, recuperar top-k na mensagem do sistema |
| Respostas em Streaming | Resposta percebida mais rápida | Melhoria de UX | Usar streaming quando disponível e liberar tokens parciais |
| Testes Determinísticos | Controle de regressão | CI estável | Executar com `temperature=0`, seeds de prompt fixos |
| Ramificação Paralela | Exploração mais rápida | Maior throughput | Usar `concurrent.futures` para passos independentes dos agentes |

#### Exemplo de Registro de Rastreamento

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Prompt de Avaliação Simples

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Persista pares (`resposta`, `avaliação`) para construir um gráfico histórico de qualidade.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.