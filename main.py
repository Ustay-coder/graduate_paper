from dotenv import load_dotenv
import os
from generator.comparison.compositor import Compositor
from generator.control.generator import Generator
from evaluator.evaluator import Evaluator
from generator.utils import load_system_prompt

# .env 파일 로드
load_dotenv()

def main(): 

    # 1. 질문지를 로드함. 
    test_questions_list = ['고령자들을 위한 최적의 암 발견 방법은 무엇일까?']
    # 1-1. Generator의 시스템 프롬프트를 로드함
    system_prompt = load_system_prompt("prompts/generator_prompt/generator_system_prompt.txt") 
    # 1-2. Compositor의 system prompt 설정함. 
    compositor_system_prompt = load_system_prompt("prompts/compositor_prompt/compositor_system_prompt.txt")
    # 2. 동일한 질문을 가지고 generator/comparsion, generator/control 두 그룹에서 데이터를 생성함. 

    for question in test_questions_list:
        # 2-1. 질문을 가지고 generator/comparsion 그룹에서 데이터를 생성함.
        compositor = Compositor(system_prompt = compositor_system_prompt)
        data_comparison = compositor.generate(question)
        # 2-2. 질문을 가지고 generator/control 그룹에서 데이터를 생성함. 
        control_generator = Generator(system_prompt = system_prompt)
        data_control = control_generator.generate(question)

        print(f"data_comparison: {data_comparison}\n")
        print(f"data_control: {data_control}\n")

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