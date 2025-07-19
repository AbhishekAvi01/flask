from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Page - This is the main home page"

@app.route('/header')
def header():
    return "This is the HEADER with logo and nav bar"

@app.route('/body')
def body():
    return "This is the BODY section with main content of the website"

@app.route('/footer')
def footer():
    return "Footer - All rights reserved"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
