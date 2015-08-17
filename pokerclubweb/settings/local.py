"""
Local settings for development.
"""
from .project import INSTALLED_APPS, MIDDLEWARE_CLASSES

# Output to console
import logging, sys
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'zildjian843'
EMAIL_HOST_PASSWORD = 'stalejungleinvent'
DEFAULT_FROM_EMAIL = 'zildjian843@gmail.com'

# Debugging assistance

WSGI_APPLICATION = 'pokerclubweb.wsgi.development.application'

INSTALLED_APPS += (
    #'debug_toolbar',
    #'django_extensions',
    'debugtools',
)

MIDDLEWARE_CLASSES += (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'debugtools.middleware.XViewMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

DEBUG_TOOLBAR_PANELS = (
    #'debug_toolbar.panels.version.VersionDebugPanel',
    #'debug_toolbar.panels.timer.TimerDebugPanel',
    #'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    #'debug_toolbar.panels.headers.HeaderDebugPanel',
    #'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    #'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
