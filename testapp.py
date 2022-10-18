
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user


#function to create web server

#Create an instance of Flask as 'app'
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'exlang'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{username}:{password}@{server}/exlang".format(
username="root", password= "nhutran2002", server="localhost")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    name  = db.Column(db.String(50), primary_key = True)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))

    def __repr__(self):
        return "name: {0) | email: {1} | password: {2}".format(self.name, self.email, self.password)

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
        email = request.form.get('email')
        password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    user1 = bool(User.query.filter_by(password=password).first())
    if user:
        if  user1:
            flash('Logged in successfully!', category='success')
            return "<p> Success <p>"
        else: 
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Incorrect email, try again.', category='error')

    return "<p>Success <p>"

#SIGN-UP
@app.route("/register", methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        
        new_user = User(email=email, password=password, name = name)

        db.session.add(new_user)
        db.session.commit
        
        # login_user(new_user, remember=True)
        # flash('Account created!', category='success')
        
        return "<p>Success <p>"

app.run()