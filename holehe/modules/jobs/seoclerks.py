from holehe.core import *
from holehe.localuseragent import ua
from holehe.tools.utils import *


async def seoclerks(email, client, out):
    name = "seoclerks"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.seoclerks.com',
        'Connection': 'keep-alive',
    }

    r = await client.get('https://www.seoclerks.com', headers=headers)
    try:
        if "token" in r.text:
            token = r.text.split('token" value="')[1].split('"')[0]
        if "__cr" in r.text:
            cr = r.text.split('__cr" value="')[1].split('"')[0]
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None

    username = get_random_string(6)
    password = get_random_string(6)

    data = {
        'token': str(token),
        '__cr': str(cr),
        'fsub': '1',
        'droplet': '',
        'user_username': str(username),
        'user_email': str(email),
        'user_password': str(password),
        'confirm_password': str(password)
    }

    r = await client.post('https://www.seoclerks.com/signup/check',
        headers=headers, data=data)
    if 'The email address you entered is already taken.' in r.json()[
            'message']:
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
