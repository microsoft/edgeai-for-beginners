# AI Toolkit pro Visual Studio Code - Průvodce vývojem Edge AI

## Úvod

Vítejte v komplexním průvodci používáním AI Toolkit pro Visual Studio Code při vývoji Edge AI. Jak se umělá inteligence přesouvá z centralizovaného cloudového výpočtu na distribuovaná edge zařízení, vývojáři potřebují výkonné, integrované nástroje, které zvládnou jedinečné výzvy nasazení na edge - od omezených zdrojů po požadavky na offline provoz.

AI Toolkit pro Visual Studio Code překonává tuto mezeru tím, že poskytuje kompletní vývojové prostředí speciálně navržené pro vytváření, testování a optimalizaci AI aplikací, které efektivně běží na edge zařízeních. Ať už vyvíjíte pro IoT senzory, mobilní zařízení, vestavěné systémy nebo edge servery, tento toolkit zjednodušuje celý váš vývojový proces v prostředí, které znáte z VS Code.

Tento průvodce vás provede základními koncepty, nástroji a osvědčenými postupy pro využití AI Toolkit ve vašich projektech Edge AI, od výběru modelu až po nasazení do produkce.

## Přehled

AI Toolkit pro Visual Studio Code je výkonné rozšíření, které zjednodušuje vývoj agentů a tvorbu AI aplikací. Toolkit poskytuje komplexní možnosti pro průzkum, hodnocení a nasazení AI modelů od široké škály poskytovatelů—včetně Anthropic, OpenAI, GitHub, Google—a zároveň podporuje lokální provádění modelů pomocí ONNX a Ollama.

Co odlišuje AI Toolkit, je jeho komplexní přístup k celému životnímu cyklu vývoje AI. Na rozdíl od tradičních nástrojů pro vývoj AI, které se zaměřují na jednotlivé aspekty, AI Toolkit poskytuje integrované prostředí, které pokrývá objevování modelů, experimentování, vývoj agentů, hodnocení a nasazení—vše v prostředí VS Code.

Platforma je speciálně navržena pro rychlé prototypování a nasazení do produkce, s funkcemi jako generování promptů, rychlé starty, bezproblémové integrace MCP (Model Context Protocol) nástrojů a rozsáhlé možnosti hodnocení. Pro vývoj Edge AI to znamená, že můžete efektivně vyvíjet, testovat a optimalizovat AI aplikace pro scénáře nasazení na edge, přičemž si zachováte celý vývojový proces v prostředí VS Code.

## Výukové cíle

Na konci tohoto průvodce budete schopni:

### Základní dovednosti
- **Nainstalovat a nakonfigurovat** AI Toolkit pro Visual Studio Code pro pracovní postupy vývoje Edge AI
- **Orientovat se a využívat** rozhraní AI Toolkit, včetně Model Catalog, Playground a Agent Builder
- **Vybrat a hodnotit** AI modely vhodné pro nasazení na edge na základě výkonu a omezení zdrojů
- **Převádět a optimalizovat** modely pomocí formátu ONNX a technik kvantizace pro edge zařízení

### Dovednosti vývoje Edge AI
- **Navrhnout a implementovat** Edge AI aplikace pomocí integrovaného vývojového prostředí
- **Provádět testování modelů** v podmínkách podobných edge pomocí lokální inference a monitorování zdrojů
- **Vytvářet a přizpůsobovat** AI agenty optimalizované pro scénáře nasazení na edge
- **Hodnotit výkon modelů** pomocí metrik relevantních pro edge computing (latence, využití paměti, přesnost)

### Optimalizace a nasazení
- **Použít techniky kvantizace a prořezávání** ke snížení velikosti modelu při zachování přijatelného výkonu
- **Optimalizovat modely** pro specifické edge hardwarové platformy včetně akcelerace CPU, GPU a NPU
- **Implementovat osvědčené postupy** pro vývoj Edge AI včetně správy zdrojů a strategií záložních řešení
- **Připravit modely a aplikace** pro nasazení do produkce na edge zařízeních

### Pokročilé koncepty Edge AI
- **Integrovat s frameworky Edge AI** včetně ONNX Runtime, Windows ML a TensorFlow Lite
- **Implementovat architektury s více modely** a scénáře federovaného učení pro edge prostředí
- **Řešit běžné problémy Edge AI** včetně omezení paměti, rychlosti inference a kompatibility hardwaru
- **Navrhnout strategie monitorování a logování** pro Edge AI aplikace v produkci

### Praktické použití
- **Vytvořit kompletní Edge AI řešení** od výběru modelu po nasazení
- **Prokázat znalosti** v edge-specifických pracovních postupech vývoje a optimalizačních technikách
- **Aplikovat naučené koncepty** na reálné případy použití Edge AI včetně IoT, mobilních a vestavěných aplikací
- **Hodnotit a porovnávat** různé strategie nasazení Edge AI a jejich kompromisy

## Klíčové funkce pro vývoj Edge AI

### 1. Katalog modelů a objevování
- **Podpora více poskytovatelů**: Procházejte a přistupujte k AI modelům od Anthropic, OpenAI, GitHub, Google a dalších poskytovatelů
- **Integrace lokálních modelů**: Zjednodušené objevování modelů ONNX a Ollama pro nasazení na edge
- **Modely z GitHubu**: Přímá integrace s hostováním modelů na GitHubu pro zjednodušený přístup
- **Porovnání modelů**: Porovnávejte modely vedle sebe, abyste našli optimální rovnováhu pro omezení edge zařízení

### 2. Interaktivní Playground
- **Interaktivní testovací prostředí**: Rychlé experimentování s možnostmi modelů v kontrolovaném prostředí
- **Podpora multimodality**: Testování s obrázky, textem a dalšími vstupy typickými pro edge scénáře
- **Experimentování v reálném čase**: Okamžitá zpětná vazba na odpovědi modelů a výkon
- **Optimalizace parametrů**: Doladění parametrů modelu pro požadavky nasazení na edge

### 3. Builder promptů (Agent Builder)
- **Generování přirozeného jazyka**: Generujte startovací prompty pomocí popisů v přirozeném jazyce
- **Iterativní zdokonalování**: Zlepšujte prompty na základě odpovědí modelů a výkonu
- **Rozklad úkolů**: Rozdělujte složité úkoly pomocí řetězení promptů a strukturovaných výstupů
- **Podpora proměnných**: Používejte proměnné v promptech pro dynamické chování agentů
- **Generování produkčního kódu**: Generujte produkčně připravený kód pro rychlý vývoj aplikací

### 4. Hromadné spuštění a hodnocení
- **Testování více modelů**: Spouštějte více promptů na vybraných modelech současně
- **Efektivní testování ve velkém měřítku**: Testujte různé vstupy a konfigurace efektivně
- **Vlastní testovací případy**: Spouštějte agenty s testovacími případy pro ověření funkčnosti
- **Porovnání výkonu**: Porovnávejte výsledky napříč různými modely a konfiguracemi

### 5. Hodnocení modelů pomocí datových sad
- **Standardní metriky**: Testujte AI modely pomocí vestavěných hodnotících nástrojů (F1 skóre, relevance, podobnost, koherence)
- **Vlastní hodnotící nástroje**: Vytvářejte vlastní hodnotící metriky pro specifické případy použití
- **Integrace datových sad**: Testujte modely na rozsáhlých datových sadách
- **Měření výkonu**: Kvantifikujte výkon modelů pro rozhodování o nasazení na edge

### 6. Možnosti doladění
- **Přizpůsobení modelů**: Přizpůsobte modely pro specifické případy použití a obory
- **Specializovaná adaptace**: Přizpůsobte modely specializovaným oborům a požadavkům
- **Optimalizace pro edge**: Doladění modelů speciálně pro omezení nasazení na edge
- **Trénink specifický pro obor**: Vytvářejte modely přizpůsobené specifickým případům použití na edge

### 7. Integrace MCP nástrojů
- **Připojení k externím nástrojům**: Připojte agenty k externím nástrojům prostřednictvím serverů Model Context Protocol
- **Akce v reálném světě**: Umožněte agentům dotazovat se na databáze, přistupovat k API nebo provádět vlastní logiku
- **Existující MCP servery**: Používejte nástroje z příkazového řádku (stdio) nebo HTTP (server-sent event) protokolů
- **Vývoj vlastních MCP**: Vytvářejte a testujte nové MCP servery pomocí nástroje Agent Builder

### 8. Vývoj a testování agentů
- **Podpora volání funkcí**: Umožněte agentům dynamicky volat externí funkce
- **Testování integrace v reálném čase**: Testujte integrace s běhy v reálném čase a používáním nástrojů
- **Verzování agentů**: Správa verzí agentů s možností porovnání výsledků hodnocení
- **Ladění a sledování**: Lokální sledování a ladění pro vývoj agentů

## Pracovní postup vývoje Edge AI

### Fáze 1: Objevování a výběr modelů
1. **Prozkoumejte katalog modelů**: Použijte katalog modelů k nalezení modelů vhodných pro nasazení na edge
2. **Porovnejte výkon**: Hodnoťte modely na základě velikosti, přesnosti a rychlosti inference
3. **Testujte lokálně**: Použijte modely Ollama nebo ONNX k lokálnímu testování před nasazením na edge
4. **Posuďte požadavky na zdroje**: Určete potřeby paměti a výpočetního výkonu pro cílová edge zařízení

### Fáze 2: Optimalizace modelů
1. **Převod na ONNX**: Převádějte vybrané modely do formátu ONNX pro kompatibilitu s edge
2. **Použijte kvantizaci**: Snižte velikost modelu pomocí kvantizace INT8 nebo INT4
3. **Optimalizace hardwaru**: Optimalizujte pro cílový edge hardware (ARM, x86, specializované akcelerátory)
4. **Ověření výkonu**: Ověřte, že optimalizované modely zachovávají přijatelnou přesnost

### Fáze 3: Vývoj aplikací
1. **Návrh agentů**: Použijte Agent Builder k vytvoření AI agentů optimalizovaných pro edge
2. **Inženýrství promptů**: Vyvíjejte prompty, které efektivně fungují s menšími edge modely
3. **Testování integrace**: Testujte agenty v simulovaných podmínkách edge
4. **Generování kódu**: Generujte produkční kód optimalizovaný pro nasazení na edge

### Fáze 4: Hodnocení a testování
1. **Hromadné hodnocení**: Testujte více konfigurací pro nalezení optimálních edge nastavení
2. **Profilování výkonu**: Analyzujte rychlost inference, využití paměti a přesnost
3. **Simulace edge**: Testujte v podmínkách podobných cílovému prostředí nasazení na edge
4. **Zátěžové testování**: Hodnoťte výkon za různých podmínek zatížení

### Fáze 5: Příprava na nasazení
1. **Finální optimalizace**: Aplikujte finální optimalizace na základě výsledků testování
2. **Balíčkování pro nasazení**: Připravte modely a kód pro nasazení na edge
3. **Dokumentace**: Dokumentujte požadavky na nasazení a konfiguraci
4. **Nastavení monitorování**: Připravte monitorování a logování pro nasazení na edge

## Cílová skupina pro vývoj Edge AI

### Vývojáři Edge AI
- Vývojáři aplikací vytvářející edge zařízení a IoT řešení poháněná AI
- Vývojáři vestavěných systémů integrující AI schopnosti do zařízení s omezenými zdroji
- Mobilní vývojáři vytvářející AI aplikace na zařízení pro smartphony a tablety

### Inženýři Edge AI
- Inženýři AI optimalizující modely pro nasazení na edge a spravující inference pipeline
- DevOps inženýři nasazující a spravující AI modely na distribuované edge infrastruktuře
- Inženýři výkonu optimalizující AI pracovní zátěže pro omezení edge hardwaru

### Výzkumníci a pedagogové
- Výzkumníci AI vyvíjející efektivní modely a algoritmy pro edge computing
- Pedagogové vyučující koncepty Edge AI a demonstrující techniky optimalizace
- Studenti učící se o výzvách a řešeních při nasazení Edge AI

## Případy použití Edge AI

### Chytrá IoT zařízení
- **Rozpoznávání obrazu v reálném čase**: Nasazení modelů počítačového vidění na IoT kamerách a senzorech
- **Zpracování hlasu**: Implementace rozpoznávání řeči a zpracování přirozeného jazyka na chytrých reproduktorech
- **Prediktivní údržba**: Spouštění modelů detekce anomálií na průmyslových edge zařízeních
- **Monitorování prostředí**: Nasazení modelů analýzy dat ze senzorů pro environmentální aplikace

### Mobilní a vestavěné aplikace
- **Překlad na zařízení**: Implementace modelů překladu jazyka, které fungují offline
- **Rozšířená realita**: Nasazení rozpoznávání objektů v reálném čase a sledování pro AR aplikace
- **Monitorování zdraví**: Spouštění modelů analýzy zdraví na nositelných zařízeních a lékařském vybavení
- **Autonomní systémy**: Implementace modelů rozhodování pro drony, roboty a vozidla

### Edge výpočetní infrastruktura
- **Edge datová centra**: Nasazení AI modelů v edge datových centrech pro aplikace s nízkou latencí
- **Integrace CDN**: Integrace schopností AI zpracování do sítí pro doručování obsahu
- **5G Edge**: Využití edge computingu s 5G pro aplikace poháněné AI
- **Fog computing**: Implementace AI zpracování v prostředích fog computingu

## Instalace a nastavení

### Instalace rozšíření
Nainstalujte rozšíření AI Toolkit přímo z Visual Studio Code Marketplace:

**ID rozšíření**: `ms-windows-ai-studio.windows-ai-studio`

**Metody instalace**:
1. **VS Code Marketplace**: Vyhledejte "AI Toolkit" v zobrazení Extensions
2. **Příkazový řádek**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Přímá instalace**: Stáhněte z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Předpoklady pro vývoj Edge AI
- **Visual Studio Code**: Doporučena nejnovější verze
- **Python prostředí**: Python 3.8+ s požadovanými AI knihovnami
- **ONNX Runtime** (volitelné): Pro inference modelů ONNX
- **Ollama** (volitelné): Pro lokální obsluhu modelů
- **Nástroje pro akceleraci hardwaru**: CUDA, OpenVINO nebo platformově specifické akcelerátory

### Počáteční konfigurace
1. **Aktivace rozšíření**: Otevřete VS Code a ověřte, že se AI Toolkit zobrazuje v Activity Bar
2. **Nastavení poskytovatele modelů**: Nakonfigurujte přístup k GitHubu, OpenAI, Anthropic nebo jiným poskytovatelům modelů
3. **Lokální prostředí**: Nastavte Python prostředí a nainstalujte požadované balíčky
4. **Akcelerace hardwaru**: Nakonfigurujte akceleraci GPU/NPU, pokud je dostupná
2. Generujte počáteční výzvy pomocí popisů v přirozeném jazyce  
3. Iterujte a upravujte výzvy na základě odpovědí modelu  
4. Integrujte nástroje MCP pro rozšířené schopnosti agentů  

#### Krok 3: Testování a hodnocení  
1. Použijte **Bulk Run** k testování více výzev na vybraných modelech  
2. Spouštějte agenty s testovacími případy pro ověření funkčnosti  
3. Hodnoťte přesnost a výkon pomocí vestavěných nebo vlastních metrik  
4. Porovnávejte různé modely a konfigurace  

#### Krok 4: Doladění a optimalizace  
1. Přizpůsobte modely pro specifické okrajové případy použití  
2. Aplikujte doladění specifické pro danou doménu  
3. Optimalizujte pro omezení nasazení na okrajových zařízeních  
4. Verzujte a porovnávejte různé konfigurace agentů  

#### Krok 5: Příprava na nasazení  
1. Generujte produkčně připravený kód pomocí Agent Builderu  
2. Nastavte připojení k MCP serveru pro produkční použití  
3. Připravte balíčky pro nasazení na okrajová zařízení  
4. Konfigurujte metriky monitorování a hodnocení  

## Ukázky pro AI Toolkit  

Vyzkoušejte naše ukázky  
[Ukázky AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) jsou navrženy tak, aby pomohly vývojářům a výzkumníkům efektivně prozkoumat a implementovat AI řešení.  

Naše ukázky zahrnují:  

Ukázkový kód: Předem připravené příklady demonstrující funkce AI, jako je trénování, nasazení nebo integrace modelů do aplikací.  
Dokumentace: Průvodce a tutoriály, které uživatelům pomohou pochopit funkce AI Toolkit a jak je používat.  
Předpoklady  

- Visual Studio Code  
- AI Toolkit pro Visual Studio Code  
- GitHub jemně-granulovaný osobní přístupový token (PAT)  
- Foundry Local  

## Nejlepší postupy pro vývoj Edge AI  

### Výběr modelu  
- **Omezení velikosti**: Vyberte modely, které se vejdou do paměťových limitů cílových zařízení  
- **Rychlost inferencí**: Upřednostněte modely s rychlou inferencí pro aplikace v reálném čase  
- **Kompromisy přesnosti**: Vyvažte přesnost modelu s omezenými zdroji  
- **Kompatibilita formátů**: Preferujte formáty ONNX nebo optimalizované pro hardware pro nasazení na okraji  

### Optimalizační techniky  
- **Kvantizace**: Použijte kvantizaci INT8 nebo INT4 ke snížení velikosti modelu a zlepšení rychlosti  
- **Prořezávání**: Odstraňte nepotřebné parametry modelu ke snížení výpočetních požadavků  
- **Destilace znalostí**: Vytvořte menší modely, které si zachovají výkon větších modelů  
- **Hardwarová akcelerace**: Využijte NPUs, GPUs nebo specializované akcelerátory, pokud jsou dostupné  

### Pracovní postup vývoje  
- **Iterativní testování**: Testujte často v podmínkách podobných okraji během vývoje  
- **Monitorování výkonu**: Nepřetržitě sledujte využití zdrojů a rychlost inferencí  
- **Správa verzí**: Sledujte verze modelů a nastavení optimalizace  
- **Dokumentace**: Dokumentujte všechna rozhodnutí o optimalizaci a kompromisy výkonu  

### Úvahy o nasazení  
- **Monitorování zdrojů**: Sledujte paměť, CPU a spotřebu energie v produkci  
- **Strategie zálohování**: Implementujte mechanismy zálohování pro selhání modelu  
- **Mechanismy aktualizace**: Plánujte aktualizace modelů a správu verzí  
- **Bezpečnost**: Implementujte vhodná bezpečnostní opatření pro aplikace Edge AI  

## Integrace s Edge AI Frameworks  

### ONNX Runtime  
- **Nasazení napříč platformami**: Nasazujte ONNX modely na různých okrajových platformách  
- **Optimalizace hardwaru**: Využijte hardwarově specifické optimalizace ONNX Runtime  
- **Podpora mobilních zařízení**: Použijte ONNX Runtime Mobile pro aplikace na smartphonech a tabletech  
- **Integrace IoT**: Nasazujte na IoT zařízení pomocí lehkých distribucí ONNX Runtime  

### Windows ML  
- **Zařízení Windows**: Optimalizujte pro okrajová zařízení a PC založené na Windows  
- **Akcelerace NPU**: Využijte Neural Processing Units na zařízeních Windows  
- **DirectML**: Použijte DirectML pro akceleraci GPU na platformách Windows  
- **Integrace UWP**: Integrujte s aplikacemi Universal Windows Platform  

### TensorFlow Lite  
- **Optimalizace pro mobilní zařízení**: Nasazujte modely TensorFlow Lite na mobilní a vestavěná zařízení  
- **Hardwaroví delegáti**: Použijte specializované hardwarové delegáty pro akceleraci  
- **Mikrokontroléry**: Nasazujte na mikrokontroléry pomocí TensorFlow Lite Micro  
- **Podpora napříč platformami**: Nasazujte na Android, iOS a vestavěné systémy Linux  

### Azure IoT Edge  
- **Hybridní cloud-okraj**: Kombinujte trénování v cloudu s inferencí na okraji  
- **Nasazení modulů**: Nasazujte AI modely jako moduly IoT Edge  
- **Správa zařízení**: Spravujte okrajová zařízení a aktualizace modelů na dálku  
- **Telemetrie**: Sbírejte data o výkonu a metriky modelů z nasazení na okraji  

## Pokročilé scénáře Edge AI  

### Nasazení více modelů  
- **Modelové soubory**: Nasazujte více modelů pro zlepšení přesnosti nebo redundanci  
- **A/B testování**: Testujte různé modely současně na okrajových zařízeních  
- **Dynamický výběr**: Vyberte modely na základě aktuálních podmínek zařízení  
- **Sdílení zdrojů**: Optimalizujte využití zdrojů napříč více nasazenými modely  

### Federované učení  
- **Distribuované trénování**: Trénujte modely na více okrajových zařízeních  
- **Zachování soukromí**: Uchovávejte trénovací data lokálně při sdílení vylepšení modelu  
- **Spolupracující učení**: Umožněte zařízením učit se z kolektivních zkušeností  
- **Koordinace okraj-cloud**: Koordinujte učení mezi okrajovými zařízeními a cloudovou infrastrukturou  

### Zpracování v reálném čase  
- **Zpracování streamů**: Zpracovávejte kontinuální datové proudy na okrajových zařízeních  
- **Inferenční latence**: Optimalizujte pro minimální latenci inferencí  
- **Batch zpracování**: Efektivně zpracovávejte dávky dat na okrajových zařízeních  
- **Adaptivní zpracování**: Přizpůsobte zpracování na základě aktuálních schopností zařízení  

## Řešení problémů při vývoji Edge AI  

### Běžné problémy  
- **Paměťová omezení**: Model je příliš velký pro paměť cílového zařízení  
- **Rychlost inferencí**: Inferenční rychlost modelu je příliš pomalá pro požadavky v reálném čase  
- **Degradace přesnosti**: Optimalizace nepřijatelně snižuje přesnost modelu  
- **Kompatibilita hardwaru**: Model není kompatibilní s cílovým hardwarem  

### Strategie ladění  
- **Profilování výkonu**: Použijte funkce sledování AI Toolkit k identifikaci úzkých míst  
- **Monitorování zdrojů**: Sledujte paměť a využití CPU během vývoje  
- **Postupné testování**: Testujte optimalizace postupně, abyste izolovali problémy  
- **Simulace hardwaru**: Použijte vývojové nástroje k simulaci cílového hardwaru  

### Řešení optimalizace  
- **Další kvantizace**: Aplikujte agresivnější techniky kvantizace  
- **Architektura modelu**: Zvažte různé architektury modelů optimalizované pro okraj  
- **Optimalizace předzpracování**: Optimalizujte předzpracování dat pro omezení na okraji  
- **Optimalizace inferencí**: Použijte optimalizace specifické pro hardware  

## Zdroje a další kroky  

### Oficiální dokumentace  
- [Dokumentace pro vývojáře AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Průvodce instalací a nastavením](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentace inteligentních aplikací VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentace Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Komunita a podpora  
- [GitHub repozitář AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub problémy a požadavky na funkce](https://aka.ms/AIToolkit/feedback)  
- [Discord komunita Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Tržiště rozšíření VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technické zdroje  
- [Dokumentace ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentace Ollama](https://ollama.ai/)  
- [Dokumentace Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentace Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Vzdělávací cesty  
- [Kurz základů Edge AI](../Module01/README.md)  
- [Průvodce malými jazykovými modely](../Module02/README.md)  
- [Strategie nasazení na okraji](../Module03/README.md)  
- [Vývoj Edge AI na Windows](./windowdeveloper.md)  

### Další zdroje  
- **Statistiky repozitáře**: 1.8k+ hvězdiček, 150+ forků, 18+ přispěvatelů  
- **Licence**: MIT Licence  
- **Bezpečnost**: Platí bezpečnostní politiky Microsoftu  
- **Telemetrie**: Respektuje nastavení telemetrie VS Code  

## Závěr  

AI Toolkit pro Visual Studio Code představuje komplexní platformu pro moderní vývoj AI, která poskytuje zjednodušené možnosti vývoje agentů, jež jsou obzvláště cenné pro aplikace Edge AI. Díky rozsáhlému katalogu modelů podporujících poskytovatele jako Anthropic, OpenAI, GitHub a Google, v kombinaci s lokálním prováděním prostřednictvím ONNX a Ollama, nabízí toolkit flexibilitu potřebnou pro různé scénáře nasazení na okraji.  

Síla toolkitu spočívá v jeho integrovaném přístupu – od objevování modelů a experimentování v Playgroundu po sofistikovaný vývoj agentů s Prompt Builderem, komplexní možnosti hodnocení a bezproblémovou integraci nástrojů MCP. Pro vývojáře Edge AI to znamená rychlé prototypování a testování AI agentů před nasazením na okraji, s možností rychlé iterace a optimalizace pro prostředí s omezenými zdroji.  

Klíčové výhody pro vývoj Edge AI zahrnují:  
- **Rychlé experimentování**: Testujte modely a agenty rychle před nasazením na okraji  
- **Flexibilita více poskytovatelů**: Přístup k modelům z různých zdrojů pro nalezení optimálních řešení na okraji  
- **Lokální vývoj**: Testujte s ONNX a Ollama pro offline a soukromý vývoj  
- **Připravenost na produkci**: Generujte produkčně připravený kód a integrujte s externími nástroji prostřednictvím MCP  
- **Komplexní hodnocení**: Používejte vestavěné a vlastní metriky k validaci výkonu Edge AI  

Jak se AI stále více přesouvá k scénářům nasazení na okraji, AI Toolkit pro VS Code poskytuje vývojové prostředí a pracovní postup potřebný k vytváření, testování a optimalizaci inteligentních aplikací pro prostředí s omezenými zdroji. Ať už vyvíjíte IoT řešení, mobilní AI aplikace nebo vestavěné inteligentní systémy, komplexní sada funkcí toolkitu a integrovaný pracovní postup podporují celý životní cyklus vývoje Edge AI.  

S průběžným vývojem a aktivní komunitou (1.8k+ hvězdiček na GitHubu) zůstává AI Toolkit na špičce nástrojů pro vývoj AI, neustále se vyvíjející, aby splňoval potřeby moderních vývojářů AI budujících scénáře nasazení na okraji.  

[Další Foundry Local](./foundrylocal.md)  

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.