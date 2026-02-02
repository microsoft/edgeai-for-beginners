# Windows 11 Chat Sample - Foundry Local

A modern chat application for Windows 11 that integrates Microsoft Foundry Local with a sleek native interface. Built using Electron and adhering to Microsoft's official Foundry Local guidelines.

## Overview

This sample showcases how to build a production-ready chat application that utilizes local AI models through Foundry Local, offering users privacy-focused AI conversations without relying on cloud services.

## Features

### 🎨 **Windows 11 Native Design**
- Integration with the Fluent Design System
- Mica material effects and transparency
- Support for native Windows 11 themes
- Responsive design for all screen sizes
- Automatic switching between dark and light modes

### 🤖 **AI Model Integration**
- Integration with Foundry Local services
- Support for multiple models with dynamic switching
- Real-time streaming responses
- Ability to toggle between local and cloud models
- Monitoring and status updates for model health

### 💬 **Chat Experience**
- Real-time typing indicators
- Persistent message history
- Exportable chat conversations
- Customizable system prompts
- Conversation branching and management

### ⚡ **Performance Features**
- Lazy loading and virtualization
- Optimized rendering for lengthy conversations
- Background preloading of models
- Efficient memory usage
- Smooth animations and transitions

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
- **RAM**: Minimum 8GB, 16GB+ recommended for larger models
- **Storage**: At least 10GB free space for models
- **GPU**: Optional but recommended for faster processing

### Software Dependencies
- **Node.js**: Version 18.0.0 or later
- **Foundry Local**: Latest version from Microsoft
- **Git**: For cloning and development purposes

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
- Mica background materials
- Acrylic transparency effects
- Rounded corners and modern spacing
- Native Windows 11 color palette
- Semantic color tokens for accessibility

**Native Windows Features**
- Jump list integration for recent chats
- Windows notifications for new messages
- Taskbar progress indicators for model operations
- System tray integration with quick actions
- Support for Windows Hello authentication

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
- Token-by-token response display
- Smooth typing animations
- Ability to cancel requests
- Typing indicators and status updates

**Conversation Management**
- Persistent chat history
- Export and import conversations
- Message search and filtering
- Conversation branching
- Customizable system prompts for each conversation

**Accessibility**
- Full keyboard navigation
- Compatibility with screen readers
- Support for high contrast mode
- Adjustable font sizes
- Integration with voice input

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
- Efficient message virtualization
- Automatic garbage collection
- Model memory monitoring
- Resource cleanup upon exit

### Rendering Optimization
- Virtual scrolling for lengthy conversations
- Lazy loading of message history
- Optimized React/DOM updates
- GPU-accelerated animations

### Network Optimization
- Connection pooling
- Request batching
- Automatic retry logic
- Offline mode support

## Security Considerations

### Data Privacy
- Local-first architecture
- No cloud data transmission (local mode)
- Encrypted conversation storage
- Secure credential management

### Application Security
- Sandboxed renderer processes
- Content Security Policy (CSP)
- No remote code execution
- Secure IPC communication

## Troubleshooting

### Common Issues

**Foundry Local Not Starting**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Model Loading Failures**
- Ensure sufficient disk space
- Verify internet connection for downloads
- Update GPU drivers
- Try alternative model variants

**Performance Issues**
- Monitor system resources
- Adjust model settings
- Enable hardware acceleration
- Close other resource-intensive applications

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
- ESLint configuration provided
- Prettier for code formatting
- TypeScript for type safety
- JSDoc comments for documentation

## Learning Outcomes

After completing this sample, you will understand:

1. **Windows 11 Native Development**
   - Implementation of the Fluent Design System
   - Integration with native Windows features
   - Best practices for Electron security

2. **AI Model Integration**
   - Architecture of Foundry Local services
   - Managing model lifecycles
   - Performance monitoring and optimization

3. **Real-time Chat Systems**
   - Handling streaming responses
   - Managing conversation states
   - Designing user-friendly experiences

4. **Production Application Development**
   - Error handling and recovery
   - Performance optimization techniques
   - Security considerations
   - Testing strategies

## Next Steps

- **Sample 09**: Multi-Agent Orchestration System
- **Sample 10**: Foundry Local as Tools Integration
- **Advanced Topics**: Custom model fine-tuning
- **Deployment**: Enterprise deployment strategies

## License

This sample adheres to the same license as the Microsoft Foundry Local project.

---

