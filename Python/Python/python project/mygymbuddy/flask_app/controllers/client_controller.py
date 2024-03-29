from flask_app import app
from flask import redirect, render_template, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.sports import Sport
from flask_app.models.users import User
from flask_app.models.messages import Message
from flask_app.models.coachs import Coach
from flask_app.models.clients import Client
from flask_app.models.sessions import Session

bcrypt = Bcrypt(app)


@app.route("/register/client", methods=["POST"])
def process_register():

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
    session["user_id"] = user_id
    return redirect(f'/user/add/{user_id}')

@app.route("/user/add/<int:id>")
def clientsinfos(id):
    all_sports=Sport.get_all_sport()
    return render_template("newclient.html",id=id,all_sports=all_sports)

@app.route('/client/new', methods=['POST'])
def add_new_client():
    print(request.form)
    Client.newclient(request.form)
    return redirect('/userdashboard')

@app.route("/dashboard")
def dash():
    #! ROUTE GUARD
    if "user_id" not in session:
        return redirect("/")
    # grab the user id from session and put in a dictionary
    data = {"id": session["user_id"]}
    # grab the user by id from DB
    current_user = Client.get_by_id(data)
    print("===> current_user:", current_user)
    return render_template("dashboard.html", username=current_user.first_name)




@app.route('/sport/client/<int:id>')
def sport_client(id):
    if not 'user_id' in session:
        return redirect('/')
    this_sport=Sport.get_sport_infos({"id":id})
    return render_template('sport.html',this_sport=this_sport)

@app.route("/request/<int:id>", methods=['post'])
def requests(id):
    client=Client.get_client_by__user_id({"id":session["user_id"]})
    Client.request({"session_id":id,"client_id":client.id})
    return redirect('/userdashboard')

@app.route(rule='/session/<int:id>')
def sessions(id):
    if not 'user_id' in session:
        return redirect('/')
    all_sessions=Session.coach_sessions({"id":id})
    return render_template('all_sessions.html',all_sessions=all_sessions)



@app.route("/sports")
def show_all_sports():
    if not 'user_id' in session:
        return redirect('/')
    sports = Sport.get_all_sport()
    user_id = session['user_id']
    return render_template("all_sports.html" , all_sports = sports,user_id=user_id)


