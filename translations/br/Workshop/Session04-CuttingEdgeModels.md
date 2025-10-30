<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T21:33:42+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "br"
}
-->
# Sessão 4: Explore Modelos de Ponta – LLMs, SLMs e Inferência Local

## Resumo

Compare Modelos de Linguagem Grandes (LLMs) e Modelos de Linguagem Pequenos (SLMs) para cenários de inferência local versus na nuvem. Aprenda padrões de implantação utilizando aceleração do ONNX Runtime, execução com WebGPU e experiências híbridas de RAG. Inclui uma demonstração de RAG com Chainlit usando um modelo local e uma exploração opcional do OpenWebUI. Você adaptará um starter de inferência com WebGPU e avaliará as trocas entre capacidade e custo/desempenho do Phi e GPT-OSS-20B.

## Objetivos de Aprendizado

- **Contrastar** SLM e LLM em termos de latência, memória e qualidade
- **Implantar** modelos com ONNXRuntime e (quando suportado) WebGPU
- **Executar** inferência no navegador (demonstração interativa preservando privacidade)
- **Integrar** um pipeline RAG com Chainlit usando um backend SLM local
- **Avaliar** utilizando heurísticas leves de qualidade e custo

## Pré-requisitos

- Sessões 1–3 concluídas
- `chainlit` instalado (já incluído em `requirements.txt` para o Módulo08)
- Navegador compatível com WebGPU (Edge / Chrome mais recente no Windows 11)
- Foundry Local em execução (`foundry status`)

### Notas de Plataforma Cruzada

O Windows continua sendo o ambiente principal. Para desenvolvedores de macOS que aguardam binários nativos:
1. Execute o Foundry Local em uma VM com Windows 11 (Parallels / UTM) OU em uma estação de trabalho remota com Windows.
2. Exponha o serviço (porta padrão 5273) e configure no macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Use os mesmos passos de ambiente virtual Python das sessões anteriores.

Instalação do Chainlit (ambas as plataformas):
```bash
pip install chainlit
```

## Fluxo da Demonstração (30 min)

### 1. Comparar Phi (SLM) e GPT-OSS-20B (LLM) (6 min)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Acompanhe: profundidade da resposta, precisão factual, riqueza estilística, latência.

### 2. Aceleração com ONNX Runtime (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Observe mudanças na taxa de transferência ao habilitar GPU versus apenas CPU.

### 3. Inferência com WebGPU no Navegador (6 min)

Adapte o starter `04-webgpu-inference` (crie `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Abra o arquivo no navegador; observe o retorno local de baixa latência.

### 4. Aplicativo de Chat RAG com Chainlit (7 min)

`samples/04-cutting-edge/chainlit_app.py` mínimo:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Execute:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Projeto Inicial: Adaptar `04-webgpu-inference` (6 min)

Entregáveis:
- Substituir lógica de busca placeholder por tokens em streaming (use a variante de endpoint `stream=True` quando habilitada)
- Adicionar gráfico de latência (lado do cliente) para alternar entre phi e gpt-oss-20b
- Incorporar contexto RAG inline (textarea para documentos de referência)

## Heurísticas de Avaliação

| Categoria | Phi-4-mini | GPT-OSS-20B | Observação |
|----------|------------|-------------|-------------|
| Latência (frio) | Rápido | Mais lento | SLM aquece rapidamente |
| Memória | Baixa | Alta | Viabilidade no dispositivo |
| Adesão ao contexto | Boa | Forte | Modelo maior pode ser mais verboso |
| Custo (local) | Mínimo | Maior (recursos) | Troca entre energia/tempo |
| Melhor caso de uso | Apps locais | Raciocínio profundo | Pipeline híbrido possível |

## Validando o Ambiente

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Solução de Problemas

| Sintoma | Causa | Ação |
|---------|-------|--------|
| Falha na busca da página web | CORS ou serviço fora do ar | Use `curl` para verificar o endpoint; habilite proxy CORS se necessário |
| Chainlit em branco | Ambiente não ativo | Ative o venv e reinstale dependências |
| Alta latência | Modelo recém-carregado | Aqueça com sequência de prompts pequenos |

## Referências

- SDK Foundry Local: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentação do Chainlit: https://docs.chainlit.io
- Avaliação RAG (Ragas): https://docs.ragas.io

---

**Duração da Sessão**: 30 min  
**Dificuldade**: Avançado

## Cenário de Exemplo e Mapeamento do Workshop

| Artefatos do Workshop | Cenário | Objetivo | Fonte de Dados / Prompt |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Equipe de arquitetura avaliando SLM vs LLM para gerador de resumo executivo | Quantificar diferença de latência + uso de tokens | Variável de ambiente única `COMPARE_PROMPT` |
| `chainlit_app.py` (demonstração RAG) | Protótipo de assistente de conhecimento interno | Respostas curtas fundamentadas com recuperação lexical mínima | Lista `DOCS` inline no arquivo |
| `webgpu_demo.html` | Prévia de inferência futurista no navegador | Mostrar retorno local de baixa latência + narrativa de UX | Apenas prompt ao vivo do usuário |

### Narrativa do Cenário
A equipe de produto deseja um gerador de resumo executivo. Um SLM leve (phi‑4‑mini) cria rascunhos de resumos; um LLM maior (gpt‑oss‑20b) pode refinar apenas relatórios de alta prioridade. Os scripts da sessão capturam métricas empíricas de latência e tokens para justificar um design híbrido, enquanto a demonstração do Chainlit ilustra como a recuperação fundamentada mantém as respostas do modelo pequeno factuais. A página conceitual do WebGPU fornece um caminho de visão para processamento totalmente no cliente quando a aceleração no navegador amadurecer.

### Contexto RAG Mínimo (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Fluxo Híbrido Rascunho→Refinamento (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Acompanhe ambos os componentes de latência para relatar o custo médio combinado.

### Melhorias Opcionais

| Foco | Melhoria | Por quê | Dica de Implementação |
|-------|------------|-----|---------------------|
| Métricas Comparativas | Acompanhar uso de tokens + latência do primeiro token | Visão holística de desempenho | Use script de benchmark aprimorado (Sessão 3) com `BENCH_STREAM=1` |
| Pipeline Híbrido | Rascunho com SLM → Refinamento com LLM | Reduzir latência e custo | Gerar com phi-4-mini, refinar resumo com gpt-oss-20b |
| UI de Streaming | Melhor UX no Chainlit | Feedback incremental | Use `stream=True` quando o streaming local for exposto; acumule chunks |
| Cache WebGPU | Inicialização JS mais rápida | Reduzir sobrecarga de recompilação | Cache de artefatos de shader compilados (capacidade futura de runtime) |
| Conjunto de QA Determinístico | Comparação justa de modelos | Remover variância | Lista fixa de prompts + `temperature=0` para execuções de avaliação |
| Pontuação de Saída | Lente estruturada de qualidade | Ir além de anedotas | Rubrica simples: coerência / factualidade / concisão (1–5) |
| Notas de Energia / Recursos | Discussão em sala de aula | Mostrar trocas | Use monitores do SO (`foundry system info`, Gerenciador de Tarefas, `nvidia-smi`) + saídas de script de benchmark |
| Emulação de Custo | Justificação pré-nuvem | Planejar escalabilidade | Mapear tokens para preços hipotéticos na nuvem para narrativa de TCO |
| Decomposição de Latência | Identificar gargalos | Alvo de otimizações | Medir preparação de prompt, envio de requisição, primeiro token, conclusão total |
| RAG + Retorno LLM | Rede de segurança de qualidade | Melhorar consultas difíceis | Se comprimento da resposta do SLM < limite ou baixa confiança → escalar |

#### Padrão Híbrido Rascunho/Refinamento de Exemplo

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Esboço de Decomposição de Latência

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Use estrutura de medição consistente entre modelos para comparações justas.

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.