# Kit de Ferramentas de IA para Visual Studio Code - Guia de Desenvolvimento de IA na Edge

## Introdução

Bem-vindo ao guia completo para usar o Kit de Ferramentas de IA no Visual Studio Code no desenvolvimento de IA na Edge. À medida que a inteligência artificial migra da computação centralizada na nuvem para dispositivos distribuídos na edge, os desenvolvedores precisam de ferramentas poderosas e integradas que possam lidar com os desafios únicos do deployment na edge - desde restrições de recursos até requisitos de operação offline.

O Kit de Ferramentas de IA para Visual Studio Code preenche essa lacuna ao fornecer um ambiente de desenvolvimento completo, especificamente projetado para construir, testar e otimizar aplicações de IA que funcionem eficientemente em dispositivos na edge. Seja você desenvolvendo para sensores IoT, dispositivos móveis, sistemas embarcados ou servidores na edge, este kit simplifica todo o seu fluxo de trabalho de desenvolvimento dentro do ambiente familiar do VS Code.

Este guia irá conduzi-lo pelos conceitos essenciais, ferramentas e melhores práticas para aproveitar o Kit de Ferramentas de IA em seus projetos de IA na Edge, desde a seleção inicial de modelos até o deployment em produção.

## Visão Geral

O Kit de Ferramentas de IA para Visual Studio Code é uma extensão poderosa que simplifica o desenvolvimento de agentes e a criação de aplicações de IA. O kit oferece capacidades abrangentes para explorar, avaliar e implementar modelos de IA de uma ampla gama de provedores — incluindo Anthropic, OpenAI, GitHub, Google — enquanto suporta a execução de modelos locais usando ONNX e Ollama.

O que diferencia o Kit de Ferramentas de IA é sua abordagem abrangente para todo o ciclo de vida do desenvolvimento de IA. Diferentemente das ferramentas tradicionais de desenvolvimento de IA que se concentram em aspectos isolados, o Kit de Ferramentas de IA fornece um ambiente integrado que cobre descoberta de modelos, experimentação, desenvolvimento de agentes, avaliação e deployment — tudo dentro do ambiente familiar do VS Code.

A plataforma é projetada especificamente para prototipagem rápida e deployment em produção, com recursos como geração de prompts, iniciadores rápidos, integrações perfeitas com ferramentas MCP (Model Context Protocol) e capacidades extensivas de avaliação. Para o desenvolvimento de IA na Edge, isso significa que você pode desenvolver, testar e otimizar aplicações de IA para cenários de deployment na edge de forma eficiente, enquanto mantém todo o fluxo de trabalho de desenvolvimento dentro do VS Code.

## Objetivos de Aprendizagem

Ao final deste guia, você será capaz de:

### Competências Principais
- **Instalar e configurar** o Kit de Ferramentas de IA para Visual Studio Code para fluxos de trabalho de desenvolvimento de IA na Edge
- **Navegar e utilizar** a interface do Kit de Ferramentas de IA, incluindo o Catálogo de Modelos, Playground e Construtor de Agentes
- **Selecionar e avaliar** modelos de IA adequados para deployment na edge com base em desempenho e restrições de recursos
- **Converter e otimizar** modelos usando o formato ONNX e técnicas de quantização para dispositivos na edge

### Habilidades de Desenvolvimento de IA na Edge
- **Projetar e implementar** aplicações de IA na Edge usando o ambiente de desenvolvimento integrado
- **Realizar testes de modelos** em condições semelhantes à edge usando inferência local e monitoramento de recursos
- **Criar e personalizar** agentes de IA otimizados para cenários de deployment na edge
- **Avaliar o desempenho de modelos** usando métricas relevantes para computação na edge (latência, uso de memória, precisão)

### Otimização e Deployment
- **Aplicar técnicas de quantização e poda** para reduzir o tamanho do modelo enquanto mantém um desempenho aceitável
- **Otimizar modelos** para plataformas de hardware específicas na edge, incluindo aceleração por CPU, GPU e NPU
- **Implementar melhores práticas** para desenvolvimento de IA na edge, incluindo gerenciamento de recursos e estratégias de fallback
- **Preparar modelos e aplicações** para deployment em dispositivos na edge

### Conceitos Avançados de IA na Edge
- **Integrar com frameworks de IA na edge** incluindo ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementar arquiteturas multi-modelo** e cenários de aprendizado federado para ambientes na edge
- **Solucionar problemas comuns de IA na edge** incluindo restrições de memória, velocidade de inferência e compatibilidade de hardware
- **Projetar estratégias de monitoramento e registro** para aplicações de IA na edge em produção

### Aplicação Prática
- **Construir soluções completas de IA na Edge** desde a seleção de modelos até o deployment
- **Demonstrar proficiência** em fluxos de trabalho de desenvolvimento específicos para a edge e técnicas de otimização
- **Aplicar conceitos aprendidos** em casos de uso reais de IA na edge, incluindo IoT, dispositivos móveis e aplicações embarcadas
- **Avaliar e comparar** diferentes estratégias de deployment de IA na edge e seus trade-offs

## Principais Recursos para Desenvolvimento de IA na Edge

### 1. Catálogo de Modelos e Descoberta
- **Suporte Multi-Provedor**: Navegue e acesse modelos de IA de Anthropic, OpenAI, GitHub, Google e outros provedores
- **Integração de Modelos Locais**: Descoberta simplificada de modelos ONNX e Ollama para deployment na edge
- **Modelos do GitHub**: Integração direta com o hosting de modelos do GitHub para acesso simplificado
- **Comparação de Modelos**: Compare modelos lado a lado para encontrar o equilíbrio ideal para as restrições de dispositivos na edge

### 2. Playground Interativo
- **Ambiente de Teste Interativo**: Experimentação rápida com capacidades de modelos em um ambiente controlado
- **Suporte Multi-modal**: Teste com imagens, texto e outros inputs típicos em cenários na edge
- **Experimentação em Tempo Real**: Feedback imediato sobre respostas e desempenho dos modelos
- **Otimização de Parâmetros**: Ajuste fino dos parâmetros do modelo para requisitos de deployment na edge

### 3. Construtor de Prompts (Agentes)
- **Geração de Linguagem Natural**: Gere prompts iniciais usando descrições em linguagem natural
- **Refinamento Iterativo**: Melhore os prompts com base nas respostas e desempenho dos modelos
- **Decomposição de Tarefas**: Divida tarefas complexas com encadeamento de prompts e outputs estruturados
- **Suporte a Variáveis**: Use variáveis em prompts para comportamento dinâmico dos agentes
- **Geração de Código para Produção**: Gere código pronto para produção para desenvolvimento rápido de aplicações

### 4. Execução em Massa e Avaliação
- **Teste Multi-Modelo**: Execute múltiplos prompts em modelos selecionados simultaneamente
- **Teste Eficiente em Escala**: Teste vários inputs e configurações de forma eficiente
- **Casos de Teste Personalizados**: Execute agentes com casos de teste para validar funcionalidades
- **Comparação de Desempenho**: Compare resultados entre diferentes modelos e configurações

### 5. Avaliação de Modelos com Conjuntos de Dados
- **Métricas Padrão**: Teste modelos de IA usando avaliadores integrados (pontuação F1, relevância, similaridade, coerência)
- **Avaliadores Personalizados**: Crie suas próprias métricas de avaliação para casos de uso específicos
- **Integração de Conjuntos de Dados**: Teste modelos contra conjuntos de dados abrangentes
- **Medida de Desempenho**: Quantifique o desempenho do modelo para decisões de deployment na edge

### 6. Capacidades de Fine-tuning
- **Customização de Modelos**: Personalize modelos para casos de uso e domínios específicos
- **Adaptação Especializada**: Adapte modelos para requisitos e domínios especializados
- **Otimização para Edge**: Ajuste modelos especificamente para restrições de deployment na edge
- **Treinamento Específico por Domínio**: Crie modelos adaptados para casos de uso específicos na edge

### 7. Integração com Ferramentas MCP
- **Conectividade com Ferramentas Externas**: Conecte agentes a ferramentas externas por meio de servidores Model Context Protocol
- **Ações no Mundo Real**: Permita que agentes consultem bases de dados, acessem APIs ou executem lógica personalizada
- **Servidores MCP Existentes**: Use ferramentas de comando (stdio) ou protocolos HTTP (eventos enviados pelo servidor)
- **Desenvolvimento de MCP Personalizado**: Construa e teste novos servidores MCP no Construtor de Agentes

### 8. Desenvolvimento e Teste de Agentes
- **Suporte a Chamadas de Função**: Permita que agentes invoquem funções externas dinamicamente
- **Teste de Integração em Tempo Real**: Teste integrações com execuções em tempo real e uso de ferramentas
- **Versionamento de Agentes**: Controle de versão para agentes com capacidades de comparação de resultados de avaliação
- **Depuração e Rastreamento**: Capacidades locais de rastreamento e depuração para desenvolvimento de agentes

## Fluxo de Trabalho de Desenvolvimento de IA na Edge

### Fase 1: Descoberta e Seleção de Modelos
1. **Explore o Catálogo de Modelos**: Use o catálogo de modelos para encontrar modelos adequados para deployment na edge
2. **Compare Desempenho**: Avalie modelos com base em tamanho, precisão e velocidade de inferência
3. **Teste Localmente**: Use modelos Ollama ou ONNX para testar localmente antes do deployment na edge
4. **Avalie Requisitos de Recursos**: Determine as necessidades de memória e computação para dispositivos na edge

### Fase 2: Otimização de Modelos
1. **Converta para ONNX**: Converta modelos selecionados para o formato ONNX para compatibilidade na edge
2. **Aplique Quantização**: Reduza o tamanho do modelo por meio de quantização INT8 ou INT4
3. **Otimização de Hardware**: Otimize para hardware específico na edge (ARM, x86, aceleradores especializados)
4. **Validação de Desempenho**: Valide se os modelos otimizados mantêm precisão aceitável

### Fase 3: Desenvolvimento de Aplicações
1. **Design de Agentes**: Use o Construtor de Agentes para criar agentes de IA otimizados para a edge
2. **Engenharia de Prompts**: Desenvolva prompts que funcionem efetivamente com modelos menores na edge
3. **Teste de Integração**: Teste agentes em condições simuladas da edge
4. **Geração de Código**: Gere código de produção otimizado para deployment na edge

### Fase 4: Avaliação e Teste
1. **Avaliação em Massa**: Teste múltiplas configurações para encontrar as melhores definições na edge
2. **Perfil de Desempenho**: Analise velocidade de inferência, uso de memória e precisão
3. **Simulação na Edge**: Teste em condições semelhantes ao ambiente de deployment na edge
4. **Teste de Estresse**: Avalie o desempenho sob várias condições de carga

### Fase 5: Preparação para Deployment
1. **Otimização Final**: Aplique otimizações finais com base nos resultados dos testes
2. **Empacotamento para Deployment**: Empacote modelos e código para deployment na edge
3. **Documentação**: Documente os requisitos e configurações de deployment
4. **Configuração de Monitoramento**: Prepare monitoramento e registro para deployment na edge

## Público-Alvo para Desenvolvimento de IA na Edge

### Desenvolvedores de IA na Edge
- Desenvolvedores de aplicações que criam dispositivos na edge e soluções IoT com IA
- Desenvolvedores de sistemas embarcados que integram capacidades de IA em dispositivos com restrições de recursos
- Desenvolvedores móveis criando aplicações de IA on-device para smartphones e tablets

### Engenheiros de IA na Edge
- Engenheiros de IA otimizando modelos para deployment na edge e gerenciando pipelines de inferência
- Engenheiros de DevOps implementando e gerenciando modelos de IA em infraestrutura distribuída na edge
- Engenheiros de desempenho otimizando cargas de trabalho de IA para restrições de hardware na edge

### Pesquisadores e Educadores
- Pesquisadores de IA desenvolvendo modelos e algoritmos eficientes para computação na edge
- Educadores ensinando conceitos de IA na edge e demonstrando técnicas de otimização
- Estudantes aprendendo sobre os desafios e soluções no deployment de IA na edge

## Casos de Uso de IA na Edge

### Dispositivos IoT Inteligentes
- **Reconhecimento de Imagens em Tempo Real**: Implementação de modelos de visão computacional em câmeras e sensores IoT
- **Processamento de Voz**: Implementação de reconhecimento de fala e processamento de linguagem natural em alto-falantes inteligentes
- **Manutenção Preditiva**: Execução de modelos de detecção de anomalias em dispositivos industriais na edge
- **Monitoramento Ambiental**: Deployment de modelos de análise de dados de sensores para aplicações ambientais

### Aplicações Móveis e Embarcadas
- **Tradução On-device**: Implementação de modelos de tradução de linguagem que funcionam offline
- **Realidade Aumentada**: Deployment de reconhecimento e rastreamento de objetos em tempo real para aplicações de RA
- **Monitoramento de Saúde**: Execução de modelos de análise de saúde em dispositivos vestíveis e equipamentos médicos
- **Sistemas Autônomos**: Implementação de modelos de tomada de decisão para drones, robôs e veículos

### Infraestrutura de Computação na Edge
- **Data Centers na Edge**: Deployment de modelos de IA em data centers na edge para aplicações de baixa latência
- **Integração com CDN**: Integração de capacidades de processamento de IA em redes de entrega de conteúdo
- **Edge 5G**: Aproveitamento da computação na edge com 5G para aplicações com IA
- **Computação em Névoa**: Implementação de processamento de IA em ambientes de computação em névoa

## Instalação e Configuração

### Instalação da Extensão
Instale a extensão do Kit de Ferramentas de IA diretamente do Visual Studio Code Marketplace:

**ID da Extensão**: `ms-windows-ai-studio.windows-ai-studio`

**Métodos de Instalação**:
1. **Marketplace do VS Code**: Pesquise por "AI Toolkit" na visualização de Extensões
2. **Linha de Comando**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalação Direta**: Baixe do [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Pré-requisitos para Desenvolvimento de IA na Edge
- **Visual Studio Code**: Versão mais recente recomendada
- **Ambiente Python**: Python 3.8+ com bibliotecas de IA necessárias
- **ONNX Runtime** (Opcional): Para inferência de modelos ONNX
- **Ollama** (Opcional): Para servir modelos localmente
- **Ferramentas de Aceleração de Hardware**: CUDA, OpenVINO ou aceleradores específicos da plataforma

### Configuração Inicial
1. **Ativação da Extensão**: Abra o VS Code e verifique se o Kit de Ferramentas de IA aparece na Barra de Atividades
2. **Configuração de Provedores de Modelos**: Configure acesso ao GitHub, OpenAI, Anthropic ou outros provedores de modelos
3. **Ambiente Local**: Configure o ambiente Python e instale os pacotes necessários
4. **Aceleração de Hardware**: Configure aceleração por GPU/NPU, se disponível
5. **Integração MCP**: Configure servidores Model Context Protocol, se necessário

### Lista de Verificação para Configuração Inicial
- [ ] Extensão do Kit de Ferramentas de IA instalada e ativada
- [ ] Catálogo de modelos acessível e modelos descobertos
- [ ] Playground funcional para teste de modelos
- [ ] Construtor de Agentes acessível para desenvolvimento de prompts
- [ ] Ambiente de desenvolvimento local configurado
- [ ] Aceleração de hardware (se disponível) configurada corretamente

## Começando com o Kit de Ferramentas de IA

### Guia de Início Rápido

Recomendamos começar com modelos hospedados pelo GitHub para uma experiência mais simplificada:

1. **Instalação**: Siga o [guia de instalação](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) para configurar o Kit de Ferramentas de IA no seu dispositivo
2. **Descoberta de Modelos**: Na visualização da extensão, selecione **CATALOG > Models** para explorar os modelos disponíveis
3. **Modelos do GitHub**: Comece com modelos hospedados pelo GitHub para integração ideal
4. **Teste no Playground**: Em qualquer cartão de modelo, selecione **Try in Playground** para começar a experimentar as capacidades do modelo

### Desenvolvimento de IA na Edge Passo a Passo

#### Passo 1: Exploração e Seleção de Modelos
1. Abra a visualização do Kit de Ferramentas de IA na Barra de Atividades do VS Code
2. Navegue pelo Catálogo de Modelos para encontrar modelos adequados para deployment na edge
3. Filtre por provedor (GitHub, ONNX, Ollama) com base nos seus requisitos na edge
4. Use **Try in Playground** para testar as capacidades do modelo imediatamente

#### Passo 2: Desenvolvimento de Agentes
1. Use o **Construtor de Prompts (Agentes)** para criar agentes de IA otimizados para a edge
2. Gerar prompts iniciais usando descrições em linguagem natural  
3. Iterar e refinar prompts com base nas respostas do modelo  
4. Integrar ferramentas MCP para capacidades avançadas de agentes  

#### Passo 3: Teste e Avaliação  
1. Utilize **Bulk Run** para testar múltiplos prompts em modelos selecionados  
2. Execute agentes com casos de teste para validar a funcionalidade  
3. Avalie precisão e desempenho usando métricas integradas ou personalizadas  
4. Compare diferentes modelos e configurações  

#### Passo 4: Ajuste e Otimização  
1. Personalize modelos para casos de uso específicos  
2. Aplique ajustes específicos para o domínio  
3. Otimize para restrições de implantação em dispositivos de borda  
4. Versione e compare diferentes configurações de agentes  

#### Passo 5: Preparação para Implantação  
1. Gere código pronto para produção usando o Agent Builder  
2. Configure conexões de servidor MCP para uso em produção  
3. Prepare pacotes de implantação para dispositivos de borda  
4. Configure métricas de monitorização e avaliação  

## Exemplos para o AI Toolkit  

Experimente os nossos exemplos  
Os [exemplos do AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) foram projetados para ajudar desenvolvedores e pesquisadores a explorar e implementar soluções de IA de forma eficaz.  

Os nossos exemplos incluem:  

Código de Exemplo: Exemplos pré-construídos para demonstrar funcionalidades de IA, como treinar, implantar ou integrar modelos em aplicações.  
Documentação: Guias e tutoriais para ajudar os utilizadores a compreender as funcionalidades do AI Toolkit e como utilizá-las.  
Pré-requisitos  

- Visual Studio Code  
- AI Toolkit para Visual Studio Code  
- Token de acesso pessoal (PAT) detalhado do GitHub  
- Foundry Local  

## Melhores Práticas para Desenvolvimento de IA na Borda  

### Seleção de Modelos  
- **Restrições de Tamanho**: Escolha modelos que se ajustem às limitações de memória dos dispositivos alvo  
- **Velocidade de Inferência**: Priorize modelos com tempos de inferência rápidos para aplicações em tempo real  
- **Compromissos de Precisão**: Equilibre a precisão do modelo com as restrições de recursos  
- **Compatibilidade de Formato**: Prefira formatos ONNX ou otimizados para hardware para implantação na borda  

### Técnicas de Otimização  
- **Quantização**: Utilize quantização INT8 ou INT4 para reduzir o tamanho do modelo e melhorar a velocidade  
- **Pruning**: Remova parâmetros desnecessários do modelo para reduzir os requisitos computacionais  
- **Distilação de Conhecimento**: Crie modelos menores que mantenham o desempenho de modelos maiores  
- **Aceleração de Hardware**: Aproveite NPUs, GPUs ou aceleradores especializados quando disponíveis  

### Fluxo de Trabalho de Desenvolvimento  
- **Testes Iterativos**: Teste frequentemente em condições semelhantes às da borda durante o desenvolvimento  
- **Monitorização de Desempenho**: Monitore continuamente o uso de recursos e a velocidade de inferência  
- **Controle de Versão**: Acompanhe versões de modelos e configurações de otimização  
- **Documentação**: Documente todas as decisões de otimização e compromissos de desempenho  

### Considerações para Implantação  
- **Monitorização de Recursos**: Monitore memória, CPU e uso de energia em produção  
- **Estratégias de Contingência**: Implemente mecanismos de fallback para falhas de modelo  
- **Mecanismos de Atualização**: Planeie atualizações de modelos e gestão de versões  
- **Segurança**: Implemente medidas de segurança adequadas para aplicações de IA na borda  

## Integração com Frameworks de IA na Borda  

### ONNX Runtime  
- **Implantação Multiplataforma**: Implante modelos ONNX em diferentes plataformas de borda  
- **Otimização de Hardware**: Aproveite as otimizações específicas de hardware do ONNX Runtime  
- **Suporte Móvel**: Utilize ONNX Runtime Mobile para aplicações em smartphones e tablets  
- **Integração IoT**: Implante em dispositivos IoT usando distribuições leves do ONNX Runtime  

### Windows ML  
- **Dispositivos Windows**: Otimize para dispositivos de borda baseados em Windows e PCs  
- **Aceleração NPU**: Aproveite as Unidades de Processamento Neural em dispositivos Windows  
- **DirectML**: Utilize DirectML para aceleração de GPU em plataformas Windows  
- **Integração UWP**: Integre com aplicações da Universal Windows Platform  

### TensorFlow Lite  
- **Otimização Móvel**: Implante modelos TensorFlow Lite em dispositivos móveis e incorporados  
- **Delegados de Hardware**: Utilize delegados de hardware especializados para aceleração  
- **Microcontroladores**: Implante em microcontroladores usando TensorFlow Lite Micro  
- **Suporte Multiplataforma**: Implante em Android, iOS e sistemas Linux incorporados  

### Azure IoT Edge  
- **Híbrido Nuvem-Borda**: Combine treino na nuvem com inferência na borda  
- **Implantação de Módulos**: Implante modelos de IA como módulos do IoT Edge  
- **Gestão de Dispositivos**: Gerencie dispositivos de borda e atualizações de modelos remotamente  
- **Telemetria**: Colete dados de desempenho e métricas de modelos das implantações na borda  

## Cenários Avançados de IA na Borda  

### Implantação Multi-Modelo  
- **Conjuntos de Modelos**: Implante múltiplos modelos para melhorar a precisão ou redundância  
- **Testes A/B**: Teste diferentes modelos simultaneamente em dispositivos de borda  
- **Seleção Dinâmica**: Escolha modelos com base nas condições atuais do dispositivo  
- **Partilha de Recursos**: Otimize o uso de recursos entre múltiplos modelos implantados  

### Aprendizagem Federada  
- **Treino Distribuído**: Treine modelos em múltiplos dispositivos de borda  
- **Preservação de Privacidade**: Mantenha os dados de treino locais enquanto compartilha melhorias de modelos  
- **Aprendizagem Colaborativa**: Permita que dispositivos aprendam com experiências coletivas  
- **Coordenação Borda-Nuvem**: Coordene o aprendizado entre dispositivos de borda e infraestrutura de nuvem  

### Processamento em Tempo Real  
- **Processamento de Fluxo**: Processe fluxos contínuos de dados em dispositivos de borda  
- **Inferência de Baixa Latência**: Otimize para latência mínima de inferência  
- **Processamento em Lote**: Processe lotes de dados de forma eficiente em dispositivos de borda  
- **Processamento Adaptativo**: Ajuste o processamento com base nas capacidades atuais do dispositivo  

## Resolução de Problemas no Desenvolvimento de IA na Borda  

### Problemas Comuns  
- **Restrições de Memória**: Modelo muito grande para a memória do dispositivo alvo  
- **Velocidade de Inferência**: Inferência do modelo muito lenta para requisitos em tempo real  
- **Degradação de Precisão**: A otimização reduz a precisão do modelo de forma inaceitável  
- **Compatibilidade de Hardware**: Modelo não compatível com o hardware alvo  

### Estratégias de Depuração  
- **Perfil de Desempenho**: Utilize os recursos de rastreamento do AI Toolkit para identificar gargalos  
- **Monitorização de Recursos**: Monitore o uso de memória e CPU durante o desenvolvimento  
- **Testes Incrementais**: Teste otimizações de forma incremental para isolar problemas  
- **Simulação de Hardware**: Utilize ferramentas de desenvolvimento para simular o hardware alvo  

### Soluções de Otimização  
- **Quantização Adicional**: Aplique técnicas de quantização mais agressivas  
- **Arquitetura de Modelo**: Considere diferentes arquiteturas de modelo otimizadas para borda  
- **Otimização de Pré-processamento**: Otimize o pré-processamento de dados para restrições de borda  
- **Otimização de Inferência**: Utilize otimizações de inferência específicas para hardware  

## Recursos e Próximos Passos  

### Documentação Oficial  
- [Documentação para Desenvolvedores do AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guia de Instalação e Configuração](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentação de Apps Inteligentes do VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentação do Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Comunidade e Suporte  
- [Repositório GitHub do AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemas e Solicitações de Funcionalidades no GitHub](https://aka.ms/AIToolkit/feedback)  
- [Comunidade Discord do Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace de Extensões do VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Recursos Técnicos  
- [Documentação do ONNX Runtime](https://onnxruntime.ai/)  
- [Documentação do Ollama](https://ollama.ai/)  
- [Documentação do Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Caminhos de Aprendizagem  
- [Curso de Fundamentos de IA na Borda](../Module01/README.md)  
- [Guia de Modelos de Linguagem Pequenos](../Module02/README.md)  
- [Estratégias de Implantação na Borda](../Module03/README.md)  
- [Desenvolvimento de IA na Borda para Windows](./windowdeveloper.md)  

### Recursos Adicionais  
- **Estatísticas do Repositório**: 1.8k+ estrelas, 150+ forks, 18+ contribuidores  
- **Licença**: Licença MIT  
- **Segurança**: Aplicam-se políticas de segurança da Microsoft  
- **Telemetria**: Respeita as configurações de telemetria do VS Code  

## Conclusão  

O AI Toolkit para Visual Studio Code representa uma plataforma abrangente para o desenvolvimento moderno de IA, oferecendo capacidades de desenvolvimento de agentes simplificadas que são particularmente valiosas para aplicações de IA na borda. Com seu extenso catálogo de modelos que suporta fornecedores como Anthropic, OpenAI, GitHub e Google, combinado com execução local através de ONNX e Ollama, o toolkit oferece a flexibilidade necessária para diversos cenários de implantação na borda.  

A força do toolkit reside na sua abordagem integrada—desde a descoberta e experimentação de modelos no Playground até o desenvolvimento sofisticado de agentes com o Prompt Builder, capacidades abrangentes de avaliação e integração perfeita com ferramentas MCP. Para desenvolvedores de IA na borda, isso significa prototipagem rápida e teste de agentes de IA antes da implantação na borda, com a capacidade de iterar rapidamente e otimizar para ambientes com restrições de recursos.  

Vantagens principais para o desenvolvimento de IA na borda incluem:  
- **Experimentação Rápida**: Teste modelos e agentes rapidamente antes de comprometer-se com a implantação na borda  
- **Flexibilidade Multi-Fornecedor**: Acesse modelos de várias fontes para encontrar soluções ideais para borda  
- **Desenvolvimento Local**: Teste com ONNX e Ollama para desenvolvimento offline e preservação de privacidade  
- **Pronto para Produção**: Gere código pronto para produção e integre com ferramentas externas via MCP  
- **Avaliação Abrangente**: Utilize métricas integradas e personalizadas para validar o desempenho de IA na borda  

À medida que a IA continua a avançar para cenários de implantação na borda, o AI Toolkit para VS Code fornece o ambiente de desenvolvimento e fluxo de trabalho necessários para construir, testar e otimizar aplicações inteligentes para ambientes com restrições de recursos. Seja desenvolvendo soluções IoT, aplicações de IA móvel ou sistemas de inteligência incorporada, o conjunto abrangente de recursos e fluxo de trabalho integrado do toolkit suporta todo o ciclo de vida do desenvolvimento de IA na borda.  

Com desenvolvimento contínuo e uma comunidade ativa (1.8k+ estrelas no GitHub), o AI Toolkit permanece na vanguarda das ferramentas de desenvolvimento de IA, evoluindo continuamente para atender às necessidades dos desenvolvedores modernos de IA que constroem para cenários de implantação na borda.  

[Próximo Foundry Local](./foundrylocal.md)  

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.