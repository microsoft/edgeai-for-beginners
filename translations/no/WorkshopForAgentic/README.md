<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:41:35+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "no"
}
-->
# 🎙️ The AI Podcast Studio Workshop

> 🌏 [中文版 (Chinese Version)](translation/zh-cn/README.md)

![logo](../../../translated_images/no/logo.8711e39dc8257d7b.png)

## Din oppgave

Velkommen til **The AI Podcast Studio**! Du skal lansere din egen teknologipodcast kalt "Future Bytes" — men her er vri: du skal bygge et produksjonsteam drevet av AI som hjelper deg å lage den. Ikke mer uendelige timer med research, manusarbeid og lydredigering. I stedet skal du kode deg frem til å bli en podkast-produsent med AI-krefter.

## Historien

Tenk deg dette: Du og vennene dine vil starte en podcast om de kuleste teknologitrendene, men alle er opptatt med skole, jobb eller bare livet. Hva om du kunne bygge et team av AI-agenter som gjorde det tunge løftet? En agent forsker på emner, en annen skriver engasjerende manus, og en tredje gjør tekst om til naturlige samtaler. Høres ut som sci-fi? La oss gjøre det til virkelighet.

## Hva du vil lære

Ved slutten av denne workshopen vil du kunne:
- 🤖 Depløyere din egen lokale AI-modell (ingen API-kostnader, ingen skyavhengighet!)
- 🔧 Bygge spesialiserte AI-agenter som faktisk samarbeider
- 🎬 Lage en komplett podkastproduksjonslinje fra idé til lyd

## Din reise: Tre akter

![arch](../../../translated_images/no/arch.5965fe504e4a3a93.png)

Som i enhver god historie har vi tre akter. Hver bygger AI-podcaststudioet ditt bit for bit:

| Episode | Din oppgave | Hva skjer | Ferdigheter låst opp |
|---------|-------------|-----------|---------------------|
| **Akt 1** | [Møt dine AI-assistenter](md/01.BuildAIAgentWithSLM.md) | Du oppdager hvordan du lager AI-agenter som kan chatte, søke på nettet og til og med løse problemer. Tenk på dem som forskningspraktikanter som aldri sover. | 🎯 Bygg din første agent<br>🛠️ Gi den superkrefter (verktøy!)<br>🧠 Lær den å tenke<br>🌐 Kople den til internett |
| **Akt 2** | [Sett sammen ditt produksjonsteam](md/02.AIAgentOrchestrationAndWorkflows.md) | Nå blir det spennende! Du skal orkestrere flere AI-agenter til å jobbe sammen som et ekte podkastteam. En forsker, en skriver, du godkjenner — lagarbeid får drømmen til å fungere. | 🎭 Koordinere flere agenter<br>🔄 Bygge godkjenningsflyter<br>🖥️ Teste med DevUI-grensesnitt<br>✋ Hold menneskene i kontroll |
| **Akt 3** | [Gi liv til din podcast](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finale! Forvandle dine tekstmanus til ekte podkastlyd med realistiske stemmer og naturlige samtaler. Din "Future Bytes"-podcast er klar for lansering! | 🎤 Tekst-til-tale-magien<br>👥 Flere høyttalerstemmer<br>⏱️ Langformet lyd<br>🚀 Full automatisering |

Hver akt låser opp nye evner. Hopp fremover hvis du er modig, men vi anbefaler å følge historien!

## Miljøkrav

Denne workshopen støtter forskjellige maskinvarermiljøer:
- **CPU**: Egnet for testing og liten skala bruk
- **GPU**: Anbefalt for produksjonsmiljøer, forbedrer betydelig inferenshastighet
- **NPU**: Støtter neste generasjons akselerasjon med nevrale prosesseringsenheter

## Hva du trenger

### Programvare-sjekkliste ✅
- **Python 3.10+** (Ditt programmeringsspråk)
- **Ollama** (Kjører AI-modeller på maskinen din)
- **VS Code** (Din kodeeditor)
- **Python-utvidelse** (Gjør VS Code smartere)
- **Git** (For å hente kode)

### Maskinvare-sjekk 💻
- **Kan jeg kjøre dette?**: 8GB RAM, 10GB ledig plass (fungerer, men kan være tregt)
- **Ideelt oppsett**: 16GB+ RAM, et anstendig GPU (problemfri kjøring!)
- **Har du NPU?**: Enda bedre! Neste generasjons ytelse låst opp 🚀

## Sett opp studioet ditt 🎬

### Steg 1: Python Power-Up

Sørg for at du har Python 3.10 eller nyere:

```bash
python --version
# Skal vise Python 3.10.x eller høyere
```

Ingen Python? Last det ned fra [python.org](https://python.org) — det er gratis!

### Steg 2: Skaff Ollama (Din AI-modell-kjører)

Gå til [ollama.ai](https://ollama.ai) og last ned Ollama for ditt operativsystem. Tenk på det som motoren som kjører AI-modellene dine lokalt.

Sjekk om det er klart:

```bash
ollama --version
```

### Steg 3: Last ned din AI-hjerne 🧠

Tid for å hente Qwen-3-8B-modellen (det er som å ansette din første AI-assistent):

```bash
ollama pull qwen3:8b
```

*Dette kan ta noen minutter. Perfekt tid for en kaffepause! ☕*

### Steg 4: Sett opp VS Code

Last ned [Visual Studio Code](https://code.visualstudio.com/) hvis du ikke har det. Det er den beste kodeeditoren der ute (prøv meg 😄).

### Steg 5: Python-utvidelsen

I VS Code:  
1. Trykk `Ctrl+Shift+X` (eller `Cmd+Shift+X` på Mac)  
2. Søk etter "Python"  
3. Installer den offisielle Microsoft Python-utvidelsen  

### Steg 6: Du er klar! 🎉

Alvorlig talt, nå er du klar til å rocke. La oss bygge litt AI-magi!

### Steg 7: Installer Microsoft Agent Framework og relaterte pakker 📦

Installer alle nødvendige avhengigheter for workshopen:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Dette vil installere Microsoft Agent Framework og alle nødvendige pakker. Ta en kaffe — første gangs oppsett kan ta noen minutter! ☕*

## Workshop-instruksjoner

Detaljert prosjektstruktur, konfigurasjonssteg og kjøreanvisninger forklares steg-for-steg under workshopen.

## Feilsøking (når ting går galt) 🔧

### "Ugh, modellnedlastingen tar evigheter!"  
**Løsning**: Bruk en VPN eller konfigurer Ollama med en mirrorkilde. Noen ganger hater bare internett oss.

### "Maskinen min dør! Slutt på minne!"  
**Løsning**: Bytt til en mindre modell eller juster `num_ctx` innstillingen for å bruke mindre minne. Tenk på det som å sette AI-en på diett.

### "Kan jeg få det raskere med GPU-en min?"  
**Løsning**: Ollama oppdager GPU-er automatisk! Bare sørg for at GPU-driverne dine er oppdaterte. Gratis hastighetsboost! 🏎️

## Ekstra ressurser (for nysgjerrige) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — Dypdykk i lokale AI-modeller  
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Lær mer om å bygge agentteam  
- [Qwen Model Info](https://qwenlm.github.io/) — Møt hjernen til AI-assistenten din  

## Lisens

MIT-lisens — Bygg kule ting, del dem, gjør verden bedre! 🌍

## Vil du bidra?

Fant en feil? Har en idé? Legg inn en Issue eller PR! Vi digger fellesskapsvibber. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->