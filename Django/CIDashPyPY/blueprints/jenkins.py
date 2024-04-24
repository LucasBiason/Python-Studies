import flask
import jenkins
from services.decorators import login_required

j = jenkins.Jenkins('http://localhost:8080', 'username', 'senha')

blueprint = flask.Blueprint('jenkins', __name__)

@blueprint.route('/jenkins', methods=[ 'GET' ])
@login_required
def get_jenkins():
    try:
        jobs_list = j.get_jobs()
        jobs = []
        for job in jobs_list:
            jobs.append(j.get_job_info(job['fullname']))
    except:
        jobs = []
        
    context = {
        'page': 'jenkins',
        'route': {
            'is_public': False
        },
        'jobs': jobs
    }

    return flask.render_template('jenkins.html', context=context)


@blueprint.route('/jenkins/build/<string:jobname>', methods=[ 'GET' ])
def get_jenkins_build(jobname):
    j.build_job(jobname)
    return flask.redirect('/jenkins')

@blueprint.route('/jenkins', methods=[ 'POST' ])
def post_jenkins():
    pass

@blueprint.route('/jenkins/update/<string:jobname>', methods=[ 'GET' ])
def get_jenkins_update(jobname):
    
    context = {
        'page': 'jenkins-update',
        'route': {
            'is_public': False
        },
    }

    return flask.render_template('jenkins_update.html', context=context)

@blueprint.route('/jenkins', methods=[ 'POST' ])
def post_jenkins_update():
    pass


    ##// j.get_whoami()
    ## j.create_job('new-pipeline', jenkins.EMPTY_CONFIG_XML) (para criar)