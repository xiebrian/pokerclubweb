from .. import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'mitpokerexec'
EMAIL_HOST_PASSWORD = 'fiveofakind'
DEFAULT_FROM_EMAIL = 'mitpokerexec@gmail.com'

DATABASES = {
    'default': {
        # Choose between PostgreSQL or MySQL:
        #'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'ENGINE':   'django.db.backends.mysql',
        'HOST':     'sql.mit.edu',
        'NAME':     'poker+pokerclubweb',
        'USER':     'poker',
        'PASSWORD':     'jaf50bew',
        #'PORT':     5432,
    },
}

WSGI_APPLICATION = 'pokerclubweb.wsgi.production.application'

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
    '.mit.edu'
)

CACHES['default']['KEY_PREFIX'] = 'pokerclubweb.production'

COMPRESS_OFFLINE = False

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'web/static'),
# )
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATIC_URL = '/pokerclubweb/web/static/'
MEDIA_URL = '/pokerclubweb/web/media/'
