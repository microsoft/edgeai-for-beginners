<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T10:23:59+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# EdgeAI入門 


![コースカバー画像](../../translated_images/cover.eb18d1b9605d754b.ja.png)

[![GitHubのコントリビューター](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHubのIssue](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHubのプルリクエスト](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft FoundryのDiscord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

これらのリソースを使い始めるには、次の手順に従ってください:

1. **リポジトリをフォークする**: クリック [![GitHubのフォーク](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **リポジトリをクローンする**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry Discord に参加して、専門家や開発者仲間と交流しましょう**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多言語サポート

#### GitHub Actions によるサポート（自動化＆常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン語](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシア語（ファールシー）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../br/README.md) | [ポルトガル語（ポルトガル）](../pt/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル文字）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**追加の翻訳を希望する場合、サポートされている言語は [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) にリストされています。**
## 導入

**EdgeAI入門**へようこそ — エッジ人工知能の変革的な世界への包括的な旅です。このコースは強力なAI機能とエッジデバイス上での実運用展開のギャップを埋め、データが生成され意思決定が行われる場所で直接AIの可能性を活用できるようにします。

### 習得できる内容

このコースは基本的な概念から本番対応の実装までを扱い、以下をカバーします:
- **小型言語モデル（SLM）**：エッジ展開に最適化されたモデル
- **ハードウェアに配慮した最適化**：多様なプラットフォーム向けの最適化
- **プライバシー保護機能を備えたリアルタイム推論**
- **企業向けアプリケーションの本番展開戦略**

### なぜ EdgeAI が重要か

エッジAIは重要な現代の課題に対応するパラダイムシフトを表しています:
- **プライバシーとセキュリティ**：クラウドへの送信なしに機密データをローカルで処理
- **リアルタイム性能**：時間が重要なアプリケーションでネットワーク遅延を排除
- **コスト効率**：帯域幅とクラウド計算コストを削減
- **回復力のある運用**：ネットワーク停止時でも機能を維持
- **法規制遵守**：データ主権要件を満たす

### エッジAI

エッジAIは、推論のためにクラウドに依存せず、データが生成される場所の近くのハードウェア上でAIアルゴリズムや言語モデルをローカルに実行することを指します。これにより遅延が削減され、プライバシーが強化され、リアルタイムの意思決定が可能になります。

### 基本原則:
- **デバイス上での推論**：AIモデルがエッジデバイス上で動作（スマートフォン、ルーター、マイクロコントローラー、産業用PCなど）
- **オフライン機能**：常時インターネット接続がなくても動作
- **低遅延**：リアルタイムシステムに適した即時応答
- **データ主権**：機密データをローカルに保持し、セキュリティとコンプライアンスを向上

### 小型言語モデル（SLM）

Phi-4、Mistral-7B、Gemma などの SLM は、より大きな LLM を最適化したバージョンで、次の目的のためにトレーニングまたは蒸留されています:
- **メモリフットプリントの削減**：限られたエッジデバイスのメモリを効率的に使用
- **計算要求の低減**：CPUおよびエッジGPU性能向けに最適化
- **高速な起動時間**：応答性の高いアプリケーションのための迅速な初期化

これにより強力なNLP機能を解放しつつ、以下の制約を満たします:
- **組み込みシステム**：IoTデバイスや産業用コントローラー
- **モバイルデバイス**：オフライン機能を持つスマートフォンやタブレット
- **IoTデバイス**：リソースの限られたセンサーやスマートデバイス
- **エッジサーバー**：GPUリソースが限られたローカル処理ユニット
- **パーソナルコンピューター**：デスクトップやノートPCでの展開シナリオ

## コースモジュールとナビゲーション

| モジュール | トピック | フォーカス領域 | 主要内容 | レベル | 所要時間 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI入門](./introduction.md) | 基礎とコンテキスト | EdgeAIの概要 • 業界での適用例 • SLMの紹介 • 学習目標 | 初心者 | 1-2時間 |
| [📚 01](../../Module01) | [EdgeAIの基礎](./Module01/README.md) | クラウドとエッジAIの比較 | EdgeAIの基礎 • 実際の事例研究 • 実装ガイド • エッジ展開 | 初心者 | 3-4時間 |
| [🧠 02](../../Module02) | [SLMモデルの基礎](./Module02/README.md) | モデルファミリーとアーキテクチャ | Phi ファミリー • Qwen ファミリー • Gemma ファミリー • BitNET • μModel • Phi-Silica | 初心者 | 4-5時間 |
| [🚀 03](../../Module03) | [SLM展開実践](./Module03/README.md) | ローカルとクラウドの展開 | 高度な学習 • ローカル環境 • クラウド展開 | 中級 | 4-5時間 |
| [⚙️ 04](../../Module04) | [モデル最適化ツールキット](./Module04/README.md) | クロスプラットフォーム最適化 | 導入 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • ワークフロー合成 | 中級 | 5-6時間 |
| [🔧 05](../../Module05) | [SLMOpsの本番運用](./Module05/README.md) | 本番運用 | SLMOpsの紹介 • モデル蒸留 • ファインチューニング • 本番展開 | 上級 | 5-6時間 |
| [🤖 06](../../Module06) | [AIエージェントと関数呼び出し](./Module06/README.md) | エージェントフレームワークとMCP | エージェント紹介 • 関数呼び出し • モデルコンテキストプロトコル | 上級 | 4-5時間 |
| [💻 07](../../Module07) | [プラットフォーム実装](./Module07/README.md) | クロスプラットフォームのサンプル | AIツールキット • Foundry Local • Windows開発 | 上級 | 3-4時間 |
| [🏭 08](../../Module08) | [Foundry Local ツールキット](./Module08/README.md) | 本番対応サンプル | サンプルアプリケーション（下記参照） | エキスパート | 8-10時間 |

### 🏭 **モジュール08：サンプルアプリケーション**

- [01: REST Chat クイックスタート](./Module08/samples/01/README.md)
- [02: OpenAI SDK 統合](./Module08/samples/02/README.md)
- [03: モデル発見とベンチマーキング](./Module08/samples/03/README.md)
- [04: Chainlit RAG アプリケーション](./Module08/samples/04/README.md)
- [05: マルチエージェントオーケストレーション](./Module08/samples/05/README.md)
- [06: Models-as-Tools ルーター](./Module08/samples/06/README.md)
- [07: 直接APIクライアント](./Module08/samples/07/README.md)
- [08: Windows 11 チャットアプリ](./Module08/samples/08/README.md)
- [09: 高度なマルチエージェントシステム](./Module08/samples/09/README.md)
- [10: Foundry Tools フレームワーク](./Module08/samples/10/README.md)

### 🎓 **ワークショップ：ハンズオン学習パス**

本番対応実装を含む包括的なハンズオンワークショップ資料:

- **[ワークショップガイド](./Workshop/Readme.md)** - 完全な学習目標、成果、およびリソースナビゲーション
- Pythonサンプル（6セッション） - ベストプラクティス、エラーハンドリング、および包括的なドキュメントで更新
- Jupyterノートブック（8本のインタラクティブ） - ベンチマークとパフォーマンス監視を含むステップバイステップのチュートリアル
- セッションガイド - 各ワークショップセッションの詳細なマークダウンガイド
- 検証ツール - コード品質の検証やスモークテストを実行するスクリプト

構築するもの:
- ストリーミング対応のローカルAIチャットアプリケーション
- 品質評価付きRAGパイプライン（RAGAS）
- 複数モデルのベンチマーキングおよび比較ツール
- マルチエージェントオーケストレーションシステム
- タスクベースの選択によるインテリジェントなモデルルーティング

### 📊 **学習パスの概要**
- **合計所要時間**：36-45時間
- **初心者向け**：モジュール01-02（7-9時間）  
- **中級向け**：モジュール03-04（9-11時間）
- **上級向け**：モジュール05-07（12-15時間）
- **エキスパート向け**：モジュール08（8-10時間）

## 構築するもの

### 🎯 コアコンピテンシー
- **Edge AIアーキテクチャ**：クラウド統合を備えたローカルファーストのAIシステムを設計する
- **モデル最適化**: エッジ展開のためにモデルを量子化および圧縮（速度85%向上、サイズ75%削減）
- **マルチプラットフォーム展開**: Windows、モバイル、組み込み、クラウド-エッジハイブリッドシステム
- **本番運用**: 本番環境におけるエッジAIの監視、スケーリング、保守

### 🏗️ 実践プロジェクト
- **Foundry ローカルチャットアプリ**: モデル切替を備えた Windows 11 ネイティブアプリケーション
- **マルチエージェントシステム**: 複雑なワークフローのためのコーディネーターと専門エージェント  
- **RAGアプリケーション**: ベクトル検索によるローカル文書処理
- **モデルルーター**: タスク分析に基づくモデル間のインテリジェントな選択
- **APIフレームワーク**: ストリーミングとヘルスモニタリングを備えた本番対応クライアント
- **クロスプラットフォームツール**: LangChain/Semantic Kernel の統合パターン

### 🏢 業界向けアプリケーション
**製造業** • **ヘルスケア** • **自動運転車** • **スマートシティ** • **モバイルアプリ**

## クイックスタート

**推奨学習パス** (合計20〜30時間):

0. **📖 はじめに** ([Introduction.md](./introduction.md)): エッジAIの基礎 + 業界の文脈 + 学習フレームワーク
1. **📚 基礎** (Modules 01-02): エッジAIの概念 + SLM モデルファミリー
2. **⚙️ 最適化** (Modules 03-04): デプロイメント + 量子化フレームワーク  
3. **🚀 本番** (Modules 05-06): SLMOps + AI エージェント + 関数呼び出し
4. **💻 実装** (Modules 07-08): プラットフォームサンプル + Foundry Local ツールキット

各モジュールには理論、ハンズオン演習、および本番対応のコードサンプルが含まれます。

## キャリアへの影響

**技術職**: エッジAIソリューションアーキテクト • MLエンジニア（エッジ） • IoT AI開発者 • モバイルAI開発者

**業界セクター**: 製造業4.0 • ヘルステック • 自律システム • FinTech • コンシューマーエレクトロニクス

**ポートフォリオプロジェクト**: マルチエージェントシステム • 本番RAGアプリ • クロスプラットフォーム展開 • パフォーマンス最適化

## Repository Structure

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
✅ **実例ケーススタディ**: Microsoft、Japan Airlines、企業導入事例  
✅ **ハンズオンサンプル**: 50以上の例、10の包括的なFoundry Localデモ  
✅ **パフォーマンス重視**: 速度85%改善、サイズ75%削減  
✅ **マルチプラットフォーム**: Windows、モバイル、組み込み、クラウド-エッジハイブリッド  
✅ **本番対応**: 監視、スケーリング、セキュリティ、コンプライアンスフレームワーク

📖 **[学習ガイドあり](STUDY_GUIDE.md)**: 時間配分ガイダンスと自己評価ツールを含む構造化された20時間学習パス。

---

**エッジAIはAI展開の未来を表します**: ローカルファースト、プライバシー保護、効率的。これらのスキルを習得し、次世代のインテリジェントなアプリケーションを構築しましょう。

## その他のコース

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 入門](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD 入門](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI 入門](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 入門](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI エージェント入門](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![生成AI 入門](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成AI（.NET）入門](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成AI（Java）入門](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成AI（JavaScript）入門](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コア学習
[![機械学習入門](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![データサイエンス入門](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI入門](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![サイバーセキュリティ入門](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web開発入門](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT入門](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR開発入門](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot シリーズ
[![Copilot（AIペアプログラミング）](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot（C#/.NET）](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilotアドベンチャー](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## サポート

If you get stuck or have any questions about building AI apps, join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you have product feedback or errors while building visit:

[![Microsoft Foundry 開発者フォーラム](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書は AI 翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の確保に努めていますが、自動翻訳には誤りや不正確な箇所が含まれている可能性があることにご留意ください。重要な情報については、原文（原言語による文書）を正式な出典として参照してください。重要な内容に関しては、専門の人間による翻訳をお勧めします。本翻訳の利用により生じた誤解や解釈の相違について、当社は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->