"""
WSGI config for wxcloudrun project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import jd

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wxcloudrun.settings')

appkey = os.getenv('JD_APP_KEY', '')
secret = os.getenv('JD_SECRET_KEY', '')

jd.setDefaultAppInfo(appkey, secret) # only need to init one time

application = get_wsgi_application()
