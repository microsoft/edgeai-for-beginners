# Sessão 6 Exemplo: Modelos como Ferramentas

Este exemplo implementa um roteador mínimo + registro de ferramentas que seleciona um modelo com base no prompt do usuário e chama o endpoint compatível com OpenAI do Foundry Local.

## Arquivos
- `router.py`: registro simples e roteamento heurístico; descoberta de endpoint + verificação de saúde.

## Executar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Observações
- O roteador usa heurísticas simples de palavras-chave para escolher entre as ferramentas `general`, `reasoning` e `code` e imprime `/v1/models` ao iniciar.
- Configuração via variáveis de ambiente:
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

## Referências
- Foundry Local (Aprenda): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integre com SDKs de inferência: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.