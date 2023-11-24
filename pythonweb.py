#!C:/Python37/python

print ("Content-Type: text/html")

print()

import cgi

print("<h1>Welcome to Python</h1>")

print("<hr/>")

print ("<h1>Using input tag</h1>")

print("<body bgcolor='red'>")

form=cgi.FieldStorage ()

email=form.getvalue ("email")

password=form.getvalue ("password")

# check=form.getvalue ("check")

# gender=form.getvalue ("gender")

# hindi =form.getvalue("hindi")

# english =form.getvalue("english")
# urdu =form.getvalue("urdu")

# select1=form.getvalue("select")

import mysql.connector

con=mysql.connector.connect(user='root', password='',host='localhost', database='webpython')

cur= con.cursor()

cur.execute("insert into student values (%s, %s)", (email,password))

con.commit()

cur.close()

con.close()

print("<h3>record inserted successfully</h3>")
# print("<a href='http://localhost/mango/index.php'>click here to go back</a>")