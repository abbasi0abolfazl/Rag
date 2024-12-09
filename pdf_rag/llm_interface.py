import requests
from typing import List, Dict

class LLMInterface:
    def __init__(self, model_name: str = "llama2"):
        self.model_name = model_name
        self.api_url = "http://localhost:11434/api/generate"

    def generate_response(self, prompt: str, context: List[str]) -> str:
        """Generate response using Ollama."""
        formatted_prompt = f"""Context information is below.
        ---------------------
        {' '.join(context)}
        ---------------------
        Given the context information, please answer the question: {prompt}
        Answer:"""

        response = requests.post(
            self.api_url,
            json={
                "model": self.model_name,
                "prompt": formatted_prompt,
                "stream": False
            }
        )
        
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception(f"Error from Ollama API: {response.text}")
