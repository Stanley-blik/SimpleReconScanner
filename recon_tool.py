import socket

def scan_port(target_ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target_ip, port))
        print(f"[+] Port {port} is OPEN")

        try:
            s.send(b'Hello\r\n')
            banner = s.recv(1024)
            print(f"    Banner: {banner.decode().strip()}")
        except:
            print("    No banner received.")
        s.close()
    except:
        pass  # Port is closed or filtered

def main():
    target_ip = input("Enter target IP address: ")
    ports = range(1, 1025)

    print(f"\n[*] Starting scan on {target_ip}\n")

    for port in ports:
        scan_port(target_ip, port)

    print("\n[*] Scan complete.")

if __name__ == "__main__":
    main()
