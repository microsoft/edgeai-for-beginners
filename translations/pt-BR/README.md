# EdgeAI para Iniciantes 


![Imagem de capa do curso](../../translated_images/pt-BR/cover.eb18d1b9605d754b.webp)

[![Contribuidores do GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Issues do GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull Requests do GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Bem-vindos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Observadores do GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forks do GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Estrelas do GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Siga estas etapas para começar a usar esses recursos:

1. **Faça um Fork do Repositório**: Clique em [![Forks do GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone o Repositório**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Participe do Azure AI Foundry Discord e conheça especialistas e outros desenvolvedores**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Suporte Multilíngue

#### Suportado via GitHub Action (Automatizado & Sempre Atualizado)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengali](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmanês (Myanmar)](../my/README.md) | [Chinês (Simplificado)](../zh-CN/README.md) | [Chinês (Tradicional, Hong Kong)](../zh-HK/README.md) | [Chinês (Tradicional, Macau)](../zh-MO/README.md) | [Chinês (Tradicional, Taiwan)](../zh-TW/README.md) | [Croata](../hr/README.md) | [Tcheco](../cs/README.md) | [Dinamarquês](../da/README.md) | [Holandês](../nl/README.md) | [Estoniano](../et/README.md) | [Finlandês](../fi/README.md) | [Francês](../fr/README.md) | [Alemão](../de/README.md) | [Grego](../el/README.md) | [Hebraico](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonésio](../id/README.md) | [Italiano](../it/README.md) | [Japonês](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malaio](../ms/README.md) | [Malaiala](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Norueguês](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polonês](../pl/README.md) | [Português (Brasil)](./README.md) | [Português (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Espanhol](../es/README.md) | [Suaíli](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tâmil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandês](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **Prefere Clonar Localmente?**
>
> Este repositório inclui mais de 50 traduções de idiomas, o que aumenta significativamente o tamanho do download. Para clonar sem as traduções, use sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Isso fornece tudo que você precisa para completar o curso com um download muito mais rápido.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Se desejar que idiomas adicionais sejam suportados, consulte a lista [aqui](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introdução

Bem-vindo ao **EdgeAI para Iniciantes** – sua jornada completa no mundo transformador da Inteligência Artificial na Borda. Este curso conecta as poderosas capacidades da IA à implantação prática e real em dispositivos de borda, permitindo que você aproveite o potencial da IA diretamente onde os dados são gerados e as decisões precisam ser tomadas.

### O que Você Irá Dominar

Este curso leva você dos conceitos fundamentais até implementações prontas para produção, abordando:
- **Modelos Pequenos de Linguagem (SLMs)** otimizados para implantação na borda
- **Otimização consciente de hardware** em múltiplas plataformas
- **Inferência em tempo real** com capacidades de preservação da privacidade
- **Estratégias de implantação em produção** para aplicações empresariais

### Por que EdgeAI é Importante

Edge AI representa uma mudança de paradigma que resolve desafios modernos críticos:
- **Privacidade & Segurança**: Processa dados sensíveis localmente sem exposição à nuvem
- **Desempenho em tempo real**: Elimina latência de rede para aplicações com restrição de tempo
- **Eficiência de custo**: Reduz custo de largura de banda e computação em nuvem
- **Operações resilientes**: Mantém funcionalidade durante quedas de rede
- **Conformidade regulatória**: Atende requisitos de soberania de dados

### Edge AI

Edge AI refere-se à execução de algoritmos de IA e modelos de linguagem localmente no hardware, próximo ao local onde os dados são gerados, sem depender de recursos na nuvem para inferência. Isso reduz a latência, aumenta a privacidade e permite decisões em tempo real.

### Princípios Centrais:
- **Inferência no dispositivo**: Modelos de IA executados em dispositivos de borda (celulares, roteadores, microcontroladores, PCs industriais)
- **Capacidade offline**: Funciona sem conectividade persistente com a internet
- **Baixa latência**: Respostas imediatas adequadas para sistemas em tempo real
- **Soberania de dados**: Mantém dados sensíveis localmente, melhorando segurança e conformidade

### Modelos Pequenos de Linguagem (SLMs)

SLMs como Phi-4, Mistral-7B e Gemma são versões otimizadas de grandes modelos de linguagem (LLMs) — treinados ou destilados para:
- **Pegada de memória reduzida**: Uso eficiente de memória limitada em dispositivos de borda
- **Menor demanda computacional**: Otimizado para desempenho em CPU e GPU de borda
- **Tempos de inicialização mais rápidos**: Inicialização rápida para aplicações responsivas

Eles desbloqueiam poderosas capacidades de PLN enquanto atendem às restrições de:
- **Sistemas embarcados**: Dispositivos IoT e controladores industriais
- **Dispositivos móveis**: Smartphones e tablets com capacidades offline
- **Dispositivos IoT**: Sensores e dispositivos inteligentes com recursos limitados
- **Servidores de borda**: Unidades de processamento local com recursos limitados de GPU
- **Computadores pessoais**: Cenários de implantação em desktop e laptop

## Módulos do Curso & Navegação

| Módulo | Tópico | Área de Foco | Conteúdo Principal | Nível | Duração |
|--------|--------|--------------|--------------------|--------|---------|
| [📖 00 ](./introduction.md) | [Introdução ao EdgeAI](./introduction.md) | Fundamentos & Contexto | Visão geral do EdgeAI • Aplicações na indústria • Introdução ao SLM • Objetivos de aprendizagem | Iniciante | 1-2 h |
| [📚 01](../../Module01) | [Fundamentos do EdgeAI](./Module01/README.md) | Comparação entre Nuvem e Edge AI | Fundamentos do EdgeAI • Estudos de Caso Reais • Guia de Implementação • Implantação na Borda | Iniciante | 3-4 h |
| [🧠 02](../../Module02) | [Fundamentos do Modelo SLM](./Module02/README.md) | Famílias e arquitetura de modelos | Família Phi • Família Qwen • Família Gemma • BitNET • μModel • Phi-Silica | Iniciante | 4-5 h |
| [🚀 03](../../Module03) | [Prática de Implantação SLM](./Module03/README.md) | Implantação local & na nuvem | Aprendizado Avançado • Ambiente Local • Implantação na Nuvem | Intermediário | 4-5 h |
| [⚙️ 04](../../Module04) | [Kit de Ferramentas para Otimização de Modelos](./Module04/README.md) | Otimização multiplataforma | Introdução • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Síntese do Fluxo de Trabalho | Intermediário | 5-6 h |
| [🔧 05](../../Module05) | [SLMOps em Produção](./Module05/README.md) | Operações em produção | Introdução ao SLMOps • Destilação de Modelos • Fine-tuning • Implantação em Produção | Avançado | 5-6 h |
| [🤖 06](../../Module06) | [Agentes de IA & Chamada de Funções](./Module06/README.md) | Frameworks de agentes & MCP | Introdução a Agentes • Chamada de Funções • Protocolo de Contexto do Modelo | Avançado | 4-5 h |
| [💻 07](../../Module07) | [Implementação em Plataforma](./Module07/README.md) | Exemplos multiplataforma | Kit de Ferramentas de IA • Foundry Local • Desenvolvimento Windows | Avançado | 3-4 h |
| [🏭 08](../../Module08) | [Kit de Ferramentas Foundry Local](./Module08/README.md) | Exemplos prontos para produção | Aplicações de exemplo (veja detalhes abaixo) | Especialista | 8-10 h |

### 🏭 **Módulo 08: Aplicações de Exemplo**

- [01: Quickstart Chat REST](./Module08/samples/01/README.md)
- [02: Integração OpenAI SDK](./Module08/samples/02/README.md)
- [03: Descoberta & Benchmarking de Modelos](./Module08/samples/03/README.md)
- [04: Aplicação Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orquestração Multi-Agentes](./Module08/samples/05/README.md)
- [06: Router Modelos-como-Ferramentas](./Module08/samples/06/README.md)
- [07: Cliente API Direto](./Module08/samples/07/README.md)
- [08: App de Chat Windows 11](./Module08/samples/08/README.md)
- [09: Sistema Multi-Agente Avançado](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Caminho de Aprendizagem Prático**

Materiais abrangentes para workshop prático com implementações prontas para produção:

- **[Guia do Workshop](./Workshop/Readme.md)** - Objetivos de aprendizagem completos, resultados e navegação pelos recursos
- **Exemplos em Python** (6 sessões) - Atualizados com melhores práticas, tratamento de erros e documentação completa
- **Notebooks Jupyter** (8 interativos) - Tutoriais passo a passo com benchmarks e monitoramento de desempenho
- **Guias de Sessão** - Guias detalhados em markdown para cada sessão do workshop
- **Ferramentas de Validação** - Scripts para verificar qualidade do código e executar testes básicos

**O que Você Vai Construir:**
- Aplicações locais de chat com suporte a streaming
- Pipelines RAG com avaliação de qualidade (RAGAS)
- Ferramentas de benchmarking e comparação multi-modelo
- Sistemas de orquestração multi-agentes
- Roteamento inteligente de modelos com seleção baseada em tarefas

### 🎙️ **Workshop Para Agentic: Mão na Massa - O Estúdio de Podcast de IA**
Construa uma linha de produção de podcast movida a IA do zero! Este workshop imersivo ensina você a criar um sistema multiagente completo que transforma ideias em episódios profissionais de podcast.

**[🎬 Comece o Workshop AI Podcast Studio](./WorkshopForAgentic/README.md)**

**Sua Missão**: Lançar o "Future Bytes" — um podcast de tecnologia totalmente alimentado por agentes de IA que você mesmo construirá. Sem dependências na nuvem, sem custos de API — tudo funciona localmente na sua máquina.

**O Que Torna Isto Único:**
- **🤖 Orquestração Multiagente Real** - Construa agentes de IA especializados que pesquisam, escrevem e produzem áudio
- **🎯 Linha Completa de Produção** - Da seleção do tema ao áudio final do podcast
- **💻 Implantação 100% Local** - Usa Ollama e modelos locais (Qwen-3-8B) para total privacidade e controle
- **🎤 Integração Texto para Fala** - Transforma roteiros em conversas naturais com múltiplos locutores
- **✋ Fluxos de Trabalho com Humanos no Loop** - Portões de aprovação garantem qualidade mantendo a automação

**Jornada de Aprendizagem em Três Atos:**

| Ato | Foco | Habilidades Chave | Duração |
|-----|-------|------------|----------|
| **[Ato 1: Conheça seus Assistentes de IA](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Construa seu primeiro agente de IA | Integração de ferramentas • Busca na web • Resolução de problemas • Raciocínio agente | 2-3 hrs |
| **[Ato 2: Monte sua Equipe de Produção](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orquestre múltiplos agentes | Coordenação de equipe • Fluxos de aprovação • Interface DevUI • Supervisão humana | 3-4 hrs |
| **[Ato 3: Dê Vida ao Seu Podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Gere áudio do podcast | Texto para fala • Síntese com múltiplos locutores • Áudio de longa duração • Automação total | 2-3 hrs |

**Tecnologias Utilizadas:**
- **Microsoft Agent Framework** - Orquestração e coordenação multiagente
- **Ollama** - Runtime local de modelo de IA (sem necessidade de nuvem)
- **Qwen-3-8B** - Modelo de linguagem open-source otimizado para tarefas agentes
- **APIs de Texto para Fala** - Síntese de voz natural para geração de podcast

**Suporte de Hardware:**
- ✅ **Modo CPU** - Funciona em qualquer computador moderno (recomendado 8GB+ RAM)
- 🚀 **Aceleração GPU** - Inferência significativamente mais rápida com GPUs NVIDIA/AMD
- ⚡ **Suporte NPU** - Aceleração por unidade neural de próxima geração

**Perfeito Para:**
- Desenvolvedores aprendendo sistemas de IA multiagente
- Quem se interessa por automação de IA e fluxos de trabalho
- Criadores de conteúdo explorando produção assistida por IA
- Estudantes estudando padrões práticos de orquestração de IA

**Comece Agora**: [🎙️ The AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Resumo do Caminho de Aprendizagem**
- **Duração Total**: 36-45 horas
- **Iniciante**: Módulos 01-02 (7-9 horas)  
- **Intermediário**: Módulos 03-04 (9-11 horas)
- **Avançado**: Módulos 05-07 (12-15 horas)
- **Expert**: Módulo 08 (8-10 horas)

## O Que Você Vai Construir

### 🎯 Competências Centrais
- **Arquitetura Edge AI**: Projetar sistemas de IA locais com integração na nuvem
- **Otimização de Modelos**: Quantizar e comprimir modelos para implantação na borda (85% mais rápido, 75% menor)
- **Implantação Multiplataforma**: Windows, mobile, embarcados e sistemas híbridos nuvem-borda
- **Operações de Produção**: Monitoramento, escalabilidade e manutenção de IA na borda em produção

### 🏗️ Projetos Práticos
- **Aplicativos Locais Foundry Chat**: Aplicativo nativo Windows 11 com troca de modelos
- **Sistemas Multiagente**: Coordenador com agentes especialistas para fluxos complexos  
- **Aplicações RAG**: Processamento local de documentos com busca vetorial
- **Roteadores de Modelos**: Seleção inteligente entre modelos segundo análise da tarefa
- **Frameworks de API**: Clientes prontos para produção com streaming e monitoramento de saúde
- **Ferramentas Cross-Platform**: Padrões de integração LangChain/Semantic Kernel

### 🏢 Aplicações Industriais
**Manufatura** • **Saúde** • **Veículos Autônomos** • **Cidades Inteligentes** • **Apps Mobile**

## Começando Rápido

**Caminho de Aprendizagem Recomendado** (20-30 horas no total):

0. **📖 Introdução** ([Introduction.md](./introduction.md)): Fundamentos EdgeAI + contexto da indústria + framework de aprendizagem
1. **📚 Fundamentos** (Módulos 01-02): Conceitos EdgeAI + famílias de modelos SLM
2. **⚙️ Otimização** (Módulos 03-04): Implantação + frameworks de quantização  
3. **🚀 Produção** (Módulos 05-06): SLMOps + agentes de IA + chamadas de função
4. **💻 Implementação** (Módulos 07-08): Exemplos de plataforma + kit Foundry Local

Cada módulo inclui teoria, exercícios práticos e amostras de código prontas para produção.

## Impacto na Carreira

**Cargos Técnicos**: Arquiteto de Soluções EdgeAI • Engenheiro ML (Edge) • Desenvolvedor AI IoT • Desenvolvedor AI Mobile

**Setores Industriais**: Manufatura 4.0 • Tecnologia em Saúde • Sistemas Autônomos • FinTech • Eletrônicos de Consumo

**Projetos para Portfólio**: Sistemas multiagente • Aplicações RAG em produção • Implantação cross-platform • Otimização de desempenho

## Estrutura do Repositório

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Destaques do Curso

✅ **Aprendizado Progressivo**: Teoria → Prática → Implantação em produção  
✅ **Estudos de Caso Reais**: Microsoft, Japan Airlines, implementações corporativas  
✅ **Exemplos Práticos**: 50+ exemplos, 10 demos completas Foundry Local  
✅ **Foco em Performance**: Melhorias de velocidade de 85%, reduções de tamanho de 75%  
✅ **Multiplataforma**: Windows, mobile, embarcado, híbrido nuvem-borda  
✅ **Pronto para Produção**: Monitoramento, escalabilidade, segurança, conformidade

📖 **[Guia de Estudo Disponível](STUDY_GUIDE.md)**: Caminho de aprendizado estruturado de 20 horas com orientação de tempo e ferramentas de autoavaliação.

---

**EdgeAI representa o futuro da implantação de IA**: local primeiro, preservando privacidade e eficiente. Domine essas habilidades para construir a próxima geração de aplicações inteligentes.

## Outros Cursos

Nossa equipe produz outros cursos! Confira:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j para Iniciantes](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js para Iniciantes](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain para Iniciantes](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentes
[![AZD para Iniciantes](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI para Iniciantes](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP para Iniciantes](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agentes de IA para Iniciantes](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série de IA Generativa
[![IA Generativa para Iniciantes](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Aprendizado Core
[![ML para Iniciantes](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciência de Dados para Iniciantes](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![IA para Iniciantes](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cibersegurança para Iniciantes](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Desenvolvimento Web para Iniciantes](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT para Iniciantes](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Desenvolvimento XR para Iniciantes](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot

[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obtendo Ajuda

Se você ficar preso ou tiver alguma dúvida sobre como construir aplicativos de IA, participe:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se você tiver feedback sobre o produto ou erros durante a construção, visite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->