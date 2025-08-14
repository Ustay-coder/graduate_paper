import os
from openai import OpenAI

"""
LLM을 사용하여 현실에 존재하지 않는 내용을 기반으로 답변하는 LLM 기반 데이터 생성기 입니다. 
"""

class FakeGenerator:
    def __init__(self, llm, system_prompt, model = "gpt-4o"):
        self.llm = llm
        self.system_prompt = system_prompt
        self.model = model

    def generate(self, context, category = "wp"):

        # 0. 카테고리별 시스템 프롬프트 + fake_generator_system_prompt + generator_system_prompt 조합
        prompt = self._generate_prompt(context, category)
        # 1. 주어진 컨텍스트를 기반으로 가짜 응답을 생성함. 
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": context}
            ]
        )
        return response.choices[0].message.content

    def _generate_prompt(self, context, category):

        # category 별로 프롬프트를 다르게 설정하고, 컨텍스트를 조합하여 프롬프트를 생성함. 

        # 1. fake generator의 system prompt 파일을 읽어옴. 
        with open("prompts/generator_prompt/fake_generator_system_prompt.txt", "r") as f:
            fake_generator_system_prompt = f.read()

        # 2. generator의 system prompt 파일을 읽어옴. 
        generator_system_prompt = self.system_prompt


        # 3. 카테고리별 프롬프트를 가져옴
        category_prompt = self._load_category_prompt(category)

        # 4. 모든 프롬프트를 조합
        prompt = self.system_prompt + "\n\n" + fake_generator_system_prompt + "\n\n" + category_prompt + "\n\n" + generator_system_prompt
        
        return prompt

    def _load_category_prompt(self, category):
        """
        카테고리에 해당하는 프롬프트 파일을 로드합니다.
        
        Args:
            category (str): 카테고리 이름
            
        Returns:
            str: 카테고리별 프롬프트 내용
        """
        category_file_mapping = {
            "wp": "wp_prompt.txt",
            "cw": "cw_prompt.txt", 
            "eu": "eu_prompt.txt",
            "ip": "ip_prompt.txt",
            "mp": "mp_prompt.txt",
            "pi": "pi_prompt.txt",
            "pm": "pm_prompt.txt",
            "sp": "sp_prompt.txt",
            "tt": "tt_prompt.txt"
        }
        
        if category in category_file_mapping:
            file_path = f"prompts/generator_prompt/categories/{category_file_mapping[category]}"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()
            except FileNotFoundError:
                print(f"Warning: Category file {file_path} not found for category '{category}'")
                return ""
        else:
            print(f"Warning: Unknown category '{category}'")
            return ""

    def _generate_response(self, prompt):
        pass
        