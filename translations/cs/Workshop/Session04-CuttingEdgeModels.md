<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-12T00:07:35+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "cs"
}
-->
# Sezení 4: Prozkoumejte nejmodernější modely – LLM, SLM a inference na zařízení

## Abstrakt

Porovnejte velké jazykové modely (LLM) a malé jazykové modely (SLM) pro scénáře inference na místě vs v cloudu. Naučte se vzory nasazení využívající akceleraci ONNX Runtime, WebGPU a hybridní RAG zkušenosti. Součástí je ukázka Chainlit RAG s lokálním modelem a volitelným průzkumem OpenWebUI. Přizpůsobíte startovací WebGPU inference a vyhodnotíte schopnosti Phi vs GPT-OSS-20B a kompromisy mezi náklady a výkonem.

## Cíle učení

- **Porovnat** SLM vs LLM z hlediska latence, paměti a kvality
- **Nasadit** modely pomocí ONNXRuntime a (kde je podporováno) WebGPU
- **Spustit** inference v prohlížeči (interaktivní demo zachovávající soukromí)
- **Integrovat** pipeline Chainlit RAG s lokálním backendem SLM
- **Vyhodnotit** pomocí lehkých heuristik kvality a nákladů

## Předpoklady

- Dokončené sezení 1–3
- Nainstalovaný `chainlit` (již v `requirements.txt` pro Modul08)
- Prohlížeč podporující WebGPU (Edge / Chrome nejnovější na Windows 11)
- Běžící Foundry Local (`foundry service status`)

### Poznámky k multiplatformnímu použití

Windows zůstává primárním cílovým prostředím. Pro vývojáře na macOS, kteří čekají na nativní binární soubory:
1. Spusťte Foundry Local ve Windows 11 VM (Parallels / UTM) NEBO na vzdálené pracovní stanici s Windows.
2. Zpřístupněte službu (výchozí port 5273) a nastavte na macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Použijte stejné kroky pro virtuální prostředí Pythonu jako v předchozích sezeních.

Instalace Chainlit (obě platformy):
```bash
pip install chainlit
```

## Průběh ukázky (30 min)

### 1. Porovnání Phi (SLM) vs GPT-OSS-20B (LLM) (6 min)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Sledujte: hloubku odpovědí, faktickou přesnost, stylistickou bohatost, latenci.

Pozorujte změny propustnosti po aktivaci GPU oproti pouze CPU.

### 3. WebGPU inference v prohlížeči (6 min)

Přizpůsobte startovací `04-webgpu-inference` (vytvořte `samples/04-cutting-edge/webgpu_demo.html`):

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

Otevřete soubor v prohlížeči; pozorujte nízkou latenci při lokálním zpracování.

### 4. Chainlit RAG chatovací aplikace (7 min)

Minimální `samples/04-cutting-edge/chainlit_app.py`:

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
    # Naive lexical scoring
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

Spusťte:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Startovací projekt: Přizpůsobte `04-webgpu-inference` (6 min)

Výstupy:
- Nahraďte logiku pro načítání dat zástupným kódem pro streamování tokenů (použijte variantu endpointu `stream=True`, jakmile bude povolena)
- Přidejte graf latence (na straně klienta) pro přepínání mezi phi a gpt-oss-20b
- Vložte kontext RAG inline (textové pole pro referenční dokumenty)

## Heuristiky hodnocení

| Kategorie | Phi-4-mini | GPT-OSS-20B | Pozorování |
|-----------|------------|-------------|------------|
| Latence (studený start) | Rychlá | Pomalejší | SLM se rychle zahřívá |
| Paměť | Nízká | Vysoká | Možnost použití na zařízení |
| Dodržování kontextu | Dobré | Silné | Větší model může být více rozvláčný |
| Náklady (lokální) | Minimální | Vyšší (zdroje) | Kompromis energie/času |
| Nejlepší použití | Aplikace na zařízení | Hluboké uvažování | Možná hybridní pipeline |

## Validace prostředí

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Řešení problémů

| Příznak | Příčina | Akce |
|---------|---------|------|
| Selhání načítání webové stránky | CORS nebo služba nefunguje | Použijte `curl` k ověření endpointu; povolte CORS proxy, pokud je potřeba |
| Prázdný Chainlit | Prostředí není aktivní | Aktivujte venv a znovu nainstalujte závislosti |
| Vysoká latence | Model právě načten | Zahřejte malou sekvencí promptů |

## Odkazy

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentace Chainlit: https://docs.chainlit.io
- Hodnocení RAG (Ragas): https://docs.ragas.io

---

**Délka sezení**: 30 min  
**Obtížnost**: Pokročilá

## Ukázkový scénář a mapování workshopu

| Artefakty workshopu | Scénář | Cíl | Zdroj dat / promptů |
|---------------------|--------|-----|---------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Tým architektury hodnotící SLM vs LLM pro generátor výkonných souhrnů | Kvantifikace rozdílu v latenci + využití tokenů | Jedna proměnná prostředí `COMPARE_PROMPT` |
| `chainlit_app.py` (ukázka RAG) | Prototyp interního asistenta znalostí | Zakotvení krátkých odpovědí s minimálním lexikálním vyhledáváním | Inline seznam `DOCS` v souboru |
| `webgpu_demo.html` | Náhled futuristické inference v prohlížeči na zařízení | Ukázka nízké latence při lokálním zpracování + UX narativ | Pouze živý uživatelský prompt |

### Narativ scénáře
Produktová organizace chce generátor výkonných souhrnů. Lehký SLM (phi‑4‑mini) vytváří návrhy souhrnů; větší LLM (gpt‑oss‑20b) může upravovat pouze vysoce prioritní zprávy. Skripty sezení zachycují empirické metriky latence a tokenů, aby ospravedlnily hybridní design, zatímco ukázka Chainlit ilustruje, jak zakotvené vyhledávání udržuje odpovědi malého modelu faktické. Konceptová stránka WebGPU poskytuje vizi pro plně klientské zpracování, jakmile se zrychlení prohlížeče vyvine.

### Minimální kontext RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybridní tok Návrh→Úprava (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Sledujte obě složky latence, abyste mohli hlásit průměrné náklady.

### Volitelná vylepšení

| Zaměření | Vylepšení | Proč | Náznak implementace |
|----------|-----------|------|---------------------|
| Srovnávací metriky | Sledujte využití tokenů + latenci prvního tokenu | Holistický pohled na výkon | Použijte vylepšený benchmarkový skript (Sezení 3) s `BENCH_STREAM=1` |
| Hybridní pipeline | Návrh SLM → Úprava LLM | Snížení latence a nákladů | Generujte pomocí phi-4-mini, upravte souhrn pomocí gpt-oss-20b |
| Streaming UI | Lepší UX v Chainlit | Postupná zpětná vazba | Použijte `stream=True`, jakmile bude lokální streamování dostupné; akumulujte části |
| WebGPU caching | Rychlejší inicializace JS | Snížení režijních nákladů na rekompilaci | Uložte zkompilované artefakty shaderů (budoucí schopnost runtime) |
| Deterministická sada QA | Spravedlivé porovnání modelů | Odstranění variability | Pevný seznam promptů + `temperature=0` pro hodnotící běhy |
| Skórování výstupů | Strukturovaný pohled na kvalitu | Překonání anekdot | Jednoduchá metrika: koherence / faktualita / stručnost (1–5) |
| Poznámky k energii / zdrojům | Diskuse ve třídě | Ukázka kompromisů | Použijte OS monitory (Správce úloh, `nvidia-smi`) + výstupy benchmarkového skriptu |
| Simulace nákladů | Ospravedlnění před cloudem | Plánování škálování | Mapujte tokeny na hypotetické cloudové ceny pro narativ TCO |
| Rozklad latence | Identifikace úzkých míst | Cílení optimalizací | Měřte přípravu promptu, odeslání požadavku, první token, kompletní dokončení |
| RAG + LLM záloha | Bezpečnostní síť kvality | Zlepšení obtížných dotazů | Pokud délka odpovědi SLM < prahová hodnota nebo nízká důvěra → eskalace |

#### Příklad hybridního vzoru Návrh/Úprava

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Náčrt rozkladu latence

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Použijte konzistentní měřicí rámec napříč modely pro spravedlivé porovnání.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->