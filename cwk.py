from flask import Flask, request, url_for, redirect, flash, session, render_template
import os
from mysql.connector import errorcode
import mysql.connector
import bcrypt
import requests



app = Flask(__name__)
#Secret key is set to securely store cookies
app.secret_key = "asecretkeythatishouldknow"


#Storing files in a particular path in server
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


#connecting to the database containing login details
try:
    #placing credentials
  mydb = mysql.connector.connect(user='M00736585Danie',password='testM007', host='127.0.0.1', database='M00736585Danie')
  #If details are incorrect, it will prompt the following error message
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


#Processing individual rows returned by the database
mycursor = mydb.cursor()

#Selecting all the info from Table Users and storing it in myresults
mycursor.execute("SELECT * FROM Users")
myresult = mycursor.fetchall()


#assigning the data received from database using this class
class User:
    def __init__(self, username, password):

        self.username = username
        #self.password = password

        #Encoding the password with utf-8 since this will be encrypted
        self.password = password.encode('utf-8')

    def __repr__(self):
        return f'<User: {self.username}>'

#Storing the credentials received into this array
users = []
for x in myresult:
    users.append(User(username= x[0], password= x[1]))

ipaddress = requests.get('https://api.ipify.org').text


#Homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    #Opening the html document for this page using render_template
    return render_template('cwkhome2.html')

#about page
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        #Removing the previous automatically
        session.pop('user_id', None)

        #Fetching the credentials entered by the user in the page
        username = request.form['username']
        password = request.form['password']

        #Checking for that particular user in that database
        user = [x for x in users if x.username == username][0]

        #If there us no such user, it fill prompt the message
        if not user:
            return 'User Not Found!', 404

        #Encrypting the user-entered password and tallying it wih the one in Database
        #for the corresponding user
        if bcrypt.checkpw(password.encode('utf-8'), user.password):
            print("Login successful")



            #Rendering the html page depending on the logged in user
            if username == 'Daniel':
                return redirect(url_for('profile'))
            elif username == 'Daniel2':
                return redirect(url_for('profile2'))
            elif username == 'Daniel3':
                return redirect(url_for('profile3'))
        else:
            #If password is wrong it will flash a messege which is encrypted with our
            #secret key
            flash("Your login details are incorrect. Please try again")
            return redirect(url_for('home'))
    return render_template('cwlogin.html')


@app.route('/Daniel', methods=['GET', 'POST'])
def profile():

    return render_template('anthony.html', blog = request.form['text'])

@app.route('/Daniel2', methods=['GET', 'POST'])
def profile2():

    return render_template('rishav.html', ipaddress = requests.get('https://api.ipify.org').text)

@app.route('/Daniel3', methods=['GET', 'POST'])
def profile3():

    return render_template('jyotipriya.html', ipaddress = requests.get('https://api.ipify.org').text)


@app.route("/upload", methods=['POST'])
def upload():
    #path for storing the images in the server
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    #If path doesnt already eist then create a new directory
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

#Specifying the host and port so the flask can be running here
if __name__ == "__main__":
    app.run(host='genesismachine.uk', port='8097')



#Closing the cursor and database connection
mycursor.close()
mydb.close()
