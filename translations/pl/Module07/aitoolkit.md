# Zestaw narzędzi AI dla Visual Studio Code - Przewodnik po rozwoju Edge AI

## Wprowadzenie

Witamy w kompleksowym przewodniku po korzystaniu z zestawu narzędzi AI dla Visual Studio Code w rozwoju Edge AI. W miarę jak sztuczna inteligencja przechodzi z centralizowanego przetwarzania w chmurze na rozproszone urządzenia brzegowe, deweloperzy potrzebują potężnych, zintegrowanych narzędzi, które poradzą sobie z wyjątkowymi wyzwaniami wdrożenia na brzegu — od ograniczeń zasobów po wymogi pracy offline.

Zestaw narzędzi AI dla Visual Studio Code wypełnia tę lukę, oferując kompletne środowisko deweloperskie specjalnie zaprojektowane do budowania, testowania i optymalizacji aplikacji AI działających wydajnie na urządzeniach brzegowych. Niezależnie od tego, czy tworzysz rozwiązania dla czujników IoT, urządzeń mobilnych, systemów wbudowanych czy serwerów brzegowych, ten zestaw upraszcza cały proces rozwoju w dobrze znanym środowisku VS Code.

Ten przewodnik przeprowadzi Cię przez podstawowe koncepcje, narzędzia oraz najlepsze praktyki wykorzystania zestawu narzędzi AI w projektach Edge AI, od początkowego wyboru modelu po wdrożenie produkcyjne.

## Przegląd

Zestaw narzędzi AI dla Visual Studio Code to potężne rozszerzenie upraszczające tworzenie agentów i aplikacji AI. Zestaw oferuje kompleksowe możliwości eksploracji, oceny i wdrażania modeli AI od szerokiej gamy dostawców — w tym Anthropic, OpenAI, GitHub, Google — przy jednoczesnym wsparciu lokalnego uruchamiania modeli za pomocą ONNX i Ollama.

Co wyróżnia Zestaw narzędzi AI, to kompleksowe podejście obejmujące cały cykl życia rozwoju AI. W przeciwieństwie do tradycyjnych narzędzi skupiających się na pojedynczych aspektach, Zestaw narzędzi oferuje zintegrowane środowisko obejmujące odkrywanie modeli, eksperymenty, rozwój agentów, ocenę i wdrażanie — wszystko w znanym środowisku VS Code.

Platforma jest specjalnie zaprojektowana do szybkiego prototypowania oraz wdrożenia produkcyjnego, z funkcjami takimi jak generowanie promptów, szybkie starty, bezproblemowe integracje narzędzi MCP (Model Context Protocol) oraz rozbudowane możliwości oceny. Dla rozwoju Edge AI oznacza to możliwość efektywnego tworzenia, testowania i optymalizacji aplikacji AI pod scenariusze wdrożenia brzegowego, zachowując pełny przepływ pracy w VS Code.

## Cele nauki

Po zakończeniu tego przewodnika będziesz potrafił:

### Kluczowe kompetencje
- **Zainstalować i skonfigurować** Zestaw narzędzi AI dla Visual Studio Code do przepływów pracy rozwoju Edge AI
- **Nawigować i korzystać** z interfejsu Zestawu narzędzi AI, w tym Katalogu modeli, Playground oraz Kreatora agentów
- **Wybierać i oceniać** modele AI odpowiednie do wdrożenia na brzegu, biorąc pod uwagę wydajność i ograniczenia zasobów
- **Konwertować i optymalizować** modele za pomocą formatu ONNX i technik kwantyzacji dla urządzeń brzegowych

### Umiejętności rozwoju Edge AI
- **Projektować i implementować** aplikacje Edge AI korzystając z zintegrowanego środowiska deweloperskiego
- **Przeprowadzać testy modeli** w warunkach typowych dla brzegu, używając lokalnego wnioskowania oraz monitorowania zasobów
- **Tworzyć i dostosowywać** agentów AI zoptymalizowanych pod scenariusze wdrożenia brzegowego
- **Ocenić wydajność modeli** za pomocą metryk istotnych dla obliczeń brzegowych (opóźnienie, zużycie pamięci, dokładność)

### Optymalizacja i wdrożenie
- **Stosować techniki kwantyzacji i przycinania** w celu zmniejszenia rozmiaru modelu przy zachowaniu akceptowalnej wydajności
- **Optymalizować modele** pod konkretne platformy sprzętowe brzegu, w tym przyspieszenia CPU, GPU i NPU
- **Wdrażać najlepsze praktyki** w rozwoju Edge AI, w tym zarządzanie zasobami i strategie awaryjne
- **Przygotować modele i aplikacje** do produkcyjnego wdrożenia na urządzeniach brzegowych

### Zaawansowane koncepcje Edge AI
- **Integracja z frameworkami Edge AI**, w tym ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementacja architektur wielomodelowych** oraz scenariuszy uczenia federacyjnego dla środowisk brzegowych
- **Rozwiązywanie typowych problemów Edge AI**, w tym ograniczeń pamięci, prędkości wnioskowania i kompatybilności sprzętu
- **Projektowanie strategii monitorowania i logowania** dla aplikacji Edge AI w produkcji

### Praktyczne zastosowanie
- **Budować kompleksowe rozwiązania Edge AI** od wyboru modelu po wdrożenie
- **Wykazać się biegłością** w przepływach pracy rozwoju i technikach optymalizacji specyficznych dla brzegowej AI
- **Stosować poznane koncepcje** w rzeczywistych przypadkach użycia Edge AI, w tym IoT, aplikacjach mobilnych i wbudowanych
- **Ocenić i porównać** różne strategie wdrożenia Edge AI oraz ich kompromisy

## Kluczowe funkcje do rozwoju Edge AI

### 1. Katalog modeli i odkrywanie
- **Wsparcie wielu dostawców**: Przeglądaj i korzystaj z modeli AI od Anthropic, OpenAI, GitHub, Google i innych dostawców
- **Integracja lokalnych modeli**: Uproszczone odkrywanie modeli ONNX oraz Ollama do wdrożenia na brzegu
- **Modele GitHub**: Bezpośrednia integracja z hostingiem modeli GitHub dla usprawnionego dostępu
- **Porównanie modeli**: Porównuj modele obok siebie, aby znaleźć optymalną równowagę pod kątem ograniczeń urządzeń brzegowych

### 2. Interaktywne środowisko testowe (Playground)
- **Interaktywne środowisko testowe**: Szybkie eksperymentowanie z możliwościami modelu w kontrolowanym środowisku
- **Wsparcie multimodalne**: Testuj wejścia takie jak obrazy, tekst i inne typowe dla scenariuszy brzegowych
- **Eksperymenty w czasie rzeczywistym**: Natychmiastowa informacja zwrotna o odpowiedziach i wydajności modelu
- **Optymalizacja parametrów**: Dostosuj parametry modeli pod wymagania wdrożenia brzegowego

### 3. Kreator promptów (Agent Builder)
- **Generowanie języka naturalnego**: Twórz początkowe prompty wykorzystując opisy w języku naturalnym
- **Iteracyjne udoskonalanie**: Poprawiaj prompty na podstawie odpowiedzi i wydajności modeli
- **Dezkompozycja zadań**: Rozbijaj złożone zadania za pomocą łańcuchów promptów i strukturalnych rezultatów
- **Wsparcie zmiennych**: Używaj zmiennych w promptach do dynamicznego zachowania agentów
- **Generacja kodu produkcyjnego**: Twórz kod gotowy na produkcję dla szybkiego rozwoju aplikacji

### 4. Masowe uruchamianie i ocena
- **Testowanie wielu modeli**: Uruchamiaj wiele promptów jednocześnie na wybranych modelach
- **Efektywne testowanie na dużą skalę**: Testuj różne wejścia i konfiguracje efektywnie
- **Niestandardowe przypadki testowe**: Uruchamiaj agentów z zestawami testowymi dla walidacji funkcjonalności
- **Porównanie wydajności**: Porównuj wyniki między różnymi modelami i konfiguracjami

### 5. Ocena modeli za pomocą zbiorów danych
- **Standardowe metryki**: Testuj modele AI przy użyciu wbudowanych oceniaczy (wynik F1, trafność, podobieństwo, spójność)
- **Niestandardowe oceniacze**: Twórz własne metryki oceny dla specyficznych zastosowań
- **Integracja zbiorów danych**: Testuj modele na obszernych zbiorach danych
- **Pomiar wydajności**: Kwantyfikuj wydajność modeli pod kątem decyzji wdrożeniowych na brzegu

### 6. Możliwości dopasowania (fine-tuning)
- **Personalizacja modeli**: Dostosuj modele do konkretnych zastosowań i dziedzin
- **Specjalistyczna adaptacja**: Adaptuj modele do specyficznych dziedzin i wymagań
- **Optymalizacja dla brzegu**: Dopasuj modele szczególnie pod kątem ograniczeń wdrożenia na brzegu
- **Trening specyficzny dla domeny**: Twórz modele dedykowane konkretnym zastosowaniom Edge AI

### 7. Integracja narzędzi MCP
- **Łączność zewnętrznych narzędzi**: Podłącz agentów do narzędzi zewnętrznych przez serwery Model Context Protocol
- **Operacje w świecie rzeczywistym**: Umożliwiaj agentom zapytania do baz danych, dostęp do API lub wykonywanie niestandardowej logiki
- **Istniejące serwery MCP**: Korzystaj z narzędzi opartych na protokołach command (stdio) lub HTTP (server-sent event)
- **Tworzenie własnych MCP**: Buduj i scaffolduj nowe serwery MCP z testowaniem w Kreatorze agentów

### 8. Rozwój i testowanie agentów
- **Wsparcie wywołań funkcji**: Pozwalaj agentom dynamicznie wywoływać zewnętrzne funkcje
- **Testy integracyjne w czasie rzeczywistym**: Testuj integracje podczas uruchomień i użycia narzędzi w czasie rzeczywistym
- **Wersjonowanie agentów**: Kontrola wersji agentów z możliwością porównania wyników oceny
- **Debugowanie i śledzenie**: Lokalna diagnostyka i śledzenie do rozwoju agentów

## Przepływ pracy rozwoju Edge AI

### Faza 1: Odkrywanie i wybór modelu
1. **Przeglądaj Katalog modeli**: Korzystaj z katalogu modelów, aby znaleźć modele odpowiednie do wdrożenia na brzegu
2. **Porównaj wydajność**: Oceń modele pod kątem rozmiaru, dokładności i szybkości wnioskowania
3. **Testuj lokalnie**: Użyj modeli Ollama lub ONNX do testów lokalnych przed wdrożeniem na brzegu
4. **Ocena wymagań zasobów**: Określ potrzeby pamięci i obliczeń dla docelowych urządzeń brzegowych

### Faza 2: Optymalizacja modelu
1. **Konwersja do ONNX**: Konwertuj wybrane modele do formatu ONNX dla kompatybilności na brzegu
2. **Zastosuj kwantyzację**: Zmniejsz rozmiar modelu przez kwantyzację INT8 lub INT4
3. **Optymalizacja sprzętu**: Optymalizuj pod docelowy sprzęt brzegowy (ARM, x86, specjalistyczne akceleratory)
4. **Weryfikacja wydajności**: Sprawdź, czy zoptymalizowane modele zachowują akceptowalną dokładność

### Faza 3: Tworzenie aplikacji
1. **Projektowanie agentów**: Użyj Kreatora agentów, aby tworzyć agentów AI zoptymalizowanych pod brzegi
2. **Inżynieria promptów**: Opracuj prompty skuteczne z mniejszymi modelami brzegowymi
3. **Testy integracyjne**: Testuj agentów w symulowanych warunkach brzegowych
4. **Generacja kodu**: Generuj kod produkcyjny zoptymalizowany pod wdrożenie na brzegu

### Faza 4: Ocena i testowanie
1. **Ocena partii**: Testuj wiele konfiguracji, aby znaleźć optymalne ustawienia brzegowe
2. **Profilowanie wydajności**: Analizuj prędkość wnioskowania, zużycie pamięci i dokładność
3. **Symulacja brzegu**: Testuj w warunkach zbliżonych do docelowego środowiska wdrożeniowego brzegowego
4. **Testy obciążeniowe**: Oceń wydajność pod różnymi warunkami obciążenia

### Faza 5: Przygotowanie do wdrożenia
1. **Ostateczna optymalizacja**: Zastosuj końcowe optymalizacje w oparciu o wyniki testów
2. **Pakowanie wdrożeniowe**: Spakuj modele i kod do wdrożenia na brzegu
3. **Dokumentacja**: Dokumentuj wymagania i konfigurację wdrożenia
4. **Konfiguracja monitoringu**: Przygotuj monitoring i logowanie dla wdrożenia na brzegu

## Docelowi odbiorcy rozwoju Edge AI

### Deweloperzy Edge AI
- Twórcy aplikacji budujących urządzenia brzegowe i rozwiązania IoT z AI
- Deweloperzy systemów wbudowanych integrujący możliwości AI w urządzenia o ograniczonych zasobach
- Programiści mobilni tworzący aplikacje AI działające bezpośrednio na smartfonach i tabletach

### Inżynierowie Edge AI
- Inżynierowie AI optymalizujący modele pod wdrożenie na brzegu i zarządzający potokami wnioskowania
- Inżynierowie DevOps wdrażający i zarządzający modelami AI w rozproszonej infrastrukturze brzegowej
- Inżynierowie wydajności optymalizujący obciążenia AI pod ograniczenia sprzętowe brzegu

### Badacze i edukatorzy
- Badacze AI rozwijający efektywne modele i algorytmy do obliczeń brzegowych
- Edukatorzy uczący koncepcji Edge AI oraz prezentujący techniki optymalizacji
- Studenci poznający wyzwania i rozwiązania we wdrażaniu Edge AI

## Przypadki użycia Edge AI

### Inteligentne urządzenia IoT
- **Rozpoznawanie obrazów w czasie rzeczywistym**: Wdrażaj modele wizji komputerowej na kamerach i czujnikach IoT
- **Przetwarzanie mowy**: Implementuj rozpoznawanie mowy i przetwarzanie języka naturalnego w inteligentnych głośnikach
- **Predykcyjne utrzymanie ruchu**: Uruchamiaj modele wykrywania anomalii na przemysłowych urządzeniach brzegowych
- **Monitorowanie środowiskowe**: Wdrażaj modele analizy danych czujników do zastosowań środowiskowych

### Aplikacje mobilne i wbudowane
- **Tłumaczenie na urządzeniu**: Implementuj modele tłumaczenia języków działające offline
- **Rozszerzona rzeczywistość**: Wdrażaj rozpoznawanie i śledzenie obiektów w czasie rzeczywistym dla aplikacji AR
- **Monitorowanie zdrowia**: Uruchamiaj modele analizy zdrowia na urządzeniach noszonych i sprzęcie medycznym
- **Systemy autonomiczne**: Implementuj modele podejmowania decyzji dla dronów, robotów i pojazdów

### Infrastruktura Edge Computing
- **Centra danych na brzegu**: Wdrażaj modele AI w centrach danych na brzegu dla aplikacji o niskich opóźnieniach
- **Integracja CDN**: Integruj możliwości przetwarzania AI w sieciach dostarczania treści
- **Brzeg 5G**: Wykorzystuj obliczenia brzegowe 5G dla aplikacji zasilanych przez AI
- **Fog Computing**: Implementuj przetwarzanie AI w środowiskach fog computing

## Instalacja i konfiguracja

### Instalacja rozszerzenia
Zainstaluj rozszerzenie Zestawu narzędzi AI bezpośrednio z Visual Studio Code Marketplace:

**ID rozszerzenia**: `ms-windows-ai-studio.windows-ai-studio`

**Metody instalacji**:
1. **VS Code Marketplace**: Wyszukaj „AI Toolkit” w widoku rozszerzeń
2. **Linia poleceń**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalacja bezpośrednia**: Pobierz z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Wymagania wstępne do rozwoju Edge AI
- **Visual Studio Code**: Zalecana najnowsza wersja
- **Środowisko Python**: Python 3.8+ z wymaganymi bibliotekami AI
- **ONNX Runtime** (opcjonalnie): Do wnioskowania modeli ONNX
- **Ollama** (opcjonalnie): Do lokalnego serwowania modeli
- **Narzędzia akceleracji sprzętowej**: CUDA, OpenVINO lub specyficzne dla platformy akceleratory

### Konfiguracja początkowa
1. **Aktywacja rozszerzenia**: Otwórz VS Code i sprawdź, czy Zestaw narzędzi AI pojawił się na pasku aktywności
2. **Konfiguracja dostawców modeli**: Skonfiguruj dostęp do GitHub, OpenAI, Anthropic lub innych dostawców modeli
3. **Środowisko lokalne**: Ustaw środowisko Python i zainstaluj wymagane pakiety
4. **Akceleracja sprzętowa**: Skonfiguruj przyspieszenie GPU/NPU, jeśli jest dostępne
5. **Integracja MCP**: Skonfiguruj serwery Model Context Protocol jeśli jest to potrzebne

### Lista kontrolna pierwszego uruchomienia
- [ ] Rozszerzenie Zestawu narzędzi AI zainstalowane i aktywowane
- [ ] Katalog modeli dostępny i modele możliwe do odkrycia
- [ ] Playground gotowy do testów modeli
- [ ] Kreator agentów dostępny do tworzenia promptów
- [ ] Środowisko lokalnego rozwoju skonfigurowane
- [ ] Akceleracja sprzętowa (jeśli dostępna) poprawnie skonfigurowana

## Pierwsze kroki z Zestawem narzędzi AI

### Szybki przewodnik startowy

Zalecamy rozpoczęcie od modeli hostowanych przez GitHub dla najbardziej zoptymalizowanego doświadczenia:

1. **Instalacja**: Postępuj zgodnie z [przewodnikiem instalacji](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup), aby skonfigurować Zestaw narzędzi AI na swoim urządzeniu
2. **Odkrywanie modeli**: Z widoku drzewa rozszerzenia wybierz **CATALOG > Models**, aby eksplorować dostępne modele
3. **Modele GitHub**: Zacznij od modeli hostowanych przez GitHub dla optymalnej integracji
4. **Testy w Playground**: Z dowolnej karty modelu wybierz **Try in Playground**, aby rozpocząć eksperymenty z możliwościami modelu

### Krok po kroku rozwoju Edge AI

#### Krok 1: Eksploracja i wybór modelu
1. Otwórz widok Zestawu narzędzi AI na pasku aktywności VS Code
2. Przeglądaj Katalog modeli w poszukiwaniu modeli gotowych do wdrożenia na brzegu
3. Filtruj według dostawcy (GitHub, ONNX, Ollama) zgodnie z wymaganiami brzegu
4. Użyj **Try in Playground**, aby natychmiast testować możliwości modeli

#### Krok 2: Tworzenie agentów
1. Skorzystaj z **Kreatora promptów (Agent Builder)**, aby tworzyć agentów AI zoptymalizowanych pod brzegi
2. Generuj początkowe prompty korzystając z opisów w języku naturalnym
3. Iteruj i udoskonalaj prompty na podstawie odpowiedzi modeli
4. Integruj narzędzia MCP dla rozszerzonych możliwości agentów


#### Krok 3: Testowanie i ewaluacja
1. Użyj **Bulk Run** do testowania wielu promptów na wybranych modelach
2. Uruchamiaj agentów z przypadkami testowymi, aby zweryfikować funkcjonalność
3. Oceniaj dokładność i wydajność, korzystając z wbudowanych lub niestandardowych metryk
4. Porównuj różne modele i konfiguracje

#### Krok 4: Dostosowywanie i optymalizacja
1. Dostosuj modele do specyficznych zastosowań edge
2. Zastosuj dostrojenie specyficzne dla danej dziedziny
3. Optymalizuj pod kątem ograniczeń wdrożeniowych na edge
4. Wersjonuj i porównuj różne konfiguracje agentów

#### Krok 5: Przygotowanie do wdrożenia
1. Generuj kod gotowy do produkcji za pomocą Agent Builder
2. Skonfiguruj połączenia serwera MCP do zastosowań produkcyjnych
3. Przygotuj pakiety wdrożeniowe dla urządzeń edge
4. Skonfiguruj monitorowanie i metryki ewaluacyjne

## Przykłady dla AI Toolkit

Wypróbuj nasze przykłady
[Przykłady AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) zostały zaprojektowane, aby pomóc programistom i badaczom skutecznie eksplorować i wdrażać rozwiązania AI.

Nasze przykłady obejmują:

Przykładowy kod: gotowe przykłady demonstrujące funkcjonalności AI, takie jak trenowanie, wdrażanie lub integracja modeli z aplikacjami.
Dokumentację: przewodniki i samouczki pomagające użytkownikom zrozumieć funkcje AI Toolkit oraz jak z nich korzystać.
Wymagania wstępne

- Visual Studio Code
- AI Toolkit dla Visual Studio Code
- Osobisty token dostępu (PAT) o precyzyjnych uprawnieniach GitHub
- Foundry Local

## Najlepsze praktyki dla rozwoju Edge AI

### Wybór modelu
- **Ograniczenia rozmiaru**: Wybieraj modele mieszczące się w ograniczeniach pamięci urządzeń docelowych
- **Szybkość inferencji**: Priorytetowo traktuj modele z szybkim czasem inferencji do zastosowań czasu rzeczywistego
- **Kompromisy dokładności**: Równoważ dokładność modelu z ograniczeniami zasobów
- **Kompatybilność formatu**: Preferuj formaty ONNX lub zoptymalizowane pod sprzęt do wdrożeń edge

### Techniki optymalizacji
- **Kwantyzacja**: Użyj kwantyzacji INT8 lub INT4, aby zmniejszyć rozmiar modelu i poprawić szybkość
- **Przycinanie**: Usuń niepotrzebne parametry modelu, aby zmniejszyć wymagania obliczeniowe
- **Destylacja wiedzy**: Twórz mniejsze modele zachowujące wydajność większych
- **Przyspieszenie sprzętowe**: Wykorzystuj NPU, GPU lub specjalizowane akceleratory, jeśli są dostępne

### Przebieg rozwoju
- **Iteracyjne testowanie**: Testuj często w warunkach przypominających edge w trakcie rozwoju
- **Monitorowanie wydajności**: Ciągle monitoruj użycie zasobów oraz szybkość inferencji
- **Kontrola wersji**: Śledź wersje modeli i ustawienia optymalizacji
- **Dokumentacja**: Dokumentuj wszystkie decyzje optymalizacyjne i kompromisy wydajności

### Rozważania wdrożeniowe
- **Monitorowanie zasobów**: Monitoruj pamięć, CPU oraz zużycie energii w środowisku produkcyjnym
- **Strategie awaryjne**: Wdrażaj mechanizmy awaryjne na wypadek awarii modelu
- **Mechanizmy aktualizacji**: Planuj aktualizacje modeli i zarządzanie wersjami
- **Bezpieczeństwo**: Zastosuj odpowiednie środki bezpieczeństwa dla aplikacji Edge AI

## Integracja z frameworkami Edge AI

### ONNX Runtime
- **Wieloplatformowe wdrożenia**: Wdrażaj modele ONNX na różnych platformach edge
- **Optymalizacja sprzętowa**: Wykorzystuj sprzętowe optymalizacje ONNX Runtime
- **Wsparcie mobilne**: Używaj ONNX Runtime Mobile do aplikacji na smartfony i tablety
- **Integracja IoT**: Wdrażaj na urządzenia IoT korzystając z lekkich dystrybucji ONNX Runtime

### Windows ML
- **Urządzenia Windows**: Optymalizuj pod urządzenia edge i PC oparte na Windows
- **Przyspieszenie NPU**: Wykorzystuj jednostki przetwarzania neuronowego na urządzeniach Windows
- **DirectML**: Korzystaj z DirectML do przyspieszenia GPU na platformach Windows
- **Integracja UWP**: Integruj z aplikacjami Universal Windows Platform

### TensorFlow Lite
- **Optymalizacja mobilna**: Wdrażaj modele TensorFlow Lite na urządzeniach mobilnych i wbudowanych
- **Delegaci sprzętowi**: Używaj specjalizowanych delegatów sprzętowych do przyspieszenia
- **Mikrokontrolery**: Wdrażaj na mikrokontrolerach korzystając z TensorFlow Lite Micro
- **Wieloplatformowe wsparcie**: Wdrażaj na Androidzie, iOS oraz systemach embedded Linux

### Azure IoT Edge
- **Hybrydowe chmura-edge**: Łącz trening w chmurze z inferencją na edge
- **Wdrażanie modułów**: Wdrażaj modele AI jako moduły IoT Edge
- **Zarządzanie urządzeniami**: Zarządzaj urządzeniami edge i aktualizacjami modeli zdalnie
- **Telemetria**: Zbieraj dane wydajności i metryki modeli z wdrożeń edge

## Zaawansowane scenariusze Edge AI

### Wdrożenie wielu modeli
- **Zespoły modeli**: Wdrażaj wiele modeli dla poprawy dokładności lub redundancji
- **Testy A/B**: Testuj różne modele jednocześnie na urządzeniach edge
- **Wybór dynamiczny**: Wybieraj modele w zależności od aktualnych warunków urządzenia
- **Współdzielenie zasobów**: Optymalizuj użycie zasobów wśród kilku wdrożonych modeli

### Federated Learning
- **Trening rozproszony**: Trenuj modele na wielu urządzeniach edge
- **Ochrona prywatności**: Zachowuj dane treningowe lokalnie, udostępniając jedynie ulepszenia modeli
- **Nauka współdzielona**: Umożliw urządzeniom naukę z doświadczeń zbiorowych
- **Koordynacja edge-chmura**: Koordynuj naukę między urządzeniami edge a infrastrukturą chmurową

### Przetwarzanie w czasie rzeczywistym
- **Przetwarzanie strumieniowe**: Przetwarzaj ciągłe strumienie danych na urządzeniach edge
- **Inferencja o niskim opóźnieniu**: Optymalizuj pod kątem minimalnego opóźnienia inferencji
- **Przetwarzanie wsadowe**: Wydajnie przetwarzaj partie danych na edge
- **Przetwarzanie adaptacyjne**: Dostosowuj przetwarzanie do aktualnych możliwości urządzenia

## Rozwiązywanie problemów w rozwoju Edge AI

### Powszechne problemy
- **Ograniczenia pamięci**: Model jest za duży na pamięć urządzenia docelowego
- **Szybkość inferencji**: Inferencja modelu jest zbyt wolna dla wymagań w czasie rzeczywistym
- **Degradacja dokładności**: Optymalizacja nieakceptowalnie obniża dokładność modelu
- **Kompatybilność sprzętowa**: Model nie jest kompatybilny ze sprzętem docelowym

### Strategie debugowania
- **Profilowanie wydajności**: Korzystaj z funkcji śledzenia AI Toolkit, aby zidentyfikować wąskie gardła
- **Monitorowanie zasobów**: Monitoruj zużycie pamięci i CPU w trakcie rozwoju
- **Testowanie przyrostowe**: Testuj optymalizacje krok po kroku, aby wyizolować problemy
- **Symulacja sprzętu**: Używaj narzędzi deweloperskich do symulacji sprzętu docelowego

### Rozwiązania optymalizacyjne
- **Dalsza kwantyzacja**: Zastosuj bardziej agresywne techniki kwantyzacji
- **Architektura modelu**: Rozważ różne architektury modeli zoptymalizowanych pod edge
- **Optymalizacja przetwarzania wstępnego**: Optymalizuj przetwarzanie danych pod ograniczenia edge
- **Optymalizacja inferencji**: Skorzystaj z optymalizacji inferencji specyficznych dla sprzętu

## Zasoby i kolejne kroki

### Oficjalna dokumentacja
- [Dokumentacja dewelopera AI Toolkit](https://aka.ms/AIToolkit/doc)
- [Przewodnik instalacji i konfiguracji](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [Dokumentacja aplikacji inteligentnych VS Code](https://code.visualstudio.com/docs/intelligentapps)
- [Dokumentacja Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Społeczność i wsparcie
- [Repozytorium AI Toolkit na GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [Zgłaszanie problemów i propozycji na GitHub](https://aka.ms/AIToolkit/feedback)
- [Społeczność Azure AI Foundry na Discord](https://aka.ms/azureaifoundry/discord)
- [Marketplace rozszerzeń VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Zasoby techniczne
- [Dokumentacja ONNX Runtime](https://onnxruntime.ai/)
- [Dokumentacja Ollama](https://ollama.ai/)
- [Dokumentacja Windows ML](https://docs.microsoft.com/en-us/windows/ai/)
- [Dokumentacja Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Ścieżki nauki
- [Kurs podstaw Edge AI](../Module01/README.md)
- [Przewodnik małych modeli językowych](../Module02/README.md)
- [Strategie wdrożeń edge](../Module03/README.md)
- [Rozwój Edge AI w Windows](./windowdeveloper.md)

### Dodatkowe zasoby
- **Statystyki repozytorium**: 1.8k+ gwiazdek, 150+ forków, 18+ kontrybutorów
- **Licencja**: Licencja MIT
- **Bezpieczeństwo**: Obowiązują zasady bezpieczeństwa Microsoft
- **Telemetria**: Respektuje ustawienia telemetrii VS Code

## Podsumowanie

AI Toolkit dla Visual Studio Code to kompleksowa platforma do nowoczesnego rozwoju AI, oferująca usprawnione możliwości budowy agentów, szczególnie cenne dla aplikacji Edge AI. Dzięki obszernej katalogowi modeli wspierających dostawców takich jak Anthropic, OpenAI, GitHub i Google, w połączeniu z lokalnym wykonaniem przez ONNX i Ollama, toolkit zapewnia elastyczność wymaganą dla różnych scenariuszy wdrożeń edge.

Siłą toolkit jest zintegrowane podejście – od odkrywania modeli i eksperymentowania w Playground, po zaawansowaną budowę agentów za pomocą Prompt Builder, kompleksowe możliwości ewaluacji i płynną integrację z narzędziami MCP. Dla deweloperów Edge AI oznacza to szybkie prototypowanie i testowanie agentów AI przed wdrożeniem na edge, z możliwością szybkiego iterowania i optymalizacji pod środowiska o ograniczonych zasobach.

Kluczowe zalety dla rozwoju Edge AI obejmują:
- **Szybkie eksperymentowanie**: Testuj modele i agentów szybko przed wdrożeniem na edge
- **Elastyczność wielodostawcy**: Uzyskaj dostęp do modeli z różnych źródeł, by znaleźć optymalne rozwiązania edge
- **Rozwój lokalny**: Testuj z ONNX i Ollama dla rozwoju offline i z zachowaniem prywatności
- **Gotowość produkcyjna**: Generuj kod gotowy do produkcji i integruj zewnętrzne narzędzia przez MCP
- **Kompleksowa ewaluacja**: Korzystaj z metryk wbudowanych i niestandardowych, by potwierdzić wydajność Edge AI

W miarę jak AI coraz częściej trafia do scenariuszy wdrożeń na edge, AI Toolkit dla VS Code dostarcza środowisko deweloperskie i workflow niezbędne do budowania, testowania i optymalizacji inteligentnych aplikacji dla środowisk o ograniczonych zasobach. Niezależnie czy tworzysz rozwiązania IoT, aplikacje AI na urządzenia mobilne, czy systemy wbudowane, rozbudowany zestaw funkcji toolkit i zintegrowany workflow wspierają cały cykl życia rozwoju Edge AI.

Dzięki ciągłemu rozwojowi i aktywnej społeczności (1.8k+ gwiazdek na GitHub) AI Toolkit pozostaje na czele narzędzi do rozwoju AI, stale ewoluując, by sprostać potrzebom nowoczesnych deweloperów budujących rozwiązania pod kątem wdrożeń edge.

[Next Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->