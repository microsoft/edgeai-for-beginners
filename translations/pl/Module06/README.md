# Rozdział 06: Systemy Agentowe SLM: Kompleksowy Przegląd

Krajobraz sztucznej inteligencji przechodzi fundamentalną transformację, gdy przechodzimy od prostych chatbotów do zaawansowanych agentów AI opartych na Małych Modelach Językowych (SLM). Ten kompleksowy przewodnik bada trzy kluczowe aspekty nowoczesnych systemów agentowych SLM: podstawowe koncepcje i strategie wdrożeniowe, możliwości wywoływania funkcji oraz rewolucyjną integrację Model Context Protocol (MCP).

## [Sekcja 1: Podstawy Agentów AI i Małych Modeli Językowych](./01.IntroduceAgent.md)

Pierwsza sekcja ustanawia podstawowe zrozumienie agentów AI i Małych Modeli Językowych, wskazując rok 2025 jako rok agentów AI, po erze chatbotów w 2023 roku i boomie na copiloty w 2024 roku. Sekcja wprowadza **systemy agentowe AI**, które myślą, rozumują, planują, korzystają z narzędzi i wykonują zadania przy minimalnym wkładzie człowieka.

### Kluczowe Koncepcje:
- **Ramowa Klasyfikacja Agentów**: Od prostych agentów reaktywnych po agentów uczących się, oferując kompleksową taksonomię dla różnych scenariuszy obliczeniowych
- **Podstawy SLM**: Definicja Małych Modeli Językowych jako modeli z mniej niż 10 miliardami parametrów, które mogą wykonywać praktyczne wnioskowanie na urządzeniach konsumenckich
- **Zaawansowane Strategie Optymalizacji**: Omówienie wdrożenia w formacie GGUF, technik kwantyzacji (Q4_K_M, Q5_K_S, Q8_0) oraz frameworków zoptymalizowanych pod kątem urządzeń brzegowych, takich jak Llama.cpp i Apple MLX
- **Porównanie SLM vs LLM**: Pokazanie redukcji kosztów o 10-30× dzięki SLM przy jednoczesnym zachowaniu skuteczności dla 70-80% typowych zadań agentowych

Sekcja kończy się praktycznymi strategiami wdrożeniowymi z użyciem Ollama, VLLM i rozwiązań brzegowych Microsoftu, ustanawiając SLM jako przyszłość efektywnego kosztowo i prywatnego wdrażania agentów AI.

## [Sekcja 2: Wywoływanie Funkcji w Małych Modelach Językowych](./02.FunctionCalling.md)

Druga sekcja zagłębia się w **możliwości wywoływania funkcji**, mechanizm, który przekształca statyczne modele językowe w dynamiczne agentów AI zdolnych do interakcji w rzeczywistym świecie. Ten techniczny przewodnik szczegółowo opisuje cały proces od wykrywania intencji po integrację odpowiedzi.

### Kluczowe Obszary Implementacji:
- **Systematyczny Przepływ Pracy**: Szczegółowe omówienie integracji narzędzi, definicji funkcji, wykrywania intencji, generowania wyjścia JSON i zewnętrznego wykonania
- **Implementacje Specyficzne dla Platformy**: Kompleksowe przewodniki dla Phi-4-mini z Ollama, wywoływania funkcji Qwen3 oraz integracji Microsoft Foundry Local
- **Zaawansowane Przykłady**: Systemy współpracy wieloagentowej, dynamiczny wybór narzędzi i wzorce integracji w przedsiębiorstwach z kompleksowym obsługiwaniem błędów
- **Rozważania Produkcyjne**: Ograniczanie szybkości, rejestrowanie audytów, środki bezpieczeństwa i strategie optymalizacji wydajności

Ta sekcja dostarcza zarówno teoretycznego zrozumienia, jak i praktycznych wzorców implementacji, umożliwiając programistom budowanie solidnych systemów wywoływania funkcji, które mogą obsługiwać wszystko, od prostych wywołań API po złożone wieloetapowe przepływy pracy w przedsiębiorstwach.

## [Sekcja 3: Integracja Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Ostatnia sekcja wprowadza **Model Context Protocol (MCP)**, rewolucyjny framework, który standaryzuje sposób, w jaki modele językowe współdziałają z zewnętrznymi narzędziami i systemami. Sekcja pokazuje, jak MCP tworzy pomost między modelami AI a rzeczywistością poprzez dobrze zdefiniowane protokoły.

### Najważniejsze Elementy Integracji:
- **Architektura Protokołu**: Warstwowy projekt systemu obejmujący warstwy aplikacji, klienta LLM, klienta MCP i przetwarzania narzędzi
- **Wsparcie dla Wielu Backendów**: Elastyczna implementacja wspierająca zarówno Ollama (rozwój lokalny), jak i vLLM (produkcja)
- **Protokoły Połączeń**: Tryb STDIO dla bezpośredniej komunikacji procesów oraz tryb SSE dla strumieniowania opartego na HTTP
- **Zastosowania w Rzeczywistości**: Automatyzacja webowa, przetwarzanie danych i przykłady integracji API z kompleksowym obsługiwaniem błędów

Integracja MCP pokazuje, jak SLM mogą być wzbogacone o zewnętrzne możliwości, kompensując ich mniejszą liczbę parametrów poprzez zwiększoną funkcjonalność, jednocześnie zachowując korzyści lokalnego wdrożenia i efektywności zasobów.

## Strategiczne Implikacje

Razem te trzy sekcje przedstawiają kompleksowy framework do zrozumienia i wdrażania systemów agentowych SLM. Ewolucja od podstawowych koncepcji przez wywoływanie funkcji do integracji MCP pokazuje wyraźną ścieżkę w kierunku demokratyzacji wdrożeń AI, gdzie:

- **Efektywność spotyka się z możliwościami** dzięki zoptymalizowanym małym modelom
- **Efektywność kosztowa** umożliwia szeroką adopcję
- **Standaryzowane protokoły** zapewniają interoperacyjność
- **Lokalne wdrożenie** chroni prywatność i redukuje opóźnienia

Ten postęp reprezentuje nie tylko technologiczny rozwój, ale także zmianę paradygmatu w kierunku bardziej dostępnych, efektywnych i praktycznych systemów AI, które mogą działać skutecznie w środowiskach o ograniczonych zasobach, jednocześnie dostarczając zaawansowane możliwości agentowe.

Połączenie SLM z zaawansowanymi strategiami wdrożeniowymi, solidnym wywoływaniem funkcji i standaryzowanymi protokołami integracji narzędzi pozycjonuje te systemy jako fundament dla następnej generacji agentów AI, którzy zmienią sposób, w jaki wchodzimy w interakcję ze sztuczną inteligencją i korzystamy z jej możliwości w różnych branżach i zastosowaniach.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.