from generator.comparison.fake_generator import FakeGenerator
from generator.comparison.real_generator import RealGenerator
from openai import OpenAI
import os

"""
LLM을 사용하여 fake_generator와 real_generator의 응답을 적절한 비율로 조합하여 새로운 응답을 생성하는 데이터 생성기 입니다. 
"""

class Compositor:
    def __init__(self, llm, system_prompt, model = "gpt-4o"):
        self.llm = llm
        self.system_prompt = system_prompt
        self.model = model

    def _generate_fake_response(self, question):
        
        # fake generator로부터 가짜 응답을 생성하는 부분 
        fake_generator = FakeGenerator(self.llm, self.system_prompt)
        fake_response = fake_generator.generate(question)
        return fake_response

    def _generate_real_response(self, question):

        # real generator로부터 진실된 응답을 생성하는 부분 
        real_generator = RealGenerator(self.llm, self.system_prompt)
        real_response = real_generator.generate(question)
        return real_response

    def generate(self, question):

        # 1. 질문을 가지고 fake_generator와 real_generator의 응답을 생성함.
        fake_response = self._generate_fake_response(question)
        real_response = self._generate_real_response(question)

        # 2. 생성된 응답을 일정 비율로 조합하여 새로운 응답을 생성함. 
        compositor_response = self._generate_compositor_response(fake_response, real_response)

        return compositor_response

    def _generate_compositor_response(self, fake_response, real_response, alpha = 0.5):
        # fake_response와 real_response를 조합하여 새로운 응답을 생성하는 함수
        # 1. fake_response와 real_response와 조합 비율을 alpha 를 조합하여 새로운 응답을 생성함. 
        system_prompt = self.system_prompt
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        user_prompt = "fake_response: " + fake_response + "\nreal_response: " + real_response + "\n조합 비율: " + str(alpha)
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        return response.choices[0].message.content