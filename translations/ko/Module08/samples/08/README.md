# Windows 11 채팅 샘플 - Foundry Local

Windows 11용 현대적인 채팅 애플리케이션으로, Microsoft Foundry Local을 아름다운 네이티브 인터페이스와 통합했습니다. Electron으로 제작되었으며 Microsoft의 공식 Foundry Local 패턴을 따릅니다.

## 개요

이 샘플은 Foundry Local을 통해 로컬 AI 모델을 활용하여 클라우드 의존 없이 사용자에게 프라이버시 중심의 AI 대화를 제공하는 프로덕션 준비된 채팅 애플리케이션을 만드는 방법을 보여줍니다.

## 주요 기능

### 🎨 **Windows 11 네이티브 디자인**
- Fluent Design System 통합
- Mica 소재 효과 및 투명성
- Windows 11 테마 지원
- 모든 화면 크기에 대응하는 반응형 레이아웃
- 자동 다크/라이트 모드 전환

### 🤖 **AI 모델 통합**
- Foundry Local 서비스 통합
- 핫스와핑 가능한 다중 모델 지원
- 실시간 스트리밍 응답
- 로컬 및 클라우드 모델 전환
- 모델 상태 및 건강 모니터링

### 💬 **채팅 경험**
- 실시간 입력 표시기
- 메시지 기록 유지
- 채팅 대화 내보내기
- 사용자 지정 시스템 프롬프트
- 대화 분기 및 관리

### ⚡ **성능 기능**
- 지연 로딩 및 가상화
- 긴 대화를 위한 최적화된 렌더링
- 백그라운드 모델 미리 로드
- 효율적인 메모리 관리
- 부드러운 애니메이션 및 전환

## 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## 사전 요구 사항

### 시스템 요구 사항
- **운영 체제**: Windows 11 (22H2 이상 권장)
- **RAM**: 최소 8GB, 대형 모델의 경우 16GB 이상 권장
- **저장 공간**: 모델을 위한 10GB 이상의 여유 공간
- **GPU**: 선택 사항이지만 빠른 추론을 위해 권장

### 소프트웨어 종속성
- **Node.js**: v18.0.0 이상
- **Foundry Local**: Microsoft의 최신 버전
- **Git**: 클로닝 및 개발용

## 설치

### 1. Foundry Local 설치
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. 클론 및 설정
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. 환경 구성
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. 애플리케이션 실행
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## 프로젝트 구조

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## 주요 기능 심층 분석

### Windows 11 통합

**Fluent Design System**
- Mica 배경 소재
- 아크릴 투명 효과
- 둥근 모서리 및 현대적인 간격
- 네이티브 Windows 11 색상 팔레트
- 접근성을 위한 의미론적 색상 토큰

**네이티브 Windows 기능**
- 최근 채팅을 위한 점프 리스트 통합
- 새 메시지에 대한 Windows 알림
- 모델 작업을 위한 작업 표시줄 진행 표시
- 빠른 작업을 위한 시스템 트레이 통합
- Windows Hello 인증 지원

### AI 모델 관리

**로컬 모델**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**하이브리드 클라우드/로컬 지원**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### 채팅 인터페이스 기능

**실시간 스트리밍**
- 토큰별 응답 표시
- 부드러운 입력 애니메이션
- 요청 취소 가능
- 입력 표시기 및 상태

**대화 관리**
- 지속적인 채팅 기록
- 대화 내보내기/가져오기
- 메시지 검색 및 필터링
- 대화 분기
- 대화별 사용자 지정 시스템 프롬프트

**접근성**
- 전체 키보드 탐색
- 화면 읽기 프로그램 호환성
- 고대비 모드 지원
- 사용자 지정 가능한 글꼴 크기
- 음성 입력 통합

## 사용 예제

### 기본 채팅 통합
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### 모델 관리
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### 설정 및 사용자 지정
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## 구성 옵션

### 애플리케이션 설정
- **테마**: 자동, 라이트, 다크 모드
- **모델**: 기본 모델 선택
- **성능**: 추론 설정
- **프라이버시**: 데이터 보존 정책
- **알림**: 메시지 알림
- **단축키**: 키보드 단축키

### 채팅 설정
- **스트리밍**: 실시간 응답 활성화/비활성화
- **컨텍스트 길이**: 대화 메모리
- **온도**: 응답 창의성
- **최대 토큰**: 응답 길이 제한
- **시스템 프롬프트**: 기본 어시스턴트 동작

### 모델 설정
- **자동 다운로드**: 모델 자동 업데이트
- **캐시 크기**: 로컬 모델 저장 제한
- **성능 모드**: CPU 대 GPU 선호도
- **건강 점검**: 모니터링 간격

## 개발

### 소스에서 빌드하기
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### 디버깅
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### 테스트
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## 성능 최적화

### 메모리 관리
- 효율적인 메시지 가상화
- 자동 가비지 컬렉션
- 모델 메모리 모니터링
- 종료 시 리소스 정리

### 렌더링 최적화
- 긴 대화를 위한 가상 스크롤링
- 메시지 기록 지연 로딩
- 최적화된 React/DOM 업데이트
- GPU 가속 애니메이션

### 네트워크 최적화
- 연결 풀링
- 요청 배치 처리
- 자동 재시도 로직
- 오프라인 모드 지원

## 보안 고려 사항

### 데이터 프라이버시
- 로컬 우선 아키텍처
- 클라우드 데이터 전송 없음 (로컬 모드)
- 암호화된 대화 저장
- 안전한 자격 증명 관리

### 애플리케이션 보안
- 샌드박스 렌더러 프로세스
- 콘텐츠 보안 정책 (CSP)
- 원격 코드 실행 없음
- 안전한 IPC 통신

## 문제 해결

### 일반적인 문제

**Foundry Local이 시작되지 않음**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**모델 로딩 실패**
- 충분한 디스크 공간 확인
- 다운로드를 위한 인터넷 연결 확인
- GPU 드라이버 업데이트 확인
- 다른 모델 변형 시도

**성능 문제**
- 시스템 리소스 모니터링
- 모델 설정 조정
- 하드웨어 가속 활성화
- 다른 리소스 집약적인 애플리케이션 닫기

### 디버그 모드
환경 변수를 설정하여 디버그 로깅 활성화:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## 기여

### 개발 설정
1. 리포지토리 포크
2. 기능 브랜치 생성
3. 종속성 설치: `npm install`
4. 변경 사항 적용 및 테스트
5. 풀 리퀘스트 제출

### 코드 스타일
- ESLint 구성 제공
- 코드 포맷팅을 위한 Prettier
- 타입 안전성을 위한 TypeScript
- 문서를 위한 JSDoc 주석

## 학습 결과

이 샘플을 완료한 후 다음을 이해할 수 있습니다:

1. **Windows 11 네이티브 개발**
   - Fluent Design System 구현
   - 네이티브 Windows 통합
   - Electron 보안 모범 사례

2. **AI 모델 통합**
   - Foundry Local 서비스 아키텍처
   - 모델 라이프사이클 관리
   - 성능 모니터링 및 최적화

3. **실시간 채팅 시스템**
   - 스트리밍 응답 처리
   - 대화 상태 관리
   - 사용자 경험 패턴

4. **프로덕션 애플리케이션 개발**
   - 오류 처리 및 복구
   - 성능 최적화
   - 보안 고려 사항
   - 테스트 전략

## 다음 단계

- **샘플 09**: 다중 에이전트 오케스트레이션 시스템
- **샘플 10**: Foundry Local을 도구로 통합
- **고급 주제**: 사용자 지정 모델 미세 조정
- **배포**: 엔터프라이즈 배포 패턴

## 라이선스

이 샘플은 Microsoft Foundry Local 프로젝트와 동일한 라이선스를 따릅니다.

---

