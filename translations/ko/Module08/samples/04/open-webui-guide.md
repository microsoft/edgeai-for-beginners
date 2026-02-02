# Open WebUI + Foundry Local 통합 가이드

이 가이드는 Open WebUI를 Microsoft Foundry Local에 연결하여 로컬 AI 모델로 구동되는 전문적인 ChatGPT 스타일 인터페이스를 설정하는 방법을 설명합니다.

## 개요

Open WebUI는 현대적이고 사용하기 쉬운 채팅 인터페이스를 제공하며, OpenAI 호환 API에 연결할 수 있습니다. Foundry Local과 연결하면 다음과 같은 이점을 얻을 수 있습니다:

- **전문 UI**: 현대적인 디자인의 ChatGPT 스타일 인터페이스
- **로컬 프라이버시**: 모든 처리가 사용자의 장치에서 이루어짐
- **모델 전환**: 다양한 로컬 모델 간 손쉬운 전환
- **대화 기록**: 지속적인 채팅 기록 및 컨텍스트 유지
- **파일 업로드**: 문서 분석 및 파일 처리 기능
- **맞춤형 페르소나**: 시스템 프롬프트 및 역할 커스터마이징

## 사전 준비

### 필수 소프트웨어

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### 모델 로드

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## 빠른 설정 (권장)

### 1단계: Docker로 Open WebUI 실행

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### 2단계: 초기 설정

1. **브라우저 열기**: `http://localhost:3000`으로 이동
2. **계정 생성**: 관리자 사용자 설정 (첫 번째 사용자가 관리자가 됨)
3. **연결 확인**: 모델이 자동으로 드롭다운에 표시되어야 함

### 3단계: 연결 테스트

1. 드롭다운에서 모델 선택 (예: "phi-4-mini")
2. 테스트 메시지 입력: "안녕하세요! 자기소개를 해주세요."
3. 로컬 모델에서 스트리밍 응답이 표시되어야 함

## 고급 설정

### 환경 변수

| 변수 | 목적 | 기본값 | 예시 |
|------|------|--------|------|
| `OPENAI_API_BASE_URL` | Foundry Local 엔드포인트 | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API 키 (필수지만 로컬에서는 사용되지 않음) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | 세션 암호화 키 | 자동 생성 | `your-secret-key` |
| `ENABLE_SIGNUP` | 신규 사용자 등록 허용 | `True` | `False` |

### 수동 설정 (대안)

환경 변수가 작동하지 않을 경우 수동으로 설정:

1. **설정 열기**: 설정 아이콘(기어)을 클릭
2. **연결로 이동**: 설정 → 연결 → OpenAI
3. **API 세부 정보 설정**:
   - API 기본 URL: `http://host.docker.internal:51211/v1`
   - API 키: `foundry-local-key` (아무 값이나 사용 가능)
4. **저장 및 테스트**: "저장" 클릭 후 모델로 테스트

### 지속적인 데이터 저장

대화 및 설정을 지속적으로 저장하려면:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## 문제 해결

### 연결 문제

**문제**: "연결 거부됨" 또는 모델이 로드되지 않음

**해결 방법**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### 모델이 나타나지 않음

**문제**: Open WebUI에 드롭다운에 모델이 표시되지 않음

**디버깅 단계**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**해결**: 모델이 제대로 로드되었는지 확인:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker 네트워크 문제

**문제**: `host.docker.internal`이 해결되지 않음

**Windows 해결 방법**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**대안**: 머신의 IP 찾기:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### 성능 문제

**응답이 느림**:
1. 모델이 GPU 가속을 사용하는지 확인: `foundry service ps`
2. 충분한 시스템 리소스(RAM/GPU 메모리) 확인
3. 테스트용으로 더 작은 모델 사용 고려

**메모리 문제**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## 사용 가이드

### 기본 채팅

1. **모델 선택**: 드롭다운에서 Foundry Local 모델 선택
2. **메시지 입력**: 하단의 텍스트 입력 사용
3. **전송**: Enter 키를 누르거나 전송 버튼 클릭
4. **응답 보기**: 실시간 스트리밍 응답 확인

### 고급 기능

**파일 업로드**:
1. 클립 아이콘 클릭
2. 문서 업로드 (PDF, TXT 등)
3. 콘텐츠에 대한 질문하기
4. 모델이 문서를 분석하고 응답 제공

**맞춤형 시스템 프롬프트**:
1. 설정 → 개인화
2. 맞춤형 시스템 프롬프트 설정
3. 일관된 AI 성격/행동 생성

**대화 관리**:
- **새 채팅**: "+" 클릭하여 새 대화 시작
- **채팅 기록**: 사이드바에서 이전 대화 접근
- **내보내기**: 채팅 기록을 텍스트/JSON으로 다운로드

**모델 비교**:
1. 동일한 Open WebUI를 여러 브라우저 탭에서 열기
2. 각 탭에서 다른 모델 선택
3. 동일한 프롬프트에 대한 응답 비교

### 통합 패턴

**개발 워크플로우**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## 프로덕션 배포

### 보안 설정

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### 다중 사용자 설정

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### 모니터링 및 로깅

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## 정리

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## 다음 단계

### 개선 아이디어

1. **맞춤형 모델**: Foundry Local에 자체 미세 조정 모델 추가
2. **API 통합**: Open WebUI 기능을 통해 외부 API 연결
3. **문서 처리**: 고급 RAG 파이프라인 설정
4. **멀티모달**: 이미지 분석을 위한 비전 모델 구성

### 확장 고려사항

- **로드 밸런싱**: 리버스 프록시 뒤에 여러 Foundry Local 인스턴스 배치
- **모델 라우팅**: 다양한 사용 사례에 적합한 모델 선택
- **리소스 관리**: 동시 사용자에 대한 GPU 메모리 최적화
- **백업 전략**: 대화 데이터 및 설정의 정기적인 백업

## 참고 자료

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---

