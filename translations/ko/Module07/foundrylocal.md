# Windows 및 Mac에서 Foundry Local

이 가이드는 Windows 및 Mac에서 Microsoft Foundry Local을 설치, 실행 및 통합하는 방법을 안내합니다. 모든 단계와 명령은 Microsoft Learn 문서를 기준으로 검증되었습니다.

- 시작하기: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- 아키텍처: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI 참조: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK 통합: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF 모델 컴파일 (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: 로컬 vs 클라우드: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows에서 설치 / 업그레이드

- 설치:
```cmd
winget install Microsoft.FoundryLocal
```
- 업그레이드:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- 버전 확인:
```cmd
foundry --version
```
     
**Mac에서 설치**

**MacOS**: 
터미널을 열고 다음 명령을 실행하세요:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI 기본 사항 (세 가지 카테고리)

- 모델:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- 서비스:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- 캐시:
```cmd
foundry cache --help
foundry cache list
```

참고:
- 서비스는 OpenAI 호환 REST API를 제공합니다. 엔드포인트 포트는 동적으로 할당되며, `foundry service status`를 사용하여 확인할 수 있습니다.
- SDK를 사용하면 편리합니다. SDK는 지원되는 경우 엔드포인트 검색을 자동으로 처리합니다.

## 3) 로컬 엔드포인트 발견 (동적 포트)

Foundry Local은 서비스가 시작될 때마다 동적 포트를 할당합니다:
```cmd
foundry service status
```
보고된 `http://localhost:<PORT>`를 OpenAI 호환 경로(예: `/v1/chat/completions`)와 함께 `base_url`로 사용하세요.

## 4) OpenAI Python SDK를 통한 간단한 테스트

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
참고 자료:
- SDK 통합: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) 사용자 모델 가져오기 (Olive로 컴파일)

카탈로그에 없는 모델이 필요한 경우, Olive를 사용하여 Foundry Local용 ONNX로 컴파일하세요.

고급 흐름 (단계는 문서를 참조하세요):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
문서:
- BYOM 컴파일: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) 문제 해결

- 서비스 상태 및 로그 확인:
```cmd
foundry service status
foundry service diag
```
- 캐시 지우기 또는 이동:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- 최신 미리보기로 업데이트:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) 관련 Windows 개발자 경험

- Foundry Local 및 Windows ML을 포함한 Windows 로컬 vs 클라우드 AI 선택:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit과 Foundry Local (채팅 엔드포인트 URL을 얻으려면 `foundry service status`를 사용하세요):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[다음 Windows 개발자](./windowdeveloper.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.