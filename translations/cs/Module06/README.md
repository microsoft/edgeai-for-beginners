# Kapitola 06: Agentické systémy SLM: Komplexní přehled

Oblast umělé inteligence prochází zásadní transformací, kdy se posouváme od jednoduchých chatbotů k sofistikovaným AI agentům poháněným malými jazykovými modely (SLM). Tento komplexní průvodce zkoumá tři klíčové aspekty moderních agentických systémů SLM: základní koncepty a strategie nasazení, schopnosti volání funkcí a revoluční integraci Model Context Protocol (MCP).

## [Sekce 1: Základy AI agentů a malých jazykových modelů](./01.IntroduceAgent.md)

První sekce vytváří základní porozumění AI agentům a malým jazykovým modelům, přičemž rok 2025 označuje jako rok AI agentů po éře chatbotů v roce 2023 a boomu copilotů v roce 2024. Tato sekce představuje **agentické AI systémy**, které myslí, plánují, používají nástroje a vykonávají úkoly s minimálním lidským zásahem.

### Klíčové koncepty:
- **Rámec klasifikace agentů**: Od jednoduchých reflexních agentů po učící se agenty, poskytující komplexní taxonomii pro různé výpočetní scénáře
- **Základy SLM**: Definování malých jazykových modelů jako modelů s méně než 10 miliardami parametrů, které dokážou provádět praktické inferenční úlohy na spotřebitelských zařízeních
- **Pokročilé optimalizační strategie**: Pokrytí nasazení ve formátu GGUF, technik kvantizace (Q4_K_M, Q5_K_S, Q8_0) a frameworků optimalizovaných pro edge, jako Llama.cpp a Apple MLX
- **SLM vs LLM kompromisy**: Ukázka 10-30× snížení nákladů při zachování efektivity pro 70-80 % typických úkolů agentů

Sekce uzavírá praktickými strategiemi nasazení pomocí Ollama, VLLM a edge řešení od Microsoftu, čímž se SLM stávají budoucností nákladově efektivního a soukromí zachovávajícího nasazení agentické AI.

## [Sekce 2: Volání funkcí v malých jazykových modelech](./02.FunctionCalling.md)

Druhá sekce se podrobně zabývá **schopnostmi volání funkcí**, mechanismem, který transformuje statické jazykové modely na dynamické AI agenty schopné interakce s reálným světem. Tento technický rozbor pokrývá kompletní workflow od detekce záměru po integraci odpovědí.

### Klíčové oblasti implementace:
- **Systematický workflow**: Detailní průzkum integrace nástrojů, definice funkcí, detekce záměru, generování JSON výstupů a externího provádění
- **Implementace specifické pro platformy**: Komplexní návody pro Phi-4-mini s Ollama, Qwen3 volání funkcí a integraci Microsoft Foundry Local
- **Pokročilé příklady**: Systémy spolupráce více agentů, dynamický výběr nástrojů a vzory integrace v podnicích s komplexním zpracováním chyb
- **Produkční aspekty**: Omezení rychlosti, auditní logování, bezpečnostní opatření a strategie optimalizace výkonu

Tato sekce poskytuje jak teoretické porozumění, tak praktické vzory implementace, umožňující vývojářům budovat robustní systémy volání funkcí, které zvládnou vše od jednoduchých API volání po komplexní vícekrokové podnikové workflow.

## [Sekce 3: Integrace Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Poslední sekce představuje **Model Context Protocol (MCP)**, revoluční rámec, který standardizuje, jak jazykové modely interagují s externími nástroji a systémy. Tato sekce ukazuje, jak MCP vytváří most mezi AI modely a reálným světem prostřednictvím dobře definovaných protokolů.

### Hlavní body integrace:
- **Architektura protokolu**: Vrstvený systémový design pokrývající aplikační vrstvu, klienta LLM, klienta MCP a vrstvu zpracování nástrojů
- **Podpora více backendů**: Flexibilní implementace podporující jak Ollama (lokální vývoj), tak vLLM (produkční) backendy
- **Protokoly připojení**: STDIO režim pro přímou komunikaci procesů a SSE režim pro HTTP-based streaming
- **Reálné aplikace**: Automatizace webu, zpracování dat a příklady integrace API s komplexním zpracováním chyb

Integrace MCP ukazuje, jak lze SLM rozšířit o externí schopnosti, kompenzovat jejich menší počet parametrů prostřednictvím rozšířené funkcionality a zároveň zachovat výhody lokálního nasazení a efektivního využití zdrojů.

## Strategické důsledky

Tyto tři sekce společně představují komplexní rámec pro pochopení a implementaci agentických systémů SLM. Evoluce od základních konceptů přes volání funkcí až po integraci MCP ukazuje jasnou cestu k demokratizovanému nasazení AI, kde:

- **Efektivita se setkává s schopnostmi** díky optimalizovaným malým modelům
- **Nákladová efektivita** umožňuje široké přijetí
- **Standardizované protokoly** zajišťují interoperabilitu
- **Lokální nasazení** zachovává soukromí a snižuje latenci

Tento vývoj představuje nejen technologický pokrok, ale také změnu paradigmatu směrem k dostupnějším, efektivnějším a praktičtějším AI systémům, které mohou efektivně fungovat v prostředích s omezenými zdroji a zároveň poskytovat sofistikované agentické schopnosti.

Kombinace SLM s pokročilými strategiemi nasazení, robustním voláním funkcí a standardizovanými protokoly pro integraci nástrojů staví tyto systémy jako základ pro další generaci AI agentů, kteří transformují způsob, jakým interagujeme s umělou inteligencí a těžíme z ní napříč průmysly a aplikacemi.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.