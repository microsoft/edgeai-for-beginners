# Modul 08 Exempel: Foundry Lokal Utvecklingsguide

## Översikt

Denna omfattande samling visar både **Foundry Local SDK** och **Shell Command**-metoder för att bygga produktionsklara AI-applikationer. Varje exempel belyser olika aspekter av edge AI-utveckling, från grundläggande REST-integration till avancerade system med flera agenter.

## Utvecklingsmetod: SDK vs Shell-kommandon

### Använd Foundry Local SDK när:

- **Programmatisk Kontroll**: Du behöver full kontroll över agentens livscykel, utvärdering eller distributionsarbetsflöden
- **Anpassade Verktyg**: Bygga automatisering kring Foundry Local (CI/CD-integration, orkestrering av flera agenter)
- **Detaljerad Åtkomst**: Kräver detaljerad agentmetadata, versionshantering eller kontroll över utvärderingsverktyg
- **Python Integration**: Arbetar i Python-tunga miljöer eller integrerar Foundry-logik i bredare applikationer
- **Företagsarbetsflöden**: Implementerar modulära arbetsflöden och reproducerbara utvärderingspipelines i linje med Microsofts referensarkitekturer

### Använd Shell-kommandon när:

- **Snabb Testning**: Utför snabb lokal testning, manuella agentstarter eller verifiering av inställningar
- **CLI Enkelhet**: Behöver enkla CLI-operationer för att starta/stoppa agenter, kontrollera loggar eller grundläggande utvärderingar
- **Lättviktsautomatisering**: Skriptar enkel automatisering utan krav på full SDK-integration
- **Snabba Iterationer**: Felsökning och utvecklingscykler, särskilt i begränsade miljöer eller resursgruppsnivå-distributioner
- **Inställning & Validering**: Initial konfiguration av miljön och snabb verifiering

## Bästa Praxis & Rekommenderat Arbetsflöde

Baserat på principer för hantering av agentens livscykel, spårning av beroenden och reproducerbarhet med minsta privilegier:

### Fas 1: Grundläggning & Inställning
1. **Börja med Shell-kommandon** för initial inställning och snabb validering
2. **Verifiera Miljön** med CLI-verktyg och grundläggande modelldistribution
3. **Testa Anslutning** med enkla REST-anrop och hälsokontroller

### Fas 2: Utveckling & Integration
1. **Övergå till SDK** för skalbara och spårbara arbetsflöden
2. **Implementera Programmatisk Kontroll** för komplexa agentinteraktioner
3. **Bygg Anpassade Verktyg** för community-klara mallar och Azure OpenAI-integration

### Fas 3: Produktion & Skalning
1. **Hybridmetod** som kombinerar CLI för drift och SDK för applikationslogik
2. **Företagsintegration** med övervakning, loggning och distributionspipelines
3. **Community-bidrag** genom återanvändbara mallar och bästa praxis

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.