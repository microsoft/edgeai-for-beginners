# モジュール08：Microsoft Foundry Local実践 - 完全な開発者ツールキット

## 概要

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) は、次世代のエッジAI開発を代表するもので、開発者がAIアプリケーションをローカルで構築、展開、スケールできる強力なツールを提供しながら、Azure AI Foundryとのシームレスな統合を維持します。このモジュールではインストールから高度なエージェント開発まで、Foundry Localの包括的な内容を提供します。

**主要技術:**
- Microsoft Foundry Local CLIおよびSDK
- Azure AI Foundryとの統合
- デバイス上でのモデル推論
- ローカルモデルのキャッシュと最適化
- エージェントベースのアーキテクチャ

## 学習目標

このモジュールを修了すると、以下を達成できます：

- **Foundry Localをマスターする**：Windows 11開発のためのインストール・設定・最適化
- <strong>多様なモデルを展開する</strong>：CLIコマンドでphi、qwen、deepseek、GPTモデルをローカルで実行
- <strong>本番ソリューションを構築する</strong>：高度なプロンプトエンジニアリングとデータ統合によるAIアプリケーション作成
- <strong>オープンソースのエコシステムを活用する</strong>：Hugging Faceモデルやコミュニティ貢献の統合
- **AIエージェントを開発する**：基盤技術とオーケストレーション機能を備えた知能エージェントの構築
- <strong>エンタープライズパターンを実装する</strong>：モジュール式でスケーラブルな本番向けAIソリューションの作成

## セッション構成

### [1: Foundry Localの始め方](./01.FoundryLocalSetup.md)
<strong>フォーカス</strong>：インストール、CLIセットアップ、モデル展開、ハードウェア最適化

<strong>主要トピック</strong>：完全インストール • CLIコマンド • モデルキャッシュ • ハードウェアアクセラレーション • マルチモデル展開

<strong>サンプル</strong>：[RESTチャットクイックスタート](./samples/01/README.md) • [OpenAI SDK統合](./samples/02/README.md) • [モデル探索＆ベンチマーク](./samples/03/README.md)

<strong>所要時間</strong>：2-3時間 | <strong>レベル</strong>：初心者

---

### [2: Azure AI FoundryでAIソリューション構築](./02.AzureAIFoundryIntegration.md)
<strong>フォーカス</strong>：高度なプロンプトエンジニアリング、データ統合、クラウド接続

<strong>主要トピック</strong>：プロンプトエンジニアリング • データ統合 • Azureワークフロー • パフォーマンス最適化 • モニタリング

<strong>サンプル</strong>：[Chainlit RAG アプリケーション](./samples/04/README.md)

<strong>所要時間</strong>：2-3時間 | <strong>レベル</strong>：中級

---

### [3: Foundry Localのオープンソースモデル](./03.OpenSourceModels.md)
<strong>フォーカス</strong>：Hugging Face統合、BYOM戦略、コミュニティモデル

<strong>主要トピック</strong>：HuggingFace統合 • Bring-your-own-model(独自モデル持込み) • Model Mondaysの洞察 • コミュニティ貢献 • モデル選択

<strong>サンプル</strong>：[マルチエージェントオーケストレーション](./samples/05/README.md)

<strong>所要時間</strong>：2-3時間 | <strong>レベル</strong>：中級

---

### [4: 最先端モデルの探求](./04.CuttingEdgeModels.md)
<strong>フォーカス</strong>：LLMとSLMの比較、EdgeAI実装、高度なデモ

<strong>主要トピック</strong>：モデル比較 • エッジ対クラウド推論 • Phi + ONNX Runtime • Chainlit RAGアプリ • WebGPU最適化

<strong>サンプル</strong>：[Models-as-Toolsルーター](./samples/06/README.md)

<strong>所要時間</strong>：3-4時間 | <strong>レベル</strong>：上級

---

### [5: AIパワードエージェントを迅速に構築](./05.AIPoweredAgents.md)
<strong>フォーカス</strong>：エージェントアーキテクチャ、システムプロンプト、基盤技術、オーケストレーション

<strong>主要トピック</strong>：エージェント設計パターン • システムプロンプトエンジニアリング • 基盤技術 • マルチエージェントシステム • 本番展開

<strong>サンプル</strong>：[マルチエージェントオーケストレーション](./samples/05/README.md) • [高度なマルチエージェントシステム](./samples/09/README.md)

<strong>所要時間</strong>：3-4時間 | <strong>レベル</strong>：上級

---

### [6: Foundry Local - Models as Tools](./06.ModelsAsTools.md)
<strong>フォーカス</strong>：モジュール化されたAIソリューション、エンタープライズスケール、生産性パターン

<strong>主要トピック</strong>：モデルをツールとして • デバイス上展開 • SDK/API統合 • エンタープライズアーキテクチャ • スケーリング戦略

<strong>サンプル</strong>：[Models-as-Toolsルーター](./samples/06/README.md) • [Foundryツールフレームワーク](./samples/10/README.md)

<strong>所要時間</strong>：3-4時間 | <strong>レベル</strong>：エキスパート

---

### [7: 直接API統合パターン](./samples/07/README.md)
<strong>フォーカス</strong>：SDK依存無しの純粋なREST API統合で最大の制御性を実現

<strong>主要トピック</strong>：HTTPクライアント実装 • カスタム認証 • モデルヘルスモニタリング • ストリーミング応答 • 本番エラー処理

<strong>サンプル</strong>：[直接APIクライアント](./samples/07/README.md)

<strong>所要時間</strong>：2-3時間 | <strong>レベル</strong>：中級

---

### [8: Windows 11ネイティブチャットアプリケーション](./samples/08/README.md)
<strong>フォーカス</strong>：Foundry Local統合によるモダンなネイティブチャットアプリの構築

<strong>主要トピック</strong>：Electron開発 • Fluent Design System • ネイティブWindows統合 • リアルタイムストリーミング • チャットインターフェース設計

<strong>サンプル</strong>：[Windows 11チャットアプリケーション](./samples/08/README.md)

<strong>所要時間</strong>：3-4時間 | <strong>レベル</strong>：上級

---

### [9: 高度なマルチエージェントオーケストレーション](./samples/09/README.md)
<strong>フォーカス</strong>：洗練されたエージェント調整、専門タスクの委任、協調AIワークフロー

<strong>主要トピック</strong>：知能的エージェント調整 • ファンクションコールパターン • エージェント間コミュニケーション • ワークフローオーケストレーション • 品質保証メカニズム

<strong>サンプル</strong>：[高度なマルチエージェントシステム](./samples/09/README.md)

<strong>所要時間</strong>：4-5時間 | <strong>レベル</strong>：エキスパート

---

### [10: Foundry Localをツールフレームワークとして](./samples/10/README.md)
<strong>フォーカス</strong>：既存アプリケーションやフレームワークへのFoundry Local統合のためのツールファーストアーキテクチャ

<strong>主要トピック</strong>：LangChain統合 • Semantic Kernel関数 • REST APIフレームワーク • CLIツール • Jupyter統合 • 本番展開パターン

<strong>サンプル</strong>：[Foundryツールフレームワーク](./samples/10/README.md)

<strong>所要時間</strong>：4-5時間 | <strong>レベル</strong>：エキスパート

## 前提条件

### システム要件
- <strong>オペレーティングシステム</strong>：Windows 11 (22H2以降)
- <strong>メモリ</strong>：16GB RAM（大型モデルの場合は32GB推奨）
- <strong>ストレージ</strong>：モデルキャッシュ用に50GBの空き容量
- <strong>ハードウェア</strong>：NPU対応デバイス推奨（Copilot+ PC）、GPUは任意
- <strong>ネットワーク</strong>：初期モデルダウンロード用に高速インターネット接続が必要

### 開発環境

- AI Toolkit拡張機能付きVisual Studio Code
- Python 3.10以上およびpip
- バージョン管理用Git
- PowerShellまたはコマンドプロンプト
- Azure CLI（クラウド統合の場合はオプション）

### 知識の前提条件
- AI/MLの基本概念の理解
- コマンドラインの基本操作
- Pythonプログラミングの基礎知識
- REST APIの概念
- プロンプト送信とモデル推論の基本知識

## モジュールのタイムライン

<strong>推定総時間</strong>: 30-38時間

| セッション | フォーカス領域 | サンプル | 時間 | 難易度 |
|---------|------------|---------|------|------------|
|  1 | セットアップと基本 | 01, 02, 03 | 2-3時間 | 初級 |
|  2 | AIソリューション | 04 | 2-3時間 | 中級 |
|  3 | オープンソース | 05 | 2-3時間 | 中級 |
|  4 | 高度なモデル | 06 | 3-4時間 | 上級 |
|  5 | AIエージェント | 05, 09 | 3-4時間 | 上級 |
|  6 | エンタープライズツール | 06, 10 | 3-4時間 | エキスパート |
|  7 | 直接API統合 | 07 | 2-3時間 | 中級 |
|  8 | Windows 11チャットアプリ | 08 | 3-4時間 | 上級 |
|  9 | 高度なマルチエージェント | 09 | 4-5時間 | エキスパート |
| 10 | ツールフレームワーク | 10 | 4-5時間 | エキスパート |

## 重要なリソース

**公式ドキュメンテーション:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - ソースコードと公式サンプル
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - セットアップと使用方法の完全ガイド
- [Model Mondays Series](https://aka.ms/model-mondays) - 週間モデルハイライトとチュートリアル

**コミュニティとサポート:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - コミュニティQ&Aおよび機能リクエスト
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - 最新ニュースとベストプラクティス

## 学習成果

このモジュールを修了すると、以下が可能になります：

### 技術的習熟
- <strong>展開および管理</strong>: 開発および本番環境でFoundry Localのインストールを管理
- <strong>モデル統合</strong>: Microsoft、Hugging Face、コミュニティ各種の多様なモデルファミリーとシームレスに連携
- <strong>アプリケーション構築</strong>: 高度な機能と最適化を備えた本番対応のAIアプリケーションを作成
- <strong>エージェント開発</strong>: グラウンディング、推論、ツール連携を備えた高度なAIエージェントを実装

### 戦略的理解
- <strong>アーキテクチャの意思決定</strong>: ローカルとクラウド展開の選択を情報に基づき判断
- <strong>パフォーマンス最適化</strong>: さまざまなハードウェア構成にわたる推論性能を最適化
- <strong>エンタープライズスケーリング</strong>: ローカルプロトタイプからエンタープライズ展開までスケール可能なアプリケーションを設計
- <strong>プライバシーとセキュリティ</strong>: ローカル推論によるプライバシー保護型AIソリューションを実装

### イノベーション能力
- <strong>迅速なプロトタイピング</strong>: 10のサンプルパターン全てでAIアプリケーションのコンセプトを迅速に構築・テスト
- <strong>コミュニティ統合</strong>: オープンソースモデルを活用し、エコシステムに貢献
- <strong>高度なパターン</strong>: RAG、エージェント、ツール連携など最先端のAIパターンを実装
- <strong>フレームワーク習熟</strong>: LangChain、Semantic Kernel、Chainlit、Electronとのエキスパートレベル統合
- <strong>本番展開</strong>: ローカルプロトタイプからエンタープライズシステムまでスケーラブルなAIソリューションを展開
- <strong>将来対応開発</strong>: 新興のAI技術とパターンに対応したアプリケーションを構築

## はじめに

1. <strong>環境設定</strong>: 推奨ハードウェアを備えたWindows 11を準備（前提条件参照）
2. **Foundry Localのインストール**: セッション1に従い完全なインストールと設定を実施
3. **サンプル01の実行**: 基本的なREST API統合から開始してセットアップを検証
4. <strong>サンプルの進行</strong>: すべてのサンプル01-10を完了し包括的な習熟を目指す

## 成功指標

10の包括的なサンプルを通じて進捗を追跡：

### 基礎レベル（サンプル01-03）
- [ ] Foundry Localのインストールと設定に成功
- [ ] REST API統合を完了（サンプル01）
- [ ] OpenAI SDK対応の実装（サンプル02）
- [ ] モデルの検出とベンチマークを実行（サンプル03）

### アプリケーションレベル（サンプル04-06）
- [ ] 4つ以上の異なるモデルファミリーを展開・実行
- [ ] 機能的なRAGチャットアプリケーションを構築（サンプル04）
- [ ] マルチエージェントオーケストレーションシステムを作成（サンプル05）
- [ ] インテリジェントモデルルーティングを実装（サンプル06）

### 高度な統合レベル（サンプル07-10）
- [ ] 本番対応のAPIクライアントを構築（サンプル07）
- [ ] Windows 11ネイティブチャットアプリを開発（サンプル08）
- [ ] 高度なマルチエージェントシステムを実装（サンプル09）
- [ ] 包括的なツールフレームワークを作成（サンプル10）

### 習熟の指標
- [ ] 10のサンプルすべてをエラーなしで実行
- [ ] 3つ以上のサンプルを特定のユースケース向けにカスタマイズ
- [ ] 2つ以上のサンプルを本番環境に近い環境で展開
- [ ] サンプルコードの改善や拡張に貢献
- [ ] Foundry Localのパターンを個人またはプロジェクトに統合

## クイックスタートガイド - 全10サンプル

### 環境設定（全サンプル共通の必須事項）

```powershell
# 1. Module08 をクローンして移動する
cd Module08

# 2. Python の仮想環境を作成する
py -m venv .venv
.\.venv\Scripts\activate

# 3. 基本的な依存関係をインストールする
pip install -r requirements.txt

# 4. Foundry Local をインストールする（未インストールの場合）
winget install Microsoft.FoundryLocal

# 5. Foundry Local のインストールを確認する
foundry --version
foundry model list
```

### 基礎コアサンプル（01-06）

**サンプル01: RESTチャットのクイックスタート**
```powershell
# Foundry Local サービスを起動
foundry model run phi-4-mini

# REST チャットデモを実行
python samples/01/chat_quickstart.py
```

**サンプル02: OpenAI SDK統合**
```powershell
# モデルが実行中であることを確認してください
foundry status

# SDKデモを実行する
python samples/02/sdk_quickstart.py
```

**サンプル03: モデル検出とベンチマーク**
```powershell
# 包括的なモデルテストを実行する
samples/03/list_and_bench.cmd

# または個々のコンポーネントを実行する
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**サンプル04: Chainlit RAGアプリケーション**
```powershell
# Chainlitの依存関係をインストールします
pip install chainlit langchain chromadb

# RAGチャットアプリケーションを起動します
chainlit run samples/04/app.py -w
# http://localhost:8000 でブラウザを開きます
```

**サンプル05: マルチエージェントオーケストレーション**
```powershell
# エージェントコーディネーターデモを実行する
python -m samples.05.agents.coordinator

# 特定のエージェント例を実行する
python samples/05/examples/specialists_demo.py
```

**サンプル06: ツールとしてのモデルルーター**
```powershell
# 環境を設定する
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# インテリジェントルーターを実行する
python samples/06/router.py "Analyze this Python code for performance issues"
```

### 高度な統合サンプル（07-10）

**サンプル07: 直接APIクライアント**
```powershell
# サンプルディレクトリに移動します
cd samples/07

# 追加の依存関係をインストールします
pip install -r requirements.txt

# 基本的なAPI例を実行します
python examples/basic_usage.py

# ストリーミングレスポンスを試します
python examples/streaming.py

# 本番パターンをテストします
python examples/production.py
```

**サンプル08: Windows 11チャットアプリケーション**
```powershell
# サンプルディレクトリに移動
cd samples/08

# Node.jsの依存関係をインストール
npm install

# Electronアプリケーションを起動
npm start

# または本番環境用にビルド
npm run build
```

**サンプル09: 高度なマルチエージェントシステム**
```powershell
# サンプルディレクトリに移動する
cd samples/09

# エージェントシステムの依存関係をインストールする
pip install -r requirements.txt

# 基本的なコーディネーション例を実行する
python examples/basic_coordination.py

# 複雑なワークフローを試す
python examples/complex_workflow.py

# インタラクティブエージェントデモ
python examples/interactive_demo.py
```

**サンプル10: Foundryツールフレームワーク**
```powershell
# サンプルディレクトリに移動
cd samples/10

# フレームワークの依存関係をインストール
pip install -r requirements.txt

# 基本的なツールデモを実行
python examples/basic_tools.py

# REST APIサーバーを起動
python examples/rest_api_server.py
# APIはhttp://localhost:8080で利用可能

# CLIアプリケーションを試す
python examples/cli_application.py --help

# Jupyterノートブックを起動
jupyter notebook examples/jupyter_notebook.ipynb

# LangChain統合をテスト
python examples/langchain_demo.py
```

### よくある問題のトラブルシューティング

**Foundry Localの接続エラー**
```powershell
# サービスの状態を確認する
foundry status

# 必要に応じて再起動する
foundry restart

# エンドポイントのアクセス可能性を確認する
curl http://localhost:5273/v1/models
```

<strong>モデル読み込みの問題</strong>
```powershell
# 利用可能なモデルを確認する
foundry model list --cached

# 欠落しているモデルをダウンロードする
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# 必要に応じて強制的にリロードする
foundry model unload --all
foundry model run phi-4-mini
```

<strong>依存関係の問題</strong>
```powershell
# pipをアップグレードして再インストールする
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Node.jsのサンプル用
npm cache clean --force
npm install
```

## まとめ


このモジュールは、Microsoftのエンタープライズグレードのツールとオープンソースエコシステムの柔軟性と革新性を融合した、エッジAI開発の最先端を表しています。Foundry Localの10の包括的なサンプルすべてを習得することで、AIアプリケーション開発の最前線に立つことができます。

**完全な学習パス:**
- <strong>基礎</strong> (サンプル01-03): API統合とモデル管理
- <strong>応用</strong> (サンプル04-06): RAG、エージェント、およびインテリジェントルーティング
- <strong>上級</strong> (サンプル07-10): 本番環境フレームワークとエンタープライズ統合

Azure OpenAI統合（セッション2）については、個別のサンプルREADMEファイルで必要な環境変数およびAPIバージョンの設定をご確認ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->