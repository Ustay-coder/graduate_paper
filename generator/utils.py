

def load_category_prompt(category):
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
