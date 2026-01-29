# Module 08 Voorbeelden: Foundry Handleiding voor Lokale Ontwikkeling

## Overzicht

Deze uitgebreide verzameling demonstreert zowel de **Foundry Local SDK** als de **Shell Command** benaderingen voor het bouwen van productieklare AI-toepassingen. Elk voorbeeld belicht verschillende aspecten van edge AI-ontwikkeling, van basis REST-integratie tot geavanceerde multi-agent systemen.

## Ontwikkelingsbenadering: SDK vs Shell Commands

### Gebruik Foundry Local SDK Wanneer:

- **Programmeerbare Controle**: Je hebt volledige controle nodig over de levenscyclus van agents, evaluatie of implementatieworkflows
- **Aangepaste Tools**: Automatisering bouwen rond Foundry Local (CI/CD-integratie, multi-agent orkestratie)
- **Gedetailleerde Toegang**: Vereist gedetailleerde agentmetadata, versiebeheer of controle over de evaluatierunner
- **Python Integratie**: Werken in Python-rijke omgevingen of Foundry-logica integreren in bredere toepassingen
- **Enterprise Workflows**: Modulaire workflows implementeren en reproduceerbare evaluatiepijplijnen opzetten volgens Microsoft referentiearchitecturen

### Gebruik Shell Commands Wanneer:

- **Snelle Tests**: Lokale tests uitvoeren, agents handmatig starten of setup-verificatie
- **Eenvoudige CLI**: Behoefte aan eenvoudige CLI-operaties voor het starten/stoppen van agents, logbestanden controleren of basis-evaluaties
- **Lichte Automatisering**: Scripts maken voor eenvoudige automatisering zonder volledige SDK-integratie
- **Snelle Iteratie**: Debugging en ontwikkelingscycli, vooral in beperkte omgevingen of implementaties op resourcegroepniveau
- **Setup & Validatie**: Initiële configuratie van de omgeving en snelle verificatietaken

## Best Practices & Aanbevolen Workflow

Gebaseerd op principes van agentlevenscyclusbeheer, afhankelijkheidstracking en reproduceerbaarheid met minimale privileges:

### Fase 1: Basis & Setup
1. **Begin met Shell Commands** voor initiële setup en snelle validatie
2. **Verifieer de Omgeving** met CLI-tools en basis modelimplementatie
3. **Test Connectiviteit** met eenvoudige REST-aanroepen en gezondheidscontroles

### Fase 2: Ontwikkeling & Integratie
1. **Schakel over naar SDK** voor schaalbare, traceerbare workflows
2. **Implementeer Programmeerbare Controle** voor complexe agentinteracties
3. **Bouw Aangepaste Tools** voor community-klare templates en Azure OpenAI-integratie

### Fase 3: Productie & Schaal
1. **Hybride Benadering** combineren van CLI voor operaties en SDK voor toepassingslogica
2. **Enterprise Integratie** met monitoring, logging en implementatiepijplijnen
3. **Community Bijdrage** via herbruikbare templates en best practices

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.