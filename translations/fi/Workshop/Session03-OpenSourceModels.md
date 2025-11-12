<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:28:42+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "fi"
}
-->
# Istunto 3: Avoimen lähdekoodin mallit Foundry Localissa

## Tiivistelmä

Opi tuomaan Hugging Face ja muita avoimen lähdekoodin malleja Foundry Localiin. Tutustu mallien valintastrategioihin, yhteisön osallistumisen työnkulkuihin, suorituskyvyn vertailumenetelmiin ja siihen, miten Foundryä voi laajentaa mukautetuilla mallirekisteröinneillä. Tämä istunto liittyy viikoittaisiin "Model Mondays" -tutkimusteemoihin ja antaa valmiudet arvioida ja ottaa käyttöön avoimen lähdekoodin malleja paikallisesti ennen laajentamista Azureen.

## Oppimistavoitteet

Istunnon lopussa osaat:

- **Löytää ja arvioida**: Tunnistaa ehdokasmallit (mistral, gemma, qwen, deepseek) laadun ja resurssien välisen tasapainon perusteella.
- **Ladata ja suorittaa**: Käyttää Foundry Local CLI:tä yhteisön mallien lataamiseen, välimuistiin tallentamiseen ja käynnistämiseen.
- **Suorittaa vertailuja**: Soveltaa johdonmukaisia viive-, token-läpäisy- ja laatuheuristiikkoja.
- **Laajentaa**: Rekisteröidä tai mukauttaa oma mallikääre SDK-yhteensopivien mallien mukaisesti.
- **Verrata**: Tuottaa rakenteellisia vertailuja SLM:n ja keskikokoisten LLM-mallien valintapäätösten tueksi.

## Esivaatimukset

- Istunnot 1 ja 2 suoritettu
- Python-ympäristö, jossa `foundry-local-sdk` on asennettuna
- Vähintään 15GB vapaata levytilaa useiden mallien välimuistia varten

### Nopea aloitus eri käyttöjärjestelmissä

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

Kun suoritat vertailuja macOS:sta Windows-palvelimella, aseta:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo (30 min)

### 1. Lataa Hugging Face -mallit CLI:n kautta (8 min)

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


### 2. Suorita ja tee nopea tarkistus (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Vertailuskripti (8 min)

Luo `samples/03-oss-models/benchmark_models.py`:

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

Suorita:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Vertaa suorituskykyä (5 min)

Keskustele kompromisseista: latausaika, muistin käyttö (seuraa Task Manageria / `nvidia-smi` / käyttöjärjestelmän resurssimonitoria), tulosten laatu vs. nopeus. Käytä Python-vertailuskriptiä (istunto 3) viiveen ja läpäisyn mittaamiseen; toista GPU-kiihdytyksen ollessa käytössä.

### 5. Aloitusprojekti (4 min)

Luo mallivertailuraporttigeneraattori (laajenna vertailuskriptiä markdown-viennillä).

## Aloitusprojekti: Laajenna `03-huggingface-models`

Paranna olemassa olevaa esimerkkiä:

1. Lisää vertailujen yhdistäminen + CSV/Markdown-vienti.
2. Toteuta yksinkertainen laadullinen pisteytys (kehotepareja + manuaalinen annotointitiedosto).
3. Lisää JSON-konfiguraatio (`models.json`) mallilistan ja kehotteiden joukon muokattavuutta varten.

## Vahvistuslista

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Kaikkien kohdemallien tulisi näkyä ja vastata testikehotteeseen.

## Esimerkkiskenaario ja työpajan kartoitus

| Työpajan skripti | Skenaario | Tavoite | Kehote / datasetin lähde |
|------------------|-----------|---------|--------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Reunaplatform-tiimi valitsee oletus-SLM:n upotetulle tiivistelmälle | Tuottaa viive + p95 + tokenit/sekunti -vertailu ehdokasmallien välillä | Inline `PROMPT` var + ympäristö `BENCH_MODELS` lista |

### Skenaarion narratiivi
Tuotetekniikan tiimin täytyy valita oletuskevyt tiivistämismalli offline-kokousmuistiinpanojen ominaisuutta varten. He suorittavat kontrolloituja deterministisiä vertailuja (temperature=0) kiinteän kehottejoukon avulla (katso esimerkki alla) ja keräävät viive- ja läpäisymetriikoita GPU-kiihdytyksen kanssa ja ilman.

### Esimerkkikehotteiden JSON (laajennettavissa)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Käy läpi jokainen kehote per malli, tallenna kehotekohtainen viive jakaumametriikoiden johdannaiseksi ja havaitse poikkeamat.

## Mallin valintakehys

| Ulottuvuus | Mittari | Miksi tärkeää |
|------------|---------|---------------|
| Viive | keskiarvo / p95 | Käyttäjäkokemuksen johdonmukaisuus |
| Läpäisy | tokenit/sekunti | Erä- ja suoratoistettavuus |
| Muisti | käytössä oleva koko | Laitteeseen sopivuus ja samanaikaisuus |
| Laatu | arviointikehotteet | Tehtävän soveltuvuus |
| Jälki | levyn välimuisti | Jakelu ja päivitykset |
| Lisenssi | käyttöoikeus | Kaupallinen yhteensopivuus |

## Laajentaminen mukautetulla mallilla

Korkean tason malli (pseudokoodi):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Katso virallinen repo kehittyviä adapteriliittymiä varten:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Vianetsintä

| Ongelma | Syynä | Korjaus |
|---------|-------|--------|
| OOM mistral-7b:ssä | Riittämätön RAM/GPU | Lopeta muut mallit; kokeile pienempää varianttia |
| Hidas ensimmäinen vastaus | Kylmä lataus | Pidä lämpimänä kevyellä kehotteella säännöllisesti |
| Lataus keskeytyy | Verkkoyhteyden epävakaus | Yritä uudelleen; esilataa hiljaisina aikoina |

## Viitteet

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Hugging Face Model Discovery: https://huggingface.co/models

---

**Istunnon kesto**: 30 min (+ valinnainen syventävä osuus)  
**Vaikeustaso**: Keskitaso

### Valinnaiset parannukset

| Parannus | Hyöty | Miten |
|----------|-------|-------|
| Suoratoiston ensimmäisen tokenin viive | Mittaa koettua reagointikykyä | Suorita vertailu `BENCH_STREAM=1` (parannettu skripti `Workshop/samples/session03`) |
| Deterministinen tila | Vakaa regressiovertailu | `temperature=0`, kiinteä kehottejoukko, tallenna JSON-tulokset versionhallintaan |
| Laadun arviointipisteytys | Lisää laadullisen ulottuvuuden | Ylläpidä `prompts.json` odotettujen ominaisuuksien kanssa; pisteytä (1–5) manuaalisesti tai toissijaisen mallin avulla |
| CSV / Markdown-vienti | Jaettava raportti | Laajenna skripti kirjoittamaan `benchmark_report.md` taulukolla ja kohokohdilla |
| Mallin ominaisuustunnisteet | Automaattinen reititys myöhemmin | Ylläpidä `models.json` tiedostoa, jossa `{alias: {capabilities:[], size_mb:..}}` |
| Välimuistin esilämmitys | Vähennä kylmäkäynnistysviivettä | Suorita yksi lämmittelykierros ennen ajastussilmukkaa (jo toteutettu) |
| Prosenttipisteen tarkkuus | Kestävä häntäviive | Käytä numpy-prosenttipistettä (jo uudelleenmuokatussa skriptissä) |
| Token-kustannusten arviointi | Taloudellinen vertailu | Arvioitu kustannus = (tokenit/sekunti * keskimääräinen tokenien määrä per pyyntö) * energiakulutuksen heuristiikka |
| Epäonnistuneiden mallien automaattinen ohitus | Kestävyys eräajoissa | Kääri jokainen vertailu try/except-lohkoon ja merkitse tilakenttä |

#### Minimal Markdown Export Snippet

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```

#### Deterministinen kehottejoukkoesimerkki

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Käytä staattista listaa satunnaisten kehotteiden sijaan vertailukelpoisten metriikoiden saamiseksi eri commitien välillä.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->