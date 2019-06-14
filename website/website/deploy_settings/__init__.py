import dj_database_url

from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 
	'localhost',
    '.pythonanywhere.com'
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database.url.config()
DATABSES["default"].update(db_from_env)
