from __future__ import absolute_import, print_function

from sentry.models import AuthIdentity
from sentry.auth.exceptions import IdentityNotValid
from sentry.auth import Provider

from .views import UserAuthView, ThaliaConfigureView
from .client import ThaliaClient, ThaliaApiError


class ThaliaAuthProvider(Provider):
    name = 'Thalia'

    def get_auth_pipeline(self):
        return [UserAuthView()]

    def get_configure_view(self):
        return ThaliaConfigureView.as_view()

    def build_identity(self, state):
        user_data = state['user']

        # Secretly update email and name on identity build,
        # since Sentry doesn't do this for us
        if AuthIdentity.objects.filter(
                ident=user_data['pk'],
                auth_provider__provider='thalia'
        ).exists():

            identity = AuthIdentity.objects.get(
                ident=user_data['pk'],
                auth_provider__provider='thalia'
            )

            identity.user.update(
                name=u'{} {}'.format(
                    user_data['first_name'],
                    user_data['last_name']
                ),
                email=user_data['email']
            )

        return {
            'id': user_data['pk'],
            'email': user_data['email'],
            'email_verified': True,
            'name': u'{} {}'.format(
                user_data['first_name'],
                user_data['last_name']
            ),
            'data': {
                'auth_token': state['auth_token']
            }
        }

    def refresh_identity(self, auth_identity):
        client = ThaliaClient()
        try:
            user_data = client.get_user(auth_identity.data['auth_token'])

            auth_identity.user.update(
                name=u'{} {}'.format(
                    user_data['first_name'],
                    user_data['last_name']
                ),
                email=user_data['email']
            )
        except ThaliaApiError as e:
            raise IdentityNotValid(e.message)

    def build_config(self, state):
        return {}
