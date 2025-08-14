import os
import openai

"""
LLM을 사용하여 현실에 존재하지 않는 내용을 기반으로 답변하는 LLM 기반 데이터 생성기 입니다. 
"""

class FakeGenerator:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def generate(self, context):
        pass

    def _generate_prompt(self, context):
        pass

    def _generate_response(self, prompt):
        pass