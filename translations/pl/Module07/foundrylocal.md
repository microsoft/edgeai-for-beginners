# Foundry Local na Windows i Mac

Ten przewodnik pomoże Ci zainstalować, uruchomić i zintegrować Microsoft Foundry Local na Windows i Mac. Wszystkie kroki i polecenia zostały zweryfikowane zgodnie z dokumentacją Microsoft Learn.

- Rozpocznij: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referencje CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integracja SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilacja modeli HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokalnie vs Chmura: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalacja / Aktualizacja na Windows

- Instalacja:
```cmd
winget install Microsoft.FoundryLocal
```
- Aktualizacja:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Sprawdzenie wersji:
```cmd
foundry --version
```
     
**Instalacja / Mac**

**MacOS**: 
Otwórz terminal i uruchom następujące polecenie:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Podstawy CLI (Trzy Kategorie)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Usługa:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Uwagi:
- Usługa udostępnia REST API kompatybilne z OpenAI. Port punktu końcowego jest dynamicznie przydzielany; użyj `foundry service status`, aby go odkryć.
- Korzystaj z SDK dla wygody; automatycznie obsługują odkrywanie punktów końcowych tam, gdzie jest to wspierane.

## 3) Odkrywanie lokalnego punktu końcowego (Dynamiczny Port)

Foundry Local przydziela dynamiczny port za każdym razem, gdy usługa jest uruchamiana:
```cmd
foundry service status
```
Użyj zgłoszonego `http://localhost:<PORT>` jako swojego `base_url` z kompatybilnymi ścieżkami OpenAI (na przykład `/v1/chat/completions`).

## 4) Szybki test za pomocą OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Referencje:
- Integracja SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Własny model (Kompilacja za pomocą Olive)

Jeśli potrzebujesz modelu, którego nie ma w katalogu, skompiluj go do ONNX dla Foundry Local za pomocą Olive.

Ogólny przepływ (zobacz dokumentację dla szczegółowych kroków):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentacja:
- Kompilacja BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Rozwiązywanie problemów

- Sprawdź status usługi i logi:
```cmd
foundry service status
foundry service diag
```
- Wyczyść lub przenieś cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Aktualizuj do najnowszej wersji preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Powiązane doświadczenia deweloperskie na Windows

- Wybory AI lokalnie vs w chmurze na Windows, w tym Foundry Local i Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit z Foundry Local (użyj `foundry service status`, aby uzyskać URL punktu końcowego czatu):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Next Windows Developer](./windowdeveloper.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.