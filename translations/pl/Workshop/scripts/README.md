# Skrypty Warsztatowe

Ten katalog zawiera skrypty automatyzacji i wsparcia używane do utrzymania jakości i spójności materiałów warsztatowych.

## Zawartość

| Plik | Cel |
|------|-----|
| `lint_markdown_cli.py` | Sprawdza poprawność bloków kodu markdown, aby zablokować przestarzałe wzorce poleceń Foundry Local CLI. |
| `export_benchmark_markdown.py` | Przeprowadza testy wydajności dla wielu modeli i generuje raporty w formacie Markdown + JSON. |

## 1. Linter wzorców Markdown CLI

`lint_markdown_cli.py` skanuje wszystkie pliki `.md`, które nie są tłumaczeniami, w poszukiwaniu niedozwolonych wzorców Foundry Local CLI **wewnątrz bloków kodu** (``` ... ```). Informacyjny tekst może nadal wspominać o przestarzałych poleceniach w celach historycznych.

### Przestarzałe wzorce (zablokowane wewnątrz bloków kodu)

Linter blokuje przestarzałe wzorce CLI. Zamiast nich należy używać nowoczesnych alternatyw.

### Wymagane zamienniki
| Przestarzałe | Użyj zamiast |
|--------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Skrypt benchmark + narzędzia systemowe (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Kody wyjścia
| Kod | Znaczenie |
|-----|-----------|
| 0 | Nie wykryto naruszeń |
| 1 | Wykryto jeden lub więcej przestarzałych wzorców |

### Uruchamianie lokalne
Z katalogu głównego repozytorium (zalecane):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hak przed zatwierdzeniem (opcjonalne)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Blokuje zatwierdzenia wprowadzające przestarzałe wzorce.

### Integracja z CI
Workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) uruchamia linter przy każdym pushu i pull request do gałęzi `main` i `Reactor`. Niepowodzenia muszą zostać naprawione przed scaleniem.

### Dodawanie nowych przestarzałych wzorców
1. Otwórz `lint_markdown_cli.py`.
2. Dodaj krotkę `(regex, suggestion)` do listy `DEPRECATED`. Użyj surowego ciągu znaków i uwzględnij granice słów `\b`, jeśli to konieczne.
3. Uruchom linter lokalnie, aby zweryfikować wykrywanie.
4. Zatwierdź i wypchnij; CI wymusi nową regułę.

Przykład dodania:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Zezwalanie na wzmianki wyjaśniające
Ponieważ egzekwowane są tylko bloki kodu, można bezpiecznie opisywać przestarzałe polecenia w narracyjnym tekście. Jeśli *konieczne* jest pokazanie ich w bloku kodu dla kontrastu, dodaj blok kodu **bez** potrójnych backticków (np. wcięcie lub cytat) lub przepisz na formę pseudo.

### Pomijanie określonych plików (zaawansowane)
Jeśli to konieczne, umieść przykłady w osobnym pliku poza repozytorium lub zmień rozszerzenie podczas tworzenia. Celowe pominięcia dla przetłumaczonych kopii są automatyczne (ścieżki zawierające `translations`).

### Rozwiązywanie problemów
| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| Linter oznacza linię, którą zaktualizowałeś | Regex zbyt ogólny | Zawęź wzorzec, dodając dodatkowe granice słów (`\b`) lub kotwice |
| CI nie przechodzi, ale lokalnie działa | Różna wersja Pythona lub niezatwierdzone zmiany | Uruchom ponownie lokalnie, upewnij się, że drzewo robocze jest czyste, sprawdź wersję Pythona w workflow (3.11) |
| Potrzeba tymczasowego obejścia | Pilna poprawka | Zastosuj poprawkę natychmiast po; rozważ użycie tymczasowej gałęzi i PR następczego (unikaj dodawania przełączników obejścia) |

### Uzasadnienie
Utrzymanie dokumentacji zgodnej z *aktualnym* stabilnym interfejsem CLI zapobiega problemom podczas warsztatów, unika zamieszania wśród uczestników i centralizuje pomiar wydajności za pomocą utrzymywanych skryptów Python zamiast zmieniających się podkomend CLI.

---
Utrzymywane jako część narzędzi do zapewnienia jakości warsztatów. W celu ulepszeń (np. automatyczne poprawianie sugestii lub generowanie raportów HTML), otwórz zgłoszenie lub prześlij PR.

## 2. Skrypt walidacji przykładów

`validate_samples.py` sprawdza wszystkie pliki z przykładami w Pythonie pod kątem poprawności składni, importów i zgodności z najlepszymi praktykami.

### Użycie
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Co sprawdza
- ✅ Poprawność składni Pythona
- ✅ Obecność wymaganych importów
- ✅ Implementacja obsługi błędów (tryb szczegółowy)
- ✅ Użycie wskazówek typów (tryb szczegółowy)
- ✅ Komentarze do funkcji (tryb szczegółowy)
- ✅ Linki referencyjne do SDK (tryb szczegółowy)

### Zmienne środowiskowe
- `SKIP_IMPORT_CHECK=1` - Pomija walidację importów
- `SKIP_SYNTAX_CHECK=1` - Pomija walidację składni

### Kody wyjścia
- `0` - Wszystkie przykłady przeszły walidację
- `1` - Jeden lub więcej przykładów nie przeszło walidacji

## 3. Skrypt testowania przykładów

`test_samples.py` przeprowadza testy wstępne na wszystkich przykładach, aby sprawdzić, czy wykonują się bez błędów.

### Użycie
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Wymagania wstępne
- Uruchomiona usługa Foundry Local: `foundry service start`
- Załadowane modele: `foundry model run phi-4-mini`
- Zainstalowane zależności: `pip install -r requirements.txt`

### Co testuje
- ✅ Przykład może być wykonany bez błędów w czasie wykonywania
- ✅ Generowany jest wymagany wynik
- ✅ Poprawna obsługa błędów w przypadku niepowodzenia
- ✅ Wydajność (czas wykonania)

### Zmienne środowiskowe
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Model używany do testowania
- `TEST_TIMEOUT=30` - Limit czasu na przykład w sekundach

### Oczekiwane błędy
Niektóre testy mogą zakończyć się niepowodzeniem, jeśli opcjonalne zależności nie są zainstalowane (np. `ragas`, `sentence-transformers`). Zainstaluj je za pomocą:
```bash
pip install sentence-transformers ragas datasets
```

### Kody wyjścia
- `0` - Wszystkie testy zakończone sukcesem
- `1` - Jeden lub więcej testów zakończyło się niepowodzeniem

## 4. Eksporter wyników benchmarków w Markdown

Skrypt: `export_benchmark_markdown.py`

Generuje odtwarzalną tabelę wydajności dla zestawu modeli.

### Użycie
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Wyniki
| Plik | Opis |
|------|------|
| `benchmark_report.md` | Tabela w Markdown (średnia, p95, tokeny/sek., opcjonalnie pierwszy token) |
| `benchmark_report.json` | Surowa tablica metryk do porównania i historii |

### Opcje
| Flaga | Opis | Domyślnie |
|-------|------|----------|
| `--models` | Alias modeli oddzielony przecinkami | (wymagane) |
| `--prompt` | Użyty prompt w każdej rundzie | (wymagane) |
| `--rounds` | Liczba rund na model | 3 |
| `--output` | Plik wyjściowy Markdown | `benchmark_report.md` |
| `--json` | Plik wyjściowy JSON | `benchmark_report.json` |
| `--fail-on-empty` | Wyjście różne od zera, jeśli wszystkie benchmarki zawiodą | wyłączone |

Zmienne środowiskowe `BENCH_STREAM=1` dodają pomiar opóźnienia pierwszego tokena.

### Uwagi
- Wykorzystuje `workshop_utils` dla spójnego uruchamiania modeli i buforowania.
- Jeśli uruchamiany z innego katalogu roboczego, skrypt próbuje znaleźć `workshop_utils` za pomocą alternatywnych ścieżek.
- Dla porównania GPU: uruchom raz, włącz akcelerację przez konfigurację CLI, uruchom ponownie i porównaj pliki JSON.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.