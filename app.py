import os
import uuid, hashlib, MySQLdb, MySQLdb.cursors, logging
from flask import Flask, session, render_template, request, redirect, url_for, jsonify, json
#from flask.ext.login import LoginManager, UserMixin, login_required

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create the application object
app = Flask(__name__)

#login_manager = LoginManager()
#login_manager.init_app(app)

app.config['SECRET_KEY'] = 'SecretKey'
app.secret_key = os.urandom(24).encode('hex')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['LoginUsername']
    userPass = request.form['LoginPassword']
    logger.info(username + " " + userPass)
    isValid = userLogin(username, userPass)
    if (isValid == 1):
        return home()
    else:
        return idk()


# use decorators to link the function to a url
@app.route('/')
def idk():
    return render_template('Login.html')  # return a string

@app.route('/home')
def home():
    return render_template('Home.html')  # render a template
    
@app.route('/upload_spreadsheet')
def upload_spreadsheet():
    return render_template('Upload-Spreadsheet.html')

@app.route('/choose_calculation')
def choose_calculation():
    return render_template('Choose-Calculation.html')
    
@app.route('/view_documents')
def view_documents():
    return render_template('View-Documents.html')

def userLogin(username, password):
    logger.info("Validating username/password")
    validusername = "admin"
    validpassword = "password"
    if ((username == validusername) and (password == validpassword)):
        return 1
    else:
        return 0

# start the server with the 'run()' method
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
