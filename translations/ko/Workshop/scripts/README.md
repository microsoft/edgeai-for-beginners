# 워크숍 스크립트

이 디렉토리에는 워크숍 자료의 품질과 일관성을 유지하기 위해 사용되는 자동화 및 지원 스크립트가 포함되어 있습니다.

## 내용물

| 파일 | 목적 |
|------|---------|
| `lint_markdown_cli.py` | 마크다운 코드 블록에서 사용이 중단된 Foundry Local CLI 명령 패턴을 차단합니다. |
| `export_benchmark_markdown.py` | 다중 모델 지연 시간 벤치마크를 실행하고 Markdown + JSON 보고서를 생성합니다. |

## 1. 마크다운 CLI 패턴 린터

`lint_markdown_cli.py`는 번역되지 않은 `.md` 파일에서 **코드 블록 내부**(``` ... ```)에 사용이 금지된 Foundry Local CLI 패턴을 스캔합니다. 정보성 텍스트에서는 역사적 맥락을 위해 중단된 명령을 언급할 수 있습니다.

### 사용 중단된 패턴 (코드 블록 내부에서 차단됨)

린터는 사용이 중단된 CLI 패턴을 차단합니다. 대신 최신 대안을 사용하세요.

### 필수 대체
| 사용 중단됨 | 대신 사용 |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | 벤치마크 스크립트 + 시스템 도구 (`작업 관리자`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### 종료 코드
| 코드 | 의미 |
|------|---------|
| 0 | 위반 사항 없음 |
| 1 | 하나 이상의 사용 중단된 패턴 발견 |

### 로컬 실행
저장소 루트에서 실행 (권장):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Pre-Commit Hook (선택 사항)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
이 설정은 사용 중단된 패턴을 도입하는 커밋을 차단합니다.

### CI 통합
GitHub Action 워크플로 (`.github/workflows/markdown-cli-lint.yml`)는 `main` 및 `Reactor` 브랜치에 대한 모든 푸시 및 풀 요청에서 린터를 실행합니다. 실패한 작업은 병합 전에 수정해야 합니다.

### 새로운 사용 중단 패턴 추가
1. `lint_markdown_cli.py`를 엽니다.
2. `DEPRECATED` 목록에 튜플 `(regex, suggestion)`을 추가합니다. 원시 문자열을 사용하고 적절한 경우 `\b` 단어 경계를 포함하세요.
3. 로컬에서 린터를 실행하여 감지를 확인합니다.
4. 커밋하고 푸시합니다. CI가 새로운 규칙을 강제합니다.

예시 추가:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### 설명적 언급 허용
코드 블록만 강제 적용되므로, 내러티브 텍스트에서 사용 중단된 명령을 안전하게 설명할 수 있습니다. 코드 블록 내부에서 대조를 위해 반드시 보여줘야 한다면, 삼중 백틱 없이 블록을 추가하거나 (예: 들여쓰기 또는 인용) 의사 형태로 다시 작성하세요.

### 특정 파일 건너뛰기 (고급)
필요한 경우, 레거시 예제를 저장소 외부의 별도 파일에 래핑하거나 초안 작성 중 다른 확장자로 이름을 변경하세요. 번역된 복사본에 대한 의도적 건너뛰기는 자동으로 처리됩니다 (`translations` 경로 포함).

### 문제 해결
| 문제 | 원인 | 해결책 |
|-------|-------|-----------|
| 린터가 업데이트한 줄을 플래그로 표시 | 정규식이 너무 광범위함 | 추가 단어 경계 (`\b`) 또는 앵커로 패턴을 좁히세요 |
| CI 실패, 로컬에서는 통과 | 다른 Python 버전 또는 커밋되지 않은 변경 사항 | 로컬에서 다시 실행, 작업 트리 정리, 워크플로 Python 버전 확인 (3.11) |
| 임시로 우회해야 함 | 긴급 핫픽스 | 즉시 수정 적용; 임시 브랜치와 후속 PR 사용 고려 (우회 스위치 추가는 피하세요) |

### 근거
*현재* 안정적인 CLI 표면과 문서를 일치시키는 것은 워크숍 마찰을 줄이고 학습자 혼란을 방지하며, 유지 관리되는 Python 스크립트를 통해 성능 측정을 중앙 집중화합니다.

---
워크숍 품질 도구 체인의 일부로 유지 관리됩니다. 개선 사항 (예: 자동 수정 제안 또는 HTML 보고서 생성)을 위해 이슈를 열거나 PR을 제출하세요.

## 2. 샘플 검증 스크립트

`validate_samples.py`는 모든 Python 샘플 파일을 구문, import, 모범 사례 준수 여부를 검증합니다.

### 사용법
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### 검증 항목
- ✅ Python 구문 유효성
- ✅ 필수 import 존재 여부
- ✅ 오류 처리 구현 (상세 모드)
- ✅ 타입 힌트 사용 (상세 모드)
- ✅ 함수 docstring (상세 모드)
- ✅ SDK 참조 링크 (상세 모드)

### 환경 변수
- `SKIP_IMPORT_CHECK=1` - import 검증 건너뛰기
- `SKIP_SYNTAX_CHECK=1` - 구문 검증 건너뛰기

### 종료 코드
- `0` - 모든 샘플이 검증 통과
- `1` - 하나 이상의 샘플이 실패

## 3. 샘플 테스트 실행기

`test_samples.py`는 모든 샘플에 대해 스모크 테스트를 실행하여 오류 없이 실행되는지 확인합니다.

### 사용법
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### 사전 요구 사항
- Foundry Local 서비스 실행 중: `foundry service start`
- 모델 로드됨: `foundry model run phi-4-mini`
- 종속성 설치됨: `pip install -r requirements.txt`

### 테스트 항목
- ✅ 샘플이 런타임 오류 없이 실행 가능
- ✅ 필수 출력 생성
- ✅ 실패 시 적절한 오류 처리
- ✅ 성능 (실행 시간)

### 환경 변수
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - 테스트에 사용할 모델
- `TEST_TIMEOUT=30` - 샘플당 타임아웃 (초)

### 예상 실패
일부 테스트는 선택적 종속성이 설치되지 않은 경우 실패할 수 있습니다 (예: `ragas`, `sentence-transformers`). 설치 방법:
```bash
pip install sentence-transformers ragas datasets
```

### 종료 코드
- `0` - 모든 테스트 통과
- `1` - 하나 이상의 테스트 실패

## 4. 벤치마크 마크다운 내보내기

스크립트: `export_benchmark_markdown.py`

모델 세트에 대한 재현 가능한 성능 표를 생성합니다.

### 사용법
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### 출력물
| 파일 | 설명 |
|------|-------------|
| `benchmark_report.md` | 마크다운 표 (평균, p95, 초당 토큰, 선택적 첫 번째 토큰) |
| `benchmark_report.json` | 비교 및 기록을 위한 원시 메트릭 배열 |

### 옵션
| 플래그 | 설명 | 기본값 |
|------|-------------|---------|
| `--models` | 쉼표로 구분된 모델 별칭 | (필수) |
| `--prompt` | 각 라운드에서 사용된 프롬프트 | (필수) |
| `--rounds` | 모델당 라운드 수 | 3 |
| `--output` | 마크다운 출력 파일 | `benchmark_report.md` |
| `--json` | JSON 출력 파일 | `benchmark_report.json` |
| `--fail-on-empty` | 모든 벤치마크가 실패하면 비-제로 종료 | 꺼짐 |

환경 변수 `BENCH_STREAM=1`은 첫 번째 토큰 지연 시간 측정을 추가합니다.

### 참고 사항
- 일관된 모델 부트스트랩 및 캐싱을 위해 `workshop_utils`를 재사용합니다.
- 다른 작업 디렉토리에서 실행되는 경우, 스크립트는 `workshop_utils`를 찾기 위해 경로 폴백을 시도합니다.
- GPU 비교를 위해: 한 번 실행, CLI 설정을 통해 가속 활성화, 다시 실행하고 JSON을 비교하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.