from flask_app import app
from flask import render_template,session,redirect,request,flash
from flask_bcrypt import Bcrypt
from flask_app.models.sports import Sport
from flask_app.models.users import User
from flask_app.models.messages import Message
from flask_app.models.coachs import Coach
from flask_app.models.clients import Client
from flask_app.controllers import user_controller
from flask_app.controllers import coach_controller
from flask_app.controllers import client_controller


bcrypt = Bcrypt(app)


@app.route("/sign_up/coach")
def sign_up_coach():
    return render_template("coach_register.html")

@app.route("/register/coach", methods=["POST"])
def register_coach():

    # validate the form here ...
    if not User.validate_user(request.form):
        return redirect("/sign_up")
    # create the hash
    print("-------->", request.form["password"])
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print("=======>", pw_hash)
    # User.create(request.form)
    data = {**request.form, "password": pw_hash}
    # store the user id inside the session
    user_id = User.newuser(data)
    return redirect(f'/coach/add/{user_id}')


@app.route('/coach/add/<int:id>')
def add_coach(id):
    if not 'user_id' in session:
        return redirect('/')
    all_sports=Sport.get_all_sport()
    return render_template("newcoach.html",user_id=id,all_sports=all_sports)

@app.route('/coach/new/<int:id>', methods=['POST'])
def create_coach(id):
    if Coach.validate_coach(request.form):

        Coach.newcoach(request.form)
        return redirect('/showinfos')
    return redirect(f'/coach/add/{id}')





@app.route('/showinfos')
def showallinfos1():
    if not 'user_id' in session:
        return redirect('/')
    all_users=User.show_all_users()
    all_coachs=Coach.get_all_coachs()
    all_clients=Client.get_all_clients()
    all_sports=Sport.get_all_sport()
    name = session['first_name']
    return render_template('allinfos.html',name=name,all_users=all_users,all_coachs=all_coachs,all_clients=all_clients,all_sports=all_sports)




@app.route('/client/<int:id>')
def one_client(id):
    if not 'user_id' in session:
        return redirect('/')
    this_client=Client.get_by_id({"id":id})
    return render_template('one_client.html',this_client=this_client)



@app.route('/sport/<int:id>')
def one_sport(id):
    if not 'user_id' in session:
        return redirect('/')
    this_sport=Sport.get_sport_infos({"id":id})
    return render_template('one_sport.html',this_sport=this_sport)




@app.route('/coach/delete/<int:id>')
def delete_coach(id):
    if not 'user_id' in session:
        return redirect('/')
    Coach.delete_coach({'id':id})
    return redirect("/showinfos")

@app.route('/user/delete/<int:id>')
def delete_user(id):
    if not 'user_id' in session:
        return redirect('/')
    User.delete_user({'id':id})
    return redirect("/showinfos")




@app.route('/client/delete/<int:id>')
def delete_client(id):
    if not 'user_id' in session:
        return redirect('/')
    Client.delete_client({'id':id})
    return redirect("/showinfos")



@app.route('/sport/delete/<int:id>')
def delete_sport(id):
    if not 'user_id' in session:
        return redirect('/')
    Sport.delete_sport({'id':id})
    return redirect("/showinfos")

# @app.route('/message/delete/<int:id>')
# def delete_message(id):
#     if not 'user_id' in session:
#         return redirect('/')
#     Admin.delete_message({'id':id})
#     return redirect("/showinfos")




@app.route('/sport/add')
def add_sport():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("newsport.html")


@app.route('/sports/new', methods=['POST'])
def create_sport():
    if not Sport.validate(request.form):
        return redirect('/sport/add')
    Sport.newsport(request.form )
    return redirect('/showinfos')











