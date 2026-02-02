# AI Toolkit pre Visual Studio Code - Príručka pre vývoj Edge AI

## Úvod

Vitajte v komplexnej príručke na používanie AI Toolkit pre Visual Studio Code pri vývoji Edge AI. Ako sa umelá inteligencia presúva z centralizovaného cloudového výpočtového prostredia na distribuované edge zariadenia, vývojári potrebujú výkonné, integrované nástroje, ktoré zvládnu jedinečné výzvy nasadenia na edge - od obmedzených zdrojov až po požiadavky na offline prevádzku.

AI Toolkit pre Visual Studio Code prekonáva túto medzeru tým, že poskytuje kompletné vývojové prostredie špeciálne navrhnuté na vytváranie, testovanie a optimalizáciu AI aplikácií, ktoré efektívne fungujú na edge zariadeniach. Či už vyvíjate pre IoT senzory, mobilné zariadenia, vstavané systémy alebo edge servery, tento nástroj zjednodušuje celý váš vývojový proces v známom prostredí VS Code.

Táto príručka vás prevedie základnými konceptmi, nástrojmi a najlepšími postupmi pri využívaní AI Toolkit vo vašich Edge AI projektoch, od výberu modelu až po nasadenie do produkcie.

## Prehľad

AI Toolkit pre Visual Studio Code je výkonný doplnok, ktorý zjednodušuje vývoj agentov a tvorbu AI aplikácií. Toolkit poskytuje komplexné možnosti na skúmanie, hodnotenie a nasadenie AI modelov od širokej škály poskytovateľov—vrátane Anthropic, OpenAI, GitHub, Google—pričom podporuje lokálne spúšťanie modelov pomocou ONNX a Ollama.

Čo odlišuje AI Toolkit, je jeho komplexný prístup k celému životnému cyklu vývoja AI. Na rozdiel od tradičných nástrojov na vývoj AI, ktoré sa zameriavajú na jednotlivé aspekty, AI Toolkit poskytuje integrované prostredie, ktoré pokrýva objavovanie modelov, experimentovanie, vývoj agentov, hodnotenie a nasadenie—všetko v známom prostredí VS Code.

Platforma je špeciálne navrhnutá na rýchle prototypovanie a nasadenie do produkcie, s funkciami ako generovanie promptov, rýchle štartéry, bezproblémové integrácie MCP (Model Context Protocol) nástrojov a rozsiahle hodnotiace možnosti. Pre vývoj Edge AI to znamená, že môžete efektívne vyvíjať, testovať a optimalizovať AI aplikácie pre scenáre nasadenia na edge, pričom si zachováte celý vývojový proces v prostredí VS Code.

## Ciele učenia

Na konci tejto príručky budete schopní:

### Základné zručnosti
- **Nainštalovať a nakonfigurovať** AI Toolkit pre Visual Studio Code pre pracovné postupy vývoja Edge AI
- **Navigovať a využívať** rozhranie AI Toolkit, vrátane Model Catalog, Playground a Agent Builder
- **Vybrať a hodnotiť** AI modely vhodné pre nasadenie na edge na základe výkonu a obmedzení zdrojov
- **Konvertovať a optimalizovať** modely pomocou ONNX formátu a techník kvantizácie pre edge zariadenia

### Zručnosti vývoja Edge AI
- **Navrhnúť a implementovať** Edge AI aplikácie pomocou integrovaného vývojového prostredia
- **Testovať modely** v podmienkach podobných edge pomocou lokálneho inferencovania a monitorovania zdrojov
- **Vytvárať a prispôsobovať** AI agentov optimalizovaných pre scenáre nasadenia na edge
- **Hodnotiť výkon modelov** pomocou metrík relevantných pre edge výpočty (latencia, využitie pamäte, presnosť)

### Optimalizácia a nasadenie
- **Použiť techniky kvantizácie a prerezávania** na zmenšenie veľkosti modelu pri zachovaní prijateľného výkonu
- **Optimalizovať modely** pre konkrétne edge hardvérové platformy vrátane CPU, GPU a NPU akcelerácie
- **Implementovať najlepšie postupy** pre vývoj Edge AI vrátane správy zdrojov a záložných stratégií
- **Pripraviť modely a aplikácie** na nasadenie do produkcie na edge zariadeniach

### Pokročilé koncepty Edge AI
- **Integrovať s edge AI frameworkmi** vrátane ONNX Runtime, Windows ML a TensorFlow Lite
- **Implementovať architektúry s viacerými modelmi** a scenáre federovaného učenia pre edge prostredia
- **Riešiť bežné problémy Edge AI** vrátane obmedzení pamäte, rýchlosti inferencovania a kompatibility hardvéru
- **Navrhnúť stratégie monitorovania a logovania** pre Edge AI aplikácie v produkcii

### Praktická aplikácia
- **Vytvoriť kompletné Edge AI riešenia** od výberu modelu po nasadenie
- **Preukázať zručnosti** v edge-špecifických vývojových pracovných postupoch a technikách optimalizácie
- **Aplikovať naučené koncepty** na reálne prípady použitia Edge AI vrátane IoT, mobilných a vstavaných aplikácií
- **Hodnotiť a porovnávať** rôzne stratégie nasadenia Edge AI a ich kompromisy

## Kľúčové funkcie pre vývoj Edge AI

### 1. Katalóg modelov a objavovanie
- **Podpora viacerých poskytovateľov**: Prehliadajte a pristupujte k AI modelom od Anthropic, OpenAI, GitHub, Google a ďalších poskytovateľov
- **Integrácia lokálnych modelov**: Zjednodušené objavovanie ONNX a Ollama modelov pre nasadenie na edge
- **GitHub modely**: Priama integrácia s hostingom modelov na GitHub pre zjednodušený prístup
- **Porovnanie modelov**: Porovnávajte modely vedľa seba, aby ste našli optimálnu rovnováhu pre obmedzenia edge zariadení

### 2. Interaktívne ihrisko (Playground)
- **Interaktívne testovacie prostredie**: Rýchle experimentovanie s schopnosťami modelov v kontrolovanom prostredí
- **Podpora multimodálnosti**: Testovanie s obrázkami, textom a ďalšími vstupmi typickými pre edge scenáre
- **Experimentovanie v reálnom čase**: Okamžitá spätná väzba na odpovede modelov a výkon
- **Optimalizácia parametrov**: Doladenie parametrov modelu pre požiadavky nasadenia na edge

### 3. Tvorca promptov (Agent Builder)
- **Generovanie prirodzeného jazyka**: Generujte štartovacie prompty pomocou popisov v prirodzenom jazyku
- **Iteratívne zdokonaľovanie**: Zlepšujte prompty na základe odpovedí modelov a výkonu
- **Rozklad úloh**: Rozdeľte zložité úlohy pomocou reťazenia promptov a štruktúrovaných výstupov
- **Podpora premenných**: Používajte premenné v promptoch pre dynamické správanie agentov
- **Generovanie produkčného kódu**: Generujte kód pripravený na produkciu pre rýchly vývoj aplikácií

### 4. Hromadné spúšťanie a hodnotenie
- **Testovanie viacerých modelov**: Spúšťajte viacero promptov na vybraných modeloch súčasne
- **Efektívne testovanie vo veľkom**: Testujte rôzne vstupy a konfigurácie efektívne
- **Vlastné testovacie prípady**: Spúšťajte agentov s testovacími prípadmi na overenie funkčnosti
- **Porovnanie výkonu**: Porovnávajte výsledky medzi rôznymi modelmi a konfiguráciami

### 5. Hodnotenie modelov pomocou dátových súborov
- **Štandardné metriky**: Testujte AI modely pomocou vstavaných hodnotiacich nástrojov (F1 skóre, relevancia, podobnosť, koherencia)
- **Vlastné hodnotiace nástroje**: Vytvorte vlastné hodnotiace metriky pre konkrétne prípady použitia
- **Integrácia dátových súborov**: Testujte modely na komplexných dátových súboroch
- **Meranie výkonu**: Kvantifikujte výkon modelov pre rozhodnutia o nasadení na edge

### 6. Možnosti doladenia
- **Prispôsobenie modelov**: Prispôsobte modely pre konkrétne prípady použitia a oblasti
- **Špecializovaná adaptácia**: Prispôsobte modely špecifickým oblastiam a požiadavkám
- **Optimalizácia pre edge**: Doladte modely špeciálne pre obmedzenia nasadenia na edge
- **Tréning špecifický pre oblasť**: Vytvárajte modely prispôsobené konkrétnym edge prípadom použitia

### 7. Integrácia MCP nástrojov
- **Pripojenie k externým nástrojom**: Pripojte agentov k externým nástrojom prostredníctvom serverov Model Context Protocol
- **Akcie v reálnom svete**: Umožnite agentom dotazovať sa na databázy, pristupovať k API alebo vykonávať vlastnú logiku
- **Existujúce MCP servery**: Používajte nástroje z príkazového riadku (stdio) alebo HTTP (server-sent event) protokolov
- **Vývoj vlastných MCP**: Vytvárajte a testujte nové MCP servery pomocou Agent Builder

### 8. Vývoj a testovanie agentov
- **Podpora volania funkcií**: Umožnite agentom dynamicky vyvolávať externé funkcie
- **Testovanie integrácie v reálnom čase**: Testujte integrácie s reálnymi spusteniami a používaním nástrojov
- **Verzovanie agentov**: Kontrola verzií agentov s možnosťou porovnania výsledkov hodnotenia
- **Lokalné sledovanie a ladenie**: Možnosti sledovania a ladenia pre vývoj agentov

## Pracovný postup vývoja Edge AI

### Fáza 1: Objavovanie a výber modelov
1. **Preskúmajte katalóg modelov**: Použite katalóg modelov na nájdenie modelov vhodných pre nasadenie na edge
2. **Porovnajte výkon**: Hodnoťte modely na základe veľkosti, presnosti a rýchlosti inferencovania
3. **Testujte lokálne**: Použite Ollama alebo ONNX modely na lokálne testovanie pred nasadením na edge
4. **Posúďte požiadavky na zdroje**: Určte potreby pamäte a výpočtového výkonu pre cieľové edge zariadenia

### Fáza 2: Optimalizácia modelov
1. **Konvertujte na ONNX**: Konvertujte vybrané modely na ONNX formát pre kompatibilitu s edge
2. **Použite kvantizáciu**: Zmenšite veľkosť modelu pomocou kvantizácie INT8 alebo INT4
3. **Optimalizácia hardvéru**: Optimalizujte pre cieľový edge hardvér (ARM, x86, špecializované akcelerátory)
4. **Validácia výkonu**: Overte, že optimalizované modely si zachovávajú prijateľnú presnosť

### Fáza 3: Vývoj aplikácií
1. **Návrh agentov**: Použite Agent Builder na vytvorenie AI agentov optimalizovaných pre edge
2. **Inžinierstvo promptov**: Vyvíjajte prompty, ktoré efektívne fungujú s menšími edge modelmi
3. **Testovanie integrácie**: Testujte agentov v simulovaných edge podmienkach
4. **Generovanie kódu**: Generujte produkčný kód optimalizovaný pre nasadenie na edge

### Fáza 4: Hodnotenie a testovanie
1. **Hromadné hodnotenie**: Testujte viacero konfigurácií na nájdenie optimálnych edge nastavení
2. **Profilovanie výkonu**: Analyzujte rýchlosť inferencovania, využitie pamäte a presnosť
3. **Simulácia edge**: Testujte v podmienkach podobných cieľovému prostrediu nasadenia na edge
4. **Záťažové testovanie**: Hodnoťte výkon pri rôznych podmienkach zaťaženia

### Fáza 5: Príprava na nasadenie
1. **Finálna optimalizácia**: Použite finálne optimalizácie na základe výsledkov testovania
2. **Balenie na nasadenie**: Zabaľte modely a kód na nasadenie na edge
3. **Dokumentácia**: Dokumentujte požiadavky na nasadenie a konfiguráciu
4. **Príprava monitorovania**: Pripravte monitorovanie a logovanie pre nasadenie na edge

## Cieľová skupina pre vývoj Edge AI

### Vývojári Edge AI
- Vývojári aplikácií vytvárajúci AI-poháňané edge zariadenia a IoT riešenia
- Vývojári vstavaných systémov integrujúci AI schopnosti do zariadení s obmedzenými zdrojmi
- Mobilní vývojári vytvárajúci AI aplikácie na zariadeniach ako smartfóny a tablety

### Inžinieri Edge AI
- AI inžinieri optimalizujúci modely pre nasadenie na edge a spravujúci inferenčné pipeline
- DevOps inžinieri nasadzujúci a spravujúci AI modely na distribuovanej edge infraštruktúre
- Inžinieri výkonu optimalizujúci AI pracovné zaťaženie pre obmedzenia edge hardvéru

### Výskumníci a pedagógovia
- AI výskumníci vyvíjajúci efektívne modely a algoritmy pre edge výpočty
- Pedagógovia vyučujúci koncepty Edge AI a demonštrujúci techniky optimalizácie
- Študenti učia sa o výzvach a riešeniach pri nasadení Edge AI

## Prípady použitia Edge AI

### Inteligentné IoT zariadenia
- **Rozpoznávanie obrazu v reálnom čase**: Nasadenie modelov počítačového videnia na IoT kamerách a senzoroch
- **Spracovanie hlasu**: Implementácia rozpoznávania reči a spracovania prirodzeného jazyka na inteligentných reproduktoroch
- **Prediktívna údržba**: Spúšťanie modelov detekcie anomálií na priemyselných edge zariadeniach
- **Monitorovanie prostredia**: Nasadenie modelov analýzy senzorových dát pre environmentálne aplikácie

### Mobilné a vstavané aplikácie
- **Preklad na zariadení**: Implementácia modelov prekladu jazyka, ktoré fungujú offline
- **Rozšírená realita**: Nasadenie rozpoznávania objektov v reálnom čase a sledovania pre AR aplikácie
- **Monitorovanie zdravia**: Spúšťanie modelov analýzy zdravia na nositeľných zariadeniach a zdravotníckych prístrojoch
- **Autonómne systémy**: Implementácia modelov rozhodovania pre drony, roboty a vozidlá

### Edge výpočtová infraštruktúra
- **Edge dátové centrá**: Nasadenie AI modelov v edge dátových centrách pre aplikácie s nízkou latenciou
- **Integrácia CDN**: Integrácia AI schopností spracovania do sietí na doručovanie obsahu
- **5G Edge**: Využitie 5G edge výpočtov pre AI-poháňané aplikácie
- **Fog Computing**: Implementácia AI spracovania v prostrediach fog computingu

## Inštalácia a nastavenie

### Inštalácia rozšírenia
Nainštalujte rozšírenie AI Toolkit priamo z Visual Studio Code Marketplace:

**ID rozšírenia**: `ms-windows-ai-studio.windows-ai-studio`

**Metódy inštalácie**:
1. **VS Code Marketplace**: Vyhľadajte "AI Toolkit" v zobrazení rozšírení
2. **Príkazový riadok**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Priama inštalácia**: Stiahnite z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Predpoklady pre vývoj Edge AI
- **Visual Studio Code**: Odporúčaná najnovšia verzia
- **Python prostredie**: Python 3.8+ s požadovanými AI knižnicami
- **ONNX Runtime** (voliteľné): Pre inferenciu ONNX model
2. Generujte počiatočné výzvy pomocou popisov v prirodzenom jazyku  
3. Iterujte a zdokonaľujte výzvy na základe odpovedí modelu  
4. Integrujte nástroje MCP na rozšírenie schopností agentov  

#### Krok 3: Testovanie a hodnotenie  
1. Použite **Bulk Run** na testovanie viacerých výziev naprieč vybranými modelmi  
2. Spustite agentov s testovacími prípadmi na overenie funkčnosti  
3. Hodnoťte presnosť a výkon pomocou vstavaných alebo vlastných metrík  
4. Porovnajte rôzne modely a konfigurácie  

#### Krok 4: Doladenie a optimalizácia  
1. Prispôsobte modely pre špecifické okrajové prípady použitia  
2. Aplikujte doladenie špecifické pre danú oblasť  
3. Optimalizujte pre obmedzenia nasadenia na okraji  
4. Vytvárajte verzie a porovnávajte rôzne konfigurácie agentov  

#### Krok 5: Príprava na nasadenie  
1. Generujte produkčne pripravený kód pomocou Agent Builder  
2. Nastavte pripojenia MCP servera na produkčné použitie  
3. Pripravte balíčky na nasadenie pre okrajové zariadenia  
4. Konfigurujte metriky monitorovania a hodnotenia  

## Ukážky pre AI Toolkit  

Vyskúšajte naše ukážky  
[Ukážky AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) sú navrhnuté tak, aby pomohli vývojárom a výskumníkom efektívne preskúmať a implementovať AI riešenia.  

Naše ukážky zahŕňajú:  

Ukážkový kód: Predpripravené príklady na demonštráciu funkcií AI, ako je tréning, nasadenie alebo integrácia modelov do aplikácií.  
Dokumentácia: Príručky a tutoriály, ktoré pomáhajú používateľom pochopiť funkcie AI Toolkit a ako ich používať.  
Predpoklady  

- Visual Studio Code  
- AI Toolkit pre Visual Studio Code  
- GitHub jemne zrnitý osobný prístupový token (PAT)  
- Foundry Local  

## Najlepšie postupy pre vývoj Edge AI  

### Výber modelu  
- **Obmedzenia veľkosti**: Vyberte modely, ktoré sa zmestia do pamäťových limitov cieľových zariadení  
- **Rýchlosť inferencie**: Uprednostnite modely s rýchlou inferenciou pre aplikácie v reálnom čase  
- **Kompromisy presnosti**: Vyvážte presnosť modelu s obmedzeniami zdrojov  
- **Kompatibilita formátov**: Preferujte ONNX alebo formáty optimalizované pre hardvér na nasadenie na okraji  

### Techniky optimalizácie  
- **Kvantizácia**: Použite kvantizáciu INT8 alebo INT4 na zmenšenie veľkosti modelu a zlepšenie rýchlosti  
- **Prerezávanie**: Odstráňte nepotrebné parametre modelu na zníženie výpočtových požiadaviek  
- **Destilácia znalostí**: Vytvorte menšie modely, ktoré si zachovajú výkon väčších modelov  
- **Hardvérová akcelerácia**: Využite NPUs, GPUs alebo špecializované akcelerátory, ak sú dostupné  

### Pracovný postup vývoja  
- **Iteratívne testovanie**: Testujte často v podmienkach podobných okraju počas vývoja  
- **Monitorovanie výkonu**: Neustále monitorujte využitie zdrojov a rýchlosť inferencie  
- **Kontrola verzií**: Sledujte verzie modelov a nastavenia optimalizácie  
- **Dokumentácia**: Dokumentujte všetky rozhodnutia o optimalizácii a kompromisy výkonu  

### Úvahy o nasadení  
- **Monitorovanie zdrojov**: Monitorujte pamäť, CPU a spotrebu energie v produkcii  
- **Stratégie zálohovania**: Implementujte mechanizmy zálohovania pre zlyhania modelu  
- **Mechanizmy aktualizácie**: Plánujte aktualizácie modelov a správu verzií  
- **Bezpečnosť**: Implementujte vhodné bezpečnostné opatrenia pre aplikácie Edge AI  

## Integrácia s rámcami Edge AI  

### ONNX Runtime  
- **Nasadenie naprieč platformami**: Nasadzujte ONNX modely na rôznych okrajových platformách  
- **Optimalizácia hardvéru**: Využite hardvérové špecifické optimalizácie ONNX Runtime  
- **Podpora mobilných zariadení**: Použite ONNX Runtime Mobile pre aplikácie na smartfónoch a tabletoch  
- **Integrácia IoT**: Nasadzujte na IoT zariadeniach pomocou ľahkých distribúcií ONNX Runtime  

### Windows ML  
- **Windows zariadenia**: Optimalizujte pre okrajové zariadenia a PC založené na Windows  
- **Akcelerácia NPU**: Využite Neural Processing Units na zariadeniach Windows  
- **DirectML**: Použite DirectML na akceleráciu GPU na platformách Windows  
- **Integrácia UWP**: Integrujte s aplikáciami Universal Windows Platform  

### TensorFlow Lite  
- **Optimalizácia pre mobilné zariadenia**: Nasadzujte TensorFlow Lite modely na mobilných a zabudovaných zariadeniach  
- **Hardvérové delegáty**: Použite špecializované hardvérové delegáty na akceleráciu  
- **Mikrokontroléry**: Nasadzujte na mikrokontroléroch pomocou TensorFlow Lite Micro  
- **Podpora naprieč platformami**: Nasadzujte na Android, iOS a zabudované Linux systémy  

### Azure IoT Edge  
- **Hybrid cloud-okraj**: Kombinujte tréning v cloude s inferenciou na okraji  
- **Nasadenie modulov**: Nasadzujte AI modely ako moduly IoT Edge  
- **Správa zariadení**: Spravujte okrajové zariadenia a aktualizácie modelov na diaľku  
- **Telemetria**: Zbierajte údaje o výkone a metriky modelov z nasadení na okraji  

## Pokročilé scenáre Edge AI  

### Nasadenie viacerých modelov  
- **Modelové súbory**: Nasadzujte viacero modelov na zlepšenie presnosti alebo redundancie  
- **A/B testovanie**: Testujte rôzne modely súčasne na okrajových zariadeniach  
- **Dynamický výber**: Vyberajte modely na základe aktuálnych podmienok zariadenia  
- **Zdieľanie zdrojov**: Optimalizujte využitie zdrojov naprieč viacerými nasadenými modelmi  

### Federované učenie  
- **Distribuovaný tréning**: Trénujte modely na viacerých okrajových zariadeniach  
- **Zachovanie súkromia**: Uchovávajte tréningové údaje lokálne pri zdieľaní zlepšení modelu  
- **Kolaboratívne učenie**: Umožnite zariadeniam učiť sa zo spoločných skúseností  
- **Koordinácia okraj-cloud**: Koordinujte učenie medzi okrajovými zariadeniami a cloudovou infraštruktúrou  

### Spracovanie v reálnom čase  
- **Spracovanie streamov**: Spracovávajte kontinuálne dátové toky na okrajových zariadeniach  
- **Inferencia s nízkou latenciou**: Optimalizujte pre minimálnu latenciu inferencie  
- **Spracovanie dávok**: Efektívne spracovávajte dávky dát na okrajových zariadeniach  
- **Adaptívne spracovanie**: Prispôsobte spracovanie na základe aktuálnych schopností zariadenia  

## Riešenie problémov pri vývoji Edge AI  

### Bežné problémy  
- **Pamäťové obmedzenia**: Model je príliš veľký pre pamäť cieľového zariadenia  
- **Rýchlosť inferencie**: Inferencia modelu je príliš pomalá pre požiadavky v reálnom čase  
- **Degradácia presnosti**: Optimalizácia znižuje presnosť modelu neprijateľne  
- **Kompatibilita hardvéru**: Model nie je kompatibilný s cieľovým hardvérom  

### Stratégie ladenia  
- **Profilovanie výkonu**: Použite funkcie sledovania AI Toolkit na identifikáciu úzkych miest  
- **Monitorovanie zdrojov**: Monitorujte pamäť a využitie CPU počas vývoja  
- **Postupné testovanie**: Testujte optimalizácie postupne na izolovanie problémov  
- **Simulácia hardvéru**: Použite vývojové nástroje na simuláciu cieľového hardvéru  

### Riešenia optimalizácie  
- **Ďalšia kvantizácia**: Aplikujte agresívnejšie techniky kvantizácie  
- **Architektúra modelu**: Zvážte rôzne architektúry modelov optimalizované pre okraj  
- **Optimalizácia predspracovania**: Optimalizujte predspracovanie dát pre obmedzenia okraja  
- **Optimalizácia inferencie**: Použite optimalizácie inferencie špecifické pre hardvér  

## Zdroje a ďalšie kroky  

### Oficiálna dokumentácia  
- [Dokumentácia pre vývojárov AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Príručka inštalácie a nastavenia](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentácia inteligentných aplikácií VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentácia Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Komunita a podpora  
- [GitHub repozitár AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub problémy a požiadavky na funkcie](https://aka.ms/AIToolkit/feedback)  
- [Discord komunita Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Trh rozšírení VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technické zdroje  
- [Dokumentácia ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentácia Ollama](https://ollama.ai/)  
- [Dokumentácia Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentácia Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Cesty učenia  
- [Kurz základov Edge AI](../Module01/README.md)  
- [Príručka malých jazykových modelov](../Module02/README.md)  
- [Stratégie nasadenia na okraji](../Module03/README.md)  
- [Vývoj Edge AI pre Windows](./windowdeveloper.md)  

### Ďalšie zdroje  
- **Štatistiky repozitára**: 1.8k+ hviezdičiek, 150+ forkov, 18+ prispievateľov  
- **Licencia**: MIT License  
- **Bezpečnosť**: Platí bezpečnostná politika Microsoftu  
- **Telemetria**: Rešpektuje nastavenia telemetrie VS Code  

## Záver  

AI Toolkit pre Visual Studio Code predstavuje komplexnú platformu pre moderný vývoj AI, poskytujúcu zjednodušené schopnosti vývoja agentov, ktoré sú obzvlášť cenné pre aplikácie Edge AI. S rozsiahlym katalógom modelov podporujúcim poskytovateľov ako Anthropic, OpenAI, GitHub a Google, v kombinácii s lokálnym vykonávaním prostredníctvom ONNX a Ollama, ponúka toolkit flexibilitu potrebnú pre rôznorodé scenáre nasadenia na okraji.  

Silnou stránkou toolkitu je jeho integrovaný prístup – od objavovania modelov a experimentovania v Playground až po sofistikovaný vývoj agentov s Prompt Builder, komplexné hodnotiace schopnosti a bezproblémovú integráciu nástrojov MCP. Pre vývojárov Edge AI to znamená rýchle prototypovanie a testovanie AI agentov pred nasadením na okraj, s možnosťou rýchlej iterácie a optimalizácie pre prostredia s obmedzenými zdrojmi.  

Kľúčové výhody pre vývoj Edge AI zahŕňajú:  
- **Rýchle experimentovanie**: Rýchle testovanie modelov a agentov pred nasadením na okraj  
- **Flexibilita viacerých poskytovateľov**: Prístup k modelom z rôznych zdrojov na nájdenie optimálnych riešení pre okraj  
- **Lokálny vývoj**: Testovanie s ONNX a Ollama pre offline a súkromný vývoj  
- **Pripravenosť na produkciu**: Generovanie produkčne pripraveného kódu a integrácia s externými nástrojmi prostredníctvom MCP  
- **Komplexné hodnotenie**: Použitie vstavaných a vlastných metrík na overenie výkonu Edge AI  

Ako sa AI naďalej presúva k scenárom nasadenia na okraji, AI Toolkit pre VS Code poskytuje vývojové prostredie a pracovný postup potrebný na vytváranie, testovanie a optimalizáciu inteligentných aplikácií pre prostredia s obmedzenými zdrojmi. Či už vyvíjate IoT riešenia, mobilné AI aplikácie alebo zabudované inteligentné systémy, komplexná sada funkcií toolkitu a integrovaný pracovný postup podporujú celý životný cyklus vývoja Edge AI.  

S neustálym vývojom a aktívnou komunitou (1.8k+ hviezdičiek na GitHub), AI Toolkit zostáva na čele nástrojov pre vývoj AI, neustále sa vyvíjajúc, aby vyhovoval potrebám moderných vývojárov AI, ktorí budujú scenáre nasadenia na okraji.  

[Next Foundry Local](./foundrylocal.md)  

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.