# Notebooks do Workshop

> **Notebooks Interativos Jupyter para Aprendizado Prático de Edge AI**
>
> Tutoriais progressivos e autônomos que evoluem de completions básicas de chat até sistemas avançados de múltiplos agentes usando Microsoft Foundry Local e Modelos de Linguagem Pequenos.

---

## 📖 Introdução

Bem-vindo à coleção de **Notebooks do Workshop EdgeAI para Iniciantes**. Esses notebooks interativos Jupyter oferecem uma experiência prática de aprendizado, onde você escreverá, executará e experimentará código de Edge AI em tempo real.

### Por que usar Jupyter Notebooks?

Diferente de tutoriais tradicionais, esses notebooks oferecem:

- **Aprendizado Interativo**: Execute células de código e veja os resultados imediatamente
- **Experimentação**: Modifique parâmetros e observe mudanças em tempo real
- **Documentação**: Explicações inline e células de markdown que orientam você pelos conceitos
- **Reprodutibilidade**: Exemplos completos e funcionais que você pode consultar e reutilizar
- **Visualização**: Veja métricas de desempenho, embeddings e resultados diretamente no notebook

### O que torna esses notebooks especiais?

Cada notebook foi projetado seguindo **melhores práticas para produção**:

✅ **Tratamento Abrangente de Erros** - Degradação suave e mensagens de erro informativas  
✅ **Dicas de Tipos e Documentação** - Assinaturas de funções claras e docstrings  
✅ **Monitoramento de Desempenho** - Rastreamento de uso de tokens e medições de latência  
✅ **Design Modular** - Padrões reutilizáveis que você pode adaptar aos seus projetos  
✅ **Complexidade Progressiva** - Construção sistemática com base em sessões anteriores  

---

## 🎯 Objetivos de Aprendizado

### Habilidades Principais que Você Desenvolverá

Ao trabalhar com esses notebooks, você dominará:

1. **Gerenciamento de Serviços de IA Local**
   - Configurar e gerenciar serviços Microsoft Foundry Local
   - Selecionar e carregar modelos apropriados para seu hardware
   - Monitorar uso de recursos e otimizar desempenho
   - Lidar com descoberta de serviços e verificação de saúde

2. **Desenvolvimento de Aplicações de IA**
   - Implementar completions de chat compatíveis com OpenAI localmente
   - Construir interfaces de streaming para melhor experiência do usuário
   - Projetar prompts eficazes para Modelos de Linguagem Pequenos
   - Integrar modelos locais em aplicações

3. **Geração Aumentada por Recuperação (RAG)**
   - Criar busca semântica com embeddings vetoriais
   - Basear respostas de LLM em documentos específicos do domínio
   - Avaliar qualidade de RAG com métricas RAGAS
   - Escalar de protótipo para produção

4. **Otimização de Desempenho**
   - Realizar benchmarks sistemáticos de múltiplos modelos
   - Medir latência, throughput e tempo do primeiro token
   - Comparar Modelos de Linguagem Pequenos com Modelos de Linguagem Grandes
   - Selecionar modelos ideais com base em trade-offs de desempenho/qualidade

5. **Orquestração de Múltiplos Agentes**
   - Projetar agentes especializados para diferentes tarefas
   - Implementar memória de agentes e gerenciamento de contexto
   - Coordenar múltiplos agentes em fluxos de trabalho complexos
   - Construir padrões de coordenação para colaboração entre agentes

6. **Roteamento Inteligente de Modelos**
   - Implementar detecção de intenção e correspondência de padrões
   - Roteamento automático de consultas para modelos apropriados
   - Construir pipelines de múltiplas etapas (planejar → executar → refinar)
   - Projetar arquiteturas escaláveis de modelos como ferramentas

---

## 🎓 Resultados de Aprendizado

### O que Você Vai Construir

| Notebook | Entregável | Habilidades Demonstradas | Dificuldade |
|----------|------------|--------------------------|-------------|
| **Sessão 01** | Aplicativo de chat com streaming | Configuração de serviço, completions básicas, UX de streaming | ⭐ Iniciante |
| **Sessão 02 (RAG)** | Pipeline RAG com avaliação | Embeddings, busca semântica, métricas de qualidade | ⭐⭐ Intermediário |
| **Sessão 02 (Avaliação)** | Avaliador de qualidade RAG | Métricas RAGAS, avaliação sistemática | ⭐⭐ Intermediário |
| **Sessão 03** | Benchmark de múltiplos modelos | Medição de desempenho, comparação de modelos | ⭐⭐ Intermediário |
| **Sessão 04** | Comparador SLM vs LLM | Análise de trade-offs, estratégias de otimização | ⭐⭐⭐ Avançado |
| **Sessão 05** | Orquestrador de múltiplos agentes | Design de agentes, memória, coordenação | ⭐⭐⭐ Avançado |
| **Sessão 06 (Roteador)** | Sistema de roteamento inteligente | Detecção de intenção, seleção de modelos | ⭐⭐⭐ Avançado |
| **Sessão 06 (Pipeline)** | Pipeline de múltiplas etapas | Fluxos de trabalho de planejar/executar/refinar | ⭐⭐⭐ Avançado |

### Progressão de Competências

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Cronograma do Workshop

### 🚀 Workshop de Meio Dia (3,5 horas)

**Perfeito para: Treinamento de equipes, hackathons, workshops em conferências**

| Horário | Duração | Sessão | Tópicos | Atividades |
|---------|---------|--------|---------|------------|
| **0:00** | 30 min | Configuração e Introdução | Configuração do ambiente, instalação do Foundry Local | Instalar dependências, verificar configuração |
| **0:30** | 30 min | Sessão 01 | Completions básicas de chat, streaming | Executar notebook, modificar prompts |
| **1:00** | 45 min | Sessão 02 | Pipeline RAG, embeddings, avaliação | Construir sistema RAG, testar consultas |
| **1:45** | 15 min | Intervalo | ☕ Café e perguntas | — |
| **2:00** | 30 min | Sessão 03 | Benchmark de múltiplos modelos | Comparar 3+ modelos |
| **2:30** | 30 min | Sessão 04 | Trade-offs SLM vs LLM | Analisar desempenho/qualidade |
| **3:00** | 30 min | Sessão 05-06 | Sistemas de múltiplos agentes e roteamento | Explorar padrões avançados |

**Resultado**: Os participantes saem com 6 aplicações de Edge AI funcionais e padrões de código prontos para produção.

---

### 🎓 Workshop de Dia Inteiro (6 horas)

**Perfeito para: Treinamento aprofundado, bootcamps, cursos universitários**

| Horário | Duração | Sessão | Tópicos | Atividades |
|---------|---------|--------|---------|------------|
| **0:00** | 45 min | Configuração e Teoria | Configuração do ambiente, fundamentos de Edge AI | Instalar, verificar, discutir casos de uso |
| **0:45** | 45 min | Sessão 01 | Completions de chat aprofundadas | Implementar chat básico e streaming |
| **1:30** | 30 min | Intervalo | ☕ Café e networking | — |
| **2:00** | 60 min | Sessão 02 (Ambas) | Pipeline RAG + Avaliação RAGAS | Construir sistema RAG completo |
| **3:00** | 30 min | Laboratório Prático 1 | RAG personalizado para seu domínio | Aplicar a seus próprios documentos |
| **3:30** | 30 min | Almoço | 🍽️ | — |
| **4:00** | 45 min | Sessão 03 | Metodologia de benchmarking | Comparação sistemática de modelos |
| **4:45** | 45 min | Sessão 04 | Estratégias de otimização | Análise SLM vs LLM |
| **5:30** | 60 min | Sessão 05-06 | Orquestração avançada | Sistemas de múltiplos agentes, roteamento |
| **6:30** | 30 min | Laboratório Prático 2 | Construir sistema de agentes personalizado | Projetar seu próprio orquestrador |

**Resultado**: Compreensão profunda de padrões de Edge AI e 2 projetos personalizados.

---

### 📚 Aprendizado Autônomo (2 semanas)

**Perfeito para: Aprendizes individuais, cursos online, estudo independente**

#### Semana 1: Fundamentos (6 horas)

| Dia | Foco | Duração | Notebooks | Tarefa |
|-----|------|---------|-----------|--------|
| **Seg** | Configuração e Básico | 1,5 hrs | Sessão 01 | Modificar prompts, testar streaming |
| **Qua** | Fundamentos de RAG | 2 hrs | Sessão 02 (ambas) | Adicionar seus próprios documentos |
| **Sex** | Benchmarking | 1,5 hrs | Sessão 03 | Comparar modelos adicionais |
| **Sáb** | Revisão e Prática | 1 hr | Todos da Semana 1 | Completar exercícios, depurar |

#### Semana 2: Avançado (5 horas)

| Dia | Foco | Duração | Notebooks | Tarefa |
|-----|------|---------|-----------|--------|
| **Seg** | Otimização | 1,5 hrs | Sessão 04 | Documentar trade-offs |
| **Qua** | Sistemas de Múltiplos Agentes | 2 hrs | Sessão 05 | Projetar agentes personalizados |
| **Sex** | Roteamento Inteligente | 1,5 hrs | Sessão 06 (ambas) | Construir lógica de roteamento |
| **Sáb** | Projeto Final | 2 hrs | Integração | Combinar múltiplos padrões |

**Resultado**: Domínio de padrões de Edge AI e projeto de portfólio.

---

## 📔 Descrições dos Notebooks

### 📘 Sessão 01: Bootstrap de Chat
**Arquivo**: `session01_chat_bootstrap.ipynb`  
**Duração**: 20-30 minutos  
**Pré-requisitos**: Nenhum  
**Dificuldade**: ⭐ Iniciante

**O que Você Vai Aprender**:
- Instalar e configurar o SDK Python do Foundry Local
- Usar `FoundryLocalManager` para descoberta automática de serviços
- Implementar completions básicas de chat com API compatível com OpenAI
- Construir respostas em streaming para melhor experiência do usuário
- Lidar com erros e indisponibilidade de serviços de forma eficaz

**Conceitos-Chave**: Gerenciamento de serviços, completions de chat, streaming, tratamento de erros

**Você Vai Construir**: Aplicativo de chat interativo com suporte a streaming

---

### 📗 Sessão 02: Pipeline RAG
**Arquivo**: `session02_rag_pipeline.ipynb`  
**Duração**: 30-45 minutos  
**Pré-requisitos**: Sessão 01  
**Dificuldade**: ⭐⭐ Intermediário

**O que Você Vai Aprender**:
- Implementar o padrão de Geração Aumentada por Recuperação (RAG)
- Criar embeddings vetoriais com sentence-transformers
- Construir busca semântica com similaridade cosseno
- Basear respostas de LLM em documentos do domínio
- Lidar com dependências opcionais usando guardas de importação

**Conceitos-Chave**: Arquitetura RAG, embeddings, busca semântica, similaridade vetorial

**Você Vai Construir**: Sistema de perguntas e respostas baseado em documentos

---

### 📗 Sessão 02: Avaliação RAG com RAGAS
**Arquivo**: `session02_rag_eval_ragas.ipynb`  
**Duração**: 30-45 minutos  
**Pré-requisitos**: Pipeline RAG da Sessão 02  
**Dificuldade**: ⭐⭐ Intermediário

**O que Você Vai Aprender**:
- Avaliar qualidade de RAG com métricas padrão da indústria
- Medir relevância de contexto, relevância de resposta, fidelidade
- Usar o framework RAGAS para avaliação sistemática
- Identificar e corrigir problemas de qualidade em RAG
- Construir conjuntos de dados de avaliação para seu domínio

**Conceitos-Chave**: Avaliação RAG, métricas RAGAS, medição de qualidade, testes sistemáticos

**Você Vai Construir**: Framework de avaliação de qualidade RAG

---

### 📙 Sessão 03: Benchmark de Modelos OSS
**Arquivo**: `session03_benchmark_oss_models.ipynb`  
**Duração**: 30-45 minutos  
**Pré-requisitos**: Sessão 01  
**Dificuldade**: ⭐⭐ Intermediário

**O que Você Vai Aprender**:
- Realizar benchmarks sistemáticos de múltiplos modelos
- Medir latência, throughput, tempo do primeiro token
- Implementar degradação suave para falhas de modelos
- Comparar desempenho entre famílias de modelos
- Visualizar e analisar resultados de benchmarks

**Conceitos-Chave**: Benchmarking de desempenho, medição de latência, comparação de modelos, análise estatística

**Você Vai Construir**: Suite de benchmarking de múltiplos modelos

---

### 📙 Sessão 04: Comparação de Modelos (SLM vs LLM)
**Arquivo**: `session04_model_compare.ipynb`  
**Duração**: 30-45 minutos  
**Pré-requisitos**: Sessões 01, 03  
**Dificuldade**: ⭐⭐⭐ Avançado

**O que Você Vai Aprender**:
- Comparar Modelos de Linguagem Pequenos com Modelos de Linguagem Grandes
- Analisar trade-offs entre desempenho e qualidade
- Medir métricas de adequação para edge
- Selecionar modelos ideais para restrições de implantação
- Documentar critérios de decisão para seleção de modelos

**Conceitos-Chave**: Seleção de modelos, análise de trade-offs, estratégias de otimização, planejamento de implantação

**Você Vai Construir**: Framework de comparação SLM vs LLM

---

### 📕 Sessão 05: Orquestrador de Múltiplos Agentes
**Arquivo**: `session05_agents_orchestrator.ipynb`  
**Duração**: 45-60 minutos  
**Pré-requisitos**: Sessões 01-02  
**Dificuldade**: ⭐⭐⭐ Avançado

**O que Você Vai Aprender**:
- Projetar agentes especializados para diferentes tarefas
- Implementar memória de agentes e gerenciamento de contexto
- Construir padrões de coordenação para colaboração entre agentes
- Lidar com comunicação e transferência entre agentes
- Monitorar desempenho de sistemas de múltiplos agentes

**Conceitos-Chave**: Arquitetura de agentes, padrões de coordenação, gerenciamento de memória, orquestração de agentes

**Você Vai Construir**: Sistema de múltiplos agentes com coordenador e especialistas

---

### 📕 Sessão 06: Roteador de Modelos
**Arquivo**: `session06_models_router.ipynb`  
**Duração**: 30-45 minutos  
**Pré-requisitos**: Sessões 01, 03  
**Dificuldade**: ⭐⭐⭐ Avançado

**O que Você Vai Aprender**:
- Implementar detecção de intenção e correspondência de padrões
- Construir roteamento de modelos baseado em palavras-chave
- Roteamento automático de consultas para modelos apropriados
- Configurar registros de múltiplos modelos
- Monitorar decisões de roteamento e desempenho

**Conceitos-Chave**: Detecção de intenção, roteamento de modelos, correspondência de padrões, seleção inteligente

**Você Vai Construir**: Sistema de roteamento inteligente de modelos

---

### 📕 Sessão 06: Pipeline de Múltiplas Etapas
**Arquivo**: `session06_models_pipeline.ipynb`  
**Duração**: 30-45 minutos  
**Pré-requisitos**: Sessões 01, Roteador da Sessão 06  
**Dificuldade**: ⭐⭐⭐ Avançado

**O que Você Vai Aprender**:
- Construir pipelines de IA de múltiplas etapas (planejar → executar → refinar)
- Integrar roteador para seleção inteligente de modelos
- Implementar tratamento de erros e recuperação no pipeline
- Monitorar desempenho e estágios do pipeline
- Projetar arquiteturas escaláveis de modelos como ferramentas

**Conceitos-chave**: Arquitetura de pipeline, processamento em múltiplas etapas, recuperação de erros, padrões de escalabilidade

**Você Vai Construir**: Pipeline inteligente de múltiplas etapas com roteamento

---

## 🚀 Começando

### Pré-requisitos

**Requisitos do Sistema**:
- **Sistema Operacional**: Windows 10/11, macOS 11+ ou Linux (Ubuntu 20.04+)
- **RAM**: Mínimo de 8GB, recomendado 16GB+
- **Armazenamento**: 10GB+ de espaço livre para modelos
- **Hardware**: CPU com AVX2; GPU (CUDA, Qualcomm NPU) opcional

**Requisitos de Software**:
- **Python 3.8+** com pip
- **Jupyter Notebook** ou **VS Code** com extensão Jupyter
- **Microsoft Foundry Local** instalado e configurado
- **Git** (para clonar o repositório)

### Passos de Instalação

#### 1. Instalar Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificar Instalação**:
```bash
foundry --version
```

#### 2. Configurar Ambiente Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Iniciar Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Abrir Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Verificação Rápida

Execute este comando em uma célula Python para verificar a configuração:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Saída Esperada**: Uma resposta de saudação do modelo local.

---

## 📝 Melhores Práticas para o Workshop

### Para Instrutores

**Antes do Workshop**:
- ✅ Enviar instruções de instalação com 1 semana de antecedência
- ✅ Testar todos os notebooks no hardware alvo
- ✅ Preparar um guia de solução de problemas para questões comuns
- ✅ Ter modelos de backup prontos (phi-3.5-mini se phi-4-mini falhar)
- ✅ Configurar um canal de chat compartilhado para dúvidas

**Durante o Workshop**:
- ✅ Começar com uma verificação rápida do ambiente (5 minutos)
- ✅ Compartilhar recursos de solução de problemas imediatamente
- ✅ Incentivar experimentação e modificações
- ✅ Usar pausas estrategicamente (após cada 2 sessões)
- ✅ Ter assistentes disponíveis para ajuda individual

**Após o Workshop**:
- ✅ Compartilhar notebooks completos e soluções
- ✅ Fornecer links para recursos adicionais
- ✅ Criar uma pesquisa de feedback para melhorias
- ✅ Oferecer horários de atendimento para dúvidas posteriores

### Para Participantes

**Maximize Seu Aprendizado**:
- ✅ Complete a configuração antes do início do workshop
- ✅ Execute cada célula de código você mesmo (não apenas leia)
- ✅ Experimente parâmetros e prompts
- ✅ Faça anotações sobre insights e dificuldades
- ✅ Pergunte quando estiver com dúvidas (outros podem ter a mesma dúvida)

**Erros Comuns a Evitar**:
- ❌ Ignorar a ordem de execução das células (execute sequencialmente)
- ❌ Não ler mensagens de erro com atenção
- ❌ Correr sem entender o conteúdo
- ❌ Ignorar explicações em markdown
- ❌ Não salvar seus notebooks modificados

**Dicas de Depuração**:
1. **Serviço Não Está Rodando**: Verifique `foundry service status`
2. **Erros de Importação**: Certifique-se de que o ambiente virtual está ativado
3. **Modelo Não Encontrado**: Execute `foundry model ls` para listar os modelos carregados
4. **Desempenho Lento**: Verifique o uso de RAM, feche outros aplicativos
5. **Resultados Inesperados**: Reinicie o kernel e execute todas as células desde o início

---

## 🔗 Recursos Adicionais

### Materiais do Workshop

- **[Guia Principal do Workshop](../Readme.md)** - Visão geral, objetivos de aprendizado, resultados de carreira
- **[Exemplos em Python](../../../../Workshop/samples)** - Scripts Python correspondentes a cada sessão
- **[Guias das Sessões](../../../../Workshop)** - Guias detalhados em markdown (Sessão01-06)
- **[Scripts](../../../../Workshop/scripts)** - Utilitários de validação e teste
- **[Solução de Problemas](./TROUBLESHOOTING.md)** - Questões comuns e soluções
- **[Guia Rápido](./quickstart.md)** - Guia rápido para começar

### Documentação

- **[Documentação do Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Documentação oficial da Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referência do SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Documentação de modelos de embeddings
- **[Framework RAGAS](https://docs.ragas.io/)** - Métricas de avaliação RAG

### Comunidade

- **[Discussões no GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Faça perguntas, compartilhe projetos
- **[Discord do Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Suporte comunitário em tempo real
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Perguntas e respostas técnicas

---

## 🎯 Recomendações de Caminho de Aprendizado

### Trilha para Iniciantes (Comece Aqui)

1. **Sessão 01** - Inicialização do Chat
2. **Sessão 02** - Pipeline RAG
3. **Sessão 03** - Benchmark de Modelos

**Tempo**: ~2 horas | **Foco**: Padrões fundamentais

---

### Trilha Intermediária

1. Complete a Trilha para Iniciantes
2. **Sessão 02** - Avaliação RAG
3. **Sessão 04** - Comparação de Modelos

**Tempo**: ~4 horas | **Foco**: Qualidade e otimização

---

### Trilha Avançada (Workshop Completo)

1. Complete a Trilha Intermediária
2. **Sessão 05** - Orquestrador Multi-Agente
3. **Sessão 06** - Roteador de Modelos
4. **Sessão 06** - Pipeline de Múltiplas Etapas

**Tempo**: ~6 horas | **Foco**: Padrões de produção

---

### Trilha de Projeto Personalizado

1. Complete a Trilha para Iniciantes (Sessões 01-03)
2. Escolha UMA sessão avançada com base no seu objetivo:
   - **Construindo um app RAG?** → Sessão 02 Avaliação
   - **Otimizando desempenho?** → Sessão 04 Comparação
   - **Workflows complexos?** → Sessão 05 Orquestrador
   - **Arquitetura escalável?** → Sessão 06 Roteador + Pipeline

**Tempo**: ~3 horas | **Foco**: Habilidades específicas para projetos

---

## 📊 Métricas de Sucesso

Acompanhe seu progresso com estes marcos:

- [ ] **Configuração Completa** - Foundry Local funcionando, todas as dependências instaladas
- [ ] **Primeiro Chat** - Sessão 01 concluída, chat em streaming funcionando
- [ ] **RAG Construído** - Sessão 02 concluída, sistema de QA de documentos funcional
- [ ] **Modelos Avaliados** - Sessão 03 concluída, dados de desempenho coletados
- [ ] **Análise de Trade-offs** - Sessão 04 concluída, critérios de seleção de modelos documentados
- [ ] **Agentes Orquestrados** - Sessão 05 concluída, sistema multi-agente funcionando
- [ ] **Roteamento Implementado** - Sessão 06 concluída, seleção inteligente de modelos funcional
- [ ] **Projeto Personalizado** - Aplicou padrões do workshop ao seu próprio caso de uso

---

## 🤝 Contribuindo

Encontrou um problema ou tem uma sugestão? Aceitamos contribuições!

- **Relatar Problemas**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Sugerir Melhorias**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Enviar PRs**: Siga as [Diretrizes de Contribuição](../../AGENTS.md)

---

## 📄 Licença

Este workshop faz parte do repositório [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) e está licenciado sob a [Licença MIT](../../../../LICENSE).

---

**Pronto para construir aplicações Edge AI prontas para produção?**  
**Comece com [Sessão 01: Inicialização do Chat](./session01_chat_bootstrap.ipynb) →**

---

*Última Atualização: 8 de outubro de 2025 | Versão do Workshop: 2.0*

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.