<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "56dfdb5231720282ba90359277270086",
  "translation_date": "2025-09-15T15:16:45+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# 初心者向けEdgeAI

![コース表紙画像](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ja.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

以下の手順に従って、このリソースを使い始めましょう：

1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork) をクリック  
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Azure AI Foundry Discordに参加して、専門家や開発者仲間と交流する**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多言語対応

#### GitHub Actionによるサポート (自動化 & 常に最新)

[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [中国語 (簡体字)](../zh/README.md) | [中国語 (繁体字, マカオ)](../mo/README.md) | [中国語 (繁体字, 香港)](../hk/README.md) | [中国語 (繁体字, 台湾)](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md)  
**追加の翻訳を希望する場合は、対応可能な言語が [こちら](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) に記載されています**

## はじめに

初心者向けEdgeAIへようこそ。ここでは、言語モデルの力とローカルデバイスの効率性が融合します。このコースでは、小型で最適化された言語モデル (SLM) が、クラウドアクセスを必要とせずにスマートフォン、IoTボード、コンパクトサーバーなどのエッジハードウェア上で直接動作する方法を紹介します。リアルタイムでプライバシーを重視したAI推論が、スマートホーム、産業モニタリング、オフラインアプリケーションをどのように変革しているかを学び、速度、セキュリティ、モジュール性に特化した軽量な展開を体験します。

### Edge AI

Edge AIとは、AIアルゴリズムや言語モデルをローカルハードウェア上で実行し、データが生成される場所に近い環境で動作させることを指します。クラウドリソースに依存せずに推論を行うことで、遅延を削減し、プライバシーを向上させ、リアルタイムの意思決定を可能にします。

### コア原則:
- **オンデバイス推論**: AIモデルがエッジデバイス (スマートフォン、ルーター、マイクロコントローラー、産業用PC) 上で動作  
- **オフライン機能**: 常時インターネット接続なしで動作  
- **低遅延**: リアルタイムシステムに適した即時応答  
- **データ主権**: 敏感なデータをローカルに保持し、セキュリティとコンプライアンスを向上  

**小型言語モデル (SLM)**  
Phi-4、Mistral-7B、GemmaなどのSLMは、大型LLMの最適化版であり、以下の特徴を持ちます:
- メモリ使用量の削減  
- 計算負荷の軽減  
- 起動時間の短縮  

これらは以下の制約を満たしながら強力なNLP機能を提供します:
- 組み込みシステム  
- モバイルデバイス  
- IoTデバイス  
- GPUが限られたエッジサーバー  
- パーソナルコンピュータ  

## コース構成

### [モジュール01: EdgeAIの基礎と変革](./Module01/README.md)  
**テーマ**: EdgeAI展開の変革的なシフト  

#### チャプター構成:
- [**セクション1: EdgeAIの基礎**](./Module01/01.EdgeAIFundamentals.md)  
  - 従来のクラウドAIとEdgeAIの比較  
  - エッジコンピューティングの課題と制約  
  - 主要技術: モデル量子化、圧縮最適化、小型言語モデル (SLM)  
  - ハードウェアアクセラレーション: NPU、GPU最適化、CPU最適化  
  - 利点: プライバシーセキュリティ、低遅延、オフライン機能、コスト効率  

- [**セクション2: 実世界のケーススタディ**](./Module01/02.RealWorldCaseStudies.md)  
  - Microsoft Phi & Muモデルエコシステム  
  - 日本航空のAI報告システムのケーススタディ  
  - 市場への影響と将来の方向性  
  - 展開の考慮事項とベストプラクティス  

- [**セクション3: 実践的な実装ガイド**](./Module01/03.PracticalImplementationGuide.md)  
  - 開発環境のセットアップ (Python 3.10+, .NET 8+)  
  - ハードウェア要件と推奨構成  
  - コアモデルファミリーリソース  
  - 量子化と最適化ツール (Llama.cpp、Microsoft Olive、Apple MLX)  
  - 評価と検証チェックリスト  

- [**セクション4: EdgeAI展開ハードウェアプラットフォーム**](./Module01/04.EdgeDeployment.md)  
  - EdgeAI展開の考慮事項と要件  
  - Intel EdgeAIハードウェアと最適化技術  
  - モバイルおよび組み込みシステム向けQualcomm AIソリューション  
  - NVIDIA Jetsonとエッジコンピューティングプラットフォーム  
  - NPUアクセラレーションを備えたWindows AI PCプラットフォーム  
  - ハードウェア固有の最適化戦略  

---

### [モジュール02: 小型言語モデルの基礎](./Module02/README.md)  
**テーマ**: SLMの理論的原則、実装戦略、そして本番展開  

#### チャプター構成:
- [**セクション1: Microsoft Phiモデルファミリーの基礎**](./Module02/01.PhiFamily.md)  
  - デザイン哲学の進化 (Phi-1からPhi-4)  
  - 効率性を重視したアーキテクチャ設計  
  - 特化した能力 (推論、マルチモーダル、エッジ展開)  

- [**セクション2: Qwenファミリーの基礎**](./Module02/02.QwenFamily.md)  
  - オープンソースの卓越性 (Qwen 1.0からQwen3) - Hugging Faceで利用可能  
  - 思考モード機能を備えた高度な推論アーキテクチャ  
  - スケーラブルな展開オプション (0.5B-235Bパラメータ)  

- [**セクション3: Gemmaファミリーの基礎**](./Module02/03.GemmaFamily.md)  
  - 研究主導の革新 (Gemma 3 & 3n)  
  - マルチモーダルの卓越性  
  - モバイル優先のアーキテクチャ  

- [**セクション4: BitNETファミリーの基礎**](./Module02/04.BitNETFamily.md)  
  - 革新的な量子化技術 (1.58ビット)  
  - https://github.com/microsoft/BitNet からの特化推論フレームワーク  
  - 極限効率による持続可能なAIリーダーシップ  

- [**セクション5: Microsoft Muモデルの基礎**](./Module02/05.mumodel.md)  
  - Windows 11に組み込まれたデバイス優先アーキテクチャ  
  - Windows 11設定とのシステム統合  
  - プライバシーを保護するオフライン操作  

- [**セクション6: Phi-Silicaの基礎**](./Module02/06.phisilica.md)  
  - Windows 11 Copilot+ PCに組み込まれたNPU最適化アーキテクチャ  
  - 卓越した効率性 (1.5Wで650トークン/秒)  
  - Windows App SDKとの開発者統合  

---

### [モジュール03: 小型言語モデルの展開](./Module03/README.md)  
**テーマ**: 理論から本番環境までのSLMライフサイクル展開  

#### チャプター構成:
- [**セクション1: SLM高度学習**](./Module03/01.SLMAdvancedLearning.md)  
  - パラメータ分類フレームワーク (Micro SLM 100M-1.4B, Medium SLM 14B-30B)  
  - 高度な最適化技術 (量子化方法、BitNET 1ビット量子化)  
  - モデル取得戦略 (PhiモデルはAzure AI Foundry、選択モデルはHugging Face)  

- [**セクション2: ローカル環境での展開**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Ollamaユニバーサルプラットフォーム展開  
  - Microsoft Foundryローカルエンタープライズソリューション  
  - フレームワーク比較分析  

- [**セクション3: コンテナ化されたクラウド展開**](./Module03/03.DeployingSLMinCloud.md)  
  - vLLM高性能推論展開  
  - Ollamaコンテナオーケストレーション  
  - ONNX Runtimeエッジ最適化実装  

---

### [モジュール04: モデル形式変換と量子化](./Module04/README.md)  
**テーマ**: プラットフォームを超えたエッジ展開のための完全なモデル最適化ツールキット  

#### チャプター構成:
- [**セクション1: モデル形式変換と量子化の基礎**](./Module04/01.Introduce.md)  
  - 精度分類フレームワーク (超低精度、低精度、中精度)  
  - GGUFとONNX形式の利点と使用例  
  - 運用効率向上のための量子化の利点  
  - パフォーマンスベンチマークとメモリ使用量比較  

- [**セクション2: Llama.cpp実装ガイド**](./Module04/02.Llamacpp.md)  
  - クロスプラットフォームインストール (Windows、macOS、Linux)  
  - GGUF形式変換と量子化レベル (Q2_KからQ8_0)  
  - ハードウェアアクセラレーション (CUDA、Metal、OpenCL、Vulkan)  
  - Python統合とREST API展開  

- [**セクション3: Microsoft Olive最適化スイート**](./Module04/03.MicrosoftOlive.md)  
  - 40以上の組み込みコンポーネントによるハードウェア対応モデル最適化  
  - 動的および静的量子化による自動最適化  
  - Azure MLワークフローとのエンタープライズ統合  
  - 人気モデルのサポート (Llama、Phi、選択されたQwenモデル、Gemma)  

- [**セクション4: Apple MLXフレームワークの詳細**](./Module04/04.AppleMLX.md)  
  - Apple Siliconの統一メモリアーキテクチャ  
  - LLaMA、Mistral、Phi-3、選択されたQwenモデルのサポート  
  - LoRA微調整とモデルカスタマイズ  
  - Hugging Faceとの統合 (4ビット/8ビット量子化)  

---

### [モジュール05: SLMOps - 小型言語モデルの運用](./Module05/README.md)  
**テーマ**: 蒸留から本番展開までのSLMライフサイクル運用  

#### チャプター構成:
- [**セクション1: SLMOpsの紹介**](./Module05/01.IntroduceSLMOps.md)  
  - SLMOpsによるAI運用のパラダイムシフト  
  - コスト効率とプライバシー優先アーキテクチャ  
  - 戦略的ビジネスインパクトと競争優位性  
  - 実世界での実装課題と解決策  

- [**セクション2: モデル蒸留 - 理論から実践へ**](./Module05/02.SLMOps-Distillation.md)  
  - 教師モデルから生徒モデルへの知識移転  
  - 2段階蒸留プロセスの実装  
  - 実践例を含むAzure ML蒸留ワークフロー  
  - 推論時間85%削減、精度92%保持  

- [**セクション3: 微調整 - 特定タスク向けモデルのカスタマイズ**](./Module05/03.SLMOps-Finetuing.md)  
  - パラメータ効率の高い微調整 (PEFT) 技術  
  - LoRAとQLoRAの高度な方法  
  - Microsoft Oliveによる微調整実装  
  - マルチアダプタートレーニングとハイパーパラメータ最適化  

- [**セクション4: 展開 - 本番対応の実装**](./Module05/04.SLMOps.Deployment.md)  
  - 本番向けのモデル変換と量子化  
  - Foundry Local展開構成  
  - パフォーマンスベンチマークと品質検証  
  - サイズ75%削減と本番監視  

---

### [モジュール06: SLMエージェントシステム - AIエージェントと機能呼び出し](./Module06/README.md)  
**テーマ**: 基礎から高度な機能呼び出しとモデルコンテキストプロトコル統合までのSLMエージェントシステムの実装  

#### チャプター構成:
- [**セクション1: AIエージェントと小型言語モデルの基礎**](./Module06/01.IntroduceAgent.md)  
  - エージェント分類フレームワーク (反射型、モデルベース型、目標ベース型、学習エージェント)  
  - SLMの基礎と最適化戦略 (GGUF、量子化、エッジフレームワーク)  
  - SLMとLLMのトレードオフ分析 (コスト10-30倍削減、タスク効果70-80%)  
- Ollama、VLLM、Microsoft Edgeソリューションを活用した実践的なデプロイメント

- [**セクション2: 小型言語モデルにおける関数呼び出し**](./Module06/02.FunctionCalling.md)
  - システマティックなワークフロー実装（意図検出、JSON出力、外部実行）
  - プラットフォーム固有の実装（Phi-4-mini、選択されたQwenモデル、Microsoft Foundry Local）
  - 高度な例（マルチエージェント協力、動的ツール選択）
  - 本番環境での考慮事項（レート制限、監査ログ、セキュリティ対策）

- [**セクション3: モデルコンテキストプロトコル (MCP) の統合**](./Module06/03.IntroduceMCP.md)
  - プロトコルアーキテクチャと階層型システム設計
  - マルチバックエンド対応（開発用Ollama、運用用vLLM）
  - 接続プロトコル（STDIOおよびSSEモード）
  - 実際のアプリケーション（ウェブ自動化、データ処理、API統合）

---

### [モジュール07: EdgeAI実装サンプル](./Module07/README.md)
**テーマ**: 多様なプラットフォームとフレームワークにわたる包括的なEdgeAI実装

#### 章構成:
- [**NVIDIA Jetson Orin NanoでのEdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - クレジットカードサイズのフォームファクターで67 TOPSのAI性能
  - ジェネレーティブAIモデルのサポート（ビジョントランスフォーマー、LLM、ビジョン言語モデル）
  - ロボティクス、ドローン、インテリジェントカメラ、自律型デバイスでの応用
  - AI開発を民主化する手頃な価格の$249プラットフォーム

- [**.NET MAUIとONNX Runtime GenAIを活用したモバイルアプリケーションでのEdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 単一のC#コードベースによるクロスプラットフォームモバイルAI
  - ハードウェアアクセラレーションのサポート（CPU、GPU、モバイルAIプロセッサ）
  - プラットフォーム固有の最適化（iOS向けCoreML、Android向けNNAPI）
  - 完全なジェネレーティブAIループの実装

- [**Azureでの小型言語モデルエンジンを活用したEdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - クラウドとエッジのハイブリッドデプロイメントアーキテクチャ
  - Azure AIサービスとONNX Runtimeの統合
  - エンタープライズ規模のデプロイメントと継続的なモデル管理
  - インテリジェントな文書処理のためのハイブリッドAIワークフロー

- [**Windows MLを活用したEdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 高性能なオンデバイス推論のためのWindows AI Foundry基盤
  - 普遍的なハードウェアサポート（AMD、Intel、NVIDIA、Qualcommシリコン）
  - 自動ハードウェア抽象化と最適化
  - 多様なWindowsハードウェアエコシステム向けの統一フレームワーク

- [**Foundry Localアプリケーションを活用したEdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - プライバシー重視のRAG実装とローカルリソース
  - Phi-3言語モデルとセマンティック検索の統合（Phiモデルのみ）
  - ローカルベクトルデータベースのサポート（SQLite、Qdrant）
  - データ主権とオフライン操作の能力

## 学習成果概要

### モジュール01の学習成果:
- クラウドとエッジAIアーキテクチャの基本的な違いを理解する
- エッジデプロイメントのためのコア最適化技術を習得する
- 実際の応用例と成功事例を認識する
- EdgeAIソリューションを実装するための実践的なスキルを習得する

### モジュール02の学習成果:
- 異なるSLM設計哲学とそのデプロイメントへの影響を深く理解する
- 計算制約と性能要件に基づく戦略的意思決定能力を習得する
- デプロイメントの柔軟性に関するトレードオフを理解する
- 効率的なAIアーキテクチャに関する未来志向の洞察を持つ

### モジュール03の学習成果:
- 戦略的なモデル選択能力を習得する
- 最適化技術の習得
- デプロイメントの柔軟性を習得する
- 本番環境での構成能力を持つ

### モジュール04の学習成果:
- 量子化の境界と実際の応用を深く理解する
- 複数の最適化フレームワーク（Llama.cpp、Olive、MLX）を使った実践的な経験を得る
- ハードウェアに応じた最適化選択能力を習得する
- クロスプラットフォームエッジコンピューティング環境での本番デプロイメントスキルを習得する

### モジュール05の学習成果:
- SLMOpsのパラダイムと運用原則を習得する
- 知識移転と効率最適化のためのモデル蒸留を実装する
- ドメイン固有のモデルカスタマイズのための微調整技術を適用する
- モニタリングと保守戦略を備えた本番対応SLMソリューションをデプロイする

### モジュール06の学習成果:
- AIエージェントと小型言語モデルのアーキテクチャの基本概念を理解する
- 複数のプラットフォームとフレームワークにわたる関数呼び出しの実装を習得する
- モデルコンテキストプロトコル (MCP) を統合して標準化された外部ツールとの相互作用を実現する
- 最小限の人間の介入で高度なエージェントシステムを構築する

### モジュール07の学習成果:
- 多様なEdgeAIプラットフォームと実装戦略に関する実践的な経験を得る
- NVIDIA、モバイル、Azure、Windowsプラットフォームにわたるハードウェア固有の最適化技術を習得する
- 性能、コスト、プライバシー要件の間のデプロイメントトレードオフを理解する
- 異なるエコシステムで実際のEdgeAIアプリケーションを構築するための実践的なスキルを開発する

## ファイル構造ツリーダイアグラム

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.AppleMLX.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## コースの特徴

- **段階的学習**: 基本概念から高度なデプロイメントまで徐々に進む
- **理論と実践の統合**: 各モジュールには理論的基盤と実践的操作が含まれる
- **実際のケーススタディ**: Microsoft、Alibaba、Googleなどの実際のケースに基づく
- **実践的な練習**: 完全な構成ファイル、APIテスト手順、デプロイメントスクリプト
- **性能ベンチマーク**: 推論速度、メモリ使用量、リソース要件の詳細な比較
- **エンタープライズ向け考慮事項**: セキュリティ実践、コンプライアンスフレームワーク、データ保護戦略

## 学習の始め方

推奨学習パス:
1. **モジュール01**から始めてEdgeAIの基本的な理解を構築する
2. **モジュール02**に進んで、さまざまなSLMモデルファミリーを深く理解する
3. **モジュール03**を学び、実践的なデプロイメントスキルを習得する
4. **モジュール04**で高度なモデル最適化とフォーマット変換を学ぶ
5. **モジュール05**を完了して、本番対応のSLMOpsを習得する
6. **モジュール06**を探索して、SLMエージェントシステムと関数呼び出しの能力を理解する
7. **モジュール07**で多様なEdgeAI実装サンプルを使った実践的な経験を得る

各モジュールは独立して完結していますが、順序立てた学習が最良の結果をもたらします。

## 学習ガイド

包括的な[学習ガイド](STUDY_GUIDE.md)が用意されており、学習体験を最大化するのに役立ちます。この学習ガイドには以下が含まれます:

- **構造化された学習パス**: コースを20時間で完了するための最適化されたスケジュール
- **時間配分のガイダンス**: 読書、演習、プロジェクトのバランスを取るための具体的な推奨事項
- **重要な概念の焦点**: 各モジュールの優先学習目標
- **自己評価ツール**: 理解度をテストするための質問と演習
- **ミニプロジェクトのアイデア**: 学習を強化するための実践的な応用

この学習ガイドは、集中的な学習（1週間）とパートタイム学習（3週間）の両方に対応しており、コースに10時間しか割けない場合でも効果的に時間を配分する方法を明確に示しています。

---

**EdgeAIの未来は、モデルアーキテクチャ、量子化技術、効率と専門性を優先するデプロイメント戦略の継続的な改善にあります。このパラダイムシフトを受け入れる組織は、AIの変革的な可能性を活用しながら、データと運用の管理を維持することができます。**

## その他のコース

私たちのチームは他にもコースを提供しています！以下をご覧ください:

- [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners using JavaScript](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML for Beginners](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [Data Science for Beginners](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI for Beginners](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT for Beginners](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR Development for Beginners](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は責任を負いません。