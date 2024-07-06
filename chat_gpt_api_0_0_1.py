import openai

class Chatgpt:
    def __init__(self, api_key: str, model_name: str = "gpt-3.5-turbo"):
        self.messages = []
        self.model_name = model_name
        openai.api_key = api_key

    def chatsession(self, prompt: str, temperature: float = 0.0, max_tokens: int = 1000, top_p: float = 1.0):
        self.messages.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=self.messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )

        self.messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        return response['choices'][0]['message']['content']
    
    def get_chat_history(self):
        return self.messages