# 세션 5 샘플: 다중 에이전트 오케스트레이션

이 샘플은 Foundry Local의 OpenAI 호환 엔드포인트를 사용하여 코디네이터 + 전문가 패턴을 시연합니다.

## 실행 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## 검증
```cmd
curl http://localhost:8000/v1/models
```

## 문제 해결
- VS Code에서 `coordinator.py` 파일의 `import specialists`가 해결되지 않는 경우, 모듈로 실행하고 인터프리터가 `Module08/.venv`를 가리키는지 확인하세요:
	- 실행: `python -m samples.05.agents.coordinator`
	- 인터프리터 선택: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## 참고 자료
- Foundry Local (학습): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents 개요: https://learn.microsoft.com/azure/ai-services/agents/overview
- 함수 호출 샘플 (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

