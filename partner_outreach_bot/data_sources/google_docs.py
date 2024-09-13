import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

class GoogleDocsClient:
    def __init__(self):
        self.creds = None
        self.credentials_path = 'partner_outreach_bot/data_sources/credentials.json'
        self.token_path = 'partner_outreach_bot/data_sources/token.json'
        self.SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
        
        # Get Google Doc IDs from environment variables (comma-separated)
        self.google_doc_ids = os.getenv("GOOGLE_DOC_IDS", "").split(",")

        # Load credentials from token.json if it exists, else authenticate using credentials.json
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.SCOPES)
                self.creds = flow.run_local_server(port=8000)
            # Save the credentials for future use
            with open(self.token_path, 'w') as token:
                token.write(self.creds.to_json())

        # Build the Google Docs API service
        self.service = build('docs', 'v1', credentials=self.creds)

    def get_documents_content(self):
        """
        Fetches and combines content from all Google Docs specified in the environment variable.
        """
        combined_content = ""
        for doc_id in self.google_doc_ids:
            doc_id = doc_id.strip()  # Clean up any extra whitespace
            if doc_id:
                content = self.get_document_content(doc_id)
                if content:
                    combined_content += f"\n--- Content from Document {doc_id} ---\n"
                    combined_content += content
        return combined_content if combined_content else "No content available from the provided documents."

    def get_document_content(self, doc_id):
        """
        Fetches the content of a single Google Doc using the given document ID.
        """
        try:
            # Fetch the document using the Google Doc ID
            document = self.service.documents().get(documentId=doc_id).execute()
            
            # Extract the content from the document's body
            doc_content = document.get('body').get('content')
            text_content = self.extract_text(doc_content)

            return text_content
        except Exception as e:
            print(f"Error retrieving document {doc_id}: {e}")
            return None

    def extract_text(self, doc_content):
        """
        Extracts the text from the document content.
        """
        text = []
        for element in doc_content:
            if 'paragraph' in element:
                for text_element in element.get('paragraph').get('elements'):
                    if 'textRun' in text_element:
                        text.append(text_element.get('textRun').get('content'))
        return ''.join(text)
