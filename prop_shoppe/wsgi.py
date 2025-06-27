"""
WSGI config for prop_shoppe project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prop_shoppe.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
