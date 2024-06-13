from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index ():
    return "Hello Word"


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=3000), debug=True)