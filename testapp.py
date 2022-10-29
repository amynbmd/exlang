
from flask import Flask, render_template, request, redirect, url_for
from flask import abort, jsonify
from flask_cors import CORS
import sqlite3 
import os
from flask_bcrypt import Bcrypt



#function to create web server

#Create an instance of Flask as 'app'
app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
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

    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    
    query_email = "SELECT email from user WHERE email = '"+email+"'  "
   

    cursor.execute(query_email)
    result = cursor.fetchall()
    if(result== []):
        abort(401)
    else:
        query_pw = "SELECT password from user WHERE email = '"+email+"' "
        cursor.execute(query_pw)
        result = cursor.fetchall()
        if(bcrypt.check_password_hash(result[0][0],request.form['password'])):
            return redirect(url_for('home_page'))
        else: 
            abort(401)
    
    return "<p>Success <p>"

#SIGN-UP
@app.route("/register", methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    pw_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    query1 = "INSERT INTO user VALUES ('{name}', '{email}', '{password}')".format(name = name, email = email, password = pw_hash)
    cursor.execute(query1)
    connection.commit()
        
    return "<p>Success <p>"


app.run()