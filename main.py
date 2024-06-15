from flask import Flask, render_template
import os

app = Flask(
    __name__, 
    template_folder="./src/templates",
    static_folder="./src/static"
)

@app.route("/")
def index ():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=3000), debug=True)