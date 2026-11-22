# ワークショップノートブック

> **ハンズオンで学ぶエッジAIのインタラクティブなJupyterノートブック**
>
> Microsoft Foundry LocalとSmall Language Modelsを使用し、基本的なチャット完了から高度なマルチエージェントシステムまで段階的に学べる自己ペース型チュートリアル。

---

## 📖 はじめに

**EdgeAI for Beginners Workshop Notebooks** コレクションへようこそ。これらのインタラクティブなJupyterノートブックは、リアルタイムでコードを記述、実行、実験しながらエッジAIを学べるハンズオン体験を提供します。

### なぜJupyterノートブックなのか？

従来のチュートリアルとは異なり、これらのノートブックは以下を提供します：

- <strong>インタラクティブな学習</strong>: コードセルを実行し、即時結果を確認
- <strong>実験</strong>: パラメーターを変更しリアルタイムで変化を観察
- <strong>ドキュメンテーション</strong>: インラインの説明とマークダウンセルで概念を案内
- <strong>再現性</strong>: 参照・再利用可能な完全な動作例
- <strong>可視化</strong>: パフォーマンス指標、埋め込み、結果をインラインで表示

### これらのノートブックの特長は何か？

各ノートブックは<strong>実運用レベルのベストプラクティス</strong>に基づき設計されています：

✅ <strong>包括的なエラーハンドリング</strong> - 優雅なフォールバックとわかりやすいエラーメッセージ  
✅ **型ヒント＆ドキュメント** - 明確な関数シグネチャとドックストリング  
✅ <strong>パフォーマンス監視</strong> - トークン使用量の追跡とレイテンシ計測  
✅ <strong>モジュラー設計</strong> - プロジェクトに適応可能な再利用パターン  
✅ <strong>段階的な複雑さ</strong> - 前回の内容に体系的に発展

---

## 🎯 学習目標

### 習得するコアスキル

これらのノートブックを通じて以下をマスターします：

1. **ローカルAIサービス管理**
   - Microsoft Foundry Localサービスの設定と管理
   - ハードウェアに適したモデルの選択と読み込み
   - リソース使用の監視とパフォーマンス最適化
   - サービス検出とヘルスチェックの対応

2. **AIアプリケーション開発**
   - OpenAI互換チャット完了機能のローカル実装
   - ユーザー体験向上のためのストリーミングインターフェース構築
   - Small Language Models用の効果的なプロンプト設計
   - ローカルモデルのアプリケーション統合

3. **Retrieval Augmented Generation (RAG)**
   - ベクトル埋め込みによるセマンティック検索の作成
   - ドメイン固有文書に基づくLLM応答の実現
   - RAGの品質をRAGAS指標で評価
   - プロトタイプから本番環境へのスケールアップ

4. <strong>パフォーマンス最適化</strong>
   - 複数モデルを体系的にベンチマーク
   - レイテンシ、スループット、ファーストトークン時間の計測
   - Small Language ModelsとLarge Language Modelsの比較
   - パフォーマンス／品質のトレードオフによる最適モデル選択

5. <strong>マルチエージェントオーケストレーション</strong>
   - タスク別の専門エージェント設計
   - エージェントのメモリとコンテキスト管理実装
   - 複雑なワークフローでのエージェント間調整
   - エージェント協業のコーディネーターパターン構築

6. <strong>インテリジェントモデルルーティング</strong>
   - インテント検出とパターンマッチングの実装
   - クエリを適切なモデルに自動ルーティング
   - 複数ステップのパイプライン構築（計画→実行→改善）
   - スケーラブルなモデルアズツールアーキテクチャ設計

---

## 🎓 学習成果

### 何を作るか

| ノートブック | 成果物 | 習得スキル | 難易度 |
|----------|-------------|---------------------|------------|
| **セッション01** | ストリーミング対応チャットアプリ | サービスセットアップ、基本完了、ストリーミングUX | ⭐ 初心者 |
| **セッション02 (RAG)** | 評価付きRAGパイプライン | 埋め込み、セマンティック検索、品質指標 | ⭐⭐ 中級 |
| **セッション02 (Eval)** | RAG品質評価器 | RAGAS指標、体系的評価 | ⭐⭐ 中級 |
| **セッション03** | マルチモデルベンチマーク | パフォーマンス計測、モデル比較 | ⭐⭐ 中級 |
| **セッション04** | SLM vs LLM比較ツール | トレードオフ分析、最適化戦略 | ⭐⭐⭐ 上級 |
| **セッション05** | マルチエージェントオーケストレーター | エージェント設計、メモリ、調整 | ⭐⭐⭐ 上級 |
| **セッション06 (ルーター)** | インテリジェントルーティングシステム | インテント検出、モデル選択 | ⭐⭐⭐ 上級 |
| **セッション06 (パイプライン)** | 多段パイプライン | 計画／実行／改善ワークフロー | ⭐⭐⭐ 上級 |

### コンピテンシーの進展

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 ワークショップスケジュール

### 🚀 半日ワークショップ（3.5時間）

**対象：チームトレーニング、ハッカソン、カンファレンスワークショップに最適**

| 時間 | 所要時間 | セッション | トピック | 活動内容 |
|------|----------|---------|--------|------------|
| **0:00** | 30分 | セットアップ＆イントロ | 環境構築、Foundry Localインストール | 依存関係インストール、セットアップ確認 |
| **0:30** | 30分 | セッション01 | 基本チャット完了、ストリーミング | ノートブック実行、プロンプト変更 |
| **1:00** | 45分 | セッション02 | RAGパイプライン、埋め込み、評価 | RAGシステム構築、クエリテスト |
| **1:45** | 15分 | 休憩 | ☕ コーヒー＆質問対応 | — |
| **2:00** | 30分 | セッション03 | マルチモデルベンチマーク | 3モデル以上比較 |
| **2:30** | 30分 | セッション04 | SLM vs LLMトレードオフ | パフォーマンス／品質分析 |
| **3:00** | 30分 | セッション05-06 | マルチエージェント＆ルーティング | 高度パターン探求 |

<strong>成果物</strong>：参加者は6つの動作するエッジAIアプリケーションと実運用レベルのコードパターンを習得して終了。

---

### 🎓 全日ワークショップ（6時間）

**対象：深堀りトレーニング、ブートキャンプ、大学講義に最適**

| 時間 | 所要時間 | セッション | トピック | 活動内容 |
|------|----------|---------|--------|------------|
| **0:00** | 45分 | セットアップ＆理論 | 環境構築、エッジAI基礎 | インストール、確認、ユースケース議論 |
| **0:45** | 45分 | セッション01 | チャット完了の詳細 | 基本＆ストリーミングチャット実装 |
| **1:30** | 30分 | 休憩 | ☕ コーヒー＆ネットワーキング | — |
| **2:00** | 60分 | セッション02 (両方) | RAGパイプライン＋RAGAS評価 | 完全なRAGシステム構築 |
| **3:00** | 30分 | ハンズオン演習1 | 独自ドメインのカスタムRAG | 自分の文書に適用 |
| **3:30** | 30分 | 昼食 | 🍽️ | — |
| **4:00** | 45分 | セッション03 | ベンチマーク方法論 | 体系的なモデル比較 |
| **4:45** | 45分 | セッション04 | 最適化戦略 | SLM vs LLM分析 |
| **5:30** | 60分 | セッション05-06 | 高度なオーケストレーション | マルチエージェントシステム、ルーティング |
| **6:30** | 30分 | ハンズオン演習2 | カスタムエージェント構築 | 自分のオーケストレーター設計 |

<strong>成果物</strong>：エッジAIパターンの深い理解と2つのカスタムプロジェクト

---

### 📚 自己学習（2週間）

**対象：個人学習者、オンラインコース、自主学習に最適**

#### 1週目：基礎（6時間）

| 曜日 | フォーカス | 所要時間 | ノートブック | 宿題 |
|-----|-------|----------|-----------|----------|
| <strong>月曜</strong> | セットアップ＆基礎 | 1.5時間 | セッション01 | プロンプト修正、ストリーミング確認 |
| <strong>水曜</strong> | RAG基礎 | 2時間 | セッション02（両方） | 自身の文書追加 |
| <strong>金曜</strong> | ベンチマーク | 1.5時間 | セッション03 | 追加モデル比較 |
| <strong>土曜</strong> | 復習＆演習 | 1時間 | 1週目全体 | 演習完了、デバッグ |

#### 2週目：応用（5時間）

| 曜日 | フォーカス | 所要時間 | ノートブック | 宿題 |
|-----|-------|----------|-----------|----------|
| <strong>月曜</strong> | 最適化 | 1.5時間 | セッション04 | トレードオフ文書化 |
| <strong>水曜</strong> | マルチエージェントシステム | 2時間 | セッション05 | カスタムエージェント設計 |
| <strong>金曜</strong> | インテリジェントルーティング | 1.5時間 | セッション06（両方） | ルーティングロジック構築 |
| <strong>土曜</strong> | 最終プロジェクト | 2時間 | 統合 | 複数パターン結合 |

<strong>成果物</strong>：エッジAIパターンの習得およびポートフォリオプロジェクト完成

---

## 📔 ノートブック詳細

### 📘 セッション01：チャットブートストラップ
<strong>ファイル</strong>: `session01_chat_bootstrap.ipynb`  
<strong>所要時間</strong>: 20〜30分  
<strong>前提条件</strong>: なし  
<strong>難易度</strong>: ⭐ 初心者

<strong>学習内容</strong>:
- Foundry Local Python SDKのインストールと設定
- `FoundryLocalManager`を使った自動サービス検出
- OpenAI互換APIでの基本チャット完了の実装
- ユーザー体験向上のためのストリーミング応答の構築
- エラーやサービス停止時の優雅な対応

<strong>主要概念</strong>: サービス管理、チャット完了、ストリーミング、エラーハンドリング

<strong>作るもの</strong>: ストリーミング対応のインタラクティブチャットアプリケーション

---

### 📗 セッション02：RAGパイプライン
<strong>ファイル</strong>: `session02_rag_pipeline.ipynb`  
<strong>所要時間</strong>: 30〜45分  
<strong>前提条件</strong>: セッション01  
<strong>難易度</strong>: ⭐⭐ 中級

<strong>学習内容</strong>:
- Retrieval Augmented Generation (RAG)パターンの実装
- sentence-transformersでベクトル埋め込みを作成
- コサイン類似度によるセマンティック検索の構築
- ドメイン文書に基づくLLM応答の実現
- インポートガードによるオプション依存の管理

<strong>主要概念</strong>: RAGアーキテクチャ、埋め込み、セマンティック検索、ベクトル類似度

<strong>作るもの</strong>: 文書に基づく質問応答システム

---

### 📗 セッション02：RAG評価（RAGAS使用）
<strong>ファイル</strong>: `session02_rag_eval_ragas.ipynb`  
<strong>所要時間</strong>: 30〜45分  
<strong>前提条件</strong>: セッション02 RAGパイプライン  
<strong>難易度</strong>: ⭐⭐ 中級

<strong>学習内容</strong>:
- 業界標準の指標を用いたRAG品質評価
- コンテキスト関連性、回答関連性、忠実度の計測
- RAGASフレームワークによる体系的評価
- RAG品質問題の検出と修正
- ドメイン専用の評価データセット構築

<strong>主要概念</strong>: RAG評価、RAGAS指標、品質計測、体系的テスト

<strong>作るもの</strong>: RAG品質評価フレームワーク

---

### 📙 セッション03：OSSモデルベンチマーク
<strong>ファイル</strong>: `session03_benchmark_oss_models.ipynb`  
<strong>所要時間</strong>: 30〜45分  
<strong>前提条件</strong>: セッション01  
<strong>難易度</strong>: ⭐⭐ 中級

<strong>学習内容</strong>:
- 複数モデルを体系的にベンチマーク
- レイテンシ、スループット、ファーストトークン時間を計測
- モデル障害時の優雅なフォールバック実装
- モデルファミリー間のパフォーマンス比較
- ベンチマーク結果の可視化と分析

<strong>主要概念</strong>: パフォーマンスベンチマーク、レイテンシ計測、モデル比較、統計分析

<strong>作るもの</strong>: マルチモデルベンチマークスイート

---

### 📙 セッション04：モデル比較（SLM vs LLM）
<strong>ファイル</strong>: `session04_model_compare.ipynb`  
<strong>所要時間</strong>: 30〜45分  
<strong>前提条件</strong>: セッション01、03  
<strong>難易度</strong>: ⭐⭐⭐ 上級

<strong>学習内容</strong>:
- Small Language ModelsとLarge Language Modelsの比較
- パフォーマンスと品質のトレードオフ分析
- エッジ適合性指標の計測
- 展開制約に基づく最適モデル選択
- モデル選択の意思決定基準文書化

<strong>主要概念</strong>: モデル選択、トレードオフ分析、最適化戦略、展開計画

<strong>作るもの</strong>: SLM vs LLM比較フレームワーク

---

### 📕 セッション05：マルチエージェントオーケストレーター
<strong>ファイル</strong>: `session05_agents_orchestrator.ipynb`  
<strong>所要時間</strong>: 45〜60分  
<strong>前提条件</strong>: セッション01-02  
<strong>難易度</strong>: ⭐⭐⭐ 上級

<strong>学習内容</strong>:
- タスク別の専門エージェント設計
- エージェントメモリとコンテキスト管理の実装
- エージェント協業のコーディネーターパターン構築
- エージェント間通信と引き継ぎの対応
- マルチエージェントシステムのパフォーマンス監視

<strong>主要概念</strong>: エージェントアーキテクチャ、コーディネーターパターン、メモリ管理、エージェントオーケストレーション

<strong>作るもの</strong>: コーディネーターと専門家によるマルチエージェントシステム

---

### 📕 セッション06：モデルルーター
<strong>ファイル</strong>: `session06_models_router.ipynb`  
<strong>所要時間</strong>: 30〜45分  
<strong>前提条件</strong>: セッション01、03  
<strong>難易度</strong>: ⭐⭐⭐ 上級

<strong>学習内容</strong>:
- インテント検出とパターンマッチングの実装
- キーワードベースのモデルルーティング構築
- クエリを適切なモデルに自動ルーティング
- マルチモデルレジストリの設定
- ルーティング判断とパフォーマンス監視

<strong>主要概念</strong>: インテント検出、モデルルーティング、パターンマッチング、インテリジェント選択

<strong>作るもの</strong>: インテリジェントモデルルーティングシステム

---

### 📕 セッション06：多段パイプライン
<strong>ファイル</strong>: `session06_models_pipeline.ipynb`  
<strong>所要時間</strong>: 30〜45分  
<strong>前提条件</strong>: セッション01、06ルーター  
<strong>難易度</strong>: ⭐⭐⭐ 上級

<strong>学習内容</strong>:
- 多段AIパイプラインの構築（計画 → 実行 → 改善）
- インテリジェントモデル選択のためのルーター統合
- パイプラインのエラーハンドリングとリカバリー実装
- パイプラインのパフォーマンスと各段階の監視
- スケーラブルなモデルアズツールアーキテクチャ設計


<strong>主要概念</strong>: パイプラインアーキテクチャ、マルチステージ処理、エラー回復、スケーラビリティパターン

<strong>構築するもの</strong>: ルーティングを備えたマルチステップインテリジェントパイプライン

---

## 🚀 はじめに

### 前提条件

<strong>システム要件</strong>:
- **OS**: Windows 10/11、macOS 11以降、またはLinux（Ubuntu 20.04以降）
- **RAM**: 最低8GB、推奨16GB以上
- <strong>ストレージ</strong>: モデル用に10GB以上の空き容量
- <strong>ハードウェア</strong>: AVX2対応CPU; GPU（CUDA、Qualcomm NPU）はオプション

<strong>ソフトウェア要件</strong>:
- **Python 3.8以上** およびpip
- **Jupyter Notebook** または **VS Code** のJupyter拡張機能
- **Microsoft Foundry Local** のインストールと構成
- **Git**（リポジトリのクローン用）

### インストール手順

#### 1. Foundry Localのインストール

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

<strong>インストール確認</strong>:
```bash
foundry --version
```

#### 2. Python環境のセットアップ

```bash
# Workshopディレクトリに移動する
cd Workshop

# 仮想環境を作成する
python -m venv .venv

# 仮想環境を有効化する
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 依存関係をインストールする
pip install -r requirements.txt
```

#### 3. Foundry Localの起動

```bash
# モデルをロードする（必要に応じて自動ダウンロード）
foundry model run phi-4-mini

# サービスが稼働していることを確認する
foundry service status
```

#### 4. Jupyterの起動

```bash
# Jupyter Notebookを起動します
jupyter notebook notebooks/

# またはJupyter拡張機能を使ってVS Codeを利用します
code notebooks/
```

### クイック検証

設定を確認するためにPythonセルでこれを実行してください:

```python
from foundry_local import FoundryLocalManager
import openai

# マネージャーを初期化する（サービスを自動検出）
manager = FoundryLocalManager("phi-4-mini")

# OpenAIクライアントを設定する
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# チャット完了をテストする
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

<strong>期待される出力</strong>: ローカルモデルからの挨拶応答。

---

## 📝 ワークショップのベストプラクティス

### 講師向け

<strong>ワークショップ前</strong>:
- ✅ インストール手順を1週間前に送付
- ✅ 対象ハードウェアで全ノートブックをテスト
- ✅ 一般的な問題に対するトラブルシューティングガイドの準備
- ✅ バックアップモデルを用意（phi-4-miniが失敗した場合はphi-3.5-mini）
- ✅ 質問用の共有チャットチャンネル設定

<strong>ワークショップ中</strong>:
- ✅ 簡単な環境チェックから開始（5分）
- ✅ すぐにトラブルシューティング資料を共有
- ✅ 実験や修正を奨励
- ✅ 休憩を戦略的に活用（2セッションごと）
- ✅ 1対1サポートのためTAを用意

<strong>ワークショップ後</strong>:
- ✅ 完全な動作ノートブックと解答を共有
- ✅ 追加リソースのリンクを提供
- ✅ 改善のためのフィードバック調査を作成
- ✅ フォローアップ質問のためのオフィスアワーを提供

### 受講者向け

<strong>学習効果を最大化するには</strong>:
- ✅ ワークショップ開始前にセットアップを完了
- ✅ すべてのコードセルを自分で実行（単に読むだけでなく）
- ✅ パラメーターやプロンプトを試す
- ✅ 気付いた点や注意点をメモ
- ✅ 詰まったら質問（他の人も同じ疑問を持っている可能性が高い）

<strong>避けるべきよくある失敗</strong>:
- ❌ セルの実行順序を無視（順番に実行すること）
- ❌ エラーメッセージをよく読まない
- ❌ 理解せずに急いで進める
- ❌ マークダウンの説明を無視する
- ❌ 修正したノートブックを保存しない

<strong>デバッグのヒント</strong>:
1. <strong>サービスが起動していない場合</strong>: `foundry service status`を確認
2. <strong>インポートエラー</strong>: 仮想環境がアクティブか確認
3. <strong>モデルが見つからない場合</strong>: `foundry model ls`でロード済みモデルを確認
4. <strong>動作が遅い場合</strong>: RAM使用量を確認し、他のアプリを閉じる
5. <strong>予期しない結果</strong>: カーネルを再起動し、すべてのセルを上から実行

---

## 🔗 追加リソース

### ワークショップ教材

- **[Workshop Main Guide](../Readme.md)** - 概要、学習目標、キャリア成果
- **[Python Samples](../../../../Workshop/samples)** - 各セッション対応のPythonスクリプト
- **[Session Guides](../../../../Workshop)** - 詳細なマークダウンガイド（Session01-06）
- **[Scripts](../../../../Workshop/scripts)** - バリデーションおよびテスト用ユーティリティ
- **[Troubleshooting](./TROUBLESHOOTING.md)** - 一般的な問題と解決策
- **[Quick Start](./quickstart.md)** - スタートアップガイドの速習版

### ドキュメント

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Microsoft公式ドキュメント
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDKリファレンス
- **[Sentence Transformers](https://www.sbert.net/)** - 埋め込みモデルのドキュメント
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG評価指標

### コミュニティ

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - 質問やプロジェクト共有
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - リアルタイムコミュニティサポート
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - 技術的Q&A

---

## 🎯 推奨学習パス

### 初心者向けトラック（ここから開始）

1. **Session 01** - チャットブートストラップ
2. **Session 02** - RAGパイプライン
3. **Session 03** - モデルベンチマーク

<strong>所要時間</strong>: 約2時間 | <strong>重点</strong>: 基礎パターン

---

### 中級トラック

1. 初心者トラックを完了
2. **Session 02** - RAG評価
3. **Session 04** - モデル比較

<strong>所要時間</strong>: 約4時間 | <strong>重点</strong>: 品質と最適化

---

### 上級トラック（全ワークショップ）

1. 中級トラックを完了
2. **Session 05** - マルチエージェントオーケストレーター
3. **Session 06** - モデルルーター
4. **Session 06** - マルチステップパイプライン

<strong>所要時間</strong>: 約6時間 | <strong>重点</strong>: 本番環境パターン

---

### カスタムプロジェクトトラック

1. 初心者トラック完了（セッション01-03）
2. 目的に応じていずれかの上級セッションを選択:
   - **RAGアプリ構築？** → セッション02評価
   - **パフォーマンス最適化？** → セッション04比較
   - **複雑なワークフロー？** → セッション05オーケストレーター
   - **スケーラブルなアーキテクチャ？** → セッション06ルーター＋パイプライン

<strong>所要時間</strong>: 約3時間 | <strong>重点</strong>: プロジェクト固有スキル

---

## 📊 成功の指標

進捗をこれらのマイルストーンで追跡:

- [ ] <strong>セットアップ完了</strong> - Foundry Local稼働、全依存関係インストール済み
- [ ] <strong>最初のチャット</strong> - セッション01完了、ストリーミングチャット動作
- [ ] **RAG構築済み** - セッション02完了、文書QAシステム稼働
- [ ] <strong>モデルベンチマーク済み</strong> - セッション03完了、性能データ収集
- [ ] <strong>トレードオフ分析済み</strong> - セッション04完了、モデル選択基準文書化
- [ ] <strong>エージェントオーケストレーション済み</strong> - セッション05完了、マルチエージェントシステム稼働
- [ ] <strong>ルーティング実装済み</strong> - セッション06完了、インテリジェントモデル選択機能
- [ ] <strong>カスタムプロジェクト</strong> - ワークショップパターンを自身のケースに適用

---

## 🤝 貢献について

問題を見つけた場合や提案がある場合は、ぜひ貢献してください！

- <strong>問題報告</strong>: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- <strong>改善提案</strong>: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- <strong>プルリクエスト提出</strong>: [Contributing Guidelines](../../AGENTS.md)に従ってください

---

## 📄 ライセンス

本ワークショップは[EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners)リポジトリの一部であり、[MITライセンス](../../../../LICENSE)の下でライセンスされています。

---

**本番環境対応のEdge AIアプリケーションを構築する準備はできましたか？**  
**[Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb)から始めましょう →**

---

*最終更新日: 2025年10月8日 | ワークショップバージョン: 2.0*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->