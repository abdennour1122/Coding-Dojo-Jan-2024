from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def submit():
    return render_template('index.html')   
@app.route('/', methods=['POST'])
def create_ninja():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def show_ninjas():
    return render_template('result.html', name=session['name'], location=session['location'], favorite_language=session['favorite_language'], comment = session['comment'])


     








if __name__=="__main__":   
    app.run(debug=True)    

