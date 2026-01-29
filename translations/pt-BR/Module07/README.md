# Capítulo 07: Exemplos de EdgeAI

Edge AI representa a convergência da inteligência artificial com a computação de borda, permitindo o processamento inteligente diretamente nos dispositivos sem depender da conectividade com a nuvem. Este capítulo explora cinco implementações distintas de EdgeAI em diferentes plataformas e frameworks, destacando a versatilidade e o poder de executar modelos de IA na borda.

## 1. EdgeAI no NVIDIA Jetson Orin Nano

O NVIDIA Jetson Orin Nano representa um avanço na computação de IA acessível na borda, oferecendo até 67 TOPS de desempenho de IA em um formato compacto do tamanho de um cartão de crédito. Esta poderosa plataforma de IA na borda democratiza o desenvolvimento de IA generativa para entusiastas, estudantes e desenvolvedores profissionais.

### Principais Características
- Oferece até 67 TOPS de desempenho de IA — uma melhoria de 1,7X em relação ao seu antecessor
- 1024 núcleos CUDA e até 32 núcleos Tensor para processamento de IA
- CPU Arm Cortex-A78AE v8.2 de 64 bits com 6 núcleos e frequência máxima de 1,5 GHz
- Preço de apenas $249, proporcionando aos desenvolvedores, estudantes e criadores a plataforma mais acessível e econômica

### Aplicações
O Jetson Orin Nano se destaca na execução de modelos modernos de IA generativa, incluindo transformadores de visão, grandes modelos de linguagem e modelos de visão-linguagem. Ele foi projetado especificamente para casos de uso de GenAI e agora é possível executar vários LLMs em um dispositivo portátil. Casos de uso populares incluem robótica com IA, drones inteligentes, câmeras inteligentes e dispositivos autônomos na borda.

**Saiba Mais**: [Supercomputador Jetson Orin Nano da NVIDIA: A Próxima Grande Revolução em EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI em Aplicativos Móveis com .NET MAUI e ONNX Runtime GenAI

Esta solução demonstra como integrar IA Generativa e Grandes Modelos de Linguagem (LLMs) em aplicativos móveis multiplataforma usando .NET MAUI (Multi-platform App UI) e ONNX Runtime GenAI. Essa abordagem permite que desenvolvedores .NET criem aplicativos móveis sofisticados com IA que funcionam nativamente em dispositivos Android e iOS.

### Principais Características
- Baseado no framework .NET MAUI, oferecendo um único código para aplicativos Android e iOS
- Integração com ONNX Runtime GenAI para executar modelos de IA generativa diretamente em dispositivos móveis
- Suporte a diversos aceleradores de hardware adaptados para dispositivos móveis, incluindo CPU, GPU e processadores de IA especializados
- Otimizações específicas para plataformas como CoreML para iOS e NNAPI para Android via ONNX Runtime
- Implementa o ciclo completo de IA generativa, incluindo pré e pós-processamento, inferência, processamento de logits, busca e amostragem, e gerenciamento de cache KV

### Benefícios para o Desenvolvimento
A abordagem .NET MAUI permite que os desenvolvedores aproveitem suas habilidades existentes em C# e .NET enquanto criam aplicativos de IA multiplataforma. O framework ONNX Runtime GenAI suporta várias arquiteturas de modelo, incluindo Llama, Mistral, Phi, Gemma e muitas outras. Kernels ARM64 otimizados aceleram a multiplicação de matrizes quantizadas em INT4, garantindo desempenho eficiente no hardware móvel enquanto mantém a experiência familiar de desenvolvimento em .NET.

### Casos de Uso
Esta solução é ideal para desenvolvedores que desejam criar aplicativos móveis com IA usando tecnologias .NET, incluindo chatbots inteligentes, aplicativos de reconhecimento de imagem, ferramentas de tradução de idiomas e sistemas de recomendação personalizados que funcionam totalmente no dispositivo para maior privacidade e capacidade offline.

**Saiba Mais**: [Exemplo de .NET MAUI ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI no Azure com Motor de Modelos de Linguagem Pequenos

A solução EdgeAI baseada no Azure da Microsoft foca na implantação eficiente de Modelos de Linguagem Pequenos (SLMs) em ambientes híbridos de nuvem e borda. Essa abordagem conecta os serviços de IA em escala de nuvem às necessidades de implantação na borda.

### Vantagens da Arquitetura
- Integração perfeita com os serviços de IA do Azure
- Executa SLMs/LLMs e modelos multimodais no dispositivo e na nuvem com ONNX Runtime
- Otimizado para implantação em escala empresarial
- Suporte para atualizações e gerenciamento contínuos de modelos

### Casos de Uso
A implementação de EdgeAI no Azure se destaca em cenários que exigem implantação de IA em nível empresarial com capacidades de gerenciamento na nuvem. Isso inclui processamento inteligente de documentos, análises em tempo real e fluxos de trabalho híbridos de IA que aproveitam recursos de computação na nuvem e na borda.

**Saiba Mais**: [Motor de SLM EdgeAI do Azure](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI com Windows ML](./windowdeveloper.md)

O Windows ML representa o runtime avançado da Microsoft otimizado para inferência de modelos no dispositivo e implantação simplificada, servindo como a base do Windows AI Foundry. Esta plataforma permite que os desenvolvedores criem aplicativos Windows com IA que aproveitam todo o espectro de hardware de PCs.

### Capacidades da Plataforma
- Funciona em todos os PCs com Windows 11 executando a versão 24H2 (build 26100) ou superior
- Compatível com hardware de PC x64 e ARM64, mesmo PCs sem NPUs ou GPUs
- Permite que os desenvolvedores tragam seus próprios modelos e os implantem eficientemente no ecossistema de parceiros de silício, incluindo AMD, Intel, NVIDIA e Qualcomm, abrangendo CPU, GPU, NPU
- Aproveitando APIs de infraestrutura, os desenvolvedores não precisam mais criar várias versões de seus aplicativos para diferentes silícios

### Benefícios para Desenvolvedores
O Windows ML abstrai o hardware e os provedores de execução, permitindo que você se concentre em escrever seu código. Além disso, o Windows ML é atualizado automaticamente para suportar as NPUs, GPUs e CPUs mais recentes à medida que são lançadas. A plataforma oferece um framework unificado para desenvolvimento de IA em todo o ecossistema diversificado de hardware do Windows.

**Saiba Mais**: 
- [Visão Geral do Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Guia de Desenvolvimento de EdgeAI no Windows](./windowdeveloper.md) - Guia abrangente para desenvolvimento de Edge AI no Windows

## [5. EdgeAI com Aplicativos Locais Foundry](./foundrylocal.md)

O Foundry Local permite que desenvolvedores de Windows e Mac criem aplicativos de Geração Aumentada por Recuperação (RAG) usando recursos locais em .NET, combinando modelos de linguagem locais com capacidades de busca semântica. Essa abordagem oferece soluções de IA focadas em privacidade que operam inteiramente em infraestrutura local.

### Arquitetura Técnica
- Combina o modelo de linguagem Phi, Embeddings Locais e Kernel Semântico para criar um cenário RAG
- Usa embeddings como vetores (arrays) de valores de ponto flutuante que representam conteúdo e seu significado semântico
- O Kernel Semântico atua como o principal orquestrador, integrando Phi e Componentes Inteligentes para criar um pipeline RAG contínuo
- Suporte para bancos de dados vetoriais locais, incluindo SQLite e Qdrant

### Benefícios da Implementação
RAG, ou Geração Aumentada por Recuperação, é apenas uma maneira sofisticada de dizer "pesquisar algumas informações e colocá-las no prompt". Esta implementação local garante privacidade de dados enquanto fornece respostas inteligentes baseadas em bases de conhecimento personalizadas. A abordagem é particularmente valiosa para cenários empresariais que exigem soberania de dados e capacidades de operação offline.

**Saiba Mais**: 
- [Foundry Local](./foundrylocal.md)
- [Exemplos de RAG Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Foundry Local no Windows

O Microsoft Foundry Local fornece um servidor REST compatível com OpenAI, alimentado pelo ONNX Runtime, para executar modelos localmente no Windows. Abaixo está um resumo rápido e validado; veja a documentação oficial para detalhes completos.

- Introdução: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
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
- Traga seu próprio modelo (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Recursos de Desenvolvimento de EdgeAI no Windows

Para desenvolvedores que estão especificamente direcionando a plataforma Windows, criamos um guia abrangente que cobre todo o ecossistema de EdgeAI no Windows. Este recurso fornece informações detalhadas sobre o Windows AI Foundry, incluindo APIs, ferramentas e melhores práticas para desenvolvimento de EdgeAI no Windows.

### Plataforma Windows AI Foundry
A plataforma Windows AI Foundry oferece um conjunto abrangente de ferramentas e APIs projetadas especificamente para desenvolvimento de IA na borda em dispositivos Windows. Isso inclui suporte especializado para hardware acelerado por NPU, integração com Windows ML e técnicas de otimização específicas para a plataforma.

**Guia Abrangente**: [Guia de Desenvolvimento de EdgeAI no Windows](../windowdeveloper.md)

Este guia cobre:
- Visão geral e componentes da plataforma Windows AI Foundry
- API Phi Silica para inferência eficiente em hardware NPU
- APIs de Visão Computacional para processamento de imagens e OCR
- Integração e otimização do runtime Windows ML
- CLI Foundry Local para desenvolvimento e testes locais
- Estratégias de otimização de hardware para dispositivos Windows
- Exemplos práticos de implementação e melhores práticas

### [Toolkit de IA para Desenvolvimento de Edge AI](./aitoolkit.md)
Para desenvolvedores que utilizam o Visual Studio Code, a extensão AI Toolkit oferece um ambiente de desenvolvimento abrangente projetado especificamente para construir, testar e implantar aplicativos de Edge AI. Este toolkit simplifica todo o fluxo de trabalho de desenvolvimento de Edge AI dentro do VS Code.

**Guia de Desenvolvimento**: [Toolkit de IA para Desenvolvimento de Edge AI](./aitoolkit.md)

O guia do AI Toolkit cobre:
- Descoberta e seleção de modelos para implantação na borda
- Fluxos de trabalho de teste e otimização locais
- Integração com ONNX e Ollama para modelos na borda
- Técnicas de conversão e quantização de modelos
- Desenvolvimento de agentes para cenários na borda
- Avaliação de desempenho e monitoramento
- Preparação para implantação e melhores práticas

## Conclusão

Essas cinco implementações de EdgeAI demonstram a maturidade e diversidade das soluções de IA na borda disponíveis atualmente. Desde dispositivos acelerados por hardware como o Jetson Orin Nano até frameworks de software como ONNX Runtime GenAI e Windows ML, os desenvolvedores têm opções sem precedentes para implantar aplicativos inteligentes na borda.

O fio condutor entre todas essas plataformas é a democratização das capacidades de IA, tornando o aprendizado de máquina sofisticado acessível a desenvolvedores de diferentes níveis de habilidade e casos de uso. Seja construindo aplicativos móveis, software de desktop ou sistemas embarcados, essas soluções de EdgeAI fornecem a base para a próxima geração de aplicativos inteligentes que operam de forma eficiente e privada na borda.

Cada plataforma oferece vantagens únicas: Jetson Orin Nano para computação acelerada por hardware na borda, ONNX Runtime GenAI para desenvolvimento móvel multiplataforma, Azure EdgeAI para integração nuvem-borda empresarial, Windows ML para aplicativos nativos do Windows e Foundry Local para implementações RAG focadas em privacidade. Juntas, elas representam um ecossistema abrangente para desenvolvimento de EdgeAI.

[Próximo Toolkit de IA](aitoolkit.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.