<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:35:48+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "pl"
}
-->
# 🎙️ Warsztaty The AI Podcast Studio

> 🌏 [中文版 (wersja chińska)](translation/zh-cn/README.md)

![logo](../../../translated_images/pl/logo.8711e39dc8257d7b.png)

## Twoja Misja

Witamy w **The AI Podcast Studio**! Zaraz uruchomisz własny podcast technologiczny o nazwie "Future Bytes" — ale jest haczyk: zbudujesz zespół produkcyjny napędzany AI, który pomoże Ci go stworzyć. Koniec z godzinami spędzonymi na researchu, pisaniu scenariuszy i montażu audio. Zamiast tego zakodujesz swoją drogę do zostania producentem podcastu z supermocami AI.

## Historia

Wyobraź sobie: Ty i Twoi znajomi chcecie zacząć podcast o najciekawszych trendach technologicznych, ale wszyscy są zajęci szkołą, pracą albo po prostu życiem. A co, gdybyś mógł zbudować zespół agentów AI, którzy wykonają ciężką pracę? Jeden agent bada tematy, drugi pisze angażujące scenariusze, a trzeci zamienia tekst w naturalnie brzmiące rozmowy. Brzmi jak science fiction? Zróbmy z tego rzeczywistość.

## Czego się nauczysz

Pod koniec tych warsztatów nauczysz się jak:
- 🤖 Uruchomić własny lokalny model AI (bez kosztów API, bez zależności od chmury!)
- 🔧 Budować wyspecjalizowanych agentów AI, którzy faktycznie ze sobą współpracują
- 🎬 Stworzyć kompletny proces produkcji podcastu od pomysłu do audio

## Twoja Podróż: Trzy Aktów

![arch](../../../translated_images/pl/arch.5965fe504e4a3a93.png)

Jak w każdej dobrej historii, mamy trzy akty. Każdy z nich buduje Twoje AI podcast studio krok po kroku:

| Odcinek | Twoja Misja | Co Się Wydarzy | Odkryte Umiejętności |
|---------|-------------|----------------|----------------------|
| **Akt 1** | [Poznaj swoich asystentów AI](md/01.BuildAIAgentWithSLM.md) | Odkrywasz, jak tworzyć agentów AI, którzy potrafią rozmawiać, przeszukiwać sieć i rozwiązywać problemy. Pomyśl o nich jak o stażystach badawczych, którzy nigdy nie śpią. | 🎯 Zbuduj swojego pierwszego agenta<br>🛠️ Dodaj mu supermoce (narzędzia!)<br>🧠 Naucz go myśleć<br>🌐 Połącz z internetem |
| **Akt 2** | [Złóż swój zespół produkcyjny](md/02.AIAgentOrchestrationAndWorkflows.md) | Teraz robi się ciekawie! Skoordynujesz wielu agentów AI, aby współpracowali jak prawdziwy zespół podcastowy. Jeden bada, drugi pisze, Ty zatwierdzasz — współpraca to klucz. | 🎭 Koordynuj wielu agentów<br>🔄 Buduj przepływy zatwierdzania<br>🖥️ Testuj za pomocą interfejsu DevUI<br>✋ Zachowaj kontrolę ludzi |
| **Akt 3** | [Ożyw swój podcast](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finał! Zamień swoje tekstowe scenariusze w prawdziwe podcastowe audio z realistycznymi głosami i naturalnymi rozmowami. Twój podcast "Future Bytes" jest gotowy do wysłania! | 🎤 Magia zamiany tekstu na mowę<br>👥 Wiele głosów prelegentów<br>⏱️ Długie formy audio<br>🚀 Pełna automatyzacja |

Każdy akt odblokowuje nowe możliwości. Jeśli jesteś odważny, możesz pominąć kilka kroków, ale zalecamy podążać za historią!

## Wymagania Środowiskowe

Te warsztaty wspierają różne środowiska sprzętowe:
- **CPU**: Odpowiednie do testowania i małych zastosowań
- **GPU**: Zalecane do produkcji, znacznie przyspiesza działanie
- **NPU**: Wspiera przyspieszenie jednostek przetwarzania neuronowego nowej generacji

## Czego Będziesz Potrzebować

### Lista oprogramowania ✅
- **Python 3.10+** (Twój język programowania)
- **Ollama** (Uruchamia modele AI na Twoim komputerze)
- **VS Code** (Twój edytor kodu)
- **Rozszerzenie Python** (Ulepsza VS Code)
- **Git** (Do pobierania kodu)

### Sprawdzenie sprzętu 💻
- **Czy mogę to uruchomić?**: 8GB RAM, 10GB wolnego miejsca (działa, ale może być wolno)
- **Idealna konfiguracja**: 16GB+ RAM, przyzwoite GPU (płynna praca!)
- **Masz NPU?**: Jeszcze lepiej! Nowa generacja wydajności odblokowana 🚀

## Skonfiguruj swoje Studio 🎬

### Krok 1: Python Power-Up

Upewnij się, że masz Pythona 3.10 lub nowszego:

```bash
python --version
# Powinno pokazywać Python 3.10.x lub wyższą wersję
```

Nie masz Pythona? Pobierz go ze [strony python.org](https://python.org) — jest darmowy!

### Krok 2: Pobierz Ollamę (Twojego Uruchamiacz AI)

Wejdź na [ollama.ai](https://ollama.ai) i pobierz Ollamę dla swojego systemu operacyjnego. To silnik, który uruchamia Twoje modele AI lokalnie.

Sprawdź, czy działa:

```bash
ollama --version
```

### Krok 3: Pobierz swój mózg AI 🧠

Czas pobrać model Qwen-3-8B (to jak zatrudnienie pierwszego asystenta AI):

```bash
ollama pull qwen3:8b
```

*To może potrwać kilka minut. Idealny moment na kawę! ☕*

### Krok 4: Skonfiguruj VS Code

Pobierz [Visual Studio Code](https://code.visualstudio.com/), jeśli jeszcze go nie masz. To najlepszy edytor kodu (dowieziemy to do końca 😄).

### Krok 5: Rozszerzenie Python

W VS Code:
1. Naciśnij `Ctrl+Shift+X` (lub `Cmd+Shift+X` na Macu)
2. Wyszukaj "Python"
3. Zainstaluj oficjalne rozszerzenie Microsoftu dla Pythona

### Krok 6: Gotowy! 🎉

Na serio, jesteś gotowy do działania. Zbudujmy trochę magii AI!

### Krok 7: Zainstaluj Microsoft Agent Framework i Pakiety 📦

Zainstaluj wszystkie potrzebne zależności do warsztatów:

```bash
pip install -r ./Installations/requirements.txt -U
```

*To zainstaluje Microsoft Agent Framework i wszystkie niezbędne pakiety. Zaparz sobie kawę — pierwsza instalacja może chwilę potrwać! ☕*

## Instrukcje Warsztatowe

Szczegółowa struktura projektu, kroki konfiguracji i metody uruchomienia będą tłumaczone krok po kroku podczas warsztatów.

## Rozwiązywanie Problemów (Gdy Coś Idzie Nie Tak) 🔧

### „Ugh, pobieranie modelu trwa wieki!”
**Naprawa**: Użyj VPN lub skonfiguruj Ollamę z mirror source. Czasami internet nas nie lubi.

### „Mój komputer pada! Brak pamięci!”
**Naprawa**: Przełącz na mniejszy model lub dostosuj ustawienie `num_ctx`, aby zużywać mniej pamięci. Pomyśl o tym jak o diecie dla Twojego AI.

### „Mogę to przyspieszyć na moim GPU?”
**Naprawa**: Ollama automatycznie wykrywa GPU! Upewnij się tylko, że masz zaktualizowane sterowniki GPU. Darmowy boost prędkości! 🏎️

## Dodatkowe Zasoby (Dla Ciekawych) 📚

- [Dokumentacja Ollama](https://github.com/ollama/ollama) — Dogłębne informacje o lokalnych modelach AI
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Dowiedz się więcej o budowaniu zespołów agentów
- [Informacje o modelu Qwen](https://qwenlm.github.io/) — Poznaj mózg swojego asystenta AI

## Licencja

MIT License — Buduj fajne rzeczy, dziel się nimi, ulepszaj świat! 🌍

## Chcesz się Zaangażować?

Znalazłeś błąd? Masz pomysł? Zgłoś Issue lub PR! Kochamy społeczność. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło wiarygodne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->