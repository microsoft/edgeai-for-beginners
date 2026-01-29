# Modul 08 Ukážky: Príručka pre lokálny vývoj Foundry

## Prehľad

Táto komplexná kolekcia demonštruje prístupy **Foundry Local SDK** a **Shell Command** na vytváranie produkčne pripravených AI aplikácií. Každá ukážka predstavuje rôzne aspekty vývoja AI na okraji, od základnej integrácie REST až po pokročilé systémy s viacerými agentmi.

## Prístup k vývoju: SDK vs Shell Commands

### Použite Foundry Local SDK, keď:

- **Programatická kontrola**: Potrebujete úplnú kontrolu nad životným cyklom agenta, hodnotením alebo pracovnými postupmi nasadenia
- **Vlastné nástroje**: Vytvárate automatizáciu okolo Foundry Local (integrácia CI/CD, orchestrácia viacerých agentov)
- **Detailný prístup**: Vyžadujete podrobné metadáta agenta, verzovanie alebo kontrolu nad hodnotiacim runnerom
- **Integrácia s Pythonom**: Pracujete v prostredí zameranom na Python alebo vkladáte logiku Foundry do širších aplikácií
- **Podnikové pracovné postupy**: Implementujete modulárne pracovné postupy a reprodukovateľné hodnotiace pipeline v súlade s referenčnými architektúrami Microsoftu

### Použite Shell Commands, keď:

- **Rýchle testovanie**: Vykonávate rýchle lokálne testovanie, manuálne spúšťanie agentov alebo overovanie nastavení
- **Jednoduchosť CLI**: Potrebujete jednoduché operácie CLI na spúšťanie/zastavovanie agentov, kontrolu logov alebo základné hodnotenia
- **Jednoduchá automatizácia**: Skriptujete jednoduchú automatizáciu bez požiadaviek na plnú integráciu SDK
- **Rýchla iterácia**: Ladíte a vyvíjate cykly, najmä v obmedzených prostrediach alebo nasadeniach na úrovni skupiny zdrojov
- **Nastavenie a validácia**: Počiatočná konfigurácia prostredia a rýchle overovacie úlohy

## Najlepšie postupy a odporúčaný pracovný postup

Na základe správy životného cyklu agenta, sledovania závislostí a princípov reprodukovateľnosti s minimálnymi privilégiami:

### Fáza 1: Základy a nastavenie
1. **Začnite so Shell Commands** na počiatočné nastavenie a rýchlu validáciu
2. **Overte prostredie** pomocou nástrojov CLI a základného nasadenia modelu
3. **Otestujte konektivitu** jednoduchými REST volaniami a kontrolami stavu

### Fáza 2: Vývoj a integrácia
1. **Prejdite na SDK** pre škálovateľné a sledovateľné pracovné postupy
2. **Implementujte programatickú kontrolu** pre komplexné interakcie agentov
3. **Vytvorte vlastné nástroje** pre šablóny pripravené pre komunitu a integráciu Azure OpenAI

### Fáza 3: Produkcia a škálovanie
1. **Hybridný prístup** kombinujúci CLI pre operácie a SDK pre aplikačnú logiku
2. **Podniková integrácia** s monitorovaním, logovaním a pipeline nasadenia
3. **Príspevok komunite** prostredníctvom opakovane použiteľných šablón a najlepších postupov

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.