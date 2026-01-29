# ಸೆಷನ್ 5 ಮಾದರಿ: ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ

ಈ ಮಾದರಿ ಫೌಂಡ್ರಿ ಲೋಕಲ್‌ನ OpenAI-ಸಮ್ಮತ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಬಳಸಿ ಸಂಯೋಜಕ + ತಜ್ಞರ ಮಾದರಿಯನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ.

## ರನ್ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## ಮಾನ್ಯತೆ
```cmd
curl http://localhost:8000/v1/models
```

## ಸಮಸ್ಯೆ ಪರಿಹಾರ
- VS ಕೋಡ್ `coordinator.py` ನಲ್ಲಿ `import specialists` ಅನ್ನು ಪರಿಹರಿಸಲಾಗದಂತೆ ಗುರುತಿಸಿದರೆ, ನೀವು ಮಾಯಾಜಾಲವಾಗಿ (module) ರನ್ ಮಾಡುತ್ತಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿ ಮತ್ತು ವ್ಯಾಖ್ಯಾತಕ (interpreter) `Module08/.venv` ಕಡೆ ಸೂಚಿಸುತ್ತಿದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ:
	- ರನ್ ಮಾಡಿ: `python -m samples.05.agents.coordinator`
	- ವ್ಯಾಖ್ಯಾತಕ ಆಯ್ಕೆಮಾಡಿ: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## ಉಲ್ಲೇಖಗಳು
- ಫೌಂಡ್ರಿ ಲೋಕಲ್ (ಕಲಿಯಿರಿ): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ಅಜೂರ್ AI ಏಜೆಂಟ್ಸ್ ಅವಲೋಕನ: https://learn.microsoft.com/azure/ai-services/agents/overview
- ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಮಾದರಿ (ಫೌಂಡ್ರಿ ಲೋಕಲ್): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->