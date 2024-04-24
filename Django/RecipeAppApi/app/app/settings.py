import os, json
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'yzp61)0ym6zi2i-@zsrq57q#2f%3vdzyxl46h3==x&c-q63&v8'

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS') or config('ALLOWED_HOSTS')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'user',
    'recipe'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST') or config('DB_HOST') or 'localhost',
        'NAME': os.environ.get('DB_NAME') or config('DB_NAME'),
        'USER': os.environ.get('DB_USER') or config('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS') or config('DB_PASS'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': json.loads(
            os.getenv('DATABASE_OPTIONS', '{}')
        ),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'core.User'

STATIC_URL = '/static/'
STATIC_ROOT = '/vol/web/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/vol/web/media'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

