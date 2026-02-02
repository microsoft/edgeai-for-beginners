# AGENTS.md

> **Guia do Desenvolvedor para Contribuir com EdgeAI para Iniciantes**
> 
> Este documento fornece informações abrangentes para desenvolvedores, agentes de IA e colaboradores que trabalham com este repositório. Ele cobre configuração, fluxos de trabalho de desenvolvimento, testes e melhores práticas.
> 
> **Última Atualização**: 30 de outubro de 2025 | **Versão do Documento**: 3.0

## Índice

- [Visão Geral do Projeto](../..)
- [Estrutura do Repositório](../..)
- [Pré-requisitos](../..)
- [Comandos de Configuração](../..)
- [Fluxo de Trabalho de Desenvolvimento](../..)
- [Instruções de Teste](../..)
- [Diretrizes de Estilo de Código](../..)
- [Diretrizes para Pull Requests](../..)
- [Sistema de Tradução](../..)
- [Integração com Foundry Local](../..)
- [Build e Implantação](../..)
- [Problemas Comuns e Soluções](../..)
- [Recursos Adicionais](../..)
- [Notas Específicas do Projeto](../..)
- [Obtendo Ajuda](../..)

## Visão Geral do Projeto

EdgeAI para Iniciantes é um repositório educacional abrangente que ensina desenvolvimento de IA de Borda com Modelos de Linguagem Pequenos (SLMs). O curso aborda fundamentos de EdgeAI, implantação de modelos, técnicas de otimização e implementações prontas para produção usando Microsoft Foundry Local e vários frameworks de IA.

**Principais Tecnologias:**
- Python 3.8+ (linguagem principal para exemplos de IA/ML)
- .NET C# (exemplos de IA/ML)
- JavaScript/Node.js com Electron (para aplicativos desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Frameworks de IA: LangChain, Semantic Kernel, Chainlit
- Otimização de Modelos: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipo de Repositório:** Repositório de conteúdo educacional com 8 módulos e 10 aplicativos de exemplo abrangentes

**Arquitetura:** Caminho de aprendizado multi-módulo com exemplos práticos demonstrando padrões de implantação de IA de borda

## Estrutura do Repositório

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Pré-requisitos

### Ferramentas Necessárias

- **Python 3.8+** - Para exemplos e notebooks de IA/ML
- **Node.js 16+** - Para o aplicativo de exemplo Electron
- **Git** - Para controle de versão
- **Microsoft Foundry Local** - Para executar modelos de IA localmente

### Ferramentas Recomendadas

- **Visual Studio Code** - Com extensões Python, Jupyter e Pylance
- **Windows Terminal** - Para uma melhor experiência de linha de comando (usuários Windows)
- **Docker** - Para desenvolvimento em contêiner (opcional)

### Requisitos do Sistema

- **RAM**: Mínimo de 8GB, 16GB+ recomendado para cenários multi-modelo
- **Armazenamento**: 10GB+ de espaço livre para modelos e dependências
- **SO**: Windows 10/11, macOS 11+ ou Linux (Ubuntu 20.04+)
- **Hardware**: CPU com suporte AVX2; GPU (CUDA, Qualcomm NPU) opcional, mas recomendada

### Conhecimentos Necessários

- Compreensão básica de programação em Python
- Familiaridade com interfaces de linha de comando
- Entendimento de conceitos de IA/ML (para desenvolvimento de exemplos)
- Fluxos de trabalho com Git e processos de pull request

## Comandos de Configuração

### Configuração do Repositório

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configuração de Exemplos em Python (Módulo08 e exemplos do Workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Configuração de Exemplos em Node.js (Exemplo 08 - Aplicativo de Chat para Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Configuração do Foundry Local

O Foundry Local é necessário para executar os exemplos. Baixe e instale do repositório oficial:

**Instalação:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Baixe da [página de releases](https://github.com/microsoft/Foundry-Local/releases)

**Início Rápido:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Nota**: O Foundry Local seleciona automaticamente a melhor variante de modelo para o seu hardware (GPU CUDA, NPU Qualcomm ou CPU).

## Fluxo de Trabalho de Desenvolvimento

### Desenvolvimento de Conteúdo

Este repositório contém principalmente **conteúdo educacional em Markdown**. Ao fazer alterações:

1. Edite os arquivos `.md` nos diretórios de módulos apropriados
2. Siga os padrões de formatação existentes
3. Certifique-se de que os exemplos de código sejam precisos e testados
4. Atualize o conteúdo traduzido correspondente, se necessário (ou deixe a automação cuidar disso)

### Desenvolvimento de Aplicativos de Exemplo

Para exemplos em Python do Módulo08 (exemplos 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Para exemplos em Python do Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Para o exemplo Electron (exemplo 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testando Aplicativos de Exemplo

Os exemplos em Python não possuem testes automatizados, mas podem ser validados executando-os:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

O exemplo Electron possui infraestrutura de testes:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instruções de Teste

### Validação de Conteúdo

O repositório utiliza fluxos de trabalho de tradução automatizados. Não é necessário teste manual para traduções.

**Validação manual para alterações de conteúdo:**
1. Revise a renderização do Markdown visualizando os arquivos `.md`
2. Verifique se todos os links apontam para destinos válidos
3. Teste quaisquer trechos de código incluídos na documentação
4. Verifique se as imagens carregam corretamente

### Teste de Aplicativos de Exemplo

**O exemplo Module08/samples/08 (aplicativo Electron) possui testes abrangentes:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Os exemplos em Python devem ser testados manualmente:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Diretrizes de Estilo de Código

### Conteúdo em Markdown

- Use hierarquia consistente de cabeçalhos (# para título, ## para seções principais, ### para subseções)
- Inclua blocos de código com especificadores de linguagem: ```python, ```bash, ```javascript
- Siga a formatação existente para tabelas, listas e ênfases
- Mantenha as linhas legíveis (aproximadamente 80-100 caracteres, mas não estritamente)
- Use links relativos para referências internas

### Estilo de Código em Python

- Siga as convenções do PEP 8
- Use dicas de tipo quando apropriado
- Inclua docstrings para funções e classes
- Use nomes de variáveis significativos
- Mantenha as funções focadas e concisas

### Estilo de Código em JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Principais convenções:**
- Configuração do ESLint fornecida no exemplo 08
- Prettier para formatação de código
- Use sintaxe moderna ES6+
- Siga os padrões existentes no código-base

## Diretrizes para Pull Requests

### Fluxo de Contribuição

1. **Faça um fork do repositório** e crie um novo branch a partir de `main`
2. **Faça suas alterações** seguindo as diretrizes de estilo de código
3. **Teste completamente** usando as instruções de teste acima
4. **Faça commits com mensagens claras** seguindo o formato de commits convencionais
5. **Envie para o seu fork** e crie um pull request
6. **Responda ao feedback** dos mantenedores durante a revisão

### Convenção de Nomes de Branch

- `feature/<modulo>-<descricao>` - Para novos recursos ou conteúdo
- `fix/<modulo>-<descricao>` - Para correções de bugs
- `docs/<descricao>` - Para melhorias na documentação
- `refactor/<descricao>` - Para refatoração de código

### Formato de Mensagem de Commit

Siga [Commits Convencionais](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Exemplos:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formato de Título
```
[ModuleXX] Brief description of change
```
ou
```
[Module08/samples/XX] Description for sample changes
```

### Código de Conduta

Todos os colaboradores devem seguir o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/). Por favor, revise o [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) antes de contribuir.

### Antes de Enviar

**Para alterações de conteúdo:**
- Visualize todos os arquivos Markdown modificados
- Verifique se os links e imagens funcionam
- Verifique erros de digitação e gramaticais

**Para alterações no código de exemplo (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Para alterações nos exemplos em Python:**
- Teste se o exemplo é executado com sucesso
- Verifique se o tratamento de erros funciona
- Verifique a compatibilidade com o Foundry Local

### Processo de Revisão

- Alterações no conteúdo educacional são revisadas quanto à precisão e clareza
- Exemplos de código são testados quanto à funcionalidade
- Atualizações de tradução são tratadas automaticamente pelo GitHub Actions

## Sistema de Tradução

**IMPORTANTE:** Este repositório utiliza tradução automatizada via GitHub Actions.

- As traduções estão no diretório `/translations/` (50+ idiomas)
- Automatizado via workflow `co-op-translator.yml`
- **NÃO edite manualmente os arquivos de tradução** - eles serão sobrescritos
- Edite apenas os arquivos de origem em inglês nos diretórios raiz e de módulos
- As traduções são geradas automaticamente ao fazer push no branch `main`

## Integração com Foundry Local

A maioria dos exemplos do Módulo08 requer que o Microsoft Foundry Local esteja em execução.

### Instalação e Configuração

**Instale o Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instale o SDK do Python:**
```bash
pip install foundry-local-sdk openai
```

### Iniciando o Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Uso do SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verificando o Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variáveis de Ambiente para Exemplos

A maioria dos exemplos usa estas variáveis de ambiente:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Nota**: Ao usar `FoundryLocalManager`, o SDK lida automaticamente com a descoberta de serviços e carregamento de modelos. Apelidos de modelos (como `phi-3.5-mini`) garantem que a melhor variante seja selecionada para o seu hardware.

## Build e Implantação

### Implantação de Conteúdo

Este repositório é principalmente de documentação - nenhum processo de build é necessário para o conteúdo.

### Build de Aplicativos de Exemplo

**Aplicativo Electron (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Exemplos em Python:**
Sem processo de build - os exemplos são executados diretamente com o interpretador Python.

## Problemas Comuns e Soluções

> **Dica**: Verifique [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) para problemas conhecidos e soluções.

### Problemas Críticos (Bloqueantes)

#### Foundry Local Não Está Executando
**Problema:** Exemplos falham com erros de conexão

**Solução:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Problemas Comuns (Moderados)

#### Problemas com Ambiente Virtual Python
**Problema:** Erros de importação de módulos

**Solução:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemas de Build no Electron
**Problema:** Falhas no npm install ou build

**Solução:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemas de Fluxo de Trabalho (Menores)

#### Conflitos no Workflow de Tradução
**Problema:** PR de tradução entra em conflito com suas alterações

**Solução:**
- Edite apenas os arquivos de origem em inglês
- Deixe o workflow de tradução automatizado cuidar das traduções
- Se ocorrerem conflitos, faça merge do `main` no seu branch após as traduções serem mescladas

#### Falhas no Download de Modelos
**Problema:** Foundry Local falha ao baixar modelos

**Solução:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Recursos Adicionais

### Caminhos de Aprendizado
- **Caminho para Iniciantes:** Módulos 01-02 (7-9 horas)
- **Caminho Intermediário:** Módulos 03-04 (9-11 horas)
- **Caminho Avançado:** Módulos 05-07 (12-15 horas)
- **Caminho para Especialistas:** Módulo 08 (8-10 horas)
- **Workshop Prático:** Materiais do Workshop (6-8 horas)

### Conteúdo Principal dos Módulos
- **Módulo01:** Fundamentos de EdgeAI e estudos de caso do mundo real
- **Módulo02:** Famílias e arquiteturas de Modelos de Linguagem Pequenos (SLM)
- **Módulo03:** Estratégias de implantação local e na nuvem
- **Módulo04:** Otimização de modelos com múltiplos frameworks (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Módulo05:** SLMOps - operações em produção
- **Módulo06:** Agentes de IA e chamadas de função
- **Módulo07:** Implementações específicas de plataforma
- **Módulo08:** Ferramentas do Foundry Local com 10 exemplos abrangentes

### Dependências Externas
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime local de modelos de IA com API compatível com OpenAI
  - [Documentação](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [SDK Python](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [SDK JavaScript](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework de otimização
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Ferramenta de otimização de modelos
- [OpenVINO](https://docs.openvino.ai/) - Ferramenta de otimização da Intel

## Notas Específicas do Projeto

### Aplicativos de Exemplo do Módulo08

O repositório inclui 10 aplicativos de exemplo abrangentes:

1. **01-REST Chat Quickstart** - Integração básica com OpenAI SDK
2. **02-OpenAI SDK Integration** - Recursos avançados do SDK
3. **03-Model Discovery & Benchmarking** - Ferramentas de comparação de modelos
4. **04-Chainlit RAG Application** - Geração aumentada por recuperação
5. **05-Multi-Agent Orchestration** - Coordenação básica de agentes
6. **06-Models-as-Tools Router** - Roteamento inteligente de modelos
7. **07-Direct API Client** - Integração de API de baixo nível
8. **08-Windows 11 Chat App** - Aplicativo desktop nativo Electron
9. **09-Advanced Multi-Agent System** - Orquestração complexa de agentes
10. **10-Framework de Ferramentas Foundry** - Integração LangChain/Semantic Kernel

### Aplicações de Exemplo do Workshop

O Workshop inclui 6 sessões progressivas com implementações práticas:

1. **Sessão 01** - Inicialização do chat com integração Foundry Local
2. **Sessão 02** - Pipeline RAG e avaliação com RAGAS
3. **Sessão 03** - Benchmarking de modelos open-source
4. **Sessão 04** - Comparação e seleção de modelos
5. **Sessão 05** - Sistemas de orquestração multi-agente
6. **Sessão 06** - Roteamento de modelos e gerenciamento de pipelines

Cada exemplo demonstra diferentes aspectos do desenvolvimento de IA de borda com Foundry Local.

### Considerações de Desempenho

- SLMs são otimizados para implantação em borda (2-16GB RAM)
- Inferência local oferece tempos de resposta de 50-500ms
- Técnicas de quantização alcançam redução de tamanho de 75% com retenção de desempenho de 85%
- Capacidades de conversação em tempo real com modelos locais

### Segurança e Privacidade

- Todo o processamento ocorre localmente - nenhum dado é enviado para a nuvem
- Adequado para aplicações sensíveis à privacidade (saúde, finanças)
- Atende aos requisitos de soberania de dados
- Foundry Local opera inteiramente em hardware local

## Obtendo Ajuda

### Documentação

- **README Principal**: [README.md](README.md) - Visão geral do repositório e caminhos de aprendizado
- **Guia de Estudo**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Recursos de aprendizado e cronograma
- **Suporte**: [SUPPORT.md](SUPPORT.md) - Como obter ajuda
- **Segurança**: [SECURITY.md](SECURITY.md) - Relatar problemas de segurança

### Suporte da Comunidade

- **Issues no GitHub**: [Relatar bugs ou solicitar recursos](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Discussões no GitHub**: [Fazer perguntas e compartilhar ideias](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Issues do Foundry Local**: [Problemas técnicos com Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contato

- **Mantenedores**: Veja [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Problemas de Segurança**: Siga a divulgação responsável em [SECURITY.md](SECURITY.md)
- **Suporte Microsoft**: Para suporte empresarial, entre em contato com o serviço de atendimento ao cliente da Microsoft

### Recursos Adicionais

- **Microsoft Learn**: [Caminhos de Aprendizado de IA e Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Documentação do Foundry Local**: [Documentação Oficial](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Exemplos da Comunidade**: Confira [Discussões no GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) para contribuições da comunidade

---

**Este é um repositório educacional focado em ensinar o desenvolvimento de IA de borda. O padrão principal de contribuição é melhorar o conteúdo educacional e adicionar/aperfeiçoar aplicações de exemplo que demonstrem conceitos de IA de borda.**

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.