import os
from openai import OpenAI
from generator.utils import load_category_prompt

"""
LLM을 사용하여 현실에 존재하는 내용을 기반으로 답변하는 LLM 기반 데이터 생성기 입니다. 
"""

class RealGenerator:
    def __init__(self, system_prompt, model = "gpt-4o"):
        self.system_prompt = system_prompt
        self.model = model

    def generate(self, question, category = "wp"):

        # 0. 카테고리별 시스템 프롬프트 + real_generator_system_prompt + generator_system_prompt 조합
        prompt = self._generate_prompt(category)
        # 1. 주어진 컨텍스트를 기반으로 현실적인 응답을 생성함. 
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

    def _generate_prompt(self, category, path = "prompts/generator_prompt/real_generator_system_prompt.txt"):

        # category 별로 프롬프트를 다르게 설정하고, 컨텍스트를 조합하여 프롬프트를 생성함. 

        # 1. real generator의 system prompt 파일을 읽어옴. 
        with open(path, "r") as f:
            real_generator_system_prompt = f.read()

        # 2. generator의 system prompt 파일을 읽어옴. 

        # 3. 카테고리별 프롬프트를 가져옴
        category_prompt = load_category_prompt(category)

        # 4. 모든 프롬프트를 조합
        prompt = self.system_prompt + "\n\n" + real_generator_system_prompt + "\n\n" + category_prompt
        
        return prompt