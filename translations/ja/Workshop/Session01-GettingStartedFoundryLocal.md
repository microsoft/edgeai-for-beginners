<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:16:13+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ja"
}
-->
# セッション1: Foundry Localの始め方

## 概要

Windows 11にFoundry Localをインストールして設定し、旅を始めましょう。CLIのセットアップ、ハードウェアアクセラレーションの有効化、モデルのキャッシュによる高速なローカル推論の方法を学びます。この実践的なセッションでは、Phi、Qwen、DeepSeek、GPT-OSS-20Bなどのモデルを再現可能なCLIコマンドで実行する方法を説明します。

## 学習目標

このセッションの終了時には以下を達成できます:

- **インストールと設定**: Windows 11でFoundry Localを最適なパフォーマンス設定でセットアップ
- **CLI操作の習得**: Foundry Local CLIを使用してモデル管理とデプロイを実施
- **ハードウェアアクセラレーションの有効化**: ONNXRuntimeまたはWebGPUを使用してGPUアクセラレーションを設定
- **複数モデルのデプロイ**: phi-4、GPT-OSS-20B、Qwen、DeepSeekモデルをローカルで実行
- **初めてのアプリ構築**: 既存のサンプルをFoundry Local Python SDKを使用するように適応

# モデルのテスト (非対話型単一プロンプト)
foundry model run phi-4-mini --prompt "こんにちは、自己紹介してください"

- Windows 11 (22H2以降)
# 利用可能なカタログモデルの一覧表示 (実行済みモデルは実行後に表示されます)
foundry model list
## NOTE: 現時点では専用の`--running`フラグはありません。ロード済みモデルを確認するには、チャットを開始するかサービスログを確認してください。
- Python 3.10+インストール済み
- Python拡張機能付きVisual Studio Code
- インストールのための管理者権限

### (オプション) 環境変数

スクリプトを移植可能にするために`.env`を作成するか、シェルで設定:
# レスポンスの比較 (非対話型)
foundry model run gpt-oss-20b --prompt "エッジAIを簡単に説明してください"
| 変数 | 目的 | 例 |
|------|------|----|
| `FOUNDRY_LOCAL_ALIAS` | 推奨モデルエイリアス (カタログが最適なバリアントを自動選択) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | エンドポイントの上書き (通常はマネージャーから自動取得) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | ストリーミングデモを有効化 | `true` |

> `FOUNDRY_LOCAL_ENDPOINT=auto` (または未設定)の場合、SDKマネージャーから自動的に取得します。

## デモフロー (30分)

### 1. Foundry LocalのインストールとCLIセットアップの確認 (10分)

# キャッシュされたモデルの一覧表示
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (プレビュー / サポートされている場合)**

ネイティブmacOSパッケージが提供されている場合 (最新情報は公式ドキュメントを確認):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

macOSネイティブバイナリがまだ利用できない場合でも以下が可能です:
1. Windows 11 ARM/Intel VM (Parallels / UTM)を使用し、Windows手順に従う。
2. コンテナを使用してモデルを実行 (コンテナイメージが公開されている場合)し、`FOUNDRY_LOCAL_ENDPOINT`を公開ポートに設定。

**Python仮想環境の作成 (クロスプラットフォーム)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

pipをアップグレードし、主要な依存関係をインストール:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### ステップ1.2: インストールの確認

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### ステップ1.3: 環境の設定

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDKブートストラッピング (推奨)

サービスを手動で開始してモデルを実行する代わりに、**Foundry Local Python SDK**がすべてをブートストラップできます:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

明示的な制御を好む場合は、後述のCLI + OpenAIクライアントを使用することも可能です。

### 2. CLIを使用したローカルモデルの実行 (10分)

#### ステップ3.1: Phi-4モデルのデプロイ

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### ステップ3.2: GPT-OSS-20Bのデプロイ

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### ステップ3.3: 追加モデルのロード

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. スタータープロジェクト: Foundry Local用に01-run-phiを適応 (5分)

#### ステップ4.1: 基本的なチャットアプリケーションの作成

`samples/01-foundry-quickstart/chat_quickstart.py`を作成 (利用可能な場合はマネージャーを使用するよう更新):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### ステップ4.2: アプリケーションのテスト

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## カバーされた主要概念

### 1. Foundry Localアーキテクチャ

- **ローカル推論エンジン**: モデルを完全にデバイス上で実行
- **OpenAI SDK互換性**: 既存のOpenAIコードとのシームレスな統合
- **モデル管理**: 複数のモデルを効率的にダウンロード、キャッシュ、実行
- **ハードウェア最適化**: GPU、NPU、CPUアクセラレーションを活用

### 2. CLIコマンドリファレンス

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK統合

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## よくある問題のトラブルシューティング

### 問題1: "Foundryコマンドが見つかりません"

**解決策:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### 問題2: "モデルのロードに失敗しました"

**解決策:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### 問題3: "localhost:5273への接続が拒否されました"

**解決策:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## パフォーマンス最適化のヒント

### 1. モデル選択戦略

- **Phi-4-mini**: 一般的なタスクに最適、メモリ使用量が少ない
- **Qwen2.5-0.5b**: 推論速度が最速、リソース消費が少ない
- **GPT-OSS-20B**: 最高品質、より多くのリソースが必要
- **DeepSeek-Coder**: プログラミングタスクに最適化

### 2. ハードウェア最適化

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. パフォーマンスの監視

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### オプションの強化

| 強化 | 内容 | 方法 |
|------|------|------|
| 共有ユーティリティ | 重複するクライアント/ブートストラップロジックを削除 | `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`)を使用 |
| トークン使用状況の可視化 | コスト/効率性の意識を早期に教育 | `SHOW_USAGE=1`を設定してプロンプト/完了/合計トークンを表示 |
| 決定論的比較 | 安定したベンチマークと回帰チェック | `temperature=0`, `top_p=1`, 一貫したプロンプトテキストを使用 |
| 最初のトークン遅延 | 知覚される応答性の指標 | ストリーミングを使用してベンチマークスクリプトを適応 (`BENCH_STREAM=1`) |
| 一時的なエラー時の再試行 | コールドスタート時のデモの回復力 | `RETRY_ON_FAIL=1` (デフォルト) & `RETRY_BACKOFF`を調整 |
| スモークテスト | 主要なフロー全体の簡易的な健全性チェック | ワークショップ前に`python Workshop/tests/smoke.py`を実行 |
| モデルエイリアスプロファイル | マシン間でモデルセットを迅速に切り替え | `.env`を維持し、`FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS`を設定 |
| キャッシュ効率 | 複数サンプル実行時の繰り返しウォームアップを回避 | ユーティリティキャッシュマネージャー; スクリプト/ノートブック間で再利用 |
| 初回実行ウォームアップ | p95遅延スパイクを削減 | `FoundryLocalManager`作成後に小さなプロンプトを実行 |

決定論的なウォームベースラインの例 (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

2回目の実行で同様の出力と同一のトークン数が表示され、決定論性が確認できます。

## 次のステップ

このセッションを完了した後:

1. **セッション2を探索**: Azure AI Foundry RAGを使用してAIソリューションを構築
2. **異なるモデルを試す**: Qwen、DeepSeek、その他のモデルファミリーを実験
3. **パフォーマンスを最適化**: 特定のハードウェアに合わせて設定を微調整
4. **カスタムアプリケーションを構築**: Foundry Local SDKを使用して独自のプロジェクトを作成

## 追加リソース

### ドキュメント
- [Foundry Local Python SDKリファレンス](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Localインストールガイド](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [モデルカタログ](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### サンプルコード
- [Module08 Sample 01](./samples/01/README.md) - RESTチャットクイックスタート
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK統合
- [Module08 Sample 03](./samples/03/README.md) - モデル探索とベンチマーク

### コミュニティ
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**セッション時間**: 実践30分 + Q&A15分  
**難易度レベル**: 初級  
**前提条件**: Windows 11, Python 3.10+, 管理者アクセス

## サンプルシナリオとワークショップマッピング

| ワークショップスクリプト / ノートブック | シナリオ | 目標 | 入力例 | 必要なデータセット |
|------------------------------------------|----------|------|--------|------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | プライバシー評価ポータルのためのオンデバイス推論を評価する内部ITチーム | ローカルSLMが標準プロンプトでサブ秒の遅延で応答することを証明 | "ローカル推論の利点を2つ挙げてください。" | なし (単一プロンプト) |
| クイックスタート適応コードブロック | 既存のOpenAIスクリプトをFoundry Localに移行する開発者 | ドロップイン互換性を示す | "ローカル推論の利点を2つ挙げてください。" | インラインプロンプトのみ |

### シナリオの概要
セキュリティとコンプライアンスチームは、機密プロトタイプデータがローカルで処理可能かどうかを検証する必要があります。彼らはブートストラップスクリプトを使用して、いくつかのプロンプト (プライバシー、遅延、コスト) を実行し、決定論的な`temperature=0`モードでベースライン出力をキャプチャし、後の比較 (セッション3のベンチマークとセッション4のSLM対LLMの対比) に備えます。

### 最小プロンプトセットJSON (オプション)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

このリストを使用して再現可能な評価ループを作成するか、将来の回帰テストハーネスのシードとして使用してください。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。