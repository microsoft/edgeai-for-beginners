# Luku 02: Pienten kielimallien perusteet

Tämä kattava perustason luku tarjoaa olennaisen katsauksen pieniin kielimalleihin (SLM), käsitellen teoreettisia periaatteita, käytännön toteutusstrategioita ja tuotantovalmiita käyttöönoton ratkaisuja. Luku luo kriittisen tietopohjan modernien tehokkaiden tekoälyarkkitehtuurien ymmärtämiseksi ja niiden strategiseksi hyödyntämiseksi erilaisissa laskentaympäristöissä.

## Luvun rakenne ja progressiivinen oppimiskehys

### **[Osa 1: Microsoft Phi -malliperheen perusteet](./01.PhiFamily.md)**
Avausosassa esitellään Microsoftin mullistava Phi-malliperhe, joka osoittaa, kuinka kompaktit ja tehokkaat mallit saavuttavat merkittäviä tuloksia samalla, kun laskentavaatimukset pysyvät huomattavasti pienempinä. Tämä perusosa käsittelee:

- **Suunnittelufilosofian kehitys**: Kattava katsaus Microsoftin Phi-perheen kehitykseen Phi-1:stä Phi-4:ään, korostaen vallankumouksellista "oppikirjatason" koulutusmetodologiaa ja skaalautuvuutta ennustusaikana
- **Tehokkuus ensin -arkkitehtuuri**: Yksityiskohtainen analyysi parametrien tehokkuuden optimoinnista, multimodaalisista integraatiomahdollisuuksista ja laitteistokohtaisista optimoinneista CPU-, GPU- ja reunalaitteille
- **Erikoistuneet ominaisuudet**: Syvällinen katsaus alakohtaisiin variantteihin, kuten Phi-4-mini-reasoning matemaattisiin tehtäviin, Phi-4-multimodal visio-kieli-prosessointiin ja Phi-3-Silica Windows 11 -sisäänrakennettuun käyttöön

Tämä osa luo perustavanlaatuisen periaatteen, että mallin tehokkuus ja kyvykkyys voivat kulkea käsi kädessä innovatiivisten koulutusmetodien ja arkkitehtuurin optimoinnin avulla.

### **[Osa 2: Qwen-malliperheen perusteet](./02.QwenFamily.md)**
Toinen osa siirtyy Alibaban kattavaan avoimen lähdekoodin lähestymistapaan, osoittaen, kuinka läpinäkyvät ja helposti saatavilla olevat mallit voivat saavuttaa kilpailukykyistä suorituskykyä samalla, kun käyttöönoton joustavuus säilyy. Keskeiset painopisteet sisältävät:

- **Avoimen lähdekoodin huippuosaaminen**: Kattava katsaus Qwenin kehitykseen Qwen 1.0:sta Qwen3:een, korostaen massiivista koulutusta (36 biljoonaa tokenia) ja monikielisiä kyvykkyyksiä 119 kielellä
- **Edistynyt päättelyarkkitehtuuri**: Yksityiskohtainen katsaus Qwen3:n innovatiivisiin "ajattelutila"-ominaisuuksiin, asiantuntijoiden yhdistelmäimplementaatioihin ja erikoistuneisiin variantteihin, kuten Qwen-Coder koodaukseen ja Qwen-Math matematiikkaan
- **Skaalautuvat käyttöönoton vaihtoehdot**: Syvällinen analyysi parametrialueista 0.5B:stä 235B:hen, mahdollistaen käyttöönoton mobiililaitteista yritysryhmiin

Tämä osa korostaa tekoälyteknologian demokratisointia avoimen lähdekoodin saatavuuden kautta samalla, kun kilpailukykyiset suorituskykyominaisuudet säilyvät.

### **[Osa 3: Gemma-malliperheen perusteet](./03.GemmaFamily.md)**
Kolmas osa tutkii Googlen kattavaa lähestymistapaa avoimen lähdekoodin multimodaaliseen tekoälyyn, esitellen, kuinka tutkimuslähtöinen kehitys voi tarjota helposti saatavilla olevia mutta tehokkaita tekoälyominaisuuksia. Tämä osa käsittelee:

- **Tutkimuslähtöinen innovaatio**: Kattava katsaus Gemma 3:n ja Gemma 3n:n arkkitehtuureihin, joissa on läpimurto Per-Layer Embeddings (PLE) -teknologia ja mobiilioptimoidut strategiat
- **Multimodaalinen huippuosaaminen**: Yksityiskohtainen katsaus visio-kieli-integraatioon, äänenkäsittelyominaisuuksiin ja funktiokutsutoimintoihin, jotka mahdollistavat kattavat tekoälykokemukset
- **Mobiili ensin -arkkitehtuuri**: Syvällinen analyysi Gemma 3n:n vallankumouksellisista tehokkuussaavutuksista, jotka tarjoavat tehokasta 2B-4B parametrien suorituskykyä muistijalanjäljillä, jotka ovat vain 2-3GB

Tämä osa osoittaa, kuinka huipputason tutkimus voidaan muuttaa käytännöllisiksi ja helposti saatavilla oleviksi tekoälyratkaisuiksi, jotka mahdollistavat uusia sovelluskategorioita.

### **[Osa 4: BitNET-malliperheen perusteet](./04.BitNETFamily.md)**
Neljäs osa esittelee Microsoftin vallankumouksellisen lähestymistavan 1-bittiseen kvantisointiin, joka edustaa äärimmäisen tehokkaan tekoälyn käyttöönoton kärkeä. Tämä edistynyt osa käsittelee:

- **Vallankumouksellinen kvantisointi**: Kattava katsaus 1.58-bittiseen kvantisointiin, jossa käytetään ternäärisiä painoja {-1, 0, +1}, saavuttaen 1.37x–6.17x nopeutuksia ja 55–82 % energiansäästöä
- **Optimoitu ennustuskehys**: Yksityiskohtainen katsaus bitnet.cpp-toteutukseen [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet), erikoistuneisiin ytimiin ja alustojen välisiin optimointeihin, jotka tarjoavat ennennäkemättömiä tehokkuushyötyjä
- **Kestävä tekoälyjohtajuus**: Syvällinen analyysi ympäristöhyödyistä, demokratisoiduista käyttöönoton mahdollisuuksista ja uusista sovellusskenaarioista, jotka mahdollistuvat äärimmäisen tehokkuuden avulla

Tämä osa osoittaa, kuinka vallankumoukselliset kvantisointitekniikat voivat dramaattisesti parantaa tekoälyn tehokkuutta samalla, kun kilpailukykyinen suorituskyky säilyy.

### **[Osa 5: Microsoft Mu -mallin perusteet](./05.mumodel.md)**
Viides osa tutkii Microsoftin mullistavaa Mu-mallia, joka on suunniteltu erityisesti laitekohtaisiin käyttöönottoihin Windowsissa. Tämä erikoistunut osa käsittelee:

- **Laite ensin -arkkitehtuuri**: Kattava katsaus Microsoftin erikoistuneeseen laitekohtaisen malliin, joka on sisäänrakennettu Windows 11 -laitteisiin
- **Järjestelmäintegraatio**: Yksityiskohtainen analyysi syvästä Windows 11 -integraatiosta, joka osoittaa, kuinka tekoäly voi parantaa järjestelmän toiminnallisuutta natiivin toteutuksen kautta
- **Yksityisyyttä suojaava suunnittelu**: Syvällinen katsaus offline-toimintaan, paikalliseen käsittelyyn ja yksityisyyttä korostavaan arkkitehtuuriin, joka pitää käyttäjätiedot laitteessa

Tämä osa osoittaa, kuinka erikoistuneet mallit voivat parantaa Windows 11 -käyttöjärjestelmän toiminnallisuutta samalla, kun yksityisyys ja suorituskyky säilyvät.

### **[Osa 6: Phi-Silica perusteet](./06.phisilica.md)**
Päätösosassa tarkastellaan Microsoftin Phi-Silicaa, erittäin tehokasta kielimallia, joka on sisäänrakennettu Windows 11:een Copilot+ PC:ille, joissa on NPU-laitteisto. Tämä edistynyt osa käsittelee:

- **Poikkeukselliset tehokkuusmittarit**: Kattava analyysi Phi-Silican merkittävistä suorituskykyominaisuuksista, jotka tarjoavat 650 tokenia sekunnissa vain 1.5 watin virrankulutuksella
- **NPU-optimointi**: Yksityiskohtainen katsaus erikoistuneeseen arkkitehtuuriin, joka on suunniteltu Windows 11 Copilot+ PC:iden neuroprosessointiyksiköille
- **Kehittäjäintegraatio**: Syvällinen katsaus Windows App SDK -integraatioon, kehotetekniikoihin ja parhaisiin käytäntöihin Phi-Silican toteuttamiseksi Windows 11 -sovelluksissa

Tämä osa esittelee laitteisto-optimoitujen laitekohtaisten kielimallien huippua, osoittaen, kuinka erikoistuneet malliarkkitehtuurit yhdistettynä omistettuun neuroprosessointilaitteistoon voivat tarjota poikkeuksellista tekoälysuorituskykyä Windows 11 -kuluttajalaitteilla.

## Kattavat oppimistulokset

Luvun suorittamisen jälkeen lukijat saavuttavat seuraavat taidot:

1. **Arkkitehtuurin ymmärtäminen**: Syvällinen käsitys eri SLM-suunnittelufilosofioista ja niiden vaikutuksista käyttöönoton skenaarioihin
2. **Suorituskyvyn ja tehokkuuden tasapaino**: Strategiset päätöksentekokyvyt sopivien malliarkkitehtuurien valitsemiseksi laskentarajoitteiden ja suorituskykyvaatimusten perusteella
3. **Käyttöönoton joustavuus**: Ymmärrys kompromisseista, jotka liittyvät omistettuun optimointiin (Phi), avoimen lähdekoodin saatavuuteen (Qwen), tutkimuslähtöiseen innovaatioon (Gemma) ja vallankumoukselliseen tehokkuuteen (BitNET)
4. **Tulevaisuuteen suuntautunut näkökulma**: Näkemyksiä tehokkaiden tekoälyarkkitehtuurien nousevista trendeistä ja niiden vaikutuksista seuraavan sukupolven käyttöönoton strategioihin

## Käytännön toteutuksen painopiste

Luku säilyttää vahvan käytännön suuntautumisen koko ajan, sisältäen:

- **Täydelliset koodiesimerkit**: Tuotantovalmiit toteutusesimerkit jokaiselle malliperheelle, mukaan lukien hienosäätömenetelmät, optimointistrategiat ja käyttöönoton konfiguraatiot
- **Kattava vertailu**: Yksityiskohtaiset suorituskykyvertailut eri malliarkkitehtuurien välillä, mukaan lukien tehokkuusmittarit, kyvykkyyden arvioinnit ja käyttötapausten optimointi
- **Yritystason turvallisuus**: Tuotantotason turvallisuustoteutukset, seurantastrategiat ja parhaat käytännöt luotettavaa käyttöönottoa varten
- **Kehysintegraatio**: Käytännön ohjeet integraatiosta suosittuihin kehyksiin, kuten Hugging Face Transformers, vLLM, ONNX Runtime ja erikoistuneet optimointityökalut

## Strateginen teknologiatiekartta

Luku päättyy tulevaisuuteen suuntautuneeseen analyysiin:

- **Arkkitehtuurin kehitys**: Nousevat trendit tehokkaassa mallisuunnittelussa ja optimoinnissa
- **Laitteisto-integraatio**: Edistysaskeleet erikoistuneissa tekoälykiihdyttimissä ja niiden vaikutus käyttöönoton strategioihin
- **Ekosysteemin kehitys**: Standardointipyrkimykset ja yhteentoimivuuden parannukset eri malliperheiden välillä
- **Yritysten käyttöönotto**: Strategiset näkökohdat organisaation tekoälyn käyttöönoton suunnittelussa

## Käytännön sovellusskenaariot

Jokainen osa tarjoaa kattavan katsauksen käytännön sovelluksiin:

- **Mobiili- ja reunalaskenta**: Optimoidut käyttöönoton strategiat resurssirajoitteisiin ympäristöihin
- **Yrityssovellukset**: Skaalautuvat ratkaisut liiketoimintatiedon, automaation ja asiakaspalvelun tarpeisiin
- **Koulutusteknologia**: Helposti saatavilla oleva tekoäly henkilökohtaisen oppimisen ja sisällöntuotannon tueksi
- **Globaali käyttöönotto**: Monikieliset ja kulttuurienväliset tekoälysovellukset

## Teknisen huippuosaamisen standardit

Luku korostaa tuotantovalmiita toteutuksia seuraavilla osa-alueilla:

- **Optimoinnin hallinta**: Edistyneet kvantisointitekniikat, ennustuksen optimointi ja resurssien hallinta
- **Suorituskyvyn seuranta**: Kattava mittareiden keräys, hälytysjärjestelmät ja suorituskykyanalytiikka
- **Turvallisuuden toteutus**: Yritystason turvallisuustoimenpiteet, yksityisyyden suoja ja vaatimustenmukaisuuskehykset
- **Skaalautuvuuden suunnittelu**: Horisontaaliset ja vertikaaliset skaalautumisstrategiat kasvaviin laskentatarpeisiin

Tämä perustason luku toimii olennaisena edellytyksenä edistyneille SLM-käyttöönoton strategioille, luoden sekä teoreettisen ymmärryksen että käytännön kyvykkyydet onnistuneeseen toteutukseen. Kattava sisältö varmistaa, että lukijat ovat hyvin valmistautuneita tekemään perusteltuja arkkitehtuuripäätöksiä ja toteuttamaan vankkoja, tehokkaita tekoälyratkaisuja, jotka vastaavat heidän erityisiin organisaatiotarpeisiinsa samalla, kun he valmistautuvat tuleviin teknologisiin kehityksiin.

Luku yhdistää huipputason tekoälytutkimuksen ja käytännön käyttöönoton realiteetit, korostaen, että modernit SLM-arkkitehtuurit voivat tarjota poikkeuksellista suorituskykyä samalla, kun operatiivinen tehokkuus, kustannustehokkuus ja ympäristön kestävyys säilyvät.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.