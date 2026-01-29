# ワークショップノートブック - トラブルシューティングガイド

## 目次

- [一般的な問題と解決策](../../../../Workshop/notebooks)
- [セッション04特有の問題](../../../../Workshop/notebooks)
- [セッション05特有の問題](../../../../Workshop/notebooks)
- [セッション06特有の問題](../../../../Workshop/notebooks)
- [ハードウェア特有の問題](../../../../Workshop/notebooks)
- [診断コマンド](../../../../Workshop/notebooks)
- [ヘルプの取得](../../../../Workshop/notebooks)

---

## 一般的な問題と解決策

### 🔴 CUDAメモリ不足

**エラーメッセージ:**
```
CUDA failure 2: out of memory
```

**原因:** GPUのVRAMが不足しており、モデルをロードできない。

**解決策:**

#### オプション1: CPUバリアントを使用する（推奨）
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### オプション2: GPUで小型モデルを使用する
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### オプション3: GPUメモリをクリアする
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### オプション4: GPUメモリを増やす（可能な場合）
- ブラウザタブやビデオ編集ソフトなどのGPUアプリを閉じる
- Windowsの視覚効果を減らす
- 統合GPUと専用GPUがある場合は専用GPUを使用する

---

### 🔴 APIConnectionError: 接続エラー

**エラーメッセージ:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**原因:** Foundry Localサービスが実行されていない、またはアクセスできない。

**解決策:**

#### ステップ1: サービスの状態を確認する
```bash
foundry service status
```

#### ステップ2: サービスが停止している場合は開始する
```bash
foundry service start
```

#### ステップ3: エンドポイントを確認する
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### ステップ4: 必要なモデルをロードする
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### ステップ5: ノートブックのカーネルを再起動する
サービスを開始し、モデルをロードした後、ノートブックのカーネルを再起動してすべてのセルを再実行してください。

---

### 🔴 カタログにモデルが見つからない

**エラーメッセージ:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**原因:** モデルがダウンロードされていない、またはFoundry Localにロードされていない。

**解決策:**

#### オプション1: モデルをダウンロードしてロードする
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### オプション2: 自動選択モードを使用する
CATALOGを基本モデル名（`-cpu`サフィックスなし）に更新してください:

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDKは、ハードウェアに最適なバリアント（CPU、GPU、NPU）を自動的に選択します。

---

### 🔴 HttpResponseError: 500 - モデルのロードに失敗

**エラーメッセージ:**
```
HttpResponseError: 500 - Failed loading model
```

**原因:** モデルファイルが破損しているか、ハードウェアと互換性がない。

**解決策:**

#### モデルを再ダウンロードする
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### 別のバリアントを使用する
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: モジュールが見つからない

**エラーメッセージ:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**原因:** foundry-local-sdkパッケージがインストールされていない。

**解決策:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � 初回リクエストが遅い

**症状:** 最初の完了に30秒以上かかるが、以降のリクエストは高速。

**原因:** これは通常の動作であり、サービスが初回リクエスト時にモデルをメモリにロードしているため。

**解決策:**

#### モデルを事前にロードする
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### サービスを継続的に実行する
```bash
# Start service manually and leave it running
foundry service start
```

---

## セッション04特有の問題

### ポート設定が間違っている

**問題:** ノートブックが間違ったポート（55769、59959、57127）に接続している

**解決策:**

1. Foundry Localが使用しているポートを確認する:
```bash
foundry service status
# Note the port number displayed
```

2. ノートブックのセル10を更新する:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. カーネルを再起動し、セル6、8、10、12、16、20、22を再実行する

---

### モデル選択が間違っている

**問題:** ノートブックがgpt-oss-20bやqwen2.5-7bを表示しており、qwen2.5-3bではない

**解決策:**

1. ノートブックのカーネルを再起動する（古い変数状態をクリア）
2. セル10を再実行する（モデルエイリアスを設定）
3. セル12を再実行する（設定を表示）
4. **確認:** セル12が`LLM Model: qwen2.5-3b`を表示していることを確認

---

### 診断セルが失敗する

**問題:** セル16が「❌ Foundry Local service not found!」を表示する

**解決策:**

1. サービスが実行されていることを確認する:
```bash
foundry service status
```

2. エンドポイントを手動でテストする:
```bash
curl http://localhost:59959/v1/models
```

3. curlが動作するがノートブックが動作しない場合:
   - ノートブックのカーネルを再起動する
   - セルを順番に再実行する: 6、8、10、12、14、16

4. curlが失敗する場合:
   - サービスを開始する: `foundry service start`
   - モデルをロードする: `foundry model run phi-4-mini`および`foundry model run qwen2.5-3b`

---

### 事前チェックが失敗する

**問題:** セル20が診断が成功しているにもかかわらず接続エラーを表示する

**解決策:**

1. モデルがロードされていることを確認する:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. モデルが欠けている場合:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. モデルがロードされた後、セル20を再実行する

---

### 比較がNone値で失敗する

**問題:** セル22が完了するが、レイテンシーがNoneと表示される

**解決策:**

1. まず事前チェックが成功していることを確認する（セル20）
2. セル22を再実行する - 初回リクエストでモデルがウォームアップする必要がある場合がある
3. 両方のモデルがロードされていることを確認する: `foundry model ls`

---

## セッション05特有の問題

### エージェントが間違ったモデルを使用している

**問題:** エージェントが期待されるモデルを使用していない

**解決策:**

設定を確認する:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

モデルが正しくない場合はカーネルを再起動する。

---

### メモリコンテキストオーバーフロー

**問題:** エージェントの応答が時間とともに劣化する

**解決策:** すでに自動的に処理されています - エージェントはメモリ内に最後の6つのメッセージのみを保持します。

---

## セッション06特有の問題

### CPUとGPUモデルの混乱

**問題:** デフォルト設定を使用しているときにCUDAエラーが発生する

**解決策:** デフォルト設定は現在CPUモデルを使用しています。CUDAエラーが発生した場合:

1. デフォルトのCPUカタログを使用していることを確認する:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. カーネルを再起動し、すべてのセルを再実行する

---

### 意図検出が機能しない

**問題:** プロンプトが間違ったモデルにルーティングされる

**解決策:**

意図検出をテストする:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

パターンに調整が必要な場合はRULESを更新する。

---

## ハードウェア特有の問題

### NVIDIA GPU

**GPUの状態を確認する:**
```bash
nvidia-smi
```

**一般的な問題:**
- **ドライバーが古い:** NVIDIAドライバーを更新する
- **CUDAバージョンの不一致:** Foundry Localを再インストールする
- **GPUメモリの断片化:** システムを再起動する

### Qualcomm NPU

**NPUの状態を確認する:**
```bash
foundry device info
```

**一般的な問題:**
- **NPUドライバーがインストールされていない:** Qualcomm NPUドライバーをインストールする
- **NPUバリアントが利用できない:** CPUバリアントを使用する
- **Windowsのバージョンが古い:** 最新のWindows 11に更新する

### CPUのみのシステム

**推奨モデル:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**パフォーマンス向上のヒント:**
- 最小のモデルを使用する
- max_tokensを減らす
- 初回リクエストに対して忍耐を持つ

---

## 診断コマンド

### すべてを確認する
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Pythonで
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## ヘルプの取得

### 1. ログを確認する
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHubの問題
- 既存の問題を検索する: https://github.com/microsoft/Foundry-Local/issues
- 新しい問題を作成する際は以下を含める:
  - エラーメッセージ（全文）
  - `foundry service status`の出力
  - `foundry --version`の出力
  - GPU/NPU情報（nvidia-smiなど）
  - 再現手順

### 3. ドキュメント
- **メインリポジトリ:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLIリファレンス:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **トラブルシューティング:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## クイック修正チェックリスト

問題が発生した場合、以下を順番に試してください:

- [ ] サービスが実行されているか確認する: `foundry service status`
- [ ] サービスを再起動する: `foundry service stop && foundry service start`
- [ ] モデルが存在するか確認する: `foundry model ls | grep phi-4-mini`
- [ ] 必要なモデルをロードする: `foundry model run phi-4-mini`
- [ ] GPUメモリを確認する: `nvidia-smi`（NVIDIAの場合）
- [ ] CPUバリアントを試す: `phi-4-mini-cpu`を使用する
- [ ] ノートブックのカーネルを再起動する
- [ ] ノートブックの出力をクリアし、すべてのセルを再実行する
- [ ] SDKを再インストールする: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] システムを再起動する（最終手段）

---

## 予防のヒント

### ベストプラクティス

1. **まずサービスを確認する:**
   ```bash
   foundry service status
   ```

2. **デフォルトでCPUバリアントを使用する:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **ノートブックを実行する前にモデルを事前にロードする:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **サービスを継続的に実行する:**
   - 不必要にサービスを停止/開始しない
   - セッション間でバックグラウンドで実行させる

5. **リソースを監視する:**
   - 実行前にGPUメモリを確認する
   - 不要なGPUアプリケーションを閉じる
   - タスクマネージャー / nvidia-smiを使用する

6. **定期的に更新する:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**最終更新日:** 2025年10月8日

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。