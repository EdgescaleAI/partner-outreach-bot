import openai
import os
from dotenv import load_dotenv

class OpenAIClient:
    def __init__(self):
        """Initializes the OpenAI API client by loading the API key from environment variables."""
        load_dotenv()  # Load environment variables from .env file
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def get_completion(self, prompt):
        """Makes an API call to OpenAI to get a completion based on the provided prompt."""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text
