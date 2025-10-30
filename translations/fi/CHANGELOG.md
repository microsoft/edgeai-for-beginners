<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T13:14:43+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fi"
}
-->
# Muutosloki

Kaikki merkittävät muutokset EdgeAI for Beginners -projektiin dokumentoidaan täällä. Tämä projekti käyttää päivämääräperusteisia merkintöjä ja Keep a Changelog -tyyliä (Lisätty, Muutettu, Korjattu, Poistettu, Dokumentaatio, Siirretty).

## 2025-10-30

### Lisätty - Module06 AI Agents Comprehensive Enhancement
- **Microsoft Agent Framework -integraatio** (`Module06/01.IntroduceAgent.md`):
  - Koko osio Microsoft Agent Frameworkista tuotantovalmiiden agenttien kehittämiseen
  - Yksityiskohtaiset integraatiomallit Foundry Localin kanssa reunasovelluksia varten
  - Esimerkkejä monen agentin orkestroinnista erikoistuneilla SLM-malleilla
  - Yritystason käyttöönoton mallit resurssien hallinnalla ja seurannalla
  - Turvallisuus- ja vaatimustenmukaisuusominaisuudet reunasovellusten agenttijärjestelmiin
  - Käytännön toteutusesimerkkejä (vähittäiskauppa, terveydenhuolto, asiakaspalvelu)

- **Tuotantotason SLM-agenttien käyttöönotto-strategiat**:
  - **Foundry Local**: Täydellinen yritystason reunasovellusten AI-ajoympäristön dokumentaatio asennuksesta, konfiguroinnista ja tuotantokäytännöistä
  - **Ollama**: Parannettu yhteisökeskeinen käyttöönotto kattavalla seurannalla ja mallien hallinnalla
  - **VLLM**: Suorituskykyinen inferenssimoottori edistyneillä optimointitekniikoilla ja yritysominaisuuksilla
  - Tuotantokäyttöönottolistat ja vertailutaulukot kaikille kolmelle alustalle

- **Reunaoptimoitujen SLM-kehysten parannukset**:
  - **ONNX Runtime**: Uusi kattava osio alustojen väliseen SLM-agenttien käyttöönottoon
  - Universaalit käyttöönoton mallit Windowsille, Linuxille, macOS:lle, iOS:lle ja Androidille
  - Laitteistokiihdytysvaihtoehdot (CPU, GPU, NPU) automaattisella tunnistuksella
  - Tuotantovalmiit ominaisuudet ja agenttikohtaiset optimoinnit
  - Täydelliset toteutusesimerkit Microsoft Agent Framework -integraatiolla

- **Viitteet ja lisälukemista**:
  - Kattava resurssikirjasto, jossa yli 100 auktoriteettista lähdettä
  - Keskeiset tutkimuspaperit AI-agenteista ja pienistä kielimalleista
  - Virallinen dokumentaatio kaikille tärkeimmille kehyksille ja työkaluille
  - Teollisuusraportit, markkina-analyysit ja tekniset vertailut
  - Koulutusresurssit, konferenssit ja yhteisöfoorumit
  - Standardit, spesifikaatiot ja vaatimustenmukaisuuskehykset

### Muutettu - Module06 Sisällön Modernisointi
- **Parannetut oppimistavoitteet**: Lisätty Microsoft Agent Frameworkin hallinta ja reunasovellusten käyttöönotto-osaaminen
- **Tuotantokeskeisyys**: Siirrytty käsitteellisestä toteutusvalmiiseen ohjeistukseen tuotantoesimerkeillä
- **Koodiesimerkit**: Päivitetty kaikki esimerkit käyttämään moderneja SDK-malleja ja parhaita käytäntöjä
- **Arkkitehtuurimallit**: Lisätty hierarkkiset agenttiarkkitehtuurit ja reuna-pilvi-yhteistyö
- **Suorituskyvyn optimointi**: Parannettu resurssien hallinnalla ja automaattisen skaalaamisen suosituksilla

### Dokumentaatio - Module06 Rakenteen Parannus
- **Kattava Agent Framework -kattavuus**: Peruskäsitteistä yritystason käyttöönottoon
- **Tuotantokäyttöönottostrategiat**: Täydelliset oppaat Foundry Localille, Ollamalle ja VLLM:lle
- **Alustojen välinen optimointi**: Lisätty ONNX Runtime universaaliin käyttöönottoon
- **Resurssikirjasto**: Laajat viitteet jatkuvaan oppimiseen ja toteutukseen

### Lisätty - Module06 Model Context Protocol (MCP) Dokumentaation Päivitys
- **MCP Johdannon Modernisointi** (`Module06/03.IntroduceMCP.md`):
  - Päivitetty uusimmilla MCP-määrityksillä modelcontextprotocol.io-sivustolta (versio 2025-06-18)
  - Lisätty virallinen USB-C-analogia standardoituihin AI-sovellusten yhteyksiin
  - Päivitetty arkkitehtuuriosio virallisella kaksikerroksisella suunnittelulla (Datalayer + Kuljetuskerros)
  - Parannettu ydinkäsitteiden dokumentaatio palvelinprimitiiiveillä (Työkalut, Resurssit, Kehotteet) ja asiakasprimitiiiveillä (Näytteenotto, Elicitointi, Lokitus)

- **Kattavat MCP-viitteet ja resurssit**:
  - Lisätty **MCP for Beginners** -linkki (https://aka.ms/mcp-for-beginners)
  - Virallinen MCP-dokumentaatio ja määritykset (modelcontextprotocol.io)
  - Kehitysresurssit, mukaan lukien MCP Inspector ja viitetoteutukset
  - Teknisiä standardeja (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Lisätty - Module04 Qualcomm QNN Integraatio
- **Uusi osio 7: Qualcomm QNN Optimointipaketti** (`Module04/05.QualcommQNN.md`):
  - Kattava 400+ rivin opas Qualcommin yhtenäisestä AI-inferenssikehyksestä
  - Yksityiskohtainen käsittely heterogeenisestä laskennasta (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Laitteistotietoinen optimointi Snapdragon-alustoille älykkäällä työkuorman jakelulla
  - Edistyneet kvantisointitekniikat (INT8, INT16, sekatarkkuus) mobiilikäyttöön
  - Virtatehokas inferenssioptimointi akkukäyttöisille laitteille ja reaaliaikaisille sovelluksille
  - Täydellinen asennusopas QNN SDK:n asennukseen ja ympäristön konfigurointiin
  - Käytännön esimerkkejä: PyTorchista QNN-konversioon, monitaustajärjestelmän optimointiin, kontekstibinaarien luomiseen
  - Edistyneet käyttömallit: mukautettu taustajärjestelmän konfigurointi, dynaaminen kvantisointi, suorituskyvyn profilointi
  - Kattava vianetsintäosio ja yhteisöresurssit

- **Parannettu Module04-rakenne**:
  - Päivitetty README.md sisältämään 7 edistyvää osaa (oli 6)
  - Lisätty Qualcomm QNN suorituskykyvertailutaulukkoon (5-15x nopeuden parannus, 50-80% muistin vähennys)
  - Kattavat oppimistulokset mobiili-AI:n käyttöönottoon ja virtatehokkuuteen

### Muutettu - Module04 Dokumentaation Päivitykset
- **Microsoft Olive -dokumentaation parannus** (`Module04/03.MicrosoftOlive.md`):
  - Lisätty kattava "Olive Recipes Repository" -osio, joka kattaa yli 100 valmiiksi rakennettua optimointireseptiä
  - Yksityiskohtainen käsittely tuetuista malliperheistä (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Käytännön esimerkkejä reseptien mukauttamisesta ja yhteisön panoksista
  - Parannettu suorituskykyvertailuilla ja integraatio-ohjeilla

- **Osioiden uudelleenjärjestely Module04:ssa**:
  - Apple MLX siirretty osioon 5 (oli osio 6)
  - Työnkulun synteesi siirretty osioon 6 (oli osio 7)
  - Qualcomm QNN sijoitettu osioon 7 (erikoistunut mobiili/reunakeskeinen painotus)
  - Päivitetty kaikki tiedostoviittaukset ja navigointilinkit vastaavasti

### Korjattu - Työpajan Esimerkkien Validointi
- **chat_bootstrap.py validointi ja korjaus**:
  - Korjattu vioittunut import-lause (`util.util.workshop_utils` → `util.workshop_utils`)
  - Luotu puuttuva `__init__.py` util-pakettiin Python-moduulin oikeaan resoluutioon
  - Asennettu tarvittavat riippuvuudet (openai, foundry-local-sdk) conda-ympäristöön
  - Onnistuneesti validoitu esimerkin suoritus sekä oletus- että mukautetuilla kehotteilla
  - Vahvistettu integraatio Foundry Local -palvelun ja mallin latauksen kanssa (phi-4-mini CUDA-optimoinnilla)

### Dokumentaatio - Kattavat Oppaan Päivitykset
- **Module04 README.md täydellinen rakenneuudistus**:
  - Lisätty Qualcomm QNN merkittäväksi optimointikehykseksi OpenVINOn, Oliven ja MLX:n rinnalle
  - Päivitetty luvun oppimistulokset sisältämään mobiili-AI:n käyttöönotto ja virtatehokkuus
  - Parannettu suorituskykyvertailutaulukko QNN-metriikoilla ja mobiili/reunakäyttötapauksilla
  - Säilytetty looginen eteneminen yritysratkaisuista alustakohtaisiin optimointeihin

- **Ristiviittaukset ja navigointi**:
  - Päivitetty kaikki sisäiset linkit ja tiedostoviittaukset uuden osionumeroinnin mukaisesti
  - Parannettu työnkulun synteesin kuvaus sisältämään mobiili-, työpöytä- ja pilviympäristöt
  - Lisätty kattavat resurssilinkit Qualcommin kehittäjäekosysteemiin

## 2025-10-08

### Lisätty - Työpajan Kattava Päivitys
- **Työpajan README.md täydellinen uudelleenkirjoitus**:
  - Lisätty kattava johdanto, joka selittää Edge AI:n arvon (yksityisyys, suorituskyky, kustannukset)
  - Luotu 6 keskeistä oppimistavoitetta yksityiskohtaisilla osaamisalueilla
  - Lisätty oppimistulostaulukko toimituksilla ja osaamismatriisilla
  - Sisällytetty uravalmiita taitoja korostava osio teollisuuden merkityksestä
  - Lisätty pika-aloitusopas vaatimuksilla ja 3-vaiheisella asennuksella
  - Luotu resurssitaulukot Python-esimerkeille (8 tiedostoa suoritusajoilla)
  - Lisätty Jupyter-muistikirjojen taulukko (8 muistikirjaa vaikeusasteilla)
  - Luotu dokumentaatiotaulukko (7 keskeistä dokumenttia "Käytä kun" -ohjeilla)
  - Lisätty oppimispolun suositukset eri taitotasoille

- **Työpajan validointi- ja testausinfrastruktuuri**:
  - Luotu `scripts/validate_samples.py` - Kattava validointityökalu syntaksille, importille ja parhaalle käytännölle
  - Luotu `scripts/test_samples.py` - Smoke-testausohjelma kaikille Python-esimerkeille
  - Lisätty validointidokumentaatio `scripts/README.md`-tiedostoon

- **Kattava dokumentaatio**:
  - Luotu `SAMPLES_UPDATE_SUMMARY.md` - 400+ rivin yksityiskohtainen opas kaikista parannuksista
  - Luotu `UPDATE_COMPLETE.md` - Päivityksen valmistumisen tiivistelmä
  - Luotu `QUICK_REFERENCE.md` - Pikaopas Työpajalle

### Muutettu - Työpajan Python-esimerkkien Modernisointi
- **Kaikki 8 Python-esimerkkiä päivitetty parhailla käytännöillä**:
  - Parannettu virheenkäsittely try-except-lohkoilla kaikissa I/O-toiminnoissa
  - Lisätty tyyppivihjeet ja kattavat docstringit
  - Toteutettu johdonmukainen [INFO]/[ERROR]/[RESULT]-lokitusmalli
  - Suojattu valinnaiset importit asennusvinkeillä
  - Parannettu käyttäjäpalautetta kaikissa esimerkeissä

- **session01/chat_bootstrap.py**:
  - Parannettu asiakasaloitus kattavilla virheilmoituksilla
  - Parannettu suoratoiston virheenkäsittely chunk-validoinnilla
  - Lisätty parempi poikkeusten käsittely palvelun saatavuusongelmille

- **session02/rag_pipeline.py**:
  - Lisätty import-suojaukset sentence-transformersille asennusvinkeillä
  - Parannettu virheenkäsittely upotus- ja generointitoiminnoille
  - Parannettu tulostusmuotoilu rakenteellisilla tuloksilla

- **session02/rag_eval_ragas.py**:
  - Suojattu valinnaiset importit (ragas, datasets) käyttäjäystävällisillä virheilmoituksilla
  - Lisätty virheenkäsittely arviointimetrikoille
  - Parannettu tulostusmuotoilu arviointituloksille

- **session03/benchmark_oss_models.py**:
  - Toteutettu armollinen heikentyminen (jatkuu mallivirheiden kohdalla)
  - Lisätty yksityiskohtainen etenemisen raportointi ja mallikohtainen virheenkäsittely
  - Parannettu tilastojen laskenta kattavalla virheiden palautuksella

- **session04/model_compare.py**:
  - Lisätty tyyppivihjeet (Tuple-palautustyypit)
  - Parannettu tulostusmuotoilu rakenteellisilla JSON-tuloksilla
  - Toteutettu mallikohtainen virheenkäsittely palautuksella

- **session05/agents_orchestrator.py**:
  - Parannettu Agent.act() kattavilla docstringeillä
  - Lisätty putkiston virheenkäsittely vaiheittaisella lokituksella
  - Parannettu muistinhallinta ja tilan seuranta

- **session06/models_router.py**:
  - Parannettu funktiodokumentaatio kaikille reitityskomponenteille
  - Lisätty yksityiskohtainen lokitus route()-funktioon
  - Parannettu testitulokset rakenteellisilla tuloksilla

- **session06/models_pipeline.py**:
  - Lisätty virheenkäsittely chat()-apuohjelmaan
  - Parannettu pipeline()-funktio vaiheittaisella lokituksella ja etenemisen raportoinnilla
  - Parannettu main()-funktio kattavalla virheiden palautuksella

### Dokumentaatio - Työpajan Dokumentaation Parannus
- Päivitetty pää README.md Työpaja-osio korostaen käytännön oppimispolkua
- Parannettu STUDY_GUIDE.md kattavalla Työpaja-osiolla, mukaan lukien:
  - Oppimistavoitteet ja opiskelualueet
  - Itsearviointikysymykset
  - Käytännön harjoitukset aikatauluarvioilla
  - Ajan jakaminen keskittyneelle ja osa-aikaiselle opiskelulle
  - Lisätty Työpaja edistymisen seurantamalliin
- Päivitetty ajan jakamisen opas 20 tunnista 30 tuntiin (sisältäen Työpajan)
- Lisätty Työpajan esimerkkien kuvaukset ja oppimistulokset README-tiedostoon

### Korjattu
- Ratkaistu epäjohdonmukaiset virheenkäsittelymallit Työpajan esimerkeissä
- Korjattu valinnaisten riippuvuuksien import-virheet asianmukaisilla suojauksilla
- Korjattu puuttuvat tyyppivihjeet kriittisissä funktioissa
- Korjattu riittämätön käyttäjäpalaute virhetilanteissa
- Korjattu validointiongelmat kattavalla testausinfrastruktuurilla

---

## 2025-09-23

### Muutettu - Merkittävä Module 08 Modernisointi
- **Kattava yhdenmukaistaminen Microsoft Foundry-Local -repository-mallien kanssa**
  - Päivitetty kaikki koodiesimerkit käyttämään moderneja `FoundryLocalManager`- ja OpenAI SDK -integraatioita
  - Korvattu vanhentuneet manuaaliset `requests`-kutsut asianmukaisella SDK-käytöllä
  - Yhdenmukaistettu toteutusmallit virallisen Microsoft-dokumentaation ja esimerkkien kanssa

- **05.AIPoweredAgents.md modernis
  - Suoritettavat esimerkit `Module08/samples/01`–`06` kansiossa Windows cmd-ohjeilla
    - `01` REST-pikakeskustelu (`chat_quickstart.py`)
    - `02` SDK-pikakäynnistys OpenAI/Foundry Local ja Azure OpenAI -tuki (`sdk_quickstart.py`)
    - `03` CLI listaus ja vertailu (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Moni-agenttien orkestrointi (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools-reititin (`router.py`)
- Azure OpenAI -tuki Session 2 SDK-esimerkissä ympäristömuuttujien konfiguroinnilla
- `.vscode/settings.json` osoittamaan `Module08/.venv`-kansioon ja parantamaan Python-analyysin tarkkuutta
- `.env` tiedosto, jossa `PYTHONPATH`-vihje VS Code/Pylance-tietoisuutta varten

### Muutettu
- Oletusmalli päivitetty `phi-4-mini`:ksi kaikissa Module 08 -dokumenteissa ja esimerkeissä; jäljellä olevat `phi-3.5`-maininnat poistettu Module 08:ssa
- Reitittimen (`Module08/samples/06/router.py`) parannukset:
  - Päätepisteiden haku `foundry service status` regex-analyysillä
  - `/v1/models`-terveystarkistus käynnistyksessä
  - Ympäristömuuttujilla konfiguroitava mallirekisteri (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vaatimukset päivitetty: `Module08/requirements.txt` sisältää nyt `openai` (yhdessä `requests` ja `chainlit` kanssa)
- Chainlit-esimerkin ohjeistus selkeytetty ja vianetsintä lisätty; tuontien ratkaisu työtilan asetuksilla

### Korjattu
- Tuontiongelmat ratkaistu:
  - Reititin ei enää riipu olemattomasta `utils`-moduulista; funktiot sisällytetty
  - Koordinaattori käyttää suhteellista tuontia (`from .specialists import ...`) ja käynnistetään moduulipolun kautta
  - VS Code/Pylance-konfiguraatio ratkaisee `chainlit`- ja pakettituonnit
- Pieni kirjoitusvirhe korjattu `STUDY_GUIDE.md`-tiedostossa ja lisätty Module 08:n kattavuus

### Poistettu
- Poistettu käyttämätön `Module08/infra/obs.py` ja tyhjä `infra/`-hakemisto; havainnointimallit säilytetty valinnaisina dokumenteissa

### Siirretty
- Module 08 -demot yhdistetty `Module08/samples`-kansioon sessionumeroiduilla kansioilla
  - Chainlit-sovellus siirretty `samples/04`-kansioon
  - Agentit siirretty `samples/05`-kansioon ja lisätty `__init__.py`-tiedostot pakettiratkaisua varten

### Dokumentaatio
- Module 08 -session dokumentaatio ja kaikki esimerkkien README-tiedostot täydennetty Microsoft Learn- ja luotettavien toimittajien viitteillä
- `Module08/README.md` päivitetty sisältämään esimerkkien yleiskatsauksen, reitittimen konfiguraation ja validointivinkit
- `Module07/README.md` Windows Foundry Local -osio validoitu Learn-dokumenttien perusteella
- `STUDY_GUIDE.md` päivitetty:
  - Lisätty Module 08 yleiskatsaukseen, aikatauluihin ja etenemisen seurantaan
  - Lisätty kattava Viitteet-osio (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historia (yhteenveto)
- Kurssin rakenne ja moduulit luotu (Moduulit 01–07)
- Iteratiivinen sisällön modernisointi, muotoilustandardien yhtenäistäminen ja lisätty tapaustutkimuksia
- Laajennettu optimointikehysten kattavuus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Julkaisematon / Jatkolista (ehdotukset)
- Valinnaiset per-esimerkki savutestit Foundry Local -saatavuuden validointiin
- Käännösten tarkistus malliviittausten yhdenmukaistamiseksi (esim. `phi-4-mini`)
- Lisää minimaalinen pyright-konfiguraatio, jos tiimit suosivat työtilan laajuista tiukkuutta

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.