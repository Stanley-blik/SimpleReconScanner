import socket
import sys

def scan_port(target_ip, port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
        try:
            s.send(b'Hello\r\n')
            banner = s.recv(1024)
            print(f"    Banner: {banner.decode().strip()}")
        except:
            print("    No banner received.")
    s.close()

def main():
    target_ip = input("Enter target IP address: ")

    # Common ports only (faster)
    ports = [
        21,   # FTP
        22,   # SSH
        23,   # Telnet
        25,   # SMTP
        53,   # DNS
        80,   # HTTP
        110,  # POP3
        143,  # IMAP
        443,  # HTTPS
        3306, # MySQL
        8080  # HTTP-alt
    ]

    print(f"\n[*] Starting scan on {target_ip}\n")

    try:
        for port in ports:
            scan_port(target_ip, port)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit()

    print("\n[*] Scan complete.")

if __name__ == "__main__":
    main()