import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Load API key securely from environment variable
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']

    # Send email via Resend API
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "from": "Clinic <onboarding@resend.dev>",   # temporary sender identity
        "to": ["vaishaleepurohit1989@gmail.com"],   # recipient inbox
        "subject": "New Consultation",
        "text": f"Patient name: {name}"
    }

    response = requests.post(url, headers=headers, json=data)

    # Log full response to Render logs
    print("Resend response:", response.status_code, response.text)

    if response.status_code == 200:
        return render_template('thankyou.html')
    else:
        return f"Error sending email: {response.text}"

if __name__ == '__main__':
    app.run(debug=True)
