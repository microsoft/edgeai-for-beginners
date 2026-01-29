# సెషన్ 4: ఆధునిక మోడల్స్ అన్వేషణ – LLMs, SLMs & ఆన్-డివైస్ ఇన్ఫరెన్స్

## సారాంశం

స్థానిక మరియు క్లౌడ్ ఇన్ఫరెన్స్ సందర్భాలలో పెద్ద భాషా మోడల్స్ (LLMs) మరియు చిన్న భాషా మోడల్స్ (SLMs) ను పోల్చండి. ONNX రన్‌టైమ్ వేగవంతీకరణ, WebGPU ఎగ్జిక్యూషన్, మరియు హైబ్రిడ్ RAG అనుభవాలను ఉపయోగించి డిప్లాయ్‌మెంట్ నమూనాలను నేర్చుకోండి. స్థానిక మోడల్‌తో కూడిన Chainlit RAG డెమో మరియు ఐచ్ఛిక OpenWebUI అన్వేషణను కలిగి ఉంటుంది. మీరు WebGPU ఇన్ఫరెన్స్ స్టార్టర్‌ను అనుకూలపరచి Phi మరియు GPT-OSS-20B సామర్థ్యం & ఖర్చు/పర్ఫార్మెన్స్ ట్రేడ్-ఆఫ్స్‌ను అంచనా వేస్తారు.

## నేర్చుకునే లక్ష్యాలు

- **SLM మరియు LLM** ను లేటెన్సీ, మెమరీ, నాణ్యత పరిమాణాలపై **తులనాత్మకంగా** చూడండి  
- ONNXRuntime మరియు (మద్దతు ఉన్న చోట) WebGPU తో **మోడల్స్‌ను డిప్లాయ్ చేయండి**  
- బ్రౌజర్ ఆధారిత ఇన్ఫరెన్స్‌ను **నడపండి** (గోప్యతా పరిరక్షణతో ఇంటరాక్టివ్ డెమో)  
- స్థానిక SLM బ్యాక్‌ఎండ్‌తో Chainlit RAG పైప్‌లైన్‌ను **ఇంటిగ్రేట్ చేయండి**  
- తేలికపాటి నాణ్యత + ఖర్చు హ్యూరిస్టిక్స్ ఉపయోగించి **అంచనా వేయండి**

## ముందస్తు అవసరాలు

- సెషన్లు 1–3 పూర్తి చేయబడినవి  
- `chainlit` ఇన్‌స్టాల్ చేయబడింది (Module08 కోసం `requirements.txt` లో ఇప్పటికే ఉంది)  
- WebGPU-సమర్థ బ్రౌజర్ (Windows 11 పై Edge / Chrome తాజా వెర్షన్)  
- Foundry Local నడుస్తోంది (`foundry service status`)

### క్రాస్-ప్లాట్‌ఫారమ్ గమనికలు

Windows ప్రధాన లక్ష్య వాతావరణంగా ఉంటుంది. macOS డెవలపర్లు స్థానిక బైనరీలను ఎదురుచూస్తున్నట్లయితే:  
1. Windows 11 VM (Parallels / UTM) లేదా రిమోట్ Windows వర్క్‌స్టేషన్‌లో Foundry Local నడపండి.  
2. సర్వీస్‌ను (డిఫాల్ట్ పోర్ట్ 5273) ఎక్స్‌పోజ్ చేసి macOS లో సెట్ చేయండి:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
3. గత సెషన్లలో ఉపయోగించినట్లే Python వర్చువల్ ఎన్విరాన్‌మెంట్ దశలను అనుసరించండి.

Chainlit ఇన్‌స్టాల్ (రెండు ప్లాట్‌ఫారమ్‌లకు):  
```bash
pip install chainlit
```
  
## డెమో ఫ్లో (30 నిమిషాలు)

### 1. Phi (SLM) vs GPT-OSS-20B (LLM) పోలిక (6 నిమిషాలు)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# వేగవంతమైన సామర్థ్య పరీక్షలు (ఒకసారి, ఇంటరాక్టివ్ కాని)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# ప్రాథమిక టోకెన్ / ఆలస్యం పరీక్ష (అనుభూతికి కొన్నిసార్లు పునరావృతం చేయండి)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```
  
ట్రాక్ చేయండి: ప్రతిస్పందన లోతు, వాస్తవ సత్యం, శైలీ సంపద, లేటెన్సీ.

GPU ఎనేబుల్ చేసిన తర్వాత CPU-మాత్రం తో పోల్చి థ్రూపుట్ మార్పులను గమనించండి.

### 3. బ్రౌజర్‌లో WebGPU ఇన్ఫరెన్స్ (6 నిమిషాలు)

స్టార్టర్ `04-webgpu-inference` ను అనుకూలపరచండి (`samples/04-cutting-edge/webgpu_demo.html` సృష్టించండి):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```
  
ఫైల్‌ను బ్రౌజర్‌లో తెరవండి; తక్కువ లేటెన్సీ స్థానిక రౌండ్‌ట్రిప్ గమనించండి.

### 4. Chainlit RAG చాట్ యాప్ (7 నిమిషాలు)

కనిష్ట `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # సాదాసీదా లెక్సికల్ స్కోరింగ్
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```
  
నడపండి:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```
  
### 5. స్టార్టర్ ప్రాజెక్ట్: `04-webgpu-inference` అనుకూలీకరణ (6 నిమిషాలు)

డెలివరబుల్స్:  
- ప్లేస్‌హోల్డర్ ఫెచ్ లాజిక్‌ను స్ట్రీమింగ్ టోకెన్లతో మార్చండి (`stream=True` ఎండ్పాయింట్ వేరియంట్ ఉపయోగించండి ఒకసారి ఎనేబుల్ అయిన తర్వాత)  
- phi vs gpt-oss-20b టోగుల్‌ల కోసం క్లయింట్-సైడ్ లేటెన్సీ చార్ట్ జోడించండి  
- RAG కాంటెక్స్ట్‌ను ఇన్‌లైన్‌లో ఎంబెడ్ చేయండి (సూచన పత్రాల కోసం టెక్స్ట్ ఏరియా)

## అంచనా హ్యూరిస్టిక్స్

| వర్గం | Phi-4-mini | GPT-OSS-20B | గమనిక |
|----------|------------|-------------|-------------|
| లేటెన్సీ (కోల్డ్) | వేగంగా | మెల్లగా | SLM త్వరగా వేడి అవుతుంది |
| మెమరీ | తక్కువ | ఎక్కువ | పరికరం సాధ్యత |
| కాంటెక్స్ట్ అనుసరణ | మంచి | బలమైన | పెద్ద మోడల్ ఎక్కువ వివరంగా ఉండవచ్చు |
| ఖర్చు (స్థానిక) | కనిష్టం | ఎక్కువ (వనరులు) | శక్తి/సమయం ట్రేడ్-ఆఫ్ |
| ఉత్తమ ఉపయోగం | ఎడ్జ్ యాప్స్ | లోతైన తర్కం | హైబ్రిడ్ పైప్‌లైన్ సాధ్యం |

## వాతావరణ ధృవీకరణ

```powershell
# క్యాటలాగ్ జాబితా (ఒక --running ఫ్లాగ్ లేదు; లోడ్ చేసిన మోడల్స్ మీరు ముందుగా నడిపినవి)
foundry model list

# రన్‌టైమ్ మెట్రిక్స్ కోసం Python బెంచ్‌మార్క్ స్క్రిప్ట్ (సెషన్ 3) మరియు OS టూల్స్ (టాస్క్ మేనేజర్ / nvidia-smi) ఉపయోగించండి 'model stats' బదులు
# ఉదాహరణ:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```
  
## సమస్య పరిష్కారం

| లక్షణం | కారణం | చర్య |
|---------|-------|--------|
| వెబ్ పేజీ ఫెచ్ విఫలమవుతుంది | CORS లేదా సర్వీస్ డౌన్ | ఎండ్పాయింట్‌ను `curl` తో ధృవీకరించండి; అవసరమైతే CORS ప్రాక్సీ ఎనేబుల్ చేయండి |
| Chainlit ఖాళీగా ఉంది | ఎన్విరాన్‌మెంట్ సక్రియం కాదు | వర్చువల్ ఎన్విరాన్‌మెంట్ యాక్టివేట్ చేసి డిపెండెన్సీలు మళ్లీ ఇన్‌స్టాల్ చేయండి |
| అధిక లేటెన్సీ | మోడల్ తాజాగా లోడ్ అయింది | చిన్న ప్రాంప్ట్ సీక్వెన్స్‌తో వేడి చేయండి |

## సూచనలు

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Chainlit డాక్స్: https://docs.chainlit.io  
- RAG అంచనా (Ragas): https://docs.ragas.io

---

**సెషన్ వ్యవధి**: 30 నిమిషాలు  
**కష్టత**: అధునాతన

## నమూనా సన్నివేశం & వర్క్‌షాప్ మ్యాపింగ్

| వర్క్‌షాప్ ఆర్టిఫాక్ట్స్ | సన్నివేశం | లక్ష్యం | డేటా / ప్రాంప్ట్ మూలం |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | ఎగ్జిక్యూటివ్ సమ్మరీ జనరేటర్ కోసం SLM vs LLM ను ఆర్కిటెక్చర్ టీమ్ అంచనా వేస్తోంది | లేటెన్సీ + టోకెన్ వినియోగం డెల్టాను కొలవడం | ఒకే `COMPARE_PROMPT` ఎన్విరాన్‌మెంట్ వేరియబుల్ |
| `chainlit_app.py` (RAG డెమో) | అంతర్గత జ్ఞాన సహాయక ప్రోటోటైప్ | కనిష్ట లెక్సికల్ రిట్రీవల్‌తో చిన్న సమాధానాలను స్థిరపరచడం | ఫైల్‌లో ఇన్‌లైన్ `DOCS` జాబితా |
| `webgpu_demo.html` | భవిష్యత్తు ఆన్-డివైస్ బ్రౌజర్ ఇన్ఫరెన్స్ ప్రివ్యూ | తక్కువ లేటెన్సీ స్థానిక రౌండ్‌ట్రిప్ + UX కథనం చూపించండి | ప్రత్యక్ష యూజర్ ప్రాంప్ట్ మాత్రమే |

### సన్నివేశ కథనం  
ఉత్పత్తి సంస్థకు ఎగ్జిక్యూటివ్ బ్రీఫింగ్ జనరేటర్ కావాలి. తేలికపాటి SLM (phi-4-mini) సారాంశాలను తయారు చేస్తుంది; పెద్ద LLM (gpt-oss-20b) కేవలం ఉన్నత ప్రాధాన్యత నివేదికలను మెరుగుపరుస్తుంది. సెషన్ స్క్రిప్టులు హైబ్రిడ్ డిజైన్‌ను న్యాయసమ్మతం చేయడానికి అనుభవాత్మక లేటెన్సీ & టోకెన్ మెట్రిక్స్‌ను సేకరిస్తాయి, Chainlit డెమో చిన్న మోడల్ సమాధానాలను వాస్తవానికి అనుగుణంగా ఉంచే గ్రౌండెడ్ రిట్రీవల్‌ను చూపిస్తుంది. WebGPU కాన్సెప్ట్ పేజీ బ్రౌజర్ వేగవంతీకరణ అభివృద్ధి చెందినప్పుడు పూర్తిగా క్లయింట్-సైడ్ ప్రాసెసింగ్ కోసం దృష్టి మార్గాన్ని అందిస్తుంది.

### కనిష్ట RAG కాంటెక్స్ట్ (Chainlit)  
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```
  
### హైబ్రిడ్ డ్రాఫ్ట్→రిఫైన్ ఫ్లో (సూక్ష్మ)  
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: పొడవైన సంక్షిప్తాలు లేదా గుర్తింపు పొందిన విషయాల కోసం మాత్రమే పెంచండి
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```
  
మిశ్రమ సగటు ఖర్చును నివేదించడానికి రెండు లేటెన్సీ భాగాలను ట్రాక్ చేయండి.

### ఐచ్ఛిక మెరుగుదలలు

| దృష్టి | మెరుగుదల | ఎందుకు | అమలు సూచన |
|-------|------------|-----|---------------------|
| తులనాత్మక మెట్రిక్స్ | టోకెన్ వినియోగం + మొదటి టోకెన్ లేటెన్సీ ట్రాక్ చేయండి | సమగ్ర పనితీరు దృశ్యం | మెరుగైన బెంచ్‌మార్క్ స్క్రిప్ట్ (సెషన్ 3) లో `BENCH_STREAM=1` ఉపయోగించండి |
| హైబ్రిడ్ పైప్‌లైన్ | SLM డ్రాఫ్ట్ → LLM రిఫైన్ | లేటెన్సీ & ఖర్చు తగ్గింపు | phi-4-mini తో జనరేట్ చేసి gpt-oss-20b తో సారాంశాన్ని మెరుగుపరచండి |
| స్ట్రీమింగ్ UI | Chainlit లో మెరుగైన UX | దశలవారీ ఫీడ్‌బ్యాక్ | స్థానిక స్ట్రీమింగ్ అందుబాటులోకి వచ్చిన తర్వాత `stream=True` ఉపయోగించండి; భాగాలను సేకరించండి |
| WebGPU క్యాచింగ్ | వేగవంతమైన JS ప్రారంభం | రీకంపైల్ ఓవర్‌హెడ్ తగ్గింపు | కంపైల్ చేసిన షేడర్ ఆర్టిఫాక్ట్స్ క్యాచింగ్ (భవిష్యత్ రన్‌టైమ్ సామర్థ్యం) |
| నిర్ణీత QA సెట్ | న్యాయమైన మోడల్ పోలిక | వైవిధ్యాన్ని తొలగించండి | స్థిరమైన ప్రాంప్ట్ జాబితా + `temperature=0` తో అంచనా పరుగులు |
| అవుట్‌పుట్ స్కోరింగ్ | నిర్మిత నాణ్యత లెన్స్ | అనుభవాల కంటే ముందుకు వెళ్లండి | సాదా రూబ్రిక్: సారాంశం / వాస్తవసత్యం / సంక్షిప్తత (1–5) |
| శక్తి / వనరు గమనికలు | తరగతి చర్చ | ట్రేడ్-ఆఫ్స్ చూపించండి | OS మానిటర్లు (టాస్క్ మేనేజర్, `nvidia-smi`) + బెంచ్‌మార్క్ స్క్రిప్ట్ అవుట్‌పుట్స్ ఉపయోగించండి |
| ఖర్చు అనుకరణ | ప్రీ-క్లౌడ్ న్యాయసమ్మతం | స్కేలింగ్ ప్రణాళిక | టోకెన్లను ఊహాత్మక క్లౌడ్ ధరలతో మ్యాప్ చేసి TCO కథనం చేయండి |
| లేటెన్సీ విభజన | బాటిల్‌నెక్స్ గుర్తించండి | లక్ష్య ఆప్టిమైజేషన్లు | ప్రాంప్ట్ ప్రిపరేషన్, అభ్యర్థన పంపడం, మొదటి టోకెన్, పూర్తి పూర్తి కొలవండి |
| RAG + LLM ఫాల్‌బ్యాక్ | నాణ్యత భద్రతా నెట్ | కష్టమైన ప్రశ్నలను మెరుగుపరచండి | SLM సమాధానం పొడవు < పరిమితి లేదా తక్కువ నమ్మకం → ఎస్కలేట్ చేయండి |

#### ఉదాహరణ హైబ్రిడ్ డ్రాఫ్ట్/రిఫైన్ నమూనా

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```
  
#### లేటెన్సీ విభజన స్కెచ్

```python
import time
t0 = time.time(); # సందేశాలను నిర్మించండి
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```
  
న్యాయమైన పోలికల కోసం మోడల్స్ అంతటా సुसंगత కొలతా నిర్మాణాన్ని ఉపయోగించండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->