# Kapitola 07: Ukázky EdgeAI

Edge AI představuje spojení umělé inteligence s edge computingem, což umožňuje inteligentní zpracování přímo na zařízeních bez nutnosti připojení ke cloudu. Tato kapitola zkoumá pět různých implementací EdgeAI na různých platformách a v různých rámcích, které ukazují všestrannost a sílu provozování AI modelů na okraji.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano představuje průlom v dostupném edge AI computingu, poskytující až 67 TOPS výkonu AI v kompaktním formátu velikosti kreditní karty. Tato výkonná platforma pro edge AI demokratizuje vývoj generativní AI pro nadšence, studenty i profesionální vývojáře.

### Klíčové vlastnosti
- Poskytuje až 67 TOPS výkonu AI—zlepšení o 1,7X oproti předchozí generaci
- 1024 CUDA jader a až 32 Tensor jader pro AI zpracování
- 6jádrový procesor Arm Cortex-A78AE v8.2 64bit s maximální frekvencí 1,5 GHz
- Cena pouhých $249, což poskytuje vývojářům, studentům a tvůrcům nejdostupnější platformu

### Aplikace
Jetson Orin Nano vyniká při provozování moderních generativních AI modelů, včetně vision transformerů, velkých jazykových modelů a vision-language modelů. Je speciálně navržen pro použití v generativní AI a nyní můžete provozovat několik LLM na zařízení velikosti dlaně. Mezi oblíbené případy použití patří robotika poháněná AI, chytré drony, inteligentní kamery a autonomní edge zařízení.

**Více informací**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI v mobilních aplikacích s .NET MAUI a ONNX Runtime GenAI

Toto řešení ukazuje, jak integrovat generativní AI a velké jazykové modely (LLMs) do mobilních aplikací napříč platformami pomocí .NET MAUI (Multi-platform App UI) a ONNX Runtime GenAI. Tento přístup umožňuje .NET vývojářům vytvářet sofistikované mobilní aplikace poháněné AI, které běží nativně na zařízeních Android a iOS.

### Klíčové vlastnosti
- Postaveno na frameworku .NET MAUI, který poskytuje jednotný kódový základ pro aplikace na Androidu i iOS
- Integrace ONNX Runtime GenAI umožňuje provozování generativních AI modelů přímo na mobilních zařízeních
- Podpora různých hardwarových akcelerátorů přizpůsobených mobilním zařízením, včetně CPU, GPU a specializovaných mobilních AI procesorů
- Optimalizace specifické pro platformy, jako je CoreML pro iOS a NNAPI pro Android prostřednictvím ONNX Runtime
- Implementuje kompletní generativní AI smyčku včetně předzpracování, inferencí, zpracování logitů, vyhledávání a vzorkování a správy KV cache

### Výhody pro vývojáře
Přístup .NET MAUI umožňuje vývojářům využít jejich stávající znalosti C# a .NET při vytváření AI aplikací napříč platformami. Framework ONNX Runtime GenAI podporuje různé modelové architektury, včetně Llama, Mistral, Phi, Gemma a mnoha dalších. Optimalizované ARM64 jádra urychlují INT4 kvantizované násobení matic, což zajišťuje efektivní výkon na mobilním hardwaru při zachování známého prostředí pro vývoj v .NET.

### Případy použití
Toto řešení je ideální pro vývojáře, kteří chtějí vytvářet mobilní aplikace poháněné AI pomocí technologií .NET, včetně inteligentních chatbotů, aplikací pro rozpoznávání obrazu, nástrojů pro překlad jazyků a personalizovaných doporučovacích systémů, které běží zcela na zařízení pro zvýšené soukromí a offline schopnosti.

**Více informací**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI v Azure s Small Language Models Engine

Řešení EdgeAI od Microsoftu založené na Azure se zaměřuje na efektivní nasazení malých jazykových modelů (SLMs) v hybridních prostředích cloud-edge. Tento přístup překonává propast mezi AI službami v měřítku cloudu a požadavky na nasazení na okraji.

### Výhody architektury
- Bezproblémová integrace s Azure AI službami
- Provozování SLMs/LLMs a multimodálních modelů na zařízení i v cloudu pomocí ONNX Runtime
- Optimalizováno pro nasazení v měřítku podniků
- Podpora průběžných aktualizací a správy modelů

### Případy použití
Implementace Azure EdgeAI vyniká ve scénářích vyžadujících nasazení AI na podnikové úrovni s možnostmi správy v cloudu. To zahrnuje inteligentní zpracování dokumentů, analýzu v reálném čase a hybridní AI pracovní postupy, které využívají jak cloud, tak edge computingové zdroje.

**Více informací**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI s Windows ML](./windowdeveloper.md)

Windows ML představuje špičkový runtime od Microsoftu optimalizovaný pro výkonné inferenční modely na zařízení a zjednodušené nasazení, sloužící jako základ Windows AI Foundry. Tato platforma umožňuje vývojářům vytvářet aplikace pro Windows poháněné AI, které využívají plný potenciál PC hardwaru.

### Schopnosti platformy
- Funguje na všech PC s Windows 11, verze 24H2 (build 26100) nebo vyšší
- Funguje na všech x64 a ARM64 PC hardwaru, dokonce i na PC bez NPU nebo GPU
- Umožňuje vývojářům přinést vlastní modely a efektivně je nasadit napříč ekosystémem partnerů pro křemíkové čipy, včetně AMD, Intel, NVIDIA a Qualcomm, pokrývající CPU, GPU, NPU
- Díky infrastrukturním API již vývojáři nemusí vytvářet více verzí své aplikace pro různé křemíkové čipy

### Výhody pro vývojáře
Windows ML abstrahuje hardware a poskytovatele exekuce, takže se můžete soustředit na psaní svého kódu. Navíc se Windows ML automaticky aktualizuje, aby podporoval nejnovější NPU, GPU a CPU, jakmile jsou vydány. Platforma poskytuje jednotný rámec pro vývoj AI napříč různorodým ekosystémem hardwaru Windows.

**Více informací**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Komplexní průvodce vývojem Windows Edge AI

## [5. EdgeAI s Foundry Local Applications](./foundrylocal.md)

Foundry Local umožňuje vývojářům na Windows a Mac vytvářet aplikace pro Retrieval Augmented Generation (RAG) pomocí místních zdrojů v .NET, kombinující místní jazykové modely se schopnostmi sémantického vyhledávání. Tento přístup poskytuje řešení AI zaměřená na soukromí, která fungují zcela na místní infrastruktuře.

### Technická architektura
- Kombinuje jazykový model Phi, místní embeddings a Semantic Kernel pro vytvoření scénáře RAG
- Používá embeddings jako vektory (pole) hodnot s plovoucí desetinnou čárkou, které reprezentují obsah a jeho sémantický význam
- Semantic Kernel funguje jako hlavní orchestrátor, integrující Phi a chytré komponenty pro vytvoření bezproblémového RAG pipeline
- Podpora místních vektorových databází včetně SQLite a Qdrant

### Výhody implementace
RAG, neboli Retrieval Augmented Generation, je jen sofistikovaný způsob, jak říci „vyhledej nějaké informace a vlož je do promptu“. Tato místní implementace zajišťuje ochranu dat při poskytování inteligentních odpovědí založených na vlastních znalostních bázích. Tento přístup je obzvláště cenný pro podnikové scénáře vyžadující suverenitu dat a schopnosti offline provozu.

**Více informací**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local poskytuje REST server kompatibilní s OpenAI, poháněný ONNX Runtime pro provozování modelů lokálně na Windows. Níže je rychlé, ověřené shrnutí; podívejte se na oficiální dokumentaci pro úplné podrobnosti.

- Začít: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referenční příručka CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Kompletní průvodce pro Windows v tomto repozitáři: [foundrylocal.md](./foundrylocal.md)

Instalace nebo upgrade na Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Prozkoumejte kategorie CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Spusťte model a objevte dynamický endpoint:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Rychlá kontrola REST pro seznam modelů (nahraďte PORT ze statusu):
```cmd
curl -s http://localhost:PORT/v1/models
```

Tipy:
- Integrace SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Přineste vlastní model (kompilace): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Vývojové zdroje Windows EdgeAI

Pro vývojáře zaměřené specificky na platformu Windows jsme vytvořili komplexní průvodce, který pokrývá celý ekosystém Windows EdgeAI. Tento zdroj poskytuje podrobné informace o Windows AI Foundry, včetně API, nástrojů a osvědčených postupů pro vývoj EdgeAI na Windows.

### Platforma Windows AI Foundry
Platforma Windows AI Foundry poskytuje komplexní sadu nástrojů a API speciálně navržených pro vývoj Edge AI na zařízeních Windows. To zahrnuje specializovanou podporu pro hardware akcelerovaný NPU, integraci Windows ML a techniky optimalizace specifické pro platformu.

**Komplexní průvodce**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Tento průvodce pokrývá:
- Přehled platformy Windows AI Foundry a jejích komponent
- Phi Silica API pro efektivní inferenci na NPU hardwaru
- API pro počítačové vidění pro zpracování obrazu a OCR
- Integraci a optimalizaci runtime Windows ML
- Foundry Local CLI pro místní vývoj a testování
- Strategie optimalizace hardwaru pro zařízení Windows
- Praktické příklady implementace a osvědčené postupy

### [AI Toolkit pro vývoj Edge AI](./aitoolkit.md)
Pro vývojáře používající Visual Studio Code poskytuje rozšíření AI Toolkit komplexní vývojové prostředí speciálně navržené pro vytváření, testování a nasazování Edge AI aplikací. Tento toolkit zjednodušuje celý pracovní postup vývoje Edge AI v rámci VS Code.

**Průvodce vývojem**: [AI Toolkit pro vývoj Edge AI](./aitoolkit.md)

Průvodce AI Toolkit pokrývá:
- Objevování a výběr modelů pro nasazení na okraji
- Místní testování a optimalizační pracovní postupy
- Integraci ONNX a Ollama pro edge modely
- Techniky konverze a kvantizace modelů
- Vývoj agentů pro edge scénáře
- Hodnocení výkonu a monitorování
- Přípravu na nasazení a osvědčené postupy

## Závěr

Těchto pět implementací EdgeAI demonstruje vyspělost a rozmanitost řešení Edge AI dostupných dnes. Od zařízení s hardwarovou akcelerací, jako je Jetson Orin Nano, po softwarové frameworky, jako je ONNX Runtime GenAI a Windows ML, mají vývojáři bezprecedentní možnosti pro nasazení inteligentních aplikací na okraji.

Společným prvkem všech těchto platforem je demokratizace schopností AI, která zpřístupňuje sofistikované strojové učení vývojářům napříč různými úrovněmi dovedností a případy použití. Ať už vytváříte mobilní aplikace, desktopový software nebo embedded systémy, tato řešení EdgeAI poskytují základ pro novou generaci inteligentních aplikací, které fungují efektivně a soukromě na okraji.

Každá platforma nabízí jedinečné výhody: Jetson Orin Nano pro edge computing s hardwarovou akcelerací, ONNX Runtime GenAI pro vývoj napříč mobilními platformami, Azure EdgeAI pro integraci cloudu a okraje na podnikové úrovni, Windows ML pro nativní aplikace na Windows a Foundry Local pro implementace RAG zaměřené na soukromí. Společně představují komplexní ekosystém pro vývoj EdgeAI.

[Další AI Toolkit](aitoolkit.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.