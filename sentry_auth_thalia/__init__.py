from __future__ import absolute_import

from sentry.auth import register

from .provider import ThaliaAuthProvider

register('thalia', ThaliaAuthProvider)
