# Modul 08 Minták: Foundry Helyi Fejlesztési Útmutató

## Áttekintés

Ez az átfogó gyűjtemény bemutatja a **Foundry Local SDK** és a **Shell Command** megközelítéseket a gyártásra kész AI alkalmazások fejlesztéséhez. Minden minta az edge AI fejlesztés különböző aspektusait mutatja be, az alapvető REST integrációtól a fejlett többügynökös rendszerekig.

## Fejlesztési Megközelítés: SDK vs Shell Parancsok

### Használja a Foundry Local SDK-t, ha:

- **Programozott Irányítás**: Teljes kontrollra van szüksége az ügynök életciklusa, értékelése vagy telepítési munkafolyamatok felett
- **Egyedi Eszközök**: Automatizálást épít a Foundry Local köré (CI/CD integráció, többügynökös orkestráció)
- **Finomhangolt Hozzáférés**: Részletes ügynök metaadatokra, verziókezelésre vagy értékelési futtató vezérlésre van szüksége
- **Python Integráció**: Python-alapú környezetben dolgozik, vagy a Foundry logikát szélesebb alkalmazásokba ágyazza
- **Vállalati Munkafolyamatok**: Moduláris munkafolyamatokat és reprodukálható értékelési csatornákat valósít meg, amelyek igazodnak a Microsoft referencia-architektúrákhoz

### Használja a Shell Parancsokat, ha:

- **Gyors Tesztelés**: Gyors helyi tesztelést, manuális ügynökindítást vagy beállítás ellenőrzést végez
- **CLI Egyszerűség**: Egyszerű CLI műveletekre van szüksége ügynökök indításához/leállításához, naplók ellenőrzéséhez vagy alapvető értékelésekhez
- **Könnyű Automatizálás**: Egyszerű automatizálást szkriptel, amely nem igényel teljes SDK integrációt
- **Gyors Iteráció**: Hibakeresési és fejlesztési ciklusok, különösen korlátozott környezetekben vagy erőforráscsoport szintű telepítések során
- **Beállítás és Ellenőrzés**: Kezdeti környezet konfiguráció és gyors ellenőrzési feladatok

## Legjobb Gyakorlatok és Ajánlott Munkafolyamat

Az ügynök életciklus-kezelés, függőségkövetés és minimális jogosultságú reprodukálhatóság elvei alapján:

### 1. Fázis: Alapok és Beállítás
1. **Kezdje Shell Parancsokkal** az első beállításhoz és gyors ellenőrzéshez
2. **Ellenőrizze a Környezetet** CLI eszközökkel és alapvető modell telepítéssel
3. **Tesztelje a Kapcsolatot** egyszerű REST hívásokkal és állapotellenőrzésekkel

### 2. Fázis: Fejlesztés és Integráció
1. **Váltson SDK-ra** a skálázható, nyomon követhető munkafolyamatok érdekében
2. **Valósítson meg Programozott Irányítást** összetett ügynök interakciókhoz
3. **Építsen Egyedi Eszközöket** közösségi sablonokhoz és Azure OpenAI integrációhoz

### 3. Fázis: Gyártás és Skálázás
1. **Hibrid Megközelítés** kombinálva CLI-t az operációhoz és SDK-t az alkalmazás logikához
2. **Vállalati Integráció** monitorozással, naplózással és telepítési csatornákkal
3. **Közösségi Hozzájárulás** újrahasználható sablonokkal és legjobb gyakorlatokkal

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.