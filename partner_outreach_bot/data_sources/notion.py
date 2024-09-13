import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NotionClient:
    def __init__(self):
        self.token = os.getenv("NOTION_API_TOKEN")
        self.page_id = os.getenv("NOTION_PAGE_ID")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
    
    def fetch_page_content(self, page_id):
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()

            # Extract text and images from the response
            return self.extract_content(data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_id}: {e}")
            return None
    
    def extract_content(self, data):
        page_content = []
        for block in data['results']:
            block_type = block['type']

            # Process text-based blocks (paragraph, headings)
            if block_type in ['paragraph', 'heading_1', 'heading_2', 'heading_3']:
                text_content = self.extract_text(block)
                page_content.append(f"{block_type.capitalize()}: {text_content}")

            # Process image blocks
            elif block_type == 'image':
                image_url = block['image']['file']['url']
                page_content.append(f"Image: {image_url}")

            else:
                # Ignore unsupported block types for now
                page_content.append(f"Unsupported block type: {block_type}")

        return "\n".join(page_content)

    def extract_text(self, block):
        block_type = block['type']
        if 'text' in block.get(block_type, {}):
            return "".join([text['plain_text'] for text in block[block_type]['text']])
        return "No text available"
    
    def get_notion_page_content(self):
        return self.fetch_page_content(self.page_id)
