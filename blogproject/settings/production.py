from blogproject.settings.common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '.aiwan.press', '144.34.167.216']