# Workshop Notebooks - Průvodce řešením problémů

## Obsah

- [Běžné problémy a jejich řešení](../../../../Workshop/notebooks)
- [Specifické problémy pro Session 04](../../../../Workshop/notebooks)
- [Specifické problémy pro Session 05](../../../../Workshop/notebooks)
- [Specifické problémy pro Session 06](../../../../Workshop/notebooks)
- [Problémy specifické pro hardware](../../../../Workshop/notebooks)
- [Diagnostické příkazy](../../../../Workshop/notebooks)
- [Jak získat pomoc](../../../../Workshop/notebooks)

---

## Běžné problémy a jejich řešení

### 🔴 CUDA Out of Memory

**Chybová zpráva:**
```
CUDA failure 2: out of memory
```

**Příčina:** GPU nemá dostatek VRAM pro načtení modelu.

**Řešení:**

#### Možnost 1: Použijte varianty pro CPU (doporučeno)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Možnost 2: Použijte menší modely na GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Možnost 3: Vyčistěte paměť GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Možnost 4: Zvyšte paměť GPU (pokud je to možné)
- Zavřete záložky v prohlížeči, video editory nebo jiné aplikace využívající GPU
- Snižte vizuální efekty Windows
- Použijte dedikované GPU, pokud máte integrované + dedikované

---

### 🔴 APIConnectionError: Connection Error

**Chybová zpráva:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Příčina:** Služba Foundry Local neběží nebo není dostupná.

**Řešení:**

#### Krok 1: Zkontrolujte stav služby
```bash
foundry service status
```

#### Krok 2: Spusťte službu, pokud je zastavena
```bash
foundry service start
```

#### Krok 3: Ověřte endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Krok 4: Načtěte požadované modely
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Krok 5: Restartujte kernel notebooku
Po spuštění služby a načtení modelů restartujte kernel notebooku a znovu spusťte všechny buňky.

---

### 🔴 Model Not Found in Catalog

**Chybová zpráva:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Příčina:** Model není stažen nebo načten v Foundry Local.

**Řešení:**

#### Možnost 1: Stáhněte a načtěte modely
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

#### Možnost 2: Použijte režim automatického výběru
Aktualizujte svůj CATALOG tak, aby používal základní názvy modelů (bez přípony `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK automaticky vybere nejlepší variantu (CPU, GPU nebo NPU) pro váš hardware.

---

### 🔴 HttpResponseError: 500 - Failed Loading Model

**Chybová zpráva:**
```
HttpResponseError: 500 - Failed loading model
```

**Příčina:** Soubor modelu je poškozen nebo není kompatibilní s hardwarem.

**Řešení:**

#### Znovu stáhněte model
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Použijte jinou variantu
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: No Module Found

**Chybová zpráva:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Příčina:** Balíček foundry-local-sdk není nainstalován.

**Řešení:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Pomalejší první požadavek

**Příznak:** První dokončení trvá více než 30 sekund, následující požadavky jsou rychlé.

**Příčina:** Toto je normální chování - služba načítá model do paměti při prvním požadavku.

**Řešení:**

#### Předem načtěte modely
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Nechte službu běžet
```bash
# Start service manually and leave it running
foundry service start
```

---

## Specifické problémy pro Session 04

### Nesprávná konfigurace portu

**Problém:** Notebook se připojuje k nesprávnému portu (55769 vs 59959 vs 57127)

**Řešení:**

1. Zjistěte, který port používá Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Aktualizujte buňku 10 v notebooku:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Restartujte kernel a znovu spusťte buňky 6, 8, 10, 12, 16, 20, 22

---

### Nesprávný výběr modelu

**Problém:** Notebook zobrazuje gpt-oss-20b nebo qwen2.5-7b místo qwen2.5-3b

**Řešení:**

1. Restartujte kernel notebooku (vymaže starý stav proměnných)
2. Znovu spusťte buňku 10 (nastavení aliasů modelů)
3. Znovu spusťte buňku 12 (zobrazení konfigurace)
4. **Ověřte:** Buňka 12 by měla zobrazit `LLM Model: qwen2.5-3b`

---

### Diagnostická buňka selhává

**Problém:** Buňka 16 zobrazuje "❌ Foundry Local service not found!"

**Řešení:**

1. Ověřte, že služba běží:
```bash
foundry service status
```

2. Otestujte endpoint ručně:
```bash
curl http://localhost:59959/v1/models
```

3. Pokud curl funguje, ale notebook ne:
   - Restartujte kernel notebooku
   - Znovu spusťte buňky v pořadí: 6, 8, 10, 12, 14, 16

4. Pokud curl selže:
   - Spusťte službu: `foundry service start`
   - Načtěte modely: `foundry model run phi-4-mini` a `foundry model run qwen2.5-3b`

---

### Pre-flight Check selhává

**Problém:** Buňka 20 zobrazuje chyby připojení, i když diagnostika prošla

**Řešení:**

1. Zkontrolujte, zda jsou modely načteny:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Pokud modely chybí:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Znovu spusťte buňku 20 po načtení modelů

---

### Porovnání selhává s hodnotami None

**Problém:** Buňka 22 se dokončí, ale zobrazuje latenci jako None

**Řešení:**

1. Zkontrolujte, zda pre-flight prošel (buňka 20)
2. Znovu spusťte buňku 22 - modely se mohou při prvním požadavku zahřívat
3. Ověřte, že oba modely jsou načteny: `foundry model ls`

---

## Specifické problémy pro Session 05

### Agent používá nesprávný model

**Problém:** Agent nepoužívá očekávaný model

**Řešení:**

Ověřte konfiguraci:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Restartujte kernel, pokud jsou modely nesprávné.

---

### Přetečení paměťového kontextu

**Problém:** Odezvy agenta se postupně zhoršují

**Řešení:** Již automaticky řešeno - agenti uchovávají pouze posledních 6 zpráv v paměti.

---

## Specifické problémy pro Session 06

### Zmatek mezi modely CPU a GPU

**Problém:** Zobrazení chyb CUDA při použití výchozí konfigurace

**Řešení:** Výchozí konfigurace nyní používá modely pro CPU. Pokud vidíte chyby CUDA:

1. Ověřte, že používáte výchozí katalog pro CPU:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Restartujte kernel a znovu spusťte všechny buňky

---

### Detekce záměru nefunguje

**Problém:** Výzvy jsou směrovány na nesprávné modely

**Řešení:**

Otestujte detekci záměru:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Aktualizujte RULES, pokud je třeba upravit vzory.

---

## Problémy specifické pro hardware

### NVIDIA GPU

**Zkontrolujte stav GPU:**
```bash
nvidia-smi
```

**Běžné problémy:**
- **Zastaralý ovladač:** Aktualizujte ovladače NVIDIA
- **Nesoulad verzí CUDA:** Přeinstalujte Foundry Local
- **Fragmentovaná paměť GPU:** Restartujte systém

### Qualcomm NPU

**Zkontrolujte stav NPU:**
```bash
foundry device info
```

**Běžné problémy:**
- **Ovladače NPU nejsou nainstalovány:** Nainstalujte ovladače Qualcomm NPU
- **Varianta NPU není dostupná:** Použijte variantu pro CPU
- **Příliš stará verze Windows:** Aktualizujte na nejnovější Windows 11

### Systémy pouze s CPU

**Doporučené modely:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Tipy pro výkon:**
- Používejte nejmenší modely
- Snižte max_tokens
- Buďte trpěliví při prvním požadavku

---

## Diagnostické příkazy

### Zkontrolujte vše
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

### V Pythonu
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

## Jak získat pomoc

### 1. Zkontrolujte logy
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub Issues
- Vyhledejte existující problémy: https://github.com/microsoft/Foundry-Local/issues
- Vytvořte nový problém s:
  - Chybovou zprávou (celý text)
  - Výstupem `foundry service status`
  - Výstupem `foundry --version`
  - Informacemi o GPU/NPU (nvidia-smi, atd.)
  - Kroky k reprodukci

### 3. Dokumentace
- **Hlavní repozitář:** https://github.com/microsoft/Foundry-Local
- **Python SDK:** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI Reference:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Troubleshooting:** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Kontrolní seznam rychlých oprav

Když se něco pokazí, zkuste postupně:

- [ ] Zkontrolujte, zda služba běží: `foundry service status`
- [ ] Restartujte službu: `foundry service stop && foundry service start`
- [ ] Ověřte, že model existuje: `foundry model ls | grep phi-4-mini`
- [ ] Načtěte požadované modely: `foundry model run phi-4-mini`
- [ ] Zkontrolujte paměť GPU: `nvidia-smi` (pokud NVIDIA)
- [ ] Vyzkoušejte variantu pro CPU: Použijte `phi-4-mini-cpu` místo `phi-4-mini`
- [ ] Restartujte kernel notebooku
- [ ] Vymažte výstupy notebooku a znovu spusťte všechny buňky
- [ ] Přeinstalujte SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Restartujte systém (poslední možnost)

---

## Tipy pro prevenci

### Nejlepší postupy

1. **Vždy nejprve zkontrolujte službu:**
   ```bash
   foundry service status
   ```

2. **Používejte varianty pro CPU jako výchozí:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Předem načtěte modely před spuštěním notebooků:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Nechte službu běžet:**
   - Zbytečně nezastavujte/spouštějte službu
   - Nechte ji běžet na pozadí mezi relacemi

5. **Monitorujte zdroje:**
   - Zkontrolujte paměť GPU před spuštěním
   - Zavřete nepotřebné aplikace využívající GPU
   - Použijte Správce úloh / nvidia-smi

6. **Pravidelně aktualizujte:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Poslední aktualizace:** 8. října 2025

---

**Upozornění**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.