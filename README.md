# Partner Outreach Bot

A GPT-powered bot designed to research marketplace partners and generate personalized outreach emails using OpenAI's API. It features a simple web interface (using Flask) to input partner details and create customized outreach emails.

## Features
- Generate personalized outreach emails based on a partner's company name, focus area, and use cases.
- Optionally use a simple web interface (Flask) to input partner details and view the generated emails.

## Repository Structure
```bash
Partner-Outreach-Bot/
│
├── LICENSE                    # License file for your project
├── README.md                  # Project documentation
├── partner_outreach_bot/       # Directory for project files
│   ├── __init__.py            # Makes it a package
│   ├── app.py                 # Main Flask app
│   ├── openai_api.py          # Contains the logic to interact with OpenAI API
│   ├── logic.py               # Business logic (email generation, input formatting)
│   └── templates/             # HTML templates for the web interface
│       └── index.html         # Input form for entering partner details
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

4. Set up environment variables:
Create a .env file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-openai-api-key
```

5. Running the Bot
Option 1: Run the script directly
```bash
python partner_outreach_bot.py
```

Option 2: Run the web app (Flask)
```bash
flask run
```
Open your browser and go to http://127.0.0.1:5000 to use the web interface.

## How it Works
The script takes the partner company’s name, focus area, and use cases as inputs and uses the OpenAI GPT model to generate a customized outreach strategy.

## Usage
Navigate to http://127.0.0.1:5000
Enter the company name, focus area, and use cases in the form, then click "Generate Email."
View the generated outreach email on the same page.

## Technologies Used
- Python: Core scripting language.
- Flask: Lightweight web framework for the user interface.
- OpenAI API: GPT-3.5 model for generating outreach emails.

## License
This project is licensed under the MIT License. See the LICENSE file for details.