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
- 가짜 생성기(Fake Generator)를 위한 시스템 프롬프트
- **추가 예정**

### real_generator_system_prompt.txt  
- 실제 생성기(Real Generator)를 위한 시스템 프롬프트
- **추가 예정**
