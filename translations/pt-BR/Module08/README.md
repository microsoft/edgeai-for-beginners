# Módulo 08: Prática com Microsoft Foundry Local - Kit Completo para Desenvolvedores

## Visão Geral

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) representa a próxima geração de desenvolvimento de IA na borda, oferecendo aos desenvolvedores ferramentas poderosas para criar, implantar e escalar aplicações de IA localmente, mantendo integração perfeita com o Azure AI Foundry. Este módulo fornece uma cobertura abrangente do Foundry Local, desde a instalação até o desenvolvimento avançado de agentes.

**Principais Tecnologias:**
- CLI e SDK do Microsoft Foundry Local
- Integração com Azure AI Foundry
- Inferência de modelos no dispositivo
- Cache e otimização de modelos locais
- Arquiteturas baseadas em agentes

## Objetivos de Aprendizagem

Ao concluir este módulo, você será capaz de:

- **Dominar o Foundry Local**: Instalar, configurar e otimizar para desenvolvimento no Windows 11
- **Implantar Modelos Diversos**: Executar modelos phi, qwen, deepseek e GPT localmente com comandos CLI
- **Criar Soluções de Produção**: Desenvolver aplicações de IA com engenharia avançada de prompts e integração de dados
- **Aproveitar o Ecossistema Open-Source**: Integrar modelos do Hugging Face e contribuições da comunidade
- **Desenvolver Agentes de IA**: Construir agentes inteligentes com capacidades de grounding e orquestração
- **Implementar Padrões Empresariais**: Criar soluções de IA modulares e escaláveis para implantação em produção

## Estrutura da Sessão

### [1: Introdução ao Foundry Local](./01.FoundryLocalSetup.md)
**Foco**: Instalação, configuração do CLI, implantação de modelos e otimização de hardware

**Tópicos Principais**: Instalação completa • Comandos CLI • Cache de modelos • Aceleração de hardware • Implantação de múltiplos modelos

**Exemplo**: [Início Rápido com REST Chat](./samples/01/README.md) • [Integração com OpenAI SDK](./samples/02/README.md) • [Descoberta e Benchmarking de Modelos](./samples/03/README.md)

**Duração**: 2-3 horas | **Nível**: Iniciante

---

### [2: Construindo Soluções de IA com Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Foco**: Engenharia avançada de prompts, integração de dados e conectividade com a nuvem

**Tópicos Principais**: Engenharia de prompts • Integração de dados • Fluxos de trabalho no Azure • Otimização de desempenho • Monitoramento

**Exemplo**: [Aplicação Chainlit RAG](./samples/04/README.md)

**Duração**: 2-3 horas | **Nível**: Intermediário

---

### [3: Modelos Open-Source no Foundry Local](./03.OpenSourceModels.md)
**Foco**: Integração com Hugging Face, estratégias BYOM e modelos da comunidade

**Tópicos Principais**: Integração com Hugging Face • Traga seu próprio modelo (BYOM) • Insights do Model Mondays • Contribuições da comunidade • Seleção de modelos

**Exemplo**: [Orquestração Multi-Agente](./samples/05/README.md)

**Duração**: 2-3 horas | **Nível**: Intermediário

---

### [4: Explorando Modelos de Ponta](./04.CuttingEdgeModels.md)
**Foco**: LLMs vs SLMs, implementação de EdgeAI e demonstrações avançadas

**Tópicos Principais**: Comparação de modelos • Inferência na borda vs na nuvem • Phi + ONNX Runtime • Aplicação Chainlit RAG • Otimização com WebGPU

**Exemplo**: [Roteador de Modelos como Ferramentas](./samples/06/README.md)

**Duração**: 3-4 horas | **Nível**: Avançado

---

### [5: Construindo Agentes de IA Rápido](./05.AIPoweredAgents.md)
**Foco**: Arquiteturas de agentes, prompts de sistema, grounding e orquestração

**Tópicos Principais**: Padrões de design de agentes • Engenharia de prompts de sistema • Técnicas de grounding • Sistemas multi-agentes • Implantação em produção

**Exemplo**: [Orquestração Multi-Agente](./samples/05/README.md) • [Sistema Multi-Agente Avançado](./samples/09/README.md)

**Duração**: 3-4 horas | **Nível**: Avançado

---

### [6: Foundry Local - Modelos como Ferramentas](./06.ModelsAsTools.md)
**Foco**: Soluções de IA modulares, escalabilidade empresarial e padrões de produção

**Tópicos Principais**: Modelos como ferramentas • Implantação no dispositivo • Integração SDK/API • Arquiteturas empresariais • Estratégias de escalabilidade

**Exemplo**: [Roteador de Modelos como Ferramentas](./samples/06/README.md) • [Framework de Ferramentas Foundry](./samples/10/README.md)

**Duração**: 3-4 horas | **Nível**: Especialista

---

### [7: Padrões de Integração Direta com API](./samples/07/README.md)
**Foco**: Integração pura com API REST sem dependências de SDK para controle máximo

**Tópicos Principais**: Implementação de cliente HTTP • Autenticação personalizada • Monitoramento de saúde de modelos • Respostas em streaming • Tratamento de erros em produção

**Exemplo**: [Cliente API Direto](./samples/07/README.md)

**Duração**: 2-3 horas | **Nível**: Intermediário

---

### [8: Aplicação de Chat Nativa no Windows 11](./samples/08/README.md)
**Foco**: Construção de aplicações modernas de chat nativas com integração ao Foundry Local

**Tópicos Principais**: Desenvolvimento com Electron • Fluent Design System • Integração nativa com Windows • Streaming em tempo real • Design de interface de chat

**Exemplo**: [Aplicação de Chat no Windows 11](./samples/08/README.md)

**Duração**: 3-4 horas | **Nível**: Avançado

---

### [9: Orquestração Multi-Agente Avançada](./samples/09/README.md)
**Foco**: Coordenação sofisticada de agentes, delegação de tarefas especializadas e fluxos de trabalho colaborativos de IA

**Tópicos Principais**: Coordenação inteligente de agentes • Padrões de chamadas de função • Comunicação entre agentes • Orquestração de fluxos de trabalho • Mecanismos de garantia de qualidade

**Exemplo**: [Sistema Multi-Agente Avançado](./samples/09/README.md)

**Duração**: 4-5 horas | **Nível**: Especialista

---

### [10: Foundry Local como Framework de Ferramentas](./samples/10/README.md)
**Foco**: Arquitetura orientada a ferramentas para integrar o Foundry Local em aplicações e frameworks existentes

**Tópicos Principais**: Integração com LangChain • Funções do Semantic Kernel • Frameworks de API REST • Ferramentas CLI • Integração com Jupyter • Padrões de implantação em produção

**Exemplo**: [Framework de Ferramentas Foundry](./samples/10/README.md)

**Duração**: 4-5 horas | **Nível**: Especialista

## Pré-requisitos

### Requisitos de Sistema
- **Sistema Operacional**: Windows 11 (22H2 ou posterior)
- **Memória**: 16GB RAM (32GB recomendados para modelos maiores)
- **Armazenamento**: 50GB de espaço livre para cache de modelos
- **Hardware**: Dispositivo com NPU recomendado (PC Copilot+), GPU opcional
- **Rede**: Internet de alta velocidade para download inicial de modelos

### Ambiente de Desenvolvimento
- Visual Studio Code com extensão AI Toolkit
- Python 3.10+ e pip
- Git para controle de versão
- PowerShell ou Prompt de Comando
- Azure CLI (opcional para integração com a nuvem)

### Conhecimentos Necessários
- Compreensão básica de conceitos de IA/ML
- Familiaridade com linha de comando
- Noções básicas de programação em Python
- Conceitos de API REST
- Conhecimento básico de prompts e inferência de modelos

## Cronograma do Módulo

**Tempo Total Estimado**: 30-38 horas

| Sessão | Área de Foco | Exemplos | Tempo | Complexidade |
|--------|--------------|----------|-------|--------------|
|  1 | Configuração & Básico | 01, 02, 03 | 2-3 horas | Iniciante |
|  2 | Soluções de IA | 04 | 2-3 horas | Intermediário |
|  3 | Open Source | 05 | 2-3 horas | Intermediário |
|  4 | Modelos Avançados | 06 | 3-4 horas | Avançado |
|  5 | Agentes de IA | 05, 09 | 3-4 horas | Avançado |
|  6 | Ferramentas Empresariais | 06, 10 | 3-4 horas | Especialista |
|  7 | Integração Direta com API | 07 | 2-3 horas | Intermediário |
|  8 | Aplicação de Chat no Windows 11 | 08 | 3-4 horas | Avançado |
|  9 | Multi-Agente Avançado | 09 | 4-5 horas | Especialista |
| 10 | Framework de Ferramentas | 10 | 4-5 horas | Especialista |

## Recursos Principais

**Documentação Oficial:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Código-fonte e exemplos oficiais
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Guia completo de configuração e uso
- [Série Model Mondays](https://aka.ms/model-mondays) - Destaques e tutoriais semanais de modelos

**Comunidade & Suporte:**
- [Discussões do Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Perguntas e respostas da comunidade e solicitações de recursos
- [Comunidade de Desenvolvedores de IA da Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Notícias e melhores práticas

## Resultados de Aprendizagem

Ao concluir este módulo, você estará preparado para:

### Domínio Técnico
- **Implantar e Gerenciar**: Instalações do Foundry Local em ambientes de desenvolvimento e produção
- **Integrar Modelos**: Trabalhar perfeitamente com diversas famílias de modelos da Microsoft, Hugging Face e fontes da comunidade
- **Criar Aplicações**: Desenvolver aplicações de IA prontas para produção com recursos avançados e otimizações
- **Desenvolver Agentes**: Implementar agentes de IA sofisticados com grounding, raciocínio e integração de ferramentas

### Compreensão Estratégica
- **Decisões Arquiteturais**: Fazer escolhas informadas entre implantação local e na nuvem
- **Otimização de Desempenho**: Otimizar o desempenho de inferência em diferentes configurações de hardware
- **Escalabilidade Empresarial**: Projetar aplicações que escalam de protótipos locais para implantações empresariais
- **Privacidade e Segurança**: Implementar soluções de IA preservando a privacidade com inferência local

### Capacidades de Inovação
- **Prototipagem Rápida**: Construir e testar conceitos de aplicações de IA rapidamente em todos os 10 padrões de exemplo
- **Integração Comunitária**: Aproveitar modelos open-source e contribuir para o ecossistema
- **Padrões Avançados**: Implementar padrões de IA de ponta, incluindo RAG, agentes e integração de ferramentas
- **Domínio de Frameworks**: Integração de nível especialista com LangChain, Semantic Kernel, Chainlit e Electron
- **Implantação em Produção**: Implantar soluções de IA escaláveis de protótipos locais para sistemas empresariais
- **Desenvolvimento Preparado para o Futuro**: Construir aplicações prontas para tecnologias e padrões emergentes de IA

## Começando

1. **Configuração do Ambiente**: Certifique-se de ter o Windows 11 com hardware recomendado (veja Pré-requisitos)
2. **Instalar Foundry Local**: Siga a Sessão 1 para instalação e configuração completas
3. **Executar Exemplo 01**: Comece com a integração básica de API REST para verificar a configuração
4. **Progredir pelos Exemplos**: Complete os exemplos 01-10 para domínio abrangente

## Métricas de Sucesso

Acompanhe seu progresso em todos os 10 exemplos abrangentes:

### Nível Fundamental (Exemplos 01-03)
- [ ] Instalar e configurar com sucesso o Foundry Local
- [ ] Completar integração com API REST (Exemplo 01)
- [ ] Implementar compatibilidade com OpenAI SDK (Exemplo 02)
- [ ] Realizar descoberta e benchmarking de modelos (Exemplo 03)

### Nível de Aplicação (Exemplos 04-06)
- [ ] Implantar e executar pelo menos 4 famílias de modelos diferentes
- [ ] Construir uma aplicação funcional de chat RAG (Exemplo 04)
- [ ] Criar sistema de orquestração multi-agente (Exemplo 05)
- [ ] Implementar roteamento inteligente de modelos (Exemplo 06)

### Nível de Integração Avançada (Exemplos 07-10)
- [ ] Construir cliente API pronto para produção (Exemplo 07)
- [ ] Desenvolver aplicação de chat nativa no Windows 11 (Exemplo 08)
- [ ] Implementar sistema multi-agente avançado (Exemplo 09)
- [ ] Criar framework abrangente de ferramentas (Exemplo 10)

### Indicadores de Domínio
- [ ] Executar com sucesso todos os 10 exemplos sem erros
- [ ] Personalizar pelo menos 3 exemplos para casos de uso específicos
- [ ] Implantar 2+ exemplos em ambientes semelhantes à produção
- [ ] Contribuir com melhorias ou extensões ao código de exemplo
- [ ] Integrar padrões do Foundry Local em projetos pessoais/profissionais

## Guia de Início Rápido - Todos os 10 Exemplos

### Configuração do Ambiente (Requerido para Todos os Exemplos)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Exemplos Fundamentais (01-06)

**Exemplo 01: Início Rápido com REST Chat**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Exemplo 02: Integração com OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Exemplo 03: Descoberta e Benchmarking de Modelos**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Exemplo 04: Aplicação Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Exemplo 05: Orquestração Multi-Agente**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Exemplo 06: Roteador de Modelos como Ferramentas**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Exemplos de Integração Avançada (07-10)

**Exemplo 07: Cliente API Direto**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Exemplo 08: Aplicação de Chat no Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Exemplo 09: Sistema Multi-Agente Avançado**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Exemplo 10: Framework de Ferramentas Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Solução de Problemas Comuns

**Erros de Conexão com Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemas de Carregamento de Modelos**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Problemas de Dependências**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Resumo
Este módulo representa o que há de mais avançado no desenvolvimento de IA de borda, combinando as ferramentas de nível empresarial da Microsoft com a flexibilidade e inovação do ecossistema de código aberto. Ao dominar o Foundry Local através de todos os 10 exemplos abrangentes, você estará na vanguarda do desenvolvimento de aplicações de IA.

**Trilha de Aprendizado Completa:**
- **Fundamentos** (Exemplos 01-03): Integração de API e gerenciamento de modelos
- **Aplicações** (Exemplos 04-06): RAG, agentes e roteamento inteligente
- **Avançado** (Exemplos 07-10): Frameworks de produção e integração empresarial

Para integração com Azure OpenAI (Sessão 2), consulte os arquivos README individuais dos exemplos para obter as variáveis de ambiente necessárias e configurações de versão da API.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.