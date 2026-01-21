import json
import http.cookiejar

# Load JSON
try:
    with open('cookie.json', 'r') as f:
        data = json.load(f)

    # Use LWPCookieJar instead of MozillaCookieJar
    cj = http.cookiejar.LWPCookieJar('cookie.jar')

    for x in data:
        c = http.cookiejar.Cookie(
            version=0,
            name=x['name'],
            value=x['value'],
            port=None,
            port_specified=False,
            domain=x['domain'],
            domain_specified=True,
            domain_initial_dot=x['domain'].startswith('.'),
            path=x['path'],
            path_specified=True,
            secure=x['secure'],
            expires=x.get('expirationDate'),
            discard=False,
            comment=None,
            comment_url=None,
            rest={'HttpOnly': x.get('httpOnly')},
            rfc2109=False
        )
        cj.set_cookie(c)

    cj.save()
    print('cookie.jar (LWP format) created successfully.')
except Exception as e:
    print(f"Error: {e}")
