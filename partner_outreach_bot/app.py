from flask import Flask, render_template, request, jsonify
from generator import ChatStrategyGenerator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-text', methods=['POST'])
def generate():
    data = request.get_json()
    user_question = data.get('user_question')
    source = data.get('source')  # Source can be 'notion', 'google_docs', or 'confluence'
    model = data.get('model')  # Model can be 'bedrock' or 'openai'

    if not user_question:
        return jsonify({'response': 'No question provided'}), 400

    # Create an instance of the ChatStrategyGenerator class
    generator = ChatStrategyGenerator()

    # Call the appropriate method based on the source
    if source == 'google_docs':
        response = generator.generate_response_from_google_docs(user_question, model)
    elif source == 'notion':
        response = generator.generate_response_from_notion(user_question, model)
    elif source == 'confluence':
        response = generator.generate_response_from_confluence(user_question, model)
    else:
        return jsonify({'response': 'Invalid source provided'}), 400

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
