<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T20:42:49+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "hk"
}
-->
# 第五節：使用 Foundry Local 快速構建 AI 驅動代理

## 摘要

利用 Foundry Local 的低延遲、保護隱私的運行環境設計和協調多角色 AI 代理。您將定義代理角色、記憶策略、工具調用模式和執行圖。本節介紹了可以通過 Chainlit 或 LangGraph 擴展的框架模式。起始項目擴展現有的代理架構範例，添加記憶持久性和評估掛鉤。

## 學習目標

- **定義角色**：系統提示和能力範圍
- **實現記憶**：短期（對話）、長期（向量/文件）、臨時便箋
- **搭建工作流程**：順序、分支和並行代理步驟
- **整合工具**：輕量化函數工具調用模式
- **評估**：基本的追蹤 + 基於標準的結果評分

## 先決條件

- 完成第一至第四節
- Python，安裝 `foundry-local-sdk`、`openai`，可選 `chainlit`
- 本地模型運行（至少 `phi-4-mini`）

### 跨平台環境代碼片段

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

如果從 macOS 運行代理並連接到遠程 Windows 主機服務：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 演示流程（30 分鐘）

### 1. 定義代理角色和記憶（7 分鐘）

創建 `samples/05-agents/agents_core.py`：

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. CLI 框架模式（3 分鐘）

```powershell
python samples/05-agents/agents_core.py
```


### 3. 添加工具調用（7 分鐘）

擴展 `samples/05-agents/tools.py`：

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


修改 `agents_core.py` 以允許簡單的工具語法：用戶輸入 `#tool:get_time`，代理在生成之前將工具輸出擴展到上下文中。

### 4. 協調工作流程（6 分鐘）

創建 `samples/05-agents/orchestrator.py`：

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. 起始項目：擴展 `05-agent-architecture`（7 分鐘）

添加：
1. 持久記憶層（例如，對話的 JSON 行追加）
2. 簡單的評估標準：事實性/清晰度/風格佔位符
3. 可選的 Chainlit 前端（兩個標籤：對話和追蹤）
4. 可選的 LangGraph 風格狀態機（如果添加依賴）以進行分支決策

## 驗證清單

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

預期結構化的管道輸出，包含工具注入註釋。

## 記憶策略概述

| 層級 | 目的 | 範例 |
|------|------|------|
| 短期 | 對話連續性 | 最近 N 條消息 |
| 情節性 | 會話回憶 | 每次會話的 JSON |
| 語義性 | 長期檢索 | 摘要的向量存儲 |
| 便箋 | 推理步驟 | 內聯思維鏈（私密） |

## 評估掛鉤（概念）

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## 疑難排解

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| 答案重複 | 上下文窗口過大/過小 | 調整記憶窗口參數 |
| 工具未調用 | 語法錯誤 | 使用 `#tool:tool_name` 格式 |
| 協調速度慢 | 多個冷啟動模型 | 預先運行預熱提示 |

## 參考資料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph（可選概念）：https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**課程時長**：30 分鐘  
**難度**：高級

## 範例場景與工作坊映射

| 工作坊腳本 | 場景 | 目標 | 範例提示 |
|------------|------|------|----------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | 知識研究機器人生成適合高層的摘要 | 雙代理管道（研究 → 編輯潤色），可選擇不同模型 | 解釋為什麼邊緣推理對合規性很重要。 |
| （擴展）`tools.py` 概念 | 添加時間和令牌估算工具 | 展示輕量化工具調用模式 | #tool:get_time |

### 場景敘述
合規文檔團隊需要快速從本地知識中獲取內部簡報，而不將草稿發送到雲端服務。一個研究代理收集簡潔的事實要點；一個編輯代理重寫以符合高層的清晰度需求。可以分配不同的模型別名以優化延遲（快速 SLM）與風格化潤色（僅在需要時使用較大的模型）。

### 範例多模型環境
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### 追蹤結構（可選）
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

將每個步驟保存到 JSONL 文件以供後續標準評分。

### 可選增強功能

| 主題 | 增強功能 | 好處 | 實施草案 |
|------|---------|------|----------|
| 多模型角色 | 每個代理使用不同模型（`AGENT_MODEL_PRIMARY`，`AGENT_MODEL_EDITOR`） | 專業化與速度 | 選擇別名環境變數，使用每個角色的別名調用 `chat_once` |
| 結構化追蹤 | 每個行為（工具、輸入、延遲、令牌）的 JSON 追蹤 | 調試與評估 | 將字典追加到列表；在結尾寫入 `.jsonl` |
| 記憶持久性 | 可重新加載的對話上下文 | 會話連續性 | 將 `Agent.memory` 傾倒到 `sessions/<ts>.json` |
| 工具註冊表 | 動態工具發現 | 可擴展性 | 維護 `TOOLS` 字典並檢查名稱/描述 |
| 重試與退避 | 穩健的長鏈 | 減少瞬時故障 | 用 try/except 包裹 `act`，並使用指數退避 |
| 標準評分 | 自動化的質量標籤 | 跟蹤改進 | 二次通過提示模型："評分清晰度 1-5" |
| 向量記憶 | 語義回憶 | 豐富的長期上下文 | 嵌入摘要，檢索 top-k 到系統消息 |
| 流式回覆 | 更快的感知響應 | 用戶體驗改進 | 使用流式回覆並刷新部分令牌 |
| 確定性測試 | 回歸控制 | 穩定的 CI | 使用 `temperature=0`，固定提示種子運行 |
| 並行分支 | 更快的探索 | 提高吞吐量 | 使用 `concurrent.futures` 處理獨立的代理步驟 |

#### 追蹤記錄範例

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### 簡單評估提示

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

保存（`answer`，`rating`）配對以構建歷史質量圖表。

---

**免責聲明**：  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。