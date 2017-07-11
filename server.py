from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriends')

@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

app.run(debug=True)