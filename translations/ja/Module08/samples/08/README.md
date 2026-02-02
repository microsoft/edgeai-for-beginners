# Windows 11 Chat Sample - Foundry Local

Windows 11向けのモダンなチャットアプリケーションで、美しいネイティブインターフェイスとMicrosoft Foundry Localを統合しています。Electronを使用し、Microsoftの公式Foundry Localパターンに従って構築されています。

## 概要

このサンプルは、Foundry Localを通じてローカルAIモデルを活用し、クラウド依存なしでプライバシー重視のAI会話を提供する、実用的なチャットアプリケーションの作成方法を示します。

## 特徴

### 🎨 **Windows 11ネイティブデザイン**
- Fluent Design Systemの統合
- Mica素材効果と透明感
- Windows 11のネイティブテーマ対応
- すべての画面サイズに対応したレスポンシブレイアウト
- ダーク/ライトモードの自動切り替え

### 🤖 **AIモデル統合**
- Foundry Localサービスの統合
- 複数モデルのサポートとホットスワッピング
- リアルタイムのストリーミング応答
- ローカルとクラウドモデルの切り替え
- モデルのヘルスモニタリングとステータス管理

### 💬 **チャット体験**
- リアルタイムの入力インジケーター
- メッセージ履歴の永続化
- チャット会話のエクスポート
- カスタムシステムプロンプト
- 会話の分岐と管理

### ⚡ **パフォーマンス機能**
- レイジーローディングと仮想化
- 長い会話のための最適化されたレンダリング
- バックグラウンドモデルのプリロード
- 効率的なメモリ管理
- スムーズなアニメーションとトランジション

## アーキテクチャ

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

## 必要条件

### システム要件
- **OS**: Windows 11 (22H2以降推奨)
- **RAM**: 最低8GB、16GB以上推奨（大規模モデル向け）
- **ストレージ**: モデル用に10GB以上の空き容量
- **GPU**: オプションだが、高速推論のため推奨

### ソフトウェア依存関係
- **Node.js**: v18.0.0以降
- **Foundry Local**: Microsoftの最新バージョン
- **Git**: クローンと開発用

## インストール

### 1. Foundry Localのインストール
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. クローンとセットアップ
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. 環境設定
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. アプリケーションの実行
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## プロジェクト構造

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

## 主な機能の詳細

### Windows 11統合

**Fluent Design System**
- Mica背景素材
- アクリル透明効果
- 丸みを帯びた角とモダンな間隔
- Windows 11のネイティブカラーパレット
- アクセシビリティのためのセマンティックカラートークン

**ネイティブWindows機能**
- 最近のチャット用ジャンプリスト統合
- 新しいメッセージのWindows通知
- モデル操作のタスクバー進捗表示
- クイックアクション付きのシステムトレイ統合
- Windows Hello認証対応

### AIモデル管理

**ローカルモデル**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**ハイブリッドクラウド/ローカルサポート**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### チャットインターフェイス機能

**リアルタイムストリーミング**
- トークンごとの応答表示
- スムーズな入力アニメーション
- リクエストのキャンセル可能
- 入力インジケーターとステータス

**会話管理**
- 永続的なチャット履歴
- 会話のエクスポート/インポート
- メッセージ検索とフィルタリング
- 会話の分岐
- 会話ごとのカスタムシステムプロンプト

**アクセシビリティ**
- フルキーボードナビゲーション
- スクリーンリーダー対応
- 高コントラストモード対応
- カスタマイズ可能なフォントサイズ
- 音声入力統合

## 使用例

### 基本的なチャット統合
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

### モデル管理
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

### 設定とカスタマイズ
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

## 設定オプション

### アプリケーション設定
- **テーマ**: 自動、ライト、ダークモード
- **モデル**: デフォルトモデル選択
- **パフォーマンス**: 推論設定
- **プライバシー**: データ保持ポリシー
- **通知**: メッセージアラート
- **ショートカット**: キーボードショートカット

### チャット設定
- **ストリーミング**: リアルタイム応答の有効/無効
- **コンテキスト長**: 会話メモリ
- **温度**: 応答の創造性
- **最大トークン**: 応答の長さ制限
- **システムプロンプト**: デフォルトのアシスタント動作

### モデル設定
- **自動ダウンロード**: モデルの自動更新
- **キャッシュサイズ**: ローカルモデルのストレージ制限
- **パフォーマンスモード**: CPU vs GPUの選択
- **ヘルスチェック**: モニタリング間隔

## 開発

### ソースからのビルド
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

### デバッグ
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### テスト
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## パフォーマンス最適化

### メモリ管理
- 効率的なメッセージ仮想化
- 自動ガベージコレクション
- モデルメモリのモニタリング
- 終了時のリソースクリーンアップ

### レンダリング最適化
- 長い会話のための仮想スクロール
- メッセージ履歴のレイジーローディング
- 最適化されたReact/DOM更新
- GPU加速アニメーション

### ネットワーク最適化
- 接続プーリング
- リクエストのバッチ処理
- 自動リトライロジック
- オフラインモード対応

## セキュリティに関する考慮事項

### データプライバシー
- ローカルファーストアーキテクチャ
- クラウドデータ送信なし（ローカルモード）
- 暗号化された会話ストレージ
- 安全な資格情報管理

### アプリケーションセキュリティ
- サンドボックス化されたレンダラープロセス
- コンテンツセキュリティポリシー (CSP)
- リモートコード実行なし
- 安全なIPC通信

## トラブルシューティング

### よくある問題

**Foundry Localが起動しない**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**モデルの読み込み失敗**
- 十分なディスク容量を確認
- ダウンロードのためのインターネット接続を確認
- GPUドライバーが最新であることを確認
- 別のモデルバリアントを試す

**パフォーマンス問題**
- システムリソースをモニタリング
- モデル設定を調整
- ハードウェアアクセラレーションを有効化
- 他のリソース集約型アプリケーションを閉じる

### デバッグモード
環境変数を設定してデバッグログを有効化:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## コントリビューション

### 開発セットアップ
1. リポジトリをフォーク
2. フィーチャーブランチを作成
3. 依存関係をインストール: `npm install`
4. 変更を加えてテスト
5. プルリクエストを送信

### コードスタイル
- ESLint構成を提供
- Prettierによるコードフォーマット
- TypeScriptによる型安全性
- JSDocコメントによるドキュメント化

## 学習成果

このサンプルを完了すると、以下を理解できます:

1. **Windows 11ネイティブ開発**
   - Fluent Design Systemの実装
   - ネイティブWindows統合
   - Electronのセキュリティベストプラクティス

2. **AIモデル統合**
   - Foundry Localサービスアーキテクチャ
   - モデルライフサイクル管理
   - パフォーマンスモニタリングと最適化

3. **リアルタイムチャットシステム**
   - ストリーミング応答の処理
   - 会話状態管理
   - ユーザー体験パターン

4. **実用的なアプリケーション開発**
   - エラー処理と回復
   - パフォーマンス最適化
   - セキュリティに関する考慮事項
   - テスト戦略

## 次のステップ

- **サンプル09**: マルチエージェントオーケストレーションシステム
- **サンプル10**: Foundry Localをツールとして統合
- **高度なトピック**: カスタムモデルの微調整
- **デプロイメント**: エンタープライズデプロイメントパターン

## ライセンス

このサンプルはMicrosoft Foundry Localプロジェクトと同じライセンスに従います。

---

