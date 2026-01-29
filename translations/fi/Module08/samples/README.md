# Moduuli 08 Esimerkit: Foundry Paikallisen Kehityksen Opas

## Yleiskatsaus

Tämä kattava kokoelma esittelee sekä **Foundry Local SDK**- että **Shell Command**-lähestymistavat tuotantovalmiiden tekoälysovellusten rakentamiseen. Jokainen esimerkki tuo esiin eri näkökulmia edge AI -kehityksestä, perus REST-integraatiosta edistyneisiin monen agentin järjestelmiin.

## Kehityslähestymistapa: SDK vs Shell-komennot

### Käytä Foundry Local SDK:ta, kun:

- **Ohjelmallinen hallinta**: Tarvitset täyden hallinnan agenttien elinkaaren, arvioinnin tai käyttöönoton työnkulkujen suhteen
- **Mukautettu työkalujen kehitys**: Rakennat automaatiota Foundry Localin ympärille (CI/CD-integraatio, monen agentin orkestrointi)
- **Tarkka pääsy**: Tarvitset yksityiskohtaista agenttien metadataa, versiointia tai arviointityökalujen hallintaa
- **Python-integraatio**: Työskentelet Python-painotteisessa ympäristössä tai upotat Foundry-logiikkaa laajempiin sovelluksiin
- **Yrityksen työnkulut**: Toteutat modulaarisia työnkulkuja ja toistettavia arviointiputkia, jotka ovat linjassa Microsoftin viitearkkitehtuurien kanssa

### Käytä Shell-komentoja, kun:

- **Nopea testaus**: Suoritat nopeita paikallisia testejä, käynnistät agentteja manuaalisesti tai tarkistat asetuksia
- **CLI-yksinkertaisuus**: Tarvitset yksinkertaisia CLI-toimintoja agenttien käynnistämiseen/pysäyttämiseen, lokien tarkistamiseen tai perusarviointeihin
- **Kevyt automaatio**: Skriptaat yksinkertaista automaatiota ilman täyttä SDK-integraatiota
- **Nopeat iteroinnit**: Virheenkorjaus- ja kehityssyklit, erityisesti rajatuissa ympäristöissä tai resurssiryhmätason käyttöönotossa
- **Asetus ja validointi**: Alustavan ympäristön konfigurointi ja nopeiden tarkistustehtävien suorittaminen

## Parhaat käytännöt ja suositeltu työnkulku

Perustuen agenttien elinkaaren hallintaan, riippuvuuksien seurantaan ja vähimmäisoikeuksien toistettavuuden periaatteisiin:

### Vaihe 1: Perusta ja asetukset
1. **Aloita Shell-komennoilla** alkuasetusten ja nopean validoinnin suorittamiseksi
2. **Vahvista ympäristö** CLI-työkaluilla ja perusmallin käyttöönotolla
3. **Testaa yhteydet** yksinkertaisilla REST-kutsuilla ja terveystarkistuksilla

### Vaihe 2: Kehitys ja integrointi
1. **Siirry SDK:han** skaalautuvien ja jäljitettävien työnkulkujen toteuttamiseksi
2. **Toteuta ohjelmallinen hallinta** monimutkaisia agenttien vuorovaikutuksia varten
3. **Rakenna mukautettuja työkaluja** yhteisövalmiita mallipohjia ja Azure OpenAI -integraatiota varten

### Vaihe 3: Tuotanto ja skaalaus
1. **Hybridi lähestymistapa** yhdistä CLI operaatioihin ja SDK sovelluslogiikkaan
2. **Yritysintegraatio** valvonnan, lokituksen ja käyttöönoton putkien kanssa
3. **Yhteisön panos** uudelleenkäytettävien mallipohjien ja parhaiden käytäntöjen kautta

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.