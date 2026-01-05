<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:50:15+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "cs"
}
-->
# 🎙️ Workshop AI Podcast Studio

> 🌏 [中文版 (Čínská verze)](translation/zh-cn/README.md)

![logo](../../../translated_images/logo.8711e39dc8257d7b.cs.png)

## Tvůj Úkol

Vítej v **The AI Podcast Studio**! Chystáš se spustit svůj vlastní tech podcast nazvaný "Future Bytes" — ale tady je ten zvrat: vybuduješ produkční tým poháněný AI, který ti s tvorbou pomůže. Už žádné nekonečné hodiny výzkumu, psaní scénářů a úprav zvuku. Místo toho si naprogramuješ cestu stát se producentem podcastu se super schopnostmi AI.

## Příběh

Představ si tohle: Ty a tvoji přátelé chcete začít podcast o nejzajímavějších technologických trendech, ale všichni jsou zaneprázdnění školou, prací nebo prostě životem. Co kdybys mohl vytvořit tým AI agentů, kteří dělají tu těžkou práci? Jeden agent vyhledává témata, druhý píše poutavé scénáře a třetí převádí text do přirozeně znějících rozhovorů. Zní to jako sci-fi? Pojďme to udělat skutečností.

## Co Se Naučíš

Na konci tohoto workshopu budeš umět:
- 🤖 Nasadit svůj vlastní lokální AI model (žádné náklady na API, žádná závislost na cloudu!)
- 🔧 Vytvořit specializované AI agenty, kteří spolu skutečně spolupracují
- 🎬 Vytvořit kompletní produkční pipeline podcastu od nápadu až po audio

## Tvoje Cesta: Tři Akté

![arch](../../../translated_images/arch.5965fe504e4a3a93.cs.png)

Jako v každém dobrém příběhu máme tři jednání. Každé postupně staví tvé AI podcastové studio:

| Epizoda | Tvoje Výzva | Co Se Děje | Odemčené Dovednosti |
|---------|-------------|------------|--------------------|
| **Akt 1** | [Seznam se se svými AI asistenty](md/01.BuildAIAgentWithSLM.md) | Objevíš, jak vytvořit AI agenty, kteří dokážou chatovat, vyhledávat na webu a dokonce řešit problémy. Představ si je jako své výzkumné stážisty, kteří nikdy nespí. | 🎯 Vytvoř svůj první agent<br>🛠️ Dej mu super schopnosti (nástroje!)<br>🧠 Nauč ho přemýšlet<br>🌐 Připoj ho k internetu |
| **Akt 2** | [Sestav svůj produkční tým](md/02.AIAgentOrchestrationAndWorkflows.md) | Teď se to začne zajímavě! Budeš orchestrálně řídit více AI agentů, aby spolupracovali jako skutečný tým podcastu. Jeden dělá výzkum, druhý píše, ty schvaluješ — týmová práce je klíč. | 🎭 Koordinuj více agentů<br>🔄 Vytvářej schvalovací workflow<br>🖥️ Testuj s rozhraním DevUI<br>✋ Udržuj lidskou kontrolu |
| **Akt 3** | [Oživ svůj podcast](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finále! Přeměň své textové scénáře na skutečné audio podcastu s realistickými hlasy a přirozenými rozhovory. Tvůj podcast "Future Bytes" je připraven k vysílání! | 🎤 Kouzlo převodu textu na řeč<br>👥 Hlasy několika mluvčích<br>⏱️ Dlouhé audio<br>🚀 Plná automatizace |

Každý akt ti odemkne nové schopnosti. Pokud jsi odvážný, můžeš přeskočit dopředu, ale doporučujeme následovat příběh!

## Požadavky na Prostředí

Tento workshop podporuje různé hardwarové prostředí:
- **CPU**: Vhodné pro testování a menší nasazení
- **GPU**: Doporučeno pro produkční prostředí, výrazně zrychluje inferenci
- **NPU**: Podpora akcelerace nového typu jednotek pro neuronové zpracování

## Co Budeš Potřebovat

### Checklist softwaru ✅
- **Python 3.10+** (tvůj programovací jazyk)
- **Ollama** (spouští AI modely na tvém počítači)
- **VS Code** (tvůj editor kódu)
- **Rozšíření pro Python** (dělá VS Code chytřejším)
- **Git** (pro práci s kódem)

### Kontrola hardwaru 💻
- **Poběží to u mě?**: 8GB RAM, 10GB volného místa (funguje, ale může být pomalé)
- **Ideální nastavení**: 16GB+ RAM, slušná GPU (pohoda!)
- **Máš NPU?**: Ještě lepší! Odemkneš výkon příští generace 🚀

## Nastav si Studio 🎬

### Krok 1: Síla Pythonu

Ujisti se, že máš Python 3.10 nebo novější:

```bash
python --version
# Mělo by zobrazovat Python 3.10.x nebo vyšší
```

Nemáš Python? Stáhni si ho na [python.org](https://python.org) — je zdarma!

### Krok 2: Stáhni si Ollama (tvůj spouštěč AI modelů)

Navštiv [ollama.ai](https://ollama.ai) a stáhni Ollama pro svůj OS. Představ si to jako motor, který lokálně spouští tvé AI modely.

Zkontroluj, jestli je vše připraveno:

```bash
ollama --version
```

### Krok 3: Stáhni svůj AI mozek 🧠

Čas stáhnout model Qwen-3-8B (je to jako najmout si prvního AI asistenta):

```bash
ollama pull qwen3:8b
```

*To může chvíli trvat. Ideální čas na kávu! ☕*

### Krok 4: Nastav VS Code

Nainstaluj [Visual Studio Code](https://code.visualstudio.com/), pokud ho ještě nemáš. Je to nejlepší editor kódu na světě (soupeřím s tebou 😄).

### Krok 5: Rozšíření Python

Ve VS Code:
1. Stiskni `Ctrl+Shift+X` (nebo `Cmd+Shift+X` na Macu)
2. Vyhledej "Python"
3. Nainstaluj oficiální rozšíření od Microsoftu

### Krok 6: Jsi připraven! 🎉

Opravdu, jsi připraven tvořit AI kouzla!

### Krok 7: Nainstaluj Microsoft Agent Framework a související balíčky 📦

Nainstaluj všechny potřebné závislosti pro workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Tím se nainstaluje Microsoft Agent Framework a všechny potřebné balíčky. Dejte si kávu — první nastavení může pár minut trvat! ☕*

## Instrukce k Workshopu

Podrobná struktura projektu, konfigurační kroky a způsoby spuštění budou vysvětleny krok za krokem během workshopu.

## Řešení Problémů (Když Něco Nejde) 🔧

### „Ach jo, stahování modelu trvá nekonečně dlouho!“
**Řešení**: Použij VPN nebo nastav Ollama s alternativním zdrojem. Někdy internet prostě na nás zlobí.

### „Můj počítač zemře! Nemá dost paměti!“
**Řešení**: Přepni na menší model nebo uprav `num_ctx` nastavení, aby se spotřebovalo méně paměti. Představ si to jako dietu pro AI.

### „Mohu to zrychlit pomocí GPU?“
**Řešení**: Ollama automaticky detekuje GPU! Jen si zkontroluj, že máš aktuální ovladače. Rychlost zdarma! 🏎️

## Další Zdroje (Pro Zvědavé) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — Hloubkový pohled na lokální AI modely
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Více o tvorbě agentních týmů
- [Informace o modelu Qwen](https://qwenlm.github.io/) — Poznej mozek svého AI asistenta

## Licence

MIT Licence — Vytvářej super věci, sdílej je a dělej svět lepším! 🌍

## Chceš přispět?

Našel jsi chybu? Máš nápad? Napiš Issue nebo PR! Máme rádi komunitní spolupráci. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornění**:
Tento dokument byl přeložen pomocí služby pro překlad s umělou inteligencí [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace doporučujeme profesionální lidský překlad. Nepřebíráme odpovědnost za jakékoli nedorozumění nebo chybné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->