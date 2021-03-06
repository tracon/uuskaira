from .settings_defaults import *

SECRET_KEY = '9()(lzm)jdr$szjfdx8^^#j_6efj@d&$9pb6l2h&=udxom3(bn'

DEBUG = True

if DEBUG:
    # XXX Monkey patch is_secure_transport to allow development over insecure HTTP

    from warnings import warn
    warn(UserWarning("Monkey_patching oauthlib.oauth2:is_secure_transport to allow OAuth2 over HTTP. Never do this in production!"))

    fake_is_secure_transport = lambda token_url: True

    import oauthlib.oauth2
    import requests_oauthlib.oauth2_session
    import oauthlib.oauth2.rfc6749.parameters
    import oauthlib.oauth2.rfc6749.clients.base

    for module in [
        oauthlib.oauth2,
        requests_oauthlib.oauth2_session,
        oauthlib.oauth2.rfc6749.parameters,
        oauthlib.oauth2.rfc6749.clients.base,
    ]:
        module.is_secure_transport = fake_is_secure_transport

ALLOWED_HOSTS = ['.tracon.fi']

KOMPASSI_HOST = 'https://kompassi.eu'
KOMPASSI_OAUTH2_AUTHORIZATION_URL = '{KOMPASSI_HOST}/oauth2/authorize'.format(**locals())
KOMPASSI_OAUTH2_TOKEN_URL = '{KOMPASSI_HOST}/oauth2/token'.format(**locals())
KOMPASSI_OAUTH2_CLIENT_ID = 'kompassi_insecure_client_id'
KOMPASSI_OAUTH2_CLIENT_SECRET = 'kompassi_insecure_client_secret'
KOMPASSI_OAUTH2_SCOPE = ['read']

KOMPASSI_ADMIN_GROUP = 'kaira-admins'
KOMPASSI_STAFF_GROUP = 'kaira-staff'

LOGOUT_REDIRECT_URL = '{KOMPASSI_HOST}/logout'.format(**locals())
