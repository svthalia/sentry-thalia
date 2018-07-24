from __future__ import absolute_import, print_function

from django.conf import settings

API_URL = getattr(settings, 'THALIA_API_URL', '')
API_SECRET = getattr(settings, 'THALIA_API_SECRET', '')
