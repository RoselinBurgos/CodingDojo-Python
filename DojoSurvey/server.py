# Assignment: Dojo Survey
# Build a flask application that accepts a form submission and presents the submitted data on a results page.

# When you build this, please make sure that your program meets the following criteria:

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
# http://localhost:5000/result - have this display a html with the information that was submitted by POST


from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result',  methods=['POST'])
def resultpage():
    name = request.form["your_name"]
    location = request.form["dojo_location"]
    language = request.form["favorite_language"]
    comment = request.form["your_comment"]
    return render_template("index2.html",name=name,location=location,language=language,comment=comment)


if __name__=="__main__":
    app.run(debug=True) 