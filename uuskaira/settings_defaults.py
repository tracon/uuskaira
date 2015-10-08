import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def mkpath(*parts):
    return os.path.join(BASE_DIR, *parts)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'form_designer',
    'uuskaira',
    'kompassi_oauth2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'kompassi_oauth2.backends.KompassiOAuth2AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

ROOT_URLCONF = 'uuskaira.urls'

WSGI_APPLICATION = 'uuskaira.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'uuskaira.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'celery': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True
        },
        'uuskaira': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True
        },
    }
}

LANGUAGE_CODE = 'fi-fi'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = mkpath('static')

LOGIN_URL = '/oauth2/login'
LOGOUT_URL = '/logout'
