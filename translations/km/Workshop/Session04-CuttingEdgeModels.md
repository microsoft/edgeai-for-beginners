# សេសชั่นទី ៤៖ ស្វែងយល់ពីគំរូបច្ចេកវិទ្យាចុងក្រោយ – LLMs, SLMs និងការបកស្រាយលើឧបករណ៍ផ្ទាល់ខ្លួន

## សេចក្ដីសង្ខេប

ប្រៀបធៀបគំរូភាសាធំៗ (LLMs) និងគំរូភាសាតូចៗ (SLMs) សម្រាប់ស្ថានភាពបកស្រាយក្នុងតំបន់ និងក្នុងពពក។ เรียนรู้រចនាបទការដាក់ចេញដោយប្រើ ONNX Runtime អូសកម្តៅ, ការប្រតិបត្ដិ WebGPU និងបទពិសោធន៍ RAG ពហុរបៀប។ រួមមានការបង្ហាញ Chainlit RAG ជាមួយគំរូក្នុងតំបន់ និងការស្វែងយល់ OpenWebUI ជាជម្រើស។ អ្នកនឹងប្ដូររចនាបទ WebGPU inference ដំបូង និងវាយតម្លៃសមត្ថភាព Phi ទល់នឹង GPT-OSS-20B និងការជួញដូរសមត្ថភាព/ថ្លៃខ្លួន។

## គោលបំណងការរៀន

- **ប្រៀបធៀប** SLM ទល់នឹង LLM លើកម្រិតការពន្យាការពេល, ជំនាញចងចាំ, គុណភាព
- **ដាក់ចេញ** គំរូជាមួយ ONNXRuntime និង (នៅកន្លែងគាំទ្រ) WebGPU
- **រត់** ការបកស្រាយក្នុងកម្មវិធីរកមើល (បង្ហាញអន្តរកម្មថែរក្សាការសម្ងាត់)
- **បញ្ចូល** ផ្លូវការពារ Chainlit RAG ជាមួយ backend SLM ក្នុងតំបន់
- **វាយតម្លៃ** ប្រើគន្លងគុណភាព + ថ្លៃខ្លួនស្រាល

## លក្ខខណ្ឌមុន

- សេសชั่น ១–៣ បានបញ្ចប់
- `chainlit` ត្រូវបានដំឡើងហើយ (បានបញ្ចូលរួចក្នុង `requirements.txt` សម្រាប់ Module08)
- កម្មវិធីរកមើលដែលគាំទ្រ WebGPU (Edge / Chrome ថ្មីៗលើ Windows 11)
- Foundry Local កំពុងដំណើរការ (`foundry service status`)

### សម្ដីតាមវេទិកាចម្រុះ

Windows ជាទីតាំងបណ្ដាញសំខាន់។ សម្រាប់អ្នកអភិវឌ្ឍ macOS ដែលរង់ចាំឯកតាតែមួយ៖  
១. រត់ Foundry Local ក្នុង VM Windows 11 (Parallels / UTM) ឬក៏ការិយាល័យបម្រើ Windows ផ្លូវច_remote។  
២. បើកសេវាកម្ម (ព្រមានសំណុំបែបបទ 5273) ហើយកំណត់នៅ macOS៖  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  
៣. ប្រើជំហាន virtual environment Python ដូចសេសชั่นមុនៗ។

ការដំឡើង Chainlit (ទាំងពីរវេទិកា):  
```bash
pip install chainlit
```
  
## ចរន្តដំណើរការ (៣០ នាទី)

### ១. ប្រៀបធៀប Phi (SLM) ទល់នឹង GPT-OSS-20B (LLM) (៦ នាទី)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# ការសាកល្បងសមត្ថភាពយ៉ាងរហ័ស (មួយដងមិនអន្តរកម្ម)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# ការធ្វើតេស្តលេខសម្គាល់មូលដ្ឋាន / ពេលយឺត (ធ្វើម្ដងឡើងវិញបន្តិចសម្រាប់យល់ដឹង)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```
  
តាមដាន: ជម្រៅចម្លើយ, ត្រឹមត្រូវតាមពិត, រស់រវើករចនាសម្ព័ន្ធ, ការពន្យាការពេល។

សង្កេតការផ្លាស់ប្តូរចំនួនដំណើរការបន្ទាប់ពីបើក GPU ទល់នឹង CPU តែម្ដង។

### ៣. ការបកស្រាយ WebGPU ក្នុងកម្មវិធីរកមើល (៦ នាទី)

ប្ដូររចនាបទចាប់ផ្តើម `04-webgpu-inference` (បង្កើត `samples/04-cutting-edge/webgpu_demo.html`):

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
  
បើកឯកសារនៅក្នុងកម្មវិធីរកមើល; សង្កេតការត្រឡប់ក្នុងតំបន់ដែលមានការពន្យាការពេលទាប។

### ៤. កម្មវិធី Chainlit RAG Chat (៧ នាទី)

`samples/04-cutting-edge/chainlit_app.py` តូចបំផុត៖

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
    # ពិន្ទុលេខាឡិចស៊ីកលាយអំណត់
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
  
រត់៖

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```
  
### ៥. គម្រោងចាប់ផ្តើម៖ ប្ដូរ `04-webgpu-inference` (៦ នាទី)

ឯកសារដែលត្រូវផ្ញើ៖  
- ជំនួសឡូជ៊ីកទាញយក placeholder ជាមួយឈុតបន្ទាត់បញ្ចូន (ប្រើវត្ថុបែប `stream=True` នៅពេលបានបើក)  
- បន្ថែមតារាងកំណត់ពន្យាការពេល (នៅភាគីអតិថិជន) សម្រាប់ស្លាក phi និង gpt-oss-20b  
- បញ្ចូលនូវបរិបទ RAG ក្នុងបន្ទាត់ (ប្រអប់អត្ថបទសម្រាប់ឯកសារយោង)

## គន្លងវាយតម្លៃ

| ប្រភេទ | Phi-4-mini | GPT-OSS-20B | ការសង្កេត |
|----------|------------|-------------|-------------|
| ការពន្យាការពេល (ត្រជាក់) | លឿន | យឺតជាង | SLM កំដរយ៉ាងឆាប់រហ័ស |
| ជំនាញចងចាំ | ទាប | ខ្ពស់ | អាចប្រើបានលើឧបករណ៍ |
| ការអនុលោមបរិបទ | ល្អ | ខ្លាំង | គំរូធំអាចមានច្រើនពាក្យជាង |
| ថ្លៃ (ក្នុងតំបន់) | តិច | ខ្ពស់ (ធនធាន) | ជួញដូរថាមពល/ពេលវេលា |
| ករណីប្រើប្រាស់ល្អបំផុត | កម្មវិធីមេដាយកណ្ដាលដែន | ការវិភាគជ្រាលជ្រៅ | អាចមានផ្លូវការពារក្នុងរូប |

## បរិយាកាសផ្ទៀងផ្ទាត់

```powershell
# បញ្ជីកាតាឡុក (គ្មានស្លាក --running; ម៉ូឌែលដែលបានផ្ទុកគឺជាម៉ូឌែលដែលអ្នកបានប្រត(est)មុន)
foundry model list

# សម្រាប់មេត្រីក៍រយៈពេលរត់ ប្រើស្គ្រីប Python benchmark (សម័យ 3) និងឧបករណ៍ប្រព័ន្ធប្រតិបត្តិការ (Task Manager / nvidia-smi) ជំនួស 'ស្ថិតិម៉ូឌែល'
# ឧទាហរណ៍:
#   cd Workshop/samples
#   កំណត់ BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```
  
## ការដោះស្រាយបញ្ហា

| រោគសញ្ញា | ហេតុផល | ដំណើរការ |
|---------|-------|--------|
| មិនអាចទាញយកគេហទំព័រ | CORS ឬសេវាកម្មបិទ | ប្រើ `curl` ដើម្បីផ្ទៀងផ្ទាត់ endpoint; បើក proxy CORS ប្រសិនបើចាំបាច់ |
| Chainlit បង្ហាញទទេ | បរិយាកាសមិនដំណើរការ | ស្វែងរក venv & ដំឡើងចំណុចសំខាន់ម្តងទៀត |
| ការពន្យាការពេលខ្ពស់ | គំរូទើបតែផ្ទុកចូល | កំដរជាមួយសំណួរតូចៗជាប់ៗគ្នា |

## ឯកសារយោង

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Chainlit Docs: https://docs.chainlit.io  
- RAG Evaluation (Ragas): https://docs.ragas.io  

---

**រយៈពេលសេសชั่น**៖ ៣០ នាទី  
**កម្រិតតឹងរ៉ឹង**៖ ជំនាញខ្ពស់

## ស្ថានភាពគំរូ និងផែនការកម្មវិធីបណ្តុះបណ្តាល

| សម្ភារៈកិច្ចវគ្គ | ស្ថានភាព | គោលបំណង | ទិន្នន័យ / ប្រភពពាក្យ |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | ក្រុមស្ថាបត្យកម្មវាយតម្លៃ SLM ទល់ LLM សម្រាប់ម៉ាស៊ីនបញ្ចូលសង្ខេបសេចក្ដីប្រតិបត្តិការ | គណនាការពន្យាការពេល + ការប្រើប្រាស់ token | បរិយាកាសបរិច្ឆេទតែមួយ `COMPARE_PROMPT` env var |
| `chainlit_app.py` (បង្ហាញ RAG) | ព្រឹត្តិការណ៍ជំនួយចំណេះដឹងក្នុងស្ថានភាព | ផ្ដល់ចម្លើយខ្លីជាមួយការទាញយកពាក្យតិច | បញ្ជី `DOCS` នៅក្នុងឯកសារ |
| `webgpu_demo.html` | មើលមុខការបកស្រាយលើកម្មវិធីរកមើលក្នុងឧបករណ៍នាពេលអនាគត | បង្ហាញការត្រឡប់ក្នុងតំបន់មូលដ្ឋានដែលពន្យាការពេលទាប + រឿងនិទានប្រើប្រាស់ | សំណួរប្រើប្រាស់ផ្ទាល់តែប៉ុណ្ណោះ |

### រឿងនិទានស្ថានភាព  
អង្គការផលិតផលចង់មានម៉ាស៊ីនបញ្ចូលសេចក្ដីប្រាប់ផ្ទាល់ជាសង្ខេប។ SLM ទម្ងន់ស្រាល (phi‑4‑mini) សរសេរសង្ខេបដើម; LLM ធំជាង (gpt‑oss‑20b) ប្រហែលតែធ្វើការកំណត់ឡើងវិញសម្រាប់របាយការណ៍អាទិភាពខ្ពស់។ ស្គ្រីបសេស្សិនកត់ត្រា latency និងមាត្រដ្ឋាន token ដើម្បីបញ្ចាក់រចនាបទម៉ាស៊ីនចំរូង ខណៈដែលបង្ហាញ Chainlit បង្ហាញរបៀបទាញយកជំនួយឲ្យចម្លើយគំរូតូចមានត្រឹមត្រូវតាមពិត។ ទំព័រការសិក្សា WebGPU ផ្ដល់ពិធីការដំណើរការលើភាគីអតិថិជនពេញលេញនៅពេលបង្កើនកម្រិត acceleration កម្មវិធីរកមើល។

### បរិបទ RAG តូចបំផុត (Chainlit)  
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```
  
### បូក/កែប្រែរចនាបទចំរូង (របៀបបង្ហាញ)  
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: ប៉ាន់ស្មានលើកម្ដងសម្រាប់សង្ខេបវែងឬប្រធានបទដែលបានសម្គាល់
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```
  
តាមដានធាតុ latency ទាំងពីរដើម្បីរាយការណ៍ថ្លៃឈ្នួលមធ្យមចំរូង។

### ការកែប្រែជាជម្រើស

| ផ្នែកផ្តោត | ការកែលម្អ | ហេតុផល | សារាណៈអនុវត្ត |
|-------|------------|-----|---------------------|
| មាត្រដ្ឋានប្រៀបធៀប | តាមដានការប្រើប្រាស់ token + ការពន្យាការពេលtokenដំបូង | ចម្រាញ់ទិដ្ឋភាពសមត្ថភាពទូលំទូលាយ | ប្រើស្គ្រីបគំនូសសន្សំប្រសើរឡើង (Sesion 3) ជាមួយ `BENCH_STREAM=1` |
| ផ្លូវការពារ Hybrid | SLM ត្រាប់ → LLM កែប្រែ | បន្ថយភាពឆ្ងាយ & ថ្លៃខ្លួន | បង្កើតជាមួយ phi-4-mini, កែបញ្ចប់ដោយ gpt-oss-20b |
| UI បញ្ចូនបន្ត | UX ល្អជាងនៅ Chainlit | តម្រង់តបជាបន្ត | ប្រើ `stream=True` នៅពេលបើកវាសូត្រនៅក្នុងតំបន់; រួមបញ្ចូលដុំទិន្នន័យ |
| ការផ្ទុក WebGPU | ចាប់ផ្តើម JS លឿន | បន្ថយរត់ compile ឡើងវិញ | ពិនិត្យដុំ shader ដែលបាន compile រួច (សមត្ថភាព runtime អនាគត) |
| ផ្ដល់QA ដោយការកំណត់លក្ខណៈ | ប្រៀបធៀបគំរូយ៉ាងស្មើ | បំបាត់ភាពបម្លែង | បញ្ជីពាក្យថ្លៃជាក់លាក់ + `temperature=0` សម្រាប់ការប្រតិបត្តិវាយតម្លៃ |
| ពិន្ទុផលិតផល | កែទស្សនវិស័យគុណភាព | មិនប៉ះពាល់ជា anecdotes | កំណត់មូលដ្ឋានភាគតិច: ភាពសម្របសម្រួល / ត្រឹមត្រូវតាមពិត / តិចតួច (1–5) |
| សញ្ញាថាមពល / ធនធាន | ពិភាក្សាក្រុមថ្នាក់ | បង្ហាញការជួញដូរ | ប្រើម៉ូនីទ័រ OS (Task Manager, `nvidia-smi`) + លទ្ធផលស្គ្រីបវាយតម្លៃ |
| បំលែងថ្លៃ | ចំណាំសកម្មភាពមុនពពក | ផែនការពង្រីក | ផ្គូផ្គង token ទៅតំលៃពពកស្មാനുംសម្រាប់រឿង TCO |
| បំបែកកំណត់ពេល | ស្វែងរកបញ្ហា | គោលដៅកែប្រែ | វាស់កំហែង prompt prep, សំណើ, token ដំបូង, បញ្ចប់ពេញ |
| RAG + LLM បម្លែងក្រោយ | បណ្តាញសុវត្ថិភាពគុណភាព | បង្កើនសំណួរលំបាក | ប្រសិនបើចម្លើយ SLM តូចជាងកម្រិត ឬ ទាបទំនុកចិត្ត → លើកកម្ពស់ |

#### ឧទាហរណ៍រចនាបទ Hybrid Draft/Refine

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```
  
#### សំណុំបំបែកការពន្យាការពេល

```python
import time
t0 = time.time(); # បង្កើតសារ
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```
  
ប្រើសម្ព័ន្ធវាស់វែងដូចគ្នាលើគំរូទាំងអស់សម្រាប់ការប្រៀបធៀបយ៉ាងសមប្រក្រតី។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ បើទោះយើងខំប្រឹងប្រែងព្យាយាមឱ្យបានត្រឹមត្រូវ ក៏សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមាតុភាគគួរត្រូវបានមើលឱ្យជាអ្នកផ្តល់ព័ត៌មានដើមដែលមានភាពសុចរិត។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនានា ឬការប្រែប្រួលអ្វីៗកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->