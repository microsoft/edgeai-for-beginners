# 第六节示例：模型作为工具

此示例实现了一个最小化的路由器和工具注册表，根据用户提示选择模型，并调用 Foundry Local 的 OpenAI 兼容端点。

## 文件
- `router.py`：简单的注册表和启发式路由；端点发现和健康检查。

## 运行（cmd.exe）
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 注意事项
- 路由器使用简单的关键词启发式方法在 `general`、`reasoning` 和 `code` 工具之间进行选择，并在启动时打印 `/v1/models`。
- 通过环境变量进行配置：
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## 参考资料
- Foundry Local（学习）：https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 与推理 SDK 集成：https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。