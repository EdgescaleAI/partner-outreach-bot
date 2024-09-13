# Partner Outreach Strategy Bot

A bot designed to research marketplace partners and generate personalized outreach strategies using AWS Bedrock’s LLM. It features a simple web interface (using Flask) to input partner details and create customized outreach strategies.

## Features
- Generate personalized outreach strategies based on a partner's company name, focus area, and use cases.
- Optionally use a simple web interface (Flask) to input partner details and view the generated strategies.
- Integrates with external content sources like Notion and Google Docs to provide relevant context for strategy generation.

## Repository Structure
```bash
Partner-Outreach-Bot/
│
├── LICENSE                    # License file for your project
├── README.md                  # Project documentation
├── partner_outreach_bot/       # Directory for project files
│   ├── __init__.py            # Makes it a package
│   ├── app.py                 # Main Flask app
│   ├── bedrock.py             # Contains the logic to interact with AWS Bedrock
│   ├── generator.py           # Business logic (strategy generation using content from Notion, Google Docs, and Bedrock API)
│   ├── templates/             # HTML templates for the web interface
│   │   └── index.html         # Input form for entering partner details and asking questions
│   ├── data_sources/          # Contains integrations for external content sources
│   │   ├── __init__.py        # Initializes the data sources module
│   │   ├── notion.py          # Integration for fetching content from Notion pages
│   │   └── google_docs.py     # Integration for fetching content from Google Docs
├── requirements.txt           # Python dependencies
└── venv/                      # Virtual environment directory
```

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/your-username/partner-outreach-bot.git
cd partner-outreach-bot
```

2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables: Create a .env file in the root directory and add your AWS credentials and the necessary environment variables:
```bash
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-west-2
BEDROCK_ENDPOINT=https://bedrock.us-west-2.amazonaws.com
NOTION_API_TOKEN=your_notion_token
GOOGLE_DOC_ID=your_google_doc_id
```

5. Running the Bot
Run the script directly
```bash
python partner_outreach_bot/app.py
```

Open your browser and go to http://127.0.0.1:3000 to use the web interface.

## How it Works
The bot integrates content from external sources like Notion pages and Google Docs, which it combines with user inputs to generate personalized outreach strategies. The strategies are generated using the AWS Bedrock model, which processes the input and context to generate relevant and customized strategies.

## Technologies Used
- Python: Core scripting language.
- Flask: Lightweight web framework for the user interface.
- AWS Bedrock: Large language models for generating outreach strategies.
- Notion API: To fetch context from Notion pages.
- Google Docs API: To fetch context from Google Docs.

## License
This project is licensed under the MIT License. See the LICENSE file for details.