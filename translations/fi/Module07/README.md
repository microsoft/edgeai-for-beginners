# Luku 07: EdgeAI-esimerkit

Edge AI yhdistää tekoälyn ja reunalaskennan, mahdollistaen älykkään tiedonkäsittelyn suoraan laitteilla ilman pilviyhteyttä. Tässä luvussa tarkastellaan viittä erilaista EdgeAI-toteutusta eri alustoilla ja kehyksillä, jotka osoittavat tekoälymallien monipuolisuuden ja tehon reunalaitteilla.

## 1. EdgeAI NVIDIA Jetson Orin Nanolla

NVIDIA Jetson Orin Nano on merkittävä edistysaskel saavutettavassa reunalaskennassa, tarjoten jopa 67 TOPS:n tekoälysuorituskyvyn kompaktissa, luottokortin kokoisessa muodossa. Tämä tehokas EdgeAI-alusta tuo generatiivisen tekoälyn kehittämisen harrastajien, opiskelijoiden ja ammattilaisten ulottuville.

### Keskeiset ominaisuudet
- Jopa 67 TOPS tekoälysuorituskykyä—1,7-kertainen parannus edeltäjään verrattuna
- 1024 CUDA-ydintä ja jopa 32 Tensor-ydintä tekoälykäsittelyyn
- 6-ytiminen Arm Cortex-A78AE v8.2 64-bittinen prosessori, jonka maksimitaajuus on 1,5 GHz
- Hinta vain 249 dollaria, tarjoten kehittäjille, opiskelijoille ja harrastajille edullisen ja saavutettavan alustan

### Sovellukset
Jetson Orin Nano loistaa modernien generatiivisten tekoälymallien, kuten visio-transformerien, suurten kielimallien ja visio-kielimallien, suorittamisessa. Se on erityisesti suunniteltu GenAI-käyttötapauksiin, ja nyt voit ajaa useita LLM-malleja kämmenen kokoisella laitteella. Suosittuja käyttökohteita ovat tekoälyohjatut robotit, älykkäät dronet, älykkäät kamerat ja autonomiset reunalaitteet.

**Lue lisää**: [NVIDIA:n Jetson Orin Nano SuperComputer: Seuraava suuri askel EdgeAI:ssa](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI mobiilisovelluksissa .NET MAUI:lla ja ONNX Runtime GenAI:lla

Tämä ratkaisu näyttää, kuinka Generatiivinen tekoäly ja suuret kielimallit (LLM:t) voidaan integroida alustariippumattomiin mobiilisovelluksiin käyttämällä .NET MAUI:ta (Multi-platform App UI) ja ONNX Runtime GenAI:ta. Tämä lähestymistapa mahdollistaa .NET-kehittäjille kehittyneiden tekoälyohjattujen mobiilisovellusten rakentamisen, jotka toimivat natiivisti Android- ja iOS-laitteilla.

### Keskeiset ominaisuudet
- Rakennettu .NET MAUI -kehyksen päälle, tarjoten yhden koodipohjan sekä Android- että iOS-sovelluksille
- ONNX Runtime GenAI -integraatio mahdollistaa generatiivisten tekoälymallien suorittamisen suoraan mobiililaitteilla
- Tukee erilaisia mobiililaitteille räätälöityjä laitteistokiihdyttimiä, kuten CPU:ta, GPU:ta ja erikoistuneita mobiilitekoälyprosessoreita
- Alustakohtaiset optimoinnit, kuten CoreML iOS:lle ja NNAPI Androidille ONNX Runtime -alustan kautta
- Toteuttaa koko generatiivisen tekoälyprosessin, mukaan lukien esikäsittely, jälkikäsittely, inferenssi, logits-käsittely, haku ja näytteenotto sekä KV-välimuistin hallinta

### Kehityksen hyödyt
.NET MAUI -lähestymistapa antaa kehittäjille mahdollisuuden hyödyntää olemassa olevia C#- ja .NET-taitojaan rakentaessaan alustariippumattomia tekoälysovelluksia. ONNX Runtime GenAI -kehys tukee useita mallirakenteita, kuten Llama, Mistral, Phi, Gemma ja monia muita. Optimoidut ARM64-ytimet nopeuttavat INT4-kvantisoinnin matriisikertolaskuja, varmistaen tehokkaan suorituskyvyn mobiililaitteilla samalla kun säilytetään tuttu .NET-kehityskokemus.

### Käyttötapaukset
Tämä ratkaisu sopii kehittäjille, jotka haluavat rakentaa tekoälyohjattuja mobiilisovelluksia .NET-teknologioilla, mukaan lukien älykkäät chatbotit, kuvantunnistussovellukset, kielikäännöstyökalut ja personoidut suositusjärjestelmät, jotka toimivat täysin laitteessa parannetun yksityisyyden ja offline-toiminnallisuuden takaamiseksi.

**Lue lisää**: [.NET MAUI ONNX Runtime GenAI -esimerkki](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI Azurella ja Small Language Models Engine -ratkaisulla

Microsoftin Azure-pohjainen EdgeAI-ratkaisu keskittyy pienten kielimallien (SLM) tehokkaaseen käyttöönottoon pilvi-reuna-hybridialustoilla. Tämä lähestymistapa yhdistää pilvipalveluiden laajuiset tekoälypalvelut ja reunalaskennan vaatimukset.

### Arkkitehtuurin edut
- Saumaton integraatio Azure AI -palveluiden kanssa
- SLM/LLM- ja multimodaalimallien suorittaminen laitteessa ja pilvessä ONNX Runtime -alustalla
- Optimoitu yritystason käyttöönottoon
- Jatkuva mallien päivitys ja hallinta

### Käyttötapaukset
Azure EdgeAI -toteutus loistaa tilanteissa, joissa tarvitaan yritystason tekoälyn käyttöönottoa pilvihallintakyvyillä. Näitä ovat esimerkiksi älykäs asiakirjojen käsittely, reaaliaikainen analytiikka ja hybridit tekoälytyönkulut, jotka hyödyntävät sekä pilvi- että reunalaskentaresursseja.

**Lue lisää**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI Windows ML:llä](./windowdeveloper.md)

Windows ML on Microsoftin huipputason ajonaikainen ympäristö, joka on optimoitu suorituskykyiseen mallien suorittamiseen laitteessa ja yksinkertaiseen käyttöönottoon. Se toimii Windows AI Foundryn perustana. Tämä alusta mahdollistaa tekoälyohjattujen Windows-sovellusten luomisen, jotka hyödyntävät PC-laitteiston koko kirjoa.

### Alustan ominaisuudet
- Toimii kaikilla Windows 11 -tietokoneilla, joissa on versio 24H2 (koontiversio 26100) tai uudempi
- Toimii kaikilla x64- ja ARM64-PC-laitteilla, myös niillä, joissa ei ole NPU:ta tai GPU:ta
- Mahdollistaa omien mallien tuomisen ja tehokkaan käyttöönoton AMD-, Intel-, NVIDIA- ja Qualcomm-ekosysteemissä, mukaan lukien CPU, GPU ja NPU
- Infrastruktuuri-API:en ansiosta kehittäjien ei tarvitse luoda useita sovellusversioita eri laitteistoille

### Kehittäjän hyödyt
Windows ML abstrahoi laitteiston ja suoritusympäristöt, joten voit keskittyä koodin kirjoittamiseen. Lisäksi Windows ML päivittyy automaattisesti tukemaan uusimpia NPU-, GPU- ja CPU-laitteita niiden julkaisun myötä. Alusta tarjoaa yhtenäisen kehyksen tekoälyn kehittämiseen Windows-laitteiden monimuotoisessa ekosysteemissä.

**Lue lisää**: 
- [Windows ML -yleiskatsaus](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI -kehitysopas](./windowdeveloper.md) - Kattava opas Windows EdgeAI-kehitykseen

## [5. EdgeAI Foundry Local -sovelluksilla](./foundrylocal.md)

Foundry Local mahdollistaa Windows- ja Mac-kehittäjille Retrieval Augmented Generation (RAG) -sovellusten rakentamisen paikallisia resursseja hyödyntäen .NET:ssä, yhdistäen paikalliset kielimallit ja semanttisen haun ominaisuudet. Tämä lähestymistapa tarjoaa yksityisyyttä korostavia tekoälyratkaisuja, jotka toimivat täysin paikallisessa infrastruktuurissa.

### Tekninen arkkitehtuuri
- Yhdistää Phi-kielimallin, paikalliset upotukset ja Semantic Kernelin RAG-skenaarion luomiseksi
- Käyttää upotuksia vektoreina (liukulukuarvojen taulukoina), jotka edustavat sisällön semanttista merkitystä
- Semantic Kernel toimii pääorkestroijana, integroimalla Phi:n ja älykkäät komponentit saumattoman RAG-putken luomiseksi
- Tukee paikallisia vektorikantoja, kuten SQLite ja Qdrant

### Toteutuksen hyödyt
RAG eli Retrieval Augmented Generation tarkoittaa yksinkertaisesti "tiedon hakemista ja sen lisäämistä kehotteeseen". Tämä paikallinen toteutus varmistaa tietosuojan samalla kun se tarjoaa älykkäitä vastauksia, jotka perustuvat mukautettuihin tietokantoihin. Lähestymistapa on erityisen arvokas yrityksille, jotka tarvitsevat tietosuvereniteettia ja offline-toimintakykyä.

**Lue lisää**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG -esimerkit](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local tarjoaa OpenAI-yhteensopivan REST-palvelimen, jota ONNX Runtime käyttää mallien suorittamiseen paikallisesti Windowsissa. Alla on nopea, validoitu yhteenveto; katso viralliset dokumentit saadaksesi täydelliset tiedot.

- Aloita: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkkitehtuuri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-viite: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Täydellinen Windows-opas tässä repossa: [foundrylocal.md](./foundrylocal.md)

Asenna tai päivitä Windowsissa (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Tutki CLI-kategorioita:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Suorita malli ja löydä dynaaminen päätepiste:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Nopea REST-tarkistus mallien listaamiseksi (korvaa PORT tilasta):
```cmd
curl -s http://localhost:PORT/v1/models
```

Vinkkejä:
- SDK-integraatio: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Tuo oma malli (käännä): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI -kehitysresurssit

Windows-alustaa erityisesti tavoitteleville kehittäjille olemme luoneet kattavan oppaan, joka kattaa koko Windows EdgeAI -ekosysteemin. Tämä resurssi tarjoaa yksityiskohtaista tietoa Windows AI Foundrysta, mukaan lukien API:t, työkalut ja parhaat käytännöt EdgeAI-kehitykseen Windowsilla.

### Windows AI Foundry -alusta
Windows AI Foundry -alusta tarjoaa kattavan työkalujen ja API:en valikoiman, joka on erityisesti suunniteltu EdgeAI-kehitykseen Windows-laitteilla. Tämä sisältää erikoistuen NPU-kiihdytetyille laitteistoille, Windows ML -integraation ja alustakohtaiset optimointitekniikat.

**Kattava opas**: [Windows EdgeAI -kehitysopas](../windowdeveloper.md)

Tämä opas kattaa:
- Windows AI Foundry -alustan yleiskatsauksen ja komponentit
- Phi Silica API tehokkaaseen inferenssiin NPU-laitteistolla
- Tietokonenäkö-API:t kuvankäsittelyyn ja OCR:ään
- Windows ML -ajonaikaisen ympäristön integraation ja optimoinnin
- Foundry Local CLI paikalliseen kehitykseen ja testaukseen
- Laitteisto-optimointistrategiat Windows-laitteille
- Käytännön toteutusesimerkit ja parhaat käytännöt

### [AI Toolkit EdgeAI-kehitykseen](./aitoolkit.md)
Visual Studio Codea käyttäville kehittäjille AI Toolkit -laajennus tarjoaa kattavan kehitysympäristön, joka on erityisesti suunniteltu EdgeAI-sovellusten rakentamiseen, testaamiseen ja käyttöönottoon. Tämä työkalu virtaviivaistaa koko EdgeAI-kehitystyönkulun VS Code -ympäristössä.

**Kehitysopas**: [AI Toolkit EdgeAI-kehitykseen](./aitoolkit.md)

AI Toolkit -opas kattaa:
- Mallien löytäminen ja valinta reunakäyttöön
- Paikalliset testaus- ja optimointityönkulut
- ONNX- ja Ollama-integraatio reunamalleille
- Mallien muunnos- ja kvantisointitekniikat
- Agenttien kehitys reunaskenaarioihin
- Suorituskyvyn arviointi ja seuranta
- Käyttöönoton valmistelu ja parhaat käytännöt

## Yhteenveto

Nämä viisi EdgeAI-toteutusta osoittavat reunalaskennan tekoälyratkaisujen kypsyyden ja monimuotoisuuden. Laitteistokiihdytetyistä reunalaitteista, kuten Jetson Orin Nano, ohjelmistokehyksiin, kuten ONNX Runtime GenAI ja Windows ML, kehittäjillä on ennennäkemättömiä mahdollisuuksia älykkäiden sovellusten käyttöönottoon reunalla.

Yhteinen piirre näissä alustoissa on tekoälyominaisuuksien demokratisointi, joka tekee kehittyneestä koneoppimisesta saavutettavaa kehittäjille eri taitotasoilla ja käyttötapauksissa. Olipa kyseessä mobiilisovellusten, työpöytäsovellusten tai sulautettujen järjestelmien rakentaminen, nämä EdgeAI-ratkaisut tarjoavat perustan seuraavan sukupolven älykkäille sovelluksille, jotka toimivat tehokkaasti ja yksityisesti reunalla.

Jokainen alusta tarjoaa ainutlaatuisia etuja: Jetson Orin Nano laitteistokiihdytettyyn reunalaskentaan, ONNX Runtime GenAI alustariippumattomaan mobiilikehitykseen, Azure EdgeAI yritystason pilvi-reuna-integraatioon, Windows ML Windows-natiiveihin sovelluksiin ja Foundry Local yksityisyyttä korostaviin RAG-toteutuksiin. Yhdessä ne muodostavat kattavan ekosysteemin EdgeAI-kehitykseen.

[Seuraava AI Toolkit](aitoolkit.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.