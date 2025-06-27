"""
WSGI config for prop_shoppe project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

# NEW: run migrations automatically on startup
from django.core.management import call_command
call_command('migrate')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prop_shoppe.settings')

application = get_wsgi_application()
