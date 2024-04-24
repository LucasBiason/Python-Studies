from functools import wraps
from flask import g, request, redirect, url_for, session

import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    datefmt='[%d/%m/%y %H:%M:%S]',
    format='%(asctime)s [%(levelname)s] %(name)s '+
           '[%(funcName)s] [%(filename)s], %(lineno)s %(message)s'

)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'email' in session:
            return redirect('/sign-in')
        return f(*args, **kwargs)
    return decorated_function


def loggingroutes(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logging.debug(
            request.url + " : " +\
            str(request.remote_addr)+ " : " +\
            (session.get('email') or 'Not Auth')
        ) 
        return f(*args, **kwargs)
    return decorated_function