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

@app.route('/one_user/<int:id>')          
def one_user(id):
     data={"id": id}
     user= User.one_user(data)
     return render_template('show.html', user=user)
@app.route('/delete/<int:id>')          
def DELETE(id):
     data={"id": id}
     user= User.DELETE(data)
     return redirect('/')
@app.route('/update',methods=['POST'])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/')
@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.one_user(data))











if __name__=="__main__":     
    app.run(debug=True)    

