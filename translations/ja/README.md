# EdgeAI for Beginners 


![Course cover image](../../translated_images/ja/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

これらのリソースの使用を開始するには、次の手順に従ってください：

1. **リポジトリをフォークする**: クリック [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discord に参加して、専門家や開発者仲間と交流しましょう**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多言語サポート

#### GitHub Actions によるサポート（自動＆常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](./README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ローカルでクローンすることをお好みですか？**

> このリポジトリには50以上の言語への翻訳が含まれているため、ダウンロードサイズが大幅に増加します。翻訳なしでクローンするには、スパースチェックアウトを使用してください：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> これにより、コースを完了するのに必要なすべてがより高速にダウンロードできます。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**追加の翻訳言語を希望される場合は、[こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)にリストされています。**
## はじめに

**EdgeAI for Beginners**へようこそ。これは、Transformativeなエッジ人工知能の世界への包括的な旅です。このコースは、強力なAI機能とエッジデバイスでの実用的な実装のギャップを埋め、データが生成され意思決定が必要な場所で直接AIの可能性を活用できるようにします。

### マスターできること

このコースでは、基本的な概念から本番稼働可能な実装までを網羅し、以下を学びます：
- **エッジ展開に最適化された小型言語モデル（SLM）**
- **多様なプラットフォームを考慮したハードウェア対応の最適化**
- **プライバシー保護機能を備えたリアルタイム推論**
- **企業アプリケーション向けの本番展開戦略**

### なぜEdgeAIが重要か

Edge AIは、現代の重要な課題に対処するパラダイムシフトを表します：
- **プライバシーとセキュリティ**：クラウドに送信せずに敏感なデータをローカル処理
- **リアルタイムパフォーマンス**：時間に敏感なアプリケーションで遅延を排除
- **コスト効率**：帯域幅およびクラウドコンピューティング費用の削減
- **耐障害性運用**：ネットワーク障害時でも機能維持
- **規制遵守**：データ主権の要件を満たす

### Edge AIとは

Edge AIは、データが生成される場所の近くにあるハードウェア上でAIアルゴリズムと言語モデルをローカルで実行し、推論にクラウドリソースを依存しないことを指します。これにより、遅延が短縮され、プライバシーが強化され、リアルタイムの意思決定が可能になります。

### 基本原則：
- **オンデバイス推論**：AIモデルはエッジデバイス（電話、ルーター、マイクロコントローラー、産業用PC）で実行
- **オフライン対応**：常時インターネット接続を必要としない
- **低遅延**：リアルタイムシステムに適した迅速な応答
- **データ主権**：機密データをローカルに保持し、セキュリティとコンプライアンスを向上

### 小型言語モデル（SLM）

Phi-4、Mistral-7B、GemmaなどのSLMは、より大きなLLMの最適化版であり、以下の点に重点を置いてトレーニングまたは蒸留されています：
- **メモリフットプリントの削減**：限られたエッジデバイスのメモリ使用を効率化
- **計算負荷の軽減**：CPUやエッジGPUのパフォーマンスに最適化
- **高速起動時間**：応答性の高いアプリケーション向けの迅速な初期化

これらは、以下の制約を満たしながら強力な自然言語処理機能を解放します：
- **組み込みシステム**：IoTデバイスや産業用コントローラー
- **モバイルデバイス**：オフライン対応のスマートフォンやタブレット
- **IoTデバイス**：限られたリソースのセンサーやスマートデバイス
- **エッジサーバー**：限られたGPUリソースのローカル処理ユニット
- **パーソナルコンピューター**：デスクトップやノートパソコンの展開シナリオ

## コースモジュールとナビゲーション

| モジュール | トピック | フォーカスエリア | キーコンテンツ | レベル | 所要時間 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI入門](./introduction.md) | 基礎と背景 | EdgeAI概要 • 業界アプリケーション • SLM紹介 • 学習目標 | 初心者 | 1-2時間 |
| [📚 01](../../Module01) | [EdgeAI基礎](./Module01/README.md) | クラウド vs エッジAI比較 | EdgeAI基礎 • 実際のケーススタディ • 実装ガイド • エッジ展開 | 初心者 | 3-4時間 |
| [🧠 02](../../Module02) | [SLMモデル基礎](./Module02/README.md) | モデルファミリー＆アーキテクチャ | Phiファミリー • Qwenファミリー • Gemmaファミリー • BitNET • μModel • Phi-Silica | 初心者 | 4-5時間 |
| [🚀 03](../../Module03) | [SLM展開実践](./Module03/README.md) | ローカル＆クラウド展開 | 応用学習 • ローカル環境 • クラウド展開 | 中級 | 4-5時間 |
| [⚙️ 04](../../Module04) | [モデル最適化ツールキット](./Module04/README.md) | クロスプラットフォーム最適化 | 入門 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • ワークフロー合成 | 中級 | 5-6時間 |
| [🔧 05](../../Module05) | [SLMOps運用](./Module05/README.md) | 本番運用 | SLMOps入門 • モデル蒸留 • ファインチューニング • 本番展開 | 上級 | 5-6時間 |
| [🤖 06](../../Module06) | [AIエージェント＆関数呼び出し](./Module06/README.md) | エージェントフレームワーク＆MCP | エージェント入門 • 関数呼び出し • モデルコンテキストプロトコル | 上級 | 4-5時間 |
| [💻 07](../../Module07) | [プラットフォーム実装](./Module07/README.md) | クロスプラットフォームサンプル | AIツールキット • Foundry Local • Windows開発 | 上級 | 3-4時間 |
| [🏭 08](../../Module08) | [Foundry Localツールキット](./Module08/README.md) | 本番対応サンプル | サンプルアプリケーション（以下参照） | 専門家 | 8-10時間 |

### 🏭 **モジュール08: サンプルアプリケーション**

- [01: RESTチャットクイックスタート](./Module08/samples/01/README.md)
- [02: OpenAI SDK統合](./Module08/samples/02/README.md)
- [03: モデルディスカバリー＆ベンチマーク](./Module08/samples/03/README.md)
- [04: Chainlit RAGアプリケーション](./Module08/samples/04/README.md)
- [05: マルチエージェントオーケストレーション](./Module08/samples/05/README.md)
- [06: モデルズ・アズ・ツールルーター](./Module08/samples/06/README.md)
- [07: ダイレクトAPIクライアント](./Module08/samples/07/README.md)
- [08: Windows 11チャットアプリ](./Module08/samples/08/README.md)
- [09: 高度なマルチエージェントシステム](./Module08/samples/09/README.md)
- [10: Foundryツールフレームワーク](./Module08/samples/10/README.md)

### 🎓 **ワークショップ: 実践学習パス**

本番対応実装を備えた包括的なハンズオンワークショップ資料：

- **[ワークショップガイド](./Workshop/Readme.md)** - 完全な学習目標、成果物、リソースナビゲーション
- **Pythonサンプル**（6セッション） - ベストプラクティス、エラー処理、詳細なドキュメントを更新済み
- **Jupyterノートブック**（8インタラクティブ） - ベンチマークとパフォーマンスモニタリング付き段階的チュートリアル
- **セッションガイド** - 各ワークショップセッションの詳細なマークダウンガイド
- **検証ツール** - コード品質検証およびスモークテスト実行用スクリプト

**作成するもの：**
- ストリーミング対応のローカルAIチャットアプリケーション
- 品質評価付きRAGパイプライン（RAGAS）
- マルチモデルベンチマークと比較ツール
- マルチエージェントオーケストレーションシステム
- タスクベースのインテリジェントモデルルーティング

### 🎙️ **Agentic向けワークショップ：実践 – AIポッドキャストスタジオ**

AI駆動のポッドキャスト制作パイプラインをゼロから構築！この没入型ワークショップでは、アイデアをプロフェッショナルなポッドキャストエピソードに変換するマルチエージェントシステムの完全な作成方法を学習します。
**[🎬 AIポッドキャストスタジオワークショップを始めよう](./WorkshopForAgentic/README.md)**

**あなたのミッション**: "Future Bytes" — 完全に自作のAIエージェントによって運営されるテックポッドキャストを立ち上げよう。クラウド依存なし、APIコストなし — すべてローカルマシンで動作。

**これがユニークな理由:**
- **🤖 真のマルチエージェントオーケストレーション** - 調査、執筆、音声制作を行う専門izedAIエージェントを構築
- **🎯 完全な制作パイプライン** - トピック選定から最終ポッドキャスト音声出力まで
- **💻 100%ローカル展開** - Ollama とローカルモデル（Qwen-3-8B）を使用し、完全なプライバシーと制御を実現
- **🎤 テキスト読み上げ統合** - スクリプトを自然な多人数会話に変換
- **✋ 人間による品質管理ワークフロー** - 承認ゲートで品質を保ちながら自動化

**三幕構成の学習の旅:**

| 幕 | フォーカス | キースキル | 期間 |
|-----|-------|------------|----------|
| **[第1幕: AIアシスタントと出会う](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 最初のAIエージェントを構築 | ツール統合・ウェブ検索・問題解決・エージェント的推論 | 2-3時間 |
| **[第2幕: 制作チームを編成](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 複数のエージェントをオーケストレーション | チーム調整・承認ワークフロー・DevUIインターフェイス・人間の監視 | 3-4時間 |
| **[第3幕: ポッドキャスト制作に挑戦](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | ポッドキャスト音声を生成 | テキスト読み上げ・多人数合成・長時間オーディオ・完全自動化 | 2-3時間 |

**使用技術:**
- **Microsoft Agent Framework** - マルチエージェントのオーケストレーションと調整
- **Ollama** - ローカルAIモデルランタイム（クラウド不要）
- **Qwen-3-8B** - エージェントタスク最適化のためのオープンソース言語モデル
- **テキスト読み上げAPI** - ポッドキャスト生成向けの自然な音声合成

**ハードウェアサポート:**
- ✅ **CPUモード** - どの現代的なPCでも動作（8GB以上のRAM推奨）
- 🚀 **GPUアクセラレーション** - NVIDIA/AMD GPUによる高速推論
- ⚡ **NPUサポート** - 次世代ニューラルプロセッシングユニットによる加速

**こんな方に最適:**
- マルチエージェントAIシステムを学ぶ開発者
- AI自動化とワークフローに興味がある方
- AI支援の制作に挑戦するコンテンツクリエイター
- 実践的なAIオーケストレーションパターンを学ぶ学生

**さあ構築を始めよう**: [🎙️ AIポッドキャストスタジオワークショップ →](./WorkshopForAgentic/README.md)

### 📊 **学習パス概要**
- **総合計時間**: 36-45時間
- **初心者パス**: モジュール01-02 (7-9時間)  
- **中級者パス**: モジュール03-04 (9-11時間)
- **上級者パス**: モジュール05-07 (12-15時間)
- **エキスパートパス**: モジュール08 (8-10時間)

## あなたが構築するもの

### 🎯 コア能力
- **エッジAIアーキテクチャ**: クラウド統合を持つローカル優先のAIシステム設計
- **モデル最適化**: エッジ展開のための量子化と圧縮（85%の速度向上、75%のサイズ削減）
- **マルチプラットフォーム展開**: Windows、モバイル、組み込み、クラウド・エッジハイブリッド
- **制作運用**: エッジAIの監視、スケーリング、維持管理

### 🏗️ 実践プロジェクト
- **Foundry Localチャットアプリ**: モデル切り替え可能なWindows 11ネイティブアプリ
- **マルチエージェントシステム**: 複雑なワークフローのためのコーディネーターと専門エージェント  
- **RAGアプリケーション**: ベクトル検索を用いたローカル文書処理
- **モデルルーター**: タスク解析に基づくモデル自動選択
- **APIフレームワーク**: ストリーミング・ヘルスモニタリング付きの本番クライアント
- **クロスプラットフォームツール**: LangChain/Semantic Kernel統合パターン

### 🏢 業界応用
**製造業**・**ヘルスケア**・**自動運転**・**スマートシティ**・**モバイルアプリ**

## クイックスタート

**推奨学習パス**（全20-30時間）:

0. **📖 入門** ([Introduction.md](./introduction.md))：EdgeAIの基礎＋業界コンテキスト＋学習フレームワーク
1. **📚 基礎**（モジュール01-02）：EdgeAI概念＋SLMモデルファミリー
2. **⚙️ 最適化**（モジュール03-04）：展開＋量子化フレームワーク  
3. **🚀 本番運用**（モジュール05-06）：SLMOps＋AIエージェント＋関数呼び出し
4. **💻 実装**（モジュール07-08）：プラットフォームサンプル＋Foundry Localツールキット

各モジュールは理論、実践演習、本番対応コード例を含む。

## キャリアへの影響

**技術職種**: EdgeAIソリューションアーキテクト・MLエンジニア（エッジ）・IoT AI開発者・モバイルAI開発者

**業界分野**: 製造4.0・ヘルスケアテック・自律システム・フィンテック・コンシューマーエレクトロニクス

**ポートフォリオプロジェクト**: マルチエージェントシステム・本番RAGアプリ・クロスプラットフォーム展開・パフォーマンス最適化

## リポジトリ構成

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## コースのハイライト

✅ **段階的学習**: 理論 → 実践 → 本番展開  
✅ **実際のケーススタディ**: Microsoft、日本航空、企業実装例  
✅ **ハンズオンサンプル**: 50以上の例、10の包括的Foundry Localデモ  
✅ **パフォーマンス重視**: 85%の速度向上、75%のサイズ縮小  
✅ **マルチプラットフォーム対応**: Windows、モバイル、組み込み、クラウド・エッジハイブリッド  
✅ **本番対応**: 監視、スケーリング、セキュリティ、コンプライアンスフレームワーク

📖 **[学習ガイドあり](STUDY_GUIDE.md)**: 時間配分指導と自己評価ツール付きの体系的20時間学習パス。

---

**EdgeAIはAI展開の未来を示します**: ローカル優先、プライバシー重視、効率的。これらのスキルをマスターし、次世代インテリジェントアプリケーションを構築しましょう。

## その他のコース

私たちのチームは他のコースも作成しています！ぜひご覧ください:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilotシリーズ

[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ヘルプを得る

AIアプリの開発で行き詰まったり質問がある場合は、次に参加してください：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

製品のフィードバックや開発中のエラーがある場合は、次をご利用ください：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の言語によるオリジナルの文書が、権威ある情報源とみなされます。重要な情報については、専門の人間翻訳を推奨します。 本翻訳の利用により生じた誤解や誤訳について、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->