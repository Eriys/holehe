from holehe.core import *
from holehe.localuseragent import *


async def xing(email, client, out):
    name = "xing"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en,en-US;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    r = await client.get("https://www.xing.com/start/signup?registration=1", headers=headers)
    headers['x-csrf-token'] = r.cookies["xing_csrf_token"]

    data = {
        'signup_minireg': {
            'email': email,
            'password': '',
            'tandc_check': '1',
            'signup_channel': 'minireg_fullpage',
            'first_name': '',
            'last_name': ''
        }
    }

    r = await client.post('https://www.xing.com/welcome/api/signup/validate', headers=headers, json=data)
    try:
        errors = r.json()["errors"]
        if "signup_minireg[email]" in errors and errors["signup_minireg[email]"].startswith(
                "We already know this e-mail address."):
            out.append({"name": name,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        else:
            out.append({"name": name,
                        "rateLimit": False,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
