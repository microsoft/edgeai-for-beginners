# 샘플 04: Chainlit을 활용한 프로덕션 채팅 애플리케이션

Microsoft Foundry Local을 사용하여 프로덕션 준비가 완료된 채팅 애플리케이션을 구축하는 다양한 접근 방식을 보여주는 포괄적인 샘플입니다. 현대적인 웹 인터페이스, 스트리밍 응답, 최첨단 브라우저 기술을 포함합니다.

## 포함된 내용

- **🚀 Chainlit 채팅 앱** (`app.py`): 스트리밍 기능을 갖춘 프로덕션 준비 채팅 애플리케이션
- **🌐 WebGPU 데모** (`webgpu-demo/`): 하드웨어 가속을 활용한 브라우저 기반 AI 추론
- **🎨 Open WebUI 통합** (`open-webui-guide.md`): 전문적인 ChatGPT 스타일 인터페이스
- **📚 교육용 노트북** (`chainlit_app.ipynb`): 대화형 학습 자료

## 빠른 시작

### 1. Chainlit 채팅 애플리케이션

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

열리는 위치: `http://localhost:8080`

### 2. WebGPU 브라우저 데모

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

열리는 위치: `http://localhost:5173`

### 3. Open WebUI 설정

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

열리는 위치: `http://localhost:3000`

## 아키텍처 패턴

### 로컬 vs 클라우드 결정 매트릭스

| 시나리오 | 추천 | 이유 |
|----------|------|------|
| **민감한 데이터** | 🏠 로컬 (Foundry) | 데이터가 기기를 벗어나지 않음 |
| **복잡한 추론** | ☁️ 클라우드 (Azure OpenAI) | 더 큰 모델에 접근 가능 |
| **실시간 채팅** | 🏠 로컬 (Foundry) | 낮은 지연 시간, 빠른 응답 |
| **문서 분석** | 🔄 하이브리드 | 추출은 로컬, 분석은 클라우드 |
| **코드 생성** | 🏠 로컬 (Foundry) | 개인정보 보호 + 특화된 모델 |
| **연구 작업** | ☁️ 클라우드 (Azure OpenAI) | 광범위한 지식 기반 필요 |

### 기술 비교

| 기술 | 사용 사례 | 장점 | 단점 |
|------|----------|------|------|
| **Chainlit** | Python 개발자, 빠른 프로토타이핑 | 쉬운 설정, 스트리밍 지원 | Python 전용 |
| **WebGPU** | 최대 개인정보 보호, 오프라인 시나리오 | 브라우저 네이티브, 서버 불필요 | 제한된 모델 크기 |
| **Open WebUI** | 프로덕션 배포, 팀 | 전문 UI, 사용자 관리 | Docker 필요 |

## 사전 요구 사항

- **Foundry Local**: 설치 및 실행 중 ([다운로드](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ 및 가상 환경
- **모델**: 최소 하나 로드됨 (`foundry model run phi-4-mini`)
- **브라우저**: WebGPU 지원 Chrome/Edge
- **Docker**: Open WebUI용 (선택 사항)

## 설치 및 설정

### 1. Python 환경 설정

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local 설정

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## 샘플 애플리케이션

### Chainlit 채팅 애플리케이션

**특징:**
- 🚀 **실시간 스트리밍**: 토큰이 생성되는 즉시 표시
- 🛡️ **강력한 오류 처리**: 우아한 복구 및 성능 저하 방지
- 🎨 **현대적인 UI**: 기본 제공 전문 채팅 인터페이스
- 🔧 **유연한 구성**: 환경 변수 및 자동 감지
- 📱 **반응형 디자인**: 데스크톱 및 모바일에서 작동

**빠른 시작:**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU 브라우저 데모

**특징:**
- 🌐 **브라우저 네이티브 AI**: 서버 불필요, 브라우저에서만 실행
- ⚡ **WebGPU 가속**: 하드웨어 가속 지원
- 🔒 **최대 개인정보 보호**: 데이터가 기기를 벗어나지 않음
- 🎯 **설치 불필요**: 호환 브라우저에서 바로 작동
- 🔄 **우아한 대체**: WebGPU가 없을 경우 CPU로 자동 전환

**실행:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI 통합

**특징:**
- 🎨 **ChatGPT 스타일 인터페이스**: 전문적이고 익숙한 UI
- 👥 **다중 사용자 지원**: 사용자 계정 및 대화 기록
- 📁 **파일 처리**: 문서 업로드 및 분석
- 🔄 **모델 전환**: 다양한 모델 간 손쉬운 전환
- 🐳 **Docker 배포**: 프로덕션 준비 완료 컨테이너 설정

**빠른 설정:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## 구성 참조

### 환경 변수

| 변수 | 설명 | 기본값 | 예시 |
|------|------|--------|------|
| `MODEL` | 사용할 모델 별칭 | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local 엔드포인트 | 자동 감지 | `http://localhost:51211` |
| `API_KEY` | API 키 (로컬에서는 선택 사항) | `""` | `your-api-key` |

## 문제 해결

### 일반적인 문제

**Chainlit 애플리케이션:**

1. **서비스를 사용할 수 없음:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **포트 충돌:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python 환경 문제:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU 데모:**

1. **WebGPU가 지원되지 않음:**
   - Chrome/Edge 113+로 업데이트
   - WebGPU 활성화: `chrome://flags/#enable-unsafe-webgpu`
   - GPU 상태 확인: `chrome://gpu`
   - 데모는 CPU로 자동 전환됨

2. **모델 로딩 오류:**
   - 모델 다운로드를 위한 인터넷 연결 확인
   - 브라우저 콘솔에서 CORS 오류 확인
   - HTTP로 제공 중인지 확인 (file:// 아님)

**Open WebUI:**

1. **연결 거부됨:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **모델이 나타나지 않음:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### 검증 체크리스트

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## 고급 사용법

### 성능 최적화

**Chainlit:**
- 스트리밍을 사용하여 더 나은 성능 제공
- 높은 동시성을 위해 연결 풀링 구현
- 반복 쿼리에 대해 모델 응답 캐싱
- 대화 기록이 큰 경우 메모리 사용 모니터링

**WebGPU:**
- 최대 개인정보 보호 및 속도를 위해 WebGPU 사용
- 작은 모델을 위한 모델 양자화 구현
- 백그라운드 처리를 위한 Web Workers 사용
- 브라우저 저장소에 컴파일된 모델 캐싱

**Open WebUI:**
- 대화 기록을 위한 지속 볼륨 사용
- Docker 컨테이너의 리소스 제한 구성
- 사용자 데이터를 위한 백업 전략 구현
- SSL 종료를 위한 리버스 프록시 설정

### 통합 패턴

**로컬/클라우드 하이브리드:**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**멀티모달 파이프라인:**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## 프로덕션 배포

### 보안 고려 사항

- **API 키**: 환경 변수를 사용하고 하드코딩하지 않기
- **네트워크**: 프로덕션에서 HTTPS 사용, 팀 액세스를 위한 VPN 고려
- **액세스 제어**: Open WebUI에 대한 인증 구현
- **데이터 개인정보 보호**: 로컬에 남는 데이터와 클라우드로 전송되는 데이터 감사
- **업데이트**: Foundry Local 및 컨테이너를 최신 상태로 유지

### 모니터링 및 유지 관리

- **상태 확인**: 엔드포인트 모니터링 구현
- **로그**: 모든 구성 요소에서 로그 중앙화
- **메트릭**: 응답 시간, 오류율, 리소스 사용 추적
- **백업**: 대화 데이터 및 구성의 정기 백업

## 참고 자료 및 리소스

### 문서
- [Chainlit 문서](https://docs.chainlit.io/) - 프레임워크 가이드
- [Foundry Local 문서](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Microsoft 공식 문서
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU 통합
- [Open WebUI 문서](https://docs.openwebui.com/) - 고급 구성

### 샘플 파일
- [`app.py`](../../../../../Module08/samples/04/app.py) - 프로덕션 Chainlit 애플리케이션
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - 교육용 노트북
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - 브라우저 기반 AI 추론
- [`open-webui-guide.md`](./open-webui-guide.md) - Open WebUI 설정 완전 가이드

### 관련 샘플
- [세션 4 문서](../../04.CuttingEdgeModels.md) - 전체 세션 가이드
- [Foundry Local 샘플](https://github.com/microsoft/foundry-local/tree/main/samples) - 공식 샘플

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.