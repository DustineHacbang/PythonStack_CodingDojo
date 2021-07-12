from flask import Flask
from flask.scaffold import F

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<name>")
def say_hi(name):
    return F"Hi {name}!"

@app.route("/repeat/<int:number>/hello")
def hello(number):
    return f"({number} * Hello)"



if __name__ == "__main__":
    app.run(debug = True )