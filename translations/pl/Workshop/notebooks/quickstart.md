# Warsztaty Notebooks - Szybki Przewodnik

## Spis Treści

- [Wymagania wstępne](../../../../Workshop/notebooks)
- [Początkowa konfiguracja](../../../../Workshop/notebooks)
- [Sesja 04: Porównanie modeli](../../../../Workshop/notebooks)
- [Sesja 05: Orkiestrator wieloagentowy](../../../../Workshop/notebooks)
- [Sesja 06: Routing modeli oparty na intencjach](../../../../Workshop/notebooks)
- [Zmienne środowiskowe](../../../../Workshop/notebooks)
- [Popularne polecenia](../../../../Workshop/notebooks)

---

## Wymagania wstępne

### 1. Zainstaluj Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Weryfikacja instalacji:**
```bash
foundry --version
```

### 2. Zainstaluj zależności Pythona

```bash
cd Workshop
pip install -r requirements.txt
```

Lub zainstaluj pojedynczo:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Początkowa konfiguracja

### Uruchom usługę Foundry Local

**Wymagane przed uruchomieniem jakiegokolwiek notebooka:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Oczekiwany wynik:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Pobierz i załaduj modele

Notatniki domyślnie używają następujących modeli:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Weryfikacja konfiguracji

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sesja 04: Porównanie modeli

### Cel
Porównanie wydajności między małymi modelami językowymi (SLM) a dużymi modelami językowymi (LLM).

### Szybka konfiguracja

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Uruchamianie notebooka

1. **Otwórz** `session04_model_compare.ipynb` w VS Code lub Jupyter
2. **Zrestartuj kernel** (Kernel → Restart Kernel)
3. **Uruchom wszystkie komórki** w kolejności

### Kluczowa konfiguracja

**Domyślne modele:**
- **SLM:** `phi-4-mini` (~4GB RAM, szybszy)
- **LLM:** `qwen2.5-3b` (~3GB RAM, zoptymalizowany pod kątem pamięci)

**Zmienne środowiskowe (opcjonalne):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Oczekiwany wynik

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Dostosowanie

**Użyj innych modeli:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Własny prompt:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Lista kontrolna weryfikacji

- [ ] Komórka 12 pokazuje poprawne modele (phi-4-mini, qwen2.5-3b)
- [ ] Komórka 12 pokazuje poprawny endpoint (port 59959)
- [ ] Diagnostyka w komórce 16 przechodzi (✅ Usługa działa)
- [ ] Kontrola przed uruchomieniem w komórce 20 przechodzi (oba modele ok)
- [ ] Porównanie w komórce 22 kończy się z wartościami opóźnienia
- [ ] Walidacja w komórce 24 pokazuje 🎉 WSZYSTKIE TESTY ZALICZONE!

### Szacowany czas
- **Pierwsze uruchomienie:** 5-10 minut (w tym pobieranie modeli)
- **Kolejne uruchomienia:** 1-2 minuty

---

## Sesja 05: Orkiestrator wieloagentowy

### Cel
Demonstracja współpracy wieloagentowej za pomocą Foundry Local SDK - agenci współpracują, aby uzyskać bardziej dopracowane wyniki.

### Szybka konfiguracja

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Uruchamianie notebooka

1. **Otwórz** `session05_agents_orchestrator.ipynb`
2. **Zrestartuj kernel**
3. **Uruchom wszystkie komórki** w kolejności

### Kluczowa konfiguracja

**Domyślna konfiguracja (ten sam model dla obu agentów):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Zaawansowana konfiguracja (różne modele):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architektura

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Oczekiwany wynik

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Rozszerzenia

**Dodaj więcej agentów:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Testowanie wsadowe:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Szacowany czas
- **Pierwsze uruchomienie:** 3-5 minut
- **Kolejne uruchomienia:** 1-2 minuty na pytanie

---

## Sesja 06: Routing modeli oparty na intencjach

### Cel
Inteligentne kierowanie promptów do wyspecjalizowanych modeli na podstawie wykrytej intencji.

### Szybka konfiguracja

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Uwaga:** Sesja 06 domyślnie używa modeli CPU dla maksymalnej kompatybilności.

### Uruchamianie notebooka

1. **Otwórz** `session06_models_router.ipynb`
2. **Zrestartuj kernel**
3. **Uruchom wszystkie komórki** w kolejności

### Kluczowa konfiguracja

**Domyślny katalog (modele CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternatywa (modele GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Wykrywanie intencji

Router używa wzorców regex do wykrywania intencji:

| Intencja | Przykłady wzorców | Kierowane do |
|----------|-------------------|--------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Wszystko inne | phi-4-mini-cpu |

### Oczekiwany wynik

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Dostosowanie

**Dodaj własną intencję:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Włącz śledzenie tokenów:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Przełączanie na modele GPU

Jeśli masz 8GB+ VRAM:

1. W **komórce #6**, zakomentuj katalog CPU
2. Odkomentuj katalog GPU
3. Załaduj modele GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Zrestartuj kernel i uruchom notebook ponownie

### Szacowany czas
- **Pierwsze uruchomienie:** 5-10 minut (ładowanie modeli)
- **Kolejne uruchomienia:** 30-60 sekund na test

---

## Zmienne środowiskowe

### Globalna konfiguracja

Ustaw przed uruchomieniem Jupyter/VS Code:

**Windows (Command Prompt):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Konfiguracja w notebooku

Ustaw na początku dowolnego notebooka:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Popularne polecenia

### Zarządzanie usługą

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Zarządzanie modelami

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Testowanie endpointów

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Polecenia diagnostyczne

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Najlepsze praktyki

### Przed uruchomieniem jakiegokolwiek notebooka

1. **Sprawdź, czy usługa działa:**
   ```bash
   foundry service status
   ```

2. **Zweryfikuj, czy modele są załadowane:**
   ```bash
   foundry model ls
   ```

3. **Zrestartuj kernel notebooka** w przypadku ponownego uruchamiania

4. **Wyczyść wszystkie wyniki** dla czystego uruchomienia

### Zarządzanie zasobami

1. **Używaj modeli CPU domyślnie** dla kompatybilności
2. **Przełącz na modele GPU** tylko jeśli masz 8GB+ VRAM
3. **Zamknij inne aplikacje GPU** przed uruchomieniem
4. **Utrzymuj działającą usługę** między sesjami notebooka
5. **Monitoruj użycie zasobów** za pomocą Task Manager / nvidia-smi

### Rozwiązywanie problemów

1. **Zawsze najpierw sprawdź usługę** przed debugowaniem kodu
2. **Zrestartuj kernel** w przypadku przestarzałej konfiguracji
3. **Uruchom ponownie komórki diagnostyczne** po jakichkolwiek zmianach
4. **Sprawdź nazwy modeli**, czy pasują do załadowanych
5. **Zweryfikuj port endpointu**, czy pasuje do statusu usługi

---

## Szybki przegląd: Alias modeli

### Popularne modele

| Alias | Rozmiar | Najlepsze zastosowanie | RAM/VRAM | Warianty |
|-------|---------|------------------------|----------|----------|
| `phi-4-mini` | ~4B | Ogólne rozmowy, podsumowania | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generowanie kodu, refaktoryzacja | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Zadania ogólne, efektywność | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Szybkość, niskie zasoby | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Klasyfikacja, minimalne zasoby | 1-2GB | `-cpu`, `-cuda-gpu` |

### Nazewnictwo wariantów

- **Nazwa podstawowa** (np. `phi-4-mini`): Automatycznie wybiera najlepszy wariant dla twojego sprzętu
- **`-cpu`**: Optymalizacja dla CPU, działa wszędzie
- **`-cuda-gpu`**: Optymalizacja dla NVIDIA GPU, wymaga 8GB+ VRAM
- **`-npu`**: Optymalizacja dla Qualcomm NPU, wymaga sterowników NPU

**Rekomendacja:** Używaj nazw podstawowych (bez sufiksu) i pozwól Foundry Local automatycznie wybrać najlepszy wariant.

---

## Wskaźniki sukcesu

Jesteś gotowy, gdy widzisz:

✅ `foundry service status` pokazuje "running"
✅ `foundry model ls` pokazuje wymagane modele
✅ Usługa dostępna na poprawnym endpointcie
✅ Kontrola zdrowia zwraca 200 OK
✅ Komórki diagnostyczne w notebooku przechodzą
✅ Brak błędów połączenia w wynikach

---

## Uzyskiwanie pomocy

### Dokumentacja
- **Główne repozytorium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referencja CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Rozwiązywanie problemów**: Zobacz `troubleshooting.md` w tym katalogu

### Problemy na GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Ostatnia aktualizacja:** 8 października 2025
**Wersja:** Warsztaty Notebooks 2.0

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.