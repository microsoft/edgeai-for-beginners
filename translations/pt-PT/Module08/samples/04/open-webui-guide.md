# Guia de Integração Open WebUI + Foundry Local

Este guia mostra como conectar o Open WebUI ao Microsoft Foundry Local para criar uma interface profissional semelhante ao ChatGPT, alimentada pelos seus modelos de IA locais.

## Visão Geral

O Open WebUI oferece uma interface de chat moderna e fácil de usar que pode conectar-se a qualquer API compatível com OpenAI. Ao conectá-lo ao Foundry Local, obtém:

- **Interface Profissional**: Interface semelhante ao ChatGPT com design moderno
- **Privacidade Local**: Todo o processamento ocorre no seu dispositivo
- **Troca de Modelos**: Alteração fácil entre diferentes modelos locais
- **Histórico de Conversas**: Histórico de chat persistente e contexto
- **Carregamento de Ficheiros**: Análise de documentos e processamento de ficheiros
- **Personas Personalizadas**: Prompts de sistema e personalização de papéis

## Pré-requisitos

### Software Necessário

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Carregar um Modelo

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Configuração Rápida (Recomendada)

### Passo 1: Executar Open WebUI com Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Passo 2: Configuração Inicial

1. **Abrir Navegador**: Navegue para `http://localhost:3000`
2. **Criar Conta**: Configure o utilizador administrador (o primeiro utilizador torna-se administrador)
3. **Verificar Conexão**: Os modelos devem aparecer automaticamente no menu suspenso

### Passo 3: Testar a Conexão

1. Selecione o seu modelo no menu suspenso (ex.: "phi-4-mini")
2. Escreva uma mensagem de teste: "Olá! Podes apresentar-te?"
3. Deve ver uma resposta em streaming do seu modelo local

## Configuração Avançada

### Variáveis de Ambiente

| Variável | Finalidade | Padrão | Exemplo |
|----------|------------|--------|---------|
| `OPENAI_API_BASE_URL` | Endpoint do Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Chave API (necessária, mas não usada localmente) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Chave de encriptação de sessão | gerada automaticamente | `your-secret-key` |
| `ENABLE_SIGNUP` | Permitir registo de novos utilizadores | `True` | `False` |

### Configuração Manual (Alternativa)

Se as variáveis de ambiente não funcionarem, configure manualmente:

1. **Abrir Configurações**: Clique em Configurações (ícone de engrenagem)
2. **Ir para Conexões**: Configurações → Conexões → OpenAI
3. **Definir Detalhes da API**:
   - URL Base da API: `http://host.docker.internal:51211/v1`
   - Chave API: `foundry-local-key` (qualquer valor funciona)
4. **Guardar e Testar**: Clique em "Guardar" e teste com um modelo

### Armazenamento Persistente de Dados

Para persistir conversas e configurações:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Resolução de Problemas

### Problemas de Conexão

**Problema**: "Conexão recusada" ou modelos não carregam

**Soluções**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Modelo Não Aparece

**Problema**: Open WebUI não mostra modelos no menu suspenso

**Passos de Depuração**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Correção**: Certifique-se de que o modelo está devidamente carregado:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problemas de Rede com Docker

**Problema**: `host.docker.internal` não resolve

**Solução para Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Alternativa**: Encontre o IP da sua máquina:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problemas de Desempenho

**Respostas Lentas**:
1. Verifique se o modelo está a usar aceleração GPU: `foundry service ps`
2. Confirme recursos suficientes no sistema (RAM/memória GPU)
3. Considere usar um modelo menor para testes

**Problemas de Memória**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Guia de Utilização

### Chat Básico

1. **Selecionar Modelo**: Escolha no menu suspenso (mostra modelos do Foundry Local)
2. **Escrever Mensagem**: Use o campo de texto na parte inferior
3. **Enviar**: Pressione Enter ou clique no botão Enviar
4. **Ver Resposta**: Veja a resposta em streaming em tempo real

### Funcionalidades Avançadas

**Carregamento de Ficheiros**:
1. Clique no ícone de clipe de papel
2. Carregue o documento (PDF, TXT, etc.)
3. Faça perguntas sobre o conteúdo
4. O modelo analisará e responderá com base no documento

**Prompts de Sistema Personalizados**:
1. Configurações → Personalização
2. Defina um prompt de sistema personalizado
3. Cria uma personalidade/comportamento consistente da IA

**Gestão de Conversas**:
- **Novo Chat**: Clique em "+" para iniciar uma nova conversa
- **Histórico de Chat**: Acesse conversas anteriores na barra lateral
- **Exportar**: Faça download do histórico de chat como texto/JSON

**Comparação de Modelos**:
1. Abra várias abas do navegador com o mesmo Open WebUI
2. Selecione modelos diferentes em cada aba
3. Compare respostas para os mesmos prompts

### Padrões de Integração

**Fluxo de Trabalho de Desenvolvimento**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Implementação em Produção

### Configuração Segura

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Configuração Multiutilizador

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Monitorização e Registo

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Limpeza

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Próximos Passos

### Ideias de Melhoria

1. **Modelos Personalizados**: Adicione os seus próprios modelos ajustados ao Foundry Local
2. **Integração de API**: Conecte-se a APIs externas através das funções do Open WebUI
3. **Processamento de Documentos**: Configure pipelines avançados de RAG
4. **Multi-modalidade**: Configure modelos de visão para análise de imagens

### Considerações de Escalabilidade

- **Balanceamento de Carga**: Várias instâncias do Foundry Local atrás de um proxy reverso
- **Roteamento de Modelos**: Diferentes modelos para diferentes casos de uso
- **Gestão de Recursos**: Otimização de memória GPU para utilizadores simultâneos
- **Estratégia de Backup**: Backup regular dos dados de conversação e configurações

## Referências

- [Documentação do Open WebUI](https://docs.openwebui.com/)
- [Repositório GitHub do Open WebUI](https://github.com/open-webui/open-webui)
- [Documentação do Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Guia de Instalação do Docker](https://docs.docker.com/get-docker/)

---

