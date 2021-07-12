from flask import Flask
from flask.templating import render_template
app= Flask(__name__)

print(__name__)

@app.route("/")
@app.route("/<string:color1>/<string:color2>/<int:numX>/<int:numY>")
def index(color1="red",color2="black",numX = 8,numY = 8):
    return render_template("index.html", color1 = color1, color2 = color2, numX = numX, numY = numY)

if __name__=="__main__":
    app.run(debug=True)