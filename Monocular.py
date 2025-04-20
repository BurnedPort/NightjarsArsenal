import socket
import argparse
import time
import random
print("👁️ Monocular (Latest Version) Loaded")


parser = argparse.ArgumentParser(description="Monocular: A simple TCP port scanner with banner grabbing.")
parser.add_argument("-t", "--target", required=True, help="Target IP or Domain")
parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default:1)")
parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default:1024)")
args = parser.parse_args()

target = args.target
start_port = args.start
end_port = args.end

print(f"\n👁️ Monocular scanning {target} from port {start_port} to {end_port}...\n")

# 🔁 Loop through each port in the range
for port in range(start_port, end_port + 1):
    time.sleep(random.uniform(0.2, 0.8))  # 👣 Slow down to avoid detection

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                # ⏱️ Start timing
                start_time = time.time()

                # 🛡️ Stealth mode timeout
                sock.settimeout(2)

                # 🕶️ Send browser-like banner request
                request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\nAccept: */*\r\nConnection: close\r\n\r\n"
                sock.sendall(request.encode())

                # 📡 Grab banner
                banner = sock.recv(1024).decode().strip()
                duration = round(time.time() - start_time, 2)

                print(f"🟢 Port {port} is OPEN → {banner} ({duration}s)")

            except:
                print(f"🟢 Port {port} is OPEN → (no banner returned)")

        sock.close()

    except KeyboardInterrupt:
        print("\n🔴 Scan interrupted by user.")
        break
    except socket.error as err:
        print(f"❌ Error on port {port}: {err}")
        continue