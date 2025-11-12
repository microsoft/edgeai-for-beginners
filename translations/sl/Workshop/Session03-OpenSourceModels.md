<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-12T00:39:57+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "sl"
}
-->
# Seja 3: Modeli odprte kode v Foundry Local

## Povzetek

Odkrijte, kako vključiti modele Hugging Face in druge modele odprte kode v Foundry Local. Naučite se strategij izbire, delovnih procesov prispevkov skupnosti, metodologije primerjave zmogljivosti ter kako razširiti Foundry z registracijami prilagojenih modelov. Ta seja se povezuje s tedenskimi temami raziskovanja "Model Mondays" in vas opremi za ocenjevanje ter operativno uporabo modelov odprte kode lokalno, preden jih razširite na Azure.

## Cilji učenja

Do konca boste sposobni:

- **Odkriti in oceniti**: Identificirati kandidate za modele (mistral, gemma, qwen, deepseek) z upoštevanjem kompromisov med kakovostjo in porabo virov.
- **Naložiti in zagnati**: Uporabiti Foundry Local CLI za prenos, predpomnjenje in zagon modelov skupnosti.
- **Primerjati**: Uporabiti dosledne heuristike za zakasnitev + prepustnost tokenov + kakovost.
- **Razširiti**: Registrirati ali prilagoditi ovitek za model po vzorcih, združljivih z SDK.
- **Primerjati**: Ustvariti strukturirane primerjave za odločitve med SLM in srednje velikimi LLM.

## Predpogoji

- Zaključeni seji 1 in 2
- Python okolje z nameščenim `foundry-local-sdk`
- Vsaj 15 GB prostega diska za več predpomnjenih modelov

### Hiter začetek okolja na več platformah

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Pri primerjanju zmogljivosti z macOS proti storitvi gostitelja Windows nastavite:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Potek demonstracije (30 min)

### 1. Nalaganje modelov Hugging Face prek CLI (8 min)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Zagon in hitra preiskava (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Skripta za primerjavo zmogljivosti (8 min)

Ustvarite `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Zaženite:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Primerjava zmogljivosti (5 min)

Razpravljajte o kompromisih: čas nalaganja, poraba pomnilnika (opazujte Task Manager / `nvidia-smi` / monitor virov OS), kakovost izhoda v primerjavi s hitrostjo. Uporabite Python skripto za primerjavo zmogljivosti (Seja 3) za zakasnitev in prepustnost; ponovite po omogočitvi pospeševanja GPU.

### 5. Začetni projekt (4 min)

Ustvarite generator poročil o primerjavi modelov (razširite skripto za primerjavo zmogljivosti z izvozom v markdown).

## Začetni projekt: Razširite `03-huggingface-models`

Izboljšajte obstoječi vzorec z:

1. Dodajanjem združevanja primerjav + izvozom v CSV/Markdown.
2. Implementacijo preprostega kvalitativnega ocenjevanja (nabor parov pozivov + datoteka za ročno označevanje).
3. Uvedbo JSON konfiguracije (`models.json`) za prilagodljiv seznam modelov in nabor pozivov.

## Preveritveni seznam za validacijo

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Vsi ciljni modeli naj se pojavijo in odgovorijo na zahtevo za klepet.

## Primer scenarija in povezava z delavnico

| Skripta delavnice | Scenarij | Cilj | Vir poziva / nabora podatkov |
|-------------------|----------|------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Ekipa platforme Edge izbira privzeti SLM za vgrajeni povzetek | Ustvarite primerjavo zakasnitve + p95 + tokenov/sekundo med kandidati za modele | Vgrajena spremenljivka `PROMPT` + seznam okolja `BENCH_MODELS` |

### Narativ scenarija

Ekipa za razvoj izdelkov mora izbrati privzeti lahek model za povzemanje za funkcijo offline zapisovanja opomb s sestankov. Izvedejo nadzorovane deterministične primerjave (temperature=0) na fiksnem naboru pozivov (glejte primer spodaj) in zbirajo metrike zakasnitve + prepustnosti z in brez pospeševanja GPU.

### Primer razširljivega nabora pozivov JSON

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Zagnajte vsak poziv za vsak model, zajemite zakasnitev na poziv za izpeljavo distribucijskih metrik in zaznavanje odstopanj.

## Okvir za izbiro modela

| Dimenzija | Metrika | Zakaj je pomembna |
|-----------|---------|-------------------|
| Zakasnitev | povprečje / p95 | Doslednost uporabniške izkušnje |
| Prepustnost | tokeni/sekundo | Skalabilnost serij in pretakanja |
| Pomnilnik | velikost rezidenta | Prilagoditev napravi in sočasnost |
| Kakovost | pozivni kriteriji | Primernost za nalogo |
| Odtis | predpomnilnik diska | Distribucija in posodobitve |
| Licenca | dovoljenje za uporabo | Skladnost s komercialnimi pravili |

## Razširitev s prilagojenim modelom

Vzorec na visoki ravni (psevdokoda):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Posvetujte se z uradnim repozitorijem za razvijajoče se vmesnike adapterjev:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Odpravljanje težav

| Težava | Vzrok | Rešitev |
|--------|-------|---------|
| OOM na mistral-7b | Premalo RAM/GPU | Ustavite druge modele; poskusite manjšo različico |
| Počasni prvi odziv | Hladno nalaganje | Ohranite aktivnost z občasnim lahkim pozivom |
| Zastoji pri prenosu | Nestabilnost omrežja | Poskusite znova; predpomnite med manj obremenjenimi urami |

## Reference

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Odkritje modelov Hugging Face: https://huggingface.co/models

---

**Trajanje seje**: 30 min (+ opcijski poglobljeni pregled)  
**Težavnost**: Srednja

### Opcijske izboljšave

| Izboljšava | Korist | Kako |
|------------|--------|------|
| Zakasnitev prvega tokena pri pretakanju | Meri zaznano odzivnost | Zaženite primerjavo zmogljivosti z `BENCH_STREAM=1` (izboljšana skripta v `Workshop/samples/session03`) |
| Deterministični način | Stabilne primerjave regresij | `temperature=0`, fiksni nabor pozivov, zajem JSON izhodov pod nadzorom različic |
| Ocena po kriterijih kakovosti | Dodaja kvalitativno dimenzijo | Vzdržujte `prompts.json` z pričakovanimi vidiki; ročno ali prek sekundarnega modela označite ocene (1–5) |
| Izvoz v CSV / Markdown | Deljivo poročilo | Razširite skripto za zapis `benchmark_report.md` s tabelo in poudarki |
| Oznake zmogljivosti modela | Pomaga pri avtomatiziranem usmerjanju kasneje | Vzdržujte `models.json` z `{alias: {capabilities:[], size_mb:..}}` |
| Faza ogrevanja predpomnilnika | Zmanjšanje pristranskosti hladnega zagona | Izvedite eno ogrevalno rundo pred časovno zanko (že implementirano) |
| Natančnost percentila | Robustna zakasnitev repa | Uporabite numpy percentil (že v preoblikovani skripti) |
| Približek stroškov tokenov | Ekonomska primerjava | Približen strošek = (tokeni/sekundo * povprečno število tokenov na zahtevo) * energijska ocena |
| Samodejno preskakovanje neuspelih modelov | Odpornost pri serijskih zagonih | Ovijte vsako primerjavo v try/except in označite statusno polje |

#### Minimalni izvoz v Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Primer determinističnega nabora pozivov

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Zagnajte statični seznam namesto naključnih pozivov za primerljive metrike med različicami.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->