# Luku 03: Pienten kielimallien (SLM) käyttöönotto

Tämä kattava luku käsittelee pienten kielimallien (SLM) käyttöönoton koko elinkaarta, sisältäen teoreettiset perusteet, käytännön toteutusstrategiat ja tuotantovalmiit konttipohjaiset ratkaisut. Luku on jaettu kolmeen edistyvään osioon, jotka vievät lukijan peruskäsitteistä kehittyneisiin käyttöönoton skenaarioihin.

## Luvun rakenne ja oppimispolku

### **[Osa 1: SLM:n edistynyt oppiminen - perusteet ja optimointi](./01.SLMAdvancedLearning.md)**
Ensimmäinen osa luo teoreettisen pohjan pienten kielimallien ymmärtämiselle ja niiden strategiselle merkitykselle edge AI -ratkaisuissa. Tämä osa käsittelee:

- **Parametrien luokittelukehys**: Yksityiskohtainen tarkastelu SLM-luokista, kuten Micro SLM:t (100M-1.4B parametriä) ja Medium SLM:t (14B-30B parametriä), keskittyen malleihin kuten Phi-4-mini-3.8B, Qwen3-sarja ja Google Gemma3, mukaan lukien laitteistovaatimukset ja muistinkäytön analyysi kullekin mallitasolle
- **Edistyneet optimointitekniikat**: Laaja käsittely kvantisointimenetelmistä, kuten Llama.cpp, Microsoft Olive ja Apple MLX -kehykset, mukaan lukien huipputason BitNET 1-bittinen kvantisointi käytännön koodiesimerkeillä, jotka näyttävät kvantisointiputket ja vertailutulokset
- **Mallien hankintastrategiat**: Syvällinen analyysi Hugging Face -ekosysteemistä ja Azure AI Foundry Model Catalogista yritystason SLM-käyttöönottoa varten, sisältäen koodiesimerkkejä ohjelmalliseen mallien lataamiseen, validointiin ja formaattimuunnokseen
- **Kehittäjä-API:t**: Koodiesimerkkejä Pythonilla, C++:lla ja C#:lla, jotka näyttävät, miten malleja ladataan, suoritetaan inferenssiä ja integroidaan suosittuihin kehyksiin, kuten PyTorch, TensorFlow ja ONNX Runtime

Tämä perustavanlaatuinen osa korostaa operatiivisen tehokkuuden, käyttöönoton joustavuuden ja kustannustehokkuuden tasapainoa, joka tekee SLM:stä ihanteellisen edge-laskentaskenaarioihin, sisältäen käytännön koodiesimerkkejä, joita kehittäjät voivat suoraan hyödyntää projekteissaan.

### **[Osa 2: Paikallinen ympäristökäyttöönotto - yksityisyyttä korostavat ratkaisut](./02.DeployingSLMinLocalEnv.md)**
Toinen osa siirtyy teoriasta käytännön toteutukseen, keskittyen paikallisiin käyttöönoton strategioihin, jotka painottavat datan suvereniteettia ja operatiivista riippumattomuutta. Keskeiset aiheet sisältävät:

- **Ollama Universal Platform**: Kattava tarkastelu alustojen välisestä käyttöönotosta, painottaen kehittäjäystävällisiä työnkulkuja, mallien elinkaaren hallintaa ja räätälöintiä Modelfiles-tiedostojen avulla, sisältäen täydelliset REST API -integraatioesimerkit ja CLI-automaatioskriptit
- **Microsoft Foundry Local**: Yritystason käyttöönoton ratkaisut ONNX-pohjaisella optimoinnilla, Windows ML -integraatiolla ja kattavilla tietoturvaominaisuuksilla, sisältäen C#- ja Python-koodiesimerkkejä natiivisovellusten integrointiin
- **Vertailuanalyysi**: Yksityiskohtainen kehysten vertailu, joka kattaa teknisen arkkitehtuurin, suorituskykyominaisuudet ja käyttötapausoptimoinnin ohjeet, sisältäen vertailukoodin inferenssinopeuden ja muistinkäytön arviointiin eri laitteistoilla
- **API-integraatio**: Esimerkkisovelluksia, jotka näyttävät, miten rakentaa verkkopalveluita, chat-sovelluksia ja datankäsittelyputkia paikallisia SLM-käyttöönottoja hyödyntäen, sisältäen koodiesimerkkejä Node.js:llä, Python Flask/FastAPI:lla ja ASP.NET Corella
- **Testauskehykset**: Automatisoidut testauslähestymistavat mallien laadunvarmistukseen, sisältäen yksikkö- ja integraatiotestiesimerkkejä SLM-toteutuksille

Tämä osa tarjoaa käytännön ohjeita organisaatioille, jotka haluavat toteuttaa yksityisyyttä suojelevia AI-ratkaisuja samalla säilyttäen täyden hallinnan käyttöönottoympäristöstään, sisältäen valmiita koodiesimerkkejä, joita kehittäjät voivat mukauttaa omiin tarpeisiinsa.

### **[Osa 3: Konttipohjainen pilvikäyttöönotto - tuotantomittakaavan ratkaisut](./03.DeployingSLMinCloud.md)**
Viimeinen osa huipentuu kehittyneisiin konttipohjaisiin käyttöönoton strategioihin, joissa Microsoftin Phi-4-mini-instruct toimii pääasiallisena tapaustutkimuksena. Tämä osa käsittelee:

- **vLLM-käyttöönotto**: Suorituskykyinen inferenssioptimointi OpenAI-yhteensopivilla API:illa, kehittyneellä GPU-kiihdytyksellä ja tuotantovalmiilla konfiguraatiolla, sisältäen täydelliset Dockerfile-tiedostot, Kubernetes-manifestit ja suorituskyvyn hienosäätöparametrit
- **Ollama Container Orchestration**: Yksinkertaistetut käyttöönoton työnkulut Docker Compose -työkaluilla, mallien optimointivariaatiot ja verkkokäyttöliittymän integrointi, sisältäen CI/CD-putkiesimerkit automatisoituun käyttöönottoon ja testaukseen
- **ONNX Runtime -toteutus**: Edge-optimoitu käyttöönotto kattavilla mallimuunnoksilla, kvantisointistrategioilla ja alustojen välisellä yhteensopivuudella, sisältäen yksityiskohtaiset koodiesimerkit mallien optimointiin ja käyttöönottoon
- **Seuranta ja näkyvyys**: Prometheus/Grafana-hallintapaneelien toteutus mukautetuilla mittareilla SLM-suorituskyvyn seurantaan, sisältäen hälytyskonfiguraatiot ja lokien keräys
- **Kuormituksen tasapainotus ja skaalaus**: Käytännön esimerkkejä horisontaalisista ja vertikaalisista skaalausstrategioista, sisältäen automaattisen skaalauksen konfiguraatiot CPU/GPU-käytön ja pyyntömallien perusteella
- **Tietoturvan vahvistaminen**: Konttien tietoturvan parhaat käytännöt, mukaan lukien käyttöoikeuksien vähentäminen, verkon käytännöt ja salaisuuksien hallinta API-avaimille ja mallien käyttöoikeustiedoille

Jokainen käyttöönoton lähestymistapa esitetään täydellisten konfiguraatioesimerkkien, testausmenetelmien, tuotantovalmiuden tarkistuslistojen ja infrastruktuuri-koodina-mallien avulla, joita kehittäjät voivat suoraan soveltaa käyttöönoton työnkulkuihinsa.

## Keskeiset oppimistulokset

Luvun suorittamalla lukijat hallitsevat:

1. **Strateginen mallivalinta**: Parametrirajojen ymmärtäminen ja sopivien SLM-mallien valinta resurssirajoitteiden ja suorituskykyvaatimusten perusteella
2. **Optimoinnin hallinta**: Edistyneiden kvantisointitekniikoiden toteuttaminen eri kehyksissä optimaalisen suorituskyvyn ja tehokkuuden tasapainon saavuttamiseksi
3. **Käyttöönoton joustavuus**: Valinta paikallisten yksityisyyttä korostavien ratkaisujen ja skaalautuvien konttipohjaisten käyttöönottojen välillä organisaation tarpeiden mukaan
4. **Tuotantovalmius**: Seuranta-, tietoturva- ja skaalausjärjestelmien konfigurointi yritystason SLM-käyttöönottoja varten

## Käytännön painotus ja tosielämän sovellukset

Luku säilyttää vahvan käytännönläheisen otteen läpi koko sisällön, sisältäen:

- **Käytännön esimerkit**: Täydelliset konfiguraatiotiedostot, API-testauksen menetelmät ja käyttöönoton skriptit
- **Suorituskyvyn vertailu**: Yksityiskohtaiset vertailut inferenssinopeudesta, muistinkäytöstä ja resurssivaatimuksista
- **Tietoturvanäkökohdat**: Yritystason tietoturvakäytännöt, vaatimustenmukaisuuskehykset ja datan suojausstrategiat
- **Parhaat käytännöt**: Tuotantotestatut ohjeet seurantaan, skaalaamiseen ja ylläpitoon

## Tulevaisuuteen suuntautunut näkökulma

Luku päättyy tulevaisuuteen katsoviin näkemyksiin, jotka käsittelevät:

- Kehittyneitä mallirakenteita parannetuilla tehokkuussuhteilla
- Syvempää laitteistointegraatiota erikoistuneiden AI-kiihdyttimien kanssa
- Ekosysteemin kehitystä kohti standardointia ja yhteentoimivuutta
- Yritysten omaksumismalleja, joita ohjaavat yksityisyys- ja vaatimustenmukaisuusvaatimukset

Tämä kattava lähestymistapa varmistaa, että lukijat ovat hyvin valmistautuneita navigoimaan sekä nykyisissä SLM-käyttöönoton haasteissa että tulevissa teknologisissa kehityksissä, tehden tietoisia päätöksiä, jotka vastaavat heidän organisaationsa erityisiä tarpeita ja rajoitteita.

Luku toimii sekä käytännön oppaana välittömään toteutukseen että strategisena resurssina pitkän aikavälin AI-käyttöönoton suunnitteluun, korostaen kriittistä tasapainoa kyvykkyyden, tehokkuuden ja operatiivisen erinomaisuuden välillä, joka määrittää onnistuneet SLM-käyttöönotot.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.