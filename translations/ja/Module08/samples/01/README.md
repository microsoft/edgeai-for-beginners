# サンプル 01: OpenAI SDKを使った簡易チャット

Microsoft Foundry Localを使用したローカルAI推論で、OpenAI SDKを活用する方法を示す簡単なチャット例。

## 概要

このサンプルでは以下を示します:
- Foundry LocalとOpenAI Python SDKの使用方法
- Azure OpenAIとFoundry Localの両方の設定を扱う方法
- 適切なエラーハンドリングとフォールバック戦略の実装
- FoundryLocalManagerを使用したサービス管理

## 前提条件

- **Foundry Local**: インストール済みでPATHに設定されていること
- **Python**: バージョン3.8以上
- **モデル**: Foundry Localにロードされたモデル（例: `phi-4-mini`）

## インストール

1. **Python環境のセットアップ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **依存関係のインストール:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Localサービスを開始し、モデルをロード:**
   ```cmd
   foundry model run phi-4-mini
   ```


## 使用方法

### Foundry Local（デフォルト）

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## コードの特徴

### FoundryLocalManagerの統合

このサンプルでは、公式のFoundry Local SDKを使用して適切なサービス管理を行います:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### エラーハンドリング

SDKが利用できない場合のフォールバックを含む堅牢なエラーハンドリング:
- 自動サービス検出
- SDKが利用できない場合の優雅な劣化処理
- トラブルシューティングのための明確なエラーメッセージ

## 環境変数

| 変数 | 説明 | デフォルト | 必須 |
|------|------|------------|------|
| `MODEL` | モデルのエイリアスまたは名前 | `phi-4-mini` | いいえ |
| `BASE_URL` | Foundry LocalのベースURL | `http://localhost:8000` | いいえ |
| `API_KEY` | APIキー（通常ローカルでは不要） | `""` | いいえ |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAIエンドポイント | - | Azureの場合 |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI APIキー | - | Azureの場合 |
| `AZURE_OPENAI_API_VERSION` | Azure APIバージョン | `2024-08-01-preview` | いいえ |

## トラブルシューティング

### よくある問題

1. **「Foundry SDKを使用できません」警告:**
   - Foundry Local SDKをインストール: `pip install foundry-local-sdk`
   - または環境変数を設定して手動で構成

2. **接続拒否:**
   - Foundry Localが実行中か確認: `foundry service status`
   - モデルがロードされているか確認: `foundry service ps`

3. **モデルが見つからない:**
   - 利用可能なモデルを一覧表示: `foundry model list`
   - モデルをロード: `foundry model run phi-4-mini`

### 検証

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## 参考資料

- [Foundry Local ドキュメント](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI互換APIリファレンス](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---

