from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("What is your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Welcome " + str(request.form['name_input']) + ", We are glad you are here!")
	return render_template("index.html")

