from flask import Flask ,render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play/<int:num>/<color>')
def play(num,color):
    return render_template("index.html",times=num , color = color )











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001)    # Run the app in debug mode.
