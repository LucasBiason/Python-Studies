
import flask
import docker
from services import decorators

blueprint = flask.Blueprint('docker', __name__)
connection = docker.DockerClient()

@blueprint.route('/docker', methods=[ 'GET' ])
@decorators.login_required
@decorators.loggingroutes
def get_docker():    

    try:
        lista_dockers = connection.containers.list(all=True)
    except Exception as msg:
        ## Dentro do container não vai rodar pois não colocamos o Docker dentro
        # ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
        print(msg)
        lista_dockers = []

    context = {
        'page': 'docker',
        'route': {
            'is_public': False
        },
        'containers': lista_dockers
    }

    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start/<string:short_id>/', methods=[ 'GET' ])
@decorators.login_required
@decorators.loggingroutes
def start_docker(short_id):
    container = connection.containers.get(short_id)
    if container and container.status != 'running':
        container.start()
        flask.flash("Container Iniciado", "success")
    elif not container:
        flask.flash("Container não Encontrado", "danger")
    else:
        flask.flash("Container já está iniciado", "danger")

    return flask.redirect('/docker')

@blueprint.route('/docker/stop/<string:short_id>/', methods=[ 'GET' ])
@decorators.login_required
@decorators.loggingroutes
def stop_docker(short_id):
    container = connection.containers.get(short_id)
    if container and container.status == 'running':
        container.stop()
        flask.flash("Container Encerrado", "success")
    elif not container:
        flask.flash("Container não Encontrado", "danger")
    else:
        flask.flash("Container já está encerrado", "danger")

    return flask.redirect('/docker')
