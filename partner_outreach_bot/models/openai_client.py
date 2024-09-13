import os
import openai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class OpenAIClient:
    def __init__(self):
        # Load the OpenAI API key from environment variables
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "gpt-3.5-turbo"
        self.max_tokens = 150
        self.temperature = 0.7
        self.top_p = 0.9

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set in environment variables")
        
        # Set the API key for OpenAI
        openai.api_key = self.api_key

    def generate_text(self, prompt):
        """
        Generates a response from OpenAI using the GPT-4 model.
        :param prompt: The text prompt for the model
        :return: Generated text response
        """
        try:
            # Call OpenAI's API for text generation using GPT-4
            response = openai.completions.create(
                model=self.model,
                prompt=prompt,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=self.top_p
            )
            
            # Extract the generated text from the API response
            generated_text = response['choices'][0]['text'].strip()
            return generated_text
        except Exception as e:
            print(f"Error generating text with OpenAI: {e}")
            return None
