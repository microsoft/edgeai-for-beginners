# Moduł 08 Przykłady: Przewodnik po lokalnym rozwoju Foundry

## Przegląd

Ta kompleksowa kolekcja prezentuje podejścia zarówno **Foundry Local SDK**, jak i **Shell Command** do tworzenia gotowych do produkcji aplikacji AI. Każdy przykład ukazuje różne aspekty rozwoju AI na urządzeniach brzegowych, od podstawowej integracji REST po zaawansowane systemy wieloagentowe.

## Podejście do rozwoju: SDK vs Polecenia Shell

### Używaj Foundry Local SDK, gdy:

- **Kontrola programowa**: Potrzebujesz pełnej kontroli nad cyklem życia agenta, oceną lub procesami wdrożeniowymi
- **Niestandardowe narzędzia**: Tworzysz automatyzację wokół Foundry Local (integracja CI/CD, orkiestracja wieloagentowa)
- **Dostęp szczegółowy**: Wymagasz szczegółowych danych o agencie, wersjonowania lub kontroli nad narzędziami oceny
- **Integracja z Pythonem**: Pracujesz w środowiskach silnie opartych na Pythonie lub wbudowujesz logikę Foundry w szersze aplikacje
- **Przepływy pracy w przedsiębiorstwie**: Wdrażasz modularne przepływy pracy i powtarzalne procesy oceny zgodne z architekturami referencyjnymi Microsoft

### Używaj poleceń Shell, gdy:

- **Szybkie testowanie**: Przeprowadzasz szybkie lokalne testy, ręczne uruchamianie agentów lub weryfikację konfiguracji
- **Prostota CLI**: Potrzebujesz prostych operacji CLI do uruchamiania/zatrzymywania agentów, sprawdzania logów lub podstawowych ocen
- **Lekka automatyzacja**: Tworzysz proste skrypty automatyzacji bez wymagań pełnej integracji SDK
- **Szybka iteracja**: Debugowanie i cykle rozwoju, szczególnie w ograniczonych środowiskach lub wdrożeniach na poziomie grupy zasobów
- **Konfiguracja i weryfikacja**: Początkowa konfiguracja środowiska i szybkie zadania weryfikacyjne

## Najlepsze praktyki i zalecany przepływ pracy

Na podstawie zarządzania cyklem życia agenta, śledzenia zależności i zasad powtarzalności z minimalnymi uprawnieniami:

### Faza 1: Podstawy i konfiguracja
1. **Rozpocznij od poleceń Shell** dla początkowej konfiguracji i szybkiej weryfikacji
2. **Zweryfikuj środowisko** za pomocą narzędzi CLI i podstawowego wdrożenia modelu
3. **Przetestuj łączność** za pomocą prostych wywołań REST i kontroli stanu

### Faza 2: Rozwój i integracja
1. **Przejdź do SDK** dla skalowalnych, śledzonych przepływów pracy
2. **Wprowadź kontrolę programową** dla złożonych interakcji agentów
3. **Twórz niestandardowe narzędzia** dla szablonów gotowych dla społeczności i integracji Azure OpenAI

### Faza 3: Produkcja i skalowanie
1. **Podejście hybrydowe** łączące CLI dla operacji i SDK dla logiki aplikacji
2. **Integracja w przedsiębiorstwie** z monitorowaniem, logowaniem i pipeline'ami wdrożeniowymi
3. **Wkład społecznościowy** poprzez wielokrotnego użytku szablony i najlepsze praktyki

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.