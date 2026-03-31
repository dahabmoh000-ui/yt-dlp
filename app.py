from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>YT-DLP Web Service</h1><p>Send a GET request with a URL to download (Experimental).</p>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
