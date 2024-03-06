from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.ninja import ninja
from flask_app.models.dojo import dojo



@app.route('/new_ninja')
def all_ninjas():
    all_dojos=dojo.get_all()
    all_ninjas=ninja.get_all()
    return render_template(template_name_or_list='new_ninja.html',all_ninjas=all_ninjas,all_dojos=all_dojos)

@app.route('/add_ninja',methods=['post'])
def create_ninja():
    data=request.form
    ninja.create_ninja(data)
    return redirect('/')

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    onedojo=dojo.get_dojo_byid({'id':dojo_id})
    data={'dojo_id':dojo_id}
    all_ninjas=ninja.get_ninja_byid(data)
    return render_template('dojos_show.html' ,all_ninjas=all_ninjas,onedojo=onedojo)




