# AI Toolkit for Visual Studio Code - Edge AI -kehityksen opas

## Johdanto

Tervetuloa kattavaan oppaaseen AI Toolkitin käytöstä Visual Studio Codessa Edge AI -kehityksessä. Kun tekoäly siirtyy keskitetystä pilvilaskennasta hajautettuihin reunalaitteisiin, kehittäjät tarvitsevat tehokkaita, integroituja työkaluja, jotka pystyvät käsittelemään reunasovellusten ainutlaatuisia haasteita - kuten resurssirajoituksia ja offline-toimintavaatimuksia.

AI Toolkit for Visual Studio Code täyttää tämän tarpeen tarjoamalla täydellisen kehitysympäristön, joka on erityisesti suunniteltu rakentamaan, testaamaan ja optimoimaan tekoälysovelluksia, jotka toimivat tehokkaasti reunalaitteilla. Olitpa kehittämässä IoT-antureille, mobiililaitteille, sulautetuille järjestelmille tai reunapalvelimille, tämä työkalu virtaviivaistaa koko kehitysprosessin tutussa VS Code -ympäristössä.

Tämä opas johdattaa sinut tärkeimpiin käsitteisiin, työkaluihin ja parhaisiin käytäntöihin AI Toolkitin hyödyntämiseksi Edge AI -projekteissasi, alkaen mallin valinnasta aina tuotantokäyttöön saakka.

## Yleiskatsaus

AI Toolkit for Visual Studio Code on tehokas laajennus, joka virtaviivaistaa agenttien kehitystä ja tekoälysovellusten luomista. Työkalu tarjoaa kattavat ominaisuudet AI-mallien tutkimiseen, arviointiin ja käyttöönottoon monilta eri tarjoajilta, kuten Anthropic, OpenAI, GitHub ja Google, samalla kun se tukee paikallista mallien suorittamista ONNX:n ja Ollaman avulla.

AI Toolkit erottuu edukseen kattavalla lähestymistavallaan koko tekoälyn kehityssykliin. Toisin kuin perinteiset tekoälytyökalut, jotka keskittyvät yksittäisiin osa-alueisiin, AI Toolkit tarjoaa integroidun ympäristön, joka kattaa mallien löytämisen, kokeilun, agenttien kehityksen, arvioinnin ja käyttöönoton - kaikki tutussa VS Code -ympäristössä.

Alusta on erityisesti suunniteltu nopeaan prototyyppaukseen ja tuotantokäyttöön, ja siinä on ominaisuuksia, kuten kehotusten luonti, nopeat aloitustyökalut, saumattomat MCP (Model Context Protocol) -integraatiot ja laajat arviointimahdollisuudet. Edge AI -kehityksessä tämä tarkoittaa, että voit tehokkaasti kehittää, testata ja optimoida tekoälysovelluksia reunasovelluksia varten samalla kun säilytät koko kehitysprosessin VS Codessa.

## Oppimistavoitteet

Oppaan lopussa osaat:

### Keskeiset taidot
- **Asentaa ja konfiguroida** AI Toolkitin Visual Studio Codeen Edge AI -kehitystä varten
- **Navigoida ja käyttää** AI Toolkitin käyttöliittymää, mukaan lukien Model Catalog, Playground ja Agent Builder
- **Valita ja arvioida** tekoälymalleja, jotka soveltuvat reunakäyttöön suorituskyvyn ja resurssirajoitusten perusteella
- **Muuntaa ja optimoida** malleja ONNX-muotoon ja kvantisointitekniikoilla reunalaitteita varten

### Edge AI -kehitystaidot
- **Suunnitella ja toteuttaa** Edge AI -sovelluksia integroidussa kehitysympäristössä
- **Testata malleja** reunamaisia olosuhteita simuloiden paikallisen inferenssin ja resurssien seurannan avulla
- **Luoda ja mukauttaa** tekoälyagentteja, jotka on optimoitu reunakäyttöön
- **Arvioida mallien suorituskykyä** reunalaskentaan liittyvien mittareiden avulla (viive, muistin käyttö, tarkkuus)

### Optimointi ja käyttöönotto
- **Soveltaa kvantisointia ja karsintaa** mallin koon pienentämiseksi säilyttäen hyväksyttävä suorituskyky
- **Optimoida malleja** tiettyjä reunalaitteiden laitteistoalustoja varten, mukaan lukien CPU-, GPU- ja NPU-kiihdytys
- **Toteuttaa parhaat käytännöt** Edge AI -kehityksessä, mukaan lukien resurssien hallinta ja varajärjestelmät
- **Valmistella malleja ja sovelluksia** tuotantokäyttöön reunalaitteilla

### Edistyneet Edge AI -käsitteet
- **Integrointi reunalaskentakehysten kanssa**, kuten ONNX Runtime, Windows ML ja TensorFlow Lite
- **Toteuttaa monimallisia arkkitehtuureja** ja hajautetun oppimisen skenaarioita reunaympäristöissä
- **Ratkaista yleisiä Edge AI -ongelmia**, kuten muistin rajoitukset, inferenssin nopeus ja laitteistoyhteensopivuus
- **Suunnitella seurantaa ja lokitusta** Edge AI -sovelluksille tuotantokäytössä

### Käytännön soveltaminen
- **Rakentaa kokonaisvaltaisia Edge AI -ratkaisuja** mallin valinnasta käyttöönottoon
- **Osoittaa osaamista** reunakohtaisissa kehitysprosesseissa ja optimointitekniikoissa
- **Soveltaa opittuja käsitteitä** todellisiin Edge AI -käyttötapauksiin, kuten IoT-, mobiili- ja sulautettuihin sovelluksiin
- **Arvioida ja vertailla** erilaisia Edge AI -käyttöönoton strategioita ja niiden kompromisseja

## Keskeiset ominaisuudet Edge AI -kehitykseen

### 1. Mallikatalogi ja löytö
- **Monen tarjoajan tuki**: Selaa ja käytä tekoälymalleja Anthropicilta, OpenAI:lta, GitHubilta, Googlelta ja muilta tarjoajilta
- **Paikallisten mallien integrointi**: Yksinkertaistettu ONNX- ja Ollama-mallien löytäminen reunakäyttöön
- **GitHub-mallit**: Suora integrointi GitHubin mallien isännöintiin
- **Mallien vertailu**: Vertaa malleja rinnakkain löytääksesi optimaalisen tasapainon reunalaitteiden rajoituksiin

### 2. Interaktiivinen Playground
- **Interaktiivinen testausympäristö**: Nopea kokeilu mallien ominaisuuksilla kontrolloidussa ympäristössä
- **Monimodaalinen tuki**: Testaa kuvia, tekstiä ja muita reunaskenaarioille tyypillisiä syötteitä
- **Reaaliaikainen kokeilu**: Välitön palaute mallin vastauksista ja suorituskyvystä
- **Parametrien optimointi**: Hienosäädä mallin parametreja reunakäyttöön

### 3. Kehotus (Agent) Builder
- **Luonnollisen kielen generointi**: Luo aloituskehotuksia luonnollisen kielen kuvauksilla
- **Iteratiivinen parantaminen**: Paranna kehotuksia mallin vastausten ja suorituskyvyn perusteella
- **Tehtävien pilkkominen**: Jaa monimutkaiset tehtävät kehotusketjuilla ja jäsennellyillä tuloksilla
- **Muuttujien tuki**: Käytä muuttujia kehotuksissa dynaamisen agenttikäyttäytymisen luomiseksi
- **Tuotantokoodin generointi**: Luo tuotantovalmiita koodeja nopeaan sovelluskehitykseen

### 4. Massatestaus ja arviointi
- **Monimallinen testaus**: Suorita useita kehotuksia valituilla malleilla samanaikaisesti
- **Tehokas testaus laajassa mittakaavassa**: Testaa erilaisia syötteitä ja kokoonpanoja tehokkaasti
- **Mukautetut testitapaukset**: Suorita agentteja testitapauksilla toiminnallisuuden varmistamiseksi
- **Suorituskyvyn vertailu**: Vertaa tuloksia eri mallien ja kokoonpanojen välillä

### 5. Mallien arviointi datasetien avulla
- **Standardimittarit**: Testaa tekoälymalleja sisäänrakennetuilla arviointityökaluilla (F1-pisteet, relevanssi, samankaltaisuus, koherenssi)
- **Mukautetut arviointityökalut**: Luo omia arviointimittareita erityisiin käyttötarkoituksiin
- **Datasetin integrointi**: Testaa malleja kattavien datasetien avulla
- **Suorituskyvyn mittaus**: Kvantifioi mallien suorituskyky reunakäyttöpäätösten tueksi

### 6. Hienosäätöominaisuudet
- **Mallien mukauttaminen**: Mukauta malleja erityisiin käyttötarkoituksiin ja toimialoihin
- **Erikoistunut sovittaminen**: Sovita malleja erikoistuneisiin toimialoihin ja vaatimuksiin
- **Reunaoptimointi**: Hienosäädä malleja erityisesti reunakäyttöön liittyviin rajoituksiin
- **Toimialakohtainen koulutus**: Luo malleja, jotka on räätälöity erityisiin reunakäyttötapauksiin

### 7. MCP-työkalujen integrointi
- **Ulkoisten työkalujen yhdistäminen**: Yhdistä agentit ulkoisiin työkaluihin Model Context Protocol -palvelimien kautta
- **Reaaliaikaiset toiminnot**: Mahdollista agenttien kyselyt tietokannoista, API-yhteydet tai mukautetun logiikan suorittaminen
- **Olemassa olevat MCP-palvelimet**: Käytä työkaluja komentoriviltä (stdio) tai HTTP-protokollasta (server-sent event)
- **Mukautettu MCP-kehitys**: Rakenna ja testaa uusia MCP-palvelimia Agent Builderissa

### 8. Agenttien kehitys ja testaus
- **Toimintokutsujen tuki**: Mahdollista agenttien dynaaminen ulkoisten toimintojen kutsuminen
- **Reaaliaikainen integraatiotestaus**: Testaa integraatioita reaaliaikaisilla ajoilla ja työkalujen käytöllä
- **Agenttien versiointi**: Versiohallinta agenteille ja vertailuominaisuudet arviointituloksille
- **Virheenkorjaus ja jäljitys**: Paikallinen jäljitys ja virheenkorjaus agenttien kehityksessä

## Edge AI -kehityksen työkulku

### Vaihe 1: Mallien löytäminen ja valinta
1. **Tutki mallikatalogia**: Käytä mallikatalogia löytääksesi malleja, jotka soveltuvat reunakäyttöön
2. **Vertaa suorituskykyä**: Arvioi malleja koon, tarkkuuden ja inferenssin nopeuden perusteella
3. **Testaa paikallisesti**: Käytä Ollama- tai ONNX-malleja testataksesi paikallisesti ennen reunakäyttöä
4. **Arvioi resurssivaatimukset**: Määritä muisti- ja laskentatarpeet kohdelaitteille

### Vaihe 2: Mallien optimointi
1. **Muunna ONNX-muotoon**: Muunna valitut mallit ONNX-muotoon reunayhteensopivuutta varten
2. **Sovella kvantisointia**: Pienennä mallin kokoa INT8- tai INT4-kvantisoinnilla
3. **Laitteistooptimointi**: Optimoi kohdelaitteiston mukaan (ARM, x86, erikoiskiihdyttimet)
4. **Suorituskyvyn validointi**: Varmista, että optimoidut mallit säilyttävät hyväksyttävän tarkkuuden

### Vaihe 3: Sovelluskehitys
1. **Agenttien suunnittelu**: Käytä Agent Builderia luodaksesi reunakäyttöön optimoituja tekoälyagentteja
2. **Kehotusmuotoilu**: Kehitä kehotuksia, jotka toimivat tehokkaasti pienempien reunamallien kanssa
3. **Integraatiotestaus**: Testaa agentteja simuloiduissa reunaympäristöissä
4. **Koodin generointi**: Luo tuotantokoodi, joka on optimoitu reunakäyttöön

### Vaihe 4: Arviointi ja testaus
1. **Massaarviointi**: Testaa useita kokoonpanoja löytääksesi optimaaliset reunasetukset
2. **Suorituskyvyn profilointi**: Analysoi inferenssin nopeutta, muistin käyttöä ja tarkkuutta
3. **Reunasimulaatio**: Testaa olosuhteissa, jotka vastaavat kohteen reunakäyttöympäristöä
4. **Rasitustestaus**: Arvioi suorituskykyä eri kuormitusolosuhteissa

### Vaihe 5: Käyttöönoton valmistelu
1. **Lopullinen optimointi**: Tee viimeiset optimoinnit testitulosten perusteella
2. **Käyttöpaketointi**: Pakkaa mallit ja koodi reunakäyttöä varten
3. **Dokumentointi**: Dokumentoi käyttöönoton vaatimukset ja kokoonpano
4. **Seurannan valmistelu**: Valmistaudu seurantaan ja lokitukseen reunakäytössä

## Kohderyhmä Edge AI -kehitykselle

### Edge AI -kehittäjät
- Sovelluskehittäjät, jotka rakentavat tekoälypohjaisia reunalaitteita ja IoT-ratkaisuja
- Sulautettujen järjestelmien kehittäjät, jotka integroivat tekoälyominaisuuksia resurssirajoitteisiin laitteisiin
- Mobiilikehittäjät, jotka luovat laitekohtaisia tekoälysovelluksia älypuhelimille ja tableteille

### Edge AI -insinöörit
- Tekoälyinsinöörit, jotka optimoivat malleja reunakäyttöön ja hallitsevat inferenssiputkia
- DevOps-insinöörit, jotka ottavat käyttöön ja hallitsevat tekoälymalleja hajautetussa reunainfrastruktuurissa
- Suorituskykyinsinöörit, jotka optimoivat tekoälytyökuormia reunalaitteiden rajoituksiin

### Tutkijat ja kouluttajat
- Tekoälytutkijat, jotka kehittävät tehokkaita malleja ja algoritmeja reunalaskentaan
- Kouluttajat, jotka opettavat Edge AI -käsitteitä ja demonstroivat optimointitekniikoita
- Opiskelijat, jotka oppivat reunalaskennan haasteista ja ratkaisuista

## Edge AI -käyttötapaukset

### Älykkäät IoT-laitteet
- **Reaaliaikainen kuvantunnistus**: Tietokonenäkömallien käyttö IoT-kameroissa ja -antureissa
- **Puheenkäsittely**: Puheentunnistuksen ja luonnollisen kielen käsittelyn toteutus älykaiuttimissa
- **Ennakoiva huolto**: Poikkeavuuksien tunnistusmallien käyttö teollisuuden reunalaitteilla
- **Ympäristön seuranta**: Anturidatan analyysimallien käyttö ympäristösovelluksissa

### Mobiili- ja sulautetut sovellukset
- **Laitekohtainen käännös**: Käännösmallien toteutus, jotka toimivat offline-tilassa
- **Lisätty todellisuus**: Reaaliaikainen objektien tunnistus ja seuranta AR-sovelluksille
- **Terveydenseuranta**: Terveysanalyysimallien käyttö puettavissa laitteissa ja lääketieteellisissä laitteissa
- **Autonomiset järjestelmät**: Päätöksentekomallien toteutus droneille, roboteille ja ajoneuvoille

### Reunalaskentainfrastruktuuri
- **Reunadatakeskukset**: Tekoälymallien käyttö reunadatakeskuksissa matalan viiveen sovelluksille
- **CDN-integraatio**: Tekoälykäsittelyn integrointi sisällönjakeluverkkoihin
- **5G-reuna**: 5G-reunalaskennan hyödyntäminen tekoälypohjaisissa sovelluksissa
- **Sumulaskenta**: Tekoälykäsittelyn toteutus sumulaskentaympäristöissä

## Asennus ja käyttöönotto

### Laajennuksen asennus
Asenna AI Toolkit -laajennus suoraan Visual Studio Code Marketplacesta:

**Laajennuksen ID**: `ms-windows-ai-studio.windows-ai-studio`

**Asennustavat**:
1. **VS Code Marketplace**: Etsi "AI Toolkit" Extensions-näkymästä
2. **Komentorivi**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **
2. Luo aloituskehotteita luonnollisen kielen kuvauksilla  
3. Iteroi ja hienosäädä kehotteita mallin vastausten perusteella  
4. Integroi MCP-työkalut parantaaksesi agenttien kyvykkyyksiä  

#### Vaihe 3: Testaus ja arviointi  
1. Käytä **Bulk Run** -toimintoa testataksesi useita kehotteita valituilla malleilla  
2. Aja agentteja testitapauksilla toiminnallisuuden varmistamiseksi  
3. Arvioi tarkkuutta ja suorituskykyä sisäänrakennetuilla tai mukautetuilla mittareilla  
4. Vertaa eri malleja ja kokoonpanoja  

#### Vaihe 4: Hienosäätö ja optimointi  
1. Mukauta malleja erityisiin reunatapauksiin  
2. Sovella alakohtaisia hienosäätöjä  
3. Optimoi reunalaitteiden rajoituksia varten  
4. Versioi ja vertaa eri agenttien kokoonpanoja  

#### Vaihe 5: Käyttöönottovalmistelu  
1. Luo tuotantovalmiit koodit Agent Builderilla  
2. Määritä MCP-palvelinyhteydet tuotantokäyttöä varten  
3. Valmistele käyttöpaketit reunalaitteille  
4. Konfiguroi seuranta- ja arviointimittarit  

## Esimerkkejä AI Toolkitille  

Kokeile esimerkkejämme  
[AI Toolkit -esimerkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) on suunniteltu auttamaan kehittäjiä ja tutkijoita AI-ratkaisujen tutkimisessa ja toteuttamisessa tehokkaasti.  

Esimerkkimme sisältävät:  

Esimerkkikoodi: Valmiita esimerkkejä, jotka havainnollistavat AI-toimintoja, kuten mallien koulutusta, käyttöönottoa tai integrointia sovelluksiin.  
Dokumentaatio: Oppaita ja tutoriaaleja, jotka auttavat käyttäjiä ymmärtämään AI Toolkitin ominaisuuksia ja niiden käyttöä.  
Edellytykset  

- Visual Studio Code  
- AI Toolkit for Visual Studio Code  
- GitHubin hienojakoiset henkilökohtaiset käyttöoikeustunnukset (PAT)  
- Foundry Local  

## Parhaat käytännöt Edge AI -kehityksessä  

### Mallin valinta  
- **Kokorajoitukset**: Valitse mallit, jotka mahtuvat kohdelaitteiden muistirajoituksiin  
- **Päätöksentekonopeus**: Suosi malleja, joilla on nopea päätöksentekoaika reaaliaikaisiin sovelluksiin  
- **Tarkkuuden kompromissit**: Tasapainota mallin tarkkuus ja resurssirajoitukset  
- **Muotoyhteensopivuus**: Suosi ONNX- tai laitteistolle optimoituja muotoja reunakäyttöön  

### Optimointitekniikat  
- **Kvantisointi**: Käytä INT8- tai INT4-kvantisointia pienentääksesi mallin kokoa ja parantaaksesi nopeutta  
- **Karsinta**: Poista tarpeettomat malliparametrit vähentääksesi laskentavaatimuksia  
- **Tietojen tislaus**: Luo pienempiä malleja, jotka säilyttävät suurempien mallien suorituskyvyn  
- **Laitteistokiihdytys**: Hyödynnä NPU-, GPU- tai erikoiskiihdyttimiä, kun saatavilla  

### Kehitystyönkulku  
- **Iteratiivinen testaus**: Testaa usein reunalaitteiden kaltaisissa olosuhteissa kehityksen aikana  
- **Suorituskyvyn seuranta**: Seuraa jatkuvasti resurssien käyttöä ja päätöksentekonopeutta  
- **Versionhallinta**: Seuraa malliversioita ja optimointiasetuksia  
- **Dokumentointi**: Dokumentoi kaikki optimointipäätökset ja suorituskyvyn kompromissit  

### Käyttöönoton huomioitavat asiat  
- **Resurssien seuranta**: Seuraa muistia, CPU:ta ja virrankulutusta tuotannossa  
- **Varajärjestelmät**: Toteuta varajärjestelmät mallin epäonnistumisten varalta  
- **Päivitysmekanismit**: Suunnittele mallipäivitykset ja versioiden hallinta  
- **Turvallisuus**: Toteuta asianmukaiset turvallisuustoimenpiteet Edge AI -sovelluksille  

## Integrointi Edge AI -kehyksiin  

### ONNX Runtime  
- **Monialustainen käyttöönotto**: Ota ONNX-mallit käyttöön eri reunalaitteilla  
- **Laitteisto-optimointi**: Hyödynnä ONNX Runtimen laitteistokohtaisia optimointeja  
- **Mobiilituki**: Käytä ONNX Runtime Mobilea älypuhelin- ja tablettisovelluksissa  
- **IoT-integraatio**: Ota käyttöön IoT-laitteilla ONNX Runtimen kevyitä jakeluita  

### Windows ML  
- **Windows-laitteet**: Optimoi Windows-pohjaisille reunalaitteille ja PC:ille  
- **NPU-kiihdytys**: Hyödynnä Neural Processing Unit -yksiköitä Windows-laitteilla  
- **DirectML**: Käytä DirectML:ää GPU-kiihdytykseen Windows-alustoilla  
- **UWP-integraatio**: Integroi Universal Windows Platform -sovelluksiin  

### TensorFlow Lite  
- **Mobiilioptimointi**: Ota TensorFlow Lite -mallit käyttöön mobiili- ja sulautetuilla laitteilla  
- **Laitteistodelegaatit**: Käytä erikoistuneita laitteistodelegaatteja kiihdytykseen  
- **Mikrokontrollerit**: Ota käyttöön mikrokontrollereilla TensorFlow Lite Micro  
- **Monialustatuki**: Ota käyttöön Android-, iOS- ja sulautetuilla Linux-järjestelmillä  

### Azure IoT Edge  
- **Pilvi-reuna hybridi**: Yhdistä pilvikoulutus ja reunapäätöksenteko  
- **Moduulikäyttöönotto**: Ota AI-mallit käyttöön IoT Edge -moduuleina  
- **Laitteiden hallinta**: Hallitse reunalaitteita ja mallipäivityksiä etänä  
- **Telemetria**: Kerää suorituskykytietoja ja mallimittareita reunakäyttöönotosta  

## Edistyneet Edge AI -skenaariot  

### Monimallikäyttöönotto  
- **Mallikokoonpanot**: Ota käyttöön useita malleja tarkkuuden parantamiseksi tai redundanssin lisäämiseksi  
- **A/B-testaus**: Testaa eri malleja samanaikaisesti reunalaitteilla  
- **Dynaaminen valinta**: Valitse mallit laitteen nykyisten olosuhteiden perusteella  
- **Resurssien jakaminen**: Optimoi resurssien käyttö useiden mallien välillä  

### Federated Learning  
- **Hajautettu koulutus**: Kouluta malleja useilla reunalaitteilla  
- **Tietosuojan säilyttäminen**: Pidä koulutusdata paikallisena ja jaa vain malliparannuksia  
- **Yhteistoiminnallinen oppiminen**: Mahdollista laitteiden oppiminen yhteisistä kokemuksista  
- **Reuna-pilvi koordinointi**: Koordinoi oppimista reunalaitteiden ja pilvi-infrastruktuurin välillä  

### Reaaliaikainen käsittely  
- **Virtauskäsittely**: Käsittele jatkuvia datavirtoja reunalaitteilla  
- **Matala viive**: Optimoi minimaalista päätöksentekoviivettä varten  
- **Eräkäsittely**: Käsittele tehokkaasti datan erämuotoista käsittelyä reunalaitteilla  
- **Mukautuva käsittely**: Säädä käsittelyä laitteen nykyisten kyvykkyyksien mukaan  

## Vianetsintä Edge AI -kehityksessä  

### Yleiset ongelmat  
- **Muistirajoitukset**: Malli liian suuri kohdelaitteen muistiin  
- **Päätöksentekonopeus**: Mallin päätöksenteko liian hidas reaaliaikaisiin vaatimuksiin  
- **Tarkkuuden heikkeneminen**: Optimointi heikentää mallin tarkkuutta liikaa  
- **Laitteistoyhteensopivuus**: Malli ei ole yhteensopiva kohdelaitteen kanssa  

### Vianetsintästrategiat  
- **Suorituskyvyn profilointi**: Käytä AI Toolkitin jäljitysominaisuuksia pullonkaulojen tunnistamiseen  
- **Resurssien seuranta**: Seuraa muistia ja CPU:n käyttöä kehityksen aikana  
- **Inkrementaalinen testaus**: Testaa optimointeja vaiheittain ongelmien eristämiseksi  
- **Laitteistosimulaatio**: Käytä kehitystyökaluja kohdelaitteiden simulointiin  

### Optimointiratkaisut  
- **Lisäkvantisointi**: Sovella aggressiivisempia kvantisointitekniikoita  
- **Mallin arkkitehtuuri**: Harkitse eri mallin arkkitehtuureja, jotka on optimoitu reunakäyttöön  
- **Esikäsittelyn optimointi**: Optimoi datan esikäsittely reunarajoituksia varten  
- **Päätöksenteko-optimointi**: Käytä laitteistokohtaisia päätöksenteko-optimointeja  

## Resurssit ja seuraavat askeleet  

### Virallinen dokumentaatio  
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)  
- [Asennus- ja käyttöopas](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Documentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)  

### Yhteisö ja tuki  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues ja ominaisuuspyynnöt](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord -yhteisö](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Teknisiä resursseja  
- [ONNX Runtime Documentation](https://onnxruntime.ai/)  
- [Ollama Documentation](https://ollama.ai/)  
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Oppimispolut  
- [Edge AI Fundamentals Course](../Module01/README.md)  
- [Small Language Models Guide](../Module02/README.md)  
- [Edge Deployment Strategies](../Module03/README.md)  
- [Windows Edge AI Development](./windowdeveloper.md)  

### Lisäresurssit  
- **Repository Stats**: 1.8k+ tähteä, 150+ haarukkaa, 18+ avustajaa  
- **Lisenssi**: MIT-lisenssi  
- **Turvallisuus**: Microsoftin turvallisuuskäytännöt koskevat  
- **Telemetria**: Kunnioittaa VS Code -telemetria-asetuksia  

## Yhteenveto  

AI Toolkit for Visual Studio Code edustaa kattavaa alustaa modernille AI-kehitykselle, tarjoten virtaviivaisia agenttikehityksen mahdollisuuksia, jotka ovat erityisen arvokkaita Edge AI -sovelluksille. Sen laaja mallikatalogi tukee tarjoajia, kuten Anthropic, OpenAI, GitHub ja Google, yhdistettynä paikalliseen suorittamiseen ONNX:n ja Ollaman kautta, tarjoten joustavuutta monipuolisiin reunakäyttöönottoskenaarioihin.  

Työkalun vahvuus piilee sen integroidussa lähestymistavassa—mallien löytämisestä ja kokeilusta Playgroundissa kehittyneeseen agenttikehitykseen Prompt Builderilla, kattaviin arviointimahdollisuuksiin ja saumattomaan MCP-työkalujen integrointiin. Edge AI -kehittäjille tämä tarkoittaa nopeaa prototyyppien ja AI-agenttien testausta ennen reunakäyttöönottoa, mahdollisuutta iterointiin ja optimointiin resurssirajoitteisissa ympäristöissä.  

Keskeiset edut Edge AI -kehityksessä:  
- **Nopea kokeilu**: Testaa malleja ja agentteja nopeasti ennen reunakäyttöönottoa  
- **Monitarjoajavalmius**: Pääsy malleihin eri lähteistä optimaalisten reunaratkaisujen löytämiseksi  
- **Paikallinen kehitys**: Testaa ONNX:llä ja Ollamalla offline- ja yksityisyyttä säilyttävässä kehityksessä  
- **Tuotantovalmius**: Luo tuotantovalmiita koodeja ja integroi ulkoisiin työkaluihin MCP:n kautta  
- **Kattava arviointi**: Käytä sisäänrakennettuja ja mukautettuja mittareita Edge AI:n suorituskyvyn validointiin  

Kun AI siirtyy yhä enemmän reunakäyttöönottoskenaarioihin, AI Toolkit for VS Code tarjoaa kehitysympäristön ja työnkulun, joka tarvitaan älykkäiden sovellusten rakentamiseen, testaamiseen ja optimointiin resurssirajoitteisissa ympäristöissä. Olipa kyseessä IoT-ratkaisujen kehitys, mobiili-AI-sovellukset tai sulautetut älyjärjestelmät, työkalun kattava ominaisuusvalikoima ja integroitu työnkulku tukevat koko Edge AI -kehityksen elinkaarta.  

Jatkuvan kehityksen ja aktiivisen yhteisön (1.8k+ GitHub-tähteä) ansiosta AI Toolkit pysyy AI-kehitystyökalujen eturintamassa, kehittyen jatkuvasti vastaamaan modernien AI-kehittäjien tarpeita, jotka rakentavat reunakäyttöönottoskenaarioita.  

[Next Foundry Local](./foundrylocal.md)  

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.