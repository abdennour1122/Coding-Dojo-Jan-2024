from Flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')         
def dojo():
    return 'dojo!' 

@app.route('/say/<flaskname>')      
def flask(flaskname):
    return f'hi {flaskname}!'  



@app.route('/repeat/<int:num>/<flaskname>')      
def repeat(num,flaskname):
    return f' {flaskname*num}'





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

