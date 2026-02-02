# 5 skyrius: SLMOps - Išsamus mažų kalbos modelių operacijų vadovas

## Apžvalga

SLMOps (Small Language Model Operations) – tai revoliucinis požiūris į dirbtinio intelekto diegimą, kuris akcentuoja efektyvumą, ekonomiškumą ir galimybes naudoti kraštiniuose įrenginiuose. Šis išsamus vadovas apima visą SLM operacijų gyvavimo ciklą – nuo pagrindinių koncepcijų supratimo iki paruoštų diegimui sprendimų įgyvendinimo.

---

## [1 skyrius: Įvadas į SLMOps](./01.IntroduceSLMOps.md)

**Revoliucija AI operacijose kraštiniuose įrenginiuose**

Šiame pagrindiniame skyriuje pristatomas paradigmos pokytis nuo tradicinių didelio masto AI operacijų iki mažų kalbos modelių operacijų (SLMOps). Sužinosite, kaip SLMOps sprendžia pagrindinius AI diegimo masto iššūkius, išlaikant ekonomiškumą ir laikantis privatumo reikalavimų.

**Ką sužinosite:**
- SLMOps atsiradimą ir reikšmę šiuolaikinėje AI strategijoje
- Kaip SLMs sujungia našumą ir išteklių efektyvumą
- Pagrindinius operacinius principus, įskaitant išmanų išteklių valdymą ir privatumo pirmumo architektūrą
- Praktinius diegimo iššūkius ir jų sprendimus
- Strateginį verslo poveikį ir konkurencinius pranašumus

**Pagrindinė mintis:** SLMOps demokratizuoja AI diegimą, suteikdamas pažangias kalbos apdorojimo galimybes organizacijoms, turinčioms ribotą techninę infrastruktūrą, leidžiant greičiau kurti ir numatyti operacines išlaidas.

---

## [2 skyrius: Modelio distiliacija - nuo teorijos iki praktikos](./02.SLMOps-Distillation.md)

**Efektyvių modelių kūrimas per žinių perdavimą**

Modelio distiliacija yra pagrindinė technika, leidžianti sukurti mažesnius, efektyvesnius modelius, kurie išlaiko didesnių modelių našumą. Šiame skyriuje pateikiamas išsamus vadovas, kaip įgyvendinti distiliacijos procesus, perduodant žinias iš didelių mokytojų modelių mažiems studentų modeliams.

**Ką sužinosite:**
- Pagrindines modelio distiliacijos koncepcijas ir privalumus
- Dviejų etapų distiliacijos procesą: sintetinės duomenų generavimas ir studentų modelio mokymas
- Praktines įgyvendinimo strategijas naudojant pažangius modelius, tokius kaip DeepSeek V3 ir Phi-4-mini
- Azure ML distiliacijos darbo eigas su praktiniais pavyzdžiais
- Geriausią praktiką hiperparametrų derinimui ir vertinimo strategijoms
- Realių atvejų analizės, parodančios reikšmingus kaštų ir našumo patobulinimus

**Pagrindinė mintis:** Modelio distiliacija leidžia organizacijoms pasiekti 85% sumažėjimą įžvalgų laike ir 95% sumažėjimą atminties poreikiuose, išlaikant 92% pradinio modelio tikslumo, todėl pažangios AI galimybės tampa praktiškai įgyvendinamos.

---

## [3 skyrius: Modelio pritaikymas - pritaikymas specifinėms užduotims](./03.SLMOps-Finetuing.md)

**Iš anksto apmokytų modelių pritaikymas jūsų unikaliems poreikiams**

Modelio pritaikymas paverčia bendros paskirties modelius specializuotais sprendimais, pritaikytais jūsų specifiniams naudojimo atvejams ir sritims. Šiame skyriuje aptariama viskas – nuo pagrindinių parametrų koregavimo iki pažangių technikų, tokių kaip LoRA ir QLoRA, efektyviam modelio pritaikymui.

**Ką sužinosite:**
- Išsamų modelio pritaikymo metodų apžvalgą ir jų taikymą
- Skirtingus pritaikymo tipus: pilnas pritaikymas, efektyvus parametrų pritaikymas (PEFT) ir užduoties specifiniai metodai
- Praktinį įgyvendinimą naudojant Microsoft Olive su praktiniais pavyzdžiais
- Pažangias technikas, įskaitant daugiadapterinį mokymą ir hiperparametrų optimizavimą
- Geriausią praktiką duomenų paruošimui, mokymo konfigūracijai ir išteklių valdymui
- Dažniausi iššūkiai ir patikrinti sprendimai sėkmingiems pritaikymo projektams

**Pagrindinė mintis:** Modelio pritaikymas naudojant tokias priemones kaip Microsoft Olive leidžia organizacijoms efektyviai pritaikyti iš anksto apmokytus modelius specifiniams poreikiams, optimizuojant našumą ir išteklių naudojimą, todėl pažangus AI tampa prieinamas įvairiose srityse.

---

## [4 skyrius: Diegimas - paruoštų modelių įgyvendinimas](./04.SLMOps.Deployment.md)

**Pritaikytų modelių diegimas naudojant Foundry Local**

Paskutinis skyrius sutelktas į kritinę diegimo fazę, apimant modelio konvertavimą, kvantizaciją ir gamybos konfigūraciją. Sužinosite, kaip diegti pritaikytus kvantizuotus modelius naudojant Foundry Local, siekiant optimalaus našumo ir išteklių panaudojimo.

**Ką sužinosite:**
- Pilną aplinkos nustatymo ir įrankių diegimo procedūrą
- Modelio konvertavimo ir kvantizacijos technikas skirtingiems diegimo scenarijams
- Foundry Local diegimo konfigūraciją su modelio specifinėmis optimizacijomis
- Našumo testavimo ir kokybės vertinimo metodikas
- Dažniausių diegimo problemų sprendimo ir optimizavimo strategijas
- Gamybos stebėjimo ir priežiūros geriausią praktiką

**Pagrindinė mintis:** Tinkama diegimo konfigūracija su kvantizacijos technikomis gali pasiekti iki 75% dydžio sumažėjimą, išlaikant priimtiną modelio kokybę, leidžiant efektyviai diegti gamybos sprendimus įvairiose techninės įrangos konfigūracijose.

---

## Pradėkite

Šis vadovas skirtas padėti jums pereiti visą SLMOps kelionę – nuo pagrindinių koncepcijų supratimo iki paruoštų diegimui sprendimų įgyvendinimo. Kiekvienas skyrius remiasi ankstesniu, suteikdamas tiek teorinį supratimą, tiek praktinius įgyvendinimo įgūdžius.

Nesvarbu, ar esate duomenų mokslininkas, siekiantis optimizuoti modelio diegimą, DevOps inžinierius, įgyvendinantis AI operacijas, ar techninis vadovas, vertinantis SLMOps savo organizacijai, šis išsamus vadovas suteikia žinių ir įrankių, reikalingų sėkmingai įgyvendinti mažų kalbos modelių operacijas.

**Pasiruošę pradėti?** Pradėkite nuo 1 skyriaus, kad suprastumėte pagrindinius SLMOps principus ir sukurtumėte pagrindą pažangioms įgyvendinimo technikoms, aptartoms vėlesniuose skyriuose.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.