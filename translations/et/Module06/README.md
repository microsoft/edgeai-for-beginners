# 6. peatükk: SLM Agentlikud Süsteemid: Põhjalik Ülevaade

Tehisintellekti maastik kogeb põhjalikku muutust, liikudes lihtsatest vestlusrobotitest keerukate AI-agentide suunas, mida juhivad Väikesed Keelemudelid (SLM-id). See põhjalik juhend uurib kolme olulist aspekti kaasaegsetes SLM-agentlikes süsteemides: põhimõisted ja juurutusstrateegiad, funktsioonikutsumise võimekus ning revolutsiooniline Mudeli Konteksti Protokolli (MCP) integreerimine.

## [1. osa: AI-agendid ja Väikeste Keelemudelite Alused](./01.IntroduceAgent.md)

Esimene osa loob aluse AI-agentide ja Väikeste Keelemudelite mõistmiseks, positsioneerides 2025. aasta AI-agentide aastaks pärast vestlusrobotite ajastut 2023. aastal ja kaaspilootide buumi 2024. aastal. Selles osas tutvustatakse **agentlikke AI-süsteeme**, mis mõtlevad, arutlevad, planeerivad, kasutavad tööriistu ja täidavad ülesandeid minimaalse inimsekkumisega.

### Olulised käsitletavad teemad:
- **Agentide Klassifikatsiooni Raamistik**: Lihtsatest refleksagentidest õppivate agentideni, pakkudes terviklikku taksonoomiat erinevate arvutistsenaariumide jaoks
- **SLM-i Põhitõed**: Väikeste Keelemudelite määratlemine kui mudelid, millel on vähem kui 10 miljardit parameetrit ja mis suudavad tarbijaseadmetel praktilist järeldust teha
- **Täiustatud Optimeerimisstrateegiad**: GGUF-formaadi juurutamine, kvantiseerimistehnikad (Q4_K_M, Q5_K_S, Q8_0) ja servaoptimeeritud raamistikud nagu Llama.cpp ja Apple MLX
- **SLM vs LLM Kaalutlused**: Näidates 10–30× kulude vähendamist SLM-idega, säilitades samas tõhususe 70–80% tüüpiliste agentide ülesannete jaoks

Osa lõpeb praktiliste juurutusstrateegiatega, kasutades Ollama, VLLM-i ja Microsofti servalahendusi, kinnitades SLM-e kui tulevikku kulutõhusate ja privaatsust säilitavate agentlike AI-süsteemide juurutamisel.

## [2. osa: Funktsioonikutsumine Väikestes Keelemudelites](./02.FunctionCalling.md)

Teine osa süveneb **funktsioonikutsumise võimekusse**, mehhanismi, mis muudab staatilised keelemudelid dünaamilisteks AI-agentideks, mis suudavad reaalses maailmas suhelda. See tehniline süvitsi minek hõlmab kogu töövoogu alates kavatsuse tuvastamisest kuni vastuse integreerimiseni.

### Põhivaldkonnad:
- **Süstemaatiline Töövoog**: Tööriistade integreerimise, funktsioonide määratlemise, kavatsuse tuvastamise, JSON-väljundi genereerimise ja välise täitmise üksikasjalik uurimine
- **Platvormispetsiifilised Juurutused**: Põhjalikud juhendid Phi-4-mini Ollama, Qwen3 funktsioonikutsumise ja Microsoft Foundry Local integreerimise kohta
- **Täiustatud Näited**: Mitme agendi koostöösüsteemid, dünaamiline tööriistade valik ja ettevõtte integreerimismustrid koos põhjaliku veakäsitlusega
- **Tootmiskaalutlused**: Kiiruse piiramine, auditi logimine, turvameetmed ja jõudluse optimeerimise strateegiad

See osa pakub nii teoreetilist arusaamist kui ka praktilisi juurutusmustreid, võimaldades arendajatel luua tugevaid funktsioonikutsumise süsteeme, mis suudavad toime tulla kõigega alates lihtsatest API-kõnedest kuni keerukate mitmeastmeliste ettevõtte töövoogudeni.

## [3. osa: Mudeli Konteksti Protokolli (MCP) Integreerimine](./03.IntroduceMCP.md)

Viimane osa tutvustab **Mudeli Konteksti Protokolli (MCP)**, revolutsioonilist raamistikku, mis standardiseerib, kuidas keelemudelid suhtlevad väliste tööriistade ja süsteemidega. Selles osas näidatakse, kuidas MCP loob silla AI-mudelite ja reaalse maailma vahel hästi määratletud protokollide kaudu.

### Integreerimise Tõmbenumbrid:
- **Protokolli Arhitektuur**: Kihiline süsteemidisain, mis hõlmab rakenduse, LLM-klienti, MCP-klienti ja tööriistade töötlemise kihte
- **Mitme Tagapõhja Tugi**: Paindlik juurutus, mis toetab nii Ollama (kohalik arendus) kui ka vLLM (tootmine) tagapõhju
- **Ühenduse Protokollid**: STDIO-režiim otsese protsessikommunikatsiooni jaoks ja SSE-režiim HTTP-põhise voogesituse jaoks
- **Reaalse Maailma Rakendused**: Veebi automatiseerimise, andmetöötluse ja API integreerimise näited koos põhjaliku veakäsitlusega

MCP integreerimine näitab, kuidas SLM-e saab täiendada väliste võimekustega, kompenseerides nende väiksemat parameetrite arvu täiustatud funktsionaalsuse kaudu, säilitades samal ajal kohaliku juurutamise ja ressursitõhususe eelised.

## Strateegilised Mõjud

Koos esitlevad need kolm osa terviklikku raamistikku SLM-agentlike süsteemide mõistmiseks ja juurutamiseks. Arenemine põhimõistetest funktsioonikutsumise kaudu MCP integreerimiseni näitab selget teed AI juurutamise demokratiseerimise suunas, kus:

- **Tõhusus kohtub võimekusega** optimeeritud väikeste mudelite kaudu
- **Kulutõhusus** võimaldab laialdast kasutuselevõttu
- **Standardiseeritud protokollid** tagavad koostalitlusvõime
- **Kohalik juurutus** säilitab privaatsuse ja vähendab latentsust

See areng ei tähista mitte ainult tehnoloogilist edasiminekut, vaid ka paradigmanihet, mis suunab AI-süsteemid muutuma kättesaadavamaks, tõhusamaks ja praktilisemaks. Need süsteemid suudavad tõhusalt toimida ressursipiirangutega keskkondades, pakkudes samal ajal keerukaid agentlikke võimekusi.

SLM-ide kombinatsioon täiustatud juurutusstrateegiate, tugeva funktsioonikutsumise ja standardiseeritud tööriistade integreerimise protokollidega positsioneerib need süsteemid järgmise põlvkonna AI-agentide aluseks, mis muudavad meie suhtlemist ja kasu tehisintellektist erinevates tööstusharudes ja rakendustes.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.