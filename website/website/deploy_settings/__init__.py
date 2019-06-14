from ..settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 
	'localhost',
    '.pythonanywere.com'
]

SECRET_KEY = get_env_variable("SECRET_KEY")

STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"