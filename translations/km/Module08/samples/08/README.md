# Windows 11 Chat Sample - Foundry Local

កម្មវិធីជជែកទំនើបសម្រាប់ Windows 11 ដែលបញ្ចូល Foundry Local របស់ Microsoft ជាមួយចំណងជើងអ្នកប្រើប្រាស់ដើមដ៏ស្អាត។ បានបង្កើតជាមួយ Electron និងអនុវត្តតាមគម្លាត Foundry Local ផ្លូវការរបស់ Microsoft។

## Overview

គំរូនេះបង្ហាញពីវិធីបង្កើតកម្មវិធីជជែកដែលមានស្រាប់សម្រាប់ផលិតកម្ម ដែលប្រើម៉ូដែល AI ក្នុងមូលដ្ឋានតាមរយៈ Foundry Local ផ្តល់ការពិភាក្សា AI ដែលផ្តោតលើភាពឯកជនដោយមិនពឹងផ្អែកលើថាសពពក។

## Features

### 🎨 **Windows 11 Native Design**
- បញ្ចូល Fluent Design System
- ផលប៉ះពាល់សម្ភារៈ Mica និងភាពថ្លា
- គាំទ្រធីមដើម Windows 11
- គ្រោងផ្ទាំងឆបគ្នាសម្រាប់ទំហំអេក្រង់ទាំងអស់
- ការប្តូររបៀបអណ្តាត/ភ្លឺដោយស្វ័យប្រវត្តិ

### 🤖 **AI Model Integration**
- បញ្ចូលសេវាកម្ម Foundry Local
- គ្រប់គ្រងម៉ូដែលច្រើន និងការប្តូរដោយរហ័ស
- תגובות ស្ទ្រីមក្នុងពេលពិត
- ការប្តូរម៉ូឌែលរវាងក្នុងកន្លែង និងថាសពពក
- ត្រួតពិនិត្យសុខភាពម៉ូដែល និងស្ថានភាព

### 💬 **Chat Experience**
- សញ្ញាកើតចុចភ្លាមពេលវេលា
- រក្សារាជីសារសារជជែក
- នាំចេញការពិភាក្សាជជែក
- ប្រើប្រាស់ system prompts ផ្ទាល់ខ្លួន
- ការបំបែក និងគ្រប់គ្រងការពិភាក្សា

### ⚡ **Performance Features**
- ការផ្ទុកយឺត និងវិច័នសាលីសេរ
- ការបង្ហាញដែលបានអុបទ៊ីម៉ាញសម្រាប់ការពិភាក្សាយូរអង្វែង
- ការរៀបចំម៉ូដែលពេលផ្ទុកពីក្រោយ
- ការគ្រប់គ្រងអង្គចងចាំមានប្រសិទ្ធភាព
- គ្រាម៉ូសូខលនិងចលករត្រួយមូល

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
- **OS**: Windows 11 (22H2 ឬពេលក្រោយបានផ្ដល់អនុសាសន៍)
- **RAM**: ចាប់ពី 8GB អប្បបរមា, 16GB+ បានផ្ដល់អនុសាសន៍សម្រាប់ម៉ូដែលធំជាង
- **Storage**: 10GB+ ទំហំទំនេរសម្រាប់ម៉ូដែល
- **GPU**: ជាជម្រើស ប៉ុន្តែបានផ្ដល់អនុសាសន៍សម្រាប់ការធ្វើអន្ដរាគមន៍លឿន

### Software Dependencies
- **Node.js**: v18.0.0 ឬនៅលើ
- **Foundry Local**: កំណែថ្មីបំផុតពី Microsoft
- **Git**: សម្រាប់ក្លូន និងការអភិវឌ្ឍន៍

## Installation

### 1. Install Foundry Local
```powershell
# ទាញយកពី GitHub releases ហើយដំឡើង
winget install Microsoft.FoundryLocal

# ផ្ទៀងផ្ទាត់​ការ​ដំឡើង
foundry --version
```

### 2. Clone and Setup
```bash
# ចូលទៅកាន់ថតគំរូ
cd Module08/samples/08

# ដំឡើងការពឹងផ្អែក
npm install

# ដំឡើង Electron ប្រសិនបើមិនបានដំឡើងជាកម្រិតសកល
npm install -g electron
```

### 3. Configure Environment
```powershell
# ជាជម្រើស៖ កំណត់ព័ត៌មានសម្គាល់សម្រាប់ម៉ូឌែលលើពពក សម្រាប់ម៉ូដ hybrid
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Run the Application
```bash
# ម៉ូដអភិវឌ្ឍន៍
npm start

# កំណែផលិត
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
- វត្ថុផ្ទៃក្រោយ Mica
- ផលប៉ះអាក្រីលិកភាពថ្លា
- ជ្រុងមុំរាប និងចម្លងទំនេរឆ្លៀតទំនើប
- ពណ៌ដើម Windows 11
- ធរណីមពណ៌សម្រាប់ភាពចូលរួមងាយស្រួល

**Native Windows Features**
- ចងចាំ Jump list សម្រាប់ជជែកថ្មីៗ
- ការជូនដំណឹង Windows សម្រាប់សារថ្មី
- ថ្នាក់របង្ហាញ Taskbar សម្រាប់ប្រតិបត្តិការម៉ូដែល
- បញ្ចូលក្នុង system tray ជាមួយសកម្មភាពរហ័ស
- គាំទ្រការផ្ទៀងផ្ទាត់ Windows Hello

### AI Model Management

**Local Models**
```javascript
// ការរកឃើញ និងផ្ទុកម៉ូដែលដោយស្វ័យប្រវត្តិ
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// ការតាមដានសុខភាពម៉ូដែល
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Hybrid Cloud/Local Support**
```javascript
// ការប្ដូរយ៉ាងរលូនរវាងម៉ូឌែលក្នុងឧបករណ៍ និងម៉ូឌែលលើពពក
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Chat Interface Features

**Real-time Streaming**
- បញ្ចាំងចម្លើយជា token ដោយ token
- សកម្មភាពវាយបញ្ចូលរលោង
- អនុញ្ញាតលុបការស្នើរសុំ
- សញ្ញាវាយបញ្ចូល និងស្ថានភាព

**Conversation Management**
- ប្រវត្តិជជែកដែលរក្សាទុកបាន
- នាំចេញ/នាំចូលការពិភាក្សា
- ស្វែងរកសារ និងតម្រង
- ការបំបែកការពិភាក្សា
- system prompts ផ្ទាល់ខ្លួនសម្រាប់ការពិភាក្សា

**Accessibility**
- ការរុករកពេញលេញជាមួយក្តាង
- ឧបករណ៍អានអេក្រង់សមរម្យ
- គាំទ្រចរន្តពាក់ព័ន្ធខ្ពស់
- អាចកំណត់ទំហំពុម្ពអក្សរ
- បញ្ចួលសំឡេងសម្រាប់វាយបញ្ចូល

## Usage Examples

### Basic Chat Integration
```javascript
// ចាប់ផ្តើមប្រព័ន្ធជជែក
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// ផ្ញើសារ
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// គ្រប់គ្រងការឆ្លើយតបស្ទ្រីម
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Model Management
```javascript
// ផ្ទុកម៉ូឌែលថ្មី
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// តាមដានប្រសិទ្ធភាពរបស់ម៉ូឌែល
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// ប្តូរម៉ូឌែលនៅកណ្ដាលការសន្ទនា
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Settings and Customization
```javascript
// កំណត់អាកប្បកិរិយារបស់ការជជែក
const settings = {
    theme: 'system', // ស្វ័យប្រវត្តិ, ស្រាល, ងងឹត
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
- **Theme**: អូតូ, Light, Dark mode
- **Model**: ជ្រើសម៉ូដែលលំនាំដើម
- **Performance**: ការកំណត់សម្រាប់ inference
- **Privacy**: គោលនយោបាយរក្សាទុកទិន្នន័យ
- **Notifications**: ការជូនដំណឹងសារ
- **Shortcuts**: ចំណុចកាត់ក្តែង

### Chat Settings
- **Streaming**: បើក/បិទចម្លើយក្នុងពេលពិត
- **Context Length**: សម័យចងចាំការពិភាក្សា
- **Temperature**: ការផ្គូផ្គងច្នៃប្រឌិតនៃចម្លើយ
- **Max Tokens**: ដែនកំណត់ប្រវែងចម្លើយ
- **System Prompts**: ឥរិយាបថជំនួយលំនាំដើម

### Model Settings
- **Auto-download**: ការទាញយកម៉ូដែលដោយស្វ័យប្រវត្តិ
- **Cache Size**: ពេលវេលាផ្ទុកម៉ូែលក្នុងមូលដ្ឋាន
- **Performance Mode**: ជម្រើស CPU ទល់នឹង GPU
- **Health Checks**: ប្រតិទិនត្រួតពិនិត្យសុខភាព

## Development

### Building from Source
```bash
# ដំឡើងអាស្រ័យភាពសម្រាប់ការអភិវឌ្ឍន៍
npm install

# រត់ក្នុងរបៀបអភិវឌ្ឍន៍
npm run dev

# បង្កើតសម្រាប់ការផលិត
npm run build

# បង្កើតកម្មវិធីដំឡើង
npm run dist
```

### Debugging
```bash
# បើកម៉ូដពិនិត្យកំហុស
set DEBUG=foundry-chat:*
npm start

# មើលឧបករណ៍អភិវឌ្ឍន៍
# ចុច F12 ក្នុងកម្មវិធី
```

### Testing
```bash
# រត់តេស្តឯកតា
npm test

# រត់តេស្តការរួមបញ្ចូល
npm run test:integration

# រត់តេស្តចុងទៅចុង
npm run test:e2e
```

## Performance Optimization

### Memory Management
- វិច័នសាលីសារសំណៅមានប្រសិទ្ធភាព
- ការប្រមូលបំណុលអង្គចងចាំដោយស្វ័យប្រវត្តិ
- តាមដានអង្គចងចាំម៉ូដែល
- សម្អាតធនធានពេលចេញ

### Rendering Optimization
- ការរមួលសង្ហារសម្រាប់ការពិភាក្សាយូរ
- ផ្ទុកយឺតប្រវត្តិសារ
- ធ្វើឲ្យ React/DOM បច្ចុប្បន្នភាពបានអុបទ៊ីម៉ាញ
- អានីម៉េសិនដែលបង្កើតដោយ GPU

### Network Optimization
- បំពង់សម្រាប់ការតភ្ជាប់
- បញ្ចូលសំណើជាក្រុម
- តុល្យភាពព្យួរឡើងវិញដោយស្វ័យប្រវត្តិ
- គាំទ្ររំដោះនៅលើអ៊ុតលាញ

## Security Considerations

### Data Privacy
- ស្ថាបត្យកម្មផ្តាច់មុខក្នុងមូលដ្ឋាន
- មិនមានការបញ្ជូនទិន្នន័យទៅថាសពពក (ម៉ូដក្នុងមូលដ្ឋាន)
- រក្សាទុកការពិភាក្សា בצורה កូដឌីក
- គ្រប់គ្រងឯកសារព័ត៌មានសុវត្ថិភាព

### Application Security
- ដំណើរការរេសិនឈើត្រារក្សានៅក្នុង sandbox
- គោលនយោបាយសុវត្ថិភាពខ្លឹមសារ (CSP)
- មិនមានការប្រតិបត្តិគូដពីចម្រង់ពីចម្ងាយ
- ការទំនាក់ទំនង IPC ដែលមានសុវត្ថិភាព

## Troubleshooting

### Common Issues

**Foundry Local Not Starting**
```powershell
# ពិនិត្យស្ថានភាពសេវាកម្ម
foundry status

# ចាប់ផ្ដើមសេវាកម្មឡើងវិញ
foundry restart

# ពិនិត្យកំណត់ហេតុ
foundry logs
```

**Model Loading Failures**
- ពិនិត្យទំហំដីដែលគ្រប់គ្រាន់
- ពិនិត្យការតភ្ជាប់អ៊ីនធឺណែតសម្រាប់ការទាញយក
- ធានាថាអ្នកបានអាប់ដេតឌ្រៃវើរការ GPU
- ព្យាយាមប្រភេទម៉ូដែលផ្សេងៗ

**Performance Issues**
- តាមដានធនធានប្រព័ន្ធ
- បត់បែនការកំណត់ម៉ូដែល
- បើកប្រើ hardware acceleration
- បិទកម្មវិធីផ្សេងៗដែលប្រើរថធនធានច្រើន

### Debug Mode
បើកកំណត់ហេតុ debug ដោយកំណត់អថេរស្ថានបរិយាកាស:
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
- កំណត់ ESLint ត្រូវបានផ្ដល់
- Prettier សម្រាប់ទ្រង់ទ្រាយកូដ
- TypeScript សម្រាប់សុវត្ថិភាពប្រភេទ
- JSDoc កំណត់សម្រាប់ឯកសារ

## Learning Outcomes

After completing this sample, you will understand:

1. **Windows 11 Native Development**
   - ការអនុវត្ត Fluent Design System
   - ការបញ្ចូលដើម Windows
   - គន្លឹះសុវត្ថិភាព Electron

2. **AI Model Integration**
   - ស្ថាបត្យកម្មសេវាកម្ម Foundry Local
   - គ្រប់គ្រងរវត្តិជីវម៉ូដែល
   - ការត្រួតពិនិត្យ និងអុបទ៊ីម៉ាញកម្មសមត្ថភាព

3. **Real-time Chat Systems**
   - ការគ្រប់គ្រងចម្លើយស្ទ្រីម
   - ការគ្រប់គ្រងស្ថានភាពការពិភាក្សា
   - គំរូបទពិសោធន៍អ្នកប្រើ

4. **Production Application Development**
   - ការដោះស្រាយកំហុស និងដំណើរការថយក្រោយ
   - ការអុបទ៊ីម៉ាញកម្រិត
   - ផ្នែកសុវត្ថិភាព
   - យុទ្ធសាស្ត្រសាកល្បង

## Next Steps

- **Sample 09**: Multi-Agent Orchestration System
- **Sample 10**: Foundry Local as Tools Integration
- **Advanced Topics**: ការបំពាក់ម៉ូដែលផ្ទាល់ខ្លួន
- **Deployment**: គំរូដាក់ពង្រីកសម្រាប់សហគ្រាស

## License

គំរូនេះអនុវត្តតាមបណ្ណាសិទ្ធិដូចគ្នាជាមួយគម្រោង Microsoft Foundry Local។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខំប្រឹងសម្រាប់ភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែម៉ាស៊ីនអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានចាត់ទុកជាប្រភពដែលមានអំណាច។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ យើងណែនាំឱ្យប្រើការបកប្រែដោយអ្នកបកប្រែមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->