from openai import OpenAI
import os
from generator.utils import load_category_prompt


"""
LLM을 사용하여 컨트롤 데이터를 생성하는 데이터 생성기 입니다. 
"""

class Generator:
    def __init__(self, llm, system_prompt, model = "gpt-4o"):
        self.llm = llm
        self.system_prompt = system_prompt
        self.model = model

    def generate(self, question, category = "wp"):

        # 0. 순수하게 system_prompt + category_prompt 조합하여 답변하도록 설정 
        prompt = self._generate_prompt(category)
        # 1. 주어진 컨텍스트를 기반으로 가짜 응답을 생성함. 
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content

    def _generate_prompt(self, category):


        # 1. 카테고리별 system prompt 파일을 읽어옴. 
        category_prompt = load_category_prompt(category)

        # 2. 모든 프롬프트를 조합
        prompt = self.system_prompt + "\n\n" + category_prompt

        return prompt