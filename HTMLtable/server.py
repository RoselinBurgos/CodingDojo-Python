# Assignment: HTML Table
# Create the following tuple of dictionaries and have it available for your route. 

# users = (
#    {'first_name' : 'Michael', 'last_name' : 'Choi'},
#    {'first_name' : 'John', 'last_name' : 'Supsupin'},
#    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#    {'first_name' : 'KB', 'last_name' : 'Tonel'}
# );

# Pass users to your template and have your template output a beautiful HTML table.


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
);

    return render_template("index1.html",users=users)


if __name__ =="__main__":
    app.run(debug=True)  