<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13cb0371a2aea01d721186ced4a25e1a",
  "translation_date": "2025-11-11T18:00:11+00:00",
  "source_file": "Module08/samples/08/README.md",
  "language_code": "pcm"
}
-->
# Windows 11 Chat Sample - Foundry Local

Na modern chat app wey dem build for Windows 11 wey dey use Microsoft Foundry Local with fine native interface. Dem build am with Electron and e dey follow Microsoft official Foundry Local pattern.

## Overview

Dis sample dey show how you fit take create chat app wey ready for production, wey dey use local AI models through Foundry Local. E dey give users private AI conversations wey no need cloud.

## Features

### 🎨 **Windows 11 Native Design**
- Fluent Design System dey inside
- Mica material effects and transparency dey
- Native Windows 11 theme support dey
- E fit adjust for all screen sizes
- E go switch between Dark/Light mode automatic

### 🤖 **AI Model Integration**
- Foundry Local service dey inside
- E fit support plenty models and you fit change am anytime
- Real-time streaming responses dey
- E fit switch between local and cloud model
- E dey monitor model health and status

### 💬 **Chat Experience**
- Real-time typing indicators dey
- E dey save message history
- You fit export chat conversations
- Custom system prompts dey
- E fit manage and branch conversations

### ⚡ **Performance Features**
- Lazy loading and virtualization dey
- E dey render long conversations well
- Background model preloading dey
- E dey manage memory well
- Smooth animations and transitions dey

## Architecture

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

## Prerequisites

### System Requirements
- **OS**: Windows 11 (22H2 or later recommended)
- **RAM**: Minimum na 8GB, but 16GB+ dey better for bigger models
- **Storage**: You go need at least 10GB free space for models
- **GPU**: E no dey compulsory but e go make inference fast

### Software Dependencies
- **Node.js**: v18.0.0 or later
- **Foundry Local**: Latest version from Microsoft
- **Git**: To clone and develop

## Installation

### 1. Install Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clone and Setup
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configure Environment
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Run the Application
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Project Structure

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

## Key Features Deep Dive

### Windows 11 Integration

**Fluent Design System**
- Mica background materials dey
- Acrylic transparency effects dey
- Rounded corners and modern spacing dey
- Native Windows 11 color palette dey
- Semantic color tokens dey for accessibility

**Native Windows Features**
- Jump list dey for recent chats
- Windows notifications dey for new messages
- Taskbar progress dey for model operations
- System tray dey with quick actions
- Windows Hello authentication dey support

### AI Model Management

**Local Models**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybrid Cloud/Local Support**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chat Interface Features

**Real-time Streaming**
- E dey show response token by token
- Smooth typing animations dey
- You fit cancel requests
- Typing indicators and status dey

**Conversation Management**
- E dey save chat history
- You fit export/import conversations
- Message search and filtering dey
- E fit branch conversations
- Custom system prompts dey for each conversation

**Accessibility**
- Full keyboard navigation dey
- E dey work with screen reader
- High contrast mode dey support
- You fit change font sizes
- Voice input dey work

## Usage Examples

### Basic Chat Integration
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

### Model Management
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

### Settings and Customization
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

## Configuration Options

### Application Settings
- **Theme**: Auto, Light, Dark mode
- **Model**: Default model selection
- **Performance**: Inference settings
- **Privacy**: Data retention policies
- **Notifications**: Message alerts
- **Shortcuts**: Keyboard shortcuts

### Chat Settings
- **Streaming**: Enable/disable real-time responses
- **Context Length**: Conversation memory
- **Temperature**: Response creativity
- **Max Tokens**: Response length limits
- **System Prompts**: Default assistant behavior

### Model Settings
- **Auto-download**: Automatic model updates
- **Cache Size**: Local model storage limits
- **Performance Mode**: CPU vs GPU preferences
- **Health Checks**: Monitoring intervals

## Development

### Building from Source
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

### Debugging
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testing
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Performance Optimization

### Memory Management
- E dey virtualize messages well
- Automatic garbage collection dey
- E dey monitor model memory
- E dey clean resources when you close am

### Rendering Optimization
- Virtual scrolling dey for long conversations
- Lazy loading dey for message history
- E dey optimize React/DOM updates
- GPU-accelerated animations dey

### Network Optimization
- Connection pooling dey
- E dey batch requests
- Automatic retry logic dey
- Offline mode dey support

## Security Considerations

### Data Privacy
- E dey work local-first
- E no dey send data go cloud (local mode)
- E dey encrypt conversation storage
- E dey manage credentials well

### Application Security
- Renderer processes dey sandboxed
- Content Security Policy (CSP) dey
- E no dey allow remote code execution
- Secure IPC communication dey

## Troubleshooting

### Common Issues

**Foundry Local No Start**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Model Loading Failures**
- Check say you get enough disk space
- Make sure internet dey work for downloads
- Update GPU drivers
- Try different model variants

**Performance Issues**
- Monitor system resources
- Adjust model settings
- Enable hardware acceleration
- Close other apps wey dey use plenty resources

### Debug Mode
Enable debug logging by setting environment variables:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Install dependencies: `npm install`
4. Make changes and test
5. Submit a pull request

### Code Style
- ESLint configuration dey
- Prettier dey for code formatting
- TypeScript dey for type safety
- JSDoc comments dey for documentation

## Learning Outcomes

After you finish dis sample, you go sabi:

1. **Windows 11 Native Development**
   - How to use Fluent Design System
   - How to integrate native Windows features
   - Electron security best practices

2. **AI Model Integration**
   - Foundry Local service architecture
   - How to manage model lifecycle
   - How to monitor and optimize performance

3. **Real-time Chat Systems**
   - How to handle streaming responses
   - How to manage conversation state
   - User experience patterns

4. **Production Application Development**
   - How to handle errors and recover
   - How to optimize performance
   - Security considerations
   - Testing strategies

## Next Steps

- **Sample 09**: Multi-Agent Orchestration System
- **Sample 10**: Foundry Local as Tools Integration
- **Advanced Topics**: Custom model fine-tuning
- **Deployment**: Enterprise deployment patterns

## License

Dis sample dey follow the same license as Microsoft Foundry Local project.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go trust. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->