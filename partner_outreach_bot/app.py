from flask import Flask, render_template, request
from logic import OutreachGenerator

# Create Flask app
app = Flask(__name__)

# Home route for the form
@app.route('/')
def home():
    return render_template('index.html')

# Route for generating email
@app.route('/generate', methods=['POST'])
def generate():
    company_name = request.form['company_name']
    focus_area = request.form['focus_area']
    use_cases = request.form['use_cases'].split(",")
    
    # Create an instance of the OutreachGenerator class
    generator = OutreachGenerator(company_name, focus_area, use_cases)
    
    # Call the email_generator method to get the email
    email = generator.email_generator()
    
    # Render the same page with the generated email
    return render_template('index.html', email=email)

if __name__ == "__main__":
    app.run(debug=True)
