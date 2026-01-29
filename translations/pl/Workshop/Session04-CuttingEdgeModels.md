# Sesja 4: Odkrywanie najnowszych modeli – LLM, SLM i inferencja na urządzeniu

## Streszczenie

Porównaj Duże Modele Językowe (LLM) i Małe Modele Językowe (SLM) w scenariuszach inferencji lokalnej i w chmurze. Poznaj wzorce wdrożeniowe wykorzystujące przyspieszenie ONNX Runtime, wykonanie WebGPU oraz hybrydowe doświadczenia RAG. Zawiera demonstrację Chainlit RAG z lokalnym modelem oraz opcjonalną eksplorację OpenWebUI. Zaadaptujesz starter inferencji WebGPU i ocenisz możliwości Phi w porównaniu z GPT-OSS-20B pod kątem kompromisów między kosztami a wydajnością.

## Cele nauki

- **Porównaj** SLM i LLM pod względem opóźnienia, pamięci i jakości
- **Wdróż** modele z ONNXRuntime i (gdzie obsługiwane) WebGPU
- **Uruchom** inferencję w przeglądarce (interaktywna demonstracja chroniąca prywatność)
- **Zintegruj** pipeline Chainlit RAG z lokalnym backendem SLM
- **Oceń** za pomocą lekkich heurystyk jakości i kosztów

## Wymagania wstępne

- Ukończone sesje 1–3
- Zainstalowany `chainlit` (już w `requirements.txt` dla Module08)
- Przeglądarka obsługująca WebGPU (Edge / Chrome najnowsza wersja na Windows 11)
- Działający Foundry Local (`foundry service status`)

### Uwagi dotyczące różnych platform

Windows pozostaje głównym środowiskiem docelowym. Dla deweloperów macOS oczekujących na natywne binaria:
1. Uruchom Foundry Local w maszynie wirtualnej Windows 11 (Parallels / UTM) LUB na zdalnej stacji roboczej Windows.
2. Udostępnij usługę (domyślny port 5273) i skonfiguruj na macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Użyj tych samych kroków konfiguracji wirtualnego środowiska Python co w poprzednich sesjach.

Instalacja Chainlit (obie platformy):
```bash
pip install chainlit
```

## Przebieg demonstracji (30 min)

### 1. Porównanie Phi (SLM) i GPT-OSS-20B (LLM) (6 min)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Śledź: głębokość odpowiedzi, dokładność faktów, bogactwo stylistyczne, opóźnienie.

Obserwuj zmiany przepustowości po włączeniu GPU w porównaniu z samym CPU.

### 3. Inferencja WebGPU w przeglądarce (6 min)

Zaadaptuj starter `04-webgpu-inference` (utwórz `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Otwórz plik w przeglądarce; obserwuj lokalny cykl zwrotny o niskim opóźnieniu.

### 4. Aplikacja czatu Chainlit RAG (7 min)

Minimalny `samples/04-cutting-edge/chainlit_app.py`:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Uruchom:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Projekt startowy: Adaptacja `04-webgpu-inference` (6 min)

Rezultaty:
- Zastąp logikę pobierania placeholdera strumieniowymi tokenami (użyj wariantu endpointu `stream=True`, gdy będzie dostępny)
- Dodaj wykres opóźnienia (po stronie klienta) dla przełączania między phi a gpt-oss-20b
- Osadź kontekst RAG inline (textarea dla dokumentów referencyjnych)

## Heurystyki oceny

| Kategoria | Phi-4-mini | GPT-OSS-20B | Obserwacja |
|-----------|------------|-------------|------------|
| Opóźnienie (zimny start) | Szybkie | Wolniejsze | SLM szybko się rozgrzewa |
| Pamięć | Niska | Wysoka | Możliwość na urządzeniu |
| Zgodność z kontekstem | Dobra | Silna | Większy model może być bardziej rozbudowany |
| Koszt (lokalny) | Minimalny | Wyższy (zasoby) | Kompromis energia/czas |
| Najlepsze zastosowanie | Aplikacje na urządzenia | Głębokie rozumowanie | Możliwy hybrydowy pipeline |

## Walidacja środowiska

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Rozwiązywanie problemów

| Objaw | Przyczyna | Działanie |
|-------|----------|-----------|
| Nieudane pobieranie strony | CORS lub usługa nie działa | Użyj `curl`, aby zweryfikować endpoint; włącz proxy CORS, jeśli potrzebne |
| Pusty Chainlit | Środowisko nieaktywne | Aktywuj venv i ponownie zainstaluj zależności |
| Wysokie opóźnienie | Model właśnie załadowany | Rozgrzej krótką sekwencją podpowiedzi |

## Źródła

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Dokumentacja Chainlit: https://docs.chainlit.io
- Ocena RAG (Ragas): https://docs.ragas.io

---

**Czas trwania sesji**: 30 min  
**Poziom trudności**: Zaawansowany

## Przykładowy scenariusz i mapowanie warsztatów

| Artefakty warsztatowe | Scenariusz | Cel | Źródło danych / podpowiedzi |
|------------------------|-----------|-----|-----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Zespół architektury oceniający SLM i LLM dla generatora podsumowań dla kadry kierowniczej | Ilościowe porównanie opóźnienia + różnicy w użyciu tokenów | Pojedyncza zmienna środowiskowa `COMPARE_PROMPT` |
| `chainlit_app.py` (demo RAG) | Prototyp asystenta wiedzy wewnętrznej | Ugruntowanie krótkich odpowiedzi przy minimalnym wyszukiwaniu leksykalnym | Lista `DOCS` w pliku |
| `webgpu_demo.html` | Futurystyczny podgląd inferencji w przeglądarce na urządzeniu | Pokaz lokalnego cyklu zwrotnego o niskim opóźnieniu + narracja UX | Tylko bieżące podpowiedzi użytkownika |

### Narracja scenariusza
Organizacja produktowa chce generatora podsumowań dla kadry kierowniczej. Lekki SLM (phi‑4‑mini) tworzy szkice podsumowań; większy LLM (gpt‑oss‑20b) może je udoskonalać tylko dla raportów o wysokim priorytecie. Skrypty sesji rejestrują empiryczne opóźnienia i metryki tokenów, aby uzasadnić hybrydowy projekt, podczas gdy demo Chainlit ilustruje, jak ugruntowane wyszukiwanie utrzymuje odpowiedzi małego modelu jako faktyczne. Strona koncepcyjna WebGPU zapewnia wizję pełnego przetwarzania po stronie klienta, gdy przyspieszenie przeglądarki dojrzeje.

### Minimalny kontekst RAG (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Hybrydowy przepływ Szkic→Udoskonalenie (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Śledź oba komponenty opóźnienia, aby zgłosić średni koszt mieszany.

### Opcjonalne ulepszenia

| Skupienie | Ulepszenie | Dlaczego | Wskazówka dotycząca implementacji |
|-----------|------------|----------|-----------------------------------|
| Metryki porównawcze | Śledzenie użycia tokenów + opóźnienia pierwszego tokena | Holistyczny widok wydajności | Użyj ulepszonego skryptu benchmarkowego (Sesja 3) z `BENCH_STREAM=1` |
| Hybrydowy pipeline | Szkic SLM → Udoskonalenie LLM | Redukcja opóźnienia i kosztów | Generuj za pomocą phi-4-mini, udoskonal podsumowanie za pomocą gpt-oss-20b |
| Interfejs użytkownika strumieniowego | Lepszy UX w Chainlit | Informacje zwrotne w czasie rzeczywistym | Użyj `stream=True`, gdy lokalne strumieniowanie będzie dostępne; gromadź fragmenty |
| Buforowanie WebGPU | Szybsza inicjalizacja JS | Redukcja kosztów rekompilacji | Buforuj skompilowane artefakty shaderów (przyszła funkcjonalność runtime) |
| Deterministyczny zestaw QA | Uczciwe porównanie modeli | Eliminacja zmienności | Stała lista podpowiedzi + `temperature=0` dla uruchomień oceny |
| Ocena wyników | Strukturalna perspektywa jakości | Wyjście poza anegdoty | Prosta rubryka: spójność / faktualność / zwięzłość (1–5) |
| Uwagi dotyczące energii / zasobów | Dyskusja w klasie | Pokazanie kompromisów | Użyj monitorów systemowych (Task Manager, `nvidia-smi`) + wyniki skryptu benchmarkowego |
| Symulacja kosztów | Uzasadnienie przed chmurą | Planowanie skalowania | Mapuj tokeny na hipotetyczne ceny w chmurze dla narracji TCO |
| Rozkład opóźnienia | Identyfikacja wąskich gardeł | Cel optymalizacji | Mierz przygotowanie podpowiedzi, wysyłanie żądań, pierwszy token, pełne zakończenie |
| RAG + LLM jako zapas | Sieć bezpieczeństwa jakości | Poprawa trudnych zapytań | Jeśli długość odpowiedzi SLM < próg lub niska pewność → eskalacja |

#### Przykładowy wzorzec hybrydowy Szkic/Udoskonalenie

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Szkic rozkładu opóźnienia

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Użyj spójnych ram pomiarowych dla modeli, aby zapewnić uczciwe porównania.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->