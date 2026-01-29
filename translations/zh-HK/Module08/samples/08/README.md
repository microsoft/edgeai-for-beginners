# Windows 11 聊天範例 - Foundry Local

一款現代化的 Windows 11 聊天應用程式，結合 Microsoft Foundry Local，並擁有美觀的原生介面。使用 Electron 架構，遵循 Microsoft 官方的 Foundry Local 模式。

## 概述

此範例展示如何建立一個可投入生產的聊天應用程式，透過 Foundry Local 利用本地 AI 模型，為用戶提供注重隱私的 AI 對話，無需依賴雲端。

## 功能

### 🎨 **Windows 11 原生設計**
- 整合 Fluent Design System
- Mica 材質效果及透明度
- 支援 Windows 11 原生主題
- 適應所有螢幕尺寸的響應式佈局
- 自動切換深色/淺色模式

### 🤖 **AI 模型整合**
- Foundry Local 服務整合
- 支援多個模型並可即時切換
- 即時串流回應
- 本地與雲端模型切換
- 模型健康狀態監控

### 💬 **聊天體驗**
- 即時打字指示器
- 訊息歷史記錄保存
- 匯出聊天對話
- 自訂系統提示
- 對話分支及管理

### ⚡ **效能功能**
- 延遲載入及虛擬化
- 優化長對話的渲染
- 背景模型預載
- 高效記憶體管理
- 流暢的動畫及過渡效果

## 架構

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

## 先決條件

### 系統需求
- **作業系統**: Windows 11 (建議 22H2 或更新版本)
- **記憶體**: 最少 8GB，建議 16GB 或以上以支援較大模型
- **儲存空間**: 至少 10GB 可用空間以存放模型
- **GPU**: 可選，但建議使用以加快推理速度

### 軟體依賴
- **Node.js**: v18.0.0 或更新版本
- **Foundry Local**: Microsoft 最新版本
- **Git**: 用於克隆及開發

## 安裝

### 1. 安裝 Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. 克隆及設置
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. 配置環境
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. 執行應用程式
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## 專案結構

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

## 核心功能深入探討

### Windows 11 整合

**Fluent Design System**
- Mica 背景材質
- Acrylic 透明效果
- 圓角及現代化間距
- Windows 11 原生色彩調色盤
- 提供語義化色彩標記以提升可及性

**原生 Windows 功能**
- 最近聊天的跳轉列表整合
- 新訊息的 Windows 通知
- 模型操作的工作列進度顯示
- 系統托盤整合快速操作
- 支援 Windows Hello 身份驗證

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

**混合雲端/本地支援**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### 聊天介面功能

**即時串流**
- 按 token 顯示回應
- 流暢的打字動畫
- 可取消的請求
- 打字指示器及狀態顯示

**對話管理**
- 聊天歷史記錄保存
- 對話匯出/匯入
- 訊息搜尋及篩選
- 對話分支
- 每個對話的自訂系統提示

**可及性**
- 完整鍵盤導航
- 支援螢幕閱讀器
- 高對比模式支援
- 可自訂字型大小
- 語音輸入整合

## 使用範例

### 基本聊天整合
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

### 設定及自訂
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

## 配置選項

### 應用程式設定
- **主題**: 自動、淺色、深色模式
- **模型**: 預設模型選擇
- **效能**: 推理設定
- **隱私**: 資料保存政策
- **通知**: 訊息提醒
- **快捷鍵**: 鍵盤快捷鍵

### 聊天設定
- **串流**: 啟用/停用即時回應
- **上下文長度**: 對話記憶
- **溫度**: 回應創意性
- **最大 token 數**: 回應長度限制
- **系統提示**: 預設助理行為

### 模型設定
- **自動下載**: 模型自動更新
- **快取大小**: 本地模型儲存限制
- **效能模式**: CPU 與 GPU 偏好
- **健康檢查**: 監控間隔

## 開發

### 從源碼建置
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

### 除錯
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### 測試
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## 效能優化

### 記憶體管理
- 高效的訊息虛擬化
- 自動垃圾回收
- 模型記憶體監控
- 退出時資源清理

### 渲染優化
- 長對話的虛擬滾動
- 訊息歷史的延遲載入
- React/DOM 更新的優化
- GPU 加速動畫

### 網路優化
- 連接池管理
- 請求批次處理
- 自動重試邏輯
- 支援離線模式

## 安全考量

### 資料隱私
- 本地優先架構
- 無雲端資料傳輸（本地模式）
- 加密的對話存儲
- 安全的憑證管理

### 應用程式安全
- 沙盒化的渲染進程
- 內容安全政策 (CSP)
- 無遠端代碼執行
- 安全的 IPC 通訊

## 疑難排解

### 常見問題

**Foundry Local 無法啟動**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**模型載入失敗**
- 確保磁碟空間充足
- 檢查網路連接以進行下載
- 確保 GPU 驅動程式已更新
- 嘗試不同的模型版本

**效能問題**
- 監控系統資源
- 調整模型設定
- 啟用硬體加速
- 關閉其他資源密集型應用程式

### 除錯模式
透過設置環境變數啟用除錯日誌：
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## 貢獻

### 開發設置
1. Fork 此儲存庫
2. 建立功能分支
3. 安裝依賴項：`npm install`
4. 進行修改並測試
5. 提交 Pull Request

### 代碼風格
- 提供 ESLint 配置
- 使用 Prettier 進行代碼格式化
- 使用 TypeScript 確保類型安全
- 使用 JSDoc 註解進行文件化

## 學習成果

完成此範例後，您將了解：

1. **Windows 11 原生開發**
   - Fluent Design System 的實現
   - 原生 Windows 整合
   - Electron 安全最佳實踐

2. **AI 模型整合**
   - Foundry Local 服務架構
   - 模型生命週期管理
   - 效能監控及優化

3. **即時聊天系統**
   - 串流回應處理
   - 對話狀態管理
   - 用戶體驗模式

4. **生產應用程式開發**
   - 錯誤處理及恢復
   - 效能優化
   - 安全考量
   - 測試策略

## 下一步

- **範例 09**: 多代理協作系統
- **範例 10**: Foundry Local 作為工具整合
- **進階主題**: 自訂模型微調
- **部署**: 企業部署模式

## 授權

此範例遵循 Microsoft Foundry Local 專案的相同授權條款。

---

