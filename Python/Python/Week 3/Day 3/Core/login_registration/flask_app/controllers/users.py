from flask_app import app
from flask import render_template,request,redirect,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt



bcrypt=Bcrypt(app)



@app.route('/')
def login():
    print("hlqisbd")
    # print(request.form)
    return render_template('home.html')



@app.route("/register",methods=['POST'])
def process_register():
    
    if not User.validate_user(request.form):

        return redirect("/")
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data={
        **request.form,
        "password":pw_hash
    }
    user_id=User.create(data)
    session["user_id"]=user_id
    return redirect("/dashboard")

 
#action route login
@app.route('/login',methods=["POST"])
def process_login():
    
    
    

    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    user_id=User.create(data)
    session["user_id"]=user_id

    return redirect('/dashboard')
    

@app.route('/dashboard')
def dash():
    if "user_id" not in session:
        return redirect("/")
    current_user=User.get_by_id
    data={"id":session['user_id']}
    return render_template("dashboard.html",username=current_user.first_name)