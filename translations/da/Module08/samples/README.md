# Modul 08 Eksempler: Foundry Lokal Udviklingsguide

## Oversigt

Denne omfattende samling demonstrerer både **Foundry Local SDK** og **Shell Command** tilgange til at bygge produktionsklare AI-applikationer. Hvert eksempel fremhæver forskellige aspekter af edge AI-udvikling, fra grundlæggende REST-integration til avancerede multi-agent systemer.

## Udviklingsmetode: SDK vs Shell Commands

### Brug Foundry Local SDK Når:

- **Programmatisk kontrol**: Du har brug for fuld kontrol over agentens livscyklus, evaluering eller udrulningsarbejdsgange
- **Tilpassede værktøjer**: Bygge automatisering omkring Foundry Local (CI/CD integration, multi-agent orkestrering)
- **Detaljeret adgang**: Kræver detaljeret agentmetadata, versionering eller kontrol over evalueringskørsler
- **Python-integration**: Arbejder i Python-tunge miljøer eller integrerer Foundry-logik i bredere applikationer
- **Enterprise-arbejdsgange**: Implementerer modulære arbejdsgange og reproducerbare evalueringspipelines i tråd med Microsofts referencearkitekturer

### Brug Shell Commands Når:

- **Hurtig testning**: Udfører hurtige lokale tests, manuelle agentstarter eller opsætningsverifikation
- **CLI enkelhed**: Har brug for enkle CLI-operationer til at starte/stoppe agenter, tjekke logs eller grundlæggende evalueringer
- **Letvægtsautomatisering**: Skripter simpel automatisering uden behov for fuld SDK-integration
- **Hurtig iteration**: Fejlfinding og udviklingscyklusser, især i begrænsede miljøer eller ressourcegruppe-niveau udrulninger
- **Opsætning & validering**: Indledende miljøkonfiguration og hurtige verifikationstests

## Bedste praksis & anbefalet arbejdsgang

Baseret på principper for agentlivscyklusstyring, afhængighedssporing og mindst privilegeret reproducerbarhed:

### Fase 1: Fundament & Opsætning
1. **Start med Shell Commands** til indledende opsætning og hurtig validering
2. **Verificer miljøet** ved hjælp af CLI-værktøjer og grundlæggende modeludrulning
3. **Test forbindelsen** med simple REST-kald og sundhedstjek

### Fase 2: Udvikling & Integration
1. **Overgang til SDK** for skalerbare, sporbare arbejdsgange
2. **Implementer programmatisk kontrol** for komplekse agentinteraktioner
3. **Byg tilpassede værktøjer** til fællesskabs-klare skabeloner og Azure OpenAI-integration

### Fase 3: Produktion & Skalering
1. **Hybrid tilgang** der kombinerer CLI til drift og SDK til applikationslogik
2. **Enterprise-integration** med overvågning, logning og udrulningspipelines
3. **Fællesskabsbidrag** gennem genanvendelige skabeloner og bedste praksis

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.