# Módulo 08 Exemplos: Guia de Desenvolvimento Local Foundry

## Visão Geral

Esta coleção abrangente demonstra as abordagens do **Foundry Local SDK** e dos **Comandos Shell** para construir aplicações de IA prontas para produção. Cada exemplo destaca diferentes aspetos do desenvolvimento de IA na periferia, desde a integração básica com REST até sistemas avançados de múltiplos agentes.

## Abordagem de Desenvolvimento: SDK vs Comandos Shell

### Utilize o Foundry Local SDK Quando:

- **Controlo Programático**: Necessita de controlo total sobre o ciclo de vida dos agentes, avaliação ou fluxos de trabalho de implementação
- **Ferramentas Personalizadas**: Construção de automação em torno do Foundry Local (integração CI/CD, orquestração de múltiplos agentes)
- **Acesso Detalhado**: Requer metadados detalhados dos agentes, controlo de versões ou do executor de avaliação
- **Integração com Python**: Trabalha em ambientes fortemente baseados em Python ou incorpora lógica do Foundry em aplicações mais amplas
- **Fluxos de Trabalho Empresariais**: Implementação de fluxos de trabalho modulares e pipelines de avaliação reprodutíveis alinhados com arquiteturas de referência da Microsoft

### Utilize Comandos Shell Quando:

- **Testes Rápidos**: Realiza testes locais rápidos, lançamentos manuais de agentes ou verificação de configuração
- **Simplicidade CLI**: Necessita de operações simples na linha de comandos para iniciar/parar agentes, verificar logs ou realizar avaliações básicas
- **Automação Leve**: Script de automação simples sem necessidade de integração completa com o SDK
- **Iteração Rápida**: Ciclos de depuração e desenvolvimento, especialmente em ambientes restritos ou implementações ao nível de grupos de recursos
- **Configuração e Validação**: Tarefas iniciais de configuração do ambiente e verificações rápidas

## Melhores Práticas e Fluxo de Trabalho Recomendado

Baseado na gestão do ciclo de vida dos agentes, rastreamento de dependências e princípios de reprodutibilidade com privilégios mínimos:

### Fase 1: Fundação e Configuração
1. **Comece com Comandos Shell** para configuração inicial e validação rápida
2. **Verifique o Ambiente** utilizando ferramentas CLI e implementações básicas de modelos
3. **Teste a Conectividade** com chamadas REST simples e verificações de saúde

### Fase 2: Desenvolvimento e Integração
1. **Transite para o SDK** para fluxos de trabalho escaláveis e rastreáveis
2. **Implemente Controlo Programático** para interações complexas entre agentes
3. **Construa Ferramentas Personalizadas** para templates prontos para a comunidade e integração com Azure OpenAI

### Fase 3: Produção e Escala
1. **Abordagem Híbrida** combinando CLI para operações e SDK para lógica de aplicação
2. **Integração Empresarial** com monitorização, registo e pipelines de implementação
3. **Contribuição Comunitária** através de templates reutilizáveis e melhores práticas

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.