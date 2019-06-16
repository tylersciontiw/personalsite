import dj_database_url
import pymysql
from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 
	'localhost',
    '.pythonanywhere.com'
]

SECRET_KEY = get_env_variable("SECRET_KEY")

