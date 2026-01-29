# Sura ya 03: Kusambaza Small Language Models (SLMs)

Sura hii ya kina inachunguza mzunguko mzima wa maisha wa usambazaji wa Small Language Models (SLMs), ikijumuisha misingi ya nadharia, mikakati ya utekelezaji wa vitendo, na suluhisho za uzalishaji zilizo kwenye kontena. Sura imegawanywa katika sehemu tatu za maendeleo zinazowapeleka wasomaji kutoka dhana za msingi hadi hali za juu za usambazaji.

## Muundo wa Sura na Safari ya Kujifunza

### **[Sehemu ya 1: Kujifunza kwa Kina kuhusu SLM - Misingi na Uboreshaji](./01.SLMAdvancedLearning.md)**
Sehemu ya mwanzo inaweka msingi wa nadharia wa kuelewa Small Language Models na umuhimu wake wa kimkakati katika usambazaji wa AI kwenye vifaa vya ukingoni. Sehemu hii inashughulikia:

- **Mfumo wa Uainishaji wa Vigezo**: Uchambuzi wa kina wa makundi ya SLM kutoka Micro SLMs (100M-1.4B vigezo) hadi Medium SLMs (14B-30B vigezo), kwa kuzingatia mifano kama Phi-4-mini-3.8B, mfululizo wa Qwen3, na Google Gemma3, ikijumuisha mahitaji ya vifaa na uchambuzi wa matumizi ya kumbukumbu kwa kila daraja la modeli
- **Mbinu za Uboreshaji wa Juu**: Uwasilishaji wa kina wa mbinu za quantization kwa kutumia Llama.cpp, Microsoft Olive, na Apple MLX, ikijumuisha BitNET 1-bit quantization ya kisasa na mifano ya vitendo ya msimbo inayoonyesha mchakato wa quantization na matokeo ya benchmarking
- **Mikakati ya Kupata Modeli**: Uchambuzi wa kina wa mfumo wa Hugging Face na Azure AI Foundry Model Catalog kwa usambazaji wa SLM wa daraja la biashara, pamoja na mifano ya msimbo kwa upakuaji wa modeli kwa njia ya programu, uthibitishaji, na ubadilishaji wa muundo
- **APIs za Waendelezaji**: Mifano ya msimbo katika Python, C++, na C# inayoonyesha jinsi ya kupakia modeli, kufanya inference, na kuunganisha na mifumo maarufu kama PyTorch, TensorFlow, na ONNX Runtime

Sehemu hii ya msingi inasisitiza usawa kati ya ufanisi wa kiutendaji, kubadilika kwa usambazaji, na gharama nafuu inayofanya SLMs kuwa bora kwa hali za kompyuta za ukingoni, na mifano ya vitendo ya msimbo ambayo waendelezaji wanaweza kutekeleza moja kwa moja katika miradi yao.

### **[Sehemu ya 2: Usambazaji wa Mazingira ya Ndani - Suluhisho za Kwanza za Faragha](./02.DeployingSLMinLocalEnv.md)**
Sehemu ya pili inabadilika kutoka nadharia hadi utekelezaji wa vitendo, ikilenga mikakati ya usambazaji wa ndani inayotanguliza uhuru wa data na uhuru wa kiutendaji. Maeneo muhimu ni pamoja na:

- **Jukwaa la Ollama Universal**: Uchunguzi wa kina wa usambazaji wa majukwaa mbalimbali kwa kuzingatia mtiririko wa kazi rafiki kwa waendelezaji, usimamizi wa mzunguko wa maisha wa modeli, na ubinafsishaji kupitia Modelfiles, ikijumuisha mifano kamili ya ujumuishaji wa REST API na hati za kiotomatiki za CLI
- **Microsoft Foundry Local**: Suluhisho za usambazaji wa daraja la biashara na uboreshaji wa msingi wa ONNX, ujumuishaji wa Windows ML, na vipengele vya usalama vya kina, na mifano ya msimbo ya C# na Python kwa ujumuishaji wa programu asilia
- **Uchambuzi wa Kulinganisha**: Ulinganisho wa kina wa mifumo ikijumuisha usanifu wa kiufundi, sifa za utendaji, na miongozo ya uboreshaji wa hali ya matumizi, na msimbo wa benchmarking wa kutathmini kasi ya inference na matumizi ya kumbukumbu kwenye vifaa tofauti
- **Ujumuishaji wa API**: Programu za mfano zinazoonyesha jinsi ya kujenga huduma za wavuti, programu za mazungumzo, na mifumo ya usindikaji wa data kwa kutumia usambazaji wa ndani wa SLM, na mifano ya msimbo katika Node.js, Python Flask/FastAPI, na ASP.NET Core
- **Mifumo ya Kupima**: Mbinu za kupima kiotomatiki kwa uhakikisho wa ubora wa modeli, ikijumuisha mifano ya majaribio ya kitengo na ujumuishaji kwa utekelezaji wa SLM

Sehemu hii inatoa mwongozo wa vitendo kwa mashirika yanayotafuta kutekeleza suluhisho za AI zinazohifadhi faragha huku yakidumisha udhibiti kamili wa mazingira yao ya usambazaji, na mifano ya msimbo inayoweza kutumika moja kwa moja na waendelezaji kulingana na mahitaji yao maalum.

### **[Sehemu ya 3: Usambazaji wa Wingu Ulio kwenye Kontena - Suluhisho za Kiwango cha Uzalishaji](./03.DeployingSLMinCloud.md)**
Sehemu ya mwisho inahitimisha mikakati ya hali ya juu ya usambazaji ulio kwenye kontena, ikionyesha Phi-4-mini-instruct ya Microsoft kama utafiti wa msingi. Sehemu hii inashughulikia:

- **Usambazaji wa vLLM**: Uboreshaji wa inference wa utendaji wa juu na APIs zinazolingana na OpenAI, kasi ya GPU ya hali ya juu, na usanidi wa daraja la uzalishaji, ikijumuisha Dockerfiles kamili, manifests za Kubernetes, na vigezo vya urekebishaji wa utendaji
- **Uratibu wa Kontena la Ollama**: Mtiririko wa kazi wa usambazaji uliorahisishwa kwa kutumia Docker Compose, varianiti za uboreshaji wa modeli, na ujumuishaji wa UI ya wavuti, na mifano ya CI/CD kwa usambazaji na upimaji wa kiotomatiki
- **Utekelezaji wa ONNX Runtime**: Usambazaji ulioboreshwa kwa ukingoni na ubadilishaji wa modeli wa kina, mikakati ya quantization, na utangamano wa majukwaa mbalimbali, ikijumuisha mifano ya msimbo wa uboreshaji wa modeli na usambazaji
- **Ufuatiliaji na Uangalizi**: Utekelezaji wa dashibodi za Prometheus/Grafana na vipimo maalum vya ufuatiliaji wa utendaji wa SLM, ikijumuisha usanidi wa arifa na mkusanyiko wa kumbukumbu
- **Usawazishaji wa Mizigo na Urekebishaji**: Mifano ya vitendo ya mikakati ya usawazishaji wa mizigo ya mlalo na wima na usanidi wa urekebishaji wa kiotomatiki kulingana na matumizi ya CPU/GPU na mifumo ya maombi
- **Kuimarisha Usalama**: Mazoea bora ya usalama wa kontena ikijumuisha kupunguza upendeleo, sera za mtandao, na usimamizi wa siri kwa funguo za API na hati za ufikiaji wa modeli

Kila mbinu ya usambazaji inawasilishwa na mifano kamili ya usanidi, taratibu za upimaji, orodha za ukaguzi wa utayari wa uzalishaji, na templeti za miundombinu-kama-msimbo ambazo waendelezaji wanaweza kutumia moja kwa moja katika mtiririko wao wa kazi wa usambazaji.

## Matokeo Muhimu ya Kujifunza

Kwa kukamilisha sura hii, wasomaji wataweza:

1. **Uchaguzi wa Kimkakati wa Modeli**: Kuelewa mipaka ya vigezo na kuchagua SLM zinazofaa kulingana na vikwazo vya rasilimali na mahitaji ya utendaji
2. **Ustadi wa Uboreshaji**: Kutekeleza mbinu za juu za quantization katika mifumo tofauti ili kufanikisha usawa bora wa utendaji na ufanisi
3. **Kubadilika kwa Usambazaji**: Kuchagua kati ya suluhisho za ndani zinazotanguliza faragha na usambazaji ulio kwenye kontena unaoweza kupanuka kulingana na mahitaji ya shirika
4. **Utayari wa Uzalishaji**: Kuseti mifumo ya ufuatiliaji, usalama, na urekebishaji kwa usambazaji wa SLM wa daraja la biashara

## Mtazamo wa Vitendo na Matumizi ya Ulimwengu Halisi

Sura inazingatia mwelekeo wa vitendo, ikijumuisha:

- **Mifano ya Vitendo**: Faili kamili za usanidi, taratibu za upimaji wa API, na hati za usambazaji
- **Ulinganisho wa Utendaji**: Uchambuzi wa kina wa kasi ya inference, matumizi ya kumbukumbu, na mahitaji ya rasilimali
- **Masuala ya Usalama**: Mazoea ya usalama wa daraja la biashara, mifumo ya kufuata sheria, na mikakati ya ulinzi wa data
- **Mazoea Bora**: Miongozo iliyothibitishwa kwa uzalishaji kwa ufuatiliaji, urekebishaji, na matengenezo

## Mtazamo wa Kujiandaa kwa Baadaye

Sura inahitimisha kwa maarifa ya mbele kuhusu mitindo inayoibuka ikijumuisha:

- Miundo ya modeli ya hali ya juu yenye uwiano bora wa ufanisi
- Ujumuishaji wa kina wa vifaa na viharakishi maalum vya AI
- Mageuzi ya mfumo kuelekea usanifishaji na utangamano
- Mwelekeo wa kupitishwa na biashara unaoendeshwa na faragha na mahitaji ya kufuata sheria

Mbinu hii ya kina inahakikisha wasomaji wanakuwa na vifaa vya kutosha kushughulikia changamoto za sasa za usambazaji wa SLM na maendeleo ya kiteknolojia ya baadaye, wakifanya maamuzi ya busara yanayolingana na mahitaji maalum ya shirika na vikwazo. 

Sura hii inahudumu kama mwongozo wa vitendo kwa utekelezaji wa haraka na rasilimali ya kimkakati kwa mipango ya muda mrefu ya usambazaji wa AI, ikisisitiza usawa muhimu kati ya uwezo, ufanisi, na ubora wa kiutendaji unaofafanua usambazaji wa SLM uliofanikiwa.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.