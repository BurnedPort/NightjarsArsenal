# libTalon.py

import requests

def try_login(url, username, password, fields, fail_string, headers):
    data = {
        fields[0]: username.strip(),
        fields[1]: password.strip()
    }

    try:
        r = requests.post(url, data=data, headers=headers, timeout=5)
        return fail_string not in r.text  # True = success
    except Exception as e:
        return None  # Error state
