# Sesja 6: Foundry Local – Modele jako narzędzia

## Streszczenie

Traktuj modele jako modułowe narzędzia w lokalnej warstwie operacyjnej AI. W tej sesji dowiesz się, jak łączyć wiele wyspecjalizowanych wywołań SLM/LLM, selektywnie kierować zadania i udostępniać zunifikowaną powierzchnię SDK dla aplikacji. Zbudujesz lekki router modeli + planista zadań, zintegrujesz go ze skryptem aplikacji i nakreślisz ścieżkę skalowania do Azure AI Foundry dla obciążeń produkcyjnych.

## Cele nauki

- **Zrozumienie** modeli jako atomowych narzędzi z zadeklarowanymi możliwościami
- **Kierowanie** żądań na podstawie intencji / heurystycznego oceniania
- **Łączenie** wyników w wieloetapowych zadaniach (rozłożenie → rozwiązanie → dopracowanie)
- **Integracja** zunifikowanego API klienta dla aplikacji końcowych
- **Skalowanie** projektu do chmury (zgodność z kontraktem OpenAI)

## Wymagania wstępne

- Ukończone sesje 1–5
- Wiele lokalnych modeli w pamięci podręcznej (np. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Fragment środowiska wieloplatformowego

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Zdalny dostęp / dostęp do usługi VM z macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Przebieg demonstracji (30 min)

### 1. Deklaracja możliwości narzędzi (5 min)

Utwórz `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Wykrywanie intencji i kierowanie (8 min)

Utwórz `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Łączenie zadań wieloetapowych (7 min)

Utwórz `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Projekt początkowy: Dostosowanie `06-models-as-tools` (5 min)

Ulepszenia:
- Dodaj obsługę strumieniowania tokenów (progresywna aktualizacja interfejsu użytkownika)
- Dodaj ocenę pewności: nakładanie się leksykalne lub rubryka podpowiedzi
- Eksportuj ślad JSON (intencja → model → opóźnienie → użycie tokenów)
- Wprowadź ponowne użycie pamięci podręcznej dla powtarzających się podzadań

### 5. Ścieżka skalowania do Azure (5 min)

| Warstwa | Lokalnie (Foundry) | Chmura (Azure AI Foundry) | Strategia przejścia |
|---------|--------------------|---------------------------|---------------------|
| Kierowanie | Heurystyka w Pythonie | Trwała mikrousługa | Konteneryzacja i wdrożenie API |
| Modele | SLM w pamięci podręcznej | Zarządzane wdrożenia | Mapowanie lokalnych nazw na identyfikatory wdrożeń |
| Obserwowalność | Statystyki CLI/ręczne | Centralne logowanie i metryki | Dodanie strukturalnych zdarzeń śledzenia |
| Bezpieczeństwo | Tylko host lokalny | Autoryzacja Azure / sieć | Wprowadzenie sejfu kluczy dla tajemnic |
| Koszty | Zasoby urządzenia | Rozliczanie zużycia | Dodanie ograniczeń budżetowych |

## Lista kontrolna walidacji

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Oczekuj wyboru modelu na podstawie intencji i ostatecznego dopracowanego wyniku.

## Rozwiązywanie problemów

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Wszystkie zadania kierowane do tego samego modelu | Słabe reguły | Wzbogacenie zestawu regex INTENT_RULES |
| Pipeline zawodzi w połowie kroku | Brak załadowanego modelu | Uruchom `foundry model run <model>` |
| Niska spójność wyników | Brak fazy dopracowania | Dodaj etap podsumowania/walidacji |

## Źródła

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentacja Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Wzorce jakości podpowiedzi: Zobacz Sesję 2

---

**Czas trwania sesji**: 30 min  
**Poziom trudności**: Zaawansowany

## Przykładowy scenariusz i mapowanie warsztatów

| Skrypty warsztatowe / Notatniki | Scenariusz | Cel | Źródło danych / katalogu |
|---------------------------------|------------|-----|--------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Asystent programisty obsługujący mieszane podpowiedzi intencji (refaktoryzacja, podsumowanie, klasyfikacja) | Heurystyczne kierowanie intencji → alias modelu z użyciem tokenów | Wbudowany `CATALOG` + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Wieloetapowe planowanie i dopracowanie dla złożonego zadania wsparcia kodowania | Rozłożenie → wyspecjalizowane wykonanie → etap dopracowania podsumowania | Ten sam `CATALOG`; kroki wywodzące się z wyniku planowania |

### Narracja scenariusza
Narzędzie zwiększające produktywność inżynierów otrzymuje zróżnicowane zadania: refaktoryzacja kodu, podsumowanie notatek architektonicznych, klasyfikacja opinii. Aby zminimalizować opóźnienia i zużycie zasobów, mały ogólny model planuje i podsumowuje, model wyspecjalizowany w kodzie zajmuje się refaktoryzacją, a lekki model zdolny do klasyfikacji etykietuje opinie. Skrypt pipeline demonstruje łączenie + dopracowanie; skrypt routera izoluje adaptacyjne kierowanie pojedynczymi podpowiedziami.

### Migawka katalogu
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Przykładowe podpowiedzi testowe
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Rozszerzenie śladu (opcjonalne)
Dodaj linie JSON śladu dla każdego kroku w `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heurystyka eskalacji (pomysł)
Jeśli plan zawiera słowa kluczowe, takie jak "optymalizacja", "bezpieczeństwo" lub długość kroku > 280 znaków → eskaluj do większego modelu (np. `gpt-oss-20b`) tylko dla tego kroku.

### Opcjonalne ulepszenia

| Obszar | Ulepszenie | Wartość | Wskazówka |
|--------|------------|---------|-----------|
| Pamięć podręczna | Ponowne użycie obiektów menedżera + klienta | Niższe opóźnienia, mniejsze obciążenie | Użyj `workshop_utils.get_client` |
| Metryki użycia | Rejestracja tokenów i opóźnień na krok | Profilowanie i optymalizacja | Mierz czas każdego wywołania; przechowuj w liście śladów |
| Adaptacyjne kierowanie | Świadomość pewności / kosztów | Lepszy kompromis jakość-koszt | Dodaj ocenę: jeśli podpowiedź > N znaków lub regex pasuje do domeny → eskaluj do większego modelu |
| Dynamiczny rejestr możliwości | Gorące przeładowanie katalogu | Brak konieczności ponownego uruchamiania | Ładuj `catalog.json` w czasie rzeczywistym; monitoruj znacznik czasu pliku |
| Strategia awaryjna | Odporność na awarie | Wyższa dostępność | Spróbuj głównego → w przypadku wyjątku alias awaryjny |
| Pipeline strumieniowy | Wczesna informacja zwrotna | Poprawa UX | Strumieniuj każdy krok i buforuj dane wejściowe do ostatecznego dopracowania |
| Wektory intencji | Bardziej precyzyjne kierowanie | Wyższa dokładność intencji | Osadź podpowiedź, grupuj i mapuj centroid → możliwość |
| Eksport śladu | Audytowalny łańcuch | Zgodność/sprawozdawczość | Emituj linie JSON: krok, intencja, model, latency_ms, tokeny |
| Symulacja kosztów | Szacowanie przed wdrożeniem w chmurze | Planowanie budżetu | Przypisz koszt/token dla modelu i agreguj na zadanie |
| Tryb deterministyczny | Powtarzalność testów | Stabilne benchmarki | Env: `temperature=0`, stała liczba kroków |

#### Przykład struktury śladu

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Szkic adaptacyjnej eskalacji

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Gorące przeładowanie katalogu modeli

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.