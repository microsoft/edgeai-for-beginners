<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T20:55:47+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "ja"
}
-->
# ワークショップスクリプト

このディレクトリには、ワークショップ資料の品質と一貫性を維持するための自動化およびサポートスクリプトが含まれています。

## 内容

| ファイル | 目的 |
|---------|------|
| `lint_markdown_cli.py` | Markdownコードフェンスをチェックし、非推奨のFoundry Local CLIコマンドパターンをブロックします。 |
| `export_benchmark_markdown.py` | 複数モデルのレイテンシベンチマークを実行し、Markdown + JSONレポートを生成します。 |

## 1. Markdown CLIパターンリンター

`lint_markdown_cli.py`は、翻訳されていないすべての`.md`ファイルをスキャンし、**コードフェンス内**（``` ... ```）で許可されていないFoundry Local CLIパターンを検出します。情報提供の文章では、歴史的な背景として非推奨コマンドを言及することは可能です。

### 非推奨パターン（コードフェンス内でブロック）

リンターは非推奨のCLIパターンをブロックします。代わりに最新の代替案を使用してください。

### 必須の置き換え
| 非推奨 | 代替案 |
|--------|--------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | ベンチマークスクリプト + システムツール（`Task Manager`, `nvidia-smi`） |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### 終了コード
| コード | 意味 |
|-------|------|
| 0 | 違反なし |
| 1 | 1つ以上の非推奨パターンが検出されました |

### ローカルでの実行
リポジトリのルートから（推奨）:

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### プリコミットフック（オプション）
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
これにより、非推奨パターンを導入するコミットがブロックされます。

### CI統合
GitHub Actionワークフロー（`.github/workflows/markdown-cli-lint.yml`）は、`main`および`Reactor`ブランチへのプッシュやプルリクエストごとにリンターを実行します。失敗したジョブはマージ前に修正する必要があります。

### 新しい非推奨パターンの追加
1. `lint_markdown_cli.py`を開きます。
2. `DEPRECATED`リストにタプル`(regex, suggestion)`を追加します。生文字列を使用し、適切な場所に`\b`の単語境界を含めます。
3. ローカルでリンターを実行して検出を確認します。
4. コミットしてプッシュします。CIが新しいルールを強制します。

追加例:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### 説明的な言及の許可
コードフェンス内のみが強制されるため、非推奨コマンドを説明文で安全に記述できます。フェンス内で対比のために表示する必要がある場合は、三重バックティックを使用しないフェンスブロック（例: インデントまたは引用）を追加するか、擬似形式に書き換えてください。

### 特定ファイルのスキップ（高度な設定）
必要に応じて、レガシー例をリポジトリ外の別ファイルにラップするか、ドラフト中に異なる拡張子で名前を変更します。翻訳されたコピーに対する意図的なスキップは自動的に行われます（`translations`を含むパス）。

### トラブルシューティング
| 問題 | 原因 | 解決策 |
|------|------|-------|
| 更新した行がリンターにフラグされる | 正規表現が広すぎる | 境界（`\b`）やアンカーを追加してパターンを狭める |
| CIが失敗するがローカルでは成功する | Pythonバージョンの違いまたは未コミットの変更 | ローカルで再実行し、作業ツリーがクリーンであることを確認し、ワークフローのPythonバージョン（3.11）を確認する |
| 一時的にバイパスする必要がある | 緊急の修正 | 修正をすぐに適用し、仮のブランチとフォローアップPRを使用することを検討（バイパススイッチの追加は避ける） |

### 根拠
ドキュメントを*現在の*安定したCLIインターフェースに合わせることで、ワークショップの混乱を防ぎ、学習者の混乱を避け、Pythonスクリプトを通じてパフォーマンス測定を集中化し、CLIサブコマンドの分散を防ぎます。

---
ワークショップ品質ツールチェーンの一環として維持されています。改善（例: 自動修正提案やHTMLレポート生成など）については、問題を報告するかPRを提出してください。

## 2. サンプル検証スクリプト

`validate_samples.py`は、すべてのPythonサンプルファイルを検証し、構文、インポート、およびベストプラクティスへの準拠を確認します。

### 使用方法
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### チェック内容
- ✅ Python構文の有効性
- ✅ 必須インポートの存在
- ✅ エラーハンドリングの実装（詳細モード）
- ✅ 型ヒントの使用（詳細モード）
- ✅ 関数のドックストリング（詳細モード）
- ✅ SDK参照リンク（詳細モード）

### 環境変数
- `SKIP_IMPORT_CHECK=1` - インポート検証をスキップ
- `SKIP_SYNTAX_CHECK=1` - 構文検証をスキップ

### 終了コード
- `0` - すべてのサンプルが検証を通過
- `1` - 1つ以上のサンプルが失敗

## 3. サンプルテストランナー

`test_samples.py`は、すべてのサンプルがエラーなく実行できるかどうかを確認するスモークテストを実行します。

### 使用方法
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### 前提条件
- Foundry Localサービスが実行中: `foundry service start`
- モデルがロードされている: `foundry model run phi-4-mini`
- 依存関係がインストールされている: `pip install -r requirements.txt`

### テスト内容
- ✅ サンプルがランタイムエラーなしで実行可能
- ✅ 必要な出力が生成される
- ✅ 失敗時の適切なエラーハンドリング
- ✅ パフォーマンス（実行時間）

### 環境変数
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - テストに使用するモデル
- `TEST_TIMEOUT=30` - サンプルごとのタイムアウト（秒）

### 予期される失敗
オプションの依存関係がインストールされていない場合、一部のテストが失敗する可能性があります（例: `ragas`, `sentence-transformers`）。以下を使用してインストールしてください:
```bash
pip install sentence-transformers ragas datasets
```

### 終了コード
- `0` - すべてのテストが成功
- `1` - 1つ以上のテストが失敗

## 4. ベンチマークMarkdownエクスポーター

スクリプト: `export_benchmark_markdown.py`

モデルセットの再現可能なパフォーマンステーブルを生成します。

### 使用方法
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### 出力
| ファイル | 説明 |
|---------|------|
| `benchmark_report.md` | Markdownテーブル（平均値、p95、トークン/秒、オプションの最初のトークン） |
| `benchmark_report.json` | 差分と履歴用の生データ配列 |

### オプション
| フラグ | 説明 | デフォルト |
|-------|------|-----------|
| `--models` | カンマ区切りのモデルエイリアス | （必須） |
| `--prompt` | 各ラウンドで使用するプロンプト | （必須） |
| `--rounds` | モデルごとのラウンド数 | 3 |
| `--output` | Markdown出力ファイル | `benchmark_report.md` |
| `--json` | JSON出力ファイル | `benchmark_report.json` |
| `--fail-on-empty` | すべてのベンチマークが失敗した場合に非ゼロ終了 | オフ |

環境変数`BENCH_STREAM=1`を設定すると、最初のトークンのレイテンシ測定が追加されます。

### 注意事項
- 一貫性のあるモデルブートストラップとキャッシュのために`workshop_utils`を再利用します。
- 異なる作業ディレクトリから実行する場合、スクリプトは`workshop_utils`を見つけるためにパスフォールバックを試みます。
- GPU比較の場合: 一度実行し、CLI設定でアクセラレーションを有効にして再実行し、JSONを差分比較します。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。