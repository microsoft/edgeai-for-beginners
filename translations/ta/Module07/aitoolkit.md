# Visual Studio Code க்கான AI Toolkit - Edge AI மேம்பாட்டு வழிகாட்டி

## அறிமுகம்

Edge AI மேம்பாட்டில் Visual Studio Code க்கான AI Toolkit ஐ பயன்படுத்துவதற்கான விரிவான வழிகாட்டிக்கு வரவேற்கிறோம். மையக Cloud கணினி செயல்பாடுகளிலிருந்து Edge சாதனங்களுக்கான விநியோகத்திற்குத் தாவும் செயற்கை நுண்ணறிவு, மேம்படுத்துபவர்கள் Edge Deployment இன் தனித்துவமான சவால்களைச் சமாளிக்க சக்திவாய்ந்த, ஒருங்கிணைந்த கருவிகளைத் தேவைப்படுகிறார்கள் - வளங்களின் கட்டுப்பாடுகள் முதல் Offline செயல்பாட்டு தேவைகள் வரை.

Visual Studio Code க்கான AI Toolkit இந்த இடைவெளியை நிரப்புகிறது, Edge சாதனங்களில் திறமையாக இயங்கும் AI பயன்பாடுகளை உருவாக்க, சோதிக்க மற்றும் மேம்படுத்துவதற்காக வடிவமைக்கப்பட்ட முழுமையான மேம்பாட்டு சூழலை வழங்குகிறது. நீங்கள் IoT சென்சார்கள், மொபைல் சாதனங்கள், Embedded Systems அல்லது Edge Servers க்காக மேம்படுத்துகிறீர்களா என்பதைப் பொருத்தவரை, இந்த Toolkit உங்கள் முழு மேம்பாட்டு வேலைப்பாடுகளை VS Code சூழலில் எளிமைப்படுத்துகிறது.

இந்த வழிகாட்டி, ஆரம்ப மாடல் தேர்வு முதல் உற்பத்தி Deployment வரை, உங்கள் Edge AI திட்டங்களில் AI Toolkit ஐ பயன்படுத்துவதற்கான முக்கியமான கருத்துக்கள், கருவிகள் மற்றும் சிறந்த நடைமுறைகளை உங்களுக்குக் கற்றுத்தரும்.

## மேற்பார்வை

Visual Studio Code க்கான AI Toolkit என்பது Agent Development மற்றும் AI பயன்பாடுகளை உருவாக்குவதற்கான சக்திவாய்ந்த Extension ஆகும். Anthropic, OpenAI, GitHub, Google போன்ற பல்வேறு வழங்குநர்களிடமிருந்து AI மாடல்களை ஆராய, மதிப்பீடு செய்ய மற்றும் Deploy செய்ய முழுமையான திறன்களை வழங்குகிறது - ONNX மற்றும் Ollama ஐப் பயன்படுத்தி உள்ளூர் மாடல் செயல்பாட்டை ஆதரிக்கிறது.

AI Toolkit ஐ தனித்துவமாக்குவது அதன் முழுமையான AI மேம்பாட்டு வாழ்க்கைச் சுழற்சிக்கான அணுகுமுறையாகும். பாரம்பரிய AI மேம்பாட்டு கருவிகள் தனித்துவமான அம்சங்களில் கவனம் செலுத்துவதற்குப் பதிலாக, AI Toolkit மாடல் கண்டுபிடிப்பு, பரிசோதனை, Agent Development, மதிப்பீடு மற்றும் Deployment ஆகியவற்றை ஒருங்கிணைந்த சூழலில் வழங்குகிறது - VS Code சூழலில்.

இந்த தளம் விரைவான Prototype மற்றும் உற்பத்தி Deployment க்காக குறிப்பாக வடிவமைக்கப்பட்டுள்ளது, Prompt Generation, Quick Starters, Seamless MCP (Model Context Protocol) Tool Integration மற்றும் விரிவான மதிப்பீட்டு திறன்களுடன். Edge AI மேம்பாட்டிற்காக, Edge Deployment சூழல்களுக்கு AI பயன்பாடுகளை திறமையாக உருவாக்க, சோதிக்க மற்றும் மேம்படுத்தலாம், VS Code இல் முழு மேம்பாட்டு வேலைப்பாடுகளை பராமரிக்கலாம்.

## கற்றல் நோக்கங்கள்

இந்த வழிகாட்டியின் முடிவில், நீங்கள் பின்வருவனவற்றைச் செய்ய முடியும்:

### முக்கிய திறன்கள்
- Edge AI மேம்பாட்டு வேலைப்பாடுகளுக்காக Visual Studio Code க்கான AI Toolkit ஐ **Install மற்றும் Configure** செய்யவும்
- **AI Toolkit Interface ஐ Navigate மற்றும் Utilize** செய்யவும், Model Catalog, Playground மற்றும் Agent Builder உட்பட
- **Edge Deployment க்கு ஏற்ற AI மாடல்களை தேர்வு மற்றும் மதிப்பீடு** செய்யவும், செயல்திறன் மற்றும் வளங்களின் கட்டுப்பாடுகளை அடிப்படையாகக் கொண்டு
- Edge சாதனங்களுக்காக ONNX Format மற்றும் Quantization Techniques ஐப் பயன்படுத்தி **மாடல்களை மாற்றவும் மற்றும் மேம்படுத்தவும்**

### Edge AI மேம்பாட்டு திறன்கள்
- **Edge AI பயன்பாடுகளை வடிவமைத்து செயல்படுத்தவும்** ஒருங்கிணைந்த மேம்பாட்டு சூழலைப் பயன்படுத்தி
- **Edge போன்ற சூழல்களில் மாடல் சோதனை** செய்யவும், உள்ளூர் inference மற்றும் Resource Monitoring ஐப் பயன்படுத்தி
- Edge Deployment சூழல்களுக்கு **Optimize செய்யப்பட்ட AI Agents ஐ உருவாக்கவும் மற்றும் Customize செய்யவும்**
- Edge Computing க்கு தொடர்புடைய Metrics (Latency, Memory Usage, Accuracy) ஐப் பயன்படுத்தி **மாடல் செயல்திறனை மதிப்பீடு செய்யவும்**

### Optimization மற்றும் Deployment
- **Quantization மற்றும் Pruning Techniques ஐப் பயன்படுத்தி** மாடல் அளவைக் குறைத்து, ஏற்றுக்கொள்ளக்கூடிய செயல்திறனை பராமரிக்கவும்
- CPU, GPU மற்றும் NPU Acceleration உட்பட குறிப்பிட்ட Edge Hardware Platforms க்கு **மாடல்களை Optimize செய்யவும்**
- **Edge AI மேம்பாட்டிற்கான சிறந்த நடைமுறைகளை செயல்படுத்தவும்**, Resource Management மற்றும் Fallback Strategies உட்பட
- Edge சாதனங்களில் **உற்பத்தி Deployment க்கு மாடல்கள் மற்றும் பயன்பாடுகளைத் தயாரிக்கவும்**

### மேம்பட்ட Edge AI கருத்துக்கள்
- ONNX Runtime, Windows ML மற்றும் TensorFlow Lite உட்பட **Edge AI Frameworks உடன் ஒருங்கிணைக்கவும்**
- Edge சூழல்களுக்கு **Multi-Model Architectures மற்றும் Federated Learning Scenarios ஐ செயல்படுத்தவும்**
- Memory Constraints, Inference Speed மற்றும் Hardware Compatibility உட்பட **சாதாரண Edge AI சிக்கல்களை Troubleshoot செய்யவும்**
- உற்பத்தியில் Edge AI பயன்பாடுகளுக்கான **Monitoring மற்றும் Logging Strategies ஐ வடிவமைக்கவும்**

### நடைமுறை பயன்பாடு
- **மாடல் தேர்வு முதல் Deployment வரை முழுமையான Edge AI தீர்வுகளை உருவாக்கவும்**
- Edge-க்கு குறிப்பிட்ட மேம்பாட்டு வேலைப்பாடுகள் மற்றும் Optimization Techniques க்கு **திறமையாக செயல்படவும்**
- IoT, Mobile மற்றும் Embedded Applications உட்பட **உலகளாவிய Edge AI பயன்பாடுகளில் கற்றுக்கொண்ட கருத்துகளைப் பயன்படுத்தவும்**
- Edge AI Deployment Strategies மற்றும் அவற்றின் Trade-offs ஐ **மதிப்பீடு செய்து ஒப்பிடவும்**

## Edge AI மேம்பாட்டிற்கான முக்கிய அம்சங்கள்

### 1. மாடல் Catalog மற்றும் கண்டுபிடிப்பு
- **Multi-Provider Support**: Anthropic, OpenAI, GitHub, Google மற்றும் பிற வழங்குநர்களிடமிருந்து AI மாடல்களை Browse மற்றும் Access செய்யவும்
- **Local Model Integration**: Edge Deployment க்கு ONNX மற்றும் Ollama மாடல்களை எளிதாக கண்டுபிடிக்கவும்
- **GitHub Models**: GitHub இன் மாடல் Hosting உடன் நேரடி ஒருங்கிணைப்பு
- **Model Comparison**: Edge சாதனங்களின் கட்டுப்பாடுகளுக்கு ஏற்ற சரியான சமநிலையை கண்டறிய மாடல்களை ஒப்பிடவும்

### 2. Interactive Playground
- **Interactive Testing Environment**: கட்டுப்படுத்தப்பட்ட சூழலில் மாடல் திறன்களை விரைவாக பரிசோதிக்கவும்
- **Multi-modal Support**: Edge சூழல்களில் பொதுவாக உள்ள Images, Text மற்றும் பிற Inputs உடன் சோதிக்கவும்
- **Real-time Experimentation**: மாடல் பதில்கள் மற்றும் செயல்திறனில் உடனடி Feedback
- **Parameter Optimization**: Edge Deployment தேவைகளுக்கு மாடல் Parameters ஐ Fine-tune செய்யவும்

### 3. Prompt (Agent) Builder
- **Natural Language Generation**: இயற்கை மொழி விளக்கங்களைப் பயன்படுத்தி Starter Prompts ஐ உருவாக்கவும்
- **Iterative Refinement**: மாடல் பதில்கள் மற்றும் செயல்திறனை அடிப்படையாகக் கொண்டு Prompts ஐ மேம்படுத்தவும்
- **Task Decomposition**: Prompt Chaining மற்றும் Structured Outputs மூலம் சிக்கலான பணிகளை உடைக்கவும்
- **Variable Support**: Dynamic Agent நடத்தைக்கான Prompts இல் Variables ஐப் பயன்படுத்தவும்
- **Production Code Generation**: விரைவான App Development க்கு உற்பத்தி-தயாரான Code ஐ உருவாக்கவும்

### 4. Bulk Run மற்றும் Evaluation
- **Multi-Model Testing**: தேர்ந்தெடுக்கப்பட்ட மாடல்களில் பல Prompts ஐ ஒரே நேரத்தில் செயல்படுத்தவும்
- **Efficient Testing at Scale**: பல Inputs மற்றும் Configurations ஐ திறமையாக சோதிக்கவும்
- **Custom Test Cases**: Functionality ஐ Validate செய்ய Test Cases உடன் Agents ஐ இயக்கவும்
- **Performance Comparison**: மாடல்கள் மற்றும் Configurations க்கு இடையிலான முடிவுகளை ஒப்பிடவும்

### 5. Model Evaluation with Datasets
- **Standard Metrics**: Built-in Evaluators (F1 Score, Relevance, Similarity, Coherence) ஐப் பயன்படுத்தி AI மாடல்களை சோதிக்கவும்
- **Custom Evaluators**: குறிப்பிட்ட பயன்பாடுகளுக்கான உங்கள் சொந்த மதிப்பீட்டு Metrics ஐ உருவாக்கவும்
- **Dataset Integration**: விரிவான Datasets க்கு எதிராக மாடல்களை சோதிக்கவும்
- **Performance Measurement**: Edge Deployment முடிவுகளுக்கான மாடல் செயல்திறனை அளவிடவும்

### 6. Fine-tuning Capabilities
- **Model Customization**: குறிப்பிட்ட Edge Deployment Constraints க்கு மாடல்களை Fine-tune செய்யவும்
- **Domain-Specific Training**: Edge பயன்பாடுகளுக்கான மாடல்களை உருவாக்கவும்

### 7. MCP Tool Integration
- **External Tool Connectivity**: Model Context Protocol Servers மூலம் Tools ஐ இணைக்கவும்
- **Real-world Actions**: Agents க்கு Databases ஐ Query செய்ய, APIs ஐ Access செய்ய அல்லது Custom Logic ஐ Execute செய்ய அனுமதிக்கவும்
- **Existing MCP Servers**: Command (stdio) அல்லது HTTP (server-sent event) Protocols ஐப் பயன்படுத்தி Tools ஐப் பயன்படுத்தவும்
- **Custom MCP Development**: Agent Builder இல் புதிய MCP Servers ஐ உருவாக்கி சோதிக்கவும்

### 8. Agent Development மற்றும் Testing
- **Function Calling Support**: Agents க்கு வெளிப்புற Functions ஐ Dynamic ஆக Invoke செய்ய அனுமதிக்கவும்
- **Real-time Integration Testing**: Tools ஐப் பயன்படுத்தி Real-time Runs உடன் Integration ஐ சோதிக்கவும்
- **Agent Versioning**: Evaluation முடிவுகளுக்கான Comparison திறன்களுடன் Agents க்கு Version Control
- **Debugging மற்றும் Tracing**: Agent Development க்கு உள்ளூர் Tracing மற்றும் Debugging திறன்கள்

## Edge AI மேம்பாட்டு வேலைப்பாடு

### கட்டம் 1: மாடல் கண்டுபிடிப்பு மற்றும் தேர்வு
1. **Model Catalog ஐ Explore செய்யவும்**: Edge Deployment க்கு ஏற்ற மாடல்களை கண்டறிய Catalog ஐப் பயன்படுத்தவும்
2. **Performance ஐ ஒப்பிடவும்**: அளவு, துல்லியம் மற்றும் Inference Speed அடிப்படையில் மாடல்களை மதிப்பீடு செய்யவும்
3. **Local Testing**: Edge Deployment க்கு முன் Ollama அல்லது ONNX மாடல்களை உள்ளூரில் சோதிக்கவும்
4. **Resource Requirements ஐ மதிப்பீடு செய்யவும்**: இலக்கு Edge சாதனங்களுக்கான Memory மற்றும் Computational தேவைகளைத் தீர்மானிக்கவும்

### கட்டம் 2: மாடல் Optimization
1. **ONNX க்கு மாற்றவும்**: Edge Compatibility க்கு தேர்ந்தெடுக்கப்பட்ட மாடல்களை ONNX Format க்கு மாற்றவும்
2. **Quantization ஐப் பயன்படுத்தவும்**: INT8 அல்லது INT4 Quantization மூலம் மாடல் அளவைக் குறைக்கவும்
3. **Hardware Optimization**: இலக்கு Edge Hardware க்கு (ARM, x86, Specialized Accelerators) Optimize செய்யவும்
4. **Performance Validation**: Optimize செய்யப்பட்ட மாடல்கள் ஏற்றுக்கொள்ளக்கூடிய துல்லியத்தை பராமரிக்கின்றனவா என்பதை Validate செய்யவும்

### கட்டம் 3: பயன்பாட்டு மேம்பாடு
1. **Agent Design**: Edge-optimized AI Agents ஐ உருவாக்க Agent Builder ஐப் பயன்படுத்தவும்
2. **Prompt Engineering**: சிறிய Edge மாடல்களுடன் திறமையாக வேலை செய்ய Prompts ஐ உருவாக்கவும்
3. **Integration Testing**: Simulated Edge சூழல்களில் Agents ஐ சோதிக்கவும்
4. **Code Generation**: Edge Deployment க்கு Optimize செய்யப்பட்ட உற்பத்தி Code ஐ உருவாக்கவும்

### கட்டம் 4: மதிப்பீடு மற்றும் சோதனை
1. **Batch Evaluation**: Edge Settings க்கு ஏற்ற சிறந்த Configurations ஐ கண்டறிய பல Configurations ஐ சோதிக்கவும்
2. **Performance Profiling**: Inference Speed, Memory Usage மற்றும் Accuracy ஐப் பகுப்பாய்வு செய்யவும்
3. **Edge Simulation**: இலக்கு Edge Deployment சூழலுக்கு ஒத்த சூழலில் சோதிக்கவும்
4. **Stress Testing**: பல்வேறு Load சூழல்களில் செயல்திறனை மதிப்பீடு செய்யவும்

### கட்டம் 5: Deployment தயாரிப்பு
1. **Final Optimization**: சோதனை முடிவுகளை அடிப்படையாகக் கொண்டு இறுதி Optimization ஐச் செய்யவும்
2. **Deployment Packaging**: Edge Deployment க்கு மாடல்கள் மற்றும் Code ஐ Package செய்யவும்
3. **Documentation**: Deployment தேவைகள் மற்றும் Configuration ஐ Document செய்யவும்
4. **Monitoring Setup**: Edge Deployment க்கு Monitoring மற்றும் Logging ஐத் தயாரிக்கவும்

## Edge AI மேம்பாட்டிற்கான இலக்கு பார்வையாளர்கள்

### Edge AI Developers
- AI-இயக்க Edge சாதனங்கள் மற்றும் IoT தீர்வுகளை உருவாக்கும் பயன்பாட்டு மேம்படுத்துபவர்கள்
- Resource-constrained சாதனங்களில் AI திறன்களை ஒருங்கிணைக்கும் Embedded Systems மேம்படுத்துபவர்கள்
- Smartphones மற்றும் Tablets க்கான On-device AI பயன்பாடுகளை உருவாக்கும் Mobile Developers

### Edge AI Engineers
- Edge Deployment க்கு மாடல்களை Optimize செய்ய AI Engineers மற்றும் Inference Pipelines ஐ நிர்வகிக்க
- Distributed Edge Infrastructure க்கு AI மாடல்களை Deploy மற்றும் நிர்வகிக்கும் DevOps Engineers
- Edge Hardware Constraints க்கு AI Workloads ஐ Optimize செய்ய Performance Engineers

### Researchers மற்றும் Educators
- Edge Computing க்கு திறமையான மாடல்கள் மற்றும் Algorithms ஐ உருவாக்க AI Researchers
- Edge AI கருத்துக்களை கற்பித்து Optimization Techniques ஐ விளக்கும் Educators
- Edge AI Deployment இல் சவால்கள் மற்றும் தீர்வுகளைப் பற்றி கற்றுக்கொள்ளும் Students

## Edge AI பயன்பாடுகள்

### Smart IoT சாதனங்கள்
- **Real-time Image Recognition**: IoT Cameras மற்றும் Sensors க்கு Computer Vision மாடல்களை Deploy செய்யவும்
- **Voice Processing**: Smart Speakers க்கு Speech Recognition மற்றும் Natural Language Processing ஐ செயல்படுத்தவும்
- **Predictive Maintenance**: Industrial Edge சாதனங்களில் Anomaly Detection மாடல்களை இயக்கவும்
- **Environmental Monitoring**: Environmental Applications க்கு Sensor Data Analysis மாடல்களை Deploy செய்யவும்

### Mobile மற்றும் Embedded பயன்பாடுகள்
- **On-device Translation**: Offline இல் வேலை செய்ய Language Translation மாடல்களை செயல்படுத்தவும்
- **Augmented Reality**: AR பயன்பாடுகளுக்கான Real-time Object Recognition மற்றும் Tracking ஐ Deploy செய்யவும்
- **Health Monitoring**: Wearable சாதனங்கள் மற்றும் மருத்துவ உபகரணங்களில் Health Analysis மாடல்களை இயக்கவும்
- **Autonomous Systems**: Drones, Robots மற்றும் Vehicles க்கு Decision-making மாடல்களை செயல்படுத்தவும்

### Edge Computing Infrastructure
- **Edge Data Centers**: குறைந்த Latency பயன்பாடுகளுக்கான Edge Data Centers இல் AI மாடல்களை Deploy செய்யவும்
- **CDN Integration**: Content Delivery Networks க்கு AI Processing திறன்களை ஒருங்கிணைக்கவும்
- **5G Edge**: AI-powered Applications க்கு 5G Edge Computing ஐ பயன்படுத்தவும்
- **Fog Computing**: Fog Computing சூழல்களில் AI Processing ஐ செயல்படுத்தவும்

## Installation மற்றும் Setup

### Extension Installation
Visual Studio Code Marketplace இல் இருந்து AI Toolkit Extension ஐ நேரடியாக Install செய்யவும்:

**Extension ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installation Methods**:
1. **VS Code Marketplace**: Extensions View இல் "AI Toolkit" ஐத் தேடவும்
2. **Command Line**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direct Install**: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) இல் இருந்து Download செய்யவும்

### Edge AI மேம்பாட்டிற்கான முன் தேவைகள்
- **Visual Studio Code**: சமீபத்திய பதிப்பு பரிந்துரைக்கப்படுகிறது
- **Python Environment**: Python 3.8+ மற்றும் தேவையான AI Libraries
- **ONNX Runtime** (Optional): ONNX மாடல் Inference க்கு
- **Ollama** (Optional): Local Model Serving க்கு
- **Hardware Acceleration Tools**: CUDA, OpenVINO அல்லது Platform-Specific Accelerators

### ஆரம்ப Configuration
1. **Extension Activation**: VS Code ஐ திறந்து AI Toolkit Activity Bar இல் தோன்றுகிறதா என்பதை உறுதிப்படுத்தவும்
2. **Model Provider Setup**: GitHub, OpenAI, Anthropic அல்லது பிற Model Providers க்கு Access ஐ Configure செய்யவும்
3. **Local Environment**: Python Environment ஐ அமைத்து தேவையான Packages ஐ Install செய்யவும்
4. **Hardware Acceleration**: GPU/NPU Acceleration ஐ Configure செய்யவும் (இருப்பின்)
5. **MCP Integration**: Model Context Protocol Servers ஐ அமைக்கவும் (தேவைப்பட்டால்)

### First-Time Setup Checklist
- [ ] AI Toolkit Extension Install செய்து Activate செய்யப்பட்டது
- [ ] Model Catalog Access செய்யக்கூடியது மற்றும் Models Discoverable
- [ ] Playground Model Testing க்கு Functional
- [ ] Prompt Development க்கு Agent Builder Access செய்யக்கூடியது
- [ ] Local Development Environment Configure செய்யப்பட்டது
- [ ] Hardware Acceleration (இருப்பின்) சரியாக Configure செய்யப்பட்டது

## AI Toolkit உடன் தொடங்குதல்

### Quick Start Guide

GitHub இல் Host செய்யப்படும் மாடல்களுடன் தொடங்க பரிந்துரைக்கிறோம்:

1. **Installation**: உங்கள் சாதனத்திற்கான AI Toolkit ஐ அமைக்க [Installation Guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) ஐப் பின்பற்றவும்
2. **Model Discovery**: Extension Tree View இல் **CATALOG > Models** ஐத் தேர்ந்தெடுத்து கிடைக்கக்கூடிய மாடல்களை Explore செய்யவும்
3. **GitHub Models**: சிறந்த Integration க்கு GitHub இல் Host செய்யப்படும் மாடல்களுடன் தொடங்கவும்
4. **Playground Testing**: எந்த Model Card இல் இருந்தும் **Try in Playground** ஐத் தேர்ந்தெடுத்து மாடல் திறன்களை பரிசோதிக்க தொடங்கவும்

### Edge AI மேம்பாட்டிற்கான படிப்படையான வழிகாட்டி

#### படி 1: மாடல் ஆராய்ச்சி மற்றும் தேர்வு
1. VS Code Activity Bar இல் AI Toolkit View ஐ திறக்கவும்
2. Edge Deployment க்கு ஏற்ற மாடல்களை Model Catalog இல் Browse செய்யவும்
3. உங்கள் Edge தேவைகளை அடிப்படையாகக் கொண்டு Provider (GitHub, ONNX, Ollama) மூலம் Filter செய்யவும்

2. இயற்கை மொழி விளக்கங்களைப் பயன்படுத்தி தொடக்க உந்துதல்களை உருவாக்கவும்  
3. மாதிரியின் பதில்களை அடிப்படையாகக் கொண்டு உந்துதல்களை திருத்தி மேம்படுத்தவும்  
4. மேம்பட்ட முகவர் திறன்களுக்காக MCP கருவிகளை ஒருங்கிணைக்கவும்  

#### படி 3: சோதனை மற்றும் மதிப்பீடு  
1. **Bulk Run**-ஐப் பயன்படுத்தி தேர்ந்தெடுக்கப்பட்ட மாதிரிகளில் பல உந்துதல்களை சோதிக்கவும்  
2. சோதனை வழக்குகளுடன் முகவர்களை இயக்கி செயல்பாட்டை சரிபார்க்கவும்  
3. உள்ளமைக்கப்பட்ட அல்லது தனிப்பயன் அளவுகோல்களைப் பயன்படுத்தி துல்லியத்தையும் செயல்திறனையும் மதிப்பீடு செய்யவும்  
4. வெவ்வேறு மாதிரிகள் மற்றும் கட்டமைப்புகளை ஒப்பிடவும்  

#### படி 4: நுணுக்கமாக அமைத்தல் மற்றும் மேம்பாடு  
1. குறிப்பிட்ட விளிம்பு பயன்பாடுகளுக்காக மாதிரிகளை தனிப்பயனாக்கவும்  
2. துறைக்கு ஏற்ற நுணுக்கமாக அமைத்தல் பயன்படுத்தவும்  
3. விளிம்பு பயன்பாட்டு கட்டுப்பாடுகளுக்காக மேம்படுத்தவும்  
4. வெவ்வேறு முகவர் கட்டமைப்புகளை பதிப்பாக்கம் செய்து ஒப்பிடவும்  

#### படி 5: வெளியீட்டு தயாரிப்பு  
1. Agent Builder-ஐப் பயன்படுத்தி உற்பத்திக்கு தயாரான குறியீட்டை உருவாக்கவும்  
2. MCP சர்வர் இணைப்புகளை உற்பத்தி பயன்பாட்டுக்காக அமைக்கவும்  
3. விளிம்பு சாதனங்களுக்கான வெளியீட்டு தொகுப்புகளை தயாரிக்கவும்  
4. கண்காணிப்பு மற்றும் மதிப்பீட்டு அளவுகோல்களை அமைக்கவும்  

## AI கருவி தொகுப்புக்கான மாதிரிகள்  

எங்கள் மாதிரிகளை முயற்சிக்கவும்  
[AI கருவி தொகுப்பு மாதிரிகள்](https://github.com/Azure-Samples/AI_Toolkit_Samples) டெவலப்பர்கள் மற்றும் ஆராய்ச்சியாளர்கள் AI தீர்வுகளைச் சரியாக ஆராய்ந்து செயல்படுத்த உதவ உருவாக்கப்பட்டுள்ளன.  

எங்கள் மாதிரிகள் அடங்கும்:  

மாதிரி குறியீடு: AI செயல்பாடுகளை, மாதிரிகளைப் பயிற்றுவித்தல், வெளியிடுதல் அல்லது பயன்பாடுகளில் ஒருங்கிணைத்தல் போன்றவற்றை விளக்குவதற்கான முன்பே உருவாக்கப்பட்ட உதாரணங்கள்.  
ஆவணங்கள்: AI கருவி தொகுப்பின் அம்சங்களைப் புரிந்து கொள்ளவும், அவற்றைப் பயன்படுத்தவும் பயனர்களுக்கு உதவும் வழிகாட்டுதல்கள் மற்றும் பயிற்சிகள்.  

முன் தேவைகள்  

- Visual Studio Code  
- Visual Studio Code-க்கான AI கருவி தொகுப்பு  
- GitHub Fine-grained தனிப்பட்ட அணுகல் டோக்கன் (PAT)  
- Foundry Local  

## விளிம்பு AI மேம்பாட்டுக்கான சிறந்த நடைமுறைகள்  

### மாதிரி தேர்வு  
- **அளவின் கட்டுப்பாடுகள்**: இலக்கு சாதனங்களின் நினைவக வரம்புக்குள் பொருந்தும் மாதிரிகளைத் தேர்ந்தெடுக்கவும்  
- **தீர்மான வேகம்**: நேரடி பயன்பாடுகளுக்காக வேகமான தீர்மான நேரம் கொண்ட மாதிரிகளை முன்னுரிமை அளிக்கவும்  
- **துல்லியத்தின் சமநிலை**: மாதிரி துல்லியத்தையும் வளங்களின் கட்டுப்பாடுகளையும் சமநிலைப்படுத்தவும்  
- **வடிவ இணக்கத்தன்மை**: விளிம்பு வெளியீட்டுக்காக ONNX அல்லது ஹார்ட்வேருக்கு ஏற்ற வடிவங்களை முன்னுரிமை அளிக்கவும்  

### மேம்பாட்டு உத்திகள்  
- **Quantization**: மாதிரியின் அளவைக் குறைத்து வேகத்தை மேம்படுத்த INT8 அல்லது INT4 Quantization பயன்படுத்தவும்  
- **Pruning**: கணினி தேவைகளை குறைக்க தேவையற்ற மாதிரி அளவுருக்களை நீக்கவும்  
- **Knowledge Distillation**: பெரிய மாதிரிகளின் செயல்திறனை பராமரிக்கும் சிறிய மாதிரிகளை உருவாக்கவும்  
- **Hardware Acceleration**: NPUs, GPUs அல்லது கிடைக்கும் சிறப்பு வேகப்படுத்திகளை பயன்படுத்தவும்  

### மேம்பாட்டு வேலைநிலை  
- **மீளும் சோதனை**: மேம்பாட்டின் போது விளிம்பு போன்ற சூழல்களில் அடிக்கடி சோதிக்கவும்  
- **செயல்திறன் கண்காணிப்பு**: வளங்களின் பயன்பாடு மற்றும் தீர்மான வேகத்தை தொடர்ந்து கண்காணிக்கவும்  
- **பதிப்பு கட்டுப்பாடு**: மாதிரி பதிப்புகள் மற்றும் மேம்பாட்டு அமைப்புகளை கண்காணிக்கவும்  
- **ஆவணங்கள்**: அனைத்து மேம்பாட்டு முடிவுகளையும் செயல்திறன் சமநிலைகளையும் ஆவணப்படுத்தவும்  

### வெளியீட்டு கருத்துக்கள்  
- **வள கண்காணிப்பு**: உற்பத்தியில் நினைவகம், CPU மற்றும் மின்சார பயன்பாட்டை கண்காணிக்கவும்  
- **Fallback Strategies**: மாதிரி தோல்விகளுக்கான மாற்று வழிகளை செயல்படுத்தவும்  
- **Update Mechanisms**: மாதிரி புதுப்பிப்புகள் மற்றும் பதிப்பு மேலாண்மைக்கான திட்டம் அமைக்கவும்  
- **Security**: விளிம்பு AI பயன்பாடுகளுக்கான சரியான பாதுகாப்பு நடவடிக்கைகளை செயல்படுத்தவும்  

## விளிம்பு AI கட்டமைப்புகளுடன் ஒருங்கிணைப்பு  

### ONNX Runtime  
- **குறுகிய-பலகை வெளியீடு**: ONNX மாதிரிகளை வெவ்வேறு விளிம்பு தளங்களில் வெளியிடவும்  
- **ஹார்ட்வேரின் மேம்பாடு**: ONNX Runtime-இன் ஹார்ட்வேருக்கு ஏற்ற மேம்பாடுகளை பயன்படுத்தவும்  
- **மொபைல் ஆதரவு**: ஸ்மார்ட்போன்கள் மற்றும் டேப்லெட்கள் பயன்பாடுகளுக்காக ONNX Runtime Mobile பயன்படுத்தவும்  
- **IoT ஒருங்கிணைப்பு**: ONNX Runtime-இன் இலகு விநியோகங்களைப் பயன்படுத்தி IoT சாதனங்களில் வெளியிடவும்  

### Windows ML  
- **Windows சாதனங்கள்**: Windows அடிப்படையிலான விளிம்பு சாதனங்கள் மற்றும் PCs-க்கு மேம்படுத்தவும்  
- **NPU வேகப்படுத்தல்**: Windows சாதனங்களில் Neural Processing Units-ஐ பயன்படுத்தவும்  
- **DirectML**: Windows தளங்களில் GPU வேகப்படுத்தலுக்காக DirectML பயன்படுத்தவும்  
- **UWP ஒருங்கிணைப்பு**: Universal Windows Platform பயன்பாடுகளுடன் ஒருங்கிணைக்கவும்  

### TensorFlow Lite  
- **மொபைல் மேம்பாடு**: மொபைல் மற்றும் உட்பொறி சாதனங்களில் TensorFlow Lite மாதிரிகளை வெளியிடவும்  
- **ஹார்ட்வேரின் பிரதிநிதிகள்**: வேகப்படுத்தலுக்காக சிறப்பு ஹார்ட்வேரின் பிரதிநிதிகளைப் பயன்படுத்தவும்  
- **Micro Controllers**: TensorFlow Lite Micro-ஐப் பயன்படுத்தி மைக்ரோ கண்ட்ரோலர்களில் வெளியிடவும்  
- **குறுகிய-பலகை ஆதரவு**: Android, iOS மற்றும் உட்பொறி Linux அமைப்புகளில் வெளியிடவும்  

### Azure IoT Edge  
- **Cloud-Edge Hybrid**: மேக பயிற்சியுடன் விளிம்பு தீர்மானத்தை இணைக்கவும்  
- **Module Deployment**: AI மாதிரிகளை IoT Edge modules ஆக வெளியிடவும்  
- **Device Management**: விளிம்பு சாதனங்கள் மற்றும் மாதிரி புதுப்பிப்புகளை தொலைவிலிருந்து நிர்வகிக்கவும்  
- **Telemetry**: விளிம்பு வெளியீட்டிலிருந்து செயல்திறன் தரவுகள் மற்றும் மாதிரி அளவுகோல்களை சேகரிக்கவும்  

## மேம்பட்ட விளிம்பு AI சூழல்கள்  

### பல மாதிரி வெளியீடு  
- **Model Ensembles**: துல்லியத்தை மேம்படுத்த அல்லது மீள்நிரப்பத்திற்காக பல மாதிரிகளை வெளியிடவும்  
- **A/B Testing**: விளிம்பு சாதனங்களில் ஒரே நேரத்தில் வெவ்வேறு மாதிரிகளை சோதிக்கவும்  
- **Dynamic Selection**: தற்போதைய சாதன நிலைமைகளின் அடிப்படையில் மாதிரிகளைத் தேர்ந்தெடுக்கவும்  
- **Resource Sharing**: பல வெளியிடப்பட்ட மாதிரிகளுக்கு இடையில் வளங்களின் பயன்பாட்டை மேம்படுத்தவும்  

### Federated Learning  
- **Distributed Training**: பல விளிம்பு சாதனங்களில் மாதிரிகளைப் பயிற்றுவிக்கவும்  
- **Privacy Preservation**: பயிற்சி தரவுகளை உள்ளூர் நிலையில் வைத்துக்கொண்டு மாதிரி மேம்பாடுகளைப் பகிரவும்  
- **Collaborative Learning**: சாதனங்கள் கூட்டாக அனுபவங்களிலிருந்து கற்றுக்கொள்ள உதவவும்  
- **Edge-Cloud Coordination**: விளிம்பு சாதனங்கள் மற்றும் மேக அமைப்புகளுக்கு இடையே கற்றலை ஒருங்கிணைக்கவும்  

### நேரடி செயலாக்கம்  
- **Stream Processing**: விளிம்பு சாதனங்களில் தொடர்ச்சியான தரவோட்டங்களை செயலாக்கவும்  
- **Low-latency Inference**: குறைந்த தீர்மான தாமதத்துக்காக மேம்படுத்தவும்  
- **Batch Processing**: விளிம்பு சாதனங்களில் தரவின் தொகுதிகளை திறமையாக செயலாக்கவும்  
- **Adaptive Processing**: தற்போதைய சாதன திறன்களின் அடிப்படையில் செயலாக்கத்தை சரிசெய்யவும்  

## விளிம்பு AI மேம்பாட்டுக்கான சிக்கல்களைத் தீர்க்குதல்  

### பொதுவான சிக்கல்கள்  
- **Memory Constraints**: இலக்கு சாதன நினைவகத்திற்காக மாதிரி மிகப்பெரியது  
- **Inference Speed**: நேரடி தேவைகளுக்காக மாதிரி தீர்மானம் மிகவும் மெதுவாக உள்ளது  
- **Accuracy Degradation**: மேம்பாடு மாதிரி துல்லியத்தை ஏற்க முடியாத அளவுக்கு குறைக்கிறது  
- **Hardware Compatibility**: மாதிரி இலக்கு ஹார்ட்வேருடன் இணக்கமாக இல்லை  

### பிழை தீர்க்கும் உத்திகள்  
- **Performance Profiling**: Bottlenecks-ஐ அடையாளம் காண AI கருவி தொகுப்பின் கண்காணிப்பு அம்சங்களைப் பயன்படுத்தவும்  
- **Resource Monitoring**: மேம்பாட்டின் போது நினைவகம் மற்றும் CPU பயன்பாட்டை கண்காணிக்கவும்  
- **Incremental Testing**: சிக்கல்களை தனித்தனியாக அடையாளம் காண மேம்பாடுகளை படிப்படியாக சோதிக்கவும்  
- **Hardware Simulation**: இலக்கு ஹார்ட்வேரை சிமுலேட் செய்ய மேம்பாட்டு கருவிகளைப் பயன்படுத்தவும்  

### மேம்பாட்டு தீர்வுகள்  
- **Further Quantization**: மேலும் தீவிரமான Quantization உத்திகளைப் பயன்படுத்தவும்  
- **Model Architecture**: விளிம்புக்கு மேம்படுத்தப்பட்ட வெவ்வேறு மாதிரி கட்டமைப்புகளைப் பரிசீலிக்கவும்  
- **Preprocessing Optimization**: விளிம்பு கட்டுப்பாடுகளுக்காக தரவின் முன் செயலாக்கத்தை மேம்படுத்தவும்  
- **Inference Optimization**: ஹார்ட்வேருக்கு ஏற்ற தீர்மான மேம்பாடுகளைப் பயன்படுத்தவும்  

## வளங்கள் மற்றும் அடுத்த படிகள்  

### அதிகாரப்பூர்வ ஆவணங்கள்  
- [AI கருவி தொகுப்பு டெவலப்பர் ஆவணங்கள்](https://aka.ms/AIToolkit/doc)  
- [நிறுவல் மற்றும் அமைப்பு வழிகாட்டி](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps ஆவணங்கள்](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) ஆவணங்கள்](https://modelcontextprotocol.io/)  

### சமூகமும் ஆதரவும்  
- [AI கருவி தொகுப்பு GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues மற்றும் அம்ச கோரிக்கைகள்](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### தொழில்நுட்ப வளங்கள்  
- [ONNX Runtime ஆவணங்கள்](https://onnxruntime.ai/)  
- [Ollama ஆவணங்கள்](https://ollama.ai/)  
- [Windows ML ஆவணங்கள்](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry ஆவணங்கள்](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### கற்றல் பாதைகள்  
- [விளிம்பு AI அடிப்படைகள் பாடநெறி](../Module01/README.md)  
- [சிறிய மொழி மாதிரிகள் வழிகாட்டி](../Module02/README.md)  
- [விளிம்பு வெளியீட்டு உத்திகள்](../Module03/README.md)  
- [Windows விளிம்பு AI மேம்பாடு](./windowdeveloper.md)  

### கூடுதல் வளங்கள்  
- **Repository Stats**: 1.8k+ stars, 150+ forks, 18+ contributors  
- **License**: MIT License  
- **Security**: Microsoft பாதுகாப்பு கொள்கைகள் பொருந்தும்  
- **Telemetry**: VS Code Telemetry அமைப்புகளை மதிக்கிறது  

## முடிவு  

Visual Studio Code-க்கான AI கருவி தொகுப்பு, Edge AI பயன்பாடுகளுக்காக குறிப்பாக மதிப்புமிக்க திறமைகளை வழங்கும், நவீன AI மேம்பாட்டுக்கான விரிவான தளத்தை பிரதிநிதித்துவப்படுத்துகிறது. Anthropic, OpenAI, GitHub மற்றும் Google போன்ற வழங்குநர்களை ஆதரிக்கும் விரிவான மாதிரி பட்டியலுடன், ONNX மற்றும் Ollama மூலம் உள்ளூர் செயல்பாடுகளுடன் இணைந்து, இந்த கருவி தொகுப்பு பல்வேறு விளிம்பு வெளியீட்டு சூழல்களுக்கு தேவையான நெகிழ்வுத்தன்மையை வழங்குகிறது.  

இந்த கருவி தொகுப்பின் பலம் அதன் ஒருங்கிணைந்த அணுகுமுறையில் உள்ளது—Playground-இல் மாதிரிகளை கண்டறிதல் மற்றும் பரிசோதனையிலிருந்து, Prompt Builder மூலம் நுண்ணிய முகவர் மேம்பாடு, விரிவான மதிப்பீட்டு திறன்கள் மற்றும் MCP கருவி ஒருங்கிணைப்புடன். Edge AI டெவலப்பர்களுக்கு, இது விளிம்பு வெளியீட்டுக்கு முன் AI முகவர்களை விரைவாக உருவாக்கவும் சோதிக்கவும், விரைவாக திருத்தவும் மற்றும் வளங்களின் கட்டுப்பாடுகளுக்காக மேம்படுத்தவும் உதவுகிறது.  

Edge AI மேம்பாட்டுக்கான முக்கிய நன்மைகள்:  
- **விரைவான பரிசோதனை**: விளிம்பு வெளியீட்டுக்கு முன் மாதிரிகள் மற்றும் முகவர்களை விரைவாக சோதிக்கவும்  
- **பல வழங்குநர் நெகிழ்வுத்தன்மை**: விளிம்பு தீர்வுகளுக்காக சிறந்த மாதிரிகளை கண்டறிய பல்வேறு ஆதாரங்களில் இருந்து அணுகவும்  
- **உள்ளூர் மேம்பாடு**: Offline மற்றும் தனியுரிமை பாதுகாப்பு மேம்பாட்டுக்காக ONNX மற்றும் Ollama-ஐ சோதிக்கவும்  
- **உற்பத்தி தயாரிப்பு**: MCP மூலம் வெளிப்புற கருவிகளுடன் ஒருங்கிணைத்து உற்பத்திக்கு தயாரான குறியீட்டை உருவாக்கவும்  
- **விரிவான மதிப்பீடு**: விளிம்பு AI செயல்திறனை சரிபார்க்க உள்ளமைக்கப்பட்ட மற்றும் தனிப்பயன் அளவுகோல்களைப் பயன்படுத்தவும்  

AI தொடர்ந்து விளிம்பு வெளியீட்டு சூழல்களுக்குச் செல்கையில், Visual Studio Code-க்கான AI கருவி தொகுப்பு, வளங்களின் கட்டுப்பாடுகளுக்காக நுண்ணிய பயன்பாடுகளை உருவாக்க, சோதிக்க மற்றும் மேம்படுத்த தேவையான மேம்பாட்டு சூழலையும் வேலைநிலையையும் வழங்குகிறது. நீங்கள் IoT தீர்வுகளை, மொபைல் AI பயன்பாடுகளை அல்லது உட்பொறி நுண்ணறிவு அமைப்புகளை உருவாக்குகிறீர்களா என்பதைப் பொருத்து, இந்த கருவி தொகுப்பின் விரிவான அம்சங்கள் மற்றும் ஒருங்கிணைந்த வேலைநிலை, முழு விளிம்பு AI மேம்பாட்டு வாழ்க்கைச்சுழற்சிக்கான ஆதரவை வழங்குகிறது.  

தொடர்ந்து மேம்பாடு மற்றும் 1.8k+ GitHub stars கொண்ட ஒரு செயலில் உள்ள சமூகத்துடன், AI கருவி தொகுப்பு, Edge Deployment சூழல்களுக்காக உருவாக்கும் நவீன AI டெவலப்பர்களின் தேவைகளை பூர்த்தி செய்ய தொடர்ந்து முன்னணியில் உள்ளது.  

[Next Foundry Local](./foundrylocal.md)  

---

**புறக்கணிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.