from flask_app.models.dojo_survey import User
from flask_app import app
from flask import render_template,redirect,request,session

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_burger():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not User.validate_user(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    User.save(request.form)
    return redirect("/users")

@app.route('/users')
def success():
    return render_template('dojo_survey.html')