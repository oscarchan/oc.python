from webob.compat import text_type
from webob.cookies import Cookie

def refresh_auth_cookie(request, response=None):
    auth_cookie = request.cookies.get(AUTH_COOKIE_NAME)
    cookie_domain = _cookie_domain(request)
    if response is None:
        response =  request.response

def get_cookie(response, key):
    existing = response.headers.getall('Set-Cookie')
    if not existing:
        return False

    cookies = Cookie()
    for header in existing:
        cookies.load(header)

    if isinstance(key, text_type):
        key = key.encode('utf8')

    if key in cookies:
        return cookies[key]

    return None

def has_cookie(response, key):
    cookie = get_cookie(response, key)

    return cookie is not None

