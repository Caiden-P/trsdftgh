from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "We've got lift-off."

@app.route('/', subdomain='dashboard')
def dashboard():
    return "Welcome to the Dashboard!"
    
