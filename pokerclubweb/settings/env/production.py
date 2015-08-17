from .. import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        #'ENGINE':   'django.db.backends.mysql',
        'HOST':     'ec2-54-163-228-0.compute-1.amazonaws.com',
        'NAME':     'd3e3n97no6755j',
        'USER':     'thpigrkwjopqne',
        'PASSWORD': 'rYj19UP1spyJeAssvJVUR0I9Qa',
        'PORT':     5432,
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
    '.herokuapp.com'
)

CACHES['default']['KEY_PREFIX'] = 'pokerclubweb.production'

