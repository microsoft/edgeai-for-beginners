# Muutosloki

Kaikki merkittävät muutokset EdgeAI for Beginners -projektissa on dokumentoitu tähän. Tämä projekti käyttää päivämääräpohjaisia merkintöjä ja Keep a Changelog -tyyliä (Lisätty, Muutettu, Korjattu, Poistettu, Dokumentaatio, Siirretty).

## 2025-10-30

### Lisätty - Module06 AI Agents Kattava Parannus
- **Microsoft Agent Framework -integraatio** (`Module06/01.IntroduceAgent.md`):
  - Täydellinen osio Microsoft Agent Frameworkista tuotantovalmiiseen agenttikehitykseen
  - Yksityiskohtaiset integraatiomallit Foundry Localin kanssa reunaympäristöön
  - Moni-agentin orkestrointiesimerkit erikoistuneilla SLM-malleilla
  - Yritystason käyttöönotot resurssienhallinnalla ja valvonnalla
  - Turvallisuus- ja vaatimustenmukaisuustoiminnot reunajärjestelmiin
  - Käytännön toteutusesimerkit (vähittäiskauppa, terveydenhuolto, asiakaspalvelu)

- **Tuotantovalmiit SLM-agenttien käyttöönotto-strategiat**:
  - **Foundry Local**: Täydellinen yritystason reunalaskentaympäristön dokumentaatio asennuksesta, konfiguroinnista ja tuotantomalleista
  - **Ollama**: Parannettu yhteisökeskeinen käyttöönotto laajalla valvonnalla ja mallien hallinnalla
  - **VLLM**: Tehokas inferenssimoottori kehittyneillä optimointitekniikoilla ja yritysominaisuuksilla
  - Tuotantoon liittyvät tarkistuslistat ja vertailutaulukot kaikille kolmelle alustalle

- **Reunalle optimoidut SLM-kehykset**:
  - **ONNX Runtime**: Uusi kattava osio ristiinalustan SLM-agenttien käyttöönotolle
  - Yleiset käyttöönotto-mallit Windowsille, Linuxille, macOS:lle, iOS:lle ja Androidille
  - Laitteisto-kiihdytysvaihtoehdot (CPU, GPU, NPU) automaattisella tunnistuksella
  - Tuotantovalmiit ominaisuudet ja agenttikohtaiset optimoinnit
  - Täydelliset toteutusesimerkit Microsoft Agent Frameworkin integraatiolla

- **Viitteet ja lisälukeminen**:
  - Kattava resurssikirjasto, yli 100 auktoritatiivista lähdettä
  - Keskeiset tutkimuspaperit AI-agenteista ja pienen kielimallin (SLM) tekniikoista
  - Viralliset dokumentaatiot kaikista merkittävistä kehyksistä ja työkaluista
  - Toimialaraportit, markkina-analyysit ja tekniset vertailut
  - Koulutusmateriaalit, konferenssit ja yhteisöfoorumit
  - Standardit, määritykset ja vaatimustenmukaisuustyökalut

### Muutettu - Module06 Sisällön Päivitys
- **Parannetut oppimistavoitteet**: Lisätty Microsoft Agent Frameworkin hallinta ja reunakäyttöönotto-ominaisuudet
- **Tuotantokeskeisyys**: Siirrytty konseptuaalisesta toteutusvalmiiseen ohjeistukseen tuotantoesimerkkien kera
- **Koodiesimerkit**: Päivitetty kaikki esimerkit käyttämään moderneja SDK-malleja ja parhaiden käytäntöjen mukaisesti
- **Arkkitehtuurimallit**: Lisätty hierarkkiset agenttiarkkitehtuurit ja reunasta pilveen -koordinaatio
- **Suorituskyvyn optimointi**: Parannettu resurssienhallinnalla ja automaattisen skaalaamisen suosituksilla

### Dokumentaatio - Module06 Rakenneparannukset
- **Kattava agenttikehysdokumentaatio**: Alkeista yritystason käyttöönottoon
- **Tuotantokäyttöönotto-strategiat**: Kattavat oppaat Foundry Localille, Ollamalle ja VLLM:lle
- **Ristiinalustan optimointi**: ONNX Runtime lisätty yleiseen käyttöönottoon
- **Resurssikirjasto**: Laajat viitteet jatkuvaan oppimiseen ja toteutukseen

### Lisätty - Module06 Model Context Protocol (MCP) Dokumentaation Päivitys
- **MCP Johdannon modernisointi** (`Module06/03.IntroduceMCP.md`):
  - Päivitetty uusimpiin MCP-määrityksiin modelcontextprotocol.io (versio 2025-06-18)
  - Lisätty virallinen USB-C-analogia standardoiduille AI-sovellusliitännöille
  - Päivitetty arkkitehtuuriosio viralliseen kahden kerroksen malliin (Data Layer + Transport Layer)
  - Laajennettu ydintietoihin palvelinprimitivien (työkalut, resurssit, kehotteet) ja asiakasprimitivien (näytteistys, kysely, kirjaus) osalta

- **Kattavat MCP-viitteet ja resurssit**:
  - Lisätty **MCP for Beginners** -linkki (https://aka.ms/mcp-for-beginners) 
  - Virallinen MCP-dokumentaatio ja määritykset (modelcontextprotocol.io)
  - Kehitysresurssit kuten MCP Inspector ja referenssikoodit
  - Teknisiä standardeja (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Lisätty - Module04 Qualcomm QNN Integraatio
- **Uusi osio 7: Qualcomm QNN Optimointisetti** (`Module04/05.QualcommQNN.md`):
  - Kattava yli 400 rivin opas Qualcommin yhtenäiseen AI-inferenssikehykseen
  - Yksityiskohtainen heterogeenisen laskennan kattavuus (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Laitteistotietoinen optimointi Snapdragon-alustoille älykkäällä kuormanjakelulla
  - Edistyneet kvantisointitekniikat (INT8, INT16, sekakäyttö) mobiilikäyttöön
  - Virtapihi inferenssien optimointi akkuvirtaisiin laitteisiin ja reaaliaikaisiin sovelluksiin
  - Täydellinen asennusopas QNN SDK:n käyttöönotosta ja ympäristön konfiguroinnista
  - Käytännön esimerkit: PyTorchin muunnos QNN:ksi, monitaustainen optimointi, kontekstin binäärigenerointi
  - Edistyneet käyttötavat: räätälöity tausta-asetus, dynaaminen kvantisointi, suorituskyvyn profilointi
  - Kattava vianmääritysohje ja yhteisöresurssit

- **Parannettu Module04 rakenne**:
  - Päivitetty README.md sisältämään 7 vaiheittaista osiota (oli 6)
  - Lisätty Qualcomm QNN suorituskykyvertailutaulukkoon (5-15x nopeutus, 50-80 % muistin säästö)
  - Kattavat oppimistavoitteet mobiili-AI:n käyttöönotolle ja virranhallinnalle

### Muutettu - Module04 Dokumentaatiopäivitykset
- **Microsoft Olive dokumentaation parannus** (`Module04/03.MicrosoftOlive.md`):
  - Lisätty kattava "Olive Recipes Repository" -osio, joka kattaa yli 100 valmiiksi rakennettua optimointireseptiä
  - Yksityiskohtainen katsaus tuettuihin malliperheisiin (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Käytännön esimerkit reseptien räätälöinnistä ja yhteisön panoksista
  - Parannettu suoritustestien ja integrointiohjeiden osalta

- **Osioiden uudelleenjärjestely Module04:ssa**:
  - Apple MLX siirretty osioon 5 (aiemmin osio 6)
  - Workflow Synthesis siirretty osioon 6 (aiemmin osio 7)  
  - Qualcomm QNN sijoitettu osioon 7 (erikoistunut mobiili/reuna-keskeinen)
  - Päivitetty kaikki tiedostoviittaukset ja navigointilinkit vastaavasti

### Korjattu - Workshop-esimerkki Validointi
- **chat_bootstrap.py validointi ja korjaus**:
  - Korjattu rikkinäinen import-lauseke (`util.util.workshop_utils` → `util.workshop_utils`)
  - Luotu puuttuva `__init__.py` util-pakettiin Python-moduulin oikeaan resoluutioon
  - Asennettu tarvittavat riippuvuudet (openai, foundry-local-sdk) conda-ympäristöön
  - Onnistuneesti validoitu esimerkkien suoritus sekä oletus- että räätälöidyillä kehotteilla
  - Vahvistettu integraatio Foundry Local -palveluun ja mallin lataukseen (phi-4-mini CUDA-optimoinnilla)

### Dokumentaatio - Kattavat oppaan päivitykset
- **Module04 README.md perusteellinen uudelleenjärjestely**:
  - Lisätty Qualcomm QNN tärkeänä optimointikehyksenä OpenVINO:n, Oliven ja MLX:n rinnalle
  - Päivitetty lukujen oppimistavoitteet mobiili-AI:n käyttöönottoon ja virranhallintaan
  - Parannettu suorituskykyvertailutaulukko QNN-mittareilla ja mobiili/reunatapauksilla
  - Säilytetty looginen eteneminen yritysratkaisuista alustakohtaisiin optimointeihin

- **Ristiviittaukset ja navigointi**:
  - Päivitetty kaikki sisäiset linkit ja tiedostoviittaukset uuden osionumeroinnin mukaisiksi
  - Parannettu workflow-synteesin kuvailua sisältämään mobiili-, työpöytä- ja pilviympäristöt
  - Lisätty laajat resurssilinkit Qualcommin kehittäjäekosysteemiin

## 2025-10-08

### Lisätty - Workshop Kattava Päivitys
- **Workshop README.md:n täydellinen uudelleenkirjoitus**:
  - Lisätty kattava johdanto Edge AI:n arvolupaukseen (yksityisyys, suorituskyky, kustannukset)
  - Luotu 6 ydintavoitetta yksityiskohtaisilla osaamisalueilla
  - Lisätty oppimistulostaulukko toimituksista ja osaamismatriisista
  - Sisällytetty aluevalmiiden taitojen osio alan merkityksellisyydestä
  - Lisätty pika-aloitusopas vaatimuksilla ja kolmivaiheisella asennuksella
  - Luotu resurssitaulukot Python-esimerkeille (8 tiedostoa ja ajoajat)
  - Lisätty Jupyter-muistikirjataulukko (8 muistikirjaa vaikeustasoilla)
  - Luotu dokumentaatiotaulukko (7 keskeistä dokumenttia "Käytä kun" -ohjeistuksella)
  - Lisätty oppimispolun suositukset eri taitotasoille

- **Workshopin validointi- ja testausinfrastruktuuri**:
  - Luotu `scripts/validate_samples.py` - Kattava validointityökalu syntaksille, importeille ja parhaalle käytännölle
  - Luotu `scripts/test_samples.py` - Savutestien ajaja kaikille Python-esimerkeille
  - Lisätty validointidokumentaatio `scripts/README.md`:ään

- **Kattava dokumentaatio**:
  - Luotu `SAMPLES_UPDATE_SUMMARY.md` - Yli 400 rivin yksityiskohtainen opas kaikista parannuksista
  - Luotu `UPDATE_COMPLETE.md` - Päivityksen päätelmätiivistelmä
  - Luotu `QUICK_REFERENCE.md` - Pikakortti Workshopille

### Muutettu - Workshop Python-esimerkkien Päivitys
- **Kaikki 8 Python-esimerkkiä päivitetty parhaisiin käytäntöihin**:
  - Parannettu virheenkäsittelyä try-except-lohkoilla kaikissa I/O-toiminnoissa
  - Lisätty tyyppivihjeet ja kattavat docstringit
  - Toteutettu johdonmukainen [INFO]/[ERROR]/[RESULT] -lokitusmalli
  - Suojattu valinnaiset importit asennusvinkeillä
  - Parannettu käyttäjäpalautetta kaikissa esimerkeissä

- **session01/chat_bootstrap.py**:
  - Parannettu asiakasinitiaalisointia kattavilla virheilmoituksilla
  - Parannettu striimausvirheiden käsittelyä palastojen validoinnilla
  - Lisätty parempi poikkeuskäsittely palvelun käyttökatkoja varten

- **session02/rag_pipeline.py**:
  - Lisätty import-suojat lause-transformereille asennusvinkeillä
  - Parannettu virheenkäsittely upotusten ja generoinnin toiminnoissa
  - Parannettu tulosten muotoilua rakenteelliseksi

- **session02/rag_eval_ragas.py**:
  - Suojattu valinnaiset importit (ragas, datasets) käyttäjäystävällisillä virheilmoituksilla
  - Lisätty virheenkäsittely arviointimittareille
  - Parannettu arviointitulosten muotoilua

- **session03/benchmark_oss_models.py**:
  - Toteutettu pehmeä degradaatio (jatkuu mallivirheistä huolimatta)
  - Lisätty yksityiskohtainen edistymisraportti ja mallikohtainen virheenkäsittely
  - Parannettu tilastolaskentaa kattavalla virheiden palautuksella

- **session04/model_compare.py**:
  - Lisätty tyyppivihjeet (Tuple-palautetyypit)
  - Parannettu tulosten muotoilua rakenteellisella JSON-muodolla
  - Toteutettu mallikohtainen virheenkäsittely palautuksineen

- **session05/agents_orchestrator.py**:
  - Parannettu Agent.act() kattavilla docstringeillä
  - Lisätty pipeline-virheiden käsittely vaiheittaisella lokituksella
  - Parannettu muistin hallintaa ja tilan seurantaa

- **session06/models_router.py**:
  - Parannettu funktiodokumentaatiota kaikille reitityskomponenteille
  - Lisätty yksityiskohtainen lokitus route()-funktioon
  - Parannettu testituloksia rakenteellisella muotoilulla

- **session06/models_pipeline.py**:
  - Lisätty virheenkäsittely chat() apufunktioon
  - Parannettu pipeline()-toimintoa vaiheittaisella lokituksella ja etenemisen raportoinnilla
  - Parannettu main()-funktiota kattavalla virheiden palautuksella

### Dokumentaatio - Workshop Dokumentaation Parannus
- Päivitetty pääasiallinen README.md Workshop-osioon, joka korostaa käytännön oppimispolkua
- Parannettu STUDY_GUIDE.md kattavalla Workshop-osioilla, mukaan lukien:
  - Oppimistavoitteet ja opintokohteet
  - Itsearviointikysymykset
  - Käytännön harjoitukset aikatauluineen
  - Ajan allokointi intensiiviseen ja osa-aikaiseen opiskeluun
  - Lisätty Workshop edistymisen seurantamalliin
- Päivitetty ajan allokointiohje 20 tunnista 30 tuntiin (sisältäen Workshopin)
- Lisätty Workshop-esimerkkien kuvaukset ja oppimistulokset README:hen

### Korjattu
- Ratkaistu epäyhtenäiset virheenkäsittelymallit Workshop-esimerkeissä
- Korjattu valinnaisia riippuvuuksia koskevat tuontivirheet asennussuojauksilla
- Korjattu puuttuvat tyyppivihjeet kriittisissä funktioissa
- Parannettu käyttäjäpalautetta virhetilanteissa
- Korjattu validointiongelmat kattavalla testausinfrastruktuurilla

---

## 2025-09-23

### Muutettu - Suuri Module 08 Modernisointi
- **Täydellinen yhteensovitus Microsoft Foundry-Local -arkiston käytäntöihin**
  - Päivitetty kaikki koodiesimerkit käyttämään modernia `FoundryLocalManager`- ja OpenAI SDK -integraatiota
  - Korvattu vanhentuneet manuaaliset `requests`-kutsut asianmukaisella SDK-käytöllä
  - Yhdistetty toteutusmallit virallisen Microsoft-dokumentaation ja esimerkkien mukaisesti

- **05.AIPoweredAgents.md uudelleen kirjoitus**:
  - Päivitetty moni-agentin orkestrointi käyttämään moderneja SDK-malleja
  - Parannettu koordinaattorin toteutus kehittyneillä ominaisuuksilla (palautejärjestelmät, suorituskyvyn valvonta)
  - Lisätty kattava virheenkäsittely ja palvelun toiminnan tarkistus
  - Integroitu oikein paikallisiin näytteisiin (`samples/05/multi_agent_orchestration.ipynb`)
  - Päivitetty funktiokutsuesimerkit käyttämään modernia `tools`-parametria vanhentuneen `functions` sijaan
  - Lisätty tuotantovalmiita malleja valvonnalla ja tilastoseurannalla

- **06.ModelsAsTools.md täydellinen uudelleenkirjoitus**:
  - Korvattu perus työkalurekisteri älykkäällä mallireitittimen toteutuksella
  - Lisätty avainsanapohjainen mallin valinta eri tehtävätyypeille (yleinen, päättely, koodi, luova)
  - Integroitu ympäristöperusteinen konfigurointi joustavalla mallinmäärityksellä
  - Parannettu palvelun kunnon valvonnalla ja virheenkäsittelyllä
  - Lisätty tuotantokäyttöönotto-malleja pyynnön seurannalla ja suorituskyvyn mittaroinnilla
  - Sovitettu paikallisiin toteutuksiin tiedostoissa `samples/06/router.py` ja `samples/06/model_router.ipynb`

- **Dokumentaation rakenneparannukset**:
  - Lisätty yleiskatsausosiot korostaen modernisointia ja SDK-sovitusta
  - Parannettu hymiöillä ja paremmalla muotoilulla luettavuuden lisäämiseksi
  - Lisätty asianmukaiset viittaukset paikallisiin esimerkkitiedostoihin dokumentaatiossa
  - Sisällytetty tuotantovalmiiden toteutusten ohjeistus ja parhaat käytännöt

### Lisätty
- Kattavat yleiskatsausosiot Module 08 tiedostoihin korostaen modernia SDK-integraatiota
- Arkkitehtuurin kohokohdat korostaen kehittyneitä ominaisuuksia (moni-agenttijärjestelmät, älykäs reititys)
- Suorat viittaukset paikallisiin esimerkkitoteutuksiin käytännön oppimista varten
- Tuotantokäyttöönotto-ohjeistus valvonnalla ja virheenkäsittelymalleilla
- Interaktiiviset Jupyterin muistikirjaesimerkit kehittyneillä ominaisuuksilla ja vertailuilla

### Korjattu
- Yhtenäisyyden puutokset dokumentaation ja todellisten esimerkkitoteutusten välillä
- Vanhentuneet SDK käyttömallit Module 08:ssa
- Puuttuvat viittaukset kattavaan paikalliseen esimerkkikirjastoon
- Epäjohdonmukaiset toteutuslähestymistavat eri osioissa

---

## 2025-09-18

### Lisätty
- Module 08: Microsoft Foundry Local – Täydellinen kehittäjätyökalupakki
  - Kuusi sessiota: asennus, Azure AI Foundry -integraatio, avoimen lähdekoodin mallit, huipputeknologian demot, agentit ja mallit työkalujen muodossa
  - Suoritettavat esimerkit kansiossa `Module08/samples/01`–`06` Windowsin komentokehotteella
    - `01` REST nopea chat (`chat_quickstart.py`)

    - `02` SDK pika-aloitus OpenAI/Foundry Local- ja Azure OpenAI -tuella (`sdk_quickstart.py`)
    - `03` CLI listaus ja vertailu (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agentti-orchestrointi (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools reititin (`router.py`)
- Azure OpenAI -tuki Session 2 SDK-esimerkkissä ympäristömuuttujakonfiguraatiolla
- `.vscode/settings.json` osoittamaan `Module08/.venv` ja parantamaan Python-analyysin resoluutiota
- `.env` tiedosto `PYTHONPATH` vihjeellä VS Code/Pylance -tunnistusta varten

### Muutettu
- Oletusmalli päivitetty `phi-4-mini`:ksi Module 08:n dokumentaatiossa ja esimerkeissä; jäljellä olevat `phi-3.5` maininnat poistettu Module 08:sta
- Reititin (`Module08/samples/06/router.py`) parannukset:
  - Päätepisteen haku `foundry service status` komennolla regex-analyysilla
  - `/v1/models` terveystarkistus käynnistyksessä
  - Ympäristömuuttujalla konfiguroitava mallirekisteri (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Päivitetyt vaatimukset: `Module08/requirements.txt` sisältää nyt `openai` (yhdessä `requests` ja `chainlit` kanssa)
- Chainlit-esimerkin ohjeistusta selkeytetty ja vianmääritys lisätty; tuonnin resoluutio työtilan asetuksilla

### Korjattu
- Ratkaistu tuontiongelmat:
  - Reititin ei enää riipu olemattomasta `utils`-moduulista; funktiot inline-muodossa
  - Koordinaattori käyttää suhteellista tuontia (`from .specialists import ...`) ja kutsutaan moduulipolun kautta
  - VS Code/Pylance -konfiguraatio `chainlit` ja pakettituontien resoluutiota varten
- Korjattu pieni kirjoitusvirhe `STUDY_GUIDE.md`:ssä ja lisätty Module 08:n kattavuus

### Poistettu
- Poistettu käyttämätön `Module08/infra/obs.py` ja tyhjä `infra/` hakemisto; havainnointimallit säilytetty valinnaisina dokumentaatiossa

### Siirretty
- Yhdistetty Module 08 demot `Module08/samples` alle istuntokohtaisiin kansioihin
  - Chainlit-sovellus siirretty `samples/04` kansioon
  - Agentit siirretty `samples/05` ja lisätty `__init__.py` tiedostot pakettien resoluutiota varten

### Dokumentaatio
- Module 08 istuntodokumentaatio ja kaikki esimerkkien README:t rikastettu Microsoft Learn- ja luotettujen toimittajien viitteillä
- `Module08/README.md` päivitetty sisältämään Yleisnäkymä esimerkeistä, reitittimen konfiguraatio ja validointivinkkejä
- `Module07/README.md` Windows Foundry Local -osio validoitu Learn-dokumentaation kanssa
- `STUDY_GUIDE.md` päivitetty:
  - Lisätty Module 08 yleiskatsaukseen, aikatauluihin ja etenemisen seurantalaskuriin
  - Lisätty kattava Viitteet-osio (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiallinen (yhteenveto)
- Kurssin arkkitehtuuri ja moduulit luotu (Moduulit 01–07)
- Sisällön iteratiivinen modernisointi, muotoilun standardisointi ja tapaustutkimusten lisääminen
- Optimointikehysten laajennettu kattavuus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Julkaisematon / Taustalla (ehdotukset)
- Valinnaiset per-esimerkki 'savuttomat' testit Foundry Local -käytettävyyden varmistamiseksi
- Käännösten tarkistus malliviittausten yhtenäistämiseksi (esim. `phi-4-mini`)
- Lisää minimaalinen pyright-konfiguraatio, mikäli tiimit haluavat työtila-laajuista tiukkuutta

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->