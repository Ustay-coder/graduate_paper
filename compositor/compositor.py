"""
LLM을 사용하여 fake_generator와 real_generator의 응답을 적절한 비율로 조합하여 새로운 응답을 생성하는 데이터 생성기 입니다. 
"""

class Compositor:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def generate(self, context):
        pass

    def _generate_prompt(self, context):
        pass

    def _generate_response(self, prompt):
        pass