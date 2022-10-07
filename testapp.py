from flask import Flask

#function to create web server

#Create an instance of Flask as 'app' 
app = Flask(__name__)

@app.route("/")
def landing_page():
    return "<p>Testing Page for ExLang!</p>"

@app.route("/home")
def home_page():
    return "<p>Welcome to our home page!<p>"

@app.route(/"register")
def signup_page():
    return "<p>Sign Up Here!!!<p>"
