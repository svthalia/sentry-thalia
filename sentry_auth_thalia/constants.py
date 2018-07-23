from __future__ import absolute_import, print_function

from django.conf import settings

API_DOMAIN = getattr(settings, 'THALIA_API_DOMAIN', '')
API_SECRET = getattr(settings, 'THALIA_API_SECRET', '')
