# 6 skyrius: SLM agentinės sistemos: išsamus apžvalga

Dirbtinio intelekto sritis patiria esminę transformaciją, pereinant nuo paprastų pokalbių robotų prie pažangių AI agentų, kuriuos valdo Mažieji Kalbos Modeliai (SLM). Ši išsami apžvalga nagrinėja tris svarbiausius šiuolaikinių SLM agentinių sistemų aspektus: pagrindines sąvokas ir diegimo strategijas, funkcijų iškvietimo galimybes bei revoliucinę Modelio Konteksto Protokolo (MCP) integraciją.

## [1 skyrius: AI agentai ir Mažųjų Kalbos Modelių pagrindai](./01.IntroduceAgent.md)

Pirmasis skyrius suteikia pagrindinį supratimą apie AI agentus ir Mažuosius Kalbos Modelius, pažymėdamas 2025 metus kaip AI agentų erą po pokalbių robotų bumo 2023 metais ir kopilotų populiarumo 2024 metais. Šiame skyriuje pristatomi **agentiniai AI sistemos**, kurios mąsto, sprendžia, planuoja, naudoja įrankius ir vykdo užduotis su minimalia žmogaus pagalba.

### Pagrindinės aptariamos sąvokos:
- **Agentų klasifikavimo sistema**: Nuo paprastų refleksinių agentų iki mokymosi agentų, pateikiant išsamų taksonomiją skirtingiems kompiuterijos scenarijams
- **SLM pagrindai**: Mažųjų Kalbos Modelių apibrėžimas kaip modelių, turinčių mažiau nei 10 milijardų parametrų, galinčių atlikti praktinę analizę vartotojų įrenginiuose
- **Pažangios optimizavimo strategijos**: GGUF formato diegimas, kvantizavimo technikos (Q4_K_M, Q5_K_S, Q8_0) ir kraštui optimizuotos platformos, tokios kaip Llama.cpp ir Apple MLX
- **SLM ir LLM kompromisai**: Parodoma 10–30 kartų sąnaudų mažinimo galimybė naudojant SLM, išlaikant efektyvumą 70–80% tipinių agentų užduočių

Skyrius baigiamas praktinėmis diegimo strategijomis, naudojant Ollama, VLLM ir Microsoft kraštines sprendimus, įtvirtinant SLM kaip ateities ekonomišką ir privatumo išsaugantį agentinio AI diegimo būdą.

## [2 skyrius: Funkcijų iškvietimas Mažuosiuose Kalbos Modeliuose](./02.FunctionCalling.md)

Antrasis skyrius išsamiai nagrinėja **funkcijų iškvietimo galimybes**, mechanizmą, kuris paverčia statinius kalbos modelius dinamiškais AI agentais, galinčiais sąveikauti su realiu pasauliu. Ši techninė analizė apima visą darbo eigą nuo ketinimų nustatymo iki atsakymų integracijos.

### Pagrindinės įgyvendinimo sritys:
- **Sisteminga darbo eiga**: Išsamus įrankių integracijos, funkcijų apibrėžimo, ketinimų nustatymo, JSON išvesties generavimo ir išorinio vykdymo tyrimas
- **Platformai pritaikyti įgyvendinimai**: Išsamūs vadovai Phi-4-mini su Ollama, Qwen3 funkcijų iškvietimu ir Microsoft Foundry vietinės integracijos
- **Pažangūs pavyzdžiai**: Daugelio agentų bendradarbiavimo sistemos, dinaminis įrankių pasirinkimas ir įmonių integracijos modeliai su išsamia klaidų tvarkyba
- **Gamybos aspektai**: Greičio apribojimai, audito žurnalai, saugumo priemonės ir našumo optimizavimo strategijos

Šis skyrius suteikia tiek teorinį supratimą, tiek praktinius įgyvendinimo modelius, leidžiančius kūrėjams kurti patikimas funkcijų iškvietimo sistemas, galinčias tvarkyti viską nuo paprastų API iškvietimų iki sudėtingų daugiapakopių įmonių darbo eigų.

## [3 skyrius: Modelio Konteksto Protokolo (MCP) integracija](./03.IntroduceMCP.md)

Paskutinis skyrius pristato **Modelio Konteksto Protokolą (MCP)**, revoliucinę sistemą, standartizuojančią, kaip kalbos modeliai sąveikauja su išoriniais įrankiais ir sistemomis. Šiame skyriuje parodoma, kaip MCP sukuria tiltą tarp AI modelių ir realaus pasaulio per gerai apibrėžtus protokolus.

### Integracijos akcentai:
- **Protokolo architektūra**: Sluoksniuota sistemos struktūra, apimanti taikymo, LLM kliento, MCP kliento ir įrankių apdorojimo sluoksnius
- **Daugelio galinių sistemų palaikymas**: Lankstus įgyvendinimas, palaikantis tiek Ollama (vietinė plėtra), tiek vLLM (gamyba) galinius sprendimus
- **Ryšio protokolai**: STDIO režimas tiesioginiam procesų ryšiui ir SSE režimas HTTP pagrindu veikiančiam srautui
- **Praktiniai pritaikymai**: Interneto automatizavimo, duomenų apdorojimo ir API integracijos pavyzdžiai su išsamia klaidų tvarkyba

MCP integracija parodo, kaip SLM gali būti papildyti išorinėmis galimybėmis, kompensuojant jų mažesnį parametrų skaičių per padidintą funkcionalumą, išlaikant vietinio diegimo ir išteklių efektyvumo privalumus.

## Strateginės pasekmės

Šie trys skyriai kartu pateikia išsamų pagrindą suprasti ir įgyvendinti SLM agentines sistemas. Evoliucija nuo pagrindinių sąvokų per funkcijų iškvietimą iki MCP integracijos parodo aiškų kelią link demokratizuoto AI diegimo, kur:

- **Efektyvumas susitinka su galimybėmis** per optimizuotus mažus modelius
- **Ekonomiškumas** skatina plačią pritaikymą
- **Standartizuoti protokolai** užtikrina suderinamumą
- **Vietinis diegimas** išsaugo privatumą ir mažina delsą

Ši pažanga reiškia ne tik technologinį progresą, bet ir paradigmos pokytį link labiau prieinamų, efektyvių ir praktiškų AI sistemų, kurios gali veikti efektyviai ribotų išteklių aplinkoje, tuo pačiu teikdamos pažangias agentines galimybes.

SLM derinys su pažangiomis diegimo strategijomis, patikimu funkcijų iškvietimu ir standartizuotais įrankių integracijos protokolais pozicionuoja šias sistemas kaip pagrindą naujos kartos AI agentams, kurie transformuos mūsų sąveiką su dirbtiniu intelektu ir jo teikiamą naudą įvairiose pramonės šakose ir taikymuose.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.