from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="localhost", user="root", password="root", database="registration", auth_plugin='mysql_native_password')
cursor = conn.cursor()
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('phone_number')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `user` WHERE `Phone_Number` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    users = cursor.fetchall()
    if len(users)>0:
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    date = request.form.get('date')
    phone_number = request.form.get('phone number')
    passport_number = request.form.get('passport number')
    email_id = request.form.get('email')
    password = request.form.get('password')
    file = request.form.get('file')

    cursor.execute("""INSERT INTO `user` (`Full_Name`, `Date_of_Birth`, `Phone_Number`,
                    `Passport_Number`, `Email_ID`, `Password`, `UserImage`) VALUES
                    ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
                   .format(name,date,phone_number,passport_number,email_id,password,file))
    conn.commit()
    return "user registered successfully"


if __name__=="__main__":
    app.run(debug=True)