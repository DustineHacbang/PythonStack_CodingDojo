from flask import Flask, render_template, session
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "counting"

@app.route("/")
def index():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    print(session["counter"])
    return render_template("counter.html")

@app.route("/counter")
def counter():
    session["counter"] += 1
    return redirect("/")

if __name__ =="__main__":
    app.run(debug = True)

