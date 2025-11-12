<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-11T22:46:37+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "br"
}
-->
# EdgeAI para Iniciantes - Workshop

> **Caminho Prático para Construir Aplicações de Edge AI Prontas para Produção**
>
> Domine o deployment de IA local com o Microsoft Foundry Local, desde a primeira conclusão de chat até a orquestração de múltiplos agentes em 6 sessões progressivas.

---

## 🎯 Introdução

Bem-vindo ao **Workshop EdgeAI para Iniciantes** - seu guia prático e prático para construir aplicações inteligentes que funcionam inteiramente em hardware local. Este workshop transforma conceitos teóricos de Edge AI em habilidades do mundo real por meio de exercícios progressivamente desafiadores usando o Microsoft Foundry Local e Modelos de Linguagem Pequenos (SLMs).

### Por que este Workshop?

**A Revolução do Edge AI Chegou**

Organizações ao redor do mundo estão migrando de IA dependente da nuvem para computação de borda por três razões críticas:

1. **Privacidade e Conformidade** - Processar dados sensíveis localmente sem transmissão para a nuvem (HIPAA, GDPR, regulamentações financeiras)
2. **Desempenho** - Eliminar latência de rede (50-500ms local vs 500-2000ms ida e volta na nuvem)
3. **Controle de Custos** - Remover custos por token de API e escalar sem despesas de nuvem

**Mas Edge AI é Diferente**

Executar IA no local exige novas habilidades:
- Seleção e otimização de modelos para restrições de recursos
- Gerenciamento de serviços locais e aceleração de hardware
- Engenharia de prompts para modelos menores
- Padrões de deployment para dispositivos de borda

**Este Workshop Entrega Essas Habilidades**

Em 6 sessões focadas (~3 horas no total), você avançará de "Hello World" para o deployment de sistemas multi-agentes prontos para produção - tudo rodando localmente na sua máquina.

---

## 📚 Objetivos de Aprendizado

Ao concluir este workshop, você será capaz de:

### Competências Principais
1. **Deploy e Gerenciamento de Serviços de IA Locais**
   - Instalar e configurar o Microsoft Foundry Local
   - Selecionar modelos apropriados para deployment em borda
   - Gerenciar o ciclo de vida dos modelos (download, carregamento, cache)
   - Monitorar uso de recursos e otimizar desempenho

2. **Construir Aplicações com IA**
   - Implementar conclusões de chat compatíveis com OpenAI localmente
   - Projetar prompts eficazes para Modelos de Linguagem Pequenos
   - Lidar com respostas em streaming para melhor experiência do usuário
   - Integrar modelos locais em aplicações existentes

3. **Criar Sistemas RAG (Geração Aumentada por Recuperação)**
   - Construir busca semântica com embeddings
   - Basear respostas de LLM em conhecimento específico do domínio
   - Avaliar a qualidade de RAG com métricas padrão da indústria
   - Escalar de protótipo para produção

4. **Otimizar Desempenho de Modelos**
   - Realizar benchmarks de múltiplos modelos para seu caso de uso
   - Medir latência, throughput e tempo do primeiro token
   - Selecionar modelos ótimos com base em trade-offs de velocidade/qualidade
   - Comparar trade-offs entre SLM e LLM em cenários reais

5. **Orquestrar Sistemas Multi-Agentes**
   - Projetar agentes especializados para diferentes tarefas
   - Implementar memória e gerenciamento de contexto de agentes
   - Coordenar agentes em fluxos de trabalho complexos
   - Roteamento inteligente de solicitações entre múltiplos modelos

6. **Deploy de Soluções Prontas para Produção**
   - Implementar tratamento de erros e lógica de repetição
   - Monitorar uso de tokens e recursos do sistema
   - Construir arquiteturas escaláveis com padrões de modelo como ferramentas
   - Planejar caminhos de migração de borda para híbrido (borda + nuvem)

---

## 🎓 Resultados de Aprendizado

### O que Você Vai Construir

Ao final deste workshop, você terá criado:

| Sessão | Entregável | Habilidades Demonstradas |
|--------|------------|--------------------------|
| **1** | Aplicação de chat com streaming | Configuração de serviço, conclusões básicas, UX de streaming |
| **2** | Sistema RAG com avaliação | Embeddings, busca semântica, métricas de qualidade |
| **3** | Suite de benchmark multi-modelo | Medição de desempenho, comparação de modelos |
| **4** | Comparador SLM vs LLM | Análise de trade-offs, estratégias de otimização |
| **5** | Orquestrador multi-agente | Design de agentes, gerenciamento de memória, coordenação |
| **6** | Sistema de roteamento inteligente | Detecção de intenção, seleção de modelo, escalabilidade |

### Matriz de Competências

| Nível de Habilidade | Sessão 1-2 | Sessão 3-4 | Sessão 5-6 |
|---------------------|------------|------------|------------|
| **Iniciante** | ✅ Configuração e básicos | ⚠️ Desafiador | ❌ Muito avançado |
| **Intermediário** | ✅ Revisão rápida | ✅ Aprendizado principal | ⚠️ Objetivos desafiadores |
| **Avançado** | ✅ Fácil de passar | ✅ Refinamento | ✅ Padrões de produção |

### Habilidades Prontas para o Mercado

**Após este workshop, você estará preparado para:**

✅ **Construir Aplicações com Foco em Privacidade**
- Aplicativos de saúde lidando com PHI/PII localmente
- Serviços financeiros com requisitos de conformidade
- Sistemas governamentais com necessidades de soberania de dados

✅ **Otimizar para Ambientes de Borda**
- Dispositivos IoT com recursos limitados
- Aplicativos móveis offline-first
- Sistemas em tempo real de baixa latência

✅ **Projetar Arquiteturas Inteligentes**
- Sistemas multi-agentes para fluxos de trabalho complexos
- Deploys híbridos borda-nuvem
- Infraestrutura de IA otimizada para custos

✅ **Liderar Iniciativas de Edge AI**
- Avaliar a viabilidade de Edge AI para projetos
- Selecionar modelos e frameworks apropriados
- Arquitetar soluções de IA locais escaláveis

---

## 🗺️ Estrutura do Workshop

### Visão Geral das Sessões (6 Sessões × 30 Minutos = 3 Horas)

| Sessão | Tópico | Foco | Duração |
|--------|--------|------|---------|
| **1** | Começando com Foundry Local | Instalar, validar, primeiras conclusões | 30 min |
| **2** | Construindo Soluções de IA com RAG | Engenharia de prompts, embeddings, avaliação | 30 min |
| **3** | Modelos Open Source | Descoberta de modelos, benchmarking, seleção | 30 min |
| **4** | Modelos de Última Geração | SLM vs LLM, otimização, frameworks | 30 min |
| **5** | Agentes com IA | Design de agentes, orquestração, memória | 30 min |
| **6** | Modelos como Ferramentas | Roteamento, encadeamento, estratégias de escalabilidade | 30 min |

---

## 🚀 Início Rápido

### Pré-requisitos

**Requisitos de Sistema:**
- **OS**: Windows 10/11, macOS 11+ ou Linux (Ubuntu 20.04+)
- **RAM**: Mínimo de 8GB, recomendado 16GB+
- **Armazenamento**: 10GB+ de espaço livre para modelos
- **CPU**: Processador moderno com suporte AVX2
- **GPU** (opcional): Compatível com CUDA ou Qualcomm NPU para aceleração

**Requisitos de Software:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Guia de Instalação](../../../Workshop))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (recomendado) ([Download](https://code.visualstudio.com/))

### Configuração em 3 Passos

#### 1. Instalar Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificar Instalação:**
```bash
foundry --version
foundry service status
```

**Certifique-se de que o Azure AI Foundry Local está rodando com uma porta fixa**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verificar funcionamento:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Encontrando Modelos Disponíveis**
Para ver quais modelos estão disponíveis na sua instância do Foundry Local, você pode consultar o endpoint de modelos:

```bash
# cmd/bash/powershell
foundry model list
```

Usando Endpoint Web 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clonar Repositório e Instalar Dependências

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Executar Seu Primeiro Exemplo

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Sucesso!** Você deve ver uma resposta em streaming sobre Edge AI.

---

## 📦 Recursos do Workshop

### Exemplos em Python

Exemplos práticos progressivos demonstrando cada conceito:

| Sessão | Exemplo | Descrição | Tempo de Execução |
|--------|---------|-----------|-------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat básico e streaming | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG com embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Avaliação de qualidade RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-modelo | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Comparação SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistema multi-agente | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Roteamento baseado em intenção | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline multi-etapas | ~60s |

### Jupyter Notebooks

Exploração interativa com explicações e visualizações:

| Sessão | Notebook | Descrição | Dificuldade |
|--------|----------|-----------|-------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Básico de chat e streaming | ⭐ Iniciante |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Construir sistema RAG | ⭐⭐ Intermediário |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Avaliar qualidade RAG | ⭐⭐ Intermediário |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking de modelos | ⭐⭐ Intermediário |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Comparação de modelos | ⭐⭐ Intermediário |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orquestração de agentes | ⭐⭐⭐ Avançado |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Roteamento por intenção | ⭐⭐⭐ Avançado |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orquestração de pipeline | ⭐⭐⭐ Avançado |

### Documentação

Guias e referências abrangentes:

| Documento | Descrição | Quando Usar |
|-----------|-----------|-------------|
| [QUICK_START.md](./QUICK_START.md) | Guia de configuração rápida | Começando do zero |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Resumo de comandos e APIs | Precisa de respostas rápidas |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Padrões e exemplos de SDK | Escrevendo código |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Guia de variáveis de ambiente | Configurando exemplos |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Problemas comuns e soluções | Depurando problemas |

---

## 🎓 Recomendações de Caminho de Aprendizado

### Para Iniciantes (3-4 horas)
1. ✅ Sessão 1: Começando (foco na configuração e chat básico)
2. ✅ Sessão 2: Básico de RAG (pule a avaliação inicialmente)
3. ✅ Sessão 3: Benchmarking simples (apenas 2 modelos)
4. ⏭️ Pule as Sessões 4-6 por enquanto
5. 🔄 Retorne às Sessões 4-6 após construir a primeira aplicação

### Para Desenvolvedores Intermediários (3 horas)
1. ⚡ Sessão 1: Validação rápida de configuração
2. ✅ Sessão 2: Pipeline completo de RAG com avaliação
3. ✅ Sessão 3: Suite completa de benchmarking
4. ✅ Sessão 4: Otimização de modelos
5. ✅ Sessões 5-6: Foco em padrões de arquitetura

### Para Praticantes Avançados (2-3 horas)
1. ⚡ Sessões 1-3: Revisão rápida e validação
2. ✅ Sessão 4: Mergulho profundo em otimização
3. ✅ Sessão 5: Arquitetura multi-agente
4. ✅ Sessão 6: Padrões de produção e escalabilidade
5. 🚀 Extensão: Construir lógica de roteamento personalizada e deploys híbridos

---

## Pacote de Sessões do Workshop (Laboratórios Focados de 30 Minutos)

Se você está seguindo o formato condensado de workshop de 6 sessões, use estes guias dedicados (cada um mapeia e complementa os módulos mais amplos acima):

| Sessão do Workshop | Guia | Foco Principal |
|--------------------|------|----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalar, validar, rodar phi & GPT-OSS-20B, aceleração |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Engenharia de prompts, padrões RAG, grounding de CSV e documentos, migração |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integração com Hugging Face, benchmarking, seleção de modelos |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, aceleração ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Funções de agentes, memória, ferramentas, orquestração |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Roteamento, encadeamento, escalando para o Azure |

Cada arquivo de sessão inclui: resumo, objetivos de aprendizado, fluxo de demonstração de 30 minutos, projeto inicial, lista de validação, solução de problemas e referências ao SDK oficial Foundry Local Python.

### Scripts de Exemplo

Instalar dependências do workshop (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Se estiver executando o serviço Foundry Local em uma máquina ou VM diferente (Windows) a partir de macOS, exporte o endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sessão | Script(s) | Descrição |
|--------|-----------|-----------|
| 1 | `samples/session01/chat_bootstrap.py` | Serviço de inicialização e chat em streaming |
| 2 | `samples/session02/rag_pipeline.py` | RAG mínimo (embeddings em memória) |
|   | `samples/session02/rag_eval_ragas.py` | Avaliação de RAG com métricas ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmark de latência e throughput multi-modelo |
| 4 | `samples/session04/model_compare.py` | Comparação SLM vs LLM (latência e saída de exemplo) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline de pesquisa de dois agentes → editorial |
| 6 | `samples/session06/models_router.py` | Demonstração de roteamento baseado em intenção |
|   | `samples/session06/models_pipeline.py` | Encadeamento de plano/execução/refinamento em várias etapas |

### Variáveis de Ambiente (Comuns Entre os Exemplos)

| Variável | Finalidade | Exemplo |
|----------|-----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias padrão de modelo único para exemplos básicos | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM explícito vs modelo maior para comparação | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Lista de aliases para benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Repetições de benchmark por modelo | `3` |
| `BENCH_PROMPT` | Prompt usado no benchmark | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Modelo de embeddings do Sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Substituir consulta de teste para pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Substituir consulta do pipeline de agentes | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias de modelo para agente de pesquisa | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias de modelo para agente editor (pode ser diferente) | `gpt-oss-20b` |
| `SHOW_USAGE` | Quando `1`, imprime uso de tokens por conclusão | `1` |
| `RETRY_ON_FAIL` | Quando `1`, tenta novamente em erros transitórios de chat | `1` |
| `RETRY_BACKOFF` | Segundos para esperar antes de tentar novamente | `1.0` |

Se uma variável não estiver configurada, os scripts utilizam valores padrão sensatos. Para demonstrações de modelo único, normalmente você só precisa de `FOUNDRY_LOCAL_ALIAS`.

### Módulo Utilitário

Todos os exemplos agora compartilham um helper `samples/workshop_utils.py` que fornece:

* Criação de cliente OpenAI + `FoundryLocalManager` com cache
* Helper `chat_once()` com opção de tentativa novamente + impressão de uso
* Relatório simples de uso de tokens (ativado via `SHOW_USAGE=1`)

Isso reduz duplicação e destaca as melhores práticas para orquestração eficiente de modelos locais.

## Melhorias Opcionais (Entre Sessões)

| Tema | Melhoria | Sessões | Env / Alternância |
|------|----------|---------|-------------------|
| Determinismo | Temperatura fixa + conjuntos de prompts estáveis | 1–6 | Configurar `temperature=0`, `top_p=1` |
| Visibilidade de Uso de Tokens | Ensino consistente de custo/eficiência | 1–6 | `SHOW_USAGE=1` |
| Primeiro Token em Streaming | Métrica de latência percebida | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Resiliência de Tentativa | Lida com inicialização fria transitória | Todas | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agentes Multi-Modelo | Especialização de papéis heterogêneos | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Roteamento Adaptativo | Heurísticas de intenção + custo | 6 | Estender roteador com lógica de escalonamento |
| Memória Vetorial | Recall semântico de longo prazo | 2,5,6 | Integrar índice de embeddings FAISS/Chroma |
| Exportação de Rastreamento | Auditoria e avaliação | 2,5,6 | Adicionar linhas JSON por etapa |
| Rubricas de Qualidade | Rastreamento qualitativo | 3–6 | Prompts de pontuação secundária |
| Testes de Fumaça | Validação rápida pré-workshop | Todas | `python Workshop/tests/smoke.py` |

### Início Rápido Determinístico

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Espere contagens de tokens estáveis em entradas idênticas repetidas.

### Avaliação de RAG (Sessão 2)

Use `rag_eval_ragas.py` para calcular relevância da resposta, fidelidade e precisão do contexto em um pequeno conjunto de dados sintético:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Estenda fornecendo um JSONL maior de perguntas, contextos e verdades fundamentais, depois convertendo para um `Dataset` do Hugging Face.

## Apêndice de Precisão de Comandos CLI

O workshop utiliza deliberadamente apenas comandos CLI Foundry Local documentados/estáveis atualmente.

### Comandos Estáveis Referenciados

| Categoria | Comando | Finalidade |
|-----------|---------|-----------|
| Core | `foundry --version` | Mostrar versão instalada |
| Serviço | `foundry service start` | Iniciar serviço local (se não for automático) |
| Serviço | `foundry service status` | Mostrar status do serviço |
| Modelos | `foundry model list` | Listar catálogo / modelos disponíveis |
| Modelos | `foundry model download <alias>` | Baixar pesos do modelo para o cache |
| Modelos | `foundry model run <alias>` | Iniciar (carregar) um modelo localmente; combinar com `--prompt` para execução única |
| Modelos | `foundry model unload <alias>` / `foundry model stop <alias>` | Descarregar um modelo da memória (se suportado) |
| Cache | `foundry cache list` | Listar modelos em cache (baixados) |

### Padrão de Prompt Único

Em vez de um subcomando `model chat` obsoleto, use:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Isso executa um ciclo único de prompt/resposta e então sai.

### Padrões Removidos / Evitados

| Obsoleto / Não Documentado | Substituição / Orientação |
|----------------------------|--------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Use `foundry model list` simples + atividade recente / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Use script de benchmark Python + ferramentas do sistema operacional (Gerenciador de Tarefas / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetria

- Latência, p95, tokens/segundo: `samples/session03/benchmark_oss_models.py`
- Latência do primeiro token (streaming): configurar `BENCH_STREAM=1`
- Uso de recursos: monitores do sistema operacional (Gerenciador de Tarefas, Monitor de Atividade, `nvidia-smi`).

À medida que novos comandos de telemetria CLI se estabilizam, podem ser incorporados com edições mínimas aos arquivos markdown da sessão.

### Lint Automático

Um linter automatizado impede a reintrodução de padrões CLI obsoletos dentro de blocos de código cercados em arquivos markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

Padrões obsoletos são bloqueados dentro de cercas de código.

Substituições recomendadas:
| Obsoleto | Substituição |
|----------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script de benchmark + ferramentas do sistema |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Executar localmente:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

Ação do GitHub: `.github/workflows/markdown-cli-lint.yml` executa em cada push e PR.

Hook opcional de pré-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabela de Migração Rápida CLI → SDK

| Tarefa | CLI One-Liner | Equivalente SDK (Python) | Notas |
|-------|---------------|--------------------------|-------|
| Executar um modelo uma vez (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK inicializa serviço e cache automaticamente |
| Baixar (cache) modelo | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager escolhe melhor variante se alias mapear para múltiplas versões |
| Listar catálogo | `foundry model list` | `# use manager for each alias or maintain known list` | CLI agrega; SDK atualmente por instância de alias |
| Listar modelos em cache | `foundry cache list` | `manager.list_cached_models()` | Após inicialização do manager (qualquer alias) |
| Obter URL do endpoint | (implícito) | `manager.endpoint` | Usado para criar cliente compatível com OpenAI |
| Aquecer um modelo | `foundry model run <alias>` então primeiro prompt | `chat_once(alias, messages=[...])` (utilitário) | Utilitários lidam com aquecimento inicial de latência fria |
| Medir latência | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (ou novo script exportador) | Prefira script para métricas consistentes |
| Parar / descarregar modelo | `foundry model unload <alias>` | (Não exposto – reiniciar serviço/processo) | Normalmente não necessário para fluxo de workshop |
| Recuperar uso de tokens | (ver saída) | `resp.usage.total_tokens` | Fornecido se backend retornar objeto de uso |

## Exportação de Markdown de Benchmark

Use o script `Workshop/scripts/export_benchmark_markdown.py` para executar um benchmark novo (mesma lógica de `samples/session03/benchmark_oss_models.py`) e emitir uma tabela Markdown amigável para GitHub mais JSON bruto.

### Exemplo

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Arquivos gerados:
| Arquivo | Conteúdo |
|---------|----------|
| `benchmark_report.md` | Tabela Markdown + dicas de interpretação |
| `benchmark_report.json` | Array de métricas bruto (para comparação / rastreamento de tendências) |

Configure `BENCH_STREAM=1` no ambiente para incluir latência do primeiro token, se suportado.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->