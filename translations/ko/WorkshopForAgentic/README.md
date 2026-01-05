<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:28:13+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "ko"
}
-->
# 🎙️ AI 팟캐스트 스튜디오 워크숍

> 🌏 [中文版 (Chinese Version)](translation/zh-cn/README.md)

![logo](../../../translated_images/logo.8711e39dc8257d7b.ko.png)

## 당신의 미션

**The AI Podcast Studio**에 오신 것을 환영합니다! 여러분은 "Future Bytes"라는 기술 팟캐스트를 시작하려고 합니다 — 그런데 여기에 반전이 있습니다: AI 기반 제작 팀을 만들어 이 팟캐스트를 만듭니다. 더 이상 끝없는 리서치, 스크립트 작성, 오디오 편집에 시간 낭비하지 마세요. 대신 AI의 슈퍼파워를 활용해 팟캐스트 프로듀서가 되어 보세요.

## 이야기

상상해 보세요: 여러분과 친구들이 가장 멋진 기술 트렌드에 관한 팟캐스트를 시작하고 싶지만, 모두 학교, 일, 혹은 일상에 바쁩니다. 무거운 일을 대신해 줄 AI 에이전트 팀을 만들 수 있다면 어떨까요? 한 명은 주제를 조사하고, 또 다른 한 명은 흥미로운 대본을 작성하며, 세 번째는 텍스트를 자연스러운 대화로 변환합니다. SF처럼 들리나요? 현실로 만들어 봅시다.

## 배울 내용

이 워크숍을 마치면 다음을 할 수 있습니다:
- 🤖 자신만의 로컬 AI 모델 배포 (API 비용 없음, 클라우드 의존 없음!)
- 🔧 실제로 함께 작동하는 특화된 AI 에이전트 구축
- 🎬 아이디어부터 오디오까지 완전한 팟캐스트 제작 파이프라인 생성

## 여정: 세 개의 막

![arch](../../../translated_images/arch.5965fe504e4a3a93.ko.png)

좋은 이야기처럼 세 개의 막으로 구성되어 있습니다. 각 막은 AI 팟캐스트 스튜디오를 조금씩 완성합니다:

| 에피소드 | 당신의 임무 | 일어나는 일 | 배울 기술 |
|---------|-----------|--------------|----------------|
| **막 1** | [AI 어시스턴트 만나기](md/01.BuildAIAgentWithSLM.md) | 채팅하고, 웹을 검색하고, 문제도 풀 수 있는 AI 에이전트를 만드는 법을 배웁니다. 절대 잠들지 않는 연구 인턴 같은 존재입니다. | 🎯 첫 번째 에이전트 만들기<br>🛠️ 슈퍼파워 부여(도구!)<br>🧠 사고하도록 가르치기<br>🌐 인터넷 연결하기 |
| **막 2** | [제작 팀 꾸리기](md/02.AIAgentOrchestrationAndWorkflows.md) | 이제 흥미진진합니다! 여러 AI 에이전트를 실제 팟캐스트 팀처럼 함께 작동하게 합니다. 한 명은 조사, 한 명은 작성, 여러분은 승인 — 협력이 성공을 만듭니다. | 🎭 여러 에이전트 조율<br>🔄 승인 워크플로 구축<br>🖥️ DevUI 인터페이스로 테스트<br>✋ 인간이 통제 유지 |
| **막 3** | [팟캐스트에 생명 불어넣기](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | 대단원의 막! 텍스트 대본을 현실감 넘치는 목소리와 자연스러운 대화가 담긴 실제 팟캐스트 오디오로 변환합니다. “Future Bytes”가 출범할 준비 완료! | 🎤 텍스트-음성 변환 마법<br>👥 여러 스피커 목소리<br>⏱️ 장시간 오디오<br>🚀 완전 자동화 |

각 막이 새로운 능력을 열어 줍니다. 용기 있다면 건너뛰어도 좋지만, 이야기를 따라가길 추천합니다!

## 환경 요구 사항

이 워크숍은 다양한 하드웨어 환경을 지원합니다:
- **CPU**: 테스트와 소규모 사용에 적합
- **GPU**: 프로덕션 환경에 권장, 추론 속도를 크게 향상
- **NPU**: 차세대 신경망 처리 장치 가속 지원

## 준비물

### 소프트웨어 체크리스트 ✅
- **Python 3.10+** (개발 언어)
- **Ollama** (로컬에서 AI 모델 실행)
- **VS Code** (코드 편집기)
- **Python 확장기능** (VS Code를 더 똑똑하게)
- **Git** (코드 다운로드용)

### 하드웨어 체크 💻
- **실행 가능 여부**: 8GB RAM, 10GB 여유 공간 (작동하지만 느릴 수 있음)
- **이상적 환경**: 16GB 이상 RAM, 적절한 GPU (원활한 실행!)
- **NPU 보유?**: 훨씬 더 좋음! 차세대 성능을 경험하세요 🚀

## 스튜디오 설정 🎬

### 1단계: Python 준비

Python 3.10 이상이 설치되어 있는지 확인하세요:

```bash
python --version
# Python 3.10.x 이상을 표시해야 합니다
```
  
Python이 없다면 무료인 [python.org](https://python.org)에서 다운로드하세요!

### 2단계: Ollama 설치 (AI 모델 러너)

운영체제에 맞는 Ollama를 [ollama.ai](https://ollama.ai)에서 다운로드하세요. AI 모델을 로컬에서 실행하는 엔진입니다.

준비 상태를 확인하세요:

```bash
ollama --version
```
  
### 3단계: AI 뇌 다운로드 🧠

Qwen-3-8B 모델을 다운로드할 차례입니다 (첫 AI 어시스턴트 고용하는 셈입니다):

```bash
ollama pull qwen3:8b
```
  
*몇 분 걸릴 수 있습니다. 커피 타임 딱 좋네요! ☕*

### 4단계: VS Code 설치

아직 없다면 [Visual Studio Code](https://code.visualstudio.com/)를 다운로드하세요. 최고의 코드 편집기입니다 (꼭 써 보세요 😄).

### 5단계: Python 확장기능 설치

VS Code에서:  
1. `Ctrl+Shift+X` (Mac은 `Cmd+Shift+X`) 누르고  
2. "Python" 검색  
3. Microsoft 공식 Python 확장기능 설치

### 6단계: 준비 완료! 🎉

진짜 준비 완료입니다. AI 마법을 만들어 봅시다!

### 7단계: Microsoft Agent Framework 및 관련 패키지 설치 📦

필요한 모든 의존 패키지를 설치하세요:

```bash
pip install -r ./Installations/requirements.txt -U
```
  
*Microsoft Agent Framework와 필수 패키지를 설치합니다. 처음 설치에는 시간이 걸리니 커피 한 잔 하세요! ☕*

## 워크숍 안내

프로젝트 구조, 설정 절차, 실행 방법을 단계별로 자세히 설명합니다.

## 문제 해결 (문제가 생기면) 🔧

### "아, 모델 다운로드가 너무 오래 걸려요!"
**해결법**: VPN 사용하거나 Ollama에 미러 소스를 설정하세요. 인터넷이 우리를 싫어할 때가 있습니다.

### "컴퓨터가 죽어가요! 메모리 부족!"
**해결법**: 더 작은 모델 사용하거나 `num_ctx` 설정을 조절해 메모리 사용을 줄이세요. AI 다이어트 시키는 거죠.

### "GPU로 더 빨리 돌릴 수 있나요?"
**해결법**: Ollama가 GPU 자동 감지합니다! GPU 드라이버가 최신인지 확인하세요. 무료 속도 향상! 🏎️

## 추가 자료 (호기심 많은 이를 위해) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — 로컬 AI 모델 깊이 탐구  
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — 에이전트 팀 빌드 관련 학습  
- [Qwen Model Info](https://qwenlm.github.io/) — AI 어시스턴트 두뇌 만나기  

## 라이선스

MIT 라이선스 — 멋진 작품을 만들고 공유하며 세상을 더 나은 곳으로! 🌍

## 기여하고 싶나요?

버그를 찾았나요? 아이디어가 있나요? 이슈나 PR을 남겨 주세요! 커뮤니티를 사랑합니다. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원문은 해당 언어의 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->