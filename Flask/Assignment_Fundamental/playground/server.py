from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/play")
@app.route("/play/<string:color>/<int:num>")
def index(color = "red" ,num = 8):
    return render_template("index.html", color = color,num = num)



if __name__ == "__main__":
    app.run(debug = True)
