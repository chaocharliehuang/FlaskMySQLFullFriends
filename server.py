from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriends')

@app.route('/')
def index():
    query = "SELECT CONCAT_WS(' ', first_name, last_name) AS 'name', age, DATE_FORMAT(created_at, '%M %D') AS month_day, YEAR(created_at) AS year FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/add_friend', methods=['POST'])
def add_friend():
    return redirect('/')

app.run(debug=True)