
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#function to create web server

#Create an instance of Flask as 'app'
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{server}/exlang".format(
username="root", password= "", server="localhost")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    username  = db.Column(db.String(50), primary_key = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))


@app.route("/")
def landing_page():
    return "<p>Testing Page for ExLang!</p>"

@app.route("/home")
def home_page():
    return "<p>Welcome to our home page!<p>"

# @app.route("/login")
# def login():
#     return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        
    return "<p>Sign Up Here!!!<p>"

