# モジュール 08: Microsoft Foundry Local - 完全な開発者ツールキットの実践

## 概要

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) は、次世代のエッジAI開発を代表するものであり、開発者がAIアプリケーションをローカルで構築、展開、スケールするための強力なツールを提供します。同時にAzure AI Foundryとのシームレスな統合を維持します。このモジュールでは、Foundry Localのインストールから高度なエージェント開発までを包括的にカバーします。

**主要技術:**
- Microsoft Foundry Local CLIとSDK
- Azure AI Foundryとの統合
- デバイス上でのモデル推論
- ローカルモデルのキャッシュと最適化
- エージェントベースのアーキテクチャ

## 学習目標

このモジュールを完了することで、以下を達成できます:

- **Foundry Localの習得**: Windows 11開発向けにインストール、設定、最適化を行う
- **多様なモデルの展開**: phi、qwen、deepseek、GPTモデルをCLIコマンドでローカルで実行
- **実用的なソリューションの構築**: 高度なプロンプトエンジニアリングとデータ統合を活用したAIアプリケーションの作成
- **オープンソースエコシステムの活用**: Hugging Faceモデルやコミュニティの貢献を統合
- **AIエージェントの開発**: グラウンディングとオーケストレーション機能を備えたインテリジェントエージェントの構築
- **エンタープライズパターンの実装**: モジュール化されたスケーラブルなAIソリューションを構築し、実運用に展開

## セッション構成

### [1: Foundry Localの始め方](./01.FoundryLocalSetup.md)
**焦点**: インストール、CLI設定、モデル展開、ハードウェア最適化

**主要トピック**: 完全なインストール • CLIコマンド • モデルキャッシュ • ハードウェアアクセラレーション • 複数モデルの展開

**サンプル**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**所要時間**: 2-3時間 | **レベル**: 初級

---

### [2: Azure AI Foundryを活用したAIソリューションの構築](./02.AzureAIFoundryIntegration.md)
**焦点**: 高度なプロンプトエンジニアリング、データ統合、クラウド接続

**主要トピック**: プロンプトエンジニアリング • データ統合 • Azureワークフロー • パフォーマンス最適化 • モニタリング

**サンプル**: [Chainlit RAG Application](./samples/04/README.md)

**所要時間**: 2-3時間 | **レベル**: 中級

---

### [3: Foundry Localでのオープンソースモデル](./03.OpenSourceModels.md)
**焦点**: Hugging Face統合、BYOM戦略、コミュニティモデル

**主要トピック**: HuggingFace統合 • 独自モデルの持ち込み • Model Mondaysの洞察 • コミュニティの貢献 • モデル選択

**サンプル**: [Multi-Agent Orchestration](./samples/05/README.md)

**所要時間**: 2-3時間 | **レベル**: 中級

---

### [4: 最先端モデルの探求](./04.CuttingEdgeModels.md)
**焦点**: LLMsとSLMsの比較、EdgeAIの実装、高度なデモ

**主要トピック**: モデル比較 • エッジとクラウド推論 • Phi + ONNX Runtime • Chainlit RAGアプリ • WebGPU最適化

**サンプル**: [Models-as-Tools Router](./samples/06/README.md)

**所要時間**: 3-4時間 | **レベル**: 上級

---

### [5: AI駆動エージェントの迅速な構築](./05.AIPoweredAgents.md)
**焦点**: エージェントアーキテクチャ、システムプロンプト、グラウンディング、オーケストレーション

**主要トピック**: エージェント設計パターン • システムプロンプトエンジニアリング • グラウンディング技術 • 複数エージェントシステム • 実運用展開

**サンプル**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**所要時間**: 3-4時間 | **レベル**: 上級

---

### [6: Foundry Local - ツールとしてのモデル](./06.ModelsAsTools.md)
**焦点**: モジュール型AIソリューション、エンタープライズスケーリング、実運用パターン

**主要トピック**: ツールとしてのモデル • デバイス上での展開 • SDK/API統合 • エンタープライズアーキテクチャ • スケーリング戦略

**サンプル**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**所要時間**: 3-4時間 | **レベル**: エキスパート

---

### [7: 直接API統合パターン](./samples/07/README.md)
**焦点**: SDK依存なしで最大限の制御を可能にする純粋なREST API統合

**主要トピック**: HTTPクライアント実装 • カスタム認証 • モデルのヘルスモニタリング • ストリーミングレスポンス • 実運用エラー処理

**サンプル**: [Direct API Client](./samples/07/README.md)

**所要時間**: 2-3時間 | **レベル**: 中級

---

### [8: Windows 11ネイティブチャットアプリケーション](./samples/08/README.md)
**焦点**: Foundry Local統合を活用したモダンなネイティブチャットアプリケーションの構築

**主要トピック**: Electron開発 • Fluent Design System • ネイティブWindows統合 • リアルタイムストリーミング • チャットインターフェース設計

**サンプル**: [Windows 11 Chat Application](./samples/08/README.md)

**所要時間**: 3-4時間 | **レベル**: 上級

---

### [9: 高度なマルチエージェントオーケストレーション](./samples/09/README.md)
**焦点**: 高度なエージェントの調整、専門的なタスクの委任、協調的なAIワークフロー

**主要トピック**: インテリジェントエージェントの調整 • 関数呼び出しパターン • エージェント間通信 • ワークフローオーケストレーション • 品質保証メカニズム

**サンプル**: [Advanced Multi-Agent System](./samples/09/README.md)

**所要時間**: 4-5時間 | **レベル**: エキスパート

---

### [10: Foundry Localをツールフレームワークとして活用](./samples/10/README.md)
**焦点**: Foundry Localを既存のアプリケーションやフレームワークに統合するツール優先のアーキテクチャ

**主要トピック**: LangChain統合 • Semantic Kernel関数 • REST APIフレームワーク • CLIツール • Jupyter統合 • 実運用展開パターン

**サンプル**: [Foundry Tools Framework](./samples/10/README.md)

**所要時間**: 4-5時間 | **レベル**: エキスパート

## 前提条件

### システム要件
- **オペレーティングシステム**: Windows 11 (22H2以降)
- **メモリ**: 16GB RAM (大規模モデルには32GB推奨)
- **ストレージ**: モデルキャッシュ用に50GBの空き容量
- **ハードウェア**: NPU対応デバイス推奨 (Copilot+ PC)、GPUはオプション
- **ネットワーク**: 初回モデルダウンロード用の高速インターネット

### 開発環境
- AI Toolkit拡張機能付きVisual Studio Code
- Python 3.10+とpip
- バージョン管理用Git
- PowerShellまたはコマンドプロンプト
- Azure CLI (クラウド統合にオプション)

### 知識の前提条件
- AI/MLの基本概念の理解
- コマンドラインの基本操作
- Pythonプログラミングの基礎
- REST APIの概念
- プロンプトとモデル推論の基本知識

## モジュールタイムライン

**総所要時間**: 30-38時間

| セッション | フォーカスエリア | サンプル | 時間 | 複雑度 |
|------------|------------------|----------|------|--------|
|  1 | セットアップと基礎 | 01, 02, 03 | 2-3時間 | 初級 |
|  2 | AIソリューション | 04 | 2-3時間 | 中級 |
|  3 | オープンソース | 05 | 2-3時間 | 中級 |
|  4 | 高度なモデル | 06 | 3-4時間 | 上級 |
|  5 | AIエージェント | 05, 09 | 3-4時間 | 上級 |
|  6 | エンタープライズツール | 06, 10 | 3-4時間 | エキスパート |
|  7 | 直接API統合 | 07 | 2-3時間 | 中級 |
|  8 | Windows 11チャットアプリ | 08 | 3-4時間 | 上級 |
|  9 | 高度なマルチエージェント | 09 | 4-5時間 | エキスパート |
| 10 | ツールフレームワーク | 10 | 4-5時間 | エキスパート |

## 主要リソース

**公式ドキュメント:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - ソースコードと公式サンプル
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - 完全なセットアップと使用ガイド
- [Model Mondays Series](https://aka.ms/model-mondays) - 毎週のモデルハイライトとチュートリアル

**コミュニティとサポート:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - コミュニティQ&Aと機能リクエスト
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - 最新ニュースとベストプラクティス

## 学習成果

このモジュールを完了することで、以下のスキルを習得できます:

### 技術的習熟
- **展開と管理**: 開発および実運用環境でのFoundry Localインストール
- **モデル統合**: Microsoft、Hugging Face、コミュニティソースの多様なモデルファミリーをシームレスに活用
- **アプリケーション構築**: 高度な機能と最適化を備えた実運用対応のAIアプリケーションの作成
- **エージェント開発**: グラウンディング、推論、ツール統合を備えた高度なAIエージェントの実装

### 戦略的理解
- **アーキテクチャの選択**: ローカル展開とクラウド展開の間で情報に基づいた選択を行う
- **パフォーマンス最適化**: 異なるハードウェア構成で推論性能を最適化
- **エンタープライズスケーリング**: ローカルプロトタイプからエンタープライズ展開までスケールするアプリケーションを設計
- **プライバシーとセキュリティ**: ローカル推論を使用したプライバシー保護型AIソリューションの実装

### イノベーション能力
- **迅速なプロトタイピング**: 10のサンプルパターンすべてを活用してAIアプリケーションコンセプトを迅速に構築およびテスト
- **コミュニティ統合**: オープンソースモデルを活用し、エコシステムに貢献
- **高度なパターン**: RAG、エージェント、ツール統合を含む最先端AIパターンを実装
- **フレームワーク習熟**: LangChain、Semantic Kernel、Chainlit、Electronとのエキスパートレベルの統合
- **実運用展開**: ローカルプロトタイプからエンタープライズシステムまでスケーラブルなAIソリューションを展開
- **未来対応開発**: 新興AI技術とパターンに対応したアプリケーションを構築

## 始め方

1. **環境設定**: 推奨ハードウェアを備えたWindows 11を準備 (前提条件を参照)
2. **Foundry Localのインストール**: セッション1に従い、完全なインストールと設定を実施
3. **サンプル01を実行**: 基本的なREST API統合からセットアップを確認
4. **サンプルを順次進める**: サンプル01-10を完了し、包括的な習熟を目指す

## 成功指標

10の包括的なサンプルを通じて進捗を追跡:

### 基礎レベル (サンプル01-03)
- [ ] Foundry Localのインストールと設定を成功させる
- [ ] REST API統合を完了 (サンプル01)
- [ ] OpenAI SDK互換性を実装 (サンプル02)
- [ ] モデルの発見とベンチマークを実施 (サンプル03)

### アプリケーションレベル (サンプル04-06)
- [ ] 少なくとも4つの異なるモデルファミリーを展開して実行
- [ ] 機能的なRAGチャットアプリケーションを構築 (サンプル04)
- [ ] マルチエージェントオーケストレーションシステムを作成 (サンプル05)
- [ ] インテリジェントモデルルーティングを実装 (サンプル06)

### 高度な統合レベル (サンプル07-10)
- [ ] 実運用対応のAPIクライアントを構築 (サンプル07)
- [ ] Windows 11ネイティブチャットアプリケーションを開発 (サンプル08)
- [ ] 高度なマルチエージェントシステムを実装 (サンプル09)
- [ ] 包括的なツールフレームワークを作成 (サンプル10)

### 習熟指標
- [ ] すべての10サンプルをエラーなく実行
- [ ] 特定のユースケースに合わせて少なくとも3つのサンプルをカスタマイズ
- [ ] 実運用環境に2つ以上のサンプルを展開
- [ ] サンプルコードに改善や拡張を貢献
- [ ] Foundry Localパターンを個人/プロフェッショナルプロジェクトに統合

## クイックスタートガイド - 全10サンプル

### 環境設定 (すべてのサンプルに必要)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### 基礎サンプル (01-06)

**サンプル01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**サンプル02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**サンプル03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**サンプル04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**サンプル05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**サンプル06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### 高度な統合サンプル (07-10)

**サンプル07: Direct API Client**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**サンプル08: Windows 11 Chat Application**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**サンプル09: Advanced Multi-Agent
このモジュールは、Microsoftのエンタープライズ向けツールとオープンソースエコシステムの柔軟性と革新性を組み合わせた、エッジAI開発の最前線を表しています。Foundry Localの10個の包括的なサンプルを習得することで、AIアプリケーション開発の最前線に立つことができます。

**学習パスの全体像:**
- **基礎** (サンプル 01-03): API統合とモデル管理
- **応用** (サンプル 04-06): RAG、エージェント、インテリジェントルーティング
- **高度** (サンプル 07-10): プロダクションフレームワークとエンタープライズ統合

Azure OpenAI統合 (セッション2) に関しては、必要な環境変数やAPIバージョン設定について、各サンプルのREADMEファイルを参照してください。

---

**免責事項**:  
本書類は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（元の言語で記載された文書）を信頼できる情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用に起因する誤解や誤認について、当方は一切の責任を負いかねます。