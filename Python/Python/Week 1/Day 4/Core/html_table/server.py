from flask import Flask ,render_template
app = Flask(__name__)   


    

@app.route('/')
def render_lists():
    users = [
       {'first_name' : 'Michael', 'last_name' : 'choi'},
       {'first_name' : 'jhon', 'last_name' : 'supspin'},
       {'first_name' : 'mark', 'last_name' : 'guillen'},
       {'first_name' : 'kb', 'last_name' : 'tonel'}
    ]
    return render_template("index.html", users = users)

   
  




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
