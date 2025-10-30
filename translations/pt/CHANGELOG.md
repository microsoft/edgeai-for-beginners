<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T12:14:37+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "pt"
}
-->
# Alterações

Todas as alterações relevantes no EdgeAI for Beginners estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 30-10-2025

### Adicionado - Melhoria Abrangente no Módulo06 Agentes de IA
- **Integração com o Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Seção completa sobre o Microsoft Agent Framework para desenvolvimento de agentes prontos para produção
  - Padrões detalhados de integração com Foundry Local para implantação em edge
  - Exemplos de orquestração de múltiplos agentes com modelos SLM especializados
  - Padrões de implantação empresarial com gestão de recursos e monitorização
  - Funcionalidades de segurança e conformidade para sistemas de agentes em edge
  - Exemplos de implementação no mundo real (retalho, saúde, atendimento ao cliente)

- **Estratégias de Implantação de Agentes SLM em Produção**:
  - **Foundry Local**: Documentação completa de runtime de IA em edge de nível empresarial com instalação, configuração e padrões de produção
  - **Ollama**: Implantação focada na comunidade com monitorização abrangente e gestão de modelos
  - **VLLM**: Motor de inferência de alto desempenho com técnicas avançadas de otimização e funcionalidades empresariais
  - Listas de verificação para implantação em produção e tabelas comparativas para todas as três plataformas

- **Melhoria nos Frameworks SLM Otimizados para Edge**:
  - **ONNX Runtime**: Nova seção abrangente para implantação de agentes SLM em plataformas cruzadas
  - Padrões universais de implantação em Windows, Linux, macOS, iOS e Android
  - Opções de aceleração de hardware (CPU, GPU, NPU) com deteção automática
  - Funcionalidades prontas para produção e otimizações específicas para agentes
  - Exemplos completos de implementação com integração ao Microsoft Agent Framework

- **Referências e Leituras Adicionais**:
  - Biblioteca de recursos abrangente com mais de 100 fontes autoritativas
  - Artigos de pesquisa fundamentais sobre agentes de IA e Modelos de Linguagem Pequenos
  - Documentação oficial de todos os principais frameworks e ferramentas
  - Relatórios da indústria, análises de mercado e benchmarks técnicos
  - Recursos educacionais, conferências e fóruns comunitários
  - Normas, especificações e frameworks de conformidade

### Alterado - Modernização do Conteúdo do Módulo06
- **Objetivos de Aprendizagem Melhorados**: Adicionado domínio do Microsoft Agent Framework e capacidades de implantação em edge
- **Foco em Produção**: Mudança de orientação conceitual para orientação pronta para implementação com exemplos de produção
- **Exemplos de Código**: Atualizados todos os exemplos para utilizar padrões modernos de SDK e melhores práticas
- **Padrões de Arquitetura**: Adicionados arquiteturas hierárquicas de agentes e coordenação edge-to-cloud
- **Otimização de Desempenho**: Melhorada com recomendações de gestão de recursos e autoescalonamento

### Documentação - Melhoria na Estrutura do Módulo06
- **Cobertura Abrangente do Framework de Agentes**: Desde conceitos básicos até implantação empresarial
- **Estratégias de Implantação em Produção**: Guias completos para Foundry Local, Ollama e VLLM
- **Otimização em Plataformas Cruzadas**: Adicionado ONNX Runtime para implantação universal
- **Biblioteca de Recursos**: Referências extensivas para aprendizagem contínua e implementação

### Adicionado - Atualização da Documentação do Protocolo de Contexto de Modelo (MCP) no Módulo06
- **Modernização da Introdução ao MCP** (`Module06/03.IntroduceMCP.md`):
  - Atualizado com as últimas especificações do MCP de modelcontextprotocol.io (versão de 18-06-2025)
  - Adicionada analogia oficial com USB-C para conexões padronizadas de aplicações de IA
  - Atualizada a seção de arquitetura com design oficial de duas camadas (Camada de Dados + Camada de Transporte)
  - Documentação aprimorada de primitivas principais com primitivas de servidor (Ferramentas, Recursos, Prompts) e primitivas de cliente (Amostragem, Elicitação, Registo)

- **Referências e Recursos Abrangentes do MCP**:
  - Adicionado link **MCP para Iniciantes** (https://aka.ms/mcp-for-beginners)
  - Documentação oficial e especificações do MCP (modelcontextprotocol.io)
  - Recursos de desenvolvimento, incluindo MCP Inspector e implementações de referência
  - Normas técnicas (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Adicionado - Integração Qualcomm QNN no Módulo04
- **Nova Seção 7: Suite de Otimização Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Guia abrangente com mais de 400 linhas cobrindo o framework unificado de inferência de IA da Qualcomm
  - Cobertura detalhada de computação heterogénea (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Otimização consciente de hardware para plataformas Snapdragon com distribuição inteligente de carga de trabalho
  - Técnicas avançadas de quantização (INT8, INT16, precisão mista) para implantação móvel
  - Otimização de inferência eficiente em termos de energia para dispositivos alimentados por bateria e aplicações em tempo real
  - Guia completo de instalação com configuração de ambiente e configuração do SDK QNN
  - Exemplos práticos: conversão de PyTorch para QNN, otimização multi-backend, geração de binários de contexto
  - Padrões de uso avançados: configuração de backend personalizado, quantização dinâmica, perfil de desempenho
  - Seção abrangente de resolução de problemas e recursos comunitários

- **Estrutura do Módulo04 Melhorada**:
  - Atualizado README.md para incluir 7 seções progressivas (antes eram 6)
  - Adicionado Qualcomm QNN à tabela de benchmarks de desempenho (melhoria de velocidade de 5-15x, redução de memória de 50-80%)
  - Resultados de aprendizagem abrangentes para implantação de IA móvel e otimização de energia

### Alterado - Atualizações na Documentação do Módulo04
- **Melhoria na documentação do Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Adicionada seção abrangente "Repositório de Receitas Olive" cobrindo mais de 100 receitas de otimização pré-construídas
  - Cobertura detalhada de famílias de modelos suportadas (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Exemplos práticos de personalização de receitas e contribuições comunitárias
  - Melhorado com benchmarks de desempenho e orientação de integração

- **Reordenamento de seções no Módulo04**:
  - Apple MLX movido para a Seção 5 (antes era Seção 6)
  - Síntese de Workflow movida para a Seção 6 (antes era Seção 7)
  - Qualcomm QNN posicionado como Seção 7 (foco especializado em edge/móvel)
  - Atualizados todas as referências de arquivos e links de navegação conforme necessário

### Corrigido - Validação de Exemplos de Workshop
- **Validação e reparação de chat_bootstrap.py**:
  - Corrigida declaração de importação corrompida (`util.util.workshop_utils` → `util.workshop_utils`)
  - Criado `__init__.py` ausente no pacote util para resolução adequada de módulos Python
  - Instaladas dependências necessárias (openai, foundry-local-sdk) no ambiente conda
  - Validação bem-sucedida da execução do exemplo com prompts padrão e personalizados
  - Confirmada integração com o serviço Foundry Local e carregamento de modelo (phi-4-mini com otimização CUDA)

### Documentação - Atualizações Abrangentes de Guias
- **Reestruturação completa do README.md do Módulo04**:
  - Adicionado Qualcomm QNN como framework de otimização principal ao lado de OpenVINO, Olive, MLX
  - Atualizados os resultados de aprendizagem do capítulo para incluir implantação de IA móvel e otimização de energia
  - Melhorada a tabela de comparação de desempenho com métricas QNN e casos de uso em edge/móvel
  - Mantida a progressão lógica de soluções empresariais para otimizações específicas de plataforma

- **Referências cruzadas e navegação**:
  - Atualizados todos os links internos e referências de arquivos para nova numeração de seções
  - Melhorada a descrição da síntese de workflow para incluir ambientes móveis, desktop e cloud
  - Adicionados links de recursos abrangentes para o ecossistema de desenvolvedores Qualcomm

## 08-10-2025

### Adicionado - Atualização Abrangente do Workshop
- **Reescrita completa do README.md do Workshop**:
  - Adicionada introdução abrangente explicando a proposta de valor do Edge AI (privacidade, desempenho, custo)
  - Criados 6 objetivos principais de aprendizagem com competências detalhadas
  - Adicionada tabela de resultados de aprendizagem com entregáveis e matriz de competências
  - Incluída seção de competências prontas para o mercado para relevância na indústria
  - Adicionado guia de início rápido com pré-requisitos e configuração em 3 etapas
  - Criadas tabelas de recursos para amostras Python (8 arquivos com tempos de execução)
  - Adicionada tabela de notebooks Jupyter (8 notebooks com classificações de dificuldade)
  - Criada tabela de documentação (7 documentos principais com orientação "Quando Usar")
  - Adicionadas recomendações de percurso de aprendizagem para diferentes níveis de habilidade

- **Infraestrutura de validação e teste do Workshop**:
  - Criado `scripts/validate_samples.py` - Ferramenta abrangente de validação para sintaxe, importações e melhores práticas
  - Criado `scripts/test_samples.py` - Executor de testes rápidos para todas as amostras Python
  - Adicionada documentação de validação ao `scripts/README.md`

- **Documentação abrangente**:
  - Criado `SAMPLES_UPDATE_SUMMARY.md` - Guia detalhado com mais de 400 linhas cobrindo todas as melhorias
  - Criado `UPDATE_COMPLETE.md` - Resumo executivo da conclusão da atualização
  - Criado `QUICK_REFERENCE.md` - Cartão de referência rápida para o Workshop

### Alterado - Modernização das Amostras Python do Workshop
- **Todas as 8 amostras Python atualizadas com melhores práticas**:
  - Melhorado o tratamento de erros com blocos try-except em todas as operações de I/O
  - Adicionadas dicas de tipo e docstrings abrangentes
  - Implementado padrão consistente de registo [INFO]/[ERROR]/[RESULT]
  - Protegidas importações opcionais com dicas de instalação
  - Melhorado o feedback ao utilizador em todas as amostras

- **session01/chat_bootstrap.py**:
  - Melhorada a inicialização do cliente com mensagens de erro abrangentes
  - Melhorado o tratamento de erros de streaming com validação de fragmentos
  - Adicionada melhor gestão de exceções para indisponibilidade de serviço

- **session02/rag_pipeline.py**:
  - Adicionados guardas de importação para sentence-transformers com dicas de instalação
  - Melhorado o tratamento de erros para operações de embedding e geração
  - Melhorado o formato de saída com resultados estruturados

- **session02/rag_eval_ragas.py**:
  - Protegidas importações opcionais (ragas, datasets) com mensagens de erro amigáveis
  - Adicionado tratamento de erros para métricas de avaliação
  - Melhorado o formato de saída para resultados de avaliação

- **session03/benchmark_oss_models.py**:
  - Implementada degradação graciosa (continua em falhas de modelos)
  - Adicionado relatório detalhado de progresso e tratamento de erros por modelo
  - Melhorado o cálculo de estatísticas com recuperação abrangente de erros

- **session04/model_compare.py**:
  - Adicionadas dicas de tipo (tipos de retorno Tuple)
  - Melhorado o formato de saída com resultados JSON estruturados
  - Implementado tratamento de erros por modelo com recuperação

- **session05/agents_orchestrator.py**:
  - Melhorado Agent.act() com docstrings abrangentes
  - Adicionado tratamento de erros na pipeline com registo etapa por etapa
  - Melhorada a gestão de memória e rastreamento de estado

- **session06/models_router.py**:
  - Melhorada a documentação de funções para todos os componentes de roteamento
  - Adicionado registo detalhado na função route()
  - Melhorada a saída de teste com resultados estruturados

- **session06/models_pipeline.py**:
  - Adicionado tratamento de erros à função auxiliar chat()
  - Melhorada pipeline() com registo de etapas e relatório de progresso
  - Melhorado main() com recuperação abrangente de erros

### Documentação - Melhoria na Documentação do Workshop
- Atualizado o README.md principal com seção do Workshop destacando o percurso de aprendizagem prático
- Melhorado STUDY_GUIDE.md com seção abrangente do Workshop incluindo:
  - Objetivos de aprendizagem e áreas de foco de estudo
  - Perguntas de autoavaliação
  - Exercícios práticos com estimativas de tempo
  - Alocação de tempo para estudo concentrado e em tempo parcial
  - Adicionado Workshop ao modelo de acompanhamento de progresso
- Atualizado o guia de alocação de tempo de 20 horas para 30 horas (incluindo Workshop)
- Adicionadas descrições de amostras do Workshop e resultados de aprendizagem ao README

### Corrigido
- Resolvidos padrões inconsistentes de tratamento de erros nas amostras do Workshop
- Corrigidos erros de importação de dependências opcionais com guardas adequados
- Corrigidas dicas de tipo ausentes em funções críticas
- Resolvido feedback insuficiente ao utilizador em cenários de erro
- Corrigidos problemas de validação com infraestrutura de testes abrangente

---

## 23-09-2025

### Alterado - Modernização Principal do Módulo 08
- **Alinhamento abrangente com padrões do repositório Microsoft Foundry-Local**
  - Atualizados todos os exemplos de código para usar integração moderna com `FoundryLocalManager` e SDK OpenAI
  - Substituídas chamadas manuais de `requests` obsoletas por uso adequado de SDK
  - Alinhados padrões de implementação com documentação oficial da Microsoft e amostras

- **Modernização de 05.AIPoweredAgents.md**:
  - Atualizada orquestração de múltiplos agentes para usar padrões modernos de SDK
  - Melhorada implementação de coordenador com funcionalidades avançadas (ciclos de feedback, monitorização de desempenho)
  - Adicionado tratamento de erros abrangente e verificação de saúde do serviço
  - Integradas referências adequadas a amostras locais (`samples/05/multi_agent_orchestration.ipynb`)
  - Atualizados exemplos de chamadas de função para usar o parâmetro moderno `tools` em vez de `functions` obsoleto
  - Adicionados padrões prontos para produção com monitorização e rastreamento de estatísticas

- **Reescrita completa de 06.ModelsAsTools.md**:
  - Substituído registro básico de ferramentas por implementação de roteador inteligente de modelos
  - Adicionada seleção de modelos baseada em palavras-chave para diferentes tipos de tarefas (geral, raciocínio, código, criativo)
  - Integrada configuração baseada em ambiente com atribuição flexível de modelos
  - Melhorada com monitorização abrangente de saúde do serviço e tratamento de erros
  - Adicionados padrões de implantação em produção com monitorização de solicitações e rastreamento de desempenho
  - Alinhado com implementação local em `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Melhorias na estrutura da documentação**:
  - Adicionadas seções de visão geral destacando modernização e alinhamento com SDK
  - Melhorado com emojis e formatação para maior legibilidade
  - Incluídas referências adequadas a arquivos de amostras locais em toda a documentação
  - Incluídas orientações de implementação pronta para produção e melhores práticas

### Adicionado
- Seções de visão geral abrangentes nos arquivos do Módulo 08 destacando integração moderna com SDK
- Destaques de arquitetura mostrando funcionalidades avançadas (sistemas de múltiplos agentes, roteamento inteligente)
- Referências diretas a implementações de amostras locais para experiência prática
- Orientação de implantação em produção com padrões de monitorização e tratamento de erros
- Exemplos interativos de notebooks Jupyter com funcionalidades avançadas e benchmarks

### Corrigido
- Discrepâncias de alinhamento entre documentação e implementações reais de amostras
- Padrões de uso de SDK obsoletos em todo o Módulo 08
- Referências ausentes à biblioteca abrangente de amostras locais
- Abordagens de implementação inconsistentes em diferentes seções

---

## 18-09-2025

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração com Azure AI Foundry, modelos open-source, demos de ponta, agentes e modelos como ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para cmd do Windows
    - `01` REST chat rápido (`chat_quickstart.py`)
    - `02` Início rápido com SDK para OpenAI/Foundry Local e suporte ao Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista e benchmark (`list_and_bench.cmd`)
    - `04` Demonstração Chainlit (`app.py`)
    - `05` Orquestração multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Router de Modelos-como-Ferramentas (`router.py`)
- Suporte ao Azure OpenAI na amostra do SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise Python
- `.env` com sugestão de `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas menções restantes a `phi-3.5` no Módulo 08
- Melhorias no Router (`Module08/samples/06/router.py`):
  - Descoberta de endpoints via `foundry service status` com análise de regex
  - Verificação de saúde em `/v1/models` na inicialização
  - Registro de modelos configurável via ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientações para o exemplo Chainlit esclarecidas e adicionadas instruções de resolução de problemas; resolução de importação via configurações de workspace

### Corrigido
- Problemas de importação resolvidos:
  - Router não depende mais de um módulo `utils` inexistente; funções foram incorporadas
  - Coordinator usa importação relativa (`from .specialists import ...`) e é invocado via caminho de módulo
  - Configuração do VS Code/Pylance para resolver `chainlit` e importações de pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Excluído `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Exemplos do Módulo 08 consolidados em `Module08/samples` com pastas numeradas por sessão
  - Aplicação Chainlit movida para `samples/04`
  - Agentes movidos para `samples/05` e adicionados arquivos `__init__.py` para resolução de pacotes

### Documentação
- Documentação da sessão do Módulo 08 e todos os READMEs dos exemplos enriquecidos com referências do Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do router e dicas de validação
- Seção Local do Foundry no Windows em `Module07/README.md` validada contra a documentação do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado Módulo 08 à visão geral, cronogramas, rastreador de progresso
  - Adicionada seção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e inclusão de estudos de caso
- Cobertura expandida de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não lançado / Pendências (propostas)
- Testes rápidos opcionais por exemplo para validar disponibilidade do Foundry Local
- Revisão de traduções para alinhar referências de modelos (ex.: `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipes prefiram rigor em todo o workspace

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.