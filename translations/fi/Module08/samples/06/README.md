# Istunto 6 Esimerkki: Mallit työkaluina

Tämä esimerkki toteuttaa yksinkertaisen reitittimen + työkalurekisterin, joka valitsee mallin käyttäjän kehotteen perusteella ja kutsuu Foundry Localin OpenAI-yhteensopivaa päätepistettä.

## Tiedostot
- `router.py`: yksinkertainen rekisteri ja heuristinen reititys; päätepisteen haku + terveystarkistus.

## Suorita (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Huomautukset
- Reititin käyttää yksinkertaisia avainsanaheuristiikkoja valitakseen `general`, `reasoning` ja `code` työkalujen välillä ja tulostaa `/v1/models` käynnistyessään.
- Konfiguroi ympäristömuuttujien avulla:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Viitteet
- Foundry Local (Oppiminen): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrointi inferenssi-SDK:iden kanssa: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.