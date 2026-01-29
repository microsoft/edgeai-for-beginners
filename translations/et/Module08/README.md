# Moodul 08: Praktiline kogemus Microsoft Foundry Localiga - Täielik arendaja tööriistakomplekt

## Ülevaade

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) esindab järgmise põlvkonna serva AI arendust, pakkudes arendajatele võimsaid tööriistu AI rakenduste loomiseks, juurutamiseks ja skaleerimiseks kohapeal, säilitades samal ajal sujuva integreerimise Azure AI Foundryga. See moodul hõlmab Foundry Locali täielikult alates paigaldamisest kuni arenenud agentide arendamiseni.

**Peamised tehnoloogiad:**
- Microsoft Foundry Local CLI ja SDK
- Azure AI Foundry integreerimine
- Mudeli järeldamine seadmes
- Kohalik mudeli vahemälu ja optimeerimine
- Agentipõhised arhitektuurid

## Õpieesmärgid

Selle mooduli läbimisel õpid:

- **Foundry Locali valdamine**: Paigaldamine, konfigureerimine ja optimeerimine Windows 11 arenduseks
- **Erinevate mudelite juurutamine**: Phi, Qwen, Deepseek ja GPT mudelite käivitamine kohapeal CLI käskudega
- **Tootmislahenduste loomine**: AI rakenduste loomine arenenud promptide inseneri ja andmete integreerimisega
- **Avatud lähtekoodiga ökosüsteemi kasutamine**: Hugging Face mudelite ja kogukonna panuste integreerimine
- **AI agentide arendamine**: Intelligentsete agentide loomine maandamise ja orkestreerimise võimekustega
- **Ettevõtte mustrite rakendamine**: Modulaarsete ja skaleeritavate AI lahenduste loomine tootmiskeskkonna jaoks

## Sessiooni struktuur

### [1: Foundry Localiga alustamine](./01.FoundryLocalSetup.md)
**Fookus**: Paigaldamine, CLI seadistamine, mudelite juurutamine ja riistvara optimeerimine

**Peamised teemad**: Täielik paigaldamine • CLI käsud • Mudeli vahemälu • Riistvara kiirendus • Mitme mudeli juurutamine

**Näidis**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK integreerimine](./samples/02/README.md) • [Mudelite avastamine ja võrdlusuuringud](./samples/03/README.md)

**Kestus**: 2-3 tundi | **Tase**: Algaja

---

### [2: AI lahenduste loomine Azure AI Foundryga](./02.AzureAIFoundryIntegration.md)
**Fookus**: Arenenud promptide insener, andmete integreerimine ja pilveühenduvus

**Peamised teemad**: Promptide insener • Andmete integreerimine • Azure töövood • Jõudluse optimeerimine • Jälgimine

**Näidis**: [Chainlit RAG rakendus](./samples/04/README.md)

**Kestus**: 2-3 tundi | **Tase**: Kesktase

---

### [3: Avatud lähtekoodiga mudelid Foundry Localis](./03.OpenSourceModels.md)
**Fookus**: Hugging Face integreerimine, BYOM strateegiad ja kogukonna mudelid

**Peamised teemad**: Hugging Face integreerimine • Oma mudeli kasutamine • Model Mondays ülevaated • Kogukonna panused • Mudeli valik

**Näidis**: [Mitme agendi orkestreerimine](./samples/05/README.md)

**Kestus**: 2-3 tundi | **Tase**: Kesktase

---

### [4: Tipptasemel mudelite uurimine](./04.CuttingEdgeModels.md)
**Fookus**: LLM vs SLM, EdgeAI rakendamine ja arenenud demod

**Peamised teemad**: Mudelite võrdlus • Serva vs pilve järeldamine • Phi + ONNX Runtime • Chainlit RAG rakendus • WebGPU optimeerimine

**Näidis**: [Mudelite tööriistade ruuter](./samples/06/README.md)

**Kestus**: 3-4 tundi | **Tase**: Edasijõudnud

---

### [5: AI-põhiste agentide kiire loomine](./05.AIPoweredAgents.md)
**Fookus**: Agendi arhitektuurid, süsteemi promptid, maandamine ja orkestreerimine

**Peamised teemad**: Agendi disainimustrid • Süsteemi promptide insener • Maandamistehnikad • Mitme agendi süsteemid • Tootmiskeskkonna juurutamine

**Näidis**: [Mitme agendi orkestreerimine](./samples/05/README.md) • [Arenenud mitme agendi süsteem](./samples/09/README.md)

**Kestus**: 3-4 tundi | **Tase**: Edasijõudnud

---

### [6: Foundry Local - mudelid kui tööriistad](./06.ModelsAsTools.md)
**Fookus**: Modulaarsete AI lahenduste loomine, ettevõtte skaleerimine ja tootmismustrid

**Peamised teemad**: Mudelid kui tööriistad • Kohapealne juurutamine • SDK/API integreerimine • Ettevõtte arhitektuurid • Skaleerimisstrateegiad

**Näidis**: [Mudelite tööriistade ruuter](./samples/06/README.md) • [Foundry tööriistade raamistik](./samples/10/README.md)

**Kestus**: 3-4 tundi | **Tase**: Ekspert

---

### [7: Otsese API integreerimise mustrid](./samples/07/README.md)
**Fookus**: REST API integreerimine ilma SDK sõltuvusteta maksimaalse kontrolli saavutamiseks

**Peamised teemad**: HTTP kliendi rakendamine • Kohandatud autentimine • Mudeli tervise jälgimine • Voogesituse vastused • Tootmise veakäsitlus

**Näidis**: [Otsese API klient](./samples/07/README.md)

**Kestus**: 2-3 tundi | **Tase**: Kesktase

---

### [8: Windows 11 kohalik vestlusrakendus](./samples/08/README.md)
**Fookus**: Kaasaegsete kohalike vestlusrakenduste loomine Foundry Locali integreerimisega

**Peamised teemad**: Electron arendus • Fluent Design System • Kohalik Windowsi integreerimine • Reaalajas voogesitus • Vestlusliidese disain

**Näidis**: [Windows 11 vestlusrakendus](./samples/08/README.md)

**Kestus**: 3-4 tundi | **Tase**: Edasijõudnud

---

### [9: Arenenud mitme agendi orkestreerimine](./samples/09/README.md)
**Fookus**: Täiustatud agentide koordineerimine, spetsialiseeritud ülesannete jaotus ja koostööl põhinevad AI töövood

**Peamised teemad**: Intelligentne agentide koordineerimine • Funktsioonide kutsumise mustrid • Agentidevaheline suhtlus • Töövoo orkestreerimine • Kvaliteedi tagamise mehhanismid

**Näidis**: [Arenenud mitme agendi süsteem](./samples/09/README.md)

**Kestus**: 4-5 tundi | **Tase**: Ekspert

---

### [10: Foundry Local kui tööriistade raamistik](./samples/10/README.md)
**Fookus**: Tööriistakeskne arhitektuur Foundry Locali integreerimiseks olemasolevatesse rakendustesse ja raamistikesse

**Peamised teemad**: LangChain integreerimine • Semantilise tuuma funktsioonid • REST API raamistikud • CLI tööriistad • Jupyter integreerimine • Tootmiskeskkonna juurutamise mustrid

**Näidis**: [Foundry tööriistade raamistik](./samples/10/README.md)

**Kestus**: 4-5 tundi | **Tase**: Ekspert

## Eeltingimused

### Süsteeminõuded
- **Operatsioonisüsteem**: Windows 11 (22H2 või uuem)
- **Mälu**: 16GB RAM (32GB soovitatav suuremate mudelite jaoks)
- **Salvestusruum**: 50GB vaba ruumi mudeli vahemälu jaoks
- **Riistvara**: NPU-toega seade soovitatav (Copilot+ PC), GPU valikuline
- **Võrk**: Kiire internet esialgsete mudelite allalaadimiseks

### Arenduskeskkond
- Visual Studio Code koos AI Toolkit laiendiga
- Python 3.10+ ja pip
- Git versioonihalduseks
- PowerShell või käsuviip
- Azure CLI (valikuline pilve integreerimiseks)

### Teadmiste eeltingimused
- AI/ML põhimõtete põhiteadmised
- Käsurea kasutamise oskus
- Python programmeerimise alused
- REST API kontseptsioonid
- Promptide ja mudeli järeldamise põhiteadmised

## Mooduli ajakava

**Kogu hinnanguline aeg**: 30-38 tundi

| Sessioon | Fookusala | Näidised | Aeg | Keerukus |
|---------|------------|---------|------|------------|
|  1 | Seadistamine ja põhialused | 01, 02, 03 | 2-3 tundi | Algaja |
|  2 | AI lahendused | 04 | 2-3 tundi | Kesktase |
|  3 | Avatud lähtekood | 05 | 2-3 tundi | Kesktase |
|  4 | Arenenud mudelid | 06 | 3-4 tundi | Edasijõudnud |
|  5 | AI agendid | 05, 09 | 3-4 tundi | Edasijõudnud |
|  6 | Ettevõtte tööriistad | 06, 10 | 3-4 tundi | Ekspert |
|  7 | Otsene API integreerimine | 07 | 2-3 tundi | Kesktase |
|  8 | Windows 11 vestlusrakendus | 08 | 3-4 tundi | Edasijõudnud |
|  9 | Arenenud mitme agendi süsteem | 09 | 4-5 tundi | Ekspert |
| 10 | Tööriistade raamistik | 10 | 4-5 tundi | Ekspert |

## Peamised ressursid

**Ametlik dokumentatsioon:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Lähtekood ja ametlikud näidised
- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Täielik seadistamise ja kasutamise juhend
- [Model Mondays sari](https://aka.ms/model-mondays) - Igakuised mudelite ülevaated ja õpetused

**Kogukond ja tugi:**
- [Foundry Local arutelud](https://github.com/microsoft/Foundry-Local/discussions) - Kogukonna küsimused ja funktsioonide taotlused
- [Microsoft AI arendajate kogukond](https://techcommunity.microsoft.com/category/artificialintelligence) - Viimased uudised ja parimad praktikad

## Õpitulemused

Selle mooduli läbimisel oled valmis:

### Tehniline meisterlikkus
- **Paigaldamine ja haldamine**: Foundry Locali paigaldamine ja haldamine arendus- ja tootmiskeskkondades
- **Mudelite integreerimine**: Töö mitmekesiste mudeliperekondadega Microsoftilt, Hugging Face'ilt ja kogukonnast
- **Rakenduste loomine**: Tootmiskõlblike AI rakenduste loomine arenenud funktsioonide ja optimeerimistega
- **Agentide arendamine**: Täiustatud AI agentide rakendamine maandamise, põhjendamise ja tööriistade integreerimisega

### Strateegiline arusaam
- **Arhitektuuri otsused**: Teadlik valik kohapealse ja pilve juurutamise vahel
- **Jõudluse optimeerimine**: Järeldamise jõudluse optimeerimine erinevates riistvarakonfiguratsioonides
- **Ettevõtte skaleerimine**: Rakenduste disain, mis skaleerub kohalikest prototüüpidest ettevõtte juurutusteni
- **Privaatsus ja turvalisus**: Privaatsust säilitavate AI lahenduste rakendamine kohapealse järeldamisega

### Innovatsioonivõimekus
- **Kiire prototüüpimine**: AI rakenduste kontseptsioonide kiire loomine ja testimine kõigi 10 näidismustri abil
- **Kogukonna integreerimine**: Avatud lähtekoodiga mudelite kasutamine ja panustamine ökosüsteemi
- **Arenenud mustrid**: Tipptasemel AI mustrite rakendamine, sealhulgas RAG, agendid ja tööriistade integreerimine
- **Raamistiku valdamine**: Ekspertide tasemel integreerimine LangChaini, Semantilise tuuma, Chainliti ja Electroniga
- **Tootmiskeskkonna juurutamine**: Skaleeritavate AI lahenduste juurutamine kohalikest prototüüpidest ettevõtte süsteemideni
- **Tulevikukindel arendus**: Rakenduste loomine, mis on valmis uute AI tehnoloogiate ja mustrite jaoks

## Alustamine

1. **Keskkonna seadistamine**: Veendu, et Windows 11 vastab soovitatud riistvaranõuetele (vt eeltingimused)
2. **Foundry Locali paigaldamine**: Järgi sessiooni 1 juhiseid täielikuks paigaldamiseks ja konfigureerimiseks
3. **Näidise 01 käivitamine**: Alusta REST API integreerimisega, et seadistust kontrollida
4. **Näidiste läbimine**: Täida näidised 01-10, et saavutada täielik meisterlikkus

## Edu mõõdikud

Jälgi oma edusamme kõigi 10 näidise läbimisel:

### Põhitaseme näidised (01-03)
- [ ] Foundry Locali edukas paigaldamine ja konfigureerimine
- [ ] REST API integreerimise lõpetamine (Näidis 01)
- [ ] OpenAI SDK ühilduvuse rakendamine (Näidis 02)
- [ ] Mudelite avastamine ja võrdlusuuringute läbiviimine (Näidis 03)

### Rakendustase (04-06)
- [ ] Vähemalt 4 erineva mudeliperekonna juurutamine ja käivitamine
- [ ] Funktsionaalse RAG vestlusrakenduse loomine (Näidis 04)
- [ ] Mitme agendi orkestreerimissüsteemi loomine (Näidis 05)
- [ ] Intelligentse mudelite ruuteri rakendamine (Näidis 06)

### Arenenud integreerimise tase (07-10)
- [ ] Tootmiskõlbliku API kliendi loomine (Näidis 07)
- [ ] Windows 11 kohalik vestlusrakendus (Näidis 08)
- [ ] Arenenud mitme agendi süsteemi rakendamine (Näidis 09)
- [ ] Tööriistade raamistik (Näidis 10)

### Meisterlikkuse näitajad
- [ ] Kõigi 10 näidise edukas käivitamine ilma vigadeta
- [ ] Vähemalt 3 näidise kohandamine konkreetsete kasutusjuhtude jaoks
- [ ] 2+ näidise juurutamine tootmiskeskkonnas
- [ ] Panustamine näidiskoodi täiustamisse või laiendamisse
- [ ] Foundry Locali mustrite integreerimine isiklikesse/professionaalsetesse projektidesse

## Kiire alustamise juhend - Kõik 10 näidist

### Keskkonna seadistamine (nõutav kõigi näidiste jaoks)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Põhitaseme näidised (01-06)

**Näidis 01: REST vestluse kiirstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Näidis 02: OpenAI SDK integreerimine**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Näidis 03: Mudelite avastamine ja võrdlusuuringud**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Näidis 04: Chainlit RAG rakendus**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Näidis 05: Mitme agendi orkestreerimine**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Näidis 06: Mudelite tööriistade ruuter**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Arenenud integreerimise näidised (07-10)

**Näidis 07: Otsese API klient**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Näidis 08: Windows 11 vestlusrakendus**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```


See moodul esindab tipptasemel serva-AI arendust, ühendades Microsofti ettevõtte tasemel tööriistad avatud lähtekoodiga ökosüsteemi paindlikkuse ja innovatsiooniga. Valdades Foundry Locali kõigi 10 põhjaliku näidise kaudu, asetate end AI-rakenduste arenduse esirinda.

**Täielik õpiteekond:**
- **Alused** (Näidised 01-03): API integreerimine ja mudelite haldamine
- **Rakendused** (Näidised 04-06): RAG, agendid ja intelligentne suunamine
- **Edasijõudnud** (Näidised 07-10): Tootmisraamistikud ja ettevõtte integratsioon

Azure OpenAI integreerimise kohta (Sessioon 2) vaadake üksikute näidiste README-faile, kus on toodud vajalikud keskkonnamuutujad ja API versiooni seaded.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.