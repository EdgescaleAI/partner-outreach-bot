import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NotionClient:
    def __init__(self):
        """
        Initializes the Notion client by loading the token and page IDs from environment variables.
        
        The environment variables should include:
        - NOTION_API_TOKEN: Notion API token
        - NOTION_PAGE_IDS: Comma-separated Notion page IDs
        """
        self.token = os.getenv("NOTION_API_TOKEN")
        self.page_ids = os.getenv("NOTION_PAGE_IDS").split(",")  # Get comma-separated page IDs
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
    
    def fetch_page_content(self, page_id):
        """
        Fetches the content of a Notion page by its page ID.
        
        :param page_id: The ID of the Notion page.
        :return: A string containing the text and image content from the page.
        """
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return self.extract_content(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_id}: {e}")
            return None
    
    def extract_content(self, data):
        """
        Extracts text and images from the Notion page's data.
        
        :param data: The JSON response from the Notion API.
        :return: A formatted string containing the text and image content.
        """
        page_content = []
        for block in data.get('results', []):
            block_type = block.get('type')

            # Process text-based blocks (paragraph, headings)
            if block_type in ['paragraph', 'heading_1', 'heading_2', 'heading_3']:
                text_content = self.extract_text(block)
                page_content.append(f"{block_type.capitalize()}: {text_content}")

            # Process image blocks
            elif block_type == 'image':
                image_url = block['image']['file']['url']
                page_content.append(f"Image: {image_url}")

            else:
                # Handle unsupported block types
                page_content.append(f"Unsupported block type: {block_type}")

        return "\n".join(page_content)

    def extract_text(self, block):
        """
        Extracts plain text from a Notion block.
        
        :param block: A block from the Notion API response.
        :return: A string containing the plain text of the block.
        """
        block_type = block['type']
        if 'text' in block.get(block_type, {}):
            return "".join([text['plain_text'] for text in block[block_type]['text']])
        return "No text available"
    
    def get_multiple_pages_content(self):
        """
        Fetches and concatenates content from multiple Notion pages.
        
        :return: A single concatenated string containing the content of all specified pages.
        """
        combined_content = ""
        for page_id in self.page_ids:
            page_id = page_id.strip()  # Remove any extra whitespace
            content = self.fetch_page_content(page_id)
            if content:
                combined_content += f"\nContent for Page ID {page_id}:\n{content}\n"
            else:
                combined_content += f"\nError fetching content for Page ID {page_id}.\n"
        
        return combined_content
