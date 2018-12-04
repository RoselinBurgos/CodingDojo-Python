# Assignment: Checkerboard
# Write a program that generates an HTML page that looks like a checkerboard.

# Your program should have the following output

# http://localhost:5000 - should display 8 by 8 checkerboard
# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard. 


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<x>/<y>")
def page2(x,y):
    timesx = int(x)
    timesy = int(y)
    return render_template("index2.html", timesx=timesx, timesy=timesy )

if __name__ =="__main__":
    app.run(debug=True)   