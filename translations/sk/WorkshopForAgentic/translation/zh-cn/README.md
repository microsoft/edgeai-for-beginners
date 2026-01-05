<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:54:47+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "sk"
}
-->
# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.sk.png)

## Tvoja úloha

Vitaj v **AI Podcast Studiu**! Práve spúšťaš vlastný technologický podcast „Budúce Bajty“ — ale tu je háčik: vytvoríš tím riadený AI, ktorý ti pomôže vytvoriť ho. Už žiadne nekonečné štúdium, písanie scenárov a úpravy zvuku. Namiesto toho sa staneš podcastovým tvorcom s AI superschopnosťami cez programovanie.

## Príbeh

Predstav si: chceš s priateľmi začať podcast o najlepších technologických trendoch, ale všetci sú zaneprázdnení štúdiom, prácou alebo životom. Čo keby si vytvoril tím AI agentov, ktorí spravia všetku ťažkú prácu? Jeden skúma témy, druhý píše pútavé scenáre, tretí premieňa text na prirodzene znejúci rozhovor. Znie to ako sci-fi? Poďme to urobiť skutočnosťou.

## Čo sa naučíš

Na konci tohto workshopu budeš vedieť:
- 🤖 Nasadiť vlastný lokálny AI model (bez poplatkov za API, bez závislosti na cloude!)
- 🔧 Vytvoriť profesionálnych AI agentov pracujúcich v spolupráci
- 🎬 Vytvoriť kompletný podcastový pracovný tok od nápadu po audio

## Tvoja cesta: Tri dejstvá

Ako v každom dobrom príbehu, máme tri dejstvá. Každé postupne vybuduje tvoje AI podcastové štúdio:

| Kapitola | Tvoja úloha | Čo sa deje | Odomknuté zručnosti |
|---------|-----------|--------------|----------------|
| **Prvé dejstvo** | [Spoznajte svojho AI asistenta](01.BuildAIAgentWithSLM.md) | Naučíš sa vytvoriť AI agentov, ktorí môžu chatovať, prehľadávať internet a riešiť problémy. Predstav ich ako nevyspatých výskumných stážistov. | 🎯 Vytvoriť svojho prvého agenta<br>🛠️ Dať mu superschopnosti (nástroje!)<br>🧠 Naučiť ho myslieť<br>🌐 Pripojiť ho k internetu |
| **Druhé dejstvo** | [Zostav si tím tvorby](02.AIAgentOrchestrationAndWorkflows.md) | Teraz sa to stáva zaujímavým! Naplánuješ viacero AI agentov, ktorí spolupracujú ako skutočný podcastový tím. Jeden skúma, druhý píše, ty schvaľuješ — tímová práca plní sny. | 🎭 Koordinovať viac agentov<br>🔄 Vytvoriť schvaľovací workflow<br>🖥️ Použiť DevUI na testovanie<br>✋ Zachovať ľudskú kontrolu |
| **Tretie dejstvo** | [Oživi svoj podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finále! Preveď svoj textový scenár na skutočné podcastové audio s realistickými hlasmi a prirodzeným dialógom. Tvoj podcast „Budúce Bajty“ je pripravený na vydanie! | 🎤 Magia text-to-speech<br>👥 Viacero rečníkov<br>⏱️ Dlhé formátové audio<br>🚀 Úplne automatizované |

Každé dejstvo odomyká nové schopnosti. Ak máš odvahu, môžeš preskakovať, ale odporúčame postupovať podľa poradia!

## Požiadavky na prostredie

Tento workshop podporuje rôzne hardvérové prostredia:
- **CPU**: vhodné pre testovanie a malé použitie
- **GPU**: odporúčané pre produkciu, výrazne zrýchľuje inferenciu
- **NPU**: podporuje akceleráciu novej generácie neurónových procesorov

## Čo potrebuješ

### Softvérový zoznam ✅
- **Python 3.10+** (tvoj programovací jazyk)
- **Ollama** (prevádzka AI modelov na tvojom zariadení)
- **VS Code** (tvoj kódový editor)
- **Python rozšírenie** (robí VS Code inteligentnejším)
- **Git** (na získavanie kódu)

### Kontrola hardvéru 💻
- **Môžem to spustiť?**: 8GB pamäte, 10GB voľného miesta (použiteľné, ale môže byť pomalé)
- **Ideálne nastavenie**: 16GB+ RAM, slušný GPU (plynulý chod!)
- **Máš NPU?**: ešte lepšie! Odomkni výkon novej generácie 🚀

## Nastav si svoje štúdio 🎬

### Krok 1: Aktualizuj Python

Uisti sa, že máš Python 3.10 alebo novšiu verziu:

```bash
python --version
# Mali by sa zobraziť Python 3.10.x alebo novšia verzia
```

Nemáš Python? Stiahni si ho na [python.org](https://python.org) — je zadarmo!

### Krok 2: Získaj Ollama (AI model runner)

Navštív [ollama.ai](https://ollama.ai) a stiahni Ollama pre svoj operačný systém. Predstav si to ako motor na lokálne spúšťanie AI modelov.

Skontroluj pripravenosť:

```bash
ollama --version
```

### Krok 3: Stiahni svoj AI mozog 🧠

Je čas získať model Qwen-3-8B (ako by si najal prvého AI asistenta):

```bash
ollama pull qwen3:8b
```

*Potrvá to niekoľko minút. Perfektný čas na kávu! ☕*

### Krok 4: Nastav VS Code

Ak ho ešte nemáš, stiahni si [Visual Studio Code](https://code.visualstudio.com/). Je to najlepší kódový editor (pochybuj, ak chceš 😄).

### Krok 5: Python rozšírenie

V VS Code:
1. Stlač `Ctrl+Shift+X` (Mac: `Cmd+Shift+X`)
2. Vyhľadaj „Python“
3. Nainštaluj oficiálne rozšírenie od Microsoftu

### Krok 6: Hotovo! 🎉

Naozaj, si pripravený. Poďme vytvoriť trochu AI mágie!

### Krok 7: Nainštaluj Microsoft Agent Framework a súvisiace balíčky 📦

Nainštaluj všetky závislosti potrebné pre workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Týmto nainštaluješ Microsoft Agent Framework a všetky potrebné balíčky. Daj si kávu — prvá inštalácia môže chvíľu trvať! ☕*

## Pokyny k workshopu

Podrobná štruktúra projektu, nastavenie a ako ho spustiť budú počas workshopu vysvetlené krok za krokom.

## Riešenie problémov (keď sa niečo pokazí) 🔧

### „Ach nie, sťahovanie modelu je príliš pomalé!“
**Riešenie**: Použi VPN alebo nakonfiguruj Ollama zrkadlový zdroj. Niekedy je sieť pomalá.

### „Môj počítač skoro padá! Pamäť nestačí!“
**Riešenie**: Prejdi na menší model alebo uprav `num_ctx` nastavenie na nižšiu pamäť. Predstav si to ako diétu pre tvoj AI.

### „Môžem použiť GPU, aby to bolo rýchlejšie?“
**Riešenie**: Ollama automaticky detekuje GPU! Len sa uisti, že máš najnovšie ovládače pre svoju grafickú kartu. Zdarma zrýchlenie! 🏎️

## Dodatočné zdroje (pre zvedavých) 📚

- [Dokumentácia Ollama](https://github.com/ollama/ollama) — hĺbkové info o lokálnych AI modeloch
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — viac o tvorbe tímov agentov
- [Informácie o modeli Qwen](https://qwenlm.github.io/) — spoznajte mozog svojho AI asistenta

## Licencia

MIT licencia — stavaj úžasné veci, zdieľaj ich a zlepši svet! 🌍

## Chceš prispieť?

Našiel si chybu? Máš nápad? Podaj Issue alebo PR! Milujeme komunitu. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->