from flask import *

app = Flask(__name__)

@app.route("/")
def f1():
	return render_template("a.html")

@app.route("/home")
def f2():
	return render_template("b.html",sname="Rya",sdept="CS")

# <variable> - input operator in flask
@app.route("/aboutus/<user_city>")
def f3(user_city):
	return render_template("c.html",city=user_city)


if __name__ == '__main__':
	app.run(debug=True)