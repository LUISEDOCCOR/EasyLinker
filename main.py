from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index ():
    return "<h1>Hello Word</h1>"


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=3000), debug=True)