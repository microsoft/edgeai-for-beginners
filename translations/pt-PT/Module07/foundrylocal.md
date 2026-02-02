# Foundry Local no Windows e Mac

Este guia ajuda a instalar, executar e integrar o Microsoft Foundry Local no Windows e Mac. Todos os passos e comandos foram validados com base na documentação do Microsoft Learn.

- Introdução: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arquitetura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referência CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrar SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compilar Modelos HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalar / Atualizar no Windows

- Instalar:
```cmd
winget install Microsoft.FoundryLocal
```
- Atualizar:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Verificar versão:
```cmd
foundry --version
```
     
**Instalar / Mac**

**MacOS**: 
Abra um terminal e execute o seguinte comando:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Noções Básicas de CLI (Três Categorias)

- Modelo:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Serviço:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Notas:
- O serviço expõe uma API REST compatível com OpenAI. A porta do endpoint é alocada dinamicamente; use `foundry service status` para descobri-la.
- Utilize os SDKs para maior conveniência; eles gerem automaticamente a descoberta de endpoints onde suportado.

## 3) Descobrir o Endpoint Local (Porta Dinâmica)

O Foundry Local atribui uma porta dinâmica cada vez que o serviço é iniciado:
```cmd
foundry service status
```
Use o endereço `http://localhost:<PORT>` como o seu `base_url` com caminhos compatíveis com OpenAI (por exemplo, `/v1/chat/completions`).

## 4) Teste Rápido via OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Referências:
- Integração com SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Trazer o Seu Próprio Modelo (Compilar com Olive)

Se precisar de um modelo que não esteja no catálogo, compile-o para ONNX para uso no Foundry Local utilizando Olive.

Fluxo de alto nível (consulte a documentação para os passos):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Documentação:
- Compilar BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Resolução de Problemas

- Verificar o estado do serviço e os logs:
```cmd
foundry service status
foundry service diag
```
- Limpar ou mover cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Atualizar para a última versão de pré-visualização:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Experiência Relacionada para Desenvolvedores no Windows

- Escolhas de IA local vs cloud no Windows, incluindo Foundry Local e Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit com Foundry Local (use `foundry service status` para obter o URL do endpoint de chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Próximo Desenvolvedor Windows](./windowdeveloper.md)

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.