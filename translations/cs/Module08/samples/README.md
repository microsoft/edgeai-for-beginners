# Modul 08 Ukázky: Příručka pro lokální vývoj Foundry

## Přehled

Tato obsáhlá kolekce ukazuje přístupy **Foundry Local SDK** a **Shell Command** pro vytváření produkčně připravených AI aplikací. Každá ukázka představuje různé aspekty vývoje edge AI, od základní integrace REST až po pokročilé systémy s více agenty.

## Přístup k vývoji: SDK vs Shell Commands

### Použijte Foundry Local SDK, pokud:

- **Programová kontrola**: Potřebujete plnou kontrolu nad životním cyklem agenta, hodnocením nebo pracovními postupy nasazení
- **Vlastní nástroje**: Vytváříte automatizaci kolem Foundry Local (integrace CI/CD, orchestraci více agentů)
- **Detailní přístup**: Vyžadujete podrobné metadata agenta, verzování nebo kontrolu nad hodnocením
- **Integrace s Pythonem**: Pracujete v prostředí zaměřeném na Python nebo začleňujete logiku Foundry do širších aplikací
- **Podnikové pracovní postupy**: Implementujete modulární pracovní postupy a reprodukovatelné hodnotící procesy v souladu s referenčními architekturami Microsoftu

### Použijte Shell Commands, pokud:

- **Rychlé testování**: Provádíte rychlé lokální testy, manuální spuštění agentů nebo ověřování nastavení
- **Jednoduchost CLI**: Potřebujete jednoduché operace CLI pro spuštění/zastavení agentů, kontrolu logů nebo základní hodnocení
- **Lehká automatizace**: Skriptujete jednoduchou automatizaci bez požadavků na plnou integraci SDK
- **Rychlá iterace**: Ladíte a vyvíjíte, zejména v omezených prostředích nebo nasazeních na úrovni skupiny zdrojů
- **Nastavení a ověření**: Počáteční konfigurace prostředí a rychlé ověřovací úkoly

## Nejlepší postupy a doporučený pracovní postup

Na základě správy životního cyklu agenta, sledování závislostí a principů reprodukovatelnosti s minimálními oprávněními:

### Fáze 1: Základy a nastavení
1. **Začněte s Shell Commands** pro počáteční nastavení a rychlé ověření
2. **Ověřte prostředí** pomocí nástrojů CLI a základního nasazení modelu
3. **Otestujte konektivitu** pomocí jednoduchých REST volání a kontrol stavu

### Fáze 2: Vývoj a integrace
1. **Přejděte na SDK** pro škálovatelné a sledovatelné pracovní postupy
2. **Implementujte programovou kontrolu** pro komplexní interakce agentů
3. **Vytvořte vlastní nástroje** pro šablony připravené pro komunitu a integraci Azure OpenAI

### Fáze 3: Produkce a škálování
1. **Hybridní přístup** kombinující CLI pro operace a SDK pro aplikační logiku
2. **Podniková integrace** s monitorováním, logováním a nasazovacími procesy
3. **Příspěvek komunitě** prostřednictvím opakovaně použitelných šablon a osvědčených postupů

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.