from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'TheSecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    passFlag = True
    if len(request.form['name']) ==0:
        flash('Invalid first name')

    if not request.form['name'].isalpha():
        flash('First name has non-alpha character')
        passFlag = False

    if len(request.form['lastname']) < 1:
        flash('Invalid last name')
        passFlag = False

    if not request.form['lastname'].isalpha():
        flash('Last name has a non-alpha character')
        passFlag = False

    if len(request.form['email']) < 1:
        flash('Invalid email')
        passFlag = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email format')
        passFlag = False

    if len(request.form['password']) < 8:
        flash('Password must contain at least 8 characters', 'wrong')
        passFlag = False

    if request.form['password'] != request.form['c_password']:
        flash('Password does not match')
        passFlag = False

    if passFlag == False:
        return redirect('/')
    else:
        return render_template("index2.html")
        

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)