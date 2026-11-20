from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to VRIKHSHAM!</h1>
    <h2>Nature, Powered by Intelligence.</h2>
    <p>Your AI-powered plant care journey starts here.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)