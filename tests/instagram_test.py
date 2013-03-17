import sys
import json

sys.path.insert(0, '..')

from social.backends.instagram import InstagramOAuth2
from tests.oauth2_tests import OAuth2Test


class InstagramTest(OAuth2Test):
    backend = InstagramOAuth2
    user_data_url = 'https://api.instagram.com/v1/users/self'
    expected_username = 'foobar'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer',
        'meta': {
            'code': 200
        },
        'data': {
            'username': 'foobar',
            'bio': '',
            'website': '',
            'profile_picture': 'http://images.instagram.com/profiles/'
                               'anonymousUser.jpg',
            'full_name': '',
            'counts': {
                'media': 0,
                'followed_by': 2,
                'follows': 0
            },
            'id': '101010101'
        },
        'user': {
            'username': 'foobar',
            'bio': '',
            'website': '',
            'profile_picture': 'http://images.instagram.com/profiles/'
                               'anonymousUser.jpg',
            'full_name': '',
            'id': '101010101'
        }
    })
    user_data_body = json.dumps({
        'meta': {
            'code': 200
        },
        'data': {
            'username': 'foobar',
            'bio': '',
            'website': '',
            'profile_picture': 'http://images.instagram.com/profiles/'
                               'anonymousUser.jpg',
            'full_name': '',
            'counts': {
                'media': 0,
                'followed_by': 2,
                'follows': 0
            },
            'id': '101010101'
        }
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
