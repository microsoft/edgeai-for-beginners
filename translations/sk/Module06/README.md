# Kapitola 06: SLM Agentické Systémy: Komplexný Prehľad

Oblasť umelej inteligencie prechádza zásadnou transformáciou, keď sa posúvame od jednoduchých chatbotov k sofistikovaným AI agentom poháňaným Malými Jazykovými Modelmi (SLM). Tento komplexný sprievodca skúma tri kľúčové aspekty moderných agentických systémov SLM: základné koncepty a stratégie nasadenia, schopnosti volania funkcií a revolučnú integráciu Model Context Protocol (MCP).

## [Sekcia 1: Základy AI Agentov a Malých Jazykových Modelov](./01.IntroduceAgent.md)

Prvá sekcia vytvára základné pochopenie AI agentov a Malých Jazykových Modelov, pričom rok 2025 označuje ako rok AI agentov po ére chatbotov v roku 2023 a boomu copilotov v roku 2024. Táto sekcia predstavuje **agentické AI systémy**, ktoré myslia, uvažujú, plánujú, používajú nástroje a vykonávajú úlohy s minimálnym zásahom človeka.

### Kľúčové Koncepty:
- **Rámec Klasifikácie Agentov**: Od jednoduchých reflexných agentov po učiace sa agentov, poskytujúci komplexnú taxonómiu pre rôzne výpočtové scenáre
- **Základy SLM**: Definovanie Malých Jazykových Modelov ako modelov s menej ako 10 miliardami parametrov, ktoré dokážu vykonávať praktické inferencie na spotrebiteľských zariadeniach
- **Pokročilé Optimalizačné Strategie**: Pokrytie nasadenia vo formáte GGUF, techniky kvantizácie (Q4_K_M, Q5_K_S, Q8_0) a rámce optimalizované pre edge, ako Llama.cpp a Apple MLX
- **Porovnanie SLM vs LLM**: Ukázanie 10-30× zníženia nákladov pri SLM, pričom si zachovávajú efektívnosť pre 70-80% typických úloh agentov

Sekcia končí praktickými stratégiami nasadenia pomocou Ollama, VLLM a riešení od Microsoftu pre edge, čím sa SLM stávajú budúcnosťou nákladovo efektívneho a súkromie zachovávajúceho nasadenia agentických AI.

## [Sekcia 2: Volanie Funkcií v Malých Jazykových Modeloch](./02.FunctionCalling.md)

Druhá sekcia sa podrobne zaoberá **schopnosťami volania funkcií**, mechanizmom, ktorý transformuje statické jazykové modely na dynamické AI agenty schopné interakcie s reálnym svetom. Táto technická analýza pokrýva kompletný pracovný postup od detekcie zámeru po integráciu odpovedí.

### Hlavné Oblasti Implementácie:
- **Systematický Pracovný Postup**: Detailné preskúmanie integrácie nástrojov, definície funkcií, detekcie zámeru, generovania JSON výstupu a externého vykonania
- **Implementácie Špecifické pre Platformu**: Komplexné návody pre Phi-4-mini s Ollama, Qwen3 volanie funkcií a integráciu Microsoft Foundry Local
- **Pokročilé Príklady**: Systémy spolupráce viacerých agentov, dynamický výber nástrojov a vzory integrácie pre podniky s komplexným spracovaním chýb
- **Produkčné Úvahy**: Obmedzovanie rýchlosti, auditovanie, bezpečnostné opatrenia a stratégie optimalizácie výkonu

Táto sekcia poskytuje teoretické pochopenie aj praktické vzory implementácie, umožňujúce vývojárom budovať robustné systémy volania funkcií, ktoré zvládnu všetko od jednoduchých API volaní po komplexné viacstupňové pracovné postupy pre podniky.

## [Sekcia 3: Integrácia Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Posledná sekcia predstavuje **Model Context Protocol (MCP)**, revolučný rámec, ktorý štandardizuje, ako jazykové modely interagujú s externými nástrojmi a systémami. Táto sekcia ukazuje, ako MCP vytvára most medzi AI modelmi a reálnym svetom prostredníctvom dobre definovaných protokolov.

### Hlavné Body Integrácie:
- **Architektúra Protokolu**: Vrstvený dizajn systému pokrývajúci aplikačnú vrstvu, klienta LLM, klienta MCP a vrstvu spracovania nástrojov
- **Podpora Viacerých Backendov**: Flexibilná implementácia podporujúca Ollama (lokálny vývoj) aj vLLM (produkcia) backendy
- **Protokoly Pripojenia**: STDIO režim pre priamu komunikáciu procesov a SSE režim pre HTTP streamovanie
- **Aplikácie v Reálnom Svete**: Automatizácia webu, spracovanie dát a príklady integrácie API s komplexným spracovaním chýb

Integrácia MCP ukazuje, ako môžu byť SLM rozšírené o externé schopnosti, kompenzujúc ich menší počet parametrov prostredníctvom zvýšenej funkčnosti, pričom si zachovávajú výhody lokálneho nasadenia a efektívneho využívania zdrojov.

## Strategické Dôsledky

Tieto tri sekcie spoločne predstavujú komplexný rámec pre pochopenie a implementáciu agentických systémov SLM. Evolúcia od základných konceptov cez volanie funkcií až po integráciu MCP demonštruje jasnú cestu k demokratizovanému nasadeniu AI, kde:

- **Efektivita sa stretáva so schopnosťou** vďaka optimalizovaným malým modelom
- **Nákladová efektívnosť** umožňuje široké prijatie
- **Štandardizované protokoly** zabezpečujú interoperabilitu
- **Lokálne nasadenie** zachováva súkromie a znižuje latenciu

Tento pokrok predstavuje nielen technologický posun, ale aj zmenu paradigmy smerom k prístupnejším, efektívnejším a praktickejším AI systémom, ktoré dokážu efektívne fungovať v prostrediach s obmedzenými zdrojmi a zároveň poskytovať sofistikované agentické schopnosti.

Kombinácia SLM s pokročilými stratégiami nasadenia, robustným volaním funkcií a štandardizovanými protokolmi integrácie nástrojov pozicionuje tieto systémy ako základ pre ďalšiu generáciu AI agentov, ktorí transformujú spôsob, akým interagujeme s umelou inteligenciou a využívame jej výhody naprieč odvetviami a aplikáciami.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.