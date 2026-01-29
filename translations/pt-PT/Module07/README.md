# Capítulo 07: Exemplos de EdgeAI

Edge AI representa a convergência da inteligência artificial com a computação na periferia, permitindo o processamento inteligente diretamente nos dispositivos sem depender da conectividade com a nuvem. Este capítulo explora cinco implementações distintas de EdgeAI em diferentes plataformas e frameworks, demonstrando a versatilidade e o poder de executar modelos de IA na periferia.

## 1. EdgeAI no NVIDIA Jetson Orin Nano

O NVIDIA Jetson Orin Nano representa um avanço na computação de IA na periferia acessível, oferecendo até 67 TOPS de desempenho de IA num formato compacto, do tamanho de um cartão de crédito. Esta poderosa plataforma de EdgeAI democratiza o desenvolvimento de IA generativa para entusiastas, estudantes e desenvolvedores profissionais.

### Principais Características
- Oferece até 67 TOPS de desempenho de IA — uma melhoria de 1,7X em relação ao seu antecessor
- 1024 núcleos CUDA e até 32 Tensor Cores para processamento de IA
- CPU Arm Cortex-A78AE v8.2 de 6 núcleos e 64 bits com frequência máxima de 1,5 GHz
- Preço de apenas $249, proporcionando aos desenvolvedores, estudantes e criadores a plataforma mais acessível e económica

### Aplicações
O Jetson Orin Nano destaca-se na execução de modelos modernos de IA generativa, incluindo transformadores de visão, grandes modelos de linguagem e modelos de visão-linguagem. Foi especificamente projetado para casos de uso de GenAI e agora é possível executar vários LLMs num dispositivo portátil. Casos de uso populares incluem robótica com IA, drones inteligentes, câmaras inteligentes e dispositivos autónomos na periferia.

**Saiba Mais**: [Supercomputador Jetson Orin Nano da NVIDIA: A Próxima Grande Inovação em EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI em Aplicações Móveis com .NET MAUI e ONNX Runtime GenAI

Esta solução demonstra como integrar IA Generativa e Grandes Modelos de Linguagem (LLMs) em aplicações móveis multiplataforma usando .NET MAUI (Multi-platform App UI) e ONNX Runtime GenAI. Esta abordagem permite que desenvolvedores .NET criem aplicações móveis sofisticadas com IA que funcionam nativamente em dispositivos Android e iOS.

### Principais Características
- Baseado no framework .NET MAUI, proporcionando um único código para aplicações Android e iOS
- Integração com ONNX Runtime GenAI permite executar modelos de IA generativa diretamente em dispositivos móveis
- Suporta vários aceleradores de hardware adaptados para dispositivos móveis, incluindo CPU, GPU e processadores de IA especializados
- Otimizações específicas da plataforma, como CoreML para iOS e NNAPI para Android através do ONNX Runtime
- Implementa o ciclo completo de IA generativa, incluindo pré e pós-processamento, inferência, processamento de logits, pesquisa e amostragem, e gestão de cache KV

### Benefícios de Desenvolvimento
A abordagem .NET MAUI permite que os desenvolvedores aproveitem as suas habilidades existentes em C# e .NET enquanto criam aplicações de IA multiplataforma. O framework ONNX Runtime GenAI suporta várias arquiteturas de modelos, incluindo Llama, Mistral, Phi, Gemma e muitos outros. Kernels ARM64 otimizados aceleram a multiplicação de matrizes quantizadas INT4, garantindo desempenho eficiente em hardware móvel enquanto mantêm a experiência familiar de desenvolvimento em .NET.

### Casos de Uso
Esta solução é ideal para desenvolvedores que desejam criar aplicações móveis com IA usando tecnologias .NET, incluindo chatbots inteligentes, aplicações de reconhecimento de imagem, ferramentas de tradução de idiomas e sistemas de recomendação personalizados que funcionam inteiramente no dispositivo para maior privacidade e capacidade offline.

**Saiba Mais**: [Exemplo de .NET MAUI ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI no Azure com Motor de Modelos de Linguagem Pequenos

A solução EdgeAI baseada no Azure da Microsoft foca-se na implementação eficiente de Modelos de Linguagem Pequenos (SLMs) em ambientes híbridos de nuvem e periferia. Esta abordagem preenche a lacuna entre serviços de IA em escala de nuvem e os requisitos de implementação na periferia.

### Vantagens da Arquitetura
- Integração perfeita com serviços de IA do Azure
- Executa SLMs/LLMs e modelos multimodais no dispositivo e na nuvem com ONNX Runtime
- Otimizado para implementação em escala empresarial
- Suporte para atualizações e gestão contínuas de modelos

### Casos de Uso
A implementação EdgeAI no Azure destaca-se em cenários que exigem implementação de IA em nível empresarial com capacidades de gestão na nuvem. Isso inclui processamento inteligente de documentos, análises em tempo real e fluxos de trabalho híbridos de IA que aproveitam recursos de computação na nuvem e na periferia.

**Saiba Mais**: [Motor de SLM do Azure EdgeAI](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI com Windows ML](./windowdeveloper.md)

O Windows ML representa o runtime de ponta da Microsoft otimizado para inferência de modelos no dispositivo e implementação simplificada, servindo como a base do Windows AI Foundry. Esta plataforma permite que os desenvolvedores criem aplicações Windows com IA que aproveitam todo o espectro de hardware de PC.

### Capacidades da Plataforma
- Funciona em todos os PCs com Windows 11 executando a versão 24H2 (build 26100) ou superior
- Funciona em todo o hardware de PC x64 e ARM64, mesmo em PCs que não possuem NPUs ou GPUs
- Permite que os desenvolvedores tragam os seus próprios modelos e os implementem eficientemente no ecossistema de parceiros de silício, incluindo AMD, Intel, NVIDIA e Qualcomm, abrangendo CPU, GPU, NPU
- Aproveitando APIs de infraestrutura, os desenvolvedores não precisam mais criar várias versões da sua aplicação para diferentes silícios

### Benefícios para Desenvolvedores
O Windows ML abstrai o hardware e os provedores de execução, permitindo que você se concentre em escrever o seu código. Além disso, o Windows ML atualiza-se automaticamente para suportar as últimas NPUs, GPUs e CPUs à medida que são lançadas. A plataforma oferece um framework unificado para desenvolvimento de IA em todo o ecossistema diversificado de hardware do Windows.

**Saiba Mais**: 
- [Visão Geral do Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Guia de Desenvolvimento de EdgeAI no Windows](./windowdeveloper.md) - Guia abrangente para desenvolvimento de Edge AI no Windows

## [5. EdgeAI com Aplicações Locais Foundry](./foundrylocal.md)

O Foundry Local permite que desenvolvedores de Windows e Mac criem aplicações de Geração Aumentada por Recuperação (RAG) usando recursos locais em .NET, combinando modelos de linguagem locais com capacidades de pesquisa semântica. Esta abordagem fornece soluções de IA focadas na privacidade que operam inteiramente em infraestrutura local.

### Arquitetura Técnica
- Combina o modelo de linguagem Phi, Embeddings Locais e Kernel Semântico para criar um cenário RAG
- Usa embeddings como vetores (arrays) de valores de ponto flutuante que representam conteúdo e seu significado semântico
- O Kernel Semântico atua como o principal orquestrador, integrando Phi e Componentes Inteligentes para criar um pipeline RAG contínuo
- Suporte para bases de dados vetoriais locais, incluindo SQLite e Qdrant

### Benefícios de Implementação
RAG, ou Geração Aumentada por Recuperação, é apenas uma forma sofisticada de dizer "procurar algumas informações e colocá-las no prompt". Esta implementação local garante privacidade de dados enquanto fornece respostas inteligentes baseadas em bases de conhecimento personalizadas. A abordagem é particularmente valiosa para cenários empresariais que exigem soberania de dados e capacidades de operação offline.

**Saiba Mais**: 
- [Foundry Local](./foundrylocal.md)
- [Exemplos de RAG do Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Foundry Local no Windows

O Microsoft Foundry Local fornece um servidor REST compatível com OpenAI, alimentado pelo ONNX Runtime, para executar modelos localmente no Windows. Abaixo está um resumo rápido e validado; consulte a documentação oficial para detalhes completos.

- Comece aqui: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arquitetura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referência CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Guia completo para Windows neste repositório: [foundrylocal.md](./foundrylocal.md)

Instale ou atualize no Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Explore categorias CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Execute um modelo e descubra o endpoint dinâmico:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Verificação rápida REST para listar modelos (substitua PORT pelo status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Dicas:
- Integração com SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Traga o seu próprio modelo (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Recursos de Desenvolvimento de EdgeAI no Windows

Para desenvolvedores que estão especificamente a direcionar a plataforma Windows, criámos um guia abrangente que cobre todo o ecossistema de EdgeAI no Windows. Este recurso fornece informações detalhadas sobre o Windows AI Foundry, incluindo APIs, ferramentas e melhores práticas para desenvolvimento de EdgeAI no Windows.

### Plataforma Windows AI Foundry
A plataforma Windows AI Foundry oferece um conjunto abrangente de ferramentas e APIs especificamente projetadas para desenvolvimento de Edge AI em dispositivos Windows. Isso inclui suporte especializado para hardware acelerado por NPU, integração com Windows ML e técnicas de otimização específicas da plataforma.

**Guia Abrangente**: [Guia de Desenvolvimento de EdgeAI no Windows](../windowdeveloper.md)

Este guia cobre:
- Visão geral e componentes da plataforma Windows AI Foundry
- API Phi Silica para inferência eficiente em hardware NPU
- APIs de Visão Computacional para processamento de imagem e OCR
- Integração e otimização do runtime Windows ML
- CLI do Foundry Local para desenvolvimento e testes locais
- Estratégias de otimização de hardware para dispositivos Windows
- Exemplos práticos de implementação e melhores práticas

### [Toolkit de IA para Desenvolvimento de Edge AI](./aitoolkit.md)
Para desenvolvedores que utilizam o Visual Studio Code, a extensão AI Toolkit fornece um ambiente de desenvolvimento abrangente especificamente projetado para criar, testar e implementar aplicações de Edge AI. Este toolkit simplifica todo o fluxo de trabalho de desenvolvimento de Edge AI dentro do VS Code.

**Guia de Desenvolvimento**: [Toolkit de IA para Desenvolvimento de Edge AI](./aitoolkit.md)

O guia do AI Toolkit cobre:
- Descoberta e seleção de modelos para implementação na periferia
- Fluxos de trabalho de teste e otimização local
- Integração com ONNX e Ollama para modelos na periferia
- Técnicas de conversão e quantização de modelos
- Desenvolvimento de agentes para cenários na periferia
- Avaliação de desempenho e monitorização
- Preparação para implementação e melhores práticas

## Conclusão

Estas cinco implementações de EdgeAI demonstram a maturidade e diversidade das soluções de IA na periferia disponíveis atualmente. Desde dispositivos acelerados por hardware como o Jetson Orin Nano até frameworks de software como ONNX Runtime GenAI e Windows ML, os desenvolvedores têm opções sem precedentes para implementar aplicações inteligentes na periferia.

O fio condutor entre todas estas plataformas é a democratização das capacidades de IA, tornando o aprendizado de máquina sofisticado acessível a desenvolvedores de diferentes níveis de habilidade e casos de uso. Seja a criar aplicações móveis, software de desktop ou sistemas embutidos, estas soluções de EdgeAI fornecem a base para a próxima geração de aplicações inteligentes que operam de forma eficiente e privada na periferia.

Cada plataforma oferece vantagens únicas: Jetson Orin Nano para computação acelerada por hardware na periferia, ONNX Runtime GenAI para desenvolvimento móvel multiplataforma, Azure EdgeAI para integração empresarial nuvem-periferia, Windows ML para aplicações nativas do Windows e Foundry Local para implementações RAG focadas na privacidade. Juntas, representam um ecossistema abrangente para desenvolvimento de EdgeAI.

[Próximo Toolkit de IA](aitoolkit.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.