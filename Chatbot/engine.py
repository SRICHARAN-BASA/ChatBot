from groq import Groq
from typing import List, Dict

class Chatbot:
    """Using this you can experience the encapsulation (_model) using this we hide implementation details from the user."""
    def __init__(self, api_key:str, model:str):
        self._client = Groq(api_key=api_key) #This is the protected variable
        self._model = model
        self.messages : List[Dict[str, str]] = []

    def add_system_message(self, content: str):
            """Adds a system message to the conversation."""
            self.messages.append({"role": "system", "content": content})

    def add_assistant_message(self, content: str):
                self.messages.append({"role": "assistant", "content": content})

    def get_streaming_response(self, user_input:str):
                    """Send user message and yield response through chunks."""
                    self.messages.append({"role": "user", "content": user_input})
                    stream = self._client.chat.completions.create(
                        model=self._model,
                        messages=self.messages,
                        stream=True,
                        temperature=0.7,
                        max_tokens=1024

                    )
                    response = ""
                    for chunk in stream:
                        if chunk.choices[0].delta.content:
                            content = chunk.choices[0].delta.content
                            response += content
                            yield content
                            self.messages.append({"role": "assistant", "content": response})

