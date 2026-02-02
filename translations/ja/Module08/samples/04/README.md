# サンプル 04: Chainlit を使ったプロダクションチャットアプリケーション

Microsoft Foundry Local を活用し、モダンなウェブインターフェース、ストリーミング応答、最新のブラウザ技術を備えたプロダクション対応のチャットアプリケーションを構築する複数のアプローチを包括的に紹介します。

## 含まれる内容

- **🚀 Chainlit チャットアプリ** (`app.py`): ストリーミング対応のプロダクションチャットアプリケーション
- **🌐 WebGPU デモ** (`webgpu-demo/`): ハードウェアアクセラレーションを活用したブラウザベースのAI推論
- **🎨 Open WebUI 統合** (`open-webui-guide.md`): プロフェッショナルなChatGPT風インターフェース
- **📚 教育用ノートブック** (`chainlit_app.ipynb`): インタラクティブな学習教材

## クイックスタート

### 1. Chainlit チャットアプリケーション

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

アクセス先: `http://localhost:8080`

### 2. WebGPU ブラウザデモ

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

アクセス先: `http://localhost:5173`

### 3. Open WebUI セットアップ

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

アクセス先: `http://localhost:3000`

## アーキテクチャパターン

### ローカル vs クラウドの意思決定マトリックス

| シナリオ | 推奨 | 理由 |
|----------|------|------|
| **プライバシーが重要なデータ** | 🏠 ローカル (Foundry) | データがデバイスを離れない |
| **複雑な推論** | ☁️ クラウド (Azure OpenAI) | 大規模モデルへのアクセス |
| **リアルタイムチャット** | 🏠 ローカル (Foundry) | 低遅延で高速応答 |
| **ドキュメント分析** | 🔄 ハイブリッド | 抽出はローカル、分析はクラウド |
| **コード生成** | 🏠 ローカル (Foundry) | プライバシー + 専用モデル |
| **研究タスク** | ☁️ クラウド (Azure OpenAI) | 幅広い知識ベースが必要 |

### 技術比較

| 技術 | 使用ケース | 利点 | 欠点 |
|------|------------|------|------|
| **Chainlit** | Python開発者、迅速なプロトタイプ作成 | 簡単なセットアップ、ストリーミング対応 | Python限定 |
| **WebGPU** | 最大限のプライバシー、オフラインシナリオ | ブラウザネイティブ、サーバー不要 | モデルサイズが制限される |
| **Open WebUI** | プロダクション展開、チーム向け | プロフェッショナルなUI、ユーザー管理 | Dockerが必要 |

## 必要条件

- **Foundry Local**: インストール済みで稼働中 ([ダウンロード](https://aka.ms/foundry-local-installer))
- **Python**: 3.10以上、仮想環境付き
- **モデル**: 少なくとも1つロード済み (`foundry model run phi-4-mini`)
- **ブラウザ**: WebGPU対応のChrome/Edge
- **Docker**: Open WebUI用 (オプション)

## インストールとセットアップ

### 1. Python環境のセットアップ

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local のセットアップ

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## サンプルアプリケーション

### Chainlit チャットアプリケーション

**特徴:**
- 🚀 **リアルタイムストリーミング**: トークンが生成されるとすぐに表示
- 🛡️ **堅牢なエラーハンドリング**: 優雅な劣化と回復
- 🎨 **モダンなUI**: プロフェッショナルなチャットインターフェース
- 🔧 **柔軟な設定**: 環境変数と自動検出
- 📱 **レスポンシブデザイン**: デスクトップとモバイルで動作

**クイックスタート:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU ブラウザデモ

**特徴:**
- 🌐 **ブラウザネイティブAI**: サーバー不要、完全にブラウザ内で動作
- ⚡ **WebGPUアクセラレーション**: 利用可能な場合はハードウェアアクセラレーション
- 🔒 **最大限のプライバシー**: データがデバイスを離れることはない
- 🎯 **ゼロインストール**: 互換性のあるブラウザで動作
- 🔄 **優雅なフォールバック**: WebGPUが利用できない場合はCPUに切り替え

**実行方法:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI 統合

**特徴:**
- 🎨 **ChatGPT風インターフェース**: プロフェッショナルで馴染みのあるUI
- 👥 **マルチユーザー対応**: ユーザーアカウントと会話履歴
- 📁 **ファイル処理**: ドキュメントのアップロードと分析
- 🔄 **モデル切り替え**: 異なるモデル間の簡単な切り替え
- 🐳 **Docker展開**: プロダクション対応のコンテナ化セットアップ

**クイックセットアップ:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## 設定リファレンス

### 環境変数

| 変数 | 説明 | デフォルト | 例 |
|------|------|------------|----|
| `MODEL` | 使用するモデルのエイリアス | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local のエンドポイント | 自動検出 | `http://localhost:51211` |
| `API_KEY` | APIキー (ローカルではオプション) | `""` | `your-api-key` |

## トラブルシューティング

### よくある問題

**Chainlit アプリケーション:**

1. **サービスが利用できない:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **ポート競合:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python環境の問題:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU デモ:**

1. **WebGPUがサポートされていない:**
   - Chrome/Edge 113以上に更新
   - WebGPUを有効化: `chrome://flags/#enable-unsafe-webgpu`
   - GPUステータスを確認: `chrome://gpu`
   - デモは自動的にCPUにフォールバックします

2. **モデルのロードエラー:**
   - モデルダウンロードのためのインターネット接続を確認
   - ブラウザコンソールでCORSエラーを確認
   - HTTP経由で提供されていることを確認 (file://ではなく)

**Open WebUI:**

1. **接続拒否:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **モデルが表示されない:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### 検証チェックリスト

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## 高度な使用法

### パフォーマンス最適化

**Chainlit:**
- ストリーミングを使用して知覚的なパフォーマンスを向上
- 高い同時接続性のために接続プールを実装
- 繰り返しクエリのためにモデル応答をキャッシュ
- 大規模な会話履歴でメモリ使用量を監視

**WebGPU:**
- 最大限のプライバシーと速度のためにWebGPUを使用
- 小型モデルのためにモデル量子化を実装
- バックグラウンド処理のためにWeb Workersを使用
- ブラウザストレージにコンパイル済みモデルをキャッシュ

**Open WebUI:**
- 会話履歴のために永続ボリュームを使用
- Dockerコンテナのリソース制限を設定
- ユーザーデータのバックアップ戦略を実装
- SSL終端のためにリバースプロキシを設定

### 統合パターン

**ローカル/クラウドのハイブリッド:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**マルチモーダルパイプライン:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## プロダクション展開

### セキュリティ考慮事項

- **APIキー**: 環境変数を使用し、ハードコードしない
- **ネットワーク**: プロダクションではHTTPSを使用し、チームアクセスにはVPNを検討
- **アクセス制御**: Open WebUIに認証を実装
- **データプライバシー**: ローカルに留まるデータとクラウドに送信されるデータを監査
- **更新**: Foundry Localとコンテナを最新状態に保つ

### 監視と保守

- **ヘルスチェック**: エンドポイントの監視を実装
- **ログ**: すべてのコンポーネントからログを集中管理
- **メトリクス**: 応答時間、エラー率、リソース使用量を追跡
- **バックアップ**: 会話データと設定の定期的なバックアップ

## 参考文献とリソース

### ドキュメント
- [Chainlit Documentation](https://docs.chainlit.io/) - フレームワークの完全ガイド
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Microsoft公式ドキュメント
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU統合
- [Open WebUI Documentation](https://docs.openwebui.com/) - 高度な設定

### サンプルファイル
- [`app.py`](../../../../../Module08/samples/04/app.py) - プロダクションChainlitアプリケーション
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - 教育用ノートブック
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - ブラウザベースのAI推論
- [`open-webui-guide.md`](./open-webui-guide.md) - 完全なOpen WebUIセットアップ

### 関連サンプル
- [Session 4 Documentation](../../04.CuttingEdgeModels.md) - 完全なセッションガイド
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - 公式サンプル

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。