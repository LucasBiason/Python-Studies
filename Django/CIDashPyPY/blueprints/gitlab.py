
import flask
import requests
from services.decorators import login_required

blueprint = flask.Blueprint('gitlab', __name__)

TOKEN = 'yBmBw5Zy-kW5m54P5hmR'
DOMAIN = 'https://gitlab.com/api/v4'
PROJECTS_URL = DOMAIN + '/projects?owned=True&private_token=' + TOKEN
PROJECT_URL = DOMAIN + '/projects/{}/?private_token=' + TOKEN
COMMITS_URL = DOMAIN + '/projects/{}/repository/commits/?private_token=' + TOKEN

@blueprint.route('/gitlab', methods=[ 'GET' ])
@login_required
def get_gitlab():
    res = requests.get(PROJECTS_URL)
    context = {
        'page': 'gitlab',
        'current_tab': flask.request.args.get('current_tab') or 'users',
        'route': {
            'is_public': False
        },
        'projects': res.json()
    }

    return flask.render_template('gitlab.html', context=context)


@blueprint.route('/gitlab/<string:project_id>/commits/', methods=[ 'GET' ])
@login_required
def get_commits(project_id):
    project = requests.get(PROJECT_URL.format(project_id))
    print(COMMITS_URL.format(project_id))
    res = requests.get(COMMITS_URL.format(project_id))
    print(res.json())
    context = {
        'page': 'gitlab',
        'current_tab': flask.request.args.get('current_tab') or 'users',
        'route': {
            'is_public': False
        },
        'project': project.json(),
        'commits': res.json()
    }

    return flask.render_template('gitlab_commits.html', context=context)


@blueprint.route('/gitlab', methods=[ 'POST' ])
def post_gitlab():
    pass