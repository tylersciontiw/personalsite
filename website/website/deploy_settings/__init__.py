import dj_database_url
import pymysql

pymysql.install_as_MySQLdb()

from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 
	'localhost',
    '.pythonanywhere.com'
]

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES["default"].update(db_from_env)
