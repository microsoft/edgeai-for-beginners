<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8de8ce76af1af156b1c2dee24ed23b0",
  "translation_date": "2025-12-24T23:21:08+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向け EdgeAI 


![コースカバー画像](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ja.png)

[![GitHub コントリビューター](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub イシュー](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub プルリクエスト](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![プルリクエスト歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry の Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

これらのリソースを使って始めるには、次の手順に従ってください:

1. **リポジトリをフォークする**: クリック [![GitHub フォーク](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **リポジトリをクローンする**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry の Discord に参加して、専門家や開発者仲間と交流する**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多言語サポート

#### GitHub Actions によるサポート（自動化・常時最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤーラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシア語（ファールシー）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../br/README.md) | [ポルトガル語（ポルトガル）](../pt/README.md) | [パンジャーブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**追加の翻訳を希望する場合、サポートされている言語は[こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)に記載されています**
## はじめに

EdgeAI for Beginners へようこそ — エッジ人工知能の革新的な世界への包括的な旅です。本コースは強力な AI 機能とエッジデバイス上での実用的な展開とのギャップを埋め、データが生成され意思決定が行われる場所で直接 AI の潜在力を活用できるようにします。

### 習得する内容

このコースでは、基礎概念から本番対応の実装までを扱います。主な内容は次の通りです:
- **エッジ向けに最適化された小型言語モデル（SLM）**
- **ハードウェアに配慮した最適化**（多様なプラットフォームに対応）
- **プライバシー保護機能を備えたリアルタイム推論**
- **エンタープライズアプリ向けの本番導入戦略**

### なぜ EdgeAI が重要か

Edge AI は現代の重要な課題に対応するパラダイムシフトをもたらします:
- **プライバシーとセキュリティ**: データをクラウドにさらすことなくローカルで処理
- **リアルタイム性能**: 時間に敏感なアプリケーションでネットワーク遅延を排除
- **コスト効率**: 帯域幅やクラウド計算コストの削減
- **堅牢な運用**: ネットワーク障害時にも機能を維持
- **規制遵守**: データ主権要件の遵守

### Edge AI

Edge AI は、推論のためにクラウド資源に依存せず、データが生成される場所に近いハードウェア上で AI アルゴリズムや言語モデルを実行することを指します。これによりレイテンシが低減し、プライバシーが強化され、リアルタイムの意思決定が可能になります。

### コア原則:
- **オンデバイス推論**: AI モデルはエッジデバイス（携帯電話、ルーター、マイクロコントローラー、産業用 PC）上で実行されます
- **オフライン機能**: 常時接続のインターネットなしで機能
- **低レイテンシ**: リアルタイムシステムに適した即時応答
- **データ主権**: 機密データをローカルに保持し、セキュリティとコンプライアンスを向上

### 小型言語モデル（SLM）

Phi-4、Mistral-7B、Gemma のような SLM は、より大きな LLM を最適化したバージョンであり、以下のために訓練または蒸留されています:
- **メモリフットプリントの削減**: 制限されたエッジデバイスのメモリで効率的に使用
- **計算要求の低減**: CPU およびエッジ GPU のパフォーマンス向けに最適化
- **起動時間の短縮**: 応答性の高いアプリケーション向けの迅速な初期化

これらは強力な NLP 機能を解放しつつ、次のような制約を満たします:
- **組み込みシステム**: IoT デバイスや産業用コントローラー
- **モバイルデバイス**: オフライン機能を持つスマートフォンやタブレット
- **IoT デバイス**: 限られたリソースのセンサーやスマートデバイス
- **エッジサーバー**: 限られた GPU リソースを持つローカル処理ユニット
- **パーソナルコンピュータ**: デスクトップやラップトップへの展開シナリオ

## コースモジュールとナビゲーション

| モジュール | トピック | フォーカス領域 | 主な内容 | レベル | 所要時間 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduction to EdgeAI](./introduction.md) | 基礎と背景 | EdgeAI 概要 • 業界での適用例 • SLM 入門 • 学習目標 | 初心者 | 1-2 hrs |
| [📚 01](../../Module01) | [EdgeAI Fundamentals](./Module01/README.md) | クラウド vs エッジ AI の比較 | EdgeAI 基礎 • 実世界のケーススタディ • 実装ガイド • エッジ展開 | 初心者 | 3-4 hrs |
| [🧠 02](../../Module02) | [SLM Model Foundations](./Module02/README.md) | モデルファミリーとアーキテクチャ | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | 初心者 | 4-5 hrs |
| [🚀 03](../../Module03) | [SLM Deployment Practice](./Module03/README.md) | ローカルおよびクラウド展開 | 高度な学習 • ローカル環境 • クラウド展開 | 中級 | 4-5 hrs |
| [⚙️ 04](../../Module04) | [Model Optimization Toolkit](./Module04/README.md) | クロスプラットフォーム最適化 | 導入 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • ワークフロー合成 | 中級 | 5-6 hrs |
| [🔧 05](../../Module05) | [SLMOps Production](./Module05/README.md) | プロダクション運用 | SLMOps 入門 • モデル蒸留 • ファインチューニング • 本番デプロイ | 上級 | 5-6 hrs |
| [🤖 06](../../Module06) | [AI Agents & Function Calling](./Module06/README.md) | エージェントフレームワークとMCP | エージェント入門 • 関数呼び出し • モデルコンテキストプロトコル | 上級 | 4-5 hrs |
| [💻 07](../../Module07) | [Platform Implementation](./Module07/README.md) | クロスプラットフォームサンプル | AI ツールキット • Foundry Local • Windows 開発 | 上級 | 3-4 hrs |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | 本番対応サンプル | サンプルアプリケーション（詳細は下記） | エキスパート | 8-10 hrs |

### 🏭 **モジュール08：サンプルアプリケーション**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Model Discovery & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Application](./Module08/samples/04/README.md)
- [05: Multi-Agent Orchestration](./Module08/samples/05/README.md)
- [06: ツールとしてのモデル ルーター](./Module08/samples/06/README.md)
- [07: Direct API Client](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Advanced Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **ワークショップ：ハンズオン学習パス**

本番対応の実装を含む包括的なハンズオンワークショップ資料：

- **[ワークショップガイド](./Workshop/Readme.md)** - 完全な学習目標、成果、およびリソースのナビゲーション
- Python サンプル（6セッション） - ベストプラクティス、エラーハンドリング、包括的なドキュメントで更新
- Jupyter ノートブック（8本、対話式） - ベンチマークとパフォーマンス監視を含むステップバイステップのチュートリアル
- セッションガイド - 各ワークショップセッションの詳細なマークダウンガイド
- 検証ツール - コード品質を検証しスモークテストを実行するスクリプト

**作るもの:**
- ストリーミング対応のローカルAIチャットアプリケーション
- 品質評価付き RAG パイプライン（RAGAS）
- マルチモデルのベンチマークと比較ツール
- マルチエージェントオーケストレーションシステム
- タスクベースの選択によるインテリジェントなモデルルーティング

### 📊 **学習パスの要約**
- **総所要時間**: 36-45 hours
- **初心者パス**: モジュール 01-02 (7-9 時間)  
- **中級パス**: モジュール 03-04 (9-11 時間)
- **上級パス**: モジュール 05-07 (12-15 時間)
- **エキスパートパス**: モジュール 08 (8-10 時間)

## 作るもの

### 🎯 コアコンピテンシー
- **Edge AI アーキテクチャ**: クラウド統合を伴うローカルファーストのAIシステムを設計する
- **Model Optimization**: エッジ展開向けにモデルを量子化および圧縮（85%の速度向上、75%のサイズ削減）
- **Multi-Platform Deployment**: Windows、モバイル、組み込み、クラウド-エッジのハイブリッドシステム
- **Production Operations**: 本番環境でのエッジAIの監視、スケーリング、運用保守

### 🏗️ 実践プロジェクト
- **Foundry Local Chat Apps**: モデル切替機能を備えたWindows 11ネイティブアプリケーション
- **Multi-Agent Systems**: 複雑なワークフローのためのコーディネータと専門エージェント  
- **RAG Applications**: ベクトル検索を用いたローカル文書処理
- **Model Routers**: タスク解析に基づくモデル間のインテリジェントな選択
- **API Frameworks**: ストリーミングとヘルスモニタリングを備えた本番対応クライアント
- **Cross-Platform Tools**: LangChain/Semantic Kernel 統合パターン

### 🏢 業界向け応用
**製造業** • **ヘルスケア** • **自動運転車** • **スマートシティ** • **モバイルアプリ**

## Quick Start

**推奨学習パス** (合計20〜30時間):

0. **📖 Introduction** ([Introduction.md](./introduction.md)): EdgeAIの基礎 + 業界コンテキスト + 学習フレームワーク
1. **📚 Foundation** (モジュール 01-02): EdgeAIの概念 + SLMモデルファミリー
2. **⚙️ Optimization** (モジュール 03-04): デプロイメント + 量子化フレームワーク  
3. **🚀 Production** (モジュール 05-06): SLMOps + AIエージェント + 関数呼び出し
4. **💻 Implementation** (モジュール 07-08): プラットフォームサンプル + Foundry Local ツールキット

各モジュールには理論、ハンズオン演習、本番対応のコードサンプルが含まれます。

## Career Impact

**技術職**: EdgeAIソリューションアーキテクト • MLエンジニア（Edge） • IoT AI開発者 • モバイルAI開発者

**産業分野**: 製造業4.0 • ヘルスケア技術 • 自律システム • FinTech • コンシューマーエレクトロニクス

**ポートフォリオプロジェクト**: マルチエージェントシステム • 本番用RAGアプリ • クロスプラットフォーム展開 • パフォーマンス最適化

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

## Course Highlights

✅ **段階的学習**: 理論 → 実践 → 本番展開  
✅ **実際のケーススタディ**: Microsoft、Japan Airlines、企業実装  
✅ **ハンズオンサンプル**: 50+ の例、10の包括的な Foundry Local デモ  
✅ **パフォーマンス重視**: 85% の速度向上、75% のサイズ削減  
✅ **マルチプラットフォーム**: Windows、モバイル、組み込み、クラウド-エッジハイブリッド  
✅ **本番対応**: 監視、スケーリング、セキュリティ、コンプライアンスのフレームワーク

📖 **[学習ガイドあり](STUDY_GUIDE.md)**: 時間配分ガイダンスと自己評価ツールを含む、構造化された20時間の学習パス。

---

**EdgeAIはAI展開の未来を代表します**: ローカルファースト、プライバシー保護、効率性。これらのスキルを習得して次世代のインテリジェントなアプリケーションを構築しましょう。

## Other Courses

私たちのチームは他のコースも制作しています！ぜひご覧ください：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 入門](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / エージェント
[![AZD 入門](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI 入門](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 入門](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AIエージェント入門](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成AIシリーズ
[![生成AI 入門](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コア学習
[![機械学習 入門](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![データサイエンス 入門](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 入門](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![サイバーセキュリティ 入門](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web開発 入門](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT 入門](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR開発 入門](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot シリーズ
[![AIペアプログラミング向け Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET 向け Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilotアドベンチャー](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Getting Help

困ったときやAIアプリの構築について質問がある場合は、参加してください：

[![Microsoft Foundry のDiscord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

製品に関するフィードバックや構築中のエラーがある場合は、次をご覧ください：

[![Microsoft Foundry 開発者フォーラム](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項:
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を用いて翻訳されました。正確性に努めていますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知ください。原文（原言語の文書）を正本としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当社は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->