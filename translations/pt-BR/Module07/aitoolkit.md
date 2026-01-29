# AI Toolkit para Visual Studio Code - Guia de Desenvolvimento de Edge AI

## Introdução

Bem-vindo ao guia completo para usar o AI Toolkit no Visual Studio Code no desenvolvimento de Edge AI. À medida que a inteligência artificial avança do processamento centralizado na nuvem para dispositivos distribuídos na borda, os desenvolvedores precisam de ferramentas poderosas e integradas que lidem com os desafios únicos do deployment na borda - desde restrições de recursos até requisitos de operação offline.

O AI Toolkit para Visual Studio Code preenche essa lacuna ao oferecer um ambiente de desenvolvimento completo, projetado especificamente para construir, testar e otimizar aplicações de IA que funcionem eficientemente em dispositivos de borda. Seja você desenvolvendo para sensores IoT, dispositivos móveis, sistemas embarcados ou servidores de borda, este toolkit simplifica todo o fluxo de trabalho de desenvolvimento dentro do ambiente familiar do VS Code.

Este guia irá conduzi-lo pelos conceitos essenciais, ferramentas e melhores práticas para aproveitar o AI Toolkit em seus projetos de Edge AI, desde a seleção inicial de modelos até o deployment em produção.

## Visão Geral

O AI Toolkit para Visual Studio Code é uma extensão poderosa que simplifica o desenvolvimento de agentes e a criação de aplicações de IA. O toolkit oferece capacidades abrangentes para explorar, avaliar e implementar modelos de IA de uma ampla gama de provedores — incluindo Anthropic, OpenAI, GitHub, Google — enquanto suporta a execução de modelos locais usando ONNX e Ollama.

O que diferencia o AI Toolkit é sua abordagem abrangente para todo o ciclo de vida do desenvolvimento de IA. Diferentemente das ferramentas tradicionais de desenvolvimento de IA que focam em aspectos isolados, o AI Toolkit fornece um ambiente integrado que cobre descoberta de modelos, experimentação, desenvolvimento de agentes, avaliação e deployment — tudo dentro do ambiente familiar do VS Code.

A plataforma é projetada especificamente para prototipagem rápida e deployment em produção, com recursos como geração de prompts, iniciadores rápidos, integrações perfeitas com ferramentas MCP (Model Context Protocol) e capacidades extensivas de avaliação. Para o desenvolvimento de Edge AI, isso significa que você pode desenvolver, testar e otimizar aplicações de IA para cenários de deployment na borda de forma eficiente, mantendo todo o fluxo de trabalho de desenvolvimento dentro do VS Code.

## Objetivos de Aprendizado

Ao final deste guia, você será capaz de:

### Competências Centrais
- **Instalar e configurar** o AI Toolkit para Visual Studio Code para fluxos de trabalho de desenvolvimento de Edge AI
- **Navegar e utilizar** a interface do AI Toolkit, incluindo o Catálogo de Modelos, Playground e Builder de Agentes
- **Selecionar e avaliar** modelos de IA adequados para deployment na borda com base em desempenho e restrições de recursos
- **Converter e otimizar** modelos usando o formato ONNX e técnicas de quantização para dispositivos de borda

### Habilidades de Desenvolvimento de Edge AI
- **Projetar e implementar** aplicações de Edge AI usando o ambiente de desenvolvimento integrado
- **Realizar testes de modelos** em condições semelhantes à borda usando inferência local e monitoramento de recursos
- **Criar e personalizar** agentes de IA otimizados para cenários de deployment na borda
- **Avaliar o desempenho de modelos** usando métricas relevantes para computação na borda (latência, uso de memória, precisão)

### Otimização e Deployment
- **Aplicar técnicas de quantização e poda** para reduzir o tamanho do modelo enquanto mantém um desempenho aceitável
- **Otimizar modelos** para plataformas de hardware específicas na borda, incluindo aceleração por CPU, GPU e NPU
- **Implementar melhores práticas** para desenvolvimento de Edge AI, incluindo gerenciamento de recursos e estratégias de fallback
- **Preparar modelos e aplicações** para deployment em dispositivos de borda

### Conceitos Avançados de Edge AI
- **Integrar com frameworks de Edge AI** incluindo ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementar arquiteturas multi-modelo** e cenários de aprendizado federado para ambientes de borda
- **Solucionar problemas comuns de Edge AI** incluindo restrições de memória, velocidade de inferência e compatibilidade de hardware
- **Projetar estratégias de monitoramento e registro** para aplicações de Edge AI em produção

### Aplicação Prática
- **Construir soluções completas de Edge AI** desde a seleção de modelos até o deployment
- **Demonstrar proficiência** em fluxos de trabalho de desenvolvimento específicos para borda e técnicas de otimização
- **Aplicar conceitos aprendidos** em casos de uso reais de Edge AI, incluindo IoT, dispositivos móveis e aplicações embarcadas
- **Avaliar e comparar** diferentes estratégias de deployment de Edge AI e seus trade-offs

## Principais Recursos para Desenvolvimento de Edge AI

### 1. Catálogo de Modelos e Descoberta
- **Suporte Multi-Provedor**: Navegue e acesse modelos de IA de Anthropic, OpenAI, GitHub, Google e outros provedores
- **Integração de Modelos Locais**: Descoberta simplificada de modelos ONNX e Ollama para deployment na borda
- **Modelos do GitHub**: Integração direta com o hosting de modelos do GitHub para acesso simplificado
- **Comparação de Modelos**: Compare modelos lado a lado para encontrar o equilíbrio ideal para as restrições de dispositivos de borda

### 2. Playground Interativo
- **Ambiente de Teste Interativo**: Experimentação rápida com capacidades de modelos em um ambiente controlado
- **Suporte Multi-modal**: Teste com imagens, texto e outros inputs típicos em cenários de borda
- **Experimentação em Tempo Real**: Feedback imediato sobre respostas e desempenho do modelo
- **Otimização de Parâmetros**: Ajuste fino dos parâmetros do modelo para requisitos de deployment na borda

### 3. Builder de Prompts (Agentes)
- **Geração de Linguagem Natural**: Gere prompts iniciais usando descrições em linguagem natural
- **Refinamento Iterativo**: Melhore os prompts com base nas respostas e desempenho do modelo
- **Decomposição de Tarefas**: Divida tarefas complexas com encadeamento de prompts e saídas estruturadas
- **Suporte a Variáveis**: Use variáveis em prompts para comportamento dinâmico de agentes
- **Geração de Código para Produção**: Gere código pronto para produção para desenvolvimento rápido de aplicativos

### 4. Execução em Massa e Avaliação
- **Teste Multi-Modelo**: Execute múltiplos prompts em modelos selecionados simultaneamente
- **Teste Eficiente em Escala**: Teste vários inputs e configurações de forma eficiente
- **Casos de Teste Personalizados**: Execute agentes com casos de teste para validar funcionalidades
- **Comparação de Desempenho**: Compare resultados entre diferentes modelos e configurações

### 5. Avaliação de Modelos com Conjuntos de Dados
- **Métricas Padrão**: Teste modelos de IA usando avaliadores integrados (F1 score, relevância, similaridade, coerência)
- **Avaliadores Personalizados**: Crie suas próprias métricas de avaliação para casos de uso específicos
- **Integração com Conjuntos de Dados**: Teste modelos contra conjuntos de dados abrangentes
- **Medição de Desempenho**: Quantifique o desempenho do modelo para decisões de deployment na borda

### 6. Capacidades de Fine-tuning
- **Customização de Modelos**: Personalize modelos para casos de uso e domínios específicos
- **Adaptação Especializada**: Adapte modelos para requisitos e domínios especializados
- **Otimização para Borda**: Ajuste modelos especificamente para restrições de deployment na borda
- **Treinamento Específico de Domínio**: Crie modelos adaptados para casos de uso específicos na borda

### 7. Integração com Ferramentas MCP
- **Conectividade com Ferramentas Externas**: Conecte agentes a ferramentas externas por meio de servidores Model Context Protocol
- **Ações no Mundo Real**: Permita que agentes consultem bancos de dados, acessem APIs ou executem lógica personalizada
- **Servidores MCP Existentes**: Use ferramentas de comando (stdio) ou protocolos HTTP (eventos enviados pelo servidor)
- **Desenvolvimento de MCP Personalizado**: Construa e teste novos servidores MCP no Builder de Agentes

### 8. Desenvolvimento e Teste de Agentes
- **Suporte a Chamadas de Função**: Permita que agentes invoquem funções externas dinamicamente
- **Teste de Integração em Tempo Real**: Teste integrações com execuções em tempo real e uso de ferramentas
- **Versionamento de Agentes**: Controle de versão para agentes com capacidades de comparação de resultados de avaliação
- **Depuração e Rastreamento**: Capacidades de rastreamento e depuração local para desenvolvimento de agentes

## Fluxo de Trabalho de Desenvolvimento de Edge AI

### Fase 1: Descoberta e Seleção de Modelos
1. **Explore o Catálogo de Modelos**: Use o catálogo de modelos para encontrar modelos adequados para deployment na borda
2. **Compare Desempenho**: Avalie modelos com base em tamanho, precisão e velocidade de inferência
3. **Teste Localmente**: Use modelos Ollama ou ONNX para testar localmente antes do deployment na borda
4. **Avalie Requisitos de Recursos**: Determine as necessidades de memória e computação para dispositivos de borda alvo

### Fase 2: Otimização de Modelos
1. **Converta para ONNX**: Converta modelos selecionados para o formato ONNX para compatibilidade com a borda
2. **Aplique Quantização**: Reduza o tamanho do modelo por meio de quantização INT8 ou INT4
3. **Otimização de Hardware**: Otimize para hardware de borda alvo (ARM, x86, aceleradores especializados)
4. **Validação de Desempenho**: Valide que os modelos otimizados mantêm precisão aceitável

### Fase 3: Desenvolvimento de Aplicações
1. **Design de Agentes**: Use o Builder de Agentes para criar agentes de IA otimizados para borda
2. **Engenharia de Prompts**: Desenvolva prompts que funcionem efetivamente com modelos menores de borda
3. **Teste de Integração**: Teste agentes em condições simuladas de borda
4. **Geração de Código**: Gere código de produção otimizado para deployment na borda

### Fase 4: Avaliação e Teste
1. **Avaliação em Lote**: Teste múltiplas configurações para encontrar as melhores definições para borda
2. **Perfil de Desempenho**: Analise velocidade de inferência, uso de memória e precisão
3. **Simulação de Borda**: Teste em condições semelhantes ao ambiente de deployment na borda
4. **Teste de Estresse**: Avalie o desempenho sob várias condições de carga

### Fase 5: Preparação para Deployment
1. **Otimização Final**: Aplique otimizações finais com base nos resultados dos testes
2. **Empacotamento para Deployment**: Empacote modelos e código para deployment na borda
3. **Documentação**: Documente os requisitos e configurações de deployment
4. **Configuração de Monitoramento**: Prepare monitoramento e registro para deployment na borda

## Público-Alvo para Desenvolvimento de Edge AI

### Desenvolvedores de Edge AI
- Desenvolvedores de aplicações que criam dispositivos de borda e soluções IoT com IA
- Desenvolvedores de sistemas embarcados que integram capacidades de IA em dispositivos com restrições de recursos
- Desenvolvedores móveis criando aplicações de IA on-device para smartphones e tablets

### Engenheiros de Edge AI
- Engenheiros de IA otimizando modelos para deployment na borda e gerenciando pipelines de inferência
- Engenheiros de DevOps implantando e gerenciando modelos de IA em infraestrutura distribuída na borda
- Engenheiros de desempenho otimizando cargas de trabalho de IA para restrições de hardware na borda

### Pesquisadores e Educadores
- Pesquisadores de IA desenvolvendo modelos e algoritmos eficientes para computação na borda
- Educadores ensinando conceitos de Edge AI e demonstrando técnicas de otimização
- Estudantes aprendendo sobre os desafios e soluções no deployment de Edge AI

## Casos de Uso de Edge AI

### Dispositivos IoT Inteligentes
- **Reconhecimento de Imagem em Tempo Real**: Implantar modelos de visão computacional em câmeras e sensores IoT
- **Processamento de Voz**: Implementar reconhecimento de fala e processamento de linguagem natural em alto-falantes inteligentes
- **Manutenção Preditiva**: Executar modelos de detecção de anomalias em dispositivos industriais de borda
- **Monitoramento Ambiental**: Implantar modelos de análise de dados de sensores para aplicações ambientais

### Aplicações Móveis e Embarcadas
- **Tradução On-device**: Implementar modelos de tradução de idiomas que funcionem offline
- **Realidade Aumentada**: Implantar reconhecimento e rastreamento de objetos em tempo real para aplicações de RA
- **Monitoramento de Saúde**: Executar modelos de análise de saúde em dispositivos vestíveis e equipamentos médicos
- **Sistemas Autônomos**: Implementar modelos de tomada de decisão para drones, robôs e veículos

### Infraestrutura de Computação na Borda
- **Data Centers na Borda**: Implantar modelos de IA em data centers na borda para aplicações de baixa latência
- **Integração com CDN**: Integrar capacidades de processamento de IA em redes de entrega de conteúdo
- **Borda 5G**: Aproveitar a computação na borda 5G para aplicações com IA
- **Computação em Névoa**: Implementar processamento de IA em ambientes de computação em névoa

## Instalação e Configuração

### Instalação da Extensão
Instale a extensão AI Toolkit diretamente do Visual Studio Code Marketplace:

**ID da Extensão**: `ms-windows-ai-studio.windows-ai-studio`

**Métodos de Instalação**:
1. **Marketplace do VS Code**: Pesquise por "AI Toolkit" na visualização de Extensões
2. **Linha de Comando**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalação Direta**: Baixe do [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Pré-requisitos para Desenvolvimento de Edge AI
- **Visual Studio Code**: Versão mais recente recomendada
- **Ambiente Python**: Python 3.8+ com bibliotecas de IA necessárias
- **ONNX Runtime** (Opcional): Para inferência de modelos ONNX
- **Ollama** (Opcional): Para servir modelos localmente
- **Ferramentas de Aceleração de Hardware**: CUDA, OpenVINO ou aceleradores específicos da plataforma

### Configuração Inicial
1. **Ativação da Extensão**: Abra o VS Code e verifique se o AI Toolkit aparece na Barra de Atividades
2. **Configuração de Provedores de Modelos**: Configure acesso ao GitHub, OpenAI, Anthropic ou outros provedores de modelos
3. **Ambiente Local**: Configure o ambiente Python e instale os pacotes necessários
4. **Aceleração de Hardware**: Configure aceleração por GPU/NPU, se disponível
5. **Integração MCP**: Configure servidores Model Context Protocol, se necessário

### Checklist de Configuração Inicial
- [ ] Extensão AI Toolkit instalada e ativada
- [ ] Catálogo de modelos acessível e modelos descobertos
- [ ] Playground funcional para teste de modelos
- [ ] Builder de Agentes acessível para desenvolvimento de prompts
- [ ] Ambiente de desenvolvimento local configurado
- [ ] Aceleração de hardware (se disponível) configurada corretamente

## Começando com o AI Toolkit

### Guia de Início Rápido

Recomendamos começar com modelos hospedados pelo GitHub para uma experiência mais simplificada:

1. **Instalação**: Siga o [guia de instalação](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) para configurar o AI Toolkit no seu dispositivo
2. **Descoberta de Modelos**: Na visualização da extensão, selecione **CATALOG > Models** para explorar os modelos disponíveis
3. **Modelos do GitHub**: Comece com modelos hospedados pelo GitHub para integração ideal
4. **Teste no Playground**: Em qualquer cartão de modelo, selecione **Try in Playground** para começar a experimentar as capacidades do modelo

### Desenvolvimento de Edge AI Passo a Passo

#### Passo 1: Exploração e Seleção de Modelos
1. Abra a visualização do AI Toolkit na Barra de Atividades do VS Code
2. Navegue pelo Catálogo de Modelos para encontrar modelos adequados para deployment na borda
3. Filtre por provedor (GitHub, ONNX, Ollama) com base nos seus requisitos de borda
4. Use **Try in Playground** para testar as capacidades do modelo imediatamente

#### Passo 2: Desenvolvimento de Agentes
1. Use o **Builder de Prompts (Agentes)** para criar agentes de IA otimizados para borda
2. Gerar prompts iniciais usando descrições em linguagem natural  
3. Iterar e refinar prompts com base nas respostas do modelo  
4. Integrar ferramentas MCP para aprimorar as capacidades dos agentes  

#### Etapa 3: Teste e Avaliação  
1. Use **Bulk Run** para testar múltiplos prompts em modelos selecionados  
2. Execute agentes com casos de teste para validar a funcionalidade  
3. Avalie precisão e desempenho usando métricas integradas ou personalizadas  
4. Compare diferentes modelos e configurações  

#### Etapa 4: Ajuste e Otimização  
1. Personalize modelos para casos de uso específicos  
2. Aplique ajustes específicos para o domínio  
3. Otimize para restrições de implantação em dispositivos de borda  
4. Versione e compare diferentes configurações de agentes  

#### Etapa 5: Preparação para Implantação  
1. Gere código pronto para produção usando o Agent Builder  
2. Configure conexões com o servidor MCP para uso em produção  
3. Prepare pacotes de implantação para dispositivos de borda  
4. Configure métricas de monitoramento e avaliação  

## Exemplos para o AI Toolkit  

Experimente nossos exemplos  
Os [exemplos do AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) foram projetados para ajudar desenvolvedores e pesquisadores a explorar e implementar soluções de IA de forma eficaz.  

Nossos exemplos incluem:  

Código de exemplo: Exemplos pré-construídos para demonstrar funcionalidades de IA, como treinamento, implantação ou integração de modelos em aplicações.  
Documentação: Guias e tutoriais para ajudar os usuários a entender os recursos do AI Toolkit e como utilizá-los.  
Pré-requisitos  

- Visual Studio Code  
- AI Toolkit para Visual Studio Code  
- Token de acesso pessoal (PAT) do GitHub  
- Foundry Local  

## Melhores Práticas para Desenvolvimento de IA na Borda  

### Seleção de Modelos  
- **Restrições de Tamanho**: Escolha modelos que se ajustem às limitações de memória dos dispositivos-alvo  
- **Velocidade de Inferência**: Priorize modelos com tempos de inferência rápidos para aplicações em tempo real  
- **Compromissos de Precisão**: Equilibre a precisão do modelo com as restrições de recursos  
- **Compatibilidade de Formato**: Prefira formatos ONNX ou otimizados para hardware para implantação na borda  

### Técnicas de Otimização  
- **Quantização**: Use quantização INT8 ou INT4 para reduzir o tamanho do modelo e melhorar a velocidade  
- **Pruning**: Remova parâmetros desnecessários do modelo para reduzir os requisitos computacionais  
- **Distilação de Conhecimento**: Crie modelos menores que mantenham o desempenho de modelos maiores  
- **Aceleração de Hardware**: Aproveite NPUs, GPUs ou aceleradores especializados quando disponíveis  

### Fluxo de Trabalho de Desenvolvimento  
- **Testes Iterativos**: Teste frequentemente em condições semelhantes às da borda durante o desenvolvimento  
- **Monitoramento de Desempenho**: Monitore continuamente o uso de recursos e a velocidade de inferência  
- **Controle de Versão**: Acompanhe versões de modelos e configurações de otimização  
- **Documentação**: Documente todas as decisões de otimização e os compromissos de desempenho  

### Considerações para Implantação  
- **Monitoramento de Recursos**: Monitore memória, CPU e uso de energia em produção  
- **Estratégias de Contingência**: Implemente mecanismos de fallback para falhas de modelo  
- **Mecanismos de Atualização**: Planeje atualizações de modelos e gerenciamento de versões  
- **Segurança**: Implemente medidas de segurança apropriadas para aplicações de IA na borda  

## Integração com Frameworks de IA na Borda  

### ONNX Runtime  
- **Implantação Multiplataforma**: Implante modelos ONNX em diferentes plataformas de borda  
- **Otimização de Hardware**: Aproveite as otimizações específicas de hardware do ONNX Runtime  
- **Suporte Móvel**: Use ONNX Runtime Mobile para aplicações em smartphones e tablets  
- **Integração com IoT**: Implante em dispositivos IoT usando distribuições leves do ONNX Runtime  

### Windows ML  
- **Dispositivos Windows**: Otimize para dispositivos de borda baseados em Windows e PCs  
- **Aceleração NPU**: Aproveite as Unidades de Processamento Neural em dispositivos Windows  
- **DirectML**: Use DirectML para aceleração de GPU em plataformas Windows  
- **Integração UWP**: Integre com aplicações da Plataforma Universal do Windows  

### TensorFlow Lite  
- **Otimização Móvel**: Implante modelos TensorFlow Lite em dispositivos móveis e embarcados  
- **Delegados de Hardware**: Use delegados de hardware especializados para aceleração  
- **Microcontroladores**: Implante em microcontroladores usando TensorFlow Lite Micro  
- **Suporte Multiplataforma**: Implante em Android, iOS e sistemas Linux embarcados  

### Azure IoT Edge  
- **Híbrido Nuvem-Borda**: Combine treinamento na nuvem com inferência na borda  
- **Implantação de Módulos**: Implante modelos de IA como módulos do IoT Edge  
- **Gerenciamento de Dispositivos**: Gerencie dispositivos de borda e atualizações de modelos remotamente  
- **Telemetria**: Colete dados de desempenho e métricas de modelos das implantações na borda  

## Cenários Avançados de IA na Borda  

### Implantação de Múltiplos Modelos  
- **Conjuntos de Modelos**: Implante múltiplos modelos para melhorar a precisão ou redundância  
- **Testes A/B**: Teste diferentes modelos simultaneamente em dispositivos de borda  
- **Seleção Dinâmica**: Escolha modelos com base nas condições atuais do dispositivo  
- **Compartilhamento de Recursos**: Otimize o uso de recursos entre múltiplos modelos implantados  

### Aprendizado Federado  
- **Treinamento Distribuído**: Treine modelos em múltiplos dispositivos de borda  
- **Preservação de Privacidade**: Mantenha os dados de treinamento locais enquanto compartilha melhorias de modelos  
- **Aprendizado Colaborativo**: Permita que dispositivos aprendam com experiências coletivas  
- **Coordenação Borda-Nuvem**: Coordene o aprendizado entre dispositivos de borda e infraestrutura de nuvem  

### Processamento em Tempo Real  
- **Processamento de Fluxo**: Processe fluxos contínuos de dados em dispositivos de borda  
- **Inferência de Baixa Latência**: Otimize para latência mínima de inferência  
- **Processamento em Lote**: Processe lotes de dados de forma eficiente em dispositivos de borda  
- **Processamento Adaptativo**: Ajuste o processamento com base nas capacidades atuais do dispositivo  

## Solução de Problemas no Desenvolvimento de IA na Borda  

### Problemas Comuns  
- **Restrições de Memória**: Modelo muito grande para a memória do dispositivo-alvo  
- **Velocidade de Inferência**: Inferência do modelo muito lenta para requisitos em tempo real  
- **Degradação de Precisão**: A otimização reduz a precisão do modelo de forma inaceitável  
- **Compatibilidade de Hardware**: Modelo incompatível com o hardware-alvo  

### Estratégias de Depuração  
- **Perfil de Desempenho**: Use os recursos de rastreamento do AI Toolkit para identificar gargalos  
- **Monitoramento de Recursos**: Monitore o uso de memória e CPU durante o desenvolvimento  
- **Testes Incrementais**: Teste otimizações de forma incremental para isolar problemas  
- **Simulação de Hardware**: Use ferramentas de desenvolvimento para simular o hardware-alvo  

### Soluções de Otimização  
- **Quantização Adicional**: Aplique técnicas de quantização mais agressivas  
- **Arquitetura de Modelo**: Considere diferentes arquiteturas de modelo otimizadas para borda  
- **Otimização de Pré-processamento**: Otimize o pré-processamento de dados para restrições da borda  
- **Otimização de Inferência**: Use otimizações de inferência específicas para hardware  

## Recursos e Próximos Passos  

### Documentação Oficial  
- [Documentação para Desenvolvedores do AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guia de Instalação e Configuração](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentação de Aplicativos Inteligentes do VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentação do Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Comunidade e Suporte  
- [Repositório GitHub do AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemas e Solicitações de Recursos no GitHub](https://aka.ms/AIToolkit/feedback)  
- [Comunidade Discord do Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace de Extensões do VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Recursos Técnicos  
- [Documentação do ONNX Runtime](https://onnxruntime.ai/)  
- [Documentação do Ollama](https://ollama.ai/)  
- [Documentação do Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Caminhos de Aprendizado  
- [Curso de Fundamentos de IA na Borda](../Module01/README.md)  
- [Guia de Modelos de Linguagem Pequenos](../Module02/README.md)  
- [Estratégias de Implantação na Borda](../Module03/README.md)  
- [Desenvolvimento de IA na Borda com Windows](./windowdeveloper.md)  

### Recursos Adicionais  
- **Estatísticas do Repositório**: Mais de 1.8k estrelas, 150+ forks, 18+ contribuidores  
- **Licença**: Licença MIT  
- **Segurança**: Políticas de segurança da Microsoft aplicáveis  
- **Telemetria**: Respeita as configurações de telemetria do VS Code  

## Conclusão  

O AI Toolkit para Visual Studio Code representa uma plataforma abrangente para o desenvolvimento moderno de IA, oferecendo capacidades de desenvolvimento de agentes simplificadas que são particularmente valiosas para aplicações de IA na borda. Com seu extenso catálogo de modelos que suporta provedores como Anthropic, OpenAI, GitHub e Google, combinado com execução local via ONNX e Ollama, o toolkit oferece a flexibilidade necessária para diversos cenários de implantação na borda.  

A força do toolkit está em sua abordagem integrada—desde a descoberta e experimentação de modelos no Playground até o desenvolvimento sofisticado de agentes com o Prompt Builder, capacidades abrangentes de avaliação e integração perfeita com ferramentas MCP. Para desenvolvedores de IA na borda, isso significa prototipagem rápida e teste de agentes de IA antes da implantação na borda, com a capacidade de iterar rapidamente e otimizar para ambientes com restrições de recursos.  

Principais vantagens para o desenvolvimento de IA na borda incluem:  
- **Experimentação Rápida**: Teste modelos e agentes rapidamente antes de comprometer-se com a implantação na borda  
- **Flexibilidade Multiplataforma**: Acesse modelos de várias fontes para encontrar soluções ideais para borda  
- **Desenvolvimento Local**: Teste com ONNX e Ollama para desenvolvimento offline e preservação de privacidade  
- **Pronto para Produção**: Gere código pronto para produção e integre com ferramentas externas via MCP  
- **Avaliação Abrangente**: Use métricas integradas e personalizadas para validar o desempenho de IA na borda  

À medida que a IA continua avançando para cenários de implantação na borda, o AI Toolkit para VS Code fornece o ambiente de desenvolvimento e o fluxo de trabalho necessários para construir, testar e otimizar aplicações inteligentes para ambientes com restrições de recursos. Seja desenvolvendo soluções de IoT, aplicações de IA móvel ou sistemas de inteligência embarcada, o conjunto de recursos abrangente e o fluxo de trabalho integrado do toolkit suportam todo o ciclo de vida do desenvolvimento de IA na borda.  

Com desenvolvimento contínuo e uma comunidade ativa (mais de 1.8k estrelas no GitHub), o AI Toolkit permanece na vanguarda das ferramentas de desenvolvimento de IA, evoluindo continuamente para atender às necessidades dos desenvolvedores modernos de IA que constroem para cenários de implantação na borda.  

[Próximo Foundry Local](./foundrylocal.md)  

---

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.