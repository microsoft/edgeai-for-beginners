# Session 2 Sample: SDK Integration

Use the OpenAI Python SDK to call either Foundry Local (OpenAI-compatible) or Azure OpenAI.

## Install
```cmd
cd Module08
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run
Foundry Local (default):
```cmd
set FOUNDRY_MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

Azure OpenAI:
```cmd
set AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
set AZURE_OPENAI_API_KEY=<your-key>
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=<your-deployment-name>
python samples\02\sdk_quickstart.py
```
