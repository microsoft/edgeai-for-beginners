# 環境設定ガイド

## 概要

ワークショップのサンプルは、リポジトリのルートにある`.env`ファイルで環境変数を使用して設定を管理しています。これにより、コードを変更せずに簡単にカスタマイズできます。

## クイックスタート

### 1. 必要条件の確認

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. 環境の設定

`.env`ファイルは既に適切なデフォルト値で設定されています。ほとんどのユーザーは変更する必要がありません。

**オプション**: 設定を確認してカスタマイズする:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. 設定を適用する

**Pythonスクリプトの場合:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**ノートブックの場合:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## 環境変数リファレンス

### コア設定

| 変数 | デフォルト値 | 説明 |
|------|-------------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | サンプルのデフォルトモデル |
| `FOUNDRY_LOCAL_ENDPOINT` | (空) | サービスエンドポイントの上書き |
| `PYTHONPATH` | ワークショップパス | Pythonモジュール検索パス |

**FOUNDRY_LOCAL_ENDPOINTを設定するタイミング:**
- リモートのFoundry Localインスタンス
- カスタムポート設定
- 開発/本番環境の分離

**例:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### セッション固有の変数

#### セッション02: RAGパイプライン
| 変数 | デフォルト値 | 目的 |
|------|-------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 埋め込みモデル |
| `RAG_QUESTION` | 事前設定済み | テスト用質問 |

#### セッション03: ベンチマーク
| 変数 | デフォルト値 | 目的 |
|------|-------------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | ベンチマーク対象モデル |
| `BENCH_ROUNDS` | `3` | モデルごとの反復回数 |
| `BENCH_PROMPT` | 事前設定済み | テスト用プロンプト |
| `BENCH_STREAM` | `0` | 最初のトークンの遅延を測定 |

#### セッション04: モデル比較
| 変数 | デフォルト値 | 目的 |
|------|-------------|------|
| `SLM_ALIAS` | `phi-4-mini` | 小型言語モデル |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型言語モデル |
| `COMPARE_PROMPT` | 事前設定済み | 比較用プロンプト |
| `COMPARE_RETRIES` | `2` | 再試行回数 |

#### セッション05: マルチエージェントオーケストレーション
| 変数 | デフォルト値 | 目的 |
|------|-------------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 研究者エージェントモデル |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | 編集者エージェントモデル |
| `AGENT_QUESTION` | 事前設定済み | テスト用質問 |

### 信頼性設定

| 変数 | デフォルト値 | 目的 |
|------|-------------|------|
| `SHOW_USAGE` | `1` | トークン使用量を表示 |
| `RETRY_ON_FAIL` | `1` | 再試行ロジックを有効化 |
| `RETRY_BACKOFF` | `1.0` | 再試行の遅延時間（秒） |

## 一般的な設定

### 開発環境設定（高速な反復）
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### 本番環境設定（品質重視）
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### ベンチマーク設定
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### マルチエージェント特化
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### リモート開発
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## 推奨モデル

### 用途別

**汎用:**
- `phi-4-mini` - 品質と速度のバランスが良い

**高速応答:**
- `qwen2.5-0.5b` - 非常に高速で分類に適している
- `phi-4-mini` - 高速かつ良好な品質

**高品質:**
- `qwen2.5-7b` - 最高品質、リソース使用量が多い
- `phi-4-mini` - 良好な品質、リソース使用量が少ない

**コード生成:**
- `deepseek-coder-1.3b` - コード専用
- `phi-4-mini` - 汎用的なコーディング

### リソース別

**低リソース（< 8GB RAM）:**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**中リソース（8-16GB RAM）:**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**高リソース（16GB+ RAM）:**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## 高度な設定

### カスタムエンドポイント

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### 温度とサンプリング（コード内で上書き）

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAIハイブリッド設定

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## トラブルシューティング

### 環境変数が読み込まれない

**症状:**
- スクリプトが間違ったモデルを使用する
- 接続エラー
- 変数が認識されない

**解決策:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### サービス接続の問題

**症状:**
- "接続が拒否されました"エラー
- "サービスが利用できません"
- タイムアウトエラー

**解決策:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### モデルが見つからない

**症状:**
- "モデルが見つかりません"エラー
- "エイリアスが認識されません"

**解決策:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### インポートエラー

**症状:**
- "モジュールが見つかりません"エラー

**解決策:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## 設定のテスト

### 環境の読み込み確認

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Foundry Local接続のテスト

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## セキュリティのベストプラクティス

### 1. 秘密情報をコミットしない

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. 別々の.envファイルを使用する

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. APIキーを定期的に更新する

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. 環境固有の設定を使用する

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDKドキュメント

- **メインリポジトリ**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **APIドキュメント**: 最新情報はSDKリポジトリを確認

## 追加リソース

- `QUICK_START.md` - 初期設定ガイド
- `Workshop/samples/*/README.md` - サンプル固有のガイド

---

**最終更新日**: 2025-01-08  
**バージョン**: 2.0  
**SDK**: Foundry Local Python SDK (最新)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->