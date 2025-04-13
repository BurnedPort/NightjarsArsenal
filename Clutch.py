import argparse
import requests
import time

print("🔧 Clutch initialized...")

parser = argparse.ArgumentParser(description= "Clutch: A simple web directory bruteforcer.")
parser.add_argument("-t", "--target", required=True, help= "Target Url")
parser.add_argument("-w", "--wordlist", default="wordlists/common_dirs.txt", help= "Path to wordlist.")
parser.add_argument("-x", "--extension", default="", help= "optional extension.")
args = parser.parse_args()

target = args.target.rstrip("/")
wordlist_path = args.wordlist
extension = args.extension

try:
    with open(wordlist_path, "r") as file:
        dirs = file.read().splitlines()
except FileNotFoundError:
    print(f"❌ Wordlist not found: {wordlist_path}")
    exit()

print(f"🚀 Launching dir scan on {target} with {len(dirs)} paths...\n")

for dir in dirs:
    path = f"{target}/{dir}{extension}"
    try:
        response = requests.get(path, timeout=3)
        code = response.status_code

        if code not in [404]:
            print(f"🟢 {code} → {path}")

        time.sleep(0.2)  # Stealth spacing

    except KeyboardInterrupt:
        print("\n🛑 Scan interrupted.")
        break
    except requests.RequestException:
        print(f"⚠️ Error reaching {path}")
        continue
