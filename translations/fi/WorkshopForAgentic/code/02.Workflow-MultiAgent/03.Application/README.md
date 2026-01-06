<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:06:28+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "fi"
}
-->
# Podcast-sovellus

Komentorivisovellus podcast-käsikirjoitusten luomiseen AI-agenttien avulla.

## Käyttö

```bash
python podcast_app.py
```

## Työnkulku

1. **Tervetuloa** - Sovellus tervehtii käyttäjää
2. **Aiheen syöttö** - Käyttäjä antaa podcastin aiheen
3. **Hakuagentti** - Etsii aiheeseen liittyvää tietoa
4. **Käsikirjoitusagentti** - Luo podcast-käsikirjoituksen
5. **Arviointi** - Käyttäjä tarkistaa ja hyväksyy/hylkää käsikirjoituksen
6. **Tallennus** - Hyväksytty käsikirjoitus tallennetaan tiedostoon `podcast.md`

## Vaatimukset

- Python 3.12+
- agent_framework
- Kaikki riippuvuudet paketista 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Keskeisten tietojen osalta suosittelemme ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virheellisistä tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->