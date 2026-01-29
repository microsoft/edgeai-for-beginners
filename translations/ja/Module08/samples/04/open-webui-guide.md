# Open WebUI + Foundry Local 統合ガイド

このガイドでは、Open WebUIをMicrosoft Foundry Localに接続し、ローカルAIモデルを活用したプロフェッショナルなChatGPT風インターフェースを構築する方法を説明します。

## 概要

Open WebUIは、OpenAI互換APIに接続可能なモダンで使いやすいチャットインターフェースを提供します。Foundry Localと接続することで以下の利点が得られます：

- **プロフェッショナルなUI**: ChatGPT風のモダンなデザインのインターフェース
- **ローカルプライバシー**: すべての処理がデバイス上で行われる
- **モデル切り替え**: 簡単に異なるローカルモデルを切り替え可能
- **会話履歴**: 永続的なチャット履歴とコンテキスト
- **ファイルアップロード**: ドキュメント解析やファイル処理機能
- **カスタムパーソナ**: システムプロンプトや役割のカスタマイズ

## 必要条件

### 必須ソフトウェア

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### モデルのロード

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## クイックセットアップ（推奨）

### ステップ1: DockerでOpen WebUIを実行

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### ステップ2: 初期設定

1. **ブラウザを開く**: `http://localhost:3000` にアクセス
2. **アカウント作成**: 管理者ユーザーを設定（最初のユーザーが管理者になります）
3. **接続確認**: モデルが自動的にドロップダウンに表示されるはずです

### ステップ3: 接続テスト

1. ドロップダウンからモデルを選択（例: "phi-4-mini"）
2. テストメッセージを入力: "こんにちは！自己紹介をお願いします。"
3. ローカルモデルからストリーミングレスポンスが表示されるはずです

## 高度な設定

### 環境変数

| 変数 | 目的 | デフォルト | 例 |
|------|------|-----------|----|
| `OPENAI_API_BASE_URL` | Foundry Localのエンドポイント | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | APIキー（ローカルでは必須ではありません） | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | セッション暗号化キー | 自動生成 | `your-secret-key` |
| `ENABLE_SIGNUP` | 新規ユーザー登録を許可 | `True` | `False` |

### 手動設定（代替方法）

環境変数が機能しない場合は、手動で設定します：

1. **設定を開く**: 設定（歯車アイコン）をクリック
2. **接続に移動**: 設定 → 接続 → OpenAI
3. **API詳細を設定**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key`（任意の値でOK）
4. **保存とテスト**: 「保存」をクリックし、モデルでテスト

### 永続的なデータ保存

会話や設定を保存するには：

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## トラブルシューティング

### 接続問題

**問題**: "Connection refused" またはモデルが読み込まれない

**解決策**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### モデルが表示されない

**問題**: Open WebUIでドロップダウンにモデルが表示されない

**デバッグ手順**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**修正**: モデルが正しくロードされていることを確認：
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Dockerネットワーク問題

**問題**: `host.docker.internal` が解決されない

**Windowsの解決策**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**代替方法**: マシンのIPを確認：
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### パフォーマンス問題

**レスポンスが遅い**:
1. モデルがGPUアクセラレーションを使用しているか確認: `foundry service ps`
2. システムリソース（RAM/GPUメモリ）が十分か確認
3. テストには小型モデルを使用することを検討

**メモリ問題**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## 使用ガイド

### 基本的なチャット

1. **モデルを選択**: ドロップダウンからFoundry Localモデルを選択
2. **メッセージを入力**: 下部のテキスト入力を使用
3. **送信**: Enterキーを押すか送信ボタンをクリック
4. **レスポンスを確認**: ストリーミングレスポンスをリアルタイムで表示

### 高度な機能

**ファイルアップロード**:
1. クリップアイコンをクリック
2. ドキュメントをアップロード（PDF、TXTなど）
3. コンテンツに関する質問をする
4. モデルがドキュメントを解析し、回答を提供

**カスタムシステムプロンプト**:
1. 設定 → パーソナライズ
2. カスタムシステムプロンプトを設定
3. 一貫したAIの性格や振る舞いを作成

**会話管理**:
- **新しいチャット**: "+"をクリックして新しい会話を開始
- **チャット履歴**: サイドバーから以前の会話にアクセス
- **エクスポート**: チャット履歴をテキスト/JSON形式でダウンロード

**モデル比較**:
1. 同じOpen WebUIを複数のブラウザタブで開く
2. 各タブで異なるモデルを選択
3. 同じプロンプトに対するレスポンスを比較

### 統合パターン

**開発ワークフロー**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## 本番環境へのデプロイ

### セキュアな設定

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### マルチユーザー設定

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### モニタリングとログ

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## クリーンアップ

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## 次のステップ

### 強化アイデア

1. **カスタムモデル**: Foundry Localに独自の微調整モデルを追加
2. **API統合**: Open WebUIの機能を通じて外部APIに接続
3. **ドキュメント処理**: 高度なRAGパイプラインを設定
4. **マルチモーダル**: 画像解析用のビジョンモデルを設定

### スケーリングの考慮事項

- **ロードバランシング**: リバースプロキシの背後に複数のFoundry Localインスタンスを配置
- **モデルルーティング**: ユースケースに応じた異なるモデルを使用
- **リソース管理**: 同時ユーザー向けのGPUメモリ最適化
- **バックアップ戦略**: 会話データと設定の定期的なバックアップ

## 参考資料

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

