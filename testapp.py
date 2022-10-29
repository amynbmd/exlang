
from flask import Flask, Response, jsonify, make_response, render_template, request, flash
from flask_cors import CORS
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user
import sqlite3 
import os
from flask_bcrypt import Bcrypt
import jsonpickle

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

class User:
    name = None
    email = None
    password = None
    profile = Profile()


#------------------------------------------TO-DO------------------------------------------#
# Please create a new user profile table in database, retrieve profile for this particular user and then map it to an object. Hardcode values below is for testing purposes only.
def getUserProfile(email):
    profile = Profile()
    if (email == "existingUser@email.com"):
        profile.wordofTheDay = "obfuscate"
        profile.isOnline = True
        profile.countryCode = "US"
        profile.picURL = ""
        profile.bio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        profile.nativeLang = "en"
        profile.learningLang = ["vi", "de", "fr"]
        profile.level = "Beginner"
        profile.interests = ["Art", "Movies", "Organizing"]
        profile.email = email

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
CORS(app)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'exlang'
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

    user = getUserByEmail(email)

    # Only try to register user if email is NOT in use.
    if (user.email is None):
        connection = sqlite3.connect(currentdirectory + "\ExLang.db")
        cursor = connection.cursor()
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        query1 = "INSERT INTO user VALUES ('{name}', '{email}', '{password}')".format(name = name, email = email, password = pw_hash)
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
#Retrieve user profile by email address and return as JSON
#Example: http://127.0.0.1:5000/user/profile
@app.route("/user/profile", methods=['POST'])
def update_user_profile():
    # data is in the following json format: {'countryCode': 'AL', 'nativeLang': 'af', 'learningLangs': ['af', 'ak', 'sq', 'fy', 'yi', 'yo', 'za'], 'level': 'Intermediate', 'interest': 'art, history, math'}
    # split interest by comma and store as array
    
    print(request.get_json())

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
app.run()