# 初心者向けEdgeAIワークショップ

> **実用的なエッジAIアプリケーションを構築するためのハンズオン学習パス**
>
> Microsoft Foundry Localを使用して、チャット完了からマルチエージェントのオーケストレーションまで、6つの段階的なセッションでローカルAIデプロイメントを習得しましょう。

---

## 🎯 はじめに

**EdgeAI for Beginners Workshop**へようこそ！このワークショップは、理論的なエッジAIの概念を実践的なスキルに変えるためのハンズオンガイドです。Microsoft Foundry LocalとSmall Language Models (SLMs)を使用した段階的な演習を通じて、ローカルハードウェア上で動作するインテリジェントなアプリケーションの構築方法を学びます。

### なぜこのワークショップなのか？

**エッジAI革命が到来**

世界中の組織が、クラウド依存型AIからエッジコンピューティングへと移行しています。その理由は以下の3つです：

1. **プライバシーとコンプライアンス** - 敏感なデータをクラウドに送信せずにローカルで処理（HIPAA、GDPR、金融規制）
2. **パフォーマンス** - ネットワーク遅延を排除（ローカル50-500ms vs クラウド500-2000msの往復）
3. **コスト管理** - トークンごとのAPIコストを削減し、クラウドの費用をかけずにスケール可能

**しかし、エッジAIは異なる**

オンプレミスでAIを実行するには新しいスキルが必要です：
- リソース制約に合わせたモデル選択と最適化
- ローカルサービス管理とハードウェアアクセラレーション
- 小型モデル向けのプロンプトエンジニアリング
- エッジデバイス向けのプロダクションデプロイメントパターン

**このワークショップでそのスキルを習得**

6つの集中セッション（合計約3時間）で、「Hello World」からプロダクション対応のマルチエージェントシステムのデプロイメントまで進みます。すべてローカルマシン上で実行されます。

---

## 📚 学習目標

このワークショップを完了することで、以下のスキルを習得できます：

### コアコンピテンシー
1. **ローカルAIサービスのデプロイと管理**
   - Microsoft Foundry Localのインストールと設定
   - エッジデプロイメントに適したモデルの選択
   - モデルライフサイクルの管理（ダウンロード、ロード、キャッシュ）
   - リソース使用状況の監視とパフォーマンスの最適化

2. **AI搭載アプリケーションの構築**
   - OpenAI互換のチャット完了をローカルで実装
   - Small Language Models向けの効果的なプロンプト設計
   - ストリーミングレスポンスを活用したUX改善
   - ローカルモデルを既存アプリケーションに統合

3. **RAG（Retrieval Augmented Generation）システムの作成**
   - 埋め込みを使用したセマンティック検索の構築
   - LLMレスポンスをドメイン固有の知識に基づかせる
   - 業界標準の指標を使用したRAG品質評価
   - プロトタイプからプロダクションへのスケールアップ

4. **モデルパフォーマンスの最適化**
   - ユースケースに適した複数モデルのベンチマーク
   - レイテンシ、スループット、初回トークン時間の測定
   - スピードと品質のトレードオフに基づく最適モデルの選択
   - 実際のシナリオでのSLMとLLMのトレードオフ比較

5. **マルチエージェントシステムのオーケストレーション**
   - 異なるタスク向けの専門エージェント設計
   - エージェントのメモリとコンテキスト管理の実装
   - 複雑なワークフローでのエージェントの調整
   - 複数モデル間でのリクエストのインテリジェントなルーティング

6. **プロダクション対応ソリューションのデプロイ**
   - エラーハンドリングとリトライロジックの実装
   - トークン使用量とシステムリソースの監視
   - モデルをツールとして活用したスケーラブルなアーキテクチャの構築
   - エッジからハイブリッド（エッジ＋クラウド）への移行計画

---

## 🎓 学習成果

### 構築するもの

ワークショップ終了時には以下を構築しています：

| セッション | 成果物 | 実証スキル |
|------------|--------|------------|
| **1** | ストリーミング対応のチャットアプリケーション | サービスセットアップ、基本的な完了、ストリーミングUX |
| **2** | 評価付きRAGシステム | 埋め込み、セマンティック検索、品質指標 |
| **3** | マルチモデルベンチマークスイート | パフォーマンス測定、モデル比較 |
| **4** | SLMとLLMの比較ツール | トレードオフ分析、最適化戦略 |
| **5** | マルチエージェントオーケストレーター | エージェント設計、メモリ管理、調整 |
| **6** | インテリジェントルーティングシステム | 意図検出、モデル選択、スケーラビリティ |

### コンピテンシーマトリックス

| スキルレベル | セッション1-2 | セッション3-4 | セッション5-6 |
|--------------|---------------|---------------|---------------|
| **初心者** | ✅ セットアップと基礎 | ⚠️ 難しい | ❌ 高度すぎる |
| **中級者** | ✅ 簡単な復習 | ✅ コア学習 | ⚠️ ストレッチ目標 |
| **上級者** | ✅ 簡単に進行 | ✅ 洗練 | ✅ プロダクションパターン |

### キャリア対応スキル

**このワークショップ終了後、以下が可能になります：**

✅ **プライバシー重視のアプリケーション構築**
- PHI/PIIをローカルで処理するヘルスケアアプリ
- コンプライアンス要件を満たす金融サービス
- データ主権が必要な政府システム

✅ **エッジ環境向けの最適化**
- リソースが限られたIoTデバイス
- オフライン優先のモバイルアプリケーション
- 低レイテンシのリアルタイムシステム

✅ **インテリジェントなアーキテクチャ設計**
- 複雑なワークフロー向けのマルチエージェントシステム
- ハイブリッドエッジクラウドデプロイメント
- コスト最適化されたAIインフラ

✅ **エッジAIイニシアチブのリード**
- プロジェクトのエッジAIの実現可能性を評価
- 適切なモデルとフレームワークの選択
- スケーラブルなローカルAIソリューションの設計

---

## 🗺️ ワークショップ構成

### セッション概要（6セッション × 30分 = 3時間）

| セッション | トピック | フォーカス | 所要時間 |
|------------|----------|------------|----------|
| **1** | Foundry Localの始め方 | インストール、検証、初回完了 | 30分 |
| **2** | RAGを活用したAIソリューション構築 | プロンプト設計、埋め込み、評価 | 30分 |
| **3** | オープンソースモデル | モデル発見、ベンチマーク、選択 | 30分 |
| **4** | 最先端モデル | SLM vs LLM、最適化、フレームワーク | 30分 |
| **5** | AI搭載エージェント | エージェント設計、オーケストレーション、メモリ | 30分 |
| **6** | ツールとしてのモデル | ルーティング、チェイニング、スケーリング戦略 | 30分 |

---

## 🚀 クイックスタート

### 必要条件

**システム要件:**
- **OS**: Windows 10/11、macOS 11+、またはLinux (Ubuntu 20.04+)
- **RAM**: 最低8GB、推奨16GB以上
- **ストレージ**: モデル用に10GB以上の空き容量
- **CPU**: AVX2対応の最新プロセッサ
- **GPU** (オプション): CUDA対応またはQualcomm NPUによるアクセラレーション

**ソフトウェア要件:**
- **Python 3.8+** ([ダウンロード](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([インストールガイド](../../../Workshop))
- **Git** ([ダウンロード](https://git-scm.com/downloads))
- **Visual Studio Code** (推奨) ([ダウンロード](https://code.visualstudio.com/))

### 3ステップでセットアップ

#### 1. Foundry Localをインストール

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**インストール確認:**
```bash
foundry --version
foundry service status
```

**Azure AI Foundry Localが固定ポートで動作していることを確認**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**動作確認:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**利用可能なモデルの確認**
Foundry Localインスタンスで利用可能なモデルを確認するには、モデルエンドポイントをクエリします：

```bash
# cmd/bash/powershell
foundry model list
```

Webエンドポイントを使用 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. リポジトリをクローンして依存関係をインストール

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. 初回サンプルを実行

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ 成功！** エッジAIに関するストリーミングレスポンスが表示されるはずです。

---

## 📦 ワークショップリソース

### Pythonサンプル

各コンセプトを実証する段階的なハンズオン例：

| セッション | サンプル | 説明 | 実行時間 |
|------------|----------|------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | 基本＆ストリーミングチャット | ~30秒 |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | 埋め込みを使用したRAG | ~45秒 |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG品質評価 | ~60秒 |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | マルチモデルベンチマーク | ~2-3分 |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM比較 | ~45秒 |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | マルチエージェントシステム | ~60秒 |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | 意図に基づくルーティング | ~45秒 |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | マルチステップパイプライン | ~60秒 |

### Jupyterノートブック

説明とビジュアルを含むインタラクティブな探索：

| セッション | ノートブック | 説明 | 難易度 |
|------------|--------------|------|--------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | チャットの基礎＆ストリーミング | ⭐ 初心者 |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAGシステムの構築 | ⭐⭐ 中級 |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG品質の評価 | ⭐⭐ 中級 |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | モデルベンチマーク | ⭐⭐ 中級 |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | モデル比較 | ⭐⭐ 中級 |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | エージェントオーケストレーション | ⭐⭐⭐ 上級 |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | 意図ルーティング | ⭐⭐⭐ 上級 |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | パイプラインオーケストレーション | ⭐⭐⭐ 上級 |

### ドキュメント

包括的なガイドとリファレンス：

| ドキュメント | 説明 | 使用タイミング |
|--------------|------|---------------|
| [QUICK_START.md](./QUICK_START.md) | クイックセットアップガイド | 初めて始めるとき |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | コマンド＆APIチートシート | すぐに答えが必要なとき |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDKパターン＆例 | コードを書くとき |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | 環境変数ガイド | サンプルを設定するとき |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | よくある問題と解決策 | 問題をデバッグするとき |

---

## 🎓 学習パスのおすすめ

### 初心者向け（3-4時間）
1. ✅ セッション1：始め方（セットアップと基本チャットに集中）
2. ✅ セッション2：RAGの基礎（評価は最初はスキップ）
3. ✅ セッション3：簡単なベンチマーク（モデル2つのみ）
4. ⏭️ セッション4-6は一旦スキップ
5. 🔄 最初のアプリケーションを構築した後にセッション4-6に戻る

### 中級開発者向け（3時間）
1. ⚡ セッション1：セットアップの簡単な確認
2. ✅ セッション2：RAGパイプラインを評価付きで完成
3. ✅ セッション3：完全なベンチマークスイート
4. ✅ セッション4：モデル最適化
5. ✅ セッション5-6：アーキテクチャパターンに集中

### 上級者向け（2-3時間）
1. ⚡ セッション1-3：簡単な復習と確認
2. ✅ セッション4：最適化の深掘り
3. ✅ セッション5：マルチエージェントアーキテクチャ
4. ✅ セッション6：プロダクションパターンとスケーリング
5. 🚀 拡張：カスタムルーティングロジックとハイブリッドデプロイメントを構築

---

## ワークショップセッションパック（集中30分ラボ）

凝縮された6セッション形式のワークショップを進める場合、以下の専用ガイドを使用してください（各ガイドは上記のモジュールドキュメントを補完します）：

| ワークショップセッション | ガイド | コアフォーカス |
|--------------------------|--------|----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | インストール、検証、phi & GPT-OSS-20Bの実行、アクセラレーション |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | プロンプト設計、RAGパターン、CSV＆ドキュメントの基盤化、移行 |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face統合、ベンチマーク、モデル選択 |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM、WebGPU、Chainlit RAG、
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Azureへのルーティング、チェーン、スケーリングパス |

各セッションファイルには以下が含まれます：概要、学習目標、30分のデモフロー、スタータープロジェクト、検証チェックリスト、トラブルシューティング、公式Foundry Local Python SDKへの参照。

### サンプルスクリプト

ワークショップ依存関係のインストール（Windows）:

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Foundry LocalサービスをmacOSから異なる（Windows）マシンやVMで実行する場合、エンドポイントをエクスポート:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| セッション | スクリプト | 説明 |
|-----------|------------|------|
| 1 | `samples/session01/chat_bootstrap.py` | サービスのブートストラップとストリーミングチャット |
| 2 | `samples/session02/rag_pipeline.py` | 最小限のRAG（インメモリ埋め込み） |
|   | `samples/session02/rag_eval_ragas.py` | RAG評価（ragasメトリクス使用） |
| 3 | `samples/session03/benchmark_oss_models.py` | 複数モデルのレイテンシとスループットベンチマーク |
| 4 | `samples/session04/model_compare.py` | SLMとLLMの比較（レイテンシとサンプル出力） |
| 5 | `samples/session05/agents_orchestrator.py` | 2エージェントの研究→編集パイプライン |
| 6 | `samples/session06/models_router.py` | 意図ベースのルーティングデモ |
|   | `samples/session06/models_pipeline.py` | 複数ステップの計画/実行/改良チェーン |

### 環境変数（サンプル共通）

| 変数 | 目的 | 例 |
|------|------|----|
| `FOUNDRY_LOCAL_ALIAS` | 基本サンプル用のデフォルト単一モデルエイリアス | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | 比較用の明示的SLMと大規模モデル | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | ベンチマークするエイリアスのカンマ区切りリスト | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | モデルごとのベンチマーク繰り返し回数 | `3` |
| `BENCH_PROMPT` | ベンチマークで使用するプロンプト | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers埋め込みモデル | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | RAGパイプラインのテストクエリを上書き | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | エージェントパイプラインクエリを上書き | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | 研究エージェント用モデルエイリアス | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | 編集エージェント用モデルエイリアス（異なる可能性あり） | `gpt-oss-20b` |
| `SHOW_USAGE` | `1`の場合、完了ごとにトークン使用量を表示 | `1` |
| `RETRY_ON_FAIL` | `1`の場合、一時的なチャットエラーで1回再試行 | `1` |
| `RETRY_BACKOFF` | 再試行前に待機する秒数 | `1.0` |

変数が設定されていない場合、スクリプトは適切なデフォルト値にフォールバックします。単一モデルデモでは通常、`FOUNDRY_LOCAL_ALIAS`のみが必要です。

### ユーティリティモジュール

すべてのサンプルは共通のヘルパー`samples/workshop_utils.py`を共有し、以下を提供します：

* キャッシュされた`FoundryLocalManager` + OpenAIクライアントの作成
* 再試行と使用量表示オプション付き`chat_once()`ヘルパー
* シンプルなトークン使用量レポート（`SHOW_USAGE=1`で有効化）

これにより重複が削減され、効率的なローカルモデルオーケストレーションのベストプラクティスが強調されます。

## オプションの拡張機能（セッション間）

| テーマ | 拡張機能 | セッション | 環境変数 / トグル |
|-------|----------|------------|------------------|
| 決定論 | 固定温度 + 安定したプロンプトセット | 1–6 | `temperature=0`, `top_p=1`を設定 |
| トークン使用量の可視化 | 一貫したコスト/効率の教育 | 1–6 | `SHOW_USAGE=1` |
| ストリーミング最初のトークン | 知覚レイテンシメトリクス | 1,3,4,6 | `BENCH_STREAM=1`（ベンチマーク） |
| 再試行の耐性 | 一時的なコールドスタートを処理 | 全て | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| 複数モデルエージェント | 異種役割の専門化 | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| 適応型ルーティング | 意図 + コストヒューリスティクス | 6 | ルーターを拡張してエスカレーションロジックを追加 |
| ベクトルメモリ | 長期的なセマンティックリコール | 2,5,6 | FAISS/Chroma埋め込みインデックスを統合 |
| トレースエクスポート | 監査と評価 | 2,5,6 | ステップごとにJSONラインを追加 |
| 品質ルーブリック | 定性的な追跡 | 3–6 | 二次スコアリングプロンプト |
| スモークテスト | ワークショップ前の簡易検証 | 全て | `python Workshop/tests/smoke.py` |

### 決定論的クイックスタート

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

同一入力を繰り返しても安定したトークン数を期待できます。

### RAG評価（セッション2）

`rag_eval_ragas.py`を使用して、小規模な合成データセットで回答の関連性、忠実性、コンテキスト精度を計算します：

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

質問、コンテキスト、正解の大規模なJSONLを提供し、Hugging Faceの`Dataset`に変換して拡張します。

## CLIコマンド精度付録

ワークショップでは、現在文書化されている安定したFoundry Local CLIコマンドのみを使用します。

### 参照された安定コマンド

| カテゴリ | コマンド | 目的 |
|----------|---------|------|
| コア | `foundry --version` | インストールされたバージョンを表示 |
| サービス | `foundry service start` | ローカルサービスを開始（自動でない場合） |
| サービス | `foundry service status` | サービスステータスを表示 |
| モデル | `foundry model list` | カタログ / 利用可能なモデルをリスト表示 |
| モデル | `foundry model download <alias>` | モデルの重みをキャッシュにダウンロード |
| モデル | `foundry model run <alias>` | モデルをローカルで起動（ロード）; `--prompt`と組み合わせてワンショット実行 |
| モデル | `foundry model unload <alias>` / `foundry model stop <alias>` | メモリからモデルをアンロード（サポートされている場合） |
| キャッシュ | `foundry cache list` | キャッシュされた（ダウンロード済み）モデルをリスト表示 |

### ワンショットプロンプトパターン

非推奨の`model chat`サブコマンドの代わりに以下を使用：

```powershell
foundry model run <alias> --prompt "Your question here"
```

これにより、単一のプロンプト/レスポンスサイクルが実行され、終了します。

### 削除された / 避けるべきパターン

| 非推奨 / 未文書 | 推奨 / ガイダンス |
|-----------------|------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | 通常の`foundry model list` + 最近のアクティビティ / ログを使用 |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | ベンチマークPythonスクリプト + OSツール（タスクマネージャー / `nvidia-smi`）を使用 |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### ベンチマークとテレメトリ

- レイテンシ、p95、トークン/秒: `samples/session03/benchmark_oss_models.py`
- 最初のトークンレイテンシ（ストリーミング）: `BENCH_STREAM=1`を設定
- リソース使用量: OSモニター（タスクマネージャー、アクティビティモニター、`nvidia-smi`）。

新しいCLIテレメトリコマンドが上流で安定化した場合、セッションマークダウンに最小限の編集で組み込むことができます。

### 自動リントガード

自動リントツールが、マークダウンファイルのコードブロック内で非推奨のCLIパターンの再導入を防ぎます：

スクリプト: `Workshop/scripts/lint_markdown_cli.py`

非推奨パターンはコードフェンス内でブロックされます。

推奨される置き換え:
| 非推奨 | 推奨 |
|--------|------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | ベンチマークスクリプト + システムツール |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

ローカルで実行:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml`が各プッシュとPRで実行されます。

オプションのプリコミットフック:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## クイックCLI → SDK移行表

| タスク | CLIワンライナー | SDK（Python）相当 | 備考 |
|-------|----------------|------------------|------|
| モデルを一度実行（プロンプト） | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDKはサービスとキャッシュを自動的にブートストラップ |
| モデルをダウンロード（キャッシュ） | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | エイリアスが複数のビルドにマッピングされる場合、マネージャーが最適なバリアントを選択 |
| カタログをリスト表示 | `foundry model list` | `# use manager for each alias or maintain known list` | CLIは集約; SDKは現在エイリアスごとのインスタンス化 |
| キャッシュされたモデルをリスト表示 | `foundry cache list` | `manager.list_cached_models()` | マネージャー初期化後（任意のエイリアス） |
| エンドポイントURLを取得 | （暗黙的） | `manager.endpoint` | OpenAI互換クライアントを作成するために使用 |
| モデルをウォームアップ | `foundry model run <alias>`その後最初のプロンプト | `chat_once(alias, messages=[...])`（ユーティリティ） | ユーティリティは初期コールドレイテンシウォームアップを処理 |
| レイテンシを測定 | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models`（または新しいエクスポータースクリプト） | 一貫したメトリクスのためにスクリプトを推奨 |
| モデルを停止 / アンロード | `foundry model unload <alias>` | （公開されていない – サービス / プロセスを再起動） | ワークショップフローでは通常不要 |
| トークン使用量を取得 | （出力を表示） | `resp.usage.total_tokens` | バックエンドが使用量オブジェクトを返す場合に提供 |

## ベンチマークマークダウンエクスポート

スクリプト`Workshop/scripts/export_benchmark_markdown.py`を使用して新しいベンチマークを実行（`samples/session03/benchmark_oss_models.py`と同じロジック）、GitHubフレンドリーなマークダウンテーブルと生のJSONを生成します。

### 例

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

生成されたファイル:
| ファイル | 内容 |
|---------|------|
| `benchmark_report.md` | マークダウンテーブル + 解釈のヒント |
| `benchmark_report.json` | 生のメトリクス配列（差分 / トレンド追跡用） |

環境で`BENCH_STREAM=1`を設定すると、サポートされている場合は最初のトークンレイテンシが含まれます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->