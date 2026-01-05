<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:39:32+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "pl"
}
-->
# 🎙️ Warsztaty AI Podcast Studio

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.pl.png)

## Twoje zadanie

Witamy w **AI Podcast Studio**! Wkrótce uruchomisz swój własny technologiczny podcast „Przyszłe Bajty” — ale jest haczyk: zbudujesz zespół produkcyjny napędzany AI, który pomoże Ci go stworzyć. Koniec z niekończącymi się badaniami, pisaniem skryptów i edycją audio. Zamiast tego nauczysz się programować i stać się producentem podcastów z supermocami AI.

## Tło historii

Wyobraź sobie: Ty i Twoi przyjaciele chcecie zacząć podcast o najfajniejszych trendach technologicznych, ale wszyscy jesteście zajęci nauką, pracą lub życiem. Co by było, gdybyś mógł zbudować zespół inteligentnych agentów AI, którzy wykonają ciężką pracę? Jeden agent zajmuje się badaniami, inny pisze angażujące skrypty, a trzeci zamienia tekst w naturalny, płynny dialog. Brzmi jak science fiction? Zamieńmy to w rzeczywistość.

## Czego się nauczysz

Na koniec tych warsztatów będziesz wiedzieć, jak:
- 🤖 Uruchomić własny lokalny model AI (bez opłat za API, bez zależności od chmury!)
- 🔧 Zbudować profesjonalnych agentów AI współpracujących w praktyce
- 🎬 Stworzyć pełny proces produkcji podcastu od pomysłu do audio

## Twoja podróż: trzy akty

Jak w każdej dobrej historii, mamy trzy akty. Każdy z nich stopniowo buduje Twoje AI Podcast Studio:

| Rozdział | Twoje zadanie | Co się stanie | Odblokowane umiejętności |
|---------|-----------|--------------|----------------|
| **Akt 1** | [Poznaj swoich asystentów AI](01.BuildAIAgentWithSLM.md) | Dowiesz się, jak stworzyć agentów AI, którzy potrafią rozmawiać, przeszukiwać internet, a nawet rozwiązywać problemy. Wyobraź sobie, że to niestrudzeni stażyści badawczy. | 🎯 Zbuduj swojego pierwszego agenta<br>🛠️ Wyposaż go w supermoce (narzędzia!)<br>🧠 Naucz go myśleć<br>🌐 Podłącz do internetu |
| **Akt 2** | [Zbuduj swój zespół produkcyjny](02.AIAgentOrchestrationAndWorkflows.md) | Teraz robi się interesująco! Zorganizujesz wielu agentów AI, którzy będą współpracować jak prawdziwy zespół podcastowy. Jeden badania, drugi pisze, Ty akceptujesz — współpraca prowadzi do sukcesu. | 🎭 Koordynacja wielu agentów<br>🔄 Budowa workflow z akceptacją<br>🖥️ Testowanie z interfejsem DevUI<br>✋ Zachowanie kontroli człowieka |
| **Akt 3** | [Ożyw swój podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Wielki finał! Zamienisz tekstowe skrypty w realistyczne podcasty z naturalnym głosem i dialogiem. Twój „Przyszły Bajt” jest gotowy do publikacji! | 🎤 Magia przekształcania tekstu w mowę<br>👥 Głosy wielu rozmówców<br>⏱️ Długie formaty audio<br>🚀 Pełna automatyzacja |

Każdy akt odblokowuje nowe umiejętności. Jeśli masz odwagę, możesz przeskakiwać, ale zalecamy uczyć się po kolei!

## Wymagania środowiskowe

Warsztaty obsługują różne środowiska sprzętowe:
- **CPU**: odpowiedni do testów i małych zastosowań
- **GPU**: polecany do produkcji, znacznie przyspiesza inferencję
- **NPU**: obsługuje akcelerację nowej generacji jednostek przetwarzania neuronowego

## Czego potrzebujesz

### Spis oprogramowania ✅
- **Python 3.10+** (Twój język programowania)
- **Ollama** (do uruchamiania modeli AI na Twoim komputerze)
- **VS Code** (Twój edytor kodu)
- **Rozszerzenie Python** (by VS Code był inteligentniejszy)
- **Git** (do pobierania kodu)

### Sprawdzenie sprzętu 💻
- **Czy mogę to uruchomić?**: 8 GB RAM, 10 GB wolnego miejsca (można, ale może być wolno)
- **Idealna konfiguracja**: 16 GB+ RAM, dobra karta GPU (płynne działanie!)
- **Masz NPU?**: To jeszcze lepiej! Odblokujesz możliwości nowej generacji 🚀

## Zbuduj swoje studio 🎬

### Krok 1: Upgrade Pythona

Upewnij się, że masz Pythona 3.10 lub nowszego:

```bash
python --version
# Powinna być wyświetlana wersja Python 3.10.x lub nowsza
```

Nie masz Pythona? Pobierz go z [python.org](https://python.org) — jest darmowy!

### Krok 2: Pobierz Ollamę (silnik do modeli AI)

Wejdź na [ollama.ai](https://ollama.ai) i pobierz Ollamę odpowiednią dla Twojego systemu operacyjnego. To silnik, który pozwoli Ci uruchamiać modele AI lokalnie.

Sprawdź, czy jest gotowa:

```bash
ollama --version
```

### Krok 3: Pobierz swój mózg AI 🧠

Czas na pobranie modelu Qwen-3-8B (tak jak zatrudnienie pierwszego asystenta AI):

```bash
ollama pull qwen3:8b
```

*To może zająć kilka minut. Idealny czas na kawę!☕*

### Krok 4: Skonfiguruj VS Code

Jeśli jeszcze go nie masz, pobierz [Visual Studio Code](https://code.visualstudio.com/). To najlepszy edytor kodu (nie przekonany? Sprawdź sam 😄).

### Krok 5: Rozszerzenie Python

W VS Code:
1. Naciśnij `Ctrl+Shift+X` (na Macu `Cmd+Shift+X`)
2. Wyszukaj „Python”
3. Zainstaluj oficjalne rozszerzenie Microsoft Python

### Krok 6: Gotowe! 🎉

Na serio, jesteś gotowy. Zbudujmy trochę magii AI!

### Krok 7: Zainstaluj Microsoft Agent Framework i potrzebne pakiety 📦

Zainstaluj wszystkie zależności wymagane w warsztatach:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Zainstaluje Microsoft Agent Framework oraz wszystkie potrzebne pakiety. W międzyczasie wypij kawę — pierwsza instalacja może chwilę potrwać!☕*

## Informacje o warsztatach

Szczegółowa struktura projektu, kroki konfiguracyjne i sposób uruchamiania będą omawiane stopniowo podczas warsztatów.

## Rozwiązywanie problemów (gdy coś pójdzie nie tak) 🔧

### „Ojej, pobieranie modelu trwa wieczność!”
**Rozwiązanie**: Użyj VPN lub skonfiguruj źródło mirror w Ollamie. Czasami sieć nie współpracuje.

### „Mój komputer laguje! Brak pamięci!”
**Rozwiązanie**: Przełącz na mniejszy model lub zmniejsz `num_ctx` by zużywać mniej pamięci. Pomyśl, że dajesz AI dietę.

### „Czy mogę użyć GPU, żeby działało szybciej?”
**Rozwiązanie**: Ollama automatycznie wykryje GPU! Po prostu upewnij się, że sterowniki GPU są aktualne. Darmowy zastrzyk prędkości! 🏎️

## Dodatkowe zasoby (dla ciekawskich) 📚

- [Dokumentacja Ollama](https://github.com/ollama/ollama) — głębsze zanurzenie w lokalne modele AI
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — dowiedz się więcej o budowaniu zespołów agentów
- [Informacje o modelu Qwen](https://qwenlm.github.io/) — poznaj mózg swojego asystenta AI

## Licencja

Licencja MIT — buduj fajne rzeczy, dziel się nimi i sprawiaj, że świat stanie się lepszy! 🌍

## Chcesz pomóc?

Znalazłeś błąd? Masz pomysł? Zgłoś Issue lub PR! Kochamy wspólnotę. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako wiążące źródło informacji. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego, ludzkiego tłumaczenia. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->