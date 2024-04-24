
import sys
import os

import flask
import ldap3

import blueprints.auth
import blueprints.docker
import blueprints.gitlab
import blueprints.jenkins

from datetime import datetime

app = flask.Flask(__name__)
app.secret_key = 'SECRET_KEY'

app.register_blueprint(blueprints.auth.blueprint)
app.register_blueprint(blueprints.docker.blueprint)
app.register_blueprint(blueprints.gitlab.blueprint)
app.register_blueprint(blueprints.jenkins.blueprint)

@app.route('/')
def index():
    return flask.redirect('/docker')
    

@app.template_filter('dt')
def filter_datetime(date, fmt=None):
    date = date.split('.')[0]
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    native = date.replace(tzinfo=None)
    format='%b %d, %Y'
    return native.strftime(format) 

if __name__ == '__main__':

    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    app.run(host='0.0.0.0',debug=True)
    