<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ed8edea2fc43898c2537130fb3ae6878",
  "translation_date": "2025-12-16T00:42:45+00:00",
  "source_file": "Module08/samples/03/README.md",
  "language_code": "kn"
}
-->
# ಸೆಷನ್ 3 ಮಾದರಿ: ಮಾದರಿ ಅನ್ವೇಷಣೆ ಮತ್ತು ತ್ವರಿತ ಬೆಂಚ್

ಮಾದರಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು ಮತ್ತು ವಿವರವಾದ ಲಾಗ್‌ಗಳೊಂದಿಗೆ ಒಂದನ್ನು ಪ್ರಾರಂಭಿಸಲು ಕನಿಷ್ಠ ಸಹಾಯಕ.

## ರನ್ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
samples\03\list_and_bench.cmd
```

## ಉಲ್ಲೇಖಗಳು
- ಫೌಂಡ್ರಿ ಲೋಕಲ್ CLI ಉಲ್ಲೇಖ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- ಫೌಂಡ್ರಿ ಲೋಕಲ್ GitHub: https://github.com/microsoft/Foundry-Local

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->