from flask import render_template, redirect, request
3
from flask_app import app

#connects model information to controller
from flask_app.models.dojo import Dojo

#defualt route
@app.route('/')
def index():
    return redirect('/dojos')

#
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",all_dojos = dojos)

#This pulls information from data base  and displays it
@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))

#this saves the dojo that is created
@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')
