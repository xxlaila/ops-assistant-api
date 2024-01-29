"""
WSGI config for OpsAssistantApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
envir = os.getenv("ENV", "test")  # dev/test/pro

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpsAssistantApi.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = f'OpsAssistantApi.settings.{envir}'

application = get_wsgi_application()
