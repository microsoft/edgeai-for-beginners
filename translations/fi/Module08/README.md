# Moduuli 08: Käytännön harjoitus Microsoft Foundry Localin kanssa - Täydellinen kehittäjätyökalupakki

## Yleiskatsaus

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) edustaa reunalaskennan AI-kehityksen seuraavaa sukupolvea, tarjoten kehittäjille tehokkaita työkaluja AI-sovellusten rakentamiseen, käyttöönottoon ja skaalaamiseen paikallisesti samalla, kun säilytetään saumaton integraatio Azure AI Foundryn kanssa. Tämä moduuli tarjoaa kattavan käsittelyn Foundry Localista asennuksesta edistyneeseen agenttikehitykseen.

**Keskeiset teknologiat:**
- Microsoft Foundry Local CLI ja SDK
- Azure AI Foundryn integrointi
- Mallien tulkinta laitteessa
- Paikallinen mallien välimuisti ja optimointi
- Agenttipohjaiset arkkitehtuurit

## Oppimistavoitteet

Suoritettuasi tämän moduulin:

- **Hallitse Foundry Local**: Asenna, konfiguroi ja optimoi Windows 11 -kehitystä varten
- **Ota käyttöön erilaisia malleja**: Suorita phi-, qwen-, deepseek- ja GPT-mallit paikallisesti CLI-komentojen avulla
- **Rakenna tuotantoratkaisuja**: Luo AI-sovelluksia kehittyneen prompt-suunnittelun ja dataintegroinnin avulla
- **Hyödynnä avoimen lähdekoodin ekosysteemiä**: Integroi Hugging Face -mallit ja yhteisön panokset
- **Kehitä AI-agentteja**: Rakenna älykkäitä agenteja pohjaten ja orkestrointikyvyillä
- **Toteuta yritystason malleja**: Luo modulaarisia, skaalautuvia AI-ratkaisuja tuotantokäyttöön

## Istunnon rakenne

### [1: Aloitus Foundry Localin kanssa](./01.FoundryLocalSetup.md)
**Painopiste**: Asennus, CLI-asetus, mallin käyttöönotto ja laitteiston optimointi

**Keskeiset aiheet**: Täydellinen asennus • CLI-komennot • Mallien välimuisti • Laitteiston kiihdytys • Monimallin käyttöönotto

**Esimerkki**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK -integraatio](./samples/02/README.md) • [Mallin löytäminen ja vertailu](./samples/03/README.md)

**Kesto**: 2-3 tuntia | **Taso**: Aloittelija

---

### [2: Rakenna AI-ratkaisuja Azure AI Foundryn kanssa](./02.AzureAIFoundryIntegration.md)
**Painopiste**: Edistynyt prompt-suunnittelu, dataintegraatio ja pilviyhteydet

**Keskeiset aiheet**: Prompt-suunnittelu • Dataintegraatio • Azure-työnkulut • Suorituskyvyn optimointi • Valvonta

**Esimerkki**: [Chainlit RAG -sovellus](./samples/04/README.md)

**Kesto**: 2-3 tuntia | **Taso**: Keskitaso

---

### [3: Avoimen lähdekoodin mallit Foundry Localissa](./03.OpenSourceModels.md)
**Painopiste**: Hugging Face -integraatio, BYOM-strategiat ja yhteisön mallit

**Keskeiset aiheet**: HuggingFace-integraatio • Bring-your-own-model • Model Mondays -näkemykset • Yhteisön panokset • Mallin valinta

**Esimerkki**: [Moni-agenttien orkestrointi](./samples/05/README.md)

**Kesto**: 2-3 tuntia | **Taso**: Keskitaso

---

### [4: Tutustu huipputeknologian malleihin](./04.CuttingEdgeModels.md)
**Painopiste**: LLM:t vs SLM:t, EdgeAI:n toteutus ja edistyneet demonstraatiot

**Keskeiset aiheet**: Mallien vertailu • Reuna- vs pilvitulkinta • Phi + ONNX Runtime • Chainlit RAG -sovellus • WebGPU-optimointi

**Esimerkki**: [Mallien työkalureititin](./samples/06/README.md)

**Kesto**: 3-4 tuntia | **Taso**: Edistynyt

---

### [5: Rakenna AI-vetoiset agentit nopeasti](./05.AIPoweredAgents.md)
**Painopiste**: Agenttiarkkitehtuurit, järjestelmäpromptit, perustaminen ja orkestrointi

**Keskeiset aiheet**: Agenttisuunnittelumallit • Järjestelmäprompt-suunnittelu • Perustamistavat • Moni-agenttijärjestelmät • Tuotantokäyttöön otto

**Esimerkki**: [Moni-agenttien orkestrointi](./samples/05/README.md) • [Edistynyt moni-agenttijärjestelmä](./samples/09/README.md)

**Kesto**: 3-4 tuntia | **Taso**: Edistynyt

---

### [6: Foundry Local - Mallit työkaluna](./06.ModelsAsTools.md)
**Painopiste**: Modulaariset AI-ratkaisut, yritysskaalaus ja tuotantomallit

**Keskeiset aiheet**: Mallit työkaluna • Laitteessa käyttöönotto • SDK/API -integraatio • Yritysarkkitehtuurit • Skaalausstrategiat

**Esimerkki**: [Mallien työkalureititin](./samples/06/README.md) • [Foundry Tools -kehys](./samples/10/README.md)

**Kesto**: 3-4 tuntia | **Taso**: Asiantuntija

---

### [7: Suorat API-integraatiomallit](./samples/07/README.md)
**Painopiste**: Puhtaan REST API -integraation toteutus ilman SDK-riippuvuuksia maksimikontrollia varten

**Keskeiset aiheet**: HTTP-asiakasohjelman toteutus • Mukautettu autentikointi • Mallin terveydentilan seuranta • Suoratoistovastaukset • Tuotanto-virheiden hallinta

**Esimerkki**: [Suora API-asiakas](./samples/07/README.md)

**Kesto**: 2-3 tuntia | **Taso**: Keskitaso

---

### [8: Windows 11:n natiivisovellus chatille](./samples/08/README.md)
**Painopiste**: Modernien natiivisten chat-sovellusten rakentaminen Foundry Local -integraation avulla

**Keskeiset aiheet**: Electron-kehitys • Fluent Design System • Natiivi Windows-integraatio • Reaaliaikainen suoratoisto • Chat-käyttöliittymän suunnittelu

**Esimerkki**: [Windows 11 Chat -sovellus](./samples/08/README.md)

**Kesto**: 3-4 tuntia | **Taso**: Edistynyt

---

### [9: Edistynyt moni-agenttien orkestrointi](./samples/09/README.md)
**Painopiste**: Monimutkainen agenttien koordinointi, erikoistunut tehtävien delegointi ja yhteistyöhön perustuvat AI-työnkulut

**Keskeiset aiheet**: Älykäs agenttien koordinointi • Funktioiden kutsumismallit • Agenttien välinen viestintä • Työnkulun orkestrointi • Laadunvarmistusmekanismit

**Esimerkki**: [Edistynyt moni-agenttijärjestelmä](./samples/09/README.md)

**Kesto**: 4-5 tuntia | **Taso**: Asiantuntija

---

### [10: Foundry Local työkalukehyksenä](./samples/10/README.md)
**Painopiste**: Työkeskeinen arkkitehtuuri Foundry Localin integroimiseksi olemassa oleviin sovelluksiin ja kehyksiin

**Keskeiset aiheet**: LangChain-integraatio • Semantic Kernel -funktiot • REST API -kehykset • CLI-työkalut • Jupyter-integraatio • Tuotantokäyttöönottomallit

**Esimerkki**: [Foundry Tools -kehys](./samples/10/README.md)

**Kesto**: 4-5 tuntia | **Taso**: Asiantuntija

## Esivaatimukset

### Järjestelmävaatimukset
- **Käyttöjärjestelmä**: Windows 11 (22H2 tai uudempi)
- **Muisti**: 16 Gt RAM (32 Gt suositeltava isommille malleille)
- **Tallennustila**: 50 Gt vapaata tilaa mallien välimuistille
- **Laitteisto**: NPU-toimintoinen laite suositeltava (Copilot+ PC), GPU vapaaehtoinen
- **Verkko**: Nopea internetyhteys mallien ensilataukseen

### Kehitysympäristö

- Visual Studio Code AI Toolkit -laajennuksella
- Python 3.10+ ja pip
- Git versiohallintaan
- PowerShell tai Komentokehote
- Azure CLI (valinnainen pilvi-integraatioon)

### Tietovaatimukset
- Perusymmärrys tekoäly-/koneoppimiskäsitteistä
- Kokemus komentoriviltä
- Python-ohjelmoinnin perusteet
- REST API -käsitteet
- Perustiedot kehotteista ja mallin päättelystä

## Moduulin aikataulu

**Kokonaisarvioitu aika**: 30-38 tuntia

| Istunto | Keskittymisalue | Esimerkit | Aika | Vaativuus |
|---------|------------|---------|------|------------|
|  1 | Asennus & Perusteet | 01, 02, 03 | 2-3 tuntia | Aloittelija |
|  2 | Tekoälyratkaisut | 04 | 2-3 tuntia | Keskitaso |
|  3 | Avoin lähdekoodi | 05 | 2-3 tuntia | Keskitaso |
|  4 | Kehittyneet mallit | 06 | 3-4 tuntia | Edistynyt |
|  5 | Tekoälyagentit | 05, 09 | 3-4 tuntia | Edistynyt |
|  6 | Yritystyökalut | 06, 10 | 3-4 tuntia | Asiantuntija |
|  7 | Suora API-integraatio | 07 | 2-3 tuntia | Keskitaso |
|  8 | Windows 11 -keskustelusovellus | 08 | 3-4 tuntia | Edistynyt |
|  9 | Kehittynyt moni-agenttijärjestelmä | 09 | 4-5 tuntia | Asiantuntija |
| 10 | Työkalukehys | 10 | 4-5 tuntia | Asiantuntija |

## Keskeiset resurssit

**Virallinen dokumentaatio:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Lähdekoodi ja viralliset esimerkit
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Täydellinen asennus- ja käyttöopas
- [Model Mondays Series](https://aka.ms/model-mondays) - Viikoittaiset malliesittelyt ja opetusohjelmat

**Yhteisö & Tuki:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Yhteisön kysymykset ja ominaisuuspyynnöt
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Viimeisimmät uutiset ja parhaat käytännöt

## Oppimistulokset

Moduulin suoritettuasi osaat:

### Tekninen osaaminen
- **Ota käyttöön ja hallitse**: Foundry Local -asennuksia kehitys- ja tuotantoympäristöissä
- **Integroi malleja**: Sujuvaa työskentelyä monipuolisten Microsoftin, Hugging Facen ja yhteisön malliperheiden kanssa
- **Rakenna sovelluksia**: Luo tuotantovalmiita tekoälysovelluksia kehittyneillä ominaisuuksilla ja optimoinneilla
- **Kehitä agentteja**: Toteuta monimutkaisia tekoälyagentteja, joissa on pohjustus, päättely ja työkalujen integrointi

### Strateginen ymmärrys
- **Arkkitehtuuripäätökset**: Tee tietoon perustuvia valintoja paikallisen ja pilvipohjaisen käyttöönoton välillä
- **Suorituskyvyn optimointi**: Optimoi päättelysuorituskyky eri laitteistokokoonpanoissa
- **Yritystason skaalaus**: Suunnittele sovelluksia, jotka skaalautuvat paikallisista prototyypeistä yritystason käyttöönottoihin
- **Yksityisyys ja turvallisuus**: Toteuta yksityisyyttä suojaavia tekoälyratkaisuja paikallisella päättelyllä

### Innovointikyvyt
- **Nopea prototypointi**: Rakenna ja testaa AI-sovellusideoita nopeasti kaikilla 10 esimerkkikuvioinnilla
- **Yhteisöintegraatio**: Hyödynnä avoimen lähdekoodin malleja ja osallistu ekosysteemiin
- **Kehittyneet mallit**: Toteuta huipputason tekoälykuviointeja kuten RAG, agentit ja työkalujen integrointi
- **Kehyksen hallinta**: Asiantuntijan tason integrointi LangChainin, Semantic Kernelin, Chainlitin ja Electronin kanssa
- **Tuotantokäyttöönotto**: Julkaise skaalautuvia tekoälyratkaisuja paikallisista prototyypeistä yritysjärjestelmiin
- **Tulevaisuuden kehitys**: Rakenna sovelluksia, jotka ovat valmiita nouseviin tekoälyteknologioihin ja -kuvioihin

## Aloittaminen

1. **Ympäristön valmistelu**: Varmista Windows 11 suositeltuilla laitteistoilla (katso Vaatimukset)
2. **Asenna Foundry Local**: Seuraa Istunto 1 täydellistä asennusta ja konfigurointia
3. **Suorita Esimerkki 01**: Aloita perus REST API -integraatiolla asetusten varmistamiseksi
4. **Edisty Esimerkeissä**: Suorita esimerkit 01-10 kattavan osaamisen saavuttamiseksi

## Onnistumisen mittarit

Seuraa edistymistäsi kaikkien 10 kattavan esimerkin kautta:

### Perustaso (Esimerkit 01-03)
- [ ] Asenna ja konfiguroi Foundry Local onnistuneesti
- [ ] Suorita REST API -integraatio (Esimerkki 01)
- [ ] Toteuta OpenAI SDK -yhteensopivuus (Esimerkki 02)
- [ ] Suorita mallin löytäminen ja vertailu (Esimerkki 03)

### Sovellustaso (Esimerkit 04-06)
- [ ] Ota käyttöön ja aja vähintään 4 eri malliperhettä
- [ ] Rakenna toimiva RAG-keskustelusovellus (Esimerkki 04)
- [ ] Luo moni-agenttien orkestrointijärjestelmä (Esimerkki 05)
- [ ] Toteuta älykäs mallien reititys (Esimerkki 06)

### Edistynyt integraatiotaso (Esimerkit 07-10)
- [ ] Rakenna tuotantovalmiita API-asiakkaita (Esimerkki 07)
- [ ] Kehitä Windows 11 natiivi keskustelusovellus (Esimerkki 08)
- [ ] Toteuta edistynyt moni-agenttijärjestelmä (Esimerkki 09)
- [ ] Luo kattava työkalukehys (Esimerkki 10)

### Hallinnan merkit
- [ ] Suorita kaikki 10 esimerkkiä virheettä
- [ ] Räätälöi vähintään 3 esimerkkiä erityistapauksiin
- [ ] Ota käyttöön 2+ esimerkkiä tuotantoympäristöissä
- [ ] Tee parannuksia tai laajennuksia esimerkkikoodiin
- [ ] Integroi Foundry Local -kuviot henkilökohtaisiin/ammatillisiin projekteihin

## Pikakäynnistysopas - Kaikki 10 esimerkkiä

### Ympäristön valmistelu (vaaditaan kaikille esimerkeille)

```powershell
# 1. Kloonaa ja siirry hakemistoon Module08
cd Module08

# 2. Luo Pythonin virtuaaliympäristö
py -m venv .venv
.\.venv\Scripts\activate

# 3. Asenna perusriippuvuudet
pip install -r requirements.txt

# 4. Asenna Foundry Local (jos sitä ei ole jo asennettu)
winget install Microsoft.FoundryLocal

# 5. Varmista Foundry Local -asennus
foundry --version
foundry model list
```

### Peruskohde-esimerkit (01-06)

**Esimerkki 01: REST Chat Pikakäynnistys**
```powershell
# Käynnistä Foundry Local -palvelu
foundry model run phi-4-mini

# Suorita REST-chat-demo
python samples/01/chat_quickstart.py
```

**Esimerkki 02: OpenAI SDK Integraatio**
```powershell
# Varmista, että malli on käynnissä
foundry status

# Suorita SDK-demo
python samples/02/sdk_quickstart.py
```

**Esimerkki 03: Mallin löytäminen & vertailu**
```powershell
# Suorita kattava mallin testaus
samples/03/list_and_bench.cmd

# Tai suorita yksittäiset komponentit
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Esimerkki 04: Chainlit RAG -sovellus**
```powershell
# Asenna Chainlit-riippuvuudet
pip install chainlit langchain chromadb

# Käynnistä RAG-chat-sovellus
chainlit run samples/04/app.py -w
# Avaa selain osoitteessa http://localhost:8000
```

**Esimerkki 05: Moni-agenttien orkestrointi**
```powershell
# Suorita agenttikoordinaattorin demo
python -m samples.05.agents.coordinator

# Suorita tiettyjen agenttien esimerkit
python samples/05/examples/specialists_demo.py
```

**Esimerkki 06: Mallit työkalujen reitittimenä**
```powershell
# Määritä ympäristö
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Suorita älykäs reititin
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Edistyneet integraatioesimerkit (07-10)

**Esimerkki 07: Suora API-asiakas**
```powershell
# Siirry näytteiden hakemistoon
cd samples/07

# Asenna lisäriippuvuudet
pip install -r requirements.txt

# Suorita perus API-esimerkit
python examples/basic_usage.py

# Kokeile suoratoistovastauksia
python examples/streaming.py

# Testaa tuotantomallit
python examples/production.py
```

**Esimerkki 08: Windows 11 keskustelusovellus**
```powershell
# Siirry esimerkkihakemistoon
cd samples/08

# Asenna Node.js-riippuvuudet
npm install

# Käynnistä Electron-sovellus
npm start

# Tai rakenna tuotantokäyttöön
npm run build
```

**Esimerkki 09: Edistynyt moni-agenttijärjestelmä**
```powershell
# Siirry sample-hakemistoon
cd samples/09

# Asenna agenttijärjestelmän riippuvuudet
pip install -r requirements.txt

# Suorita peruskoordinaatioesimerkki
python examples/basic_coordination.py

# Kokeile monimutkaista työnkulkua
python examples/complex_workflow.py

# Interaktiivinen agenttidemo
python examples/interactive_demo.py
```

**Esimerkki 10: Foundryn työkalukehys**
```powershell
# Siirry esimerkkihakemistoon
cd samples/10

# Asenna kehyksen riippuvuudet
pip install -r requirements.txt

# Suorita perus työkalujen demo
python examples/basic_tools.py

# Käynnistä REST API -palvelin
python examples/rest_api_server.py
# API saatavilla osoitteessa http://localhost:8080

# Kokeile komentorivisovellusta
python examples/cli_application.py --help

# Käynnistä Jupyter-muistikirja
jupyter notebook examples/jupyter_notebook.ipynb

# Testaa LangChain-integraatio
python examples/langchain_demo.py
```

### Yleisten ongelmien vianmääritys

**Foundry Local-yhteysvirheet**
```powershell
# Tarkista palvelun tila
foundry status

# Käynnistä uudelleen tarvittaessa
foundry restart

# Varmista päätepisteen saavutettavuus
curl http://localhost:5273/v1/models
```

**Mallin latausongelmat**
```powershell
# Tarkista saatavilla olevat mallit
foundry model list --cached

# Lataa puuttuvat mallit
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Pakota uudelleenlataus tarvittaessa
foundry model unload --all
foundry model run phi-4-mini
```

**Riippuvuuksien ongelmat**
```powershell
# Päivitä pip ja asenna uudelleen
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Node.js-esimerkeille
npm cache clean --force
npm install
```

## Yhteenveto


Tämä moduuli edustaa reunalaskennan tekoälyn huippua, yhdistäen Microsoftin yritystason työkalut avoimen lähdekoodin ekosysteemin joustavuuteen ja innovaatioihin. Hallitsemalla Foundry Localin kaikkien 10 kattavan esimerkin kautta, olet tekoälysovellusten kehityksen eturintamassa.

**Täydellinen oppimispolku:**
- **Perusteet** (Esimerkit 01-03): API-integraatio ja mallien hallinta
- **Sovellukset** (Esimerkit 04-06): RAG, agentit ja älykäs reititys
- **Edistynyt** (Esimerkit 07-10): Tuotantokehykset ja yritysintegrointi

Azure OpenAI -integraatiota varten (Istunto 2) katso yksittäisten esimerkkien README-tiedostot vaadittavista ympäristömuuttujista ja API-version asetuksista.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->