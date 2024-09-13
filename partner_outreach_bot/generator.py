from data_sources import NotionClient, GoogleDocsClient
from models import BedrockClient, OpenAIClient

class ChatStrategyGenerator:
    def __init__(self):
        # Initialize the clients for both Google Docs, Notion, Bedrock, and OpenAI
        self.google_docs_client = GoogleDocsClient()
        self.notion_client = NotionClient()
        self.bedrock_client = BedrockClient()
        self.openai_client = OpenAIClient()

    def generate_response_from_google_docs(self, user_question, model="bedrock"):
        """
        Generates a response using Google Docs content as context and sends it to either Bedrock or OpenAI.
        """
        # Fetch the content from Google Docs (Google Doc ID fetched from environment variable)
        google_doc_content = self.google_docs_client.get_documents_content()

        if google_doc_content:
            prompt = f"""
You are an expert in the relevant domain. Use the following context to provide a precise, detailed answer to the user's question.

User's Question: {user_question}
Context from Google Docs: {google_doc_content}

Your response should follow these guidelines:

1. Summary: Start with a concise summary that directly addresses the user's question.
2. Detailed Explanation: Break down the explanation into key points or steps, structured logically.
3. Contextual References: Reference specific information from the context provided where applicable.
4. Actionable Recommendations: End with actionable recommendations or next steps for the user to take.
"""
            # Use Bedrock or OpenAI based on the model selected
            if model == "bedrock":
                response = self.bedrock_client.invoke_bedrock_model(prompt)
            else:
                response = self.openai_client.generate_text(prompt)
            
            return response
        else:
            return "No content found in the Google Doc."

    def generate_response_from_notion(self, user_question, model="bedrock"):
        """
        Generates a response using Notion content as context and sends it to either Bedrock or OpenAI.
        """
        # Fetch the content from Notion
        notion_context = self.notion_client.get_notion_page_content()

        if notion_context:
            prompt = f"""
You are an expert in the relevant domain. Use the following context to provide a precise, detailed answer to the user's question.

User's Question: {user_question}
Context from Notion: {notion_context}

Your response should follow these guidelines:

1. Summary: Start with a concise summary that directly addresses the user's question.
2. Detailed Explanation: Break down the explanation into key points or steps, structured logically.
3. Contextual References: Reference specific information from the context provided where applicable.
4. Actionable Recommendations: End with actionable recommendations or next steps for the user to take.
"""
            # Use Bedrock or OpenAI based on the model selected
            if model == "bedrock":
                response = self.bedrock_client.invoke_bedrock_model(prompt)
            else:
                response = self.openai_client.generate_text(prompt)
            
            return response
        else:
            return "No content found in the Notion pages."

