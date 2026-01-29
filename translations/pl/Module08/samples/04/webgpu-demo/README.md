# WebGPU + ONNX Runtime Demo

Ten pokaz demonstruje, jak uruchamiać modele AI bezpośrednio w przeglądarce, wykorzystując WebGPU do przyspieszenia sprzętowego oraz ONNX Runtime Web.

## Co Ten Pokaz Demonstruje

- **AI w przeglądarce**: Uruchamianie modeli całkowicie w przeglądarce
- **Przyspieszenie WebGPU**: Wykorzystanie sprzętowego przyspieszenia, gdy jest dostępne
- **Prywatność**: Żadne dane nie opuszczają Twojego urządzenia
- **Bez instalacji**: Działa w każdej kompatybilnej przeglądarce
- **Płynne przejście**: Automatyczne przejście na CPU, jeśli WebGPU jest niedostępne

## Wymagania

**Kompatybilność przeglądarki:**
- Chrome/Edge 113+ z włączonym WebGPU
- Sprawdź status WebGPU: `chrome://gpu`
- Włącz WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Uruchamianie Pokazu

### Opcja 1: Lokalny serwer (zalecane)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opcja 2: Live Server w VS Code

1. Zainstaluj rozszerzenie "Live Server" w VS Code
2. Kliknij prawym przyciskiem na `index.html` → "Open with Live Server"
3. Pokaz otworzy się automatycznie w przeglądarce

## Co Zobaczysz

1. **Wykrywanie WebGPU**: Sprawdza kompatybilność przeglądarki
2. **Ładowanie modelu**: Pobiera i inicjalizuje klasyfikator MNIST
3. **Wykonanie inferencji**: Przeprowadza predykcję na danych testowych
4. **Metryki wydajności**: Wyświetla czas ładowania i szybkość inferencji
5. **Wyświetlanie wyników**: Pewność predykcji i surowe wyniki

## Oczekiwana Wydajność

| Dostawca wykonania | Ładowanie modelu | Inferencja | Uwagi |
|-------------------|------------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Przyspieszenie sprzętowe |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Fallback programowy |

## Rozwiązywanie Problemów

**WebGPU Niedostępne:**
- Zaktualizuj do Chrome/Edge 113+
- Włącz WebGPU w `chrome://flags`
- Sprawdź, czy sterowniki GPU są aktualne
- Pokaz automatycznie przejdzie na CPU

**Błędy ładowania:**
- Upewnij się, że serwujesz przez HTTP (nie file://)
- Sprawdź połączenie sieciowe dla pobierania modelu
- Zweryfikuj, czy CORS nie blokuje modelu ONNX

**Problemy z wydajnością:**
- WebGPU zapewnia znaczące przyspieszenie w porównaniu do CPU
- Pierwsze uruchomienie może być wolniejsze z powodu pobierania modelu
- Kolejne uruchomienia korzystają z pamięci podręcznej przeglądarki

## Integracja z Foundry Local

Ten pokaz WebGPU uzupełnia Foundry Local, pokazując:

- **Inferencję po stronie klienta** dla maksymalnej prywatności
- **Możliwości offline** w przypadku braku internetu  
- **Wdrożenia na krawędzi** dla środowisk o ograniczonych zasobach
- **Architektury hybrydowe** łączące inferencję lokalną i serwerową

Dla aplikacji produkcyjnych warto rozważyć:
- Wykorzystanie Foundry Local do inferencji po stronie serwera
- Wykorzystanie WebGPU do wstępnego przetwarzania/obróbki po stronie klienta
- Implementację inteligentnego routingu między inferencją lokalną a zdalną

## Szczegóły Techniczne

**Używany model:**
- Klasyfikator cyfr MNIST (format ONNX)
- Wejście: obrazy w skali szarości 28x28
- Wyjście: rozkład prawdopodobieństwa dla 10 klas
- Rozmiar: ~500KB (szybkie pobieranie)

**ONNX Runtime Web:**
- Dostawca wykonania WebGPU dla przyspieszenia GPU
- Dostawca wykonania WASM dla fallbacku CPU
- Automatyczna optymalizacja i optymalizacja grafu

**API przeglądarki:**
- WebGPU dla dostępu do sprzętu
- Web Workers dla przetwarzania w tle (planowane ulepszenie)
- WebAssembly dla efektywnych obliczeń

## Kolejne Kroki

- Wypróbuj z własnymi modelami ONNX
- Zaimplementuj przesyłanie rzeczywistych obrazów i klasyfikację
- Dodaj inferencję strumieniową dla większych modeli
- Zintegruj z wejściem z kamery/mikrofonu

---

