import pymysql
from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [ 
	'localhost',
    '.pythonanywhere.com'
]

SECRET_KEY = get_env_variable("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tylersciontipersonal$tylersciontipers$website',
        'USER': 'tylersciontipers',
        'PASSWORD': 'Dutch2002',
        'HOST': 'tylersciontipersonal.mysql.pythonanywhere-services.com',
    }
}
