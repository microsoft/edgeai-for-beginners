<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:43:15+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "sv"
}
-->
# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/sv/logo.8711e39dc8257d7b.png)

## Din uppgift

Välkommen till **AI Podcast Studio**! Du är på väg att lansera din egen tech-podcast "Future Bytes" – men här är twisten: du kommer att bygga ett AI-driven produktionsteam som hjälper dig att skapa den. Ingen mer ändlös research, manusförfattande och ljudredigering. Istället kommer du att programmera dig själv till en podcastproducent med AI-superkrafter.

## Berättelsens bakgrund

Föreställ dig: Du och dina vänner vill starta en podcast om de coolaste tekniktrenderna, men alla är upptagna med studier, jobb eller livet. Vad händer om du kan bygga ett team av AI-agenter som gör det tråkiga arbetet? En agent forskar om ämnet, en annan skriver engagerande manus, och en tredje omvandlar texten till naturligt flödande dialog. Låter det som science fiction? Låt oss göra det verklighet.

## Vad du kommer att lära dig

I slutet av denna workshop kommer du att veta hur du:
- 🤖 Distribuerar dina egna lokala AI-modeller (inga API-kostnader, inget molnavhängig!)
- 🔧 Bygger professionella AI-agenter som samverkar praktiskt
- 🎬 Skapar en komplett podcastproduktion från idé till ljud

## Din resa: Tre akter

Som varje bra berättelse har vi tre akter. Varje akt bygger stegvis upp din AI podcaststudio:

| Kapitel | Din uppgift | Vad händer | Färdigheter som låses upp |
|---------|-------------|------------|---------------------------|
| **Akt 1** | [Träffa dina AI-assistenter](01.BuildAIAgentWithSLM.md) | Du kommer att upptäcka hur du skapar AI-agenter som kan chatta, söka på webben och till och med lösa problem. Föreställ dig dem som forskarpraktikanter som aldrig sover. | 🎯 Bygg din första agent<br>🛠️ Ge den superkrafter (verktyg!)<br>🧠 Lär den att tänka<br>🌐 Koppla upp till internet |
| **Akt 2** | [Bygg ditt produktionsteam](02.AIAgentOrchestrationAndWorkflows.md) | Nu blir det roligt! Du kommer att orkestrera flera AI-agenter som samverkar som ett riktigt podcastteam. En forskar, en skriver, du godkänner – teamwork som gör drömmar verkliga. | 🎭 Koordinera flera agenter<br>🔄 Bygg arbetsflöden för godkännande<br>🖥️ Testa i DevUI-gränssnittet<br>✋ Behåll mänsklig kontroll |
| **Akt 3** | [Få din podcast att leva](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finalen! Omvandla dina textmanus till verkliga podcastljud med livfulla röster och naturliga samtal. Din "Future Bytes"-podcast är redo att släppas! | 🎤 Text-till-tal magi<br>👥 Flera talarröster<br>⏱️ Långformat ljud<br>🚀 Fullt automatiserad |

Varje akt låser upp nya förmågor. Du kan hoppa fram och tillbaka om du är modig, men vi rekommenderar att följa ordningen!

## Miljökrav

Denna workshop stöder olika hårdvaruinställningar:
- **CPU**: Bra för test och småskaligt bruk
- **GPU**: Rekommenderas för produktion, ökar inferenshastigheten avsevärt
- **NPU**: Stöder nästa generations neurala processorenheter för acceleration

## Vad du behöver

### Programvarulista ✅
- **Python 3.10+** (ditt programmeringsspråk)
- **Ollama** (kör AI-modeller på din maskin)
- **VS Code** (din kodredigerare)
- **Python-tillägg** (gör VS Code smartare)
- **Git** (för att hämta koden)

### Hårdvarukontroll 💻
- **Kan jag köra det?**: 8GB RAM, 10GB tillgängligt utrymme (går men blir kanske lite segt)
- **Idealisk konfiguration**: 16GB+ RAM, ett schysst GPU (flyter på fint!)
- **Har du NPU?**: Det är ännu bättre! Få nästa generations prestanda 🚀

## Bygg din studio 🎬

### Steg 1: Uppgradera Python

Säkerställ att du har Python 3.10 eller senare:

```bash
python --version
# Bör visa Python 3.10.x eller senare versioner
```

Ingen Python? Hämta från [python.org](https://python.org) – det är gratis!

### Steg 2: Skaffa Ollama (din AI-modelldrivare)

Gå till [ollama.ai](https://ollama.ai) och ladda ner Ollama för ditt operativsystem. Tänk på det som motorn som kör AI-modeller lokalt.

Kontrollera att allt är redo:

```bash
ollama --version
```

### Steg 3: Ladda ner ditt AI-hjärna 🧠

Dags att skaffa Qwen-3-8B-modellen (som att anställa din första AI-assistent):

```bash
ollama pull qwen3:8b
```

*Det kan ta några minuter. Perfekt tid för en kopp kaffe! ☕*

### Steg 4: Ställ in VS Code

Om du inte redan har det, hämta [Visual Studio Code](https://code.visualstudio.com/). Det är den bästa kodredigeraren (ingen protest 😄).

### Steg 5: Python-tillägg

I VS Code:
1. Tryck `Ctrl+Shift+X` (på Mac `Cmd+Shift+X`)
2. Sök efter "Python"
3. Installera Microsofts officiella Python-tillägg

### Steg 6: Klart! 🎉

På riktigt, du är redo. Låt oss skapa lite AI-magi!

### Steg 7: Installera Microsoft Agent Framework och relaterade paket 📦

Installera alla beroenden för workshopen:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Detta installerar Microsoft Agent Framework och alla nödvändiga paket. Ta en kopp kaffe – första installationen kan ta några minuter! ☕*

## Instruktioner för workshopen

Detaljerad projektstruktur, konfigurationssteg och exekveringsmetoder kommer att gås igenom stegvis under workshopen.

## Felsökning (när saker går fel) 🔧

### "Åh nej, modellen laddas ner för långsamt!"
**Lösning**: Använd VPN eller konfigurera Ollama spegelserver. Ibland är nätet bara långsamt.

### "Min dator hänger sig! Minnet räcker inte!"
**Lösning**: Byt till en mindre modell eller justera `num_ctx` för att använda mindre minne. Tänk på det som en diet för din AI.

### "Kan jag använda GPU för att göra det snabbare?"
**Lösning**: Ollama känner automatiskt av GPU:n! Se bara till att dina GPU-drivrutiner är uppdaterade. Gratis hastighetsboost! 🏎️

## Extra resurser (för den nyfikne) 📚

- [Ollama dokumentation](https://github.com/ollama/ollama) – Fördjupa dig i lokala AI-modeller
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) – Läs mer om att bygga agentteam
- [Qwen modellinfo](https://qwenlm.github.io/) – Lär känna din AI-assistents hjärna

## Licens

MIT-licens – Bygg coola saker, dela dem, gör världen bättre! 🌍

## Vill du bidra?

Hittat en bugg? Har idéer? Skicka in en Issue eller PR! Vi älskar communityn. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av den AI-baserade översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Trots att vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->