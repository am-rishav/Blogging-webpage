import mysql.connector
import bcrypt
from flask import Flask
import urllib.request as req

app = Flask(__name__)
app.secret_key = "thisisasecretkeyofdaniel"
#establishing the connection
conn = mysql.connector.connect(
   user='M00736585Danie',password='testM007', host='127.0.0.1', database='M00736585Danie')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
email = "Daniel3"
password = "testM007"
# Preparing SQL query to INSERT a record into the database.

hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())




try:
   # Executing the SQL command
   cursor.execute("INSERT INTO Users (username, password) VALUES(%s, %s)",(email, hashed))

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()


# Closing the connection
conn.close()


if __name__ == "__main__":
    app.run(host='genesismachine.uk', port='8090')
