# Windows Edge AI -kehitysopas

## Johdanto

Tervetuloa Windows Edge AI -kehityksen pariin – kattavaan oppaaseen, joka auttaa sinua rakentamaan älykkäitä sovelluksia hyödyntäen Microsoftin Windows AI Foundry -alustaa ja laitteistopohjaista tekoälyä. Tämä opas on suunniteltu erityisesti Windows-kehittäjille, jotka haluavat integroida huippuluokan Edge AI -ominaisuuksia sovelluksiinsa hyödyntäen Windowsin laitteistokiihdytyksen täyttä potentiaalia.

### Windows AI:n edut

Windows AI Foundry tarjoaa yhtenäisen, luotettavan ja turvallisen alustan, joka tukee koko tekoälyn kehityskaarta – mallin valinnasta ja hienosäädöstä optimointiin ja käyttöönottoon CPU-, GPU-, NPU- ja hybridipilviarkkitehtuureissa. Tämä alusta demokratisoi tekoälyn kehityksen tarjoamalla:

- **Laitteistoabstraktio**: Saumaton käyttöönotto AMD-, Intel-, NVIDIA- ja Qualcomm-piirisarjoilla
- **Laitteistopohjainen älykkyys**: Tekoäly, joka toimii täysin paikallisella laitteistolla ja säilyttää yksityisyyden
- **Optimoitu suorituskyky**: Windows-laitteistolle valmiiksi optimoidut mallit
- **Yrityskäyttöön valmis**: Tuotantotason turvallisuus- ja vaatimustenmukaisuusominaisuudet

### Windows ML
Windows Machine Learning (ML) mahdollistaa C#-, C++- ja Python-kehittäjille ONNX AI -mallien suorittamisen paikallisesti Windows-tietokoneilla ONNX Runtime -alustan avulla, joka hallitsee automaattisesti eri laitteistojen (CPU, GPU, NPU) suorituspalveluita. [ONNX Runtime](https://onnxruntime.ai/docs/) tukee malleja PyTorch-, Tensorflow/Keras-, TFLite-, scikit-learn- ja muista kehyksistä.

![WindowsML Kaavio, joka kuvaa ONNX-mallin kulkua Windows ML:n kautta NPUs-, GPUs- ja CPUs-laitteisiin.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML tarjoaa Windows-laajuisen jaetun kopion ONNX Runtime -alustasta sekä mahdollisuuden ladata suorituspalveluita (EP) dynaamisesti.

### Miksi Windows Edge AI:lle?

**Universaali laitteistotuki**  
Windows ML optimoi automaattisesti laitteistojen suorituskyvyn koko Windows-ekosysteemissä, varmistaen, että tekoälysovelluksesi toimivat optimaalisesti riippumatta taustalla olevasta piiriteknologiasta.

**Integroitu tekoälyalusta**  
Sisäänrakennettu Windows ML -päätöksentekomoottori poistaa monimutkaiset asennusvaatimukset, jolloin kehittäjät voivat keskittyä sovelluslogiikkaan infrastruktuurin sijaan.

**Copilot+ PC -optimointi**  
Tarkoitukseen suunnitellut API:t, jotka on kehitetty erityisesti seuraavan sukupolven Windows-laitteille, joissa on omistettuja Neural Processing Unit (NPU) -yksiköitä, tarjoavat poikkeuksellisen suorituskyvyn per watt.

**Kehittäjäekosysteemi**  
Rikkaat työkalut, kuten Visual Studio -integraatio, kattava dokumentaatio ja esimerkkisovellukset, nopeuttavat kehityssyklejä.

## Oppimistavoitteet

Tämän Windows Edge AI -kehitysoppaan suorittamalla hallitset olennaiset taidot tuotantovalmiiden tekoälysovellusten rakentamiseen Windows-alustalla.

### Keskeiset tekniset taidot

**Windows AI Foundry -osaaminen**
- Ymmärrä Windows AI Foundry -alustan arkkitehtuuri ja komponentit
- Navigoi tekoälyn kehityskaarta Windows-ekosysteemissä
- Toteuta turvallisuusparhaita käytäntöjä laitteistopohjaisissa tekoälysovelluksissa
- Optimoi sovellukset eri Windows-laitteistokokoonpanoille

**API-integraatio**
- Hallitse Windows AI API:t tekstin, kuvan ja multimodaalisten sovellusten kehittämiseen
- Toteuta Phi Silica -kielimallin integrointi tekstin generointiin ja päättelyyn
- Käytä sisäänrakennettuja kuvankäsittely-API:ita tietokonenäköominaisuuksien toteuttamiseen
- Mukauta valmiiksi koulutettuja malleja LoRA (Low-Rank Adaptation) -tekniikoilla

**Foundry Local -toteutus**
- Selaa, arvioi ja ota käyttöön avoimen lähdekoodin kielimalleja Foundry Local CLI:n avulla
- Ymmärrä mallien optimointi ja kvantisointi paikallista käyttöä varten
- Toteuta offline-tekoälyominaisuuksia, jotka toimivat ilman internet-yhteyttä
- Hallitse mallien elinkaarta ja päivityksiä tuotantoympäristöissä

**Windows ML -käyttöönotto**
- Tuo mukautettuja ONNX-malleja Windows-sovelluksiin Windows ML:n avulla
- Hyödynnä automaattista laitteistokiihdytystä CPU-, GPU- ja NPU-arkkitehtuureissa
- Toteuta reaaliaikainen päätöksenteko optimaalisella resurssien käytöllä
- Suunnittele skaalautuvia tekoälysovelluksia erilaisille Windows-laiteluokille

### Sovelluskehitystaidot

**Windowsin monialustakehitys**
- Rakenna tekoälyllä tehostettuja sovelluksia .NET MAUI:n avulla universaalia Windows-käyttöönottoa varten
- Integroi tekoälyominaisuuksia Win32-, UWP- ja progressiivisiin verkkosovelluksiin
- Toteuta responsiivisia käyttöliittymiä, jotka mukautuvat tekoälyn käsittelytiloihin
- Käsittele asynkronisia tekoälytoimintoja oikeilla käyttäjäkokemusmalleilla

**Suorituskyvyn optimointi**
- Profiiloi ja optimoi tekoälyn päätöksentekosuorituskykyä eri laitteistokokoonpanoissa
- Toteuta tehokas muistinhallinta suurille kielimalleille
- Suunnittele sovelluksia, jotka mukautuvat käytettävissä oleviin laitteistoresursseihin
- Käytä välimuististrategioita usein käytettyjen tekoälytoimintojen tehostamiseen

**Tuotantovalmius**
- Toteuta kattava virheenkäsittely ja varajärjestelmät
- Suunnittele telemetria ja seuranta tekoälysovellusten suorituskyvyn arviointiin
- Käytä turvallisuusparhaita käytäntöjä paikallisten tekoälymallien tallennukseen ja suorittamiseen
- Suunnittele käyttöönotto- ja jakelustrategiat yritys- ja kuluttajasovelluksille

### Liiketoiminnallinen ja strateginen ymmärrys

**Tekoälysovellusten arkkitehtuuri**
- Suunnittele hybridialustoja, jotka optimoivat paikallisen ja pilvipohjaisen tekoälyn käsittelyn välillä
- Arvioi kompromisseja mallin koon, tarkkuuden ja päätöksentekonopeuden välillä
- Suunnittele tietovirta-arkkitehtuureja, jotka säilyttävät yksityisyyden ja mahdollistavat älykkyyden
- Toteuta kustannustehokkaita tekoälyratkaisuja, jotka skaalautuvat käyttäjien tarpeiden mukaan

**Markkinapositiointi**
- Ymmärrä Windowsin natiivien tekoälysovellusten kilpailuedut
- Tunnista käyttötapaukset, joissa laitteistopohjainen tekoäly tarjoaa ylivoimaisen käyttäjäkokemuksen
- Kehitä markkinoillemenostrategioita tekoälyllä tehostetuille Windows-sovelluksille
- Aseta sovellukset hyödyntämään Windows-ekosysteemin etuja

## Windows App SDK AI -esimerkit

Windows App SDK tarjoaa kattavia esimerkkejä tekoälyn integroinnista eri kehysten ja käyttöönoton skenaarioiden kautta. Nämä esimerkit ovat olennaisia viitteitä Windows AI -kehitysmallien ymmärtämiseen.

### Windows AI Foundry -esimerkit

| Esimerkki | Kehys | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------|----------------|-------------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API:t | Täydellinen WinUI-sovellus, joka esittelee Windows AI API:t, ARM64-optimoinnin ja paketoidun käyttöönoton |

**Keskeiset teknologiat:**
- Windows AI API:t
- WinUI 3 -kehys
- ARM64-alustan optimointi
- Copilot+ PC -yhteensopivuus
- Paketoitu sovelluksen käyttöönotto

**Edellytykset:**
- Windows 11, suositeltu Copilot+ PC
- Visual Studio 2022
- ARM64-rakennuskonfiguraatio
- Windows App SDK 1.8.1+

### Windows ML -esimerkit

#### C++-esimerkit

| Esimerkki | Tyyppi | Painopistealue | Keskeiset ominaisuudet |
|-----------|--------|----------------|-------------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Perus Windows ML | EP:n tunnistus, komentorivivaihtoehdot, mallin kääntäminen |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Kehysriippuvainen käyttöönotto | Jaettu runtime, pienempi käyttöönottojälki |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Itsenäinen käyttöönotto | Standalone-käyttöönotto, ei runtime-riippuvuuksia |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Kirjaston käyttö | WindowsML jaettu kirjasto, muistinhallinta |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet-opetusohjelma | Mallin muunnos, EP:n kääntäminen, Build 2025 -opetusohjelma |

#### C#-esimerkit

**Konsolisovellukset**

| Esimerkki | Tyyppi | Painopistealue | Keskeiset ominaisuudet |
|-----------|--------|----------------|-------------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsolisovellus | Perus C#-integraatio | Jaettujen apuvälineiden käyttö, komentorivikäyttöliittymä |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet-opetusohjelma | Mallin muunnos, EP:n kääntäminen, Build 2025 -opetusohjelma |

**GUI-sovellukset**

| Esimerkki | Kehys | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------|----------------|-------------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Työpöytä-GUI | Kuvien luokittelu WPF-käyttöliittymällä |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Perinteinen GUI | Kuvien luokittelu Windows Forms -käyttöliittymällä |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Kuvien luokittelu WinUI 3 -käyttöliittymällä |

#### Python-esimerkit

| Esimerkki | Kieli | Painopistealue | Keskeiset ominaisuudet |
|-----------|-------|----------------|-------------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Kuvien luokittelu | WinML Python -sidokset, eräkuvien käsittely |

### Esimerkkien edellytykset

**Järjestelmävaatimukset:**
- Windows 11 PC, versio 24H2 (build 26100) tai uudempi
- Visual Studio 2022, C++- ja .NET-työkuormat
- Windows App SDK 1.8.1 tai uudempi
- Python 3.10–3.13 Python-esimerkeille x64- ja ARM64-laitteilla

**Windows AI Foundry -vaatimukset:**
- Suositeltu Copilot+ PC optimaaliseen suorituskykyyn
- ARM64-rakennuskonfiguraatio Windows AI -esimerkeille
- Paketti-identiteetti vaaditaan (paketoimattomia sovelluksia ei enää tueta)

### Yleinen esimerkkityönkulku

Useimmat Windows ML -esimerkit noudattavat tätä vakiokaavaa:

1. **Ympäristön alustaminen** – Luo ONNX Runtime -ympäristö
2. **Suorituspalveluiden rekisteröinti** – Tunnista ja rekisteröi saatavilla olevat laitteistokiihdyttimet (CPU, GPU, NPU)
3. **Mallin lataaminen** – Lataa ONNX-malli, tarvittaessa käännä kohdelaitteistolle
4. **Syötteen esikäsittely** – Muunna kuvat/data mallin syöteformaattiin
5. **Päätöksenteko** – Suorita malli ja hanki ennusteet
6. **Tulosten käsittely** – Käytä softmaxia ja näytä parhaat ennusteet

### Käytetyt mallitiedostot

| Malli | Tarkoitus | Sisältyy | Huomautukset |
|-------|----------|----------|--------------|
| SqueezeNet | Kevyt kuvien luokittelu | ✅ Sisältyy | Valmiiksi koulutettu, käyttövalmis |
| ResNet-50 | Tarkka kuvien luokittelu | ❌ Vaatii muunnoksen | Käytä [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) -työkalua muunnokseen |

### Laitteistotuki

Kaikki esimerkit tunnistavat ja hyödyntävät automaattisesti saatavilla olevan laitteiston:
- **CPU** – Universaali tuki kaikilla Windows-laitteilla
- **GPU** – Automaattinen tunnistus ja optimointi saatavilla olevalle grafiikkalaitteistolle
- **NPU** – Hyödyntää Neural Processing Unit -yksiköitä tuetuilla laitteilla (Copilot+ PC:t)

## Windows AI Foundry -alustan komponentit

### 1. Windows AI API:t

Windows AI API:t tarjoavat käyttövalmiita tekoälyominaisuuksia, jotka toimivat paikallisilla malleilla ja ovat optimoitu tehokkuuden ja suorituskyvyn kannalta Copilot+ PC -laitteilla, vaatimatta monimutkaista asennusta.

#### Keskeiset API-kategoriat

**Phi Silica -kielimalli**
- Pieni mutta tehokas kielimalli tekstin generointiin ja päättelyyn
- Optimoitu reaaliaikaiseen päätöksentekoon vähäisellä virrankulutuksella
- Tukee mukautettua hienosäätöä LoRA-tekniikoilla
- Integraatio Windowsin semanttiseen hakuun ja tiedonhakuun

**Tietokonenäkö-API:t**
- **Tekstin tunnistus (OCR)**: Tunnista tekstiä kuvista tarkasti
- **Kuvan superresoluutio**: Paranna kuvien tarkkuutta paikallisilla tekoälymalleilla
- **Kuvan segmentointi**: Tunnista ja eristä tiettyjä kohteita kuvista
- **Kuvan kuvaus**: Luo yksityiskohtaisia tekstikuvauksia visuaalisesta sisällöstä
- **Kohteen poisto**: Poista ei-toivotut kohteet kuvista tekoälyllä

**Multimodaaliset ominaisuudet**
- **Näkö- ja kieli-integraatio**: Yhdistä tekstin ja kuvan ymmärrys
- **Semanttinen haku**: Mahdollista luonnollisen kielen kyselyt multimediasisällössä
- **Tiedonhaku**: Rakenna älykkäitä hakukokemuksia paikallisella datalla

### 2. Foundry Local

Foundry Local tarjoaa kehittäjille nopean pääsyn käyttövalmiisiin avoimen lähdekoodin kielimalleihin Windows-piirisarjoilla, mahdollistaen mallien
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Järjestelmäintegraatio | Matalan tason SDK:n käyttö, asynkroniset operaatiot, reqwest HTTP -asiakas |

#### Esimerkkikategoriat käyttötapauksen mukaan

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Täydellinen RAG-toteutus Semantic Kernelin, Qdrant-vektoritietokannan ja JINA-embeddingien avulla
- **Arkkitehtuuri**: Dokumenttien syöttö → Tekstin pilkkominen → Vektorien embeddingit → Samankaltaisuushaku → Kontekstuaaliset vastaukset
- **Teknologiat**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddingit, suoratoistochatin täydentäminen

**Työpöytäsovellukset**
- **electron/foundry-chat**: Tuotantovalmis chat-sovellus, jossa paikallisen/pilvimallin vaihto
- **Ominaisuudet**: Mallin valitsin, suoratoistovastaukset, virheenkäsittely, monialustainen käyttöönotto
- **Arkkitehtuuri**: Electron-pääprosessi, IPC-kommunikointi, turvalliset esilatausskriptit

**SDK-integraatioesimerkit**
- **JavaScript (Node.js)**: Perusmallin vuorovaikutus ja suoratoistovastaukset
- **Python**: OpenAI-yhteensopivan API:n käyttö asynkronisella suoratoistolla
- **Rust**: Matalan tason integraatio reqwestin ja tokion kanssa asynkronisia operaatioita varten

#### Foundry Local -esimerkkien edellytykset

**Järjestelmävaatimukset:**
- Windows 11, jossa Foundry Local asennettuna
- Node.js v16+ JavaScript/Electron-esimerkeille
- .NET 8.0+ C#-esimerkeille
- Python 3.10+ Python-esimerkeille
- Rust 1.70+ Rust-esimerkeille

**Asennus:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Esimerkkikohtainen asennus

**dotNET RAG -esimerkki:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat -esimerkki:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust -esimerkit:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Keskeiset ominaisuudet

**Mallikatalogi**
- Laaja kokoelma valmiiksi optimoituja avoimen lähdekoodin malleja
- Mallit optimoitu CPU-, GPU- ja NPU-käyttöön välittömään käyttöönottoon
- Tuki suosituimmille malliperheille, kuten Llama, Mistral, Phi, ja erikoistuneille alakohtaisille malleille

**CLI-integraatio**
- Komentoriviliittymä mallien hallintaan ja käyttöönottoon
- Automaattiset optimointi- ja kvantisointityönkulut
- Integraatio suosittuihin kehitysympäristöihin ja CI/CD-putkistoihin

**Paikallinen käyttöönotto**
- Täysin offline-toiminta ilman pilviriippuvuuksia
- Tuki mukautetuille malliformaateille ja -konfiguraatioille
- Tehokas mallipalvelu automaattisella laitteisto-optimoinnilla

### 3. Windows ML

Windows ML toimii Windowsin keskeisenä AI-alustana ja integroituina inferenssiajona, joka mahdollistaa mukautettujen mallien tehokkaan käyttöönoton laajassa Windows-laitteistoympäristössä.

#### Arkkitehtuurin edut

**Universaali laitteistotuki**
- Automaattinen optimointi AMD-, Intel-, NVIDIA- ja Qualcomm-piirisarjoille
- Tuki CPU-, GPU- ja NPU-suoritukselle läpinäkyvällä vaihdolla
- Laitteistoabstraktio, joka poistaa alustakohtaisen optimointityön

**Mallien joustavuus**
- Tuki ONNX-malliformaatille automaattisella konversiolla suosituista kehyksistä
- Mukautettujen mallien käyttöönotto tuotantotason suorituskyvyllä
- Integraatio olemassa oleviin Windows-sovellusarkkitehtuureihin

**Yritysintegraatio**
- Yhteensopivuus Windowsin turvallisuus- ja vaatimustenmukaisuuskehysten kanssa
- Tuki yrityskäyttöönotolle ja hallintatyökaluille
- Integraatio Windows-laitteiden hallinta- ja seurantajärjestelmiin

## Kehitystyönkulku

### Vaihe 1: Ympäristön asennus ja työkalujen konfigurointi

**Kehitysympäristön valmistelu**
1. Asenna Visual Studio 2022 C++- ja .NET-työkuormilla
2. Asenna Windows App SDK 1.8.1 tai uudempi
3. Konfiguroi Windows AI Foundry CLI -työkalut
4. Asenna AI Toolkit -laajennus Visual Studio Codeen
5. Ota käyttöön suorituskyvyn profilointi- ja seurantatyökalut
6. Varmista ARM64-rakennuskonfiguraatio Copilot+ PC -optimointia varten

**Esimerkkivaraston asennus**
1. Kloonaa [Windows App SDK Samples -varasto](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Siirry `Samples/WindowsAIFoundry/cs-winui`-hakemistoon Windows AI API -esimerkkejä varten
3. Siirry `Samples/WindowsML`-hakemistoon kattavia Windows ML -esimerkkejä varten
4. Tarkista [rakennusvaatimukset](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) kohdealustoille

**AI Dev Gallery -tutkimus**
- Tutki esimerkkisovelluksia ja viiteimplementaatioita
- Testaa Windows AI API:ta interaktiivisilla demonstraatioilla
- Tarkista lähdekoodi parhaiden käytäntöjen ja mallien osalta
- Tunnista relevantit esimerkit omaan käyttötapaukseesi

### Vaihe 2: Mallin valinta ja integraatio

**Vaatimusten analyysi**
- Määritä AI-ominaisuuksien toiminnalliset vaatimukset
- Aseta suorituskyvyn rajoitukset ja optimointitavoitteet
- Arvioi yksityisyyden ja turvallisuuden vaatimukset
- Suunnittele käyttöönottoarkkitehtuuri ja skaalausstrategiat

**Mallin arviointi**
- Käytä Foundry Localia avoimen lähdekoodin mallien testaamiseen käyttötapauksessasi
- Benchmarkkaa Windows AI API:t mukautettujen mallivaatimusten mukaan
- Arvioi kompromissit mallin koon, tarkkuuden ja inferenssinopeuden välillä
- Prototyyppaa integraatiolähestymistapoja valituilla malleilla

### Vaihe 3: Sovelluskehitys

**Ydinintegraatio**
- Toteuta Windows AI API -integraatio asianmukaisella virheenkäsittelyllä
- Suunnittele käyttöliittymät, jotka tukevat AI-prosessointityönkulkuja
- Toteuta välimuisti- ja optimointistrategiat mallin inferenssille
- Lisää telemetria ja seuranta AI-toiminnan suorituskyvyn mittaamiseen

**Testaus ja validointi**
- Testaa sovelluksia eri Windows-laitteistokonfiguraatioilla
- Vahvista suorituskykymittarit eri kuormitustilanteissa
- Toteuta automatisoitu testaus AI-toiminnallisuuden luotettavuuden varmistamiseksi
- Suorita käyttäjäkokemustestaus AI-parannettujen ominaisuuksien kanssa

### Vaihe 4: Optimointi ja käyttöönotto

**Suorituskyvyn optimointi**
- Profiloi sovelluksen suorituskyky kohdelaitteistokonfiguraatioilla
- Optimoi muistin käyttö ja mallin latausstrategiat
- Toteuta mukautuva käyttäytyminen käytettävissä olevien laitteistokapasiteettien mukaan
- Hienosäädä käyttäjäkokemus eri suorituskykytilanteisiin

**Tuotantokäyttöönotto**
- Pakkaa sovellukset asianmukaisilla AI-malliriippuvuuksilla
- Toteuta päivitysmekanismit malleille ja sovelluslogiikalle
- Konfiguroi seuranta ja analytiikka tuotantoympäristöihin
- Suunnittele käyttöönotto- ja jakelustrategiat yritys- ja kuluttajakäyttöön

## Käytännön toteutusesimerkit

### Esimerkki 1: Älykäs dokumenttien käsittelysovellus

Rakenna Windows-sovellus, joka käsittelee dokumentteja useiden AI-ominaisuuksien avulla:

**Käytetyt teknologiat:**
- Phi Silica dokumenttien tiivistämiseen ja kysymys-vastaus-toimintoihin
- OCR-API:t tekstin poimintaan skannatuista dokumenteista
- Kuvan kuvaus-API:t kaavioiden ja diagrammien analysointiin
- Mukautetut ONNX-mallit dokumenttien luokitteluun

**Toteutustapa:**
- Suunnittele modulaarinen arkkitehtuuri, jossa on liitettävät AI-komponentit
- Toteuta asynkroninen käsittely suurille dokumenttierille
- Lisää etenemisen indikaattorit ja peruutustuki pitkäkestoisille operaatioille
- Sisällytä offline-ominaisuus arkaluontoisten dokumenttien käsittelyyn

### Esimerkki 2: Vähittäiskaupan varastonhallintajärjestelmä

Luo AI-pohjainen varastonhallintajärjestelmä vähittäiskaupan sovelluksiin:

**Käytetyt teknologiat:**
- Kuvan segmentointi tuotteiden tunnistamiseen
- Mukautetut visiomallit brändi- ja kategoriatunnistukseen
- Foundry Local -käyttöönotto erikoistuneille vähittäiskaupan kielimalleille
- Integraatio olemassa oleviin POS- ja varastojärjestelmiin

**Toteutustapa:**
- Rakenna kameraintegraatio reaaliaikaiseen tuoteskannaukseen
- Toteuta viivakoodin ja visuaalisen tuotetunnistuksen ominaisuudet
- Lisää luonnollisen kielen varastokyselyt paikallisten kielimallien avulla
- Suunnittele skaalautuva arkkitehtuuri monikauppakäyttöönottoa varten

### Esimerkki 3: Terveydenhuollon dokumentointiassistentti

Kehitä yksityisyyttä säilyttävä terveydenhuollon dokumentointityökalu:

**Käytetyt teknologiat:**
- Phi Silica lääketieteellisten muistiinpanojen luomiseen ja kliiniseen päätöksentukeen
- OCR käsinkirjoitettujen lääketieteellisten asiakirjojen digitalisointiin
- Mukautetut lääketieteelliset kielimallit, jotka otetaan käyttöön Windows ML:n kautta
- Paikallinen vektorivarasto lääketieteellisen tiedon hakua varten

**Toteutustapa:**
- Varmista täysin offline-toiminta potilaan yksityisyyden suojaamiseksi
- Toteuta lääketieteellisen terminologian validointi ja ehdotukset
- Lisää auditointiloki sääntelyvaatimusten noudattamiseksi
- Suunnittele integraatio olemassa oleviin sähköisiin potilastietojärjestelmiin

## Suorituskyvyn optimointistrategiat

### Laitteistotietoinen kehitys

**NPU-optimointi**
- Suunnittele sovellukset hyödyntämään NPU-ominaisuuksia Copilot+ PC:llä
- Toteuta sujuva siirtyminen GPU/CPU:lle laitteilla, joilla ei ole NPU:ta
- Optimoi malliformaatit NPU-spesifiseen kiihdytykseen
- Seuraa NPU:n käyttöä ja lämpöominaisuuksia

**Muistin hallinta**
- Toteuta tehokkaat mallin lataus- ja välimuististrategiat
- Käytä muistimappauksia suurille malleille käynnistysajan lyhentämiseksi
- Suunnittele muistitehokkaita sovelluksia resurssirajoitteisille laitteille
- Toteuta mallin kvantisointi muistin optimointia varten

**Akkutehokkuus**
- Optimoi AI-toiminnot mahdollisimman vähäiseen virrankulutukseen
- Toteuta mukautuva käsittely akun tilan perusteella
- Suunnittele tehokas taustakäsittely jatkuville AI-toiminnoille
- Käytä virran profilointityökaluja energian käytön optimointiin

### Skaalautuvuuden huomioiminen

**Monisäikeisyys**
- Suunnittele säikeiden turvalliset AI-toiminnot rinnakkaiseen käsittelyyn
- Toteuta tehokas työnjako käytettävissä olevien ytimien kesken
- Käytä async/await-malleja ei-blokkaaviin AI-toimintoihin
- Suunnittele säikeiden optimointi eri laitteistokonfiguraatioille

**Välimuististrategiat**
- Toteuta älykäs välimuisti usein käytetyille AI-toiminnoille
- Suunnittele välimuistin mitätöintistrategiat mallipäivityksille
- Käytä pysyvää välimuistia kalliille esikäsittelytoiminnoille
- Toteuta hajautettu välimuisti monikäyttäjätilanteisiin

## Turvallisuus ja yksityisyys parhaat käytännöt

### Tietosuoja

**Paikallinen käsittely**
- Varmista, että arkaluontoiset tiedot eivät koskaan poistu paikalliselta laitteelta
- Toteuta turvallinen tallennus AI-malleille ja väliaikaisille tiedoille
- Käytä Windowsin turvallisuusominaisuuksia sovelluksen hiekkalaatikointiin
- Sovella salaus tallennettuihin malleihin ja välituloksiin

**Mallin turvallisuus**
- Vahvista mallin eheys ennen latausta ja suorittamista
- Toteuta turvalliset mallipäivitysmekanismit
- Käytä allekirjoitettuja malleja manipuloinnin estämiseksi
- Sovella käyttöoikeusvalvontaa mallitiedostoille ja konfiguraatioille

### Vaatimustenmukaisuuden huomioiminen

**Sääntelyyn mukautuminen**
- Suunnittele sovellukset GDPR-, HIPAA- ja muiden sääntelyvaatimusten mukaisiksi
- Toteuta auditointiloki AI-päätöksentekoprosesseille
- Tarjoa läpinäkyvyysominaisuuksia AI:n tuottamille tuloksille
- Mahdollista käyttäjän hallinta AI:n tietojen käsittelyyn

**Yritysturvallisuus**
- Integroi Windowsin yritysturvallisuuspolitiikkoihin
- Tue hallittua käyttöönottoa yrityksen hallintatyökalujen kautta
- Toteuta roolipohjainen käyttöoikeusvalvonta AI-ominaisuuksille
- Tarjoa hallinnolliset valvontatyökalut AI-toiminnallisuudelle

## Vianetsintä ja virheenkorjaus

### Yleiset kehityshaasteet

**Rakennuskonfiguraatio-ongelmat**
- Varmista ARM64-alustakonfiguraatio Windows AI API -esimerkeille
- Tarkista Windows App SDK -version yhteensopivuus (vaaditaan 1.8.1+)
- Varmista, että paketin identiteetti on oikein konfiguroitu (vaaditaan Windows AI API:ille)
- Vahvista, että rakennustyökalut tukevat kohdekehysversiota

**Mallin latausongelmat**
- Vahvista ONNX-mallin yhteensopivuus Windows ML:n kanssa
- Tarkista mallin tiedostojen eheys ja formaattivaatimukset
- Vahvista laitteistokapasiteettivaatimukset tiettyjä malleja varten
- Korjaa muistiallokaatio-ongelmat mallin latauksen aikana
- Varmista suoritustarjoajan rekisteröinti laitteistokiihdytykselle

**Käyttöönoton tilavaihtoehdot**
- **Itse sisällytetty tila**: Täysin tuettu suuremmalla käyttöönoton koolla
- **Kehysriippuvainen tila**: Pienempi jalanjälki, mutta vaatii jaetun ajonaikaisen ympäristön
- **Pakkaamattomat sovellukset**: Ei enää tuettu Windows AI API:ille
- Käytä `dotnet run -p:Platform=ARM64 -p:SelfContained=true` itse sisällytetyssä ARM64-käyttöönotossa

**Suorituskykyongelmat**
- Profiloi sovelluksen suorituskyky eri laitteistokonfiguraatioilla
- Tunnista pullonkaulat AI-käsittelyputkistoissa
- Optimoi datan esikäsittely- ja jälkikäsittelytoiminnot
- Tote
- [Windows ML Yleiskatsaus](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK Järjestelmävaatimukset](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK Kehitysympäristön Määrittäminen](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Esimerkkirepositoriot ja Koodi
- [Windows App SDK Esimerkit - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Esimerkit - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Inference Esimerkit](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Esimerkkirepositorio](https://github.com/microsoft/WindowsAppSDK-Samples)

### Kehitystyökalut
- [AI Toolkit Visual Studio Codea varten](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Galleria](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Esimerkit](https://learn.microsoft.com/windows/ai/samples/)
- [Mallin Muunnostyökalut](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tekninen Tuki
- [Windows ML Dokumentaatio](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentaatio](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentaatio](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Ilmoita Ongelmista - Windows App SDK Esimerkit](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Yhteisö ja Tuki
- [Windows Kehittäjäyhteisö](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blogi](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Koulutus](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tämä opas on suunniteltu kehittymään nopeasti etenevän Windows AI -ekosysteemin mukana. Säännölliset päivitykset varmistavat, että sisältö pysyy ajan tasalla uusimpien alustan ominaisuuksien ja kehityskäytäntöjen kanssa.*

[08. Käytännön Harjoituksia Microsoft Foundry Local - Täydellinen Kehittäjätyökalupakki](../Module08/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.