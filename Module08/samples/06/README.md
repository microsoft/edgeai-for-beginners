# Session 6 Sample: Models as Tools

This sample implements a minimal router + tool registry that selects a model based on the user prompt and calls Foundry Local’s OpenAI-compatible endpoint.

## Files
- `router.py`: simple registry and heuristic routing; endpoint discovery + health check.

## Run (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run deepseek-r1-7b
foundry model run qwen2.5-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notes
- The router uses simple keyword heuristics to pick between `general`, `reasoning`, and `code` tools and prints `/v1/models` on start.
- Configure via environment variables:
```cmd
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## References
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrate with inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
