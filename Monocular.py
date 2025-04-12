import socket
import argparse

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
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                # 🪪 Attempt to grab a banner
                sock.sendall(b"HEAD / HTTP/1.1\r\nHost: %b\r\n\r\n" % target.encode())
                banner = sock.recv(1024).decode().strip()
                print(f"🟢 Port {port} is OPEN → {banner}")
            except:
                print(f"🟢 Port {port} is OPEN → (no banner returned)")

        sock.close()

    except KeyboardInterrupt:
        print("\n🔴 Scan interrupted by user.")
        break
    except socket.error as err:
        print(f"❌ Error on port {port}: {err}")
        continue