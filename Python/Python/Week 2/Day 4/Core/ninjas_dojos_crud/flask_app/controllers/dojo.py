from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo import dojo


@app.route('/')
def all_dojos():
    all_dojos=dojo.get_all()
    return render_template('dojos.html',all_dojos=all_dojos)

@app.route('/add_dojo',methods=['post'])
def create():
    data=request.form
    dojo.create_dojo(data)
    return redirect('/')

