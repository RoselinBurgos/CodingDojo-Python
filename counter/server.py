from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroypage():
    session.clear()
    return redirect('/')

@app.route('/addtwo',methods=['POST'])
def addtwopage():
    if request.form['button'] == 'add2':
        session['count'] +=1
    if request.form['button'] == 'clear':
        session['count'] = 0
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    