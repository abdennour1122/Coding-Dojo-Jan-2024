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

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/loginform")
def loginform():
    return render_template("login.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/userdashboard")
def user_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    user=User.get_by_id({'id':user_id})
    # all_clients = Coach.show_all_clients_of_coach({"id":user_id})
    all_sessions = Session.show_all_Sessions()
    all_sports=Sport.get_all_sport()
    
    return render_template("home_user.html", user_id=user_id, user=user, all_sessions=all_sessions,all_sports=all_sports)

@app.route('/users/add')
def add_user():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("newuser.html")


@app.route('/login', methods=['post'])
def login():
    user_from_db=User.get_by_email({'email':request.form['email']})
    if not user_from_db:
        flash("Password or email is wrong please try again","login")
        return redirect('/loginform')
    if user_from_db.role==1:
        session['user_id']=user_from_db.id
        session["first_name"]=user_from_db.first_name
        return redirect("/showinfos")
    if user_from_db.role==2:
        session['user_id']=user_from_db.id
        session["first_name"]=user_from_db.first_name
        return redirect("/coachdashboard")
    session['user_id']=user_from_db.id
    session["first_name"]=user_from_db.first_name
    return redirect("/userdashboard")

@app.route('/user/new', methods=['POST'])
def register():
    if User.validate_user(request.form):
        pw_hash=bcrypt.generate_password_hash(request.form['password'])
        data={**request.form,'password':pw_hash}
        user_id=User.newuser(data)
        session['user_id']=user_id
        session["first_name"]=data['first_name']
        return redirect(f'/user/add/{user_id}')
    return redirect('/users/add')


@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect("/")

