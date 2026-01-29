# Kapitola 03: Nasadzovanie malých jazykových modelov (SLM)

Táto komplexná kapitola skúma celý životný cyklus nasadzovania malých jazykových modelov (SLM), zahŕňajúc teoretické základy, praktické implementačné stratégie a produkčne pripravené kontajnerové riešenia. Kapitola je rozdelená do troch progresívnych sekcií, ktoré čitateľov vedú od základných konceptov až po pokročilé scenáre nasadzovania.

## Štruktúra kapitoly a vzdelávacia cesta

### **[Sekcia 1: Pokročilé učenie SLM - základy a optimalizácia](./01.SLMAdvancedLearning.md)**
Úvodná sekcia vytvára teoretický základ pre pochopenie malých jazykových modelov a ich strategického významu v nasadeniach AI na okraji siete. Táto sekcia zahŕňa:

- **Rámec klasifikácie parametrov**: Podrobný prieskum kategórií SLM od mikro SLM (100M-1,4B parametrov) po stredné SLM (14B-30B parametrov), so zameraním na modely ako Phi-4-mini-3.8B, séria Qwen3 a Google Gemma3, vrátane analýzy hardvérových požiadaviek a pamäťovej náročnosti pre jednotlivé úrovne modelov
- **Pokročilé techniky optimalizácie**: Komplexné pokrytie kvantizačných metód pomocou Llama.cpp, Microsoft Olive a Apple MLX rámcov, vrátane najnovšej BitNET 1-bit kvantizácie s praktickými ukážkami kódu zobrazujúcimi kvantizačné procesy a výsledky benchmarkov
- **Stratégie získavania modelov**: Hĺbková analýza ekosystému Hugging Face a katalógu modelov Azure AI Foundry pre nasadenie SLM na podnikovej úrovni, s ukážkami kódu na programové sťahovanie, validáciu a konverziu formátov modelov
- **API pre vývojárov**: Ukážky kódu v jazykoch Python, C++ a C#, ktoré demonštrujú načítanie modelov, vykonávanie inferencie a integráciu s populárnymi rámcami ako PyTorch, TensorFlow a ONNX Runtime

Táto základná sekcia zdôrazňuje rovnováhu medzi operačnou efektivitou, flexibilitou nasadenia a nákladovou efektívnosťou, ktorá robí SLM ideálnymi pre scenáre výpočtov na okraji siete, s praktickými ukážkami kódu, ktoré môžu vývojári priamo implementovať vo svojich projektoch.

### **[Sekcia 2: Nasadenie v lokálnom prostredí - riešenia zamerané na ochranu súkromia](./02.DeployingSLMinLocalEnv.md)**
Druhá sekcia prechádza od teórie k praktickej implementácii, zameriavajúc sa na stratégie lokálneho nasadenia, ktoré uprednostňujú suverenitu dát a operačnú nezávislosť. Kľúčové oblasti zahŕňajú:

- **Univerzálna platforma Ollama**: Komplexný prieskum nasadenia naprieč platformami so zameraním na vývojársky priateľské pracovné postupy, správu životného cyklu modelov a prispôsobenie prostredníctvom Modelfiles, vrátane kompletných ukážok integrácie REST API a automatizačných skriptov CLI
- **Microsoft Foundry Local**: Riešenia nasadenia na podnikovej úrovni s optimalizáciou založenou na ONNX, integráciou Windows ML a komplexnými bezpečnostnými funkciami, s ukážkami kódu v jazykoch C# a Python pre natívnu integráciu aplikácií
- **Porovnávacia analýza**: Podrobná porovnávacia analýza rámcov zahŕňajúca technickú architektúru, charakteristiky výkonu a optimalizačné pokyny pre použitie, s benchmarkovým kódom na hodnotenie rýchlosti inferencie a pamäťovej náročnosti na rôznom hardvéri
- **Integrácia API**: Ukážkové aplikácie demonštrujúce, ako vytvárať webové služby, chatovacie aplikácie a dátové spracovateľské potrubia pomocou lokálnych nasadení SLM, s ukážkami kódu v Node.js, Python Flask/FastAPI a ASP.NET Core
- **Testovacie rámce**: Automatizované testovacie prístupy na zabezpečenie kvality modelov, vrátane ukážok jednotkových a integračných testov pre implementácie SLM

Táto sekcia poskytuje praktické pokyny pre organizácie, ktoré chcú implementovať riešenia AI zamerané na ochranu súkromia, pričom si zachovávajú plnú kontrolu nad svojím prostredím nasadenia, s pripravenými ukážkami kódu, ktoré môžu vývojári prispôsobiť svojim špecifickým požiadavkám.

### **[Sekcia 3: Kontajnerové nasadenie v cloude - riešenia na produkčnej úrovni](./03.DeployingSLMinCloud.md)**
Záverečná sekcia sa zameriava na pokročilé stratégie kontajnerového nasadenia, pričom ako hlavná prípadová štúdia slúži Microsoft Phi-4-mini-instruct. Táto sekcia zahŕňa:

- **Nasadenie vLLM**: Optimalizácia inferencie s vysokým výkonom pomocou OpenAI-kompatibilných API, pokročilé GPU akcelerácie a konfigurácie na produkčnej úrovni, vrátane kompletných Dockerfile súborov, Kubernetes manifestov a parametrov ladenia výkonu
- **Orchestrácia kontajnerov Ollama**: Zjednodušené pracovné postupy nasadenia s Docker Compose, varianty optimalizácie modelov a integrácia webového UI, s ukážkami CI/CD potrubí na automatizované nasadenie a testovanie
- **Implementácia ONNX Runtime**: Nasadenie optimalizované pre okraj siete s komplexnou konverziou modelov, kvantizačnými stratégiami a kompatibilitou naprieč platformami, vrátane podrobných ukážok kódu na optimalizáciu a nasadenie modelov
- **Monitorovanie a pozorovateľnosť**: Implementácia dashboardov Prometheus/Grafana s vlastnými metrikami na monitorovanie výkonu SLM, vrátane konfigurácií upozornení a agregácie logov
- **Vyvažovanie záťaže a škálovanie**: Praktické príklady horizontálnych a vertikálnych stratégií škálovania s konfiguráciami automatického škálovania na základe využitia CPU/GPU a vzorcov požiadaviek
- **Zabezpečenie kontajnerov**: Najlepšie praktiky zabezpečenia kontajnerov vrátane zníženia privilégií, politík siete a správy tajomstiev pre API kľúče a prístupové údaje k modelom

Každý prístup k nasadeniu je prezentovaný s kompletnými konfiguráciami, postupmi testovania, kontrolnými zoznamami pripravenosti na produkciu a šablónami infraštruktúry ako kódu, ktoré môžu vývojári priamo použiť vo svojich pracovných postupoch nasadenia.

## Kľúčové výsledky učenia

Po absolvovaní tejto kapitoly čitatelia zvládnu:

1. **Strategický výber modelov**: Pochopenie hraníc parametrov a výber vhodných SLM na základe obmedzení zdrojov a požiadaviek na výkon
2. **Majstrovstvo v optimalizácii**: Implementácia pokročilých kvantizačných techník naprieč rôznymi rámcami na dosiahnutie optimálnej rovnováhy medzi výkonom a efektivitou
3. **Flexibilita nasadenia**: Výber medzi lokálnymi riešeniami zameranými na ochranu súkromia a škálovateľnými kontajnerovými nasadeniami na základe potrieb organizácie
4. **Pripravenosť na produkciu**: Konfigurácia systémov monitorovania, zabezpečenia a škálovania pre nasadenia SLM na podnikovej úrovni

## Praktická orientácia a aplikácie v reálnom svete

Kapitola si udržuje silnú praktickú orientáciu, zahŕňajúc:

- **Praktické príklady**: Kompletné konfiguračné súbory, postupy testovania API a skripty na nasadenie
- **Benchmarking výkonu**: Podrobné porovnania rýchlosti inferencie, pamäťovej náročnosti a požiadaviek na zdroje
- **Bezpečnostné aspekty**: Praktiky zabezpečenia na podnikovej úrovni, rámce súladu a stratégie ochrany dát
- **Najlepšie praktiky**: Usmernenia overené v produkcii pre monitorovanie, škálovanie a údržbu

## Perspektíva pripravená na budúcnosť

Kapitola sa uzatvára pohľadom na vznikajúce trendy, vrátane:

- Pokročilých architektúr modelov s lepšími pomermi efektivity
- Hlbšej integrácie hardvéru so špecializovanými AI akcelerátormi
- Vývoja ekosystému smerom k štandardizácii a interoperabilite
- Vzorov prijatia v podnikoch poháňaných ochranou súkromia a požiadavkami na súlad

Tento komplexný prístup zabezpečuje, že čitatelia sú dobre pripravení zvládnuť aktuálne výzvy nasadzovania SLM, ako aj budúce technologické vývojové trendy, pričom robia informované rozhodnutia, ktoré sú v súlade s ich špecifickými požiadavkami a obmedzeniami organizácie.

Kapitola slúži ako praktický sprievodca na okamžitú implementáciu a strategický zdroj na dlhodobé plánovanie nasadzovania AI, zdôrazňujúc kritickú rovnováhu medzi schopnosťami, efektivitou a operačnou dokonalosťou, ktorá definuje úspešné nasadenia SLM.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.