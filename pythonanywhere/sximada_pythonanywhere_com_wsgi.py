import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'service_web.settings'
os.environ['DOTENV'] = '/home/sximada/.env'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
