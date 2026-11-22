# Moodul 08: Käed külge Microsoft Foundry Localiga - Täielik arendaja tööriistakast

## Ülevaade

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) esindab järgmise põlvkonna serva AI arendust, pakkudes arendajatele võimsaid tööriistu AI rakenduste kohalikuks loomiseks, juurutamiseks ja skaleerimiseks, säilitades samal ajal sujuva integreerimise Azure AI Foundryga. See moodul hõlmab Foundry Locali kõikehõlmavalt alates installatsioonist kuni täiustatud agentide arenduseni.

**Põhitehnoloogiad:**
- Microsoft Foundry Local CLI ja SDK
- Azure AI Foundry integratsioon
- Mudeli järeldus seadmes
- Kohalik mudeli vahemälu ja optimeerimine
- Agentidel põhinevad arhitektuurid

## Õpieesmärgid

Selle mooduli lõpetamisel:

- **Valdad Foundry Locali**: Installi, konfigureeri ja optimeeri Windows 11 arenduseks
- **Juuruta erinevaid mudeleid**: Käivita phi, qwen, deepseek ja GPT mudeleid kohapeal CLI käskude abil
- **Ehita tootmislahendusi**: Loo AI rakendusi arenenud promptide insenertehnika ja andmete integreerimisega
- **Kasuta avatud lähtekoodiga ökosüsteemi**: Integreeri Hugging Face mudeleid ja kogukonna panuseid
- **Arenda AI agente**: Loo intelligentseid agente maandamise ja orkestreerimise võimetega
- **Rakenda ettevõtte mustreid**: Loo modulaarseid, skaleeritavaid AI lahendusi tootmisse viimiseks

## Sessiooni struktuur

### [1: Foundry Localiga alustamine](./01.FoundryLocalSetup.md)
**Fookus**: Installatsioon, CLI seadistamine, mudeli juurutus ja riistvara optimeerimine

**Põhiteemad**: Täielik installatsioon • CLI käsud • Mudeli vahemälu • Riistvara kiirendus • Mitme mudeli juurutus

**Näited**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK integratsioon](./samples/02/README.md) • [Mudeli avastamine ja võrdlus](./samples/03/README.md)

**Kestus**: 2-3 tundi | **Tase**: Algaja

---

### [2: AI lahenduste loomine Azure AI Foundryga](./02.AzureAIFoundryIntegration.md)
**Fookus**: Arenenud promptide insenertehnika, andmete integreerimine ja pilveühendus

**Põhiteemad**: Promptide insenertehnika • Andmete integreerimine • Azure töövood • Tulemuste optimeerimine • Jälgimine

**Näide**: [Chainlit RAG rakendus](./samples/04/README.md)

**Kestus**: 2-3 tundi | **Tase**: Kesktase

---

### [3: Avatud lähtekoodiga mudelid Foundry Localis](./03.OpenSourceModels.md)
**Fookus**: Hugging Face integratsioon, BYOM strateegiad ja kogukonna mudelid

**Põhiteemad**: HuggingFace integratsioon • Too-enda-mudel (BYOM) • Mudeliteesmaspäevade teadmised • Kogukonna panused • Mudelivalik

**Näide**: [Mitmeagendi orkestreerimine](./samples/05/README.md)

**Kestus**: 2-3 tundi | **Tase**: Kesktase

---

### [4: Tippmudelite uurimine](./04.CuttingEdgeModels.md)
**Fookus**: LLMid vs SLMid, EdgeAI rakendused ja arenenud demo näited

**Põhiteemad**: Mudelite võrdlus • Serva- vs pilvepõhine järeldus • Phi + ONNX Runtime • Chainlit RAG rakendus • WebGPU optimeerimine

**Näide**: [Mudelitööriistade marsruuter](./samples/06/README.md)

**Kestus**: 3-4 tundi | **Tase**: Edasijõudnud

---

### [5: Kiire AI-agentide loomine](./05.AIPoweredAgents.md)
**Fookus**: Agendi arhitektuurid, süsteemipromptid, maandamine ja orkestreerimine

**Põhiteemad**: Agendi disainimustrid • Süsteemipromptide insenertehnika • Maandamistehnikad • Mitmeagendi süsteemid • Tootmisse viimine

**Näited**: [Mitmeagendi orkestreerimine](./samples/05/README.md) • [Täiustatud mitmeagendi süsteem](./samples/09/README.md)

**Kestus**: 3-4 tundi | **Tase**: Edasijõudnud

---

### [6: Foundry Local - mudelid tööriistadena](./06.ModelsAsTools.md)
**Fookus**: Modulaarsetel AI lahendustel, ettevõtte skaleerimisel ja tootmismustritel

**Põhiteemad**: Mudelid tööriistadena • Seadmel juurutamine • SDK/API integratsioon • Ettevõtte arhitektuurid • Skaleerimisstrateegiad

**Näited**: [Mudelitööriistade marsruuter](./samples/06/README.md) • [Foundry tööriistade raamistik](./samples/10/README.md)

**Kestus**: 3-4 tundi | **Tase**: Ekspert

---

### [7: Otsene API integratsiooni mustrid](./samples/07/README.md)
**Fookus**: Puhtalt REST API integratsioon ilma SDK-de sõltuvusteta maksimaalse kontrolli saavutamiseks

**Põhiteemad**: HTTP kliendi implementeerimine • Kohandatud autentimine • Mudeli tervise jälgimine • Voogedastuse vastused • Tootmises vigade käitlemine

**Näide**: [Otsene API klient](./samples/07/README.md)

**Kestus**: 2-3 tundi | **Tase**: Kesktase

---

### [8: Windows 11 natiivse vestlusrakenduse loomine](./samples/08/README.md)
**Fookus**: Kaasaegsete natiivsete vestlusrakenduste loomine Foundry Locali integreerimisega

**Põhiteemad**: Elektroon arendus • Fluent Designi süsteem • Natiivne Windowsi integreerimine • Reaalaegne voogedastus • Vestluse liidese disain

**Näide**: [Windows 11 vestlusrakendus](./samples/08/README.md)

**Kestus**: 3-4 tundi | **Tase**: Edasijõudnud

---

### [9: Täiustatud mitmeagendi orkestreerimine](./samples/09/README.md)
**Fookus**: Peenetundeline agentide koordineerimine, spetsialiseerunud ülesannete jagamine ja koostöö AI töövood

**Põhiteemad**: Intelligente agentide koordineerimine • Funktsioonikutsumise mustrid • Agendidevaheline suhtlus • Töövoo orkestreerimine • Kvaliteedi tagamise mehhanismid

**Näide**: [Täiustatud mitmeagendi süsteem](./samples/09/README.md)

**Kestus**: 4-5 tundi | **Tase**: Ekspert

---

### [10: Foundry Local kui tööriistade raamistik](./samples/10/README.md)
**Fookus**: Tööriistakeskne arhitektuur Foundry Locali integreerimiseks olemasolevatesse rakendustesse ja raamistikesse

**Põhiteemad**: LangChain integratsioon • Semantiline Kernel funktsioonid • REST API raamistikud • CLI tööriistad • Jupyter integratsioon • Tootmis juurutuse mustrid

**Näide**: [Foundry tööriistade raamistik](./samples/10/README.md)

**Kestus**: 4-5 tundi | **Tase**: Ekspert

## Eeltingimused

### Süsteeminõuded
- **Operatsioonisüsteem**: Windows 11 (22H2 või uuem)
- **Mälu**: 16GB RAM (32GB soovitatav suuremate mudelite jaoks)
- **Salvestusruum**: 50GB vaba ruumi mudeli vahemäluks
- **Riistvara**: Soovitatav NPU-toega seade (Copilot+ PC), GPU valikuline
- **Võrk**: Kiire internet esialgseks mudelite allalaadimiseks

### Arenduskeskkond

- Visual Studio Code koos AI tööriistakomplektiga laiendusega
- Python 3.10+ ja pip
- Git versioonihalduseks
- PowerShell või käsuviip
- Azure CLI (pilveintegratsiooni jaoks valikuline)

### Teadmiste eeltingimused
- AI/ML kontseptsioonide põhitõdede mõistmine
- Käsurea tutvumine
- Python programmeerimise alused
- REST API kontseptsioonid
- Põhilised teadmised käsuandmisest ja mudelite ennustusest

## Mooduli ajakava

**Kokku hinnatud aeg**: 30-38 tundi

| Sessioon | Fookusala | Näited | Aeg | Komplekssus |
|---------|------------|---------|------|------------|
|  1 | Seadistamine & Alused | 01, 02, 03 | 2-3 tundi | Algaja |
|  2 | AI lahendused | 04 | 2-3 tundi | Kesktase |
|  3 | Avatud lähtekood | 05 | 2-3 tundi | Kesktase |
|  4 | Täiustatud mudelid | 06 | 3-4 tundi | Edasijõudnu |
|  5 | AI agendid | 05, 09 | 3-4 tundi | Edasijõudnu |
|  6 | Ettevõtte tööriistad | 06, 10 | 3-4 tundi | Ekspert |
|  7 | Otsene API integratsioon | 07 | 2-3 tundi | Kesktase |
|  8 | Windows 11 juturakendus | 08 | 3-4 tundi | Edasijõudnu |
|  9 | Täiustatud mitmeagendi süsteem | 09 | 4-5 tundi | Ekspert |
| 10 | Tööriistade raamistik | 10 | 4-5 tundi | Ekspert |

## Peamised ressursid

**Ametlik dokumentatsioon:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Lähtekood ja ametlikud näited
- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Täielik seadistus- ja kasutusjuhend
- [Model Mondays seeria](https://aka.ms/model-mondays) - Igapäevased mudelite tutvustused ja õpetused

**Kogukond & Tugi:**
- [Foundry Local arutelud](https://github.com/microsoft/Foundry-Local/discussions) - Kogukonna K&V ning funktsioonisoovid
- [Microsoft AI arendajate kogukond](https://techcommunity.microsoft.com/category/artificialintelligence) - Viimased uudised ja parimad praktikad

## Õpitulemused

Pärast selle mooduli lõpetamist oskad sa:

### Tehniline oskus
- **Paigalda ja halda**: Foundry Local paigaldusi nii arendus- kui ka tootmiskeskkondades
- **Integreeri mudeleid**: Töötada sujuvalt erinevate Microsofti, Hugging Face’i ja kogukonna mudelitega
- **Arenda rakendusi**: Loo tootmiskõlblikke AI rakendusi keerukate funktsioonide ja optimeeringutega
- **Arenda agente**: Rakenda keerukaid AI agente koos taustteadmiste, järelduste ja tööriistade integratsiooniga

### Strateegiline mõistmine
- **Arhitektuurilised otsused**: Tee teadlikke valikuid lokaalse vs pilvepõhise juurutuse vahel
- **Jõudluse optimeerimine**: Optimeeri ennustusprotsessi jõudlust erinevatel riistvarasätetel
- **Ettevõtte skaala**: Kujunda rakendused, mis skaleeruvad lokaalsetest prototüüpidest ettevõttetasemele
- **Privaatsus ja turvalisus**: Rakenda privaatsust säilitavaid AI lahendusi lokaalse ennustamisega

### Innovatsioonivõimekus
- **Kiire prototüüpimine**: Ehita ja testi kiiresti AI rakenduste kontseptsioone kõigis 10 näidismustris
- **Kogukonna integratsioon**: Kasuta avatud lähtekoodiga mudeleid ja panusta ökosüsteemi
- **Täpsemad mustrid**: Rakenda tipptasemel AI mustreid, sealhulgas RAG, agente ja tööriistade integratsiooni
- **Raamistiku valdamine**: Eksperditase integratsioon LangChaini, Semantic Kernel’i, Chainliti ja Electroniga
- **Tootmisse juurutamine**: Juuruta skaleeritavaid AI lahendusi lokaalsetest prototüüpidest ettevõttesüsteemideni
- **Tulevikuks valmis arendus**: Loo rakendusi, mis on valmis uusimate AI tehnoloogiate ja mustrite jaoks

## Alustamine

1. **Keskkonna seadistamine**: Veendu, et on olemas Windows 11 soovitatud riistvaraga (vt eeltingimusi)
2. **Installi Foundry Local**: Järgi sessiooni 1 juhiseid paigalduseks ja seadistuseks
3. **Käivita näidis 01**: Alusta põhilise REST API integratsiooniga setup’i kontrollimiseks
4. **Edasi näidistega**: Läbi kõik näited 01-10 põhjalikuks oskuste omandamiseks

## Edu mõõdikud

Jälgi oma edenemist kõigi 10 põhjalikult läbi töötatud näidise kaudu:

### Põhitaseme näited (01-03)
- [ ] Edukas Foundry Local paigaldus ja seadistus
- [ ] Täielik REST API integratsioon (näidis 01)
- [ ] OpenAI SDK ühilduvuse rakendamine (näidis 02)
- [ ] Mudeli avastamine ja võrdlus (näidis 03)

### Rakendusetase (04-06)
- [ ] Juhi ja käivita vähemalt 4 erinevat mudeliperet
- [ ] Loo funktsionaalne RAG vestlusrakendus (näidis 04)
- [ ] Loo mitmeagendi orkestreerimissüsteem (näidis 05)
- [ ] Rakenda intelligentne mudelite marsruutimine (näidis 06)

### Täiustatud integratsioonitase (07-10)
- [ ] Loo tootmiskõlblik API klient (näidis 07)
- [ ] Arenda Windows 11 natiivne juturakendus (näidis 08)
- [ ] Rakenda täiustatud mitmeagendi süsteem (näidis 09)
- [ ] Loo põhjalik tööriistade raamistik (näidis 10)

### Oskuse märgid
- [ ] Käivita edukalt kõik 10 näidist ilma vigadeta
- [ ] Kohanda vähemalt 3 näidet spetsiifilisteks kasutusjuhtudeks
- [ ] Juuruta 2+ näidist tootmislaadsetes keskkondades
- [ ] Panusta näidiskoodi täiustustesse või laiendustesse
- [ ] Integreeri Foundry Local mustreid isiklikes/professionaalsetes projektides

## Kiire stardi juhend - kõik 10 näidet

### Keskkonna seadistamine (nõutav kõigi näidiste jaoks)

```powershell
# 1. Klooni ja liigu kataloogi Module08
cd Module08

# 2. Loo Python virtuaalne keskkond
py -m venv .venv
.\.venv\Scripts\activate

# 3. Paigalda põhisisendid
pip install -r requirements.txt

# 4. Paigalda Foundry Local (kui pole veel paigaldatud)
winget install Microsoft.FoundryLocal

# 5. Kontrolli Foundry Local paigaldust
foundry --version
foundry model list
```

### Põhinäited (01-06)

**Näidis 01: REST Chat kiire käivitus**
```powershell
# Käivita Foundry Local teenus
foundry model run phi-4-mini

# Käivita REST vestluse demo
python samples/01/chat_quickstart.py
```

**Näidis 02: OpenAI SDK integratsioon**
```powershell
# Veenduge, et mudel töötab
foundry status

# Käivitage SDK demo
python samples/02/sdk_quickstart.py
```

**Näidis 03: Mudeli avastamine ja võrdlus**
```powershell
# Käivita ulatuslik mudelitestimine
samples/03/list_and_bench.cmd

# Või käivita üksikud komponendid
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Näidis 04: Chainlit RAG rakendus**
```powershell
# Paigalda Chainlit sõltuvused
pip install chainlit langchain chromadb

# Käivita RAG vestlusrakendus
chainlit run samples/04/app.py -w
# Avab brauseri aadressil http://localhost:8000
```

**Näidis 05: Mitmeagendi orkestreerimine**
```powershell
# Käivita agendi koordinaatori demo
python -m samples.05.agents.coordinator

# Käivita spetsiifiliste agendinäidete näited
python samples/05/examples/specialists_demo.py
```

**Näidis 06: Mudelid-tööriistadena marsruutimine**
```powershell
# Konfigureeri keskkond
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Käivita intelligentne ruuter
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Täiustatud integratsiooninäited (07-10)

**Näidis 07: Otsene API klient**
```powershell
# Navigeeri näidiskausta
cd samples/07

# Paigalda täiendavad sõltuvused
pip install -r requirements.txt

# Käivita põhilised API näited
python examples/basic_usage.py

# Proovi voogedastatud vastuseid
python examples/streaming.py

# Testi tootmismustreid
python examples/production.py
```

**Näidis 08: Windows 11 juturakendus**
```powershell
# Liigu näidiskataloogi
cd samples/08

# Paigalda Node.js sõltuvused
npm install

# Käivita Electroni rakendus
npm start

# Või ehita tootmiseks
npm run build
```

**Näidis 09: Täiustatud mitmeagendi süsteem**
```powershell
# Liikuge proovikausta
cd samples/09

# Paigaldage agendi süsteemi sõltuvused
pip install -r requirements.txt

# Käivitage põhiline koordineerimise näide
python examples/basic_coordination.py

# Proovige keerukat töövoogu
python examples/complex_workflow.py

# Interaktiivne agendi demonstratsioon
python examples/interactive_demo.py
```

**Näidis 10: Foundry tööriistade raamistik**
```powershell
# Liigu proovidirektoriumi
cd samples/10

# Paigalda raamistikusõltuvused
pip install -r requirements.txt

# Käivita põhivahendite demo
python examples/basic_tools.py

# Käivita REST API server
python examples/rest_api_server.py
# API saadaval aadressil http://localhost:8080

# Proovi käsurea rakendust
python examples/cli_application.py --help

# Käivita Jupyteri märkmik
jupyter notebook examples/jupyter_notebook.ipynb

# Testi LangChaini integratsiooni
python examples/langchain_demo.py
```

### Levinud probleemide tõrkeotsing

**Foundry Local ühenduse vead**
```powershell
# Kontrolli teenuse olekut
foundry status

# Taaskäivita vajadusel
foundry restart

# Kontrolli lõpp-punkti kättesaadavust
curl http://localhost:5273/v1/models
```

**Mudelite laadimise probleemid**
```powershell
# Kontrolli saadaolevaid mudeleid
foundry model list --cached

# Laadi puuduvad mudelid alla
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Vajadusel sundlaadi uuesti
foundry model unload --all
foundry model run phi-4-mini
```

**Sõltuvusprobleemid**
```powershell
# Uuenda pipi ja paigalda uuesti
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Node.js näidete jaoks
npm cache clean --force
npm install
```

## Kokkuvõte


See moodul esindab serva-AI arenduse tipptaset, ühendades Microsofti ettevõtetele mõeldud tööriistad avatud lähtekoodiga ökosüsteemi paindlikkuse ja innovatsiooniga. Õppides põhjalikult Foundry Locali kõiki 10 näidist, asetute AI rakenduste arenduse esiritta.

**Täielik õpitee:**
- **Alused** (näidised 01-03): API integratsioon ja mudelite haldamine
- **Rakendused** (näidised 04-06): RAG, agendid ja intelligentne marsruutimine
- **Täiustatud** (näidised 07-10): Tootmise raamistikud ja ettevõtte integratsioon

Azure OpenAI integratsiooni jaoks (seanss 2) vaadake üksikute näidiste README-faile, kus on toodud vajalikud keskkonnamuutujad ja API versiooni sätted.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->