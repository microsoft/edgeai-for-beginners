# Windows 11 聊天示例 - Foundry Local

一个现代化的 Windows 11 聊天应用程序，结合了 Microsoft Foundry Local 和优美的原生界面。基于 Electron 构建，并遵循微软官方的 Foundry Local 模式。

## 概述

此示例展示了如何创建一个生产级聊天应用程序，通过 Foundry Local 利用本地 AI 模型，为用户提供注重隐私的 AI 对话，无需依赖云服务。

## 功能

### 🎨 **Windows 11 原生设计**
- 集成 Fluent Design System
- Mica 材质效果和透明度
- 支持 Windows 11 原生主题
- 响应式布局，适配所有屏幕尺寸
- 自动切换深色/浅色模式

### 🤖 **AI 模型集成**
- 集成 Foundry Local 服务
- 支持多模型热切换
- 实时流式响应
- 本地与云模型切换
- 模型健康监控与状态管理

### 💬 **聊天体验**
- 实时输入指示器
- 消息历史持久化
- 导出聊天记录
- 自定义系统提示
- 对话分支与管理

### ⚡ **性能特性**
- 延迟加载与虚拟化
- 优化长对话的渲染
- 背景模型预加载
- 高效内存管理
- 流畅的动画与过渡效果

## 架构

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

## 前提条件

### 系统要求
- **操作系统**: Windows 11（建议 22H2 或更高版本）
- **内存**: 最低 8GB，建议 16GB+ 用于较大模型
- **存储**: 至少 10GB 可用空间用于模型
- **GPU**: 可选，但推荐用于更快的推理

### 软件依赖
- **Node.js**: v18.0.0 或更高版本
- **Foundry Local**: 从微软获取最新版本
- **Git**: 用于克隆和开发

## 安装

### 1. 安装 Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. 克隆并设置
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. 配置环境
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. 运行应用程序
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## 项目结构

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

## 关键功能深入解析

### Windows 11 集成

**Fluent Design System**
- Mica 背景材质
- Acrylic 透明效果
- 圆角和现代间距
- Windows 11 原生调色板
- 语义化颜色标记，提升可访问性

**原生 Windows 功能**
- 最近聊天的跳转列表集成
- 新消息的 Windows 通知
- 模型操作的任务栏进度显示
- 系统托盘集成快速操作
- 支持 Windows Hello 身份验证

### AI 模型管理

**本地模型**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**混合云/本地支持**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### 聊天界面功能

**实时流式响应**
- 按令牌逐步显示响应
- 流畅的输入动画
- 可取消的请求
- 输入指示器与状态显示

**对话管理**
- 持久化聊天历史
- 导出/导入对话
- 消息搜索与过滤
- 对话分支管理
- 每个对话的自定义系统提示

**可访问性**
- 完整的键盘导航
- 屏幕阅读器兼容
- 支持高对比度模式
- 可定制字体大小
- 集成语音输入

## 使用示例

### 基础聊天集成
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

### 模型管理
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

### 设置与自定义
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

## 配置选项

### 应用设置
- **主题**: 自动、浅色、深色模式
- **模型**: 默认模型选择
- **性能**: 推理设置
- **隐私**: 数据保留策略
- **通知**: 消息提醒
- **快捷键**: 键盘快捷方式

### 聊天设置
- **流式响应**: 启用/禁用实时响应
- **上下文长度**: 对话记忆
- **温度**: 响应创造性
- **最大令牌**: 响应长度限制
- **系统提示**: 默认助手行为

### 模型设置
- **自动下载**: 自动模型更新
- **缓存大小**: 本地模型存储限制
- **性能模式**: CPU 与 GPU 优化选择
- **健康检查**: 监控间隔

## 开发

### 从源码构建
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

### 调试
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### 测试
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## 性能优化

### 内存管理
- 高效的消息虚拟化
- 自动垃圾回收
- 模型内存监控
- 退出时资源清理

### 渲染优化
- 长对话的虚拟滚动
- 消息历史的延迟加载
- 优化 React/DOM 更新
- GPU 加速动画

### 网络优化
- 连接池管理
- 请求批处理
- 自动重试逻辑
- 离线模式支持

## 安全注意事项

### 数据隐私
- 本地优先架构
- 无云数据传输（本地模式）
- 加密的对话存储
- 安全的凭证管理

### 应用安全
- 沙盒化的渲染进程
- 内容安全策略 (CSP)
- 无远程代码执行
- 安全的 IPC 通信

## 故障排除

### 常见问题

**Foundry Local 无法启动**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**模型加载失败**
- 确保磁盘空间充足
- 检查下载所需的网络连接
- 确保 GPU 驱动已更新
- 尝试不同的模型版本

**性能问题**
- 监控系统资源
- 调整模型设置
- 启用硬件加速
- 关闭其他资源密集型应用

### 调试模式
通过设置环境变量启用调试日志：
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## 贡献

### 开发设置
1. Fork 仓库
2. 创建功能分支
3. 安装依赖: `npm install`
4. 进行修改并测试
5. 提交 Pull Request

### 代码风格
- 提供 ESLint 配置
- 使用 Prettier 格式化代码
- 使用 TypeScript 提供类型安全
- 使用 JSDoc 注释进行文档化

## 学习成果

完成此示例后，您将了解：

1. **Windows 11 原生开发**
   - Fluent Design System 实现
   - 原生 Windows 集成
   - Electron 安全最佳实践

2. **AI 模型集成**
   - Foundry Local 服务架构
   - 模型生命周期管理
   - 性能监控与优化

3. **实时聊天系统**
   - 流式响应处理
   - 对话状态管理
   - 用户体验模式

4. **生产级应用开发**
   - 错误处理与恢复
   - 性能优化
   - 安全注意事项
   - 测试策略

## 下一步

- **示例 09**: 多代理编排系统
- **示例 10**: Foundry Local 工具集成
- **高级主题**: 自定义模型微调
- **部署**: 企业部署模式

## 许可证

此示例遵循 Microsoft Foundry Local 项目的相同许可证。

---

