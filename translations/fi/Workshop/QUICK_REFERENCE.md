# Työpajan näytteet - Pikaopas

**Viimeksi päivitetty**: 8. lokakuuta 2025

---

## 🚀 Pika-aloitus

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Näyteyleiskatsaus

| Istunto | Näyte | Tarkoitus | Aika |
|---------|-------|-----------|------|
| 01 | `chat_bootstrap.py` | Peruschatti + suoratoisto | ~30s |
| 02 | `rag_pipeline.py` | RAG upotuksilla | ~45s |
| 02 | `rag_eval_ragas.py` | RAG-arviointi | ~60s |
| 03 | `benchmark_oss_models.py` | Mallien vertailu | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Moniagenttijärjestelmä | ~60s |
| 06 | `models_router.py` | Tarkoituksenmukainen reititys | ~45s |
| 06 | `models_pipeline.py` | Monivaiheinen putki | ~60s |

---

## 🛠️ Ympäristömuuttujat

### Välttämättömät
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Istuntokohtaiset
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Vahvistus ja testaus

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Vianmääritys

### Yhteysvirhe
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Tuontivirhe
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Mallia ei löydy
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Hidas suorituskyky
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Yleiset mallit

### Peruschatti
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Asiakkaan haku
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Virheenkäsittely
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Suoratoisto
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Mallin valinta

| Malli | Koko | Parhaimmillaan | Nopeus |
|-------|------|----------------|--------|
| `qwen2.5-0.5b` | 0.5B | Nopea luokittelu | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Nopea koodin generointi | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Luova kirjoittaminen | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Koodi, refaktorointi | ⚡⚡ |
| `phi-4-mini` | 4B | Yleinen, tiivistys | ⚡⚡ |
| `qwen2.5-7b` | 7B | Monimutkainen päättely | ⚡ |

---

## 🔗 Resurssit

- **SDK-dokumentaatio**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Pikaopas**: `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Vinkkejä

1. **Välimuistiasiakkaat**: `workshop_utils` hoitaa välimuistin puolestasi
2. **Käytä pienempiä malleja**: Aloita `qwen2.5-0.5b`-mallilla testaukseen
3. **Ota käyttötilastot käyttöön**: Aseta `SHOW_USAGE=1` seurataksesi tokenien käyttöä
4. **Eräkäsittely**: Käsittele useita kehotteita peräkkäin
5. **Pienennä max_tokens**: Vähentää viivettä nopeampia vastauksia varten

---

## 🎯 Näyteprosessit

### Testaa kaikki
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Mallien vertailu
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG-putki
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Moniagenttijärjestelmä
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Pika-apu**: Aja mikä tahansa näyte komennolla `--help` kansiosta `samples` tai tarkista docstring:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Kaikki näytteet päivitetty lokakuussa 2025 Foundry Local SDK:n parhaiden käytäntöjen mukaisesti** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->