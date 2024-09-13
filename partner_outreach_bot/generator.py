from data_sources import NotionClient, GoogleDocsClient
from bedrock import BedrockClient

class ChatStrategyGenerator:
    def __init__(self):
        # Initialize the clients for both Google Docs, Notion, and Bedrock
        self.google_docs_client = GoogleDocsClient()
        self.notion_client = NotionClient()
        self.bedrock_client = BedrockClient()

    async def generate_response_from_google_docs(self, user_question):
        """
        Generates a response using Google Docs content as context and sends it to Bedrock.
        """
        # Fetch the content from Google Docs (Google Doc ID fetched from environment variable)
        google_doc_content = self.google_docs_client.get_document_content()
        
        # Combine the user input with the context from the Google Docs page
        if google_doc_content:
            prompt = f"User Question: {user_question}\nContext from Google Docs:\n{google_doc_content}"
            print(prompt)
            response = await self.bedrock_client.invoke_bedrock_model(prompt)
            print(response)
            return response
        else:
            return "No content found in the Google Doc."

    async def generate_response_from_notion(self, user_question):
        """
        Generates a response using Notion content as context and sends it to Bedrock.
        """
        # Fetch the content from Notion
        notion_context = self.notion_client.get_notion_page_content()
        
        # Combine the user input with the context from the Notion pages
        if notion_context:
            prompt = f"User Question: {user_question}\nContext from Notion:\n{notion_context}"
            print(prompt)
            response = await self.bedrock_client.invoke_bedrock_model(prompt)
            return response
            print(response)
        else:
            return "No content found in the Notion pages."
