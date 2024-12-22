from mistralai import Mistral

class ChatClient:
    def __init__(self, api_key, model):
        self.client = Mistral(api_key=api_key)
        self.model = model

    def get_response(self, conversation_history):
        response = self.client.chat.complete(model=self.model, messages=conversation_history)
        return response.choices[0].message.content
