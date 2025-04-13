import argparse
import requests
import socket

print("🕊️ Perch taking flight...")

parser = argparse.ArgumentParser(description= "Perch: Subdomain enumeration tool.")
parser.add_argument("-d", "--domain", required=True, help="Target domain")
parser.add_argument("-w", "--wordlist", default="wordlists/subdomains.txt", help="Path to wordlist")
args = parser.parse_args()

domain = args.domain
wordlist_path = args.wordlist

try:
    with open(wordlist_path, "r") as file:
        subdomains = file.read().splitlines()
    print(f"🔍 Loaded {len(subdomains)} subdomains from {wordlist_path}")
except FileNotFoundError:
    print(f"❌ Wordlist not found: {wordlist_path}")
    exit()

for sub in subdomains:
    subdomain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"🟢 Found: {subdomain} → {ip}")
    except socket.gaierror:
        pass