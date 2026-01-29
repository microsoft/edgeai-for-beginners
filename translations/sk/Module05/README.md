# Kapitola 05: SLMOps - Komplexný sprievodca operáciami malých jazykových modelov

## Prehľad

SLMOps (Small Language Model Operations) predstavuje revolučný prístup k nasadzovaniu AI, ktorý kladie dôraz na efektivitu, nákladovú úspornosť a schopnosti edge computingu. Tento komplexný sprievodca pokrýva celý životný cyklus operácií SLM, od pochopenia základných konceptov až po implementáciu pripravenú na produkciu.

---

## [Sekcia 1: Úvod do SLMOps](./01.IntroduceSLMOps.md)

**Revolúcia v AI operáciách na okraji siete**

Táto úvodná kapitola predstavuje posun od tradičných veľkých AI operácií k operáciám malých jazykových modelov (SLMOps). Zistíte, ako SLMOps rieši kľúčové výzvy pri nasadzovaní AI vo veľkom rozsahu, pričom zachováva nákladovú efektívnosť a súlad s ochranou súkromia.

**Čo sa naučíte:**
- Vznik a význam SLMOps v modernej AI stratégii
- Ako SLMs spájajú výkon a efektívnosť zdrojov
- Základné operačné princípy vrátane inteligentného riadenia zdrojov a architektúry zameranej na ochranu súkromia
- Výzvy pri implementácii v reálnom svete a ich riešenia
- Strategický obchodný dopad a konkurenčné výhody

**Hlavná myšlienka:** SLMOps demokratizuje nasadzovanie AI tým, že sprístupňuje pokročilé schopnosti spracovania jazyka organizáciám s obmedzenou technickou infraštruktúrou, čo umožňuje rýchlejšie vývojové cykly a predvídateľnejšie prevádzkové náklady.

---

## [Sekcia 2: Distilácia modelov - Od teórie k praxi](./02.SLMOps-Distillation.md)

**Vytváranie efektívnych modelov prostredníctvom prenosu znalostí**

Distilácia modelov je základnou technikou na vytváranie menších, efektívnejších modelov, ktoré si zachovávajú výkon svojich väčších náprotivkov. Táto kapitola poskytuje komplexný návod na implementáciu distilačných pracovných postupov, ktoré prenášajú znalosti z veľkých učiteľských modelov na kompaktné študentské modely.

**Čo sa naučíte:**
- Základné koncepty a výhody distilácie modelov
- Dvojstupňový proces distilácie: generovanie syntetických dát a tréning študentského modelu
- Praktické stratégie implementácie pomocou najmodernejších modelov ako DeepSeek V3 a Phi-4-mini
- Distilačné pracovné postupy v Azure ML s praktickými príkladmi
- Najlepšie postupy pre ladenie hyperparametrov a hodnotiace stratégie
- Prípadové štúdie z reálneho sveta, ktoré demonštrujú významné zlepšenia nákladov a výkonu

**Hlavná myšlienka:** Distilácia modelov umožňuje organizáciám dosiahnuť 85% zníženie času inferencie a 95% zníženie požiadaviek na pamäť, pričom si zachováva 92% presnosti pôvodného modelu, čím sa pokročilé AI schopnosti stávajú prakticky nasaditeľné.

---

## [Sekcia 3: Jemné doladenie - Prispôsobenie modelov pre konkrétne úlohy](./03.SLMOps-Finetuing.md)

**Prispôsobenie predtrénovaných modelov vašim jedinečným požiadavkám**

Jemné doladenie transformuje všeobecné modely na špecializované riešenia prispôsobené vašim konkrétnym prípadom použitia a oblastiam. Táto kapitola pokrýva všetko od základného nastavenia parametrov až po pokročilé techniky ako LoRA a QLoRA na efektívne prispôsobenie modelov.

**Čo sa naučíte:**
- Komplexný prehľad metodológií jemného doladenia a ich aplikácií
- Rôzne typy jemného doladenia: úplné jemné doladenie, jemné doladenie efektívne na parametre (PEFT) a prístupy špecifické pre úlohy
- Praktická implementácia pomocou Microsoft Olive s praktickými príkladmi
- Pokročilé techniky vrátane tréningu s viacerými adaptérmi a optimalizácie hyperparametrov
- Najlepšie postupy pre prípravu dát, konfiguráciu tréningu a riadenie zdrojov
- Bežné výzvy a osvedčené riešenia pre úspešné projekty jemného doladenia

**Hlavná myšlienka:** Jemné doladenie s nástrojmi ako Microsoft Olive umožňuje organizáciám efektívne prispôsobiť predtrénované modely konkrétnym potrebám, pričom optimalizuje výkon a obmedzenia zdrojov, čím sprístupňuje najmodernejšiu AI pre rôzne aplikácie.

---

## [Sekcia 4: Nasadenie - Implementácia modelov pripravených na produkciu](./04.SLMOps.Deployment.md)

**Nasadenie jemne doladených modelov do produkcie pomocou Foundry Local**

Záverečná kapitola sa zameriava na kritickú fázu nasadenia, pokrývajúc konverziu modelov, kvantizáciu a konfiguráciu produkcie. Naučíte sa, ako nasadiť jemne doladené kvantizované modely pomocou Foundry Local pre optimálny výkon a využitie zdrojov.

**Čo sa naučíte:**
- Kompletné nastavenie prostredia a postupy inštalácie nástrojov
- Techniky konverzie a kvantizácie modelov pre rôzne scenáre nasadenia
- Konfigurácia nasadenia Foundry Local s optimalizáciami špecifickými pre model
- Metodológie benchmarkingu výkonu a validácie kvality
- Riešenie bežných problémov pri nasadení a stratégie optimalizácie
- Najlepšie postupy pre monitorovanie a údržbu produkcie

**Hlavná myšlienka:** Správna konfigurácia nasadenia s technikami kvantizácie môže dosiahnuť až 75% zníženie veľkosti modelu, pričom si zachováva prijateľnú kvalitu modelu, čo umožňuje efektívne produkčné nasadenia na rôznych hardvérových konfiguráciách.

---

## Začíname

Tento sprievodca je navrhnutý tak, aby vás previedol celou cestou SLMOps, od pochopenia základných konceptov až po implementáciu pripravenú na produkciu. Každá kapitola stavia na predchádzajúcej, poskytujúc teoretické znalosti aj praktické zručnosti implementácie.

Či už ste dátový vedec, ktorý sa snaží optimalizovať nasadenie modelov, DevOps inžinier implementujúci AI operácie, alebo technický líder hodnotiaci SLMOps pre svoju organizáciu, tento komplexný sprievodca poskytuje znalosti a nástroje potrebné na úspešnú implementáciu operácií malých jazykových modelov.

**Pripravení začať?** Začnite s Kapitolou 1, aby ste pochopili základné princípy SLMOps a vybudovali si základy pre pokročilé techniky implementácie, ktoré sú pokryté v nasledujúcich kapitolách.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.