import mysql.connector
import bcrypt
from flask import Flask
import pygeoip, requests, json
import urllib.request as req

app = Flask(__name__)
app.secret_key = "Asecretkeythatiknow"
#establishing the connection
conn = mysql.connector.connect(
   user='M00728678Jyoti',password='Beingrishav10', host='127.0.0.1', database='M00728678Jyoti')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
email = "Jyotipriya"
password = "BeingJyotipriya10"
# Preparing SQL query to INSERT a record into the database.

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
p = "BeingJyotipriya10"

ip_addr = requests.get('https://api.ipify.org').text
location = requests.get('http://genesismachine.uk:8090/stats').text
devices = requests.get('http://genesismachine.uk:8090/devices').text



try:
   # Executing the SQL command
   cursor.execute("INSERT INTO Userss (username, password) VALUES(%s, %s)",(email, hashed))

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

if bcrypt.checkpw(p.encode('utf-8'), hashed):
    print (f'Logged in, Welcome {email}!')

# Closing the connection
conn.close()


if __name__ == "__main__":
    app.run(host='genesismachine.uk', port='8090')
