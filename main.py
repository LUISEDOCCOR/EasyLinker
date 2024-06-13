from flask import Flask
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def index ():
    return "Hello Word"

load_dotenv()
PORT = None
if(os.getenv("PORT")):
    PORT = os.getenv("PORT")
else:
    PORT = 3000

if __name__ == "__main__":
    app.run(port=PORT, debug=True)