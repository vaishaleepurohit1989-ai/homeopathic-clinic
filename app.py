from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yourclinicemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'  # use Gmail App Password
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    msg = Message("New Consultation",
                  sender="yourclinicemail@gmail.com",
                  recipients=["momclinic@gmail.com"])
    msg.body = f"Patient name: {name}"
    mail.send(msg)
    return "Thank you! Your details were sent."
if __name__ == '__main__':
    app.run(debug=True)

