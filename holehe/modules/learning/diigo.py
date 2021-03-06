from holehe.core import *
from holehe.localuseragent import *


async def diigo(email, client, out):
    name = "diigo"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.diigo.com/sign-up?plan=free',
    }
    try:
        await client.get("https://www.diigo.com/sign-up?plan=free", headers=headers)
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})

    headers["X-Requested-With"] = 'XMLHttpRequest'

    params = {
        'email': email,
    }
    try:
        r = await client.get('https://www.diigo.com/user_mana2/check_email', headers=headers, params=params)
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None
    if r.status_code == 200:
        if r.text == "0":
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
    else:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
