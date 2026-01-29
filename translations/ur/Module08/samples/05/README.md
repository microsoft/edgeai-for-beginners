# سیشن 5 نمونہ: ملٹی ایجنٹ آرکسٹریشن

یہ نمونہ Foundry Local کے OpenAI-compatible endpoint کا استعمال کرتے ہوئے کوآرڈینیٹر + ماہرین کے پیٹرن کو ظاہر کرتا ہے۔

## چلائیں (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## تصدیق کریں
```cmd
curl http://localhost:8000/v1/models
```

## مسئلے کا حل
- اگر VS Code `import specialists` کو `coordinator.py` میں غیر حل شدہ کے طور پر ظاہر کرے، تو یقینی بنائیں کہ آپ اسے ماڈیول کے طور پر چلا رہے ہیں اور انٹرپریٹر `Module08/.venv` کی طرف اشارہ کر رہا ہے:
	- چلائیں: `python -m samples.05.agents.coordinator`
	- انٹرپریٹر منتخب کریں: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## حوالہ جات
- Foundry Local (سیکھیں): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents کا جائزہ: https://learn.microsoft.com/azure/ai-services/agents/overview
- فنکشن کالنگ نمونہ (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

