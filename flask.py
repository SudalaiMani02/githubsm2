from flask import Flask

app = Flask(__name__)

# Route 1 - Home
@app.route("/")
def home():
    return "Welcome to my Flask App!"

# Route 2 - About
@app.route("/about")
def about():
    return "This is the About page."

# Route 3 - Contact
@app.route("/contact")
def contact():
    return "Contact us at contact@example.com"

# Route 4 - Services
@app.route("/services")
def services():
    return "We provide web development services."

# Route 5 - Help
@app.route("/help")
def help_page():
    return "How can I assist you?"

if __name__ == "__main__":
    app.run(debug=True)
