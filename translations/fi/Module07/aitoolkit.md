# AI Toolkit Visual Studio Codeen – Edge AI -kehitysohje

## Johdanto

Tervetuloa kattavaan oppaaseen AI Toolkitin käytöstä Visual Studio Codessa Edge AI -kehityksessä. Kun tekoäly siirtyy keskitetystä pilvilaskennasta hajautettuihin reuna­laitteisiin, kehittäjät tarvitsevat tehokkaita, integroituja työkaluja, jotka pystyvät käsittelemään reunaympäristön ainutlaatuiset haasteet – resurssirajoituksista offline-toimintavaatimuksiin.

AI Toolkit Visual Studio Codelle sulkee tämän kuilun tarjoamalla täydellisen kehitysympäristön, joka on suunniteltu erityisesti AI-sovellusten rakentamiseen, testaamiseen ja optimointiin tehokkaasti reunalaitteilla. Kehititpä sitten IoT-antureille, mobiililaitteille, sulautetuille järjestelmille tai reunapalvelimille, tämä työkalu virtaviivaistaa koko kehitysprosessiasi tutussa VS Code -ympäristössä.

Tämä opas vie sinut läpi keskeiset käsitteet, työkalut ja parhaat käytännöt AI Toolkitin hyödyntämiseksi Edge AI -projekteissasi, alkaen mallin valinnasta tuotantoon siirtoon.

## Yleiskatsaus

AI Toolkit Visual Studio Codelle on tehokas laajennus, joka nopeuttaa agenttien kehitystä ja tekoälysovellusten luomista. Työkalu tarjoaa laajat ominaisuudet AI-mallien tutkimiseen, arviointiin ja käyttöönottoon monilta toimittajilta — mukaan lukien Anthropic, OpenAI, GitHub, Google — samalla tukien paikallista mallien suorittamista ONNX:llä ja Ollamalla.

Mikä erottaa AI Toolkitin on sen kokonaisvaltainen lähestymistapa AI-kehityksen koko elinkaareen. Toisin kuin perinteiset AI-työkalut, jotka keskittyvät yksittäisiin osa-alueisiin, AI Toolkit tarjoaa integroidun ympäristön, joka kattaa mallien löytämisen, kokeilun, agenttien kehityksen, arvioinnin ja käyttöönoton — kaikki tutussa VS Code -ympäristössä.

Alusta on suunniteltu erityisesti nopeaan prototyyppien tekoon ja tuotantoon siirtoon, sisältäen ominaisuuksia kuten kehotteiden generoinnin, pika-aloitukset, saumattomat MCP-työkalujen integraatiot ja laajat arviointimahdollisuudet. Edge AI -kehityksessä tämä tarkoittaa, että voit tehokkaasti kehittää, testata ja optimoida AI-sovelluksia reunaympäristöihin pitäen koko kehityksen työnkulun VS Codessa.

## Oppimistavoitteet

Oppaan lopussa osaat:

### Perustaidot
- **Asentaa ja konfiguroida** AI Toolkittiä Visual Studio Codeen Edge AI -kehitystyönkulkuja varten
- **Navigoida ja käyttää** AI Toolkit -käyttöliittymää, mukaan lukien malliluettelo, leikkikenttä ja agenttirakentaja
- **Valita ja arvioida** reunaympäristöihin soveltuvia AI-malleja suorituskyvyn ja resurssirajoitusten perusteella
- **Muuntaa ja optimoi** malleja ONNX-muotoon ja kvantisointitekniikoilla reunalaitteille

### Edge AI -kehitystaidot
- **Suunnitella ja toteuttaa** Edge AI -sovelluksia integroidussa kehitysympäristössä
- **Suorittaa mallien testaus** reunamaisissa olosuhteissa paikallisen inferenssin ja resurssien monitoroinnin avulla
- **Luoda ja muokata** AI-agentteja, jotka on optimoitu reunaympäristöihin
- **Arvioida mallien suorituskykyä** reunalaskennan mittareilla (latenssi, muistin käyttö, tarkkuus)

### Optimointi ja käyttöönotto
- **Soveltaa kvantisointi- ja karsintatekniikoita** vähentämään mallien kokoa säilyttäen hyväksyttävä suorituskyky
- **Optimoida malleja** tiettyjä reunalaitteiden alustoja, kuten CPU:tä, GPU:ta ja NPU:ta varten
- **Toteuttaa parhaat käytännöt** reunatekoälyn kehityksessä, mukaan lukien resurssien hallinta ja varastrategiat
- **Valmistella mallit ja sovellukset** tuotantokäyttöönottoa varten reunalaitteilla

### Edistyneet Edge AI -käsitteet
- **Integroida reunatekoälykehyksiin** kuten ONNX Runtime, Windows ML ja TensorFlow Lite
- **Toteuttaa monimalliset arkkitehtuurit** ja liitetyn oppimisen skenaariot reunaympäristöissä
- **Ratkoa yleisiä reunatekoälyyn liittyviä ongelmia** kuten muistin rajoitukset, inferenssin nopeus ja laitteistoyhteensopivuus
- **Suunnitella seurantaja lokitusstrategioita** reunatekoälysovelluksille tuotannossa

### Käytännön sovellukset
- **Rakentaa end-to-end Edge AI -ratkaisuja** mallin valinnasta aina käyttöönottoon asti
- **Osoittaa osaamista** reunakehityksen työnkuluissa ja optimointitekniikoissa
- **Soveltaa opittuja käsitteitä** todellisiin reunatekoälykäyttöihin, kuten IoT, mobiili ja sulautetut sovellukset
- **Arvioida ja verrata** eri reunatekoälykäyttöönottojen strategioita ja niiden kompromisseja

## Keskeiset ominaisuudet Edge AI -kehitykseen

### 1. Malliluettelo ja etsintä
- **Monitoimittajatuki**: Selaa ja käytä AI-malleja Anthropicilta, OpenAI:lta, GitHubilta, Googlelta ja muilta toimittajilta
- **Paikallinen mallien integrointi**: Yksinkertaistettu ONNX- ja Ollama-mallien etsintä reunakäyttöön
- **GitHub-mallit**: Suora integraatio GitHubin mallien hostingiin sujuvaa käyttöä varten
- **Mallien vertailu**: Vertaa malleja rinnakkain löytääksesi optimaalisen tasapainon reunalaitteen rajoitusten kanssa

### 2. Interaktiivinen leikkikenttä
- **Vuorovaikutteinen testausympäristö**: Nopeita kokeiluja mallien ominaisuuksilla kontrolloidussa ympäristössä
- **Monimodaalituki**: Testaa kuvia, tekstiä ja muita reunaympäristössä tyypillisiä syötteitä
- **Reaaliaikaiset kokeilut**: Välitön palaute mallin vastauksista ja suorituskyvystä
- **Parametrien optimointi**: Hienosäädä mallin parametreja reunakäyttövaatimuksiin

### 3. Kehote (Agent) rakentaja
- **Luonnollisen kielen generointi**: Luo aloituskehotteita luonnollisilla kielenkuvauksilla
- **Iteratiivinen parantaminen**: Kehitä kehotteita mallin vastausten ja suorituskyvyn perusteella
- **Tehtävien pilkkominen**: Jaa monimutkaiset tehtävät kehotteiden ketjuttamisella ja rakenteellisilla tuloksilla
- **Muuttujien tuki**: Käytä muuttujia kehotteissa dynaamiselle agentin käyttäytymiselle
- **Tuotantokoodin generointi**: Luo tuotantovalmiita koodeja nopeaan sovelluskehitykseen

### 4. Eräajo ja arviointi
- **Monimallinen testaus**: Suorita useita kehotteita samanaikaisesti valituissa malleissa
- **Tehokas testaus laajasti**: Testaa erilaisia syötteitä ja kokoonpanoja tehokkaasti
- **Mukautetut testitapaukset**: Suorita agenteilla testitapauksia toiminnallisuuden varmistamiseksi
- **Suorituskyvyn vertailu**: Vertaa tuloksia eri mallien ja kokoonpanojen välillä

### 5. Mallin arviointi dataseteillä
- **Vakio­mittarit**: Testaa AI-malleja sisäänrakennetuilla arvioijilla (F1-pisteet, merkityksellisyys, samankaltaisuus, johdonmukaisuus)
- **Mukautetut arvioijat**: Luo omia arviointimittareita erityisiä käyttötapauksia varten
- **Datasetin integrointi**: Testaa malleja kattavia datasettejä vastaan
- **Suorituskyvyn mittaus**: Kvantifioi mallin suorituskyky reunakäyttöönottoa varten

### 6. Hienosäätömahdollisuudet
- **Mallien räätälöinti**: Mukauta malleja erityisiin käyttötarkoituksiin ja toimialoihin
- **Erikoistunut sovitus**: Sopeuta malleja erikoistuneisiin toimialoihin ja vaatimuksiin
- **Reunaoptimointi**: Hienosäädä malleja erityisesti reunaympäristön rajoituksiin
- **Toimialakohtainen koulutus**: Luo malleja, jotka on räätälöity tiettyihin reunakäyttöihin

### 7. MCP-työkalujen integraatio
- **Ulkopuolisten työkalujen liittäminen**: Yhdistä agentit ulkoisiin työkaluihin Model Context Protocol -palvelimien kautta
- **Todelliset toiminnot**: Mahdollista agenttien kyselyt tietokantoihin, API-pääsy tai mukautetun logiikan ajaminen
- **Olemassa olevat MCP-palvelimet**: Käytä työkaluja komentoprotokollista (stdio) tai HTTP (server-sent event) -protokollista
- **Mukautettu MCP-kehitys**: Rakenna ja luo uusia MCP-palvelimia testauksella Agent Builderissa

### 8. Agenttien kehitys ja testaus
- **Funktiokutsujen tuki**: Mahdollista agenttien dynaaminen ulkoisten funktioiden kutsuminen
- **Reaaliaikaiset integraatiotestit**: Testaa integraatioita reaaliaikaisilla suorityksillä ja työkalujen käytöllä
- **Agenttien versiointi**: Versiohallinta agenteille ja vertailuominaisuudet arviointituloksiin
- **Virheenkorjaus ja jäljitys**: Paikalliset jäljitys- ja virheenkorjausmahdollisuudet agentin kehitykseen

## Edge AI -kehityksen työnkulku

### Vaihe 1: Mallien etsintä ja valinta
1. **Tutki malliluetteloa**: Käytä malliluetteloa löytääksesi reunakäyttöön soveltuvat mallit
2. **Vertaa suorituskykyä**: Arvioi malleja koon, tarkkuuden ja inferenssin nopeuden perusteella
3. **Testaa paikallisesti**: Käytä Ollama- tai ONNX-malleja paikalliseen testaukseen ennen reunakäyttöä
4. **Arvioi resurssivaatimukset**: Määrittele muisti- ja laskentatarpeet kohde-reunalaitteille

### Vaihe 2: Mallien optimointi
1. **Muunna ONNX-muotoon**: Muunna valitut mallit ONNX-muotoon reunayhteensopivuutta varten
2. **Sovella kvantisointi**: Vähennä mallin kokoa INT8- tai INT4-kvantisoinnilla
3. **Laitteisto-optimointi**: Optimoi kohde-reunalaitteiston (ARM, x86, erikoiskiihdyttimet) mukaisesti
4. **Suorituskyvyn validointi**: Varmista optimoitujen mallien säilyvän hyväksyttävä tarkkuus

### Vaihe 3: Sovelluskehitys
1. **Agenttien suunnittelu**: Käytä Agent Builderia luodaksesi reunalle optimoituja AI-agentteja
2. **Kehotelman suunnittelu**: Kehitä kehotteita, jotka toimivat hyvin pienempien reunamallien kanssa
3. **Integraatiotestaus**: Testaa agenteja simuloiduissa reunaympäristöissä
4. **Koodin generointi**: Luo tuotantokoodi, joka on optimoitu reunakäyttöön

### Vaihe 4: Arviointi ja testaus
1. **Eräarviointi**: Testaa useita kokoonpanoja optimaalisten reunasetusten löytämiseksi
2. **Suorituskyvyn profilointi**: Analysoi inferenssin nopeus, muistin käyttö ja tarkkuus
3. **Reunasimulaatio**: Testaa olosuhteissa, jotka vastaavat kohdereunan ympäristöä
4. **Kuormitustestaus**: Arvioi suorituskykyä erilaisissa kuormitustilanteissa

### Vaihe 5: Käyttöönoton valmistelu
1. **Loppuoptimointi**: Käytä lopulliset optimoinnit testitulosten perusteella
2. **Pakkaa käyttöönottoa varten**: Pakkkaa mallit ja koodi reunakäyttöönottoa varten
3. **Dokumentointi**: Dokumentoi käyttöönoton vaatimukset ja asetukset
4. **Seurannan valmistelu**: Valmistele seuranta ja lokitus reunakäyttöä varten

## Kohdeyleisö Edge AI -kehitykselle

### Reuna AI -kehittäjät
- Sovelluskehittäjät, jotka rakentavat tekoälyllä varustettuja reunalaitteita ja IoT-ratkaisuja
- Sulautettujen järjestelmien kehittäjät, jotka integroivat tekoälyominaisuuksia resurssirajoitteisiin laitteisiin
- Mobiilikehittäjät, jotka luovat laitekohtaisia AI-sovelluksia älypuhelimille ja tableteille

### Reuna AI -insinöörit
- AI-insinöörit, jotka optimoivat malleja reunaympäristöihin ja hallinnoivat inferenssiputkia
- DevOps-insinöörit, jotka käyttöönottoivat ja hallinnoivat AI-malleja hajautetussa reunainfrastruktuurissa
- Suorituskyky-insinöörit, jotka optimoivat tekoälyn kuormia reunalaitteiden rajoituksiin

### Tutkijat ja opettajat
- AI-tutkijat, jotka kehittävät tehokkaita malleja ja algoritmeja reunalaskentaan
- Opettajat, jotka opettavat Edge AI -käsitteitä ja demonstroivat optimointitekniikoita
- Opiskelijat, jotka oppivat reunatekoälyn käyttöönoton haasteista ja ratkaisuista

## Edge AI -käyttötapaukset

### Älykkäät IoT-laitteet
- **Reaaliaikainen kuvatunnistus**: Ota käyttöön konenäkömalleja IoT-kameroissa ja antureissa
- **Puheenkäsittely**: Toteuta puheentunnistus ja luonnollisen kielen käsittely älykaiuttimissa
- **Ennakoiva kunnossapito**: Aja poikkeamien havaitsemisen malleja teollisilla reunalaitteilla
- **Ympäristön seuranta**: Ota käyttöön sensordatan analysointimalleja ympäristö­sovelluksiin

### Mobiili- ja sulautetut sovellukset
- **Laitteella tapahtuva kääntäminen**: Toteuta kielimallinnoksia offline-käyttöön
- **Lisätty todellisuus**: Käytä reaaliaikaista objektintunnistusta ja seurantaa AR-sovelluksissa
- **Terveysseuranta**: Aja terveysanalyysimalleja kannettavilla laitteilla ja lääketieteellisillä välineillä
- **Autonomiset järjestelmät**: Toteuta päätöksentekomalleja droneille, robo­teille ja ajoneuvoille

### Reunalaskenta-infrastruktuuri
- **Reunalaskentakeskukset**: Käytä AI-malleja reunatietokeskuksissa matalan latenssin sovelluksiin
- **CDN-integraatio**: Integroi AI-prosessointiominaisuudet sisällönjakeluverkostoihin
- **5G Edge**: Hyödynnä 5G-reunalaskentaa tekoälyllä tehostetuille sovelluksille
- **Sumulaskenta**: Toteuta AI-prosessointia sumulaskenta-ympäristöissä

## Asennus ja käyttöönotto

### Laajennuksen asennus
Asenna AI Toolkit -laajennus suoraan Visual Studio Code Marketplacesta:

**Laajennuksen tunniste**: `ms-windows-ai-studio.windows-ai-studio`

**Asennustavat**:
1. **VS Code Marketplace**: Etsi "AI Toolkit" Laajennukset-näkymästä
2. **Komentoriviltä**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Suora asennus**: Lataa [VS Code Marketplacesta](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Edge AI -kehityksen vaatimukset
- **Visual Studio Code**: Suositellaan uusinta versiota
- **Python-ympäristö**: Python 3.8+ tarvittavine AI-kirjastoineen
- **ONNX Runtime** (valinnainen): ONNX-mallien inferenssiin
- **Ollama** (valinnainen): Paikalliseen mallipalveluun
- **Laitteistokiihdytys­työkalut**: CUDA, OpenVINO tai alustakohtaiset kiihdyttimet

### Ensimmäisen käyttöönoton konfigurointi
1. **Laajennuksen aktivointi**: Avaa VS Code ja varmista että AI Toolkit näkyy Aktiviteettipalkissa
2. **Mallitoimittajien asetukset**: Määritä pääsy GitHubiin, OpenAI:hin, Anthropiciin tai muihin mallitoimittajiin
3. **Paikallinen ympäristö**: Aseta Python-ympäristö ja asenna vaaditut paketit
4. **Laitteistokiihdytys**: Konfiguroi GPU/NPU-kiihdytys, jos saatavilla
5. **MCP-integraatio**: Määritä Model Context Protocol -palvelimet tarvittaessa

### Ensiasetusten tarkistuslista
- [ ] AI Toolkit -laajennus asennettu ja aktivoitu
- [ ] Malliluettelo on käytettävissä ja mallit löydettävissä
- [ ] Leikkikenttä toimii mallien testaamiseen
- [ ] Agent Builder on käytettävissä kehoteiden kehitykseen
- [ ] Paikallinen kehitysympäristö konfiguroitu
- [ ] Laitteistokiihdytys (jos saatavilla) on asianmukaisesti konfiguroitu

## Aloittaminen AI Toolkitin kanssa

### Pikaohje

Suosittelemme aloittamaan GitHubin isännöimillä malleilla sujuvinta käyttökokemusta varten:

1. **Asennus**: Seuraa [asennusopasta](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) AI Toolkitin käyttöönottoon laitteellasi
2. **Mallin etsintä**: Laajennuksen puunäkymästä valitse **CATALOG > Models** tutkiaksesi saatavilla olevia malleja
3. **GitHub-mallit**: Aloita GitHubin isännöimistä malleista optimaalisen integraation takia
4. **Leikkikentän testaus**: Valitse mistä tahansa mallikortista **Try in Playground** aloittaaksesi kokeilun mallin ominaisuuksilla

### Vaiheittainen Edge AI -kehitys

#### Vaihe 1: Mallien tutkiminen ja valinta
1. Avaa AI Toolkit -näkymä VS Coden Aktiviteettipalkista
2. Selaa malliluetteloa reunakäyttöön sopivien mallien löytämiseksi
3. Suodata toimittajan mukaan (GitHub, ONNX, Ollama) reuna-vaatimusten mukaan
4. Käytä **Try in Playground** -toimintoa mallin ominaisuuksien välittömään testaamiseen

#### Vaihe 2: Agenttien kehitys
1. Käytä **Prompt (Agent) Builderia** luodaksesi reunalle optimoituja AI-agentteja
2. Generoi aloituskehotteita luonnollisten kielikuvauksien avulla
3. Iteroi ja hienosäädä kehotteita mallin vastausten pohjalta
4. Integroi MCP-työkaluja agenttien toiminnallisuuden laajentamiseksi


#### Vaihe 3: Testaus ja arviointi
1. Käytä **Bulk Run** -toimintoa testataksesi useita kehotteita valituissa malleissa
2. Suorita agentteja testitapauksilla toiminnallisuuden varmistamiseksi
3. Arvioi tarkkuutta ja suorituskykyä sisäänrakennettujen tai mukautettujen mittareiden avulla
4. Vertaa eri malleja ja kokoonpanoja

#### Vaihe 4: Hienosäätö ja optimointi
1. Mukauta malleja erityisiin reunalaitetapauksiin
2. Käytä alakohtaista hienosäätöä
3. Optimoi reunalaitteiden käyttöönoton rajoitukset huomioiden
4. Versioi ja vertaile eri agenttikokoonpanoja

#### Vaihe 5: Käyttöön valmistautuminen
1. Generoi tuotantokelpoinen koodi Agent Builderin avulla
2. Määritä MCP-palvelinyhteydet tuotantokäyttöä varten
3. Valmistele käyttöönotto-paketit reunalaitteille
4. Konfiguroi valvonta- ja arviointimittarit

## Näytteitä AI Toolkitista

Kokeile näytteitämme
[AI Toolkit -näytteet](https://github.com/Azure-Samples/AI_Toolkit_Samples) on suunniteltu auttamaan kehittäjiä ja tutkijoita tutustumaan ja toteuttamaan tekoälyratkaisuja tehokkaasti.

Näytteemme sisältävät:

Näytekoodi: Esirakennetut esimerkit AI-toiminnallisuuksien, kuten mallien koulutuksen, käyttöönoton tai sovelluksiin integroinnin, havainnollistamiseksi.
Dokumentaatio: Oppaat ja tutoriaalit auttamaan käyttäjiä ymmärtämään AI Toolkitin ominaisuuksia ja niiden käyttöä.
Esivaatimukset

- Visual Studio Code
- AI Toolkit Visual Studio Codeen
- GitHubin hienojakoinen henkilökohtainen käyttöoikeustunnus (PAT)
- Foundry Local

## Parhaat käytännöt reunatiedon tekoälyn kehitykseen

### Mallin valinta
- **Koko-rajoitukset**: Valitse malleja, jotka mahtuvat kohdelaitteen muistirajoituksiin
- **Päätelmän nopeus**: Priorisoi malleja, joiden päätösajan on nopea reaaliaikaiseen käyttöön
- **Tarkkuuden kompromissit**: Tasapainota mallin tarkkuus ja resurssirajoitukset
- **Yhteensopivuusformaatti**: Suosi ONNX- tai laitteistoon optimoituja formaatteja reunakäyttöön

### Optimointitekniikat
- **Kvantisointi**: Käytä INT8- tai INT4-kvantisointia mallikoon pienentämiseksi ja nopeuden parantamiseksi
- **Karsinta**: Poista tarpeettomat malliparametrit laskentavaatimusten vähentämiseksi
- **Tietämyksen tiivistäminen**: Luo pienempiä malleja, jotka säilyttävät suurten mallien suorituskyvyn
- **Laitteistokiihdytys**: Hyödynnä tarvittaessa NPU-, GPU- tai erikoiskiihdyttimiä

### Kehitystyönkulku
- **Iteratiivinen testaus**: Testaa usein reunamaista ympäristöä vastaavissa oloissa kehityksen aikana
- **Suorituskyvyn seuranta**: Seuraa jatkuvasti resurssien käyttöä ja päätöksen nopeutta
- **Versiohallinta**: Seuraa malliversioita ja optimointiasetuksia
- **Dokumentaatio**: Dokumentoi kaikki optimointipäätökset ja suorituskyvyn kompromissit

### Käyttöönottoa koskevat seikat
- **Resurssien seuranta**: Seuraa muistia, suorittimen käyttöä ja virrankulutusta tuotannossa
- **Varajärjestelmät**: Toteuta varajärjestelmät mallin virhetilanteita varten
- **Päivitysmenetelmät**: Suunnittele mallipäivitykset ja versiohallinta
- **Tietoturva**: Toteuta asianmukaiset tietoturvatoimet reunatiedon tekoälysovelluksissa

## Integraatio reunatiedon tekoälykehyksiin

### ONNX Runtime
- **Monialustainen käyttöönotto**: Ota ONNX-mallit käyttöön eri reunalaitteissa
- **Laitteisto-optimointi**: Hyödynnä ONNX Runtimen laittelaitteistokohtaiset optimoinnit
- **Mobiilituki**: Käytä ONNX Runtime Mobilea älypuhelimissa ja tableteissa
- **IoT-integraatio**: Ota käyttöön IoT-laitteissa ONNX Runtimen kevyiden jakeluiden avulla

### Windows ML
- **Windows-laitteet**: Optimoi Windows-pohjaisille reunalaitteille ja tietokoneille
- **NPU-kiihdytys**: Hyödynnä neuroverkon prosessointiyksiköitä Windows-laitteissa
- **DirectML**: Käytä DirectML:ää GPU-kiihdytykseen Windows-alustoilla
- **UWP-integraatio**: Integroi Universal Windows Platform -sovelluksiin

### TensorFlow Lite
- **Mobiilioptimointi**: Ota TensorFlow Lite -mallit käyttöön mobiili- ja sulautetuissa laitteissa
- **Laitteistodelegaattorit**: Käytä erityisiä laitteistodelegaattoreita kiihdytykseen
- **Mikrokontrollerit**: Käytä TensorFlow Lite Micron avulla mikrokontrollereissa
- **Monialustatuki**: Toteuta Android-, iOS-, ja sulautetut Linux-järjestelmissä

### Azure IoT Edge
- **Pilvi-reuna hybridi**: Yhdistä pilvikoulutus ja reunapäätelmä
- **Moduulien käyttöönotto**: Ota AI-mallit käyttöön IoT Edge -moduuleina
- **Laitteiden hallinta**: Hallinnoi reunalaitteita ja mallipäivityksiä etänä
- **Telemetria**: Kerää suorituskykytietoja ja mallimittareita reunakäytöstä

## Edistyneet reunatiedon tekoälytapahtumat

### Monimallinen käyttöönotto
- **Mallien yhdistelmät**: Ota useita malleja käyttöön tarkkuuden tai varmuuden lisäämiseksi
- **A/B-testit**: Testaa eri malleja samanaikaisesti reunalaitteilla
- **Dynaaminen valinta**: Valitse mallit laitteen tämänhetkisten olosuhteiden mukaan
- **Resurssien jakaminen**: Optimoi resurssien käyttö monien mallien kesken

### Hajautettu oppiminen
- **Jakautunut koulutus**: Kouluta malleja useilla reunalaitteilla
- **Yksityisyyden suoja**: Säilytä koulutusdata laitteessa ja jaa vain malliparannukset
- **Yhteistyöoppiminen**: Mahdollista laitteiden oppiminen yhteisistä kokemuksista
- **Reuna-pilvi koordinointi**: Koordinoi oppimista reunalaitteiden ja pilvi-infrastruktuurin välillä

### Reaaliaikainen käsittely
- **Virtauskäsittely**: Käsittele jatkuvia datavirtoja reunalaitteissa
- **Matala viive**: Optimoi päätökset minimaalisella latenssilla
- **Eräkäsittely**: Käsittele dataerät tehokkaasti reunalaitteissa
- **Soveltuva käsittely**: Säädä käsittelyä laitteen kapasiteetin mukaan

## Reunatiedon tekoälyn vianetsintä

### Yleisiä ongelmia
- **Muistirajoitukset**: Malli liian suuri kohdelaitteen muistiin
- **Päätöksen nopeus**: Mallin päätöksenteko liian hidas reaaliaikavaatimuksiin
- **Tarkkuuden heikkeneminen**: Optimointi heikentää mallin tarkkuutta liikaa
- **Laitteistoyhteensopivuus**: Malli ei ole yhteensopiva kohdelaitteiston kanssa

### Virheenkorjausstrategiat
- **Suorituskyvyn profilointi**: Käytä AI Toolkitin jäljitysominaisuuksia pullonkaulojen tunnistamiseen
- **Resurssien seuranta**: Seuraa muistia ja prosessorin käyttöä kehityksen aikana
- **Inkrementaalinen testaus**: Testaa optimointeja vaiheittain ongelmien eristämiseksi
- **Laitteistosimulaatio**: Käytä kehitystyökaluja kohdelaitteiston simuloimiseen

### Optimointiratkaisut
- **Lisäkvantisointi**: Käytä aggressiivisempia kvantisointitekniikoita
- **Mallin arkkitehtuuri**: Harkitse erilaisia reunalle optimoituja arkkitehtuureja
- **Esikäsittelyn optimointi**: Optimoi datan esikäsittely reunavaatimusten mukaan
- **Päätösoptimointi**: Käytä laitteistokohtaisia päätösoptimointeja

## Resurssit ja seuraavat askeleet

### Virallinen dokumentaatio
- [AI Toolkitin kehittäjädokumentaatio](https://aka.ms/AIToolkit/doc)
- [Asennus- ja käyttöönotto-opas](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Intelligent Apps -dokumentaatio](https://code.visualstudio.com/docs/intelligentapps)
- [Model Context Protocol (MCP) -dokumentaatio](https://modelcontextprotocol.io/)

### Yhteisö ja tuki
- [AI Toolkitin GitHub-repositorio](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub-ongelmat ja ominaisuuspyynnöt](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord -yhteisö](https://aka.ms/azureaifoundry/discord)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Teknisiä resursseja
- [ONNX Runtimen dokumentaatio](https://onnxruntime.ai/)
- [Ollaman dokumentaatio](https://ollama.ai/)
- [Windows ML -dokumentaatio](https://docs.microsoft.com/en-us/windows/ai/)
- [Azure AI Foundryn dokumentaatio](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Oppimispolut
- [Edge AI Fundamentals Course](../Module01/README.md)
- [Pienten kielimallien opas](../Module02/README.md)
- [Reuna-järjestelmien käyttöönotto](../Module03/README.md)
- [Windows Edge AI:n kehitys](./windowdeveloper.md)

### Lisäresurssit
- **Repositoriostatistiikka**: 1,8k+ tähteä, 150+ haarukkaa, 18+ kontribuuttoria
- **Lisenssi**: MIT-lisenssi
- **Tietoturva**: Microsoftin tietoturvakäytännöt voimassa
- **Telemetria**: Kunnioittaa VS Coden telemetriasääntöjä

## Yhteenveto

AI Toolkit Visual Studio Codelle edustaa kattavaa alustaa nykyaikaiseen tekoälyn kehitykseen tarjoten sujuvia agenttien kehitysominaisuuksia, jotka ovat erityisen hyödyllisiä reunatiedon tekoälysovelluksissa. Laaja mallivalikoima, joka tukee tarjoajia kuten Anthropic, OpenAI, GitHub ja Google, yhdistettynä paikalliseen suoritukseen ONNX:llä ja Ollamalla, antaa joustavuutta erilaisiin reunalaitteiden käyttötapauksiin.

Työkalupaketin vahvuus on sen integroidussa lähestymistavassa — mallien löytämisestä ja kokeilusta Playgroundissa kehittyneeseen agenttien kehitykseen Prompt Builderin kanssa, kokonaisvaltaisiin arviointimahdollisuuksiin ja saumattomaan MCP-työkalujen integraatioon. Reunatiedon tekoälyn kehittäjille tämä tarkoittaa nopeaa prototypointia ja agenttien testausta ennen reunakäyttöön vientiä, kykyä nopeaan iterointiin ja optimointiin resurssirajoitteisissa ympäristöissä.

Keskeisiä etuja reunatiedon tekoälyn kehityksessä ovat:
- **Nopea kokeilu**: Testaa malleja ja agentteja nopeasti ennen reunakäyttöönottoa
- **Moni-toimittajainen joustavuus**: Käytä malleja eri lähteistä parhaan reunaratkaisun löytämiseksi
- **Paikallinen kehitys**: Testaa ONNX:llä ja Ollamalla offline-tilassa ja yksityisyyttä kunnioittaen
- **Tuotantovalmius**: Generoi tuotantokelpoinen koodi ja integroi ulkoisiin työkaluihin MCP:n kautta
- **Kattava arviointi**: Käytä sisäänrakennettuja ja mukautettuja mittareita reunatiedon AI:n suorituskyvyn validoimiseen

Kun tekoäly siirtyy yhä enemmän reunakäyttöskenaarioihin, AI Toolkit VS Codelle tarjoaa kehitysympäristön ja työnkulun älykkäiden sovellusten rakentamiseen, testaamiseen ja optimointiin resurssirajoitteisissa ympäristöissä. Kehitätpä sitten IoT-ratkaisuja, mobiilitekoälysovelluksia tai sulautettuja älyjärjestelmiä, työkalupaketin monipuoliset ominaisuudet ja integroitu työnkulku tukevat koko reunatiedon tekoälyn kehityssykliä.

Jatkuvan kehityksen ja aktiivisen yhteisön (1,8k+ GitHub-tähteä) myötä AI Toolkit pysyy tekoälyn kehitystyökalujen eturintamassa, kehittyen jatkuvasti vastaamaan modernien tekoälykehittäjien tarpeita reunakäyttöskenaarioissa.

[Seuraava Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->