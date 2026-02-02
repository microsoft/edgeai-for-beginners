# Workshop Notebooks - Príručka na riešenie problémov

## Obsah

- [Bežné problémy a riešenia](../../../../Workshop/notebooks)
- [Problémy špecifické pre Session 04](../../../../Workshop/notebooks)
- [Problémy špecifické pre Session 05](../../../../Workshop/notebooks)
- [Problémy špecifické pre Session 06](../../../../Workshop/notebooks)
- [Problémy súvisiace s hardvérom](../../../../Workshop/notebooks)
- [Diagnostické príkazy](../../../../Workshop/notebooks)
- [Získanie pomoci](../../../../Workshop/notebooks)

---

## Bežné problémy a riešenia

### 🔴 CUDA Out of Memory

**Chybová správa:**
```
CUDA failure 2: out of memory
```

**Príčina:** GPU nemá dostatok VRAM na načítanie modelu.

**Riešenia:**

#### Možnosť 1: Použiť CPU varianty (odporúčané)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Možnosť 2: Použiť menšie modely na GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Možnosť 3: Vyčistiť pamäť GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Možnosť 4: Zvýšiť pamäť GPU (ak je to možné)
- Zatvorte karty prehliadača, video editory alebo iné aplikácie využívajúce GPU
- Znížte vizuálne efekty Windows
- Použite dedikovanú GPU, ak máte integrovanú + dedikovanú

---

### 🔴 APIConnectionError: Connection Error

**Chybová správa:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Príčina:** Služba Foundry Local nebeží alebo nie je dostupná.

**Riešenia:**

#### Krok 1: Skontrolujte stav služby
```bash
foundry service status
```

#### Krok 2: Spustite službu, ak je zastavená
```bash
foundry service start
```

#### Krok 3: Overte koncový bod
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Krok 4: Načítajte požadované modely
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Krok 5: Reštartujte kernel notebooku
Po spustení služby a načítaní modelov reštartujte kernel notebooku a znovu spustite všetky bunky.

---

### 🔴 Model Not Found in Catalog

**Chybová správa:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Príčina:** Model nie je stiahnutý alebo načítaný vo Foundry Local.

**Riešenia:**

#### Možnosť 1: Stiahnite a načítajte modely
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Možnosť 2: Použite režim automatického výberu
Aktualizujte svoj CATALOG tak, aby používal základné názvy modelov (bez prípony `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK automaticky vyberie najlepší variant (CPU, GPU alebo NPU) pre váš hardvér.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Chybová správa:**
```
HttpResponseError: 500 - Failed loading model
```

**Príčina:** Súbor modelu je poškodený alebo nekompatibilný s hardvérom.

**Riešenia:**

#### Znovu stiahnite model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Použite iný variant
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Chybová správa:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Príčina:** Balík foundry-local-sdk nie je nainštalovaný.

**Riešenia:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Pomalá prvá požiadavka

**Príznak:** Prvé dokončenie trvá viac ako 30 sekúnd, následné požiadavky sú rýchle.

**Príčina:** Toto je normálne správanie - služba načítava model do pamäte pri prvej požiadavke.

**Riešenia:**

#### Predbežné načítanie modelov
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Nechajte službu bežať
```bash
# Start service manually and leave it running
foundry service start
```

---

## Problémy špecifické pre Session 04

### Nesprávna konfigurácia portu

**Problém:** Notebook sa pripája na nesprávny port (55769 vs 59959 vs 57127)

**Riešenie:**

1. Skontrolujte, ktorý port používa Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Aktualizujte bunku 10 v notebooku:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Reštartujte kernel a znovu spustite bunky 6, 8, 10, 12, 16, 20, 22

---

### Nesprávny výber modelu

**Problém:** Notebook zobrazuje gpt-oss-20b alebo qwen2.5-7b namiesto qwen2.5-3b

**Riešenie:**

1. Reštartujte kernel notebooku (vymaže starý stav premenných)
2. Znovu spustite bunku 10 (nastavenie aliasov modelov)
3. Znovu spustite bunku 12 (zobrazenie konfigurácie)
4. **Overte:** Bunka 12 by mala zobraziť `LLM Model: qwen2.5-3b`

---

### Diagnostická bunka zlyháva

**Problém:** Bunka 16 zobrazuje "❌ Foundry Local service not found!"

**Riešenie:**

1. Overte, že služba beží:
```bash
foundry service status
```

2. Otestujte koncový bod manuálne:
```bash
curl http://localhost:59959/v1/models
```

3. Ak curl funguje, ale notebook nie:
   - Reštartujte kernel notebooku
   - Znovu spustite bunky v poradí: 6, 8, 10, 12, 14, 16

4. Ak curl zlyhá:
   - Spustite službu: `foundry service start`
   - Načítajte modely: `foundry model run phi-4-mini` a `foundry model run qwen2.5-3b`

---

### Predletová kontrola zlyháva

**Problém:** Bunka 20 zobrazuje chyby pripojenia, aj keď diagnostika prešla

**Riešenie:**

1. Skontrolujte, či sú modely načítané:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Ak modely chýbajú:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Znovu spustite bunku 20 po načítaní modelov

---

### Porovnanie zlyháva s hodnotami None

**Problém:** Bunka 22 dokončí, ale zobrazuje latenciu ako None

**Riešenie:**

1. Skontrolujte, či predletová kontrola prešla (bunka 20)
2. Znovu spustite bunku 22 - modely sa môžu potrebovať zahriať pri prvej požiadavke
3. Overte, že oba modely sú načítané: `foundry model ls`

---

## Problémy špecifické pre Session 05

### Agent používa nesprávny model

**Problém:** Agent nepoužíva očakávaný model

**Riešenie:**

Overte konfiguráciu:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Reštartujte kernel, ak sú modely nesprávne.

---

### Pretečenie pamäťového kontextu

**Problém:** Odpovede agenta sa časom zhoršujú

**Riešenie:** Už automaticky riešené - agenti si uchovávajú iba posledných 6 správ v pamäti.

---

## Problémy špecifické pre Session 06

### Zmätok medzi CPU a GPU modelmi

**Problém:** Chyby CUDA pri použití predvolenej konfigurácie

**Riešenie:** Predvolená konfigurácia teraz používa CPU modely. Ak vidíte chyby CUDA:

1. Overte, že používate predvolený CPU katalóg:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Reštartujte kernel a znovu spustite všetky bunky

---

### Detekcia zámeru nefunguje

**Problém:** Výzvy sú smerované na nesprávne modely

**Riešenie:**

Otestujte detekciu zámeru:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Aktualizujte RULES, ak je potrebné upraviť vzory.

---

## Problémy súvisiace s hardvérom

### NVIDIA GPU

**Skontrolujte stav GPU:**
```bash
nvidia-smi
```

**Bežné problémy:**
- **Zastaralý ovládač:** Aktualizujte ovládače NVIDIA
- **Nesúlad verzie CUDA:** Znovu nainštalujte Foundry Local
- **Fragmentovaná pamäť GPU:** Reštartujte systém

### Qualcomm NPU

**Skontrolujte stav NPU:**
```bash
foundry device info
```

**Bežné problémy:**
- **Ovládače NPU nie sú nainštalované:** Nainštalujte ovládače Qualcomm NPU
- **Variant NPU nie je dostupný:** Použite CPU variant
- **Príliš stará verzia Windows:** Aktualizujte na najnovší Windows 11

### Systémy iba s CPU

**Odporúčané modely:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Tipy na výkon:**
- Používajte najmenšie modely
- Znížte max_tokens
- Majte trpezlivosť pri prvej požiadavke

---

## Diagnostické príkazy

### Skontrolujte všetko
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### V Pythone
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Získanie pomoci

### 1. Skontrolujte logy
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Vyhľadajte existujúce problémy: https://github.com/microsoft/Foundry-Local/issues
- Vytvorte nový problém s:
  - Chybovou správou (celý text)
  - Výstupom `foundry service status`
  - Výstupom `foundry --version`
  - Informáciami o GPU/NPU (nvidia-smi, atď.)
  - Krokmi na reprodukciu

### 3. Dokumentácia
- **Hlavné úložisko:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Referencia:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Riešenie problémov:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Kontrolný zoznam rýchlych opráv

Keď sa niečo pokazí, skúste tieto kroky v poradí:

- [ ] Skontrolujte, či služba beží: `foundry service status`
- [ ] Reštartujte službu: `foundry service stop && foundry service start`
- [ ] Overte existenciu modelu: `foundry model ls | grep phi-4-mini`
- [ ] Načítajte požadované modely: `foundry model run phi-4-mini`
- [ ] Skontrolujte pamäť GPU: `nvidia-smi` (ak NVIDIA)
- [ ] Skúste CPU variant: Použite `phi-4-mini-cpu` namiesto `phi-4-mini`
- [ ] Reštartujte kernel notebooku
- [ ] Vymažte výstupy notebooku a znovu spustite všetky bunky
- [ ] Znovu nainštalujte SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Reštartujte systém (posledná možnosť)

---

## Tipy na prevenciu

### Najlepšie postupy

1. **Vždy najprv skontrolujte službu:**
   ```bash
   foundry service status
   ```

2. **Používajte CPU varianty predvolene:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Predbežne načítajte modely pred spustením notebookov:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Nechajte službu bežať:**
   - Neprestávajte/spúšťajte službu zbytočne
   - Nechajte ju bežať na pozadí medzi reláciami

5. **Monitorujte zdroje:**
   - Skontrolujte pamäť GPU pred spustením
   - Zatvorte nepotrebné aplikácie využívajúce GPU
   - Použite Správcu úloh / nvidia-smi

6. **Pravidelne aktualizujte:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Posledná aktualizácia:** 8. október 2025

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.