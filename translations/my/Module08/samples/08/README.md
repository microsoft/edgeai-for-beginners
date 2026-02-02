# Windows 11 Chat Sample - Foundry Local

Windows 11 အတွက် Microsoft Foundry Local ကိုလှပသော native interface ဖြင့်ပေါင်းစပ်ထားသော chat application တစ်ခု။ Electron ဖြင့်တည်ဆောက်ပြီး Microsoft ရဲ့ Foundry Local ပုံစံများကိုလိုက်နာထားသည်။

## အကျဉ်းချုပ်

ဒီနမူနာက Foundry Local ကိုအသုံးပြုပြီး cloud မလိုအပ်တဲ့ privacy-focused AI စကားဝိုင်းများကိုပေးစွမ်းနိုင်သော production-ready chat application တစ်ခုကိုဘယ်လိုဖန်တီးရမလဲဆိုတာကိုပြသထားသည်။

## အင်္ဂါရပ်များ

### 🎨 **Windows 11 Native Design**
- Fluent Design System ပေါင်းစပ်မှု
- Mica material အကျိုးသက်ရောက်မှုနှင့် transparency
- Windows 11 theme ကို native ပုံစံဖြင့်ထောက်ပံ့မှု
- မည်သည့် screen size မဆို responsive layout
- Dark/Light mode ကိုအလိုအလျောက်ပြောင်းလဲမှု

### 🤖 **AI Model Integration**
- Foundry Local service ပေါင်းစပ်မှု
- မော်ဒယ်များစွာကို hot-swapping ဖြင့်ထောက်ပံ့မှု
- Real-time streaming အဖြေများ
- Local နှင့် cloud မော်ဒယ်များကိုပြောင်းလဲနိုင်မှု
- မော်ဒယ်၏ကျန်းမာရေးနှင့်အခြေအနေကိုစောင့်ကြည့်မှု

### 💬 **Chat Experience**
- Real-time typing indicators
- Message history ကိုသိမ်းဆည်းမှု
- Chat စကားဝိုင်းများကို export လုပ်နိုင်မှု
- Custom system prompts
- Conversation branching နှင့်စီမံခန့်ခွဲမှု

### ⚡ **Performance Features**
- Lazy loading နှင့် virtualization
- ရှည်လျားသောစကားဝိုင်းများအတွက် rendering ကို optimize လုပ်ထားမှု
- Background model preloading
- Memory ကိုထိရောက်စွာစီမံခန့်ခွဲမှု
- Smooth animations နှင့် transitions

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

## လိုအပ်ချက်များ

### System Requirements
- **OS**: Windows 11 (22H2 သို့မဟုတ်နောက်ဆုံး version အကြံပြုသည်)
- **RAM**: အနည်းဆုံး 8GB၊ 16GB+ ကိုကြီးမားသောမော်ဒယ်များအတွက်အကြံပြုသည်
- **Storage**: မော်ဒယ်များအတွက် 10GB+ အခမဲ့နေရာ
- **GPU**: Optional ဖြစ်သော်လည်းအမြန်ဆုံး inference အတွက်အကြံပြုသည်

### Software Dependencies
- **Node.js**: v18.0.0 သို့မဟုတ်နောက်ဆုံး version
- **Foundry Local**: Microsoft မှရရှိနိုင်သောနောက်ဆုံး version
- **Git**: Clone နှင့် development အတွက်

## Installation

### 1. Foundry Local ကို Install လုပ်ပါ
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clone နှင့် Setup
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Environment ကို Configure လုပ်ပါ
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Application ကို Run လုပ်ပါ
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

## အဓိက Features အကြောင်းအနက်ရှင်း

### Windows 11 Integration

**Fluent Design System**
- Mica background materials
- Acrylic transparency effects
- Rounded corners နှင့် modern spacing
- Native Windows 11 color palette
- Accessibility အတွက် semantic color tokens

**Native Windows Features**
- Jump list integration for recent chats
- Windows notifications for new messages
- Taskbar progress for model operations
- System tray integration with quick actions
- Windows Hello authentication support

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
- Token-by-token အဖြေပြသမှု
- Smooth typing animations
- Cancellable requests
- Typing indicators နှင့် status

**Conversation Management**
- Chat history ကိုသိမ်းဆည်းမှု
- Conversation export/import
- Message ရှာဖွေမှုနှင့် filtering
- Conversation branching
- Conversation တစ်ခုစီအတွက် custom system prompts

**Accessibility**
- Keyboard navigation အပြည့်အစုံ
- Screen reader compatibility
- High contrast mode ထောက်ပံ့မှု
- Font size customization
- Voice input integration

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

### Settings နှင့် Customization
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
- **Streaming**: Real-time responses ကို enable/disable
- **Context Length**: Conversation memory
- **Temperature**: Response creativity
- **Max Tokens**: Response length limits
- **System Prompts**: Default assistant behavior

### Model Settings
- **Auto-download**: မော်ဒယ်များကိုအလိုအလျောက် update
- **Cache Size**: Local model storage limits
- **Performance Mode**: CPU vs GPU preferences
- **Health Checks**: Monitoring intervals

## Development

### Source မှတည်ဆောက်ခြင်း
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
- Message virtualization ကိုထိရောက်စွာလုပ်ဆောင်မှု
- Automatic garbage collection
- Model memory monitoring
- Exit အချိန်တွင် resource cleanup

### Rendering Optimization
- Virtual scrolling for long conversations
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
- Cloud data transmission မရှိခြင်း (local mode)
- Encrypted conversation storage
- Secure credential management

### Application Security
- Sandboxed renderer processes
- Content Security Policy (CSP)
- Remote code execution မရှိခြင်း
- Secure IPC communication

## Troubleshooting

### Common Issues

**Foundry Local မစတင်နိုင်ခြင်း**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Model Loading Failures**
- Disk space လုံလောက်မှုကိုစစ်ဆေးပါ
- Downloads အတွက် internet connection ကိုစစ်ဆေးပါ
- GPU drivers ကို update လုပ်ပါ
- မော်ဒယ်အမျိုးအစားများကိုစမ်းသပ်ပါ

**Performance Issues**
- System resources ကိုစောင့်ကြည့်ပါ
- Model settings ကိုချိန်ညှိပါ
- Hardware acceleration ကို enable လုပ်ပါ
- အခြား resource-intensive applications ကိုပိတ်ပါ

### Debug Mode
Environment variables ကို set လုပ်ခြင်းဖြင့် debug logging ကို enable လုပ်ပါ:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contributing

### Development Setup
1. Repository ကို Fork လုပ်ပါ
2. Feature branch တစ်ခုဖန်တီးပါ
3. Dependencies install: `npm install`
4. Changes ပြုလုပ်ပြီးစမ်းသပ်ပါ
5. Pull request တင်ပါ

### Code Style
- ESLint configuration ထည့်သွင်းထားသည်
- Prettier ဖြင့် code formatting
- TypeScript ဖြင့် type safety
- JSDoc comments ဖြင့် documentation

## Learning Outcomes

ဒီနမူနာကိုပြီးမြောက်ပြီးနောက် သင်လေ့လာနိုင်မည့်အရာများ:

1. **Windows 11 Native Development**
   - Fluent Design System ကိုအကောင်အထည်ဖော်ခြင်း
   - Native Windows integration
   - Electron security အကောင်းဆုံးလေ့လာမှုများ

2. **AI Model Integration**
   - Foundry Local service architecture
   - Model lifecycle management
   - Performance monitoring နှင့် optimization

3. **Real-time Chat Systems**
   - Streaming response ကို handling
   - Conversation state management
   - User experience patterns

4. **Production Application Development**
   - Error handling နှင့် recovery
   - Performance optimization
   - Security considerations
   - Testing strategies

## Next Steps

- **Sample 09**: Multi-Agent Orchestration System
- **Sample 10**: Foundry Local as Tools Integration
- **Advanced Topics**: Custom model fine-tuning
- **Deployment**: Enterprise deployment patterns

## License

ဒီနမူနာသည် Microsoft Foundry Local project နှင့်တူညီသော license ကိုလိုက်နာသည်။

---

