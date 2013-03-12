"""
XING OAuth support

No extra configurations are needed to make this work.
"""
from social.utils import parse_qs
from social.backends.oauth import BaseOAuth1
from social.exceptions import AuthCanceled, AuthUnknownError


class XingOAuth(BaseOAuth1):
    """Xing OAuth authentication backend"""
    name = 'xing'
    AUTHORIZATION_URL = 'https://www.xing.com/v1/authorize'
    REQUEST_TOKEN_URL = 'https://api.xing.com/v1/request_token'
    ACCESS_TOKEN_URL = 'https://api.xing.com/v1/access_token'
    SCOPE_SEPARATOR = '+'
    EXTRA_DATA = [
        ('id', 'id'),
        ('user_id', 'user_id')
    ]

    def get_user_details(self, response):
        """Return user details from Xing account"""
        first_name, last_name = response['first_name'], response['last_name']
        email = response.get('email', '')
        return {'username': first_name + last_name,
                'fullname': first_name + ' ' + last_name,
                'first_name': first_name,
                'last_name': last_name,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Return user data provided"""
        try:
            profile = self.get_json('https://api.xing.com/v1/users/me.json',
                                    auth=self.oauth_auth(access_token))
            profile = profile['users'][0]
        except (ValueError, KeyError, IndexError):
            pass
        else:
            return {
                'user_id': profile['id'],
                'id': profile['id'],
                'first_name': profile['first_name'],
                'last_name': profile['last_name'],
                'email': profile['active_email']
            }

    def auth_complete(self, *args, **kwargs):
        """Complete auth process. Check Xing error response."""
        oauth_problem = self.data.get('oauth_problem')
        if oauth_problem:
            if oauth_problem == 'user_refused':
                raise AuthCanceled(self, '')
            else:
                raise AuthUnknownError(self, 'Xing error was %s' %
                                                    oauth_problem)
        return super(XingOAuth, self).auth_complete(*args, **kwargs)

    def unauthorized_token(self):
        """Makes first request to oauth. Returns an unauthorized Token."""
        return parse_qs(super(XingOAuth, self).unauthorized_token())
