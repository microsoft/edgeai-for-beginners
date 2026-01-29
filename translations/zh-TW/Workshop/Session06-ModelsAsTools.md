# 第六節：Foundry Local – 模型作為工具

## 摘要

將模型視為本地 AI 操作層中的可組合工具。本節課展示如何串聯多個專門的 SLM/LLM 調用，選擇性地路由任務，並向應用程式暴露統一的 SDK 接口。您將構建一個輕量級的模型路由器 + 任務規劃器，將其整合到應用程式腳本中，並概述向 Azure AI Foundry 擴展以支持生產工作負載的路徑。

## 學習目標

- **概念化** 模型作為具有明確能力的原子工具
- **路由** 根據意圖/啟發式評分分配請求
- **串聯** 跨多步任務的輸出（分解 → 解決 → 精煉）
- **整合** 統一的客戶端 API 以供下游應用程式使用
- **擴展** 設計至雲端（保持與 OpenAI 兼容的合約）

## 先決條件

- 完成第一至第五節課程
- 緩存多個本地模型（例如 `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`）

### 跨平台環境片段

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
從 macOS 遠程/虛擬機服務訪問:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## 演示流程（30 分鐘）

### 1. 工具能力聲明（5 分鐘）

創建 `samples/06-tools/models_catalog.py`：

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```
  

### 2. 意圖檢測與路由（8 分鐘）

創建 `samples/06-tools/router.py`：

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```
  

### 3. 多步任務串聯（7 分鐘）

創建 `samples/06-tools/pipeline.py`：

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```
  

### 4. 初始項目：改編 `06-models-as-tools`（5 分鐘）

增強功能：
- 添加流式令牌支持（漸進式 UI 更新）
- 添加信心評分：詞彙重疊或提示標準
- 導出追蹤 JSON（意圖 → 模型 → 延遲 → 令牌使用）
- 為重複的子步驟實現緩存重用

### 5. 向 Azure 擴展的路徑（5 分鐘）

| 層級 | 本地（Foundry） | 雲端（Azure AI Foundry） | 過渡策略 |
|------|-----------------|--------------------------|----------|
| 路由 | 啟發式 Python | 耐用微服務 | 容器化並部署 API |
| 模型 | 緩存的 SLMs | 管理部署 | 將本地名稱映射到部署 ID |
| 可觀察性 | CLI 統計/手動 | 集中式日誌和指標 | 添加結構化追蹤事件 |
| 安全性 | 僅限本地主機 | Azure 認證/網絡 | 引入密鑰保管庫以存儲機密 |
| 成本 | 設備資源 | 消耗計費 | 添加預算防護措施 |

## 驗證清單

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```
  
預期基於意圖的模型選擇和最終精煉輸出。

## 疑難排解

| 問題 | 原因 | 解決方法 |
|------|------|----------|
| 所有任務都路由到同一模型 | 規則弱 | 擴充 INTENT_RULES 正則表達式集 |
| 管道在中途失敗 | 缺少已加載的模型 | 運行 `foundry model run <model>` |
| 輸出一致性低 | 缺少精煉階段 | 添加摘要/驗證通過 |

## 參考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Azure AI Foundry 文檔: https://learn.microsoft.com/azure/ai-foundry  
- 提示質量模式: 參見第二節課程  

---

**課程時長**: 30 分鐘  
**難度**: 高級

## 示例場景與工作坊映射

| 工作坊腳本 / 筆記本 | 場景 | 目標 | 數據集 / 目錄來源 |
|---------------------|------|------|-------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | 開發者助手處理混合意圖提示（重構、摘要、分類） | 啟發式意圖 → 模型別名路由與令牌使用 | 內嵌 `CATALOG` + 正則表達式 `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | 複雜編碼輔助任務的多步規劃與精煉 | 分解 → 專門執行 → 摘要精煉步驟 | 相同的 `CATALOG`; 步驟源自規劃輸出 |

### 場景敘述
一個工程生產力工具接收異構任務：重構代碼、摘要架構筆記、分類反饋。為了最小化延遲和資源使用，一個小型通用模型負責規劃和摘要，一個專門的代碼模型負責重構，一個輕量級分類模型標記反饋。管道腳本展示了串聯 + 精煉；路由腳本隔離了自適應單提示路由。

### 目錄快照
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```
  

### 示例測試提示
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```
  

### 追蹤擴展（可選）
為 `models_pipeline.py` 添加每步追蹤 JSON 行：
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```
  

### 升級啟發式（想法）
如果規劃包含關鍵詞如 "優化"、"安全性"，或步驟長度 > 280 字符 → 僅對該步驟升級到更大的模型（例如 `gpt-oss-20b`）。

### 可選增強功能

| 領域 | 增強功能 | 價值 | 提示 |
|------|----------|------|------|
| 緩存 | 重用管理器 + 客戶端對象 | 降低延遲，減少開銷 | 使用 `workshop_utils.get_client` |
| 使用指標 | 捕獲令牌與每步延遲 | 分析與優化 | 計時每次路由調用；存儲於追蹤列表 |
| 自適應路由 | 信心/成本感知 | 更好的質量成本平衡 | 添加評分：如果提示 > N 字符或正則表達式匹配領域 → 升級到更大的模型 |
| 動態能力註冊表 | 熱加載目錄 | 無需重啟重新部署 | 在運行時加載 `catalog.json`; 監視文件時間戳 |
| 回退策略 | 故障下的穩健性 | 更高的可用性 | 嘗試主模型 → 在異常時回退到別名 |
| 流式管道 | 提早反饋 | UX 改進 | 流式每步並緩衝最終精煉輸入 |
| 向量意圖嵌入 | 更細緻的路由 | 更高的意圖準確性 | 嵌入提示，聚類並映射中心 → 能力 |
| 追蹤導出 | 可審計的鏈條 | 合規/報告 | 發出 JSON 行：步驟、意圖、模型、延遲毫秒、令牌 |
| 成本模擬 | 雲端前估算 | 預算規劃 | 為每個模型分配假設成本/令牌並按任務聚合 |
| 確定性模式 | 可重現性基準 | 穩定的基準測試 | 環境：`temperature=0`，固定步驟數 |

#### 追蹤結構示例

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```
  

#### 自適應升級草圖

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```
  

#### 模型目錄熱加載

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```  

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。