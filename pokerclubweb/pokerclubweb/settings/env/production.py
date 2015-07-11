from .. import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        #'ENGINE':   'django.db.backends.mysql',
        'NAME':     'pokerclubweb',
        'USER':     'pokerclubweb',
        'PASSWORD': '',
        'OPTIONS':  {'autocommit': True,},   # Stop that "current transaction is aborted" error in PostgreSQL
    },
}

RAVEN_CONFIG = {
    'dsn': '',
}

INSTALLED_APPS += (
    #'raven.contrib.django.raven_compat',
    #'gunicorn',
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

ALLOWED_HOSTS = (
    '.pokerclubweb.tld',
    '.pokerclubweb.tld.',
)

CACHES['default']['KEY_PREFIX'] = 'pokerclubweb.production'

