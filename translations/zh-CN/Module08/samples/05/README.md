# 第五节示例：多代理协调

此示例展示了使用 Foundry Local 的 OpenAI 兼容端点实现协调器 + 专家模式。

## 运行 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## 验证
```cmd
curl http://localhost:8000/v1/models
```

## 故障排除
- 如果 VS Code 在 `coordinator.py` 中标记 `import specialists` 为未解析，请确保以模块方式运行，并且解释器指向 `Module08/.venv`：
	- 运行：`python -m samples.05.agents.coordinator`
	- 选择解释器：`Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## 参考资料
- Foundry Local (学习): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents 概述: https://learn.microsoft.com/azure/ai-services/agents/overview
- 函数调用示例 (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

