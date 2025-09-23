import os
from openai import OpenAI

# Mode selection:
# - Foundry Local (default): set FOUNDRY_MODEL
# - OpenAI-compatible: set BASE_URL and optionally API_KEY and MODEL
# - Azure OpenAI: set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY (and optionally, API version)

azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
azure_api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
foundry_model = os.environ.get("FOUNDRY_MODEL")

if azure_endpoint and azure_api_key:
    # Azure OpenAI path
    # MODEL should be the Azure deployment name
    model = os.environ.get("MODEL", "your-deployment-name")
    client = OpenAI(
        base_url=f"{azure_endpoint}/openai",
        api_key=azure_api_key,
        default_query={"api-version": azure_api_version},
    )
elif foundry_model:
    from foundry_local import FoundryLocalManager

    # Create a FoundryLocalManager instance. This will start the Foundry
    # Local service if it is not already running and load the specified model.
    manager = FoundryLocalManager(foundry_model)
    model_info = manager.get_model_info(foundry_model)
    model = model_info.id if model_info else foundry_model
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key  # API key is not required for local usage
    )
else:
    # OpenAI-compatible path
    base_url = os.environ.get("BASE_URL", "http://localhost:8000")
    model = os.environ.get("MODEL", "phi-4-mini")
    api_key = os.environ.get("API_KEY", "")
    client = OpenAI(base_url=f"{base_url}/v1", api_key=api_key)

resp = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Say hello from the SDK quickstart."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
