<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T22:07:16+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ja"
}
-->
# セッション1: Foundry Localの始め方

## 概要

Microsoft Foundry Localを使用して、AIモデルのインストール、設定、初めての実行方法を学びます。この実践的なセッションでは、インストールからPhi-4、Qwen、DeepSeekなどのモデルを使用した最初のチャットアプリケーションの構築まで、ローカル推論のステップバイステップの導入を提供します。

## 学習目標

このセッション終了時には以下を達成できます:

- **インストールと設定**: Foundry Localを正しくインストールし、動作確認を行う
- **CLI操作の習得**: Foundry Local CLIを使用してモデル管理とデプロイを行う
- **初めてのモデル実行**: ローカルAIモデルをデプロイし、対話する
- **チャットアプリの構築**: Foundry Local Python SDKを使用して基本的なチャットアプリケーションを作成する
- **ローカルAIの理解**: ローカル推論とモデル管理の基本を理解する

## 前提条件

### システム要件

- **Windows**: Windows 11 (22H2以降) または **macOS**: macOS 11+ (限定サポート)
- **RAM**: 最低8GB、推奨16GB以上
- **ストレージ**: モデル用に10GB以上の空き容量
- **Python**: 3.10以降がインストールされていること
- **管理者権限**: インストールのための管理者権限

### 開発環境

- Python拡張機能付きVisual Studio Code (推奨)
- コマンドラインアクセス (WindowsではPowerShell、macOSではTerminal)
- リポジトリをクローンするためのGit (オプション)

## ワークショップの流れ (30分)

### ステップ1: Foundry Localのインストール (5分)

#### Windowsでのインストール

Windowsパッケージマネージャーを使用してFoundry Localをインストールします:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

代替方法: [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)から直接ダウンロード

#### macOSでのインストール (限定サポート)

> [!NOTE] 
> macOSのサポートは現在プレビュー版です。最新の利用可能情報は公式ドキュメントを確認してください。

Homebrewを使用してインストール可能な場合:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOSユーザー向け代替方法:**
- Windows 11 VM (Parallels/UTM)を使用し、Windowsの手順に従う
- コンテナを使用可能な場合は実行し、`FOUNDRY_LOCAL_ENDPOINT`を設定

### ステップ2: インストールの確認 (3分)

インストール後、ターミナルを再起動し、Foundry Localが動作しているか確認します:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

期待される出力にはバージョン情報と利用可能なコマンドが表示されます。

### ステップ3: Python環境のセットアップ (5分)

このワークショップ専用のPython環境を作成します:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### ステップ4: 初めてのモデルを実行 (7分)

次に、ローカルで初めてのAIモデルを実行します！

#### Phi-4 Miniで開始 (推奨モデル)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> このコマンドはモデルをダウンロード (初回のみ) し、Foundry Localサービスを自動的に開始します。

#### 実行中の確認

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### 他のモデルを試す

phi-4-miniが動作したら、他のモデルを試してみましょう:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### ステップ5: 初めてのチャットアプリケーションを構築 (10分)

次に、先ほど開始したモデルを使用するPythonアプリケーションを作成します。

#### チャットスクリプトの作成

`my_first_chat.py`という新しいファイルを作成します (または提供されたサンプルを使用):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **関連例**: より高度な使用例については以下を参照してください:
>
> - **Pythonサンプル**: `Workshop/samples/session01/chat_bootstrap.py` - ストリーミング応答とエラーハンドリングを含む
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - 詳細な説明付きのインタラクティブ版

#### チャットアプリケーションのテスト

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

代替方法: 提供されたサンプルを直接使用

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

またはインタラクティブノートブックを試す
Workshop/notebooks/session01_chat_bootstrap.ipynbをVS Codeで開く

以下の例の会話を試してみてください:

- "Microsoft Foundry Localとは何ですか？"
- "AIモデルをローカルで実行する3つの利点を挙げてください"
- "エッジAIについて教えてください"

## 達成したこと

おめでとうございます！以下を成功させました:

1. ✅ **Foundry Localをインストール**し、動作確認を完了
2. ✅ **初めてのAIモデル** (phi-4-mini) をローカルで開始
3. ✅ **異なるモデルをテスト** コマンドラインで
4. ✅ **チャットアプリケーションを構築** ローカルAIに接続
5. ✅ **クラウド依存なしでローカルAI推論を体験**

## 実行内容の理解

### ローカルAI推論

- AIモデルは完全にコンピュータ上で実行されます
- データはクラウドに送信されません
- 応答はCPU/GPUを使用してローカルで生成されます
- プライバシーとセキュリティが維持されます

### モデル管理

- `foundry model run`はモデルをダウンロードして開始します
- **FoundryLocalManager SDK**はサービスの起動とモデルのロードを自動的に処理します
- モデルは将来の使用のためにローカルにキャッシュされます
- 複数のモデルをダウンロードできますが、通常は1つずつ実行されます
- サービスはモデルのライフサイクルを自動的に管理します

### SDKとCLIのアプローチ

- **CLIアプローチ**: `foundry model run <model>`を使用した手動モデル管理
- **SDKアプローチ**: `FoundryLocalManager(alias)`を使用した自動サービス+モデル管理
- **推奨**: アプリケーションにはSDKを使用し、テストや探索にはCLIを使用

## よく使うコマンドのリファレンス

### 基本的なCLIコマンド

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### モデルの推奨

- **phi-4-mini**: 初心者向けモデル - 高速、軽量、品質良好
- **qwen2.5-0.5b**: 最速の推論、最小メモリ使用量
- **gpt-oss-20b**: 高品質な応答、より多くのリソースが必要
- **deepseek-coder-1.3b**: プログラミングとコードタスクに最適化

## トラブルシューティング

### "Foundryコマンドが見つかりません"

**解決策:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "モデルのロードに失敗しました"

**解決策:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "localhostで接続が拒否されました"

**解決策:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## 次のステップ

### すぐに行うべきアクション

1. **異なるモデルとプロンプトを試す**
2. **チャットアプリケーションを変更して異なるモデルを試す**
3. **独自のプロンプトを作成して応答をテストする**
4. **セッション2: RAGアプリケーションの構築**を探索する

### 高度な学習パス

1. **セッション2**: RAG (Retrieval-Augmented Generation) を使用したAIソリューションの構築
2. **セッション3**: 異なるオープンソースモデルの比較
3. **セッション4**: 最新モデルの活用
4. **セッション5**: マルチエージェントAIシステムの構築

## 環境変数 (オプション)

より高度な使用のために、以下の環境変数を設定できます:

| 変数 | 目的 | 例 |
|------|------|-----|
| `FOUNDRY_LOCAL_ALIAS` | 使用するデフォルトモデル | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | エンドポイントURLの上書き | `http://localhost:5273/v1` |

プロジェクトディレクトリに`.env`ファイルを作成:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## 追加リソース

### ドキュメント

- [Foundry Local Python SDK リファレンス](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local インストールガイド](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [モデルカタログ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### サンプルコード

- **セッション01 Pythonサンプル**: `Workshop/samples/session01/chat_bootstrap.py` - ストリーミング付きの完全なチャットアプリ
- **セッション01 ノートブック**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - インタラクティブなチュートリアル  
- [Module08 Sample 01](../Module08/samples/01/README.md) - RESTチャットクイックスタート
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK統合
- [Module08 Sample 03](../Module08/samples/03/README.md) - モデルの発見とベンチマーク

### コミュニティ

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**セッション時間**: 実践30分 + Q&A 15分  
**難易度**: 初級  
**前提条件**: Windows 11/macOS 11+, Python 3.10+, 管理者権限

## ワークショップの例シナリオ

### 実際のコンテキスト

**シナリオ**: 企業のITチームが、外部サービスにデータを送信せずに、従業員のフィードバックを処理するためのオンデバイスAI推論を評価する必要があります。

**目標**: ローカルAIモデルが完全なデータプライバシーを維持しながら、サブセカンドの応答速度で高品質な応答を提供できることを実証する。

### テストプロンプト

以下のプロンプトを使用してセットアップを検証してください:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### 成功基準

- ✅ すべてのプロンプトが2秒以内に応答を得られる
- ✅ データがローカルマシンを離れない
- ✅ 応答が関連性があり役立つ
- ✅ チャットアプリケーションがスムーズに動作する

この検証により、Foundry Localのセットアップがセッション2～6の高度なワークショップに向けて準備が整っていることを確認できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->