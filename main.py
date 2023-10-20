from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/.well-known/discord')
def index():
    return 'dh=b24e55f63476d9c315b548017767722178647a36'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
