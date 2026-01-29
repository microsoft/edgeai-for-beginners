# AI Toolkit dla Visual Studio Code - Przewodnik po rozwoju Edge AI

## Wprowadzenie

Witamy w kompleksowym przewodniku dotyczącym korzystania z AI Toolkit dla Visual Studio Code w rozwoju Edge AI. W miarę jak sztuczna inteligencja przenosi się z centralnego przetwarzania w chmurze na rozproszone urządzenia brzegowe, programiści potrzebują potężnych, zintegrowanych narzędzi, które sprostają unikalnym wyzwaniom wdrożeń na brzegu - od ograniczeń zasobów po wymagania dotyczące pracy offline.

AI Toolkit dla Visual Studio Code wypełnia tę lukę, oferując kompletne środowisko programistyczne zaprojektowane specjalnie do budowy, testowania i optymalizacji aplikacji AI, które działają efektywnie na urządzeniach brzegowych. Niezależnie od tego, czy tworzysz dla czujników IoT, urządzeń mobilnych, systemów wbudowanych czy serwerów brzegowych, ten zestaw narzędzi usprawnia cały proces rozwoju w znanym środowisku VS Code.

Ten przewodnik przeprowadzi Cię przez kluczowe pojęcia, narzędzia i najlepsze praktyki związane z wykorzystaniem AI Toolkit w projektach Edge AI, od wyboru modelu po wdrożenie produkcyjne.

## Przegląd

AI Toolkit dla Visual Studio Code to potężne rozszerzenie, które upraszcza rozwój agentów i tworzenie aplikacji AI. Zestaw narzędzi oferuje kompleksowe możliwości eksploracji, oceny i wdrażania modeli AI od szerokiej gamy dostawców — w tym Anthropic, OpenAI, GitHub, Google — jednocześnie wspierając lokalne wykonywanie modeli za pomocą ONNX i Ollama.

To, co wyróżnia AI Toolkit, to jego kompleksowe podejście do całego cyklu życia rozwoju AI. W przeciwieństwie do tradycyjnych narzędzi AI, które koncentrują się na pojedynczych aspektach, AI Toolkit zapewnia zintegrowane środowisko obejmujące odkrywanie modeli, eksperymentowanie, rozwój agentów, ocenę i wdrażanie — wszystko w znanym środowisku VS Code.

Platforma została zaprojektowana z myślą o szybkim prototypowaniu i wdrożeniu produkcyjnym, z funkcjami takimi jak generowanie promptów, szybkie starty, bezproblemowe integracje narzędzi MCP (Model Context Protocol) oraz rozbudowane możliwości oceny. Dla rozwoju Edge AI oznacza to, że możesz efektywnie rozwijać, testować i optymalizować aplikacje AI dla scenariuszy wdrożeń na brzegu, jednocześnie utrzymując pełny przepływ pracy w VS Code.

## Cele nauki

Na koniec tego przewodnika będziesz w stanie:

### Kluczowe kompetencje
- **Zainstalować i skonfigurować** AI Toolkit dla Visual Studio Code w ramach przepływów pracy rozwoju Edge AI
- **Nawigować i korzystać** z interfejsu AI Toolkit, w tym Model Catalog, Playground i Agent Builder
- **Wybrać i ocenić** modele AI odpowiednie do wdrożenia na brzegu, biorąc pod uwagę wydajność i ograniczenia zasobów
- **Konwertować i optymalizować** modele za pomocą formatu ONNX i technik kwantyzacji dla urządzeń brzegowych

### Umiejętności rozwoju Edge AI
- **Projektować i wdrażać** aplikacje Edge AI za pomocą zintegrowanego środowiska programistycznego
- **Testować modele** w warunkach przypominających pracę na brzegu, korzystając z lokalnego wnioskowania i monitorowania zasobów
- **Tworzyć i dostosowywać** agentów AI zoptymalizowanych pod kątem scenariuszy wdrożeń na brzegu
- **Ocenić wydajność modeli** za pomocą metryk istotnych dla obliczeń brzegowych (opóźnienie, zużycie pamięci, dokładność)

### Optymalizacja i wdrożenie
- **Zastosować techniki kwantyzacji i przycinania** w celu zmniejszenia rozmiaru modelu przy zachowaniu akceptowalnej wydajności
- **Optymalizować modele** dla konkretnych platform sprzętowych na brzegu, w tym CPU, GPU i akceleratorów NPU
- **Wdrażać najlepsze praktyki** w rozwoju Edge AI, w tym zarządzanie zasobami i strategie awaryjne
- **Przygotować modele i aplikacje** do wdrożenia produkcyjnego na urządzeniach brzegowych

### Zaawansowane koncepcje Edge AI
- **Integracja z frameworkami Edge AI** w tym ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementacja architektur wielomodelowych** i scenariuszy uczenia federacyjnego dla środowisk brzegowych
- **Rozwiązywanie typowych problemów Edge AI** w tym ograniczeń pamięci, szybkości wnioskowania i kompatybilności sprzętowej
- **Projektowanie strategii monitorowania i logowania** dla aplikacji Edge AI w produkcji

### Zastosowanie praktyczne
- **Budowa kompleksowych rozwiązań Edge AI** od wyboru modelu po wdrożenie
- **Demonstracja biegłości** w specyficznych dla brzegu przepływach pracy rozwoju i technikach optymalizacji
- **Zastosowanie zdobytej wiedzy** w rzeczywistych przypadkach użycia Edge AI, w tym IoT, aplikacjach mobilnych i wbudowanych
- **Ocena i porównanie** różnych strategii wdrożeń Edge AI oraz ich kompromisów

## Kluczowe funkcje dla rozwoju Edge AI

### 1. Katalog modeli i odkrywanie
- **Wsparcie dla wielu dostawców**: Przeglądaj i uzyskuj dostęp do modeli AI od Anthropic, OpenAI, GitHub, Google i innych dostawców
- **Integracja lokalnych modeli**: Uproszczone odkrywanie modeli ONNX i Ollama dla wdrożeń na brzegu
- **Modele GitHub**: Bezpośrednia integracja z hostingiem modeli GitHub dla uproszczonego dostępu
- **Porównanie modeli**: Porównuj modele obok siebie, aby znaleźć optymalną równowagę dla ograniczeń urządzeń brzegowych

### 2. Interaktywne środowisko testowe
- **Interaktywne środowisko testowe**: Szybkie eksperymentowanie z możliwościami modeli w kontrolowanym środowisku
- **Wsparcie multimodalne**: Testowanie z obrazami, tekstem i innymi typowymi wejściami w scenariuszach brzegowych
- **Eksperymentowanie w czasie rzeczywistym**: Natychmiastowa informacja zwrotna na temat odpowiedzi modeli i ich wydajności
- **Optymalizacja parametrów**: Dostosowywanie parametrów modeli do wymagań wdrożeń na brzegu

### 3. Budowanie promptów (agentów)
- **Generowanie języka naturalnego**: Tworzenie początkowych promptów za pomocą opisów w języku naturalnym
- **Iteracyjne doskonalenie**: Poprawa promptów na podstawie odpowiedzi modeli i ich wydajności
- **Rozkładanie zadań**: Rozbijanie złożonych zadań za pomocą łańcuchów promptów i strukturalnych wyników
- **Wsparcie dla zmiennych**: Używanie zmiennych w promptach dla dynamicznego zachowania agentów
- **Generowanie kodu produkcyjnego**: Tworzenie kodu gotowego do produkcji dla szybkiego rozwoju aplikacji

### 4. Masowe uruchamianie i ocena
- **Testowanie wielu modeli**: Wykonywanie wielu promptów na wybranych modelach jednocześnie
- **Efektywne testowanie na dużą skalę**: Testowanie różnych wejść i konfiguracji w sposób efektywny
- **Niestandardowe przypadki testowe**: Uruchamianie agentów z przypadkami testowymi w celu weryfikacji funkcjonalności
- **Porównanie wydajności**: Porównywanie wyników między różnymi modelami i konfiguracjami

### 5. Ocena modeli za pomocą zbiorów danych
- **Standardowe metryki**: Testowanie modeli AI za pomocą wbudowanych narzędzi oceny (F1 score, trafność, podobieństwo, spójność)
- **Niestandardowe narzędzia oceny**: Tworzenie własnych metryk oceny dla specyficznych przypadków użycia
- **Integracja zbiorów danych**: Testowanie modeli na podstawie kompleksowych zbiorów danych
- **Pomiar wydajności**: Kwantyfikacja wydajności modeli dla decyzji o wdrożeniu na brzegu

### 6. Możliwości dostrajania
- **Dostosowywanie modeli**: Dostosowywanie modeli do specyficznych przypadków użycia i dziedzin
- **Specjalistyczna adaptacja**: Adaptacja modeli do specjalistycznych dziedzin i wymagań
- **Optymalizacja dla brzegu**: Dostrajanie modeli specjalnie pod kątem ograniczeń wdrożeń na brzegu
- **Trening specyficzny dla dziedziny**: Tworzenie modeli dostosowanych do specyficznych przypadków użycia na brzegu

### 7. Integracja narzędzi MCP
- **Łączność z narzędziami zewnętrznymi**: Łączenie agentów z narzędziami zewnętrznymi za pomocą serwerów Model Context Protocol
- **Działania w rzeczywistości**: Umożliwienie agentom zapytań do baz danych, dostępu do API lub wykonywania niestandardowej logiki
- **Istniejące serwery MCP**: Korzystanie z narzędzi z protokołów command (stdio) lub HTTP (server-sent event)
- **Rozwój niestandardowych MCP**: Tworzenie i testowanie nowych serwerów MCP w Agent Builder

### 8. Rozwój i testowanie agentów
- **Wsparcie dla wywoływania funkcji**: Umożliwienie agentom dynamicznego wywoływania funkcji zewnętrznych
- **Testowanie integracji w czasie rzeczywistym**: Testowanie integracji z rzeczywistymi uruchomieniami i użyciem narzędzi
- **Wersjonowanie agentów**: Kontrola wersji agentów z możliwością porównania wyników oceny
- **Debugowanie i śledzenie**: Lokalna możliwość śledzenia i debugowania dla rozwoju agentów

## Przepływ pracy rozwoju Edge AI

### Faza 1: Odkrywanie i wybór modeli
1. **Eksploracja katalogu modeli**: Korzystaj z katalogu modeli, aby znaleźć modele odpowiednie do wdrożeń na brzegu
2. **Porównanie wydajności**: Oceń modele pod kątem rozmiaru, dokładności i szybkości wnioskowania
3. **Testowanie lokalne**: Korzystaj z modeli Ollama lub ONNX do testowania lokalnego przed wdrożeniem na brzegu
4. **Ocena wymagań zasobów**: Określ potrzeby pamięci i obliczeniowe dla docelowych urządzeń brzegowych

### Faza 2: Optymalizacja modeli
1. **Konwersja do ONNX**: Konwertuj wybrane modele do formatu ONNX dla kompatybilności z brzegiem
2. **Zastosowanie kwantyzacji**: Zmniejsz rozmiar modelu za pomocą kwantyzacji INT8 lub INT4
3. **Optymalizacja sprzętowa**: Optymalizuj dla docelowego sprzętu brzegowego (ARM, x86, specjalistyczne akceleratory)
4. **Walidacja wydajności**: Sprawdź, czy zoptymalizowane modele zachowują akceptowalną dokładność

### Faza 3: Rozwój aplikacji
1. **Projektowanie agentów**: Korzystaj z Agent Builder do tworzenia agentów AI zoptymalizowanych pod kątem brzegu
2. **Inżynieria promptów**: Twórz prompty, które skutecznie działają z mniejszymi modelami brzegowymi
3. **Testowanie integracji**: Testuj agentów w symulowanych warunkach brzegowych
4. **Generowanie kodu**: Twórz kod produkcyjny zoptymalizowany dla wdrożeń na brzegu

### Faza 4: Ocena i testowanie
1. **Ocena masowa**: Testuj wiele konfiguracji, aby znaleźć optymalne ustawienia dla brzegu
2. **Profilowanie wydajności**: Analizuj szybkość wnioskowania, zużycie pamięci i dokładność
3. **Symulacja brzegu**: Testuj w warunkach zbliżonych do docelowego środowiska wdrożenia na brzegu
4. **Testy obciążeniowe**: Oceń wydajność w różnych warunkach obciążenia

### Faza 5: Przygotowanie do wdrożenia
1. **Ostateczna optymalizacja**: Zastosuj ostateczne optymalizacje na podstawie wyników testów
2. **Pakowanie wdrożeniowe**: Pakuj modele i kod do wdrożenia na brzegu
3. **Dokumentacja**: Dokumentuj wymagania i konfigurację wdrożenia
4. **Konfiguracja monitorowania**: Przygotuj monitorowanie i logowanie dla wdrożenia na brzegu

## Docelowa grupa odbiorców rozwoju Edge AI

### Programiści Edge AI
- Twórcy aplikacji budujący urządzenia brzegowe z AI i rozwiązania IoT
- Programiści systemów wbudowanych integrujący możliwości AI w urządzeniach o ograniczonych zasobach
- Twórcy aplikacji mobilnych tworzący aplikacje AI na urządzeniach mobilnych i tabletach

### Inżynierowie Edge AI
- Inżynierowie AI optymalizujący modele do wdrożeń na brzegu i zarządzający pipeline'ami wnioskowania
- Inżynierowie DevOps wdrażający i zarządzający modelami AI w rozproszonej infrastrukturze brzegowej
- Inżynierowie wydajności optymalizujący obciążenia AI dla ograniczeń sprzętowych brzegu

### Naukowcy i edukatorzy
- Naukowcy AI rozwijający efektywne modele i algorytmy dla obliczeń brzegowych
- Edukatorzy uczący koncepcji Edge AI i demonstrujący techniki optymalizacji
- Studenci uczący się o wyzwaniach i rozwiązaniach w wdrożeniach Edge AI

## Przypadki użycia Edge AI

### Inteligentne urządzenia IoT
- **Rozpoznawanie obrazów w czasie rzeczywistym**: Wdrażanie modeli wizji komputerowej na kamerach IoT i czujnikach
- **Przetwarzanie głosu**: Implementacja rozpoznawania mowy i przetwarzania języka naturalnego na inteligentnych głośnikach
- **Predykcyjne utrzymanie**: Uruchamianie modeli wykrywania anomalii na przemysłowych urządzeniach brzegowych
- **Monitorowanie środowiska**: Wdrażanie modeli analizy danych z czujników dla aplikacji środowiskowych

### Aplikacje mobilne i wbudowane
- **Tłumaczenie na urządzeniu**: Implementacja modeli tłumaczenia językowego działających offline
- **Rozszerzona rzeczywistość**: Wdrażanie rozpoznawania obiektów w czasie rzeczywistym i śledzenia dla aplikacji AR
- **Monitorowanie zdrowia**: Uruchamianie modeli analizy zdrowia na urządzeniach noszonych i sprzęcie medycznym
- **Systemy autonomiczne**: Implementacja modeli podejmowania decyzji dla dronów, robotów i pojazdów

### Infrastruktura obliczeniowa na brzegu
- **Centra danych na brzegu**: Wdrażanie modeli AI w centrach danych na brzegu dla aplikacji o niskim opóźnieniu
- **Integracja CDN**: Integracja możliwości przetwarzania AI w sieciach dostarczania treści
- **Brzeg 5G**: Wykorzystanie obliczeń brzegowych 5G dla aplikacji zasilanych AI
- **Obliczenia mgły**: Implementacja przetwarzania AI w środowiskach obliczeń mgły

## Instalacja i konfiguracja

### Instalacja rozszerzenia
Zainstaluj rozszerzenie AI Toolkit bezpośrednio z Visual Studio Code Marketplace:

**ID rozszerzenia**: `ms-windows-ai-studio.windows-ai-studio`

**Metody instalacji**:
1. **VS Code Marketplace**: Wyszukaj "AI Toolkit" w widoku Extensions
2. **Wiersz poleceń**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Bezpośrednia instalacja**: Pobierz z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Wymagania wstępne dla rozwoju Edge AI
- **Visual Studio Code**: Zalecana najnowsza wersja
- **Środowisko Python**: Python 3.8+ z wymaganymi bibliotekami AI
- **ONNX Runtime** (opcjonalnie): Do wnioskowania modeli ONNX
- **Ollama** (opcjonalnie): Do lokalnego serwowania modeli
- **
2. Generowanie początkowych promptów na podstawie opisów w języku naturalnym  
3. Iteracja i udoskonalanie promptów w oparciu o odpowiedzi modelu  
4. Integracja narzędzi MCP w celu zwiększenia możliwości agentów  

#### Krok 3: Testowanie i ocena  
1. Użyj **Bulk Run**, aby przetestować wiele promptów na wybranych modelach  
2. Uruchom agentów z przypadkami testowymi, aby zweryfikować funkcjonalność  
3. Oceń dokładność i wydajność za pomocą wbudowanych lub niestandardowych metryk  
4. Porównaj różne modele i konfiguracje  

#### Krok 4: Dostosowanie i optymalizacja  
1. Dostosuj modele do specyficznych przypadków użycia na krawędzi  
2. Zastosuj dostosowanie do specyficznych dziedzin  
3. Optymalizuj pod kątem ograniczeń wdrożeniowych na krawędzi  
4. Wersjonuj i porównuj różne konfiguracje agentów  

#### Krok 5: Przygotowanie do wdrożenia  
1. Generuj kod gotowy do produkcji za pomocą Agent Builder  
2. Skonfiguruj połączenia serwera MCP do użytku produkcyjnego  
3. Przygotuj pakiety wdrożeniowe dla urządzeń na krawędzi  
4. Skonfiguruj metryki monitorowania i oceny  

## Przykłady dla AI Toolkit  

Wypróbuj nasze przykłady  
[Przykłady AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) zostały zaprojektowane, aby pomóc programistom i badaczom w eksploracji i wdrażaniu rozwiązań AI w efektywny sposób.  

Nasze przykłady obejmują:  

Kod przykładowy: Gotowe przykłady demonstrujące funkcjonalności AI, takie jak trenowanie, wdrażanie czy integracja modeli z aplikacjami.  
Dokumentacja: Przewodniki i samouczki pomagające użytkownikom zrozumieć funkcje AI Toolkit i sposób ich użycia.  
Wymagania wstępne  

- Visual Studio Code  
- AI Toolkit dla Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Najlepsze praktyki w rozwoju Edge AI  

### Wybór modelu  
- **Ograniczenia rozmiaru**: Wybierz modele, które mieszczą się w ograniczeniach pamięci docelowych urządzeń  
- **Szybkość wnioskowania**: Priorytetem są modele z szybkim czasem wnioskowania dla aplikacji w czasie rzeczywistym  
- **Kompromisy w dokładności**: Zrównoważ dokładność modelu z ograniczeniami zasobów  
- **Kompatybilność formatu**: Preferuj formaty ONNX lub zoptymalizowane pod kątem sprzętu dla wdrożeń na krawędzi  

### Techniki optymalizacji  
- **Kwantyzacja**: Użyj kwantyzacji INT8 lub INT4, aby zmniejszyć rozmiar modelu i poprawić szybkość  
- **Przycinanie**: Usuń niepotrzebne parametry modelu, aby zmniejszyć wymagania obliczeniowe  
- **Destylacja wiedzy**: Twórz mniejsze modele, które zachowują wydajność większych  
- **Przyspieszenie sprzętowe**: Wykorzystaj NPU, GPU lub specjalistyczne akceleratory, jeśli są dostępne  

### Przebieg rozwoju  
- **Testowanie iteracyjne**: Testuj często w warunkach podobnych do tych na krawędzi podczas rozwoju  
- **Monitorowanie wydajności**: Ciągle monitoruj wykorzystanie zasobów i szybkość wnioskowania  
- **Kontrola wersji**: Śledź wersje modeli i ustawienia optymalizacji  
- **Dokumentacja**: Dokumentuj wszystkie decyzje optymalizacyjne i kompromisy wydajności  

### Rozważania dotyczące wdrożenia  
- **Monitorowanie zasobów**: Monitoruj pamięć, CPU i zużycie energii w produkcji  
- **Strategie awaryjne**: Wdrażaj mechanizmy awaryjne na wypadek awarii modelu  
- **Mechanizmy aktualizacji**: Planuj aktualizacje modeli i zarządzanie wersjami  
- **Bezpieczeństwo**: Wdrażaj odpowiednie środki bezpieczeństwa dla aplikacji Edge AI  

## Integracja z frameworkami Edge AI  

### ONNX Runtime  
- **Wdrożenie międzyplatformowe**: Wdrażaj modele ONNX na różnych platformach krawędziowych  
- **Optymalizacja sprzętowa**: Wykorzystaj optymalizacje specyficzne dla sprzętu w ONNX Runtime  
- **Wsparcie mobilne**: Używaj ONNX Runtime Mobile dla aplikacji na smartfony i tablety  
- **Integracja IoT**: Wdrażaj na urządzeniach IoT za pomocą lekkich dystrybucji ONNX Runtime  

### Windows ML  
- **Urządzenia Windows**: Optymalizuj dla urządzeń krawędziowych i komputerów z systemem Windows  
- **Przyspieszenie NPU**: Wykorzystaj Neural Processing Units na urządzeniach Windows  
- **DirectML**: Używaj DirectML do przyspieszenia GPU na platformach Windows  
- **Integracja UWP**: Integruj z aplikacjami Universal Windows Platform  

### TensorFlow Lite  
- **Optymalizacja mobilna**: Wdrażaj modele TensorFlow Lite na urządzeniach mobilnych i wbudowanych  
- **Delegaty sprzętowe**: Używaj specjalistycznych delegatów sprzętowych do przyspieszenia  
- **Mikrokontrolery**: Wdrażaj na mikrokontrolerach za pomocą TensorFlow Lite Micro  
- **Wsparcie międzyplatformowe**: Wdrażaj na Androidzie, iOS i wbudowanym systemie Linux  

### Azure IoT Edge  
- **Hybryda chmura-krawędź**: Łącz trenowanie w chmurze z wnioskowaniem na krawędzi  
- **Wdrożenie modułów**: Wdrażaj modele AI jako moduły IoT Edge  
- **Zarządzanie urządzeniami**: Zdalnie zarządzaj urządzeniami krawędziowymi i aktualizacjami modeli  
- **Telemetria**: Zbieraj dane o wydajności i metryki modeli z wdrożeń na krawędzi  

## Zaawansowane scenariusze Edge AI  

### Wdrożenie wielu modeli  
- **Zespoły modeli**: Wdrażaj wiele modeli dla poprawy dokładności lub redundancji  
- **Testy A/B**: Testuj różne modele jednocześnie na urządzeniach krawędziowych  
- **Dynamiczny wybór**: Wybieraj modele na podstawie aktualnych warunków urządzenia  
- **Dzielenie zasobów**: Optymalizuj wykorzystanie zasobów między wieloma wdrożonymi modelami  

### Federacyjne uczenie  
- **Rozproszone trenowanie**: Trenuj modele na wielu urządzeniach krawędziowych  
- **Zachowanie prywatności**: Przechowuj dane treningowe lokalnie, jednocześnie dzieląc się ulepszeniami modeli  
- **Uczenie się w grupie**: Umożliwiaj urządzeniom uczenie się na podstawie wspólnych doświadczeń  
- **Koordynacja krawędź-chmura**: Koordynuj uczenie się między urządzeniami krawędziowymi a infrastrukturą chmurową  

### Przetwarzanie w czasie rzeczywistym  
- **Przetwarzanie strumieniowe**: Przetwarzaj ciągłe strumienie danych na urządzeniach krawędziowych  
- **Wnioskowanie o niskim opóźnieniu**: Optymalizuj pod kątem minimalnego opóźnienia wnioskowania  
- **Przetwarzanie wsadowe**: Efektywnie przetwarzaj partie danych na urządzeniach krawędziowych  
- **Przetwarzanie adaptacyjne**: Dostosowuj przetwarzanie na podstawie aktualnych możliwości urządzenia  

## Rozwiązywanie problemów w rozwoju Edge AI  

### Typowe problemy  
- **Ograniczenia pamięci**: Model zbyt duży dla pamięci docelowego urządzenia  
- **Szybkość wnioskowania**: Wnioskowanie modelu zbyt wolne dla wymagań czasu rzeczywistego  
- **Pogorszenie dokładności**: Optymalizacja obniża dokładność modelu w nieakceptowalnym stopniu  
- **Kompatybilność sprzętowa**: Model niekompatybilny z docelowym sprzętem  

### Strategie debugowania  
- **Profilowanie wydajności**: Używaj funkcji śledzenia AI Toolkit, aby zidentyfikować wąskie gardła  
- **Monitorowanie zasobów**: Monitoruj pamięć i użycie CPU podczas rozwoju  
- **Testowanie stopniowe**: Testuj optymalizacje stopniowo, aby zidentyfikować problemy  
- **Symulacja sprzętu**: Używaj narzędzi deweloperskich do symulacji docelowego sprzętu  

### Rozwiązania optymalizacyjne  
- **Dalsza kwantyzacja**: Zastosuj bardziej agresywne techniki kwantyzacji  
- **Architektura modelu**: Rozważ różne architektury modeli zoptymalizowane dla krawędzi  
- **Optymalizacja wstępnego przetwarzania**: Optymalizuj wstępne przetwarzanie danych dla ograniczeń krawędziowych  
- **Optymalizacja wnioskowania**: Używaj optymalizacji wnioskowania specyficznych dla sprzętu  

## Zasoby i kolejne kroki  

### Oficjalna dokumentacja  
- [Dokumentacja dla deweloperów AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Przewodnik instalacji i konfiguracji](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentacja aplikacji inteligentnych VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentacja Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Społeczność i wsparcie  
- [Repozytorium GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemy i prośby o funkcje na GitHub](https://aka.ms/AIToolkit/feedback)  
- [Społeczność Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace rozszerzeń VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Zasoby techniczne  
- [Dokumentacja ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentacja Ollama](https://ollama.ai/)  
- [Dokumentacja Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentacja Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Ścieżki edukacyjne  
- [Kurs podstaw Edge AI](../Module01/README.md)  
- [Przewodnik po małych modelach językowych](../Module02/README.md)  
- [Strategie wdrożeniowe na krawędzi](../Module03/README.md)  
- [Rozwój Edge AI na Windows](./windowdeveloper.md)  

### Dodatkowe zasoby  
- **Statystyki repozytorium**: Ponad 1,8k gwiazdek, ponad 150 forków, ponad 18 współtwórców  
- **Licencja**: Licencja MIT  
- **Bezpieczeństwo**: Obowiązują zasady bezpieczeństwa Microsoft  
- **Telemetria**: Respektuje ustawienia telemetrii VS Code  

## Podsumowanie  

AI Toolkit dla Visual Studio Code to kompleksowa platforma do nowoczesnego rozwoju AI, oferująca usprawnione możliwości rozwoju agentów, które są szczególnie wartościowe dla aplikacji Edge AI. Dzięki rozbudowanemu katalogowi modeli wspierającemu dostawców takich jak Anthropic, OpenAI, GitHub i Google, w połączeniu z lokalnym wykonaniem za pomocą ONNX i Ollama, narzędzie oferuje elastyczność potrzebną dla różnorodnych scenariuszy wdrożeniowych na krawędzi.  

Siła narzędzia tkwi w jego zintegrowanym podejściu—od odkrywania modeli i eksperymentowania w Playground, przez zaawansowany rozwój agentów z Prompt Builder, kompleksowe możliwości oceny, aż po bezproblemową integrację narzędzi MCP. Dla deweloperów Edge AI oznacza to szybkie prototypowanie i testowanie agentów AI przed wdrożeniem na krawędzi, z możliwością szybkiej iteracji i optymalizacji dla środowisk o ograniczonych zasobach.  

Kluczowe zalety dla rozwoju Edge AI obejmują:  
- **Szybkie eksperymentowanie**: Testuj modele i agentów szybko przed wdrożeniem na krawędzi  
- **Elastyczność wielodostawców**: Dostęp do modeli z różnych źródeł w celu znalezienia optymalnych rozwiązań na krawędzi  
- **Rozwój lokalny**: Testuj z ONNX i Ollama dla rozwoju offline i ochrony prywatności  
- **Gotowość produkcyjna**: Generuj kod gotowy do produkcji i integruj z zewnętrznymi narzędziami za pomocą MCP  
- **Kompleksowa ocena**: Używaj wbudowanych i niestandardowych metryk do walidacji wydajności Edge AI  

W miarę jak AI coraz bardziej zmierza w kierunku scenariuszy wdrożeniowych na krawędzi, AI Toolkit dla VS Code zapewnia środowisko rozwoju i przepływ pracy potrzebne do budowy, testowania i optymalizacji inteligentnych aplikacji dla środowisk o ograniczonych zasobach. Niezależnie od tego, czy rozwijasz rozwiązania IoT, mobilne aplikacje AI, czy systemy inteligencji wbudowanej, zestaw funkcji narzędzia i zintegrowany przepływ pracy wspierają cały cykl rozwoju Edge AI.  

Dzięki ciągłemu rozwojowi i aktywnej społeczności (ponad 1,8k gwiazdek na GitHub), AI Toolkit pozostaje na czele narzędzi rozwojowych AI, nieustannie ewoluując, aby sprostać potrzebom współczesnych deweloperów AI budujących dla scenariuszy wdrożeniowych na krawędzi.  

[Next Foundry Local](./foundrylocal.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.