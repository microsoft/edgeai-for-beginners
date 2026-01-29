# Foundry Local を API として利用するサンプル

このサンプルは、Microsoft Foundry Local を OpenAI SDK に依存せずに REST API サービスとして使用する方法を示しています。最大限の制御とカスタマイズを可能にする直接的な HTTP 統合パターンを紹介します。

## 概要

Microsoft の公式 Foundry Local パターンに基づき、このサンプルでは以下を提供します:
- FoundryLocalManager を使用した直接的な REST API 統合
- カスタム HTTP クライアントの実装
- モデル管理とヘルスモニタリング
- ストリーミングおよび非ストリーミングレスポンスの処理
- 実運用向けのエラーハンドリングとリトライロジック

## 前提条件

1. **Foundry Local のインストール**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python の依存関係**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## アーキテクチャ

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 主な機能

### 1. **直接的な HTTP 統合**
- SDK に依存しない純粋な REST API 呼び出し
- カスタム認証とヘッダー
- リクエスト/レスポンス処理の完全な制御

### 2. **モデル管理**
- 動的なモデルのロードとアンロード
- ヘルスモニタリングとステータスチェック
- パフォーマンスメトリクスの収集

### 3. **実運用向けパターン**
- 指数バックオフを用いたリトライメカニズム
- フォールトトレランスのためのサーキットブレーカー
- 包括的なログとモニタリング

### 4. **柔軟なレスポンス処理**
- リアルタイムアプリケーション向けのストリーミングレスポンス
- 高スループットシナリオ向けのバッチ処理
- カスタムレスポンスの解析と検証

## 使用例

### 基本的な API 統合
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### ストリーミング統合
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### ヘルスモニタリング
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## ファイル構造

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local の統合

このサンプルは Microsoft の公式パターンに従っています:

1. **SDK 統合**: サービス管理に `FoundryLocalManager` を使用
2. **REST エンドポイント**: `/v1/chat/completions` などのエンドポイントへの直接呼び出し
3. **認証**: ローカルサービス向けの適切な API キー管理
4. **モデル管理**: カタログリスト、ダウンロード、ロードパターン
5. **エラーハンドリング**: Microsoft 推奨のエラーコードとレスポンス

## 始め方

1. **依存関係のインストール**
   ```bash
   pip install -r requirements.txt
   ```

2. **基本的な例を実行**
   ```bash
   python examples/basic_usage.py
   ```

3. **ストリーミングを試す**
   ```bash
   python examples/streaming.py
   ```

4. **実運用設定**
   ```bash
   python examples/production.py
   ```

## 設定

カスタマイズ用の環境変数:
- `FOUNDRY_MODEL`: 使用するデフォルトモデル (デフォルト: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: リクエストタイムアウト (秒) (デフォルト: 30)
- `FOUNDRY_RETRIES`: リトライ試行回数 (デフォルト: 3)
- `FOUNDRY_LOG_LEVEL`: ログレベル (デフォルト: "INFO")

## ベストプラクティス

1. **接続管理**: HTTP 接続を再利用してパフォーマンスを向上
2. **エラーハンドリング**: 指数バックオフを用いた適切なリトライロジックを実装
3. **リソースモニタリング**: モデルのメモリ使用量とパフォーマンスを追跡
4. **セキュリティ**: ローカルサービスでも適切な認証を使用
5. **テスト**: 単体テストと統合テストの両方を含める

## トラブルシューティング

### よくある問題

**サービスが起動していない**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**モデルのロード問題**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**接続エラー**
- Foundry Local が正しいポートで動作しているか確認
- ファイアウォール設定を確認
- 適切な認証ヘッダーを使用しているか確認

## パフォーマンス最適化

1. **接続プーリング**: 複数のリクエストに対してセッションオブジェクトを使用
2. **非同期操作**: asyncio を活用して並行リクエストを実行
3. **キャッシュ**: 適切な場合にモデルレスポンスをキャッシュ
4. **モニタリング**: レスポンスタイムを追跡し、タイムアウトを調整

## 学習成果

このサンプルを完了すると、以下を理解できます:
- Foundry Local との直接的な REST API 統合
- カスタム HTTP クライアント実装パターン
- 実運用向けのエラーハンドリングとモニタリング
- Microsoft Foundry Local のサービスアーキテクチャ
- ローカル AI サービス向けのパフォーマンス最適化技術

## 次のステップ

- サンプル 08: Windows 11 チャットアプリケーションを探索
- サンプル 09: マルチエージェントオーケストレーションを試す
- サンプル 10: Foundry Local をツール統合として学ぶ

---

