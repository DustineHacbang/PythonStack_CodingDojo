
from flask_app import app
from flask import render_template,redirect,request,session,flash
#from {model_folder} import {model_file}

@app.route('/')# The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html') 
