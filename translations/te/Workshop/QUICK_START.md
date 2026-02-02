# వర్క్‌షాప్ క్విక్ స్టార్ట్ గైడ్

## ముందస్తు అవసరాలు

### 1. Foundry Local ఇన్‌స్టాల్ చేయండి

అధికారిక ఇన్‌స్టాలేషన్ గైడ్‌ను అనుసరించండి:  
https://github.com/microsoft/Foundry-Local

```bash
# ఫౌండ్రీ లోకల్ సర్వీస్ ప్రారంభించండి
foundry service start

# ఒక మోడల్ లోడ్ చేయండి (వర్క్‌షాప్ కోసం phi-4-mini సిఫార్సు చేయబడింది)
foundry model run phi-4-mini

# సర్వీస్ నడుస్తున్నదని నిర్ధారించుకోండి
foundry service status
```

### 2. Python డిపెండెన్సీలు ఇన్‌స్టాల్ చేయండి

వర్క్‌షాప్ డైరెక్టరీ నుండి:

```bash
# వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి (సిఫార్సు చేయబడింది)
python -m venv .venv

# వర్చువల్ ఎన్విరాన్‌మెంట్‌ను యాక్టివేట్ చేయండి
# విండోస్:
.venv\Scripts\activate
# మాక్‌ఓఎస్/లినక్స్:
source .venv/bin/activate

# అవసరాలను ఇన్‌స్టాల్ చేయండి
pip install -r requirements.txt
```

## వర్క్‌షాప్ నమూనాలు నడపడం

### సెషన్ 01: ప్రాథమిక చాట్

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**పరిసర వేరియబుల్స్:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### సెషన్ 02: RAG పైప్‌లైన్

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**పరిసర వేరియబుల్స్:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### సెషన్ 02: RAG మూల్యాంకనం (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**గమనిక**: `requirements.txt` ద్వారా అదనపు డిపెండెన్సీలు అవసరం

### సెషన్ 03: బెంచ్‌మార్కింగ్

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**పరిసర వేరియబుల్స్:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**ఫలితం**: లేటెన్సీ, థ్రూపుట్, మరియు మొదటి-టోకెన్ మెట్రిక్స్‌తో JSON

### సెషన్ 04: మోడల్ పోలిక

```bash
cd Workshop/samples
python -m session04.model_compare
```

**పరిసర వేరియబుల్స్:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### సెషన్ 05: మల్టీ-ఏజెంట్ ఆర్కెస్ట్రేషన్

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**పరిసర వేరియబుల్స్:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### సెషన్ 06: మోడల్ రౌటర్

```bash
cd Workshop/samples
python -m session06.models_router
```

**పరీక్షలు రౌటింగ్ లాజిక్**ను బహుళ ఉద్దేశాలతో (కోడ్, సారాంశం, వర్గీకరణ)

### సెషన్ 06: పైప్‌లైన్

```bash
python -m session06.models_pipeline
```

**సంక్లిష్టమైన బహుళ-దశ పైప్‌లైన్** ప్లానింగ్, అమలు, మరియు మెరుగుదలతో

## స్క్రిప్టులు

### బెంచ్‌మార్క్ రిపోర్ట్ ఎగుమతి

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**ఫలితం**: మార్క్‌డౌన్ పట్టిక + JSON మెట్రిక్స్

### మార్క్‌డౌన్ CLI నమూనాలు లింట్ చేయడం

```bash
python lint_markdown_cli.py --verbose
```

**ఉద్దేశ్యం**: డాక్యుమెంటేషన్‌లో పాత CLI నమూనాలను గుర్తించడం

## పరీక్షలు

### స్మోక్ టెస్టులు

```bash
cd Workshop
python -m tests.smoke
```

**పరీక్షలు**: ముఖ్య నమూనాల ప్రాథమిక కార్యాచరణ

## సమస్య పరిష్కారం

### సర్వీస్ నడవడం లేదు

```bash
# స్థితిని తనిఖీ చేయండి
foundry service status

# నడుస్తున్నట్లయితే ప్రారంభించండి
foundry service start

# ఒక మోడల్ లోడ్ చేయండి
foundry model run phi-4-mini
```

### మాడ్యూల్ దిగుమతి లోపాలు

```bash
# వర్చువల్ ఎన్విరాన్‌మెంట్ సక్రియమై ఉందని నిర్ధారించుకోండి
.venv\Scripts\activate  # విండోస్
source .venv/bin/activate  # మాక్OS/లినక్స్

# ఆధారాలను మళ్లీ ఇన్‌స్టాల్ చేయండి
pip install -r requirements.txt
```

### కనెక్షన్ లోపాలు

```bash
# ఎండ్‌పాయింట్‌ను తనిఖీ చేయండి
foundry service status

# అవసరమైతే స్పష్టమైన ఎండ్‌పాయింట్‌ను సెట్ చేయండి
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### మోడల్ కనుగొనబడలేదు

```bash
# అందుబాటులో ఉన్న మోడల్స్ జాబితా
foundry model list

# ఒక మోడల్ డౌన్లోడ్ చేసి నడపండి
foundry model run phi-4-mini
```

## పరిసర వేరియబుల్స్ సూచిక

### కోర్ కాన్ఫిగరేషన్
| వేరియబుల్ | డిఫాల్ట్ | వివరణ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | మారుతుంది | ఉపయోగించాల్సిన మోడల్ అలియాస్ |
| `FOUNDRY_LOCAL_ENDPOINT` | ఆటో | సర్వీస్ ఎండ్‌పాయింట్‌ను ఓవర్‌రైడ్ చేయండి |
| `SHOW_USAGE` | `0` | టోకెన్ వినియోగం గణాంకాలు చూపించు |
| `RETRY_ON_FAIL` | `1` | రీట్రై లాజిక్ ఎనేబుల్ చేయండి |
| `RETRY_BACKOFF` | `1.0` | ప్రారంభ రీట్రై ఆలస్యం (సెకన్లు) |

### సెషన్-స్పెసిఫిక్
| వేరియబుల్ | డిఫాల్ట్ | వివరణ |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ఎంబెడ్డింగ్ మోడల్ |
| `RAG_QUESTION` | నమూనా చూడండి | RAG పరీక్ష ప్రశ్న |
| `BENCH_MODELS` | మారుతుంది | కామాతో విడదీసిన మోడల్స్ |
| `BENCH_ROUNDS` | `3` | బెంచ్‌మార్క్ పునరావృతులు |
| `BENCH_PROMPT` | నమూనా చూడండి | బెంచ్‌మార్క్ ప్రాంప్ట్ |
| `BENCH_STREAM` | `0` | మొదటి-టోకెన్ లేటెన్సీ కొలవడం |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | ప్రాథమిక ఏజెంట్ మోడల్ |
| `AGENT_MODEL_EDITOR` | ప్రాథమిక | ఎడిటర్ ఏజెంట్ మోడల్ |
| `SLM_ALIAS` | `phi-4-mini` | చిన్న భాషా మోడల్ |
| `LLM_ALIAS` | `qwen2.5-7b` | పెద్ద భాషా మోడల్ |
| `COMPARE_PROMPT` | నమూనా చూడండి | పోలిక ప్రాంప్ట్ |

## సిఫార్సు చేసిన మోడల్స్

### అభివృద్ధి & పరీక్షలు
- **phi-4-mini** - సమతుల్యమైన నాణ్యత మరియు వేగం  
- **qwen2.5-0.5b** - వర్గీకరణకు చాలా వేగంగా  
- **gemma-2-2b** - మంచి నాణ్యత, మోస్తరు వేగం  

### ఉత్పత్తి సందర్భాలు
- **phi-4-mini** - సాధారణ ప్రయోజనం  
- **deepseek-coder-1.3b** - కోడ్ ఉత్పత్తి  
- **qwen2.5-7b** - ఉన్నత నాణ్యత ప్రతిస్పందనలు  

## SDK డాక్యుమెంటేషన్

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## సహాయం పొందడం

1. సర్వీస్ స్థితి తనిఖీ చేయండి: `foundry service status`  
2. లాగ్‌లు చూడండి: Foundry Local సర్వీస్ లాగ్‌లు తనిఖీ చేయండి  
3. SDK డాక్యుమెంటేషన్ చూడండి: https://github.com/microsoft/Foundry-Local  
4. నమూనా కోడ్ సమీక్షించండి: అన్ని నమూనాలకు వివరమైన డాక్స్ట్రింగ్స్ ఉన్నాయి  

## తదుపరి దశలు

1. అన్ని వర్క్‌షాప్ సెషన్లను క్రమంగా పూర్తి చేయండి  
2. వివిధ మోడల్స్‌తో ప్రయోగాలు చేయండి  
3. మీ ఉపయోగాల కోసం నమూనాలను సవరించండి  

---

**చివరిసారిగా నవీకరించబడింది**: 2025-01-08  
**వర్క్‌షాప్ వెర్షన్**: తాజా  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->