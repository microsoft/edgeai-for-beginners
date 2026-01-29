# Modul 08 Eksempler: Veiledning for Lokal Utvikling med Foundry

## Oversikt

Denne omfattende samlingen demonstrerer både **Foundry Local SDK** og **Shell Command** tilnærminger for å bygge produksjonsklare AI-applikasjoner. Hvert eksempel viser ulike aspekter av edge AI-utvikling, fra grunnleggende REST-integrasjon til avanserte multi-agent systemer.

## Utviklingstilnærming: SDK vs Shell Commands

### Bruk Foundry Local SDK Når:

- **Programmatisk Kontroll**: Du trenger full kontroll over agentens livssyklus, evaluering eller distribusjonsarbeidsflyter
- **Tilpasset Verktøy**: Bygge automatisering rundt Foundry Local (CI/CD-integrasjon, multi-agent orkestrering)
- **Detaljert Tilgang**: Krever detaljert agentmetadata, versjonering eller kontroll over evalueringskjøringer
- **Python-Integrasjon**: Arbeider i Python-tunge miljøer eller integrerer Foundry-logikk i bredere applikasjoner
- **Bedriftsarbeidsflyter**: Implementerer modulære arbeidsflyter og reproduserbare evalueringspipelines i tråd med Microsofts referansearkitekturer

### Bruk Shell Commands Når:

- **Rask Testing**: Utfører rask lokal testing, manuelle agentstarter eller oppsettverifisering
- **CLI Enkelhet**: Trenger enkle CLI-operasjoner for å starte/stoppe agenter, sjekke logger eller grunnleggende evalueringer
- **Lettvekts Automatisering**: Skripter enkel automatisering uten behov for full SDK-integrasjon
- **Rask Iterasjon**: Feilsøking og utviklingssykluser, spesielt i begrensede miljøer eller ressursgruppe-nivå distribusjoner
- **Oppsett & Validering**: Innledende miljøkonfigurasjon og rask verifisering

## Beste Praksis & Anbefalt Arbeidsflyt

Basert på prinsipper for agentlivssyklusadministrasjon, avhengighetssporing og minst privilegert reproduserbarhet:

### Fase 1: Grunnlag & Oppsett
1. **Start med Shell Commands** for innledende oppsett og rask validering
2. **Verifiser Miljøet** ved hjelp av CLI-verktøy og grunnleggende modellutplassering
3. **Test Tilkobling** med enkle REST-anrop og helsesjekker

### Fase 2: Utvikling & Integrasjon
1. **Overgang til SDK** for skalerbare, sporbare arbeidsflyter
2. **Implementer Programmatisk Kontroll** for komplekse agentinteraksjoner
3. **Bygg Tilpassede Verktøy** for fellesskapsklare maler og Azure OpenAI-integrasjon

### Fase 3: Produksjon & Skala
1. **Hybrid Tilnærming** som kombinerer CLI for drift og SDK for applikasjonslogikk
2. **Bedriftsintegrasjon** med overvåking, logging og distribusjonspipelines
3. **Fellesskapsbidrag** gjennom gjenbrukbare maler og beste praksis

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.