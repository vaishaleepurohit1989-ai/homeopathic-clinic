from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # For now, just print the data to the console
    print(f"New consultation request from {name} ({email}): {message}")

    return f"Thank you {name}, we’ll reach out to you soon!"

if __name__ == "__main__":
    app.run(debug=True)
