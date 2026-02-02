# サンプル 02: OpenAI SDK 統合

Microsoft Foundry Local と Azure OpenAI の両方をサポートし、ストリーミングレスポンスと適切なエラーハンドリングを備えた OpenAI Python SDK の高度な統合をデモンストレーションします。

## 概要

このサンプルでは以下を紹介します：
- Foundry Local と Azure OpenAI のシームレスな切り替え
- ユーザー体験を向上させるストリーミングチャット補完
- FoundryLocalManager SDK の適切な使用方法
- 堅牢なエラーハンドリングとフォールバックメカニズム
- 実運用に適したコードパターン

## 前提条件

- **Foundry Local**: インストール済みで稼働中（ローカル推論用）
- **Python**: OpenAI SDK を含むバージョン 3.8 以上
- **Azure OpenAI**: 有効なエンドポイントと API キー（クラウド推論用）

## インストール

1. **Python 環境のセットアップ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **依存関係のインストール:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local の起動（ローカルモード用）:**
   ```cmd
   foundry model run phi-4-mini
   ```


## 使用シナリオ

### Foundry Local（デフォルト）

**オプション 1: FoundryLocalManager を使用（推奨）**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**オプション 2: 手動設定**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## コードアーキテクチャ

### クライアントファクトリーパターン

このサンプルでは、適切なクライアントを作成するためにファクトリーパターンを使用しています：

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### ストリーミングレスポンス

リアルタイムのレスポンス生成を実現するストリーミングのデモンストレーション：

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## 環境変数

### Foundry Local 設定

| 変数名 | 説明 | デフォルト | 必須 |
|--------|------|-----------|------|
| `MODEL` | 使用するモデルのエイリアス | `phi-4-mini` | いいえ |
| `BASE_URL` | Foundry Local のエンドポイント | `http://localhost:8000` | いいえ |
| `API_KEY` | API キー（ローカルではオプション） | `""` | いいえ |

### Azure OpenAI 設定

| 変数名 | 説明 | デフォルト | 必須 |
|--------|------|-----------|------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI リソースのエンドポイント | - | はい |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API キー | - | はい |
| `AZURE_OPENAI_API_VERSION` | API バージョン | `2024-08-01-preview` | いいえ |
| `MODEL` | Azure デプロイメント名 | `your-deployment-name` | はい |

## 高度な機能

### 自動サービス検出

このサンプルは、環境変数に基づいて適切なサービスを自動的に検出します：

1. **Azure モード**: `AZURE_OPENAI_ENDPOINT` と `AZURE_OPENAI_API_KEY` が設定されている場合
2. **Foundry SDK モード**: Foundry Local SDK が利用可能な場合
3. **手動モード**: 手動設定にフォールバック

### エラーハンドリング

- SDK から手動設定へのスムーズなフォールバック
- トラブルシューティングのための明確なエラーメッセージ
- ネットワーク問題に対する適切な例外処理
- 必須環境変数の検証

## パフォーマンスに関する考慮事項

### ローカル vs クラウドのトレードオフ

**Foundry Local の利点:**
- ✅ API コストなし
- ✅ データプライバシー（データがデバイス外に出ない）
- ✅ 対応モデルでの低遅延
- ✅ オフラインで動作可能

**Azure OpenAI の利点:**
- ✅ 最新の大規模モデルへのアクセス
- ✅ 高スループット
- ✅ ローカル計算リソース不要
- ✅ エンタープライズグレードの SLA

## トラブルシューティング

### よくある問題

1. **"Foundry SDK を使用できません" 警告:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure 認証エラー:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **モデルが利用できない:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### ヘルスチェック

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## 次のステップ

- **サンプル 03**: モデルの検出とベンチマーク
- **サンプル 04**: Chainlit RAG アプリケーションの構築
- **サンプル 05**: マルチエージェントのオーケストレーション
- **サンプル 06**: ツールとしてのモデルルーティング

## 参考資料

- [Azure OpenAI ドキュメント](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK リファレンス](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK ドキュメント](https://github.com/openai/openai-python)
- [ストリーミング補完ガイド](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---

