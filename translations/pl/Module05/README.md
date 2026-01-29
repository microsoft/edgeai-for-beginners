# Rozdział 05: SLMOps - Kompleksowy przewodnik po operacjach na małych modelach językowych

## Przegląd

SLMOps (Small Language Model Operations) to rewolucyjne podejście do wdrażania AI, które kładzie nacisk na efektywność, opłacalność i możliwości obliczeń na krawędzi. Ten kompleksowy przewodnik obejmuje pełny cykl życia operacji SLM, od zrozumienia podstawowych koncepcji po wdrożenia gotowe do produkcji.

---

## [Sekcja 1: Wprowadzenie do SLMOps](./01.IntroduceSLMOps.md)

**Rewolucja w operacjach AI na krawędzi**

Ten podstawowy rozdział przedstawia zmianę paradygmatu z tradycyjnych operacji AI na dużą skalę na operacje na małych modelach językowych (SLMOps). Dowiesz się, jak SLMOps rozwiązuje kluczowe wyzwania związane z wdrażaniem AI na dużą skalę, jednocześnie zachowując efektywność kosztową i zgodność z zasadami prywatności.

**Czego się nauczysz:**
- Znaczenie i rola SLMOps w nowoczesnej strategii AI
- Jak małe modele językowe łączą wydajność z efektywnością zasobów
- Podstawowe zasady operacyjne, w tym inteligentne zarządzanie zasobami i architektura zorientowana na prywatność
- Wyzwania związane z wdrożeniem w rzeczywistych warunkach i ich rozwiązania
- Strategiczny wpływ na biznes i przewagi konkurencyjne

**Kluczowy wniosek:** SLMOps demokratyzuje wdrażanie AI, udostępniając zaawansowane możliwości przetwarzania języka organizacjom z ograniczoną infrastrukturą techniczną, umożliwiając szybsze cykle rozwoju i bardziej przewidywalne koszty operacyjne.

---

## [Sekcja 2: Destylacja modelu - od teorii do praktyki](./02.SLMOps-Distillation.md)

**Tworzenie efektywnych modeli poprzez transfer wiedzy**

Destylacja modelu to kluczowa technika pozwalająca na tworzenie mniejszych, bardziej efektywnych modeli, które zachowują wydajność swoich większych odpowiedników. Ten rozdział oferuje kompleksowy przewodnik po wdrażaniu procesów destylacji, które przenoszą wiedzę z dużych modeli nauczycieli do kompaktowych modeli uczniów.

**Czego się nauczysz:**
- Podstawowe koncepcje i korzyści płynące z destylacji modelu
- Dwustopniowy proces destylacji: generowanie danych syntetycznych i trening modelu ucznia
- Strategie wdrożeniowe z wykorzystaniem najnowocześniejszych modeli, takich jak DeepSeek V3 i Phi-4-mini
- Przykłady praktyczne destylacji w Azure ML
- Najlepsze praktyki w zakresie strojenia hiperparametrów i strategii oceny
- Studia przypadków pokazujące znaczące oszczędności kosztów i poprawę wydajności

**Kluczowy wniosek:** Destylacja modelu pozwala organizacjom osiągnąć 85% redukcji czasu wnioskowania i 95% zmniejszenia wymagań pamięciowych, zachowując 92% dokładności pierwotnego modelu, co czyni zaawansowane możliwości AI praktycznie wdrażalnymi.

---

## [Sekcja 3: Dostosowywanie - personalizacja modeli do konkretnych zadań](./03.SLMOps-Finetuing.md)

**Dostosowywanie modeli wstępnie wytrenowanych do unikalnych wymagań**

Dostosowywanie przekształca modele ogólnego przeznaczenia w specjalistyczne rozwiązania dostosowane do Twoich konkretnych przypadków użycia i dziedzin. Ten rozdział obejmuje wszystko, od podstawowej regulacji parametrów po zaawansowane techniki, takie jak LoRA i QLoRA, umożliwiające efektywną personalizację modeli.

**Czego się nauczysz:**
- Kompleksowy przegląd metodologii dostosowywania i ich zastosowań
- Różne typy dostosowywania: pełne dostosowywanie, dostosowywanie efektywne pod względem parametrów (PEFT) i podejścia specyficzne dla zadań
- Praktyczne wdrożenie z użyciem Microsoft Olive z przykładami
- Zaawansowane techniki, w tym trening z wieloma adapterami i optymalizacja hiperparametrów
- Najlepsze praktyki w zakresie przygotowania danych, konfiguracji treningu i zarządzania zasobami
- Typowe wyzwania i sprawdzone rozwiązania dla udanych projektów dostosowywania

**Kluczowy wniosek:** Dostosowywanie z narzędziami takimi jak Microsoft Olive pozwala organizacjom efektywnie dostosowywać modele wstępnie wytrenowane do specyficznych potrzeb, jednocześnie optymalizując wydajność i ograniczenia zasobów, czyniąc zaawansowane AI dostępne w różnych zastosowaniach.

---

## [Sekcja 4: Wdrożenie - implementacja modeli gotowych do produkcji](./04.SLMOps.Deployment.md)

**Wprowadzanie dostosowanych modeli do produkcji z Foundry Local**

Ostatni rozdział koncentruje się na kluczowej fazie wdrożenia, obejmując konwersję modeli, kwantyzację i konfigurację produkcyjną. Dowiesz się, jak wdrażać dostosowane modele kwantyzowane za pomocą Foundry Local, aby osiągnąć optymalną wydajność i wykorzystanie zasobów.

**Czego się nauczysz:**
- Kompletny proces konfiguracji środowiska i instalacji narzędzi
- Techniki konwersji modeli i kwantyzacji dla różnych scenariuszy wdrożeniowych
- Konfiguracja wdrożenia w Foundry Local z optymalizacjami specyficznymi dla modelu
- Metodologie benchmarkingu wydajności i walidacji jakości
- Rozwiązywanie typowych problemów związanych z wdrożeniem i strategie optymalizacji
- Najlepsze praktyki w zakresie monitorowania i utrzymania produkcji

**Kluczowy wniosek:** Odpowiednia konfiguracja wdrożenia z technikami kwantyzacji pozwala osiągnąć do 75% redukcji rozmiaru przy zachowaniu akceptowalnej jakości modelu, umożliwiając efektywne wdrożenia produkcyjne na różnych konfiguracjach sprzętowych.

---

## Rozpoczęcie pracy

Ten przewodnik został zaprojektowany, aby przeprowadzić Cię przez pełną podróż SLMOps, od zrozumienia podstawowych koncepcji po wdrożenia gotowe do produkcji. Każdy rozdział buduje na poprzednim, oferując zarówno teoretyczne zrozumienie, jak i praktyczne umiejętności wdrożeniowe.

Niezależnie od tego, czy jesteś data scientistem optymalizującym wdrożenie modelu, inżynierem DevOps wdrażającym operacje AI, czy liderem technicznym oceniającym SLMOps dla swojej organizacji, ten kompleksowy przewodnik dostarcza wiedzy i narzędzi potrzebnych do skutecznego wdrożenia operacji na małych modelach językowych.

**Gotowy, aby zacząć?** Rozpocznij od Rozdziału 1, aby zrozumieć podstawowe zasady SLMOps i zbudować fundament dla zaawansowanych technik wdrożeniowych omówionych w kolejnych rozdziałach.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.