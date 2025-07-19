from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define the route
@app.route('/home')
def home():
    return "Hello, World! This is a basic Flask app."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
