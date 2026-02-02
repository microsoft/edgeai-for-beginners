# Windows Edge AI 開発ガイド

## はじめに

Windows Edge AI 開発へようこそ。このガイドは、MicrosoftのWindows AI Foundryプラットフォームを使用して、デバイス上でAIの力を活用するインテリジェントなアプリケーションを構築するための包括的な手引きです。Windowsのハードウェアアクセラレーションを最大限に活用しながら、最先端のEdge AI機能をアプリケーションに統合したいと考えるWindows開発者向けに設計されています。

### Windows AI の利点

Windows AI Foundryは、モデル選択や微調整から最適化、CPU、GPU、NPU、ハイブリッドクラウドアーキテクチャへの展開まで、AI開発者ライフサイクル全体をサポートする統一された信頼性の高い安全なプラットフォームです。このプラットフォームは以下を提供することでAI開発を民主化します：

- **ハードウェア抽象化**: AMD、Intel、NVIDIA、Qualcommのシリコン間でシームレスな展開
- **デバイス上のインテリジェンス**: ローカルハードウェア上で完全に動作するプライバシー保護型AI
- **最適化されたパフォーマンス**: Windowsハードウェア構成に最適化されたモデル
- **エンタープライズ対応**: 生産グレードのセキュリティとコンプライアンス機能

### Windows ML
Windows Machine Learning (ML)は、C#、C++、Python開発者がONNX Runtimeを介してWindows PC上でONNX AIモデルをローカルで実行できるようにします。これにより、CPU、GPU、NPUなどの異なるハードウェアに対する自動実行プロバイダー管理が可能です。[ONNX Runtime](https://onnxruntime.ai/docs/)は、PyTorch、Tensorflow/Keras、TFLite、scikit-learnなどのフレームワークからのモデルで使用できます。

![WindowsML ONNXモデルがWindows MLを通じてNPU、GPU、CPUに到達する様子を示す図](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows MLは、Windows全体で共有されるONNX Runtimeのコピーと、実行プロバイダー（EP）を動的にダウンロードする機能を提供します。

### WindowsをEdge AIに選ぶ理由

**ユニバーサルハードウェアサポート**
Windows MLは、Windowsエコシステム全体で自動ハードウェア最適化を提供し、基盤となるシリコンアーキテクチャに関係なくAIアプリケーションが最適に動作することを保証します。

**統合AIランタイム**
組み込みのWindows ML推論エンジンにより、複雑なセットアップ要件が排除され、開発者はインフラストラクチャの懸念ではなくアプリケーションロジックに集中できます。

**Copilot+ PC最適化**
専用のニューラルプロセッシングユニット（NPU）を備えた次世代Windowsデバイス向けに設計されたAPIが、ワットあたりの優れた性能を提供します。

**開発者エコシステム**
Visual Studio統合、包括的なドキュメント、開発サイクルを加速するサンプルアプリケーションなど、豊富なツール群。

## 学習目標

このWindows Edge AI開発ガイドを完了することで、Windowsプラットフォーム上で生産準備が整ったAIアプリケーションを構築するための重要なスキルを習得できます。

### コア技術スキル

**Windows AI Foundryの習得**
- Windows AI Foundryプラットフォームのアーキテクチャとコンポーネントを理解する
- Windowsエコシステム内でAI開発ライフサイクル全体をナビゲートする
- デバイス上のAIアプリケーションのセキュリティベストプラクティスを実装する
- Windowsハードウェア構成に応じたアプリケーションを最適化する

**API統合の専門知識**
- テキスト、ビジョン、マルチモーダルアプリケーション向けのWindows AI APIを習得する
- Phi Silica言語モデル統合を使用してテキスト生成と推論を実装する
- 組み込みの画像処理APIを使用してコンピュータビジョン機能を展開する
- LoRA（低ランク適応）技術を使用して事前学習済みモデルをカスタマイズする

**Foundry Localの実装**
- Foundry Local CLIを使用してオープンソース言語モデルをブラウズ、評価、展開する
- ローカル展開のためのモデル最適化と量子化を理解する
- インターネット接続なしで機能するオフラインAI機能を実装する
- 生産環境でのモデルライフサイクルと更新を管理する

**Windows MLの展開**
- Windows MLを使用してカスタムONNXモデルをWindowsアプリケーションに導入する
- CPU、GPU、NPUアーキテクチャ全体で自動ハードウェアアクセラレーションを活用する
- 最適なリソース利用でリアルタイム推論を実装する
- 多様なWindowsデバイスカテゴリ向けにスケーラブルなAIアプリケーションを設計する

### アプリケーション開発スキル

**クロスプラットフォームWindows開発**
- .NET MAUIを使用してAI対応アプリケーションを構築し、Windows全体で展開する
- AI機能をWin32、UWP、プログレッシブWebアプリケーションに統合する
- AI処理状態に適応するレスポンシブUIデザインを実装する
- 適切なユーザーエクスペリエンスパターンで非同期AI操作を処理する

**パフォーマンス最適化**
- 異なるハードウェア構成全体でAI推論性能をプロファイルし最適化する
- 大規模言語モデルの効率的なメモリ管理を実装する
- 利用可能なハードウェア能力に基づいて優雅に劣化するアプリケーションを設計する
- 頻繁に使用されるAI操作のためのキャッシング戦略を適用する

**生産準備**
- 包括的なエラーハンドリングとフォールバックメカニズムを実装する
- AIアプリケーション性能のテレメトリとモニタリングを設計する
- ローカルAIモデルの保存と実行に関するセキュリティベストプラクティスを適用する
- エンタープライズおよびコンシューマーアプリケーション向けの展開戦略を計画する

### ビジネスと戦略的理解

**AIアプリケーションアーキテクチャ**
- ローカルとクラウドAI処理の間で最適化するハイブリッドアーキテクチャを設計する
- モデルサイズ、精度、推論速度の間のトレードオフを評価する
- プライバシーを維持しながらインテリジェンスを可能にするデータフローアーキテクチャを計画する
- ユーザー需要に応じてスケールするコスト効率の高いAIソリューションを実装する

**市場ポジショニング**
- WindowsネイティブAIアプリケーションの競争上の優位性を理解する
- デバイス上のAIが優れたユーザー体験を提供するユースケースを特定する
- AI強化Windowsアプリケーションの市場投入戦略を開発する
- Windowsエコシステムの利点を活用するアプリケーションをポジショニングする

## Windows App SDK AI サンプル

Windows App SDKは、複数のフレームワークと展開シナリオにわたるAI統合を示す包括的なサンプルを提供します。これらのサンプルは、Windows AI開発パターンを理解するための重要な参考資料です。

### Windows AI Foundry サンプル

| サンプル | フレームワーク | フォーカスエリア | 主な特徴 |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API統合 | Windows AI API、ARM64最適化、パッケージ化展開を示す完全なWinUIアプリ |

**主な技術:**
- Windows AI API
- WinUI 3フレームワーク
- ARM64プラットフォーム最適化
- Copilot+ PC互換性
- パッケージ化アプリ展開

**前提条件:**
- Copilot+ PC推奨のWindows 11
- Visual Studio 2022
- ARM64ビルド構成
- Windows App SDK 1.8.1以上

### Windows ML サンプル

#### C++ サンプル

| サンプル | タイプ | フォーカスエリア | 主な特徴 |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | コンソールアプリ | 基本的なWindows ML | EP探索、コマンドラインオプション、モデルコンパイル |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | コンソールアプリ | フレームワーク展開 | 共有ランタイム、小型展開フットプリント |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | コンソールアプリ | 自己完結型展開 | スタンドアロン展開、ランタイム依存なし |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | ライブラリ使用 | 共有ライブラリでのWindowsML、メモリ管理 |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | デモ | ResNetチュートリアル | モデル変換、EPコンパイル、Build 2025チュートリアル |

#### C# サンプル

**コンソールアプリケーション**

| サンプル | タイプ | フォーカスエリア | 主な特徴 |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | コンソールアプリ | 基本的なC#統合 | 共有ヘルパー使用、コマンドラインインターフェース |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | デモ | ResNetチュートリアル | モデル変換、EPコンパイル、Build 2025チュートリアル |

**GUIアプリケーション**

| サンプル | フレームワーク | フォーカスエリア | 主な特徴 |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | デスクトップGUI | WPFインターフェースでの画像分類 |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | 従来型GUI | Windows Formsでの画像分類 |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | モダンGUI | WinUI 3インターフェースでの画像分類 |

#### Python サンプル

| サンプル | 言語 | フォーカスエリア | 主な特徴 |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | 画像分類 | WinML Pythonバインディング、バッチ画像処理 |

### サンプルの前提条件

**システム要件:**
- Windows 11 PC（バージョン24H2、ビルド26100以上）
- C++および.NETワークロードを備えたVisual Studio 2022
- Windows App SDK 1.8.1以上
- x64およびARM64デバイスでのPythonサンプル用Python 3.10-3.13

**Windows AI Foundry特有:**
- Copilot+ PC推奨（最適なパフォーマンスのため）
- Windows AIサンプル用ARM64ビルド構成
- パッケージIDが必要（非パッケージ化アプリはサポートされなくなりました）

### 共通サンプルワークフロー

ほとんどのWindows MLサンプルは以下の標準パターンに従います：

1. **環境の初期化** - ONNX Runtime環境を作成
2. **実行プロバイダーの登録** - 利用可能なハードウェアアクセラレータ（CPU、GPU、NPU）を探索し登録
3. **モデルの読み込み** - ONNXモデルを読み込み、必要に応じてターゲットハードウェア用にコンパイル
4. **入力の前処理** - 画像/データをモデル入力形式に変換
5. **推論の実行** - モデルを実行し予測を取得
6. **結果の処理** - ソフトマックスを適用し、トップ予測を表示

### 使用されるモデルファイル

| モデル | 目的 | 含まれるか | 備考 |
|-------|---------|----------|-------|
| SqueezeNet | 軽量画像分類 | ✅ 含まれる | 事前学習済み、すぐに使用可能 |
| ResNet-50 | 高精度画像分類 | ❌ 変換が必要 | [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion)を使用して変換 |

### ハードウェアサポート

すべてのサンプルは利用可能なハードウェアを自動的に検出し利用します：
- **CPU** - すべてのWindowsデバイスでのユニバーサルサポート
- **GPU** - 利用可能なグラフィックスハードウェアの自動検出と最適化
- **NPU** - 対応デバイス（Copilot+ PC）でニューラルプロセッシングユニットを活用

## Windows AI Foundry プラットフォームコンポーネント

### 1. Windows AI API

Windows AI APIは、デバイス上のモデルによって駆動される即使用可能なAI機能を提供し、Copilot+ PCデバイスで効率と性能に最適化され、最小限のセットアップで利用可能です。

#### コアAPIカテゴリ

**Phi Silica言語モデル**
- テキスト生成と推論のための小型で強力な言語モデル
- 最小限の電力消費でリアルタイム推論に最適化
- LoRA技術を使用したカスタム微調整のサポート
- Windowsセマンティック検索と知識検索との統合

**コンピュータビジョンAPI**
- **テキスト認識（OCR）**: 高精度で画像からテキストを抽出
- **画像超解像**: ローカルAIモデルを使用して画像をアップスケール
- **画像セグメンテーション**: 画像内の特定のオブジェクトを識別し分離
- **画像説明**: 視覚コンテンツの詳細なテキスト説明を生成
- **オブジェクト消去**: AI駆動のインペインティングで画像から不要なオブジェクトを削除

**マルチモーダル機能**
- **ビジョンと言語の統合**: テキストと画像の理解を組み合わせる
- **セマンティック検索**: マルチメディアコンテンツに対する自然言語クエリを可能にする
- **知識検索**: ローカルデータを使用してインテリジェントな検索体験を構築

### 2. Foundry Local

Foundry Localは、Windowsシリコン上でオープンソース言語モデルを迅速に利用できるようにし、ローカルアプリケーションでモデルをブラウズ、テスト、対話、展開する能力を提供します。

#### Foundry Local サンプルアプリケーション

[Foundry Localリポジトリ](https://github.com/microsoft/Foundry-Local/tree/main
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | システム統合 | 低レベルSDKの使用、非同期操作、reqwest HTTPクライアント |

#### 使用例別サンプルカテゴリ

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Semantic Kernel、Qdrantベクトルデータベース、JINA埋め込みを使用した完全なRAG実装
- **アーキテクチャ**: ドキュメント取り込み → テキスト分割 → ベクトル埋め込み → 類似性検索 → コンテキスト対応の応答
- **技術**: Microsoft.SemanticKernel、Qdrant.Client、BERT ONNX埋め込み、ストリーミングチャット完了

**デスクトップアプリケーション**
- **electron/foundry-chat**: ローカル/クラウドモデル切り替えが可能なプロダクション対応チャットアプリケーション
- **機能**: モデルセレクター、ストリーミング応答、エラーハンドリング、クロスプラットフォーム展開
- **アーキテクチャ**: Electronメインプロセス、IPC通信、セキュアなプリロードスクリプト

**SDK統合例**
- **JavaScript (Node.js)**: 基本的なモデル操作とストリーミング応答
- **Python**: OpenAI互換APIを使用した非同期ストリーミング
- **Rust**: reqwestとtokioを使用した非同期操作の低レベル統合

#### Foundry Localサンプルの前提条件

**システム要件:**
- Foundry LocalがインストールされたWindows 11
- JavaScript/Electronサンプル用のNode.js v16以上
- C#サンプル用の.NET 8.0以上
- Pythonサンプル用のPython 3.10以上
- Rustサンプル用のRust 1.70以上

**インストール:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### サンプル固有のセットアップ

**dotNET RAGサンプル:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electronチャットサンプル:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rustサンプル:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### 主な特徴

**モデルカタログ**
- 最適化済みのオープンソースモデルの包括的なコレクション
- CPU、GPU、NPUにわたるモデルの最適化で即時展開可能
- Llama、Mistral、Phi、専門分野モデルなどの人気モデルファミリーをサポート

**CLI統合**
- モデル管理と展開のためのコマンドラインインターフェース
- 自動化された最適化と量子化ワークフロー
- 人気の開発環境やCI/CDパイプラインとの統合

**ローカル展開**
- クラウド依存なしの完全オフライン操作
- カスタムモデル形式と構成のサポート
- 自動ハードウェア最適化による効率的なモデル提供

### 3. Windows ML

Windows MLは、Windows上でカスタムモデルを効率的に展開できるコアAIプラットフォームおよび統合推論ランタイムとして機能します。

#### アーキテクチャの利点

**ユニバーサルハードウェアサポート**
- AMD、Intel、NVIDIA、Qualcommシリコン向けの自動最適化
- CPU、GPU、NPU実行のサポートと透明な切り替え
- プラットフォーム固有の最適化作業を排除するハードウェア抽象化

**モデルの柔軟性**
- 人気のフレームワークからの自動変換を備えたONNXモデル形式のサポート
- 生産グレードのパフォーマンスを備えたカスタムモデル展開
- 既存のWindowsアプリケーションアーキテクチャとの統合

**エンタープライズ統合**
- Windowsのセキュリティおよびコンプライアンスフレームワークとの互換性
- エンタープライズ展開および管理ツールのサポート
- Windowsデバイス管理および監視システムとの統合

## 開発ワークフロー

### フェーズ1: 環境セットアップとツール構成

**開発環境の準備**
1. C++および.NETワークロードを含むVisual Studio 2022をインストール
2. Windows App SDK 1.8.1以降をインストール
3. Windows AI Foundry CLIツールを構成
4. Visual Studio Code用AI Toolkit拡張機能をセットアップ
5. パフォーマンスプロファイリングおよび監視ツールを確立
6. Copilot+ PC最適化のためのARM64ビルド構成を確認

**サンプルリポジトリのセットアップ**
1. [Windows App SDK Samplesリポジトリ](https://github.com/microsoft/WindowsAppSDK-Samples)をクローン
2. Windows AI API例のために`Samples/WindowsAIFoundry/cs-winui`に移動
3. 包括的なWindows ML例のために`Samples/WindowsML`に移動
4. ターゲットプラットフォームの[ビルド要件](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements)を確認

**AI Dev Galleryの探索**
- サンプルアプリケーションと参考実装を探索
- Windows AI APIを使用したインタラクティブなデモをテスト
- ベストプラクティスとパターンのためのソースコードをレビュー
- 特定の使用例に関連するサンプルを特定

### フェーズ2: モデル選択と統合

**要件分析**
- AI機能の機能要件を定義
- パフォーマンス制約と最適化目標を確立
- プライバシーとセキュリティ要件を評価
- 展開アーキテクチャとスケーリング戦略を計画

**モデル評価**
- 使用例に適したオープンソースモデルをFoundry Localでテスト
- カスタムモデル要件に対するWindows AI APIのベンチマーク
- モデルサイズ、精度、推論速度のトレードオフを評価
- 選択したモデルで統合アプローチをプロトタイプ化

### フェーズ3: アプリケーション開発

**コア統合**
- 適切なエラーハンドリングを備えたWindows AI API統合を実装
- AI処理ワークフローに対応するユーザーインターフェースを設計
- モデル推論のためのキャッシュと最適化戦略を実装
- AI操作パフォーマンスのためのテレメトリと監視を追加

**テストと検証**
- 異なるWindowsハードウェア構成でアプリケーションをテスト
- 様々な負荷条件下でのパフォーマンス指標を検証
- AI機能の信頼性のための自動テストを実装
- AI強化機能を備えたユーザーエクスペリエンステストを実施

### フェーズ4: 最適化と展開

**パフォーマンス最適化**
- ターゲットハードウェア構成全体でアプリケーションパフォーマンスをプロファイル
- メモリ使用量とモデル読み込み戦略を最適化
- 利用可能なハードウェア機能に基づく適応的な動作を実装
- 異なるパフォーマンスシナリオに対応するユーザーエクスペリエンスを微調整

**本番展開**
- 適切なAIモデル依存関係を備えたアプリケーションをパッケージ化
- モデルとアプリケーションロジックの更新メカニズムを実装
- 本番環境の監視と分析を構成
- エンタープライズおよび消費者向け展開のための展開戦略を計画

## 実践的な実装例

### 例1: インテリジェントドキュメント処理アプリケーション

複数のAI機能を使用してドキュメントを処理するWindowsアプリケーションを構築:

**使用技術:**
- Phi Silicaによるドキュメント要約と質問応答
- スキャンされたドキュメントからのテキスト抽出のためのOCR API
- チャートや図表分析のための画像説明API
- ドキュメント分類のためのカスタムONNXモデル

**実装アプローチ:**
- プラグイン可能なAIコンポーネントを備えたモジュラーアーキテクチャを設計
- 大規模なドキュメントバッチの非同期処理を実装
- 長時間実行操作の進行状況インジケーターとキャンセルサポートを追加
- 敏感なドキュメント処理のためのオフライン機能を含む

### 例2: 小売在庫管理システム

小売アプリケーション向けのAI対応在庫システムを作成:

**使用技術:**
- 製品識別のための画像セグメンテーション
- ブランドとカテゴリ分類のためのカスタムビジョンモデル
- 専門的な小売言語モデルのFoundry Local展開
- 既存のPOSおよび在庫システムとの統合

**実装アプローチ:**
- リアルタイム製品スキャンのためのカメラ統合を構築
- バーコードと視覚的製品認識を実装
- ローカル言語モデルを使用した自然言語在庫クエリを追加
- 複数店舗展開のためのスケーラブルなアーキテクチャを設計

### 例3: 医療文書アシスタント

プライバシーを保護する医療文書ツールを開発:

**使用技術:**
- Phi Silicaによる医療ノート生成と臨床意思決定支援
- 手書きの医療記録をデジタル化するためのOCR
- Windows MLを介して展開されたカスタム医療言語モデル
- 医療知識検索のためのローカルベクトルストレージ

**実装アプローチ:**
- 患者のプライバシーを保護する完全オフライン操作を確保
- 医療用語の検証と提案を実装
- 規制遵守のための監査ログを追加
- 既存の電子カルテシステムとの統合を設計

## パフォーマンス最適化戦略

### ハードウェア対応開発

**NPU最適化**
- Copilot+ PCでNPU機能を活用するアプリケーションを設計
- NPUがないデバイスではGPU/CPUへの優雅なフォールバックを実装
- NPU特有の加速のためにモデル形式を最適化
- NPUの利用状況と熱特性を監視

**メモリ管理**
- 効率的なモデル読み込みとキャッシュ戦略を実装
- 起動時間を短縮するために大規模モデルのメモリマッピングを使用
- リソース制約のあるデバイス向けにメモリ意識型アプリケーションを設計
- メモリ最適化のためにモデル量子化を実装

**バッテリー効率**
- 最小限の電力消費でAI操作を最適化
- バッテリー状態に基づく適応的な処理を実装
- 継続的なAI操作のための効率的なバックグラウンド処理を設計
- エネルギー使用を最適化するための電力プロファイリングツールを使用

### スケーラビリティの考慮事項

**マルチスレッド化**
- 同時処理のためのスレッドセーフなAI操作を設計
- 利用可能なコア全体で効率的な作業分配を実装
- 非ブロッキングAI操作のためのasync/awaitパターンを使用
- 異なるハードウェア構成向けのスレッドプール最適化を計画

**キャッシュ戦略**
- 頻繁に使用されるAI操作のためのインテリジェントキャッシュを実装
- モデル更新のためのキャッシュ無効化戦略を設計
- 高価な前処理操作のための永続的キャッシュを使用
- マルチユーザーシナリオのための分散キャッシュを実装

## セキュリティとプライバシーのベストプラクティス

### データ保護

**ローカル処理**
- 敏感なデータがローカルデバイスを離れないことを確保
- AIモデルと一時データの安全な保存を実装
- アプリケーションのサンドボックス化のためにWindowsセキュリティ機能を使用
- 保存されたモデルと中間処理結果に暗号化を適用

**モデルセキュリティ**
- 読み込みと実行前にモデルの整合性を検証
- 安全なモデル更新メカニズムを実装
- 改ざんを防ぐために署名済みモデルを使用
- モデルファイルと構成にアクセス制御を適用

### コンプライアンスの考慮事項

**規制への適合**
- GDPR、HIPAAなどの規制要件を満たすアプリケーションを設計
- AI意思決定プロセスの監査ログを実装
- AI生成結果の透明性機能を提供
- AIデータ処理に対するユーザーコントロールを有効化

**エンタープライズセキュリティ**
- Windowsエンタープライズセキュリティポリシーと統合
- エンタープライズ管理ツールを通じた管理された展開をサポート
- AI機能のための役割ベースのアクセス制御を実装
- AI機能の管理コントロールを提供

## トラブルシューティングとデバッグ

### 一般的な開発課題

**ビルド構成の問題**
- Windows AI APIサンプルのためのARM64プラットフォーム構成を確認
- Windows App SDKバージョンの互換性を確認 (1.8.1以上が必要)
- Windows AI APIに必要なパッケージIDが正しく構成されていることを確認
- ターゲットフレームワークバージョンをサポートするビルドツールを確認

**モデル読み込みの問題**
- Windows MLとのONNXモデル互換性を検証
- モデルファイルの整合性と形式要件を確認
- 特定のモデルに必要なハードウェア機能要件を確認
- モデル読み込み中のメモリ割り当て問題をデバッグ
- ハードウェア加速のための実行プロバイダー登録を確認

**展開モードの考慮事項**
- **自己完結型モード**: 完全にサポートされるが展開サイズが大きい
- **フレームワーク依存モード**: フットプリントが小さいが共有ランタイムが必要
- **非パッケージ化アプリケーション**: Windows AI APIではサポートされなくなった
- ARM64自己完結型展開のために`dotnet run -p:Platform=ARM64 -p:SelfContained=true`を使用

**パフォーマンスの問題**
- 異なるハードウェア構成全体でアプリケーションパフォーマンスをプロファイル
- AI処理パイプラインのボトルネックを特定
- データ前処理と後処理操作を最適化
- パフォーマンス監視とアラートを実装

**統合の困難**
- 適切なエラーハンドリングを備えたAPI統合問題をデバッグ
- 入力データ形式と前処理要件を検証
- エッジケースとエラー条件を徹底的にテスト
- 本番問題をデバッグするための包括的なログを実装

### デバッグツールと手法

**Visual Studio統合**
- モデル実行分析のためのAI Toolkitデバッガーを使用
- AI操作のパフォーマンスプロファイリングを実装
- 適切な例外処理を備えた非同期AI操作をデバッグ
- 最適化のためのメモリプロファイリングツールを使用

**Windows AI Foundryツール**
- モデルテストと検証のためにFoundry Local CLIを
- [Windows ML 概要](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK システム要件](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK 開発環境のセットアップ](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### サンプルリポジトリとコード
- [Windows App SDK サンプル - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK サンプル - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime 推論例](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK サンプルリポジトリ](https://github.com/microsoft/WindowsAppSDK-Samples)

### 開発ツール
- [Visual Studio Code 用 AI ツールキット](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI 開発ギャラリー](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI サンプル](https://learn.microsoft.com/windows/ai/samples/)
- [モデル変換ツール](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### 技術サポート
- [Windows ML ドキュメント](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime ドキュメント](https://onnxruntime.ai/docs/)
- [Windows App SDK ドキュメント](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [問題報告 - Windows App SDK サンプル](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### コミュニティとサポート
- [Windows 開発者コミュニティ](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry ブログ](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI トレーニング](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*このガイドは、急速に進化する Windows AI エコシステムに合わせて設計されています。定期的な更新により、最新のプラットフォーム機能や開発のベストプラクティスに対応します。*

[08. Microsoft Foundry Local を使った実践 - 完全な開発者ツールキット](../Module08/README.md)

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。