<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T22:16:31+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "fi"
}
-->
# Työpajan pikaopas

## Esivaatimukset

### 1. Asenna Foundry Local

Seuraa virallista asennusopasta:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Asenna Python-riippuvuudet

Työpajan hakemistosta:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Työpajan esimerkkien suorittaminen

### Istunto 01: Peruskeskustelu

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Ympäristömuuttujat:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Istunto 02: RAG-putki

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Ympäristömuuttujat:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Istunto 02: RAG-arviointi (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Huom:** Vaatii lisäriippuvuuksia, jotka asennetaan `requirements.txt`-tiedoston kautta.

### Istunto 03: Suorituskyvyn arviointi

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Ympäristömuuttujat:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Tuloste:** JSON, joka sisältää viive-, läpimeno- ja ensimmäisen tokenin metrikat.

### Istunto 04: Mallien vertailu

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Ympäristömuuttujat:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Istunto 05: Moniagenttinen orkestrointi

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Ympäristömuuttujat:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Istunto 06: Mallireititin

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testaa reitityslogiikkaa** useilla tarkoituksilla (koodi, tiivistäminen, luokittelu).

### Istunto 06: Putki

```bash
python -m session06.models_pipeline
```

**Monimutkainen monivaiheinen putki**, joka sisältää suunnittelun, toteutuksen ja hienosäädön.

## Skriptit

### Suorituskykyraportin vienti

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Tuloste:** Markdown-taulukko + JSON-metrikat

### Markdown CLI -mallien tarkistus

```bash
python lint_markdown_cli.py --verbose
```

**Tarkoitus:** Havaitse vanhentuneet CLI-mallit dokumentaatiosta.

## Testaus

### Perustestit

```bash
cd Workshop
python -m tests.smoke
```

**Testit:** Keskeisten esimerkkien perustoiminnallisuus.

## Vianetsintä

### Palvelu ei käynnissä

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Moduulin tuontivirheet

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Yhteysvirheet

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Mallia ei löydy

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Ympäristömuuttujien viite

### Ydinmääritykset
| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | Vaihtelee | Käytettävä mallialias |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Ylikirjoita palvelun päätepiste |
| `SHOW_USAGE` | `0` | Näytä tokenien käyttötilastot |
| `RETRY_ON_FAIL` | `1` | Ota käyttöön uudelleenyritto |
| `RETRY_BACKOFF` | `1.0` | Alkuperäinen viive uudelleenyrittämisessä (sekunteina) |

### Istuntokohtaiset
| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Upotusmalli |
| `RAG_QUESTION` | Katso esimerkki | RAG-testikysymys |
| `BENCH_MODELS` | Vaihtelee | Pilkulla erotetut mallit |
| `BENCH_ROUNDS` | `3` | Suorituskykytestin toistot |
| `BENCH_PROMPT` | Katso esimerkki | Suorituskykytestin kehotus |
| `BENCH_STREAM` | `0` | Mittaa ensimmäisen tokenin viive |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Ensisijainen agenttimalli |
| `AGENT_MODEL_EDITOR` | Ensisijainen | Editorin agenttimalli |
| `SLM_ALIAS` | `phi-4-mini` | Pieni kielimalli |
| `LLM_ALIAS` | `qwen2.5-7b` | Suuri kielimalli |
| `COMPARE_PROMPT` | Katso esimerkki | Vertailukehotus |

## Suositellut mallit

### Kehitys ja testaus
- **phi-4-mini** - Tasapainoinen laatu ja nopeus
- **qwen2.5-0.5b** - Erittäin nopea luokittelussa
- **gemma-2-2b** - Hyvä laatu, kohtuullinen nopeus

### Tuotantokäyttö
- **phi-4-mini** - Yleiskäyttöinen
- **deepseek-coder-1.3b** - Koodin generointi
- **qwen2.5-7b** - Korkealaatuiset vastaukset

## SDK-dokumentaatio

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Apua

1. Tarkista palvelun tila: `foundry service status`  
2. Katso lokit: Tarkista Foundry Local -palvelun lokit  
3. Tutustu SDK-dokumentaatioon: https://github.com/microsoft/Foundry-Local  
4. Tarkista esimerkkikoodi: Kaikissa esimerkeissä on yksityiskohtaiset kommentit.

## Seuraavat askeleet

1. Suorita kaikki työpajan istunnot järjestyksessä  
2. Kokeile erilaisia malleja  
3. Muokkaa esimerkkejä omiin käyttötarkoituksiisi  
4. Tutustu `SDK_MIGRATION_NOTES.md`-tiedostoon edistyneitä malleja varten  

---

**Viimeksi päivitetty**: 2025-01-08  
**Työpajan versio**: Uusin  
**SDK**: Foundry Local Python SDK

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.