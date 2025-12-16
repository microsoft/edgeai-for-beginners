<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-12-15T20:26:43+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "te"
}
-->
# పరిసరాల కాన్ఫిగరేషన్ గైడ్

## అవలోకనం

వర్క్‌షాప్ నమూనాలు కాన్ఫిగరేషన్ కోసం పరిసర వేరియబుల్స్‌ను ఉపయోగిస్తాయి, ఇవి రిపోజిటరీ రూట్‌లోని `.env` ఫైల్‌లో కేంద్రీకృతంగా ఉంటాయి. ఇది కోడ్ మార్చకుండా సులభంగా అనుకూలీకరించడానికి అనుమతిస్తుంది.

## త్వరిత ప్రారంభం

### 1. ముందస్తు అవసరాలను ధృవీకరించండి

```bash
# Foundry Local ఇన్‌స్టాల్ అయిందో లేదో తనిఖీ చేయండి
foundry --version

# సర్వీస్ నడుస్తుందో లేదో తనిఖీ చేయండి
foundry service status

# ఒక మోడల్ లోడ్ చేయండి
foundry model run phi-4-mini
```

### 2. పరిసరాన్ని కాన్ఫిగర్ చేయండి

`.env` ఫైల్ ఇప్పటికే సున్నితమైన డిఫాల్ట్‌లతో కాన్ఫిగర్ చేయబడింది. ఎక్కువ మంది వినియోగదారులు ఏదీ మార్చాల్సిన అవసరం ఉండదు.

**ఐచ్ఛికం**: సెట్టింగులను సమీక్షించి అనుకూలీకరించండి:
```bash
# .env ఫైల్‌ను సవరించండి
notepad .env  # విండోస్
nano .env     # మాక్OS/లినక్స్
```

### 3. కాన్ఫిగరేషన్‌ను వర్తింపజేయండి

**Python స్క్రిప్టుల కోసం:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# పర్యావరణ చరాలు స్వయంచాలకంగా లోడ్ చేయబడ్డాయి
```

**నోట్‌బుక్స్ కోసం:**
```python
# .env మార్పుల తర్వాత కర్నెల్‌ను రీస్టార్ట్ చేయండి
# సెల్స్ అమలు చేసినప్పుడు వేరియబుల్స్ లోడ్ అవుతాయి
```

## పరిసర వేరియబుల్స్ సూచిక

### కోర్ కాన్ఫిగరేషన్

| వేరియబుల్ | డిఫాల్ట్ | వివరణ |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | నమూనాల కోసం డిఫాల్ట్ మోడల్ |
| `FOUNDRY_LOCAL_ENDPOINT` | (ఖాళీ) | సర్వీస్ ఎండ్‌పాయింట్‌ను ఓవర్‌రైడ్ చేయండి |
| `PYTHONPATH` | వర్క్‌షాప్ మార్గాలు | Python మాడ్యూల్ శోధన మార్గం |

**ఎప్పుడు FOUNDRY_LOCAL_ENDPOINT సెట్ చేయాలి:**
- రిమోట్ ఫౌండ్రీ లోకల్ ఇన్స్టాన్స్
- కస్టమ్ పోర్ట్ కాన్ఫిగరేషన్
- అభివృద్ధి/ఉత్పత్తి వేరుపాటు

**ఉదాహరణ:**
```bash
# స్థానిక కస్టమ్ పోర్ట్
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# రిమోట్ ఇన్స్టాన్స్
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### సెషన్-స్పెసిఫిక్ వేరియబుల్స్

#### సెషన్ 02: RAG పైప్‌లైన్
| వేరియబుల్ | డిఫాల్ట్ | ఉద్దేశ్యం |
|----------|---------|---------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | ఎంబెడ్డింగ్ మోడల్ |
| `RAG_QUESTION` | ముందుగా కాన్ఫిగర్ చేయబడింది | పరీక్ష ప్రశ్న |

#### సెషన్ 03: బెంచ్‌మార్కింగ్
| వేరియబుల్ | డిఫాల్ట్ | ఉద్దేశ్యం |
|----------|---------|---------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | బెంచ్‌మార్క్ చేయాల్సిన మోడల్స్ |
| `BENCH_ROUNDS` | `3` | ప్రతి మోడల్‌కు పునరావృతాలు |
| `BENCH_PROMPT` | ముందుగా కాన్ఫిగర్ చేయబడింది | పరీక్ష ప్రాంప్ట్ |
| `BENCH_STREAM` | `0` | మొదటి టోకెన్ లేటెన్సీ కొలవండి |

#### సెషన్ 04: మోడల్ పోలిక
| వేరియబుల్ | డిఫాల్ట్ | ఉద్దేశ్యం |
|----------|---------|---------|
| `SLM_ALIAS` | `phi-4-mini` | చిన్న భాషా మోడల్ |
| `LLM_ALIAS` | `qwen2.5-7b` | పెద్ద భాషా మోడల్ |
| `COMPARE_PROMPT` | ముందుగా కాన్ఫిగర్ చేయబడింది | పోలిక ప్రాంప్ట్ |
| `COMPARE_RETRIES` | `2` | మళ్లీ ప్రయత్నాల సంఖ్య |

#### సెషన్ 05: బహుళ ఏజెంట్ ఆర్కెస్ట్రేషన్
| వేరియబుల్ | డిఫాల్ట్ | ఉద్దేశ్యం |
|----------|---------|---------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | పరిశోధక ఏజెంట్ మోడల్ |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | ఎడిటర్ ఏజెంట్ మోడల్ |
| `AGENT_QUESTION` | ముందుగా కాన్ఫిగర్ చేయబడింది | పరీక్ష ప్రశ్న |

### నమ్మకదారితన కాన్ఫిగరేషన్

| వేరియబుల్ | డిఫాల్ట్ | ఉద్దేశ్యం |
|----------|---------|---------|
| `SHOW_USAGE` | `1` | టోకెన్ వినియోగాన్ని ప్రింట్ చేయండి |
| `RETRY_ON_FAIL` | `1` | మళ్లీ ప్రయత్నించే లాజిక్‌ను ఎనేబుల్ చేయండి |
| `RETRY_BACKOFF` | `1.0` | మళ్లీ ప్రయత్నించే ఆలస్యం (సెకన్లు) |

## సాధారణ కాన్ఫిగరేషన్లు

### అభివృద్ధి సెటప్ (త్వరిత పునరావృతం)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### ఉత్పత్తి సెటప్ (నాణ్యతపై దృష్టి)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### బెంచ్‌మార్కింగ్ సెటప్
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### బహుళ ఏజెంట్ ప్రత్యేకత
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # పరిశోధన కోసం వేగంగా
AGENT_MODEL_EDITOR=qwen2.5-7b         # సవరించడానికి నాణ్యత
```

### రిమోట్ అభివృద్ధి
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## సిఫార్సు చేసిన మోడల్స్

### ఉపయోగం ప్రకారం

**సాధారణ ప్రయోజనం:**
- `phi-4-mini` - సమతుల్య నాణ్యత మరియు వేగం

**త్వరిత ప్రతిస్పందనలు:**
- `qwen2.5-0.5b` - చాలా వేగంగా, వర్గీకరణకు మంచిది
- `phi-4-mini` - మంచి నాణ్యతతో వేగంగా

**అత్యున్నత నాణ్యత:**
- `qwen2.5-7b` - ఉత్తమ నాణ్యత, ఎక్కువ వనరుల వినియోగం
- `phi-4-mini` - మంచి నాణ్యత, తక్కువ వనరులు

**కోడ్ జనరేషన్:**
- `deepseek-coder-1.3b` - కోడ్ కోసం ప్రత్యేకీకరించబడింది
- `phi-4-mini` - సాధారణ ప్రయోజన కోడింగ్

### వనరుల అందుబాటులో

**తక్కువ వనరులు (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**మధ్యస్థ వనరులు (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**అధిక వనరులు (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## అధునాతన కాన్ఫిగరేషన్

### కస్టమ్ ఎండ్‌పాయింట్లు

```bash
# అభివృద్ధి వాతావరణం
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# స్టేజింగ్ వాతావరణం
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# ఉత్పత్తి వాతావరణం
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### ఉష్ణోగ్రత & శాంప్లింగ్ (కోడ్‌లో ఓవర్‌రైడ్ చేయండి)

```python
# మీ స్క్రిప్ట్స్/నోట్‌బుక్స్‌లో
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI హైబ్రిడ్ సెటప్

```bash
# అభివృద్ధికి లోకల్ ఉపయోగించండి
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# ఉత్పత్తి ఫాల్బ్యాక్ కోసం Azure ను కాన్ఫిగర్ చేయండి
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## సమస్య పరిష్కారం

### పరిసర వేరియబుల్స్ లోడ్ కాలేదు

**లక్షణాలు:**
- స్క్రిప్టులు తప్పు మోడల్స్ ఉపయోగిస్తున్నాయి
- కనెక్షన్ లోపాలు
- వేరియబుల్స్ గుర్తించబడలేదు

**పరిష్కారాలు:**
```bash
# 1. రిపాజిటరీ రూట్‌లో .env ఉన్నదని నిర్ధారించుకోండి
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. ఫైల్ .env.txt కాదు అని తనిఖీ చేయండి (Windows)
# దాచిన ఎక్స్‌టెన్షన్ ఉండకూడదు

# 3. నోట్‌బుక్స్ కోసం: కర్నెల్‌ను రీస్టార్ట్ చేయండి
# కర్నెల్ > రీస్టార్ట్

# 4. స్క్రిప్ట్స్ కోసం: వర్కింగ్ డైరెక్టరీని తనిఖీ చేయండి
pwd  # ఇది వర్క్‌షాప్ లేదా రిపాజిటరీ రూట్‌లో ఉండాలి
```

### సర్వీస్ కనెక్షన్ సమస్యలు

**లక్షణాలు:**
- "కనెక్షన్ నిరాకరించబడింది" లోపాలు
- "సర్వీస్ అందుబాటులో లేదు"
- టైమ్‌అవుట్ లోపాలు

**పరిష్కారాలు:**
```bash
# 1. సేవ స్థితిని తనిఖీ చేయండి
foundry service status

# 2. నడుస్తున్నట్లయితే ప్రారంభించండి
foundry service start

# 3. ఎండ్‌పాయింట్‌ను ధృవీకరించండి
# స్థితి అవుట్‌పుట్‌లో పోర్ట్‌ను తనిఖీ చేయండి
foundry service status | grep "Port"

# 4. అవసరమైతే .env ను నవీకరించండి
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### మోడల్ కనుగొనబడలేదు

**లక్షణాలు:**
- "మోడల్ కనుగొనబడలేదు" లోపాలు
- "అలియాస్ గుర్తించబడలేదు"

**పరిష్కారాలు:**
```bash
# 1. అందుబాటులో ఉన్న మోడల్స్ జాబితా చేయండి
foundry model list

# 2. అవసరమైన మోడల్‌ను లోడ్ చేయండి
foundry model run phi-4-mini

# 3. అందుబాటులో ఉన్న మోడల్‌తో .env ను నవీకరించండి
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### ఇంపోర్ట్ లోపాలు

**లక్షణాలు:**
- "మాడ్యూల్ కనుగొనబడలేదు" లోపాలు

**పరిష్కారాలు:**

```bash
# 1. వర్చువల్ ఎన్విరాన్‌మెంట్‌ను సక్రియం చేయండి
.venv\Scripts\activate  # విండోస్
source .venv/bin/activate  # మాక్‌ఓఎస్/లినక్స్

# 2. ఆధారాలను ఇన్‌స్టాల్ చేయండి
pip install -r requirements.txt
```

## పరీక్షా కాన్ఫిగరేషన్

### పరిసర లోడింగ్‌ను ధృవీకరించండి

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### ఫౌండ్రీ లోకల్ కనెక్షన్‌ను పరీక్షించండి

```python
# టెస్ట్_కనెక్షన్.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## భద్రత ఉత్తమ ఆచారాలు

### 1. రహస్యాలను ఎప్పుడూ కమిట్ చేయవద్దు

```bash
# .gitignore లో ఈవాటిని చేర్చాలి:
.env
.env.local
*.key
```

### 2. వేర్వేరు .env ఫైళ్లను ఉపయోగించండి

```bash
.env              # డిఫాల్ట్ కాన్ఫిగరేషన్
.env.local        # స్థానిక ఓవర్‌రైడ్లు (గిట్‌ఇగ్నోర్ చేయబడింది)
.env.production   # ఉత్పత్తి కాన్ఫిగ్ (సురక్షిత నిల్వ)
```

### 3. API కీలు రొటేట్ చేయండి

```bash
# Azure OpenAI లేదా ఇతర క్లౌడ్ సేవల కోసం
# కీలు నియమితంగా మార్చండి మరియు .env ను నవీకరించండి
```

### 4. పరిసర-స్పెసిఫిక్ కాన్ఫిగరేషన్ ఉపయోగించండి

```bash
# అభివృద్ధి
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# ఉత్పత్తి (రహస్యాల నిర్వహణను ఉపయోగించండి)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK డాక్యుమెంటేషన్

- **ప్రధాన రిపోజిటరీ**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API డాక్యుమెంటేషన్**: తాజా కోసం SDK రిపోజిటరీని తనిఖీ చేయండి

## అదనపు వనరులు

- `QUICK_START.md` - ప్రారంభ గైడ్
- `Workshop/samples/*/README.md` - నమూనా-స్పెసిఫిక్ గైడ్లు

---

**చివరిసారిగా నవీకరించబడింది**: 2025-01-08  
**సంస్కరణ**: 2.0  
**SDK**: Foundry Local Python SDK (తాజా)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->