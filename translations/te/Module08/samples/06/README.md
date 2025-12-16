<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f0c6af41a1ae2c5a770c8170da8bd6e",
  "translation_date": "2025-12-16T00:41:38+00:00",
  "source_file": "Module08/samples/06/README.md",
  "language_code": "te"
}
-->
# సెషన్ 6 నమూనా: టూల్స్‌గా మోడల్స్

ఈ నమూనా ఒక కనిష్ట రౌటర్ + టూల్ రిజిస్ట్రీని అమలు చేస్తుంది, ఇది యూజర్ ప్రాంప్ట్ ఆధారంగా ఒక మోడల్‌ను ఎంచుకుని Foundry Local యొక్క OpenAI-అనుకూల ఎండ్‌పాయింట్‌ను పిలుస్తుంది.

## ఫైళ్లు
- `router.py`: సాదా రిజిస్ట్రీ మరియు హ్యూరిస్టిక్ రౌటింగ్; ఎండ్‌పాయింట్ కనుగొనడం + ఆరోగ్య తనిఖీ.

## రన్ (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## గమనికలు
- రౌటర్ సాదా కీవర్డ్ హ్యూరిస్టిక్స్ ఉపయోగించి `general`, `reasoning`, మరియు `code` టూల్స్ మధ్య ఎంచుకుంటుంది మరియు ప్రారంభంలో `/v1/models` ను ప్రింట్ చేస్తుంది.
- వాతావరణ వేరియబుల్స్ ద్వారా కాన్ఫిగర్ చేయండి:
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

## సూచనలు
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ఇన్ఫరెన్స్ SDKలతో ఇంటిగ్రేట్ చేయడం: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. అసలు పత్రం దాని స్వదేశీ భాషలో ఉన్నది అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->