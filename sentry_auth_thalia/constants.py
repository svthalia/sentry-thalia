from __future__ import absolute_import, print_function

from django.conf import settings

API_DOMAIN = getattr(settings, 'THALIA_API_DOMAIN', 'http://192.168.5.201:8000')
API_SECRET = getattr(settings, 'THALIA_API_SECRET', '')
