# Partner Outreach Strategy Bot

A bot designed to research marketplace partners and generate personalized outreach strategies using AWS Bedrock’s LLM and OpenAI models. It features a simple web interface (using Flask) to input partner details and create customized outreach strategies.

## Features
- Generate personalized outreach strategies based on gathered partner's information.
- Optionally use a simple web interface (Flask) to input partner details and view the generated strategies.
- Integrates with external content sources like Notion, Confluence and Google Docs to provide relevant context for strategy generation.

## Repository Structure
```bash
Partner-Outreach-Bot/
│
├── LICENSE                    # License file for your project
├── README.md                  # Project documentation
├── partner_outreach_bot/       # Directory for project files
│   ├── __init__.py            # Makes it a package
│   ├── app.py                 # Main Flask app
│   ├── generator.py           # Business logic (strategy generation using content from Notion, Google Docs, Bedrock, and OpenAI)
│   ├── templates/             # HTML templates for the web interface
│   │   └── index.html         # Input form for entering partner details and asking questions
│   ├── data_sources/          # Contains integrations for external content sources
│   │   ├── __init__.py        # Initializes the data sources module
│   │   ├── notion.py          # Integration for fetching content from Notion pages
│   │   ├── google_docs.py     # Integration for fetching content from Google Docs
│   │   └── confluence.py      # Integration for fetching content from Confluence pages  # NEW FILE
│   ├── models/                # Contains AI models for generating responses
│   │   ├── __init__.py        # Initializes the models module
│   │   ├── bedrock_client.py  # Contains logic to interact with AWS Bedrock
│   │   └── openai_client.py   # Contains logic to interact with OpenAI GPT models
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
OPENAI_API_KEY=
NOTION_API_TOKEN=
NOTION_PAGE_IDS=
GOOGLE_DOC_IDS=
CONFLUENCE_API_TOKEN=
CONFLUENCE_PAGE_IDS=
CONFLUENCE_USERNAME=
CONFLUENCE_BASE_URL=
```

5. Running the Bot
Run the script directly
```bash
python partner_outreach_bot/app.py
```

Open your browser and go to http://127.0.0.1:3000 to use the web interface.

## How it Works
The bot integrates content from external sources like Notion pages, Confluence and Google Docs, which it combines with user inputs to generate personalized outreach strategies. The strategies are generated using the AWS Bedrock and OpenAI models, which processes the input and context to generate relevant and customized strategies.

## Technologies Used
- Python: Core scripting language.
- Flask: Lightweight web framework for the user interface.
- AWS Bedrock: Large language models for generating outreach strategies.
- OpenAI: Large language models for generating outreach strategies.
- Notion API: To fetch context from Notion pages.
- COnfluence API: To fetch context from Confluence Docs.
- Google Docs API: To fetch context from Google Docs.

## License
This project is licensed under the Apache License. See the LICENSE file for details.