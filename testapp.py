
from flask import Flask, render_template, request, flash
from flask_cors import CORS
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import sqlite3 
import os


#function to create web server

#Create an instance of Flask as 'app'
# db = SQLAlchemy()
app = Flask(__name__)
bcrpyt = Bcrypt(app)
CORS(app)
#We should store our private key in a more secure way, like encryption or somewhere on github.
app.config['SECRET_KEY'] = 'exlang'
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{server}/exlang".format(
# username="root", password= "nhutran2002", server="localhost")
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:nhutran2002@locahost/exlang"
# app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
# db = SQLAlchemy(app)   
# db.init_app(app)
currentdirectory  = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def landing_page():
    return "<p>Testing Page for ExLang!</p>"

@app.route("/home")
def home_page():
    return "<p>Welcome to our home page!<p>"

#LOGIN
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        candidate = password
        #Make a call to the database with the candidate email and password that returns correct password, compare with password entered by user for authorization to login
        #Something like: realPassword = database.PassWordQuery(email) <-- I think we're using query1 for this
        #and then (bcrypt.check_password_hash(realPassword, candiate), if true, authorize login
        if (bcrypt.check_password_hash(pwhash, candidate):
          #login to page

    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    
    query1 = "SELECT email from user WHERE email = '"+email+"' and password = '"+password+"' "
    cursor.execute(query1)
    result = cursor.fetchall()
    if(result== []):
        print("Incorrect email or password")
    else: 
        print(result)

    # if user:
    #     if  user1:
    #         flash('Logged in successfully!', category='success')
    #         print("True1")
    #         return "<p> Success <p>"
    #     else: 
    #         flash('Incorrect password, try again.', category='error')
    # else:
    #     print("True2")
    #     flash('Incorrect email, try again.', category='error')
    return "<p>Success <p>"

#SIGN-UP
@app.route("/register", methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            pwhash = bcrypt.generate_password_hash(password).decode('utf-8')
            #We should change this to store the password HASH on the database, not the password in plaintext
    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO user VALUES ('{name}', '{email}', '{password}')".format(name = name, email = email, password = pwhash)
    cursor.execute(query1)
    connection.commit()
        
    return "<p>Success <p>"

# with app.app_context():
#     db.create_all()

app.run()
