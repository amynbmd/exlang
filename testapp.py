
import os
import sqlite3

import jsonpickle
from flask import (Flask, Response, flash, jsonify, make_response,
                   render_template, request)
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)


class Profile():
    email = None
    wordofTheDay = None
    isOnline = False
    countryCode = None
    picURL = None
    bio = None
    nativeLang = None
    level = None
    learningLang = []
    interests = []
    availability = []
    friends = []
    zoomLocation = None

class User:
    name = None
    email = None
    password = None
    profile = Profile()


#------------------------------------------TO-DO------------------------------------------#
# Please create a new user profile table in database, retrieve profile for this particular user and then map it to an object. Hardcode values below is for testing purposes only.
def getUserProfile(email):
    profile = Profile()
    
    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    query1 = "SELECT email from USER_PROFILE WHERE email = '"+email+"'"
    cursor.execute(query1)
    result1 = cursor.fetchall()
    
    if (len(result1)!=0):
        
        # profile.wordofTheDay = "obfuscate"
        # profile.isOnline = True
        query = "SELECT countryCode,native_Lang,level, bio from USER_PROFILE WHERE email = '"+email+"'"
        cursor.execute(query)
        result = cursor.fetchall()

        print(result)

        if result:
            profile.countryCode = result[0][0]
            profile.nativeLang = result[0][1]
            profile.level = result[0][2]
            profile.bio = result[0][3]


        list2 = []
        query2 = "SELECT learning_lang from LEARNING_LANG WHERE email = '"+email+"' ORDER BY learning_lang"
        cursor.execute(query2)
        result2 = cursor.fetchall()
        i=0
        while i <len(result2):
            list2 += result2[i]
            i = i+1
        profile.learningLang = list2
        

        # profile.picURL = ""
        # profile.bio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
       
        list3 = []
        query3 = "SELECT interest from INTERESTS WHERE email = '"+email+"' ORDER BY interest"
        cursor.execute(query3)
        result3 = cursor.fetchall()
        i=0
        while i <len(result3):
            list3 += result3[i]
            i = i+1
        profile.interests = list3
        
        profile.email = email        
        
    connection.commit()   
    return profile



def getUserByEmail(email):
    user = User()

    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    query1 = "SELECT * from user WHERE email = '"+email+"'"
    cursor.execute(query1)
    result = cursor.fetchall()

    if result:
        user.name = result[0][0]
        user.email = result[0][1]
        user.password = result[0][2]
        user.profile = getUserProfile(user.email)

    return user


#function to create web server

#Create an instance of Flask as 'app'
app = Flask(__name__)
bcrpyt = Bcrypt(app)
CORS(app)
bcrypt = Bcrypt(app)
#We should store our private key in a more secure way, like encryption or somewhere on github.
app.config['SECRET_KEY'] = 'exlang'
currentdirectory  = os.path.dirname(os.path.abspath(__file__))
user_email = "none"

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
    #and then (bcrypt.check_password_hash(realPassword, candiate), if True, authorize login
    user = getUserByEmail(email)
    

    if(user.email is not None and bcrypt.check_password_hash(user.password, password)):
        user.password = None
        return jsonpickle.encode(user), 200
    else:    
        data = {'message': 'Incorrect email or password!'}
        return jsonify(data), 401


#SIGN-UP
@app.route("/register", methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
    # connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    # cursor = connection.cursor()
    # pw_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    # query1 = "INSERT INTO user VALUES ('{name}', '{email}', '{password}')".format(name = name, email = email, password = pw_hash)
    # cursor.execute(query1)
    # connection.commit()
        
            
    user = getUserByEmail(email)
    # Only try to register user if email is NOT in use.
    if (user.email is None):
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        query1 = "INSERT INTO USER VALUES ('{name}', '{email}', '{password}')".format(name = name, email = email, password = pw_hash)
        cursor.execute(query1)
        connection.commit()
        user = getUserByEmail(email)
        return jsonpickle.encode(user), 200

    else:
        data = {'message': 'This Email Address is already in used! Please try a different Email Address.'}
        return jsonify(data), 401        


#Retrieve user profile by email address and return as JSON
#Example: http://127.0.0.1:5000/user/profile/firstlast@email.com
@app.route("/user/profile/<email>", methods=['GET'])
def user_profile(email):
    assert email == request.view_args['email']

    user = getUserByEmail(email)
    if (user.email is not None):
        user.password = None
        return jsonpickle.encode(user), 200
    else:
        data = {'message': 'User not found!'}
        return jsonify(data), 404


#------------------------------------------TO-DO: Save the data from this endpoint to database------------------------------------------#
#Save user profile from JSON.
#Example: http://127.0.0.1:5000/user/profile
@app.route("/user/profile", methods=['POST'])
def update_user_profile():
    json = request.get_json()
    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    print(json)
    user = getUserByEmail(json["email"])

    if not user:
        query1 =  "INSERT INTO USER_PROFILE(email,countryCode, native_Lang, level) VALUES ('{email}', '{countryCode}', '{native_Lang}','{level}')".format(
        email=json["email"],countryCode = json["countryCode"],native_Lang = json["nativeLang"],level= json["level"])
        cursor.execute(query1)

        array  = json["learningLangs"]
        for i in array:
            query = "INSERT INTO LEARNING_LANG(email,learning_lang) VALUES ('{email}', '{learning_lang}')".format(
            email=json["email"],learning_lang = i.strip())
            cursor.execute(query)
        
        list = json["interest"]
        x = list.split(",")
        for i in x:
            query2 = "INSERT INTO INTERESTS(email,interest) VALUES ('{email}', '{interest}')".format(
            email=json["email"],interest = i.strip())
            cursor.execute(query2)

    else:

        cursor.execute("DELETE FROM USER_PROFILE WHERE email = '{email}'".format(email=json["email"]))
        query1 =  "INSERT INTO USER_PROFILE(email,countryCode, native_Lang, level, bio) VALUES ('{email}', '{countryCode}', '{native_Lang}','{level}', '{bio}')".format(
        email=json["email"],countryCode = json["countryCode"],native_Lang = json["nativeLang"],level=json["level"], bio=json["bio"])
        cursor.execute(query1)

        cursor.execute("DELETE FROM LEARNING_LANG WHERE email = '{email}'".format(email=json["email"]))
        array  = json["learningLangs"]
        for i in array:
            query = "INSERT INTO LEARNING_LANG(email,learning_lang) VALUES ('{email}', '{learning_lang}')".format(
            email=json["email"],learning_lang = i.strip())
            cursor.execute(query)
        

        cursor.execute("DELETE FROM INTERESTS WHERE email = '{email}'".format(email=json["email"]))
        list = json["interest"]
        x = list.split(",")
        for i in x:
            query2 = "INSERT INTO INTERESTS(email,interest) VALUES ('{email}', '{interest}')".format(
            email=json["email"],interest = i.strip())
            cursor.execute(query2)


    connection.commit()



    return jsonpickle.encode(request.get_json()), 200


#Get user availability from DB.
#Example: http://127.0.0.1:5000/user/availability/existingUser@email.com
@app.route("/user/availability/<email>", methods=['GET'])
def get_user_availability(email):
    assert email == request.view_args['email']
    
    #--------------------------------------------------------------------------------To-Do: Get user availability in the following JSON format.
    availability = {
        "email": email,
        "sunday":{
            "isAvailable":False,
            "startTime":"",
            "endTime":""
        },
        "monday":{
            "isAvailable":True,
            "startTime":"08:00",
            "endTime":"10:00"
        },
        "tuesday":{
            "isAvailable":True,
            "startTime":"15:00",
            "endTime":"17:00"
        },
        "wednesday":{
            "isAvailable":False,
            "startTime":"",
            "endTime":""
        },
        "thursday":{
            "isAvailable":True,
            "startTime":"15:00",
            "endTime":"17:00"
        },
        "friday":{
            "isAvailable":True,
            "startTime":"12:00",
            "endTime":"14:00"
        },
        "saturday":{
            "isAvailable":False,
            "startTime":"",
            "endTime":""
        }
    }

    return jsonpickle.encode(availability), 200


#Save user availability from JSON.
#Example: http://127.0.0.1:5000/user/availability
@app.route("/user/availability", methods=['POST'])
def update_user_availability():
    json = request.get_json()
    email = json["email"]
    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    day = ""
    day1 = "monday"
    day2 = "tuesday"
    day3 = "wednesday"
    day4 = "thursday"
    day5 = "friday"
    day6 = "saturday"
    day7 = "sunday"
    i=1
    while i < 8:
        if(i==1):
            day = day1
        elif(i==2):
            day = day2
        elif(i==3):
            day = day3
        elif(i==4):
            day = day4
        elif(i==5):
            day = day5
        elif(i==6):
            day = day6
        elif(i==7):
            day = day7
        if json[day]['isAvailable'] == True:
            cursor.execute("DELETE FROM AVAILABILITY WHERE email = '{email}' AND day = '{day}'".format(email=json["email"],day = day) )
            query1 = "INSERT INTO AVAILABIlITY(email,day,start_time,end_time) VALUES ('{email}', '{day}','{start_time}','{end_time}')".format(
                email=json["email"],day = day,start_time = json[day]["startTime"],end_time = json[day]["endTime"])
            cursor.execute(query1)
        else:
            cursor.execute("DELETE FROM AVAILABILITY WHERE email = '{email}' AND day = '{day}'".format(email=json["email"],day = day) )

        i=i+1
   
    connection.commit()

    
    

    #--------------------------------------------------------------------------------To-Do: Save user availability to db. Time is in 24hr string format.
    '''
    {
        "email":"existingUser@email.com",
        "sunday":{
            "isAvailable":False,
            "startTime":"",
            "endTime":""
        },
        "monday":{
            "isAvailable":True,
            "startTime":"08:00",
            "endTime":"10:00"
        },
        "tuesday":{
            "isAvailable":True,
            "startTime":"15:00",
            "endTime":"17:00"
        },
        "wednesday":{
            "isAvailable":True,
            "startTime":"08:00",
            "endTime":"10:00"
        },
        "thursday":{
            "isAvailable":True,
            "startTime":"15:00",
            "endTime":"17:00"
        },
        "friday":{
            "isAvailable":True,
            "startTime":"08:00",
            "endTime":"10:00"
        },
        "saturday":{
            "isAvailable":False,
            "startTime":"",
            "endTime":""
        }
    }   
    '''

    return jsonpickle.encode(request.get_json()), 200

@app.route("/user/session-setting", methods=['POST'])
def update_user_session_setting():
    json = request.get_json()
    email = json["email"]
    connection = sqlite3.connect(currentdirectory + "\ExLang.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM SESSION WHERE email = '{email}' ".format(email=json["email"]) )
    query1 = "INSERT INTO SESSION(email,duration,people,timeZone) VALUES ('{email}', '{duration}','{people}','{timeZone}')".format(
                email=json["email"],duration = json["sessionDuration"],people = json["peopleBook"],timeZone = json["timeZone"])
    cursor.execute(query1)
    connection.commit()


    print(json)    

    #--------------------------------------------------------------------------------To-Do: Save to db.
    '''
    {
        "sessionDuration":60,
        "peopleBook":"Friends",
        "timeZone":"EDT",
        "email":"existingUser@email.com"
    }
    '''


    return jsonpickle.encode(request.get_json()), 200

#List of countries for UI dropdown select list.
#Example: http://127.0.0.1:5000/countries
@app.route("/countries", methods=['GET'])
def countries():
    data = [ 
        {"name": "Afghanistan", "code": "AF"}, 
        {"name": "land Islands", "code": "AX"}, 
        {"name": "Albania", "code": "AL"}, 
        {"name": "Algeria", "code": "DZ"}, 
        {"name": "American Samoa", "code": "AS"}, 
        {"name": "AndorrA", "code": "AD"}, 
        {"name": "Angola", "code": "AO"}, 
        {"name": "Anguilla", "code": "AI"}, 
        {"name": "Antarctica", "code": "AQ"}, 
        {"name": "Antigua and Barbuda", "code": "AG"}, 
        {"name": "Argentina", "code": "AR"}, 
        {"name": "Armenia", "code": "AM"}, 
        {"name": "Aruba", "code": "AW"}, 
        {"name": "Australia", "code": "AU"}, 
        {"name": "Austria", "code": "AT"}, 
        {"name": "Azerbaijan", "code": "AZ"}, 
        {"name": "Bahamas", "code": "BS"}, 
        {"name": "Bahrain", "code": "BH"}, 
        {"name": "Bangladesh", "code": "BD"}, 
        {"name": "Barbados", "code": "BB"}, 
        {"name": "Belarus", "code": "BY"}, 
        {"name": "Belgium", "code": "BE"}, 
        {"name": "Belize", "code": "BZ"}, 
        {"name": "Benin", "code": "BJ"}, 
        {"name": "Bermuda", "code": "BM"}, 
        {"name": "Bhutan", "code": "BT"}, 
        {"name": "Bolivia", "code": "BO"}, 
        {"name": "Bosnia and Herzegovina", "code": "BA"}, 
        {"name": "Botswana", "code": "BW"}, 
        {"name": "Bouvet Island", "code": "BV"}, 
        {"name": "Brazil", "code": "BR"}, 
        {"name": "British Indian Ocean Territory", "code": "IO"}, 
        {"name": "Brunei Darussalam", "code": "BN"}, 
        {"name": "Bulgaria", "code": "BG"}, 
        {"name": "Burkina Faso", "code": "BF"}, 
        {"name": "Burundi", "code": "BI"}, 
        {"name": "Cambodia", "code": "KH"}, 
        {"name": "Cameroon", "code": "CM"}, 
        {"name": "Canada", "code": "CA"}, 
        {"name": "Cape Verde", "code": "CV"}, 
        {"name": "Cayman Islands", "code": "KY"}, 
        {"name": "Central African Republic", "code": "CF"}, 
        {"name": "Chad", "code": "TD"}, 
        {"name": "Chile", "code": "CL"}, 
        {"name": "China", "code": "CN"}, 
        {"name": "Christmas Island", "code": "CX"}, 
        {"name": "Cocos (Keeling) Islands", "code": "CC"}, 
        {"name": "Colombia", "code": "CO"}, 
        {"name": "Comoros", "code": "KM"}, 
        {"name": "Congo", "code": "CG"}, 
        {"name": "Congo, The Democratic Republic of the", "code": "CD"}, 
        {"name": "Cook Islands", "code": "CK"}, 
        {"name": "Costa Rica", "code": "CR"}, 
        {"name": "Cote D\"Ivoire", "code": "CI"}, 
        {"name": "Croatia", "code": "HR"}, 
        {"name": "Cuba", "code": "CU"}, 
        {"name": "Cyprus", "code": "CY"}, 
        {"name": "Czech Republic", "code": "CZ"}, 
        {"name": "Denmark", "code": "DK"}, 
        {"name": "Djibouti", "code": "DJ"}, 
        {"name": "Dominica", "code": "DM"}, 
        {"name": "Dominican Republic", "code": "DO"}, 
        {"name": "Ecuador", "code": "EC"}, 
        {"name": "Egypt", "code": "EG"}, 
        {"name": "El Salvador", "code": "SV"}, 
        {"name": "Equatorial Guinea", "code": "GQ"}, 
        {"name": "Eritrea", "code": "ER"}, 
        {"name": "Estonia", "code": "EE"}, 
        {"name": "Ethiopia", "code": "ET"}, 
        {"name": "Falkland Islands (Malvinas)", "code": "FK"}, 
        {"name": "Faroe Islands", "code": "FO"}, 
        {"name": "Fiji", "code": "FJ"}, 
        {"name": "Finland", "code": "FI"}, 
        {"name": "France", "code": "FR"}, 
        {"name": "French Guiana", "code": "GF"}, 
        {"name": "French Polynesia", "code": "PF"}, 
        {"name": "French Southern Territories", "code": "TF"}, 
        {"name": "Gabon", "code": "GA"}, 
        {"name": "Gambia", "code": "GM"}, 
        {"name": "Georgia", "code": "GE"}, 
        {"name": "Germany", "code": "DE"}, 
        {"name": "Ghana", "code": "GH"}, 
        {"name": "Gibraltar", "code": "GI"}, 
        {"name": "Greece", "code": "GR"}, 
        {"name": "Greenland", "code": "GL"}, 
        {"name": "Grenada", "code": "GD"}, 
        {"name": "Guadeloupe", "code": "GP"}, 
        {"name": "Guam", "code": "GU"}, 
        {"name": "Guatemala", "code": "GT"}, 
        {"name": "Guernsey", "code": "GG"}, 
        {"name": "Guinea", "code": "GN"}, 
        {"name": "Guinea-Bissau", "code": "GW"}, 
        {"name": "Guyana", "code": "GY"}, 
        {"name": "Haiti", "code": "HT"}, 
        {"name": "Heard Island and Mcdonald Islands", "code": "HM"}, 
        {"name": "Holy See (Vatican City State)", "code": "VA"}, 
        {"name": "Honduras", "code": "HN"}, 
        {"name": "Hong Kong", "code": "HK"}, 
        {"name": "Hungary", "code": "HU"}, 
        {"name": "Iceland", "code": "IS"}, 
        {"name": "India", "code": "IN"}, 
        {"name": "Indonesia", "code": "ID"}, 
        {"name": "Iran, Islamic Republic Of", "code": "IR"}, 
        {"name": "Iraq", "code": "IQ"}, 
        {"name": "Ireland", "code": "IE"}, 
        {"name": "Isle of Man", "code": "IM"}, 
        {"name": "Israel", "code": "IL"}, 
        {"name": "Italy", "code": "IT"}, 
        {"name": "Jamaica", "code": "JM"}, 
        {"name": "Japan", "code": "JP"}, 
        {"name": "Jersey", "code": "JE"}, 
        {"name": "Jordan", "code": "JO"}, 
        {"name": "Kazakhstan", "code": "KZ"}, 
        {"name": "Kenya", "code": "KE"}, 
        {"name": "Kiribati", "code": "KI"}, 
        {"name": "Korea, Democratic People\"S Republic of", "code": "KP"}, 
        {"name": "Korea, Republic of", "code": "KR"}, 
        {"name": "Kuwait", "code": "KW"}, 
        {"name": "Kyrgyzstan", "code": "KG"}, 
        {"name": "Lao People\"S Democratic Republic", "code": "LA"}, 
        {"name": "Latvia", "code": "LV"}, 
        {"name": "Lebanon", "code": "LB"}, 
        {"name": "Lesotho", "code": "LS"}, 
        {"name": "Liberia", "code": "LR"}, 
        {"name": "Libyan Arab Jamahiriya", "code": "LY"}, 
        {"name": "Liechtenstein", "code": "LI"}, 
        {"name": "Lithuania", "code": "LT"}, 
        {"name": "Luxembourg", "code": "LU"}, 
        {"name": "Macao", "code": "MO"}, 
        {"name": "Macedonia, The Former Yugoslav Republic of", "code": "MK"}, 
        {"name": "Madagascar", "code": "MG"}, 
        {"name": "Malawi", "code": "MW"}, 
        {"name": "Malaysia", "code": "MY"}, 
        {"name": "Maldives", "code": "MV"}, 
        {"name": "Mali", "code": "ML"}, 
        {"name": "Malta", "code": "MT"}, 
        {"name": "Marshall Islands", "code": "MH"}, 
        {"name": "Martinique", "code": "MQ"}, 
        {"name": "Mauritania", "code": "MR"}, 
        {"name": "Mauritius", "code": "MU"}, 
        {"name": "Mayotte", "code": "YT"}, 
        {"name": "Mexico", "code": "MX"}, 
        {"name": "Micronesia, Federated States of", "code": "FM"}, 
        {"name": "Moldova, Republic of", "code": "MD"}, 
        {"name": "Monaco", "code": "MC"}, 
        {"name": "Mongolia", "code": "MN"}, 
        {"name": "Montenegro", "code": "ME"},
        {"name": "Montserrat", "code": "MS"},
        {"name": "Morocco", "code": "MA"}, 
        {"name": "Mozambique", "code": "MZ"}, 
        {"name": "Myanmar", "code": "MM"}, 
        {"name": "Namibia", "code": "NA"}, 
        {"name": "Nauru", "code": "NR"}, 
        {"name": "Nepal", "code": "NP"}, 
        {"name": "Netherlands", "code": "NL"}, 
        {"name": "Netherlands Antilles", "code": "AN"}, 
        {"name": "New Caledonia", "code": "NC"}, 
        {"name": "New Zealand", "code": "NZ"}, 
        {"name": "Nicaragua", "code": "NI"}, 
        {"name": "Niger", "code": "NE"}, 
        {"name": "Nigeria", "code": "NG"}, 
        {"name": "Niue", "code": "NU"}, 
        {"name": "Norfolk Island", "code": "NF"}, 
        {"name": "Northern Mariana Islands", "code": "MP"}, 
        {"name": "Norway", "code": "NO"}, 
        {"name": "Oman", "code": "OM"}, 
        {"name": "Pakistan", "code": "PK"}, 
        {"name": "Palau", "code": "PW"}, 
        {"name": "Palestinian Territory, Occupied", "code": "PS"}, 
        {"name": "Panama", "code": "PA"}, 
        {"name": "Papua New Guinea", "code": "PG"}, 
        {"name": "Paraguay", "code": "PY"}, 
        {"name": "Peru", "code": "PE"}, 
        {"name": "Philippines", "code": "PH"}, 
        {"name": "Pitcairn", "code": "PN"}, 
        {"name": "Poland", "code": "PL"}, 
        {"name": "Portugal", "code": "PT"}, 
        {"name": "Puerto Rico", "code": "PR"}, 
        {"name": "Qatar", "code": "QA"}, 
        {"name": "Reunion", "code": "RE"}, 
        {"name": "Romania", "code": "RO"}, 
        {"name": "Russian Federation", "code": "RU"}, 
        {"name": "RWANDA", "code": "RW"}, 
        {"name": "Saint Helena", "code": "SH"}, 
        {"name": "Saint Kitts and Nevis", "code": "KN"}, 
        {"name": "Saint Lucia", "code": "LC"}, 
        {"name": "Saint Pierre and Miquelon", "code": "PM"}, 
        {"name": "Saint Vincent and the Grenadines", "code": "VC"}, 
        {"name": "Samoa", "code": "WS"}, 
        {"name": "San Marino", "code": "SM"}, 
        {"name": "Sao Tome and Principe", "code": "ST"}, 
        {"name": "Saudi Arabia", "code": "SA"}, 
        {"name": "Senegal", "code": "SN"}, 
        {"name": "Serbia", "code": "RS"}, 
        {"name": "Seychelles", "code": "SC"}, 
        {"name": "Sierra Leone", "code": "SL"}, 
        {"name": "Singapore", "code": "SG"}, 
        {"name": "Slovakia", "code": "SK"}, 
        {"name": "Slovenia", "code": "SI"}, 
        {"name": "Solomon Islands", "code": "SB"}, 
        {"name": "Somalia", "code": "SO"}, 
        {"name": "South Africa", "code": "ZA"}, 
        {"name": "South Georgia and the South Sandwich Islands", "code": "GS"}, 
        {"name": "Spain", "code": "ES"}, 
        {"name": "Sri Lanka", "code": "LK"}, 
        {"name": "Sudan", "code": "SD"}, 
        {"name": "Suriname", "code": "SR"}, 
        {"name": "Svalbard and Jan Mayen", "code": "SJ"}, 
        {"name": "Swaziland", "code": "SZ"}, 
        {"name": "Sweden", "code": "SE"}, 
        {"name": "Switzerland", "code": "CH"}, 
        {"name": "Syrian Arab Republic", "code": "SY"}, 
        {"name": "Taiwan, Province of China", "code": "TW"}, 
        {"name": "Tajikistan", "code": "TJ"}, 
        {"name": "Tanzania, United Republic of", "code": "TZ"}, 
        {"name": "Thailand", "code": "TH"}, 
        {"name": "Timor-Leste", "code": "TL"}, 
        {"name": "Togo", "code": "TG"}, 
        {"name": "Tokelau", "code": "TK"}, 
        {"name": "Tonga", "code": "TO"}, 
        {"name": "Trinidad and Tobago", "code": "TT"}, 
        {"name": "Tunisia", "code": "TN"}, 
        {"name": "Turkey", "code": "TR"}, 
        {"name": "Turkmenistan", "code": "TM"}, 
        {"name": "Turks and Caicos Islands", "code": "TC"}, 
        {"name": "Tuvalu", "code": "TV"}, 
        {"name": "Uganda", "code": "UG"}, 
        {"name": "Ukraine", "code": "UA"}, 
        {"name": "United Arab Emirates", "code": "AE"}, 
        {"name": "United Kingdom", "code": "GB"}, 
        {"name": "United States", "code": "US"}, 
        {"name": "United States Minor Outlying Islands", "code": "UM"}, 
        {"name": "Uruguay", "code": "UY"}, 
        {"name": "Uzbekistan", "code": "UZ"}, 
        {"name": "Vanuatu", "code": "VU"}, 
        {"name": "Venezuela", "code": "VE"}, 
        {"name": "Viet Nam", "code": "VN"}, 
        {"name": "Virgin Islands, British", "code": "VG"}, 
        {"name": "Virgin Islands, U.S.", "code": "VI"}, 
        {"name": "Wallis and Futuna", "code": "WF"}, 
        {"name": "Western Sahara", "code": "EH"}, 
        {"name": "Yemen", "code": "YE"}, 
        {"name": "Zambia", "code": "ZM"}, 
        {"name": "Zimbabwe", "code": "ZW"} 
        ]
    return jsonify(data), 200


#List of languages for UI dropdown select list.
#Example: http://127.0.0.1:5000/languages
@app.route("/languages", methods=['GET'])
def languages():
    data = [
        {
            "code": "ab",
            "name": "Abkhaz"
        },
        {
            "code": "aa",
            "name": "Afar"
        },
        {
            "code": "af",
            "name": "Afrikaans"
        },
        {
            "code": "ak",
            "name": "Akan"
        },
        {
            "code": "sq",
            "name": "Albanian"
        },
        {
            "code": "am",
            "name": "Amharic"
        },
        {
            "code": "ar",
            "name": "Arabic"
        },
        {
            "code": "an",
            "name": "Aragonese"
        },
        {
            "code": "hy",
            "name": "Armenian"
        },
        {
            "code": "as",
            "name": "Assamese"
        },
        {
            "code": "av",
            "name": "Avaric"
        },
        {
            "code": "ae",
            "name": "Avestan"
        },
        {
            "code": "ay",
            "name": "Aymara"
        },
        {
            "code": "az",
            "name": "Azerbaijani"
        },
        {
            "code": "bm",
            "name": "Bambara"
        },
        {
            "code": "ba",
            "name": "Bashkir"
        },
        {
            "code": "eu",
            "name": "Basque"
        },
        {
            "code": "be",
            "name": "Belarusian"
        },
        {
            "code": "bn",
            "name": "Bengali"
        },
        {
            "code": "bh",
            "name": "Bihari"
        },
        {
            "code": "bi",
            "name": "Bislama"
        },
        {
            "code": "bs",
            "name": "Bosnian"
        },
        {
            "code": "br",
            "name": "Breton"
        },
        {
            "code": "bg",
            "name": "Bulgarian"
        },
        {
            "code": "my",
            "name": "Burmese"
        },
        {
            "code": "ca",
            "name": "Catalan; Valencian"
        },
        {
            "code": "ch",
            "name": "Chamorro"
        },
        {
            "code": "ce",
            "name": "Chechen"
        },
        {
            "code": "ny",
            "name": "Chichewa; Chewa; Nyanja"
        },
        {
            "code": "zh",
            "name": "Chinese"
        },
        {
            "code": "cv",
            "name": "Chuvash"
        },
        {
            "code": "kw",
            "name": "Cornish"
        },
        {
            "code": "co",
            "name": "Corsican"
        },
        {
            "code": "cr",
            "name": "Cree"
        },
        {
            "code": "hr",
            "name": "Croatian"
        },
        {
            "code": "cs",
            "name": "Czech"
        },
        {
            "code": "da",
            "name": "Danish"
        },
        {
            "code": "dv",
            "name": "Divehi; Dhivehi; Maldivian;"
        },
        {
            "code": "nl",
            "name": "Dutch"
        },
        {
            "code": "en",
            "name": "English"
        },
        {
            "code": "eo",
            "name": "Esperanto"
        },
        {
            "code": "et",
            "name": "Estonian"
        },
        {
            "code": "ee",
            "name": "Ewe"
        },
        {
            "code": "fo",
            "name": "Faroese"
        },
        {
            "code": "fj",
            "name": "Fijian"
        },
        {
            "code": "fi",
            "name": "Finnish"
        },
        {
            "code": "fr",
            "name": "French"
        },
        {
            "code": "ff",
            "name": "Fula; Fulah; Pulaar; Pular"
        },
        {
            "code": "gl",
            "name": "Galician"
        },
        {
            "code": "ka",
            "name": "Georgian"
        },
        {
            "code": "de",
            "name": "German"
        },
        {
            "code": "el",
            "name": "Greek, Modern"
        },
        {
            "code": "gn",
            "name": "Guaraní"
        },
        {
            "code": "gu",
            "name": "Gujarati"
        },
        {
            "code": "ht",
            "name": "Haitian; Haitian Creole"
        },
        {
            "code": "ha",
            "name": "Hausa"
        },
        {
            "code": "he",
            "name": "Hebrew (modern)"
        },
        {
            "code": "hz",
            "name": "Herero"
        },
        {
            "code": "hi",
            "name": "Hindi"
        },
        {
            "code": "ho",
            "name": "Hiri Motu"
        },
        {
            "code": "hu",
            "name": "Hungarian"
        },
        {
            "code": "ia",
            "name": "Interlingua"
        },
        {
            "code": "id",
            "name": "Indonesian"
        },
        {
            "code": "ie",
            "name": "Interlingue"
        },
        {
            "code": "ga",
            "name": "Irish"
        },
        {
            "code": "ig",
            "name": "Igbo"
        },
        {
            "code": "ik",
            "name": "Inupiaq"
        },
        {
            "code": "io",
            "name": "Ido"
        },
        {
            "code": "is",
            "name": "Icelandic"
        },
        {
            "code": "it",
            "name": "Italian"
        },
        {
            "code": "iu",
            "name": "Inuktitut"
        },
        {
            "code": "ja",
            "name": "Japanese"
        },
        {
            "code": "jv",
            "name": "Javanese"
        },
        {
            "code": "kl",
            "name": "Kalaallisut, Greenlandic"
        },
        {
            "code": "kn",
            "name": "Kannada"
        },
        {
            "code": "kr",
            "name": "Kanuri"
        },
        {
            "code": "ks",
            "name": "Kashmiri"
        },
        {
            "code": "kk",
            "name": "Kazakh"
        },
        {
            "code": "km",
            "name": "Khmer"
        },
        {
            "code": "ki",
            "name": "Kikuyu, Gikuyu"
        },
        {
            "code": "rw",
            "name": "Kinyarwanda"
        },
        {
            "code": "ky",
            "name": "Kirghiz, Kyrgyz"
        },
        {
            "code": "kv",
            "name": "Komi"
        },
        {
            "code": "kg",
            "name": "Kongo"
        },
        {
            "code": "ko",
            "name": "Korean"
        },
        {
            "code": "ku",
            "name": "Kurdish"
        },
        {
            "code": "kj",
            "name": "Kwanyama, Kuanyama"
        },
        {
            "code": "la",
            "name": "Latin"
        },
        {
            "code": "lb",
            "name": "Luxembourgish, Letzeburgesch"
        },
        {
            "code": "lg",
            "name": "Luganda"
        },
        {
            "code": "li",
            "name": "Limburgish, Limburgan, Limburger"
        },
        {
            "code": "ln",
            "name": "Lingala"
        },
        {
            "code": "lo",
            "name": "Lao"
        },
        {
            "code": "lt",
            "name": "Lithuanian"
        },
        {
            "code": "lu",
            "name": "Luba-Katanga"
        },
        {
            "code": "lv",
            "name": "Latvian"
        },
        {
            "code": "gv",
            "name": "Manx"
        },
        {
            "code": "mk",
            "name": "Macedonian"
        },
        {
            "code": "mg",
            "name": "Malagasy"
        },
        {
            "code": "ms",
            "name": "Malay"
        },
        {
            "code": "ml",
            "name": "Malayalam"
        },
        {
            "code": "mt",
            "name": "Maltese"
        },
        {
            "code": "mi",
            "name": "Māori"
        },
        {
            "code": "mr",
            "name": "Marathi (Marāṭhī)"
        },
        {
            "code": "mh",
            "name": "Marshallese"
        },
        {
            "code": "mn",
            "name": "Mongolian"
        },
        {
            "code": "na",
            "name": "Nauru"
        },
        {
            "code": "nv",
            "name": "Navajo, Navaho"
        },
        {
            "code": "nb",
            "name": "Norwegian Bokmål"
        },
        {
            "code": "nd",
            "name": "North Ndebele"
        },
        {
            "code": "ne",
            "name": "Nepali"
        },
        {
            "code": "ng",
            "name": "Ndonga"
        },
        {
            "code": "nn",
            "name": "Norwegian Nynorsk"
        },
        {
            "code": "no",
            "name": "Norwegian"
        },
        {
            "code": "ii",
            "name": "Nuosu"
        },
        {
            "code": "nr",
            "name": "South Ndebele"
        },
        {
            "code": "oc",
            "name": "Occitan"
        },
        {
            "code": "oj",
            "name": "Ojibwe, Ojibwa"
        },
        {
            "code": "cu",
            "name": "Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic"
        },
        {
            "code": "om",
            "name": "Oromo"
        },
        {
            "code": "or",
            "name": "Oriya"
        },
        {
            "code": "os",
            "name": "Ossetian, Ossetic"
        },
        {
            "code": "pa",
            "name": "Panjabi, Punjabi"
        },
        {
            "code": "pi",
            "name": "Pāli"
        },
        {
            "code": "fa",
            "name": "Persian"
        },
        {
            "code": "pl",
            "name": "Polish"
        },
        {
            "code": "ps",
            "name": "Pashto, Pushto"
        },
        {
            "code": "pt",
            "name": "Portuguese"
        },
        {
            "code": "qu",
            "name": "Quechua"
        },
        {
            "code": "rm",
            "name": "Romansh"
        },
        {
            "code": "rn",
            "name": "Kirundi"
        },
        {
            "code": "ro",
            "name": "Romanian, Moldavian, Moldovan"
        },
        {
            "code": "ru",
            "name": "Russian"
        },
        {
            "code": "sa",
            "name": "Sanskrit (Saṁskṛta)"
        },
        {
            "code": "sc",
            "name": "Sardinian"
        },
        {
            "code": "sd",
            "name": "Sindhi"
        },
        {
            "code": "se",
            "name": "Northern Sami"
        },
        {
            "code": "sm",
            "name": "Samoan"
        },
        {
            "code": "sg",
            "name": "Sango"
        },
        {
            "code": "sr",
            "name": "Serbian"
        },
        {
            "code": "gd",
            "name": "Scottish Gaelic; Gaelic"
        },
        {
            "code": "sn",
            "name": "Shona"
        },
        {
            "code": "si",
            "name": "Sinhala, Sinhalese"
        },
        {
            "code": "sk",
            "name": "Slovak"
        },
        {
            "code": "sl",
            "name": "Slovene"
        },
        {
            "code": "so",
            "name": "Somali"
        },
        {
            "code": "st",
            "name": "Southern Sotho"
        },
        {
            "code": "es",
            "name": "Spanish; Castilian"
        },
        {
            "code": "su",
            "name": "Sundanese"
        },
        {
            "code": "sw",
            "name": "Swahili"
        },
        {
            "code": "ss",
            "name": "Swati"
        },
        {
            "code": "sv",
            "name": "Swedish"
        },
        {
            "code": "ta",
            "name": "Tamil"
        },
        {
            "code": "te",
            "name": "Telugu"
        },
        {
            "code": "tg",
            "name": "Tajik"
        },
        {
            "code": "th",
            "name": "Thai"
        },
        {
            "code": "ti",
            "name": "Tigrinya"
        },
        {
            "code": "bo",
            "name": "Tibetan Standard, Tibetan, Central"
        },
        {
            "code": "tk",
            "name": "Turkmen"
        },
        {
            "code": "tl",
            "name": "Tagalog"
        },
        {
            "code": "tn",
            "name": "Tswana"
        },
        {
            "code": "to",
            "name": "Tonga (Tonga Islands)"
        },
        {
            "code": "tr",
            "name": "Turkish"
        },
        {
            "code": "ts",
            "name": "Tsonga"
        },
        {
            "code": "tt",
            "name": "Tatar"
        },
        {
            "code": "tw",
            "name": "Twi"
        },
        {
            "code": "ty",
            "name": "Tahitian"
        },
        {
            "code": "ug",
            "name": "Uighur, Uyghur"
        },
        {
            "code": "uk",
            "name": "Ukrainian"
        },
        {
            "code": "ur",
            "name": "Urdu"
        },
        {
            "code": "uz",
            "name": "Uzbek"
        },
        {
            "code": "ve",
            "name": "Venda"
        },
        {
            "code": "vi",
            "name": "Vietnamese"
        },
        {
            "code": "vo",
            "name": "Volapük"
        },
        {
            "code": "wa",
            "name": "Walloon"
        },
        {
            "code": "cy",
            "name": "Welsh"
        },
        {
            "code": "wo",
            "name": "Wolof"
        },
        {
            "code": "fy",
            "name": "Western Frisian"
        },
        {
            "code": "xh",
            "name": "Xhosa"
        },
        {
            "code": "yi",
            "name": "Yiddish"
        },
        {
            "code": "yo",
            "name": "Yoruba"
        },
        {
            "code": "za",
            "name": "Zhuang, Chuang"
        }
        ]
    return jsonify(data), 200


#List of Levels for UI drop down list.
#Example: http://127.0.0.1:5000/levels
@app.route("/levels", methods=['GET'])
def levels():
    data = [
        {
            "code": "Beginner",
            "name": "Beginner",
        },
        {
            "code": "Intermediate",
            "name": "Intermediate",
        },
        {
            "code": "Advanced",
            "name": "Advanced",
        }
    ]
    return jsonify(data), 200

#List of Timezones for UI drop down list.
#Example: http://127.0.0.1:5000/timezones
@app.route("/timezones", methods=['GET'])
def timezones():
    data = [
        {
            "value":"Dateline Standard Time",
            "abbr":"DST",
            "offset":-12,
            "isdst":False,
            "text":"(UTC-12:00) International Date Line West"
        },
        {
            "value":"UTC-11",
            "abbr":"U",
            "offset":-11,
            "isdst":False,
            "text":"(UTC-11:00) Coordinated Universal Time-11"
        },
        {
            "value":"Hawaiian Standard Time",
            "abbr":"HST",
            "offset":-10,
            "isdst":False,
            "text":"(UTC-10:00) Hawaii"
        },
        {
            "value":"Alaskan Standard Time",
            "abbr":"AKDT",
            "offset":-8,
            "isdst":True,
            "text":"(UTC-09:00) Alaska"
        },
        {
            "value":"Pacific Standard Time (Mexico)",
            "abbr":"PDT",
            "offset":-7,
            "isdst":True,
            "text":"(UTC-08:00) Baja California"
        },
        {
            "value":"Pacific Standard Time",
            "abbr":"PDT",
            "offset":-7,
            "isdst":True,
            "text":"(UTC-08:00) Pacific Time (US & Canada)"
        },
        {
            "value":"US Mountain Standard Time",
            "abbr":"UMST",
            "offset":-7,
            "isdst":False,
            "text":"(UTC-07:00) Arizona"
        },
        {
            "value":"Mountain Standard Time (Mexico)",
            "abbr":"MDT",
            "offset":-6,
            "isdst":True,
            "text":"(UTC-07:00) Chihuahua, La Paz, Mazatlan"
        },
        {
            "value":"Mountain Standard Time",
            "abbr":"MDT",
            "offset":-6,
            "isdst":True,
            "text":"(UTC-07:00) Mountain Time (US & Canada)"
        },
        {
            "value":"Central America Standard Time",
            "abbr":"CAST",
            "offset":-6,
            "isdst":False,
            "text":"(UTC-06:00) Central America"
        },
        {
            "value":"Central Standard Time",
            "abbr":"CDT",
            "offset":-5,
            "isdst":True,
            "text":"(UTC-06:00) Central Time (US & Canada)"
        },
        {
            "value":"Central Standard Time (Mexico)",
            "abbr":"CDT",
            "offset":-5,
            "isdst":True,
            "text":"(UTC-06:00) Guadalajara, Mexico City, Monterrey"
        },
        {
            "value":"Canada Central Standard Time",
            "abbr":"CCST",
            "offset":-6,
            "isdst":False,
            "text":"(UTC-06:00) Saskatchewan"
        },
        {
            "value":"SA Pacific Standard Time",
            "abbr":"SPST",
            "offset":-5,
            "isdst":False,
            "text":"(UTC-05:00) Bogota, Lima, Quito"
        },
        {
            "value":"Eastern Standard Time",
            "abbr":"EDT",
            "offset":-4,
            "isdst":True,
            "text":"(UTC-05:00) Eastern Time (US & Canada)"
        },
        {
            "value":"US Eastern Standard Time",
            "abbr":"UEDT",
            "offset":-4,
            "isdst":True,
            "text":"(UTC-05:00) Indiana (East)"
        },
        {
            "value":"Venezuela Standard Time",
            "abbr":"VST",
            "offset":-4.5,
            "isdst":False,
            "text":"(UTC-04:30) Caracas"
        },
        {
            "value":"Paraguay Standard Time",
            "abbr":"PST",
            "offset":-4,
            "isdst":False,
            "text":"(UTC-04:00) Asuncion"
        },
        {
            "value":"Atlantic Standard Time",
            "abbr":"ADT",
            "offset":-3,
            "isdst":True,
            "text":"(UTC-04:00) Atlantic Time (Canada)"
        },
        {
            "value":"Central Brazilian Standard Time",
            "abbr":"CBST",
            "offset":-4,
            "isdst":False,
            "text":"(UTC-04:00) Cuiaba"
        },
        {
            "value":"SA Western Standard Time",
            "abbr":"SWST",
            "offset":-4,
            "isdst":False,
            "text":"(UTC-04:00) Georgetown, La Paz, Manaus, San Juan"
        },
        {
            "value":"Pacific SA Standard Time",
            "abbr":"PSST",
            "offset":-4,
            "isdst":False,
            "text":"(UTC-04:00) Santiago"
        },
        {
            "value":"Newfoundland Standard Time",
            "abbr":"NDT",
            "offset":-2.5,
            "isdst":True,
            "text":"(UTC-03:30) Newfoundland"
        },
        {
            "value":"E. South America Standard Time",
            "abbr":"ESAST",
            "offset":-3,
            "isdst":False,
            "text":"(UTC-03:00) Brasilia"
        },
        {
            "value":"Argentina Standard Time",
            "abbr":"AST",
            "offset":-3,
            "isdst":False,
            "text":"(UTC-03:00) Buenos Aires"
        },
        {
            "value":"SA Eastern Standard Time",
            "abbr":"SEST",
            "offset":-3,
            "isdst":False,
            "text":"(UTC-03:00) Cayenne, Fortaleza"
        },
        {
            "value":"Greenland Standard Time",
            "abbr":"GDT",
            "offset":-2,
            "isdst":True,
            "text":"(UTC-03:00) Greenland"
        },
        {
            "value":"Montevideo Standard Time",
            "abbr":"MST",
            "offset":-3,
            "isdst":False,
            "text":"(UTC-03:00) Montevideo"
        },
        {
            "value":"Bahia Standard Time",
            "abbr":"BST",
            "offset":-3,
            "isdst":False,
            "text":"(UTC-03:00) Salvador"
        },
        {
            "value":"UTC-02",
            "abbr":"U",
            "offset":-2,
            "isdst":False,
            "text":"(UTC-02:00) Coordinated Universal Time-02"
        },
        {
            "value":"Mid-Atlantic Standard Time",
            "abbr":"MDT",
            "offset":-1,
            "isdst":True,
            "text":"(UTC-02:00) Mid-Atlantic - Old"
        },
        {
            "value":"Azores Standard Time",
            "abbr":"ADT",
            "offset":0,
            "isdst":True,
            "text":"(UTC-01:00) Azores"
        },
        {
            "value":"Cape Verde Standard Time",
            "abbr":"CVST",
            "offset":-1,
            "isdst":False,
            "text":"(UTC-01:00) Cape Verde Is."
        },
        {
            "value":"Morocco Standard Time",
            "abbr":"MDT",
            "offset":1,
            "isdst":True,
            "text":"(UTC) Casablanca"
        },
        {
            "value":"UTC",
            "abbr":"CUT",
            "offset":0,
            "isdst":False,
            "text":"(UTC) Coordinated Universal Time"
        },
        {
            "value":"GMT Standard Time",
            "abbr":"GDT",
            "offset":1,
            "isdst":True,
            "text":"(UTC) Dublin, Edinburgh, Lisbon, London"
        },
        {
            "value":"Greenwich Standard Time",
            "abbr":"GST",
            "offset":0,
            "isdst":False,
            "text":"(UTC) Monrovia, Reykjavik"
        },
        {
            "value":"W. Europe Standard Time",
            "abbr":"WEDT",
            "offset":2,
            "isdst":True,
            "text":"(UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna"
        },
        {
            "value":"Central Europe Standard Time",
            "abbr":"CEDT",
            "offset":2,
            "isdst":True,
            "text":"(UTC+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague"
        },
        {
            "value":"Romance Standard Time",
            "abbr":"RDT",
            "offset":2,
            "isdst":True,
            "text":"(UTC+01:00) Brussels, Copenhagen, Madrid, Paris"
        },
        {
            "value":"Central European Standard Time",
            "abbr":"CEDT",
            "offset":2,
            "isdst":True,
            "text":"(UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb"
        },
        {
            "value":"W. Central Africa Standard Time",
            "abbr":"WCAST",
            "offset":1,
            "isdst":False,
            "text":"(UTC+01:00) West Central Africa"
        },
        {
            "value":"Namibia Standard Time",
            "abbr":"NST",
            "offset":1,
            "isdst":False,
            "text":"(UTC+01:00) Windhoek"
        },
        {
            "value":"GTB Standard Time",
            "abbr":"GDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) Athens, Bucharest"
        },
        {
            "value":"Middle East Standard Time",
            "abbr":"MEDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) Beirut"
        },
        {
            "value":"Egypt Standard Time",
            "abbr":"EST",
            "offset":2,
            "isdst":False,
            "text":"(UTC+02:00) Cairo"
        },
        {
            "value":"Syria Standard Time",
            "abbr":"SDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) Damascus"
        },
        {
            "value":"E. Europe Standard Time",
            "abbr":"EEDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) E. Europe"
        },
        {
            "value":"South Africa Standard Time",
            "abbr":"SAST",
            "offset":2,
            "isdst":False,
            "text":"(UTC+02:00) Harare, Pretoria"
        },
        {
            "value":"FLE Standard Time",
            "abbr":"FDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius"
        },
        {
            "value":"Turkey Standard Time",
            "abbr":"TDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) Istanbul"
        },
        {
            "value":"Israel Standard Time",
            "abbr":"JDT",
            "offset":3,
            "isdst":True,
            "text":"(UTC+02:00) Jerusalem"
        },
        {
            "value":"Libya Standard Time",
            "abbr":"LST",
            "offset":2,
            "isdst":False,
            "text":"(UTC+02:00) Tripoli"
        },
        {
            "value":"Jordan Standard Time",
            "abbr":"JST",
            "offset":3,
            "isdst":False,
            "text":"(UTC+03:00) Amman"
        },
        {
            "value":"Arabic Standard Time",
            "abbr":"AST",
            "offset":3,
            "isdst":False,
            "text":"(UTC+03:00) Baghdad"
        },
        {
            "value":"Kaliningrad Standard Time",
            "abbr":"KST",
            "offset":3,
            "isdst":False,
            "text":"(UTC+03:00) Kaliningrad, Minsk"
        },
        {
            "value":"Arab Standard Time",
            "abbr":"AST",
            "offset":3,
            "isdst":False,
            "text":"(UTC+03:00) Kuwait, Riyadh"
        },
        {
            "value":"E. Africa Standard Time",
            "abbr":"EAST",
            "offset":3,
            "isdst":False,
            "text":"(UTC+03:00) Nairobi"
        },
        {
            "value":"Iran Standard Time",
            "abbr":"IDT",
            "offset":4.5,
            "isdst":True,
            "text":"(UTC+03:30) Tehran"
        },
        {
            "value":"Arabian Standard Time",
            "abbr":"AST",
            "offset":4,
            "isdst":False,
            "text":"(UTC+04:00) Abu Dhabi, Muscat"
        },
        {
            "value":"Azerbaijan Standard Time",
            "abbr":"ADT",
            "offset":5,
            "isdst":True,
            "text":"(UTC+04:00) Baku"
        },
        {
            "value":"Russian Standard Time",
            "abbr":"RST",
            "offset":4,
            "isdst":False,
            "text":"(UTC+04:00) Moscow, St. Petersburg, Volgograd"
        },
        {
            "value":"Mauritius Standard Time",
            "abbr":"MST",
            "offset":4,
            "isdst":False,
            "text":"(UTC+04:00) Port Louis"
        },
        {
            "value":"Georgian Standard Time",
            "abbr":"GST",
            "offset":4,
            "isdst":False,
            "text":"(UTC+04:00) Tbilisi"
        },
        {
            "value":"Caucasus Standard Time",
            "abbr":"CST",
            "offset":4,
            "isdst":False,
            "text":"(UTC+04:00) Yerevan"
        },
        {
            "value":"Afghanistan Standard Time",
            "abbr":"AST",
            "offset":4.5,
            "isdst":False,
            "text":"(UTC+04:30) Kabul"
        },
        {
            "value":"West Asia Standard Time",
            "abbr":"WAST",
            "offset":5,
            "isdst":False,
            "text":"(UTC+05:00) Ashgabat, Tashkent"
        },
        {
            "value":"Pakistan Standard Time",
            "abbr":"PST",
            "offset":5,
            "isdst":False,
            "text":"(UTC+05:00) Islamabad, Karachi"
        },
        {
            "value":"India Standard Time",
            "abbr":"IST",
            "offset":5.5,
            "isdst":False,
            "text":"(UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi"
        },
        {
            "value":"Sri Lanka Standard Time",
            "abbr":"SLST",
            "offset":5.5,
            "isdst":False,
            "text":"(UTC+05:30) Sri Jayawardenepura"
        },
        {
            "value":"Nepal Standard Time",
            "abbr":"NST",
            "offset":5.75,
            "isdst":False,
            "text":"(UTC+05:45) Kathmandu"
        },
        {
            "value":"Central Asia Standard Time",
            "abbr":"CAST",
            "offset":6,
            "isdst":False,
            "text":"(UTC+06:00) Astana"
        },
        {
            "value":"Bangladesh Standard Time",
            "abbr":"BST",
            "offset":6,
            "isdst":False,
            "text":"(UTC+06:00) Dhaka"
        },
        {
            "value":"Ekaterinburg Standard Time",
            "abbr":"EST",
            "offset":6,
            "isdst":False,
            "text":"(UTC+06:00) Ekaterinburg"
        },
        {
            "value":"Myanmar Standard Time",
            "abbr":"MST",
            "offset":6.5,
            "isdst":False,
            "text":"(UTC+06:30) Yangon (Rangoon)"
        },
        {
            "value":"SE Asia Standard Time",
            "abbr":"SAST",
            "offset":7,
            "isdst":False,
            "text":"(UTC+07:00) Bangkok, Hanoi, Jakarta"
        },
        {
            "value":"N. Central Asia Standard Time",
            "abbr":"NCAST",
            "offset":7,
            "isdst":False,
            "text":"(UTC+07:00) Novosibirsk"
        },
        {
            "value":"China Standard Time",
            "abbr":"CST",
            "offset":8,
            "isdst":False,
            "text":"(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi"
        },
        {
            "value":"North Asia Standard Time",
            "abbr":"NAST",
            "offset":8,
            "isdst":False,
            "text":"(UTC+08:00) Krasnoyarsk"
        },
        {
            "value":"Singapore Standard Time",
            "abbr":"MPST",
            "offset":8,
            "isdst":False,
            "text":"(UTC+08:00) Kuala Lumpur, Singapore"
        },
        {
            "value":"W. Australia Standard Time",
            "abbr":"WAST",
            "offset":8,
            "isdst":False,
            "text":"(UTC+08:00) Perth"
        },
        {
            "value":"Taipei Standard Time",
            "abbr":"TST",
            "offset":8,
            "isdst":False,
            "text":"(UTC+08:00) Taipei"
        },
        {
            "value":"Ulaanbaatar Standard Time",
            "abbr":"UST",
            "offset":8,
            "isdst":False,
            "text":"(UTC+08:00) Ulaanbaatar"
        },
        {
            "value":"North Asia East Standard Time",
            "abbr":"NAEST",
            "offset":9,
            "isdst":False,
            "text":"(UTC+09:00) Irkutsk"
        },
        {
            "value":"Tokyo Standard Time",
            "abbr":"TST",
            "offset":9,
            "isdst":False,
            "text":"(UTC+09:00) Osaka, Sapporo, Tokyo"
        },
        {
            "value":"Korea Standard Time",
            "abbr":"KST",
            "offset":9,
            "isdst":False,
            "text":"(UTC+09:00) Seoul"
        },
        {
            "value":"Cen. Australia Standard Time",
            "abbr":"CAST",
            "offset":9.5,
            "isdst":False,
            "text":"(UTC+09:30) Adelaide"
        },
        {
            "value":"AUS Central Standard Time",
            "abbr":"ACST",
            "offset":9.5,
            "isdst":False,
            "text":"(UTC+09:30) Darwin"
        },
        {
            "value":"E. Australia Standard Time",
            "abbr":"EAST",
            "offset":10,
            "isdst":False,
            "text":"(UTC+10:00) Brisbane"
        },
        {
            "value":"AUS Eastern Standard Time",
            "abbr":"AEST",
            "offset":10,
            "isdst":False,
            "text":"(UTC+10:00) Canberra, Melbourne, Sydney"
        },
        {
            "value":"West Pacific Standard Time",
            "abbr":"WPST",
            "offset":10,
            "isdst":False,
            "text":"(UTC+10:00) Guam, Port Moresby"
        },
        {
            "value":"Tasmania Standard Time",
            "abbr":"TST",
            "offset":10,
            "isdst":False,
            "text":"(UTC+10:00) Hobart"
        },
        {
            "value":"Yakutsk Standard Time",
            "abbr":"YST",
            "offset":10,
            "isdst":False,
            "text":"(UTC+10:00) Yakutsk"
        },
        {
            "value":"Central Pacific Standard Time",
            "abbr":"CPST",
            "offset":11,
            "isdst":False,
            "text":"(UTC+11:00) Solomon Is., New Caledonia"
        },
        {
            "value":"Vladivostok Standard Time",
            "abbr":"VST",
            "offset":11,
            "isdst":False,
            "text":"(UTC+11:00) Vladivostok"
        },
        {
            "value":"New Zealand Standard Time",
            "abbr":"NZST",
            "offset":12,
            "isdst":False,
            "text":"(UTC+12:00) Auckland, Wellington"
        },
        {
            "value":"UTC+12",
            "abbr":"U",
            "offset":12,
            "isdst":False,
            "text":"(UTC+12:00) Coordinated Universal Time+12"
        },
        {
            "value":"Fiji Standard Time",
            "abbr":"FST",
            "offset":12,
            "isdst":False,
            "text":"(UTC+12:00) Fiji"
        },
        {
            "value":"Magadan Standard Time",
            "abbr":"MST",
            "offset":12,
            "isdst":False,
            "text":"(UTC+12:00) Magadan"
        },
        {
            "value":"Kamchatka Standard Time",
            "abbr":"KDT",
            "offset":13,
            "isdst":True,
            "text":"(UTC+12:00) Petropavlovsk-Kamchatsky - Old"
        },
        {
            "value":"Tonga Standard Time",
            "abbr":"TST",
            "offset":13,
            "isdst":False,
            "text":"(UTC+13:00) Nuku'alofa"
        },
        {
            "value":"Samoa Standard Time",
            "abbr":"SST",
            "offset":13,
            "isdst":False,
            "text":"(UTC+13:00) Samoa"
        }
    ]    
    return jsonify(data), 200    

app.run()
