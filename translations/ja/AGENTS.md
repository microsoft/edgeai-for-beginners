# AGENTS.md

> **初心者向けEdgeAIへの貢献に関する開発者ガイド**
> 
> このドキュメントは、このリポジトリで作業する開発者、AIエージェント、貢献者向けに包括的な情報を提供します。セットアップ、開発ワークフロー、テスト、ベストプラクティスについて説明しています。
> 
> **最終更新日**: 2025年10月30日 | **ドキュメントバージョン**: 3.0

## 目次

- [プロジェクト概要](../..)
- [リポジトリ構造](../..)
- [前提条件](../..)
- [セットアップコマンド](../..)
- [開発ワークフロー](../..)
- [テスト手順](../..)
- [コードスタイルガイドライン](../..)
- [プルリクエストガイドライン](../..)
- [翻訳システム](../..)
- [Foundry Localの統合](../..)
- [ビルドとデプロイ](../..)
- [一般的な問題とトラブルシューティング](../..)
- [追加リソース](../..)
- [プロジェクト固有の注意事項](../..)
- [ヘルプの取得](../..)

## プロジェクト概要

EdgeAI for Beginnersは、小型言語モデル（SLM）を使用したEdge AI開発を学ぶための包括的な教育リポジトリです。このコースでは、EdgeAIの基礎、モデルのデプロイ、最適化技術、Microsoft Foundry LocalやさまざまなAIフレームワークを使用した実践的な実装について学びます。

**主要技術:**
- Python 3.8+（AI/MLサンプルの主要言語）
- .NET C#（AI/MLサンプル）
- JavaScript/Node.jsとElectron（デスクトップアプリケーション用）
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AIフレームワーク: LangChain, Semantic Kernel, Chainlit
- モデル最適化: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**リポジトリタイプ:** 8つのモジュールと10の包括的なサンプルアプリケーションを含む教育コンテンツリポジトリ

**アーキテクチャ:** 実践的なサンプルを通じてEdge AIデプロイメントパターンを示すマルチモジュール学習パス

## リポジトリ構造

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## 前提条件

### 必要なツール

- **Python 3.8+** - AI/MLサンプルとノートブック用
- **Node.js 16+** - Electronサンプルアプリケーション用
- **Git** - バージョン管理用
- **Microsoft Foundry Local** - AIモデルをローカルで実行するため

### 推奨ツール

- **Visual Studio Code** - Python、Jupyter、Pylance拡張機能付き
- **Windows Terminal** - コマンドライン体験向上（Windowsユーザー向け）
- **Docker** - コンテナ化された開発用（オプション）

### システム要件

- **RAM**: 最低8GB、マルチモデルシナリオでは16GB以上推奨
- **ストレージ**: モデルと依存関係用に10GB以上の空き容量
- **OS**: Windows 10/11、macOS 11+、またはLinux（Ubuntu 20.04+）
- **ハードウェア**: AVX2対応CPU; GPU（CUDA、Qualcomm NPU）はオプションだが推奨

### 知識の前提条件

- Pythonプログラミングの基本的な理解
- コマンドラインインターフェースの使用経験
- AI/MLの概念の理解（サンプル開発用）
- Gitワークフローとプルリクエストプロセスの理解

## セットアップコマンド

### リポジトリセットアップ

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Pythonサンプルセットアップ（Module08とワークショップサンプル）

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.jsサンプルセットアップ（サンプル08 - Windowsチャットアプリ）

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Localセットアップ

Foundry Localはサンプルを実行するために必要です。公式リポジトリからダウンロードしてインストールしてください。

**インストール方法:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **手動**: [リリースページ](https://github.com/microsoft/Foundry-Local/releases)からダウンロード

**クイックスタート:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**注意**: Foundry Localはハードウェアに最適なモデルバリアントを自動的に選択します（CUDA GPU、Qualcomm NPU、またはCPU）。

## 開発ワークフロー

### コンテンツ開発

このリポジトリは主に**Markdown教育コンテンツ**を含んでいます。変更を加える際は以下を行ってください:

1. 適切なモジュールディレクトリ内の`.md`ファイルを編集
2. 既存のフォーマットパターンに従う
3. コード例が正確でテスト済みであることを確認
4. 必要に応じて対応する翻訳コンテンツを更新（または自動化に任せる）

### サンプルアプリケーション開発

Module08 Pythonサンプル（サンプル01-07, 09-10）:
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

ワークショップPythonサンプル:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electronサンプル（サンプル08）:
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### サンプルアプリケーションのテスト

Pythonサンプルには自動テストがありませんが、実行して検証できます:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electronサンプルにはテストインフラがあります:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## テスト手順

### コンテンツ検証

リポジトリは自動翻訳ワークフローを使用しています。翻訳の手動テストは不要です。

**コンテンツ変更の手動検証:**
1. `.md`ファイルをプレビューしてMarkdownレンダリングを確認
2. すべてのリンクが有効なターゲットを指していることを確認
3. ドキュメントに含まれるコードスニペットをテスト
4. 画像が正しく読み込まれることを確認

### サンプルアプリケーションのテスト

**Module08/samples/08（Electronアプリ）は包括的なテストを備えています:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Pythonサンプルは手動でテストする必要があります:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## コードスタイルガイドライン

### Markdownコンテンツ

- 一貫した見出し階層を使用（タイトルには#、メインセクションには##、サブセクションには###）
- 言語指定付きのコードブロックを含める: ```python, ```bash, ```javascript
- テーブル、リスト、強調の既存のフォーマットに従う
- 読みやすい行を維持（約80-100文字を目安、厳密ではない）
- 内部参照には相対リンクを使用

### Pythonコードスタイル

- PEP 8規約に従う
- 適切な箇所で型ヒントを使用
- 関数やクラスにドキュメント文字列を含める
- 意味のある変数名を使用
- 関数を簡潔かつ焦点を絞ったものにする

### JavaScript/Node.jsコードスタイル

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**主な規約:**
- サンプル08に提供されているESLint設定を使用
- Prettierでコードフォーマットを行う
- モダンなES6+構文を使用
- コードベースの既存のパターンに従う

## プルリクエストガイドライン

### 貢献ワークフロー

1. **リポジトリをフォーク**し、`main`から新しいブランチを作成
2. **コードスタイルガイドラインに従って変更を加える**
3. **上記のテスト手順を使用して徹底的にテスト**
4. **明確なメッセージでコミット**（従来のコミット形式に従う）
5. **フォークにプッシュ**し、プルリクエストを作成
6. **レビュー中にメンテナーからのフィードバックに対応**

### ブランチ命名規則

- `feature/<module>-<description>` - 新機能やコンテンツの場合
- `fix/<module>-<description>` - バグ修正の場合
- `docs/<description>` - ドキュメント改善の場合
- `refactor/<description>` - コードリファクタリングの場合

### コミットメッセージ形式

[Conventional Commits](https://www.conventionalcommits.org/)に従う:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**例:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### タイトル形式
```
[ModuleXX] Brief description of change
```
または
```
[Module08/samples/XX] Description for sample changes
```

### 行動規範

すべての貢献者は[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)に従う必要があります。貢献する前に[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)を確認してください。

### 提出前に

**コンテンツ変更の場合:**
- 変更したすべてのMarkdownファイルをプレビュー
- リンクと画像が機能することを確認
- タイポや文法エラーをチェック

**サンプルコード変更の場合（Module08/samples/08）:**
```bash
npm run lint
npm test
```

**Pythonサンプル変更の場合:**
- サンプルが正常に実行されることをテスト
- エラーハンドリングが機能することを確認
- Foundry Localとの互換性をチェック

### レビュープロセス

- 教育コンテンツの変更は正確性と明確さを確認
- コードサンプルは機能性をテスト
- 翻訳の更新はGitHub Actionsによって自動的に処理

## 翻訳システム

**重要:** このリポジトリはGitHub Actionsによる自動翻訳を使用しています。

- 翻訳は`/translations/`ディレクトリにあります（50以上の言語）
- `co-op-translator.yml`ワークフローによって自動化
- **翻訳ファイルを手動で編集しないでください** - 上書きされます
- ルートおよびモジュールディレクトリ内の英語ソースファイルのみ編集
- 翻訳は`main`ブランチへのプッシュ時に自動生成されます

## Foundry Localの統合

ほとんどのModule08サンプルはMicrosoft Foundry Localの実行を必要とします。

### インストールとセットアップ

**Foundry Localのインストール:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDKのインストール:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Localの起動
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDKの使用方法（Python）
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Localの検証
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### サンプル用環境変数

ほとんどのサンプルは以下の環境変数を使用します:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**注意**: `FoundryLocalManager`を使用する場合、SDKはサービス検出とモデル読み込みを自動的に処理します。モデルエイリアス（例: `phi-3.5-mini`）はハードウェアに最適なバリアントを選択します。

## ビルドとデプロイ

### コンテンツデプロイ

このリポジトリは主にドキュメントで構成されているため、コンテンツにビルドプロセスは必要ありません。

### サンプルアプリケーションのビルド

**Electronアプリケーション（Module08/samples/08）:**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Pythonサンプル:**
ビルドプロセスは不要 - サンプルはPythonインタープリターで直接実行されます。

## 一般的な問題とトラブルシューティング

> **ヒント**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)で既知の問題と解決策を確認してください。

### 重大な問題（ブロッキング）

#### Foundry Localが実行されていない
**問題:** サンプルが接続エラーで失敗する

**解決策:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### 一般的な問題（中程度）

#### Python仮想環境の問題
**問題:** モジュールインポートエラー

**解決策:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electronビルドの問題
**問題:** npm installまたはビルドの失敗

**解決策:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### ワークフローの問題（軽微）

#### 翻訳ワークフローの競合
**問題:** 翻訳PRが変更と競合する

**解決策:**
- 英語のソースファイルのみ編集
- 自動翻訳ワークフローに翻訳を任せる
- 競合が発生した場合、翻訳がマージされた後に`main`をブランチにマージ

#### モデルダウンロードの失敗
**問題:** Foundry Localがモデルのダウンロードに失敗する

**解決策:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## 追加リソース

### 学習パス
- **初心者向けパス:** モジュール01-02（7-9時間）
- **中級者向けパス:** モジュール03-04（9-11時間）
- **上級者向けパス:** モジュール05-07（12-15時間）
- **エキスパート向けパス:** モジュール08（8-10時間）
- **実践ワークショップ:** ワークショップ資料（6-8時間）

### 主要モジュールコンテンツ
- **Module01:** EdgeAIの基礎と実世界のケーススタディ
- **Module02:** 小型言語モデル（SLM）のファミリーとアーキテクチャ
- **Module03:** ローカルおよびクラウドデプロイメント戦略
- **Module04:** 複数フレームワークを使用したモデル最適化（Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX）
- **Module05:** SLMOps - 本番運用
- **Module06:** AIエージェントと関数呼び出し
- **Module07:** プラットフォーム固有の実装
- **Module08:** Foundry Localツールキットと10の包括的なサンプル

### 外部依存関係
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI互換APIを備えたローカルAIモデルランタイム
  - [ドキュメント](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 最適化フレームワーク
- [Microsoft Olive](https://microsoft.github.io/Olive/) - モデル最適化ツールキット
- [OpenVINO](https://docs.openvino.ai/) - Intelの最適化ツールキット

## プロジェクト固有の注意事項

### Module08サンプルアプリケーション

リポジトリには10の包括的なサンプルアプリケーションが含まれています:

1. **01-REST Chat Quickstart** - 基本的なOpenAI SDK統合
2. **02-OpenAI SDK Integration** - 高度なSDK機能
3. **03-Model Discovery & Benchmarking** - モデル比較ツール
4. **04-Chainlit RAG Application** - 検索強化生成
5. **05-Multi-Agent Orchestration** - 基本的なエージェント調整
6. **06-Models-as-Tools Router** - インテリジェントモデルルーティング
7. **07-Direct API Client** - 低レベルAPI統合
8. **08-Windows 11 Chat App** - ネイティブElectronデスクトップアプリケーション
9. **09-Advanced Multi-Agent System** - 複雑なエージ
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel統合

### ワークショップサンプルアプリケーション

ワークショップは、実践的な実装を含む6つの段階的なセッションで構成されています：

1. **セッション01** - Foundry Local統合によるチャットのブートストラップ
2. **セッション02** - RAGパイプラインとRAGASによる評価
3. **セッション03** - オープンソースモデルのベンチマーク
4. **セッション04** - モデルの比較と選択
5. **セッション05** - マルチエージェントオーケストレーションシステム
6. **セッション06** - モデルルーティングとパイプライン管理

各サンプルは、Foundry Localを使用したエッジAI開発の異なる側面を示しています。

### パフォーマンスに関する考慮事項

- SLMはエッジ展開向けに最適化されています（2-16GB RAM）
- ローカル推論は50-500msの応答時間を提供
- 量子化技術により、サイズを75%削減しつつ85%の性能を維持
- ローカルモデルによるリアルタイム会話機能

### セキュリティとプライバシー

- すべての処理はローカルで行われ、クラウドにデータは送信されません
- プライバシーに敏感なアプリケーション（医療、金融）に適しています
- データ主権要件を満たします
- Foundry Localは完全にローカルハードウェア上で動作します

## ヘルプを得る

### ドキュメント

- **メインREADME**: [README.md](README.md) - リポジトリ概要と学習パス
- **学習ガイド**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - 学習リソースとタイムライン
- **サポート**: [SUPPORT.md](SUPPORT.md) - ヘルプの取得方法
- **セキュリティ**: [SECURITY.md](SECURITY.md) - セキュリティ問題の報告

### コミュニティサポート

- **GitHub Issues**: [バグ報告や機能リクエスト](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [質問やアイデアの共有](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Localに関する技術的問題](https://github.com/microsoft/Foundry-Local/issues)

### 連絡先

- **メンテナー**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)を参照
- **セキュリティ問題**: [SECURITY.md](SECURITY.md)に記載された責任ある開示手順に従う
- **Microsoftサポート**: エンタープライズサポートについては、Microsoftカスタマーサービスにお問い合わせください

### 追加リソース

- **Microsoft Learn**: [AIと機械学習の学習パス](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Localドキュメント**: [公式ドキュメント](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **コミュニティサンプル**: コミュニティの貢献については[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)を確認

---

**このリポジトリは、エッジAI開発の教育に焦点を当てています。主な貢献パターンは、教育コンテンツの改善と、エッジAIの概念を示すサンプルアプリケーションの追加や強化です。**

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。