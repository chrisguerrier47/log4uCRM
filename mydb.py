import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE log4U")

print("All Done!")

