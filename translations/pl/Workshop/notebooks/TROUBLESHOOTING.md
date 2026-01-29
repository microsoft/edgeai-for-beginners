# Notatniki Warsztatowe - Przewodnik Rozwiązywania Problemów

## Spis Treści

- [Typowe Problemy i Rozwiązania](../../../../Workshop/notebooks)
- [Problemy Specyficzne dla Sesji 04](../../../../Workshop/notebooks)
- [Problemy Specyficzne dla Sesji 05](../../../../Workshop/notebooks)
- [Problemy Specyficzne dla Sesji 06](../../../../Workshop/notebooks)
- [Problemy Sprzętowe](../../../../Workshop/notebooks)
- [Polecenia Diagnostyczne](../../../../Workshop/notebooks)
- [Uzyskiwanie Pomocy](../../../../Workshop/notebooks)

---

## Typowe Problemy i Rozwiązania

### 🔴 CUDA Brak Pamięci

**Komunikat błędu:**
```
CUDA failure 2: out of memory
```

**Przyczyna:** GPU nie ma wystarczającej ilości VRAM, aby załadować model.

**Rozwiązania:**

#### Opcja 1: Użyj Wariantów CPU (Zalecane)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opcja 2: Użyj Mniejszych Modeli na GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opcja 3: Wyczyść Pamięć GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opcja 4: Zwiększ Pamięć GPU (jeśli to możliwe)
- Zamknij karty przeglądarki, edytory wideo lub inne aplikacje korzystające z GPU
- Zredukuj efekty wizualne w Windows
- Użyj dedykowanego GPU, jeśli masz zintegrowany + dedykowany

---

### 🔴 APIConnectionError: Błąd Połączenia

**Komunikat błędu:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Przyczyna:** Usługa Foundry Local nie działa lub jest niedostępna.

**Rozwiązania:**

#### Krok 1: Sprawdź Status Usługi
```bash
foundry service status
```

#### Krok 2: Uruchom Usługę, jeśli Zatrzymana
```bash
foundry service start
```

#### Krok 3: Zweryfikuj Punkt Końcowy
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Krok 4: Załaduj Wymagane Modele
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Krok 5: Zrestartuj Kernel Notatnika
Po uruchomieniu usługi i załadowaniu modeli, zrestartuj kernel notatnika i uruchom ponownie wszystkie komórki.

---

### 🔴 Model Nie Znaleziony w Katalogu

**Komunikat błędu:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Przyczyna:** Model nie został pobrany lub załadowany w Foundry Local.

**Rozwiązania:**

#### Opcja 1: Pobierz i Załaduj Modele
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

#### Opcja 2: Użyj Trybu Auto-Wybierania
Zaktualizuj swój CATALOG, aby używać nazw bazowych modeli (bez przyrostka `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK automatycznie wybierze najlepszy wariant (CPU, GPU lub NPU) dla Twojego sprzętu.

---

### 🔴 HttpResponseError: 500 - Nieudane Ładowanie Modelu

**Komunikat błędu:**
```
HttpResponseError: 500 - Failed loading model
```

**Przyczyna:** Plik modelu jest uszkodzony lub niekompatybilny ze sprzętem.

**Rozwiązania:**

#### Pobierz Model Ponownie
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Użyj Innego Wariantu
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Brak Modułu

**Komunikat błędu:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Przyczyna:** Pakiet foundry-local-sdk nie jest zainstalowany.

**Rozwiązania:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Wolne Pierwsze Żądanie

**Objaw:** Pierwsze ukończenie trwa ponad 30 sekund, kolejne żądania są szybkie.

**Przyczyna:** To normalne zachowanie - usługa ładuje model do pamięci przy pierwszym żądaniu.

**Rozwiązania:**

#### Wstępne Ładowanie Modeli
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Utrzymanie Usługi w Działaniu
```bash
# Start service manually and leave it running
foundry service start
```

---

## Problemy Specyficzne dla Sesji 04

### Nieprawidłowa Konfiguracja Portu

**Problem:** Notatnik łączy się z nieprawidłowym portem (55769 vs 59959 vs 57127)

**Rozwiązanie:**

1. Sprawdź, którego portu używa Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Zaktualizuj Komórkę 10 w notatniku:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Zrestartuj kernel i uruchom ponownie komórki 6, 8, 10, 12, 16, 20, 22

---

### Nieprawidłowy Wybór Modelu

**Problem:** Notatnik pokazuje gpt-oss-20b lub qwen2.5-7b zamiast qwen2.5-3b

**Rozwiązanie:**

1. Zrestartuj kernel notatnika (czyści stare zmienne)
2. Uruchom ponownie Komórkę 10 (Ustaw Alias Modelu)
3. Uruchom ponownie Komórkę 12 (Wyświetl Konfigurację)
4. **Zweryfikuj:** Komórka 12 powinna pokazywać `LLM Model: qwen2.5-3b`

---

### Niepowodzenie Komórki Diagnostycznej

**Problem:** Komórka 16 pokazuje "❌ Usługa Foundry Local nie znaleziona!"

**Rozwiązanie:**

1. Zweryfikuj, czy usługa działa:
```bash
foundry service status
```

2. Przetestuj punkt końcowy ręcznie:
```bash
curl http://localhost:59959/v1/models
```

3. Jeśli curl działa, ale notatnik nie:
   - Zrestartuj kernel notatnika
   - Uruchom komórki w kolejności: 6, 8, 10, 12, 14, 16

4. Jeśli curl nie działa:
   - Uruchom usługę: `foundry service start`
   - Załaduj modele: `foundry model run phi-4-mini` i `foundry model run qwen2.5-3b`

---

### Niepowodzenie Kontroli Przedstartowej

**Problem:** Komórka 20 pokazuje błędy połączenia, mimo że diagnostyka przeszła pomyślnie

**Rozwiązanie:**

1. Sprawdź, czy modele są załadowane:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Jeśli modele są brakujące:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Uruchom ponownie Komórkę 20 po załadowaniu modeli

---

### Niepowodzenie Porównania z Wartościami None

**Problem:** Komórka 22 kończy się, ale pokazuje opóźnienie jako None

**Rozwiązanie:**

1. Sprawdź, czy kontrola przedstartowa przeszła pomyślnie (Komórka 20)
2. Uruchom ponownie Komórkę 22 - modele mogą wymagać rozgrzania przy pierwszym żądaniu
3. Zweryfikuj, czy oba modele są załadowane: `foundry model ls`

---

## Problemy Specyficzne dla Sesji 05

### Agent Używa Nieprawidłowego Modelu

**Problem:** Agent nie używa oczekiwanego modelu

**Rozwiązanie:**

Zweryfikuj konfigurację:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Zrestartuj kernel, jeśli modele są nieprawidłowe.

---

### Przepełnienie Kontekstu Pamięci

**Problem:** Odpowiedzi agenta pogarszają się z czasem

**Rozwiązanie:** Już obsługiwane automatycznie - agenci przechowują tylko ostatnie 6 wiadomości w pamięci.

---

## Problemy Specyficzne dla Sesji 06

### Zamieszanie CPU vs GPU Model

**Problem:** Pojawiają się błędy CUDA przy użyciu domyślnej konfiguracji

**Rozwiązanie:** Domyślna konfiguracja teraz używa modeli CPU. Jeśli widzisz błędy CUDA:

1. Zweryfikuj, czy używasz domyślnego katalogu CPU:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Zrestartuj kernel i uruchom ponownie wszystkie komórki

---

### Nieprawidłowe Wykrywanie Intencji

**Problem:** Podpowiedzi są kierowane do nieprawidłowych modeli

**Rozwiązanie:**

Przetestuj wykrywanie intencji:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Zaktualizuj RULES, jeśli wzorce wymagają dostosowania.

---

## Problemy Sprzętowe

### NVIDIA GPU

**Sprawdź Status GPU:**
```bash
nvidia-smi
```

**Typowe Problemy:**
- **Przestarzały sterownik**: Zaktualizuj sterowniki NVIDIA
- **Niezgodność wersji CUDA**: Zainstaluj ponownie Foundry Local
- **Fragmentacja pamięci GPU**: Zrestartuj system

### Qualcomm NPU

**Sprawdź Status NPU:**
```bash
foundry device info
```

**Typowe Problemy:**
- **Sterowniki NPU nie zainstalowane**: Zainstaluj sterowniki Qualcomm NPU
- **Wariant NPU niedostępny**: Użyj wariantu CPU
- **Zbyt stara wersja Windows**: Zaktualizuj do najnowszego Windows 11

### Systemy Tylko CPU

**Zalecane Modele:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Wskazówki Dotyczące Wydajności:**
- Używaj najmniejszych modeli
- Zredukuj max_tokens
- Zwiększ cierpliwość przy pierwszym żądaniu

---

## Polecenia Diagnostyczne

### Sprawdź Wszystko
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

### W Pythonie
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

## Uzyskiwanie Pomocy

### 1. Sprawdź Logi
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Problemy na GitHub
- Wyszukaj istniejące problemy: https://github.com/microsoft/Foundry-Local/issues
- Utwórz nowy problem, podając:
  - Komunikat błędu (pełny tekst)
  - Wynik `foundry service status`
  - Wynik `foundry --version`
  - Informacje o GPU/NPU (nvidia-smi, itd.)
  - Kroki reprodukcji

### 3. Dokumentacja
- **Główne Repozytorium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Referencja CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Rozwiązywanie Problemów**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Lista Szybkich Napraw

Gdy coś pójdzie nie tak, spróbuj w tej kolejności:

- [ ] Sprawdź, czy usługa działa: `foundry service status`
- [ ] Zrestartuj usługę: `foundry service stop && foundry service start`
- [ ] Zweryfikuj, czy model istnieje: `foundry model ls | grep phi-4-mini`
- [ ] Załaduj wymagane modele: `foundry model run phi-4-mini`
- [ ] Sprawdź pamięć GPU: `nvidia-smi` (jeśli NVIDIA)
- [ ] Spróbuj wariantu CPU: Użyj `phi-4-mini-cpu` zamiast `phi-4-mini`
- [ ] Zrestartuj kernel notatnika
- [ ] Wyczyść wyniki notatnika i uruchom ponownie wszystkie komórki
- [ ] Zainstaluj ponownie SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Zrestartuj system (ostateczność)

---

## Wskazówki Zapobiegawcze

### Najlepsze Praktyki

1. **Zawsze najpierw sprawdzaj usługę:**
   ```bash
   foundry service status
   ```

2. **Używaj wariantów CPU domyślnie:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Wstępnie ładuj modele przed uruchomieniem notatników:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Utrzymuj usługę w działaniu:**
   - Nie zatrzymuj/uruchamiaj usługi niepotrzebnie
   - Pozwól jej działać w tle między sesjami

5. **Monitoruj zasoby:**
   - Sprawdź pamięć GPU przed uruchomieniem
   - Zamknij niepotrzebne aplikacje korzystające z GPU
   - Używaj Menedżera Zadań / nvidia-smi

6. **Aktualizuj regularnie:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Ostatnia Aktualizacja:** 8 października 2025

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.