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
