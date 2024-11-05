"""
WSGI config for blango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")
from blango.settings import Dev
from configurations.wsgi import get_wsgi_application
from configurations import values
application = get_wsgi_application()

class Prod(Dev):
  DEBUG = False
  SECRET_KEY = values.SecretValue()
  ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io"])


