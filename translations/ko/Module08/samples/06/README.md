# 세션 6 샘플: 도구로서의 모델

이 샘플은 사용자 프롬프트에 따라 모델을 선택하고 Foundry Local의 OpenAI 호환 엔드포인트를 호출하는 최소한의 라우터 + 도구 레지스트리를 구현합니다.

## 파일
- `router.py`: 간단한 레지스트리와 휴리스틱 라우팅; 엔드포인트 검색 + 상태 확인.

## 실행 (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## 참고 사항
- 라우터는 간단한 키워드 휴리스틱을 사용하여 `general`, `reasoning`, `code` 도구 중에서 선택하며 시작 시 `/v1/models`를 출력합니다.
- 환경 변수를 통해 구성:
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

## 참고 자료
- Foundry Local (학습): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- 추론 SDK와 통합: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.