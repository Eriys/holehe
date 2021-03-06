from holehe.core import *
from holehe.localuseragent import *


async def strava(email, client, out):
    name = "strava"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://www.strava.com/register/free?cta=sign-up&element=button&source=website_show',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    r = await client.get("https://www.strava.com/register/free?cta=sign-up&element=button&source=website_show", headers=headers)
    try:
        headers['X-CSRF-Token'] = r.text.split(
            '<meta name="csrf-token" content="')[1].split('"')[0]
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    headers['X-Requested-With'] = 'XMLHttpRequest'

    params = {
        'email': email
    }

    r = await client.get('https://www.strava.com/athletes/email_unique', headers=headers, params=params)

    if r.text == "false":
        out.append({"name": name,
                    "rateLimit": False,
                    "exists": True,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    elif r.text == "true":
        out.append({"name": name,
                    "rateLimit": False,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    else:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
