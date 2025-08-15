import os 
from openai import OpenAI

class Evaluator: 
    def __init__(self, model = "gpt-4o", prompt = "prompts/evaluator_prompt/evaluator_system_prompt.txt"):
        self.model = model
        self.prompt = prompt

    def evaluate(self, context):

        """ context의 점수를 매기는 함수 """

        # 1. 프롬프트 생성
        prompt = self._generate_prompt()

        # 2. 프롬프트를 기반으로 점수를 매기는 함수 호출
        response = self._evaluate_response(prompt, context)

        # 3. 점수를 반환
        return response

    def _evaluate_response(self, prompt, context):

        # 1. 프롬프트를 기반으로 점수를 매기는 함수 호출
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt}, 
                {"role": "user", "content": context}
            ]
        )
        return response.choices[0].message.content

    def _generate_prompt(self):
        # 추후에 Temperature와 Role에 따른 프롬프트를 생성할 수 있도록 수정해야 함. 

        return self.prompt