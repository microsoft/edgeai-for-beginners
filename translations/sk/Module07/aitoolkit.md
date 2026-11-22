# Nástrojový balík AI pre Visual Studio Code - Sprievodca vývojom Edge AI

## Úvod

Vitajte v komplexnom sprievodcovi používania nástrojového balíka AI pre Visual Studio Code pri vývoji Edge AI. Ako sa umelá inteligencia presúva z centralizovaného cloud computingu na rozptýlené edge zariadenia, vývojári potrebujú silné, integrované nástroje, ktoré zvládnu jedinečné výzvy edge nasadenia – od obmedzení zdrojov po požiadavky na offline prevádzku.

Nástrojový balík AI pre Visual Studio Code prekonáva tento rozdiel tým, že poskytuje kompletné vývojové prostredie špeciálne navrhnuté na budovanie, testovanie a optimalizáciu AI aplikácií, ktoré bežia efektívne na edge zariadeniach. Či už vyvíjate pre IoT senzory, mobilné zariadenia, zabudované systémy alebo edge servery, tento balík zjednodušuje celý váš vývojový pracovný tok v známom prostredí VS Code.

Tento sprievodca vás prevedie základnými konceptmi, nástrojmi a osvedčenými postupmi pri využívaní nástrojového balíka AI vo vašich projektoch Edge AI, od počiatočného výberu modelu až po produkčné nasadenie.

## Prehľad

Nástrojový balík AI pre Visual Studio Code je výkonné rozšírenie, ktoré zjednodušuje vývoj agentov a tvorbu AI aplikácií. Balík poskytuje rozsiahle možnosti preskúmania, vyhodnocovania a nasadenia AI modelov z rôznych poskytovateľov — vrátane Anthropic, OpenAI, GitHub, Google — pričom podporuje aj lokálne spúšťanie modelov pomocou ONNX a Ollama.

Čo odlišuje nástrojový balík AI, je jeho komplexný prístup k celému životnému cyklu vývoja AI. Na rozdiel od tradičných nástrojov AI, ktoré sa zameriavajú na jednotlivé aspekty, nástrojový balík AI poskytuje integrované prostredie pokrývajúce objavovanie modelov, experimentovanie, vývoj agentov, hodnotenie a nasadenie — všetko v známom prostredí VS Code.

Platforma je špeciálne navrhnutá na rýchly prototyp a produkčné nasadenie, s funkciami ako generovanie promptov, rýchle štarty, bezproblémové integrácie nástrojov MCP (Model Context Protocol) a rozsiahle možnosti hodnotenia. Pre vývoj Edge AI to znamená, že môžete efektívne vyvíjať, testovať a optimalizovať AI aplikácie pre edge nasadenie a pritom udržiavať celý vývojový pracovný tok v rámci VS Code.

## Výukové ciele

Na konci tohto sprievodcu budete schopní:

### Základné zručnosti
- **Inštalovať a konfigurovať** nástrojový balík AI pre Visual Studio Code pre pracovné toky Edge AI vývoja
- **Navigovať a využívať** rozhranie nástrojového balíka AI, vrátane Katalógu modelov, Hriště a Staviteľa agentov
- **Vybrať a vyhodnotiť** AI modely vhodné pre edge nasadenie na základe výkonu a obmedzení zdrojov
- **Konvertovať a optimalizovať** modely pomocou formátu ONNX a techník kvantizácie pre edge zariadenia

### Zručnosti pri vývoji Edge AI
- **Navrhovať a implementovať** Edge AI aplikácie pomocou integrovaného vývojového prostredia
- **Testovať modely** v podmienkach pripomínajúcich edge pomocou lokálneho inferenčného spúšťania a monitorovania zdrojov
- **Vytvárať a prispôsobovať** AI agentov optimalizovaných pre scénare edge nasadenia
- **Hodnotiť výkon modelov** pomocou metrík relevantných pre edge computing (latencia, využitie pamäte, presnosť)

### Optimalizácia a nasadenie
- **Aplikovať techniky kvantizácie a prúningu** na zníženie veľkosti modelu pri zachovaní prijateľného výkonu
- **Optimalizovať modely** pre špecifické edge hardvérové platformy vrátane CPU, GPU a NPU akcelerácie
- **Implementovať osvedčené postupy** pre Edge AI vývoj vrátane správy zdrojov a stratégií záložného fungovania
- **Pripraviť modely a aplikácie** na produkčné nasadenie na edge zariadeniach

### Pokročilé koncepty Edge AI
- **Integrovať s edge AI frameworkmi** vrátane ONNX Runtime, Windows ML a TensorFlow Lite
- **Implementovať architektúry s viacerými modelmi** a scenáre federatívneho učenia pre edge prostredia
- **Riešiť bežné problémy Edge AI** vrátane obmedzení pamäte, rýchlosti inference a kompatibility s hardvérom
- **Navrhovať stratégie monitorovania a logovania** Edge AI aplikácií v produkcii

### Praktické použitie
- **Stavať komplexné Edge AI riešenia** od výberu modelu cez nasadenie
- **Preukázať zručnosti** v edge-špecifických vývojových pracovných tokoch a optimalizačných technikách
- **Aplikovať naučené koncepty** na reálne prípady použitia Edge AI vrátane IoT, mobilných a zabudovaných aplikácií
- **Vyhodnotiť a porovnať** rôzne stratégie nasadenia Edge AI a ich kompromisy

## Kľúčové funkcie pre vývoj Edge AI

### 1. Katalóg modelov a objavovanie
- **Podpora viacerých poskytovateľov**: Prezerať a pristupovať k AI modelom od Anthropic, OpenAI, GitHub, Google a ďalších poskytovateľov
- **Integrácia lokálnych modelov**: Zjednodušené objavovanie ONNX a Ollama modelov pre edge nasadenie
- **GitHub modely**: Priama integrácia s hostovaním modelov GitHub pre zjednodušený prístup
- **Porovnanie modelov**: Porovnávať modely vedľa seba, aby ste našli optimálnu rovnováhu pre obmedzenia edge zariadení

### 2. Interaktívne hriště
- **Interaktívne testovacie prostredie**: Rýchle experimentovanie s možnosťami modelov v kontrolovanom prostredí
- **Podpora multimodality**: Testovať s obrázkami, textom a inými vstupmi typickými v edge scenároch
- **Experimentovanie v reálnom čase**: Okamžitá odozva na reakcie modelu a jeho výkon
- **Optimalizácia parametrov**: Doladiť parametre modelu pre požiadavky edge nasadenia

### 3. Staviteľ promptov (Agentov)
- **Generovanie prirodzeného jazyka**: Generovať úvodné prompty pomocou prirodzených jazykových popisov
- **Iteratívne doladenie**: Zlepšovať prompty na základe odpovedí modelu a jeho výkonu
- **Dezkripcia úloh**: Rozložiť zložité úlohy pomocou reťazenia promptov a štruktúrovaných výstupov
- **Podpora premenných**: Používať premenné v promptoch pre dynamické správanie agentov
- **Generovanie produkčného kódu**: Generovať produkčný kód pre rýchly vývoj aplikácií

### 4. Hromadné spúšťanie a vyhodnocovanie
- **Testovanie viacerých modelov**: Spúšťať viaceré prompty súčasne cez vybrané modely
- **Efektívne testovanie vo veľkom meradle**: Testovať rôzne vstupy a konfigurácie efektívne
- **Vlastné testovacie prípady**: Spúšťať agentov s testovacími prípadmi na overenie funkčnosti
- **Porovnanie výkonu**: Porovnávať výsledky naprieč rôznymi modelmi a konfiguráciami

### 5. Hodnotenie modelov pomocou datasetov
- **Štandardné metriky**: Testovať AI modely pomocou vstavaných vyhodnocovačov (F1 skóre, relevantnosť, podobnosť, koherencia)
- **Vlastné vyhodnocovače**: Vytvoriť vlastné hodnotiace metriky pre špecifické použitia
- **Integrácia datasetov**: Testovať modely na komplexných datasetoch
- **Meranie výkonu**: Kvantifikovať výkon modelov pre rozhodnutia o edge nasadení

### 6. Schopnosti doladenia
- **Prispôsobenie modelov**: Prispôsobiť modely pre konkrétne prípady použitia a domény
- **Špecializovaná adaptácia**: Adaptovať modely na špecializované domény a požiadavky
- **Optimalizácia pre edge**: Doladiť modely špeciálne pre obmedzenia edge nasadenia
- **Tréning špecifický pre doménu**: Vytvárať modely prispôsobené konkrétnym edge prípadom použitia

### 7. Integrácia MCP nástrojov
- **Pripojenie externých nástrojov**: Pripojiť agentov k externým nástrojom cez Model Context Protocol servery
- **Akcie v reálnom svete**: Umožniť agentom dotazovať sa v databázach, pristupovať k API alebo spúšťať vlastnú logiku
- **Existujúce MCP servery**: Používať nástroje z protokolov príkaz (stdio) alebo HTTP (server-sent event)
- **Vývoj vlastných MCP**: Postaviť a vytvoriť nové MCP servery s testovaním v Staviteľovi agentov

### 8. Vývoj a testovanie agentov
- **Podpora volania funkcií**: Umožniť agentom dynamicky vyvolávať externé funkcie
- **Testovanie integrácií v reálnom čase**: Testovať integrácie pomocou reálnych spustení a využívania nástrojov
- **Verzionovanie agentov**: Správa verzií agentov s možnosťou porovnávania výsledkov hodnotenia
- **Lokalné ladenie a sledovanie**: Lokálne schopnosti sledovania a ladenia pre vývoj agentov

## Pracovný tok vývoja Edge AI

### Fáza 1: Objavovanie a výber modelu
1. **Preskúmať katalóg modelov**: Použiť katalóg modelov na nájdenie modelov vhodných pre edge nasadenie
2. **Porovnať výkon**: Vyhodnotiť modely podľa veľkosti, presnosti a rýchlosti inferencie
3. **Testovať lokálne**: Použiť Ollama alebo ONNX modely na lokálne testovanie pred edge nasadením
4. **Posúdiť požiadavky na zdroje**: Určiť pamäťové a výpočtové potreby pre cieľové edge zariadenia

### Fáza 2: Optimalizácia modelu
1. **Konvertovať do ONNX**: Konvertovať vybrané modely do formátu ONNX pre kompatibilitu s edge
2. **Aplikovať kvantizáciu**: Zmenšiť veľkosť modelu pomocou INT8 alebo INT4 kvantizácie
3. **Optimalizácia hardvéru**: Optimalizovať pre cieľový edge hardvér (ARM, x86, špecializované akcelerátory)
4. **Overiť výkon**: Overiť, že optimalizované modely si zachovávajú prijateľnú presnosť

### Fáza 3: Vývoj aplikácie
1. **Navrhnúť agenta**: Použiť Staviteľa agentov na vytvorenie agentov optimalizovaných pre edge
2. **Inžinierstvo promptov**: Vypracovať prompty, ktoré efektívne fungujú s menšími edge modelmi
3. **Testovanie integrácie**: Testovať agentov v simulovaných edge podmienkach
4. **Generovanie kódu**: Generovať produkčný kód optimalizovaný pre edge nasadenie

### Fáza 4: Hodnotenie a testovanie
1. **Hromadné hodnotenie**: Testovať viaceré konfigurácie na nájdenie optimálnych edge nastavení
2. **Profilovanie výkonu**: Analyzovať rýchlosť inferencie, využitie pamäte a presnosť
3. **Simulácia edge**: Testovať v podmienkach podobných cieľovému edge prostrediu
4. **Stresové testovanie**: Hodnotiť výkon pod rôznym zaťažením

### Fáza 5: Príprava na nasadenie
1. **Konečná optimalizácia**: Aplikovať konečné optimalizácie na základe výsledkov testovania
2. **Balíkovanie nasadenia**: Zabaliť modely a kód pre edge nasadenie
3. **Dokumentácia**: Zdokumentovať požiadavky a konfiguráciu nasadenia
4. **Nastavenie monitorovania**: Pripraviť monitorovanie a logovanie pre edge nasadenie

## Cieľové publikum pre vývoj Edge AI

### Vývojári Edge AI
- Vývojári aplikácií budujúcich AI poháňané edge zariadenia a IoT riešenia
- Vývojári zabudovaných systémov integrujúci AI schopnosti do zariadení s obmedzenými zdrojmi
- Mobilní vývojári vytvárajúci AI aplikácie priamo na zariadeniach ako sú smartfóny a tablety

### Inžinieri Edge AI
- AI inžinieri optimalizujúci modely pre edge nasadenie a spravujúci inference pipeline
- DevOps inžinieri nasadzujúci a spravujúci AI modely v distribuovanej edge infraštruktúre
- Výkonní inžinieri optimalizujúci AI záťaže pre hardvérové obmedzenia edge

### Výskumníci a pedagógovia
- AI výskumníci vyvíjajúci efektívne modely a algoritmy pre edge computing
- Pedagógovia učiaci koncepty Edge AI a demonštrujúci optimalizačné techniky
- Študenti učící sa o výzvach a riešeniach v edge AI nasadení

## Prípady použitia Edge AI

### Inteligentné IoT zariadenia
- **Rozpoznávanie obrazov v reálnom čase**: Nasadiť počítačové videnie na IoT kamery a senzory
- **Spracovanie hlasu**: Implementovať rozpoznávanie reči a spracovanie prirodzeného jazyka na inteligentných reproduktoroch
- **Prediktívna údržba**: Spúšťať modely detekcie anomálií na priemyselných edge zariadeniach
- **Monitorovanie životného prostredia**: Nasadiť modely analýzy senzorových dát pre environmentálne aplikácie

### Mobilné a zabudované aplikácie
- **Preklad na zariadení**: Implementovať jazykové prekladové modely, ktoré fungujú offline
- **Rozšírená realita**: Nasadiť rozpoznávanie a sledovanie objektov v reálnom čase pre AR aplikácie
- **Monitorovanie zdravia**: Spúšťať modely analyzujúce zdravie na nositeľných zariadeniach a lekárskom vybavení
- **Autonómne systémy**: Implementovať rozhodovacie modely pre drony, roboty a vozidlá

### Infrastruktúra edge computingu
- **Edge dátové centrá**: Nasadiť AI modely v edge dátových centrách pre aplikácie s nízkou latenciou
- **Integrácia CDN**: Integrovať schopnosti spracovania AI do sieťí na doručovanie obsahu
- **5G Edge**: Využívať 5G edge computing pre AI poháňané aplikácie
- **Fog computing**: Implementovať spracovanie AI vo fog computing prostrediach

## Inštalácia a nastavenie

### Inštalácia rozšírenia
Nainštalujte rozšírenie AI Toolkit priamo z Visual Studio Code Marketplace:

**ID rozšírenia**: `ms-windows-ai-studio.windows-ai-studio`

**Spôsoby inštalácie**:
1. **VS Code Marketplace**: Vyhľadajte "AI Toolkit" v zobrazení Rozšírenia
2. **Príkazový riadok**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Priama inštalácia**: Stiahnite z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Predpoklady pre vývoj Edge AI
- **Visual Studio Code**: Odporúčaná najnovšia verzia
- **Python prostredie**: Python 3.8+ s potrebnými AI knižnicami
- **ONNX Runtime** (voliteľné): Pre inferenciu ONNX modelov
- **Ollama** (voliteľné): Pre lokálne poskytovanie modelov
- **Nástroje na hardvérovú akceleráciu**: CUDA, OpenVINO alebo platformovo špecifické akcelerátory

### Počiatočná konfigurácia
1. **Aktivácia rozšírenia**: Otvorte VS Code a overte, či sa nástrojový balík AI zobrazuje v Paneli aktivít
2. **Nastavenie poskytovateľa modelov**: Nakonfigurujte prístup k poskytovateľom modelov ako GitHub, OpenAI, Anthropic alebo iným
3. **Lokálne prostredie**: Nastavte Python prostredie a nainštalujte potrebné balíčky
4. **Hardvérová akcelerácia**: Nakonfigurujte GPU/NPU akceleráciu ak je k dispozícii
5. **Integrácia MCP**: Nastavte MCP servery podľa potreby

### Kontrolný zoznam pri prvom nastavení
- [ ] Rozšírenie AI Toolkit nainštalované a aktivované
- [ ] Katalóg modelov prístupný a možné modely objaviť
- [ ] Hrište funkčné pre testovanie modelov
- [ ] Staviteľ agentov prístupný pre vývoj promptov
- [ ] Lokálne vývojové prostredie nakonfigurované
- [ ] Hardvérová akcelerácia (ak je dostupná) správne nastavená

## Začíname s nástrojovým balíkom AI

### Rýchly štart

Odporúčame začať s modelmi hosťovanými na GitHub pre najplynulejší zážitok:

1. **Inštalácia**: Postupujte podľa [inštalačného sprievodcu](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) na nastavenie nástrojového balíka AI pre vaše zariadenie
2. **Objavovanie modelov**: V rozšírení v zobrazení stromu vyberte **CATALOG > Models** pre preskúmanie dostupných modelov
3. **GitHub modely**: Začnite s modelmi hosťovanými na GitHub pre optimálnu integráciu
4. **Testovanie na Hrišti**: Z akéhokoľvek modelového karty vyberte **Try in Playground** na začiatok experimentovania s možnosťami modelu

### Krok za krokom vývoj Edge AI

#### Krok 1: Preskúmanie a výber modelu
1. Otvorte zobrazenie nástrojového balíka AI v Paneli aktivít VS Code
2. Prezrite Katalóg modelov pre modely vhodné pre edge nasadenie
3. Filtrovať podľa poskytovateľa (GitHub, ONNX, Ollama) podľa vašich edge požiadaviek
4. Použiť **Try in Playground** na okamžité testovanie schopností modelu

#### Krok 2: Vývoj agenta
1. Použiť **Staviteľ promptov (Agentov)** na vytvorenie agentov optimalizovaných pre edge
2. Generovať úvodné prompty pomocou opisov v prirodzenom jazyku
3. Iterovať a doladiť prompty na základe odpovedí modelu
4. Integrovať MCP nástroje pre rozšírené schopnosti agentov


#### Krok 3: Testovanie a hodnotenie
1. Použite **Hromadné spustenie** na testovanie viacerých promptov naprieč vybranými modelmi
2. Spustite agentov s testovacími prípadmi na overenie funkčnosti
3. Vyhodnoťte presnosť a výkon pomocou vstavaných alebo vlastných metrík
4. Porovnajte rôzne modely a konfigurácie

#### Krok 4: Doladenie a optimalizácia
1. Prispôsobte modely pre špecifické použitia na okraji (edge)
2. Aplikujte doménovo špecifické doladenie
3. Optimalizujte pre obmedzenia nasadenia na okraji
4. Verzionujte a porovnávajte rôzne konfigurácie agentov

#### Krok 5: Príprava nasadenia
1. Generujte produkčný kód pomocou Agent Buildera
2. Nastavte pripojenia na MCP server pre produkčné použitie
3. Pripravte balíčky nasadenia pre zariadenia na okraji
4. Nakonfigurujte monitorovanie a vyhodnocovacie metriky

## Ukážky pre AI Toolkit

Vyskúšajte naše ukážky
[Ukážky AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) sú navrhnuté tak, aby pomohli vývojárom a výskumníkom efektívne objavovať a implementovať AI riešenia.

Naše ukážky zahŕňajú:

Ukážkový kód: Predpripravené príklady na demonštráciu AI funkcií, ako napríklad tréning, nasadzovanie alebo integrácia modelov do aplikácií.
Dokumentáciu: Sprievodcov a tutoriály na pomoc užívateľom pochopiť funkcie AI Toolkitu a ich použitie.
Predpoklady

- Visual Studio Code
- AI Toolkit pre Visual Studio Code
- GitHub jemnozrnný osobný prístupový token (PAT)
- Foundry Local

## Najlepšie postupy pre vývoj Edge AI

### Výber modelu
- **Veľkostné obmedzenia**: Vyberte modely, ktoré sa zmestia do pamäťových limitov cieľových zariadení
- **Rýchlosť inferencie**: Uprednostnite modely s rýchlou inferenciou pre aplikácie v reálnom čase
- **Kompromisy presnosti**: Vyvažujte presnosť modelu s obmedzeniami zdrojov
- **Kompatibilita formátov**: Preferujte ONNX alebo hardvérovo optimalizované formáty pre nasadenie na okraji

### Optimalizačné techniky
- **Kvantizácia**: Používajte kvantizáciu INT8 alebo INT4 na zníženie veľkosti modelu a zrýchlenie
- **Pruning (ořezávanie)**: Odstráňte zbytočné parametre modelu na zníženie výpočtových nárokov
- **Knowledge Distillation**: Vytvorte menšie modely, ktoré si zachovávajú výkon väčších modelov
- **Hardvérová akcelerácia**: Využite NPU, GPU alebo špecializované akcelerátory, keď sú dostupné

### Vývojový pracovný postup
- **Iteratívne testovanie**: Testujte často v podmienkach podobných okraju počas vývoja
- **Monitorovanie výkonu**: Neustále sledujte využitie zdrojov a rýchlosť inferencie
- **Správa verzií**: Sledujte verzie modelov a nastavenia optimalizácie
- **Dokumentácia**: Dokumentujte všetky rozhodnutia o optimalizáciách a kompromisy výkonu

### Úvahy pri nasadení
- **Monitorovanie zdrojov**: Sledujte pamäť, CPU a spotrebu energie v produkcii
- **Náhradné stratégie**: Implementujte záložné mechanizmy pre zlyhania modelov
- **Mechanizmy aktualizácie**: Plánujte aktualizácie modelov a správu verzií
- **Bezpečnosť**: Implementujte vhodné bezpečnostné opatrenia pre aplikácie Edge AI

## Integrácia s Edge AI Frameworkmi

### ONNX Runtime
- **Nasadenie naprieč platformami**: Nasadzujte ONNX modely na rôzne edge platformy
- **Hardvérová optimalizácia**: Využite hardvérovo špecifické optimalizácie ONNX Runtime
- **Podpora mobilných zariadení**: Použite ONNX Runtime Mobile pre aplikácie na smartfónoch a tabletoch
- **IoT integrácia**: Nasadzujte na IoT zariadeniach pomocou ľahkých distribúcií ONNX Runtime

### Windows ML
- **Windows zariadenia**: Optimalizujte pre edge zariadenia a PC s Windows
- **NPU akcelerácia**: Využite Neural Processing Units na Windows zariadeniach
- **DirectML**: Použite DirectML pre GPU akceleráciu na Windows platformách
- **Integrácia UWP**: Integrujte s aplikáciami Universal Windows Platform

### TensorFlow Lite
- **Mobilná optimalizácia**: Nasadzujte TensorFlow Lite modely na mobilné a zabudované zariadenia
- **Hardvérové delegáty**: Použite špecializované hardvérové delegáty na akceleráciu
- **Mikrokontroléry**: Nasadzujte na mikrokontroléroch pomocou TensorFlow Lite Micro
- **Podpora naprieč platformami**: Nasadzujte na Android, iOS a embedded Linux systémoch

### Azure IoT Edge
- **Hybrid cloud-edge**: Kombinujte cloudový tréning s inferenciou na okraji
- **Nasadenie modulov**: Nasadzujte AI modely ako IoT Edge moduly
- **Správa zariadení**: Spravujte edge zariadenia a aktualizácie modelov na diaľku
- **Telemetria**: Zbierajte výkonové údaje a metriky modelov z edge nasadení

## Pokročilé scenáre Edge AI

### Nasadenie viacerých modelov
- **Modelové zostavy**: Nasadzujte viaceré modely na zlepšenie presnosti alebo redundancie
- **A/B testovanie**: Testujte rôzne modely súčasne na edge zariadeniach
- **Dynamický výber**: Vyberajte modely podľa aktuálnych podmienok zariadenia
- **Zdieľanie zdrojov**: Optimalizujte využitie zdrojov medzi viacerými nasadenými modelmi

### Federované učenie
- **Distribuovaný tréning**: Trénujte modely na viacerých edge zariadeniach
- **Ochrana súkromia**: Zachovávajte tréningové dáta lokálne a zdieľajte iba zlepšenia modelu
- **Spolupracujúce učenie**: Umožnite zariadeniam učiť sa z kolektívnych skúseností
- **Koordinácia edge-cloud**: Koordinujte učenie medzi zariadeniami na okraji a cloudovou infraštruktúrou

### Spracovanie v reálnom čase
- **Spracovanie prúdov**: Spracovávajte kontinuálne dátové toky na edge zariadeniach
- **Inferencie s nízkou latenciou**: Optimalizujte pre minimálnu latenciu inferencie
- **Dávkové spracovanie**: Efektívne spracovávajte dávky dát na edge zariadeniach
- **Adaptívne spracovanie**: Prispôsobujte spracovanie podľa aktuálnych schopností zariadenia

## Riešenie problémov pri vývoji Edge AI

### Bežné problémy
- **Pamäťové obmedzenia**: Model je príliš veľký pre pamäť cieľového zariadenia
- **Rýchlosť inferencie**: Inferencia modelu je príliš pomalá pre požiadavky reálneho času
- **Zníženie presnosti**: Optimalizácia neakceptovateľne znižuje presnosť modelu
- **Hardvérová kompatibilita**: Model nie je kompatibilný s cieľovým hardvérom

### Stratégie ladenia
- **Profilovanie výkonu**: Použite funkcie sledovania AI Toolkitu na identifikáciu úzkych miest
- **Monitorovanie zdrojov**: Sledujte počas vývoja využitie pamäte a CPU
- **Postupné testovanie**: Testujte optimalizácie postupne, aby ste izolovali problémy
- **Simulácia hardvéru**: Používajte vývojové nástroje na simuláciu cieľového hardvéru

### Riešenia optimalizácie
- **Ďalšia kvantizácia**: Aplikujte agresívnejšie kvantizačné techniky
- **Architektúra modelu**: Zvážte rôzne architektúry modelov optimalizované pre edge
- **Optimalizácia predspracovania**: Optimalizujte predspracovanie dát pre edge obmedzenia
- **Optimalizácia inferencie**: Využite hardvérovo špecifické optimalizácie inferencie

## Zdroje a ďalšie kroky

### Oficiálna dokumentácia
- [Dokumentácia pre vývojárov AI Toolkit](https://aka.ms/AIToolkit/doc)
- [Príručka inštalácie a nastavenia](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [Dokumentácia VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)
- [Dokumentácia Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Komunita a podpora
- [GitHub repozitár AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub Issues a žiadosti o funkcie](https://aka.ms/AIToolkit/feedback)
- [Discord komunita Azure AI Foundry](https://aka.ms/azureaifoundry/discord)
- [Trh s rozšíreniami VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Technické zdroje
- [Dokumentácia ONNX Runtime](https://onnxruntime.ai/)
- [Dokumentácia Ollama](https://ollama.ai/)
- [Dokumentácia Windows ML](https://docs.microsoft.com/en-us/windows/ai/)
- [Dokumentácia Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Učebné cesty
- [Kurz základy Edge AI](../Module01/README.md)
- [Sprievodca malými jazykovými modelmi](../Module02/README.md)
- [Stratégie nasadenia na okraji](../Module03/README.md)
- [Vývoj Windows Edge AI](./windowdeveloper.md)

### Ďalšie zdroje
- **Štatistiky repozitára**: viac než 1,8 tisíca hviezdičiek, 150+ fork-ov, 18+ prispievateľov
- **Licencia**: MIT licencia
- **Bezpečnosť**: Vzťahujú sa bezpečnostné politiky Microsoftu
- **Telemetria**: Rešpektuje nastavenia telemetrie VS Code

## Záver

AI Toolkit pre Visual Studio Code predstavuje komplexnú platformu pre moderný AI vývoj, ktorá poskytuje zjednodušené možnosti vývoja agentov, čo je obzvlášť cenné pre aplikácie Edge AI. S rozsiahlym katalógom modelov podporujúcim poskytovateľov ako Anthropic, OpenAI, GitHub a Google, v kombinácii s lokálnym spustením prostredníctvom ONNX a Ollama, toolkit ponúka flexibilitu potrebnú pre rôzne scenáre nasadenia na okraji.

Silou toolkitu je integrovaný prístup — od objavovania a experimentovania s modelmi v Playground, cez sofistikovaný vývoj agentov s Prompt Builderom, komplexnú možnosť hodnotenia až po bezproblémovú integráciu nástroja MCP. Pre vývojárov Edge AI to znamená rýchle prototypovanie a testovanie AI agentov pred nasadením na okraji, s možnosťou rýchlej iterácie a optimalizácie pre prostredia s obmedzenými zdrojmi.

Kľúčové výhody pre vývoj Edge AI zahŕňajú:
- **Rýchle experimentovanie**: Rýchlo testujte modely a agentov pred záväzným nasadením na okraji
- **Flexibilita viacerých poskytovateľov**: Získajte prístup k modelom z rôznych zdrojov na nájdenie optimálnych riešení pre edge
- **Lokálny vývoj**: Testujte s ONNX a Ollama pre offline a súkromie zachovávajúci vývoj
- **Pripravenosť na produkciu**: Generujte produkčný kód a integrujte sa s externými nástrojmi cez MCP
- **Komplexné hodnotenie**: Používajte vstavané aj vlastné metriky na overenie výkonu Edge AI

Ako AI pokračuje v posune smerom k scenárom nasadenia na okraji, AI Toolkit pre VS Code poskytuje vývojové prostredie a pracovný postup potrebný na vytváranie, testovanie a optimalizáciu inteligentných aplikácií pre prostredia s obmedzenými zdrojmi. Či už vyvíjate IoT riešenia, mobilné AI aplikácie alebo embedded inteligentné systémy, komplexný súbor funkcií toolkitu a integrovaný pracovný postup podporujú celý životný cyklus vývoja Edge AI.

S pokračujúcim vývojom a aktívnou komunitou (viac než 1,8 tisíc hviezdičiek na GitHub-e) zostáva AI Toolkit na čele vývojových nástrojov AI, neustále sa vyvíja, aby spĺňal potreby moderných AI vývojárov vytvárajúcich aplikácie pre nasadenie na okraj.

[Ďalší Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->