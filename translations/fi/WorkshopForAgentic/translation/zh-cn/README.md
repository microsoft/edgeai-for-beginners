<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:45:53+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "fi"
}
-->
# 🎙️ AI-podcast-studio-työpaja

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.fi.png)

## Tehtäväsi

Tervetuloa **AI-podcast-studioon**! Olet julkaisemassa omaa teknologiapodcastiasi "Future Bytes" – mutta tässä on käänne: rakennat tekoälyllä toimivan tuotantotiimin auttamaan sinua luomaan sen. Ei enää loputonta tutkimusta, käsikirjoittamista ja äänenmuokkausta. Sen sijaan ohjelmoit itseäsi tekoälykyvykkääksi podcast-tuottajaksi.

## Tarinan tausta

Kuvittele: sinä ja kaverisi haluatte aloittaa podcastin kiinnostavimmista teknologisista trendeistä, mutta jokaisella on kiire opintojen, työn tai elämän kanssa. Mitä jos voisit rakentaa tekoälyagenttien tiimin hoitamaan raskaan työn? Yksi agentti tutkii aiheet, toinen kirjoittaa mukaansatempaavat käsikirjoitukset, kolmas muuntaa tekstin luonnolliseksi sujuvaksi dialogiksi. Kuulostaa scifi-skenaariolta? Tehdään siitä todellisuutta.

## Mitä opit

Työpajan lopussa tiedät, miten:
- 🤖 Oletusolet omat paikalliset tekoälymallisi käyttöön (ilman API-kuluja, ilman pilvipalvelusta riippuvuutta!)
- 🔧 Rakennat käytännön yhteistyössä toimivia ammattilaisterekoälyagentteja
- 🎬 Luot täydellisen podcast-tuotantoprosessin ideasta ääneen saakka

## Matkasi: Kolmiosainen tarina

Kuten missä tahansa hyvässä tarinassa, meillä on kolme näytöstä. Jokaisessa näytöksessä rakennat vähitellen oman AI-podcast-studiosi:

| Luku | Tehtäväsi | Mitä tapahtuu | Avatut taidot |
|---------|-----------|--------------|----------------|
| **Näytös 1** | [Tutustu AI-avustajaasi](01.BuildAIAgentWithSLM.md) | Opit luomaan tekoälyagentteja, jotka voivat keskustella, etsiä tietoa verkosta ja jopa ratkaista ongelmia. Kuvittele heitä tutkimusapulaisina, jotka eivät koskaan nuku. | 🎯 Rakenna ensimmäinen agenttisi<br>🛠️ Anna sille supervoimat (työkalut!)<br>🧠 Opeta se ajattelemaan<br>🌐 Yhdistä internetiin |
| **Näytös 2** | [Muodosta tuotantotiimisi](02.AIAgentOrchestrationAndWorkflows.md) | Nyt homma muuttuu hauskaksi! Sovitat useita tekoälyagentteja työskentelemään yhdessä kuin aito podcast-tiimi. Yksi tutkii, toinen kirjoittaa, sinä hyväksyt – tiimityöllä unelmat toteutuvat. | 🎭 Koordinoi useita agentteja<br>🔄 Rakenna hyväksymisprosessit<br>🖥️ Testaa DevUI-käyttöliittymällä<br>✋ Pidä ihmisohjaus |
| **Näytös 3** | [Elävöitä podcastisi](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Suuri finaali! Muunna käsikirjoituksesi tekstistä autenttiseksi podcast-ääniraidaksi, jolla on aidot äänet ja luonnollinen dialogi. Podcastisi "Future Bytes" on julkaisuvalmis! | 🎤 Tekstistä puheeksi -taikuus<br>👥 Monipuhujaäänet<br>⏱️ Pitkän muodon ääniraidat<br>🚀 Täysin automatisoitu |

Jokainen näytös avaa uusia taitoja. Jos olet rohkea, voit katsella hypellen, mutta suosittelemme oppimaan järjestyksessä!

## Ympäristövaatimukset

Työpaja tukee erilaisia laitteistoja:
- **CPU**: soveltuu testaamiseen ja pienimuotoiseen käyttöön
- **GPU**: suositellaan tuotantokäyttöön, parantaa merkittävästi suorituskykyä
- **NPU**: tukee seuraavan sukupolven neuroverkon prosessointiyksikön kiihdytystä

## Mitä tarvitset

### Ohjelmistolistaus ✅
- **Python 3.10+** (ohjelmointikielesi)
- **Ollama** (tekoälymallien ajuri koneellasi)
- **VS Code** (koodieditorisi)
- **Python-laajennus** (tekee VS Codesta fiksumman)
- **Git** (koodin hakemiseen)

### Laitteistotarkistus 💻
- **Voinko ajaa?**: 8GB RAM, 10GB vapaata tilaa (käytettävissä, mutta voi olla hidasta)
- **Ihanteellinen kokoonpano**: 16GB+ RAM, hyvä GPU (sujuva suoritus!)
- **Onko NPU?**: Silloin vielä parempi! Avaat seuraavan sukupolven suorituskyvyn 🚀

## Rakenna studiosi 🎬

### Vaihe 1: Päivitä Python

Varmista, että sinulla on Python 3.10 tai uudempi:

```bash
python --version
# Näytettävä Python 3.10.x tai uudempi versio
```

Ei vielä Pythonia? Hanki se ilmaiseksi osoitteesta [python.org](https://python.org)!

### Vaihe 2: Lataa Ollama (tekoälymalliajon moottori)

Siirry osoitteeseen [ollama.ai](https://ollama.ai) ja lataa laitteeseesi sopiva versio Ollamasta. Se toimii moottorina paikallisesti ajoitettaville tekoälymalleille.

Testaa, että se on käyttövalmis:

```bash
ollama --version
```

### Vaihe 3: Lataa AI-aivosi 🧠

On aika hakea Qwen-3-8B-malli (kuin palkkaisit ensimmäisen tekoälyapulaisesi):

```bash
ollama pull qwen3:8b
```

*Tämä voi kestää muutaman minuutin. Täydellinen kahvitauko! ☕*

### Vaihe 4: Aseta VS Code

Jos sinulla ei vielä ole, lataa [Visual Studio Code](https://code.visualstudio.com/). Se on paras koodieditori (kiistakysymyksiä ei oteta vastaan 😄).

### Vaihe 5: Python-laajennus

VS Codessa:
1. Paina `Ctrl+Shift+X` (Macilla `Cmd+Shift+X`)
2. Etsi "Python"
3. Asenna Microsoftin virallinen Python-laajennus

### Vaihe 6: Homma hanskassa! 🎉

Olet oikeasti valmis. Luodaan vähän tekoälytaikaa!

### Vaihe 7: Asenna Microsoft Agent Framework ja riippuvuudet 📦

Asenna työpajan vaatimat kaikki paketit:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Tämä asentaa Microsoft Agent Frameworkin ja kaikki tarvittavat kirjastot. Nauti kahvi – ensimmäinen asennus voi kestää hetken! ☕*

## Työpajan ohjeet

Yksityiskohtainen projektiarkkitehtuuri, käyttöönotto ja suoritusmenetelmät käydään läpi vaihe vaiheelta työpajan aikana.

## Vianetsintä (jos jotain menee pieleen) 🔧

### "Voi ei, mallin lataus on liian hidasta!"
**Ratkaisu**: Käytä VPN:ää tai konfiguroi Ollama peilipalvelin. Verkko ei aina ole paras ystävä.

### "Koneeni on kuormittumassa! Muisti loppumassa!"
**Ratkaisu**: Vaihda pienempään malliin tai säädä `num_ctx` -asetusta käyttämään vähemmän muistia. Ajattele sitä AI:n dieettinä.

### "Voinko nopeuttaa sitä GPU:lla?"
**Ratkaisu**: Ollama tunnistaa GPU:n automaattisesti! Varmista vain, että GPU-ajurit ovat ajan tasalla. Ilmainen suorituskyvyn lisäys! 🏎️

## Lisäresurssit (uteliaille) 📚

- [Ollama-dokumentaatio](https://github.com/ollama/ollama) — syvällistä tietoa paikallisista tekoälymalleista
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — lisätietoja agenttitiimien rakentamisesta
- [Qwen-mallin tiedot](https://qwenlm.github.io/) — tunne tekoälyavustajasi aivot

## Lisenssi

MIT-lisenssi — rakenna siistejä juttuja, jaa ne, tee maailmasta parempi! 🌍

## Haluatko osallistua?

Löysit virheen? Ideoita? Avaa Issue tai lähetä PR! Rakastamme yhteisön henkeä. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ota huomioon, että automaattikäännöksissä saattaa olla virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä on pidettävä auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->