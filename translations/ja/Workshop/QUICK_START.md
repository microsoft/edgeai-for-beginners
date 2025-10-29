<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T20:51:07+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ja"
}
-->
# ワークショップ クイックスタートガイド

## 前提条件

### 1. Foundry Localのインストール

公式インストールガイドに従ってください:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python依存関係のインストール

ワークショップディレクトリから以下を実行してください:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## ワークショップサンプルの実行

### セッション 01: 基本的なチャット

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**環境変数:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### セッション 02: RAGパイプライン

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**環境変数:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### セッション 02: RAG評価 (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**注意**: `requirements.txt`を使用して追加の依存関係をインストールする必要があります

### セッション 03: ベンチマーク

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**環境変数:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**出力:** レイテンシ、スループット、最初のトークンメトリクスを含むJSON

### セッション 04: モデル比較

```bash
cd Workshop/samples
python -m session04.model_compare
```

**環境変数:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### セッション 05: マルチエージェントオーケストレーション

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**環境変数:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### セッション 06: モデルルーター

```bash
cd Workshop/samples
python -m session06.models_router
```

**ルーティングロジックをテスト**: 複数の意図（コード、要約、分類）

### セッション 06: パイプライン

```bash
python -m session06.models_pipeline
```

**複雑なマルチステップパイプライン**: 計画、実行、改良を含む

## スクリプト

### ベンチマークレポートのエクスポート

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**出力:** Markdownテーブル + JSONメトリクス

### Markdown CLIパターンのLint

```bash
python lint_markdown_cli.py --verbose
```

**目的:** ドキュメント内の非推奨CLIパターンを検出

## テスト

### スモークテスト

```bash
cd Workshop
python -m tests.smoke
```

**テスト内容:** 主要なサンプルの基本機能

## トラブルシューティング

### サービスが実行されていない

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### モジュールインポートエラー

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### 接続エラー

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### モデルが見つからない

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## 環境変数リファレンス

### コア設定
| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `FOUNDRY_LOCAL_ALIAS` | 変動 | 使用するモデルのエイリアス |
| `FOUNDRY_LOCAL_ENDPOINT` | 自動 | サービスエンドポイントを上書き |
| `SHOW_USAGE` | `0` | トークン使用統計を表示 |
| `RETRY_ON_FAIL` | `1` | リトライロジックを有効化 |
| `RETRY_BACKOFF` | `1.0` | 初期リトライ遅延（秒） |

### セッション固有
| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 埋め込みモデル |
| `RAG_QUESTION` | サンプル参照 | RAGテスト質問 |
| `BENCH_MODELS` | 変動 | カンマ区切りのモデル |
| `BENCH_ROUNDS` | `3` | ベンチマークの反復回数 |
| `BENCH_PROMPT` | サンプル参照 | ベンチマークプロンプト |
| `BENCH_STREAM` | `0` | 最初のトークンのレイテンシを測定 |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 主エージェントモデル |
| `AGENT_MODEL_EDITOR` | 主 | エディターエージェントモデル |
| `SLM_ALIAS` | `phi-4-mini` | 小型言語モデル |
| `LLM_ALIAS` | `qwen2.5-7b` | 大型言語モデル |
| `COMPARE_PROMPT` | サンプル参照 | 比較プロンプト |

## 推奨モデル

### 開発とテスト
- **phi-4-mini** - 品質と速度のバランスが良い
- **qwen2.5-0.5b** - 分類に非常に高速
- **gemma-2-2b** - 良好な品質、適度な速度

### 本番環境
- **phi-4-mini** - 汎用目的
- **deepseek-coder-1.3b** - コード生成
- **qwen2.5-7b** - 高品質な応答

## SDKドキュメント

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## ヘルプを得る方法

1. サービスステータスを確認: `foundry service status`  
2. ログを確認: Foundry Localサービスログを確認  
3. SDKドキュメントを確認: https://github.com/microsoft/Foundry-Local  
4. サンプルコードを確認: すべてのサンプルには詳細なドックストリングがあります  

## 次のステップ

1. ワークショップセッションを順番に完了する  
2. 異なるモデルを試す  
3. サンプルを自分のユースケースに合わせて変更する  
4. `SDK_MIGRATION_NOTES.md`を確認して高度なパターンを学ぶ  

---

**最終更新日**: 2025-01-08  
**ワークショップバージョン**: 最新  
**SDK**: Foundry Local Python SDK

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。