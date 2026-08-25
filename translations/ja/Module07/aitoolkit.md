# Visual Studio Code用AIツールキット - エッジAI開発ガイド

## はじめに

Visual Studio Code用AIツールキットをエッジAI開発に活用するための包括的なガイドへようこそ。人工知能が中央集約型のクラウドコンピューティングから分散型のエッジデバイスへと移行する中で、開発者はリソース制約からオフライン動作要件まで、エッジ展開のユニークな課題を処理できる強力で統合されたツールを必要としています。

Visual Studio Code用AIツールキットはこのギャップを埋め、エッジデバイス上で効率的に動作するAIアプリケーションの構築、テスト、最適化に特化した完全な開発環境を提供します。IoTセンサー、モバイルデバイス、組み込みシステム、エッジサーバー向けの開発にかかわらず、このツールキットはおなじみのVS Code環境内で開発ワークフロー全体を合理化します。

このガイドでは、初期モデル選択から本番展開まで、エッジAIプロジェクトでAIツールキットを活用するための基本概念、ツール、ベストプラクティスについて解説します。

## 概要

Visual Studio Code用AIツールキットは、エージェント開発とAIアプリケーション作成を効率化する強力な拡張機能です。Anthropic、OpenAI、GitHub、Googleなど幅広いプロバイダーからのAIモデルの探索、評価、展開を統合的にサポートし、ONNXやOllamaを用いたローカルモデル実行も可能です。

AIツールキットの特長は、従来の単一機能に焦点を当てたAI開発ツールとは異なり、モデル探索、実験、エージェント開発、評価、展開を一つのVS Code環境で完結できる包括的な開発ライフサイクルを提供する点です。

このプラットフォームは迅速なプロトタイピングと本番展開の両方に対応しており、プロンプト生成、クイックスターター、シームレスなMCP（Model Context Protocol）ツール統合、幅広い評価機能などを備えています。エッジAI開発においては、VS Code内で完全な開発ワークフローを維持しながら、エッジ展開シナリオに適したAIアプリケーションの効率的な開発、テスト、最適化を実現します。

## 学習目標

このガイドを終えるころには、以下のことができるようになります：

### コアスキル
- **Visual Studio Code用AIツールキットのインストールと設定** エッジAI開発ワークフローに対応
- **AIツールキットインターフェースの操作** モデルカタログ、プレイグラウンド、エージェントビルダーを含む
- **エッジ展開に適したAIモデルの選択と評価** 性能とリソース制約に基づく
- **ONNXフォーマットと量子化技術を用いたモデルの変換と最適化** エッジデバイス向け

### エッジAI開発スキル
- **統合開発環境でのエッジAIアプリケーションの設計と実装**
- <strong>ローカル推論とリソースモニタリングを用いたエッジ条件下でのモデルテストの実施</strong>
- **エッジ展開シナリオに最適化されたAIエージェントの作成とカスタマイズ**
- **レイテンシ、メモリ使用量、精度などエッジ計算に関連する指標を使ったモデル性能評価**

### 最適化と展開
- <strong>モデルサイズを抑えつつ性能を維持するための量子化とプルーニング技術の適用</strong>
- **CPU、GPU、NPUアクセラレーションを含む特定のエッジハードウェアプラットフォーム向けのモデル最適化**
- **リソース管理やフォールバック戦略を含むエッジAI開発のベストプラクティスの実装**
- <strong>エッジデバイスでの本番展開に向けたモデルとアプリケーションの準備</strong>

### 高度なエッジAI概念
- **ONNX Runtime、Windows ML、TensorFlow Liteを含むエッジAIフレームワークとの統合**
- <strong>マルチモデルアーキテクチャやフェデレーテッドラーニングのエッジ環境での実装</strong>
- **メモリ制約、推論速度、ハードウェア互換性など一般的なエッジAI問題のトラブルシューティング**
- **本番環境のエッジAIアプリケーション向けの監視およびログ戦略の設計**

### 実践的応用
- **モデル選択から展開までのエンドツーエンドのエッジAIソリューション構築**
- <strong>エッジ特有の開発ワークフローと最適化技術の熟達</strong>
- **学んだ概念をIoT、モバイル、組み込みアプリケーションなど実際のエッジAIユースケースに応用**
- **様々なエッジAI展開戦略の評価と比較、及びそれぞれのトレードオフの理解**

## エッジAI開発の主な機能

### 1. モデルカタログと探索
- <strong>マルチプロバイダー対応</strong>: Anthropic、OpenAI、GitHub、Googleなどのモデルを閲覧・利用可能
- <strong>ローカルモデル統合</strong>: エッジ展開向けONNXとOllamaモデルの簡単な探索
- **GitHubモデル**: GitHubのモデルホスティングと直接統合しアクセスを効率化
- <strong>モデル比較</strong>: エッジデバイスの制約に最適なバランスを見つけるためのモデル比較機能

### 2. インタラクティブプレイグラウンド
- <strong>インタラクティブなテスト環境</strong>: モデル能力を制御された環境で即座に試験可能
- <strong>マルチモーダル対応</strong>: 画像、テキストなどエッジシナリオに典型的な入力でテスト可能
- <strong>リアルタイム実験</strong>: モデル応答と性能に対する即時フィードバック
- <strong>パラメータ最適化</strong>: エッジ展開要件に合わせてモデルパラメータを微調整

### 3. プロンプト（エージェント）ビルダー
- <strong>自然言語生成</strong>: 自然言語説明からスタータープロンプトを生成
- <strong>反復改善</strong>: モデル応答と性能に基づくプロンプトの改良
- <strong>タスク分解</strong>: プロンプトチェーンと構造化出力で複雑なタスクを分解
- <strong>変数対応</strong>: プロンプトに変数を用いて動的なエージェント動作を実現
- <strong>本番コード生成</strong>: 迅速なアプリ開発のため本番対応コードを生成

### 4. 一括実行と評価
- <strong>マルチモデルテスト</strong>: 選択した複数モデルに対し複数プロンプトを同時実行
- <strong>大規模効率テスト</strong>: 様々な入力・構成の効率的なテスト
- <strong>カスタムテストケース</strong>: エージェントをテストケースで実行し機能検証
- <strong>性能比較</strong>: 異なるモデルや構成の結果比較

### 5. データセットを用いたモデル評価
- <strong>標準評価指標</strong>: 内蔵評価器によるAIモデル評価（F1スコア、関連性、類似度、一貫性）
- <strong>カスタム評価器</strong>: 特定ユースケース向けの独自評価指標作成
- <strong>データセット統合</strong>: 包括的なデータセットに対するモデルテスト
- <strong>性能測定</strong>: エッジ展開決定のためのモデル性能定量化

### 6. ファインチューニング機能
- <strong>モデルカスタマイズ</strong>: 特定ユースケース・ドメイン向けにモデルをカスタマイズ
- <strong>専門的適応</strong>: 専門ドメインや要件にモデル適応
- <strong>エッジ最適化</strong>: エッジ展開制約向けにモデルをファインチューニング
- <strong>ドメイン特化トレーニング</strong>: 特定エッジユースケースに合わせたモデル作成

### 7. MCPツール統合
- <strong>外部ツール接続</strong>: Model Context Protocolサーバー経由でエージェントと外部ツールを接続
- <strong>実世界のアクション</strong>: エージェントによるデータベース照会、APIアクセス、カスタムロジック実装
- **既存MCPサーバー利用**: command (stdio)やHTTP(server-sent event)プロトコルのツール活用
- **カスタムMCP開発**: Agent Builderで新規MCPサーバーの構築とテスト支援

### 8. エージェント開発とテスト
- <strong>関数呼び出し対応</strong>: エージェントが外部関数を動的に呼び出す機能
- <strong>リアルタイム統合テスト</strong>: ツール使用を含むリアルタイム実行による統合テスト
- <strong>エージェントバージョニング</strong>: バージョン管理と評価結果の比較機能
- <strong>デバッグとトレース</strong>: ローカルトレースおよびデバッグ機能でエージェント開発を支援

## エッジAI開発ワークフロー

### フェーズ1: モデル探索と選択
1. <strong>モデルカタログを探索</strong>: エッジ展開に適したモデルをモデルカタログで発見
2. <strong>性能比較</strong>: サイズ、精度、推論速度に基づきモデル評価
3. <strong>ローカルテスト</strong>: OllamaやONNXモデルを用いてローカルでテスト実施
4. <strong>リソース要件評価</strong>: 対象エッジデバイスのメモリと計算要件を確認

### フェーズ2: モデル最適化
1. **ONNX変換**: 選択モデルをエッジ対応のONNX形式に変換
2. <strong>量子化適用</strong>: INT8またはINT4量子化でモデルサイズ削減
3. <strong>ハードウェア最適化</strong>: ターゲットエッジハードウェア（ARM、x86、専用アクセラレータ）向け最適化
4. <strong>性能検証</strong>: 最適化後も許容精度を維持しているか確認

### フェーズ3: アプリケーション開発
1. <strong>エージェント設計</strong>: Agent Builderでエッジ最適化されたAIエージェントを作成
2. <strong>プロンプト設計</strong>: 小型エッジモデルに対応した効果的なプロンプトを開発
3. <strong>統合テスト</strong>: シミュレートされたエッジ条件下でエージェントをテスト
4. <strong>コード生成</strong>: エッジ展開に最適化された本番コード生成

### フェーズ4: 評価とテスト
1. <strong>バッチ評価</strong>: 複数構成をテストして最適なエッジ設定を発見
2. <strong>性能プロファイリング</strong>: 推論速度、メモリ使用量、精度の解析
3. <strong>エッジシミュレーション</strong>: ターゲットエッジ環境に近い条件でのテスト
4. <strong>ストレステスト</strong>: さまざまな負荷条件で性能評価

### フェーズ5: 展開準備
1. <strong>最終最適化</strong>: テスト結果に基づく最終的な最適化実施
2. <strong>展開パッケージ作成</strong>: エッジ展開用のモデルとコードをパッケージング
3. <strong>ドキュメント作成</strong>: 展開要件および設定内容の文書化
4. <strong>監視設定</strong>: エッジ展開のための監視とログ収集準備

## エッジAI開発の対象ユーザー

### エッジAI開発者
- AI搭載エッジデバイスやIoTソリューションを開発するアプリケーション開発者
- リソース制約のあるデバイスにAI機能を組み込む組み込みシステム開発者
- スマートフォンやタブレット向けオンデバイスAIアプリケーション開発者

### エッジAIエンジニア
- エッジ展開向けモデル最適化および推論パイプライン管理を担当するAIエンジニア
- 分散エッジインフラでAIモデルを展開・管理するDevOpsエンジニア
- エッジハードウェアの制約に対応したAIワークロード最適化のパフォーマンスエンジニア

### 研究者・教育者
- エッジコンピューティング向け効率的なモデルやアルゴリズムを開発するAI研究者
- エッジAI概念や最適化技術を教える教育者
- エッジAI展開の課題や解決策を学ぶ学生

## エッジAIユースケース

### スマートIoTデバイス
- <strong>リアルタイム画像認識</strong>: IoTカメラやセンサーでコンピュータビジョンモデルを展開
- <strong>音声処理</strong>: スマートスピーカーで音声認識や自然言語処理を実装
- <strong>予知保全</strong>: 産業用エッジデバイスで異常検知モデルを実行
- <strong>環境モニタリング</strong>: 環境用途向けセンサーデータ分析モデルの展開

### モバイルおよび組み込みアプリケーション
- <strong>オンデバイス翻訳</strong>: オフラインで動作する言語翻訳モデルを実装
- <strong>拡張現実</strong>: ARアプリ向けリアルタイム物体認識と追跡を展開
- <strong>健康モニタリング</strong>: ウェアラブルデバイスや医療機器で健康解析モデルを実行
- <strong>自律システム</strong>: ドローン、ロボット、車両向け意思決定モデルを実装

### エッジコンピューティングインフラ
- <strong>エッジデータセンター</strong>: 低レイテンシアプリケーション向けにエッジデータセンターでAIモデルを展開
- **CDN統合**: コンテンツ配信ネットワークにAI処理機能を統合
- **5Gエッジ**: 5Gエッジコンピューティングを活用したAI対応アプリケーション
- <strong>フォグコンピューティング</strong>: フォグ環境でのAI処理実装

## インストールとセットアップ

### 拡張機能のインストール
Visual Studio Code MarketplaceからAIツールキット拡張機能を直接インストールします：

**拡張機能ID**: `ms-windows-ai-studio.windows-ai-studio`

<strong>インストール方法</strong>:
1. **VS Code Marketplace**: 拡張機能ビューで「AI Toolkit」を検索
2. <strong>コマンドライン</strong>: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. <strong>直接インストール</strong>: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)からダウンロード

### エッジAI開発の前提条件
- **Visual Studio Code**: 最新版推奨
- **Python環境**: 必要なAIライブラリを含むPython 3.8以上
- **ONNX Runtime**（任意）: ONNXモデル推論用
- **Ollama**（任意）: ローカルモデルサービス用
- <strong>ハードウェアアクセラレーションツール</strong>: CUDA、OpenVINO、またはプラットフォーム固有のアクセラレータ

### 初期設定
1. <strong>拡張機能の有効化</strong>: VS Codeを開き、アクティビティバーにAIツールキットが表示されていることを確認
2. <strong>モデルプロバイダーの設定</strong>: GitHub、OpenAI、Anthropicなどのモデルプロバイダーへのアクセスを設定
3. <strong>ローカル環境設定</strong>: Python環境セットアップと必要パッケージのインストール
4. <strong>ハードウェアアクセラレーション設定</strong>: GPU/NPUアクセラレーションが利用可能なら設定
5. **MCP統合**: 必要に応じてModel Context Protocolサーバーを設定

### 初回セットアップチェックリスト
- [ ] AIツールキット拡張機能がインストール・有効化されている
- [ ] モデルカタログにアクセス可能でモデルが探索可能
- [ ] プレイグラウンドがモデルテスト用に機能している
- [ ] エージェントビルダーがプロンプト作成に利用可能
- [ ] ローカル開発環境が設定されている
- [ ] ハードウェアアクセラレーション（利用可能なら）が正しく設定されている

## AIツールキットの使い始め

### クイックスタートガイド

最もスムーズな体験にはGitHubホストモデルから始めることをお勧めします：

1. <strong>インストール</strong>: お使いのデバイスにAIツールキットをセットアップするには[インストールガイド](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)に従ってください
2. <strong>モデル探索</strong>: 拡張機能のツリー表示から **CATALOG > Models** を選び利用可能なモデルを探します
3. **GitHubモデル**: 統合に最適なGitHubホストモデルから開始
4. <strong>プレイグラウンドテスト</strong>: 任意のモデルカードで **Try in Playground** を選択しモデル機能を試す

### ステップバイステップ エッジAI開発

#### ステップ1: モデル探索と選択
1. VS CodeのアクティビティバーでAIツールキットビューを開く
2. エッジ展開に適したモデルをモデルカタログで閲覧
3. エッジ要件に基づきプロバイダー（GitHub、ONNX、Ollama）で絞り込み
4. **Try in Playground** を使って即座にモデル機能をテスト

#### ステップ2: エージェント開発
1. **Prompt (Agent) Builder** でエッジ最適化されたAIエージェントを作成
2. 自然言語説明からスタータープロンプトを生成
3. モデル応答に基づいてプロンプトを繰り返し改良
4. MCPツールを統合してエージェント機能を強化


#### ステップ 3: テストと評価
1. **Bulk Run** を使用して選択したモデル間で複数のプロンプトをテストする
2. テストケースでエージェントを実行して機能を検証する
3. 組み込みまたはカスタム指標を使用して精度とパフォーマンスを評価する
4. 異なるモデルや構成を比較する

#### ステップ 4: ファインチューニングと最適化
1. 特定のエッジユースケース向けにモデルをカスタマイズする
2. ドメイン固有のファインチューニングを適用する
3. エッジ展開の制約に合わせて最適化する
4. 異なるエージェント構成のバージョン管理と比較を行う

#### ステップ 5: 展開準備
1. Agent Builder を使って本番環境対応コードを生成する
2. 本番利用向けに MCP サーバー接続を設定する
3. エッジデバイス向けの展開パッケージを準備する
4. モニタリングと評価指標を設定する

## AI Toolkit のサンプル

サンプルを試す
[AI Toolkit samples](https://github.com/Azure-Samples/AI_Toolkit_Samples) は、開発者や研究者が効果的にAIソリューションを探索・実装できるように設計されています。 

サンプルには以下が含まれます:

サンプルコード: 訓練、展開、またはモデルをアプリケーションに統合するなどのAI機能を示す事前構築済みの例。
ドキュメント: AI Toolkit の機能や使い方を理解するためのガイドとチュートリアル。
前提条件

- Visual Studio Code
- Visual Studio Code 用 AI Toolkit
- GitHub の詳細なパーソナルアクセストークン（PAT）
- Foundry Local

## エッジAI開発のベストプラクティス

### モデル選択
- <strong>サイズの制約</strong>: ターゲットデバイスのメモリ制限に合うモデルを選択する
- <strong>推論速度</strong>: リアルタイムアプリケーションのために高速な推論時間のモデルを優先する
- <strong>精度のトレードオフ</strong>: モデルの精度とリソース制約のバランスを取る
- <strong>フォーマット互換性</strong>: エッジ展開のためにONNXやハードウェア最適化フォーマットを好む

### 最適化技術
- <strong>量子化</strong>: モデルサイズを縮小し速度を向上させるためにINT8またはINT4量子化を使用する
- <strong>プルーニング</strong>: 計算負荷を減らすために不要なモデルパラメータを削除する
- <strong>知識蒸留</strong>: 大きいモデルの性能を維持しつつ小型モデルを作成する
- <strong>ハードウェアアクセラレーション</strong>: 利用可能な場合はNPU、GPU、または専用アクセラレータを活用する

### 開発ワークフロー
- <strong>反復テスト</strong>: 開発中にエッジに類似した条件で頻繁にテストを行う
- <strong>パフォーマンスモニタリング</strong>: リソース使用状況と推論速度を継続的に監視する
- <strong>バージョン管理</strong>: モデルのバージョンと最適化設定を追跡する
- <strong>ドキュメンテーション</strong>: すべての最適化判断とパフォーマンスのトレードオフを文書化する

### 展開の考慮点
- <strong>リソースモニタリング</strong>: 本番環境でメモリ、CPU、電力使用量を監視する
- <strong>フォールバック戦略</strong>: モデルの障害に備えたフォールバックメカニズムを実装する
- <strong>更新メカニズム</strong>: モデルの更新とバージョン管理を計画する
- <strong>セキュリティ</strong>: エッジAIアプリケーションに適切なセキュリティ対策を実装する

## エッジAIフレームワークとの統合

### ONNX Runtime
- <strong>クロスプラットフォーム展開</strong>: 異なるエッジプラットフォーム上でONNXモデルを展開する
- <strong>ハードウェア最適化</strong>: ONNX Runtimeのハードウェア固有の最適化を活用する
- <strong>モバイルサポート</strong>: スマートフォンやタブレットアプリ向けにONNX Runtime Mobileを使用する
- **IoT統合**: ONNX Runtimeの軽量ディストリビューションを使ってIoTデバイスへ展開する

### Windows ML
- **Windowsデバイス**: WindowsベースのエッジデバイスやPC向けに最適化する
- **NPUアクセラレーション**: Windowsデバイスのニュープロセッシングユニットを活用する
- **DirectML**: WindowsプラットフォームでのGPUアクセラレーションにDirectMLを使用する
- **UWP統合**: Universal Windows Platformアプリケーションと統合する

### TensorFlow Lite
- <strong>モバイル最適化</strong>: モバイルおよび組み込みデバイスでTensorFlow Liteモデルを展開する
- <strong>ハードウェアデリゲート</strong>: 専用ハードウェアデリゲートを使って加速する
- <strong>マイクロコントローラー</strong>: TensorFlow Lite Microを使ってマイクロコントローラーに展開する
- <strong>クロスプラットフォームサポート</strong>: Android、iOS、組み込みLinuxシステムに展開する

### Azure IoT Edge
- <strong>クラウド・エッジハイブリッド</strong>: クラウドでの訓練とエッジでの推論を組み合わせる
- <strong>モジュール展開</strong>: AIモデルをIoT Edgeモジュールとして展開する
- <strong>デバイス管理</strong>: エッジデバイスとモデル更新をリモートで管理する
- <strong>テレメトリ</strong>: エッジ展開から性能データとモデル指標を収集する

## 高度なエッジAIシナリオ

### マルチモデル展開
- <strong>モデルアンサンブル</strong>: 精度向上や冗長化のために複数のモデルを展開する
- **A/Bテスト**: エッジデバイスで異なるモデルを同時にテストする
- <strong>動的選択</strong>: 現在のデバイス状況に基づいてモデルを選択する
- <strong>リソース共有</strong>: 複数の展開モデルでリソース使用を最適化する

### フェデレーテッドラーニング
- <strong>分散訓練</strong>: 複数のエッジデバイスでモデルを訓練する
- <strong>プライバシー保護</strong>: 訓練データはローカルに保持しつつモデルの改善を共有する
- <strong>協調学習</strong>: デバイス同士が集合的な経験から学習可能にする
- <strong>エッジ・クラウド連携</strong>: エッジデバイスとクラウド間で学習を調整する

### リアルタイム処理
- <strong>ストリーム処理</strong>: エッジデバイス上で連続データストリームを処理する
- <strong>低遅延推論</strong>: 推論遅延を最小化するように最適化する
- <strong>バッチ処理</strong>: エッジデバイスでデータバッチを効率的に処理する
- <strong>適応処理</strong>: 現在のデバイス能力に応じて処理を調整する

## エッジAI開発のトラブルシューティング

### よくある問題
- <strong>メモリ制約</strong>: ターゲットデバイスのメモリに対してモデルが大きすぎる
- <strong>推論速度</strong>: モデル推論がリアルタイム要件に対して遅すぎる
- <strong>精度劣化</strong>: 最適化によりモデル精度が許容範囲外に低下する
- <strong>ハードウェア互換性</strong>: モデルがターゲットハードウェアと互換性がない

### デバッグ戦略
- <strong>パフォーマンスプロファイリング</strong>: ボトルネックを特定するために AI Toolkit のトレース機能を使う
- <strong>リソースモニタリング</strong>: 開発中にメモリとCPU使用状況を監視する
- <strong>段階的テスト</strong>: 最適化を段階的にテストして問題を特定する
- <strong>ハードウェアシミュレーション</strong>: 開発ツールを使ってターゲットハードウェアをシミュレートする

### 最適化ソリューション
- <strong>さらなる量子化</strong>: より攻撃的な量子化技術を適用する
- <strong>モデルアーキテクチャ</strong>: エッジ向けに最適化された異なるモデル構造を検討する
- <strong>前処理の最適化</strong>: エッジ制約に合わせてデータ前処理を最適化する
- <strong>推論の最適化</strong>: ハードウェア固有の推論最適化を使用する

## リソースと次のステップ

### 公式ドキュメント
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)
- [Installation and Setup Guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Intelligent Apps Documentation](https://code.visualstudio.com/docs/intelligentapps)
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)

### コミュニティとサポート
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub Issues and Feature Requests](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### 技術リソース
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Ollama Documentation](https://ollama.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### 学習パス
- [Edge AI Fundamentals Course](../Module01/README.md)
- [Small Language Models Guide](../Module02/README.md)
- [Edge Deployment Strategies](../Module03/README.md)
- [Windows Edge AI Development](./windowdeveloper.md)

### 追加リソース
- <strong>リポジトリ統計</strong>: 1.8k以上のスター、150以上のフォーク、18以上のコントリビューター
- <strong>ライセンス</strong>: MITライセンス
- <strong>セキュリティ</strong>: Microsoft のセキュリティポリシーが適用されます
- <strong>テレメトリ</strong>: VS Codeのテレメトリ設定を尊重します

## 結論

Visual Studio Code 用 AI Toolkit は、モダンなAI開発のための包括的なプラットフォームを表し、特にエッジAIアプリケーションに価値の高いエージェント開発機能を提供します。Anthropic、OpenAI、GitHub、Google などのプロバイダーをサポートする豊富なモデルカタログと、ONNX や Ollama によるローカル実行の組み合わせにより、多様なエッジ展開シナリオに求められる柔軟性を備えています。

このツールキットの強みは、モデルの発見や実験（Playground）から、Prompt Builder を使った高度なエージェント開発、包括的な評価機能、シームレスな MCP ツール統合に至るまで、一体化されたアプローチにあります。エッジAI開発者にとっては、エッジ展開前の迅速なプロトタイプ作成とテストが可能であり、迅速な反復とリソース制約のある環境への最適化を実現します。

エッジAI開発の主な利点は以下の通りです:
- <strong>迅速な実験</strong>: エッジ展開前にモデルやエージェントを素早くテストできる
- <strong>マルチプロバイダーの柔軟性</strong>: 様々なソースのモデルにアクセスして最適なエッジソリューションを見つける
- <strong>ローカル開発</strong>: オフラインかつプライバシー保護された開発のために ONNX と Ollama を利用してテスト
- <strong>本番対応</strong>: 本番環境対応コードを生成し、MCP 経由で外部ツールと統合可能
- <strong>包括的な評価</strong>: 組み込みとカスタム指標でエッジAIパフォーマンスを検証

AI がエッジ展開シナリオへと進むにつれて、VS Code 用 AI Toolkit はリソース制約のある環境向けにインテリジェントなアプリケーションを構築、テスト、最適化するための開発環境とワークフローを提供します。IoTソリューション、モバイルAIアプリケーション、組み込みインテリジェンスシステムのいずれを開発する場合でも、このツールキットの包括的な機能セットと統合ワークフローがエッジAIの開発ライフサイクル全体を支援します。

継続的な開発と活発なコミュニティ（1.8k以上のGitHubスター）により、AI Toolkit はエッジ展開シナリオ向けのモダンAI開発ニーズに応えながら、最先端のAI開発ツールとして進化し続けています。

[Next Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->