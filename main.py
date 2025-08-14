from dotenv import load_dotenv
import os
from generator.comparison.compositor import Compositor
from generator.control.generator import Generator
from evaluator.evaluator import Evaluator
from generator.utils import load_system_prompt

# .env 파일 로드
load_dotenv()

def main(): 
    print("=== 프로그램 시작 ===")
    
    # 1. 질문지를 로드함. 
    print("1단계: 질문지 로드 중...")
    test_questions_list = ['고령자들을 위한 최적의 암 발견 방법은 무엇일까?']
    print(f"   로드된 질문: {test_questions_list}")
    
    # 1-1. Generator의 시스템 프롬프트를 로드함
    print("2단계: Generator 시스템 프롬프트 로드 중...")
    try:
        system_prompt = load_system_prompt("prompts/generator_prompt/generator_system_prompt.txt") 
        print("   Generator 시스템 프롬프트 로드 완료")
    except Exception as e:
        print(f"   에러 발생: {e}")
        return
    
    # 1-2. Compositor의 system prompt 설정함. 
    print("3단계: Compositor 시스템 프롬프트 로드 중...")
    try:
        compositor_system_prompt = load_system_prompt("prompts/compositor_prompt/compositor_system_prompt.txt")
        print("   Compositor 시스템 프롬프트 로드 완료")
    except Exception as e:
        print(f"   에러 발생: {e}")
        return
    
    # 2. 동일한 질문을 가지고 generator/comparsion, generator/control 두 그룹에서 데이터를 생성함. 
    print("4단계: 데이터 생성 시작...")

    for i, question in enumerate(test_questions_list):
        print(f"   질문 {i+1} 처리 중: {question}")
        
        # 2-1. 질문을 가지고 generator/comparsion 그룹에서 데이터를 생성함.
        print("   4-1단계: Compositor로 데이터 생성 중...")
        try:
            compositor = Compositor(system_prompt = compositor_system_prompt)
            print("     Compositor 객체 생성 완료")
            data_comparison = compositor.generate(question)
            print("     Compositor 데이터 생성 완료")
        except Exception as e:
            print(f"     Compositor 에러 발생: {e}")
            return
        
        # 2-2. 질문을 가지고 generator/control 그룹에서 데이터를 생성함. 
        print("   4-2단계: Control Generator로 데이터 생성 중...")
        try:
            control_generator = Generator(system_prompt = system_prompt)
            print("     Control Generator 객체 생성 완료")
            data_control = control_generator.generate(question)
            print("     Control Generator 데이터 생성 완료")
        except Exception as e:
            print(f"     Control Generator 에러 발생: {e}")
            return

        print("   4-3단계: 생성된 데이터 출력...")
        print(f"   data_comparison: {data_comparison}\n")
        print(f"   data_control: {data_control}\n")

    # 3. 생성된 데이터를 evaluator에서 평가함. 
    # evaluator = Evaluator()
    # data_comparison_evaluated = evaluator.evaluate(data_comparison)
    # data_control_evaluated = evaluator.evaluate(data_control)
    
    # # 4. 평가된 데이터를 비교함.
    # analyze = evaluator.analyze(data_comparison_evaluated, data_control_evaluated)

    # # 5. 비교 결과를 출력/저장함. 
    # print(analyze)
    # evaluator.save_result(analyze)

if __name__ == "__main__":
    main()