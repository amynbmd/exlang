
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

class Profile():
  wordofTheDay = "test"
  numfriends = 0
  boolean isOnline = false
  country = "United States of America"
  nativeLang = "English"
  learningLang = "Mandarin"
  #placeholder to represent user's interests as array#
  interests = ["Sports", "Entertainment", "News", "Science"]
  name = "Testing Test"
  #placeholder URL
  picURL = "http:google.com/testing"
  bio = "This is a string representing a user's potential bio, we should set about a 250 char limit."
  #placeholder array representing a user's available times and dates for meeting
  availability = ["12:20pm 10/31/2022", "1:20pm 10/31/2022"]
  #This will store the user's friends as an array/dict#
  friends = []

  
#Add line to get "Firstname Lastname" from user
class User(db.Model):
    __tablename__ = 'user'
    username  = db.Column(db.String(50), primary_key = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))
    profile = Profile()


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

