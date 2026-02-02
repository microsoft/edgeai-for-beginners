# ワークショップノートブック - クイックスタートガイド

## 目次

- [前提条件](../../../../Workshop/notebooks)
- [初期設定](../../../../Workshop/notebooks)
- [セッション04: モデル比較](../../../../Workshop/notebooks)
- [セッション05: マルチエージェントオーケストレーター](../../../../Workshop/notebooks)
- [セッション06: 意図ベースのモデルルーティング](../../../../Workshop/notebooks)
- [環境変数](../../../../Workshop/notebooks)
- [共通コマンド](../../../../Workshop/notebooks)

---

## 前提条件

### 1. Foundry Localのインストール

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**インストール確認:**
```bash
foundry --version
```

### 2. Python依存関係のインストール

```bash
cd Workshop
pip install -r requirements.txt
```

または個別にインストール:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## 初期設定

### Foundry Localサービスの開始

**ノートブックを実行する前に必須:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

期待される出力:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### モデルのダウンロードとロード

ノートブックでは以下のモデルがデフォルトで使用されます:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### 設定確認

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## セッション04: モデル比較

### 目的
Small Language Models (SLM) と Large Language Models (LLM) の性能を比較します。

### クイックセットアップ

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### ノートブックの実行

1. **開く** `session04_model_compare.ipynb` をVS CodeまたはJupyterで
2. **カーネルを再起動** (Kernel → Restart Kernel)
3. **すべてのセルを順番に実行**

### 主な設定

**デフォルトモデル:**
- **SLM:** `phi-4-mini` (~4GB RAM、高速)
- **LLM:** `qwen2.5-3b` (~3GB RAM、メモリ最適化)

**環境変数 (オプション):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### 期待される出力

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### カスタマイズ

**異なるモデルを使用:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**カスタムプロンプト:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### 検証チェックリスト

- [ ] セル12に正しいモデルが表示される (phi-4-mini, qwen2.5-3b)
- [ ] セル12に正しいエンドポイントが表示される (ポート59959)
- [ ] セル16の診断が成功する (✅ サービスが稼働中)
- [ ] セル20の事前チェックが成功する (両モデルOK)
- [ ] セル22の比較が遅延値とともに完了する
- [ ] セル24の検証で 🎉 ALL CHECKS PASSED! が表示される

### 所要時間
- **初回実行:** 5-10分 (モデルダウンロードを含む)
- **2回目以降:** 1-2分

---

## セッション05: マルチエージェントオーケストレーター

### 目的
Foundry Local SDKを使用して、複数のエージェントが協力して洗練された出力を生成する方法を示します。

### クイックセットアップ

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### ノートブックの実行

1. **開く** `session05_agents_orchestrator.ipynb`
2. **カーネルを再起動**
3. **すべてのセルを順番に実行**

### 主な設定

**デフォルト設定 (両エージェントに同じモデルを使用):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**高度な設定 (異なるモデルを使用):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### アーキテクチャ

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### 期待される出力

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### 拡張

**エージェントを追加:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**バッチテスト:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### 所要時間
- **初回実行:** 3-5分
- **2回目以降:** 質問ごとに1-2分

---

## セッション06: 意図ベースのモデルルーティング

### 目的
検出された意図に基づいてプロンプトを専門モデルにインテリジェントにルーティングします。

### クイックセットアップ

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**注意:** セッション06は最大限の互換性を確保するためにCPUモデルをデフォルトとしています。

### ノートブックの実行

1. **開く** `session06_models_router.ipynb`
2. **カーネルを再起動**
3. **すべてのセルを順番に実行**

### 主な設定

**デフォルトカタログ (CPUモデル):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**代替 (GPUモデル):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### 意図検出

ルーターは正規表現パターンを使用して意図を検出します:

| 意図 | パターン例 | ルーティング先 |
|------|------------|----------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | その他すべて | phi-4-mini-cpu |

### 期待される出力

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### カスタマイズ

**カスタム意図を追加:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**トークントラッキングを有効化:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### GPUモデルへの切り替え

8GB以上のVRAMがある場合:

1. **セル#6**でCPUカタログをコメントアウト
2. GPUカタログをアンコメント
3. GPUモデルをロード:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. カーネルを再起動し、ノートブックを再実行

### 所要時間
- **初回実行:** 5-10分 (モデルロード)
- **2回目以降:** テストごとに30-60秒

---

## 環境変数

### グローバル設定

Jupyter/VS Codeを開始する前に設定:

**Windows (コマンドプロンプト):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### ノートブック内設定

任意のノートブックの開始時に設定:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## 共通コマンド

### サービス管理

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### モデル管理

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### エンドポイントテスト

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### 診断コマンド

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## ベストプラクティス

### ノートブックを開始する前に

1. **サービスが稼働中か確認:**
   ```bash
   foundry service status
   ```

2. **モデルがロードされているか確認:**
   ```bash
   foundry model ls
   ```

3. **ノートブックカーネルを再起動** 再実行する場合
4. **すべての出力をクリア** クリーンな実行のため

### リソース管理

1. **デフォルトでCPUモデルを使用** 互換性のため
2. **GPUモデルに切り替え** 8GB以上のVRAMがある場合のみ
3. **他のGPUアプリケーションを閉じる** 実行前に
4. **サービスを稼働状態に保つ** ノートブックセッション間で
5. **リソース使用状況を監視** タスクマネージャー / nvidia-smiで

### トラブルシューティング

1. **まずサービスを確認** コードをデバッグする前に
2. **カーネルを再起動** 古い設定が表示される場合
3. **診断セルを再実行** 変更後
4. **モデル名を確認** ロードされているものと一致するか
5. **エンドポイントポートを確認** サービスステータスと一致するか

---

## クイックリファレンス: モデルエイリアス

### 一般的なモデル

| エイリアス | サイズ | 最適用途 | RAM/VRAM | バリアント |
|------------|--------|----------|----------|------------|
| `phi-4-mini` | ~4B | 一般的なチャット、要約 | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | コード生成、リファクタリング | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | 一般的なタスク、効率的 | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | 高速、低リソース | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | 分類、最小リソース | 1-2GB | `-cpu`, `-cuda-gpu` |

### バリアント命名

- **基本名** (例: `phi-4-mini`): ハードウェアに最適なバリアントを自動選択
- **`-cpu`**: CPU最適化、どこでも動作
- **`-cuda-gpu`**: NVIDIA GPU最適化、8GB以上のVRAMが必要
- **`-npu`**: Qualcomm NPU最適化、NPUドライバーが必要

**推奨:** 基本名 (サフィックスなし) を使用し、Foundry Localに最適なバリアントを自動選択させる。

---

## 成功の指標

以下が確認できれば準備完了です:

✅ `foundry service status` が "running" を表示  
✅ `foundry model ls` が必要なモデルを表示  
✅ サービスが正しいエンドポイントでアクセス可能  
✅ ヘルスチェックが200 OKを返す  
✅ ノートブック診断セルが成功  
✅ 出力に接続エラーがない  

---

## ヘルプを得る

### ドキュメント
- **メインリポジトリ**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLIリファレンス**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **トラブルシューティング**: このディレクトリ内の `troubleshooting.md` を参照

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**最終更新日:** 2025年10月8日  
**バージョン:** ワークショップノートブック 2.0

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。