<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:20:26+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "de"
}
-->
# 🎙️ Der AI Podcast Studio Workshop

> 🌏 [中文版 (Chinesische Version)](translation/zh-cn/README.md)

![logo](../../../translated_images/de/logo.8711e39dc8257d7b.png)

## Deine Mission

Willkommen bei **The AI Podcast Studio**! Du bist dabei, deinen eigenen Tech-Podcast namens "Future Bytes" zu starten — aber hier kommt der Clou: Du baust ein KI-gestütztes Produktionsteam, das dir bei der Erstellung hilft. Keine endlosen Stunden mehr mit Recherche, Skripterstellung und Audiobearbeitung. Stattdessen programmierst du dich zum Podcast-Produzenten mit KI-Superkräften.

## Die Geschichte

Stell dir vor: Du und deine Freunde wollt einen Podcast über die coolsten Tech-Trends starten, aber jeder ist mit Schule, Arbeit oder dem Leben beschäftigt. Was, wenn du ein Team von KI-Agenten zusammenstellen könntest, die die schwere Arbeit übernehmen? Ein Agent recherchiert Themen, der nächste schreibt spannende Skripte, und ein dritter verwandelt Text in natürlich klingende Gespräche. Klingt nach Sci-Fi? Lass es uns Wirklichkeit werden lassen.

## Was Du Lernen Wirst

Am Ende dieses Workshops weißt du, wie du:
- 🤖 Dein eigenes lokales KI-Modell einsetzt (keine API-Kosten, keine Cloud-Abhängigkeit!)
- 🔧 Spezialisierte KI-Agenten baust, die wirklich zusammenarbeiten
- 🎬 Eine komplette Podcast-Produktionspipeline von der Idee bis zum Audio erstellst

## Deine Reise: Drei Akte

![arch](../../../translated_images/de/arch.5965fe504e4a3a93.png)

Wie jede gute Geschichte besteht sie aus drei Akten. Jeder baut dein KI-Podcast-Studio Stück für Stück auf:

| Episode | Deine Aufgabe | Was passiert | Freigeschaltete Fähigkeiten |
|---------|---------------|--------------|-----------------------------|
| **Akt 1** | [Lerne deine KI-Assistenten kennen](md/01.BuildAIAgentWithSLM.md) | Du entdeckst, wie du KI-Agenten erschaffst, die chatten, im Web suchen und sogar Probleme lösen können. Denk an sie als deine unermüdlichen Recherche-Praktikanten. | 🎯 Baue deinen ersten Agenten<br>🛠️ Verleihe ihm Superkräfte (Werkzeuge!)<br>🧠 Bringe ihm Denken bei<br>🌐 Verbinde ihn mit dem Internet |
| **Akt 2** | [Stelle dein Produktionsteam zusammen](md/02.AIAgentOrchestrationAndWorkflows.md) | Jetzt wird es spannend! Du orchestrierst mehrere KI-Agenten, damit sie zusammenarbeiten wie ein echtes Podcast-Team. Einer recherchiert, einer schreibt, du gibst die Freigabe – Teamwork macht den Traum wahr. | 🎭 Koordiniere mehrere Agenten<br>🔄 Baue Freigabeworkflows<br>🖥️ Teste mit DevUI-Oberfläche<br>✋ Halte Menschen in der Kontrolle |
| **Akt 3** | [Bring deinen Podcast zum Leben](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Das Finale! Verwandle deine Textskripte in echten Podcast-Audio mit realistischen Stimmen und natürlichen Gesprächen. Dein "Future Bytes"-Podcast ist versandbereit! | 🎤 Text-zu-Sprache-Magie<br>👥 Mehrere Sprecherstimmen<br>⏱️ Langform-Audio<br>🚀 Vollautomatisierung |

Jeder Akt schaltet neue Fähigkeiten frei. Spring gerne vor, wenn du mutig bist, aber wir empfehlen, die Geschichte zu verfolgen!

## Systemanforderungen

Dieser Workshop unterstützt verschiedene Hardware-Umgebungen:
- **CPU**: Geeignet für Tests und kleine Nutzungen
- **GPU**: Empfohlen für Produktionsumgebungen, verbessert die Inferenzgeschwindigkeit erheblich
- **NPU**: Unterstützt Beschleunigung durch die nächste Generation neuronaler Verarbeitungseinheiten

## Was Du Brauchst

### Software-Checkliste ✅
- **Python 3.10+** (Deine Programmiersprache)
- **Ollama** (Führt KI-Modelle auf deinem Rechner aus)
- **VS Code** (Dein Code-Editor)
- **Python Extension** (Macht VS Code schlauer)
- **Git** (Um Code zu holen)

### Hardware-Check 💻
- **Kann ich das ausführen?**: 8GB RAM, 10GB freier Speicher (funktioniert, könnte aber langsam sein)
- **Ideale Ausstattung**: 16GB+ RAM, eine anständige GPU (läuft geschmeidig!)
- **NPU vorhanden?**: Noch besser! Leistung der nächsten Generation freigeschaltet 🚀

## Richte Dein Studio Ein 🎬

### Schritt 1: Python Power-Up

Stelle sicher, dass du Python 3.10 oder neuer installiert hast:

```bash
python --version
# Sollte Python 3.10.x oder höher anzeigen
```

Kein Python? Hol es dir kostenlos von [python.org](https://python.org)!

### Schritt 2: Hol dir Ollama (Deinen KI-Modell-Runner)

Gehe zu [ollama.ai](https://ollama.ai) und lade Ollama für dein Betriebssystem herunter. Stell es dir als Motor vor, der deine KI-Modelle lokal ausführt.

Prüfe, ob alles bereit ist:

```bash
ollama --version
```

### Schritt 3: Lade Dein KI-Gehirn herunter 🧠

Zeit, das Modell Qwen-3-8B zu holen (wie deinen ersten KI-Assistenten einstellen):

```bash
ollama pull qwen3:8b
```

*Das kann ein paar Minuten dauern. Perfekte Zeit für eine Kaffeepause! ☕*

### Schritt 4: Richte VS Code ein

Lade [Visual Studio Code](https://code.visualstudio.com/) herunter, wenn du es noch nicht hast. Es ist der beste Code-Editor (beweis mir das Gegenteil 😄).

### Schritt 5: Python Extension

In VS Code:
1. Drücke `Ctrl+Shift+X` (oder `Cmd+Shift+X` auf dem Mac)
2. Suche nach "Python"
3. Installiere die offizielle Python-Erweiterung von Microsoft

### Schritt 6: Du bist bereit! 🎉

Ernsthaft, jetzt kannst du loslegen. Lass uns AI-Magie bauen!

### Schritt 7: Installiere Microsoft Agent Framework und benötigte Pakete 📦

Installiere alle benötigten Abhängigkeiten für den Workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Dadurch werden Microsoft Agent Framework und alle nötigen Pakete installiert. Hol dir einen Kaffee – die Erstinstallation kann einige Minuten dauern! ☕*

## Workshop-Anleitung

Detaillierte Projektstruktur, Konfigurationsschritte und Ausführungsanweisungen werden während des Workshops Schritt für Schritt erläutert.

## Fehlerbehebung (Wenn mal was schiefgeht) 🔧

### "Ugh, der Modell-Download dauert ewig!"
**Lösung**: Nutze ein VPN oder konfiguriere Ollama mit einem Mirror-Server. Manchmal hat das Internet einfach keinen Spaß mit uns.

### "Mein Computer steigt aus! Kein Speicher mehr!"
**Lösung**: Wechsle zu einem kleineren Modell oder passe die `num_ctx`-Einstellung an, um weniger Speicher zu verwenden. Denk daran, deine KI auf Diät zu setzen.

### "Kann ich das mit meiner GPU schneller machen?"
**Lösung**: Ollama erkennt GPUs automatisch! Stelle nur sicher, dass deine GPU-Treiber aktuell sind. Kostenloses Turbo-Upgrade! 🏎️

## Zusatzressourcen (Für Neugierige) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — Tiefer Einblick in lokale KI-Modelle
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Erfahre mehr über den Aufbau von Agententeams
- [Qwen Modell Info](https://qwenlm.github.io/) — Lerne das Gehirn deines KI-Assistenten kennen

## Lizenz

MIT Lizenz — Baue coole Sachen, teile sie, mach die Welt besser! 🌍

## Willst Du Mitwirken?

Bug gefunden? Idee? Erstelle ein Issue oder PR! Wir lieben die Community-Vibes. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, können automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten. Das Originaldokument in seiner ursprünglichen Sprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->