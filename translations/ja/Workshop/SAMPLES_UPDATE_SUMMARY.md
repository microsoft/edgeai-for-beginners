<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:55:09+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ja"
}
-->
# ワークショップサンプル - Foundry Local SDK更新概要

## 概要

`Workshop/samples`ディレクトリ内のすべてのPythonサンプルが、Foundry Local SDKのベストプラクティスに従い、ワークショップ全体での一貫性を確保するために更新されました。

**日付**: 2025年10月8日  
**対象範囲**: 6つのワークショップセッションにわたる9つのPythonファイル  
**主な焦点**: エラーハンドリング、ドキュメント、SDKパターン、ユーザーエクスペリエンス

---

## 更新されたファイル

### セッション01: はじめに
- ✅ `chat_bootstrap.py` - 基本的なチャットとストリーミングの例

### セッション02: RAGソリューション
- ✅ `rag_pipeline.py` - 埋め込みを使用したRAGの実装
- ✅ `rag_eval_ragas.py` - RAGASメトリクスを使用したRAGの評価

### セッション03: オープンソースモデル
- ✅ `benchmark_oss_models.py` - 複数モデルのベンチマーク

### セッション04: 最先端モデル
- ✅ `model_compare.py` - SLMとLLMの比較

### セッション05: AI駆動エージェント
- ✅ `agents_orchestrator.py` - 複数エージェントの調整

### セッション06: ツールとしてのモデル
- ✅ `models_router.py` - 意図に基づくモデルルーティング
- ✅ `models_pipeline.py` - マルチステップルーティングパイプライン

### サポートインフラストラクチャ
- ✅ `workshop_utils.py` - すでにベストプラクティスに従っているため変更なし

---

## 主な改善点

### 1. エラーハンドリングの強化

**変更前:**
```python
manager, client, model_id = get_client(alias)
```

**変更後:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**メリット:**
- 明確なエラーメッセージによるスムーズなエラーハンドリング
- 問題解決のための具体的なヒント
- スクリプトの適切な終了コード

### 2. インポート管理の改善

**変更前:**
```python
from sentence_transformers import SentenceTransformer
```

**変更後:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**メリット:**
- 依存関係が不足している場合の明確なガイダンス
- 不明瞭なインポートエラーの防止
- ユーザーフレンドリーなインストール手順

### 3. 包括的なドキュメント

**すべてのサンプルに追加:**
- docstring内の環境変数のドキュメント
- SDKリファレンスリンク
- 使用例
- 詳細な関数/パラメータのドキュメント
- IDEサポートを向上させる型ヒント

**例:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. ユーザーへのフィードバックの改善

**情報豊富なログを追加:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**進捗インジケーター:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**構造化された出力:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. 強化されたベンチマーク

**セッション03の改善点:**
- モデルごとのエラーハンドリング（失敗時も継続）
- 詳細な進捗報告
- ウォームアップラウンドの適切な実行
- 最初のトークンの遅延測定サポート
- ステージの明確な分離

### 6. 一貫した型ヒント

**全体に追加:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**メリット:**
- IDEのオートコンプリート機能の向上
- 早期のエラー検出
- 自己文書化コード

### 7. モデルルーターの強化

**セッション06の改善点:**
- 包括的な意図検出ドキュメント
- モデル選択アルゴリズムの説明
- 詳細なルーティングログ
- テスト出力のフォーマット
- バッチテストでのエラー回復

### 8. マルチエージェントのオーケストレーション

**セッション05の改善点:**
- ステージごとの進捗報告
- エージェントごとのエラーハンドリング
- 明確なパイプライン構造
- メモリ管理ドキュメントの改善

---

## テストチェックリスト

### 前提条件
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### 各サンプルのテスト

#### セッション01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### セッション02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### セッション03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### セッション04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### セッション05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### セッション06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## 環境変数リファレンス

### グローバル（すべてのサンプル）
| 変数 | 説明 | デフォルト |
|------|------|------------|
| `FOUNDRY_LOCAL_ALIAS` | 使用するモデルのエイリアス | サンプルごとに異なる |
| `FOUNDRY_LOCAL_ENDPOINT` | サービスエンドポイントの上書き | 自動検出 |
| `SHOW_USAGE` | トークン使用量を表示 | `0` |
| `RETRY_ON_FAIL` | リトライロジックを有効化 | `1` |
| `RETRY_BACKOFF` | リトライ遅延の初期値 | `1.0` |

### サンプル固有
| 変数 | 使用セッション | 説明 |
|------|---------------|------|
| `EMBED_MODEL` | セッション02 | 埋め込みモデル名 |
| `RAG_QUESTION` | セッション02 | RAGのテスト質問 |
| `BENCH_MODELS` | セッション03 | ベンチマーク対象モデル（カンマ区切り） |
| `BENCH_ROUNDS` | セッション03 | ベンチマークラウンド数 |
| `BENCH_PROMPT` | セッション03 | ベンチマーク用テストプロンプト |
| `BENCH_STREAM` | セッション03 | 最初のトークンの遅延を測定 |
| `SLM_ALIAS` | セッション04 | 小型言語モデル |
| `LLM_ALIAS` | セッション04 | 大型言語モデル |
| `COMPARE_PROMPT` | セッション04 | 比較テストプロンプト |
| `AGENT_MODEL_PRIMARY` | セッション05 | 主エージェントモデル |
| `AGENT_MODEL_EDITOR` | セッション05 | 編集エージェントモデル |
| `AGENT_QUESTION` | セッション05 | エージェントのテスト質問 |
| `PIPELINE_TASK` | セッション06 | パイプラインのタスク |

---

## 互換性の変更

**なし** - すべての変更は後方互換性があります。

既存のスクリプトは引き続き動作します。新機能は以下の通りです:
- オプションの環境変数
- 機能を壊さない明確なエラーメッセージ
- 追加のログ（抑制可能）
- 型ヒントの向上（実行時の影響なし）

---

## 実装されたベストプラクティス

### 1. 常にWorkshop Utilsを使用
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. 適切なエラーハンドリングパターン
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. 情報豊富なログ
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. 型ヒント
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. 包括的なdocstring
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. 環境変数サポート
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. 優雅な劣化処理
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## よくある問題と解決策

### 問題: インポートエラー
**解決策:** 不足している依存関係をインストール
```bash
pip install sentence-transformers ragas datasets numpy
```

### 問題: 接続エラー
**解決策:** Foundry Localが稼働していることを確認
```bash
foundry service status
foundry model run phi-4-mini
```

### 問題: モデルが見つからない
**解決策:** 利用可能なモデルを確認
```bash
foundry model ls
foundry model download <alias>
```

### 問題: パフォーマンスが遅い
**解決策:** 小型モデルを使用するか、パラメータを調整
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## 次のステップ

### 1. すべてのサンプルをテスト
上記のテストチェックリストを使用して、すべてのサンプルが正しく動作することを確認してください。

### 2. ドキュメントを更新
- 新しい例を使用してセッションのMarkdownファイルを更新
- メインREADMEにトラブルシューティングセクションを追加
- クイックリファレンスガイドを作成

### 3. 統合テストを作成
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. パフォーマンスベンチマークを追加
エラーハンドリングの改善によるパフォーマンス向上を追跡。

### 5. ユーザーフィードバック
ワークショップ参加者から以下のフィードバックを収集:
- エラーメッセージの明確さ
- ドキュメントの充実度
- 使いやすさ

---

## リソース

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **クイックリファレンス**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **移行ノート**: `Workshop/SDK_MIGRATION_NOTES.md`
- **メインリポジトリ**: https://github.com/microsoft/Foundry-Local

---

## メンテナンス

### 新しいサンプルの追加
新しいサンプルを作成する際は、以下のパターンに従ってください:

1. クライアント管理に`workshop_utils`を使用
2. 包括的なエラーハンドリングを追加
3. 環境変数サポートを含める
4. 型ヒントとdocstringを追加
5. 情報豊富なログを提供
6. docstringに使用例を含める
7. SDKドキュメントへのリンクを追加

### 更新のレビュー
サンプルの更新をレビューする際は、以下を確認してください:
- [ ] すべてのI/O操作でのエラーハンドリング
- [ ] 公開関数の型ヒント
- [ ] 包括的なdocstring
- [ ] 環境変数のドキュメント
- [ ] 情報豊富なユーザーフィードバック
- [ ] SDKリファレンスリンク
- [ ] 一貫したコードスタイル

---

**まとめ**: すべてのワークショップPythonサンプルが、Foundry Local SDKのベストプラクティスに従い、エラーハンドリングの強化、包括的なドキュメント、ユーザーエクスペリエンスの向上を実現しました。既存の機能はそのまま維持され、さらに強化されています。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。