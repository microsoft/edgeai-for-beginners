# Windows Edge AI -kehitysohje

## Johdanto

Tervetuloa Windows Edge AI -kehitykseen – kokonaisvaltaiseen oppaaseesi älykkäiden sovellusten rakentamiseen, jotka hyödyntävät paikallisen laitteen tekoälyä Microsoftin Windows AI Foundry -alustan avulla. Tämä opas on suunnattu erityisesti Windows-kehittäjille, jotka haluavat integroida huipputason Edge AI -ominaisuudet sovelluksiinsa hyödyntäen samalla koko Windows-laitteiston tehostusta.

### Windows AI -etu

Windows AI Foundry edustaa yhtenäistä, luotettavaa ja turvallista alustaa, joka tukee koko tekoälyn kehitysprosessia – mallin valinnasta ja hienosäädöstä optimointiin ja käyttöönottoon CPU-, GPU-, NPU- ja hybridi-pilviarkkitehtuureissa. Tämä alusta demokratisoi tekoälyn kehityksen tarjoamalla:

- **Laitteistovälitys**: Saumaton käyttöönotto AMD:n, Intelin, NVIDIA:n ja Qualcommin piireillä
- **Paikallinen älykkyys**: Yksityisyyttä suojaava tekoäly, joka toimii kokonaan paikallisessa laitteistossa
- **Optimoitu suorituskyky**: Mallit valmiiksi optimoituina Windowsin laitteistokonfiguraatioille
- **Yritystason valmius**: Tuotantoluokan turvallisuus- ja vaatimustenmukaisuustoiminnot

### Windows ML
Windows Machine Learning (ML) mahdollistaa C#, C++ ja Python -kehittäjille ONNX- tekoälymallien ajamisen paikallisesti Windows-tietokoneissa ONNX Runtime -alustan kautta, automaattisella suoritusympäristön hallinnalla eri laitteistoille (CPU:t, GPU:t, NPU:t). [ONNX Runtime](https://onnxruntime.ai/docs/) tukee malleja PyTorchista, Tensorflow/Kerasista, TFLitestä, scikit-learnistä ja muista kehyksistä.


![WindowsML Kaavio, joka havainnollistaa ONNX-mallin kulkua Windows ML:n kautta NPUIhin, GPU:hin ja CPU:ihin.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML tarjoaa yhteisen koko Windows -ympäristön katveisen ONNX Runtime -kopion sekä mahdollisuuden ladata suorituspalveluita (EP) dynaamisesti.

### Miksi Windows Edge AI:lle?

**Universaali laitteistotuki**
Windows ML tarjoaa automaattisen laitteistojen optimoinnin koko Windows-ekosysteemissä, varmistaen tekoälysovellustesi optimaalisen suorituskyvyn riippumatta taustalla olevasta piirikokoonpanosta.

**Integroitu tekoälyajoympäristö**
Sisäänrakennettu Windows ML -päättelymoottori poistaa monimutkaiset käyttöönotto-vaatimukset, jolloin kehittäjät voivat keskittyä sovelluslogiikkaan infrastruktuurihuolien sijaan.

**Copilot+ PC -optimointi**
Tarkoitukseen suunnitellut rajapinnat nimenomaan seuraavan sukupolven Windows-laitteille, joissa on omistetut neuroprosessorit (NPU), jotka tarjoavat poikkeuksellisen suorituskyvyn wattia kohti.

**Kehittäjäekosysteemi**
Runsaat työkalut, mukaan lukien Visual Studion integraatio, kattava dokumentaatio ja esimerkkisovellukset, jotka nopeuttavat kehityssyklejä.

## Oppimistavoitteet

Täydentämällä tämän Windows Edge AI -kehitysohjeen hallitset olennaiset taidot tuotantovalmiiden tekoälysovellusten rakentamiseen Windows-alustalla.

### Keskeiset tekniset osaamisalueet

**Windows AI Foundry -hallinta**
- Ymmärrä Windows AI Foundryn alustan arkkitehtuuri ja komponentit
- Navigoi koko tekoälykehityksen elinkaaren Windows-ekosysteemissä
- Ota käyttöön turvallisuuden parhaat käytännöt paikallisissa tekoälysovelluksissa
- Optimoi sovellukset erilaisille Windows-laitteistokonfiguraatioille

**API-integraatio-osaaminen**
- Hallitse Windows AI API:t tekstin, kuvantunnistuksen ja multimodaalisovellusten osalta
- Toteuta Phi Silica -kielimallin integraatio tekstin generointiin ja päättelyyn
- Ota käyttöön tietokonenäön ominaisuudet sisäänrakennettujen kuvan käsittely-API:en avulla
- Mukauta esikoulutettuja malleja LoRA (Low-Rank Adaptation) -tekniikoilla

**Foundry Local -käyttöönotto**
- Selaa, arvioi ja ota käyttöön avoimen lähdekoodin kielimalleja Foundry Local CLI:n avulla
- Ymmärrä mallien optimointi ja kvantisointi paikallisessa käyttöönotossa
- Toteuta offline-tekoälyominaisuudet ilman internet-yhteyttä
- Hallinnoi mallien elinkaaria ja päivityksiä tuotantoympäristöissä

**Windows ML -käyttöönotto**
- Vie mukautetut ONNX-mallit Windows-sovelluksiin Windows ML:n avulla
- Hyödynnä automaattista laitteistokiihdytystä CPU-, GPU- ja NPU-arkkitehtuureissa
- Toteuta reaaliaikainen päättely optimaalisella resurssien käytöllä
- Suunnittele skaalautuvia tekoälysovelluksia monenlaisiin Windows-laitteisiin

### Sovelluskehitystaidot

**Monialustainen Windows-kehitys**
- Rakenna tekoälyllä tehostettuja sovelluksia .NET MAUI:n avulla universaaliin Windows-käyttöönottoon
- Integroidu tekoälyominaisuudet Win32-, UWP- ja progressiivisiin web-sovelluksiin
- Toteuta reagoivat käyttöliittymäsuunnitelmat, jotka mukautuvat tekoälyn prosessointitiloihin
- Käsittele asynkronisia tekoälytoimintoja asianmukaisilla käyttökokemuksen kaavoilla

**Suorituskyvyn optimointi**
- Profiloi ja optimoi tekoälypäättelyn suorituskykyä eri laitteistokonfiguraatioissa
- Toteuta tehokas muistinhallinta suurille kielimalleille
- Suunnittele sovelluksia, jotka degradeeruvat sujuvasti käytettävissä olevien laitteistoresurssien mukaan
- Sovella välimuististrategioita usein käytetyille tekoälytoiminnoille

**Tuotantovalmius**
- Toteuta kattava virheenkäsittely ja varatoimenpiteet
- Suunnittele telemetria ja valvonta tekoälysovelluksen suorituskyvylle
- Sovella turvallisuuden parhaita käytäntöjä paikallisen tekoälymallin tallennukseen ja käyttöön
- Suunnittele käyttöönotto strategiat yritys- ja kuluttajasovelluksille

### Liiketoiminta- ja strateginen ymmärrys

**Tekoälysovellusten arkkitehtuuri**
- Suunnittele hybridiarkkitehtuurit, jotka optimoivat paikallisen ja pilvitekoälyn käsittelyn välillä
- Arvioi kompromisseja mallin koon, tarkkuuden ja päättelynopeuden välillä
- Suunnittele tietovirta-arkkitehtuurit, jotka säilyttävät yksityisyyden mahdollistaen samalla älykkyyden
- Toteuta kustannustehokkaita tekoälyratkaisuja, jotka skaalautuvat käyttäjien tarpeiden mukaan

**Markkina-asema**
- Ymmärrä Windows-natiivien tekoälysovellusten kilpailuedut
- Tunnista käyttötapaukset, joissa paikallinen tekoäly tarjoaa ylivoimaiset käyttäjäkokemukset
- Kehitä markkinoille tulon strategioita tekoälyllä rikastetuille Windows-sovelluksille
- Aseta sovellukset hyödyntämään Windows-ekosysteemin etuja

## Windows App SDK:n tekoälyn esimerkit

Windows App SDK tarjoaa kattavat esimerkit, jotka demonstroivat tekoälyn integrointia useissa kehyksissä ja käyttöönotto-tilanteissa. Nämä esimerkit ovat olennaisia lähteitä Windows AI -kehitysmallien ymmärtämisessä.

### Windows AI Foundry -esimerkit

| Esimerkki | Kehys | Keskittymisalue | Keskeiset ominaisuudet |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API -integraatio | Täydellinen WinUI-sovellus, joka demonstroi Windows AI -rajapintoja, ARM64-optimointia, pakattua käyttöönottoa |

**Keskeiset teknologiat:**
- Windows AI API:t
- WinUI 3 -kehys
- ARM64-alustan optimointi
- Copilot+ PC -yhteensopivuus
- Pakattu sovelluskäyttöönotto

**Ennakkovaatimukset:**
- Windows 11 Copilot+ PC suositeltu
- Visual Studio 2022
- ARM64-rakennuskonfiguraatio
- Windows App SDK 1.8.1+

### Windows ML -esimerkit

#### C++-esimerkit

| Esimerkki | Tyyppi | Keskittymisalue | Keskeiset ominaisuudet |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Perus Windows ML | EP-palveluiden löytö, komentorivivaihtoehdot, mallikäännös |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Kehyskäyttöönotto | Jaettu ajoaika, pienempi käyttöönotto |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konsolisovellus | Itsenäinen käyttöönotto | Itsenäinen käyttöönotto, ei ajonaikaisia riippuvuuksia |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Kirjaston käyttö | WindowsML jaettu kirjasto, muistinhallinta |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet-opas | Mallin konversio, EP-käännös, Build 2025 -opas |

#### C#-esimerkit

**Konsolisovellukset**

| Esimerkki | Tyyppi | Keskittymisalue | Keskeiset ominaisuudet |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konsolisovellus | Perus C#-integraatio | Jaetut apuohjelmat, komentorivikäyttöliittymä |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet-opas | Mallin konversio, EP-käännös, Build 2025 -opas |

**GUI-sovellukset**

| Esimerkki | Kehys | Keskittymisalue | Keskeiset ominaisuudet |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Pöytäkoneen GUI | Kuvien luokittelu WPF-käyttöliittymällä |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Perinteinen GUI | Kuvien luokittelu Windows Forms -käyttöliittymällä |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Kuvien luokittelu WinUI 3 -käyttöliittymällä |

#### Python-esimerkit

| Esimerkki | Kieli | Keskittymisalue | Keskeiset ominaisuudet |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Kuvien luokittelu | WinML Python-liitännät, eräkuvan käsittely |

### Esimerkkien ennakkovaatimukset

**Järjestelmävaatimukset:**
- Windows 11 -tietokone versio 24H2 (build 26100) tai uudempi
- Visual Studio 2022 C++- ja .NET-työkuormilla
- Windows App SDK 1.8.1 tai uudempi
- Python 3.10-3.13 Python-esimerkeille x64- ja ARM64-laitteissa

**Windows AI Foundryyn liittyen:**
- Copilot+ PC suositeltu optimaaliseen suorituskykyyn
- ARM64-rakennuskonfiguraatio Windows AI -esimerkkeihin
- Paketin tunnuspaketti vaaditaan (pakkaamattomia sovelluksia ei enää tueta)

### Yleinen esimerkkityönkulku

Useimmat Windows ML -esimerkit seuraavat tätä vakiokaavaa:

1. **Ympäristön alustaminen** - Luo ONNX Runtime -ympäristö
2. **Suorituspalveluiden rekisteröinti** - Löydä ja rekisteröi käytettävissä olevat laitteistokiihdyttimet (CPU, GPU, NPU)
3. **Mallin lataus** - Lataa ONNX-malli, valinnaisesti käännä kohdelaitteistolle
4. **Esikäsittele syöte** - Muunna kuvat/data mallin syöteformaattiin
5. **Suorita päättely** - Käynnistä malli ja saa ennusteet
6. **Käsittele tulokset** - Käytä softmax-toimintoa ja näytä tärkeimmät ennusteet

### Käytetyt mallifailit

| Malli | Tarkoitus | Mukana | Huomautukset |
|-------|---------|----------|-------|
| SqueezeNet | Kevyt kuvien luokittelu | ✅ Mukana | Valmiiksi koulutettu, käyttövalmis |
| ResNet-50 | Korkean tarkkuuden kuvien luokittelu | ❌ Tarvitsee konversion | Käytä [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) -työkalua konversioon |

### Laitteistotuki

Kaikki esimerkit tunnistavat ja käyttävät automaattisesti käytettävissä olevaa laitteistoa:
- **CPU** - Universalituki kaikissa Windows-laitteissa
- **GPU** - Automaattinen tunnistus ja optimointi käytettävissä olevalle grafiikkalaitteistolle
- **NPU** - Hyödyntää neuroprosessoriyksiköitä tuetuissa laitteissa (Copilot+ PC:t)

## Windows AI Foundry -alustan komponentit

### 1. Windows AI API:t

Windows AI API:t tarjoavat käyttövalmiita tekoälyominaisuuksia paikallisten mallien avulla, optimoituna tehokkuuden ja suorituskyvyn kannalta Copilot+ PC -laitteilla, ilman merkittäviä käyttöönotto-vaatimuksia.

#### Keskeiset API-luokat

**Phi Silica -kielimalli**
- Pieni mutta tehokas kielimalli tekstin generointiin ja päättelyyn
- Optimoitu reaaliaikaiseen päättelyyn vähäisellä virrankulutuksella
- Tuki mukautetulle hienosäädölle LoRA-tekniikoilla
- Integraatio Windowsin semanttiseen hakuun ja tiedonhakutoimintoihin

**Tietokonenäkö API:t**
- **Tekstin tunnistus (OCR)**: Poimi tekstiä kuvista korkealla tarkkuudella
- **Kuvien superresoluutio**: Skaalaa kuvia paikallisten tekoälymallien avulla
- **Kuvien segmentointi**: Tunnista ja eristä tiettyjä kohteita kuvista
- **Kuvauksen generointi**: Luo yksityiskohtaisia tekstikuvauksia visuaalisesta sisällöstä
- **Kohteen poisto**: Poista ei-toivotut kohteet kuvista tekoälyllä toteutetulla inpaint-tekniikalla

**Multimodaaliset ominaisuudet**
- **Näön ja kielen integraatio**: Yhdistä tekstin ja kuvan ymmärrys
- **Semanttinen haku**: Mahdollista luonnollisen kielen kyselyt multimediasisällössä
- **Tiedonhaku**: Luo älykkäitä hakukokemuksia paikallisten tietojen avulla

### 2. Foundry Local

Foundry Local tarjoaa kehittäjille nopean pääsyn käyttövalmiisiin avoimen lähdekoodin kielimalleihin Windows-piireillä, tarjoten mahdollisuuden selata, testata, vuorovaikuttaa ja ottaa malleja käyttöön paikallisissa sovelluksissa.

#### Foundry Local -esimerkkisovellukset

[Foundry Local -varasto](https://github.com/microsoft/Foundry-Local/tree/main/samples) tarjoaa kattavia esimerkkejä eri ohjelmointikielillä ja kehyksillä, esitellen erilaisia integraatiomalleja ja käyttötapauksia.

| Esimerkki | Kieli/Kehys | Keskittymisalue | Keskeiset ominaisuudet |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG-toteutus | Semantic Kernel -integraatio, Qdrant-vektorikauppa, JINA-upotukset, dokumenttien tuonti, reaaliaikainen keskustelu |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Pöytäkoneen chat-sovellus | Monialustainen keskustelu, paikallisen ja pilvimallin vaihto, OpenAI SDK -integraatio, reaaliaikainen suoratoisto |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Perusintegraatio | Yksinkertainen SDK:n käyttö, mallin alustus, peruskeskustelutoiminnot |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Perusintegraatio | Python SDK:n käyttö, suoratoistovastaukset, OpenAI-yhteensopiva API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Järjestelmäintegraatio | Matalan tason SDK:n käyttö, asynkroniset operaatiot, reqwest HTTP-asiakas |

#### Näytekategoriat käyttötapauksen mukaan

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Täydellinen RAG-toteutus Semantic Kernelillä, Qdrant-vektoritietokannalla ja JINA-upotuksilla
- **Arkkitehtuuri**: Dokumenttien syöttö → Tekstin pilkkominen → Vektoriupotukset → Samankaltaisuushaku → Kontekstia ymmärtävät vastaukset
- **Teknologiat**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX -upotukset, suoratoistava chat-kompletio

**Työpöytäsovellukset**
- **electron/foundry-chat**: Tuotantovalmiiksi asti kehitetty chat-sovellus paikallisella/pilvimallin vaihdolla
- **Ominaisuudet**: Mallin valitsin, suoratoistavat vastaukset, virheenkäsittely, monialustainen käyttöönotto
- **Arkkitehtuuri**: Electron-pääprosessi, IPC-viestintä, turvalliset preload-skriptit

**SDK-integraatioesimerkit**
- **JavaScript (Node.js)**: Peruskäyttö mallin kanssa ja suoratoistavat vastaukset
- **Python**: OpenAI-yhteensopivan API:n käyttö asynkronisella suoratoistolla
- **Rust**: Matalan tason integraatio reqwest- ja tokio-kirjastoilla asynkronisiin operaatioihin

#### Foundry Local -näytteiden edellytykset

**Järjestelmävaatimukset:**
- Windows 11, johon on asennettu Foundry Local
- Node.js v16+ JavaScript/Electron-näytteitä varten
- .NET 8.0+ C#-näytteitä varten
- Python 3.10+ Python-näytteitä varten
- Rust 1.70+ Rust-näytteitä varten

**Asennus:**
```powershell
# Asenna Foundry Local
winget install Microsoft.FoundryLocal

# Vahvista asennus
foundry --version
foundry model list
```

#### Näytekohtekohtaisten asetusten tekeminen

**dotNET RAG -näyte:**
```powershell
# Asenna tarvittavat paketit NuGetin kautta
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Käynnistä Qdrantin vektoritietokanta
docker run -p 6333:6333 qdrant/qdrant

# Suorita Jupyter-muistikirja
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat -näyte:**
```powershell
# Aseta ympäristömuuttujat pilvihakua varten
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Asenna riippuvuudet ja suorita
npm install
npm start
```

**JavaScript/Python/Rust-näytteet:**
```powershell
# Lataa malli (esimerkki phi-3.5-mini)
foundry model run phi-3.5-mini

# Suorita vastaava esimerkki
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Keskeiset ominaisuudet

**Malliluettelo**
- Laaja kokoelma valmiiksi optimoituja avoimen lähdekoodin malleja
- Mallit optimoitu CPU:ille, GPU:ille ja NPU:ille välittömään käyttöönottoon
- Tuki suosituimmille malliperheille kuten Llama, Mistral, Phi ja erikoistuneille toimialamalleille

**CLI-integraatio**
- Komentoriviliittymä mallien hallintaan ja käyttöönottoon
- Automatisoidut optimointi- ja kvantisointityönkulut
- Integrointi suosittuihin kehitysympäristöihin ja CI/CD-putkiin

**Paikallinen käyttöönotto**
- Täysi offline-toiminta ilman pilviriippuvuuksia
- Tuki räätälöidyille malliformaateille ja asetuksille
- Tehokas mallien tarjoaminen automaattisella laitteisto-optimoinnilla

### 3. Windows ML

Windows ML toimii Windowsin ydintekoälyalustana ja sulautettuna inferenssiympäristönä, joka mahdollistaa kehittäjille räätälöityjen mallien tehokkaan käyttöönoton laajalla Windows-laitteistokentällä.

#### Arkkitehtuurin edut

**Yleinen laitteistotuki**
- Automaattinen optimointi AMD:n, Intelin, NVIDIA:n ja Qualcommin piireille
- Tuki CPU:n, GPU:n ja NPU:n suorittamiseen läpinäkyvällä vaihdolla
- Laitteistoabstrahointi, joka poistaa alustakohtaisen optimointityön tarpeen

**Mallien joustavuus**
- Tuki ONNX-malliformaatille automaattisella muunnoksella suosituista kehyksistä
- Räätälöity mallien käyttö tuotantotason suorituskyvyllä
- Integraatio olemassa oleviin Windows-sovellusarkkitehtuureihin

**Yritysintegraatio**
- Yhteensopiva Windowsin turvallisuus- ja vaatimustenmukaisuuden puitteiden kanssa
- Tuki yrityskäyttöön ja hallintatyökaluille
- Integraatio Windowsin laitehallinta- ja valvontajärjestelmien kanssa

## Kehitystyön työnkulku

### Vaihe 1: Ympäristön valmistelu ja työkalujen konfigurointi

**Kehitysympäristön valmistelu**
1. Asenna Visual Studio 2022 C++- ja .NET-työkuormilla
2. Asenna Windows App SDK 1.8.1 tai uudempi
3. Konfiguroi Windows AI Foundry CLI -työkalut
4. Ota käyttöön AI Toolkit -laajennus Visual Studio Codeen
5. Perusta suorituskyvyn profilointi- ja valvontatyökalut
6. Varmista ARM64-käännösasetus Copilot+ PC -optimointia varten

**Näytearkiston valmistelu**
1. Kopioi [Windows App SDK Samples -varasto](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Siirry kansioon `Samples/WindowsAIFoundry/cs-winui` Windows AI API -esimerkkien löytämiseksi
3. Siirry kansioon `Samples/WindowsML` laajojen Windows ML -esimerkkien löytämiseksi
4. Tutki [rakennusvaatimukset](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) valitsemillesi alustoille

**AI Dev Galleryn tutkiminen**
- Tutki näytesovelluksia ja viitesuorituksia
- Testaa Windows AI API:ita interaktiivisten demonstraatioiden kautta
- Tarkastele lähdekoodia parhaiden käytäntöjen ja mallien löytämiseksi
- Löydä soveltuvia näytteitä omaan käyttötapaukseesi

### Vaihe 2: Mallin valinta ja integrointi

**Vaatimusmäärittely**
- Määrittele tekoälytoimintojen toiminnalliset vaatimukset
- Aseta suorituskyvyn rajoitteet ja optimointitavoitteet
- Arvioi tietosuoja- ja turvallisuusvaatimukset
- Suunnittele käyttöönottoarkkitehtuuri ja skaalausstrategiat

**Mallin arviointi**
- Käytä Foundry Localia testataksesi avoimen lähdekoodin malleja käyttötapaukseesi
- Vertaa Windows AI API:ita omiin mallivaatimuksiin
- Arvioi mallin koon, tarkkuuden ja inferenssinopeuden kompromisseja
- Prototyppaa integrointitapoja valituilla malleilla

### Vaihe 3: Sovelluskehitys

**Ydinintegraatio**
- Toteuta Windows AI API -integraatio asianmukaisella virheenkäsittelyllä
- Suunnittele käyttöliittymät, jotka tukevat tekoälyprosessointia
- Toteuta välimuistit ja optimointistrategiat mallin inferenssille
- Lisää käyttötilasto- ja valvontatoiminnot tekoälyn suoritustehon seurantaan

**Testaus ja validointi**
- Testaa sovelluksia eri Windows-laitteistokonfiguraatioissa
- Varmista suorituskykymittareiden toteutuminen eri kuormitustilanteissa
- Toteuta automaattiset testit tekoälytoimintojen luotettavuudelle
- Tee käyttökokemuksen testauksia tekoälyllä parannetuilla ominaisuuksilla

### Vaihe 4: Optimointi ja käyttöönotto

**Suorituskyvyn optimointi**
- Tee sovelluksen suorituskyvyn profilointi kohdelaitteilla
- Optimoi muistin käyttö ja mallin latausstrategiat
- Toteuta laitteisto-ominaisuuksiin mukautuva toiminta
- Hienosäädä käyttäjäkokemusta eri suorituskykytasoilla

**Tuotantokäyttöönotto**
- Pakkaa sovellukset asianmukaisine tekoälymalliriippuvuuksineen
- Toteuta päivitysmenettelyt malleille ja sovelluslogiikalle
- Konfiguroi valvonta ja analytiikka tuotantoympäristöihin
- Suunnittele käyttöönoton vaiheistus yritys- ja kuluttajakohderyhmiin

## Käytännön toteutusesimerkkejä

### Esimerkki 1: Älykäs dokumenttien käsittelysovellus

Rakenna Windows-sovellus, joka käsittelee dokumentteja käyttäen useita tekoälyominaisuuksia:

**Käytetyt teknologiat:**
- Phi Silica dokumenttien tiivistykseen ja kysymys-vastaus-toimintoihin
- OCR API:t tekstin poimintaan skannatuista dokumenteista
- Kuvauksen API:t kaavioiden ja diagrammien analysointiin
- Räätälöidyt ONNX-mallit dokumenttien luokitteluun

**Toteutustapa:**
- Suunnittele modulaarinen arkkitehtuuri liitettävinä tekoälykomponentteina
- Toteuta asynkroninen käsittely suurille dokumenttipaketeille
- Lisää etenemisindikaattorit ja peruutustuki pitkille operaatioille
- Sisällytä offline-ominaisuus arkaluontoiseen dokumenttien käsittelyyn

### Esimerkki 2: Vähittäiskaupan varastonhallintajärjestelmä

Luo tekoälyllä tehostettu varastonhallintajärjestelmä vähittäiskauppaa varten:

**Käytetyt teknologiat:**
- Kuvan segmentointi tuotetunnistukseen
- Räätälöidyt näkömallit brändi- ja kategoriaklassifikointiin
- Foundry Local -käyttöönotto erikoistuneille vähittäiskielimalleille
- Integraatio olemassa oleviin POS- ja varastojärjestelmiin

**Toteutustapa:**
- Rakenna kameraintegraatio reaaliaikaista tuotteen skannausta varten
- Toteuta viivakoodi- ja visuaalinen tuotetunnistus
- Lisää luonnollisen kielen varastokyselyt paikallisilla kielimalleilla
- Suunnittele skaalautuva arkkitehtuuri monimyymäläkäyttöön

### Esimerkki 3: Terveydenhuollon dokumentointiapulainen

Kehitä yksityisyyttä suojaava terveydenhuollon dokumentointityökalu:

**Käytetyt teknologiat:**
- Phi Silica lääketieteelliseen muistiinpanojen luontiin ja kliinisen päätöksenteon tukeen
- OCR käsinkirjoitettujen lääketieteellisten tietojen digitointiin
- Räätälöidyt lääketieteen kielimallit Windows ML:n kautta
- Paikallinen vektorivarasto lääketieteellisen tiedon hakua varten

**Toteutustapa:**
- Varmista täysi offline-toiminta potilastietojen yksityisyyden takaamiseksi
- Toteuta lääketieteellisten termien validointi ja ehdotus
- Lisää audit-lokit säädösten noudattamisen varmistamiseksi
- Suunnittele integraatio olemassa oleviin sähköisiin potilastietojärjestelmiin

## Suorituskyvyn optimointistrategiat

### Laitteistotietoisen kehityksen periaatteet

**NPU-optimointi**
- Suunnittele sovelluksia hyödyntämään NPU-ominaisuuksia Copilot+ PC:illä
- Toteuta sulava paluu GPU/CPU-käyttöön laitteissa, joissa ei ole NPU:ta
- Optimoi malliformaatit NPU:n spesifiselle kiihdytykselle
- Seuraa NPU:n käyttöä ja lämpöominaisuuksia

**Muistinhallinta**
- Toteuta tehokkaita mallin lataamisen ja välimuistien hallinnan strategioita
- Käytä muistikartoitusta suurten mallien käynnistyksen nopeuttamiseksi
- Suunnittele muistitietoisia sovelluksia resurssirajoitetuille laitteille
- Toteuta mallin kvantisointi muistin optimointiin

**Akun kesto**
- Optimoi tekoälytoiminnot virrankulutuksen minimointiin
- Toteuta mukautuva käsittely akun varaustason mukaan
- Suunnittele tehokas taustaprosessointi jatkuville tekoälytoiminnoille
- Käytä virrankulutuksen profilointityökaluja energiankulutuksen optimointiin

### Skaalautuvuuden näkökohdat

**Monisäikeisyys**
- Suunnittele säieturvalliset tekoälytoiminnot rinnakkaiseen käsittelyyn
- Toteuta tehokas työnjako käytettävissä olevien ytimien kesken
- Käytä async/await-kuvioita ei-blokkaavaan tekoälykäsittelyyn
- Suunnittele säikeiden hallinnan optimointi eri laitteistokonfiguraatioille

**Välimuististrategiat**
- Toteuta älykäs välimuisti usein käytetyille tekoälytoiminnoille
- Suunnittele välimuistin mitätöintistrategiat mallipäivityksille
- Käytä pysyvää välimuistia kalliille esikäsittelyoperaatioille
- Toteuta hajautettu välimuisti monikäyttäjäympäristöihin

## Turvallisuus- ja yksityisyyskäytännöt

### Datan suojaus

**Paikallinen käsittely**
- Varmista, että arkaluonteiset tiedot eivät koskaan poistu paikalliselta laitteelta
- Toteuta turvallinen säilytys tekoälymalleille ja väliaikaiselle datalle
- Käytä Windowsin turvallisuusominaisuuksia sovellusten hiekkalaatikkona
- Käytä salauksia tallennetuille malleille ja välituloksille

**Mallin turvallisuus**
- Varmista mallin eheys ennen latausta ja suoritusta
- Toteuta turvalliset päivitysmenettelyt malleille
- Käytä allekirjoitettuja malleja manipuloinnin estämiseksi
- Käytä käyttöoikeuden hallintaa mallitiedostoille ja asetuksille

### Vaikutusten arviointi

**Sääntelyn mukaisuus**
- Suunnittele sovellukset vastaamaan GDPR:n, HIPAA:n ja muiden sääntelyvaatimusten kanssa
- Toteuta tarkastuslokit tekoälypäätöksenteon jäljitettävyyteen
- Tarjoa läpinäkyvyystoiminnot tekoälyn tuottamille tuloksille
- Mahdollista käyttäjän kontrolli tekoälydatan käsittelyyn

**Yritysturvallisuus**
- Integroi Windowsin yritysturvapolitiikkojen kanssa
- Tue hallittu käyttöönotto yrityshallintatyökaluilla
- Toteuta roolipohjaiset käyttöoikeudet tekoälyominaisuuksille
- Tarjoa hallinnolliset kontrollit tekoälytoiminnallisuudelle

## Vianmääritys ja debuggaus

### Tyypillisimmät kehityshaasteet

**Rakennusasetusten ongelmat**
- Varmista ARM64-alustan konfiguraatio Windows AI API -näytteille
- Tarkista Windows App SDK:n versioyhteensopivuus (1.8.1+ vaaditaan)
- Varmista, että paketin tunniste on oikein konfiguroitu (vaaditaan Windows AI API -käyttöön)
- Tarkista työkalujen tuki kohdekehysversiolle

**Mallin latausongelmat**
- Varmista ONNX-mallin yhteensopivuus Windows ML:n kanssa
- Tarkista mallitiedoston eheys ja formaattivaatimukset
- Tarkista laitteiston vaatimukset tiettyihin malleihin
- Debuggaa muistinvarausongelmia mallin latauksen aikana
- Varmista suorituspalveluntarjoajan rekisteröinti laitteistokiihdytykselle

**Käyttöönottotilan näkökulmat**
- **Itse sisältävä tila**: Täysin tuettu, mutta vaatii suuremman käyttöönoton koon
- **Kehykseen sidottu tila**: Pienempi jalanjälki, mutta vaatii jaetun suoritusaikaympäristön
- **Pakatuttomat sovellukset**: Ei enää tuettu Windows AI API:ille
- Käytä `dotnet run -p:Platform=ARM64 -p:SelfContained=true` itse sisältävän ARM64-käyttöönoton tekemiseen

**Suorituskykyongelmat**
- Profiilita sovelluksen suorituskyky eri laitteistokonfiguraatioissa
- Tunnista pullonkaulat tekoälykäsittelyputkissa
- Optimoi dataesikäsittely- ja jälkikäsittelytoiminnot
- Toteuta suorituskyvyn seuranta ja hälytykset

**Integraatiohaasteet**
- Debuggaa API-integraatioongelmia asianmukaisella virheenkäsittelyllä
- Varmista syötteiden datamuodot ja esikäsittelyvaatimukset
- Testaa reunatapaukset ja virhetilanteet huolellisesti
- Toteuta kattava lokitus tuotannossa ilmenevien ongelmien tutkiimiseksi

### Debuggaustyökalut ja -menetelmät

**Visual Studio -integraatio**
- Käytä AI Toolkitin debuggaajaa mallin suoritusanalyysiin
- Toteuta suorituskyvyn profilointi tekoälytoiminnoille
- Debuggaa asynkronisia tekoälyoperaatioita asianmukaisella poikkeusten käsittelyllä
- Käytä muistin profilointityökaluja optimointiin

**Windows AI Foundry -työkalut**
- Hyödynnä Foundry Local CLI:tä mallien testaukseen ja validointiin
- Käytä Windows AI API -testausvälineitä integraation varmennukseen
- Toteuta räätälöity lokitus tekoälytoimintojen valvontaan
- Luo automaattisia testejä tekoälytoimintojen luotettavuudelle

## Sovellustesi tulevaisuuden varmistaminen

### Nousevat teknologiat

**Seuraavan sukupolven laitteistot**
- Suunnittele sovelluksia hyödyntämään tulevia NPU-ominaisuuksia
- Varaudu mallien kasvaneisiin kokoihin ja monimutkaisuuteen
- Toteuta adaptiivisia arkkitehtuureja kehittyvälle laitteistolle
- Harkitse kvanttivalmiita algoritmeja tulevaa yhteensopivuutta varten

**Kehittyneet tekoälyominaisuudet**
- Valmistaudu multimodaaliseen tekoälyintegraatioon useiden datatyyppien kanssa
- Suunnittele reaaliaikaista yhteistyötekoälyä useille laitteille
- Suunnittele liittoutuneen oppimisen ominaisuuksia
- Harkitse reunapilvi-hybridiajattelun älykkäitä arkkitehtuureja

### Jatkuva oppiminen ja sopeutuminen

**Mallipäivitykset**
- Toteuta saumattomat mallipäivitysmenettelyt
- Suunnittele sovellukset mukautumaan parantuneisiin mallitoimintoihin
- Varaudu taaksepäin yhteensopivuuteen olemassa olevien mallien kanssa
- Toteuta A/B-testaus mallin suorituskyvyn arviointiin

**Ominaisuuksien kehittyminen**
- Suunnittele modulaariset arkkitehtuurit uusille tekoälyominaisuuksille
- Varaudu uusien Windows AI API:iden integraatioon
- Toteuta ominaisuuksien liput asteittaiseen käyttöönottoon
- Suunnittele käyttöliittymät, jotka sopeutuvat parannettuihin tekoälyominaisuuksiin

## Yhteenveto

Windows Edge AI -kehitys edustaa tehokkaiden tekoälyominaisuuksien yhdistämistä vankkaan, turvalliseen ja skaalautuvaan Windows-alustaan. Hallitsemalla Windows AI Foundryn ekosysteemin kehittäjät pystyvät luomaan älykkäitä sovelluksia, jotka tarjoavat poikkeuksellisen käyttäjäkokemuksen säilyttäen samanaikaisesti korkeimmat tietosuoja-, turvallisuus- ja suorituskykystandardit.

Windows AI API:en, Foundry Localin ja Windows ML:n yhdistelmä tarjoaa vertaansa vailla olevan perustan seuraavan sukupolven älykkäiden Windows-sovellusten rakentamiseen. Kun tekoäly kehittyy, Windows-alusta varmistaa sovellustesi skaalautuvuuden nousevien teknologioiden kanssa pitäen samalla yhteensopivuuden ja suorituskyvyn laajassa Windows-laitteistokentässä.

Olitpa rakentamassa kuluttajasovelluksia, yritysratkaisuja tai erikoistuneita toimialatyökaluja, Windows Edge AI -kehitys antaa sinulle voiman luoda älykkäitä, reagoivia ja syvästi integroituja kokemuksia, jotka hyödyntävät modernien Windows-laitteiden täydellistä potentiaalia.

## Lisäresurssit

### Dokumentaatio ja oppiminen
- [Windows AI Foundry Documentation](https://learn.microsoft.com/windows/ai/)
- [Windows AI APIs Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Get started building an app with Windows AI APIs](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Getting Started](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Overview](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK System Requirements](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windows App SDK -kehitysympäristön asennus](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Esimerkkivarastot ja -koodi
- [Windows App SDK -esimerkit - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK -esimerkit - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime -päättelyesimerkit](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK -esimerkkivarasto](https://github.com/microsoft/WindowsAppSDK-Samples)

### Kehitystyökalut
- [AI-työkalupaketti Visual Studio Codeen](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI -esimerkit](https://learn.microsoft.com/windows/ai/samples/)
- [Mallin muunnostyökalut](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tekninen tuki
- [Windows ML -dokumentaatio](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime -dokumentaatio](https://onnxruntime.ai/docs/)
- [Windows App SDK -dokumentaatio](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Raportoi ongelmista - Windows App SDK -esimerkit](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Yhteisö ja tuki
- [Windows-kehittäjäyhteisö](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry -blogi](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI -koulutus](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tämä opas on suunniteltu kehittymään nopeasti etenevän Windows AI -ekosysteemin mukana. Säännölliset päivitykset varmistavat yhteensopivuuden uusimpien alustamahdollisuuksien ja parhaiden kehityskäytäntöjen kanssa.*

[08. Käytännön harjoitus Microsoft Foundry Localin kanssa - täydellinen kehittäjätyökalupaketti](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->