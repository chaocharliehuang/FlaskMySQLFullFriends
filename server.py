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
    data = {
        'first_name': request.form['name'].split()[0],
        'last_name': request.form['name'].split()[1],
        'age': request.form['age'],
    }
    insert_query = "INSERT INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    mysql.query_db(insert_query, data)
    return redirect('/')

app.run(debug=True)