# Sura ya 06: Mifumo ya Wakala wa SLM: Muhtasari wa Kina

Mandhari ya akili bandia yanapitia mabadiliko makubwa tunapohama kutoka kwa chatbots rahisi hadi mawakala wa AI wenye uwezo mkubwa wanaotumia Small Language Models (SLMs). Mwongozo huu wa kina unachunguza vipengele vitatu muhimu vya mifumo ya kisasa ya wakala wa SLM: dhana za msingi na mikakati ya utekelezaji, uwezo wa kuita kazi, na ujumuishaji wa Mapinduzi ya Model Context Protocol (MCP).

## [Sehemu ya 1: Misingi ya Mawakala wa AI na Small Language Models](./01.IntroduceAgent.md)

Sehemu ya kwanza inaweka msingi wa uelewa wa mawakala wa AI na Small Language Models, ikitaja mwaka wa 2025 kama mwaka wa mawakala wa AI kufuatia enzi ya chatbots ya 2023 na kuongezeka kwa copilot mwaka wa 2024. Sehemu hii inatambulisha **mifumo ya AI ya wakala** inayofikiria, kuamua, kupanga, kutumia zana, na kutekeleza majukumu kwa usaidizi mdogo wa binadamu.

### Dhana Muhimu Zinazojadiliwa:
- **Mfumo wa Uainishaji wa Mawakala**: Kutoka kwa mawakala wa reflex rahisi hadi mawakala wa kujifunza, ikitoa uainishaji wa kina kwa hali tofauti za kompyuta
- **Misingi ya SLM**: Kufafanua Small Language Models kama mifano yenye vigezo chini ya bilioni 10 inayoweza kufanya uchambuzi wa vitendo kwenye vifaa vya watumiaji
- **Mikakati ya Uboreshaji wa Juu**: Kujadili muundo wa GGUF, mbinu za quantization (Q4_K_M, Q5_K_S, Q8_0), na mifumo iliyoboreshwa kwa vifaa kama Llama.cpp na Apple MLX
- **Faida na Hasara za SLM dhidi ya LLM**: Kuonyesha kupunguzwa kwa gharama kwa 10-30× na SLMs huku zikidumisha ufanisi kwa 70-80% ya majukumu ya kawaida ya wakala

Sehemu hii inahitimisha kwa mikakati ya utekelezaji wa vitendo kwa kutumia Ollama, VLLM, na suluhisho za Microsoft za vifaa vya ukingo, ikianzisha SLMs kama mustakabali wa utekelezaji wa AI wa wakala wa gharama nafuu na unaohifadhi faragha.

## [Sehemu ya 2: Kuita Kazi katika Small Language Models](./02.FunctionCalling.md)

Sehemu ya pili inaingia kwa kina katika **uwezo wa kuita kazi**, utaratibu unaobadilisha mifano ya lugha tuli kuwa mawakala wa AI wenye nguvu wanaoweza kuingiliana na ulimwengu halisi. Uchambuzi huu wa kiufundi unashughulikia mtiririko mzima kutoka kwa kugundua nia hadi ujumuishaji wa majibu.

### Maeneo Muhimu ya Utekelezaji:
- **Mtiririko wa Mfumo**: Uchambuzi wa kina wa ujumuishaji wa zana, ufafanuzi wa kazi, kugundua nia, kizazi cha matokeo ya JSON, na utekelezaji wa nje
- **Utekelezaji Maalum wa Jukwaa**: Mwongozo wa kina kwa Phi-4-mini na Ollama, kuita kazi kwa Qwen3, na ujumuishaji wa Microsoft Foundry Local
- **Mifano ya Juu**: Mifumo ya ushirikiano wa mawakala wengi, uteuzi wa zana za nguvu, na mifumo ya ujumuishaji wa biashara yenye utunzaji wa makosa wa kina
- **Masuala ya Uzalishaji**: Kuweka mipaka ya kiwango, ukaguzi wa kumbukumbu, hatua za usalama, na mikakati ya uboreshaji wa utendaji

Sehemu hii inatoa uelewa wa kinadharia na mifumo ya utekelezaji wa vitendo, ikiruhusu watengenezaji kujenga mifumo thabiti ya kuita kazi inayoweza kushughulikia kila kitu kutoka kwa miito rahisi ya API hadi mtiririko wa kazi wa hatua nyingi wa biashara.

## [Sehemu ya 3: Ujumuishaji wa Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Sehemu ya mwisho inatambulisha **Model Context Protocol (MCP)**, mfumo wa mapinduzi unaosawazisha jinsi mifano ya lugha inavyoshirikiana na zana na mifumo ya nje. Sehemu hii inaonyesha jinsi MCP inavyounda daraja kati ya mifano ya AI na ulimwengu halisi kupitia itifaki zilizoainishwa vizuri.

### Vipengele vya Ujumuishaji:
- **Muundo wa Itifaki**: Muundo wa mfumo wa tabaka unaoshughulikia tabaka za programu, mteja wa LLM, mteja wa MCP, na tabaka za usindikaji wa zana
- **Msaada wa Backend Nyingi**: Utekelezaji rahisi unaounga mkono Ollama (maendeleo ya ndani) na vLLM (uzalishaji)
- **Itifaki za Muunganisho**: Hali ya STDIO kwa mawasiliano ya moja kwa moja ya mchakato na hali ya SSE kwa utiririshaji wa msingi wa HTTP
- **Matumizi ya Ulimwengu Halisi**: Mifano ya kiotomatiki ya wavuti, usindikaji wa data, na ujumuishaji wa API na utunzaji wa makosa wa kina

Ujumuishaji wa MCP unaonyesha jinsi SLMs zinavyoweza kuimarishwa na uwezo wa nje, kufidia idadi yao ndogo ya vigezo kupitia utendaji ulioboreshwa huku zikidumisha faida za utekelezaji wa ndani na ufanisi wa rasilimali.

## Athari za Kistratejia

Pamoja, sehemu hizi tatu zinawasilisha mfumo wa kina wa kuelewa na kutekeleza mifumo ya wakala wa SLM. Mageuzi kutoka dhana za msingi kupitia kuita kazi hadi ujumuishaji wa MCP yanaonyesha njia wazi kuelekea utekelezaji wa AI ulio demokrasia ambapo:

- **Ufanisi unakutana na uwezo** kupitia mifano midogo iliyoboreshwa
- **Gharama nafuu** inaruhusu kupitishwa kwa wingi
- **Itifaki zilizosawazishwa** zinahakikisha ushirikiano
- **Utekelezaji wa ndani** unahifadhi faragha na kupunguza ucheleweshaji

Maendeleo haya yanawakilisha si tu maendeleo ya kiteknolojia bali mabadiliko ya dhana kuelekea mifumo ya AI inayopatikana zaidi, yenye ufanisi, na ya vitendo inayoweza kufanya kazi kwa ufanisi katika mazingira yenye rasilimali chache huku ikitoa uwezo wa wakala wa hali ya juu.

Mchanganyiko wa SLMs na mikakati ya juu ya utekelezaji, kuita kazi thabiti, na itifaki za ujumuishaji wa zana zilizosawazishwa unaiweka mifumo hii kama msingi wa kizazi kijacho cha mawakala wa AI ambao watabadilisha jinsi tunavyoshirikiana na kufaidika na akili bandia katika sekta na matumizi mbalimbali.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.