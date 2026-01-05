<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:44:57+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "no"
}
-->
# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.no.png)

## Din oppgave

Velkommen til **AI Podcast Studio**! Du er i ferd med å lansere din egen teknologipodcast "Future Bytes" — men her kommer en vri: du skal bygge et AI-drevet produksjonsteam som hjelper deg å lage den. Ingen flere endeløse timer med research, manusforfatting og lydredigering. I stedet blir du en podkastprodusent med AI-superkrefter gjennom programmering.

## Historiebakgrunn

Tenk deg: Du og vennene dine vil starte en podkast om de kuleste teknologitrendene, men alle er opptatt med studier, jobb eller liv. Hva om du kunne bygge et team av AI-agenter som gjør det kjedelige arbeidet for deg? En agent forsker på temaet, en annen skriver engasjerende manus, og en tredje konverterer tekst til naturlig samtale. Høres ut som science fiction? La oss gjøre det til virkelighet.

## Hva du vil lære

Etter denne workshopen vil du vite hvordan du:
- 🤖 Distribuerer dine egne lokale AI-modeller (ingen API-kostnader, ingen skyavhengighet!)
- 🔧 Bygger profesjonelle AI-agenter som samarbeider i praksis
- 🎬 Lager en komplett podkastproduksjonsflyt fra idé til lyd

## Din reise: Tre akter

Som i enhver god historie har vi tre akter. Hver akt bygger gradvis opp ditt AI podcast studio:

| Kapittel | Din oppgave | Hva skjer | Låser opp ferdigheter |
|---------|-----------|--------------|----------------|
| **Akt 1** | [Bli kjent med AI-assistenten din](01.BuildAIAgentWithSLM.md) | Du vil lære å lage AI-agenter som kan chatte, søke på nettet og til og med løse problemer. Tenk på dem som forskningsassistenter som aldri sover. | 🎯 Bygg din første agent<br>🛠️ Gi den superkrefter (verktøy!)<br>🧠 Lær den å tenke<br>🌐 Koble til internett |
| **Akt 2** | [Sett sammen produksjonsteamet ditt](02.AIAgentOrchestrationAndWorkflows.md) | Nå blir det gøy! Du skal orkestrere flere AI-agenter som samarbeider som et ekte podkastlag. En forsker, en skriver, du godkjenner — lagarbeid gjør drømmen mulig. | 🎭 Koordiner flere agenter<br>🔄 Lag godkjenningsflyt<br>🖥️ Test med DevUI<br>✋ Behold menneskelig kontroll |
| **Akt 3** | [La podkasten din komme til live](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Grand finale! Konverter manuset ditt til ekte podkastlyd med realistiske stemmer og naturlig dialog. Din "Future Bytes"-podkast er klar til lansering! | 🎤 Tekst-til-tale magi<br>👥 Flestemmeløsninger<br>⏱️ Langformat lyd<br>🚀 Fullstendig automatisert |

Hver akt låser opp nye ferdigheter. Hvis du er modig, kan du hoppe rundt, men vi anbefaler å følge rekkefølgen!

## Miljøkrav

Workshopen støtter ulike maskinvaremiljøer:
- **CPU**: Egnet for testing og småskala bruk
- **GPU**: Anbefales for produksjon, betydelig økt inferanshastighet
- **NPU**: Støtter neste generasjons nevral prosesseringsenheter for akselerasjon

## Hva du trenger

### Programvareliste ✅
- **Python 3.10+** (programmeringsspråket ditt)
- **Ollama** (for å kjøre AI-modeller lokalt)
- **VS Code** (kodeeditoren din)
- **Python-utvidelsen** (gjør VS Code smartere)
- **Git** (for å hente koden)

### Maskinvare-sjekk 💻
- **Kan jeg kjøre det?**: 8 GB minne, 10 GB ledig diskplass (brukbart, men kan være litt tregt)
- **Ideal konfigurasjon**: 16 GB+ minne, et bra GPU-kort (jevn kjøring!)
- **Har du NPU?**: Enda bedre! Lås opp neste generasjons ytelse 🚀

## Sette opp studioet ditt 🎬

### Steg 1: Oppgrader Python

Sørg for at du har Python 3.10 eller nyere:

```bash
python --version
# Bør vise Python 3.10.x eller nyere versjon
```

Har du ikke Python? Få det fra [python.org](https://python.org) — det er gratis!

### Steg 2: Skaff Ollama (AI-modellmotoren din)

Besøk [ollama.ai](https://ollama.ai) for å laste ned Ollama som passer ditt operativsystem. Tenk på det som motoren som kjører AI-modeller lokalt.

Sjekk at det er klart:

```bash
ollama --version
```

### Steg 3: Last ned AI-hjernen din 🧠

Det er på tide å skaffe Qwen-3-8B-modellen (som å ansette din første AI-assistent):

```bash
ollama pull qwen3:8b
```

*Dette kan ta noen minutter. Perfekt kafferast! ☕*

### Steg 4: Sett opp VS Code

Hvis du ikke har det, skaff [Visual Studio Code](https://code.visualstudio.com/). Det er den beste kodeeditoren (utfordrer mottas 😄).

### Steg 5: Python-utvidelsen

I VS Code:
1. Trykk `Ctrl+Shift+X` (på Mac `Cmd+Shift+X`)
2. Søk etter "Python"
3. Installer Microsofts offisielle Python-utvidelse

### Steg 6: Ferdig! 🎉

Alvorlig talt, du er klar. La oss lage noe AI-magi!

### Steg 7: Installer Microsoft Agent Framework og avhengigheter 📦

Installer alle nødvendige pakker for workshopen:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Dette installerer Microsoft Agent Framework og alle nødvendige pakker. Ta en kaffe — første gang kan det ta noen minutter! ☕*

## Workshopinstruksjoner

Detaljert prosjektstruktur, oppsett og kjøring vil bli forklart trinnvis i løpet av workshopen.

## Feilsøking (når ting går galt) 🔧

### "Å nei, nedlastingen av modellen går altfor sakte!"
**Løsning**: Bruk VPN eller konfigurer Ollama speilserver. Noen ganger er nettet tregt.

### "Maskinen min er i ferd med å henge seg opp! For lite minne!"
**Løsning**: Bytt til en mindre modell eller juster `num_ctx` for å bruke mindre minne. Tenk på det som å sette AI-en på diett.

### "Kan jeg få det raskere med GPU?"
**Løsning**: Ollama oppdager GPU automatisk! Bare sørg for at GPU-driverne dine er oppdaterte. Gratis hastighetsboost! 🏎️

## Ekstra ressurser (for nysgjerrige) 📚

- [Ollama dokumentasjon](https://github.com/ollama/ollama) — Fordyp deg i lokale AI-modeller
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Lær mer om å bygge agentteam
- [Qwen modellinformasjon](https://qwenlm.github.io/) — Møt hjernen til AI-assistenten din

## Lisens

MIT-lisens — bygg kule ting, del dem, og gjør verden bedre! 🌍

## Vil du bidra?

Finner du en feil? Har du en idé? Send en Issue eller PR! Vi elsker fellesskapet. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->