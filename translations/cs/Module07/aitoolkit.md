# AI Toolkit pro Visual Studio Code – Průvodce vývojem Edge AI

## Úvod

Vítejte v komplexním průvodci používáním AI Toolkitu pro Visual Studio Code ve vývoji Edge AI. Jak se umělá inteligence přesouvá z centralizovaného cloud computingu na distribuovaná edge zařízení, vývojáři potřebují výkonné, integrované nástroje, které zvládnou jedinečné výzvy edge nasazení – od omezení zdrojů až po požadavky na offline provoz.

AI Toolkit pro Visual Studio Code překonává tento propast tím, že poskytuje úplné vývojové prostředí speciálně navržené pro vytváření, testování a optimalizaci AI aplikací, které efektivně běží na edge zařízeních. Ať už vyvíjíte pro IoT senzory, mobilní zařízení, vestavěné systémy nebo edge servery, tento toolkit zjednodušuje celý váš vývojový workflow v prostředí, které znáte z VS Code.

Tento průvodce vás provede základními koncepty, nástroji a osvědčenými postupy pro využití AI Toolkitu ve vašich projektech Edge AI, od výběru modelu až po nasazení do produkce.

## Přehled

AI Toolkit pro Visual Studio Code je výkonné rozšíření, které zefektivňuje vývoj agentů a tvorbu AI aplikací. Toolkit nabízí komplexní možnosti pro prohlížení, hodnocení a nasazení AI modelů od široké škály poskytovatelů — včetně Anthropic, OpenAI, GitHub, Google — a zároveň podporuje lokální spuštění modelů pomocí ONNX a Ollama.

Co odlišuje AI Toolkit, je jeho komplexní přístup k celému životnímu cyklu vývoje AI. Na rozdíl od tradičních nástrojů, které se zaměřují pouze na jednotlivé aspekty, AI Toolkit poskytuje integrované prostředí pokrývající objevování modelů, experimentování, vývoj agentů, hodnocení a nasazení — vše v prostředí známém z VS Code.

Platforma je zvlášť navržena pro rychlé prototypování a nasazení do produkce, s funkcemi jako generování promptů, rychlé startéry, bezproblémové integrace nástrojů MCP (Model Context Protocol) a rozsáhlé možnosti hodnocení. Pro vývoj Edge AI to znamená, že můžete efektivně vyvíjet, testovat a optimalizovat AI aplikace pro edge scénáře, přičemž zachováte plný vývojový workflow ve VS Code.

## Cíle učení

Po dokončení tohoto průvodce budete schopni:

### Základní dovednosti
- **Nainstalovat a nakonfigurovat** AI Toolkit pro Visual Studio Code pro pracovní postupy Edge AI vývoje
- **Orientovat se a používat** rozhraní AI Toolkitu včetně Model Catalog, Playground a Agent Builderu
- **Vybrat a zhodnotit** AI modely vhodné pro edge nasazení na základě výkonu a omezení zdrojů
- **Převést a optimalizovat** modely pomocí formátu ONNX a kvantizačních technik pro edge zařízení

### Dovednosti vývoje Edge AI
- **Navrhovat a implementovat** Edge AI aplikace s využitím integrovaného vývojového prostředí
- **Provádět testování modelů** v podmínkách podobných edge pomocí lokálního inferenčního prostředí a monitorování zdrojů
- **Vytvářet a přizpůsobovat** AI agenty optimalizované pro edge scénáře nasazení
- **Hodnotit výkon modelů** pomocí metrik relevantních pro edge computing (latence, využití paměti, přesnost)

### Optimalizace a nasazení
- **Používat kvantizační a ořezávací** techniky ke snížení velikosti modelu při zachování přijatelného výkonu
- **Optimalizovat modely** pro specifické edge hardwarové platformy včetně akcelerací CPU, GPU a NPU
- **Implementovat osvědčené postupy** pro vývoj Edge AI včetně řízení zdrojů a fallback strategií
- **Připravit modely a aplikace** pro produkční nasazení na edge zařízeních

### Pokročilé koncepty Edge AI
- **Integrovat s edge AI frameworky** včetně ONNX Runtime, Windows ML a TensorFlow Lite
- **Implementovat multi-modelové architektury** a scénáře federovaného učení pro edge prostředí
- **Řešit běžné problémy Edge AI** včetně omezení paměti, rychlosti inferenčního běhu a kompatibility hardwaru
- **Navrhovat monitorování a logování** pro Edge AI aplikace v produkci

### Praktická aplikace
- **Postavit komplexní Edge AI řešení** od výběru modelu až po nasazení
- **Prokázat znalosti** ve specifických workflow a optimalizačních technikách Edge AI vývoje
- **Aplikovat naučené koncepty** na reálné případy použití Edge AI včetně IoT, mobilních a vestavěných aplikací
- **Hodnotit a porovnávat** různé strategie nasazení Edge AI a jejich kompromisy

## Klíčové funkce pro vývoj Edge AI

### 1. Katalog a objevování modelů
- **Podpora více poskytovatelů**: Prohlížejte a přistupujte k AI modelům od Anthropic, OpenAI, GitHub, Google a dalších poskytovatelů
- **Lokální integrace modelů**: Zjednodušené objevování ONNX a Ollama modelů pro edge nasazení
- **Modely GitHub**: Přímá integrace s hostingem modelů na GitHub pro zjednodušený přístup
- **Porovnávání modelů**: Porovnávejte modely vedle sebe pro nalezení optimálního poměru omezení edge zařízení

### 2. Interaktivní Playground
- **Interaktivní testovací prostředí**: Rychlý experiment s možnostmi modelu v kontrolovaném prostředí
- **Podpora multimodality**: Testování s obrázky, textem a dalšími vstupy běžnými v edge scénářích
- **Experimentace v reálném čase**: Okamžitá zpětná vazba na odpovědi modelů a jejich výkon
- **Optimalizace parametrů**: Doladění parametrů modelu pro požadavky edge nasazení

### 3. Builder promptů (agentů)
- **Generování přirozeného jazyka**: Generování startovacích promptů pomocí přirozených jazykových popisů
- **Iterativní vylepšování**: Zlepšování promptů na základě odpovědí a výkonu modelu
- **Rozklad úloh**: Rozložení složitých úloh pomocí řetězení promptů a strukturovaných výstupů
- **Podpora proměnných**: Použití proměnných v promptech pro dynamické chování agentů
- **Generování produkčního kódu**: Vytváření kódu připraveného k nasazení pro rychlý vývoj aplikací

### 4. Hromadný běh a hodnocení
- **Testování více modelů najednou**: Spouštění více promptů napříč vybranými modely současně
- **Efektivní testování ve velkém měřítku**: Testování různých vstupů a konfigurací efektivně
- **Vlastní testovací případy**: Spouštění agentů s testovacími scénáři pro ověření funkčnosti
- **Porovnávání výkonu**: Porovnání výsledků mezi různými modely a konfiguracemi

### 5. Hodnocení modelů s datasetem
- **Standardní metriky**: Testování AI modelů pomocí vestavěných hodnotitelů (F1 skóre, relevance, podobnost, koherence)
- **Vlastní hodnotitele**: Vytváření vlastních evaluačních metrik pro specifické případy použití
- **Integrace datasetů**: Testování modelů vůči rozsáhlým datasetům
- **Měření výkonu**: Kvantifikace výkonu modelu pro rozhodování o edge nasazení

### 6. Možnosti doladění
- **Přizpůsobení modelů**: Přizpůsobení modelů pro konkrétní případy použití a domény
- **Specializovaná adaptace**: Přizpůsobení modelů specializovaným doménám a požadavkům
- **Optimalizace pro edge**: Doladění modelů specificky pro omezení edge nasazení
- **Trénink specifický pro doménu**: Vytváření modelů šitých na míru konkrétním edge případům použití

### 7. Integrace nástrojů MCP
- **Připojení k externím nástrojům**: Připojte agenty k externím nástrojům přes Model Context Protocol servery
- **Akce reálného světa**: Umožněte agentům dotazovat se do databází, přistupovat k API nebo vykonávat vlastní logiku
- **Existující MCP servery**: Používejte nástroje z příkazového (stdio) nebo HTTP (server-sent event) protokolu
- **Vývoj vlastních MCP**: Vytvářejte a scaffoldujte nové MCP servery s testováním v Agent Builderu

### 8. Vývoj a testování agentů
- **Podpora volání funkcí**: Umožněte agentům dynamicky volat externí funkce
- **Testování integrace v reálném čase**: Testujte integrace během reálných běhů a použití nástrojů
- **Verzování agentů**: Řízení verzí agentů s možnostmi porovnání výsledků hodnocení
- **Ladění a sledování**: Lokální sledování a ladění při vývoji agentů

## Workflow vývoje Edge AI

### Fáze 1: Objevování a výběr modelu
1. **Prozkoumejte katalog modelů**: Použijte katalog modelů k nalezení modelů vhodných pro edge nasazení
2. **Porovnejte výkon**: Hodnoťte modely podle velikosti, přesnosti a rychlosti inferenčního běhu
3. **Testujte lokálně**: Použijte Ollama nebo ONNX modely pro lokální testování před nasazením na edge
4. **Zhodnoťte požadavky na zdroje**: Určete paměťové a výpočetní potřeby cílových edge zařízení

### Fáze 2: Optimalizace modelu
1. **Převod do ONNX**: Převeďte vybrané modely do formátu ONNX pro kompatibilitu s edge
2. **Aplikujte kvantizaci**: Snižte velikost modelu pomocí INT8 nebo INT4 kvantizace
3. **Optimalizace hardwaru**: Optimalizujte pro cílový edge hardware (ARM, x86, specializované akcelerátory)
4. **Validace výkonu**: Ověřte, že optimalizované modely zachovávají přijatelnou přesnost

### Fáze 3: Vývoj aplikace
1. **Návrh agentů**: Použijte Agent Builder k vytvoření edge-optimalizovaných AI agentů
2. **Vývoj promptů**: Vytvořte prompty, které efektivně fungují s menšími edge modely
3. **Testování integrace**: Testujte agenty v simulovaných edge podmínkách
4. **Generování kódu**: Generujte produkční kód optimalizovaný pro edge nasazení

### Fáze 4: Hodnocení a testování
1. **Hromadné hodnocení**: Testujte více konfigurací k nalezení optimálních edge nastavení
2. **Profilování výkonu**: Analyzujte rychlost inferenčního běhu, využití paměti a přesnost
3. **Simulace edge**: Testujte ve scénářích podobných prostředí cílového edge nasazení
4. **Zátěžové testy**: Hodnoťte výkon za různých zátěžových podmínek

### Fáze 5: Příprava na nasazení
1. **Konečná optimalizace**: Aplikujte konečné optimalizace na základě výsledků testů
2. **Vytvoření balíčku pro nasazení**: Zabalte modely a kód pro edge nasazení
3. **Dokumentace**: Zdokumentujte požadavky a konfiguraci nasazení
4. **Nastavení monitorování**: Připravte monitoring a logování pro edge nasazení

## Cílová skupina pro vývoj Edge AI

### Vývojáři Edge AI
- Vývojáři aplikací pro AI poháněná edge zařízení a IoT řešení
- Vývojáři vestavěných systémů integrující AI schopnosti do zařízení s omezenými zdroji
- Mobilní vývojáři vytvářející AI aplikace přímo na zařízeních jako jsou chytré telefony a tablety

### Inženýři Edge AI
- AI inženýři optimalizující modely pro edge nasazení a spravující inference pipeline
- DevOps inženýři nasazující a spravující AI modely v distribuované edge infrastruktuře
- Výkonní inženýři optimalizující AI výpočty s ohledem na hardwarová omezení edge zařízení

### Výzkumníci a vzdělavatelé
- AI výzkumníci vyvíjející efektivní modely a algoritmy pro edge computing
- Vzdělavatelé vyučující koncepty Edge AI a demonstrující optimalizační techniky
- Studenti učící se výzvám a řešením v nasazení Edge AI

## Případy použití Edge AI

### Chytrá IoT zařízení
- **Rozpoznávání obrazu v reálném čase**: Nasazení počítačového vidění na IoT kamery a senzory
- **Zpracování hlasu**: Implementace rozpoznávání řeči a NLP na chytrých reproduktorech
- **Prediktivní údržba**: Spouštění modelů detekce anomálií na průmyslových edge zařízeních
- **Monitorování prostředí**: Nasazení analýzy dat ze senzorů pro environmentální aplikace

### Mobilní a vestavěné aplikace
- **Překlad přímo na zařízení**: Implementace modelů překladu, které fungují offline
- **Augmentovaná realita**: Nasazení rozpoznávání a sledování objektů v reálném čase pro AR aplikace
- **Monitorování zdraví**: Spouštění modelů analýzy zdraví na nositelných zařízeních a lékařské technice
- **Autonomní systémy**: Implementace rozhodovacích modelů pro drony, roboty a vozidla

### Edge computing infrastruktura
- **Edge datová centra**: Nasazení AI modelů v edge datových centrech pro aplikace s nízkou latencí
- **Integrace CDN**: Integrace AI procesních schopností do sítí pro doručování obsahu
- **5G Edge**: Využití 5G edge computingu pro AI poháněné aplikace
- **Fog computing**: Implementace AI zpracování v prostředích fog computingu

## Instalace a nastavení

### Instalace rozšíření
Nainstalujte rozšíření AI Toolkit přímo z Visual Studio Code Marketplace:

**ID rozšíření**: `ms-windows-ai-studio.windows-ai-studio`

**Způsoby instalace**:
1. **VS Code Marketplace**: Vyhledejte „AI Toolkit“ v přehledu rozšíření
2. **Příkazový řádek**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Přímá instalace**: Stáhněte z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Požadavky pro vývoj Edge AI
- **Visual Studio Code**: Doporučená nejnovější verze
- **Python prostředí**: Python 3.8+ s potřebnými AI knihovnami
- **ONNX Runtime** (volitelně): Pro inferenci ONNX modelů
- **Ollama** (volitelně): Pro lokální poskytování modelů
- **Nástroje pro hardwarovou akceleraci**: CUDA, OpenVINO nebo platformově specifické akcelerátory

### Počáteční konfigurace
1. **Aktivace rozšíření**: Otevřete VS Code a ověřte, že AI Toolkit je viditelný v Activity Baru
2. **Nastavení poskytovatelů modelů**: Nakonfigurujte přístup k GitHub, OpenAI, Anthropic nebo jiným poskytovatelům modelů
3. **Lokální prostředí**: Nastavte Python prostředí a nainstalujte potřebné balíčky
4. **Hardwarová akcelerace**: Nakonfigurujte GPU/NPU akceleraci, pokud je dostupná
5. **Integrace MCP**: Nastavte Model Context Protocol servery podle potřeby

### Kontrolní seznam pro první nastavení
- [ ] AI Toolkit rozšíření nainstalováno a aktivováno
- [ ] Katalog modelů přístupný a modely zjišťovatelné
- [ ] Playground funkční pro testování modelů
- [ ] Agent Builder dostupný pro vývoj promptů
- [ ] Lokální vývojové prostředí nakonfigurováno
- [ ] Hardwarová akcelerace (pokud dostupná) správně nastavena

## Začínáme s AI Toolkitem

### Rychlý start

Doporučujeme začít s modely hostovanými na GitHubu pro co nejplynulejší zkušenost:

1. **Instalace**: Postupujte podle [instalačního průvodce](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) pro nastavení AI Toolkitu pro vaše zařízení
2. **Objevování modelů**: V stromovém zobrazení rozšíření zvolte **CATALOG > Models** pro prozkoumání dostupných modelů
3. **Modely GitHub**: Začněte s modely hostovanými na GitHubu pro optimální integraci
4. **Testování v Playgroundu**: U jakékoli karty modelu vyberte **Try in Playground** pro zahájení experimentování s možnostmi modelu

### Kroky krok za krokem pro vývoj Edge AI

#### Krok 1: Prozkoumání a výběr modelu
1. Otevřete pohled AI Toolkitu v Activity Baru VS Code
2. Procházejte Katalog modelů pro modely vhodné pro edge nasazení
3. Filtrování podle poskytovatele (GitHub, ONNX, Ollama) podle vašich edge požadavků
4. Použijte **Try in Playground** k okamžitému testování schopností modelu

#### Krok 2: Vývoj agentů
1. Použijte **Prompt (Agent) Builder** k vytvoření edge-optimalizovaných AI agentů
2. Generujte startovací prompty pomocí popisů v přirozeném jazyce
3. Iterujte a dolaďujte prompty podle odpovědí modelu
4. Integrujte MCP nástroje pro rozšířené schopnosti agentů


#### Krok 3: Testování a hodnocení
1. Použijte **Bulk Run** k testování více promptů napříč vybranými modely
2. Spusťte agenty s testovacími případy pro ověření funkčnosti
3. Vyhodnoťte přesnost a výkon pomocí vestavěných nebo vlastních metrik
4. Porovnejte různé modely a konfigurace

#### Krok 4: Doladění a optimalizace
1. Přizpůsobte modely pro specifické případy použití na edge zařízení
2. Aplikujte doménově specifické doladění
3. Optimalizujte pro omezení nasazení na edge
4. Verzionujte a porovnávejte různé konfigurace agentů

#### Krok 5: Příprava nasazení
1. Generujte produkční kód pomocí Agent Builderu
2. Nastavte připojení k MCP serverům pro produkční použití
3. Připravte balíčky nasazení pro edge zařízení
4. Nakonfigurujte metriky monitorování a hodnocení

## Vzorky pro AI Toolkit

Vyzkoušejte naše vzorky
[Vzorky AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) jsou navrženy tak, aby pomohly vývojářům a výzkumníkům efektivně zkoumat a implementovat AI řešení.

Naše vzorky zahrnují:

Vzorkový kód: Předpřipravené příklady k předvedení AI funkcionalit, jako je trénování, nasazení nebo integrace modelů do aplikací.
Dokumentace: Průvodce a návody, které uživatelům pomáhají porozumět funkcím AI Toolkitu a jejich použití.
Požadavky

- Visual Studio Code
- AI Toolkit pro Visual Studio Code
- GitHub token s jemným řízením přístupu (PAT)
- Foundry Local

## Nejlepší praktiky pro Edge AI vývoj

### Výběr modelu
- **Velikostní omezení**: Vyberte modely, které se vejdou do paměťových limitů cílových zařízení
- **Rychlost inference**: Upřednostněte modely s rychlými dobami inference pro aplikace v reálném čase
- **Kompromisy přesnosti**: Vyvažte přesnost modelu s omezeními zdrojů
- **Kompatibilita formátu**: Preferujte formáty ONNX nebo hardwarově optimalizované pro nasazení na edge

### Optimalizační techniky
- **Kvantizace**: Použijte kvantizaci INT8 nebo INT4 ke snížení velikosti modelu a zlepšení rychlosti
- **Pruning**: Odstraňte nepotřebné parametry modelu ke snížení výpočetních nároků
- **Distilace znalostí**: Vytvořte menší modely, které si zachovávají výkon větších
- **Hardwarová akcelerace**: Využijte NPUs, GPU nebo specializované akcelerátory, pokud jsou k dispozici

### Vývojový proces
- **Iterativní testování**: Testujte často za podmínek podobných edge během vývoje
- **Monitorování výkonu**: Neustále sledujte využití zdrojů a rychlost inference
- **Správa verzí**: Sledujte verze modelů a nastavení optimalizace
- **Dokumentace**: Dokumentujte všechna rozhodnutí o optimalizaci a kompromisy výkonu

### Úvahy o nasazení
- **Monitorování zdrojů**: Sledujte paměť, CPU a spotřebu energie v produkci
- **Záložní strategie**: Implementujte záložní mechanismy pro případ selhání modelu
- **Mechanismy aktualizace**: Plánujte aktualizace modelů a správu verzí
- **Bezpečnost**: Nasazujte vhodná bezpečnostní opatření pro edge AI aplikace

## Integrace s Edge AI frameworky

### ONNX Runtime
- **Multiplatformní nasazení**: Nasazujte ONNX modely napříč různými edge platformami
- **Hardwarová optimalizace**: Využijte hardwarově specifické optimalizace ONNX Runtime
- **Podpora mobilních zařízení**: Používejte ONNX Runtime Mobile pro aplikace na smartphonech a tabletech
- **Integrace IoT**: Nasazujte na IoT zařízení pomocí lehkých distribucí ONNX Runtime

### Windows ML
- **Zařízení Windows**: Optimalizujte pro edge zařízení a PC založená na Windows
- **NPU akcelerace**: Využijte Neural Processing Units na zařízeních Windows
- **DirectML**: Používejte DirectML pro GPU akceleraci na Windows platformách
- **Integrace UWP**: Integrujte s aplikacemi Universal Windows Platform

### TensorFlow Lite
- **Optimalizace pro mobilní zařízení**: Nasazujte modely TensorFlow Lite na mobilních a embedded zařízeních
- **Hardwarové delegáty**: Využívejte specializované hardwarové delegáty pro akceleraci
- **Mikrořadiče**: Nasazujte na mikrokontrolérech pomocí TensorFlow Lite Micro
- **Multiplatformní podpora**: Nasazujte v Androidu, iOS a embedded Linux systémech

### Azure IoT Edge
- **Hybrid cloud-edge**: Kombinujte cloudové trénování s edge inferencí
- **Nasazení modulů**: Nasazujte AI modely jako IoT Edge moduly
- **Správa zařízení**: Spravujte edge zařízení a aktualizace modelů vzdáleně
- **Telemetrie**: Shromažďujte údaje o výkonu a metriky modelů z edge nasazení

## Pokročilé scénáře Edge AI

### Nasazení více modelů
- **Ensemble modely**: Nasazujte více modelů pro zlepšení přesnosti nebo redundance
- **A/B testování**: Současně testujte různé modely na edge zařízeních
- **Dynamický výběr**: Vyberte modely na základě aktuálních podmínek zařízení
- **Sdílení zdrojů**: Optimalizujte využití zdrojů mezi více nasazenými modely

### Federativní učení
- **Distribuované trénování**: Trénujte modely na více edge zařízeních
- **Ochrana soukromí**: Uchovávejte trénovací data lokálně a sdílejte vylepšení modelů
- **Kolektivní učení**: Umožněte zařízením učit se ze společných zkušeností
- **Koordinace edge-cloud**: Koordinujte učení mezi edge zařízeními a cloudovou infrastrukturou

### Zpracování v reálném čase
- **Zpracování streamu**: Zpracovávejte kontinuální datové toky na edge zařízeních
- **Nízká latence inference**: Optimalizujte pro minimální zpoždění inference
- **Dávkové zpracování**: Efektivně zpracovávejte dávky dat na edge zařízeních
- **Adaptivní zpracování**: Přizpůsobujte zpracování podle aktuálních schopností zařízení

## Řešení problémů při vývoji Edge AI

### Běžné problémy
- **Paměťová omezení**: Model je příliš velký pro paměť cílového zařízení
- **Rychlost inference**: Inference modelu je příliš pomalá pro požadavky v reálném čase
- **Zhoršení přesnosti**: Optimalizace snižuje přesnost modelu nepřijatelně
- **Hardwarová kompatibilita**: Model není kompatibilní s cílovým hardwarem

### Strategie ladění
- **Profilování výkonu**: Použijte sledovací funkce AI Toolkitu k identifikaci úzkých míst
- **Monitorování zdrojů**: Sledujte využití paměti a CPU během vývoje
- **Postupné testování**: Testujte optimalizace postupně, abyste izolovali problémy
- **Simulace hardwaru**: Použijte vývojové nástroje k simulaci cílového hardwaru

### Řešení optimalizace
- **Další kvantizace**: Aplikujte agresivnější kvantizační techniky
- **Architektura modelu**: Zvažte různé architektury modelu optimalizované pro edge
- **Optimalizace předzpracování**: Optimalizujte předzpracování dat pro omezení na edge
- **Optimalizace inference**: Používejte hardwarově specifické optimalizace inference

## Zdroje a další kroky

### Oficiální dokumentace
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)
- [Příručka instalace a nastavení](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [Dokumentace VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)
- [Dokumentace Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Komunita a podpora
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub Issues a návrhy funkcí](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord komunita](https://aka.ms/azureaifoundry/discord)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Technické zdroje
- [Dokumentace ONNX Runtime](https://onnxruntime.ai/)
- [Dokumentace Ollama](https://ollama.ai/)
- [Dokumentace Windows ML](https://docs.microsoft.com/en-us/windows/ai/)
- [Dokumentace Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Výukové cesty
- [Kurz základy Edge AI](../Module01/README.md)
- [Průvodce malými jazykovými modely](../Module02/README.md)
- [Strategie nasazení na Edge](../Module03/README.md)
- [Vývoj Edge AI pro Windows](./windowdeveloper.md)

### Další zdroje
- **Statistiky repozitáře**: více než 1,8k hvězdiček, 150+ forků, 18+ přispěvatelů
- **Licence**: MIT Licence
- **Bezpečnost**: Platí bezpečnostní politiky Microsoftu
- **Telemetrie**: Respektuje nastavení telemetrie ve VS Code

## Závěr

AI Toolkit pro Visual Studio Code představuje komplexní platformu pro moderní AI vývoj, nabízí zjednodušené možnosti vývoje agentů, což je zvláště cenné pro aplikace Edge AI. Díky rozsáhlému katalogu modelů podporujícím poskytovatele jako Anthropic, OpenAI, GitHub a Google, v kombinaci s lokálním spuštěním přes ONNX a Ollama, toolkit poskytuje flexibilitu potřebnou pro různé scénáře nasazení na edge.

Síla tohoto toolkitu spočívá v jeho integrovaném přístupu – od objevování modelů a experimentování v Playgroundu, přes sofistikovaný vývoj agentů pomocí Prompt Builderu, po komplexní možnosti hodnocení a bezproblémovou integraci nástrojů MCP. Pro vývojáře Edge AI to znamená rychlé prototypování a testování AI agentů před nasazením na edge, s možností rychlého iterování a optimalizace pro prostředí s omezenými zdroji.

Klíčové výhody pro vývoj Edge AI zahrnují:
- **Rychlé experimentování**: Rychle testujte modely a agenty před závazkem k nasazení na edge
- **Vícezdrojová flexibilita**: Přístup k modelům z různých zdrojů pro nalezení optimálních řešení na edge
- **Lokální vývoj**: Testujte s ONNX a Ollama pro offline vývoj respektující soukromí
- **Produkční připravenost**: Generujte kód připravený pro produkci a integrujte s externími nástroji přes MCP
- **Komplexní hodnocení**: Používejte vestavěné a vlastní metriky k ověření výkonu Edge AI

Jak AI pokračuje směrem k edge nasazením, AI Toolkit pro VS Code poskytuje vývojové prostředí a workflow potřebné pro budování, testování a optimalizaci inteligentních aplikací pro prostředí s omezenými zdroji. Ať už vyvíjíte IoT řešení, mobilní AI aplikace nebo embedded inteligentní systémy, bohatá funkční sada toolkitu a integrovaný workflow podporují celý životní cyklus vývoje Edge AI.

S pokračujícím vývojem a aktivní komunitou (více než 1,8k hvězdiček na GitHubu) zůstává AI Toolkit na čele vývojových nástrojů pro AI, neustále se vyvíjí, aby vyhověl potřebám moderních AI vývojářů budujících pro scénáře nasazení na edge.

[Next Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->