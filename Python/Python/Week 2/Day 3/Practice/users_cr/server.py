from flask import Flask ,render_template,request, redirect
app = Flask(__name__)   

from User_model import User

@app.route('/')
def all_users():
    users = User.all_users()
    return render_template('all_users.html', all_users=users)

# Display route for create
@app.route('/add')          
def hello_world():
    return render_template('index.html') 

# action route for create form 
@app.route('/new',methods=["post"])          
def new_user():
     data=request.form
     User.create(data)
     return redirect('/')








if __name__=="__main__":     
    app.run(debug=True)    

