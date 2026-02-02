# Kapitola 04: Konverzia formátov modelov a kvantizácia - Prehľad kapitoly

Vznik EdgeAI urobil z konverzie formátov modelov a kvantizácie nevyhnutné technológie na nasadenie pokročilých schopností strojového učenia na zariadeniach s obmedzenými zdrojmi. Táto komplexná kapitola poskytuje úplný návod na pochopenie, implementáciu a optimalizáciu modelov pre scenáre nasadenia na okraji.

## 📚 Štruktúra kapitoly a učebná cesta

Táto kapitola je rozdelená do siedmich postupných sekcií, pričom každá nadväzuje na predchádzajúcu, aby vytvorila komplexné pochopenie optimalizácie modelov pre výpočty na okraji:

---

## [Sekcia 1: Základy konverzie formátov modelov a kvantizácie](./01.Introduce.md)

### 🎯 Prehľad
Táto základná sekcia vytvára teoretický rámec pre optimalizáciu modelov v prostredí výpočtov na okraji, pokrývajúc hranice kvantizácie od 1-bitovej po 8-bitovú presnosť a kľúčové stratégie konverzie formátov.

**Kľúčové témy:**
- Rámec klasifikácie presnosti (ultra-nízka, nízka, stredná presnosť)
- Výhody a použitie formátov GGUF a ONNX
- Výhody kvantizácie pre operačnú efektivitu a flexibilitu nasadenia
- Porovnania výkonu a pamäťových nárokov

**Výsledky učenia:**
- Pochopiť hranice kvantizácie a klasifikácie
- Identifikovať vhodné techniky konverzie formátov
- Naučiť sa pokročilé stratégie optimalizácie pre nasadenie na okraji

---

## [Sekcia 2: Príručka implementácie Llama.cpp](./02.Llamacpp.md)

### 🎯 Prehľad
Komplexný návod na implementáciu Llama.cpp, výkonného rámca v C++, ktorý umožňuje efektívne inferencie veľkých jazykových modelov s minimálnym nastavením na rôznych hardvérových konfiguráciách.

**Kľúčové témy:**
- Inštalácia na platformách Windows, macOS a Linux
- Konverzia formátu GGUF a rôzne úrovne kvantizácie (Q2_K až Q8_0)
- Hardvérová akcelerácia s CUDA, Metal, OpenCL a Vulkan
- Integrácia s Pythonom a stratégie nasadenia do produkcie

**Výsledky učenia:**
- Ovládnuť inštaláciu na rôznych platformách a zostavenie zo zdroja
- Implementovať techniky kvantizácie a optimalizácie modelov
- Nasadiť modely v serverovom režime s integráciou REST API

---

## [Sekcia 3: Optimalizačný balík Microsoft Olive](./03.MicrosoftOlive.md)

### 🎯 Prehľad
Preskúmanie Microsoft Olive, nástroja na optimalizáciu modelov s ohľadom na hardvér, ktorý obsahuje viac ako 40 zabudovaných optimalizačných komponentov, navrhnutých pre nasadenie modelov na podnikovej úrovni na rôznych hardvérových platformách.

**Kľúčové témy:**
- Funkcie automatickej optimalizácie s dynamickou a statickou kvantizáciou
- Inteligencia s ohľadom na hardvér pre nasadenie na CPU, GPU a NPU
- Podpora populárnych modelov (Llama, Phi, Qwen, Gemma) priamo z balíka
- Integrácia do podnikového prostredia s Azure ML a produkčnými pracovnými postupmi

**Výsledky učenia:**
- Využiť automatizovanú optimalizáciu pre rôzne architektúry modelov
- Implementovať stratégie nasadenia na rôznych platformách
- Vytvoriť optimalizačné pipeline pripravené na podnikové nasadenie

---

## [Sekcia 4: Optimalizačný balík OpenVINO Toolkit](./04.openvino.md)

### 🎯 Prehľad
Komplexné preskúmanie OpenVINO Toolkit od Intelu, open-source platformy na nasadenie výkonných AI riešení v cloude, na mieste a na okraji s pokročilými schopnosťami Neural Network Compression Framework (NNCF).

**Kľúčové témy:**
- Nasadenie na rôznych platformách s hardvérovou akceleráciou (CPU, GPU, VPU, AI akcelerátory)
- Neural Network Compression Framework (NNCF) pre pokročilú kvantizáciu a prerezávanie
- OpenVINO GenAI pre optimalizáciu a nasadenie veľkých jazykových modelov
- Schopnosti modelového servera na podnikovej úrovni a škálovateľné stratégie nasadenia

**Výsledky učenia:**
- Ovládnuť konverziu a optimalizačné pracovné postupy modelov OpenVINO
- Implementovať pokročilé techniky kvantizácie s NNCF
- Nasadiť optimalizované modely na rôznych hardvérových platformách pomocou Model Server

---

## [Sekcia 5: Hlboký ponor do rámca Apple MLX](./05.AppleMLX.md)

### 🎯 Prehľad
Komplexné pokrytie Apple MLX, revolučného rámca špeciálne navrhnutého pre efektívne strojové učenie na Apple Silicon, s dôrazom na schopnosti veľkých jazykových modelov a lokálne nasadenie.

**Kľúčové témy:**
- Výhody jednotnej pamäťovej architektúry a Metal Performance Shaders
- Podpora modelov LLaMA, Mistral, Phi-3, Qwen a Code Llama
- LoRA jemné doladenie pre efektívnu prispôsobenie modelov
- Integrácia s Hugging Face a podpora kvantizácie (4-bitová a 8-bitová)

**Výsledky učenia:**
- Ovládnuť optimalizáciu Apple Silicon pre nasadenie LLM
- Implementovať techniky jemného doladenia a prispôsobenia modelov
- Vytvoriť podnikové AI aplikácie s vylepšenými funkciami ochrany súkromia

---

## [Sekcia 6: Syntéza pracovného postupu vývoja Edge AI](./06.workflow-synthesis.md)

### 🎯 Prehľad
Komplexná syntéza všetkých optimalizačných rámcov do jednotných pracovných postupov, rozhodovacích matíc a osvedčených postupov pre nasadenie Edge AI pripravené na produkciu na rôznych platformách a použitiach vrátane mobilných zariadení, stolných počítačov a cloudových prostredí.

**Kľúčové témy:**
- Jednotná architektúra pracovného postupu integrujúca viacero optimalizačných rámcov
- Rozhodovacie stromy výberu rámca a analýza kompromisov výkonu
- Validácia pripravenosti na produkciu a komplexné stratégie nasadenia
- Stratégie budúcnosti pre nové hardvérové a modelové architektúry

**Výsledky učenia:**
- Ovládnuť systematický výber rámca na základe požiadaviek a obmedzení
- Implementovať pipeline Edge AI pripravené na produkciu s komplexným monitorovaním
- Navrhnúť prispôsobiteľné pracovné postupy, ktoré sa vyvíjajú s novými technológiami a požiadavkami

---

## [Sekcia 7: Optimalizačný balík Qualcomm QNN](./07.QualcommQNN.md)

### 🎯 Prehľad
Komplexné preskúmanie Qualcomm QNN (Qualcomm Neural Network), jednotného rámca AI inferencie navrhnutého na využitie heterogénnej výpočtovej architektúry Qualcomm vrátane Hexagon NPU, Adreno GPU a Kryo CPU pre maximálny výkon a energetickú efektivitu na mobilných a okrajových zariadeniach.

**Kľúčové témy:**
- Heterogénne výpočty s jednotným prístupom k NPU, GPU a CPU
- Optimalizácia s ohľadom na hardvér pre platformy Snapdragon s inteligentným rozdelením záťaže
- Pokročilé techniky kvantizácie (INT8, INT16, zmiešaná presnosť) pre mobilné nasadenie
- Energeticky efektívna inferencia optimalizovaná pre zariadenia na batériu a aplikácie v reálnom čase

**Výsledky učenia:**
- Ovládnuť hardvérovú akceleráciu Qualcomm pre mobilné AI nasadenie
- Implementovať energeticky efektívne optimalizačné stratégie pre výpočty na okraji
- Nasadiť modely pripravené na produkciu v ekosystéme Qualcomm s optimálnym výkonom

---

## 🎯 Výsledky učenia kapitoly

Po dokončení tejto komplexnej kapitoly čitatelia dosiahnu:

### **Technické znalosti**
- Hlboké pochopenie hraníc kvantizácie a praktických aplikácií
- Praktické skúsenosti s viacerými optimalizačnými rámcami
- Zručnosti na nasadenie do produkcie v prostredí výpočtov na okraji

### **Strategické pochopenie**
- Schopnosti výberu optimalizácie s ohľadom na hardvér
- Informované rozhodovanie o kompromisoch výkonu
- Stratégie nasadenia a monitorovania pripravené na podnikové prostredie

### **Porovnania výkonu**

| Rámec      | Kvantizácia | Použitie pamäte | Zlepšenie rýchlosti | Použitie |
|------------|-------------|-----------------|---------------------|----------|
| Llama.cpp  | Q4_K_M      | ~4GB            | 2-3x                | Nasadenie na rôznych platformách |
| Olive      | INT4        | Zníženie o 60-75% | 2-6x              | Podnikové pracovné postupy |
| OpenVINO   | INT8/INT4   | Zníženie o 50-75% | 2-5x              | Optimalizácia pre Intel hardvér |
| QNN        | INT8/INT4   | Zníženie o 50-80% | 5-15x             | Mobilné/okrajové nasadenie Qualcomm |
| MLX        | 4-bitová    | ~4GB            | 2-4x                | Optimalizácia pre Apple Silicon |

## 🚀 Ďalšie kroky a pokročilé aplikácie

Táto kapitola poskytuje kompletný základ pre:
- Vývoj vlastných modelov pre špecifické oblasti
- Výskum v optimalizácii Edge AI
- Vývoj komerčných AI aplikácií
- Veľkorozmerné podnikové nasadenie Edge AI

Znalosti z týchto siedmich sekcií ponúkajú komplexnú sadu nástrojov na orientáciu v rýchlo sa vyvíjajúcom prostredí optimalizácie a nasadenia modelov Edge AI.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.