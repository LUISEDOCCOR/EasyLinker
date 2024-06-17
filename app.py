from flask import Flask
app = Flask(
    __name__, 
    template_folder="./src/templates",
    static_folder="./src/static"
)