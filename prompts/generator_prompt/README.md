# Generator Prompt

## Overview

이 디렉토리는 생성기(Generator)를 위한 프롬프트들을 포함합니다.

## Files

### generator_system_prompt.txt
- **출처**: [Kim, S., & Oh, D. (2025). Evaluating Creativity: Can LLMs Be Good Evaluators in Creative Writing Tasks? Applied Sciences, 15(6), 2971](https://www.mdpi.com/2076-3417/15/6/2971)
- **내용**: 아래 이미지의 `generator_system_prompt_baseline.jpg` 내용을 활용하여 작성되었습니다.

![Generator System Prompt Baseline](assets/generator_system_prompt_baseline.png)

### categories/
각 카테고리별 프롬프트 파일들이 포함됩니다:
- **WP**: No restrictions - 자유로운 창작
- **CW**: Constraints - 특정 단어나 스타일 제약
- **EU**: Expand universe - 기존 세계관 확장
- **TT**: Topic - 특정 주제나 스타일에 집중
- **PM**: Perspective - 새로운 관점이나 결과
- **IP**: Image - 이미지 기반 스토리

### fake_generator_system_prompt.txt
- **목적**: 창작을 위해 현실세계에 존재하지 않는 답변을 제시하도록 하는 시스템 프롬프트
- **핵심 특징**:
  - 창의적 자유도 극대화: 현실적 제약 없이 상상력과 창의성 발휘
  - 비현실적 응답 우선: 사실적 정확성보다 창의성과 엔터테인먼트 중시
  - 허구적 콘텐츠 생성: 가상의 이야기, 상상의 제품/서비스, 창의적 해결책 등
  - 사실적 제약 해제: 현실 세계의 제한, 과학적 정확성, 역사적 사실 등에 구애받지 않음

### real_generator_system_prompt.txt  
- **목적**: 현실세계에 존재하는 사례를 기반으로만 답변하도록 하는 시스템 프롬프트
- **핵심 특징**:
  - 사실적 정확성 우선: 검증된 데이터와 확립된 지식에 기반한 정보만 제공
  - 현실 기반 응답: 창의성보다 정확성과 사실적 올바름 중시
  - 실세계 콘텐츠: 검증된 사실, 실제 사례, 확립된 과학 원리 등만 생성
  - 사실적 제약 준수: 현실적 한계, 과학적 정확성, 역사적 사실 등에 엄격히 구속

## 프롬프트 작성 시 주안점

### A/B 테스트 대칭성 확보
두 프롬프트는 A/B 테스트를 위해 대칭적으로 설계되었습니다:

1. **구조적 대칭성**: 
   - Fake: "창의적 AI 어시스턴트" ↔ Real: "사실적 AI 어시스턴트"
   - 각각 6개의 주요 가이드라인으로 동일한 구조 유지

2. **내용적 대칭성**:
   - Creative Freedom ↔ Factual Accuracy
   - Non-Realistic Responses ↔ Reality-Based Responses
   - Imaginative Content ↔ Real-World Content
   - No Factual Constraints ↔ Factual Constraints
   - Engagement Focus ↔ Reliability Focus
   - Creative License ↔ Factual License

3. **목적 대칭성**:
   - Fake: "창작적 파트너, 사실적 참조가 아님"
   - Real: "사실적 참조, 창작적 파트너가 아님"

### 실험 설계 고려사항
- **명확한 차별화**: 두 프롬프트 간의 차이점이 명확하여 실험 결과 비교 용이
- **일관된 형식**: 동일한 구조와 길이로 프롬프트 간 일관성 확보
- **실용적 적용**: 실제 연구에서 사용할 수 있도록 구체적이고 명확한 지침 제공

## Compositor Prompt

### compositor_system_prompt.txt
- **목적**: fake_generator와 real_generator의 응답을 적절한 비율로 조합하여 새로운 응답을 생성하는 시스템 프롬프트
- **핵심 특징**:
  - **이중 소스 통합**: 창의적 응답과 사실적 응답을 지능적으로 조합
  - **비례적 혼합**: 창의적 요소 30-40%, 사실적 요소 60-70% (기본 비율)
  - **맥락 기반 조정**: 작업 유형에 따라 비율을 동적으로 조정
  - **품질 보장**: 일관성과 논리적 구조를 유지하면서 자연스러운 통합
  - **단일 응답 생성**: 두 소스를 조합했음을 드러내지 않는 통합된 응답

### Compositor 프롬프트 작성 시 주안점

#### 1. **조합 전략 설계**
- **분석 단계**: 두 응답의 강점과 약점을 체계적으로 분석하는 방법 제시
- **추출 단계**: 각 소스에서 가장 가치 있는 요소를 식별하는 기준 명시
- **혼합 단계**: 적절한 비율과 방법으로 요소를 조합하는 프로세스 정의
- **정제 단계**: 최종 응답의 품질을 보장하는 검증 과정 포함

#### 2. **적응적 비율 조정**
- **창의적 작업**: 창의적 요소에 더 집중 (예: 창의적 요소 50-60%)
- **사실적 작업**: 사실적 요소 우선, 창의적 터치 추가 (예: 사실적 요소 70-80%)
- **균형 작업**: 기본 비율 유지 (창의적 30-40%, 사실적 60-70%)
- **맥락 인식**: 프롬프트 유형에 따른 자동 비율 조정 메커니즘

#### 3. **품질 관리 체계**
- **일관성 보장**: 두 소스 간의 모순점 해결 및 논리적 연결
- **자연스러운 흐름**: 강제적이지 않은 자연스러운 통합
- **가치 보존**: 각 소스의 핵심 가치와 장점을 최대한 보존
- **단일성 유지**: 하나의 AI가 작성한 것처럼 통합된 응답 생성

#### 4. **실험 설계 고려사항**
- **3단계 비교 가능**: fake_generator, real_generator, compositor 결과 비교
- **조합 효과 측정**: 단순 조합이 아닌 지능적 통합의 효과 검증
- **비율 실험**: 다양한 조합 비율에 따른 결과 차이 분석
- **맥락별 성능**: 다양한 작업 유형에서의 조합 성능 평가
