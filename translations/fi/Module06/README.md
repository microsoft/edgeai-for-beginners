# Luku 06: SLM-agenttijärjestelmät: Kattava yleiskatsaus

Tekoälyn kenttä kokee merkittävän muutoksen, kun siirrymme yksinkertaisista chatbot-ohjelmista kehittyneisiin AI-agentteihin, joita tukevat pienet kielimallit (SLM). Tämä kattava opas käsittelee kolmea keskeistä osa-aluetta nykyaikaisissa SLM-agenttijärjestelmissä: perustavanlaatuiset käsitteet ja käyttöönoton strategiat, toimintojen kutsumiskyvyt sekä vallankumouksellinen Model Context Protocol (MCP) -integraatio.

## [Osio 1: AI-agenttien ja pienten kielimallien perusta](./01.IntroduceAgent.md)

Ensimmäinen osio luo perustan AI-agenttien ja pienten kielimallien ymmärtämiselle, ja asettaa vuoden 2025 AI-agenttien aikakaudeksi chatbotien aikakauden (2023) ja copilot-buumin (2024) jälkeen. Tässä osiossa esitellään **agenttiset AI-järjestelmät**, jotka ajattelevat, järkeilevät, suunnittelevat, käyttävät työkaluja ja suorittavat tehtäviä minimaalisella ihmisen panoksella.

### Keskeiset käsitteet:
- **Agenttien luokittelukehys**: Yksinkertaisista refleksiagenteista oppiviin agentteihin, tarjoten kattavan taksonomian eri laskentaskenaarioille
- **SLM:n perusteet**: Määritellään pienet kielimallit malleiksi, joissa on alle 10 miljardia parametria ja jotka voivat suorittaa käytännön päättelyä kuluttajalaitteilla
- **Edistyneet optimointistrategiat**: Käsitellään GGUF-muodon käyttöönottoa, kvantisointitekniikoita (Q4_K_M, Q5_K_S, Q8_0) ja reunalaitteille optimoituja kehyksiä, kuten Llama.cpp ja Apple MLX
- **SLM vs LLM -vaihtokaupat**: Näytetään 10–30× kustannussäästö SLM:ien avulla samalla säilyttäen tehokkuus 70–80 %:ssa tyypillisistä agenttitehtävistä

Osio päättyy käytännön käyttöönoton strategioihin Ollaman, VLLM:n ja Microsoftin reunaratkaisujen avulla, ja vahvistaa SLM:t kustannustehokkaan ja yksityisyyttä suojelevan agenttisen AI:n tulevaisuutena.

## [Osio 2: Toimintojen kutsuminen pienissä kielimalleissa](./02.FunctionCalling.md)

Toinen osio syventyy **toimintojen kutsumiskykyihin**, mekanismiin, joka muuttaa staattiset kielimallit dynaamisiksi AI-agenteiksi, jotka kykenevät vuorovaikutukseen todellisessa maailmassa. Tämä tekninen syväluotaus kattaa koko työnkulun intentin tunnistamisesta vastauksen integrointiin.

### Keskeiset toteutusalueet:
- **Systemaattinen työnkulku**: Yksityiskohtainen tarkastelu työkalujen integroinnista, toimintojen määrittelystä, intentin tunnistamisesta, JSON-tulosten luomisesta ja ulkoisesta suorittamisesta
- **Alustakohtaiset toteutukset**: Kattavat oppaat Phi-4-mini Ollaman kanssa, Qwen3:n toimintojen kutsuminen ja Microsoft Foundry Local -integraatio
- **Edistyneet esimerkit**: Moniagenttiset yhteistyöjärjestelmät, dynaaminen työkalujen valinta ja yritysintegraatiomallit kattavalla virheenkäsittelyllä
- **Tuotantokäytön näkökohdat**: Nopeusrajoitukset, auditointilokit, turvallisuustoimenpiteet ja suorituskyvyn optimointistrategiat

Tämä osio tarjoaa sekä teoreettista ymmärrystä että käytännön toteutusmalleja, jotka mahdollistavat kehittäjille vankkojen toimintojen kutsumisjärjestelmien rakentamisen, jotka voivat käsitellä kaikkea yksinkertaisista API-kutsuista monimutkaisiin monivaiheisiin yritystyönkulkuihin.

## [Osio 3: Model Context Protocol (MCP) -integraatio](./03.IntroduceMCP.md)

Viimeinen osio esittelee **Model Context Protocol (MCP)** -protokollan, vallankumouksellisen kehyksen, joka standardoi kielimallien vuorovaikutuksen ulkoisten työkalujen ja järjestelmien kanssa. Tässä osiossa näytetään, kuinka MCP luo sillan AI-mallien ja todellisen maailman välille hyvin määriteltyjen protokollien avulla.

### Integraation kohokohdat:
- **Protokollan arkkitehtuuri**: Kerrostettu järjestelmän suunnittelu, joka kattaa sovellus-, LLM-asiakas-, MCP-asiakas- ja työkalujen käsittelykerrokset
- **Monitaustatuki**: Joustava toteutus, joka tukee sekä Ollamaa (paikallinen kehitys) että vLLM:ää (tuotanto) taustoina
- **Yhteysprotokollat**: STDIO-tila suoraa prosessiviestintää varten ja SSE-tila HTTP-pohjaista suoratoistoa varten
- **Todelliset sovellukset**: Verkkoprosessointi, datankäsittely ja API-integraatioesimerkit kattavalla virheenkäsittelyllä

MCP-integraatio osoittaa, kuinka SLM:t voidaan laajentaa ulkoisilla kyvyillä, kompensoiden niiden pienempää parametrimäärää parannetulla toiminnallisuudella samalla säilyttäen paikallisen käyttöönoton ja resurssitehokkuuden edut.

## Strategiset vaikutukset

Nämä kolme osiota yhdessä tarjoavat kattavan kehyksen SLM-agenttijärjestelmien ymmärtämiseen ja toteuttamiseen. Kehitys perustavanlaatuisista käsitteistä toimintojen kutsumiseen ja MCP-integraatioon osoittaa selkeän polun kohti demokratisoitua AI:n käyttöönottoa, jossa:

- **Tehokkuus kohtaa kyvykkyyden** optimoitujen pienten mallien avulla
- **Kustannustehokkuus** mahdollistaa laajan käyttöönoton
- **Standardoidut protokollat** varmistavat yhteentoimivuuden
- **Paikallinen käyttöönotto** säilyttää yksityisyyden ja vähentää viivettä

Tämä kehitys edustaa paitsi teknologista edistystä myös paradigman muutosta kohti helpommin saavutettavia, tehokkaampia ja käytännöllisempiä AI-järjestelmiä, jotka voivat toimia tehokkaasti resurssirajoitteisissa ympäristöissä samalla tarjoten kehittyneitä agenttikyvykkyyksiä.

SLM:ien yhdistäminen edistyneisiin käyttöönoton strategioihin, vankkoihin toimintojen kutsumismekanismeihin ja standardoituihin työkalujen integraatioprotokolliin asettaa nämä järjestelmät seuraavan sukupolven AI-agenttien perustaksi, jotka muuttavat tapaa, jolla vuorovaikutamme tekoälyn kanssa ja hyödymme siitä eri toimialoilla ja sovelluksissa.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.