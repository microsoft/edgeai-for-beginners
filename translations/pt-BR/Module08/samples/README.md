# Módulo 08 Exemplos: Guia de Desenvolvimento Local do Foundry

## Visão Geral

Esta coleção abrangente demonstra as abordagens do **Foundry Local SDK** e **Comandos Shell** para construir aplicações de IA prontas para produção. Cada exemplo destaca diferentes aspectos do desenvolvimento de IA na borda, desde integração básica com REST até sistemas avançados de múltiplos agentes.

## Abordagem de Desenvolvimento: SDK vs Comandos Shell

### Use o Foundry Local SDK Quando:

- **Controle Programático**: Você precisa de controle total sobre o ciclo de vida do agente, avaliação ou fluxos de trabalho de implantação
- **Ferramentas Personalizadas**: Construção de automação em torno do Foundry Local (integração CI/CD, orquestração de múltiplos agentes)
- **Acesso Detalhado**: Necessidade de metadados detalhados do agente, controle de versionamento ou do executor de avaliação
- **Integração com Python**: Trabalhando em ambientes com uso intensivo de Python ou incorporando lógica do Foundry em aplicações mais amplas
- **Fluxos de Trabalho Empresariais**: Implementação de fluxos de trabalho modulares e pipelines de avaliação reproduzíveis alinhados com arquiteturas de referência da Microsoft

### Use Comandos Shell Quando:

- **Testes Rápidos**: Realização de testes locais rápidos, lançamentos manuais de agentes ou verificação de configuração
- **Simplicidade CLI**: Necessidade de operações simples via CLI para iniciar/parar agentes, verificar logs ou realizar avaliações básicas
- **Automação Leve**: Criação de scripts de automação simples sem necessidade de integração completa com o SDK
- **Iteração Rápida**: Ciclos de depuração e desenvolvimento, especialmente em ambientes restritos ou implantações no nível de grupos de recursos
- **Configuração e Validação**: Configuração inicial do ambiente e tarefas rápidas de verificação

## Melhores Práticas e Fluxo de Trabalho Recomendado

Baseado em princípios de gerenciamento do ciclo de vida do agente, rastreamento de dependências e reprodutibilidade com privilégios mínimos:

### Fase 1: Fundação e Configuração
1. **Comece com Comandos Shell** para configuração inicial e validação rápida
2. **Verifique o Ambiente** usando ferramentas CLI e implantação básica de modelos
3. **Teste a Conectividade** com chamadas REST simples e verificações de saúde

### Fase 2: Desenvolvimento e Integração
1. **Transicione para o SDK** para fluxos de trabalho escaláveis e rastreáveis
2. **Implemente Controle Programático** para interações complexas entre agentes
3. **Construa Ferramentas Personalizadas** para templates prontos para a comunidade e integração com Azure OpenAI

### Fase 3: Produção e Escala
1. **Abordagem Híbrida** combinando CLI para operações e SDK para lógica de aplicação
2. **Integração Empresarial** com monitoramento, registro de logs e pipelines de implantação
3. **Contribuição Comunitária** através de templates reutilizáveis e melhores práticas

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.