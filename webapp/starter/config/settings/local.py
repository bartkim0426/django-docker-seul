import os

from .partials import *


DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ['127.0.0.1', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_NAME'],
        'USER': os.environ["POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': os.environ["POSTGRES_HOST"],
        'PORT': os.environ["POSTGRES_PORT"],
    }
}

MEDIA_ROOT = str(ROOT_DIR('mediafiles'))
# before collectstatic
# for prevent duplication of STATIC_ROOT and STATICFILES_DIRS
# STATIC_ROOT = str(ROOT_DIR('staticfiles'))
# STATICFILES_DIRS = (
#     str(ROOT_DIR.path('static')),
# )

# after collectstatic
STATIC_ROOT = str(ROOT_DIR('static-files'))
STATICFILES_DIRS = (
    str(ROOT_DIR.path('staticfiles')),
)
