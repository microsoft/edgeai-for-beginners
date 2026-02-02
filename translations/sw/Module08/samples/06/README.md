# Kipindi cha 6 Mfano: Miundo kama Vifaa

Mfano huu unatekeleza router ndogo + usajili wa zana ambao huchagua mfano kulingana na maelezo ya mtumiaji na kuita mwisho wa Foundry Local unaoendana na OpenAI.

## Faili
- `router.py`: usajili rahisi na njia ya kiakili; ugunduzi wa mwisho + ukaguzi wa afya.

## Endesha (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Maelezo
- Router hutumia kanuni rahisi za maneno muhimu kuchagua kati ya zana za `general`, `reasoning`, na `code` na kuchapisha `/v1/models` mwanzoni.
- Sanidi kupitia vigezo vya mazingira:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Marejeleo
- Foundry Local (Jifunze): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Jumuisha na SDK za utabiri: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.