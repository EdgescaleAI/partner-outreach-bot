from openai_api import OpenAIClient

class OutreachGenerator:
    def __init__(self, company_name, focus_area, use_cases):
        self.company_name = company_name
        self.focus_area = focus_area
        self.use_cases = use_cases
        self.openai_client = OpenAIClient()  # Instantiate OpenAIClient

    def create_prompt(self):
        """Creates the prompt based on the provided company details."""
        return f"Write a personalized outreach email for {self.company_name}, introducing our infrastructure for {self.focus_area}. Highlight use cases such as {', '.join(self.use_cases)}."
    
    def email_generator(self):
        """Generates the email using OpenAI's API."""
        prompt = self.create_prompt()
        return self.openai_client.get_completion(prompt)
