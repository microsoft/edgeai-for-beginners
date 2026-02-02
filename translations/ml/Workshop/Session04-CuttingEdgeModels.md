# സെഷൻ 4: ആധുനിക മോഡലുകൾ അന്വേഷിക്കുക – LLMs, SLMs & ഓൺ-ഡിവൈസ് ഇൻഫറൻസ്

## സംഗ്രഹം

പ്രാദേശികവും ക്ലൗഡ് ഇൻഫറൻസ് സാഹചര്യങ്ങളിലുമായി വലിയ ഭാഷാ മോഡലുകൾ (LLMs) ചെറു ഭാഷാ മോഡലുകൾ (SLMs) എന്നിവ താരതമ്യം ചെയ്യുക. ONNX റൺടൈം ആക്സിലറേഷൻ, WebGPU എക്സിക്യൂഷൻ, ഹൈബ്രിഡ് RAG അനുഭവങ്ങൾ ഉപയോഗിച്ച് ഡിപ്ലോയ്മെന്റ് പാറ്റേണുകൾ പഠിക്കുക. ഒരു ലോക്കൽ മോഡലോടുകൂടിയ Chainlit RAG ഡെമോയും ഓപ്ഷണൽ OpenWebUI എക്സ്പ്ലോറേഷനും ഉൾപ്പെടുന്നു. നിങ്ങൾ ഒരു WebGPU ഇൻഫറൻസ് സ്റ്റാർട്ടർ അഡാപ്റ്റ് ചെയ്ത് Phi vs GPT-OSS-20B ശേഷിയും ചെലവ്/പ്രവർത്തന തുല്യങ്ങളും വിലയിരുത്തും.

## പഠന ലക്ഷ്യങ്ങൾ

- **താരതമ്യം ചെയ്യുക** SLM vs LLM ലാറ്റൻസി, മെമ്മറി, ഗുണനിലവാര അക്ഷങ്ങളിൽ
- **ഡിപ്ലോയ് ചെയ്യുക** മോഡലുകൾ ONNXRuntime ഉപയോഗിച്ച് (സഹായിക്കുന്നിടത്ത്) WebGPU-യോടൊപ്പം
- **ഓടിക്കുക** ബ്രൗസർ അടിസ്ഥാന ഇൻഫറൻസ് (സ്വകാര്യത സംരക്ഷിക്കുന്ന ഇന്ററാക്ടീവ് ഡെമോ)
- **ഇന്റഗ്രേറ്റ് ചെയ്യുക** Chainlit RAG പൈപ്പ്‌ലൈൻ ഒരു പ്രാദേശിക SLM ബാക്ക്‌എൻഡുമായി
- **വിലയിരുത്തുക** ലഘു ഗുണനിലവാരവും ചെലവും അടിസ്ഥാനമാക്കിയുള്ള ഹ്യൂറിസ്റ്റിക്സ് ഉപയോഗിച്ച്

## മുൻകൂട്ടി ആവശ്യങ്ങൾ

- സെഷനുകൾ 1–3 പൂർത്തിയായി
- `chainlit` ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ട് (Module08-ന്റെ `requirements.txt`-ൽ ഇതിനകം)
- WebGPU-സാധ്യമായ ബ്രൗസർ (Windows 11-ൽ Edge / Chrome ഏറ്റവും പുതിയത്)
- Foundry Local ഓണായി (`foundry service status`)

### ക്രോസ്-പ്ലാറ്റ്ഫോം കുറിപ്പുകൾ

Windows പ്രധാന ലക്ഷ്യ പരിസ്ഥിതിയാണ്. macOS ഡെവലപ്പർമാർക്ക് നേറ്റീവ് ബൈനറികൾ കാത്തിരിക്കുമ്പോൾ:  
1. Windows 11 VM (Parallels / UTM) അല്ലെങ്കിൽ റിമോട്ട് Windows വർക്ക്‌സ്റ്റേഷൻ ഉപയോഗിച്ച് Foundry Local ഓടിക്കുക.  
2. സർവീസ് (ഡിഫോൾട്ട് പോർട്ട് 5273) എക്സ്പോസ് ചെയ്ത് macOS-ൽ സജ്ജമാക്കുക:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
3. മുൻ സെഷനുകളിലെ പോലെ Python വെർച്വൽ എൻവയോൺമെന്റ് ഘട്ടങ്ങൾ ഉപയോഗിക്കുക.

Chainlit ഇൻസ്റ്റാൾ (രണ്ടു പ്ലാറ്റ്ഫോമുകൾക്കും):  
```bash
pip install chainlit
```
  
## ഡെമോ ഫ്ലോ (30 മിനിറ്റ്)

### 1. Phi (SLM) vs GPT-OSS-20B (LLM) താരതമ്യം (6 മിനിറ്റ്)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# വേഗത്തിലുള്ള കഴിവ് പരിശോധനകൾ (ഒന്ന്-ഷോട്ട്, അന്യസംവേദനരഹിതം)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# അടിസ്ഥാന ടോക്കൺ / വൈകിയ പരിശോധന (അനുഭവത്തിനായി കുറച്ച് തവണ ആവർത്തിക്കുക)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```
  
പ്രതികരണ ആഴം, വാസ്തവസമ്മതത്വം, ശൈലീ സമൃദ്ധി, ലാറ്റൻസി ട്രാക്ക് ചെയ്യുക.

GPU സജീവമാക്കിയതിനു ശേഷം ത്രൂപുട്ട് മാറ്റങ്ങൾ നിരീക്ഷിക്കുക, CPU മാത്രം ഉപയോഗിച്ചപ്പോൾ താരതമ്യം ചെയ്യുക.

### 3. ബ്രൗസറിൽ WebGPU ഇൻഫറൻസ് (6 മിനിറ്റ്)

സ്റ്റാർട്ടർ `04-webgpu-inference` അഡാപ്റ്റ് ചെയ്യുക (`samples/04-cutting-edge/webgpu_demo.html` സൃഷ്ടിക്കുക):

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
  
ഫയൽ ബ്രൗസറിൽ തുറക്കുക; കുറഞ്ഞ ലാറ്റൻസി പ്രാദേശിക റൗണ്ട്‌ട്രിപ്പ് കാണുക.

### 4. Chainlit RAG ചാറ്റ് ആപ്പ് (7 മിനിറ്റ്)

കുറഞ്ഞത് `samples/04-cutting-edge/chainlit_app.py`:

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
    # ലളിതമായ ലെക്സിക്കൽ സ്കോറിംഗ്
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
  
ഓടിക്കുക:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```
  
### 5. സ്റ്റാർട്ടർ പ്രോജക്ട്: `04-webgpu-inference` അഡാപ്റ്റ് ചെയ്യുക (6 മിനിറ്റ്)

ഡെലിവറബിളുകൾ:  
- പ്ലേസ്‌ഹോൾഡർ ഫെച്ച് ലജിക് സ്റ്റ്രീമിംഗ് ടോക്കൺസുമായി മാറ്റുക (`stream=True` എൻഡ്‌പോയിന്റ് വേർഷൻ ഉപയോഗിക്കുക, സജീവമാക്കിയ ശേഷം)  
- phi vs gpt-oss-20b ടോഗിൾസിനായി ക്ലയന്റ്-സൈഡ് ലാറ്റൻസി ചാർട്ട് ചേർക്കുക  
- RAG കോൺടെക്സ്റ്റ് ഇൻലൈൻ (റഫറൻസ് ഡോക്യുമെന്റുകൾക്കായി ടെക്സ്റ്റ് ഏരിയ) എംബെഡ് ചെയ്യുക

## വിലയിരുത്തൽ ഹ്യൂറിസ്റ്റിക്സ്

| വിഭാഗം | Phi-4-mini | GPT-OSS-20B | നിരീക്ഷണം |
|----------|------------|-------------|-------------|
| ലാറ്റൻസി (തണുത്തത്) | വേഗം | മന്ദം | SLM വേഗത്തിൽ ചൂടാകുന്നു |
| മെമ്മറി | കുറവ് | ഉയരം | ഉപകരണം സാധുത |
| കോൺടെക്സ്റ്റ് അനുസരണം | നല്ലത് | ശക്തം | വലിയ മോഡൽ കൂടുതൽ വിശദീകരണപരമായിരിക്കാം |
| ചെലവ് (പ്രാദേശികം) | കുറഞ്ഞത് | കൂടുതലാണ് (സ്രോതസ്സ്) | ഊർജ്ജം/സമയം തുല്യങ്ങൾ |
| മികച്ച ഉപയോഗം | എഡ്ജ് ആപ്പുകൾ | ആഴത്തിലുള്ള ചിന്തനം | ഹൈബ്രിഡ് പൈപ്പ്‌ലൈൻ സാധ്യമാണ് |

## പരിസ്ഥിതി സ്ഥിരീകരണം

```powershell
# ലിസ്റ്റ് കാറ്റലോഗ് (running ഫ്ലാഗ് ഇല്ല; ലോഡ് ചെയ്ത മോഡലുകൾ നിങ്ങൾ മുമ്പ് പ്രവർത്തിപ്പിച്ചവയാണ്)
foundry model list

# റൺടൈം മെട്രിക്‌സിനായി Python ബെഞ്ച്മാർക്ക് സ്ക്രിപ്റ്റ് (സെഷൻ 3)യും OS ടൂളുകളും (ടാസ്‌ക് മാനേജർ / nvidia-smi) 'model stats' എന്നതിനുപകരം ഉപയോഗിക്കുക
# ഉദാഹരണം:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```
  
## പ്രശ്നപരിഹാരം

| ലക്ഷണം | കാരണം | നടപടി |
|---------|-------|--------|
| വെബ് പേജ് ഫെച്ച് പരാജയം | CORS അല്ലെങ്കിൽ സർവീസ് ഡൗൺ | എൻഡ്‌പോയിന്റ് പരിശോധിക്കാൻ `curl` ഉപയോഗിക്കുക; ആവശ്യമെങ്കിൽ CORS പ്രോക്സി സജീവമാക്കുക |
| Chainlit ശൂന്യം | പരിസ്ഥിതി സജീവമല്ല | വെർച്വൽ എൻവയോൺമെന്റ് സജീവമാക്കി ഡിപ്പെൻഡൻസികൾ വീണ്ടും ഇൻസ്റ്റാൾ ചെയ്യുക |
| ഉയർന്ന ലാറ്റൻസി | മോഡൽ ഇപ്പോൾ ലോഡ് ചെയ്തിരിക്കുന്നു | ചെറിയ പ്രോംപ്റ്റ് സീക്വൻസുമായി ചൂടാക്കുക |

## റഫറൻസുകൾ

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Chainlit ഡോക്യുമെന്റേഷൻ: https://docs.chainlit.io  
- RAG വിലയിരുത്തൽ (Ragas): https://docs.ragas.io

---

**സെഷൻ ദൈർഘ്യം**: 30 മിനിറ്റ്  
**പ്രയാസം**: ഉയർന്ന

## സാമ്പിൾ സീനാരിയോ & വർക്ക്‌ഷോപ്പ് മാപ്പിംഗ്

| വർക്ക്‌ഷോപ്പ് ആർട്ടിഫാക്ടുകൾ | സീനാരിയോ | ലക്ഷ്യം | ഡാറ്റ / പ്രോംപ്റ്റ് ഉറവിടം |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | എക്സിക്യൂട്ടീവ് സംഗ്രഹ ജനറേറ്ററിനായി SLM vs LLM വിലയിരുത്തുന്ന ആർക്കിടെക്ചർ ടീം | ലാറ്റൻസി + ടോക്കൺ ഉപയോഗം അളക്കുക | ഒറ്റ `COMPARE_PROMPT` എൻവയോൺമെന്റ് വേരിയബിൾ |
| `chainlit_app.py` (RAG ഡെമോ) | ആന്തരിക നോളജ് അസിസ്റ്റന്റ് പ്രോട്ടോടൈപ്പ് | കുറഞ്ഞ ലെക്സിക്കൽ റിട്രീവലോടെ ചുരുക്കം ഉത്തരങ്ങൾ ഉറപ്പാക്കുക | ഫയലിൽ ഇൻലൈൻ `DOCS` ലിസ്റ്റ് |
| `webgpu_demo.html` | ഭാവി ഓൺ-ഡിവൈസ് ബ്രൗസർ ഇൻഫറൻസ് പ്രിവ്യൂ | കുറഞ്ഞ ലാറ്റൻസി പ്രാദേശിക റൗണ്ട്‌ട്രിപ്പ് + UX നറേറ്റീവ് കാണിക്കുക | ലൈവ് യൂസർ പ്രോംപ്റ്റ് മാത്രം |

### സീനാരിയോ നറേറ്റീവ്  
ഉൽപ്പന്ന സംഘടനയ്ക്ക് എക്സിക്യൂട്ടീവ് ബ്രിഫിംഗ് ജനറേറ്റർ വേണം. ഒരു ലഘു SLM (phi-4-mini) സംഗ്രഹങ്ങൾ തയ്യാറാക്കുന്നു; വലിയ LLM (gpt-oss-20b) ഉയർന്ന പ്രാധാന്യമുള്ള റിപ്പോർട്ടുകൾ മാത്രം മെച്ചപ്പെടുത്തും. സെഷൻ സ്ക്രിപ്റ്റുകൾ ഹൈബ്രിഡ് ഡിസൈൻ ന്യായീകരിക്കാൻ പ്രായോഗിക ലാറ്റൻസി & ടോക്കൺ മെട്രിക്‌സ് പിടിക്കുന്നു, Chainlit ഡെമോ ചെറിയ മോഡൽ ഉത്തരങ്ങൾ വാസ്തവസമ്മതമാക്കാൻ ഗ്രൗണ്ടഡ് റിട്രീവൽ എങ്ങനെ സഹായിക്കുന്നുവെന്ന് കാണിക്കുന്നു. WebGPU ആശയ പേജ് ബ്രൗസർ ആക്സിലറേഷൻ മെച്ചപ്പെട്ടപ്പോൾ പൂർണ്ണ ക്ലയന്റ്-സൈഡ് പ്രോസസ്സിംഗിന് ദിശ കാണിക്കുന്നു.

### കുറഞ്ഞ RAG കോൺടെക്സ്റ്റ് (Chainlit)  
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```
  
### ഹൈബ്രിഡ് ഡ്രാഫ്റ്റ്→റിഫൈൻ ഫ്ലോ (സ്യൂഡോ)  
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # ഹ്യൂറിസ്റ്റിക്: ദൈർഘ്യമേറിയ ബ്രീഫുകൾക്കോ ഫ്ലാഗ് ചെയ്ത വിഷയങ്ങൾക്കോ മാത്രമേ ഉയർത്തുകയുള്ളൂ
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```
  
രണ്ടു ലാറ്റൻസി ഘടകങ്ങളും ട്രാക്ക് ചെയ്ത് സംയോജിത ശരാശരി ചെലവ് റിപ്പോർട്ട് ചെയ്യുക.

### ഓപ്ഷണൽ മെച്ചപ്പെടുത്തലുകൾ

| ശ്രദ്ധ | മെച്ചപ്പെടുത്തൽ | കാരണം | നടപ്പാക്കൽ സൂചന |
|-------|------------|-----|---------------------|
| താരതമ്യ മെട്രിക്‌സ് | ടോക്കൺ ഉപയോഗവും ആദ്യ ടോക്കൺ ലാറ്റൻസിയും ട്രാക്ക് ചെയ്യുക | സമഗ്ര പ്രകടന കാഴ്ച | മെച്ചപ്പെടുത്തിയ ബെഞ്ച്മാർക്ക് സ്ക്രിപ്റ്റ് (സെഷൻ 3) `BENCH_STREAM=1` ഉപയോഗിക്കുക |
| ഹൈബ്രിഡ് പൈപ്പ്‌ലൈൻ | SLM ഡ്രാഫ്റ്റ് → LLM റിഫൈൻ | ലാറ്റൻസി & ചെലവ് കുറയ്ക്കുക | phi-4-mini ഉപയോഗിച്ച് ജനറേറ്റ് ചെയ്ത് gpt-oss-20b-യോടെ സംഗ്രഹം മെച്ചപ്പെടുത്തുക |
| സ്റ്റ്രീമിംഗ് UI | Chainlit-ൽ മെച്ചപ്പെട്ട UX | ക്രമാതീത ഫീഡ്ബാക്ക് | പ്രാദേശിക സ്റ്റ്രീമിംഗ് സജീവമാക്കിയ ശേഷം `stream=True` ഉപയോഗിക്കുക; കഷണങ്ങൾ കൂട്ടിച്ചേർക്കുക |
| WebGPU കാഷിംഗ് | വേഗത്തിലുള്ള JS ഇൻഷിയലൈസ് | പുനഃസംയോജനം ചെലവ് കുറയ്ക്കുക | കംപൈൽ ചെയ്ത ഷേഡർ ആർട്ടിഫാക്ടുകൾ കാഷ് ചെയ്യുക (ഭാവി റൺടൈം കഴിവ്) |
| നിർണ്ണായക QA സെറ്റ് | നീതിപൂർവ്വം മോഡൽ താരതമ്യം | വ്യത്യാസം നീക്കംചെയ്യുക | സ്ഥിരമായ പ്രോംപ്റ്റ് ലിസ്റ്റും `temperature=0` മൂല്യവും ഉപയോഗിച്ച് വിലയിരുത്തൽ നടത്തുക |
| ഔട്ട്പുട്ട് സ്കോറിംഗ് | ഘടനാപരമായ ഗുണനിലവാര ലെൻസ് | അനുഭവകഥകൾക്കപ്പുറം പോകുക | ലളിതമായ റൂബ്രിക്: സുസംബന്ധം / വാസ്തവസമ്മതത്വം / സംക്ഷിപ്തത (1–5) |
| ഊർജ്ജം / സ്രോതസ്സ് കുറിപ്പുകൾ | ക്ലാസ്‌റൂം ചർച്ച | തുല്യങ്ങൾ കാണിക്കുക | OS മോണിറ്ററുകൾ (ടാസ്‌ക് മാനേജർ, `nvidia-smi`) + ബെഞ്ച്മാർക്ക് സ്ക്രിപ്റ്റ് ഔട്ട്പുട്ടുകൾ ഉപയോഗിക്കുക |
| ചെലവ് അനുകരണം | പ്രീ-ക്ലൗഡ് ന്യായീകരണം | സ്കെയിലിംഗ് പദ്ധതി | ടോക്കണുകൾ ഹിപോതറ്റിക്കൽ ക്ലൗഡ് വിലയുമായി മാപ്പ് ചെയ്ത് TCO നറേറ്റീവ് തയ്യാറാക്കുക |
| ലാറ്റൻസി വിഭജനം | ബോട്ടിൽനെക്കുകൾ തിരിച്ചറിയുക | ലക്ഷ്യമിട്ട മെച്ചപ്പെടുത്തലുകൾ | പ്രോംപ്റ്റ് തയ്യാറാക്കൽ, അഭ്യർത്ഥന അയയ്ക്കൽ, ആദ്യ ടോക്കൺ, പൂർണ്ണ പൂർത്തീകരണം അളക്കുക |
| RAG + LLM ഫാൾബാക്ക് | ഗുണനിലവാര സുരക്ഷാ നെറ്റ് | ബുദ്ധിമുട്ടുള്ള ചോദ്യങ്ങൾ മെച്ചപ്പെടുത്തുക | SLM ഉത്തരം നീളം < പരിധി അല്ലെങ്കിൽ കുറഞ്ഞ ആത്മവിശ്വാസം → ഉയർത്തുക |

#### ഉദാഹരണ ഹൈബ്രിഡ് ഡ്രാഫ്റ്റ്/റിഫൈൻ പാറ്റേൺ

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```
  
#### ലാറ്റൻസി വിഭജനം സ്കെച്ച്

```python
import time
t0 = time.time(); # സന്ദേശങ്ങൾ നിർമ്മിക്കുക
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```
  
നീതിപൂർവ്വം താരതമ്യത്തിനായി മോഡലുകൾക്കിടയിൽ സ്ഥിരമായ അളവുകൾ ഉപയോഗിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാപത്രം**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->