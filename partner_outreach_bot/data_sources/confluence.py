import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup  # To process HTML content

class ConfluenceClient:
    def __init__(self):
        """
        Initializes the Confluence client.
        
        The environment variables should include:
        - CONFLUENCE_BASE_URL
        - CONFLUENCE_USERNAME
        - CONFLUENCE_API_TOKEN
        - CONFLUENCE_PAGE_IDS (comma-separated)
        """
        load_dotenv()  # Load environment variables from .env file
        self.base_url = os.getenv("CONFLUENCE_BASE_URL")
        self.username = os.getenv("CONFLUENCE_USERNAME")
        self.api_token = os.getenv("CONFLUENCE_API_TOKEN")
        self.page_ids = os.getenv("CONFLUENCE_PAGE_IDS").split(',')  # Get comma-separated page IDs
        self.auth = HTTPBasicAuth(self.username, self.api_token)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_page_content(self, page_id):
        """
        Fetches and processes the content of a Confluence page by its page ID.
        
        :param page_id: The ID of the Confluence page.
        :return: The content of the page in plain text format.
        """
        url = f"{self.base_url}/rest/api/content/{page_id}?expand=body.storage"
        response = requests.get(url, headers=self.headers, auth=self.auth)

        if response.status_code == 200:
            page_data = response.json()
            html_content = page_data['body']['storage']['value']
            
            # Convert HTML to plain text using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            plain_text_content = soup.get_text(separator="\n")  # Get plain text with line breaks

            return plain_text_content
        else:
            raise Exception(f"Failed to fetch page content for page {page_id}. Status Code: {response.status_code}, Error: {response.text}")

    def get_combined_pages_content(self):
        """
        Fetches and processes the content of multiple Confluence pages and combines them into one text block.
        
        :return: A single concatenated string containing the content of all specified pages.
        """
        combined_content = ""
        for page_id in self.page_ids:
            try:
                content = self.get_page_content(page_id.strip())  # Strip whitespace from page IDs
                combined_content += f"\nContent for Page ID {page_id.strip()}:\n{content}\n"  # Append page content
            except Exception as e:
                print(f"Error fetching content for page {page_id.strip()}: {str(e)}")
        return combined_content
