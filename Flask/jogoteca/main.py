import flask
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

# run the application
if __name__ == "__main__":
    from views import *
    app.run(debug=True)

