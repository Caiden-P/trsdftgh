# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Set the server name for subdomain handling
app.config['SERVER_NAME'] = 'transcendshare.com'  # Change this to your actual domain

@app.route('/', defaults={'subdomain': None})
@app.route('/', subdomain='www')  # For the main site (www.domain.com)
def home(subdomain):
    return "Welcome to the main site!"

@app.route('/', subdomain='dashboard')  # Access dashboard via dashboard.domain.com
def dashboard():
    return "Welcome to the Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
