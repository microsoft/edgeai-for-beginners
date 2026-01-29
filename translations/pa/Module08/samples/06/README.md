# ਸੈਸ਼ਨ 6 ਨਮੂਨਾ: ਮਾਡਲਾਂ ਨੂੰ ਸੰਦ ਵਜੋਂ ਵਰਤਣਾ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਇੱਕ ਘੱਟੋ-ਘੱਟ ਰਾਊਟਰ + ਸੰਦ ਰਜਿਸਟਰੀ ਸ਼ਾਮਲ ਹੈ ਜੋ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਦੇ ਆਧਾਰ 'ਤੇ ਮਾਡਲ ਚੁਣਦਾ ਹੈ ਅਤੇ Foundry Local ਦੇ OpenAI-ਅਨੁਕੂਲ ਐਂਡਪੌਇੰਟ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ।

## ਫਾਈਲਾਂ
- `router.py`: ਸਧਾਰਨ ਰਜਿਸਟਰੀ ਅਤੇ ਹੀਯੂਰਿਸਟਿਕ ਰਾਊਟਿੰਗ; ਐਂਡਪੌਇੰਟ ਖੋਜ + ਸਿਹਤ ਜਾਂਚ।

## ਚਲਾਓ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## ਨੋਟਸ
- ਰਾਊਟਰ ਸਧਾਰਨ ਕੀਵਰਡ ਹੀਯੂਰਿਸਟਿਕਸ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ `general`, `reasoning`, ਅਤੇ `code` ਸੰਦਾਂ ਵਿੱਚੋਂ ਚੋਣ ਕਰਨ ਲਈ ਅਤੇ ਸ਼ੁਰੂ 'ਤੇ `/v1/models` ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।
- ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਰਾਹੀਂ ਸੰਰਚਨਾ ਕਰੋ:
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

## ਹਵਾਲੇ
- Foundry Local (ਸਿੱਖੋ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ਅਨੁਮਾਨ SDKs ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣੀਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।