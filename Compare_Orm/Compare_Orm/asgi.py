"""
ASGI config for Compare_Orm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django_tortoise import get_boosted_asgi_application  # first line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

application = get_asgi_application()

# get_boosted_asgi_application function monkey patch all registered apps models;
# each model will has abjects attribute (the objects attribute was not modified),
# which is a Tortoise model actually
application = get_boosted_asgi_application(application)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Compare_Orm.settings')

#application = get_asgi_application()
