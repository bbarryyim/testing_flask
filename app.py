from connexion.resolver import RestyResolver
from flask import render_template
import connexion

app = connexion.App(__name__, host='localhost', port=8080, specification_dir='swagger/')
app.add_api('my_app.yaml', resolver=RestyResolver('api'))

@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:8080/

    :return: the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
