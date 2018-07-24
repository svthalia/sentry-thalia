from __future__ import absolute_import, print_function

from requests.exceptions import RequestException
from sentry import http
from sentry.utils import json

from .constants import API_URL, API_SECRET


class ThaliaApiError(Exception):
    def __init__(self, message='', status=0):
        super(ThaliaApiError, self).__init__(message)
        self.status = status


class ThaliaClient(object):
    def __init__(self):
        self.http = http.build_session()

    def _headers(self, token):
        headers = {
            'Accept-Language': 'en-GB'
        }
        if token:
            headers['Authorization'] = 'Token {0}'.format(token)
        return headers

    def _get(self, path, token=None, params={}):
        try:
            req = self.http.get(
                '{0}/{1}'.format(API_URL, path.lstrip('/')),
                params=params,
                headers=self._headers(token),
            )
        except RequestException as e:
            raise ThaliaApiError(
                unicode(e), status=getattr(e, 'status_code', 0)
            )

        try:
            content = json.loads(req.content)
        except ValueError:
            raise ThaliaApiError(req.content, status=0)

        if req.status_code < 200 or req.status_code >= 300:
            raise ThaliaApiError(content, status=req.status_code)

        return content

    def _post(self, path, token=None, params={}, payload={}):
        try:
            req = self.http.post(
                '{0}/{1}'.format(API_URL, path.lstrip('/')),
                params=params,
                data=payload,
                headers=self._headers(token),
            )
        except RequestException as e:
            raise ThaliaApiError(
                unicode(e), status=getattr(e, 'status_code', 0)
            )

        try:
            content = json.loads(req.content)
        except ValueError:
            raise ThaliaApiError(req.content, status=0)

        if req.status_code < 200 or req.status_code >= 300:
            raise ThaliaApiError(content, status=req.status_code)

        return content

    def authenticate(self, username, password):
        return self._post('/api/v1/token-auth', payload={
            'username': username,
            'password': password
        })

    def get_user(self, auth_token):
        return self._get('/api/v1/sentry-access', auth_token, params={
            'secret': API_SECRET
        })
