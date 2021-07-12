from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # return "Hello World!"
    return render_template("index.html", name = "Dustine", age = 28)

@app.route("/hello/<name>/<int:age>")
def hello(name, age):
    # return f"Hello there {name}!"
    return render_template("index.html", name = name, age = age)



@app.route("/user/<username>/<int:id>")
def show_profile(username, id):
    print(type(username))
    print(type(id))

    return f"Username: {username}, ID: {id}."


@app.route("/champions")
def champions():
    champions = ["Ash", "Zack", "Lux","Sona"]

    return render_template("list.html", champions = champions)

if __name__ == "__main__":
    app.run(debug = True)

