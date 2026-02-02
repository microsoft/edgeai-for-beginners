# Windows 11 Chat Sample - Foundry Local

Nowoczesna aplikacja czatu dla Windows 11, integrująca Microsoft Foundry Local z pięknym, natywnym interfejsem. Zbudowana przy użyciu Electron i zgodnie z oficjalnymi wzorcami Foundry Local od Microsoftu.

## Przegląd

Ten przykład pokazuje, jak stworzyć gotową do produkcji aplikację czatu, która wykorzystuje lokalne modele AI za pośrednictwem Foundry Local, oferując użytkownikom rozmowy z AI skoncentrowane na prywatności, bez zależności od chmury.

## Funkcje

### 🎨 **Natywny design Windows 11**
- Integracja z Fluent Design System
- Efekty materiału Mica i przezroczystość
- Obsługa natywnego motywu Windows 11
- Responsywny układ dla wszystkich rozmiarów ekranów
- Automatyczne przełączanie trybu jasnego/ciemnego

### 🤖 **Integracja modeli AI**
- Integracja z usługą Foundry Local
- Obsługa wielu modeli z możliwością szybkiego przełączania
- Odpowiedzi w czasie rzeczywistym
- Przełączanie między modelami lokalnymi i chmurowymi
- Monitorowanie stanu i kondycji modeli

### 💬 **Doświadczenie czatu**
- Wskaźniki pisania w czasie rzeczywistym
- Zachowanie historii wiadomości
- Eksportowanie rozmów czatu
- Niestandardowe systemowe podpowiedzi
- Rozgałęzianie i zarządzanie rozmowami

### ⚡ **Funkcje wydajnościowe**
- Lazy loading i wirtualizacja
- Optymalizacja renderowania dla długich rozmów
- Wstępne ładowanie modeli w tle
- Efektywne zarządzanie pamięcią
- Płynne animacje i przejścia

## Architektura

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## Wymagania wstępne

### Wymagania systemowe
- **OS**: Windows 11 (zalecana wersja 22H2 lub nowsza)
- **RAM**: Minimum 8GB, zalecane 16GB+ dla większych modeli
- **Storage**: Minimum 10GB wolnego miejsca na modele
- **GPU**: Opcjonalne, ale zalecane dla szybszego wnioskowania

### Wymagania dotyczące oprogramowania
- **Node.js**: v18.0.0 lub nowsza
- **Foundry Local**: Najnowsza wersja od Microsoftu
- **Git**: Do klonowania i rozwoju

## Instalacja

### 1. Zainstaluj Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Sklonuj i skonfiguruj
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Skonfiguruj środowisko
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Uruchom aplikację
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Struktura projektu

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## Szczegółowe omówienie funkcji

### Integracja z Windows 11

**Fluent Design System**
- Materiały tła Mica
- Efekty przezroczystości Acrylic
- Zaokrąglone rogi i nowoczesne odstępy
- Natywna paleta kolorów Windows 11
- Semantyczne tokeny kolorów dla dostępności

**Natywne funkcje Windows**
- Integracja listy szybkiego dostępu dla ostatnich czatów
- Powiadomienia Windows o nowych wiadomościach
- Postęp na pasku zadań dla operacji modelu
- Integracja z zasobnikiem systemowym z szybkimi akcjami
- Obsługa uwierzytelniania Windows Hello

### Zarządzanie modelami AI

**Modele lokalne**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Obsługa hybrydowa chmura/lokal**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Funkcje interfejsu czatu

**Streaming w czasie rzeczywistym**
- Wyświetlanie odpowiedzi token po tokenie
- Płynne animacje pisania
- Możliwość anulowania żądań
- Wskaźniki pisania i status

**Zarządzanie rozmowami**
- Zachowanie historii czatu
- Eksport/import rozmów
- Wyszukiwanie i filtrowanie wiadomości
- Rozgałęzianie rozmów
- Niestandardowe systemowe podpowiedzi dla każdej rozmowy

**Dostępność**
- Pełna nawigacja za pomocą klawiatury
- Kompatybilność z czytnikami ekranu
- Obsługa trybu wysokiego kontrastu
- Możliwość dostosowania rozmiaru czcionek
- Integracja wejścia głosowego

## Przykłady użycia

### Podstawowa integracja czatu
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Zarządzanie modelami
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Ustawienia i personalizacja
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## Opcje konfiguracji

### Ustawienia aplikacji
- **Motyw**: Automatyczny, jasny, ciemny tryb
- **Model**: Domyślny wybór modelu
- **Wydajność**: Ustawienia wnioskowania
- **Prywatność**: Polityki przechowywania danych
- **Powiadomienia**: Alerty wiadomości
- **Skróty**: Skróty klawiaturowe

### Ustawienia czatu
- **Streaming**: Włącz/wyłącz odpowiedzi w czasie rzeczywistym
- **Długość kontekstu**: Pamięć rozmowy
- **Temperatura**: Kreatywność odpowiedzi
- **Maksymalna liczba tokenów**: Limity długości odpowiedzi
- **Systemowe podpowiedzi**: Domyślne zachowanie asystenta

### Ustawienia modelu
- **Automatyczne pobieranie**: Automatyczne aktualizacje modeli
- **Rozmiar pamięci podręcznej**: Limity lokalnego przechowywania modeli
- **Tryb wydajności**: Preferencje CPU vs GPU
- **Kontrole kondycji**: Interwały monitorowania

## Rozwój

### Budowanie ze źródła
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Debugowanie
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Testowanie
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optymalizacja wydajności

### Zarządzanie pamięcią
- Efektywna wirtualizacja wiadomości
- Automatyczne zbieranie śmieci
- Monitorowanie pamięci modelu
- Czyszczenie zasobów przy zamykaniu

### Optymalizacja renderowania
- Wirtualne przewijanie dla długich rozmów
- Lazy loading historii wiadomości
- Optymalizacja aktualizacji React/DOM
- Animacje przyspieszane przez GPU

### Optymalizacja sieci
- Grupowanie połączeń
- Grupowanie żądań
- Automatyczna logika ponawiania
- Obsługa trybu offline

## Rozważania dotyczące bezpieczeństwa

### Prywatność danych
- Architektura lokalna jako priorytet
- Brak transmisji danych do chmury (tryb lokalny)
- Szyfrowane przechowywanie rozmów
- Bezpieczne zarządzanie poświadczeniami

### Bezpieczeństwo aplikacji
- Procesy renderowania w sandboxie
- Polityka bezpieczeństwa treści (CSP)
- Brak zdalnego wykonywania kodu
- Bezpieczna komunikacja IPC

## Rozwiązywanie problemów

### Typowe problemy

**Foundry Local nie uruchamia się**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Problemy z ładowaniem modeli**
- Sprawdź wystarczającą ilość miejsca na dysku
- Zweryfikuj połączenie internetowe dla pobrań
- Upewnij się, że sterowniki GPU są aktualne
- Wypróbuj różne warianty modeli

**Problemy z wydajnością**
- Monitoruj zasoby systemowe
- Dostosuj ustawienia modelu
- Włącz akcelerację sprzętową
- Zamknij inne aplikacje obciążające zasoby

### Tryb debugowania
Włącz logowanie debugowania, ustawiając zmienne środowiskowe:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Wkład w projekt

### Konfiguracja rozwoju
1. Sforkuj repozytorium
2. Utwórz gałąź funkcji
3. Zainstaluj zależności: `npm install`
4. Wprowadź zmiany i przetestuj
5. Prześlij pull request

### Styl kodu
- Dostarczona konfiguracja ESLint
- Prettier do formatowania kodu
- TypeScript dla bezpieczeństwa typów
- Komentarze JSDoc dla dokumentacji

## Efekty nauki

Po ukończeniu tego przykładu zrozumiesz:

1. **Natywny rozwój dla Windows 11**
   - Implementacja Fluent Design System
   - Integracja z Windows
   - Najlepsze praktyki bezpieczeństwa Electron

2. **Integracja modeli AI**
   - Architektura usługi Foundry Local
   - Zarządzanie cyklem życia modelu
   - Monitorowanie wydajności i optymalizacja

3. **Systemy czatu w czasie rzeczywistym**
   - Obsługa odpowiedzi strumieniowych
   - Zarządzanie stanem rozmowy
   - Wzorce doświadczenia użytkownika

4. **Rozwój aplikacji produkcyjnych**
   - Obsługa błędów i odzyskiwanie
   - Optymalizacja wydajności
   - Rozważania dotyczące bezpieczeństwa
   - Strategie testowania

## Kolejne kroki

- **Przykład 09**: System orkiestracji wieloagentowej
- **Przykład 10**: Foundry Local jako integracja narzędzi
- **Zaawansowane tematy**: Dostosowywanie modeli
- **Wdrożenie**: Wzorce wdrożenia dla przedsiębiorstw

## Licencja

Ten przykład podlega tej samej licencji co projekt Microsoft Foundry Local.

---

