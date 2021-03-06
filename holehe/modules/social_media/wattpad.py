from holehe.core import *
from holehe.localuseragent import *


async def wattpad(email, client, out):
    name = "wattpad"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'https://www.wattpad.com/',
        'TE': 'Trailers',
    }
    try:

        await client.get("https://www.wattpad.com", headers=headers)
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None
    headers["X-Requested-With"] = 'XMLHttpRequest'
    params = {
        'email': email,
    }
    r = await client.get('https://www.wattpad.com/api/v3/users/validate', headers=headers, params=params)
    if (r.status_code == 200 or r.status_code == 400):
        if "Cette adresse" not in r.text or r.text == '{"message":"OK","code":200}':
            out.append({"name": name,
                        "rateLimit": False,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        else:
            out.append({"name": name,
                        "rateLimit": False,
                        "exists": True,
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
