
from flask import Flask, render_template, request,  jsonify
import datetime
import mysql.connector
from flask_mysqldb import MYSQL
import MySQLdb.cursors
from requests import request
import mysql

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mayuresh'
app.config['MYSQL_DB'] = 'user_details'

mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET']) # To render Homepage
def index1():
    if request.method == 'POST' and 'name' in request.form and  'age' in request.form and 'txtPANCard' in request.form and'phone' in request.form  and 'address' in request.form and 'city' in request.form and 'state' in request.form:
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        txtPANCard = request.form['txtPANCard ']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO user details WHERE name = % s AND age = % s AND phone = % s AND txtPANCard = % s AND address = % s AND city = % s AND state = % s', (name, age, phone, txtPANCard, address, city, state, ))
        mysql.connection.commit()
        cur.close()
    return render_template('index1.html')

def user_deatils():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM user details')
    transaction = cursor.fetchall()
    for i in transaction:
        print(i)
user_deatils()


def alloted_limit():
    AL = 100000
    print(AL)
alloted_limit()

@app.route('/index2/', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST' and 'Loan Amount' in request.form and 'Duration of Loan' in request.form and  'rate of intrest' in request.form and 'Transaction Date' in request.form :
        Loan_Amount = request.form['Loan Amount']
        Duration_of_Loan = request.form['Duration of Loan']
        rate_of_intrest = request.form['rate of intrest']
        Transaction_Date = request.form['Transaction Date']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO transaction , ( Loan_Amount, Duration_of_Loan, rate_of_intrest, Transaction_Date))
        mysql.connection.commit()
        cur.close()
    return  render_template('index2.html')


@app.route('/result/', methods=['GET', 'POST'])# This will be called from UI
def Interest_amount():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM transaction')
    transaction = cursor.fetchall()

    P = int(transaction['Loan Amount']),
    T = float(transaction['Duration of Loan']),
    R = float(transaction['rate of intrest'])

    Interest= (P * R * T) / 100
    print( Interest)
Interest_amount()

def last_date_dt():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT Transaction Date FROM transaction')
        transaction = cursor.fetchone()
        first_date = transaction['Transaction Date'],
        first_date_dt = datetime.datetime.strptime(first_date, '%d/%m/%Y'),
        lastdate = first_date_dt + datetime.timedelta(days=180),
        datetime.datetime.strftime(lastdate, '%d/%m/%Y')
        print( lastdate)
last_date_dt()

def final_amount():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM transaction')
    transaction = cursor.fetchall()
    P = int(transaction['Loan Amount']),
    I = int(transaction['Interest_amount']),
    A = P + I,
    r = R / 100,
    R = r * 100,
    T = int(request.form['Duration of Loan'])

    Finalamount = P(1 + r*T)
    print(finalamount)
final_amount()



if __name__ == '__main__':
    app.run(debug=True)


























