<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-12T01:05:00+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "et"
}
-->
# Sessie 3: Avatud lähtekoodiga mudelid Foundry Localis

## Kokkuvõte

Avasta, kuidas tuua Hugging Face'i ja teisi avatud lähtekoodiga mudeleid Foundry Locali. Õpi valikustrateegiaid, kogukonna panustamise töövooge, jõudluse võrdlemise metoodikat ja seda, kuidas laiendada Foundryt kohandatud mudelite registreerimisega. See sessioon haakub iganädalaste "Model Mondays" uurimisteemadega ja annab sulle oskused avatud lähtekoodiga mudelite hindamiseks ja rakendamiseks kohapeal enne nende skaleerimist Azure'i.

## Õpieesmärgid

Sessiooni lõpuks oskad:

- **Avastada ja hinnata**: Tuvastada kandidaatmudeleid (mistral, gemma, qwen, deepseek), arvestades kvaliteedi ja ressursside kompromisse.
- **Laadida ja käivitada**: Kasutada Foundry Local CLI-d kogukonna mudelite allalaadimiseks, vahemällu salvestamiseks ja käivitamiseks.
- **Võrdlusuuringuid teha**: Rakendada järjepidevaid latentsuse, tokenite läbilaskevõime ja kvaliteedi heuristikaid.
- **Laiendada**: Registreerida või kohandada mudeli wrapperit, järgides SDK-ga ühilduvaid mustreid.
- **Võrrelda**: Luua struktureeritud võrdlusi SLM-i ja keskmise suurusega LLM-i valikute jaoks.

## Eeltingimused

- Sessioonid 1 ja 2 läbitud
- Python'i keskkond, kus on paigaldatud `foundry-local-sdk`
- Vähemalt 15GB vaba kettaruumi mitme mudeli vahemälu jaoks

### Platvormideülene keskkonna kiirkäivitus

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

Kui teed võrdlusuuringut macOS-ist Windowsi hostiteenuse vastu, seadista:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo voog (30 min)

### 1. Hugging Face'i mudelite laadimine CLI kaudu (8 min)

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

### 2. Käivitamine ja kiire testimine (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```

### 3. Võrdlusuuringu skript (8 min)

Loo `samples/03-oss-models/benchmark_models.py`:

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

Käivita:

```powershell
python samples/03-oss-models/benchmark_models.py
```

### 4. Jõudluse võrdlemine (5 min)

Arutle kompromisside üle: laadimisaeg, mälumaht (vaata Task Manager / `nvidia-smi` / OS-i ressursimonitor), väljundi kvaliteet vs kiirus. Kasuta Python'i võrdlusuuringu skripti (Sessie 3) latentsuse ja läbilaskevõime mõõtmiseks; korda protsessi pärast GPU kiirenduse lubamist.

### 5. Algusprojekt (4 min)

Loo mudelite võrdlusaruande generaator (laienda võrdlusuuringu skripti markdowni ekspordiga).

## Algusprojekt: Laienda `03-huggingface-models`

Täienda olemasolevat näidet:

1. Lisa võrdlusuuringute koondamine + CSV/Markdowni väljund.
2. Rakenda lihtne kvalitatiivne hindamine (küsimuste paaride komplekt + käsitsi märgistamise stub-fail).
3. Lisa JSON-konfiguratsioonifail (`models.json`) pistikprogrammide mudeliloendi ja küsimuste komplekti jaoks.

## Kontrollnimekiri valideerimiseks

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Kõik sihtmudelid peaksid ilmuma ja vastama testvestluse päringule.

## Näidistsenaarium ja töötoa kaardistamine

| Töötoa skript | Stsenaarium | Eesmärk | Küsimus / Andmestiku allikas |
|---------------|-------------|---------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Servaplatvormi meeskond valib vaikimisi SLM-i manustatud kokkuvõttefunktsiooni jaoks | Toota latentsuse + p95 + tokenite/sek võrdlus kandidaatmudelite vahel | Sisseehitatud `PROMPT` muutujaga + keskkonna `BENCH_MODELS` loend |

### Stsenaariumi narratiiv
Tootearenduse meeskond peab valima vaikimisi kerge kokkuvõtte mudeli võrguühenduseta koosolekumärkmete funktsiooni jaoks. Nad viivad läbi kontrollitud deterministlikud võrdlusuuringud (temperature=0) fikseeritud küsimuste komplekti alusel (vt allolevat näidet) ja koguvad latentsuse + läbilaskevõime mõõdikuid koos ja ilma GPU kiirenduseta.

### Näide küsimuste komplekti JSON-ist (laiendatav)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Korda iga küsimust iga mudeli puhul, jäädvusta iga küsimuse latentsus, et tuletada jaotusmõõdikud ja tuvastada kõrvalekalded.

## Mudeli valiku raamistik

| Mõõde | Mõõdik | Miks see oluline on |
|-------|--------|---------------------|
| Latentsus | keskmine / p95 | Kasutajakogemuse järjepidevus |
| Läbilaskevõime | tokenid/sek | Partii- ja voogedastuse skaleeritavus |
| Mälu | kasutatav maht | Seadme sobivus ja samaaegsus |
| Kvaliteet | hindamisküsimused | Ülesande sobivus |
| Jälg | kettavahemälu | Jaotamine ja uuendused |
| Litsents | kasutusõigused | Kaubanduslik vastavus |

## Kohandatud mudeli lisamine

Kõrgetasemeline muster (pseudokood):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Vaata ametlikku repo't adapteriliideste arenduste kohta:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Tõrkeotsing

| Probleem | Põhjus | Lahendus |
|----------|--------|----------|
| OOM mistral-7b puhul | Ebapiisav RAM/GPU | Peata teised mudelid; proovi väiksemat varianti |
| Aeglane esimene vastus | Külm laadimine | Hoia soojas perioodilise kerge küsimusega |
| Allalaadimine takerdub | Võrgu ebastabiilsus | Proovi uuesti; eellaadi mittekoormatud ajal |

## Viited

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face'i mudelite avastamine: https://huggingface.co/models

---

**Sessiooni kestus**: 30 min (+ valikuline süvitsiminek)  
**Raskusaste**: Keskmine

### Valikulised täiustused

| Täiustus | Kasu | Kuidas |
|----------|------|--------|
| Esimese tokeni latentsuse voogedastus | Mõõdab tajutavat reageerimiskiirust | Käivita võrdlusuuring `BENCH_STREAM=1` abil (täiustatud skript `Workshop/samples/session03` kaustas) |
| Deterministlik režiim | Stabiilsed regressioonivõrdlused | `temperature=0`, fikseeritud küsimuste komplekt, jäädvusta JSON-väljundid versioonikontrolli all |
| Kvaliteedi hindamise skoorimine | Lisab kvalitatiivse mõõtme | Halda `prompts.json` oodatavate aspektidega; märgi skoorid (1–5) käsitsi või teise mudeli abil |
| CSV / Markdowni eksport | Jagatav aruanne | Laienda skripti, et kirjutada `benchmark_report.md` tabeli ja esiletõstudega |
| Mudeli võimekuse sildid | Aitab hiljem automatiseeritud suunamist | Halda `models.json` koos `{alias: {capabilities:[], size_mb:..}}` |
| Vahemälu soojendusfaas | Vähendab külmkäivituse kallutatust | Teosta üks soojendusring enne ajastusahelat (juba rakendatud) |
| Protsentiili täpsus | Tugev sabalatentsus | Kasuta numpy protsentiili (juba refaktoreeritud skriptis) |
| Tokenite kulu hinnang | Majanduslik võrdlus | Ligikaudne kulu = (tokenid/sek * keskmine tokenite arv päringu kohta) * energia heuristika |
| Ebaõnnestunud mudelite automaatne vahelejätmine | Vastupidavus partii käitamisel | Mähi iga võrdlusuuring try/except sisse ja märgi olekuväli |

#### Minimaalne Markdowni ekspordi näidis

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Deterministliku küsimuste komplekti näide

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Kasuta staatilist loendit juhuslike küsimuste asemel, et saada võrreldavaid mõõdikuid erinevate versioonide vahel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->