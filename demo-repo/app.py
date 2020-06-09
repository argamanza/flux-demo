from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flux Demo! This is version 0.1.0"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
