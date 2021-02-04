from blogproject.settings.common import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = True
ALLOWED_HOSTS = ['*']