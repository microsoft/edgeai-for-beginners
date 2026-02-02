# Przykład 04: Produkcyjne aplikacje czatowe z Chainlit

Kompleksowy przykład prezentujący różne podejścia do budowy gotowych do produkcji aplikacji czatowych z wykorzystaniem Microsoft Foundry Local, z nowoczesnymi interfejsami webowymi, strumieniowymi odpowiedziami i najnowszymi technologiami przeglądarkowymi.

## Co zawiera

- **🚀 Aplikacja czatowa Chainlit** (`app.py`): Gotowa do produkcji aplikacja czatowa ze strumieniowaniem
- **🌐 Demo WebGPU** (`webgpu-demo/`): Wnioskowanie AI w przeglądarce z akceleracją sprzętową
- **🎨 Integracja Open WebUI** (`open-webui-guide.md`): Profesjonalny interfejs podobny do ChatGPT
- **📚 Edukacyjny notebook** (`chainlit_app.ipynb`): Interaktywne materiały edukacyjne

## Szybki start

### 1. Aplikacja czatowa Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```
  
Otwiera się pod: `http://localhost:8080`

### 2. Demo WebGPU w przeglądarce

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```
  
Otwiera się pod: `http://localhost:5173`

### 3. Konfiguracja Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```
  
Otwiera się pod: `http://localhost:3000`

## Wzorce architektury

### Lokalny vs chmurowy - macierz decyzyjna

| Scenariusz | Rekomendacja | Powód |
|------------|--------------|-------|
| **Dane wrażliwe na prywatność** | 🏠 Lokalnie (Foundry) | Dane nigdy nie opuszczają urządzenia |
| **Złożone rozumowanie** | ☁️ Chmura (Azure OpenAI) | Dostęp do większych modeli |
| **Czat w czasie rzeczywistym** | 🏠 Lokalnie (Foundry) | Niższe opóźnienia, szybsze odpowiedzi |
| **Analiza dokumentów** | 🔄 Hybrydowo | Lokalnie dla ekstrakcji, w chmurze dla analizy |
| **Generowanie kodu** | 🏠 Lokalnie (Foundry) | Prywatność + wyspecjalizowane modele |
| **Zadania badawcze** | ☁️ Chmura (Azure OpenAI) | Potrzebna szeroka baza wiedzy |

### Porównanie technologii

| Technologia | Zastosowanie | Zalety | Wady |
|-------------|--------------|--------|------|
| **Chainlit** | Dla programistów Python, szybkie prototypowanie | Łatwa konfiguracja, wsparcie strumieniowe | Tylko Python |
| **WebGPU** | Maksymalna prywatność, scenariusze offline | Natywne dla przeglądarki, brak potrzeby serwera | Ograniczony rozmiar modelu |
| **Open WebUI** | Wdrożenia produkcyjne, zespoły | Profesjonalny interfejs, zarządzanie użytkownikami | Wymaga Dockera |

## Wymagania wstępne

- **Foundry Local**: Zainstalowany i uruchomiony ([Pobierz](https://aka.ms/foundry-local-installer))
- **Python**: Wersja 3.10+ z wirtualnym środowiskiem
- **Model**: Przynajmniej jeden załadowany (`foundry model run phi-4-mini`)
- **Przeglądarka**: Chrome/Edge z obsługą WebGPU dla demo
- **Docker**: Dla Open WebUI (opcjonalnie)

## Instalacja i konfiguracja

### 1. Konfiguracja środowiska Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
  
### 2. Konfiguracja Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```
  
## Przykładowe aplikacje

### Aplikacja czatowa Chainlit

**Funkcje:**
- 🚀 **Strumieniowanie w czasie rzeczywistym**: Tokeny pojawiają się w miarę ich generowania
- 🛡️ **Solidne zarządzanie błędami**: Łagodne degradacje i odzyskiwanie
- 🎨 **Nowoczesny interfejs**: Profesjonalny interfejs czatu od razu gotowy
- 🔧 **Elastyczna konfiguracja**: Zmienne środowiskowe i automatyczne wykrywanie
- 📱 **Responsywny design**: Działa na komputerach i urządzeniach mobilnych

**Szybki start:**  
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```
  
### Demo WebGPU w przeglądarce

**Funkcje:**
- 🌐 **Natywne AI w przeglądarce**: Brak potrzeby serwera, działa całkowicie w przeglądarce
- ⚡ **Akceleracja WebGPU**: Przyspieszenie sprzętowe, gdy dostępne
- 🔒 **Maksymalna prywatność**: Dane nigdy nie opuszczają Twojego urządzenia
- 🎯 **Zero instalacji**: Działa w każdej kompatybilnej przeglądarce
- 🔄 **Łagodne przejście**: Automatyczne przejście na CPU, jeśli WebGPU niedostępne

**Uruchamianie:**  
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```
  
### Integracja Open WebUI

**Funkcje:**
- 🎨 **Interfejs podobny do ChatGPT**: Profesjonalny, znajomy UI
- 👥 **Wsparcie dla wielu użytkowników**: Konta użytkowników i historia rozmów
- 📁 **Przetwarzanie plików**: Przesyłanie i analiza dokumentów
- 🔄 **Przełączanie modeli**: Łatwe przełączanie między różnymi modelami
- 🐳 **Wdrożenie w Dockerze**: Gotowa do produkcji konfiguracja kontenerowa

**Szybka konfiguracja:**  
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```
  
## Referencja konfiguracji

### Zmienne środowiskowe

| Zmienna | Opis | Domyślna wartość | Przykład |
|---------|------|------------------|----------|
| `MODEL` | Alias modelu do użycia | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Punkt końcowy Foundry Local | Automatyczne wykrywanie | `http://localhost:51211` |
| `API_KEY` | Klucz API (opcjonalny dla lokalnego) | `""` | `your-api-key` |

## Rozwiązywanie problemów

### Typowe problemy

**Aplikacja Chainlit:**

1. **Usługa niedostępna:**  
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```
  
2. **Konflikty portów:**  
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```
  
3. **Problemy ze środowiskiem Python:**  
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```
  
**Demo WebGPU:**

1. **Brak wsparcia dla WebGPU:**
   - Zaktualizuj do Chrome/Edge 113+
   - Włącz WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Sprawdź status GPU: `chrome://gpu`
   - Demo automatycznie przełączy się na CPU

2. **Błędy ładowania modelu:**
   - Upewnij się, że masz połączenie z internetem do pobrania modelu
   - Sprawdź konsolę przeglądarki pod kątem błędów CORS
   - Zweryfikuj, czy serwujesz przez HTTP (nie file://)

**Open WebUI:**

1. **Odmowa połączenia:**  
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```
  
2. **Modele nie pojawiają się:**  
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```
  
### Lista kontrolna walidacji

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```
  
## Zaawansowane użycie

### Optymalizacja wydajności

**Chainlit:**
- Używaj strumieniowania dla lepszej percepcji wydajności
- Implementuj pooling połączeń dla wysokiej równoczesności
- Buforuj odpowiedzi modelu dla powtarzających się zapytań
- Monitoruj użycie pamięci przy dużych historiach rozmów

**WebGPU:**
- Używaj WebGPU dla maksymalnej prywatności i szybkości
- Implementuj kwantyzację modelu dla mniejszych modeli
- Używaj Web Workers do przetwarzania w tle
- Buforuj skompilowane modele w pamięci przeglądarki

**Open WebUI:**
- Używaj trwałych woluminów dla historii rozmów
- Konfiguruj limity zasobów dla kontenera Dockera
- Implementuj strategie backupu dla danych użytkowników
- Konfiguruj reverse proxy dla zakończenia SSL

### Wzorce integracji

**Hybrydowe lokalne/chmurowe:**  
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```
  
**Pipeline wielomodalny:**  
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```
  
## Wdrożenie produkcyjne

### Rozważania dotyczące bezpieczeństwa

- **Klucze API**: Używaj zmiennych środowiskowych, nigdy nie zapisuj na stałe
- **Sieć**: Używaj HTTPS w produkcji, rozważ VPN dla dostępu zespołu
- **Kontrola dostępu**: Implementuj uwierzytelnianie dla Open WebUI
- **Prywatność danych**: Audytuj, które dane pozostają lokalne, a które trafiają do chmury
- **Aktualizacje**: Utrzymuj Foundry Local i kontenery w najnowszej wersji

### Monitorowanie i utrzymanie

- **Kontrole zdrowia**: Implementuj monitorowanie punktów końcowych
- **Logowanie**: Centralizuj logi ze wszystkich komponentów
- **Metryki**: Śledź czasy odpowiedzi, wskaźniki błędów, użycie zasobów
- **Backup**: Regularnie twórz kopie zapasowe danych rozmów i konfiguracji

## Odniesienia i zasoby

### Dokumentacja
- [Dokumentacja Chainlit](https://docs.chainlit.io/) - Kompletny przewodnik po frameworku
- [Dokumentacja Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Oficjalne dokumenty Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integracja WebGPU
- [Dokumentacja Open WebUI](https://docs.openwebui.com/) - Zaawansowana konfiguracja

### Pliki przykładowe
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produkcyjna aplikacja Chainlit
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Edukacyjny notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Wnioskowanie AI w przeglądarce
- [`open-webui-guide.md`](./open-webui-guide.md) - Kompletny przewodnik po konfiguracji Open WebUI

### Powiązane przykłady
- [Dokumentacja sesji 4](../../04.CuttingEdgeModels.md) - Kompletny przewodnik po sesji
- [Przykłady Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Oficjalne przykłady

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.