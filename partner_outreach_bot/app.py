from flask import Flask, render_template, request, jsonify
from generator import ChatStrategyGenerator
import asyncio

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-text', methods=['POST'])
async def generate():
    data = request.get_json()  # Get JSON data from the request
    user_question = data.get('user_question')
    source = data.get('source')  # Source can be 'notion' or 'google_docs'

    if not user_question:
        return jsonify({'response': 'No question provided'}), 400

    # Create an instance of the ChatStrategyGenerator class
    generator = ChatStrategyGenerator()

    # Depending on the source, call the appropriate generator function
    if source == 'google_docs':
        response = await generator.generate_response_from_google_docs(user_question)
    else:
        response = await generator.generate_response_from_notion(user_question)

    # Return the response as JSON
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
