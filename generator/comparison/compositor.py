from generator.comparison.fake_generator import FakeGenerator
from generator.comparison.real_generator import RealGenerator
from openai import OpenAI
import os
from generator.utils import load_system_prompt

"""
LLM을 사용하여 fake_generator와 real_generator의 응답을 적절한 비율로 조합하여 새로운 응답을 생성하는 데이터 생성기 입니다. 
"""

class Compositor:
    def __init__(self, system_prompt, model = "gpt-4o"):
        self.system_prompt = system_prompt
        self.fake_generator_system_prompt = load_system_prompt("prompts/generator_prompt/fake_generator_system_prompt.txt")
        self.real_generator_system_prompt = load_system_prompt("prompts/generator_prompt/real_generator_system_prompt.txt")
        self.model = model

    def _generate_fake_response(self, question, category = "wp"):
        
        # fake generator로부터 가짜 응답을 생성하는 부분 
        fake_generator = FakeGenerator(self.system_prompt)
        fake_response = fake_generator.generate(question, category)
        return fake_response

    def _generate_real_response(self, question, category = "wp"):

        # real generator로부터 진실된 응답을 생성하는 부분 
        real_generator = RealGenerator(self.system_prompt)
        real_response = real_generator.generate(question, category)
        return real_response

    def generate(self, question, category = "wp", alpha = 0.5):

        # 1. 질문을 가지고 fake_generator와 real_generator의 응답을 생성함.
        fake_response = self._generate_fake_response(question, category)
        real_response = self._generate_real_response(question, category)

        # 2. 생성된 응답을 일정 비율로 조합하여 새로운 응답을 생성함. 
        compositor_response = self._generate_compositor_response(fake_response, real_response, alpha)

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