# Exemplo 04: Aplicações de Chat em Produção com Chainlit

Um exemplo abrangente que demonstra várias abordagens para construir aplicações de chat prontas para produção utilizando o Microsoft Foundry Local, com interfaces web modernas, respostas em streaming e tecnologias avançadas de navegador.

## O que está incluído

- **🚀 Aplicação de Chat Chainlit** (`app.py`): Aplicação de chat pronta para produção com streaming
- **🌐 Demonstração WebGPU** (`webgpu-demo/`): Inferência de IA baseada no navegador com aceleração de hardware
- **🎨 Integração Open WebUI** (`open-webui-guide.md`): Interface profissional semelhante ao ChatGPT
- **📚 Notebook Educacional** (`chainlit_app.ipynb`): Materiais interativos de aprendizagem

## Início Rápido

### 1. Aplicação de Chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Abre em: `http://localhost:8080`

### 2. Demonstração WebGPU no Navegador

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Abre em: `http://localhost:5173`

### 3. Configuração Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Abre em: `http://localhost:3000`

## Padrões de Arquitetura

### Matriz de Decisão Local vs Nuvem

| Cenário | Recomendação | Motivo |
|---------|--------------|--------|
| **Dados Sensíveis à Privacidade** | 🏠 Local (Foundry) | Os dados nunca saem do dispositivo |
| **Raciocínio Complexo** | ☁️ Nuvem (Azure OpenAI) | Acesso a modelos maiores |
| **Chat em Tempo Real** | 🏠 Local (Foundry) | Menor latência, respostas mais rápidas |
| **Análise de Documentos** | 🔄 Híbrido | Local para extração, nuvem para análise |
| **Geração de Código** | 🏠 Local (Foundry) | Privacidade + modelos especializados |
| **Tarefas de Pesquisa** | ☁️ Nuvem (Azure OpenAI) | Necessidade de uma base de conhecimento ampla |

### Comparação de Tecnologias

| Tecnologia | Caso de Uso | Vantagens | Desvantagens |
|------------|-------------|-----------|--------------|
| **Chainlit** | Desenvolvedores Python, prototipagem rápida | Configuração fácil, suporte a streaming | Apenas Python |
| **WebGPU** | Máxima privacidade, cenários offline | Nativo do navegador, sem necessidade de servidor | Tamanho limitado de modelo |
| **Open WebUI** | Implementação em produção, equipas | UI profissional, gestão de utilizadores | Requer Docker |

## Pré-requisitos

- **Foundry Local**: Instalado e em execução ([Download](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ com ambiente virtual
- **Modelo**: Pelo menos um carregado (`foundry model run phi-4-mini`)
- **Navegador**: Chrome/Edge com suporte a WebGPU para demonstrações
- **Docker**: Para Open WebUI (opcional)

## Instalação e Configuração

### 1. Configuração do Ambiente Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuração do Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Aplicações de Exemplo

### Aplicação de Chat Chainlit

**Funcionalidades:**
- 🚀 **Streaming em Tempo Real**: Os tokens aparecem à medida que são gerados
- 🛡️ **Gestão Robusta de Erros**: Degradação e recuperação graciosas
- 🎨 **UI Moderna**: Interface de chat profissional pronta para uso
- 🔧 **Configuração Flexível**: Variáveis de ambiente e deteção automática
- 📱 **Design Responsivo**: Funciona em dispositivos desktop e móveis

**Início Rápido:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Demonstração WebGPU no Navegador

**Funcionalidades:**
- 🌐 **IA Nativa do Navegador**: Sem necessidade de servidor, executa inteiramente no navegador
- ⚡ **Aceleração WebGPU**: Aceleração de hardware quando disponível
- 🔒 **Máxima Privacidade**: Nenhum dado sai do seu dispositivo
- 🎯 **Instalação Zero**: Funciona em qualquer navegador compatível
- 🔄 **Fallback Gracioso**: Reverte para CPU se WebGPU não estiver disponível

**Execução:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integração Open WebUI

**Funcionalidades:**
- 🎨 **Interface Semelhante ao ChatGPT**: UI profissional e familiar
- 👥 **Suporte Multi-utilizador**: Contas de utilizadores e histórico de conversas
- 📁 **Processamento de Ficheiros**: Carregar e analisar documentos
- 🔄 **Alternância de Modelos**: Alternância fácil entre diferentes modelos
- 🐳 **Implementação com Docker**: Configuração pronta para produção em contêineres

**Configuração Rápida:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referência de Configuração

### Variáveis de Ambiente

| Variável | Descrição | Padrão | Exemplo |
|----------|-----------|--------|---------|
| `MODEL` | Alias do modelo a usar | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint do Foundry Local | Deteção automática | `http://localhost:51211` |
| `API_KEY` | Chave API (opcional para local) | `""` | `your-api-key` |

## Resolução de Problemas

### Problemas Comuns

**Aplicação Chainlit:**

1. **Serviço não disponível:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Conflitos de porta:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problemas no ambiente Python:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Demonstração WebGPU:**

1. **WebGPU não suportado:**
   - Atualize para Chrome/Edge 113+
   - Ative WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Verifique o estado da GPU: `chrome://gpu`
   - A demonstração reverterá automaticamente para CPU

2. **Erros ao carregar o modelo:**
   - Certifique-se de que tem conexão à internet para download do modelo
   - Verifique o console do navegador para erros de CORS
   - Confirme que está a servir via HTTP (não file://)

**Open WebUI:**

1. **Conexão recusada:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modelos não aparecem:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Lista de Verificação de Validação

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Uso Avançado

### Otimização de Desempenho

**Chainlit:**
- Use streaming para melhor desempenho percebido
- Implemente pooling de conexões para alta concorrência
- Cache de respostas de modelos para consultas repetidas
- Monitore o uso de memória com históricos de conversas grandes

**WebGPU:**
- Use WebGPU para máxima privacidade e velocidade
- Implemente quantização de modelos para modelos menores
- Use Web Workers para processamento em segundo plano
- Cache de modelos compilados no armazenamento do navegador

**Open WebUI:**
- Use volumes persistentes para histórico de conversas
- Configure limites de recursos para o contêiner Docker
- Implemente estratégias de backup para dados de utilizadores
- Configure proxy reverso para terminação SSL

### Padrões de Integração

**Híbrido Local/Nuvem:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Pipeline Multi-modal:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Implementação em Produção

### Considerações de Segurança

- **Chaves API**: Use variáveis de ambiente, nunca codifique diretamente
- **Rede**: Use HTTPS em produção, considere VPN para acesso da equipa
- **Controlo de Acesso**: Implemente autenticação para Open WebUI
- **Privacidade de Dados**: Audite quais dados permanecem locais vs. vão para a nuvem
- **Atualizações**: Mantenha Foundry Local e contêineres atualizados

### Monitorização e Manutenção

- **Verificações de Saúde**: Implemente monitorização de endpoints
- **Registos**: Centralize os registos de todos os componentes
- **Métricas**: Acompanhe tempos de resposta, taxas de erro, uso de recursos
- **Backup**: Backup regular dos dados de conversação e configurações

## Referências e Recursos

### Documentação
- [Documentação Chainlit](https://docs.chainlit.io/) - Guia completo do framework
- [Documentação Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Documentação oficial da Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integração WebGPU
- [Documentação Open WebUI](https://docs.openwebui.com/) - Configuração avançada

### Ficheiros de Exemplo
- [`app.py`](../../../../../Module08/samples/04/app.py) - Aplicação Chainlit de produção
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook educacional
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inferência de IA baseada no navegador
- [`open-webui-guide.md`](./open-webui-guide.md) - Configuração completa do Open WebUI

### Exemplos Relacionados
- [Documentação da Sessão 4](../../04.CuttingEdgeModels.md) - Guia completo da sessão
- [Exemplos Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Exemplos oficiais

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.