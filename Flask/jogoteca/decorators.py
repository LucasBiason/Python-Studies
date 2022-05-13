import flask
from functools import wraps

def login_required(f, *args, **kwarg):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        proxima = str(flask.request.path)
        if not 'usuario_logado' in flask.session\
            or flask.session['usuario_logado'] == None:
            return flask.redirect(
                flask.url_for('login') + '?proxima=' + proxima
            )
        return f(*args, **kwargs)
    
    return decorated_function