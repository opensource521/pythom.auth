import json

from tests.oauth2 import OAuth2Test


class YandexOAuth2Test(OAuth2Test):
    backend_path = 'social.backends.yandex.YandexOAuth2'
    user_data_url = 'https://login.yandex.ru/info'
    expected_username = 'foobar'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer'
    })
    user_data_body = json.dumps({
        'display_name': 'foobar',
        'real_name': 'Foo Bar',
        'sex': None,
        'id': '101010101',
        'default_email': 'foobar@yandex.com',
        'emails': ['foobar@yandex.com']
    })

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()
