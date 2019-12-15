from connexion.resolver import RestyResolver
from flask import render_template, request, redirect, url_for
import connexion

app = connexion.App(__name__, host='localhost', port=8080, specification_dir='swagger/')
app.add_api('my_app.yaml', resolver=RestyResolver('api'))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/getOne/")
def getone():
    return render_template("getOne.html")


@app.route("/getonecontrol")
def getonecontrol():
    lname = request.form['lastname']
    return redirect(url_for('api/items/' + lname))


if __name__ == '__main__':
    app.run(debug=True)
