# Kapitola 03: Nasazení malých jazykových modelů (SLM)

Tato obsáhlá kapitola se zabývá celým životním cyklem nasazení malých jazykových modelů (SLM), pokrývá teoretické základy, praktické implementační strategie a produkčně připravená kontejnerová řešení. Kapitola je strukturována do tří postupných sekcí, které čtenáře vedou od základních konceptů k pokročilým scénářům nasazení.

## Struktura kapitoly a vzdělávací cesta

### **[Sekce 1: Pokročilé učení SLM - základy a optimalizace](./01.SLMAdvancedLearning.md)**
Úvodní sekce stanovuje teoretický základ pro pochopení malých jazykových modelů a jejich strategického významu v nasazeních AI na okraji sítě. Tato sekce zahrnuje:

- **Rámec klasifikace parametrů**: Podrobný průzkum kategorií SLM od mikro SLM (100M-1,4B parametrů) po střední SLM (14B-30B parametrů), se zaměřením na modely jako Phi-4-mini-3.8B, série Qwen3 a Google Gemma3, včetně analýzy požadavků na hardware a paměťové nároky pro každou úroveň modelu
- **Pokročilé optimalizační techniky**: Komplexní pokrytí metod kvantizace pomocí Llama.cpp, Microsoft Olive a Apple MLX frameworků, včetně nejmodernější kvantizace BitNET 1-bit s praktickými ukázkami kódu zobrazujícími kvantizační pipeline a výsledky benchmarků
- **Strategie získávání modelů**: Hloubková analýza ekosystému Hugging Face a katalogu modelů Azure AI Foundry pro nasazení SLM na podnikové úrovni, s ukázkami kódu pro programové stahování modelů, validaci a konverzi formátů
- **API pro vývojáře**: Ukázky kódu v Pythonu, C++ a C#, které ukazují, jak načítat modely, provádět inference a integrovat je s populárními frameworky jako PyTorch, TensorFlow a ONNX Runtime

Tato základní sekce zdůrazňuje rovnováhu mezi provozní efektivitou, flexibilitou nasazení a nákladovou efektivitou, která činí SLM ideálními pro scénáře edge computingu, s praktickými ukázkami kódu, které mohou vývojáři přímo implementovat ve svých projektech.

### **[Sekce 2: Nasazení v lokálním prostředí - řešení s prioritou na soukromí](./02.DeployingSLMinLocalEnv.md)**
Druhá sekce přechází od teorie k praktické implementaci, zaměřuje se na strategie lokálního nasazení, které upřednostňují suverenitu dat a provozní nezávislost. Klíčové oblasti zahrnují:

- **Ollama Universal Platform**: Komplexní průzkum nasazení napříč platformami s důrazem na uživatelsky přívětivé pracovní postupy, správu životního cyklu modelů a přizpůsobení prostřednictvím Modelfiles, včetně kompletních příkladů integrace REST API a automatizačních skriptů CLI
- **Microsoft Foundry Local**: Řešení nasazení na podnikové úrovni s optimalizací založenou na ONNX, integrací Windows ML a komplexními bezpečnostními funkcemi, s ukázkami kódu v C# a Pythonu pro integraci do nativních aplikací
- **Komparativní analýza**: Podrobná porovnání frameworků pokrývající technickou architekturu, výkonové charakteristiky a optimalizační pokyny pro konkrétní případy použití, s benchmarkovým kódem pro hodnocení rychlosti inference a využití paměti na různém hardwaru
- **Integrace API**: Ukázkové aplikace ukazující, jak vytvářet webové služby, chatovací aplikace a datové zpracovatelské pipeline pomocí lokálních nasazení SLM, s ukázkami kódu v Node.js, Python Flask/FastAPI a ASP.NET Core
- **Testovací frameworky**: Automatizované přístupy k testování kvality modelů, včetně příkladů jednotkových a integračních testů pro implementace SLM

Tato sekce poskytuje praktické pokyny pro organizace, které chtějí implementovat řešení AI s ochranou soukromí, přičemž si zachovávají plnou kontrolu nad svým prostředím nasazení, s připravenými ukázkami kódu, které mohou vývojáři přizpůsobit svým specifickým požadavkům.

### **[Sekce 3: Kontejnerové nasazení v cloudu - řešení pro produkční škálování](./03.DeployingSLMinCloud.md)**
Závěrečná sekce se zaměřuje na pokročilé strategie kontejnerového nasazení, přičemž jako hlavní případová studie slouží Microsoftův Phi-4-mini-instruct. Tato sekce zahrnuje:

- **Nasazení vLLM**: Optimalizace inference s vysokým výkonem pomocí OpenAI-kompatibilních API, pokročilé akcelerace GPU a konfigurace pro produkční prostředí, včetně kompletních Dockerfile, manifestů Kubernetes a parametrů pro ladění výkonu
- **Orchestrace kontejnerů Ollama**: Zjednodušené pracovní postupy nasazení s Docker Compose, varianty optimalizace modelů a integrace webového UI, s příklady CI/CD pipeline pro automatizované nasazení a testování
- **Implementace ONNX Runtime**: Optimalizované nasazení pro edge s komplexní konverzí modelů, strategiemi kvantizace a kompatibilitou napříč platformami, včetně podrobných ukázek kódu pro optimalizaci a nasazení modelů
- **Monitoring a pozorovatelnost**: Implementace dashboardů Prometheus/Grafana s vlastními metrikami pro monitorování výkonu SLM, včetně konfigurací upozornění a agregace logů
- **Vyvažování zátěže a škálování**: Praktické příklady horizontálních a vertikálních strategií škálování s konfiguracemi automatického škálování na základě využití CPU/GPU a vzorců požadavků
- **Zpevnění bezpečnosti**: Nejlepší bezpečnostní postupy pro kontejnery včetně snížení privilegií, síťových politik a správy tajných klíčů pro API a přístupové údaje k modelům

Každý přístup k nasazení je prezentován s kompletními příklady konfigurace, postupy testování, kontrolními seznamy připravenosti pro produkci a šablonami infrastruktury jako kódu, které mohou vývojáři přímo použít ve svých pracovních postupech nasazení.

## Klíčové vzdělávací výstupy

Po dokončení této kapitoly čtenáři zvládnou:

1. **Strategický výběr modelů**: Pochopení hranic parametrů a výběr vhodných SLM na základě omezení zdrojů a požadavků na výkon
2. **Mistrovství v optimalizaci**: Implementace pokročilých technik kvantizace napříč různými frameworky pro dosažení optimální rovnováhy mezi výkonem a efektivitou
3. **Flexibilita nasazení**: Výběr mezi lokálními řešeními zaměřenými na ochranu soukromí a škálovatelnými kontejnerovými nasazeními podle potřeb organizace
4. **Připravenost na produkci**: Konfigurace systémů monitorování, bezpečnosti a škálování pro nasazení SLM na podnikové úrovni

## Praktická orientace a aplikace v reálném světě

Kapitola si po celou dobu udržuje silnou praktickou orientaci, zahrnuje:

- **Praktické příklady**: Kompletní konfigurační soubory, postupy testování API a skripty pro nasazení
- **Benchmarking výkonu**: Podrobné porovnání rychlosti inference, využití paměti a požadavků na zdroje
- **Bezpečnostní aspekty**: Praktiky bezpečnosti na podnikové úrovni, rámce pro dodržování předpisů a strategie ochrany dat
- **Nejlepší postupy**: Ověřené pokyny pro monitorování, škálování a údržbu v produkčním prostředí

## Perspektiva připravená na budoucnost

Kapitola uzavírá pohledem na vznikající trendy, včetně:

- Pokročilé architektury modelů s lepšími poměry efektivity
- Hlubší integrace hardwaru se specializovanými AI akcelerátory
- Vývoj ekosystému směrem ke standardizaci a interoperabilitě
- Vzorce adopce na podnikové úrovni poháněné ochranou soukromí a požadavky na dodržování předpisů

Tento komplexní přístup zajišťuje, že čtenáři budou dobře vybaveni k navigaci jak současnými výzvami nasazení SLM, tak budoucím technologickým vývojům, a budou schopni činit informovaná rozhodnutí, která odpovídají jejich specifickým organizačním požadavkům a omezením.

Kapitola slouží jako praktický průvodce pro okamžitou implementaci i jako strategický zdroj pro dlouhodobé plánování nasazení AI, zdůrazňuje kritickou rovnováhu mezi schopnostmi, efektivitou a provozní dokonalostí, která definuje úspěšná nasazení SLM.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.