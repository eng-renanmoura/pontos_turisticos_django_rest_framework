"""
WSGI config for pontos_turisticos_django_rest_framework project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pontos_turisticos_django_rest_framework.settings')

application = get_wsgi_application()
