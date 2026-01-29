# 08 modulio pavyzdžiai: Foundry vietinio kūrimo vadovas

## Apžvalga

Ši išsami kolekcija demonstruoja tiek **Foundry vietinio SDK**, tiek **komandų eilutės** metodus, skirtus kurti gamybai paruoštas AI programas. Kiekvienas pavyzdys atskleidžia skirtingus kraštinių AI kūrimo aspektus – nuo paprastos REST integracijos iki pažangių daugiaveiksnių sistemų.

## Kūrimo metodas: SDK vs komandų eilutės

### Naudokite Foundry vietinį SDK, kai:

- **Programinė kontrolė**: Reikia visiškos kontrolės agento gyvavimo ciklui, vertinimui ar diegimo procesams
- **Individualūs įrankiai**: Automatizacijos kūrimas aplink Foundry Local (CI/CD integracija, daugiaveiksnių agentų orkestracija)
- **Detalus priėjimas**: Reikia išsamios agento metaduomenų, versijų ar vertinimo vykdyklės kontrolės
- **Python integracija**: Dirbate Python aplinkoje arba įterpiate Foundry logiką į platesnes programas
- **Įmonės darbo procesai**: Moduliniai darbo procesai ir atkartojamos vertinimo sistemos, suderintos su Microsoft referencinėmis architektūromis

### Naudokite komandų eilutę, kai:

- **Greitas testavimas**: Atliekate greitą vietinį testavimą, rankinį agentų paleidimą ar nustatymų patikrinimą
- **Komandų eilutės paprastumas**: Reikia paprastų CLI operacijų agentų paleidimui/sustabdymui, žurnalų tikrinimui ar pagrindiniams vertinimams
- **Lengva automatizacija**: Skriptų kūrimas paprastai automatizacijai be pilno SDK integracijos poreikio
- **Greitas iteravimas**: Derinimo ir kūrimo ciklai, ypač ribotose aplinkose ar išteklių grupės lygio diegimuose
- **Nustatymas ir patikrinimas**: Pradinė aplinkos konfigūracija ir greiti patikrinimo uždaviniai

## Geriausia praktika ir rekomenduojamas darbo procesas

Remiantis agento gyvavimo ciklo valdymu, priklausomybių stebėjimu ir minimalios privilegijos atkartojamumo principais:

### 1 etapas: Pagrindai ir nustatymas
1. **Pradėkite nuo komandų eilutės** pradiniam nustatymui ir greitam patikrinimui
2. **Patikrinkite aplinką** naudodami CLI įrankius ir pagrindinį modelio diegimą
3. **Testuokite ryšį** su paprastais REST užklausomis ir sveikatos patikrinimais

### 2 etapas: Kūrimas ir integracija
1. **Pereikite prie SDK** siekiant mastelio ir atsekamų darbo procesų
2. **Įgyvendinkite programinę kontrolę** sudėtingoms agentų sąveikoms
3. **Kurkite individualius įrankius** bendruomenei skirtoms šablonams ir Azure OpenAI integracijai

### 3 etapas: Gamyba ir mastelis
1. **Hibridinis metodas** derinant CLI operacijoms ir SDK programų logikai
2. **Įmonės integracija** su stebėjimu, žurnalų tvarkymu ir diegimo procesais
3. **Bendruomenės indėlis** per pakartotinai naudojamus šablonus ir geriausią praktiką

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.