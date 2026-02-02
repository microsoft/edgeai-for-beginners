# 第五節範例：多代理協作

此範例展示了使用 Foundry Local 的 OpenAI 相容端點進行協調者 + 專家模式的應用。

## 執行 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## 驗證
```cmd
curl http://localhost:8000/v1/models
```

## 疑難排解
- 如果 VS Code 在 `coordinator.py` 中標記 `import specialists` 為未解析，請確保以模組方式執行，且解譯器指向 `Module08/.venv`：
	- 執行：`python -m samples.05.agents.coordinator`
	- 選擇解譯器：`Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## 參考資料
- Foundry Local (學習): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents 概述: https://learn.microsoft.com/azure/ai-services/agents/overview
- 函數呼叫範例 (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

