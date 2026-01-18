#Employee managemnet sytemym using python
import mysql.connector
#making connection
con = mysql.connector.connect(
    host="localhost", user="root", password="", database="employee")
mycursor=con.cursor()

mycursor.execute("CREATE DATABASE Employee")

