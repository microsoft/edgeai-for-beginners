# Windows 11 Chat Sample - Foundry Local

Um aplicativo de chat moderno para Windows 11 que integra o Microsoft Foundry Local com uma interface nativa e elegante. Construído com Electron e seguindo os padrões oficiais do Foundry Local da Microsoft.

## Visão Geral

Este exemplo demonstra como criar um aplicativo de chat pronto para produção que utiliza modelos de IA locais através do Foundry Local, oferecendo aos usuários conversas com IA focadas em privacidade, sem dependências de nuvem.

## Funcionalidades

### 🎨 **Design Nativo do Windows 11**
- Integração com o Fluent Design System
- Efeitos de material Mica e transparência
- Suporte a temas nativos do Windows 11
- Layout responsivo para todos os tamanhos de tela
- Alternância automática entre modos claro/escuro

### 🤖 **Integração com Modelos de IA**
- Integração com o serviço Foundry Local
- Suporte a múltiplos modelos com troca dinâmica
- Respostas em tempo real via streaming
- Alternância entre modelos locais e na nuvem
- Monitoramento de saúde e status dos modelos

### 💬 **Experiência de Chat**
- Indicadores de digitação em tempo real
- Persistência do histórico de mensagens
- Exportação de conversas de chat
- Prompts personalizados do sistema
- Ramificação e gerenciamento de conversas

### ⚡ **Recursos de Desempenho**
- Carregamento sob demanda e virtualização
- Renderização otimizada para conversas longas
- Pré-carregamento de modelos em segundo plano
- Gerenciamento eficiente de memória
- Animações e transições suaves

## Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## Pré-requisitos

### Requisitos do Sistema
- **SO**: Windows 11 (22H2 ou posterior recomendado)
- **RAM**: Mínimo de 8GB, 16GB+ recomendado para modelos maiores
- **Armazenamento**: 10GB+ de espaço livre para modelos
- **GPU**: Opcional, mas recomendada para inferência mais rápida

### Dependências de Software
- **Node.js**: v18.0.0 ou posterior
- **Foundry Local**: Última versão da Microsoft
- **Git**: Para clonagem e desenvolvimento

## Instalação

### 1. Instalar o Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clonar e Configurar
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configurar Ambiente
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Executar o Aplicativo
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Estrutura do Projeto

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## Detalhamento das Funcionalidades

### Integração com Windows 11

**Fluent Design System**
- Materiais de fundo Mica
- Efeitos de transparência com Acrylic
- Cantos arredondados e espaçamento moderno
- Paleta de cores nativa do Windows 11
- Tokens de cores semânticas para acessibilidade

**Recursos Nativos do Windows**
- Integração com lista de atalhos para chats recentes
- Notificações do Windows para novas mensagens
- Progresso na barra de tarefas para operações de modelo
- Integração com a bandeja do sistema com ações rápidas
- Suporte à autenticação com Windows Hello

### Gerenciamento de Modelos de IA

**Modelos Locais**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Suporte Híbrido Nuvem/Local**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funcionalidades da Interface de Chat

**Streaming em Tempo Real**
- Exibição de respostas token por token
- Animações suaves de digitação
- Solicitações canceláveis
- Indicadores de digitação e status

**Gerenciamento de Conversas**
- Histórico de chat persistente
- Exportação/importação de conversas
- Busca e filtragem de mensagens
- Ramificação de conversas
- Prompts personalizados do sistema por conversa

**Acessibilidade**
- Navegação completa por teclado
- Compatibilidade com leitores de tela
- Suporte ao modo de alto contraste
- Tamanhos de fonte personalizáveis
- Integração com entrada por voz

## Exemplos de Uso

### Integração Básica de Chat
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Gerenciamento de Modelos
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Configurações e Personalização
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## Opções de Configuração

### Configurações do Aplicativo
- **Tema**: Automático, modo claro, modo escuro
- **Modelo**: Seleção de modelo padrão
- **Desempenho**: Configurações de inferência
- **Privacidade**: Políticas de retenção de dados
- **Notificações**: Alertas de mensagens
- **Atalhos**: Atalhos de teclado

### Configurações de Chat
- **Streaming**: Ativar/desativar respostas em tempo real
- **Comprimento do Contexto**: Memória da conversa
- **Temperatura**: Criatividade das respostas
- **Máximo de Tokens**: Limites de comprimento das respostas
- **Prompts do Sistema**: Comportamento padrão do assistente

### Configurações de Modelos
- **Auto-download**: Atualizações automáticas de modelos
- **Tamanho do Cache**: Limites de armazenamento de modelos locais
- **Modo de Desempenho**: Preferências de CPU vs GPU
- **Verificações de Saúde**: Intervalos de monitoramento

## Desenvolvimento

### Construção a partir do Código-Fonte
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Depuração
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testes
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Otimização de Desempenho

### Gerenciamento de Memória
- Virtualização eficiente de mensagens
- Coleta automática de lixo
- Monitoramento de memória de modelos
- Limpeza de recursos ao sair

### Otimização de Renderização
- Rolagem virtual para conversas longas
- Carregamento sob demanda do histórico de mensagens
- Atualizações otimizadas do React/DOM
- Animações aceleradas por GPU

### Otimização de Rede
- Pooling de conexões
- Agrupamento de solicitações
- Lógica de repetição automática
- Suporte ao modo offline

## Considerações de Segurança

### Privacidade de Dados
- Arquitetura local-primeiro
- Sem transmissão de dados na nuvem (modo local)
- Armazenamento de conversas criptografado
- Gerenciamento seguro de credenciais

### Segurança do Aplicativo
- Processos de renderização isolados
- Política de Segurança de Conteúdo (CSP)
- Sem execução de código remoto
- Comunicação IPC segura

## Solução de Problemas

### Problemas Comuns

**Foundry Local Não Inicia**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Falhas no Carregamento de Modelos**
- Verifique espaço suficiente em disco
- Cheque a conexão com a internet para downloads
- Certifique-se de que os drivers da GPU estão atualizados
- Experimente variantes diferentes de modelos

**Problemas de Desempenho**
- Monitore os recursos do sistema
- Ajuste as configurações do modelo
- Ative a aceleração de hardware
- Feche outros aplicativos que consomem muitos recursos

### Modo de Depuração
Ative o registro de depuração configurando variáveis de ambiente:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contribuindo

### Configuração de Desenvolvimento
1. Faça um fork do repositório
2. Crie um branch de funcionalidade
3. Instale as dependências: `npm install`
4. Faça alterações e teste
5. Envie um pull request

### Estilo de Código
- Configuração do ESLint fornecida
- Prettier para formatação de código
- TypeScript para segurança de tipos
- Comentários JSDoc para documentação

## Resultados de Aprendizado

Após concluir este exemplo, você entenderá:

1. **Desenvolvimento Nativo no Windows 11**
   - Implementação do Fluent Design System
   - Integração nativa com Windows
   - Melhores práticas de segurança com Electron

2. **Integração com Modelos de IA**
   - Arquitetura do serviço Foundry Local
   - Gerenciamento do ciclo de vida de modelos
   - Monitoramento e otimização de desempenho

3. **Sistemas de Chat em Tempo Real**
   - Manipulação de respostas em streaming
   - Gerenciamento de estado de conversas
   - Padrões de experiência do usuário

4. **Desenvolvimento de Aplicativos para Produção**
   - Tratamento de erros e recuperação
   - Otimização de desempenho
   - Considerações de segurança
   - Estratégias de teste

## Próximos Passos

- **Exemplo 09**: Sistema de Orquestração Multi-Agente
- **Exemplo 10**: Foundry Local como Integração de Ferramentas
- **Tópicos Avançados**: Ajuste fino de modelos personalizados
- **Implantação**: Padrões de implantação empresarial

## Licença

Este exemplo segue a mesma licença do projeto Microsoft Foundry Local.

---

