<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:55:28+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ja"
}
-->
# Foundry Local SDK 移行ノート

## 概要

Workshopフォルダ内のすべてのPythonファイルが、公式の[Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local)の最新パターンに従って更新されました。

## 変更点の概要

### コアインフラストラクチャ (`workshop_utils.py`)

#### 機能強化:
- **エンドポイントオーバーライドのサポート**: `FOUNDRY_LOCAL_ENDPOINT`環境変数のサポートを追加
- **エラーハンドリングの改善**: 詳細なエラーメッセージを含む例外処理の改善
- **キャッシュ機能の強化**: マルチエンドポイントシナリオに対応するため、キャッシュキーにエンドポイントを含むよう変更
- **指数バックオフ**: 信頼性向上のため、リトライロジックに指数バックオフを採用
- **型アノテーション**: IDEサポートを向上させるため、包括的な型ヒントを追加

#### 新機能:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### サンプルアプリケーション

#### セッション01: チャットブートストラップ (`chat_bootstrap.py`)
- デフォルトモデルを`phi-3.5-mini`から`phi-4-mini`に更新
- エンドポイントオーバーライドのサポートを追加
- SDKリファレンスを含むドキュメントを強化

#### セッション02: RAGパイプライン (`rag_pipeline.py`)
- デフォルトモデルを`phi-4-mini`に更新
- エンドポイントオーバーライドのサポートを追加
- 環境変数の詳細を含むドキュメントを改善

#### セッション02: RAG評価 (`rag_eval_ragas.py`)
- モデルのデフォルトを更新
- エンドポイント設定を追加
- エラーハンドリングを強化

#### セッション03: ベンチマーク (`benchmark_oss_models.py`)
- デフォルトモデルリストに`phi-4-mini`を追加
- 包括的な環境変数ドキュメントを追加
- 関数ドキュメントを改善
- 全体でエンドポイントオーバーライドのサポートを追加

#### セッション04: モデル比較 (`model_compare.py`)
- デフォルトLLMを`gpt-oss-20b`から`qwen2.5-7b`に更新
- エンドポイント設定を追加
- ドキュメントを強化

#### セッション05: マルチエージェントオーケストレーション (`agents_orchestrator.py`)
- 型ヒントを追加（`str | None`を`Optional[str]`に変更）
- Agentクラスのドキュメントを強化
- エンドポイントオーバーライドのサポートを追加
- 初期化パターンを改善

#### セッション06: モデルルーター (`models_router.py`)
- エンドポイント設定を追加
- 意図検出のドキュメントを強化
- ルーティングロジックのドキュメントを改善

#### セッション06: パイプライン (`models_pipeline.py`)
- 包括的な関数ドキュメントを追加
- ステップごとのドキュメントを改善
- エラーハンドリングを強化

### スクリプト

#### ベンチマークエクスポート (`export_benchmark_markdown.py`)
- エンドポイントオーバーライドのサポートを追加
- デフォルトモデルを更新
- 関数ドキュメントを強化
- エラーハンドリングを改善

#### CLIリンター (`lint_markdown_cli.py`)
- SDKリファレンスリンクを追加
- 使用方法のドキュメントを改善

### テスト

#### スモークテスト (`smoke.py`)
- エンドポイントオーバーライドのサポートを追加
- ドキュメントを強化
- テストケースのドキュメントを改善
- エラーレポートを向上

## 環境変数

すべてのサンプルは以下の環境変数をサポートします:

### コア設定
- `FOUNDRY_LOCAL_ALIAS` - 使用するモデルエイリアス（サンプルによってデフォルト値が異なる）
- `FOUNDRY_LOCAL_ENDPOINT` - サービスエンドポイントのオーバーライド（任意）
- `SHOW_USAGE` - トークン使用統計を表示（デフォルト: "0"）
- `RETRY_ON_FAIL` - リトライロジックを有効化（デフォルト: "1"）
- `RETRY_BACKOFF` - リトライの初期遅延時間（秒）（デフォルト: "1.0"）

### サンプル固有
- `EMBED_MODEL` - RAGサンプル用の埋め込みモデル
- `BENCH_MODELS` - ベンチマーク用のカンマ区切りモデル
- `BENCH_ROUNDS` - ベンチマークラウンド数
- `BENCH_PROMPT` - ベンチマーク用テストプロンプト
- `BENCH_STREAM` - 最初のトークンのレイテンシを測定
- `RAG_QUESTION` - RAGサンプル用テスト質問
- `AGENT_MODEL_PRIMARY` - プライマリエージェントモデル
- `AGENT_MODEL_EDITOR` - エディターエージェントモデル
- `SLM_ALIAS` - 小型言語モデルエイリアス
- `LLM_ALIAS` - 大型言語モデルエイリアス

## 実装されたSDKベストプラクティス

### 1. 適切なクライアント初期化
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. モデル情報の取得
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. エラーハンドリング
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. 指数バックオフを使用したリトライロジック
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. ストリーミングサポート
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## カスタムサンプルの移行ガイド

新しいサンプルを作成する場合や既存のサンプルを更新する場合:

1. **`workshop_utils.py`のヘルパーを使用**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **エンドポイントオーバーライドをサポート**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **包括的なドキュメントを追加**:
   - ドキュメント文字列に環境変数を記載
   - SDKリファレンスリンク
   - 使用例

4. **型ヒントを使用**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **適切なエラーハンドリングを実装**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## テスト

すべてのサンプルは以下でテスト可能です:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDKドキュメントリファレンス

- **メインリポジトリ**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **APIドキュメント**: 最新のAPIドキュメントはSDKリポジトリを確認してください

## 互換性を壊す変更点

### 予期される変更なし
すべての変更は後方互換性があります。更新内容は主に以下を含みます:
- 新しいオプション機能の追加（エンドポイントオーバーライド）
- エラーハンドリングの改善
- ドキュメントの強化
- 推奨される最新モデル名への更新

### オプションの強化
コードを以下のように更新することを検討してください:
- 明示的なエンドポイント制御のための`FOUNDRY_LOCAL_ENDPOINT`
- トークン使用状況の可視化のための`SHOW_USAGE=1`
- 最新のモデルデフォルト（`phi-3.5-mini`ではなく`phi-4-mini`）

## よくある問題と解決策

### 問題: "クライアントの初期化に失敗しました"
**解決策**: Foundry Localサービスが稼働していることを確認してください:
```bash
foundry service start
foundry model run phi-4-mini
```

### 問題: "モデルが見つかりません"
**解決策**: 利用可能なモデルを確認してください:
```bash
foundry model list
```

### 問題: エンドポイント接続エラー
**解決策**: エンドポイントを確認してください:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## 次のステップ

1. **Module08サンプルを更新**: Module08/samplesに同様のパターンを適用
2. **統合テストを追加**: 包括的なテストスイートを作成
3. **パフォーマンスベンチマーク**: 更新前後のパフォーマンスを比較
4. **ドキュメントの更新**: 新しいパターンを含むメインREADMEを更新

## 貢献ガイドライン

新しいサンプルを追加する際には:
1. 一貫性を保つために`workshop_utils.py`を使用
2. 既存のサンプルのパターンに従う
3. 包括的なドキュメント文字列を追加
4. SDKリファレンスリンクを含める
5. エンドポイントオーバーライドをサポート
6. 適切な型ヒントを追加
7. ドキュメント文字列に使用例を含める

## バージョン互換性

これらの更新は以下に互換性があります:
- `foundry-local-sdk` (最新)
- `openai>=1.30.0`
- Python 3.8+

---

**最終更新日**: 2025-01-08  
**管理者**: EdgeAI Workshop Team  
**SDKバージョン**: Foundry Local SDK (最新 0.7.117+67073234e7)

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は責任を負いません。