<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f0c6af41a1ae2c5a770c8170da8bd6e",
  "translation_date": "2025-12-16T00:42:08+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "kn"
}
-->
# ಸೆಷನ್ 6 ಮಾದರಿಗಳು: ಸಾಧನಗಳಾಗಿ

ಈ ಮಾದರಿ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತವಾಗಿ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡುವ ಮತ್ತು Foundry Local ನ OpenAI-ಸಮ್ಮತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಕರೆ ಮಾಡುವ ಕನಿಷ್ಠ ರೌಟರ್ + ಸಾಧನ ರಿಜಿಸ್ಟ್ರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತದೆ.

## ಫೈಲ್‌ಗಳು
- `router.py`: ಸರಳ ರಿಜಿಸ್ಟ್ರಿ ಮತ್ತು ಹ್ಯೂರಿಸ್ಟಿಕ್ ರೌಟಿಂಗ್; ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ವೇಷಣೆ + ಆರೋಗ್ಯ ಪರಿಶೀಲನೆ.

## ರನ್ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## ಟಿಪ್ಪಣಿಗಳು
- ರೌಟರ್ ಸರಳ ಕೀವರ್ಡ್ ಹ್ಯೂರಿಸ್ಟಿಕ್ಸ್ ಬಳಸಿ `general`, `reasoning`, ಮತ್ತು `code` ಸಾಧನಗಳ ನಡುವೆ ಆಯ್ಕೆಮಾಡುತ್ತದೆ ಮತ್ತು ಪ್ರಾರಂಭದಲ್ಲಿ `/v1/models` ಅನ್ನು ಮುದ್ರಿಸುತ್ತದೆ.
- ಪರಿಸರ ಚರಗಳ ಮೂಲಕ ಸಂರಚಿಸಿ:
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

## ಉಲ್ಲೇಖಗಳು
- Foundry Local (ಕಲಿಯಿರಿ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ಇನ್ಫರೆನ್ಸ್ SDK ಗಳೊಂದಿಗೆ ಏಕೀಕರಣ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->