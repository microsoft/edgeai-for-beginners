# Registro de Alterações

Todas as mudanças importantes no EdgeAI para Iniciantes estão documentadas aqui. Este projeto utiliza entradas baseadas em datas e o estilo Keep a Changelog (Adicionado, Alterado, Corrigido, Removido, Documentação, Movido).

## 2025-10-30

### Adicionado - Aprimoramento Abrangente de Agentes de IA no Módulo06
- **Integração com o Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Seção completa sobre o Microsoft Agent Framework para desenvolvimento de agentes prontos para produção
  - Padrões detalhados de integração com Foundry Local para implantação em edge
  - Exemplos de orquestração de múltiplos agentes com modelos SLM especializados
  - Padrões de implantação empresarial com gerenciamento de recursos e monitoramento
  - Recursos de segurança e conformidade para sistemas de agentes em edge
  - Exemplos de implementação no mundo real (varejo, saúde, atendimento ao cliente)

- **Estratégias de Implantação de Agentes SLM em Produção**:
  - **Foundry Local**: Documentação completa de runtime de IA em edge de nível empresarial com instalação, configuração e padrões de produção
  - **Ollama**: Implantação focada na comunidade com monitoramento abrangente e gerenciamento de modelos
  - **VLLM**: Motor de inferência de alto desempenho com técnicas avançadas de otimização e recursos empresariais
  - Listas de verificação de implantação em produção e tabelas comparativas para todas as três plataformas

- **Aprimoramento de Frameworks SLM Otimizados para Edge**:
  - **ONNX Runtime**: Nova seção abrangente para implantação de agentes SLM em múltiplas plataformas
  - Padrões universais de implantação em Windows, Linux, macOS, iOS e Android
  - Opções de aceleração de hardware (CPU, GPU, NPU) com detecção automática
  - Recursos prontos para produção e otimizações específicas para agentes
  - Exemplos completos de implementação com integração ao Microsoft Agent Framework

- **Referências e Leituras Adicionais**:
  - Biblioteca de recursos abrangente com mais de 100 fontes autoritativas
  - Artigos de pesquisa fundamentais sobre agentes de IA e Modelos de Linguagem Pequenos
  - Documentação oficial de todos os principais frameworks e ferramentas
  - Relatórios da indústria, análises de mercado e benchmarks técnicos
  - Recursos educacionais, conferências e fóruns comunitários
  - Padrões, especificações e frameworks de conformidade

### Alterado - Modernização do Conteúdo do Módulo06
- **Objetivos de Aprendizagem Aprimorados**: Adicionado domínio do Microsoft Agent Framework e capacidades de implantação em edge
- **Foco em Produção**: Mudança de orientação conceitual para orientações prontas para implementação com exemplos de produção
- **Exemplos de Código**: Atualizados todos os exemplos para usar padrões modernos de SDK e melhores práticas
- **Padrões de Arquitetura**: Adicionado arquiteturas hierárquicas de agentes e coordenação edge-to-cloud
- **Otimização de Desempenho**: Aprimorado com recomendações de gerenciamento de recursos e autoescalonamento

### Documentação - Aprimoramento da Estrutura do Módulo06
- **Cobertura Abrangente do Framework de Agentes**: Desde conceitos básicos até implantação empresarial
- **Estratégias de Implantação em Produção**: Guias completos para Foundry Local, Ollama e VLLM
- **Otimização Multiplataforma**: Adicionado ONNX Runtime para implantação universal
- **Biblioteca de Recursos**: Referências extensivas para aprendizado contínuo e implementação

### Adicionado - Atualização da Documentação do Protocolo de Contexto de Modelo (MCP) no Módulo06
- **Modernização da Introdução ao MCP** (`Module06/03.IntroduceMCP.md`):
  - Atualizado com as últimas especificações do MCP de modelcontextprotocol.io (versão 2025-06-18)
  - Adicionado analogia oficial com USB-C para conexões padronizadas de aplicações de IA
  - Atualizada seção de arquitetura com design oficial de duas camadas (Camada de Dados + Camada de Transporte)
  - Documentação aprimorada de primitivas principais com primitivas de servidor (Ferramentas, Recursos, Prompts) e primitivas de cliente (Amostragem, Elicitação, Registro)

- **Referências e Recursos Abrangentes do MCP**:
  - Adicionado link **MCP para Iniciantes** (https://aka.ms/mcp-for-beginners)
  - Documentação oficial do MCP e especificações (modelcontextprotocol.io)
  - Recursos de desenvolvimento, incluindo MCP Inspector e implementações de referência
  - Padrões técnicos (JSON-RPC 2.0, JSON Schema, OpenAPI, Eventos Enviados pelo Servidor)

### Adicionado - Integração com Qualcomm QNN no Módulo04
- **Nova Seção 7: Suite de Otimização Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Guia abrangente com mais de 400 linhas cobrindo o framework unificado de inferência de IA da Qualcomm
  - Cobertura detalhada de computação heterogênea (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Otimização consciente de hardware para plataformas Snapdragon com distribuição inteligente de carga de trabalho
  - Técnicas avançadas de quantização (INT8, INT16, precisão mista) para implantação móvel
  - Otimização de inferência eficiente em termos de energia para dispositivos alimentados por bateria e aplicações em tempo real
  - Guia completo de instalação com configuração do SDK QNN e ambiente
  - Exemplos práticos: conversão de PyTorch para QNN, otimização multi-backend, geração de binários de contexto
  - Padrões de uso avançados: configuração de backend personalizado, quantização dinâmica, perfil de desempenho
  - Seção abrangente de solução de problemas e recursos comunitários

- **Estrutura do Módulo04 Aprimorada**:
  - Atualizado README.md para incluir 7 seções progressivas (antes eram 6)
  - Adicionado Qualcomm QNN à tabela de benchmarks de desempenho (melhoria de velocidade de 5-15x, redução de memória de 50-80%)
  - Resultados de aprendizado abrangentes para implantação de IA móvel e otimização de energia

### Alterado - Atualizações na Documentação do Módulo04
- **Aprimoramento da documentação do Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Adicionada seção abrangente "Repositório de Receitas Olive" cobrindo mais de 100 receitas de otimização pré-construídas
  - Cobertura detalhada de famílias de modelos suportados (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Exemplos práticos de personalização de receitas e contribuições da comunidade
  - Aprimorado com benchmarks de desempenho e orientações de integração

- **Reordenamento de seções no Módulo04**:
  - Apple MLX movido para a Seção 5 (era Seção 6)
  - Síntese de Fluxo de Trabalho movida para a Seção 6 (era Seção 7)
  - Qualcomm QNN posicionado como Seção 7 (foco especializado em dispositivos móveis/edge)
  - Atualizados todas as referências de arquivos e links de navegação conforme necessário

### Corrigido - Validação de Exemplos de Workshop
- **Validação e reparo do chat_bootstrap.py**:
  - Corrigido declaração de importação corrompida (`util.util.workshop_utils` → `util.workshop_utils`)
  - Criado `__init__.py` ausente no pacote util para resolução adequada de módulos Python
  - Instaladas dependências necessárias (openai, foundry-local-sdk) no ambiente conda
  - Validação bem-sucedida da execução do exemplo com prompts padrão e personalizados
  - Confirmada integração com o serviço Foundry Local e carregamento de modelo (phi-4-mini com otimização CUDA)

### Documentação - Atualizações Abrangentes de Guias
- **Reestruturação completa do README.md do Módulo04**:
  - Adicionado Qualcomm QNN como framework de otimização principal ao lado de OpenVINO, Olive, MLX
  - Atualizados os resultados de aprendizado do capítulo para incluir implantação de IA móvel e otimização de energia
  - Aprimorada tabela de comparação de desempenho com métricas QNN e casos de uso em dispositivos móveis/edge
  - Mantida progressão lógica de soluções empresariais para otimizações específicas de plataforma

- **Referências cruzadas e navegação**:
  - Atualizados todos os links internos e referências de arquivos para nova numeração de seções
  - Aprimorada descrição de síntese de fluxo de trabalho para incluir ambientes móveis, desktop e nuvem
  - Adicionados links de recursos abrangentes para o ecossistema de desenvolvedores Qualcomm

## 2025-10-08

### Adicionado - Atualização Abrangente do Workshop
- **Reescrita completa do README.md do Workshop**:
  - Adicionada introdução abrangente explicando a proposta de valor do Edge AI (privacidade, desempenho, custo)
  - Criados 6 objetivos principais de aprendizado com competências detalhadas
  - Adicionada tabela de resultados de aprendizado com entregáveis e matriz de competências
  - Incluída seção de habilidades para carreira com relevância na indústria
  - Adicionado guia de início rápido com pré-requisitos e configuração em 3 etapas
  - Criadas tabelas de recursos para amostras Python (8 arquivos com tempos de execução)
  - Adicionada tabela de notebooks Jupyter (8 notebooks com classificações de dificuldade)
  - Criada tabela de documentação (7 documentos principais com orientação "Quando Usar")
  - Adicionadas recomendações de caminho de aprendizado para diferentes níveis de habilidade

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
  - Aprimorado tratamento de erros com blocos try-except em todas as operações de I/O
  - Adicionados hints de tipo e docstrings abrangentes
  - Implementado padrão consistente de log [INFO]/[ERROR]/[RESULT]
  - Protegidas importações opcionais com dicas de instalação
  - Melhorado feedback ao usuário em todas as amostras

- **session01/chat_bootstrap.py**:
  - Aprimorada inicialização do cliente com mensagens de erro abrangentes
  - Melhorado tratamento de erros de streaming com validação de chunks
  - Adicionado tratamento de exceções para indisponibilidade de serviço

- **session02/rag_pipeline.py**:
  - Adicionados guardas de importação para sentence-transformers com dicas de instalação
  - Aprimorado tratamento de erros para operações de embedding e geração
  - Melhorado formatação de saída com resultados estruturados

- **session02/rag_eval_ragas.py**:
  - Protegidas importações opcionais (ragas, datasets) com mensagens de erro amigáveis
  - Adicionado tratamento de erros para métricas de avaliação
  - Aprimorada formatação de saída para resultados de avaliação

- **session03/benchmark_oss_models.py**:
  - Implementada degradação graciosa (continua em falhas de modelos)
  - Adicionado relatório detalhado de progresso e tratamento de erros por modelo
  - Aprimorado cálculo de estatísticas com recuperação abrangente de erros

- **session04/model_compare.py**:
  - Adicionados hints de tipo (tipos de retorno Tuple)
  - Aprimorada formatação de saída com resultados JSON estruturados
  - Implementado tratamento de erros por modelo com recuperação

- **session05/agents_orchestrator.py**:
  - Aprimorado Agent.act() com docstrings abrangentes
  - Adicionado tratamento de erros no pipeline com registro etapa por etapa
  - Melhorado gerenciamento de memória e rastreamento de estado

- **session06/models_router.py**:
  - Aprimorada documentação de funções para todos os componentes de roteamento
  - Adicionado log detalhado na função route()
  - Melhorado saída de teste com resultados estruturados

- **session06/models_pipeline.py**:
  - Adicionado tratamento de erros à função auxiliar chat()
  - Aprimorado pipeline() com registro de etapas e relatório de progresso
  - Melhorado main() com recuperação abrangente de erros

### Documentação - Aprimoramento da Documentação do Workshop
- Atualizado README.md principal com seção do Workshop destacando o caminho de aprendizado prático
- Aprimorado STUDY_GUIDE.md com seção abrangente do Workshop incluindo:
  - Objetivos de aprendizado e áreas de foco de estudo
  - Perguntas de autoavaliação
  - Exercícios práticos com estimativas de tempo
  - Alocação de tempo para estudo concentrado e em meio período
  - Adicionado Workshop ao modelo de rastreamento de progresso
- Atualizado guia de alocação de tempo de 20 horas para 30 horas (incluindo Workshop)
- Adicionadas descrições de amostras do Workshop e resultados de aprendizado ao README

### Corrigido
- Resolvido padrões inconsistentes de tratamento de erros nas amostras do Workshop
- Corrigidos erros de importação de dependências opcionais com guardas adequados
- Corrigidos hints de tipo ausentes em funções críticas
- Resolvido feedback insuficiente ao usuário em cenários de erro
- Corrigidos problemas de validação com infraestrutura de testes abrangente

---

## 2025-09-23

### Alterado - Modernização Principal do Módulo 08
- **Alinhamento abrangente com padrões do repositório Microsoft Foundry-Local**
  - Atualizados todos os exemplos de código para usar integração moderna com `FoundryLocalManager` e SDK OpenAI
  - Substituídas chamadas manuais de `requests` obsoletas por uso adequado de SDK
  - Alinhados padrões de implementação com documentação oficial da Microsoft e exemplos

- **Modernização do 05.AIPoweredAgents.md**:
  - Atualizada orquestração de múltiplos agentes para usar padrões modernos de SDK
  - Aprimorada implementação de coordenador com recursos avançados (loops de feedback, monitoramento de desempenho)
  - Adicionado tratamento abrangente de erros e verificação de saúde do serviço
  - Integradas referências adequadas a amostras locais (`samples/05/multi_agent_orchestration.ipynb`)
  - Atualizados exemplos de chamadas de função para usar o parâmetro moderno `tools` em vez de `functions` obsoleto
  - Adicionados padrões prontos para produção com monitoramento e rastreamento de estatísticas

- **Reescrita completa do 06.ModelsAsTools.md**:
  - Substituído registro básico de ferramentas por implementação inteligente de roteador de modelos
  - Adicionada seleção de modelos baseada em palavras-chave para diferentes tipos de tarefas (geral, raciocínio, código, criativo)
  - Integrada configuração baseada em ambiente com atribuição flexível de modelos
  - Aprimorado com monitoramento abrangente de saúde do serviço e tratamento de erros
  - Adicionados padrões de implantação em produção com monitoramento de solicitações e rastreamento de desempenho
  - Alinhado com implementação local em `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Melhorias na estrutura da documentação**:
  - Adicionadas seções de visão geral destacando modernização e alinhamento com SDK
  - Aprimorado com emojis e melhor formatação para maior legibilidade
  - Incluídas referências adequadas a arquivos de amostras locais em toda a documentação
  - Adicionado orientação de implementação pronta para produção e melhores práticas

### Adicionado
- Seções de visão geral abrangentes nos arquivos do Módulo 08 destacando integração moderna com SDK
- Destaques de arquitetura mostrando recursos avançados (sistemas de múltiplos agentes, roteamento inteligente)
- Referências diretas a implementações de amostras locais para experiência prática
- Orientação de implantação em produção com padrões de monitoramento e tratamento de erros
- Exemplos interativos de notebooks Jupyter com recursos avançados e benchmarks

### Corrigido
- Discrepâncias de alinhamento entre documentação e implementações reais de amostras
- Padrões de uso de SDK obsoletos em todo o Módulo 08
- Referências ausentes à biblioteca abrangente de amostras locais
- Abordagens de implementação inconsistentes em diferentes seções

---

## 2025-09-18

### Adicionado
- Módulo 08: Microsoft Foundry Local – Kit de Ferramentas Completo para Desenvolvedores
  - Seis sessões: configuração, integração com Azure AI Foundry, modelos open-source, demonstrações de ponta, agentes e modelos como ferramentas
  - Exemplos executáveis em `Module08/samples/01`–`06` com instruções para cmd do Windows
    - `01` REST chat rápido (`chat_quickstart.py`)
    - `02` Introdução ao SDK com suporte OpenAI/Foundry Local e Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista-e-benchmark (`list_and_bench.cmd`)
    - `04` Demonstração Chainlit (`app.py`)
    - `05` Orquestração multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Roteador Models-as-Tools (`router.py`)
- Suporte ao Azure OpenAI no exemplo do SDK da Sessão 2 com configuração de variáveis de ambiente
- `.vscode/settings.json` apontando para `Module08/.venv` para melhorar a resolução de análise do Python
- `.env` com sugestão de `PYTHONPATH` para reconhecimento no VS Code/Pylance

### Alterado
- Modelo padrão atualizado para `phi-4-mini` em toda a documentação e exemplos do Módulo 08; removidas as menções restantes ao `phi-3.5` no Módulo 08
- Melhorias no roteador (`Module08/samples/06/router.py`):
  - Descoberta de endpoint via `foundry service status` com análise regex
  - Verificação de saúde em `/v1/models` na inicialização
  - Registro de modelos configurável via ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos atualizados: `Module08/requirements.txt` agora inclui `openai` (junto com `requests`, `chainlit`)
- Orientações para o exemplo Chainlit esclarecidas e adicionadas soluções de problemas; resolução de importação via configurações do workspace

### Corrigido
- Problemas de importação resolvidos:
  - O roteador não depende mais de um módulo `utils` inexistente; funções foram incorporadas
  - O coordenador usa importação relativa (`from .specialists import ...`) e é invocado via caminho do módulo
  - Configuração do VS Code/Pylance para resolver importações de `chainlit` e pacotes
- Corrigido pequeno erro de digitação em `STUDY_GUIDE.md` e adicionada cobertura do Módulo 08

### Removido
- Excluído `Module08/infra/obs.py` não utilizado e removido o diretório vazio `infra/`; padrões de observabilidade mantidos como opcionais na documentação

### Movido
- Demos do Módulo 08 consolidados em `Module08/samples` com pastas numeradas por sessão
  - Aplicativo Chainlit movido para `samples/04`
  - Agentes movidos para `samples/05` e adicionados arquivos `__init__.py` para resolução de pacotes

### Documentação
- Documentação da sessão do Módulo 08 e todos os READMEs dos exemplos enriquecidos com referências do Microsoft Learn e fornecedores confiáveis
- `Module08/README.md` atualizado com Visão Geral dos Exemplos, configuração do roteador e dicas de validação
- Seção Local do Foundry no Windows em `Module07/README.md` validada com base na documentação do Learn
- `STUDY_GUIDE.md` atualizado:
  - Adicionado Módulo 08 ao resumo, cronogramas, rastreador de progresso
  - Adicionada seção abrangente de Referências (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumo)
- Arquitetura do curso e módulos estabelecidos (Módulos 01–07)
- Modernização iterativa de conteúdo, padronização de formatação e adição de estudos de caso
- Cobertura expandida de frameworks de otimização (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Não lançado / Backlog (propostas)
- Testes rápidos opcionais por exemplo para validar a disponibilidade do Foundry Local
- Revisar traduções para alinhar referências de modelos (ex.: `phi-4-mini`) onde apropriado
- Adicionar configuração mínima do pyright caso as equipes prefiram rigor em todo o workspace

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.