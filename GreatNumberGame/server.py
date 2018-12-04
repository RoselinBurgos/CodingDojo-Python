from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random
random.randrange(0,101)


@app.route('/')
def index():

    if 'setnumber' not in session:
        session['setnumber'] = random.randrange(0,101)
        print(session['setnumber'])
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def stuff():
    new = ""
    boxcolor=""
    newbutton=""
    guess = request.form['guess']

    if session['setnumber'] > int(request.form['guess']): 
        new = "Too low" 
        boxcolor= "pink"
    
    if session['setnumber'] < int(request.form['guess']): 
        new ="Too High"
        boxcolor = "red"
        
    if session['setnumber'] == int(request.form['guess']):  
        new ="You guessed it!"
        boxcolor="green"
        newbutton = '<a href ="/"><button class="bton2" type="button">Play Again</button></a>'
        session.clear()
    
    return render_template('index.html',new=new, boxcolor=boxcolor,newbutton=newbutton)
       
    

if __name__=="__main__":   
    app.run(debug=True)    