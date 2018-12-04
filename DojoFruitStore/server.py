from flask import Flask, render_template, request, redirect
app = Flask(__name__)  
import datetime

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    name = request.form["first_name"]
    last = request.form["last_name"]
    stu = request.form["student_id"]
    strawberry = request.form["strawberry"]
    raspberry = request.form["raspberry"]
    apple = request.form["apple"]
    blackberry = request.form["blackberry"]
    now= datetime.datetime.now()
    date= now.strftime("%c")

    print(request.form)
    return render_template("checkout.html",name=name,last=last,stu=stu,strawberry=strawberry,raspberry=raspberry,apple=apple,blackberry=blackberry,date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    