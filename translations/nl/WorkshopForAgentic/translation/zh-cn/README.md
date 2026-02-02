# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/nl/logo.8711e39dc8257d7b.webp)

## Jouw opdracht

Welkom bij **AI Podcast Studio**! Je staat op het punt je eigen tech-podcast "Future Bytes" te lanceren — maar hier is een twist: je bouwt een AI-gestuurd productieteam om je te helpen het te creëren. Geen eindeloos onderzoek, script schrijven en audio-editing meer. In plaats daarvan word jij een podcastmaker met AI-superkrachten via programmeren.

## Verhaalachtergrond

Stel je voor: jij en je vrienden willen een podcast starten over de nieuwste coole tech-trends, maar iedereen is druk met studeren, werken of leven. Wat als je een team AI-agenten kunt bouwen die het zware werk voor je doet? Eén agent doet research, een andere schrijft boeiende scripts, een derde zet tekst om in natuurlijk vloeiende dialogen. Klinkt als science fiction? Laten we het werkelijkheid maken.

## Wat je zult leren

Aan het einde van deze workshop weet je hoe je:
- 🤖 Je eigen lokale AI-modellen inzet (geen API-kosten, geen cloud-dependency!)
- 🔧 Praktische, samenwerkende professionele AI-agenten bouwt
- 🎬 Een volledige podcastproductieworkflow maakt van idee tot audio

## Jouw reis: drie acts

Net als elk goed verhaal hebben we drie acts. Elke act bouwt stapsgewijs jouw AI-podcaststudio:

| Hoofdstuk | Jouw opdracht | Wat gebeurt er | Ontgrendel vaardigheden |
|---------|-----------|--------------|----------------|
| **Act 1** | [Leer je AI-assistent kennen](01.BuildAIAgentWithSLM.md) | Je ontdekt hoe je AI-agenten maakt die kunnen chatten, op het internet zoeken en zelfs problemen oplossen. Zie ze als nooit-slaapende onderzoeksstagiaires. | 🎯 Bouw je eerste agent<br>🛠️ Voorzie hem van superkrachten (tools!)<br>🧠 Leer hem denken<br>🌐 Verbind met het internet |
| **Act 2** | [Bouw je productieteam](02.AIAgentOrchestrationAndWorkflows.md) | Nu wordt het leuk! Je orkestreert meerdere AI-agenten die samenwerken als een echt podcastteam. Eén doet research, één schrijft, jij keurt goed — teamwork maakt dromen waar. | 🎭 Coördineer meerdere agenten<br>🔄 Bouw goedkeuringsworkflows<br>🖥️ Test met DevUI interface<br>✋ Houd de menselijke controle |
| **Act 3** | [Breng je podcast tot leven](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | De grote finale! Zet je tekstscript om in echte podcastaudio met realistische stemmen en natuurlijke gesprekken. Je "Future Bytes" podcast staat klaar voor publicatie! | 🎤 Tekst-naar-spraak magie<br>👥 Meerdere sprekers stemmen<br>⏱️ Lange audioformaten<br>🚀 Volledig geautomatiseerd |

Elke act ontgrendelt nieuwe vaardigheden. Durf je meteen te springen? Kan, maar we raden aan ze op volgorde te volgen!

## Omgevingsvereisten

Deze workshop ondersteunt diverse hardware-omgevingen:
- **CPU**: geschikt voor testen en klein gebruik
- **GPU**: aanbevolen voor productieomgevingen, verbetert de snelheid aanzienlijk
- **NPU**: ondersteunt next-gen neurale verwerkingsunits versnelling

## Wat je nodig hebt

### Softwarelijst ✅
- **Python 3.10+** (jouw programmeertaal)
- **Ollama** (draait AI-modellen op je machine)
- **VS Code** (jouw code-editor)
- **Python extensie** (maakt VS Code slimmer)
- **Git** (om code te halen)

### Hardwarecheck 💻
- **Kan ik het draaien?**: 8GB RAM, 10GB vrije schijfruimte (werkt, maar kan traag zijn)
- **Ideale configuratie**: 16GB+ RAM, een degelijke GPU (vloeiend draaien!)
- **Heb je een NPU?**: nog beter! Ontgrendel next-gen prestaties 🚀

## Bouw je studio 🎬

### Stap 1: Python upgraden

Zorg dat je Python 3.10 of hoger hebt:

```bash
python --version
# Moet Python 3.10.x of hoger weergeven
```

Geen Python? Haal het van [python.org](https://python.org) — het is gratis!

### Stap 2: Haal Ollama binnen (jouw AI-modellen-engine)

Ga naar [ollama.ai](https://ollama.ai) en download Ollama voor jouw besturingssysteem. Zie het als de motor die AI-modellen lokaal laat draaien.

Controleer of het klaar is:

```bash
ollama --version
```

### Stap 3: Download je AI-brein 🧠

Het is tijd om het Qwen-3-8B model te downloaden (alsof je je eerste AI-assistent aanneemt):

```bash
ollama pull qwen3:8b
```

*Dit kan een paar minuten duren. Perfecte koffiepauze! ☕*

### Stap 4: Installeer VS Code

Als je het nog niet hebt, haal [Visual Studio Code](https://code.visualstudio.com/). De beste code-editor (discussie gesloten 😄).

### Stap 5: Python extensie

In VS Code:
1. Druk `Ctrl+Shift+X` (op Mac `Cmd+Shift+X`)
2. Zoek "Python"
3. Installeer de officiële Microsoft Python extensie

### Stap 6: Klaar! 🎉

Serieus, je bent er klaar voor. Laten we AI-magie bouwen!

### Stap 7: Installeer Microsoft Agent Framework en benodigde pakketten 📦

Installeer alle dependencies voor de workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Dit installeert Microsoft Agent Framework en alle noodzakelijke pakketten. Pak een koffie — de eerste installatie kan even duren! ☕*

## Workshop gids

De gedetailleerde projectstructuur, configuratiestappen en instructies volgen tijdens de workshop.

## Probleemoplossing (als er problemen zijn) 🔧

### "Argh, het model downloaden gaat te traag!"
**Oplossing**: Gebruik een VPN of configureer Ollama mirror bronnen. Soms is het netwerk traag.

### "Mijn PC loopt vast! Te weinig geheugen!"
**Oplossing**: Schakel over naar een kleiner model of pas de `num_ctx` instelling aan om minder geheugen te gebruiken. Zie het als een dieet voor je AI.

### "Kan ik GPU gebruiken om het sneller te maken?"
**Oplossing**: Ollama detecteert automatisch GPU! Zorg dat je GPU-bestuurders up-to-date zijn. Gratis snelheidsboost! 🏎️

## Extra bronnen (voor de nieuwsgierige) 📚

- [Ollama documentatie](https://github.com/ollama/ollama) — Leer alles over lokale AI-modellen
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Meer over het bouwen van agententeams
- [Qwen modelinformatie](https://qwenlm.github.io/) — Leer je AI-assistenten brein kennen

## Licentie

MIT-licentie — bouw coole dingen, deel ze en maak de wereld beter! 🌍

## Wil je bijdragen?

Bug gevonden? Ideeën? Submit een issue of PR! We houden van een actieve community. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->