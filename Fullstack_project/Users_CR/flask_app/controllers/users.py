from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import User
#from {model_folder} import {model_file}

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    return render_template('create.html') 

@app.route('/users')
def users():
    return render_template("create.html",users=users.get_all())


@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')