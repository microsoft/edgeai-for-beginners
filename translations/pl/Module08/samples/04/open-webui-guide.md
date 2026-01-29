# Przewodnik integracji Open WebUI + Foundry Local

Ten przewodnik pokazuje, jak połączyć Open WebUI z Microsoft Foundry Local, aby uzyskać profesjonalny interfejs podobny do ChatGPT, zasilany lokalnymi modelami AI.

## Przegląd

Open WebUI oferuje nowoczesny, przyjazny dla użytkownika interfejs czatu, który można połączyć z dowolnym API zgodnym z OpenAI. Łącząc go z Foundry Local, zyskujesz:

- **Profesjonalny interfejs**: Interfejs podobny do ChatGPT z nowoczesnym designem
- **Prywatność lokalna**: Wszystkie procesy odbywają się na Twoim urządzeniu
- **Przełączanie modeli**: Łatwe przełączanie między różnymi lokalnymi modelami
- **Historia rozmów**: Trwała historia czatu i kontekst
- **Przesyłanie plików**: Analiza dokumentów i przetwarzanie plików
- **Własne persony**: Dostosowanie systemowych podpowiedzi i ról

## Wymagania wstępne

### Wymagane oprogramowanie

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Załaduj model

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Szybka konfiguracja (zalecana)

### Krok 1: Uruchom Open WebUI za pomocą Dockera

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Krok 2: Wstępna konfiguracja

1. **Otwórz przeglądarkę**: Przejdź do `http://localhost:3000`
2. **Utwórz konto**: Skonfiguruj użytkownika admina (pierwszy użytkownik zostaje administratorem)
3. **Zweryfikuj połączenie**: Modele powinny automatycznie pojawić się w rozwijanym menu

### Krok 3: Przetestuj połączenie

1. Wybierz swój model z rozwijanego menu (np. "phi-4-mini")
2. Wpisz wiadomość testową: "Cześć! Czy możesz się przedstawić?"
3. Powinieneś zobaczyć strumieniową odpowiedź od lokalnego modelu

## Zaawansowana konfiguracja

### Zmienne środowiskowe

| Zmienna | Cel | Domyślna wartość | Przykład |
|---------|-----|------------------|----------|
| `OPENAI_API_BASE_URL` | Punkt końcowy Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Klucz API (wymagany, ale nie używany lokalnie) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Klucz szyfrowania sesji | automatycznie generowany | `your-secret-key` |
| `ENABLE_SIGNUP` | Zezwól na rejestrację nowych użytkowników | `True` | `False` |

### Konfiguracja ręczna (alternatywa)

Jeśli zmienne środowiskowe nie działają, skonfiguruj ręcznie:

1. **Otwórz ustawienia**: Kliknij ikonę ustawień (zębatka)
2. **Przejdź do połączeń**: Ustawienia → Połączenia → OpenAI
3. **Ustaw szczegóły API**:
   - Podstawowy URL API: `http://host.docker.internal:51211/v1`
   - Klucz API: `foundry-local-key` (dowolna wartość działa)
4. **Zapisz i przetestuj**: Kliknij "Zapisz", a następnie przetestuj z modelem

### Trwałe przechowywanie danych

Aby zachować rozmowy i ustawienia:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Rozwiązywanie problemów

### Problemy z połączeniem

**Problem**: "Odmowa połączenia" lub modele się nie ładują

**Rozwiązania**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Model się nie pojawia

**Problem**: Open WebUI nie pokazuje modeli w rozwijanym menu

**Kroki debugowania**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Naprawa**: Upewnij się, że model został poprawnie załadowany:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problemy z siecią Dockera

**Problem**: `host.docker.internal` nie rozwiązuje się

**Rozwiązanie dla Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Alternatywa**: Znajdź adres IP swojego urządzenia:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problemy z wydajnością

**Wolne odpowiedzi**:
1. Sprawdź, czy model korzysta z akceleracji GPU: `foundry service ps`
2. Zweryfikuj wystarczające zasoby systemowe (RAM/pamięć GPU)
3. Rozważ użycie mniejszego modelu do testów

**Problemy z pamięcią**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Przewodnik użytkowania

### Podstawowy czat

1. **Wybierz model**: Wybierz z rozwijanego menu (pokazuje modele Foundry Local)
2. **Wpisz wiadomość**: Użyj pola tekstowego na dole
3. **Wyślij**: Naciśnij Enter lub kliknij przycisk Wyślij
4. **Zobacz odpowiedź**: Zobacz strumieniową odpowiedź w czasie rzeczywistym

### Zaawansowane funkcje

**Przesyłanie plików**:
1. Kliknij ikonę spinacza
2. Prześlij dokument (PDF, TXT itp.)
3. Zadawaj pytania dotyczące treści
4. Model przeanalizuje i odpowie na podstawie dokumentu

**Własne systemowe podpowiedzi**:
1. Ustawienia → Personalizacja
2. Ustaw własną systemową podpowiedź
3. Tworzy spójne osobowości/zachowanie AI

**Zarządzanie rozmowami**:
- **Nowy czat**: Kliknij "+" aby rozpocząć nową rozmowę
- **Historia czatu**: Dostęp do poprzednich rozmów z paska bocznego
- **Eksport**: Pobierz historię czatu jako tekst/JSON

**Porównanie modeli**:
1. Otwórz wiele kart przeglądarki z tym samym Open WebUI
2. Wybierz różne modele w każdej karcie
3. Porównaj odpowiedzi na te same pytania

### Wzorce integracji

**Przepływ pracy deweloperskiej**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Wdrożenie produkcyjne

### Bezpieczna konfiguracja

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Konfiguracja dla wielu użytkowników

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Monitorowanie i logowanie

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Czyszczenie

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Kolejne kroki

### Pomysły na ulepszenia

1. **Własne modele**: Dodaj własne modele dostrojone do Foundry Local
2. **Integracja API**: Połącz z zewnętrznymi API za pomocą funkcji Open WebUI
3. **Przetwarzanie dokumentów**: Skonfiguruj zaawansowane potoki RAG
4. **Multi-modalność**: Skonfiguruj modele wizji do analizy obrazów

### Rozważania dotyczące skalowania

- **Równoważenie obciążenia**: Wiele instancji Foundry Local za reverse proxy
- **Routing modeli**: Różne modele dla różnych przypadków użycia
- **Zarządzanie zasobami**: Optymalizacja pamięci GPU dla równoczesnych użytkowników
- **Strategia kopii zapasowych**: Regularne tworzenie kopii zapasowych danych rozmów i konfiguracji

## Źródła

- [Dokumentacja Open WebUI](https://docs.openwebui.com/)
- [Repozytorium GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Dokumentacja Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Przewodnik instalacji Dockera](https://docs.docker.com/get-docker/)

---

